---
type: source
category: "Browser & web automation"
source_url: https://github.com/responsively-org/responsively-app
tags:
  - responsive-design
  - browser-devtools
  - mcp-server
  - multi-device-preview
  - screenshots
  - electron
  - coding-agents
  - agpl-3
related:
  - INSANE0777-Awwwards-mcp
  - dembrandt-dembrandt
  - microsoft-playwright-mcp
  - browse.sh
  - Ying-Kai-Liao-jev-browser
product: responsively
detail_level: standard
created: 2026-10-28
updated: 2026-10-28
---

Responsively App (~25.5k★, AGPL-3.0, TypeScript) is a modified browser/devtool for side-by-side multi-device responsive web development; it now ships a built-in MCP server (`@responsively/mcp`) so coding agents can load a local site, switch device previews, interact, and verify layouts with per-device screenshots.

_All claims below are sourced from ../../raw/github/responsively-org-responsively-app.md unless otherwise noted._

## What it does

Shows your site at several screen sizes at once for faster responsive work, and exposes that surface to AI agents via MCP so they can screenshot each view, fix layout breaks, and re-check — keeping AI-built desktop layouts from failing on phones/tablets.

## Installation

Download/install the desktop app from https://responsively.app / GitHub releases (latest noted `v2.0.0-beta.0`). Then connect an agent:

```bash
claude mcp add responsively -- npx -y @responsively/mcp
```

Or Cursor `.cursor/mcp.json` with `npx -y @responsively/mcp`. The app launches on demand on first tool call (HTTP MCP at `http://127.0.0.1:12720/mcp`).

## Key features

- Multi-device side-by-side preview browser for responsive development
- Built-in MCP for Claude Code / Cursor / compatible agents
- Per-device screenshots and interactive verification loops
- Localhost-only MCP listener; env overrides `RESPONSIVELY_MCP_PORT` / `RESPONSIVELY_MCP_BRIDGE`

## Architecture

Electron-based modified browser plus an on-demand MCP bridge package `@responsively/mcp` that talks to the running app's local MCP HTTP endpoint. Repo also contains a `responsively-mcp` top-level package path.

## Example usage

Launch the app once (especially on Linux AppImage so the CLI learns its location), add the MCP server to your agent, point it at a local dev URL, and ask it to screenshot phone/tablet/desktop and fix overflow.

## Maintenance status

~25,495 stars, 1,422 forks, AGPL-3.0, `main`, release tag `v2.0.0-beta.0`, homepage https://responsively.app.
