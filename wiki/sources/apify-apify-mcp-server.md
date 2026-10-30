---
type: source
category: "MCP servers & integrations"
source_url: https://github.com/apify/apify-mcp-server
tags:
  - mcp-server
  - apify-store
  - web-scraping
  - actor-tools
  - oauth
  - stdio-http
  - data-extraction
  - agent-marketplace
related:
  - firecrawl.dev
  - browse.sh
  - browser-use.com
  - tavily.com
  - serper.dev
product: apify-mcp-server
detail_level: standard
created: 2026-10-30
updated: 2026-10-30
---

The official Apify Model Context Protocol server connects AI agents to Apify Store — thousands of ready-made Actors for web scraping, SERP monitoring, lead enrichment, e-commerce, social media, and browser-style automation — through one MCP connection at `https://mcp.apify.com` (hosted OAuth) or the local npm package `@apify/actors-mcp-server` (stdio). Agents search the store, inspect Actor schemas and pricing, run Actors, and read structured dataset results without installing a separate MCP server per site.

_All claims below are sourced from ../../raw/github/apify-apify-mcp-server.md unless otherwise noted._

## What it does

Actors on the Apify platform become MCP tools. A typical agent loop: `search-actors` → `fetch-actor-details` (input schema, README, pricing) → `call-actor` (returns run status and storage IDs; default wait 30s, up to 45s) → `get-dataset-items` (paginated results). Loading `call-actor` or an Actor tool also exposes `get-dataset-items`, `get-key-value-store-record`, `get-actor-run`, and `abort-actor-run`. Specific Actors can be exposed as named tools (e.g. `apify/web-search`); Actors that are themselves MCP servers are reached via `fetch-actor-mcp-tool-list` / `call-actor-mcp-tool`.

Default load includes the `actors` and `docs` categories, two Actor tools (RAG Web Browser and Web Fetch), and `report-problem` (telemetry-gated for some clients). Everything else is opt-in by category or tool name via the `tools` parameter.

## Installation

**Hosted (recommended):** open the [MCP configurator](https://mcp.apify.com), pick a client, copy config, and sign in with OAuth. Endpoint: `https://mcp.apify.com`. Clients that cannot OAuth may send `Authorization: Bearer <APIFY_TOKEN>`.

**Claude Code:**

```bash
claude mcp add apify "https://mcp.apify.com" -t http
```

**Cursor / multi-client via Apify CLI:**

```bash
apify mcp install cursor
```

(Same pattern for `claude-code`, `vscode`, `codex`, `kiro`, `antigravity`.)

**VS Code / generic HTTP config:**

```json
{
  "servers": {
    "apify": {
      "type": "http",
      "url": "https://mcp.apify.com"
    }
  }
}
```

**Local stdio** (Node.js 22+):

```json
{
  "mcpServers": {
    "actors-mcp-server": {
      "command": "npx",
      "args": ["-y", "@apify/actors-mcp-server"],
      "env": {
        "APIFY_TOKEN": "YOUR_APIFY_TOKEN"
      }
    }
  }
}
```

Also listed in the Docker MCP catalog; releases ship an `apify-mcp-server.mcpb` bundle. Stdio-only clients can bridge to the hosted server with `npx mcp-remote https://mcp.apify.com`. An official Apify Claude Code plugin can install this MCP server together with Apify agent skills.

## Key features

- **Store-backed tool marketplace** — one connection, dynamic discovery of Actors instead of per-site MCP installs
- **Hosted vs local** — Streamable HTTP + OAuth (or Bearer) at mcp.apify.com; local stdio via npm; Actors always run on Apify in both modes
- **Tool selection** — `?tools=` / `--tools` for categories, tool names, and Actor names; pin tools in production because defaults can change
- **Platform helpers** — docs search/fetch, runs/logs/storage, tasks & schedules, builds & versions, Apify API search/read/write
- **MCP Apps UI mode** — optional widget tools (`search-actors-widget`, `fetch-actor-details-widget`) via `ui` parameter
- **Cost controls** — `maxTotalChargeUsd` / `maxItems` in `call-actor` options; connecting is free, Actor runs bill to the Apify account
- **Partial no-auth discovery** — selected search/docs/API detail tools work without a token when only those tools are selected
- **Telemetry opt-out** — on by default (`telemetry-enabled=false` / `TELEMETRY_ENABLED=false`)

## Architecture

Open-source package `@apify/actors-mcp-server` (this repo) implements the server core; the hosted service at mcp.apify.com runs that logic from a separate private repository. Transport: Streamable HTTP remotely, stdio locally. Hosted mode can infer output schemas for Actor results; local mode does not.

Tool loading is category- and name-driven; selecting an Actor or `call-actor` auto-adds the run/storage helpers (⚡). Tool annotations include `title`, `readOnlyHint`, and `openWorldHint`. `resources/read` accepts Apify API GET URLs (inlined up to 256 KB); no prompts are registered yet. Actor input schemas are adapted for client compatibility (truncated long descriptions, enum size limits, REQUIRED prefixes, nested special inputs, inferred array item types).

## Example usage

Tool selection on the hosted URL:

```text
https://mcp.apify.com?tools=actors,docs,apify/web-search,apify/web-fetch
https://mcp.apify.com?tools=apify/instagram-scraper
```

Local equivalent:

```bash
npx @apify/actors-mcp-server --tools actors,docs,apify/web-search,apify/web-fetch
```

Example agent prompts from the README: summarize X posts about autonomous AI agents; compare Notion/Coda/Airtable pricing; top Google SERP for a query; dentists on Google Maps in Austin; LinkedIn profile/company scrapes; Instagram/TikTok monitoring; Amazon product lists; crawl a docs site to Markdown for RAG.

## Maintenance status

13,878 GitHub stars, 409 forks, TypeScript, MIT License, default branch `master`, latest release 0.20.0 (2026-10-29), homepage https://mcp.apify.com. Requires Node.js 22+; developed with pnpm. Bug reports and docs PRs welcome; unsolicited code PRs are closed unless a maintainer invites work on an issue. Docs: https://docs.apify.com/mcp.
