# backnotprop/plannotator

## Metadata
- Stars: 5580
- Primary language: TypeScript
- Default branch: main
- Latest release: v0.19.22 (2026-05-24)
- License: Apache 2.0 / MIT (dual license)
- Homepage: https://plannotator.ai
- Fetched: 2026-05-25
- Final URL: https://github.com/backnotprop/plannotator

## Description
Annotate and review coding agent plans and code diffs visually, share with your team, send feedback to agents with one click.

## README
<p align="center">
  <img src="apps/marketing/public/og-image.webp" alt="Plannotator" width="80%" />
</p>

# Plannotator

Interactive Plan & Code Review for AI Coding Agents. Mark up and refine your plans or code diffs using a visual UI, share for team collaboration, and seamlessly integrate with **Claude Code**, **Copilot CLI**, **Gemini CLI**, **OpenCode**, **Pi**, **Codex**, and **Droid**.

**Plan Mode Demos:**
<table>
<tr>
<td align="center" width="50%">
<h3>Claude Code</h3>
<a href="https://www.youtube.com/watch?v=a_AT7cEN_9I">
Watch Demo
</a>
</td>
<td align="center" width="50%">
<h3>OpenCode</h3>
<a href="https://youtu.be/_N7uo0EFI-U">
Watch Demo
</a>
</td>
</tr>
</table>

**Annotate:** Plans, specs, folders, files, urls. send feedback directly to agents.

