---
type: source
source_url: https://runcabinet.com
tags: [knowledge-base, agent-orchestration, self-hosted, file-based-storage, scheduled-jobs, agentic-os, embedded-html-apps, web-terminal, wysiwyg-editor]
related:
  - "[[hilash-cabinet]]"
  - "[[coleam00-claude-memory-compiler]]"
product: cabinet
detail_level: standard
created: 2026-04-25
updated: 2026-04-27
---

Cabinet (runcabinet.com) is a free, open-source, self-hosted knowledge base OS built around AI-first workflows. It positions itself as an "operating system for your work" — markdown files on disk form a persistent brain for AI agents, enabling knowledge workers and small teams to build autonomous, memory-rich workflows without a database or subscription fee. As a product in the Agentic AI space it is directly relevant as an end-to-end deployment of persistent agent memory: agents have goals, skills, and scheduled jobs and operate 24/7 against a file-backed knowledge store.

_All claims below are sourced from ../../raw/web/runcabinet.com.md unless otherwise noted._

## What It Does

Cabinet combines a WYSIWYG markdown editor, an embedded xterm.js web terminal, and an AI agent orchestration layer into a single self-hosted application. Files live on disk — no external database — and every save is auto-committed to git. Users create AI agents (CEO, Editor, Marketer, etc.) with defined goals and skills; those agents can be @mentioned in team chat or triggered on cron schedules to execute tasks autonomously.

## Key Features

| Feature | Description |
|---|---|
| File-based storage | Markdown on disk; portable, git-backed, no database |
| AI agent orchestration | Custom agents with goals, skills, and scheduled jobs |
| Embedded HTML apps | Drop `index.html` into any folder for interactive dashboards |
| Web terminal | Full xterm.js terminal access in the browser |
| WYSIWYG editor | Rich text editing with markdown toggle |
| Scheduled jobs | Cron-based automation for 24/7 agent operation |
| Git integration | Auto-commits on every save; linked repo via `.repo.yaml` |
| Full-text search | Instant fuzzy search across all pages |
| PDF & CSV support | Native inline rendering and editable tables |
| Team chat | Internal channels with agent @mentions |
| Mission & task system | Kanban boards and progress tracking |

## Architecture and Concepts

Cabinet's central design principle is the file-system-as-database: markdown files are the source of truth, which makes the knowledge base portable and diff-able. AI agents operate against this file store with persistent context across sessions — the knowledge base acts as long-term memory for agents, solving the session-amnesia problem inherent to stateless LLM calls. Embedded HTML apps extend the system without a framework layer: any `index.html` dropped into a folder renders as an interactive tool inside the Cabinet UI.

## When to Use

- Startup or small team needing an AI-augmented operations hub with no infrastructure overhead
- Individuals who want a self-hosted alternative to cloud knowledge bases (Notion, Confluence) with native AI agent support
- Projects requiring 24/7 autonomous agent operation against a persistent, git-versioned knowledge store
- Use cases: founder OS, sales pipeline automation, newsletter production, open-source project maintenance

## Ecosystem

- **Install:** `npx cabinetai run` — scaffolds workspace locally; Mac-primary
- **License:** MIT
- **GitHub:** https://github.com/hilash/cabinet
- **Community:** Discord at discord.gg/hJa5TRTbTH
