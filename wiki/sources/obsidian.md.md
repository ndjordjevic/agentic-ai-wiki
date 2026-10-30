---
type: source
category: "Knowledge, RAG, memory & context"
source_url: https://obsidian.md
tags:
  - local-first-notes
  - wikilinks
  - knowledge-base
  - community-plugins
  - obsidian-cli
  - agent-automation
related:
  - kepano-obsidian-skills
  - agricidaniel-claude-obsidian
  - graphify.net
  - 6eanut-llm-wiki
product: obsidian
detail_level: standard
created: 2026-10-30
updated: 2026-10-30
---

Obsidian is a free, local-first Markdown knowledge app (links, graph, Canvas) with thousands of community plugins/themes, optional Sync/Publish add-ons, and — importantly for agents — an official Obsidian CLI that can script vault operations and expose developer tooling (reload plugins, screenshots, `eval`) while the desktop app runs. Often used as a live viewer for markdown Claude writes.

_All claims below are sourced from ../../raw/web/obsidian.md.md unless otherwise noted._

## What it does

Obsidian stores notes as plain Markdown on the user's device (offline, private, no required account). Core UX: bidirectional [[wikilinks]], interactive graph view, infinite Canvas boards, core + community plugins, and themes/CSS snippets. Optional Obsidian Sync (E2E encryption, version history, shared vaults) and Obsidian Publish (hosted wiki/garden sites). Desktop/mobile apps; commercial license optional for organizations.

## Key features

- Local vaults in open formats; no lock-in
- Links, graph, Canvas for knowledge structuring
- Community directory: ~9.5k plugins / ~780 themes (including a large AI category)
- Obsidian CLI: terminal/TUI control of the running app — daily notes, search, create/read, tags, tasks, plus developer commands for agentic plugin testing
- Sync ($4/user/mo annual) and Publish ($8/site/mo); Catalyst ($25 one-time) and Commercial ($50/user/yr) support licenses
- Free forever for personal use; no telemetry / no selling user data per pricing FAQ

## Architecture and concepts

Vault = folder of Markdown (and attachments). Wikilink resolution by note name; plugins extend via TypeScript API (docs at docs.obsidian.md). CLI requires the Obsidian app process (first command can launch it); headless sync is a separate product path. Help at help.obsidian.md; docs repo github.com/obsidianmd/obsidian-docs for contributions.

## Main APIs

- **Obsidian CLI** (`obsidian …`): scripting surface for vault I/O and developer tools (`plugin:reload`, `dev:screenshot`, `eval`, etc.)
- **Plugin API** (TypeScript): build community plugins/themes — getting-started and submit flows on docs.obsidian.md
- No public cloud notes API required for core local use

## When to use

- Personal knowledge bases, research gardens, and agent-written markdown you want to review outside chat (as in the Claude tools roundup)
- Teams needing local-first notes with optional E2E Sync
- Plugin/theme developers and coding agents that need to drive/reload Obsidian via CLI

## Ecosystem

Massive community plugin/theme marketplace; Web Clipper; integrations via community plugins. Agent-adjacent wiki sources: [[kepano-obsidian-skills]], [[agricidaniel-claude-obsidian]]. Developer community + Catalyst early betas.
