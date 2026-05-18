---
type: source
source_url: https://github.com/coleam00/archon
tags:
  - workflow-engine
  - harness-builder
  - git-worktrees
  - yaml-workflows
  - dag-execution
  - deterministic-ai
  - multi-platform-adapter
  - ai-coding-agent
related:
  - obra-superpowers
  - njbrake-agent-of-empires
  - gsd-build-get-shit-done
  - anthropic.com-managed-agents
  - gastownhall-beads
product: archon
detail_level: standard
created: 2026-05-14
updated: 2026-05-18
---

Archon (21,422 ★, MIT, TypeScript) is the first open-source harness builder for AI coding — a YAML workflow engine that makes AI-assisted development deterministic and repeatable. Where tools like Claude Code or Codex provide the intelligence, Archon provides the structure: a DAG-based execution model in which development phases (plan, implement, validate, review, approve, PR) are defined as YAML nodes, run in isolated git worktrees, and driven by a central orchestrator that routes messages from any of five platform adapters (CLI, Web UI, Slack, Telegram, GitHub/Discord). The result is "fire and forget" AI coding: you trigger a workflow, Archon handles sequencing, isolation, human-in-the-loop approval gates, and PR creation — you come back to a finished pull request.

_All claims below are sourced from ../../raw/github/coleam00-archon.md unless otherwise noted._

## What it does

Archon translates the question "how should an AI agent work on this repo?" into a committed, version-controlled YAML file. Each node in a workflow is either a deterministic step (bash command, git operation, test run) or an AI step (a natural-language prompt sent to Claude Code, Codex, or Pi). Loop nodes iterate until a condition is satisfied (`ALL_TASKS_COMPLETE`, `APPROVED`). Human-approval nodes pause and wait for interactive input. The workflow engine executes the DAG, manages worktree creation and cleanup, persists state in SQLite or PostgreSQL (7 tables: Codebases, Conversations, Sessions, Workflow Runs, Isolation Environments, Messages, Workflow Events), and streams progress to all registered platform adapters simultaneously.

## Key features

- **17 built-in workflows** covering the full development lifecycle: `archon-fix-github-issue`, `archon-idea-to-pr`, `archon-plan-to-pr`, `archon-smart-pr-review`, `archon-comprehensive-pr-review` (5 parallel reviewers), `archon-architect`, `archon-refactor-safely`, `archon-resolve-conflicts`, and more.
- **YAML-first workflow authoring** — workflows live in `.archon/workflows/`, commands in `.archon/commands/`; files committed to the repo are shared across the whole team and override bundled defaults.
- **Git worktree isolation** — every workflow run spawns its own git worktree on a uniquely named branch; five workflows can run in parallel on the same repo with zero conflicts.
- **Loop nodes** — AI iteration loops (`until: ALL_TASKS_COMPLETE`) and human-in-the-loop gates (`until: APPROVED`, `interactive: true`) are first-class node types.
- **Multi-platform adapters** — Web UI, CLI, Telegram (5 min setup), Slack (15 min), GitHub Webhooks (15 min), Discord (5 min). All conversations flow into a single monitoring sidebar.
- **Visual Workflow Builder** — drag-and-drop DAG editor in the Web UI for creating and editing workflows without touching YAML.
- **Multi-provider AI support** — Claude Code SDK, Codex SDK, and Pi as pluggable `IAgentProvider` implementations.
- **Telemetry** — anonymous `workflow_invoked` event (workflow name, platform, version, random install UUID); opt out with `ARCHON_TELEMETRY_DISABLED=1` or `DO_NOT_TRACK=1`.

## Architecture

Archon is a Bun + TypeScript monorepo with 11 packages under `packages/`:

- **`core/`** — orchestrator, message routing, context management. Central hub that all adapters and the workflow executor connect to.
- **`workflows/`** — DAG workflow engine: YAML loader (`dagNodeSchema.safeParse()`), `validateDagStructure()` for cycle detection and `$nodeId.output` reference validation, loop node executor, retry logic.
- **`adapters/`** — platform adapter implementations, each implementing the `IPlatformAdapter` interface. Handles streaming and batch AI responses in real time.
- **`providers/`** — AI provider clients implementing `IAgentProvider` (Claude Code SDK, Codex SDK, Pi).
- **`server/`** — Hono HTTP/API server with Zod OpenAPI (`registerOpenApiRoute`); route schemas in `routes/schemas/`, engine schemas in `packages/workflows/src/schemas/`.
- **`web/`** — React Web UI (Chat, Dashboard, Workflow Builder, Workflow Execution pages).
- **`git/`** — git operations library using `execFileAsync`; worktree creation, branch management, conflict detection.
- **`isolation/`** — worktree isolation environment lifecycle.
- **`cli/`** — compiled CLI binary distributed via curl installer, Homebrew, and Windows PowerShell.
- **`docs-web/`** — documentation website source for archon.diy.
- **`auth-service/`** — authentication service.

Database: SQLite (default) or PostgreSQL, 7 tables. Branch strategy: `dev` is the working branch; `main` is release-only. Version managed via root `package.json`; releases use the `/release` skill.

## Installation

**Full setup (5 minutes — recommended):**
```bash
git clone https://github.com/coleam00/Archon
cd Archon
bun install
claude  # then say "Set up Archon"
```

**Quick install (30 seconds):**
```bash
curl -fsSL https://archon.diy/install | bash       # macOS/Linux
brew install coleam00/archon/archon                # Homebrew
irm https://archon.diy/install.ps1 | iex           # Windows
```

Prerequisites: Bun, Claude Code, GitHub CLI.

## Example usage

```bash
cd /path/to/your/project
claude
```
```
Use archon to fix issue #42
```
Archon selects the appropriate workflow (`archon-fix-github-issue`), creates an isolated worktree on a new branch, runs the DAG (classify → investigate → plan → implement → validate → PR → review → self-fix), and returns a pull request URL. Custom workflows drop into `.archon/workflows/` alongside the defaults — same-named files override bundled ones.

## When to use

Archon is the right choice when:
- AI coding runs are inconsistent — different models, different moods, different results — and you want the same steps every time.
- You need parallel AI coding tasks (multiple issues, multiple features) without branch conflicts.
- You want to run AI coding from Slack, Telegram, or GitHub without sitting at a terminal.
- Your team has an established development process (plan → implement → test → review → PR) that you want AI to follow rather than improvise.
- You want human approval gates wired into the AI loop, not bolted on after.

Less suitable when you need a general-purpose agent framework for non-coding domains — Archon is explicitly scoped to software development workflows.

## Maintenance status

Stars: 21,422 | Forks: 3,265 | License: MIT | Latest: v0.3.11 (2026-05-13) | Language: TypeScript | Branch: `dev`. Actively developed; last push 2026-05-14. Full documentation at [archon.diy](https://archon.diy) including a 10-chapter "Book of Archon" narrative tutorial.

## Ecosystem

Archon integrates with: Claude Code (primary AI engine), Codex SDK, Pi, GitHub (webhooks, PR creation, issue tracking), Slack, Telegram, Discord. Workflows are composable with any bash-compatible tool. Docker image ships Claude Code pre-installed. Deployment docs cover VPS and production setups. Previous v1 (Python-based task management + RAG) preserved on `archive/v1-task-management-rag` branch.
