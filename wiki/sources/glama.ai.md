---
type: source
category: "MCP servers & integrations"
source_url: https://glama.ai/
tags: [mcp-registry, mcp-gateway, mcp-hosting, mcp-inspector, tool-definition-quality-score, mcp-security-scanning, mcp-connectors]
related: [smithery.ai]
product: glama
detail_level: standard
created: 2026-10-14
updated: 2026-10-14
---

Glama is an MCP registry plus control plane. It indexes about 97.6k open-source MCP servers, 30.7k remote connectors, and nearly 1M individual tools. It calls itself a superset of the official MCP Registry. Every listed server is built in a sandbox, introspected, checked for malicious behaviour, and given a quality score. On top of the directory, Glama sells the production layer: a browser-based **MCP Inspector**, one-click **MCP hosting**, and an **MCP Gateway** that logs every JSON-RPC call, gates individual tools, and manages OAuth credentials. It also runs an older multi-model **Chat** workspace. The wiki tracks it as the main alternative to [[smithery.ai]] for finding MCP servers and running them in production. Its most distinctive feature is the security and quality vetting it applies to every listing.

_All claims below are sourced from ../../raw/web/glama.ai.md unless otherwise noted._

## What it does

Glama has three layers. The **directory** (`/mcp`) covers servers, connectors, clients, tools, categories, and attributes. It pulls from GitHub, the official MCP Registry, the awesome-mcp-servers list, and community submissions. Each server page has ready-to-paste config blocks for Cursor, Claude Desktop, Claude Code, and VS Code. You can search at the **tool** level (for example "query Postgres" or "send email"), not just by server. **Working tools** take a chosen server toward production: the Inspector tests it, Hosting deploys it, and the Gateway sits in front of the traffic. The **public API** at `glama.ai/api/mcp` exposes the whole dataset to other directories and tools, under attribution terms. Server authors list a server for free by pointing at a GitHub repo, or submit a remote connector by URL. They can then claim ownership of a listing through DNS or GitHub verification.

## Key features

- **Vetted registry** — every server is built from a Dockerfile, either the maintainer's or one inferred by AI. It then runs in a throwaway Firecracker microVM and is introspected (`tools/list`, `resources/list`, `prompts/list`, plus the `readOnlyHint`/`destructiveHint`/`idempotentHint`/`openWorldHint` annotations). Glama watches the server at the syscall and network level. If the build fails, the listing stays up but is hidden from search and recommendations.
- **Tool Definition Quality Score (TDQS)** — scores every tool from 1 to 5 on six dimensions: purpose clarity, usage guidelines, behavioral transparency, parameter semantics, conciseness, and contextual completeness. It also scores whether a server's tools fit together coherently and whether they match the server's stated purpose. Results are public, come with fix suggestions, and the scorer is open source (`glama-ai/tool-definition-quality-score`). Glama cites research showing that well-described tools are selected 260% more often, and that 97% of tools have at least one defect.
- **Connector drift and prompt-injection detection** — remote connectors are re-checked on a schedule using sandbox credentials. Each check's schema is compared with the previous one and kept as version history. Changes are scanned for instructions aimed at the LLM, role overrides, and exfiltration prompts, and findings are labeled *Malicious* or *Risky*.
- **MCP Gateway** — a reverse proxy that gives one URL (`glama.ai/endpoints/<id>/mcp`) for every server and connector you add. It provides managed OAuth 2.1 with automatic refresh, full JSON-RPC payload logs with JSON export for a SIEM, per-tool on/off control enforced at the gateway, and alerts when a server changes its tool definitions.
- **MCP hosting** — a dedicated machine for each deployment, `/ping` health checks that understand the MCP handshake, an optional `/data` volume, encrypted environment variables, live runtime logs, and tool-call analytics from 1 hour to 90 days. Deployments are private by default. You can make one public to get a directory listing, which Glama pitches as the advantage over Fly.io or Cloudflare Workers.
- **Online MCP Inspector** — free and needs no login. It connects to Streamable HTTP or SSE servers and covers tools, resources, resource templates, prompts, elicitation, sampling, roots, tasks, progress, cancellation, subscriptions, logging, completion, and pagination. For auth it supports OAuth 2.1, DCR, PKCE, bearer tokens, custom headers, and query-string keys. All state is stored in the URL, so a session can be bookmarked or shared.
- **Client directory and Chat** — a list of MCP-capable clients with the features each supports, plus the Glama Chat workspace. Chat offers side-by-side answers from several models, document Q&A, diagrams, request logs, and SOC 2 compliance.

## Architecture and concepts

**Servers vs. connectors.** A *server* is source code you can run, built from a GitHub repo. A *connector* is a remote deployment that someone already runs, with its own URL, transport, auth scheme, and advertised tools. Only approved connectors that are reachable over Streamable HTTP are listed. In the Gateway, a *connection profile* wraps one connector with your credentials and produces a dedicated endpoint. Access tokens are scoped to that profile, and logs are visible to workspace members according to their role.

**Indexing pipeline.**
1. The maintainer signs in with GitHub OAuth and must have write or admin access to the repo.
2. Glama clones the full Git history and keeps it in sync.
3. It builds the server in a Firecracker sandbox.
4. It introspects the running server.
5. It analyzes the server's behaviour, looking for access to credential paths, traffic to unexpected hosts, exfiltration-shaped payloads, forks into unrelated binaries, and writes outside the working directory.
6. It computes the TDQS scores.

