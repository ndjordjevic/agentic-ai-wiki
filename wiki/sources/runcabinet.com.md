---
type: source
source_url: https://runcabinet.com/
companion_urls:
  - https://github.com/hilash/cabinet
raw_files:
  - ../../raw/web/runcabinet.com.md
  - ../../raw/github/hilash-cabinet.md
tags:
  - ai-first-knowledge-base
  - self-hosted
  - ai-agents
  - markdown-on-disk
  - git-backed
  - open-source
  - startup-os
  - scheduled-jobs
related:
  - paperclip.ing
  - reseek.net
product: cabinet
detail_level: deep
created: 2026-04-29
updated: 2026-05-13
---

Cabinet is a free, open-source, self-hosted AI-first startup OS where an entire knowledge base lives as markdown files on disk. It combines WYSIWYG editing, AI agents with scheduled jobs, embedded HTML apps, a web terminal, git-backed history, and built-in team chat — all without a database or vendor lock-in. The project is positioned as the product Andrej Karpathy described when he noted there was "room here for an incredible new product instead of a hacky collection of scripts" for LLM-backed knowledge bases.

_All claims below are sourced from ../../raw/web/runcabinet.com.md unless otherwise noted._

## What it does

Cabinet gives AI agents a persistent, structured memory: a knowledge base that both humans and agents read and write to continuously. Every file lives as a markdown document on disk; there is no hidden database, no API rate limits, and no data trapped inside a cloud provider. Users install via `npx cabinetai run`, answer five onboarding questions about their company and goals, and Cabinet scaffolds a custom AI team with pre-defined roles, recurring jobs, and workspaces inside the KB.

The key differentiator is that Cabinet combines three things most tools keep separate: a rich knowledge base (like Obsidian or Notion), an AI agent orchestration layer (like [[paperclip.ing|Paperclip]]), and embedded live apps. Drop an `index.html` into any KB directory and it renders as a live iframe; add a `.app` marker and the sidebar auto-collapses for a full-screen experience.

## Key features

**Knowledge base and editing:** WYSIWYG editing powered by Tiptap (ProseMirror-based) with slash commands, tables, and code blocks; toggle to raw markdown at any time. Full-text search via Cmd+K using FlexSearch, rebuilt on every change. PDFs render inline; CSVs open as editable tables with row/column operations. Linked git repos allow agents to read source code via `.repo.yaml` files in any KB directory. (../../raw/github/hilash-cabinet.md)

**AI agents:** Cabinet ships 20 pre-built agent templates spanning Leadership (CEO, COO, CFO, CTO), Product, Marketing, Engineering, Sales & Support, Analytics, and Operations. Each agent has goals, skills, and recurring cron jobs — a Content Marketer scouts Reddit every 6 hours; a CEO agent runs weekly goal reviews. Agents communicate via built-in team channels; users `@mention` an agent to trigger a response. The AI panel also supports `@PageName` mentions to attach arbitrary KB pages as context. (../../raw/github/hilash-cabinet.md)

**AI runtime:** Agent tasks, jobs, and heartbeats run through a provider adapter layer with persisted conversations and transcript-driven live views. Supported CLI providers include Claude Code (`claude_local` adapter) and Codex CLI (`codex_local` adapter); Gemini CLI was recently added. Per-run overrides can choose provider, model, and reasoning effort. (../../raw/github/hilash-cabinet.md)

**Scheduled jobs:** Cron-based automation with recurring jobs per agent. The unified daemon (`cabinet-daemon.ts`) handles WebSocket connections, the job scheduler, the AI runner, and PTY sessions in a single process. (../../raw/github/hilash-cabinet.md)

**Version control and history:** Every save auto-commits to git. A full diff viewer and Version History panel let users restore any page to any prior commit. Linked repo support via `.repo.yaml` connects KB directories to external source code repos. (../../raw/github/hilash-cabinet.md)

## Architecture

The app is a Next.js 16 (TypeScript) frontend paired with a Node.js daemon server. (../../raw/github/hilash-cabinet.md)

```
src/
  app/api/         → Next.js API routes (tree, pages, search, agents, git, upload, assets)
  components/      → Sidebar, editor, AI panel, tasks, agents, jobs, terminal, composer, search, layout
  stores/          → Zustand state (tree, editor, ai-panel, task, app)
  lib/             → Storage (path-utils, page-io, tree-builder), markdown, git, agents, jobs
server/
  cabinet-daemon.ts → Unified daemon: structured runs, PTY sessions, scheduler, WebSocket events
  terminal-server.ts → Standalone PTY WebSocket server (legacy/debugging)
data/
  .agents/.library/ → 20 pre-built agent templates
  getting-started/  → Default KB page
```
(../../raw/github/hilash-cabinet.md)

