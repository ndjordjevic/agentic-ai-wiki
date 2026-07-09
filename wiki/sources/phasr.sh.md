---
type: source
category: "Terminal, session & parallel-agent runners"
source_url: https://phasr.sh/
companion_urls:
  - https://github.com/irishabh96/phasr
raw_files:
  - ../../raw/web/phasr.sh.md
  - ../../raw/github/irishabh96-phasr.md
tags:
  - parallel-agents
  - git-worktrees
  - agent-orchestration
  - human-in-the-loop
  - desktop-app
  - provider-agnostic
  - code-review
  - tauri
related:
  - vibekanban.com
  - coleam00-archon
  - njbrake-agent-of-empires
  - garrytan-gbrain
  - paperclip.ing
product: phasr
detail_level: standard
created: 2026-07-08
updated: 2026-07-08
---

Phasr is a free, open-source macOS desktop workspace for running multiple CLI coding agents in parallel, each in its own Git worktree, with real-time diff review and explicit human approval before anything merges to main. The product site positions it as agent-agnostic orchestration — Claude Code, Codex, Gemini, Cursor, Aider, and any terminal-native agent — while the companion repo (`irishabh96/phasr`) implements the stack as a Tauri 2 + React 19 app with Rust-backed PTYs, SQLite persistence, and optional Clerk/Supabase cloud sync. (../../raw/github/irishabh96-phasr.md)

_All claims below are sourced from ../../raw/web/phasr.sh.md unless otherwise noted._

## What it does

Phasr is a review-first multi-agent development environment. Operators open a repository workspace, define independent tasks, launch multiple agents concurrently, and review each agent's isolated changes before approving merges. The core loop is: decompose work into narrow tasks → run agents in parallel on separate worktrees → triage diffs by file and risk → approve, request revision, or discard → merge only approved branches.

The product is in public beta (pre-1.0), macOS Apple Silicon only, distributed as an unsigned DMG with a one-time Gatekeeper quarantine bypass. It is MIT-licensed and marketed as free and open source.

## Key features

**Parallel execution** — launch dozens of agents across independent tasks with live status, progress tracking, and automatic resource management.

**Universal agent compatibility** — any CLI agent that runs in a terminal works in Phasr; no proprietary protocols or vendor lock-in. Supported agents include Claude Code, Codex CLI, Gemini CLI, Cursor Agent, Aider, and OpenCode.

**Git worktree isolation** — each agent task gets its own worktree and branch (e.g., `phasr/task-1742-add-rate-limiting`), preventing file collisions and shared working-directory conflicts. Worktrees are created from HEAD, used exclusively by the agent, then presented for review or cleanup.

**IDE integration** — one-click deep links to VS Code, Cursor, JetBrains, Zed, Sublime, Terminal, Xcode, and Finder for reviewing or editing agent output in native editors.

**Human-in-the-loop review** — file-level diffs, change summaries, side-by-side views, risk scoring for critical paths (auth, payments, migrations), inline chat comments agents can act on, and explicit Approve / Reject / Request modification flows. Nothing lands on main without approval.

**Provider-agnostic model routing** — configure different models per task within the same session; orchestration adapts prompts and context windows. Teams can route cheap models to boilerplate tasks and expensive models to complex refactors.

On the implementation side, the companion repo adds per-workspace PTY terminals with xterm.js streaming, SQLite via sqlx, TanStack Router/Query, Zustand state, and an `orchestrator` module in the Rust backend alongside dedicated `git/` worktree helpers. (../../raw/github/irishabh96-phasr.md)

## Architecture

Phasr's isolation model uses Git worktrees rather than containers or branch-only separation. Worktrees share the object store but have independent indexes and working directories — fast to create, low disk overhead, no container runtime required. The blog contrasts this with Docker-per-agent (heavy startup/memory) and branch-only approaches (no separate working directories).

The desktop app architecture is Tauri 2 (Rust shell) + React 19 frontend. Backend modules under `src-tauri/src/` include `commands/` (Tauri handlers), `domain/` (types), `store/` (SQLite repos), `pty/` (terminal runtime), `git/` (worktree + diff), `orchestrator/`, and `sync/` (cloud metadata). Frontend routes live under `src/routes/` with auth-gated `_app/` layout. (../../raw/github/irishabh96-phasr.md)

Review pipeline stages: (1) agent streams work in isolated worktree, (2) semantic diff viewer surfaces on completion, (3) human approves → PR, requests revision → agent re-enters with feedback, or discards → worktree removed.

## Installation

**End users (macOS Apple Silicon):**
1. Download latest `Phasr_<version>_aarch64.dmg` from GitHub Releases.
2. Drag Phasr to Applications.
3. Bypass Gatekeeper quarantine once: `xattr -dr com.apple.quarantine /Applications/Phasr.app`

**Prerequisites:** one or more agent CLIs on PATH (`claude`, `codex`, `copilot`, `gemini`, `opencode`) plus `git`. Configure agents in Settings → Agents.

**Developers:**
```sh
git clone https://github.com/irishabh96/phasr
cd phasr
pnpm install
pnpm tauri dev
```

Production README notes Clerk + Supabase env vars for sign-in and cloud sync; CONTRIBUTING.md documents a local-only mode without cloud credentials (SQLite workspaces, no sign-in). (../../raw/github/irishabh96-phasr.md)

## Example usage

Operator quickstart from docs:
1. Install Phasr and open a repository workspace.
2. Connect coding agents (Claude Code, Codex CLI, Gemini CLI, Aider).
3. Create independent tasks and launch in parallel.
4. Review each worktree diff, approve clean changes, and merge.

Task planning checklist: narrow file scope per task, branch naming conventions, per-task test commands, explicit human approval for high-risk diffs.

Dev workflow commands: `pnpm tauri dev` (full app), `pnpm dev` (Vite UI only), `pnpm typecheck`, `cargo test --manifest-path src-tauri/Cargo.toml`. (../../raw/github/irishabh96-phasr.md)

## When to use

- You want to run multiple coding agents on the same repo simultaneously without merge conflicts or overwritten uncommitted work.
- You need a review gate before AI-generated code touches main — speed without sacrificing oversight.
- You use multiple CLI agents or models and want per-task provider selection without switching tools.
- You prefer lightweight Git worktree isolation over container-per-agent overhead.
- You work on macOS Apple Silicon and accept pre-1.0, unsigned-build limitations.

Less suited when you need Linux/Windows support today (not planned pre-1.0), fully offline/no-cloud operation in production builds (README requires Clerk/Supabase at runtime for releases), or team collaboration features still on the Q2 2026 roadmap.

## Maintenance status

19 GitHub stars, 0 forks, MIT license, TypeScript primary language, default branch `master`, latest release v0.2.4 (2026-06-22). Pre-1.0 public beta; unsigned macOS builds; signed releases planned. Roadmap (March 2026): Q1 core workspace shipped; Q2 team collaboration in progress; Q3 cloud workspaces and mobile app planned (PRO); Q4 GitHub/Linear integrations and enterprise readiness (SSO, audit logs, self-hosted) planned. (../../raw/github/irishabh96-phasr.md)

## Ecosystem

Integrations marketed on the landing page: Git, GitHub, Linear, Supabase, Vercel, and major IDEs/editors. Compatible agent ecosystem spans the major CLI coding tools. Blog and docs cover parallel execution, worktree isolation, human-in-the-loop review, and multi-model orchestration patterns. Future integrations roadmap includes two-way issue/PR sync and deployment automation hooks.
