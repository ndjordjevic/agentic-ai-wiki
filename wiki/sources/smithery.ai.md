---
type: source
category: "MCP servers & integrations"
source_url: https://smithery.ai/
tags: [mcp-registry, mcp-gateway, managed-oauth, agent-connections, service-tokens, mcp-triggers, mcp-tunnel, smithery-cli]
related: [monid.ai, skills.sh]
product: smithery
detail_level: standard
created: 2026-10-14
updated: 2026-10-14
---

Smithery is an MCP registry and managed-connection platform: a public catalog of thousands of Model Context Protocol servers (and a skills registry) plus a hosted "Connect" layer that lets an agent attach to any of them through one REST/MCP surface while Smithery handles OAuth, credential storage, token refresh, and session lifecycle. Its pitch is "give agents more agency" — connect a tool once, then reuse that connection across Claude, GPT, open-source models, chat agents, background agents, and CLI tools. For server authors it is also a distribution channel (server pages, scanning, analytics, verification). It matters to this wiki as the main hub where MCP servers are discovered, published, and wired into agents without each app re-implementing MCP auth plumbing.

_All claims below are sourced from ../../raw/web/smithery.ai.md unless otherwise noted._

## What it does

Smithery has two sides. **For agent builders (Use/Connect):** you create *connections* — long-lived sessions to MCP servers from the registry or any custom MCP URL — inside a *namespace*, and Smithery maintains the OAuth apps for popular integrations, stores credentials encrypted and write-only, refreshes tokens automatically, and manages reconnects and keepalives so your app stays stateless. Agents then list and call tools via the CLI, the `@smithery/api` SDK (which yields a transport usable by the Vercel AI SDK or the official MCP TypeScript SDK), plain REST, or a single namespace-wide MCP endpoint. **For server authors (Build/Publish):** you publish a remote server by URL (Smithery Gateway proxies to your upstream) or a local stdio server as an MCPB bundle; Smithery scans it to build a server page, renders a config/OAuth UI, handles spec compliance and caching in the gateway, and reports tool-call analytics. The landing page frames it as "Connect agents to thousands of tools and services. Auth, credentials, and sessions handled for you," with a rotating catalog of featured servers (Exa, Context7, Hugging Face, Tavily, OneSignal, and many niche ones) each showing usage counts and an "Add to toolbox" action.

## Key features

- **Zero OAuth configuration** — no redirect URIs, client IDs, or secrets; Smithery owns the OAuth relationship with upstream providers and sends users through a hosted `setupUrl`.
- **Automatic token refresh** — tokens refresh before expiry; a failed refresh flips the connection to `auth_required`.
- **Write-only credential vault** — credentials can be used to execute requests but never read back. The auth/credential layer is the open-source **agent.pw** "agent vault".
- **Multi-user connections** — tag connections with `metadata` (e.g. `userId`) and filter by it to give each end user their own integrations.
- **Namespace MCP endpoint** — `https://mcp.smithery.run/{namespace}` bundles every connection in a namespace behind one MCP URL; tool names are prefixed with the connection ID (`user-123-github.search_repositories`) and the endpoint advertises protected-resource metadata so clients run OAuth themselves.
- **Scoped service tokens** — short-lived (max 24h) tokens minted from an API key, restricted by namespace, resource, operation, and metadata, safe to hand to browsers, mobile apps, or untrusted agents.
- **Uplink** — expose an MCP server running on your own machine (local HTTP or a spawned stdio command) as a normal Smithery connection over a TLS WebSocket tunnel, without deploying it.
- **Triggers (preview)** — an `ai.smithery/events` MCP extension letting servers emit upstream events as signed webhooks delivered directly to the consumer.
- **Typed SDKs (preview)** — every published server gets a generated TypeScript package from `pkg.smithery.ai` (e.g. `@smithery/exa`) with typed tool calls validated against output schemas.
- **Skills registry** — search and install Agent Skills (`smithery skill add anthropics/frontend-design --agent claude-code`) alongside MCP servers.
- **LLM-friendly docs** — every docs page is available as `.md`, there is a docs `llms.txt`, and the docs themselves are served over MCP at `https://smithery.ai/docs/mcp`.

## Architecture and concepts

**MCP** is the underlying protocol: servers expose tools and context, clients (LLM apps) call them, over a transport that may be local (stdio) or remote (Streamable HTTP). Smithery sits between the two as registry plus broker. A **namespace** is a globally unique container (lowercase, hyphenated) that owns servers, connections, and skills and doubles as a shared team workspace, similar to a project ID; plans cap namespaces (Hobby 3, Pay as you Go 100, Custom 100+). A **connection** has a developer-defined or generated `connectionId`, stored credentials, optional `metadata`, and returned `serverInfo`, and reports one of four states: `connected`, `auth_required` (with `setupUrl`), `input_required` (with `setupUrl`, the config schema under `http`, and the `missing` fields), or `error`. Server config values are delivered either as headers (typically API keys) or URL query parameters, as declared by the server's schema via an `x-from` extension.

