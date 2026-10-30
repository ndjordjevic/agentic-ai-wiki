---
type: source
category: "Coding-agent harnesses & methodologies"
source_url: https://kylon.io/
tags:
  - company-harness
  - team-agents
  - bring-your-own-agent
  - draft-first-approvals
  - rooms-threads
  - kylon-cli
  - agent-governance
  - credit-metering
related:
  - paperclip.ing
  - app.sauna.ai
  - joinoasis.com
  - block-buzz
  - composio-community-open-dot
  - cognition.ai
  - hermes-agent.nousresearch.com
product: kylon.io
detail_level: standard
created: 2026-10-30
updated: 2026-10-30
---

Kylon (by Pure Reason) is a commercial **company harness**: one workspace where people and AI agents run the business together. Agents are workspace members with identity, typed durable memory, RBAC, sandboxed runtimes, skills, Automations, and draft-first approvals—not private chatbots. Teams can host Kylon Cloud agents or bring Claude Code, Codex, Devin (and ACP agents) into the same rooms via the `kylon` CLI gateway.

_All claims below are sourced from ../../raw/web/kylon.io.md unless otherwise noted._

## What it does

Kylon inverts the one-person AI tab: shared Rooms and threads are the context, and agents live in them as colleagues. People @mention agents (or let smart routing pick), agents act through authorized Connections (OAuth, MCP, API keys) with credentials injected at run time (not pasted into chat), and consequential outbound (Gmail/Outlook email, X, LINE) becomes editable draft cards a human Sends. Agents also build Apps (each with its own Postgres when needed), follow Skills, schedule Automations/follow-ups, and hand work between agents (capped at 12 autonomous hops). Surfaces: web (`app.kylon.io`), macOS desktop, iOS/Android (and iPad). English and Japanese.

## Key features

- **Six harness layers** under the chat UX: identity/access, agent routing, connections (API proxy, secret vault, model routing), runtime (sandbox, skills, automations, BYO agent, browser, sub-agents, CLI/API), build-and-ship (git drafts/previews, App DBs, file system), governance (draft-first approvals, run history, usage metering, data scoping).
- **Typed agent memory** (preference, feedback, reference, context) scoped everywhere / per room / per person, with 15–60 day review intervals.
- **Bring your own agent** — Claude Code, Codex, Devin Cloud; Custom ACP where enabled; docs also mention Gemini CLI, Grok Build, Hermes on some deployments.
- **3,000+ integrations** plus first-party data tools via the proxy (Apollo, Apify, Ahrefs, Seedance, etc. called out on marketing pages).
- **App templates** (sales CRM, creator CRM, hiring, travel desk, TikTok sampling, etc.) built in-chat with review/publish.
- **Workspace CLI + proxy APIs** for agents/developers (`kylon` gateway + `api.kylon.io/proxy/...`).
- **Security program**: GDPR claimed; SOC 2 Type II and ISO/IEC 27001:2022 audits in progress (Trust Center).

## Architecture and concepts

Core objects: Workspace (boundary), Rooms/Threads (shared work), Agents (hosted cloud computer or computer-connected BYO), Connections (owned OAuth/MCP/key accounts with delegation vs standing grants), Skills, Apps/databases, Automations (`workflow` in CLI), Files, Workspace Knowledge, Feed/search, credits/billing. Hosted agents run in jails limited to the current room/shared/agent files; sub-agents are private helpers without room post/browser, 30-minute cap. Model routing maps intelligence levels to OpenAI/Anthropic/Gemini (and open models) with failover; BYO agents use their own provider logins.

## Main APIs

- **CLI** — install via `curl -fsSL https://api.kylon.io/install.sh | sh` (macOS/Linux), PowerShell installer or `npm i -g kylon-cli` / `npx kylon-cli@latest login` (Windows); then `kylon login`, `kylon status`, `kylon gateway status`, `kylon workspace …`, `kylon onboard`.
- **Proxy** — base `https://api.kylon.io/proxy/...`; agent runtimes use `KYLON_API_TOKEN` (human CLI credentials cannot call the proxy). Tools API example: `curl -s https://api.kylon.io/proxy/tools/connections -H "Authorization: Bearer ${KYLON_API_TOKEN}"`. Families: tools, app connections, model APIs, provider APIs, billing/errors.
- **Docs** — [docs.kylon.io](https://docs.kylon.io) (Mintlify) with `llms.txt`; marketing site ships per-page `.md` and site-wide `llms.txt` / `llms-full.txt`.

## When to use

Choose Kylon when an SMB, agency, or ops team wants **shared rooms + governance** around multiple named agents (not a single org bot), draft-first outbound, and the option to put existing Claude Code/Codex/Devin sessions into the same company context. Less of a fit if you only need a personal agent VM (Grok Bot / Muse / Dots-class) or a pure automation canvas (Zapier/n8n) without team rooms.

## Ecosystem

Built by Pure Reason (Pure Reason Inc., Delaware; PURE REASON PTE. LTD., Singapore; Palo Alto + Singapore offices). Competes/compares on-site with Slack/Teams-as-work-surface, Dust, Viktor, OpenAI Dots, Grok Bot, Muse, Copilot, and many CRM/automation tools. Adjacent wiki sources: [[paperclip.ing]] (OSS agent-company control plane), [[app.sauna.ai]] / [[joinoasis.com]] (multiplayer AI workspaces), [[block-buzz]] (agents-as-members messaging), [[composio-community-open-dot]] (Dots-like desktop agents), [[cognition.ai]] (Devin), [[hermes-agent.nousresearch.com]] (Hermes BYO path mentioned in docs).
