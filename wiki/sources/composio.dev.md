---
type: source
category: "MCP servers & integrations"
source_url: https://composio.dev/
companion_urls:
  - https://github.com/ComposioHQ/composio
raw_files:
  - ../../raw/web/composio.dev.md
  - ../../raw/github/ComposioHQ-composio.md
tags:
  - tool-router
  - managed-auth
  - mcp-gateway
  - session-sdk
  - agent-toolkits
  - composio-connect
  - proxy-execute
  - agent-skills
related:
  - composio-community-open-dot
  - monid.ai
  - skills.sh
  - openrouter.ai
  - smithery.ai
  - glama.ai
product: composio
detail_level: standard
created: 2026-11-03
updated: 2026-11-03
studied: true

---

Composio is an agent-tooling platform that gives AI agents secure, consent-gated access to 1,000–1,500+ apps (Gmail, Slack, Notion, GitHub, HubSpot, and many more) through managed authentication, a session-based tool router, hosted MCP ("Composio Connect"), CLI/plugins for personal agents, and Python/TypeScript SDKs for apps whose users connect their own accounts. It matters to this wiki as the integration layer behind products like [[composio-community-open-dot]], and as a peer to tool gateways such as [[monid.ai]] — focused on *acting in* SaaS apps rather than only fetching data APIs.

_All claims below are sourced from ../../raw/web/composio.dev.md unless otherwise noted._

## What it does

Composio sits between an agent (or application) and third-party apps. Two product paths: **For You** — connect your own accounts to Claude, ChatGPT/Codex, Cursor, Hermes, OpenClaw, and other MCP clients via plugins or `https://connect.composio.dev/mcp`; and **Platform** — session SDKs so each of your users gets scoped tool discovery, OAuth connections, and execution without shipping provider tokens to the model. Sessions expose a small set of meta-tools so toolkit schemas load on demand instead of dumping hundreds of tools into context. Credentials stay on Composio's side (or in VPC/self-hosted/customer-managed-key deployments); actions can be limited and audited.

## Key features

- **1,000+ toolkits / 1,500+ apps** with OAuth and managed token refresh; custom MCP servers can be added when an app isn't listed.
- **Sessions** — `composio.create(user_id)` (Python/TS) ties user identity, toolkit scope, auth, and execution state; default meta-tools for search, connect, and execute; optional sandbox for large tool results. (../../raw/github/ComposioHQ-composio.md)
- **Composio Connect** — hosted MCP at `https://connect.composio.dev/mcp` with seven meta-tools for existing MCP clients (not a full per-app tool dump).
- **Native agent plugins** — shortest path for Codex and Claude Code; CLI (`curl -fsSL https://composio.dev/install | sh`, `composio login`) for terminal agents; unattended agents use `composio login --agent`.
- **Proxy Execute** — call provider HTTP APIs that aren't wrapped as tools without exporting tokens to the agent.
- **MCP Gateway / Firewall / Instant** — team MCP control plane, tool-result inspection against prompt-injection in content, and a wallet for paid audio/video/search/browser tools without per-provider keys.
- **Official Agent Skill** — `npx skills add ComposioHQ/composio --skill composio` for coding-agent setup patterns. (../../raw/github/ComposioHQ-composio.md)
- **Security posture** — SOC 2 Type II; Trust Center; Hobby plan cites 100k tool calls/month free; REST API current base `https://backend.composio.dev/api/v3.1`.

## Architecture

The open-source monorepo (`ComposioHQ/composio`, default branch `next`) ships `@composio/core` (TypeScript), the `composio` Python package (not legacy `composio-core`), the `composio` CLI, provider adapters (OpenAI Agents, Claude Agent SDK, Vercel AI SDK, LangChain, and more), docs, examples, and skills. Sessions are the recommended integration; direct `tools.get` / `tools.execute` remains supported as legacy. Provider packages follow the *framework* (e.g. `@composio/openai-agents` for the Agents SDK vs `@composio/openai` for Chat Completions). Terminology migration: entity ID → user ID, actions → tools, apps → toolkits, integration → auth config. (../../raw/github/ComposioHQ-composio.md)

## Installation

```bash
# CLI (For You / terminal agents)
curl -fsSL https://composio.dev/install | sh
export PATH="$HOME/.local/bin:$PATH"
composio login          # or: composio login --agent

# MCP clients
# Add remote MCP: https://connect.composio.dev/mcp

# Platform SDK (Python 3.11–3.15)
uv add composio composio-openai-agents openai-agents

# Platform SDK (TypeScript, Node ≥ 22.22.3, ESM)
npm install @composio/core @composio/openai-agents @openai/agents

# Coding-agent skill
npx skills add ComposioHQ/composio --skill composio
```

Set `COMPOSIO_API_KEY` from the dashboard for application backends. (../../raw/github/ComposioHQ-composio.md)

## Example usage

```python
from composio import Composio

composio = Composio()
session = composio.create(user_id="user_123")
tools = session.tools()
# pass tools to your agent framework; execute via session.execute(...)
```

```typescript
import { Composio } from "@composio/core";

const composio = new Composio();
const session = await composio.create("user_123");
const tools = await session.tools();
```

(../../raw/github/ComposioHQ-composio.md)

## When to use

Use Composio when an agent must **discover and act in** connected SaaS apps with managed auth (personal assistant path or multi-tenant Platform sessions). Prefer [[monid.ai]]-style gateways when you mainly need pay-per-call *data* APIs without write-into-app OAuth. Skip Composio for model-only chat or public docs fetch with no account connections. Don't treat a Composio login as bypassing the app owner's consent.

## Maintenance status

GitHub companion: ~30.9k stars, ~4.9k forks, MIT, TypeScript primary, default branch `next`, homepage docs.composio.dev; latest stable CLI release `@composio/cli@0.6.0` (2026-11-01) with active CLI betas. Actively pushed. (../../raw/github/ComposioHQ-composio.md)

## Ecosystem

Works with ChatGPT/Codex, Claude (web/Cowork/Code), Cursor, Grok Bot, Hermes, OpenClaw, and generic MCP clients. Powers app connectivity in [[composio-community-open-dot]]. Catalogued alongside MCP registries ([[smithery.ai]], [[glama.ai]]) and skill distribution ([[skills.sh]]). Contrasts with [[openrouter.ai]] (model routing) the way [[monid.ai]] does for data tools — Composio's center of gravity is authenticated app *actions*.
