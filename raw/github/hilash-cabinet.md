# hilash/cabinet

## Metadata
- Stars: 2381
- Primary language: TypeScript
- Default branch: main
- Latest release: v0.4.4
- License: MIT License
- Homepage: https://runcabinet.com
- Fetched: 2026-07-03
- Final URL: https://github.com/hilash/cabinet

## Description

AI-first knowledge base and startup OS

## README

<p align="center">
  <img src="assets/cabinet-wordmark.svg" alt="cabinet /ˈkab.ɪ.nət/" width="920">
</p>

<p align="center">
  <img src="https://runcabinet.com/demo.gif" alt="Cabinet demo" width="900">
</p>

<h1 align="center">🗄️ Cabinet</h1>

<p align="center">
  <strong>Your knowledge base. Your AI team.</strong><br />
  <sub>🗂️ Files on disk &nbsp;•&nbsp; 📁 AI workspaces &nbsp;•&nbsp; 🧠 Agents with memory</sub>
</p>

<p align="center">
  The AI-first startup OS where everything lives as markdown files on disk. No database. No vendor lock-in. Self-hosted. Your data never leaves your machine.
</p>

<p align="center">
  Built by Hila Shmuel, former Engineering Manager at Apple — now building Cabinet in public, with the open-source community.
</p>

<p align="center">
  <a href="https://x.com/HilaShmuel" target="_blank" rel="noopener noreferrer">@HilaShmuel</a>&nbsp; • &nbsp;
  <a href="https://runcabinet.com" target="_blank" rel="noopener noreferrer">runcabinet.com</a>&nbsp; • &nbsp;
  <a href="mailto:hi@runcabinet.com" target="_blank" rel="noopener noreferrer">hi@runcabinet.com</a>
</p>

<p align="center">
  <a href="https://github.com/hilash/cabinet/stargazers" target="_blank" rel="noopener noreferrer">
    <img src="https://img.shields.io/github/stars/hilash/cabinet?style=for-the-badge&logo=github&logoColor=white&label=Star%20the%20vision%20%F0%9F%98%8D%F0%9F%8C%9F&labelColor=4b4b4b&color=f5b301" alt="Star Cabinet on GitHub" valign="middle">
  </a>&nbsp;
  <a href="https://discord.gg/hJa5TRTbTH" target="_blank" rel="noopener noreferrer">
    <img src="https://img.shields.io/badge/Discord-Join%20the%20community-5865F2?style=for-the-badge&logo=discord&logoColor=white&labelColor=4b4b4b" alt="Join the Discord" valign="middle">
  </a>&nbsp;
  <a href="https://runcabinet.com/waitlist" target="_blank" rel="noopener noreferrer">
    <img src="https://img.shields.io/badge/%F0%9F%97%84%EF%B8%8F%20Cabinet-Cloud%20Waitlist-55c938?style=for-the-badge&labelColor=4b4b4b" alt="Cabinet Cloud Waitlist" valign="middle">
  </a>&nbsp;
  <a href="https://coderabbit.ai" target="_blank" rel="noopener noreferrer">
    <img src="https://img.shields.io/coderabbit/prs/github/hilash/cabinet?utm_source=oss&utm_medium=github&utm_campaign=hilash%2Fcabinet&labelColor=171717&color=FF570A&link=https%3A%2F%2Fcoderabbit.ai&label=CodeRabbit+Reviews" alt="CodeRabbit Pull Request Reviews" valign="middle">
  </a>
</p>

---

## From zero to AI team in 2 minutes

```bash
npx create-cabinet@latest
cd cabinet
npm run dev:all
```

