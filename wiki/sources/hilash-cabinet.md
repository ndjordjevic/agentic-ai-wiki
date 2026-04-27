---
type: source
source_url: https://github.com/hilash/cabinet
tags: [knowledge-base, agent-orchestration, claude-code, codex, provider-adapter, scheduled-jobs, self-hosted, typescript, nextjs, daemon-architecture, agent-personas]
related:
  - "[[runcabinet.com]]"
  - "[[coleam00-claude-memory-compiler]]"
  - "[[gsd-build-get-shit-done]]"
  - "[[paperclip.ing]]"
  - "[[paperclipai-paperclip]]"
product: cabinet
detail_level: standard
created: 2026-04-25
updated: 2026-04-27
---

`hilash/cabinet` is the open-source codebase behind Cabinet (runcabinet.com): a TypeScript/Next.js self-hosted knowledge base OS that combines file-based markdown storage, AI agent orchestration (Claude Code and Codex via a provider adapter layer), cron-scheduled jobs, an embedded HTML app system, and a git-backed version history into a single self-hosted application. With 1,702 stars and an active release cadence (v0.3.4, April 2026), it is the most complete open-source implementation in this wiki of a production agentic knowledge-base deployment — showing how persistent agent memory, multi-role agent teams, and scheduled autonomous operation are architected at code level.

_All claims below are sourced from ../../raw/github/hilash-cabinet.md unless otherwise noted._

## What It Does

Cabinet solves the session-amnesia problem of AI tools: every new Claude or Codex session forgets your project context. Cabinet provides a persistent, file-based knowledge base that agents read and write across sessions. The user installs with `npx create-cabinet@latest`, answers 5 onboarding questions, and receives a custom AI team (CEO, CTO, Marketer, etc.) with recurring jobs already defined. Agents execute tasks against the knowledge base and their output accumulates there — context compounds over time rather than being discarded.

## Installation

```bash
npx create-cabinet@latest
cd cabinet
npm run dev:all
```

- Requires Node.js 20+ and at least one CLI provider: Claude Code CLI or Codex CLI
- macOS or Linux (Windows via WSL)
- For direct CLI management: `npx cabinetai run` / `cabinetai create [name]`

## Key Features

| Feature | Description |
|---|---|
| File-based knowledge base | Markdown on disk, no database; portable and git-versioned |
| AI agent orchestration | 20 pre-built role templates (CEO, CTO, Marketer, etc.) with goals, skills, scheduled jobs |
| Provider adapter layer | Structured adapters for Claude Code (`claude_local`) and Codex (`codex_local`); per-run model/effort override |
| Scheduled jobs | Cron-based automation via node-cron; agents run 24/7 (e.g., Reddit scout every 6h, weekly reports) |
| Embedded HTML apps | Any directory with `index.html` and no `index.md` renders as an iframe; `.app` marker for full-screen mode |
| Web terminal | xterm.js interactive terminal for direct CLI sessions |
| WYSIWYG editor | Tiptap (ProseMirror) with markdown toggle, tables, slash commands, auto-save at 500ms |
| Git-backed history | Every save auto-commits; full diff viewer; page restore to any prior commit |
| Missions & Tasks | Kanban boards for goal decomposition and progress tracking |
| Linked repos | `.repo.yaml` in a data dir links it to a Git repo; agents read source code in context |
| Full-text search | Cmd+K instant fuzzy search across all pages |

## Architecture

The system has three tiers:

**1. Data tier** — `data/` directory on disk. Pages are directories with `index.md` + assets, or standalone `.md` files. YAML frontmatter stores title, created, modified, tags, icon, order. No database. Path traversal prevention enforced at every API route (all paths must start with `DATA_DIR`).

**2. Application tier** — Next.js 16 (App Router) + TypeScript web app (`src/`). API routes cover tree, pages, upload, assets, search, agents, git. State managed with Zustand stores (tree, editor, ai-panel, task, app). Editor is Tiptap with HTML intermediate for markdown roundtrip.

**3. Daemon tier** — `server/cabinet-daemon.ts`: unified WebSocket server that handles structured AI runs, PTY terminal sessions, cron job scheduler, and real-time event streaming. Structured adapters are the default path; legacy PTY adapters remain as escape hatches.

**Agent model** — Agents are defined as persona files in `.agents/` directories. The `.cabinet` manifest (YAML) defines cabinet identity, kind (`root` or `child`), and parent-child context sharing via `shared_context` paths. The `cabinetai` CLI (`cabinetai/` package) manages installation, cabinet creation, and server lifecycle; it auto-downloads the app to `~/.cabinet/app/v{version}/` on first run.

**Core philosophy (from CLAUDE.md):** "Humans define intent. Agents do the work. The knowledge base is the shared memory between both."

## Example Usage

```bash
# Create and start a new cabinet
npx create-cabinet my-startup
cd my-startup
npx cabinetai run

# Use the CLI directly
cabinetai create engineering    # child cabinet inside an existing one
cabinetai import saas-startup   # import a template from the registry
cabinetai doctor                # run health checks
cabinetai update                # pull a newer app version
```

The onboarding wizard at `http://localhost:3000` (or port 4000 via `cabinetai run`) builds the custom agent team from 5 questions. Agents appear as workspaces in the sidebar; jobs fire on their cron schedules automatically.

## Maintenance Status

Active — v0.3.4 released April 14, 2026 (11 days before this wiki entry). 1,702 stars, 173 forks. Built by Hila Shmuel (ex-Apple Engineering Manager) in public. Contributions welcome via Discord alignment first. Cloud waitlist open at runcabinet.com. MIT license.