Every commit or rebuild repeats steps 2–6, and Glama reports more than a million scans in the past year. Connectors skip the build step. Glama connects to them as an MCP client using sandbox credentials, and registers automatically when the connector supports OAuth DCR (RFC 7591). Each listing ends up with five signals: the full schema, the scores, a behavioural profile, change history, and a last-scanned timestamp.

**Gateway vs. proxy.** Glama defines a proxy as a pass-through for a single upstream server. A gateway adds tool-level access control, encrypted OAuth storage with refresh, `Mcp-Session-Id` lifecycle tracking, usage analytics, and full call logging. Credentials are encrypted with AES-256-GCM, each with its own IV, and are decrypted only at the moment of an upstream request. When a tool is disabled, the gateway returns a JSON-RPC error without forwarding the call. Because full payloads are logged, the docs warn users to mask sensitive arguments on the client side.

**Hosting** turns stdio servers into Streamable HTTP endpoints. It builds from a Dockerfile, an npm package, or a PyPI module, either through the Glama GitHub App (which reads `glama.json` or the Dockerfile) or straight from the registry. Crashed processes restart automatically. Billing is metered by machine hours and egress, on top of the workspace plan.

**Claiming and metadata.** Authors control how a repo is indexed through a `glama.json` file covering name, description, category, environment variables, and build spec. To claim a connector, the owner verifies a domain with a TXT record at `_glama-claim.<domain>` or a file at `/.well-known/glama.json`, or links a GitHub user or organization. One verification covers every connector under that domain or account, and domain verifications are re-checked daily. A connector's auth badge (`auth:none`/`api-key`/`basic`/`oauth2`) comes from the auth method declared on its test profile.

## Main APIs

- **MCP API** at `https://glama.ai/api/mcp/v1/...` uses bearer auth with `glm_...` keys and cursor pagination (`first`, `after`, `endCursor`, `hasNextPage`). Endpoint groups:
  - **Servers**: list, attributes, retrieve.
  - **Connectors**: list, attributes, retrieve.
  - **Instances**: the user's own hosted deployments.
  - **Telemetry**: anonymous tool-usage reporting with no auth.

  An OpenAPI spec is at `glama.ai/api/mcp/openapi.json`, and an RFC 9727 API catalog is at `/.well-known/api-catalog`. The rate limit is 100 requests per second per IP across all Glama APIs, reported in `RateLimit-*` headers. Exceeding it returns 429, and continuing returns a sticky 403. **Attribution is mandatory**: every page that shows the data needs a followable "Glama" credit, and every listed item must link to its Glama page. A commercial licence can waive this.
- **Gateway endpoints** follow the form `https://glama.ai/endpoints/<id>/mcp`. Paste one into Claude (Customize → Connectors), ChatGPT (Developer Mode → Apps & Connectors), Cursor (`~/.cursor/mcp.json`), or VS Code (`MCP: Add Server`).
- **Local tunnel** for testing stdio servers in the hosted Inspector: `npx mcp-proxy --port 8080 --tunnel [--tunnelSubdomain myapp] -- tsx server.js` creates a `*.tunnel.gla.ma` URL.
- **Schemas**: `glama.ai/mcp/schemas/server.json` defines `glama.json` for servers, and `glama.ai/mcp/schemas/connector.json` defines the connector claim file.

## When to use

Use Glama to choose an MCP server when you care about whether it is safe and well-built, not just whether it exists. The sandbox behaviour reports, drift and prompt-injection history, and TDQS breakdowns are the strongest signals here, and tool-level search helps when you know the capability but not the server. Use the Inspector to debug any remote MCP server quickly from the browser, including OAuth flows. Use the Gateway or Hosting when a team runs MCP in production and needs one governed endpoint with a call audit trail, the ability to switch off individual tools, and managed credentials. Use public hosting when you want a server on a directory people already search. Use the API to build your own MCP catalog, and accept the attribution requirement if you do. Look elsewhere for local stdio development (the official `@modelcontextprotocol/inspector` fits better) or for SDK-level, multi-tenant connection brokering per end user, where [[smithery.ai]]'s namespaces, metadata-tagged connections, and scoped service tokens are a closer fit.

## Ecosystem

Glama sits next to the official MCP Registry, which is vendor-neutral and run by the MCP steering group. Glama mirrors that registry and adds its own analysis on top. The awesome-mcp-servers list (`punkpeye/awesome-mcp-servers`) is one of the directory's data sources. The indexing pipeline is maintained by Frank Fiegel and contributors in the `glama-ai` GitHub org, and the `mcp-proxy` package provides the tunnel. Popular listings include Filesystem, Context7, codebase-memory-mcp, Playwright MCP, cognee-mcp, BlenderMCP, and Serena. Hosted connectors include Linear, Stripe, and PostHog. Glama works with the major MCP clients: Claude Desktop and Claude Code, ChatGPT, Cursor, Windsurf, Zed, VS Code, JetBrains, Replit, and Sourcegraph. Within this wiki it overlaps most with [[smithery.ai]]. Both are MCP registries with a managed OAuth and credential layer. Smithery leans toward SDK-driven, per-user connection brokering, while Glama leans toward vetting and quality scoring, a governed gateway with call logs, and one-click hosting.
