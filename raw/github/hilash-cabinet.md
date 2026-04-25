# hilash/cabinet

## Metadata
- Stars: 1702
- Primary language: TypeScript
- Default branch: main
- Latest release: v0.3.4 (2026-04-14)
- License: (none)
- Homepage: (none)
- Fetched: 2026-04-25
- Final URL: https://github.com/hilash/cabinet

## Description
AI-first knowledge base and startup OS

## README

<p align="center">
  <strong>Cabinet — Your knowledge base. Your AI team.</strong><br />
  Files on disk · AI workspaces · Agents with memory
</p>

The AI-first startup OS where everything lives as markdown files on disk. No database. No vendor lock-in. Self-hosted. Your data never leaves your machine.

Built by Hila Shmuel, former Engineering Manager at Apple.

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

### Philosophy

- **Yours** — data stays local, visible, and portable; not trapped inside an AI provider's system
- **Git everything** — memory should have history; inspect changes, revert mistakes, audit how knowledge evolves
- **BYOAI** — Bring your own AI: works with Claude, Codex, local models, and whatever comes next
- **KISS** — plain files, clear behavior, systems developers can reason about
- **Security** — minimize surprise, reduce unnecessary exposure, make trust a design requirement
- **Self-hosted** — AI holding your context should run in an environment you control

### Feature table

| Feature | What it does |
|---|---|
| WYSIWYG + Markdown | Rich text editing with Tiptap. Tables, code blocks, slash commands. |
| AI Agents | Each has goals, skills, scheduled jobs. Watch them work like a real team. |
| Scheduled Jobs | Cron-based agent automation. Reddit scout every 6 hours. Weekly reports on Monday. |
| Embedded HTML Apps | Drop an `index.html` in any folder — it renders as an iframe. Full-screen mode. |
| Web Terminal | Interactive local AI CLI terminal in the browser. |
| File-Based Everything | No database. Markdown on disk. Your data is always yours, always portable. |
| Git-Backed History | Every save auto-commits. Full diff viewer. Restore any page to any point in time. |
| Missions & Tasks | Break goals into missions. Track progress with Kanban boards. |
| Internal Chat | Built-in team channels. Agents and humans communicate. |
| Full-Text Search | Cmd+K instant search across all pages. Fuzzy matching. |
| PDF & CSV Viewers | First-class support for PDFs and spreadsheets. |
| Dark/Light Mode | Theme toggle. Dark mode by default. |

### Ship HTML apps inside your knowledge base

Drop an `index.html` in any directory — it renders as an embedded app. Full-screen mode with sidebar auto-collapse. AI-generated apps written directly into your KB. Version controlled via git. No build step.

### Comparison: Cabinet vs. Obsidian vs. Notion

| Feature | Cabinet | Obsidian | Notion |
|---|---|---|---|
| AI agent orchestration | Yes | No | No |
| Scheduled cron jobs | Yes | No | No |
| Embedded HTML apps | Yes | No | No |
| Web terminal | Yes | No | No |
| Self-hosted, files on disk | Yes | Yes | No |
| No database / no lock-in | Yes | Yes | No |
| Git-backed version history | Yes | Via plugin | No |
| WYSIWYG + Markdown | Yes | Yes | Yes |

### Hire your AI team in 5 questions

Cabinet ships with 20 pre-built agent templates:

| Department | Agents |
|---|---|
| Leadership | CEO, COO, CFO, CTO |
| Product | Product Manager, UX Designer |
| Marketing | Content Marketer, SEO Specialist, Social Media, Growth Marketer, Copywriter |
| Engineering | Editor, QA Agent, DevOps Engineer |
| Sales & Support | Sales Agent, Customer Success |
| Analytics | Data Analyst |
| Operations | People Ops, Legal Advisor, Researcher |

### AI Runtime

Cabinet no longer treats the browser terminal as the only way to run AI work.

- Tasks, jobs, and heartbeats run through a provider adapter layer with persisted conversations and transcript-driven live views.
- Per-run overrides can choose provider, model, and reasoning effort; personas and jobs can inherit defaults.
- Current defaults are structured local adapters: `claude_local` for Claude Code and `codex_local` for Codex CLI.
- The web terminal stays as a first-class interactive surface for direct CLI sessions.

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
- At least one supported CLI provider: Claude Code CLI or Codex CLI
- macOS or Linux (Windows via WSL)

### Commands

```bash
npm run dev          # Next.js dev server (port 3000)
npm run dev:daemon   # Unified daemon: structured runs, terminal sessions, WebSockets, scheduler (port 3001)
npm run dev:all      # Both servers
npm run build        # Production build
npm run start        # Production mode (both servers)
```

---

## CABINETAI.md — CLI & Deployment

`cabinetai` is the runtime CLI for Cabinet. It manages installation, creates cabinets, and starts the server — all from a single `npx` command.

**Architecture:** The Cabinet web app installs to `~/.cabinet/app/v{version}/` (auto-downloaded on first use). Cabinets are lightweight data directories anywhere on disk — just a `.cabinet` manifest + `.agents/` + `.jobs/` + content files. No database.

### Commands

| Command | Description |
|---|---|
| `cabinetai create [name]` | Create a new cabinet directory |
| `cabinetai run` | Start Cabinet serving the current directory |
| `cabinetai import <template>` | Import a pre-made cabinet from the registry |
| `cabinetai list` | List cabinets in the current directory |
| `cabinetai doctor` | Run health checks on the environment |
| `cabinetai update` | Download a newer app version |
| `cabinetai uninstall` | Remove cached app versions from ~/.cabinet |

