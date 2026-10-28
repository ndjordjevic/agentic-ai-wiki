---
type: source
category: "Design & UI generation"
source_url: https://github.com/Nutlope/inspo
tags:
  - mcp-server
  - design-inspiration
  - design-md
  - ui-reference
  - together-ai
  - anti-ai-slop
  - reference-components
  - visual-taste
related:
  - Nutlope-hallmark
  - Nutlope-variate
  - designmd.cc
  - voltagent-awesome-design-md
  - open-design.ai
  - ibelick-ui-skills
product: inspo
detail_level: standard
created: 2026-10-28
updated: 2026-10-28
---

Nutlope/inspo (Inspo, ~941★, MIT, Together AI) is a curated archive of real production websites — 2,320 pages across 832 sites, each with desktop/mobile captures, traced palettes, fonts, detected tech, and fold-by-fold autopsies — exposed to coding agents over MCP so they can study visual taste before writing UI. Install is one line (`npx -y inspo-mcp install` or hosted `https://inspomcp.dev/api/mcp`); `recommend(brief)` is the primary entry tool. Complements [[Nutlope-hallmark]] (structural anti-slop skill from the same author) and DESIGN.md ecosystems like [[designmd.cc]] / [[voltagent-awesome-design-md]].

_All claims below are sourced from ../../raw/github/Nutlope-inspo.md unless otherwise noted._

## What it does

Agents have tools but not taste; Inspo ships a static, queryable catalogue of shipped sites so an agent can pull real palettes, type ramps, CSS variables, named macrostructures, and copy-pasteable reference JSX before it emits UI. Fifteen MCP tools cover search, recommend, design-system extraction (`get_design_system` → DESIGN.md), color/similarity/macrostructure lookup, component crops, and curated collections. Results include absolute screenshot URLs (Vercel Blob) plus baked-in `heroGuidance` and `spacingGuidance` drawn from archive measurements.

## Installation

One command detects Claude Code, Cursor, Codex, VS Code, Windsurf, Zed, and Claude Desktop and writes config pointed at the hosted endpoint:

```bash
npx -y inspo-mcp install
```

Hosted (no clone):

```bash
claude mcp add --transport http inspo https://inspomcp.dev/api/mcp
```

Or stdio via npm (`npx -y inspo-mcp`), or clone + `pnpm install` for local gallery (`pnpm dev`) and MCP smoke tests (`pnpm --filter @inspo/mcp test`). Self-host runbook is `DEPLOY.md`; client snippets live on inspomcp.dev/mcp.

## Key features

- **Catalogue scale** — 2,320 pages / 832 sites; desktop + mobile; palettes, fonts, tech, tags, fold autopsies; a DESIGN.md per site.
- **68 reference components** — heroes, pricing, footers, navs, etc., with copy-pasteable JSX via `get_reference_jsx`.
- **Fifteen MCP tools** — lead with `recommend(brief)`; also `search_screens`, `get_design_system`, `compare`, `find_by_color`, `find_similar`, macrostructure/component finders, `get_filters`, `get_site_pages`, `get_screen`, collections.
- **Dual transport** — stdio npm package `inspo-mcp` (CDN catalogue) and Streamable HTTP on the Vercel site (`/api/mcp`); MCP registry name `io.github.nutlope/inspo` (v0.1.15).
- **OSS-model profiles** — `INSPO_PROFILE=lite|full`, `INSPO_IMAGES=thumbs|none`, `INSPO_MAX_TOKENS` budget; client auto-detection for Kimi/OpenCode/Cline/etc.
- **Read-only + SSRF-guarded** — tools are read-only; live design-system fetch validates public hosts/ports and byte-caps bodies.

## Architecture

pnpm + Turborepo monorepo: `apps/mcp` (TypeScript MCP server — `tools.ts`, `profile.ts`, stdio + shared HTTP handler), `apps/web` (Next.js 16 + Tailwind v4 gallery; hosted MCP is a route handler in the same app), `apps/worker` (Playwright capture on Fly.io; Together AI for tags/autopsies/embeddings), `apps/cli`, plus `packages/db` (static seed JSON, optional Neon/pgvector), `packages/shared`, `packages/taxonomy` (tag allow-lists). Query path needs no database — catalogue ships as a static seed; embeddings sidecar from CDN. Capture → encode → Blob upload → merge seed → enrich → publish is documented in `SEEDING.md`.

## Example usage

```bash
npx -y inspo-mcp install
# or
claude mcp add --transport http inspo https://inspomcp.dev/api/mcp
```

Typical agent flow: call `recommend` with a brief (optional macrostructure/pageType/vibe filters), then `get_design_system` / `get_reference_jsx` on shortlisted hits. For text-only harnesses: `https://inspomcp.dev/api/mcp?profile=lite&images=none`. Dev loop: `pnpm --filter @inspo/mcp test` boots the server in-process and exercises core tools.

## Maintenance status

941 stars, 62 forks, MIT (Together AI and contributors), TypeScript, default branch `main`, no GitHub Releases listed; npm/MCP registry version **0.1.15**; last push 2026-10-27. Homepage: https://inspomcp.dev. Roadmap (README): side-by-side desktop/mobile on screen pages, backfill component crops, paginate list tools, retina mobile re-shoot; accounts/paywalls intentionally skipped. Screenshots remain designers' work; DMCA at /dmca.
  - ui-skills.com
  - usehallmark.com
  - aura.build
