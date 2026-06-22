---
type: source
source_url: https://pumadb.ai/
tags:
  - agent-memory
  - mcp
  - rest-api
  - durable-state
  - typed-memory
  - server-side
related:
  - reseek.net
  - supermemory.ai
  - n8n.io
product: pumadb
detail_level: standard
created: 2026-06-22
updated: 2026-06-22
---

pumaDB is a hosted agent memory API for small server-side apps and agents. It combines durable JSON tables, a REST API, and a hosted Streamable HTTP MCP server so agents can store notes, preferences, research clippings, task state, and app records without running their own database.

_All claims below are sourced from ../../raw/web/pumadb.ai.md unless otherwise noted._

## What it does

pumaDB gives agents lightweight durable memory and safe structured storage. The same service supports direct REST calls from trusted backends and hosted MCP access for agent clients like Codex, Claude, and ChatGPT.

## Key features

- **Hosted MCP** — `https://api.pumadb.ai/mcp` with OAuth discovery and dynamic client registration.
- **REST API** — `https://api.pumadb.ai` for server-side code, CLIs, workers, and serverless routes.
- **Durable JSON tables** — rows get `id`, `created_at`, and `updated_at`; filters are top-level equality checks.
- **Recovery trail** — updates and deletes archive prior versions, and restore recreates deleted rows.
- **Typed safe memory** — `remember` tools store inert resources, code snippets, Markdown, commands, and config.
- **Secret hygiene** — `puma_live_*` keys stay on the server; browser-executed code is explicitly out of scope.

## Architecture and concepts

pumaDB splits usage into two paths:

1. **MCP for agents** — the hosted streamable HTTP endpoint exposes table tools and safe memory helpers to connected clients.
2. **REST for apps** — trusted backend code writes and reads JSON rows directly, using bearer auth from server-side environment variables.

The API is row-oriented rather than schema-heavy: tables are created implicitly by writes, queries use simple equality filters, and versioning is built in for undo/recovery workflows.

## Main APIs

| Endpoint | Purpose |
|---|---|
| `POST /v1/{table}` | Add a JSON row |
| `GET /v1/{table}` | Query rows with filter and limit |
| `POST /v1/{table}/batch` | Run atomic same-table writes |
| `POST /v1/{table}/update_row` | Update one row by id |
| `POST /v1/{table}/update_where` | Update rows by filter |
| `GET /v1/{table}/versions` | List archived row versions |
| `POST /v1/{table}/restore` | Restore an archived version |
| `GET /v1/_tables` | List tables and counts |
| `POST /v1/_row_links` | Create a short-lived row viewer/editor link |
| `POST /v1/_query_links` | Create a short-lived query viewer link |

## When to use

Use pumaDB when you need lightweight durable state for agents, notes, preferences, research clippings, task state, or application records without standing up a database. It is a good fit for backend routes, serverless functions, CLIs, and agent clients that can connect through MCP. It is not meant for client-side code that cannot keep API keys secret.

## Ecosystem

- **Docs** — `https://api.pumadb.ai/docs`
- **Install** — `https://api.pumadb.ai/install`
- **How to use** — `https://api.pumadb.ai/how-to-use`
- **Hermes guide** — `https://api.pumadb.ai/install/hermes`
- **Markdown instructions** — `https://api.pumadb.ai/llms.md`
- **Agent clients** — Codex, Claude, ChatGPT, and any MCP-capable tool that supports hosted Streamable HTTP servers