Open [http://localhost:4000](http://localhost:4000). The onboarding wizard builds your custom AI team in 5 questions.

---

## Install, update, uninstall

Cabinet runs entirely through `npx` — no global install needed. The CLI is the [`cabinetai`](https://www.npmjs.com/package/cabinetai) package; `create-cabinet` is a thin wrapper around it.

### Install / create

```bash
npx create-cabinet@latest          # create a cabinet and start it
npx cabinetai create my-startup    # just create, don't start
npx cabinetai run                  # start Cabinet in the current dir
```

On first run, Cabinet downloads the app to `~/.cabinet/app/v{version}/` and installs its dependencies there. Your cabinet directory is just a folder of markdown files — put it anywhere.

### Update

```bash
npx cabinetai update               # check for and install a newer app version
```

The CLI compares your installed app version against `cabinet-release.json` from the latest GitHub Release.

### Uninstall / remove

```bash
npx cabinetai uninstall            # remove cached app versions only
npx cabinetai uninstall --all      # also remove global state + telemetry data
npx cabinetai uninstall --yes      # skip the confirmation prompt
npx cabinetai remove               # alias for uninstall
```

The command prints a summary of what will be deleted and asks for confirmation before doing anything. **Your cabinet directories and their data are never touched — those you'd delete manually.**

`--all` additionally removes the platform-specific telemetry directory:

- macOS: `~/Library/Application Support/cabinet-telemetry/`
- Windows: `%APPDATA%\cabinet-telemetry\`
- Linux: `$XDG_CONFIG_HOME/cabinet/` (falls back to `~/.config/cabinet/`)

To wipe Cabinet completely, run `uninstall --all` and then `rm -rf` your cabinet directories yourself.

See [docs/CABINETAI.md](docs/CABINETAI.md) for the full CLI reference.

---

## The problem

Every time you start a new Claude session, it forgets everything. Your project context, your decisions, your research — gone. Scattered docs in Notion. AI sessions with no memory. Manual copy-paste between tools.

## The solution

One knowledge base. AI agents that remember everything. Scheduled jobs that compound. Your team grows while you sleep.

> If it feels like enterprise workflow software, it's wrong. If it feels like watching a team work, it's right.

---

## Philosophy

Cabinet is built around a few principles that we think matter deeply for the future of AI + data tools:

- **Yours** — Your data stays yours: local, visible, and portable. It’s not trapped inside a particular AI provider’s system with no clean way to get it out. You stay in control of your information.
- **Git everything** — Memory should have history. You should be able to inspect changes, revert mistakes, audit how knowledge evolves, and treat your AI system like the important infrastructure it is.
- **BYOAI** — Bring your own AI. Cabinet should work with Claude, Codex, OpenCode, local models, and whatever comes next, without forcing your knowledge into a single provider’s ecosystem.
- **KISS** — Keep it simple, stupid. AI tools should be understandable, inspectable, and hackable. We prefer plain files, clear behavior, and systems that developers can actually reason about.
- **Security** — We care deeply about security. If AI is going to work with your documents, research, plans, and internal context, the system should minimize surprise, reduce unnecessary exposure, and make trust a design requirement rather than an afterthought.
- **Self-hosted** — If AI is going to hold your context, plans, research, and operating memory, it should run in an environment you control.

## Everything you need. Nothing you don't.

| Feature | What it does |
|---|---|
| **WYSIWYG + Markdown** | Rich text editing with Tiptap. Tables, code blocks, slash commands. |
| **AI Agents** | Each has goals, skills, scheduled jobs. Watch them work like a real team. |
| **Skills** | Browse and install from skills.sh or any GitHub repo. Attach per agent, or `@`-mention in the composer to scope to a single task. |
| **Scheduled Jobs** | Cron-based agent automation. Reddit scout every 6 hours. Weekly reports on Monday. |
| **Embedded HTML Apps** | Drop an `index.html` in any folder — it renders as an iframe. Full-screen mode. |
| **Web Terminal** | Interactive local AI CLI terminal in the browser. Kept for direct sessions, debugging, and future terminal-native features such as tmux-style Cabinet workflows. |
| **File-Based Everything** | No database. Markdown on disk. Your data is always yours, always portable. |
| **Git-Backed History** | Every save auto-commits. Full diff viewer. Restore any page to any point in time. |
| **Missions & Tasks** | Break goals into missions. Track progress with Kanban boards. |
| **Internal Chat** | Built-in team channels. Agents and humans communicate. |
| **Full-Text Search** | Cmd+K instant search across all pages. Fuzzy matching. |
| **PDF & CSV Viewers** | First-class support for PDFs and spreadsheets. |
| **Dark/Light Mode** | Theme toggle. Dark mode by default. |

---

## Ship HTML apps inside your knowledge base

This is the biggest difference between Cabinet and tools like Obsidian or Notion. Drop an `index.html` in any directory — it renders as an embedded app. Full-screen mode with sidebar auto-collapse. AI-generated apps written directly into your KB. Version controlled via git. No build step.

---

## Not another note-taking app

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

---

## Hire your AI team in 5 questions

Cabinet ships with 20 pre-built agent templates. Each has a role, recurring jobs, recommended skills, and a workspace in the knowledge base.

| Department | Agents |
|---|---|
| **Leadership** | CEO, COO, CFO, CTO |
| **Product** | Product Manager, UX Designer |
| **Marketing** | Content Marketer, SEO Specialist, Social Media, Growth Marketer, Copywriter |
| **Engineering** | Editor, QA Agent, DevOps Engineer |
| **Sales & Support** | Sales Agent, Customer Success |
| **Analytics** | Data Analyst |
| **Operations** | People Ops, Legal Advisor, Researcher |

---

## How it works

1. **Install & Run** — One command. Next.js + daemon start.
2. **Answer 5 Questions** — Cabinet builds your custom AI team.
3. **Watch Your Team Work** — Agents create missions, write content, scout Reddit, file reports.
4. **Knowledge Compounds** — Every agent run, every edit adds to the KB. Context builds over time.

---

## AI Runtime Today

Cabinet no longer treats the browser terminal as the only way to run AI work.

- **Tasks, jobs, and heartbeats** now run through a provider adapter layer with persisted conversations and transcript-driven live views.
- **Per-run overrides** can choose provider, model, and reasoning effort, while personas and jobs can still inherit defaults.
- **Current defaults** are structured local adapters: `claude_local` for Claude Code and `codex_local` for Codex CLI.
- **The web terminal is staying** as a first-class interactive surface for direct CLI sessions and future terminal-native features such as Cabinet-managed tmux-like workspaces.

---

## Architecture

```
cabinet/
  src/
    app/api/         -> Next.js API routes
    components/      -> React components (sidebar, editor, agents, jobs, terminal)
    stores/          -> Zustand state management
    lib/             -> Storage, markdown, git, agents, jobs
  server/
    cabinet-daemon.ts -> WebSocket + job scheduler + structured adapters + agent executor
    pty/              -> PTY session module (spawn, Claude lifecycle, ansi)
  data/
    .agents/.library/ -> 20 pre-built agent templates
    getting-started/  -> Default KB page
```

**Tech stack:** Next.js 16, TypeScript, Tailwind CSS, shadcn/ui, Tiptap, Zustand, xterm.js, node-cron

---

## Requirements

- **Node.js** 22+ (LTS). The repo ships an `.nvmrc` — run `nvm use` to auto-switch. Node 20 still works but produces an `EBADENGINE` warning from a transitive `chevrotain@12` pulled in by mermaid.
- At least one supported CLI provider:
  - **Claude Code CLI** (`npm install -g @anthropic-ai/claude-code`)
  - **Codex CLI** (`npm install -g @openai/codex` or `brew install --cask codex`)
- **Source mode:** macOS, Linux, or Windows
- **Electron desktop packaging:** macOS and Windows

## Configuration

```bash
cp .env.example .env.local
```

| Variable | Default | Description |
|----------|---------|-------------|
| `KB_PASSWORD` | _(empty)_ | Password to protect the UI. Leave empty for no auth. The auth cookie is PBKDF2(password, per-install salt) with login rate-limiting; changing the password logs everyone out once. |
| `CABINET_AUTH_SALT` | _(auto)_ | Per-install auth salt, auto-generated into `.cabinet.env` on first run. Set only to pin a value; changing it forces a one-time re-login. |
| `CABINET_LOGIN_PBKDF2_ITERS` | `600000` | PBKDF2 iteration count for the auth token. Lower only for constrained hardware. |
| `CABINET_LOGIN_MAX_ATTEMPTS` / `_WINDOW_MS` / `_LOCKOUT_MS` / `CABINET_LOGIN_GLOBAL_MAX` | `10` / `900000` / `900000` / `60` | Login rate-limit tuning (per-client + global failed-attempt buckets). |
| `DOMAIN` | `localhost` | Domain for the app. |

### Authentication

Setting `KB_PASSWORD` turns on a single password gate for the whole UI/API
(leave it empty for no auth). The session cookie is `PBKDF2-HMAC-SHA256` over a
per-install salt that's auto-generated into `.cabinet.env` on first run, the
login endpoint is rate-limited against brute force, and the gate verifies in
constant time. Changing the password (or salt/iterations) logs everyone out
once. Full details, threat model, and tuning: **[docs/AUTH.md](docs/AUTH.md)**.

## Commands

```bash
npm run dev          # Next.js dev server (port 4000 by default)
npm run dev:daemon   # Unified daemon: structured runs, terminal sessions, WebSockets, scheduler (port 4100 by default)
npm run dev:all      # Both servers
npm run electron:start   # Launch Electron desktop against the local dev servers
npm run build        # Production build
npm run start        # Production mode (both servers)
npm run electron:make:win  # Build a portable Windows zip
```

---

## Ready to build your AI team?

Cabinet is free, open source, and self-hosted. Your data never leaves your machine.

```bash
npx create-cabinet my-startup
```

[Get Started](https://runcabinet.com) | <a href="https://github.com/hilash/cabinet/stargazers" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/github/stars/hilash/cabinet?label=GitHub%20Stars&logo=github&color=f5b301" alt="GitHub Stars" valign="middle"></a>

---

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for breaking changes, or follow the full release history on the [documentation site](https://runcabinet.com).

## Privacy

Cabinet sends anonymous usage telemetry by default (event counts, versions,
platform — never file contents, paths, prompts, or secrets).

To turn it off, pick one:

```bash
export CABINET_TELEMETRY_DISABLED=1   # env var (any shell session)
```

…or open **Settings → Privacy** and toggle **Send anonymous usage telemetry**
off. To also wipe the local install ID and queue, run
`npx cabinetai uninstall --all`.

See [TELEMETRY.md](TELEMETRY.md) for the full event list, payload schema,
and where data is stored.

## Community

Questions, ideas, feedback, screenshots, wild experiments — bring them to the [Discord](https://discord.gg/hJa5TRTbTH). That’s where the Cabinet community hangs out and where a lot of the product direction gets shaped in real time.

---

## Contributing

Cabinet is moving fast right now. We’d love thoughtful contributors who want to help shape it early.

If you’re thinking about opening a PR, please start by joining the [Discord](https://discord.gg/hJa5TRTbTH) and talking with Hila before coding. Hila is Cabinet’s builder, and that early sync helps us keep the roadmap coherent while the product is still evolving rapidly.

Once the direction is aligned, open your PR on [GitHub](https://github.com/hilash/cabinet). The goal is not gatekeeping — it’s making sure your energy goes into work that has a clear path to landing and shipping.

---

MIT License

---

## Star History

<a href="https://www.star-history.com/?repos=hilash%2Fcabinet&type=date&legend=top-left" target="_blank" rel="noopener noreferrer">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=hilash/cabinet&type=date&theme=dark&legend=top-left" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=hilash/cabinet&type=date&legend=top-left" />
   <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=hilash/cabinet&type=date&legend=top-left" />
 </picture>
</a>


## Docs

### docs/CLAUDE.md

# CLAUDE.md — Cabinet

## What is this project?

Cabinet is an AI-first self-hosted knowledge base and startup OS. All content lives as markdown files on disk. The web UI provides WYSIWYG editing, a collapsible tree sidebar, drag-and-drop page organization, structured AI runs for tasks/jobs/heartbeats, and interactive `WebTerminal` surfaces for direct CLI sessions.

**Core philosophy:** Humans define intent. Agents do the work. The knowledge base is the shared memory between both.

## Tech Stack

- **Framework:** Next.js 16 (App Router), TypeScript
- **UI:** Tailwind CSS + shadcn/ui (base-ui based, NOT Radix — no `asChild` prop)
- **Editor:** Tiptap (ProseMirror-based) with markdown roundtrip via HTML intermediate
- **State:** Zustand (tree-store, editor-store, ai-panel-store, task-store, app-store)
- **Fonts:** Inter (sans) + JetBrains Mono (code)
- **Icons:** Lucide (no emoji in system chrome)
- **Markdown:** gray-matter (frontmatter), unified/remark (MD→HTML), turndown (HTML→MD)
- **AI providers:** Claude Code, Codex CLI, Cursor CLI, OpenCode, Copilot CLI, Grok CLI, Pi, and a generic CLI adapter — all driven through the shared adapter runtime in `src/lib/agents/`.

## Architecture

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
  app/api/agents/skills/     → Skill library: list/CRUD, import (github/skills.sh/local), bundle-into-cabinet, trust, scan, catalog
  app/api/git/               → Git log, diff, commit endpoints
  stores/                    → Zustand (tree, editor, ai-panel, task, app)
  components/sidebar/        → Tree navigation, drag-and-drop, context menu
  components/editor/         → Tiptap WYSIWYG + toolbar, website/PDF/CSV/office viewers
  components/editor/office/  → Read-only viewers for .docx, .xlsx, .pptx
  components/ai-panel/       → Right-side AI chat panel
  components/tasks/          → Task board + task detail panel
  components/agents/         → Agents workspace + live/result conversation views
  components/jobs/           → Jobs manager UI
  components/terminal/       → xterm.js web terminal
  components/composer/       → Shared composer + task runtime picker (supports @page, @agent, @skill mentions)
  components/skills/         → Skill library, detail page, add dialog, picker, "Skills offered" transcript footer
  components/search/         → Cmd+K search dialog
  components/layout/         → App shell, header
  lib/storage/               → Filesystem ops (path-utils, page-io, tree-builder, task-io)
  lib/markdown/              → MD↔HTML conversion
  lib/git/                   → Git service (auto-commit, history, diff)
  lib/agents/                → Adapter runtime, conversation runner, personas, providers
  lib/agents/skills/         → Multi-origin skill loader, trust gating, sync (mount/symlink), discovery scan, lock file
  lib/jobs/                  → Job scheduler (node-cron)
server/
  cabinet-daemon.ts          → Unified daemon: structured adapter runs, PTY sessions, scheduler, event bus
  pty/                       → PTY session module: ansi, claude-lifecycle, manager, types
data/                        → Content directory (KB pages, tasks, jobs)
```

## Key Rules

1. **No database** — everything is files on disk under `/data`
2. **Pages** are directories with `index.md` + assets, or standalone `.md` files. PDFs and CSVs are also first-class content types.
3. **Frontmatter** (YAML) stores metadata: title, created, modified, tags, icon, order
4. **Path traversal prevention** — all resolved paths must start with DATA_DIR
5. **shadcn/ui uses base-ui** (not Radix) — DialogTrigger, ContextMenuTrigger etc. do NOT have `asChild`
6. **Dark mode default** — theme toggle available, use `next-themes` with `attribute="class"`
7. **Auto-save** — debounced 500ms after last keystroke in editor-store
8. **AI runs use a mixed runtime model** — tasks/jobs/heartbeats default to structured adapters; terminal mode (PTY sessions) is a first-class alternative that runs inside the same daemon process via `server/pty/`. `WebTerminal` is the interactive surface for both.
9. **Terminal is a first-class runtime** — not deprecated, not an escape hatch. Terminal mode is user-selectable per task (Native / Terminal toggle in the composer) and is the direction for future terminal-native workflows (Cabinet-managed tmux-like sessions).
10. **Version restore** — users can restore any page to a previous git commit via the Version History panel
11. **Embedded apps** — dirs with `index.html` + no `index.md` render as iframes. Add `.app` marker for full-screen mode (sidebar + AI panel auto-collapse)
12. **Linked repos** — `.repo.yaml` in a data dir links it to a Git repo (local path + remote URL). Agents use this to read/search source code in context. See `data/CLAUDE.md` for full spec.
13. **Office documents** — `.docx`, `.xlsx`/`.xlsm`, `.pptx` render inline via dynamically-imported client viewers (docx-preview, SheetJS, pptx-preview). Read-only; "Download" + "Reveal" actions in the viewer header. Legacy binary formats (`.doc`, `.xls`, `.ppt`) keep the Fallback viewer.
14. **Google Workspace pages** — a markdown page with a `google:` frontmatter key (`url`, optional `kind` / `embedUrl`) is rendered by `GoogleDocViewer` instead of the Tiptap editor. The iframe needs "Anyone with the link" or "Publish to Web" on Google's side. OAuth-based sync is not yet implemented.
15. **Skills** — Anthropic-format skill bundles (`SKILL.md` + frontmatter + optional `references/`/`scripts/`/`assets/`). Resolved across four origins with precedence: cabinet-scoped (`data/<cabinet>/.agents/skills/`) > cabinet-root (`<repo>/.agents/skills/`) > linked-repo > system (`~/.claude/skills/`, `~/.agents/skills/`) > legacy-home (`~/.cabinet/skills/`). Personas reference skills by key in `skills:` (persistent attachment) and `recommendedSkills:` (template defaults shown as preselected toggles in the new-agent flow). Trust gating evaluates each skill at mount time using auto-detected trust level × verified-publisher × author `trust-policy:` frontmatter; operator decisions persist in `.cabinet/skills-trust.json`. Compose `@skill-name` to attach a skill run-only without persisting to the persona. Plan: `docs/SKILLS_PLAN.md`.
16. **Registry templates come from the cabinets manifest** — the home carousel and the *Cabinets / AI teams, off the shelf* page (`registry-browser.tsx`) read from `https://raw.githubusercontent.com/hilash/cabinets/HEAD/manifest.json`, which is auto-built by the `build-manifest.yml` GitHub Action in the [`cabinets`](https://github.com/hilash/cabinets) registry on every push. The fetch is cached in-process for 10 minutes (`src/lib/registry/registry-manifest.ts`) and falls back to a small bundled list if offline. Cover images are fetched directly from `…/HEAD/<slug>/cover.jpg`. **Do not** hand-edit registry-manifest.ts to add new cabinets — add them to the registry repo and CI rebuilds the manifest.
17. **No em-dashes in user-facing copy.** Do not use `—` (em-dash, `&mdash;`, U+2014) in UI strings, onboarding/marketing copy, in-app docs, or anything a user reads. Use a period, comma, parentheses, or rewrite. Em-dashes in code comments, commit messages, and internal docs (like this file) are fine. This rule exists because em-dashes read as "AI-written" and we want copy that sounds human.
18. **Connect Knowledge (cloud & local sources)** — per-room knowledge sources live in `<room>/.agents/.config/knowledge-sources.json` (`src/lib/knowledge-sources/store.ts`), NOT a global table. Two surfaces: a per-room cloud **browser** section (`surface: "browser"`, served read-only through the `gdrive:`-prefixed serve/reveal routes) and **inline mounts** (`surface: "inline"`) — a symlink at `treePath` pointing at the provider's desktop-sync folder, recorded with `provider` + `policy`. The tree-builder marks inline mount nodes (`knowledgeProvider`/`knowledgePolicy`) by cross-referencing `getInlineSourceMap()` and propagates policy to descendants. **Read-only is enforced server-side:** `assertWritablePath()` returns 403 for any write *strictly under* a read-only inline mount — add this guard to any NEW file-mutation route (pages/assets/upload already have it). Providers come from `detectProvider()` in `src/lib/google-drive/detect-desktop.ts` (Google Drive, iCloud, OneDrive/SharePoint, Dropbox) reading the local desktop-sync mount, no OAuth. Native `.gdoc/.gsheet` shortcuts are parsed by `src/lib/google-drive/native-docs.ts` (used by the tree-builder + `readPage`) so they render via `GoogleDocViewer` (rule 14). Notion/Confluence are MCP connectors (Integrations Hub), not file sources. Registry: `src/lib/knowledge-sources/providers.ts`. Plan: `docs/CONNECT_KNOWLEDGE_PRD.md`.

## AI Editing Behavior (CRITICAL)

When Cabinet starts an AI edit or task run:

1. **The request becomes a conversation** with `providerId`, `adapterType`, and optional adapter config such as model or effort.
2. **Detached runs** go through `/api/agents/conversations` → `conversation-runner` → `cabinet-daemon`.
3. **Structured adapters are the default** for detached Claude/Codex runs; terminal mode (PTY, named `*_legacy` in the adapter registry for historical reasons) is a first-class alternative surfaced by the composer's Native / Terminal toggle.
4. **Terminal-mode tasks render with `WebTerminal`** — xterm.js bound to the daemon's PTY WebSocket — instead of the structured TurnBlock transcript.
5. **Models should edit targeted files directly when useful** and reflect durable value in KB files, not only transcript text.
6. **If content gets corrupted** — users can restore from Version History (clock icon → select commit → Restore)

The AI panel supports `@` mentions — users type `@PageName` to attach pages as context, `@AgentName` to dispatch to another agent, or `@skill-name` to attach a skill for this run only (does NOT persist to the persona's `skills:` list). Mentioned pages' content is fetched and appended to the prompt; mentioned skills are merged with the persona's skills and trust-gated before mounting via `prepareSkillMount`.


## Commands

```bash
npm run dev          # Start Next.js dev server (default: localhost:4000, auto-bumps if busy)
npm run dev:daemon   # Start unified daemon (default: localhost:4100, auto-bumps if busy)
                     #   PTY sessions + structured adapters + scheduler + event bus, under tsx watch
npm run dev:all      # Start both servers
npm run debug:chrome # Launch Chrome with CDP on localhost:9222 for frontend debugging
npm run build        # Production build
npm run lint         # ESLint
npm run skills:sync  # Verify skills-lock.json against on-disk skill bundles (drift report)
```

## Frontend Debugging

Use `npm run debug:chrome` when you need a debuggable browser session. It launches Chrome or Chromium with `--remote-debugging-port=9222`, opens Cabinet at `http://localhost:4000` by default (override by passing a URL as the first argument), and prints the DevTools endpoints:

- `http://127.0.0.1:9222/json/version`
- `http://127.0.0.1:9222/json/list`

This makes it possible to attach over CDP and inspect real DOM, network, and screenshots instead of guessing at frontend state.

## Cabinetai CLI invariants

### Where the npx tools live

Both npm packages ship from this monorepo, not separate repos:

- **`cabinetai/`** — published as [`cabinetai`](https://www.npmjs.com/package/cabinetai). The full CLI: `create`, `run`, `update`, `doctor`, `import`, `list`, `uninstall`, `reset-config`. Built with esbuild from `cabinetai/src/`.
- **`cli/index.cjs`** — published as [`create-cabinet`](https://www.npmjs.com/package/create-cabinet). A thin wrapper that calls `cabinetai create <dir>` and then `cabinetai run` in the new subdir. Pinned to a matching `cabinetai` version via its `dependencies`.

### Safety rules (read before "fixing" anything in the bootstrap path)

1. **`cabinetai/src/lib/scaffold.ts::bootstrapCabinetAt()` refuses to scaffold a cabinet when the resolved target is `os.homedir()` or the filesystem root.** Exits 1 with a friendly message recommending an empty subdir or `--data-dir <empty-dir>`. Covers cwd fallthrough, `--data-dir ~`, and `CABINET_DATA_DIR=~`. See [#71](https://github.com/hilash/cabinet/pull/71) (closes [#59](https://github.com/hilash/cabinet/issues/59)).

2. **Do NOT "fix" this by relocating `CABINET_HOME`.** That approach was rejected in [#60](https://github.com/hilash/cabinet/pull/60) — read the close comment for the full reasoning. The historical ENOTDIR crash was a safety net; removing it without the guard lets `cabinetai run` from `~` silently scribble `.agents/`, `.jobs/`, `.cabinet-state/`, `index.md`, and a `.cabinet` manifest file directly into the user's home directory.

3. **`create-cabinet` (cli/index.cjs) is safe transitively** — `cabinetai create` always scaffolds into `cwd/<slug>` and errors on empty slug (so `.`, `..`, `~`, `$HOME` all bounce). The post-create `cabinetai run` then runs from the new subdir, never HOME. The guard in #71 is defense-in-depth.

4. **When fixing a crash anywhere in the bootstrap/install path, trace what happens *before* the crash.** If the crash is the only thing stopping a worse silent outcome (HOME pollution, data loss, unrecoverable state), fix the root cause upstream instead of removing the crash.

## Progress Tracking

After every change you make to this project, append an entry to `PROGRESS.md` using this format:

```
[YYYY-MM-DD] Brief description of what changed in 1-3 sentences.
```

This is mandatory. Do not skip it. The PROGRESS.md file is the changelog for this project.


### docs/CABINETAI.md

# cabinetai — CLI & Deployment

## Overview

`cabinetai` is the runtime CLI for Cabinet. It manages the app installation, creates cabinets, and starts the server — all from a single `npx` command.

**Architecture:** The Cabinet web app installs to `~/.cabinet/app/v{version}/` (auto-downloaded on first use). Cabinets are lightweight data directories anywhere on disk — just a `.cabinet` manifest + `.agents/` + `.jobs/` + content files. No database.

## Quick Start

```bash
mkdir my-startup && cd my-startup
npx cabinetai run
```

Or with explicit create:

```bash
npx cabinetai create my-startup
cd my-startup
npx cabinetai run
```

## Commands

| Command | Description |
|---|---|
| `cabinetai create [name]` | Create a new cabinet directory |
| `cabinetai run` | Start Cabinet serving the current directory |
| `cabinetai import <template>` | Import a pre-made cabinet from the registry |
| `cabinetai list` | List cabinets in the current directory |
| `cabinetai doctor` | Run health checks on the environment |
| `cabinetai update` | Download a newer app version |
| `cabinetai uninstall` (alias: `remove`) | Remove cached app versions from ~/.cabinet |

### `cabinetai create [name]`

Creates a new cabinet directory in the current folder.

```bash
cabinetai create my-startup          # root cabinet
cd my-startup
cabinetai create engineering         # child cabinet inside an existing one
```

What it creates:

```
my-startup/
  .cabinet          # YAML manifest (name, id, kind, version)
  .agents/          # Agent personas directory
  .jobs/            # Scheduled job definitions
  .cabinet-state/   # Runtime state (auto-managed)
  index.md          # Entry page with frontmatter
```

### `cabinetai run`

Starts Cabinet serving the current cabinet directory.

```bash
cabinetai run
cabinetai run --no-open              # don't open browser
cabinetai run --app-version 0.3.1    # use a specific app version
```

On first run, downloads the app to `~/.cabinet/app/` and installs dependencies. If the current directory is not already a cabinet, `run` bootstraps it in place by creating the `.cabinet`, `.agents/`, `.jobs/`, and `.cabinet-state/` structure before starting the server.

| Env Variable | Default | Description |
|---|---|---|
| `CABINET_APP_PORT` | `4000` | App server port |
| `CABINET_DAEMON_PORT` | `4100` | Daemon server port |

### `cabinetai import <template>`

Imports a cabinet template from the [hilash/cabinets](https://github.com/hilash/cabinets) registry.

```bash
cabinetai import saas-startup
cabinetai import career-ops
cabinetai import text-your-mom
```

### `cabinetai list`

Lists all cabinets in the current directory tree.

```bash
cabinetai list
```

```
  Name              Kind    Path              Agents  Jobs
  My Startup        root    .                 3       2
  Engineering       child   engineering       2       1
```

### `cabinetai doctor`

Runs health checks: Node.js version, cabinet structure, app installation, dependencies, port availability.

```bash
cabinetai doctor
cabinetai doctor --fix       # attempt auto-repair
cabinetai doctor --quiet     # suppress output, auto-fix only
```

### `cabinetai update`

Downloads a newer app version by checking the release manifest on GitHub.

```bash
cabinetai update
```

### `cabinetai uninstall` (alias: `remove`)

Removes cached app versions from `~/.cabinet/`. Prints a summary of what will be deleted and asks for confirmation. Your cabinet directories and their data are never touched — those you'd delete manually.

```bash
cabinetai uninstall          # remove cached app versions only
cabinetai uninstall --all    # remove ~/.cabinet AND telemetry data
cabinetai uninstall --yes    # skip the confirmation prompt
cabinetai remove             # alias for uninstall
```

With `--all`, also removes the platform-specific telemetry directory:

- macOS: `~/Library/Application Support/cabinet-telemetry`
- Windows: `%APPDATA%\cabinet-telemetry`
- Linux: `$XDG_CONFIG_HOME/cabinet` (falls back to `~/.config/cabinet`)

---

## File System Layout

### Global (`~/.cabinet/`)

```
~/.cabinet/
  app/
    v0.3.1/               # Version-pinned app install
      package.json
      node_modules/
      .next/
      server/
      src/
      .env.local
  state/
    runtime-ports.json    # Currently running server info
  config.json             # Global config (optional)
```

### Cabinet directory (anywhere on disk)

```
my-startup/
  .cabinet                # YAML manifest
  .cabinet-state/         # Runtime state (auto-created by app)
    runtime-ports.json
    install.json
    file-schema.json
  .agents/
    ceo/
      persona.md
      tasks/
    cto/
      persona.md
  .jobs/
    weekly-brief.yaml
  index.md                # Entry page
  company/
    index.md
  engineering/
    .cabinet              # Child cabinet manifest
    .agents/
    .jobs/
    index.md
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

---

## Package Structure

Three npm packages, all versioned in lockstep:

| File | npm package | Purpose |
|---|---|---|
| `package.json` | `cabinet` (private) | The Next.js web app. Source of truth for version. |
| `cli/package.json` | `create-cabinet` | Thin wrapper — delegates to `cabinetai create` + `cabinetai run` |
| `cabinetai/package.json` | `cabinetai` | Full CLI. All logic lives here. |

```
cabinet/
  package.json              # cabinet (the app) — version source of truth
  cli/
    package.json            # create-cabinet
    index.cjs               # Thin wrapper, delegates to cabinetai
    README.md
  cabinetai/
    package.json            # cabinetai
    README.md
    esbuild.config.mjs      # Bundles to single dist/index.js
    tsconfig.json
    src/
      index.ts              # Commander.js program, registers all commands
      version.ts            # Version injected at build time by esbuild
      commands/
        create.ts
        run.ts
        doctor.ts
        update.ts
        import.ts
        list.ts
        uninstall.ts
      lib/
        log.ts              # Colored console output
        process.ts          # npmCommand(), spawn helpers
        paths.ts            # CABINET_HOME, findCabinetRoot(), slugify()
        ports.ts            # Port detection, runtime-ports.json I/O
        app-manager.ts      # ensureApp() — download + install app if missing
        cabinet-manifest.ts # Read/write .cabinet YAML files
        health-checks.ts    # Doctor check implementations
    dist/
      index.js              # Single bundled file (gitignored)
```

### How `create-cabinet` relates to `cabinetai`

`npx create-cabinet my-project` is equivalent to `cabinetai create my-project && cd my-project && cabinetai run`.

The wrapper resolves `cabinetai` from local `node_modules` first, then falls back to `npx cabinetai@latest`.

---

## Releasing

One command bumps all versions, commits, tags, and pushes:

```bash
./scripts/release.sh patch   # or minor, major
```

### What `release.sh` does

1. Reads the current version from `package.json`
2. Calculates the next version based on bump type
3. Updates `"version"` in all three package.json files:
   - `package.json` — cabinet app
   - `cli/package.json` — create-cabinet
   - `cabinetai/package.json` — cabinetai
4. Runs `npm install --package-lock-only` to update the lockfile
5. Regenerates `cabinet-release.json` with the new tag
6. Commits: `Release vX.Y.Z`
7. Creates git tag: `vX.Y.Z`
8. Pushes commit + tag to `origin/main`

### What GitHub Actions does (triggered by the tag)

| Job | What it publishes |
|---|---|
| `release-assets` | GitHub Release + `cabinet-release.json` artifact |
| `publish-cli` | `create-cabinet@X.Y.Z` to npm |
| `publish-cabinetai` | `cabinetai@X.Y.Z` to npm (builds with esbuild first) |
| `electron-macos` | Signed macOS DMG + ZIP attached to the GitHub Release |

### Verify after release

```bash
npm view create-cabinet version     # should match
npm view cabinetai version          # should match
gh release view vX.Y.Z -R hilash/cabinet
npx cabinetai --version
```

### Release manifest

`cabinet-release.json` is published as a GitHub Release asset. The `cabinetai update` command fetches it to check for newer versions:

```
https://github.com/hilash/cabinet/releases/latest/download/cabinet-release.json
```

### Required GitHub secrets

| Secret | Used by |
|---|---|
| `NPM_TOKEN` | `publish-cli` and `publish-cabinetai` |
| `APPLE_ID` | Electron notarization |
| `APPLE_APP_PASSWORD` | Electron notarization |
| `APPLE_TEAM_ID` | Electron notarization |
| `APPLE_SIGN_IDENTITY` | Electron code signing |
| `APPLE_CERTIFICATE` | Electron code signing |
| `APPLE_CERTIFICATE_PASSWORD` | Electron code signing |

`GITHUB_TOKEN` is provided automatically by GitHub Actions.

---

## Key Implementation Details

### `ensureApp(version)`

Checks if `~/.cabinet/app/v{version}/` exists and is ready. If not:

1. Tries to download the release tarball from GitHub (`/archive/refs/tags/vX.Y.Z.tar.gz`)
2. Falls back to `git clone --depth 1 --branch vX.Y.Z` if tarball is unavailable
3. Falls back to `git clone --depth 1` (HEAD) if the tag doesn't exist
4. Runs `npm install`
5. Copies `.env.example` to `.env.local`

### `findCabinetRoot(startDir)`

Walks up from `startDir` looking for a `.cabinet` file (not directory). Returns the directory containing it. This is how `cabinetai run` knows which cabinet to serve.

### Version injection

The CLI version is injected at build time via esbuild `define`:

```js
define: { "CABINETAI_VERSION": JSON.stringify(pkg.version) }
```

No hardcoded version strings in source code. `version.ts` reads the injected constant.

### Port detection

Default ports: app=4000, daemon=4100. Scans up to 200 ports from the preferred starting port. Configurable via `CABINET_APP_PORT` and `CABINET_DAEMON_PORT` env vars.

### Server reuse

`cabinetai run` checks `.cabinet-state/runtime-ports.json` — if a server is already running for this cabinet directory (health check confirms), it reuses the existing server and opens the browser.


### docs/AUTH.md

# Authentication & access control

Cabinet ships with a single, optional password gate for the whole UI/API. It is
**off by default** (no login) and turns on the moment you set `KB_PASSWORD`.

This document describes the auth model after the issue #11 hardening
(PBKDF2 + per-install salt + login rate-limiting). For the user-facing env
reference, see the table in the main [README](../README.md#configuration).

---

## TL;DR

- Set `KB_PASSWORD` → the whole app requires login. Leave it empty → no auth.
- The session cookie (`kb-auth`) is `PBKDF2-HMAC-SHA256(password, per-install salt)`,
  not a fast plain hash.
- A per-install random salt is generated once into `.cabinet.env`.
- The login endpoint is rate-limited (per-client + a global ceiling) to stop
  brute force.
- Changing the password, salt, or iteration count logs everyone out once.

## How it works

### The gate

`src/proxy.ts` is the Next.js **proxy** (the renamed-in-Next-16 middleware; it is
auto-detected at `src/proxy.ts` and runs on the Node.js runtime). On every
request, when auth is enabled, it requires a valid `kb-auth` cookie:

- Allowed without a cookie: `/login`, `/api/auth/login`, `/api/auth/check`,
  `/api/health*`, and Next static assets.
- Missing/invalid cookie → API routes get `401`, page routes redirect to
  `/login`.
- Verification is **constant-time**, and the expected token is **memoized** per
  process, so the gate stays O(1) per request (PBKDF2 runs once per process, not
  per request).

### The token

The `kb-auth` cookie value is:

```
PBKDF2-HMAC-SHA256(password, salt, iterations)  →  256-bit, lowercase hex
```

- **Slow KDF (PBKDF2)** — default **600,000** iterations. This is the
  defense-in-depth that makes *offline* password recovery from a leaked cookie
  expensive.
- **Per-install salt** — a random 32-byte value, distinct per deployment, so a
  leaked cookie can't be attacked with precomputed/cross-install tables.
- One shared module, `src/lib/auth/kb-auth.ts`, is the single source of truth
  for the derivation; the gate, the login route, and the check route all use it
  so they can never drift.

Cookie attributes are unchanged: `HttpOnly`, `SameSite=Lax`, `Path=/`, 30-day
`Max-Age`, and `Secure` in production unless `KB_ALLOW_HTTP=1`.

### Login + rate limiting

`POST /api/auth/login` (`src/app/api/auth/login/route.ts`):

- Derives the candidate token with PBKDF2 and **constant-time compares** it to
  the expected token — so each guess costs one PBKDF2 (there is no fast
  plaintext comparison).
- Is rate-limited (`src/lib/auth/login-rate-limit.ts`) with **two buckets**:
  - a **global** failed-attempt bucket — the real, unspoofable guarantee, and
  - a **best-effort per-client** bucket keyed on `X-Forwarded-For`. This is
    additive friction only; forwarded headers are not trusted as a security
    boundary on direct LAN/Tailscale access.
- Over the limit → `429` + `Retry-After` (JSON) or a `303` to `/login?error=rate`
  (native form post). Only **failed** attempts consume budget; a success resets
  that client's bucket.

The buckets live in memory in the Next.js process and reset on restart.

## Configuration

| Variable | Default | Purpose |
|---|---|---|
| `KB_PASSWORD` | _(empty)_ | Enable auth by setting it. Empty = no auth. |
| `CABINET_AUTH_SALT` | _(auto)_ | Per-install salt. Auto-generated into `.cabinet.env` on first run; set it only to pin a value. |
| `CABINET_LOGIN_PBKDF2_ITERS` | `600000` | KDF cost. Lower only for constrained hardware; below ~300000 is discouraged. |
| `CABINET_LOGIN_MAX_ATTEMPTS` | `10` | Failed attempts per client before lockout. |
| `CABINET_LOGIN_WINDOW_MS` | `900000` | Counting window (15 min). |
| `CABINET_LOGIN_LOCKOUT_MS` | `900000` | Lockout duration once tripped (15 min). |
| `CABINET_LOGIN_GLOBAL_MAX` | `60` | Global failed-attempt ceiling per window. |
| `KB_ALLOW_HTTP` | _(unset)_ | Set to `1` to drop the `Secure` cookie flag in production (e.g. plain-HTTP LAN). |

### The per-install salt

On first boot with this version, `src/instrumentation.ts` generates a random
`CABINET_AUTH_SALT` and stores it in `.cabinet.env` (atomic write, `0600`,
gitignored). It is read back into `process.env` on every boot. If generation
ever fails, the code falls back to a legacy fixed salt so the gate, login, and
check stay mutually consistent (just without per-install uniqueness).

`.cabinet.env` is editable from **Settings → Integrations**, where the salt
appears as a masked entry. Changing or clearing it forces a one-time re-login.

## Upgrading / migration

Switching from the old `SHA-256(password + "cabinet-salt")` scheme to PBKDF2
changes the token value, so **all existing `kb-auth` cookies become invalid** —
everyone (including you) re-logs-in once. The cookie name and attributes are
unchanged; there is no data migration.

## Threat model notes

- **Online brute force** (the practical risk, especially now that Cabinet can be
  reached over LAN / Tailscale / VPN) is stopped primarily by **rate limiting**.
- **PBKDF2 + per-install salt** is defense-in-depth: it slows *offline* password
  recovery if a cookie/verifier leaks. It does **not** revoke a leaked bearer
  cookie — rotating the password (or salt) invalidates all cookies.
- The single shared `KB_PASSWORD` model is unchanged: there are no per-user
  accounts, and login is not CSRF-tokened (login CSRF is not a meaningful
  escalation for a single shared secret).
- **Scheduler daemon:** the daemon's server-to-server calls (scheduled jobs +
  heartbeats) authenticate against this same gate by attaching the `kb-auth`
  cookie via `authCookieHeader()` from `src/lib/auth/kb-auth.ts` (PR #142). For
  the derived token to match, every input — `KB_PASSWORD`, `CABINET_AUTH_SALT`,
  and any `CABINET_LOGIN_PBKDF2_ITERS` override — must be visible in *both* the
  Next app and the daemon process. The salt lives in `.cabinet.env` (both load
  it at boot); the daemon also backfills these keys from `.env` for the
  production `start:daemon` path, which doesn't otherwise load `.env`.

## Testing it

Unit tests (run with `npm test`):

- `src/lib/auth/kb-auth.test.ts` — PBKDF2 against an independent `node:crypto`
  reference, iteration parsing, constant-time compare, memoization, and
  `authCookieHeader` (empty when auth is off, exact cookie when on).
- `src/lib/auth/login-rate-limit.test.ts` — lockout, success reset, global
  bucket tripping when client keys rotate.
- `test/proxy.test.ts`, `src/app/api/auth/login/route.test.ts` — gate behavior
  and the login form/JSON flows (including the 429 / `?error=rate` paths). Also
  an end-to-end guard that the daemon's `authCookieHeader()` cookie passes the
  real `proxy()` gate on an `/api/*` route.

Manual end-to-end:

```bash
# Start with auth on (low thresholds make the lockout quick to observe).
# Put these in .env, then `npm run dev:all`:
#   KB_PASSWORD=your-test-password
#   CABINET_LOGIN_MAX_ATTEMPTS=3
#   CABINET_LOGIN_LOCKOUT_MS=15000
```

1. A fresh `CABINET_AUTH_SALT` appears in `.cabinet.env` (and persists across restarts).
2. Visiting any page unauthenticated redirects to `/login`; `/api/*` returns `401`.
3. The correct password logs in (sets the `kb-auth` cookie) and the gate passes.
4. Several wrong passwords trip the lockout (`429` / `?error=rate` + `Retry-After`);
   the correct password is refused while locked, then works again after the lockout window.


### docs/PROVIDER-CLI.md

# Provider CLI Runtime

Date: 2026-04-18

Consolidated reference for Cabinet's multi-CLI provider system. Describes the adapter runtime, the eight built-in providers, shared utilities, plugin loader, session codec, in-UI verification, runtime picker, migration history, and outstanding work.

## 1. Goal

Cabinet executes agent work through interchangeable CLI providers. Each provider is a local binary the user installs and authenticates once. Cabinet spawns it headless, streams structured output into the transcript, persists session handles, and classifies failures in the UI.

Previous state: Claude + Codex hard-wired into a terminal-first execution model with heavy per-provider duplication.

Current state: eight built-in providers + a plugin loader for third-party adapters, a shared adapter interface, a reusable runtime picker driven entirely off provider metadata, and a standalone troubleshooting page that exercises every provider server API.

## 2. Built-in Providers

| Provider | Adapter type | Auth | Session resume | Effort levels | Billing |
|----------|--------------|------|----------------|---------------|---------|
| Claude Code (`claude-code`) | `claude_local` | Anthropic login / API key | ✅ (`--resume`) | none | subscription / api |
| Codex CLI (`codex-cli`) | `codex_local` | OpenAI login / API key | ✅ | low / medium / high | subscription / api |
| Gemini CLI (`gemini-cli`) | `gemini_local` | Google login / API key | ✅ | none | subscription / api |
| Cursor CLI (`cursor-cli`) | `cursor_local` | Cursor login | ✅ | none | subscription |
| OpenCode (`opencode`) | `opencode_local` | per-provider keys | ✅ | `minimal … max` via `--variant` | api (multi-provider) |
| Pi (`pi-cli`) | `pi_local` | per-provider keys | ✅ (file-based) | `off … xhigh` thinking levels | api |
| Grok CLI (`grok-cli`) | `grok_local` | xAI API key | ❌ | none | api |
| Copilot CLI (`copilot-cli`) | `copilot_local` | GitHub login | ❌ | none | subscription |

Provider metadata lives under `src/lib/agents/providers/<id>.ts` and is registered in `src/lib/agents/provider-registry.ts`. Every provider carries an `installSteps` array — the final step is always `Verify setup — Confirm headless mode works`, which the in-UI verifier runs.

## 3. Adapter Interface

`src/lib/agents/adapters/types.ts` defines `AgentExecutionAdapter`:

```ts
interface AgentExecutionAdapter {
  type: string;                 // e.g. "claude_local"
  name: string;
  providerId: string;
  executionEngine: "structured_cli" | "pty" | ...;
  supportsSessionResume: boolean;
  experimental?: boolean;

  execute(ctx: AdapterExecuteContext): Promise<AdapterExecuteResult>;
  testEnvironment?(): Promise<AdapterEnvironmentReport>;

  // Optional paperclip-style extensions
  sessionCodec?: AdapterSessionCodec;
  listModels?(): Promise<AgentAdapterModel[]>;
  listSkills?(ctx: { cwd?: string }): Promise<AdapterSkillSnapshot>;
  syncSkills?(ctx: { cwd?: string }, desired: string[]): Promise<AdapterSkillSnapshot>;
}

interface AdapterSessionCodec {
  deserialize(raw: unknown): Record<string, unknown> | null;
  serialize(params: Record<string, unknown>): Record<string, unknown> | null;
  getDisplayId?(params: Record<string, unknown>): string | null;
}
```

## 4. Shared Utilities

All adapters reuse the same building blocks (currently co-located in `src/lib/agents/adapters/`, to be extracted into `_shared/`):

- **Stream-JSON consumer** — line-by-line JSONL accumulator with typed event callbacks. Template: `claude-stream.ts` accumulator shape.
- **`runChildProcess`** — spawn wrapper used by every adapter: handles PATH (`ADAPTER_RUNTIME_PATH`), stdin piping, stdout/stderr chunking, timeouts, clean termination.
- **Stderr noise filters** — per-provider regex lists that drop CLI bootstrap chatter (OpenCode `sqlite-migration:*`, Gemini YOLO notices) so only real errors reach the user.
- **Session-codec pattern** — `{ sessionId, cwd }` shape (Cursor/Claude/Codex) or file-backed snapshot (Pi). On unknown-session error the runner retries with `clearSession: true`.
- **CLI arg builders** — effort → flag mappings (`--variant`, `--thinking`, `--reasoning-effort`) kept beside each adapter; all return arrays so call sites compose cleanly.

## 5. Plugin Loader

`src/lib/agents/adapters/plugin-loader.ts` loads third-party adapters at daemon boot:

- Config: `~/.cabinet/adapter-plugins.json`
  ```json
  { "plugins": [
    { "package": "@vendor/cabinet-adapter-x", "enabled": true },
    { "package": "./local/dir", "enabled": true, "path": "./local/dir" }
  ]}
  ```
- Dynamic `import()` + extracts `createAgentAdapter()` / `createServerAdapter()` / default / `adapter` export.
- Registers via `agentAdapterRegistry.registerExternal(adapter)`. A fallback map preserves the built-in so `unregisterExternal()` restores it when the plugin is disabled.
- `server/cabinet-daemon.ts` awaits the loader after `listen()` so the first conversation sees every registered adapter.

## 6. In-UI Verification

`src/app/api/agents/providers/[id]/verify/route.ts` exposes `POST /api/agents/providers/:id/verify`:

1. Resolves the provider's last install step with a `command`.
2. Runs it via `/bin/sh -c` with `PATH=ADAPTER_RUNTIME_PATH`, 60 s timeout, 16k char cap on stdout/stderr.
3. Classifies the result via keyword heuristics on combined stdout+stderr+spawn error:
   - `pass` — `exitCode === 0` and no error pattern matched
   - `not_installed` — ENOENT / `command not found` / `no such file`
   - `auth_required` — 401 / `not authenticated` / `missing api key` / `please log in` / `run … login`
   - `payment_required` — `payment required` / `subscription required` / `upgrade plan` / `billing required`
   - `quota_exceeded` — `quota exceeded` / `resource.*exhausted` / `rate-limit` / `too many requests`
   - `other_error` — anything else
4. Returns `{ status, failedStepTitle, command, exitCode, signal, output, stderr, durationMs, hint }`.

Consumed by:

- **Settings → Providers** (`src/components/settings/settings-page.tsx`) — per-provider verify button, status chip, failed-step highlighting, hint line.
- **Onboarding wizard** (`src/components/onboarding/onboarding-wizard.tsx`) — 4-column responsive grid sorted ready → installed-but-not-auth → not-installed, with a single install/verify drawer below the grid (not inline per card). Auto-selects the first ready provider and reuses `RuntimeSelectionBanner` above the model chips.
- **Providers Demo** (`/providers-demo`, see §6.1) — full test harness that hits every provider server API end-to-end.

Both onboarding + settings surfaces drive their install steps off `provider.installSteps` (via `buildProviderSetupSteps`) — no hardcoded per-provider content.

Unified verify command per provider (matches the adapter's exact invocation so "works in terminal" implies "works in Cabinet"):

- **Claude Code** — `claude -p 'Reply with exactly OK' --output-format text`
- **Codex CLI** — `codex exec --skip-git-repo-check --dangerously-bypass-approvals-and-sandbox 'Reply with exactly OK'`
- **Gemini CLI** — `gemini -p 'Reply with exactly OK' --yolo`
- **Cursor CLI** — `cursor-agent -p 'Reply with exactly OK' --output-format text --yolo`
- **OpenCode** — `opencode run 'Reply with exactly OK'`
- **Pi** — `pi --mode json -p 'Reply with exactly OK'`
- **Grok CLI** — `grok -p 'Reply with exactly OK'`
- **Copilot CLI** — `copilot -p 'Reply with exactly OK' --allow-all-tools`

OpenCode & Pi are multi-provider routers, so their verify is **model-aware** (`AgentProvider.buildVerifyCommand(defaultModel)`, see §11 #23): when that provider is the *configured default*, the verifier injects `--model <Cabinet default model>` so "verify passed" means the user's actual path works, not the CLI's opaque internal default. Other six providers ignore the hook → install-step command unchanged.

### 6.1 Providers Demo page

`/providers-demo` (`src/app/providers-demo/page.tsx`) is a standalone troubleshooting harness. Linked from Settings → Providers via a **Troubleshoot AI providers** button (Stethoscope icon) that opens it in a new tab. Inherits the app's theme tokens so it renders in whichever theme the user picked.

What it exercises in one view:

- `GET /api/agents/providers` — populates the provider cards + summary bar (provider count, ready count, default provider/model/effort).
- `GET /api/agents/providers/status` — separate button; renders the cached `{ available, authenticated }` mini-grid.
- `POST /api/agents/providers/:id/verify` — per-card Verify button with inline result (status pill, exit code, duration, failed-step label, hint, collapsible command + stdout + stderr).
- `POST /api/agents/headless` — per-card Send prompt button; shared prompt textarea with `{{provider}}` templating replaced against the provider's display name. Disabled when the provider isn't ready.

UX details:

- Scrolling **API call log** at the bottom records every fetch (method, URL, status, duration, timestamp) with expandable request/response JSON.
- Model + effort selectors are rendered for reference; `/api/agents/headless` currently uses each provider's default model, noted inline.
- Log cap: 100 entries (FIFO). Clear button resets.

## 7. Runtime Picker (shared component)

`src/components/composer/task-runtime-picker.tsx` exports two reusable pieces:

```tsx
export function RuntimeSelectionBanner({
  providers, value, label, trailing, className,
});

export function RuntimeMatrixPicker({
  providers,
  value: { providerId, model, effort },
  onChange,
  includeUnavailable = false,      // true for Settings, false for composer
});
```

Behavior:

- **Ready-first ordering** — `ready.push(p); unready.push(p); return [...ready, ...unready]`. `isProviderReady = enabled && available && authenticated`.
- **Unready tabs** — rendered with `opacity-50 grayscale`, `disabled` prop, a "Not ready" chip, and a hint (`describeProviderUnreadyReason`) pulled from whichever of `enabled` / `available` / `authenticated` is failing.
- **Horizontal scroll** — `overflow-x-auto scrollbar-none` + `w-max min-w-full` so 8+ tabs don't clip in a narrow column.
- **Banner** — colored `Default Model: (icon)(provider)(model)` strip tied to the provider's own `iconAsset` + theme accent; shared between composer and Settings.

Settings replaced three hand-rolled blocks (provider buttons + model grid + effort grid) with a single `<RuntimeMatrixPicker includeUnavailable />` + `<RuntimeSelectionBanner />`.

## 8. Glyphs & Icons

- Every provider declares `iconAsset: "/providers/<slug>.svg"` on its metadata.
- `src/components/agents/provider-glyph.tsx` takes an `asset` prop and falls back to a lookup map for compatibility; the hardcoded icon map was removed in favor of provider-driven lookup.
- Placeholder SVG monograms shipped for cursor / opencode / pi / grok / copilot under `public/providers/`.

## 9. Tests

- `src/lib/agents/adapters/registry.test.ts` — asserts all 10 adapter types register and the 8 provider→adapter defaults map correctly.
- `src/lib/agents/adapters/{cursor-local,opencode-local,pi-local}.test.ts` — exercise stream-parsing, effort flag mapping, stderr noise filtering, and session-codec round-trip against fake shell scripts that emit real stream-json.
- Existing Claude / Codex / Gemini adapter tests untouched (behavior-neutral refactor for them).
- `test/opencode-models-parse.test.ts` + `test/pi-models-parse.test.ts` — pure `parse<Provider>Models` units: vendor/model parsing, blank/comment/noise stripping, and the empty-or-banner-only → offline-fallback guard (never a blank picker). `test/runtime-options-dynamic-models.test.ts` — `resolveProviderModel` hydration guard (un-hydrated dynamic provider preserves an unknown saved id; hydrated/non-dynamic keep legacy snap-to-`models[0]`). Run via `npm test` (root `test/*.test.ts`).

## 10. Files Map

```
src/lib/agents/
  provider-interface.ts                     // AgentProvider + iconAsset field
  provider-registry.ts                      // registers all 8 providers
  providers/
    claude-code.ts  codex-cli.ts  gemini-cli.ts
    cursor-cli.ts   opencode.ts   pi.ts    grok-cli.ts   copilot-cli.ts
  adapters/
    types.ts                                // adapter interface + session codec
    registry.ts                             // built-in + registerExternal fallback
    plugin-loader.ts                        // ~/.cabinet/adapter-plugins.json
    claude-local.ts + claude-stream.ts
    codex-local.ts  + codex-stream.ts
    gemini-local.ts + gemini-stream.ts
    cursor-local.ts + cursor-stream.ts
    opencode-local.ts + opencode-stream.ts
    pi-local.ts + pi-stream.ts
    grok-local.ts
    copilot-local.ts
src/app/
  api/agents/providers/route.ts             // GET list + PUT settings
  api/agents/providers/status/route.ts      // GET { available, authenticated } cache (30s)
  api/agents/providers/[id]/verify/route.ts // POST verify + classify
  api/agents/headless/route.ts              // POST one-shot prompt
  providers-demo/page.tsx                   // troubleshooting harness
src/components/
  composer/task-runtime-picker.tsx          // RuntimeMatrixPicker + Banner
  settings/settings-page.tsx                // runtime picker + Troubleshoot link
  onboarding/onboarding-wizard.tsx          // 4-col grid + verify drawer
  onboarding/home-blueprint-background.tsx  // animated floorplan on Welcome home
  agents/provider-glyph.tsx                 // asset-driven glyph
  agents/conversation-{content-viewer,live-view,session-view}.tsx
public/providers/{claude,codex,gemini,cursor,opencode,pi,grok,copilot}.svg
server/cabinet-daemon.ts                    // awaits plugin loader at boot
```

## 11. Migration History

Phased work that landed on this branch (see commit trail below):

1. **Adapter foundation** — shared adapter system under `src/lib/agents/adapters/`, threading `adapterType` / `adapterConfig` / execution engine through personas, jobs, conversations, and daemon sessions.
2. **Structured adapters for Claude / Codex / Gemini** — stream-json parsing instead of raw PTY replay; structured usage + session metadata flow into transcripts natively.
3. **Daemon runtime generalization** — `server/cabinet-daemon.ts` manages both legacy PTY and structured adapter-backed sessions, writing into the same conversation store.
4. **Provider + adapter selection UI** — providers API exposes adapter metadata; runtime-selection helpers surface defaults, available adapters, and override semantics across agent settings / creation / job editors / mission control.
5. **Terminal mode promoted to first-class** — the `*_legacy` PTY adapters (named that way for historical reasons) power the user-selectable **Terminal** mode in the task composer; `WebTerminal` is the interactive surface for these sessions.
6. **Native live-session UI** — replaced task live-rendering that previously depended on `WebTerminal`. Shared renderer across `task-detail-panel`, `jobs-manager`, `agents-workspace`.
7. **Shared task composer** — per-task runtime overrides + compact runtime picker (brain-icon trigger) unified across task board, home screen, agents workspace, AI panel, and status-bar entry points.
8. **Runtime picker consolidation** — provider tabs / model rows / effort columns matrix with a selected-model summary row.
9. **Paperclip-style adapter shape** — three new providers (Cursor / OpenCode / Pi) added using CLI-spawn + stream-json + session-codec pattern, consistent with Claude / Codex / Gemini.
10. **Session codec groundwork** — optional `AdapterSessionCodec` on the adapter interface; each new adapter ships its own codec. Per-conversation persistence is the Round B item.
11. **External adapter plugin loader** — `~/.cabinet/adapter-plugins.json`, dynamic `import()`, `registerExternal` + fallback preservation.
12. **Provider branding** — `iconAsset` field + local SVG assets for all providers; `ProviderGlyph` shared component.
13. **Settings guide generalization** — hardcoded per-provider setup map replaced with `buildProviderSetupSteps(provider.installSteps)`.
14. **Unified headless verify step** — every provider's install guide ends with the same "Reply with exactly OK" one-shot that matches the adapter's exact invocation.
15. **Runtime picker layout for 6+ providers** — horizontal scroll on tab row + relaxed width constraint; Cursor renamed to "Cursor CLI" for tab balance.
16. **Grok CLI + Copilot CLI providers** — plain-stdout passthrough (no stream-json), subscription/api billing, ship monogram SVGs + registry entries.
17. **Adapter tests** — stream-parsing + session-codec round-trip tests for Cursor / OpenCode / Pi; registry test asserts all 10 adapter types + 8 provider defaults.
18. **Onboarding redesign (2026-04-18)** — 4-col responsive card grid sorted ready-first, single install/verify drawer below the grid, `RuntimeSelectionBanner` above model chips. Fixed refetch-on-select bug (`checkProvider` deps). Welcome home step gained `HomeBlueprintBackground` — animated SVG floor plan with 8 rooms + wandering agent dots, respects `prefers-reduced-motion`.
19. **Providers Demo page (2026-04-18)** — `/providers-demo` exercises every provider server API; API call log with expandable bodies; "Troubleshoot AI providers" button added to Settings → Providers.
20. **Terminal mode across all 8 providers (2026-04-19, round 1)** — registered `<provider>_legacy` PTY adapters for every provider (was Claude + Codex only). Runtime picker gains a Native/Terminal toggle above the provider tabs; Terminal mode swaps the picker to a dark chrome, hides model + effort controls (PTY uses the CLI's own defaults), and tags the selection banner with a `PTY` pill + terminal glyph. `ConversationRuntimeOverride` gains `runtimeMode: "native" | "terminal"`; POST `/api/agents/conversations` translates `runtimeMode === "terminal"` into the provider's legacy adapter type via `LEGACY_ADAPTER_BY_PROVIDER_ID`. Normalization + sameSelection preserve `runtimeMode` so the picker latches.
21. **Terminal-mode task viewer (2026-04-19, round 2)** — when `isLegacyAdapterType(meta.adapterType)`, the task's Chat tab swaps from the markdown TurnBlock list to a real xterm-backed `WebTerminal` (previously the PTY's raw TUI was being rendered as scrambled markdown). A fixed `TerminalPromptHeader` sits above the terminal with the original prompt, a copy button, provider chip, live-status pill, and PTY badge. When the task is idle, the composer renders below in a dark theme with `runtimeMode: "terminal"` pinned in the initial runtime so Continue routes back through the legacy adapter via `continueConversationRun`. Icon markers added on: task board cards (left emerald rail + `PTY` chip), task detail header (`PTY` chip next to title), and sidebar recent tasks (small terminal glyph at trailing edge). Finished status is deduced naturally from `meta.status === "idle"` when the daemon closes the PTY. Known limitation: each continuation spawns a fresh PTY process; the xterm buffer (scrollback) is preserved in the browser but the underlying CLI process restarts per turn.

22. **OpenCode dynamic model discovery wired end-to-end (2026-05-16)** — closes the §12.1 #3 phantom and the recurring Discord reports ("I use OpenCode with Minimax/GLM/Kimi but Cabinet only shows OpenAI/Anthropic/Google/XAI"). Root cause was two coupled bugs: (a) the `listModels()` endpoint shipped in `0587bec` had **zero frontend consumers** — the picker only ever read the static `OPENCODE_FALLBACK_MODELS`; (b) `resolveProviderModel` resolved solely against that static list, so even a saved `opencode/minimax-*` default was silently snapped to `models[0]` by `normalizeSelection` on every render. Fix: providers API advertises `dynamicModels: typeof p.listModels === "function"` (capability flag, not a hardcoded id — honors §13); new app-store `ensureProviderModels(id, {refresh?})` action lazily fetches + merges the real list (deduped, sets `modelsHydrated`); `GET …/models?refresh=1` busts the 60s cache for the "just added my API key" case; `resolveProviderModel` preserves an unknown requested/fallback id as a synthetic entry while a dynamic provider is un-hydrated (prevents the clobber); a searchable, sub-provider-grouped `ProviderModelCombobox` (own fetch for display so it works on store-backed *and* local-state surfaces) replaces the fixed matrix for `dynamicModels` providers, with an effort row + refresh button. `opencode models` is **entitlement-gated** (authed providers' full lists + the always-on OpenCode Zen free subset; verified live = 97 ids = `{opencode:5, google:38, openai:54}` against `OPENAI_API_KEY`+`GEMINI_API_KEY`), so the list users see is their *runnable* set, mirroring OpenCode's own picker. The fix is **capability-driven, not OpenCode-specific**: every surface keys off `provider.dynamicModels` (= the provider implements `listModels()`), so the combobox + hydration + resolver-guard light up for *any* such provider, present or future. Audited all 8 — exactly two implement the hook (`opencode`, `pi`), and both are now fully fixed end-to-end (live API confirms `dynamicModels:true` for both, `false` for the other six). **Pi was not "fixed for free" — it had the identical latent parser bug** (`pi --list-models` output that is non-empty but all-`#`-banner returned `[]` → blank picker) and got the *same* hardening: pure `parsePiModels` with the empty→fallback guard + 15s timeout, mirroring `parseOpenCodeModels`. Pure parsers extracted for both; tests: `test/opencode-models-parse.test.ts` + `test/pi-models-parse.test.ts` (parse / noise / banner-only / empty → fallback, never blank) + `test/runtime-options-dynamic-models.test.ts` (hydration-guard matrix) — 16/16. Grok/Copilot/Claude/Codex/Gemini/Cursor unaffected (no hook → curated static matrix unchanged, which is correct for their small fixed model sets).

23. **OpenCode seamless-integration follow-up — A + C + B (2026-05-16)** — three remaining lifecycle seams after #22, all capability-driven (OpenCode + Pi; six others untouched). **(A) Honest readiness.** `opencode.ts` healthCheck previously returned `authenticated:true` on any `opencode --version` success regardless of provider keys → fresh installs showed a confident "Ready". Now parses `opencode auth list` (pure `parseOpenCodeAuth`, ANSI-stripped) and makes the status *text* honest — `OpenCode 1.4.7 · 2 providers configured` vs `· no provider keys — Zen free models only` — while deliberately keeping `authenticated:true` (Zen `-free` models run with no key; flipping it would *hide* OpenCode from the composer, a worse regression). **(C) Offline truthfulness.** `listModels()` now throws on a genuine CLI failure instead of swallowing to fallback, so the models route's `dynamic` flag is honest; `dynamic` is returned on cache hits too; the app-store only sets `modelsHydrated` when `dynamic:true` (a transient offline fallback no longer lets `resolveProviderModel` snap a saved id); the combobox shows an amber "showing offline defaults — configure + Refresh" hint when `dynamic:false`. **(B) Trustworthy verify.** New optional `AgentProvider.buildVerifyCommand(defaultModel)`; the verify route injects the Cabinet default model **only when that provider is the configured default**, so "verify passed" validates the user's real path, not the CLI's internal default. Pure parsers/builders + tests: `opencode-auth-parse` + `provider-verify-command` (+ existing model-parse/resolver) — 26/26. Lint/tsc clean (no new issues).

### Commit trail (selected)

- `7cd6c31` scaffold adapter foundation
- `3e30f5a` thread adapter metadata through daemon sessions
- `5aa39a5` run claude through structured adapter sessions
- `0a9e52c` run codex through structured adapter sessions
- `5428af5` expose adapter selection in agent settings
- `1e0f1a3` expose adapter selection in mission control dialogs
- `85fa8d9` replace task live terminal with native view
- `2357097` share native live conversation view
- `88de2b1` 5 CLI providers + in-UI verification + shared runtime picker
- `89a3cc4` animated home blueprint + redesigned provider step + study default
- `19980e0` /providers-demo page + Troubleshoot button in Settings

## 12. Next Steps

### 12.0 TL;DR — what's actually left

Consolidated list of unclosed items. Everything not listed here is shipped (see detailed matrices in §12.1 / §12.2 / §12.3).

#### A. Needs code — mechanical, no decisions required

| Ref | Item | Notes |
|---|---|---|
| #2b | Skills injection for the other 6 providers — extend `adapterConfig.skillsDir` wiring to Cursor, OpenCode, Pi, Codex, Gemini, Grok, Copilot | Claude is done via `--add-dir`. Each CLI has its own context-dir flag (Cursor `--add-dir` too, OpenCode env var, Pi env var, Codex `-c`, Gemini ?, Grok/Copilot likely none). |
| #4 | Full per-provider directory split — `adapters/<provider>-local/{index,execute,parse,test,skills}.ts` + extract remaining shared helpers into `_shared/` (stream-json consumer, stderr-filter, session-codec, health-check) | Phase 1 shipped (`_shared/cli-args.ts`). Behavior-neutral churn; low ROI. |
| #5 | `agent-live-panel.tsx` should not render `WebTerminal` for structured-adapter conversations | WebTerminal works fine for both today; this is cleanup, not a bug. |

#### B. Needs product decision

| Ref | Item | Decision needed |
|---|---|---|
| #9 | Reasoning-effort policy per provider | How far to push effort controls — Cursor has none, OpenCode/Pi have per-variant levels, Codex has low/medium/high, Claude/Gemini/Grok/Copilot have none. Which providers should expose effort at all in UI? |

#### C. Needs external input

| Ref | Item | Blocked on |
|---|---|---|
| #11 | Polish placeholder glyphs for Cursor/OpenCode/Pi/Grok/Copilot | Licensed artwork |

#### D. Known limitations (out-of-scope by design)

| Ref | Item | Why out of scope |
|---|---|---|
| T19-full | Distill PTY output into a clean agent turn with artifact extraction + `<ask_user>` detection | Terminal mode is "I drive the CLI"; structured summary/artifacts belong to native mode. Current distillation is a 1-line deterministic summary. |
| T20-repl | Same-process continue keeping an interactive REPL alive across turns with a persistent read-eval loop | Current impl opportunistically stdin-injects when the PTY is alive, spawns fresh otherwise. True always-alive REPL would need a launch-mode refactor and only benefits providers with REPL mode. |

#### Product guarantees now in place

Worth calling out since these used to be caveats:

- **Terminal-mode Continue always preserves context** (shipped T25 `847c6e0` + `8ca5eb9`). Native resume via `--resume` / `--session` for Claude/Cursor/OpenCode; prompt-level replay via `buildContinuationPrompt({ mode: "replay" })` for Codex/Gemini/Grok/Copilot/Pi. No path loses the prior conversation.
- **Refresh a finished terminal task → transcript is always shown** (shipped T21 `80f2a44`). Three-tier fallback: live session → `completedOutput` cache → on-disk transcript → empty-state marker. The old silent-new-CLI bug is gone.
- **Skills are an end-to-end surface** (shipped §12.3 UI-1..4 + backend). Catalog at `~/.cabinet/skills/`, per-agent selection via persona frontmatter or the Details multiselect, Task-header chip shows what's attached, Settings → Skills lists the catalog, Claude adapter injects via `--add-dir`.

**Snapshot:**
- Provider track (§12.1): 9 / 12 shipped (3 partial).
- Terminal track (§12.2): 25 / 25 resolved.
- Skills UI (§12.3): 4 / 4 shipped.
- Unclosed items above: **6** (3 mechanical code + 1 product call + 1 artwork + 2 by-design limitations).

### 12.1 Status matrix

| # | Item | Status | Commit(s) |
|---|------|--------|-----------|
| 1 | Session codec persistence per conversation | ✅ Already shipped — `writeSession(conversationId, { codecBlob, resumeId, … })` + `deserialize(session.codecBlob)` on continuation | — |
| 2 | Skills injection — catalog at `~/.cabinet/skills/<slug>/SKILL.md`; `_shared/skills-injection.ts` exposes `readSkillCatalog` + `syncSkillsToTmpdir` (symlinks selected skills into `$TMPDIR/cabinet-skills/<sessionId>/`); persona frontmatter gains `skills: [slug, …]`; runner injects `skillsDir` into adapterConfig before spawn; Claude adapter wires it via `--add-dir`. Other 7 adapters ignore the field as no-ops until each CLI's skills contract is wired. | 🟡 Partial | `77c17af` |
| 3 | Dynamic model discovery (OpenCode / Pi) | ✅ Done — **was a phantom**: `0587bec` shipped the `listModels()` hook + `GET /api/agents/providers/:id/models` endpoint but **no frontend ever called it** — the picker rendered the static `OPENCODE_FALLBACK_MODELS` (openai/anthropic/google/xai), so users with Minimax/GLM/Kimi/Zen saw the wrong 7. Now actually wired (see §11 #22): provider advertises `dynamicModels`; app-store `ensureProviderModels` lazily hydrates the real entitlement-gated list (`opencode models` ≈ authed providers + Zen free subset); `resolveProviderModel` preserves an unknown saved id while un-hydrated so `normalizeSelection` can't clobber it; searchable grouped combobox replaces the matrix for dynamic providers. Capability-driven (`provider.dynamicModels`), so it covers any current/future `listModels` provider. Audited all 8 — only `opencode` + `pi` have the hook; **both fully fixed incl. the same `parse<Provider>Models` empty→fallback hardening + tests (16/16)** — Pi had the identical latent blank-picker bug, not a free ride. | `0587bec` + §11 #22 |
| 4 | Per-provider directory refactor (paperclip shape) — Phase 1: `_shared/cli-args.ts` extracted (`readStringConfig` + `readEffortConfig`), all 8 adapters consume from there instead of duplicating. Full per-provider directory split (`<provider>-local/{index,execute,parse,test,skills}.ts`) still deferred as low-ROI mechanical churn | 🟡 Partial | `98c757d` |
| 5 | Stop rendering WebTerminal in `agent-live-panel.tsx` for structured adapters | 🟨 Deferred — minor; PTY now has its own mode | — |
| 6 | Label legacy PTY adapters as experimental | ✅ Superseded — promoted to first-class **terminal mode** via Native/Terminal toggle | `a767892`, `e922c63` |
| 7 | Integration coverage for adapter lifecycle | ✅ Done — registry test covers 16 adapters + `legacy-ids.test.ts` asserts client/server sync | `656526d` |
| 8 | Reduce "provider = PTY CLI" assumptions — centralize the `type === "cli"` UX filter into `isAgentProviderSelectable()` so one predicate change lights up API providers across onboarding / settings / agents-workspace / providers-demo | ✅ Done | `1e0edbd` |
| 9 | Reasoning-effort policy per provider | 🟨 Deferred — product call | — |
| 10 | Model + effort on `/api/agents/headless` | ✅ Done for Claude + Codex — endpoint + `OneShotInvocationOptions` | `979d87a` |
| 10b | Model-override for the other 6 providers — Gemini (`-m`), Cursor/Grok/Copilot (`--model`), OpenCode (`--model` + `--variant`), Pi (`--model` + `--thinking`) | ✅ Done | `db351ac` |
| 11 | Polish placeholder glyphs | 🟨 Deferred — needs licensed artwork | — |
| 12 | Daemon-level PTY keep-alive (same-process continue) — daemon `POST /session/:id/input` writes stdin to live PTY; `continueConversationRun` legacy branch tries `writeDaemonSessionInput()` first, falls back to `createDaemonSession` if exited | ✅ Done | `5aebc4c` |

### 12.2 Terminal-streamed tasks — status matrix

Separate track covering the "user runs task in Terminal mode" experience. Audit and roadmap.

| # | Item | Status | Commit(s) |
|---|------|--------|-----------|
| T1 | Register legacy `<provider>_legacy` PTY adapters for all 8 providers | ✅ Done | `a767892` |
| T2 | `RuntimeMatrixValue.runtimeMode: "native" \| "terminal"` | ✅ Done | `a767892` |
| T3 | Native/Terminal toggle in the runtime picker (dark chrome, hides model/effort) | ✅ Done | `a767892` |
| T4 | `normalizeSelection` + `sameSelection` preserve `runtimeMode` (toggle latches) | ✅ Done | `e922c63` |
| T5 | POST `/api/agents/conversations` translates `runtimeMode === "terminal"` → `LEGACY_ADAPTER_BY_PROVIDER_ID[providerId]` | ✅ Done | `a767892` |
| T6 | POST `/api/agents/conversations/[id]/continue` same translation for continuations | ✅ Done | `745c655` |
| T7 | `task-client.ts` (`postTurn`, `createTaskRequest`) forward `runtimeMode` in payload | ✅ Done | `745c655` |
| T8 | Task viewer swaps Chat tab → `WebTerminal` when `isLegacyAdapterType(adapterType)` | ✅ Done | `c3a3f84` |
| T9 | Fixed `TerminalPromptHeader` (prompt, copy, provider chip, PTY badge, status pill) | ✅ Done (now folded into fullscreen top strip) | `c3a3f84`, `4313979` |
| T10 | Continue flow — composer appears when PTY exits, `runtimeMode: "terminal"` pinned | ✅ Done | `dc6aec1` |
| T11 | Client-safe `legacy-ids.ts` module (fixes `child_process` client-bundle error) | ✅ Done | `b0230c5` |
| T12 | Composer banner (emerald strip) when terminal mode is selected | ✅ Done | `9310067` |
| T13 | Task card marker: left emerald rail + `PTY` chip on tasks board | ✅ Done | `5e8ac62` |
| T14 | Task detail header: `PTY` chip next to title | ✅ Done (legacy view) | `5e8ac62` |
| T15 | Sidebar recent tasks: trailing terminal glyph | ✅ Done | `5e8ac62` |
| T16 | Fullscreen terminal layout (thin dark top strip + WebTerminal fills viewport) | ✅ Done | `4313979` |
| T17 | Running indicator = terminal-icon chip with pulsing ring when live (replaces separate "live" + "PTY" chips) | ✅ Done | `89f5b2a` |
| T18 | Legacy-adapter continuation — `continueConversationRun` reopens the PTY via `createDaemonSession` instead of bailing on the missing `adapter.execute` | ✅ Done | `a012478` |
| T19 | Distill PTY output on exit — `finalizeSessionConversation` now emits a deterministic summary (`Terminal <provider> session <status> · N lines[ — last output: …]`) for legacy_pty_cli sessions so `meta.summary` isn't box-drawing junk. Raw transcript on disk untouched; artifact extraction + `<ask_user>` detection explicitly skipped for PTY mode (out of scope — terminal mode is "I drive the CLI") | ✅ Done | `98c757d` |
| T20 | Same-process continue (keep CLI alive across turns, inject prompts via stdin) — daemon `POST /session/:id/input`; runner probes liveness first, writes to stdin if alive, spawns fresh PTY only on fallback | ✅ Done | `5aebc4c` |
| T21 | WebTerminal reconnect-after-navigate-away UX — covers both live reconnect (in-memory session replay via `attachSessionSocket`) and refresh of an already-finished task (WebTerminal passes `reconnect=1`; daemon serves transcript from `completedOutput` cache → on-disk transcript → empty-state marker, never spawns a new PTY). Replay prefixed with a provenance banner (`[cabinet] <providerId> · <adapterType> · started X · finished Y`) + clear-screen so xterm renders from the top instead of auto-scrolling to the transcript tail. Fixes the silent-new-CLI bug where refreshing a finished task re-ran the prompt, and the Claude-banner-at-tail confusion where xterm landed on stale output from pre-T21 spawn paths. | ✅ Done | `80f2a44`, `090d5ba` |
| T25 | Terminal-mode Continue uses provider-native resume OR prompt-level replay — two recovery paths after PTY exit: (a) native resume via `--resume` / `--session` for Claude / Cursor / OpenCode when the previous run captured a provider session id; (b) `buildContinuationPrompt({ mode: "replay" })` prepends the prior turns to the new user message for providers without resume (Codex / Gemini / Grok / Copilot / Pi) or when capture was missed. Both paths preserve context; only native resume is "free" (no extra input tokens). Runner threads `adapterSessionId` into `createDaemonSession`; the daemon forwards via `OneShotInvocationOptions.resumeId` / `SessionInvocationOptions.resumeId`. UI composer shows "resumes in the same <provider> session" for native; "Cabinet will prepend the prior transcript so the new run still has context" for replay. | ✅ Done | `847c6e0`, `8ca5eb9` |
| T22 | Token bar / context window hidden in terminal fullscreen layout | ✅ Done — fullscreen top strip already omits `TokenBar` (PTY output doesn't self-report usage uniformly) | `4313979` |
| T23 | Stop-PTY button in the top strip — calls `stopConversation()` → PATCH `{ action: "stop" }` → daemon SIGTERMs the PTY | ✅ Done | `a012478` |
| T24 | Terminal-mode "experimental" advisory vs. first-class messaging | ✅ First-class — Native/Terminal is a positive product choice, not a warning |
| T26 | Terminal / Details tab toggle in the fullscreen task viewer — two tabs at the very top: Terminal (xterm stream, default) and Details (renders `ConversationResultView` cards: PROMPT + RESULT + ARTIFACTS). Details body lives on a light theme-matched panel with a compact back-row header. Detail lazy-fetched on first click via `/api/agents/conversations/:id`, cached, refetched on task status/lastActivity change. Artifacts click through to the editor via `openArtifactPath()`. Tab row uses the same `rounded-t-md` + `-mb-px` seam pattern as the runtime picker. Details tab shows artifact count as an emerald chip when present. | ✅ Done | `fa1e5e4` |

### 12.3 Skills UI — status matrix

The skills system shipped with zero UI (see §12.1 #2). Track the four surfaces that would make skills visible:

| # | Item | Status | Commit |
|---|------|--------|--------|
| UI-1 | Agent detail → Skills field in Details section (superseded by UI-4) | ✅ Done | `63d3499`, `6a070fc` |
| UI-2 | Settings → "Skills catalog" browser — lists everything in `~/.cabinet/skills/` with name + description + path | ✅ Done (coming-soon preview) | `40c2865` |
| UI-3 | Task viewer → violet `Sparkles` chip "N skills" (single slug for N=1) in the header when `adapterConfig.skills` is populated; full list on hover | ✅ Done | `63d3499` |
| UI-4 | Agent editor → skills multiselect widget backed by the catalog — toggleable pills per entry, orphan-slug detection, replace-semantics save via PUT `/api/agents/personas/:slug { skills }` | ✅ Done | `6a070fc` |

Current UX: users edit `skills: [slug, slug]` directly in the agent's markdown frontmatter.

### 12.4 Runtime picker UX polish

| # | Item | Status | Commit |
|---|------|--------|--------|
| UX-1 | EFFORT_TONES table: dark-mode variants on every tone (header text, bg fills, borders, selected shadow) so the `SELECTED MODEL` banner + matrix chips read correctly against dark themes | ✅ Done | `2981581` |
| UX-2 | Terminal mode: replace the Tabs + matrix with a dedicated `TerminalProviderPanel` (dark card, header "Pick a CLI to spawn in a PTY:", 2-3 col grid of CLI cards with glyph + name + ready/log-in/not-installed status, footer noting model/effort defaults + resume-capable providers). Click a ready card = select it with an emerald highlight. | ✅ Done | `2981581` |
| UX-3 | Composer collapsed trigger button indicates terminal mode — `>_` terminal glyph in an emerald-bordered dark zinc container, trailing "Terminal" label in emerald uppercase (replacing the effort label since PTY uses CLI defaults). Whole button: dark zinc bg + emerald/40 border. | ✅ Done | `09c87a2` |
| UX-4 | Native-mode provider tabs collapse to icon-only when inactive. Active tab widens to icon + name (+ "Not ready" chip when unready); inactive tabs render just the ProviderGlyph with tooltip. Fits all 8 providers without horizontal scroll. | ✅ Done | `09c87a2` |
| UX-5 | Native/Terminal rendered as true **tabs** (not buttons) — 50/50 `grid-cols-2` with `px-2 pt-2` margin, each tab is `rounded-t-md` with `border-t/l/r`, `-mb-px` merges the active tab's bottom edge into the panel below. Active tab bg matches its panel (background for Native, zinc-950 + emerald-ring for Terminal) so the seam disappears. Inactive tabs get muted bg + transparent border. | ✅ Done | `542de01`, `ecdad67` |
| UX-6 | Terminal panel footer carries the EXPERIMENTAL + HACKER MODE framing (not the tab label). Three-paragraph notice: red `EXPERIMENTAL` + emerald `HACKER MODE` pills lead the trade-off copy ("Great if you want to watch the CLI talk to itself; less great if you want Cabinet to organize the output"), then the model/effort + resume wiring note, then the Discord CTA. Tab label itself is clean (just icon + "Terminal"). | ✅ Done | `542de01`, `ecdad67` |

## 13. Operational Notes

### Adding a new provider

The full file map is in §10. Minimum touch-list:

**New files**
- `src/lib/agents/providers/<id>.ts` — provider metadata. Must declare `iconAsset: "/providers/<id>.svg"` (§8) so the glyph picks it up without further wiring.
- `src/lib/agents/adapters/<id>-local.ts` — adapter implementation.
- `src/lib/agents/adapters/<id>-stream.ts` — only if the CLI emits structured streaming output (NDJSON / stream-json).
- `public/providers/<id>.svg` — logo asset.
- `src/lib/agents/adapters/<id>-local.test.ts` (+ `<id>-stream.test.ts` and `test/fixtures/<id>-stream/*.ndjson` for streaming providers).

**Edits**
- `src/lib/agents/provider-registry.ts` — import + `providerRegistry.register(...)`.
- `src/lib/agents/adapters/registry.ts` — four spots: `LEGACY_ADAPTER_BY_PROVIDER_ID`, `DEFAULT_ADAPTER_BY_PROVIDER_ID`, legacy adapter factory, `register()` call.
- `src/lib/agents/adapters/legacy-ids.ts` — add `<id>_legacy` to `LEGACY_ADAPTER_TYPES`. Plus add the provider id to `PROVIDERS_WITH_TERMINAL_RESUME` if the CLI supports `--resume` / `--session` (gates the "new session" advisory in the task viewer).
- `src/components/layout/status-bar.tsx` — `PROVIDER_INSTALL_URLS` (powers the "Install" button in the System Status popover).
- `test/provider-launch-mode.test.ts` — launch-mode case.
- `src/lib/agents/adapters/registry.test.ts` — adapter presence assertion.

**Install-step contract:** the final entry of `installSteps` must be a `Verify setup` command that exits 0 on success. The in-UI verifier (§6) runs it as the canonical health check.

**Do NOT add the new id to component-level lists.** The Settings page, composer picker (Native + Terminal tabs), onboarding grid, providers-demo, and troubleshooter all read `/api/agents/providers` and discover the provider via `iconAsset`, `runtimeModes`, and `supportsTerminalResume` flags on its metadata. If you find yourself editing `task-runtime-picker.tsx`, `settings-page.tsx`, or `onboarding-wizard.tsx` to enumerate providers, that's a smell.

**Dynamic model discovery (optional, capability-driven).** If the CLI exposes a per-machine / entitlement-gated model list (like `opencode models` or `pi --list-models`) rather than a small fixed set, implement `listModels()` on the provider metadata. That single hook is the whole contract: `/api/agents/providers` auto-advertises `dynamicModels: true`, and the app-store hydration + searchable grouped combobox + `resolveProviderModel` un-hydrated-id guard all light up with **zero component edits** (see §11 #22). The static `models` array stays as the offline fallback. Ship a *pure* `parse<Provider>Models(stdout)` that (a) drops CLI chrome/noise and (b) returns the fallback — never `[]` — on empty or banner-only output (the blank-picker trap that bit both opencode and pi), plus a `test/<provider>-models-parse.test.ts` mirroring the existing two. Do **not** hand-wire the provider id anywhere in the picker.

### Other notes

- **Unready providers** stay visible in Settings (`includeUnavailable`) but are hidden in the composer picker by default. Users can always see what's available vs. installable from Settings.
- **Verify failures** surface the failing step title + hint inline — users know whether to install, authenticate, pay, or wait out a quota without reading raw stderr.
- **Debugging a provider**: open `/providers-demo` from Settings → Providers → **Troubleshoot AI providers**. Runs every provider API end-to-end with live logs.


### docs/PRD.md

# Cabinet Agent System — MVP Design

## Vision

Cabinet is a Startup OS where you onboard an AI team that works for you. You answer 5 questions, a CEO agent appears, and it suggests teammates. Each agent has skills, recurring jobs, and a place in the knowledge base where their work shows up. You watch them work like watching a real team — through sessions and the KB itself.

**Design principle:** If it feels like enterprise workflow software, it's wrong. If it feels like watching a team work, it's right.

---

## 1. Information Architecture

### Sidebar Navigation

```
┌─────────────────────────┐
│ Cabinet                 │
│                         │
│ ── Team ──              │
│ ▾ Agents                │  ← collapsible
│   🤖 General            │  ← always present (headless Claude)
│   📝 Editor             │  ← sorted first
│   🎯 CEO          ●     │  ← green dot = active
│   📣 Mktg         ●     │
│                         │
│ ── Knowledge Base ──    │
│ ▸ (tree view)           │  ← existing tree
│                         │
│ [+ New Page]     [⚙]    │  ← settings gear icon
└─────────────────────────┘
```

- Clicking "Agents" header opens the agent list grid AND toggles the collapsible list
- Clicking an individual agent opens its detail view directly
- **General** agent is always present (not fetched from API) — headless Claude, no persona
- **Editor** agent is sorted to appear first among fetched agents
- Each agent shows emoji, name, and active status dot (green/gray)

### What changed from current
- **Mission Control** → removed (too complex)
- **Missions** → removed (agents work via jobs and sessions, not mission boards)
- **Activity** → removed (agent sessions serve as the activity log)
- **Chat** → removed for now (will revisit later)
- **Goals** → removed from agent detail (simplify)
- **Jobs** → moved under Agents (each agent owns its jobs)
- **Settings** → moved to gear icon at bottom of sidebar

---

## 2. Agents

### 2.1 Default Agents

Two agents are always present in the sidebar:

- **General** (`slug: "general"`) — Headless Claude with no persona, no heartbeat. Manual sessions only. For ad-hoc tasks that don't belong to a specific agent.
- **Editor** (`slug: "editor"`) — KB content editing, formatting, linking. Live terminal view for running sessions.

Additional agents (CEO, Content Marketer, etc.) are added from the library during onboarding or manually.

### 2.2 Agent List View

When you click "Agents" in the sidebar, you see a **card grid** of your active agents:

```
┌─────────────────────────────────────────────────────┐
│  Agents                          [+ Add from Library]│
│                                                      │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐          │
│  │ 🎯 CEO   │  │ 📝 Editor│  │ 📣 Mktg  │          │
│  │ Lead     │  │ Specialist│ │ Specialist│          │
│  │ ●  Active│  │ ○  Idle  │  │ ● Running │          │
│  │ 3 jobs   │  │ 1 job    │  │ 5 jobs    │          │
│  └──────────┘  └──────────┘  └──────────┘          │
│                                                      │
│  ┌──────────┐                                       │
│  │ + New    │  ← create custom agent                │
│  │ Agent    │                                       │
│  └──────────┘                                       │
└─────────────────────────────────────────────────────┘
```

Each card shows: name, emoji, type (lead/specialist), status indicator, job count.

### 2.3 Agent Detail View

Clicking an agent opens a **detail view with a vertical sidebar** for navigation. Each agent maps to a real directory on disk at `/data/.agents/{slug}/`.

```
┌─────────────────────────────────────────────────────┐
│  ← Back    🎯 CEO Agent             [▶ Run] [⏸ Pause]│
├──────────┬──────────────────────────────────────────┤
│          │                                          │
│ Defn     │  (content for selected section)          │
│ Skills   │                                          │
│ Jobs     │                                          │
│ Sessions │                                          │
│          │                                          │
└──────────┴──────────────────────────────────────────┘
```

#### Section: Definition
- The agent's `persona.md` metadata and instructions
- Shows: department, type, heartbeat cron, budget, workspace, channels, tags
- Persona instructions rendered as readable text

#### Section: Skills
- List of skills attached to this agent (its persona's `skills:` field)
- Each skill: name, description, origin badge, trust level
- Skills are **shared** Anthropic-format SKILL.md bundles — agents reference them by key, they aren't per-agent files. Library lives in cabinet-root or cabinet-scoped `.agents/skills/` (see "Skill SKILL.md Format" below for the schema and `docs/SKILLS_PLAN.md` for the full origin model).
- The agent detail Skills section is multi-select; toggling persists to the persona's `skills:` array via PUT `/api/agents/personas/<slug>`.
- New agents created from a library template auto-promote `recommendedSkills` → `skills` so they have a "good first run" without manual setup.

#### Section: Jobs
- List of the agent's recurring jobs
- Each job shows: name, schedule (human-readable cron), last run status, next run time
- Click a job to expand: see prompt/instructions, run history, enable/disable toggle
- [+ Add Job] button to create a new job for this agent

#### Section: Sessions
- **ChatGPT/Claude Code-style session browser**
- Left panel: scrollable list of past sessions (status, summary, date, duration)
- Right panel: selected session output (monospace transcript)
- [+] button to start a new ad-hoc session with the agent
- New session view has a centered prompt input
- Each session maps to a heartbeat run or manual prompt execution

### 2.4 Agent Disk Layout

Each agent is a directory under `/data/.agents/`. This mirrors the Claude Code agents-on-disk pattern:

```
/data/.agents/{slug}/
  persona.md              ← YAML frontmatter + markdown instructions
  jobs/
    {job-id}.md           ← job definition with cron in frontmatter
  skills/
    {skill-name}.md       ← skill definition
  sessions/
    {session-id}.json     ← session metadata
  memory/
    context.md            ← agent's running context
    decisions.md          ← decisions log
    learnings.md          ← accumulated learnings
    stats.json            ← usage stats (heartbeatsUsed, lastHeartbeat)
```

### 2.5 Agent Library

Accessed via [+ Add from Library] button on the agents page:

```
┌─────────────────────────────────────────────────────┐
│  Agent Library                          [Search...]  │
│                                                      │
│  ── Leadership ──                                    │
│  ┌──────────────────────┐  ┌──────────────────────┐ │
│  │ 🎯 CEO               │  │ 📊 COO               │ │
│  │ Strategic leadership, │  │ Operations, process  │ │
│  │ goal setting, team    │  │ optimization, team   │ │
│  │ coordination          │  │ efficiency           │ │
│  │            [+ Add]    │  │            [+ Add]   │ │
│  └──────────────────────┘  └──────────────────────┘ │
│                                                      │
│  ── Marketing ──                                     │
│  ...                                                 │
└─────────────────────────────────────────────────────┘
```

Clicking [+ Add] copies the template to `/data/.agents/{slug}/` and opens the agent detail view.

---

## 3. Onboarding Flow

### Step 1: Welcome
```
┌─────────────────────────────────────────────────────┐
│           Welcome to Cabinet                         │
│                                                      │
│   Let's set up your AI team. I'll ask a few          │
│   questions to get the right agents working           │
│   for you.                                           │
│                              [Let's go →]            │
└─────────────────────────────────────────────────────┘
```

### Step 2: Five Questions
1. **What's your company/project name?** (text input)
2. **What do you do?** (text input)
3. **What are your top 3 goals right now?** (text input)
4. **How big is your team?** (just me / 2-5 / 5-20 / 20+)
5. **What's your most immediate priority?** (text input)

### Step 3: Team Suggestion
Agent selection based on answers. Check agents you want.

### Step 4: Magic Happens
- Selected agents are created from library templates
- Company context injected into each agent's persona.md
- KB workspace directories created for each agent's output area
- User lands on the Agent list view

---

## 4. Data Architecture

### Directory Structure

```
/data/
  .agents/
    .library/                    ← shipped templates (read-only feel)
      ceo/persona.md
      editor/persona.md
      content-marketer/persona.md
      ...
    .config/
      company.json               ← company context from onboarding
      onboarding-complete.json
    .history/
      {slug}.jsonl               ← heartbeat history logs
    .memory/
      {slug}/                    ← shared memory store
        context.md
        decisions.md
        learnings.md
        stats.json
    .messages/
      {slug}/                    ← inter-agent inbox
    {agent-slug}/                ← active agents (one dir per agent)
      persona.md                 ← agent definition
      jobs/
        {job-id}.md              ← job definition with cron
      skills/
        {skill-name}.md          ← skill definition
      sessions/
        {session-id}.json        ← session metadata

  # Agent output goes into regular KB:
  podcasts/                      ← Marketing agent's podcast workspace
  go-to-market/                  ← Marketing agent's GTM workspace
  ...
```

### Agent persona.md Format

```markdown
---
name: CEO
slug: ceo
emoji: 🎯
type: lead
department: leadership
workspace: /
schedule:
  heartbeat: "0 9 * * 1-5"
  timezone: America/New_York
budget:
  max_runs_per_month: 100
---

# CEO Agent

You are the CEO of {{company_name}}. Your role is to:

1. **Set strategic direction** — define and track company goals
2. **Coordinate the team** — assign tasks to agents
3. **Review progress** — check status, unblock agents
4. **Communicate** — post updates, respond to human input
```

### Job .md Format

```markdown
---
id: reddit-scout
name: Reddit Scout
schedule: "0 */6 * * *"
enabled: true
timeout: 300
output_path: /go-to-market/reddit/
skills:
  - web-search
on_complete:
  - git_commit
---

# Reddit Scout

Search subreddits for posts relevant to {{company_description}}...
```

### Skill SKILL.md Format

Cabinet adopts the Anthropic-compatible skill format used by Claude Code, Codex CLI, and Gemini CLI. Skills live as directories with `SKILL.md` + optional `references/`, `assets/`, `scripts/` subdirs.

```markdown
---
name: web-search                      # kebab-case key, must match dir name
description: >                        # ROUTING logic, not marketing copy
  Use when the agent needs to search the web for current information.
  Don't use for queries answerable from the KB or attached files.
allowed-tools: Bash(curl *)           # optional, comma-separated
trust-policy: prompt-once             # optional, Cabinet-specific:
                                      # auto-allow | prompt-once | always-prompt | refuse
---

# Web Search

Detailed instructions the agent reads when this skill is expanded…
```

**Origins** (resolution precedence — first match wins on key collision):
1. **Cabinet (scoped)** — `data/<cabinet>/.agents/skills/<key>/`
2. **Cabinet (root)** — `<repo>/.agents/skills/<key>/`
3. **Linked repo** — `<linked>/.agents/skills/<key>/` (read-only, via `.repo.yaml`)
4. **System** — `~/.claude/skills/<key>/` and `~/.agents/skills/<key>/` (host-managed; Claude Code already loads these)
5. **Legacy** — `~/.cabinet/skills/<key>/` (back-compat single-origin location)

**Trust gating** runs at mount time: bundle's auto-detected `trustLevel` (`markdown_only` | `assets` | `scripts_executables`) × verified-publisher signal × author `trust-policy` frontmatter. Operator approve/revoke decisions persist in `.cabinet/skills-trust.json`.

**Persona attachment** — agent persona frontmatter:
```yaml
skills:
  - web-search          # active attachments
  - shadcn
recommendedSkills:      # template defaults, auto-promoted to skills on agent creation
  - kb-page-author
```

**Composer `@`-mention** — typing `@skill-name` attaches the skill to the run **only**, not the persona. Use the agent detail Skills section for persistent attachment.

See `docs/SKILLS_PLAN.md` for the full design and `docs/CLAUDE.md` Rule 15 for runtime semantics.

---

## 5. Server Architecture

### Overview

Cabinet runs as **two processes** started with a single command:

```
npm run start
  ├── Next.js        (default port 4000) — UI + API routes
  └── Cabinet Daemon (default port 4100) — WebSocket + scheduler + agent execution
```
Port defaults are provided by `src/lib/runtime/runtime-config.ts` and auto-bumped by the dev wrappers when busy. Override with `CABINET_APP_PORT` / `CABINET_DAEMON_PORT`.

### Cabinet Daemon (`server/cabinet-daemon.ts`)

```
Cabinet Daemon
├── PTY module           ← server/pty/ — spawn + Claude lifecycle + ansi
├── Structured adapters  ← Claude stream-json, Codex, Cursor, OpenCode (subprocess)
├── Job Scheduler        ← node-cron, fires agent jobs on schedule
├── Event Bus            ← WebSocket channels for real-time updates (/api/daemon/events)
└── HTTP + WS endpoints  ← /session/*, /sessions, /reload-schedules, /trigger, /health
                           + WS /api/daemon/pty (terminal sessions)
```

**Agent Execution Flow:**
1. Job fires (cron) or manual trigger
2. Daemon generates a temporary CLAUDE.md for the run
3. Daemon spawns `claude -p "{job prompt}"` with the generated context
4. Output is captured, logged to SQLite, broadcast via WebSocket
5. Post-actions fire (git commit, etc.)

### SQLite Database (`/data/.cabinet.db`)

Used for **structured, high-volume, queryable data**. Content stays as markdown files.

```sql
-- What goes in SQLite
sessions        -- agent session metadata (id, agent, start, end, status, trigger)
job_runs        -- job execution history (id, job, agent, start, end, status, output)

-- What stays as markdown files
agent personas  -- /data/.agents/{slug}/persona.md
job definitions -- /data/.agents/{slug}/jobs/{id}.md
skill files     -- /data/.agents/{slug}/skills/{name}.md
KB content      -- /data/**/*.md
```

### WebSocket Event Channels

```typescript
"agent:status"    → { agent, status: "running"|"idle"|"error", sessionId }
"agent:output"    → { agent, sessionId, chunk }
"job:started"     → { agent, jobId, runId }
"job:completed"   → { agent, jobId, runId, status }
```

---

## 6. API Endpoints

```
# Agents
GET    /api/agents/personas          → list all agents
POST   /api/agents/personas          → create agent
GET    /api/agents/personas/[slug]   → get agent detail (persona, memory, history)
PUT    /api/agents/personas/[slug]   → update agent / run / toggle
DELETE /api/agents/personas/[slug]   → delete agent

# Agent Library
GET    /api/agents/library           → list available templates
POST   /api/agents/library/[slug]/add → instantiate agent from template

# Jobs (under agents)
GET    /api/agents/[slug]/jobs       → list agent's jobs
POST   /api/agents/[slug]/jobs       → create job for agent
PUT    /api/agents/[slug]/jobs/[id]  → update job
DELETE /api/agents/[slug]/jobs/[id]  → delete job
POST   /api/agents/[slug]/jobs/[id]/run → trigger job manually

# Onboarding
GET    /api/onboarding/status        → check if onboarding complete
POST   /api/onboarding/setup         → process onboarding answers, create team
```

---

## 7. Frontend Components

```
src/components/
  agents/
    agent-list.tsx              ← card grid of agents
    agent-detail.tsx            ← vertical sidebar nav (Definition, Skills, Jobs, Sessions)
    agent-dashboard.tsx         ← monitoring dashboard
    agent-session-view.tsx      ← GeneralAgentView for headless Claude
  onboarding/
    onboarding-wizard.tsx       ← 5-question flow
  settings/
    settings-page.tsx           ← system settings
  sidebar/
    sidebar.tsx                 ← collapsible agent list under Team
```

---

## 8. Implementation Phases

### Phase 1: Foundation (Agent Restructure) ✅
1. Create agent library templates in `/data/.agents/.library/`
2. Build new agent list view (card grid)
3. Build agent detail view with vertical sidebar (Definition, Skills, Jobs, Sessions)
4. Move jobs under agents (agent owns jobs)
5. Update sidebar navigation with collapsible agent list
6. Default agents: General (always present) + Editor (sorted first)

### Phase 2: Onboarding ✅
1. Build onboarding wizard (5 questions)
2. Build team suggestion view
3. Create setup API
4. Auto-detect first run and show onboarding

### Phase 3: Polish
1. Skill management UI
2. Job output → KB output path linking
3. Session transcript improvements
4. Agent creation/deletion from UI

---

## 9. Naming Glossary

| Term | Definition |
|------|-----------|
| **Agent** | A persistent AI persona with a role, skills, and jobs. Like a team member. Maps to `/data/.agents/{slug}/` on disk. |
| **General** | The default headless Claude agent — no persona, no heartbeat. For ad-hoc tasks. |
| **Job** | A recurring scheduled task that an agent runs. Has a cron schedule and prompt. Stored in agent's `jobs/` dir. |
| **Skill** | A reusable capability available to an agent. Stored in agent's `skills/` dir. |
| **Session** | A single Claude Code execution (one run of an agent). Browsable like ChatGPT history. |
| **Workspace** | The KB directory where an agent's output lives. |
| **Library** | Pre-built agent templates shipped with Cabinet. |


## Top-level structure

```
  .audit-shots/
  .dockerignore
  .env.example
  .github/
  .gitignore
  .nvmrc
  assets/
  cabinet/
  cabinet-release.json  — Release version manifest for cabinetai update
  cabinetai/  — npm cabinetai CLI package (npx cabinetai run)
  CHANGELOG.md  — Release changelog
  cli/  — CLI tooling
  components.json
  docs/  — Architecture, PRDs, CLI reference, agent instructions
  electron/  — Electron desktop packaging
  eslint.config.mjs
  forge.config.cjs
  LICENSE
  mcps/  — MCP server integrations
  next.config.ts
  package-lock.json
  package.json  — npm dependencies and scripts
  postcss.config.mjs
  PROGRESS.md  — Append-only progress log
  public/
  README.md  — Main documentation
  RELEASE_NOTES_v0.4.0.md
  resources/
  scripts/  — Build/deployment scripts
  server/  — cabinet-daemon.ts — WebSocket, scheduler, adapter runtime, PTY
  src/  — Main Next.js app (components, API routes, stores, lib)
  TELEMETRY.md
  test/  — Test suite
  tsconfig.json
```