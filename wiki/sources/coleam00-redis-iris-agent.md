---
type: source
category: "Knowledge, RAG, memory & context"
source_url: https://github.com/coleam00/redis-iris-agent
tags: [pydantic-ai, mcp-toolset, agent-memory, context-retriever, redis-iris, python, reference-implementation]
related: [redis.io, pydantic.dev]
product: redis-iris-agent
detail_level: standard
created: 2026-07-09
updated: 2026-07-09
---

redis-iris-agent (Cole Medin, MIT, Python) is a small reference implementation showing how a [Pydantic AI](https://ai.pydantic.dev) agent consumes [[redis.io]]'s Redis Iris context layer end to end — Context Retriever as an MCP toolset and Agent Memory as plain tools — with a full reproducible demo dataset rather than just a marketing description. It matters for this wiki as the concrete "how do you actually wire this up" counterpart to Redis's own product page: it shows the exact tool-call shape (`search_memory`, `get_customer_by_id`, `filter_order_by_customer_id`, ...) an LLM sees when both context primitives are combined in one turn.

_All claims below are sourced from ../../raw/github/coleam00-redis-iris-agent.md unless otherwise noted._

## What it does

The agent answers natural-language questions by combining two Redis Iris primitives in a single Pydantic AI `Agent`: Context Retriever, which is Redis's live business-data layer exposed as an auto-generated, governed MCP toolset (`get_*_by_id`, `filter_*_by_*`, `search_*_by_text`, `find_*_by_*_range` — one tool set per indexed entity field type), and Agent Memory, wrapped as two plain tools (`search_memory`, `store_memory`) for short-term session state plus long-term recall that persists across sessions and is auto-promoted from conversation in the background. The README frames the split cleanly: Context Retriever is "the data," Agent Memory is "who the user is." Both services are explicitly marked **preview** — the repo is a proof-of-concept, not a production template.

## Key features

- **MCP-native data access** — Context Retriever publishes a standard streamable-HTTP MCP endpoint at `/mcp`, authenticated via an `X-API-Key` header; Pydantic AI's native MCP client consumes it as one `MCPToolset(url, headers=...)` passed to the `Agent` as a toolset — no hand-written API layer or raw SQL.
- **Two memory tiers in one wrapper** — `src/redis_iris_agent/memory.py` wraps the managed `redis-agent-memory` SDK to expose session-scoped working memory and durable long-term recall through the same two tools.
- **Reproducible demo** — a fictitious "Northpeak Outfitters" support-desk dataset (134 records: customers, products, orders, shipments, tickets) loaded via `seed_northpeak.py`, a surface auto-provisioned via `configure_surface.py` (5 entities → ~29 generated tools, plus a minted agent key), and a scripted two-session hero flow (`demo_hero.py`) that states a preference in one session and recalls it alongside live order data in a brand-new session.
- **Colorful CLI** — a rich/prompt-toolkit chat loop (`cli.py`) with in-chat commands: `/tools` (list available Context Retriever tools), `/clear`, `/newsession` (resets working memory, keeps long-term memory), `/whoami`, `/help`, `/exit`.
- **Server-scoped access control** — the Context Retriever agent key scopes exactly what data the agent can reach server-side, rather than relying on prompt-level restriction.

## Architecture and concepts

The agent is a thin composition layer: `config.py` loads and validates environment configuration for both services (Context Retriever is required, Agent Memory is optional and only activates when all three `AGENT_MEMORY_*` variables are set); `agent.py` builds the Pydantic AI `Agent` with the MCP toolset plus the two memory tool wrappers; `cli.py` runs the interactive loop. Tool generation on the Context Retriever side is schema-driven: each indexed field type maps to exactly one tool kind (tag → `filter`, text → `search`, numeric → `find…range`, key → `get…by_id`), so an entity with no text field simply has no `search` tool. A noted rough edge: LLM providers reject tool names containing spaces, and Context Retriever derives tool names from entity names, so multi-word entity names produce invalid tool names that the client sanitizes — the recommendation is single-word, space-free entity names.

## Installation

Requires a Redis Cloud database (free 30MB tier is sufficient), a Context Retriever service defined over it (created via the Redis Cloud console or provisioned from code via `configure_surface.py`), a Context Retriever agent key, optionally an Agent Memory service (endpoint, store id, key), an LLM provider key (Anthropic by default, via `MODEL=anthropic:claude-sonnet-4-6`), and [`uv`](https://docs.astral.sh/uv/). Setup is `uv sync` then `cp .env.example .env` and fill in keys (`.env` is git-ignored).

## Example usage

Pointing at an existing service: set `CONTEXT_RETRIEVER_AGENT_KEY` (and an LLM key) in `.env`, then `uv run redis-iris-agent` (or `uv run python -m redis_iris_agent.cli`) starts the chat; the agent discovers whatever tools the service exposes. Running the full demo instead: set `REDIS_URL`, `CTX_ADMIN_KEY`, the `AGENT_MEMORY_*` values, and an LLM key, then run `uv run python seed_northpeak.py` (load data), `uv run python configure_surface.py` (provision the surface and mint an agent key, written to `_agentkey.tmp`), and `uv run python demo_hero.py` (the scripted cross-session hero flow) — or just `uv run redis-iris-agent` to chat freely. `seed_northpeak.py` loads additively by default; `--flush` wipes the whole database including Agent Memory keys.

## Maintenance status

6 stars, 4 forks, MIT license, no tagged releases, default branch `main`, last pushed 2026-07-04. A small, single-author (Cole Medin) demo/reference repo rather than an actively maintained library — consistent with its stated proof-of-concept framing rather than production-template status.

## Ecosystem

Built on [[pydantic.dev]] (Pydantic AI's native MCP client and `Agent`/toolset abstractions) and directly demonstrates [[redis.io]]'s Redis Iris bundle — specifically the Context Retriever and Agent Memory components — in a runnable form. It is the practical companion to Redis's own marketing-oriented Iris page: where [[redis.io]] describes the value proposition, this repo shows the actual tool-call sequence, environment configuration, and integration code an agent builder would need to reproduce it with Pydantic AI.
