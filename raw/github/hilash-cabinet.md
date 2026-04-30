# hilash/cabinet

## Metadata
- Stars: (see https://github.com/hilash/cabinet)
- Primary language: TypeScript
- Default branch: main
- Latest release: none tagged
- License: MIT
- Homepage: https://runcabinet.com
- Fetched: 2026-04-29
- Final URL: https://github.com/hilash/cabinet

## Description

Cabinet is an AI-first self-hosted knowledge base and startup OS. All content lives as markdown files on disk. The web UI provides WYSIWYG editing, a collapsible tree sidebar, drag-and-drop page organization, structured AI runs for tasks/jobs/heartbeats, and interactive WebTerminal surfaces for direct CLI sessions.

Built by Hila Shmuel, former Engineering Manager at Apple — building Cabinet in public with the open-source community.

## README

**Your knowledge base. Your AI team.**
🗂️ Files on disk • 📁 AI workspaces • 🧠 Agents with memory

The AI-first startup OS where everything lives as markdown files on disk. No database. No vendor lock-in. Self-hosted. Your data never leaves your machine.

### From zero to AI team in 2 minutes

```bash
npx create-cabinet@latest
cd cabinet
npm run dev:all
```

Open http://localhost:3000. The onboarding wizard builds your custom AI team in 5 questions.

### The problem

Every time you start a new Claude session, it forgets everything. Your project context, your decisions, your research — gone. Scattered docs in Notion. AI sessions with no memory. Manual copy-paste between tools.

### The solution

One knowledge base. AI agents that remember everything. Scheduled jobs that compound. Your team grows while you sleep.

> If it feels like enterprise workflow software, it's wrong. If it feels like watching a team work, it's right.

### Philosophy

Cabinet is built around a few principles:

- **Yours** — Your data stays yours: local, visible, and portable. Not trapped inside a particular AI provider's system.
- **Git everything** — Memory should have history. Inspect changes, revert mistakes, audit how knowledge evolves.
- **BYOAI** — Bring your own AI. Works with Claude, Codex, OpenCode, local models, and whatever comes next.
- **KISS** — Keep it simple, stupid. Plain files, clear behavior, systems developers can reason about.
- **Security** — Minimize surprise, reduce unnecessary exposure, make trust a design requirement.
- **Self-hosted** — Runs in an environment you control.

### Everything you need. Nothing you don't.

| Feature | What it does |
|---|---|
| WYSIWYG + Markdown | Rich text editing with Tiptap. Tables, code blocks, slash commands. |
| AI Agents | Each has goals, skills, scheduled jobs. Watch them work like a real team. |
| Scheduled Jobs | Cron-based agent automation. Reddit scout every 6 hours. Weekly reports on Monday. |
| Embedded HTML Apps | Drop an `index.html` in any folder — it renders as an iframe. Full-screen mode. |
| Web Terminal | Interactive local AI CLI terminal in the browser. Kept for direct sessions, debugging, and future terminal-native features. |
| File-Based Everything | No database. Markdown on disk. Your data is always yours, always portable. |
| Git-Backed History | Every save auto-commits. Full diff viewer. Restore any page to any point in time. |
| Missions & Tasks | Break goals into missions. Track progress with Kanban boards. |
| Internal Chat | Built-in team channels. Agents and humans communicate. |
| Full-Text Search | Cmd+K instant search across all pages. Fuzzy matching. |
| PDF & CSV Viewers | First-class support for PDFs and spreadsheets. |
| Dark/Light Mode | Theme toggle. Dark mode by default. |

### Ship HTML apps inside your knowledge base

Drop an `index.html` in any directory — it renders as an embedded app. Full-screen mode with sidebar auto-collapse. AI-generated apps written directly into your KB. Version controlled via git. No build step.

### Hire your AI team in 5 questions

Cabinet ships with 20 pre-built agent templates. Each has a role, recurring jobs, and a workspace in the knowledge base.

| Department | Agents |
|---|---|
| Leadership | CEO, COO, CFO, CTO |
| Product | Product Manager, UX Designer |
| Marketing | Content Marketer, SEO Specialist, Social Media, Growth Marketer, Copywriter |
| Engineering | Editor, QA Agent, DevOps Engineer |
| Sales & Support | Sales Agent, Customer Success |
| Analytics | Data Analyst |
| Operations | People Ops, Legal Advisor, Researcher |

### How it works

1. Install & Run — One command. Next.js + daemon start.
2. Answer 5 Questions — Cabinet builds your custom AI team.
3. Watch Your Team Work — Agents create missions, write content, scout Reddit, file reports.
4. Knowledge Compounds — Every agent run, every edit adds to the KB. Context builds over time.

### AI Runtime Today

Cabinet no longer treats the browser terminal as the only way to run AI work.

- Tasks, jobs, and heartbeats now run through a provider adapter layer with persisted conversations and transcript-driven live views.
- Per-run overrides can choose provider, model, and reasoning effort, while personas and jobs can still inherit defaults.
- Current defaults are structured local adapters: `claude_local` for Claude Code and `codex_local` for Codex CLI.
- The web terminal is staying as a first-class interactive surface for direct CLI sessions and future terminal-native features.

### Architecture

```
cabinet/
  src/
    app/api/         -> Next.js API routes
    components/      -> React components (sidebar, editor, agents, jobs, terminal)
    stores/          -> Zustand state management
    lib/             -> Storage, markdown, git, agents, jobs
  server/
    cabinet-daemon.ts -> WebSocket + job scheduler + agent executor
  data/
    .agents/.library/ -> 20 pre-built agent templates
    getting-started/  -> Default KB page
```

Tech stack: Next.js 16, TypeScript, Tailwind CSS, shadcn/ui, Tiptap, Zustand, xterm.js, node-cron

### Requirements

- Node.js 20+
- At least one supported CLI provider:
  - Claude Code CLI: `npm install -g @anthropic-ai/claude-code`
  - Codex CLI: `npm install -g @openai/codex` or `brew install --cask codex`
- macOS or Linux (Windows via WSL)

### Configuration

```bash
cp .env.example .env.local
```

| Variable | Default | Description |
|---|---|---|
| KB_PASSWORD | (empty) | Password to protect the UI. Leave empty for no auth. |
| DOMAIN | localhost | Domain for the app. |

### Commands

```bash
npm run dev          # Next.js dev server (port 3000)
npm run dev:daemon   # Unified daemon: structured runs, terminal sessions, WebSockets, scheduler (port 3001)
npm run dev:all      # Both servers
npm run build        # Production build
npm run start        # Production mode (both servers)
```

### Contributing

Join the Discord and talk with Hila before coding. Once direction is aligned, open a PR on GitHub. MIT License.

### Changelog

See CHANGELOG.md for breaking changes, or follow on the documentation site at runcabinet.com.

## CLAUDE.md

### What is this project?

Cabinet is an AI-first self-hosted knowledge base and startup OS. All content lives as markdown files on disk. The web UI provides WYSIWYG editing, a collapsible tree sidebar, drag-and-drop page organization, structured AI runs for tasks/jobs/heartbeats, and interactive WebTerminal surfaces for direct CLI sessions.

Core philosophy: Humans define intent. Agents do the work. The knowledge base is the shared memory between both.

### Tech Stack

- Framework: Next.js 16 (App Router), TypeScript
- UI: Tailwind CSS + shadcn/ui (base-ui based, NOT Radix — no `asChild` prop)
- Editor: Tiptap (ProseMirror-based) with markdown roundtrip via HTML intermediate
- State: Zustand (tree-store, editor-store, ai-panel-store, app-store)
- Fonts: Inter (sans) + JetBrains Mono (code)
- Icons: Lucide (no emoji in system chrome)
- Markdown: gray-matter (frontmatter), unified/remark (MD→HTML), turndown (HTML→MD)
- AI: Claude Code and Codex CLI via the adapter runtime; WebTerminal stays in the product for interactive sessions

### Architecture (from CLAUDE.md)

```
src/
  app/api/tree/              → GET tree structure from /data
  app/api/pages/[...path]/   → GET/PUT/POST/DELETE/PATCH pages
  app/api/upload/[...path]/  → POST file upload to page directory
  app/api/assets/[...path]/  → GET/PUT static file serving + raw file writes
  app/api/search/            → GET full-text search
  app/api/agents/conversations/ → Manual task/conversation creation + listing
  app/api/agents/providers/  → Provider, model, adapter metadata
  app/api/agents/tasks/      → Task board data
  app/api/agents/scheduler/  → Scheduler control/status
  app/api/git/               → Git log, diff, commit endpoints
  stores/                    → Zustand (tree, editor, ai-panel, task, app)
  components/sidebar/        → Tree navigation, drag-and-drop, context menu
  components/editor/         → Tiptap WYSIWYG + toolbar, website/PDF/CSV viewers
  components/ai-panel/       → Right-side AI chat panel
  components/tasks/          → Task board + task detail panel
  components/agents/         → Agents workspace + live/result conversation views
  components/jobs/           → Jobs manager UI
  components/terminal/       → xterm.js web terminal
  components/composer/       → Shared composer + task runtime picker
  components/search/         → Cmd+K search dialog
  components/layout/         → App shell, header
  lib/storage/               → Filesystem ops (path-utils, page-io, tree-builder, task-io)
  lib/markdown/              → MD↔HTML conversion
  lib/git/                   → Git service (auto-commit, history, diff)
  lib/agents/                → Adapter runtime, conversation runner, personas, providers
  lib/jobs/                  → Job scheduler (node-cron)
server/
  cabinet-daemon.ts          → Unified daemon for structured runs, PTY sessions, scheduler, events
  terminal-server.ts         → Standalone PTY WebSocket server kept for focused terminal debugging/legacy use
data/                        → Content directory (KB pages, tasks, jobs)
```

### Key Rules

1. No database — everything is files on disk under `/data`
2. Pages are directories with `index.md` + assets, or standalone `.md` files. PDFs and CSVs are first-class content types.
3. Frontmatter (YAML) stores metadata: title, created, modified, tags, icon, order
4. Path traversal prevention — all resolved paths must start with DATA_DIR
5. shadcn/ui uses base-ui (not Radix) — DialogTrigger, ContextMenuTrigger etc. do NOT have `asChild`
6. Dark mode default — theme toggle available, use `next-themes` with `attribute="class"`
7. Auto-save — debounced 500ms after last keystroke in editor-store
8. AI runs use a mixed runtime model — tasks/jobs/heartbeats default to structured adapters; WebTerminal remains for interactive sessions and experimental legacy PTY flows.
9. Do not assume the terminal is being removed — the product direction is away from terminal-first task execution, while keeping terminal functionality for direct sessions and future features.
10. Version restore — users can restore any page to a previous git commit via the Version History panel
11. Embedded apps — dirs with `index.html` + no `index.md` render as iframes. Add `.app` marker for full-screen mode.
12. Linked repos — `.repo.yaml` in a data dir links it to a Git repo (local path + remote URL). Agents use this to read/search source code in context.

### AI Editing Behavior

When Cabinet starts an AI edit or task run:
1. The request becomes a conversation with `providerId`, `adapterType`, and optional adapter config.
2. Detached runs go through `/api/agents/conversations` → `conversation-runner` → `cabinet-daemon`.
3. Structured adapters are the default for detached Claude/Codex runs.
4. Interactive editor/live surfaces may still mount WebTerminal when terminal feedback matters.
5. Models should edit targeted files directly when useful and reflect durable value in KB files.
6. If content gets corrupted — users can restore from Version History.

The AI panel supports `@` mentions — users type `@PageName` to attach other pages as context.

## Top-level structure

```
.agents/          — Agent library (.library/ contains 20 pre-built agent templates)
.dockerignore
.env.example      — Environment variable template (KB_PASSWORD, DOMAIN)
.github/          — GitHub CI/CD configuration
.gitignore
AI-claude-editor.md — AI editor instructions
AI_PROVIDER_RUNTIME_PROGRESS.md — Runtime progress tracking
CABINETAI.md      — cabinetai npm package documentation
CABINET_UI_WORK_SUMMARY.md — UI work summary
CLAUDE.md         — AI agent instructions for this repo (important)
EDITOR.md         — Editor subsystem documentation
PRD.md            — Product requirements document (17KB)
PROGRESS.md       — Changelog / progress log (57KB, append-only)
README.md         — Main documentation
assets/           — Static assets (wordmark, demo gif)
cabinet-release.json — Release configuration
cabinetai/        — The npm cabinetai package (CLI entry point for npx cabinetai run)
cli/              — CLI tooling
components.json   — shadcn/ui component registry
data/             — Content directory (KB pages, tasks, jobs, agent workspaces)
deployment-packaging-versioning.md — Deployment docs
electron/         — Electron desktop app wrapper
eslint.config.mjs — Lint configuration
forge.config.cjs  — Electron Forge packaging configuration
next.config.ts    — Next.js configuration
notifications.md  — Notifications system docs
package.json      — npm dependencies and scripts
public/           — Next.js public assets
scripts/          — Build/deployment scripts
server/           — Daemon server (WebSocket, scheduler, AI runner)
skills-lock.json  — Skills lock file
src/              — Main Next.js app source (components, API routes, stores, lib)
test/             — Test suite
tsconfig.json     — TypeScript configuration
```