**Tech stack:** Next.js 16, TypeScript, Tailwind CSS, shadcn/ui (base-ui, not Radix), Tiptap/ProseMirror, Zustand, xterm.js, node-cron, gray-matter, unified/remark, turndown. (../../raw/github/hilash-cabinet.md)

Core rules the codebase enforces: no database (everything under `/data`); pages are directories with `index.md` + assets or standalone `.md` files; YAML frontmatter stores title, created, modified, tags, icon, order; path traversal prevention (all resolved paths must start with `DATA_DIR`); auto-save debounced 500ms. (../../raw/github/hilash-cabinet.md)

## Installation

Requirements: Node.js 20+; macOS or Linux (Windows via WSL); at least one CLI provider — Claude Code CLI (`npm install -g @anthropic-ai/claude-code`) or Codex CLI (`npm install -g @openai/codex`). (../../raw/github/hilash-cabinet.md)

```bash
npx create-cabinet@latest
cd cabinet
npm run dev:all
```

Environment configuration: (../../raw/github/hilash-cabinet.md)

```bash
cp .env.example .env.local
```

| Variable | Default | Description |
|---|---|---|
| `KB_PASSWORD` | (empty) | Password to protect the UI. Leave empty for no auth. |
| `DOMAIN` | `localhost` | Domain for the app. |

## Example usage

Start both servers and open the knowledge base: (../../raw/github/hilash-cabinet.md)

```bash
npm run dev:all
# Next.js on localhost:3000, daemon on localhost:3001
```

The onboarding wizard asks five questions (company name, what you do, goals, team structure, main workflows) and scaffolds a custom AI team. Each agent gets a KB workspace directory, a set of recurring cron jobs, and access to the full knowledge base.

Embedding an HTML app in the KB: (../../raw/github/hilash-cabinet.md)

```
data/tools/lead-scorer/
  index.html      ← renders as live iframe in Cabinet
  .app            ← triggers full-screen mode; sidebar + AI panel auto-collapse
  styles.css
  app.js
```

Triggering an AI task from the AI panel: (../../raw/github/hilash-cabinet.md)
- Type `@PageName` in the AI panel to attach a KB page as context.
- Agents write their output directly back to KB files, ensuring all results are version-controlled and searchable.
- Use the task board (Kanban) to track missions assigned to agents.

## When to use

Cabinet fits teams and solo founders who want their AI agents to have persistent memory and context without depending on a cloud service. It is well-suited for:

- Solo founders and small startups that want a single OS for strategy docs, agent automation, and HTML dashboards.
- Developers who want AI agents that read and write directly to files (no API limits, no lock-in).
- Teams that want full audit history of how their knowledge base evolves — every change is a git commit.
- Anyone building on top of the Karpathy pattern of feeding rich structured context into LLMs.

Cabinet is not a fit for teams that need multi-user cloud collaboration, mobile access, or a managed SaaS — those use cases favor Notion or similar. For pure agent orchestration without a content layer, [[paperclip.ing|Paperclip]] may be a better match.

## Maintenance status

Cabinet is an active open-source project maintained by Hila Shmuel (former Engineering Manager at Apple), building in public. The last commit (2026-04-16) added Gemini CLI provider support, versioned Claude model labels, and a shared ProviderGlyph component. The project is under MIT license. There is a cloud waitlist at runcabinet.com/waitlist for a hosted version. Community discussion happens on Discord. (../../raw/github/hilash-cabinet.md)

## Ecosystem

Cabinet is explicitly positioned against Obsidian (no agents, no scheduling), Notion (cloud-locked, no agents), and [[paperclip.ing|Paperclip]] (agent orchestration but no content layer). The comparison table on the landing page shows Cabinet as the only tool with all of: knowledge base, AI agent orchestration, embedded HTML apps, web terminal, and git-backed history.

The project uses the Karpathy LLM-wiki pattern as its philosophical foundation: raw data → LLM-compiled wiki → agent-operated knowledge base. Cabinet operationalizes this pattern as a product rather than a collection of scripts.

External integrations planned/available: Claude Code CLI, Codex CLI, Gemini CLI, local models (BYOAI), Discord community, GitHub-linked repos via `.repo.yaml`.