**Authentication** uses two credentials: backend-only **API keys** with full namespace access, and **service tokens** carrying a `policy` array of constraints over `namespaces`, `resources` (`connections`/`servers`/`namespaces`/`skills`), `operations` (`read`/`write`/`execute`), `metadata`, and `ttl`. Within a constraint, adding a field narrows (AND); adding list elements widens (OR); multiple constraints are independent grants. Child tokens can only narrow their parent.

**Uplink** works by having the CLI register an uplink-backed connection, open a persistent WebSocket scoped to it, and bridge JSON-RPC to the local process — transparent to MCP sessions, progress notifications, sampling/elicitation/roots, and streaming. Only one live tunnel per connection is allowed (`--force` takes over), and availability follows the host machine, so it is positioned as a development and personal-automation primitive, not hosting.

**Triggers** track the webhook slice of the MCP committee's draft events proposal: Smithery forwards the consumer's `delivery.url` and Standard Webhooks `delivery.secret` to the server's `ai.smithery/events/subscribe`, the server registers the upstream webhook and returns `{ id, refreshBefore }`, consumers re-subscribe before the TTL lapses (idempotent upsert), and events go server → consumer directly — Smithery is not in the delivery path, keeping trigger support serverless-friendly. Poll/push delivery, cursor replay, and delivery-status reporting are not implemented.

**Publishing** requires Streamable HTTP and (if auth is needed) OAuth support for URL servers; client registration uses MCP Client ID Metadata Documents. If scanning is blocked (auth walls, WAFs blocking `SmitheryBot/1.0` from Cloudflare Workers, or servers returning 403 instead of 401), authors can serve a static server card at `/.well-known/mcp/server-card.json` (SEP-1649). Published servers can then complete an official-vendor verification checklist.

## Main APIs

- **CLI** (`npm install -g smithery@latest`, Node 20+; source at `github.com/smithery-ai/cli`): `smithery auth login|logout|whoami|token`, `smithery mcp search|add|list|get|update|remove|publish`, `smithery tool list|find|get|call`, `smithery skill search|add`, `smithery namespace list|use|create`; `mcp add <server> --client claude|cursor` installs into a local client instead of creating a remote connection. Global flags `--json`, `--table`, `--verbose`.
- **TypeScript SDK** `@smithery/api`: `new Smithery()`, `smithery.connections.set(id, { namespace, mcpUrl, headers, metadata })`, `smithery.connections.list(namespace, { metadata })`, `smithery.namespaces.set/create`, `smithery.tokens.create({ policy })`, and `createConnection({ client, mcpUrl | connectionId, namespace })` from `@smithery/api/mcp`, which returns a transport (throws `SmitheryAuthorizationError` when OAuth is needed).
- **REST** at `api.smithery.ai` (servers, releases, runtime logs, skills, namespaces, tokens, team API keys) and `smithery.run/{namespace}/{connectionId}` for connections, plus per-connection tool listing/calling, namespace-wide tool listing, and trigger list/get/subscribe/unsubscribe endpoints. An OpenAPI spec is published.
- **MCP endpoints**: `https://mcp.smithery.run/{namespace}` (aggregated namespace), `https://server.smithery.ai/<server>` (hosted server URLs), and the `ai.smithery/events/{list,subscribe,unsubscribe}` extension methods for trigger-capable servers.

## When to use

Use Smithery when your app or agent needs to reach many third-party MCP servers on behalf of many users and you do not want to build OAuth flows, credential storage, token refresh, and session management for each one — especially in multi-tenant products where per-user connections and scoped browser-safe tokens matter. It is also the obvious place to find an MCP server for a task, to carry the same connected accounts across multiple agent harnesses via one namespace URL, or to test a local MCP server against a real agent via Uplink. As a server author, publish there for distribution, a config/OAuth UI, and usage analytics. Skip it when you only use one or two MCP servers you already host and authenticate yourself, or when you need event delivery modes beyond webhooks (Triggers are preview and webhook-only).

## Ecosystem

Smithery is the registry/broker layer of the MCP ecosystem: it fronts servers from vendors and the community (Exa, Context7, Browserbase, Desktop Commander, GitHub, Notion, Hugging Face, Tavily, and many long-tail servers) and its own packages such as the `smithery/mouseless` computer-use MCP. Its credential layer is the open-source agent.pw, its CLI is open source at `smithery-ai/cli`, and it integrates with the Vercel AI SDK and the official MCP TypeScript SDK; docs point to xmcp for building servers and Gram for hosting them, and to Anthropic's MCPB spec for local bundles. Within this wiki it overlaps most with [[monid.ai]], which also gives agents runtime access to many external tools behind one account (Monid as a metered data-API gateway, Smithery as an MCP connection broker), and with [[skills.sh]] on the Agent Skills registry side.
