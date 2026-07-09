# coleam00/redis-iris-agent

## Metadata
- Stars: 6
- Forks: 4
- Primary language: Python
- Default branch: main
- Latest release: none
- License: MIT License
- Homepage: (none)
- Fetched: 2026-07-09
- Final URL: https://github.com/coleam00/redis-iris-agent

## Description
Pydantic AI agent with a Redis Iris context layer: Context Retriever (live data via MCP) + Agent Memory, with a reproducible support-desk demo

## README
# Redis Iris Agent (Pydantic AI)

A [Pydantic AI](https://ai.pydantic.dev) agent that gives an LLM a real **context
layer** with [**Redis Iris**](https://redis.io/iris/):

- **Context Retriever** → live business data, through governed MCP tools that Redis
  auto-generates from your entity model (`get_*_by_id`, `filter_*_by_*`,
  `search_*_by_text`, `find_*_by_*_range`). No per-query code, no raw SQL, no
  hand-written API layer.
- **Agent Memory** → short-term (session) plus long-term memory that scales across
  users and sessions. Durable facts are auto-promoted from a conversation in the
  background, and exposed to the agent as `search_memory` / `store_memory` tools.

Context Retriever is the **data**; Agent Memory is **who the user is**. Together
they're a context layer: the agent recalls what a user wants and queries live data
to satisfy it — across sessions and users, not just you. It ships with a colorful
conversational CLI and a complete, reproducible demo (a fictitious support desk).

> **Both Context Retriever and Agent Memory are in preview.** This is a
> proof-of-concept, not a production template.

```
you › It's Jordan Rivera, customer C1004. Why is my order late, and can you handle it like last time?
  ↳ search_memory               {'query': 'Jordan Rivera C1004 preferences'}
  ↳ get_customer_by_id          {'id': 'C1004'}
  ↳ filter_order_by_customer_id {'value': 'C1004'}
  ↳ filter_shipment_by_order_id {'value': 'O5099'}

iris ›
Your Summit 2-Person Tent (order O5099) is 4 days delayed with UPS. Per your saved
preference, I'm arranging an expedited reship rather than a refund — no action
needed on your end.
```

That single answer combines **Agent Memory** (a preference you stated in an earlier
session) with **Context Retriever** (the live, delayed order and shipment).

## How it works

```
                 ┌─────────────────────────────┐
                 │      Pydantic AI Agent       │
   you  ───────► │        (your LLM)            │
                 └───────┬──────────────┬───────┘
        toolsets=[MCPToolset]      tool_plain
                 │                      │
                 ▼                      ▼
      Context Retriever          Agent Memory
      (MCP, X-API-Key)           (search_memory / store_memory
      auto-generated tools        + per-turn session logging)
      over your Redis data        long-term recall across sessions
                 │                      │
                 └───────► Redis Cloud ◄┘
```

Context Retriever publishes a standard **streamable-HTTP MCP** endpoint at `/mcp`,
authenticated with an `X-API-Key` header. Pydantic AI has a native MCP client, so
that half is one `MCPToolset(url, headers=...)` handed to the `Agent` as a toolset.
Agent Memory is the managed `redis-agent-memory` SDK, wrapped as two plain tools.
See `src/redis_iris_agent/`.

## Prerequisites

1. A **Redis Cloud** database (the free 30 MB tier is plenty).
2. A **Context Retriever service** over that database with your entities/fields
   defined — either created in the Redis Cloud console, or provisioned from code
   (see [the demo](#option-b--run-the-full-demo-northpeak-outfitters), which does
   this for you).
3. A **Context Retriever agent key** (sent as the `X-API-Key` header).
4. *(Optional)* an **Agent Memory service** — its endpoint, store id, and key — to
   enable memory.
5. An **LLM provider API key** for whatever model you point the agent at
   (Anthropic by default).
6. [`uv`](https://docs.astral.sh/uv/) installed.

## Setup

```bash
uv sync                 # install into a local venv
cp .env.example .env    # then fill in your keys (see Configuration below)
```

`.env` is git-ignored — your keys never get committed.

## Option A — point it at your own service

If you already have a Context Retriever service, set `CONTEXT_RETRIEVER_AGENT_KEY`
(and an LLM key) in `.env` and run the chat:

```bash
uv run redis-iris-agent
# or: uv run python -m redis_iris_agent.cli
```

Ask questions in plain English; the agent discovers and calls whatever tools your
service exposes. Add the three `AGENT_MEMORY_*` values to turn on memory.

## Option B — run the full demo (Northpeak Outfitters)

A complete, reproducible support-desk demo over fictitious data. Set `REDIS_URL`,
`CTX_ADMIN_KEY`, the `AGENT_MEMORY_*` values, and an LLM key in `.env`, then:

```bash
# 1. Load 134 support records (customers, products, orders, shipments, tickets)
uv run python seed_northpeak.py

# 2. Provision a Context Retriever surface (5 entities -> ~29 tools) and mint an
#    agent key. Writes the new key to _agentkey.tmp; copy it into .env as
#    CONTEXT_RETRIEVER_AGENT_KEY.
uv run python configure_surface.py

# 3. Run the hero flow: state a preference in one session, then recall it + look up
#    live order data in a brand-new session — both tools, one answer.
uv run python demo_hero.py

# ...or just chat with it:
uv run redis-iris-agent
```

`seed_northpeak.py` loads additively and never flushes by default (see the warning
in its header — `--flush` wipes the whole DB, Agent Memory keys included).

### In-chat commands

| Command       | What it does                                                                 |
| ------------- | --------------------------------------------------------------------------- |
| `/tools`      | List the Context Retriever tools the agent can call                         |
| `/clear`      | Clear conversation history (start a fresh context)                          |
| `/newsession` | New session, same user — working memory resets, long-term memory persists   |
| `/whoami`     | Show the current user id / session id and whether memory is on              |
| `/help`       | Show help                                                                   |
| `/exit`       | Quit (also `/quit`, or Ctrl-D)                                             |

## Configuration

All configuration is via environment variables (loaded from `.env`).

**The agent:**

| Variable                      | Required | Default                                              | Purpose                                        |
| ----------------------------- | -------- | ---------------------------------------------------- | ---------------------------------------------- |
| `CONTEXT_RETRIEVER_AGENT_KEY` | yes      | —                                                    | Agent key, sent as the `X-API-Key` header      |
| `CTX_MCP_URL`                 | no       | `https://gcp-us-east4.context-surfaces.redis.io/mcp` | Context Retriever MCP endpoint (region-pinned) |
| `MODEL`                       | no       | `anthropic:claude-sonnet-4-6`                        | Any Pydantic AI model string                   |
| `ANTHROPIC_API_KEY` (etc.)    | one      | —                                                    | API key matching your `MODEL`'s provider       |

**Agent Memory** (optional — set all three to enable):

| Variable                | Purpose                        |
| ----------------------- | ------------------------------ |
| `AGENT_MEMORY_ENDPOINT` | Agent Memory service base URL  |
| `AGENT_MEMORY_STORE_ID` | Agent Memory store id          |
| `AGENT_MEMORY_KEY`      | Agent Memory service key       |

**Demo scripts only** (`seed_northpeak.py` / `configure_surface.py`):

| Variable        | Purpose                                                                 |
| --------------- | ----------------------------------------------------------------------- |
| `REDIS_URL`     | Redis connection string, e.g. `redis://default:<pw>@<host>:<port>`      |
| `CTX_ADMIN_KEY` | Context Retriever **admin** key (manages the surface, mints agent keys) |

## Project layout

```
src/redis_iris_agent/
  config.py   # env loading + validation (Context Retriever + optional Agent Memory)
  agent.py    # builds the Pydantic AI agent + CR MCP toolset + memory tools
  memory.py   # optional Agent Memory wrapper (session logging + long-term recall)
  cli.py      # rich/prompt-toolkit chat loop with history + /newsession
seed_northpeak.py      # load the demo support dataset into Redis
configure_surface.py   # provision a Context Retriever surface + mint an agent key
demo_hero.py           # the combined Context-Retriever + Agent-Memory demo
```

## Notes

- **Access is scoped server-side** by the agent key, so the agent only ever sees the
  data that key is allowed to reach — the thing a folder of files can't give you.
- LLM providers reject tool names with spaces or odd characters. Context Retriever
  derives tool names from your entity names, so an entity named with a space yields
  an invalid tool name; the agent sanitizes those client-side. Prefer single-word,
  space-free entity names.
- The field's index type decides the generated tool: **tag → `filter`**, **text →
  `search`**, **numeric → `find…range`**, key → `get…by_id`. A field is one index
  type. That's why an entity with no text field has no `search` tool.

## License

MIT — see [LICENSE](LICENSE).

## Top-level structure
- `README.md` — project readme (fetched above)
- `LICENSE` — MIT license text
- `pyproject.toml` — Python package metadata / `uv` project config
- `uv.lock` — locked dependency versions for `uv`
- `.env.example` — template for required environment variables
- `.python-version` — pinned Python version for `uv`
- `.gitignore`
- `configure_surface.py` — provisions a Context Retriever surface (entities/fields) and mints an agent key
- `demo_hero.py` — runs the combined Context-Retriever + Agent-Memory demo flow
- `seed_northpeak.py` — loads the 134-record Northpeak Outfitters demo dataset into Redis (additive by default; `--flush` wipes the DB)
- `src/redis_iris_agent/` — the agent package:
  - `config.py` — env loading + validation (Context Retriever + optional Agent Memory)
  - `agent.py` — builds the Pydantic AI agent + Context Retriever MCP toolset + memory tools
  - `memory.py` — optional Agent Memory wrapper (session logging + long-term recall)
  - `cli.py` — rich/prompt-toolkit chat loop with history + `/newsession`
  - `__init__.py`
