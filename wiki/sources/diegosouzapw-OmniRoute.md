---
type: source
category: "Model infra, ML & providers"
source_url: https://github.com/diegosouzapw/OmniRoute
tags:
  - ai-gateway
  - multi-provider
  - openai-compatible
  - quota-aware-routing
  - token-compression
  - mcp
  - a2a
  - self-hosted
related:
  - openrouter.ai
  - litellm.ai
  - router-for-me-CLIProxyAPI
  - hermes-agent.nousresearch.com
product: omniroute
detail_level: standard
created: 2026-10-20
updated: 2026-10-20
---

OmniRoute is a free MIT AI gateway (npm `omniroute`, homepage [omniroute.online](https://omniroute.online)) that puts hundreds of LLM providers — including many free tiers — behind one local OpenAI/Claude/Gemini-compatible endpoint, with quota-aware auto-fallback, stacked token compression, MCP/A2A, and Desktop/PWA clients. With ~78.6k GitHub stars (v3.8.52 as of October 2026), it is aimed at coding agents and IDEs (Claude Code, Codex, Cursor, OpenCode, Cline, Copilot) that should keep working when one provider hits limits.

_All claims below are sourced from ../../raw/github/diegosouzapw-OmniRoute.md unless otherwise noted._

## What it does

You install OmniRoute on your machine, connect your own provider accounts/keys, then point tools at `http://localhost:20128/v1` with an OmniRoute API key and model `auto` (or a named combo). The smart router compresses eligible payloads, picks a healthy target among connected providers, and can fall through a 4-tier cascade — Subscription → API Key → Cheap → Free — while another eligible target remains.

Headline catalog (v3.8.52+): **375 providers**, **~1,400–1,475 unique chat model IDs**, **150+ / 153 catalog-marked free** tiers, and an audited ~**1.62B free tokens/month** aggregate across third-party free pools (BYO accounts; not an OmniRoute grant). Dashboard live used/remaining lives at `/dashboard/free-tiers`.

## Installation

```bash
npm install -g omniroute
omniroute
# Dashboard: http://localhost:20128 · API: http://localhost:20128/v1
```

Other surfaces: Docker (`diegosouzapw/omniroute`), Bun, pnpm, Arch AUR (`omniroute-bin`), Nix/devbox, Termux, Electron desktop, PWA, and macOS menu-bar tray (`brew install --cask zoispag/tap/omniroute-tray`). Headless: `omniroute serve --headless` or `OMNIROUTE_HEADLESS=1`. From source: `cp .env.example .env && npm install` then `PORT=20128 npm run dev`.

Connect a provider in Dashboard → Providers, copy a key from Endpoints, set Base URL `/v1` and model `auto` in your coding tool.

## Key features

- **One endpoint, many providers** — OpenAI Chat Completions, Claude, Gemini, and Responses API compatibility at `/v1`; 37 CLI/agent integrations through one config.
- **Combos + 20 routing strategies** — chains of models with automatic failover; strategies include priority, weighted, fill-first, round-robin, p2c, least-used, cost-optimized, quota-weighted, cache-optimized, fusion, pipeline, and `auto` / `auto/subscription` / `auto/thrifty` variants. Auto-Combo scores candidates on 16 factors.
- **Quota-aware resilience** — three layers: provider circuit breaker, per-key connection cooldown, per-model lockout; Quota-Share fair pools; `X-OmniRoute-Decision` transparency header.
- **Token compression** — 12-engine pipeline (default stack `RTK → Caveman`); claimed 15–95% savings on eligible workloads (~89% average for stacked RTK+Caveman); structured content preserved.
- **MCP & A2A** — MCP stdio (`omniroute --mcp`), HTTP/SSE with **110 tools**; A2A via `/.well-known/agent.json` (JSON-RPC 2.0 + SSE); OmniConductor for inbound A2A delegation.
- **Local-first** — gateway on your machine; AES-256-GCM encrypted credentials; telemetry off by default; Desktop/PWA/Termux.

## Architecture

Built as a TypeScript monorepo: **Next.js 16** app (`src/`) + **open-sse** streaming engine + Electron desktop. Runtime: Node.js 22/24; SQLite (`better-sqlite3`) with 209 migrations; Zod schemas.

Request path (simplified):

```
Client → /v1/chat/completions (Next.js)
  → CORS → Zod → auth/policy → compression
  → combo routing / Auto-Combo
  → translate → executor → upstream fetch (+ retry)
  → response translate → SSE or JSON
```

Handlers/executors/translators live under `open-sse/`; combo routing in `open-sse/services/combo.ts`; MCP in `open-sse/mcp-server/`; A2A in `src/lib/a2a/`.

## Example usage

```bash
curl http://localhost:20128/v1/chat/completions \
  -H "Authorization: Bearer YOUR_OMNIROUTE_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model":"auto","messages":[{"role":"user","content":"Hello!"}]}'

curl http://localhost:20128/v1/models -H "Authorization: Bearer YOUR_OMNIROUTE_KEY"
omniroute chat          # TUI
omniroute --mcp         # MCP stdio for Claude Desktop / Cursor
```

Copy-paste quickstarts for Python, Node, PHP, and cURL live in `examples/quickstart/`.

## Maintenance status

- **Stars:** 78,636 (fetched 2026-10-20)
- **Latest release:** v3.8.52 (default branch `release/v3.8.53`; roadmap toward v3.9.0 LTS)
- **License:** MIT
- **Language:** TypeScript (Next.js 16 + React 19)
- **Activity:** actively developed (pushed 2026-10-20); 900+ contributors claimed
- **Community:** Discord, Telegram, WhatsApp; homepage https://omniroute.online
