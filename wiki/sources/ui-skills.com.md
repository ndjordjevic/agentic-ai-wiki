---
type: source
category: "Design & UI generation"
source_url: https://www.ui-skills.com/skills
companion_urls:
  - https://github.com/ibelick/ui-skills
raw_files:
  - ../../raw/web/ui-skills.com.md
  - ../../raw/github/ibelick-ui-skills.md
tags:
  - design-skills
  - skills-catalog
  - mcp
  - agent-skills
  - design-engineering
  - cli
  - playbook
  - ui-registry
related:
  - ibelick-ui-skills
  - skills.sh
  - emilkowalski-skills
  - leonxlnx-taste-skill
  - Nutlope-inspo
  - designmd.cc
  - open-design.ai
  - Owl-Listener-designer-skills
product: ui-skills.com
detail_level: standard
created: 2026-10-28
updated: 2026-10-28
---

UI Skills (ui-skills.com) is a curated registry of **439** design-engineering Agent Skills — browsable on the web, fetchable via `npx ui-skills`, and queryable over MCP at `https://www.ui-skills.com/mcp` — so coding agents can discover and load the smallest useful UI skill for a task instead of installing every pack by hand. The companion open-source repo is [[ibelick-ui-skills]] (~10k★, MIT). The site also ships a Playbook of distilled UI lessons, topic/collection browsing, a DESIGN.md catalog, and agent compatibility pages. (../../raw/github/ibelick-ui-skills.md)

_All claims below are sourced from ../../raw/web/ui-skills.com.md unless otherwise noted._

## What it does

UI Skills is a discovery and delivery layer for design-engineering skills: a skills catalog (`/skills`, `/skills/registry.txt`, full `llms.txt`), a zero-install CLI, and a remote MCP server with `list_skills` / `get_skill` over the same registry. Featured skills on the homepage include routing (`ui-skills-root`), improve/audit skills (`improve-ui`, `improve-animations`, `improve`), and well-known packs from authors like Anthropic (`frontend-design`), Emil Kowalski, Paul Bakaus (`impeccable`), and Leonxlnx (`gpt-tasteskill`). Topics span accessibility, motion, systems, visual, interaction, performance, craft, taste, typography, color, 3D, frameworks (Next.js, Nuxt, Vue, React Native, SwiftUI, shadcn/ui), and more.

## Key features

- **439-skill registry** — TSV registry + per-skill pages under `/skills/<author>/<slug>`; `llms.txt` catalogs the full set for agents.
- **CLI** — `npx ui-skills` with `start`, `categories`, `list` / `list --category motion`, `get <skill>`.
- **MCP** — Streamable HTTP at `https://www.ui-skills.com/mcp` (server card v0.2.4); tools `list_skills` and `get_skill`.
- **Playbook** — Interactive distilled lessons (aspect-ratio, text-balance, touch targets, focus rings, motion easing, etc.).
- **Browse surfaces** — Topics, collections (mobile app, website layout, visual hierarchy, design principles, landing pages, buttons), authors, components, icons, DESIGN.md gallery (`/design-md`), jobs board.
- **Agent matrix** — `/agents` lists 25+ clients (Claude Code, Cursor, Codex, Copilot, Windsurf, Gemini, Cline, OpenCode, Pi, Zed, Devin CLI, …) that work with the skills CLI.

## Architecture

Public site is an Astro app (generator Astro v7.3.2 in page HTML) with structured data for topics/collections. The registry is a plain-text catalog mirrored to GitHub raw SKILL.md URLs; CLI and MCP both read that registry. Site DESIGN.md (`/design.md`) defines a quiet editorial design language (Inter Variable + JetBrains Mono, restrained surfaces). Companion repo hosts the open-source packaging, sample skills under `skills/`, and MCP/CLI implementation. (../../raw/github/ibelick-ui-skills.md)

## Installation

```bash
npx ui-skills start
npx ui-skills categories
npx ui-skills list --category motion
npx ui-skills get baseline-ui
```

MCP endpoint for agents:

```
https://www.ui-skills.com/mcp
```

Server card: `https://www.ui-skills.com/.well-known/mcp/server-card.json`. GitHub stars shown on the site as 9.8k+★ for [[ibelick-ui-skills]]. (../../raw/github/ibelick-ui-skills.md)

## Example usage

An agent connected to the MCP calls `list_skills` (optional query) then `get_skill` with a discovery name/slug/pathSlug to pull SKILL.md into context. From a terminal, `npx ui-skills start` prints the routing skill (`ui-skills-root`) that steers by topic/stack/intent to the smallest useful skill set; `npx ui-skills get baseline-ui` prints that skill's full markdown. (../../raw/github/ibelick-ui-skills.md)

## When to use

Use UI Skills when you need **discovery** across many authors' design skills (not a single opinionated pack), want CLI/MCP access to the same catalog, or want playbook-style micro-lessons and DESIGN.md references alongside skills. Prefer a single pack ([[emilkowalski-skills]], [[leonxlnx-taste-skill]], [[Nutlope-inspo]] for live-site taste) when you already know the skill you want.

## Maintenance status

Companion repo: ~10k★, MIT, TypeScript, latest release v0.2.3, MCP server card version **0.2.4**; site claims 439 skills and 9.8k+★. Homepage/GitHub: https://www.ui-skills.com/, https://github.com/ibelick/ui-skills. (../../raw/github/ibelick-ui-skills.md)

## Ecosystem

Overlaps the Agent Skills directory [[skills.sh]] and individual design packs already in this wiki ([[emilkowalski-skills]], [[Owl-Listener-designer-skills]], [[open-design.ai]], [[designmd.cc]]). The `/design-md` gallery curates public DESIGN.md files in the same spirit as [[voltagent-awesome-design-md]] / [[designmd.cc]].
