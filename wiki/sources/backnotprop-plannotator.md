---
type: source
source_url: https://github.com/backnotprop/plannotator
tags:
  - plan-review
  - claude-code-plugin
  - code-review
  - agent-hooks
  - visual-annotation
  - exit-plan-mode
  - multi-agent-ide
  - zero-knowledge-sharing
related:
  - everyinc-compound-engineering-plugin
  - openai-codex-plugin-cc
  - othmanadi-planning-with-files
  - anombyte93-prd-taskmaster
  - obra-superpowers
  - goOZSXmrYQ4-my-complete-agentic-coding-workflow-to-b
product: plannotator
detail_level: standard
created: 2026-05-25
updated: 2026-05-25
---

Plannotator is an open-source visual plan-and-code-review UI for AI coding agents, most prominently Claude Code. It intercepts the agent's `ExitPlanMode` hook and opens an interactive browser UI where humans can annotate, approve, request changes, or ask AI follow-up questions before the agent proceeds — turning an opaque plan-then-execute loop into a collaborative, human-in-the-loop workflow. With 5,580 stars and v0.19.22 as of May 2026, it is one of the most widely adopted Claude Code plugins and supports seven runtimes: Claude Code, Copilot CLI, Gemini CLI, OpenCode, Pi, Codex, and Droid.

_All claims below are sourced from ../../raw/github/backnotprop-plannotator.md unless otherwise noted._

## What it does

Plannotator sits between an AI agent's planning step and its execution step. When the agent finishes drafting a plan, Plannotator opens a browser UI showing the plan in a rich viewer with annotation tools. The human can inline-delete, insert, replace, or comment on any section; request changes with structured feedback that is sent back into the agent's context; or approve the plan and let the agent continue. The same review loop applies to code diffs (git diffs or GitHub PRs) and arbitrary markdown files, URLs, or folders.

## Key features

- **Visual plan review** — built-in `ExitPlanMode` / `Stop` hook integration; plans open in the browser automatically; no manual invocation required for plan mode.
- **Plan diff** — automatic diff view showing what changed when the agent revises a plan in response to feedback.
- **Code review** — `/plannotator-review` (slash command) for current git changes or a remote GitHub PR URL; inline line-level annotation; Ask AI side chat while reviewing.
- **Annotate any file** — `/plannotator-annotate <file|folder|url>` annotates markdown, HTML, folder trees, or remote URLs; Ask AI about the active document.
- **Annotate last message** — `/plannotator-last` surfaces the agent's most recent response for annotation and structured feedback.
- **End-to-end encrypted sharing** — small plans encode entirely in the URL hash (no server); large plans use AES-256-GCM in the browser before upload to a zero-knowledge paste service; decryption key stays in the URL; pastes auto-delete after 7 days; self-hostable.
- **Agent skills** — ships a suite of skills in agentskills.io format: `plannotator-review`, `plannotator-annotate`, `plannotator-last`, `plannotator-compound` (map-reduce analysis over denied plans), `plannotator-setup-goal`, and `plannotator-visual-explainer`.

## Architecture

Plannotator is a Bun monorepo with app-specific integration layers and a shared packages layer.

**App integrations** (`apps/`): each supported runtime gets its own integration — `apps/hook/` is the Claude Code plugin (`ExitPlanMode` hook + `PermissionRequest` hook + slash commands); `apps/copilot/` is the Copilot CLI integration; `apps/gemini/` is the Gemini CLI integration; `apps/opencode-plugin/` is the OpenCode plugin; `apps/pi-extension/` is the Pi npm extension; `apps/codex/` uses Codex's experimental `Stop` hook; `apps/droid-plugin/` is commands-only (no plan interception). Each entry is a thin wrapper that calls the shared `@plannotator/server` package and injects the platform-specific browser-open and hook plumbing.

**Shared packages** (`packages/`): `@plannotator/server` provides `startPlannotatorServer()`, `startReviewServer()`, and `startAnnotateServer()`; `@plannotator/ui` provides the shared React components (Viewer, Toolbar, Settings, plan diff views, sidebar, keyboard shortcuts); `@plannotator/ai` is the provider-agnostic AI backbone; `@plannotator/shared` contains cross-runtime utilities (plan storage, version history, draft persistence); `@plannotator/editor` is the plan review React app; `@plannotator/review-editor` is the code review UI.

**Paste service** (`apps/paste-service/`): platform-agnostic core with pluggable storage backends (filesystem, KV, S3) and deployment targets (Bun native, Cloudflare Workers).

**VS Code extension** (`apps/vscode-extension/`): optional VS Code integration that opens plans in editor tabs with theme-matched rendering.

## Installation

**Global binary (all platforms):**
```bash
curl -fsSL https://plannotator.ai/install.sh | bash
```

**Claude Code:**
```
/plugin marketplace add backnotprop/plannotator
```

**Copilot CLI:**
```
/plugin marketplace add backnotprop/plannotator
/plugin install plannotator-copilot@plannotator
```
Plan review activates automatically when Copilot CLI enters plan mode (`Shift+Tab`).

**Gemini CLI** (requires 0.36.0+): the install script auto-detects `~/.gemini` and configures the plan hook and policy.

**OpenCode:** add `"@plannotator/opencode@latest"` to `plugin` in `opencode.json`; run the install script for `/plannotator-review`.

**Pi:** `pi install npm:@plannotator/pi-extension`

**Codex:** install script auto-enables `Stop` hooks on macOS/Linux/WSL; feedback flows back into the agent loop automatically.

**Droid:** `droid plugin marketplace add https://github.com/backnotprop/plannotator` then `droid plugin install plannotator@plannotator` (commands-only; no plan interception).

## Example usage

```bash
# In Claude Code — plan mode activates automatically via ExitPlanMode hook
# Agent proposes a plan → browser opens → annotate → Approve or Request changes

# Code review for staged/unstaged changes:
/plannotator-review

# Review a GitHub pull request:
/plannotator-review https://github.com/org/repo/pull/123

# Annotate a markdown file:
/plannotator-annotate ARCHITECTURE.md

# Annotate the agent's last response:
/plannotator-last
```

For development, link the binary from source:
```bash
bun install && bun link
# Then rebuild HTML when UI changes:
bun run --cwd apps/review build && bun run build:hook
```

## When to use

Plannotator fits any workflow where you want a human checkpoint between an agent's plan and its execution — especially destructive or high-stakes operations. It is particularly well-suited for teams sharing plans across colleagues (the encrypted sharing feature), for reviewing AI-generated code diffs before they land (code review), and for annotating agent-produced documents iteratively. It is less suited for fully automated pipelines where no human is present, though the `plannotator-compound` skill can perform agentic map-reduce analysis over denied plans without human interaction.

## Maintenance status

5,580 stars; 382 forks; latest release v0.19.22 (May 2026); actively developed (pushed 2026-05-25); Apache 2.0 / MIT dual license; self-hosted paste service option; SLSA provenance verification from v0.17.2; CONTRIBUTING.md present.
