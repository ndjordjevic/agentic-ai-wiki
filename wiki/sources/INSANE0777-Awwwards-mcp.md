---
type: source
category: "MCP servers & integrations"
source_url: https://github.com/INSANE0777/Awwwards-mcp
tags:
  - awwwards
  - mcp-server
  - design-inspiration
  - screenshots
  - motion-census
  - design-dna
  - coding-agents
  - no-api-key
related:
  - responsively-org-responsively-app
  - dembrandt-dembrandt
  - AThevon-genjutsu
  - designmd.cc
  - stitch.withgoogle.com
  - microsoft-playwright-mcp
product: awwwards-mcp
detail_level: standard
created: 2026-10-28
updated: 2026-10-28
---

awwwards-mcp (~362★, MIT, TypeScript, v1.14.0) is a free open-source MCP server that gives coding agents (Claude Code, Codex, Cursor, OpenCode, etc.) design inspiration from Awwwards — search with real screenshots, pull "design DNA," capture/record live sites, and verify recreations — positioned as a Mobbin-style visual reference loop with no API key.

_All claims below are sourced from ../../raw/github/INSANE0777-Awwwards-mcp.md unless otherwise noted._

## What it does

Agents query award-winning sites in natural language, see screenshots inline, extract palettes/tech stacks/design elements/award history, then optionally band-map any URL, census scroll/hover motion, fingerprint frameworks, and recreate pages section-by-section into Vite/Astro/Next with a measured motion manifest — closing the loop with `verify_build` scoring.

## Installation

Published on npm as `awwwards-mcp` (homepage). Wire as an MCP server in Claude Code / Cursor / compatible clients per the README tool list and install instructions in the raw capture.

## Key features

- Free-text FTS5/BM25 search over Awwwards-indexed sites with real screenshots
- Design DNA extraction (colors, stack, elements, awards)
- Capture/census tools that run on **any URL**, not only Awwwards entries
- Motion filmstrips, band maps, GSAP timeline generation from captured motion
- Project scaffolding (Vite/Astro/Next) plus `verify_build` band/motion/perf scoring

## Architecture

MCP tool surface over a local/searchable Awwwards-oriented index plus Playwright-style capture/verification pipelines for arbitrary URLs. Search uses porter stemming and prefix matching with AND semantics for multi-word queries.

## Example usage

Typical agent loop: search ("dark 3D portfolio sites") → inspect design DNA → capture a reference URL → recreate sections → `verify_build`. Exact tool names and configs are in the README.

## Maintenance status

~362 stars, 18 forks, MIT, default branch `main`, latest release `v1.14.0`, homepage npm `awwwards-mcp`.
