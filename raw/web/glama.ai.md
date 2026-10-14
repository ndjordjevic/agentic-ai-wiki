# glama.ai

## Fetch log
- Inbox URL: https://glama.ai/
- Final URL: https://glama.ai/
- Fetched: 2026-10-14
- Pages: 9
- Mode: standard

## llms.txt — https://glama.ai/llms.txt
# Glama

> A directory of 97,619 Model Context Protocol servers and 30,699 remote connectors, every one scanned, scored, and testable in the browser. A superset of the official MCP Registry.

Glama indexes MCP servers and clients, inspects each one, and publishes the result as web pages and as a public API. The catalog is far too large to enumerate here. Search it through the MCP API rather than by crawling.

## Programmatic access

- [MCP API reference](https://glama.ai/mcp/reference): REST API over the directory. Search servers, read their tools, scores, and hosting attributes.
- [MCP API OpenAPI description](https://glama.ai/api/mcp/openapi.json): OpenAPI description of the MCP API, for generating a client.
- [API catalog](https://glama.ai/.well-known/api-catalog): RFC 9727 linkset naming every Glama API alongside its description document.

## Directory

- [MCP directory](https://glama.ai/mcp): Search, compare, and connect to MCP servers, connectors, clients, and tools.
- [MCP servers](https://glama.ai/mcp/servers): 97,619 MCP servers indexed from GitHub, the official MCP Registry, and community submissions, each scanned and scored.
- [MCP connectors](https://glama.ai/mcp/connectors): 30,699 remote MCP servers reachable over Streamable HTTP, with no local installation.
- [MCP clients](https://glama.ai/mcp/clients): Applications that speak MCP: editors, chat clients, and agents.
- [MCP tools](https://glama.ai/mcp/tools): 988,329 tools exposed by servers in the directory, searchable by name and purpose.
- [Categories](https://glama.ai/mcp/categories): Servers grouped by what they do.
- [Attributes](https://glama.ai/mcp/attributes): Servers filtered by license, hosting model, transport, and other properties.

## Working with MCP servers

- [MCP Inspector](https://glama.ai/mcp/inspector): Test any MCP server from the browser, including tools, resources, prompts, tasks, elicitation, sampling, and OAuth 2.1.
- [MCP Gateway](https://glama.ai/mcp/gateway): A reverse proxy between AI clients and MCP servers, with call logging, per-tool access control, managed OAuth credentials, and usage analytics.
- [MCP hosting](https://glama.ai/mcp/hosting): Deploy MCP servers on dedicated infrastructure with a built-in gateway, call logs, per-tool access control, and directory distribution.
- [Chat](https://glama.ai/chat): Privacy-first AI workspace: chat across models with MCP servers attached.

## How the directory works

- [Ranking methodology](https://glama.ai/mcp/methodology): How servers are discovered, scanned, scored, and ranked.
- [MCP FAQ](https://glama.ai/mcp/faq): Common questions about MCP and about this directory.
- [glama.json schema](https://glama.ai/mcp/schemas/server.json): JSON Schema for the glama.json a repository commits to claim and maintain its server listing.
- [Connector schema](https://glama.ai/mcp/schemas/connector.json): JSON Schema for claiming a remote connector listing.
- [Support](https://glama.ai/support): Contact us about the directory, a listing, or an account.

## Optional

- [Blog](https://glama.ai/blog): Long-form writing on MCP, agents, and the directory.
- [Terms of service](https://glama.ai/policies/terms-of-service): Terms governing use of Glama.
- [Privacy policy](https://glama.ai/policies/privacy-policy): How we handle personal data.
- [Vulnerability disclosure](https://glama.ai/policies/vulnerability-disclosure): How to report a security vulnerability.
## Landing page — https://glama.ai/

The MCP Server Registry, Inspector & Gateway | Glama

# Every MCP server, in one registry

A superset of the official MCP Registry – every server scanned, scored, and testable in your browser.

97,619 MCP servers · 30,699 MCP connectors · 988,329 MCP tools · Last indexed Oct 14, 2026

## Popular on Glama

Run an open-source server yourself, or plug into a hosted connector someone else already runs.

The most-starred servers in the registry, each scanned and quality-scored. Free to browse and install locally; paid to host on Glama.

- Filesystem MCP Server — Node.js server implementing Model Context Protocol (MCP) for filesystem operations. 91K
- Context7 MCP — A Model Context Protocol server that fetches up-to-date, version-specific documentation and code examples from libraries directly into LLM prompts, helping developers get accurate answers without outdated or hallucinated information. 63K
- codebase-memory-mcp — High-performance code intelligence MCP server. Indexes codebases into a persistent knowledge graph — average repo in milliseconds. 159 languages, sub-ms queries, 99% fewer tokens. Single static binary, zero dependencies. 46K
- Playwright MCP Server — A Model Context Protocol server that enables LLMs to interact with web pages through structured accessibility snapshots without requiring vision models or screenshots. 38K
- cognee-mcp — Memory manager for AI apps and Agents using various graph and vector stores and allowing ingestion from 30+ data sources. 32K
- AIHawk — Enables assistants such as Claude Code, Codex, and Gemini CLI to drive a real browser over MCP — navigating, clicking, typing, and reading live pages from plain-English instructions. Supports optional proxy routing, persistent profiles for surviving logins, and reproducible browser identities via seeds. 32K
- BlenderMCP — Connects Blender to Claude AI through the Model Context Protocol (MCP), allowing Claude to directly interact with and control Blender for AI-assisted 3D modeling, scene manipulation, and rendering. 30K
- Serena — A fully featured coding agent that uses symbolic operations (enabled by language servers) and works well even in large code bases. Essentially a free to use alternative to Cursor and Windsurf Agents, Cline, Roo Code and others. 30K

Explore all 97,619 servers →

Remote endpoints that work in Claude, ChatGPT, Cursor, and VS Code. Free to use – connect directly, or through the Glama Gateway for auth and logs.

## Find a server by topic

Browse a category, or jump straight to a ranked shortlist rebuilt every week.

## From first test to production

Everything you need once you have picked a server.

- Test in your browser — Paste a server URL and debug it in an ephemeral sandbox – list tools, call them, and watch the raw JSON-RPC. No install. (Open the Inspector)
- Host in one click — Deploy an open-source server in one click. Glama runs it on dedicated infrastructure and handles the Docker, TLS, and OAuth plumbing. (Explore hosting)
- Control every call — One endpoint in front of every server and connector your agents use – with call logs, per-tool access control, and managed OAuth credentials. (See how the Gateway works)

## MCP questions, answered

(Same Q&A as the FAQ page below: What is an MCP server? / What are MCP connectors? / How do I add an MCP server to Claude Desktop or Claude Code? / How is Glama different from the official MCP registry?)

## Building an MCP server?

List it for free. Glama indexes every tool, and visitors can try it in the Inspector without installing anything.

## MCP Gateway — https://glama.ai/mcp/gateway

# MCP Gateway

Every MCP call from your agents flows through Glama – so you know exactly what your AI is doing, and you decide what it's allowed to do.

MCP Client → Glama MCP Gateway → MCP Server. Every call logged · Every tool gated · Every credential managed

## What is an MCP Gateway?

An MCP Gateway is a reverse proxy that sits between AI clients and MCP servers. It appears as an MCP server to the client while acting as an MCP client to the upstream server. Without a gateway, every agent manages its own connections to every server – a tangled point-to-point mess that breaks at enterprise scale. The Glama MCP Gateway consolidates all of that into one control plane where every call is visible, auditable, and revocable.

## Route any MCP endpoint

The Gateway is source-agnostic. It fronts every kind of MCP endpoint with the same logging, access control, credential management, and analytics:

- Open-source MCP servers hosted on Glama — Deploy any server from the registry to Glama's infrastructure in one click. The Gateway fronts it automatically.
- Hosted MCP connectors — Pre-indexed remote services like Linear, Stripe, and PostHog. Connect through the Gateway for centralized auth, call logging, and per-tool access control.
- Any remote MCP server — Any MCP endpoint you already run or want to use – bring your own credentials, point the Gateway at the URL, and route the traffic through your control plane.

## How to connect

### Open-source servers hosted on Glama

1. Pick a server from the registry.
2. Click Deploy on Glama – Glama builds and hosts it on dedicated infrastructure.
3. A Gateway endpoint is generated automatically when the deployment is healthy.
4. Paste the URL into Claude, Cursor, ChatGPT, or VS Code.

`https://glama.ai/endpoints/<id>/mcp` — Every call through this URL is logged, access-controlled, and credential-managed automatically.

### Hosted MCP connectors

Option 1 – Direct: use the connector's native endpoint (`https://mcp.<vendor>.com/mcp`). Fastest path, but you manage credentials and have no logging or access control.

Option 2 – Through the Glama Gateway: create a connection profile for the connector. You get a dedicated URL (`https://glama.ai/endpoints/<id>/mcp`) backed by call logging, per-tool access control, managed OAuth, and usage analytics.

## What you get

- Unified access — One URL fronting every connector you add, no setup per client; Managed OAuth 2.1 with automatic refresh
- Full observability — Every JSON-RPC message logged with full payloads; JSON export of the audit log for your SIEM
- Tool-level control — Per-tool access control enforced at the gateway; Alerts when a server changes its tool definitions

## Gateway vs. proxy

An MCP proxy is a thin pass-through: a JSON-RPC request comes in, gets forwarded upstream, and a response goes back. A gateway keeps the proxy and layers access control, encrypted OAuth storage with automatic token refresh, session lifecycle tracking, aggregated usage analytics, and full call logging on top. Use a proxy for basic routing against one upstream server. Use the Glama MCP Gateway when you are running MCP at scale and need governance.

## MCP hosting — https://glama.ai/mcp/hosting

# MCP Server Hosting

Deploy private or public MCP servers on dedicated infrastructure – with a gateway, call logs, per-tool access control, and directory distribution built in.

## Running an MCP server in production is deceptively hard

You need authentication that matches the MCP specification, TLS that terminates correctly for Streamable HTTP, session handling that does not break behind a load balancer, OAuth credential refresh, per-user rate limits, secret rotation, audit logs, and runtime monitoring that understands JSON-RPC.

A 2026 scan of 2,181 remote MCP endpoints found 52% completely dead and only 9% healthy. A separate 2025 scan of internet-exposed MCP servers found 100% missing authentication entirely.

Glama has operated more than 20,000 MCP server instances.

## What you get on day one

- Container infrastructure, purpose-built for MCP — Dedicated machines per deployment; Health checks against /ping with retry-on-failure; Optional persistent volumes mounted at /data
- Gateway in front of every deployment — OAuth 2.1 credentials managed with automatic refresh; Per-tool access control; Every JSON-RPC call logged with full payloads for audit
- Observability built for MCP — Runtime logs tailed live from the machine; Tool-call analytics across 1h, 24h, 7d, 14d, 30d, 90d windows; Automated health tests that understand the MCP handshake
- Secure by default — Environment variables encrypted at rest; Access tokens scoped to connection profiles; Private by default – flip to public listing when ready

## Three ways to deploy

- From the registry — Browse /mcp/servers, pick a server, click Deploy on Glama, paste the generated Gateway URL into your client.
- From GitHub — Install the Glama GitHub App on your organization; pick a repository; Glama reads glama.json or your Dockerfile; deploy on demand and roll back by redeploying an earlier build.
- From a package or image — Point at a Dockerfile, an npm package, or a PyPI module; set environment variables (encrypted at rest); Glama provisions a machine and issues a Gateway endpoint.

## Private by default. Public when you're ready.

Private deployment: endpoint gated by connection-profile access tokens; shared with workspace members by role; not indexed or listed. Right answer for internal CRM, Jira, or Confluence MCP servers.

Public deployment: listed in the Glama directory under your account; indexed by tool search; shown on category, integration, and client pages. Right answer for SaaS vendors shipping an MCP server to their users.

Directory distribution is unique to Glama. Fly.io, Cloudflare Workers, and self-hosted stacks give you compute; they do not give you a place to be found.

## How Glama compares

Comparison table vs Fly.io, Cloudflare Workers, Self-hosted on: container hosting, Docker image support, one-click deploy from an MCP registry, gateway included (auth · ACL · call logs), managed OAuth 2.1 with refresh, tool-level analytics, MCP-aware health checks, browser-based inspector/playground, public directory listing with SEO, encrypted environment variables. (Glama claims all; Fly.io/Cloudflare offer generic metrics and generic HTTP health checks; Cloudflare's gateway is a separate product.)

## Hosting questions, answered

- Private by default; access tokens issued per connection profile.
- Public endpoint speaks Streamable HTTP; stdio servers are wrapped automatically.
- Runtimes: Dockerfile, npm, PyPI; custom build steps and CMD arguments configurable.
- GitHub App deploys; redeploys from dashboard or webhook.
- Paste the Gateway URL into Claude, Cursor, ChatGPT, VS Code, Zed as a streamable-http endpoint.
- Env vars encrypted at rest with a server-side key, decrypted in memory only at start; access tokens hashed.
- Team access via workspace roles.
- Crashes: retry-on-failure restart policy + /ping health check; unhealthy deployments surface in analytics.
- Hosting runs your code; the Gateway fronts the traffic — same control plane.
- Public deployments can be switched back to private at any time; connected users lose access immediately.
- Pricing: billed on top of workspace plan; metered by machine hours and egress.

## Ranking methodology — https://glama.ai/mcp/methodology

# How Glama indexes the MCP ecosystem

Glama's registry is not a passive directory. Every server – open-source or hosted connector – passes through an automated analysis pipeline that builds, runs, introspects, audits, and scores it, and repeats that process for as long as the server exists. Over one million scans in the preceding twelve months.

### 1.1 Maintainer verification
Submitting maintainer authenticates through GitHub OAuth; Glama verifies write/admin access to the repository.

### 1.2 Source ingestion
Glama clones and continuously syncs the complete Git history; registry reflects repository state within minutes of a push; every tag and commit remains inspectable.

### 1.3 Sandboxed build and execution on Firecracker
Each server is built from a Dockerfile – authored by the maintainer or inferred by Glama's AI-assisted build system – and runs inside an isolated Firecracker microVM with ephemeral filesystem and network. If the inferred build fails, the profile page is preserved but distribution is withheld (not in search, categories, or recommendations) until a reproducible build succeeds.

### 1.4 Protocol introspection
`tools/list`, `resources/list`, `prompts/list` and schema endpoints; full JSON Schema captured including MCP annotation hints (`readOnlyHint`, `destructiveHint`, `idempotentHint`, `openWorldHint`).

### 1.5 Behavioural analysis
Process observed at syscall and network layers. Representative patterns: access to credential paths not required (SSH keys, cloud creds, browser cookies); outbound traffic to hosts not in manifest/source; exfiltration payload signatures; process forks into unrelated binaries; filesystem writes outside the working directory. Findings classified Malicious (internal review, possible de-listing) or Risky (surfaced on public listing).

### 1.6 Tool Definition Quality Score (TDQS)
Six dimensions, each 1–5: Purpose Clarity, Usage Guidelines, Behavioral Transparency, Parameter Semantics, Conciseness, Contextual Completeness; rolled into an overall tier. Derived from research (856 tools across 103 servers; survey of 10,831 MCP servers): well-described tools selected 260% more often; 97% of tools have at least one defect, 56% lack clarity on what the tool does, 89% omit usage constraints. Also scored at two higher levels: tool-set coherence and server cohesiveness (stated purpose vs exposed capabilities).

### 1.7 Score transparency
Full per-dimension breakdowns shown publicly with gap analysis and suggestions. TDQS is open source: github.com/glama-ai/tool-definition-quality-score.

### 1.8 Re-scan cadence
Every new commit and rebuild re-runs 1.2–1.6.

## 2. Hosted MCP connectors
2.1 Authenticated sandbox connection using maintainer-provided sandbox credentials (never production); OAuth 2.1 DCR (RFC 7591) connectors auto-registered. 2.2 Scheduled introspection against the `streamable-http` endpoint. 2.3 Schema drift and prompt-injection detection — each sweep diffed against the previous, versioned history kept, diffs analyzed for LLM-directed instructions, role overrides, exfiltration prompts. 2.4 Payload monitoring of sandbox JSON-RPC traffic including response bodies. 2.5 TDQS for connectors, updated every sweep.

## 3. Relationship to the official MCP Registry
Glama is a superset: ingests and re-publishes everything in the official registry and layers sandbox-derived data on top (behavioural analysis, schema captures, TDQS, drift history, quality annotations). Available via public API at glama.ai/mcp/reference.

## 4. What this produces
Five signals per entry: full capability schema; TDQS + tool-set coherence + server cohesiveness scores; behavioural profile; schema/behaviour change history; last-scanned timestamp. "A directory tells you a server exists; a registry tells you what it is."

Pipeline built and maintained by Frank Fiegel and contributors; codebases at github.com/glama-ai.

## MCP Inspector — https://glama.ai/mcp/inspector

# MCP Inspector Online

Test and debug MCP servers directly in your browser: call tools, read resources, explore prompts, troubleshoot authentication. No installation or Glama account required. Connects to remote Streamable HTTP and SSE endpoints. State persisted in URL for sharing/bookmarking; connect through the built-in proxy or directly to servers that allow browser requests; extra debug info in the browser console.

## How to test an MCP server online
1. Add Server with name and HTTP/SSE endpoint URL.
2. Configure authentication: OAuth, bearer token, or custom headers.
3. Connect to discover tools, resources, and prompts.
4. Open Tools, enter arguments, run.

## Glama vs. the official MCP Inspector
Glama: browser-based, remote servers, no install, Streamable HTTP and SSE, OAuth debugging. Official (`npx @modelcontextprotocol/inspector`): local development, launches stdio servers directly. To test stdio with Glama, expose via HTTP proxy + tunnel.

## Supported MCP Features
- Core primitives: Tools, Resources, Resource Templates, Prompts
- Server → client requests: Elicitation, Sampling, Roots
- Long-running operations: Tasks, Progress Notifications, Cancellation
- Real-time updates: Resource Subscriptions, List-changed Notifications, Logging
- Utilities: Ping, Completion, Pagination
- Authentication: OAuth 2.1, Dynamic Client Registration (DCR), PKCE, Bearer Token, Custom Headers, Search Params
- Transports: Streamable HTTP, SSE (legacy), Local stdio via mcp-proxy public tunnel
- Content types: Text, Images (PNG, JPEG, WebP), Audio (WAV, MP3), Embedded Resources

## Expose Local MCP Servers

```
npx mcp-proxy --port 8080 --tunnel -- tsx server.js
npx mcp-proxy --port 8080 --tunnel --tunnelSubdomain myapp -- tsx server.js
# tunnel established at https://bright-wombat-83.tunnel.gla.ma
```

## Bookmarkable URLs
URL parameters: `servers` (JSON array of server configs), `active`, `tab` (`tools`, `resources`, `resource-templates`, `prompts`), `tool`, `args`. Configurations can include credentials — remove secrets before sharing.

## MCP API reference — https://glama.ai/mcp/reference

# Build with the MCP directory

Base URL `https://glama.ai/api/mcp` — Bearer authentication / 100 requests per second / cursor pagination.

```
export GLAMA_API_KEY='glm_...'
curl --request GET \
  --url 'https://glama.ai/api/mcp/v1/connectors?first=10&sort=recommended%3Adesc' \
  --header "Authorization: Bearer $GLAMA_API_KEY"
```

Directory read endpoints require an API key; the usage telemetry endpoint is unauthenticated so MCP clients can report tool usage without a Glama account.

Rate limits: 100 req/s per IP across all Glama APIs; ten consecutive rejections earn a temporary ban. IETF draft headers `RateLimit-Limit`, `RateLimit-Remaining`, `RateLimit-Reset`. 429 `rate_limit_exceeded`, then 403 `forbidden` (does not clear on its own).

## Attribution is required
Data is licensed under the API Data License: every page displaying API data must carry a visible, followable credit link to https://glama.ai (no nofollow/sponsored/ugc), and every server or connector shown must link to its own Glama listing (the `url` the API returns). Attribution can be waived under a commercial licence.

## Data Sources
Community submissions; automated discovery with manual curation; integration with the Official MCP Server Registry; Awesome MCP Servers list (github.com/punkpeye/awesome-mcp-servers).

Endpoint groups:
- Servers: List MCP servers; MCP server attributes; Retrieve an MCP server by ID; Retrieve an MCP server
- Connectors (remote MCP servers — only approved connectors reachable over streamable HTTP): List; Attributes; Retrieve
- Instances: Hosted MCP server instances (user-owned, not public)
- Telemetry: Anonymous MCP tool usage reporting

## Chat — https://glama.ai/chat

All-in-one AI workspace. "Trusted by 50,000+ Businesses and Professionals."

- One Question, Multiple AI Perspectives — compare responses side-by-side.
- Turn Mountains of Documents into Instant Insights (Pro/Business) — upload PDF, Word, text; answers with page references.
- Never Lose Important Information Again — search across documents and chats; save and tag conversations.
- Visualize Complex Ideas Instantly (Pro/Business) — text to diagrams.
- Breakdown and Solve Math Problems (Pro/Business) — KaTeX output.
- Future-Proof Your AI Strategy — instant access to new models (GPT, Claude, Gemini, ...).
- Everything Has A Shortcut — keyboard shortcuts.
- Compose Faster With A Modern Editor.
- Your Data is Safe — AES 256, TLS 1.2+, SOC 2 compliance, never used for AI training.
- Built for Seamless Teamwork — share resources (private by default), track usage, manage access, consolidated billing.
- Complete Transparency with Detailed Logs — every model request logged; export logs to JSON.

## MCP FAQ — https://glama.ai/mcp/faq

MCP FAQ – questions about the protocol, the registry, and the Gateway | Glama

# MCP questions, answered

Answers to the most common questions about Model Context Protocol (MCP) servers, connectors, hosting, and the Glama MCP Gateway.

What is an MCP server?

An MCP server is a small program that exposes tools, resources, and prompts to an AI client over the Model Context Protocol. It speaks `JSON-RPC 2.0` over `stdio`, Server-Sent Events, or Streamable HTTP – and once connected, the AI can call any tool the server defines.

MCP-compatible clients include Claude Desktop, Claude Code, ChatGPT, Cursor, Windsurf, VS Code, Zed, and JetBrains IDEs. One MCP server works across all of them – you install it once, every client can use it.

Glama indexes every MCP server in the ecosystem – browse by category, search across every tool they expose, or deploy a hosted connector in one click.

How do I add an MCP server to Cursor?

Open Cursor Settings → Features → MCP → + Add New MCP Server, or edit `~/.cursor/mcp.json` directly. Each server takes a `command`, an `args` array, and an optional `env` map – for example, `command: "npx"` with `args: ["-y", "@example/mcp-server"]`.

Pick any server from the Glama registry – each server page shows the exact JSON block to paste, pre-filled for Cursor, Claude Desktop, Claude Code, and VS Code. To test a remote server before adding it, use the Glama MCP Inspector – no install required.

How do I add an MCP server to Claude Desktop or Claude Code?

In Claude Desktop, open Settings → Developer → Edit Config – that opens `claude_desktop_config.json`. Add your server under the `mcpServers` key using the same `command`/`args`/`env` structure Cursor uses, then quit and relaunch Claude Desktop.

In Claude Code, run `claude mcp add ` from your terminal – it writes the entry to your project's MCP config directly.

Every server on the Glama registry ships with a pre-filled config block for both clients – copy it, paste it, done. To test a server remotely before wiring it up, open the Glama MCP Inspector and point it at the server URL.

Why won't my MCP server start?

Three causes account for almost every "MCP server won't connect" report:

- Missing `-y` flag – `npx` refuses to auto-install without it. Change `"args": ["@example/mcp-server"]` to `"args": ["-y", "@example/mcp-server"]`.
- Windows path escaping – inside `claude_desktop_config.json`, use forward slashes (`C:/Users/...`) or doubled backslashes. Single backslashes break JSON parsing.
- `spawn ENOENT` – the client can't find the binary. Give `command` an absolute path, or make sure the binary is on `PATH` for the shell the client launches from – Claude Desktop launches without your login shell's `PATH`.

If the handshake completes but individual tool calls fail, open the Glama MCP Inspector and point it at the server URL – it shows raw JSON-RPC requests and responses so you can see exactly where the error originates.

What is the Model Context Protocol (MCP)?

MCP is an open-source standard introduced by Anthropic in November 2024 that standardizes how AI applications connect to external tools and data sources. Think of it as USB-C for AI – one protocol replaces custom integrations between every AI app and every tool.

Before MCP, every AI application needed custom code to talk to every tool – an N×M integration problem. MCP reduces it to N+M: each app implements MCP once, each tool implements MCP once.

An MCP setup has three roles:

- The host – the AI application (Claude Desktop, ChatGPT, Cursor, VS Code)
- A client – the host's internal connection to one specific server
- An MCP server – exposes three primitives to the client: 

- tools – functions the model can call (like "send email" or "query Postgres")
- resources – data the model can read (like a config file or database schema)
- prompts – templated messages the user can pick from

Servers speak to clients over `stdio`, Server-Sent Events, or the modern Streamable HTTP transport using `JSON-RPC 2.0`.

Glama sits at the infrastructure layer. We index every MCP server and hosted connector in the ecosystem, search every tool they expose, and proxy every call through a gateway that logs inputs and outputs, enforces per-tool access control, and manages OAuth credentials – so your agents get the MCP ecosystem plus production-grade observability.

What is an MCP Gateway?

An MCP Gateway is a reverse proxy that sits between AI clients and MCP servers. It appears as an MCP server to the client while acting as an MCP client to the backend.

Without a gateway, every agent manages its own connections to every server – a tangled point-to-point mess that breaks at enterprise scale. A gateway consolidates all of that into one control plane that:

- Authenticates – one identity in front of every connected server
- Injects credentials – OAuth tokens and API keys stored once, refreshed automatically
- Controls tool access – enable or disable individual tools per connection
- Manages sessions – `Mcp-Session-Id` tracking across reconnects
- Logs every call – full JSON-RPC audit trail

Glama's MCP Gateway turns the open MCP ecosystem into a production-grade control plane – every connector in the registry is fronted by the gateway, so every call your agents make is visible, auditable, and revocable. Read the full Gateway overview →

What is an MCP Proxy, and how is it different from an MCP Gateway?

An MCP Proxy is a thin pass-through – it takes a JSON-RPC request from a client, forwards it to an upstream MCP server, and returns the response. Nothing else.

An MCP Gateway includes a proxy and adds the control plane on top:

- Access control – enable or disable individual tools per connection
- Credential management – encrypted OAuth storage and automatic token refresh
- Session lifecycle – `Mcp-Session-Id` tracking across reconnects
- Usage analytics – aggregated tool call counts, latency, cost attribution
- Full call logging – every JSON-RPC message persisted for audit

Use a proxy when you need basic routing for a single upstream server. Use a gateway when you are running MCP at enterprise scale and need governance. Glama is a full gateway – not a roll-your-own routing layer.

What are MCP connectors?

An MCP connector is a pre-configured MCP server you can plug into an AI client in one step. In Claude, ChatGPT, and other clients, any remote MCP server a user has added to their account shows up as a "connector".

A Glama connector goes further. It adds hosting, managed credentials, and per-tool access control on top of the underlying server – so you don't have to run the server, store the tokens, or touch any config. Paste the Glama URL into Claude, ChatGPT, or Cursor, and the Glama Gateway does the rest.

What is MCP hosting?

MCP hosting is a managed service that runs an MCP server for you on infrastructure you don't have to provision. You get a public URL with TLS, OAuth and credential management, health checks, monitoring, and scaling – without running the server yourself.

Most MCP hosting platforms – Cloudflare Workers, Google Cloud Run, Azure Functions, AWS Bedrock AgentCore, Heroku – require you to bring your own server code. You write the MCP server, they run it.

Glama is different. We host open-source MCP servers from the registry directly: pick a server someone else already published, click deploy, and get a `streamable-http` endpoint fronted by the Glama Gateway – without writing a line of code yourself. Full call logging, per-tool access control, and managed OAuth credentials come out of the box.

How does Glama's MCP Gateway log tool calls and control tool access?

Every JSON-RPC message – request, response, and SSE server event – is persisted to Glama's database with the full payload, including:

- `tool` name
- Input arguments
- Output result
- Timestamps and session IDs

Call logs are scoped to the connection profile owner – workspace members with the right role can view shared logs.

Per-tool access control is a per-connection on/off flag. Disable a tool and the gateway returns a JSON-RPC error to the client without ever forwarding the request upstream – the tool author never knows the call was attempted.

OAuth credentials are stored encrypted and automatically refreshed, so your client never holds the tokens. Revoking access is one click – no credential rotation required on the client side.

Heads up: the gateway captures full JSON-RPC payloads, so tool arguments containing sensitive data (API keys, PII, customer data) are visible in the audit log. For sensitive workloads, mask those arguments at the client side before calling.

Where are MCP credentials and call logs stored?

Credentials. Glama stores OAuth access tokens, refresh tokens, and API keys encrypted with AES-256-GCM – each value gets its own random 16-byte IV and authentication tag, and the 256-bit key is held server-side only. They are decrypted in memory only at the moment of making an upstream request, and automatically refreshed before expiration. Your client never sees the raw credentials – only the Glama Gateway does.

Call logs. Full JSON-RPC payloads – including tool name, input arguments, and upstream output – are stored per connection profile so you can audit exactly what your agents did, with timestamps and session IDs for traceability.

How do I test or debug an MCP server?

Use the Glama MCP Inspector – an in-browser tool that connects to any MCP server URL and lets you:

- List tools, resources, and prompts
- Call them with structured inputs
- See raw JSON-RPC responses
- Handle OAuth flows, bearer tokens, and custom headers
- Exercise advanced spec features – tasks, elicitations, sampling, progress notifications, audio, and images

All state is encoded in the URL so you can share or bookmark a debug session. No install, no login, no local MCP client required – paste a URL, click inspect, and you're debugging.

The official reference inspector (`@modelcontextprotocol/inspector`) is an npm-installed local tool. Glama's is web-based – it works against remote MCP servers directly, and requests go from your browser to the MCP server without Glama ever logging them.

Can I search for a specific MCP tool, not just a server?

Yes. When you know what capability you need but don't know which server provides it, tool-level search gets you there in one query.

Glama indexes every tool exposed by every server in its registry – names, descriptions, input schemas, and the MCP annotation hints (`readOnlyHint`, `destructiveHint`, `idempotentHint`) that tell you whether a tool is safe to run in automated agent loops. You can search for capabilities like:

- `query Postgres` – find every database-query tool
- `send email` – find every email-sending tool
- `generate Figma component` – find every Figma-integration tool

Once you've found a matching tool, you can either install the underlying server yourself or plug in the Glama-hosted connector for that server in one click. Few other MCP directories index at the tool level.

How do I add a Glama connector to Claude, ChatGPT, or Cursor?

A Glama connector URL works across every MCP-compatible client. Depending on your client:

- Claude – Customize → Connectors → click + → Add custom connector
- ChatGPT – Settings → Apps & Connectors → Create (Developer Mode must be enabled)
- Cursor – Settings → Features → MCP → + Add New MCP Server, or edit `~/.cursor/mcp.json`
- VS Code – Command Palette → `MCP: Add Server`, or edit `.vscode/mcp.json` in your workspace

For other MCP-compatible clients (Windsurf, Zed, JetBrains IDEs, Replit, …), setup is client-specific – check your client's MCP configuration docs. Any client that speaks MCP will accept a Glama connector URL – one connector, every agent.

How do I submit an MCP server?

Submit open-source MCP servers to the Glama registry straight from a GitHub repository. On the servers page, click Add MCP Server and fill in:

- The GitHub repository URL for your server
- A display name and short description

Glama runs automated quality checks (license detection, security scan, health test) during indexing. Most submissions pass automatically within minutes and become discoverable through Glama's search, category pages, and recommendation feeds.

Control how your server is indexed by adding a `glama.json` metadata file to your repo – it lets you set the display name, description, category, environment variables, and build spec. Servers must be on GitHub today; for other sources, reach out on Discord.

How do I submit an MCP connector?

Connectors are remote MCP servers you've already deployed somewhere with a public endpoint. On the connectors page, click Add MCP Server → Connector and provide:

- A name and short description
- The server URL – must be HTTPS and speak the `streamable-http` transport
- Optional private test credentials (API keys, OAuth details) so Glama can verify the connector is reachable

If your server implements OAuth 2.1 dynamic client registration (RFC 7591), you can skip the test credentials – Glama will register automatically.

Only healthy connectors are indexed for search. Unhealthy connectors stay in pending state until they become reachable. Submitted connectors are public by default and discoverable immediately once healthy. You can mark a connector as deprecated later if you're retiring the upstream server – users browsing Glama will see a notice.

How does Glama decide my connector's authentication badge?

The auth method on your connector's test profile is what sets the `auth:` badge. A maintainer's declaration is what the badge reflects wherever there is one; where there is not, Glama falls back to what it can detect – a server that advertises OAuth metadata and refuses unauthenticated traffic is listed as `auth:oauth2` automatically. Nothing else is inferred, because a connector that lets anyone list tools looks identical to one that needs no auth at all.

To set it, claim your connector and open its page, then create or edit the test profile and pick the authentication method your server actually requires – No Auth, API Key, Basic Auth, or OAuth 2.0. That choice becomes the connector's primary auth method and updates the badge. Until a test profile declares one, a connector reads as `auth:none`.

Open discovery with authenticated calls is a common shape – `tools/list` is left open so directories can index and health-check the server, while every `tools/call` requires a key and returns `401` with `WWW-Authenticate`. Declare the method the calls need, since that is what someone integrating the connector has to provide. Set the test profile to API Key, add a test credential so health checks exercise the authenticated path, and describe the open-discovery behaviour in your connector description.

Selecting No Auth will not clear a badge your server contradicts. If the last health check was refused with a `401`, the test profile still switches to connecting without credentials, but the connector stays listed as it was – publishing `auth:none` for a server that turns away unauthenticated callers would tell integrators they need no key when they do. Health-checking a server without credentials is not the same claim as the server being open.

The badge carries one method. If your server accepts more than one – say an API key or OAuth – set the test profile to the one most integrators will use and document the rest in the description. Declaring a method also overrides the automatic OAuth detection above, so a server that speaks both is listed the way its maintainer describes it.

How do I claim an MCP connector?

Claiming proves that you control a remote MCP connector. It does not move, proxy, or interrupt the server.

You verify the domain or GitHub account a connector belongs to, not each connector separately. One verification covers every connector under it – including connectors published or imported later – so a publisher with many connectors verifies once.

1. Open the connector listing, choose Claim ownership, and sign in to Glama.
2. Complete one verification: 

- Your domain. For a connector listed in the official MCP Registry under a domain namespace, verify the domain the namespace is named after: `com.example/server` is verified through `example.com`. This works even when the connector runs on someone else's platform, such as a hosting provider. For any other connector, verify the domain it is served from. Add the TXT record Glama shows at `_glama-claim. `, or publish the JSON Glama shows at `https:// /.well-known/glama.json`, then choose Check.
- GitHub identity. For a namespace such as `io.github.alice/server`, link the matching GitHub user, then choose Claim with GitHub. An organization namespace such as `io.github.acme/server` also needs that organization to have installed the Glama AI GitHub App and approved its permissions, because GitHub discloses organization membership only to apps it has installed.
3. Glama emails you for each connector the verification covers and gives you access to listing details, thumbnails, health checks, and analytics.

The HTTP ownership file has this structure:

```json
{
  "$schema": "https://glama.ai/mcp/schemas/connector.json",
  "claim": "glama_claim_..."
}

```

When several Glama accounts verify the same domain, `claim` may be a list of tokens.

Your claim token is opaque, stable, and bound to your Glama account – the same token works for every domain you verify. It contains no email address or other personal information. Never publish an email address, Glama session token, GitHub token, or connector credential as ownership proof.

Glama re-checks domain verifications daily. If it can no longer find your token, it emails you and starts a seven-day grace period before removing access. Restore the same token during that period to keep ownership.

When both a connector's registry publisher and the owner of its hosting domain have verified, the registry publisher manages the listing. If the publisher's verification later lapses, the hosting domain's owner manages it again.

If verification fails, confirm that you copied the current token exactly. The HTTP file must be public, served over HTTPS, and must not redirect to another domain. DNS changes may need more time to propagate.

For a connector linked to the official MCP Registry, registry updates continue to replace its name, description, and URL by default. After claiming, open Manage connector and enable Use Glama listing details as the source of truth if edits made on Glama should be preserved. Categories and thumbnails are always managed on Glama; registry linkage and technical connection settings continue to sync.

Which AI clients support MCP?

The following AI clients support MCP natively or via adapter:

- Claude Desktop, Claude Code
- ChatGPT
- Cursor, Windsurf, Zed
- VS Code (with the MCP extension)
- JetBrains IDEs
- Replit
- Sourcegraph (via Cody)

Glama tracks every MCP-compatible client with its supported features listed in the client directory.

How is Glama different from the official MCP registry?

The official MCP Registry is a vendor-neutral index of MCP server metadata maintained by the MCP steering group – the canonical source of truth for publicly published servers.

Glama builds on top of it with much deeper per-connector data and a full control plane:

- Rich metadata on every connector – health checks, quality scores, security audits, tool schemas with annotations, usage telemetry, license info, and maintainer notes
- One-click hosting on managed infrastructure
- Full observability and control over every call – JSON-RPC logging, per-tool access control, managed OAuth credentials, and usage analytics

Use the official registry for vendor-neutral metadata. Use Glama when you need depth, observability, and control over production MCP traffic. See our indexing methodology for the full technical description of how every server in the Glama registry is built, introspected, audited, and scored.