### Cabinet directory layout

```
my-startup/
  .cabinet          # YAML manifest (name, id, kind, version)
  .agents/          # Agent personas directory
  .jobs/            # Scheduled job definitions
  .cabinet-state/   # Runtime state (auto-managed)
  index.md          # Entry page with frontmatter
```

### `.cabinet` manifest format

```yaml
schemaVersion: 1
id: my-startup
name: My Startup
kind: root              # or "child"
version: 0.1.0
description: ""
entry: index.md

# Child cabinets only:
parent:
  shared_context:
    - /company/strategy/index.md

access:
  mode: subtree-plus-parent-brief
```

### Package structure

Three npm packages versioned in lockstep:

| File | npm package | Purpose |
|---|---|---|
| `package.json` | `cabinet` (private) | The Next.js web app. Source of truth for version. |
| `cli/package.json` | `create-cabinet` | Thin wrapper — delegates to `cabinetai create` + `cabinetai run` |
| `cabinetai/package.json` | `cabinetai` | Full CLI. All logic lives here. |

---

## CLAUDE.md — Agent Instruction File

### What is this project?

Cabinet is an AI-first self-hosted knowledge base and startup OS. All content lives as markdown files on disk. The web UI provides WYSIWYG editing, a collapsible tree sidebar, drag-and-drop page organization, structured AI runs for tasks/jobs/heartbeats, and interactive WebTerminal surfaces for direct CLI sessions.

**Core philosophy:** Humans define intent. Agents do the work. The knowledge base is the shared memory between both.

### Tech Stack

- Framework: Next.js 16 (App Router), TypeScript
- UI: Tailwind CSS + shadcn/ui (base-ui based, NOT Radix — no `asChild` prop)
- Editor: Tiptap (ProseMirror-based) with markdown roundtrip via HTML intermediate
- State: Zustand (tree-store, editor-store, ai-panel-store, app-store)
- AI: Claude Code and Codex CLI via the adapter runtime

### Key Rules (from CLAUDE.md)

1. No database — everything is files on disk under `/data`
2. Pages are directories with `index.md` + assets, or standalone `.md` files
3. Frontmatter (YAML) stores metadata: title, created, modified, tags, icon, order
4. Path traversal prevention — all resolved paths must start with DATA_DIR
5. shadcn/ui uses base-ui (not Radix) — DialogTrigger, ContextMenuTrigger etc. do NOT have `asChild`
6. Dark mode default — theme toggle available
7. Auto-save — debounced 500ms after last keystroke in editor-store
8. AI runs use a mixed runtime model — tasks/jobs/heartbeats default to structured adapters; WebTerminal for interactive sessions
9. Version restore — users can restore any page to a previous git commit
10. Embedded apps — dirs with `index.html` + no `index.md` render as iframes; `.app` marker for full-screen mode
11. Linked repos — `.repo.yaml` links a data dir to a Git repo; agents use this to read/search source code in context

### AI Editing Behavior

1. The request becomes a conversation with `providerId`, `adapterType`, and optional adapter config
2. Detached runs go through `/api/agents/conversations` → `conversation-runner` → `cabinet-daemon`
3. Structured adapters are the default for detached Claude/Codex runs
4. Models should edit targeted files directly and reflect durable value in KB files, not only transcript text
5. If content gets corrupted — users can restore from Version History

---

## Top-level structure

```
.agents/              ← Agent skills directory (has .agents/skills/ subdirectory)
AI-claude-editor.md   ← AI editing flow documentation
AI_PROVIDER_RUNTIME_PROGRESS.md ← Provider adapter runtime progress log
CABINETAI.md          ← CLI & deployment documentation (key doc, fetched above)
CABINET_UI_WORK_SUMMARY.md ← UI work summary
CLAUDE.md             ← Agent instruction file for Claude Code (key file, fetched above)
EDITOR.md             ← Editor documentation
PRD.md                ← Product requirements document
PROGRESS.md           ← Append-only changelog (57k — large dev log)
README.md             ← Full readme (fetched above)
assets/               ← Static assets (images, SVGs)
cabinet-release.json  ← Release manifest for cabinetai update command
cabinetai/            ← cabinetai CLI npm package source (TypeScript, esbuild)
cli/                  ← create-cabinet thin wrapper npm package
components.json       ← shadcn/ui component config
data/                 ← Content directory (KB pages, .agents/.library/, .jobs/)
deployment-packaging-versioning.md ← Deployment docs
electron/             ← Electron desktop app (macOS DMG)
eslint.config.mjs     ← ESLint config (boilerplate)
forge.config.cjs      ← Electron Forge config
next.config.ts        ← Next.js config
notifications.md      ← Notifications design doc
package-lock.json     ← (boilerplate, skip)
package.json          ← App package.json (version source of truth)
postcss.config.mjs    ← PostCSS config (boilerplate)
public/               ← Static public files
scripts/              ← Release scripts (release.sh)
server/               ← cabinet-daemon.ts (WebSocket + scheduler + agent executor)
skills-lock.json      ← Skills registry lock file
src/                  ← Main Next.js app source (TypeScript)
test/                 ← Test suite
tsconfig.json         ← TypeScript config (boilerplate)
.agents/              ← Agent definitions (skills/ subdirectory)
.dockerignore         ← Docker ignore (boilerplate)
.env.example          ← Environment variable template
.github/              ← GitHub Actions (boilerplate)
.gitignore            ← Git ignore (boilerplate)
```
