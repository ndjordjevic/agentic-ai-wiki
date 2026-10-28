---
type: source
category: "Design & UI generation"
source_url: https://github.com/dembrandt/dembrandt
tags:
  - design-tokens
  - design-system-extraction
  - playwright
  - mcp-server
  - w3c-tokens
  - ci-drift-gate
  - cli
  - design-md
related:
  - dembrandt-dembrandt-skills
  - designmd.cc
  - voltagent-awesome-design-md
  - stitch.withgoogle.com
  - INSANE0777-Awwwards-mcp
  - AThevon-genjutsu
product: dembrandt
detail_level: standard
created: 2026-10-28
updated: 2026-10-28
---

Dembrandt (~3.9k★, MIT, TypeScript, v0.39.2) extracts a live website's design system into tokens in one command — logo, colors, typography, spacing, borders, shadows, motion, components — as W3C design tokens, with CI drift gates and an MCP server so agents can run extractions/comparisons.

_All claims below are sourced from ../../raw/github/dembrandt-dembrandt.md unless otherwise noted._

## What it does

Point Dembrandt at a URL; Chromium (via playwright-core) scans the site and writes a design-token style guide your agent can build from. Compare scans before/after edits to catch accidental visual drift. Pair with [[dembrandt-dembrandt-skills]] for UX judgment skills on top of the engine.

## Installation

```bash
npm install -g dembrandt
dembrandt install-browser   # required once — playwright-core ships no browser
dembrandt dembrandt.com
# or: npx dembrandt …
```

MCP install deep-links for Cursor/VS Code run `npx -y dembrandt mcp`. Requires Node 18+.

## Key features

- One-command design-system extraction to W3C tokens
- Logo/colors/typography/spacing/borders/shadows/motion/components
- MCP server for agent-driven extract/compare
- GitHub Marketplace "Drift Gate" Action for CI enforcement
- Browser install step via `dembrandt install-browser`

## Architecture

CLI + MCP over Playwright Chromium. Extraction is live-DOM based (not screenshot-only). Outputs feed agent workflows and CI; skills live in a separate repo.

## Example usage

```bash
dembrandt example.com
# agent: compare previous vs current scan after a UI edit
```

## Maintenance status

~3,871 stars, 335 forks, MIT, `main`, release `v0.39.2`, homepage http://dembrandt.com/.