**New:** [Code Review](https://x.com/backnotprop/status/2031145299738263567?s=20)
  - send your feedback to agents
  - built-in: ask ai, agent code reviews

### Features

| Feature | Trigger | Description |
|---|---|---|
| **Visual Plan Review** | Built-in hook | Approve or deny agent plans with inline annotations and Ask AI side chat |
| **Plan Diff** | Automatic | See what changed when the agent revises a plan |
| **Code Review** | `/plannotator-review` | View git diffs or remote PRs. Package annotations and ask AI about the code as you review. |
| **Annotate Any File** | `/plannotator-annotate <file\|folder\|url>` | Annotate markdown, HTML, URLs, or folders, ask AI about the active document, and send feedback to your agent |
| **Annotate Last Message** | `/plannotator-last` | Annotate the agent's last response and send structured feedback |

#### Sharing Plans

Plannotator lets you privately share plans, annotations, and feedback with colleagues. For example, a colleague can annotate a shared plan, and you can import their feedback to send directly back to the coding agent.

**Small plans** are encoded entirely in the URL hash. No server involved, nothing stored anywhere.

**Large plans** use a short link service with **end-to-end encryption**. Your plan is encrypted with AES-256-GCM in your browser before upload. The server stores only ciphertext it cannot read. The decryption key lives only in the URL you share. Pastes auto-delete after 7 days.

- Zero-knowledge storage, similar to [PrivateBin](https://privatebin.info/)
- Fully open source and **self-hostable** ([see docs](https://plannotator.ai/docs/guides/sharing-and-collaboration/))

## Install

### Install for Claude Code

```bash
curl -fsSL https://plannotator.ai/install.sh | bash
```

```
/plugin marketplace add backnotprop/plannotator
```

Restart Claude Code after plugin install.

### Install for Copilot CLI

```bash
curl -fsSL https://plannotator.ai/install.sh | bash
```

```
/plugin marketplace add backnotprop/plannotator
/plugin install plannotator-copilot@plannotator
```

Restart Copilot CLI after plugin install. Plan review activates automatically when you use plan mode (`Shift+Tab` to enter plan mode).

### Install for Gemini CLI

```bash
curl -fsSL https://plannotator.ai/install.sh | bash
```

```
/plan                              # Enter plan mode — plans open in your browser
/plannotator-review                # Code review for current changes
/plannotator-review <pr-url>       # Review a GitHub pull request
/plannotator-annotate <file.md>    # Annotate a markdown file
```

Requires Gemini CLI 0.36.0 or later.

### Install for OpenCode

```json
{ "plugin": ["@plannotator/opencode@latest"] }
```

```bash
curl -fsSL https://plannotator.ai/install.sh | bash
```

### Install for Pi

```bash
pi install npm:@plannotator/pi-extension
```

### Install for Codex

```bash
curl -fsSL https://plannotator.ai/install.sh | bash
```

```
$plannotator-review          # Code review skill for current changes
$plannotator-annotate        # Annotate a markdown file, URL, or folder
$plannotator-last            # Annotate the last agent message
```

### Install for Droid

```bash
curl -fsSL https://plannotator.ai/install.sh | bash
droid plugin marketplace add https://github.com/backnotprop/plannotator
droid plugin install plannotator@plannotator
```

## How It Works

When your AI agent finishes planning, Plannotator:

1. Opens the Plannotator UI in your browser
2. Lets you annotate the plan visually (delete, insert, replace, comment)
3. Lets you ask AI about the plan or a highlighted selection when a provider is available
4. **Approve** → Agent proceeds with implementation
5. **Request changes** → Your annotations are sent back as structured feedback

(Similar flow for code review, except you can also comment on specific lines of code diffs)

## Development

```bash
bun install
bun link
```

After linking, commands like `plannotator review` use `apps/hook/server/index.ts` from your local repo. Rebuild the bundled HTML when changing UI code:

```bash
bun run --cwd apps/review build && bun run build:hook
```

## Docs
### AGENTS.md / CLAUDE.md Summary

A plan review UI for Claude Code that intercepts `ExitPlanMode` via hooks, letting users approve or request changes with annotated feedback. Also provides code review for git diffs and annotation of arbitrary markdown files.

### Project Architecture

```
plannotator/
├── apps/
│   ├── hook/                     # Claude Code plugin
│   │   ├── .claude-plugin/plugin.json
│   │   ├── commands/             # Slash commands (plannotator-review.md, plannotator-annotate.md)
│   │   ├── hooks/hooks.json      # PermissionRequest hook config
│   │   └── server/index.ts       # Entry point (plan + review + annotate + archive subcommands)
│   ├── opencode-plugin/          # OpenCode plugin
│   ├── gemini/                   # Gemini CLI integration
│   ├── copilot/                  # Copilot CLI integration
│   ├── codex/                    # OpenAI Codex integration
│   ├── pi-extension/             # Pi extension
│   ├── droid-plugin/             # Droid plugin
│   ├── vscode-extension/         # VS Code extension — opens plans in editor tabs
│   ├── marketing/                # Astro 5 static marketing/docs site (plannotator.ai)
│   ├── paste-service/            # Zero-knowledge paste service for large plan sharing
│   ├── review/                   # Standalone review server (for development)
│   └── skills/                   # Agent skills (agentskills.io format)
│       ├── plannotator-review/
│       ├── plannotator-annotate/
│       ├── plannotator-last/
│       ├── plannotator-compound/      # Map-reduce analysis agent
│       ├── plannotator-setup-goal/    # Goal scaffolder for /goal workflows
│       └── plannotator-visual-explainer/
├── packages/
│   ├── server/                   # Shared server implementation
│   ├── ui/                       # Shared React components + theme
│   ├── ai/                       # Provider-agnostic AI backbone
│   ├── shared/                   # Shared types + cross-runtime utilities
│   ├── editor/                   # Plan review app (React)
│   └── review-editor/            # Code review UI
├── docs/
│   ├── adversarial_rubric.md     # Quality rubric for plan review
│   └── issue-694-code-navigation-recap.md
├── AGENTS.md                     # Agent instructions
├── CLAUDE.md                     # Claude Code instructions
├── CONTRIBUTING.md
└── openpackage.yml               # Package manifest for agent skills marketplace
```

## Top-level structure
```
.agents/           — Agent configuration files
.claude-plugin/    — Claude Code plugin manifest
.factory-plugin/   — Factory.ai plugin manifest
.github/           — GitHub Actions CI/CD
apps/              — Platform-specific integrations (hook, gemini, codex, copilot, droid, pi, opencode, vscode-extension, marketing, paste-service, review, skills)
bin/               — CLI router binaries
docs/              — Internal documentation (adversarial rubric, issue recaps)
packages/          — Shared packages (server, ui, ai, shared, editor, review-editor)
scripts/           — Build/release scripts
tests/             — Test suite
AGENTS.md          — Agent instruction file
CLAUDE.md          — Claude Code instruction file
CONTRIBUTING.md    — Contribution guide
openpackage.yml    — Marketplace manifest
package.json       — Bun monorepo root
```
