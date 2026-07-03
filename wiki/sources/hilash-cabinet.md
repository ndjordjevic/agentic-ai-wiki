---
type: source
source_url: https://github.com/hilash/cabinet
tags:
  - ai-first-knowledge-base
  - self-hosted
  - markdown-on-disk
  - ai-agents
  - provider-adapters
  - scheduled-jobs
  - skills-ecosystem
  - git-backed
related:
  - runcabinet.com
  - paperclip.ing
  - 6eanut-llm-wiki
  - supermemory.ai
  - kepano-obsidian-skills
  - skills.sh
  - coleam00-claude-memory-compiler
  - langchain-ai-openwiki
product: cabinet
detail_level: standard
created: 2026-07-03
updated: 2026-07-03
---

`hilash/cabinet` (2.4k+ stars, MIT, TypeScript) is the open-source implementation of Cabinet — a self-hosted AI-first startup OS where the entire knowledge base lives as markdown on disk, agents run through a provider-adapter runtime with persisted conversations, and scheduled cron jobs compound context over time. The `cabinetai` npm CLI (`npx create-cabinet@latest`) downloads the app to `~/.cabinet/app/v{version}/` and treats each cabinet as a lightweight data directory (`.cabinet` manifest + `.agents/` + content files) anywhere on disk. See also [[runcabinet.com]] for the marketing-site and product-positioning companion page.

_All claims below are sourced from ../../raw/github/hilash-cabinet.md unless otherwise noted._

## What it does

Cabinet operationalizes Andrej Karpathy's LLM-wiki insight as a product: humans and agents share one git-backed markdown knowledge base with no database. The Next.js UI provides WYSIWYG editing (Tiptap), a collapsible tree sidebar, full-text Cmd+K search, embedded HTML apps (`index.html` in any folder), PDF/CSV/office viewers, and an Agents workspace where 20 pre-built persona templates (CEO, Content Marketer, Editor, etc.) run tasks, jobs, and heartbeats. Philosophy: humans define intent, agents do the work, the KB is shared memory.

## Installation

```bash
npx create-cabinet@latest
cd cabinet
npm run dev:all
```

Open `http://localhost:4000`. Requirements: Node.js 22+ (`.nvmrc` in repo); at least one CLI provider (Claude Code, Codex, Cursor, OpenCode, Copilot, Grok, or Pi). Electron desktop builds target macOS and Windows. Update via `npx cabinetai update`; uninstall cached app with `npx cabinetai uninstall` (cabinet data directories are never deleted automatically).

## Key features

- **File-based everything** — pages are directories with `index.md` + assets or standalone `.md`; YAML frontmatter stores title, tags, icon, order; every save auto-commits to git with diff viewer and version restore.
- **Provider adapter runtime** — tasks, jobs, and heartbeats run through structured local adapters (`claude_local`, `codex_local`, etc.) with persisted multi-turn conversations, transcript-driven live views, per-run provider/model/reasoning overrides, and a first-class Web Terminal (PTY) for interactive CLI sessions.
- **Skills** — Anthropic-format `SKILL.md` bundles resolved across cabinet-scoped, linked-repo, and system origins (`~/.claude/skills/`, `~/.agents/skills/`); trust gating, `skills.sh`/GitHub import, `@skill` compose mentions, and persona `skills:` attachments.
- **Scheduled jobs** — `node-cron` scheduler in `cabinet-daemon.ts` for recurring agent automation (Reddit scout, weekly reports, etc.).
- **Missions & tasks** — Kanban task boards backed by the conversation system (`/api/agents/conversations`); multi-turn tasks with SSE live updates and KB artifact cards.
- **Connect Knowledge** — per-room inline mounts from desktop-sync folders (Google Drive, iCloud, OneDrive, Dropbox) with server-side read-only enforcement; MCP connectors for Notion/Confluence via Integrations Hub.
- **Registry templates** — home carousel reads `hilash/cabinets` manifest (auto-built by CI); operators add cabinets to the registry repo, not hardcoded in app source.
- **Security** — optional `KB_PASSWORD` gate with PBKDF2 session cookies, rate-limited login, path-traversal prevention on all file APIs.

## Architecture

```
src/          → Next.js 16 App Router (API routes, React components, Zustand stores)
server/       → cabinet-daemon.ts (WebSocket, scheduler, adapter runtime, PTY)
cabinetai/    → npm CLI (create, run, update, uninstall)
data/         → Default KB + .agents/.library/ (20 agent templates)
mcps/         → MCP server integrations
electron/     → Desktop packaging (Electron Forge)
```

**Tech stack:** Next.js 16, TypeScript, Tailwind + shadcn/ui (base-ui, not Radix), Tiptap, Zustand, xterm.js, gray-matter, unified/remark, node-cron.

**Core rules from `docs/CLAUDE.md`:** no database; shadcn uses base-ui (no `asChild`); auto-save debounced 500ms; embedded apps via `index.html` + optional `.app` full-screen marker; linked repos via `.repo.yaml` for agent source-code context; office docs (`.docx`, `.xlsx`, `.pptx`) render inline via client viewers.

## Example usage

Create and start a cabinet:

```bash
npx cabinetai create my-startup
cd my-startup
npx cabinetai run
```

Run both dev servers from source checkout:

```bash
npm run dev:all    # Next.js :4000 + daemon :4100
```

Attach a skill at compose time with `@skill-name`; configure auth via `.env.local` (`KB_PASSWORD`, `DOMAIN`). See `docs/CABINETAI.md` for full CLI reference and `docs/AUTH.md` for threat model.

## Maintenance status

Active open-source project by Hila Shmuel (former Apple EM), building in public. Latest release **v0.4.4** (2026-05-23); 2,381 stars, 235 forks; MIT license; last push 2026-07-03. Community on Discord; cloud waitlist at runcabinet.com/waitlist. Anonymous telemetry is on by default (`CABINET_TELEMETRY_DISABLED=1` or Settings → Privacy to disable). Contributing: sync with Hila on Discord before large PRs during rapid iteration.
