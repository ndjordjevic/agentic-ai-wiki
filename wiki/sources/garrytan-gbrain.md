---
type: source
source_url: https://github.com/garrytan/gbrain
tags:
  - knowledge-graph
  - agent-memory
  - hybrid-search
  - rag
  - mcp-server
  - dream-cycle
  - personal-knowledge
  - typescript
related:
  - garrytan-gstack
  - supermemory.ai
  - hermes-agent.nousresearch.com
  - felix-forever-hermes-agent-desktop
  - 0xnyk-awesome-hermes-agent
product: gbrain
detail_level: standard
created: 2026-06-18
updated: 2026-07-07
---

GBrain is a persistent knowledge-graph and hybrid-retrieval brain layer for AI agents — built by Garry Tan (YC President/CEO) as the production memory infrastructure behind his OpenClaw and Hermes deployments. It separates itself from keyword-search personal-knowledge tools with two compounding features: a synthesis layer that answers questions with cited prose and an honest gap analysis (what the brain doesn't know yet), and a self-wiring knowledge graph that extracts typed entity edges on every page write with zero LLM calls. In benchmarks on a 240-page corpus it reaches **P@5 49.1% / R@5 97.9%**, a **+31.4 P@5 gain** over vector-only RAG. The same brain layer powers Garry's live deployment: 146,646 pages, 24,585 people, 5,339 companies, 66 autonomous cron jobs that enrich, deduplicate, and consolidate knowledge overnight.

_All claims below are sourced from ../../raw/github/garrytan-gbrain.md unless otherwise noted._

## What it does

GBrain is an agent brain: a Postgres-backed, git-synced knowledge store that an AI agent reads before every external API call. It ingests arbitrary markdown (meetings, emails, tweets, voice calls, ideas), maintains a typed entity graph, runs overnight enrichment cron jobs, and answers queries through either raw retrieval (`gbrain search`) or a synthesized-answer mode (`gbrain think`). The synthesis mode composes well-cited prose across the retrieved pages and adds a gap analysis flagging stale, uncited, or contradictory claims — the differentiator over page-list search tools. It also works as a team/company brain: each user gets a scoped view of a shared database with zero cross-user leakage.

## Installation

Three installation paths:

**Agent-driven (recommended)** — paste one line into any agent (Claude Code, Codex, Cursor, OpenClaw, Hermes) and the agent reads `INSTALL_FOR_AGENTS.md`, asks for API keys, loads 43 skills, configures the dream cycle, and verifies end-to-end in ~30 minutes.

```
Retrieve and follow the instructions at:
https://raw.githubusercontent.com/garrytan/gbrain/master/INSTALL_FOR_AGENTS.md
```

**Quick MCP attach (Claude Code / Codex):**

```bash
gbrain init --pglite                     # local brain, 2 seconds, no Docker
claude mcp add gbrain -- gbrain serve    # or: codex mcp add gbrain -- gbrain serve
```

**Remote brain attach:**

```bash
gbrain connect https://your-host/mcp --token gbrain_xxx --install
```

**CLI standalone:**

```bash
bun install -g github:garrytan/gbrain
gbrain init --pglite && gbrain import ~/notes/ && gbrain query "..."
```

## Key features

- **Hybrid search** — vector (HNSW/pgvector) + BM25 + reciprocal-rank fusion + source-tier boost + ZeroEntropy reranker. Three named modes (`conservative` / `balanced` / `tokenmax`). Per-query graph signals for adjacency, cross-source corroboration, and session demote. `gbrain search "<q>" --explain` shows per-stage attribution.
- **Synthesis layer** (`gbrain think`) — retrieves, then composes cited-prose answers with explicit gap analysis identifying what is missing, stale, or contradicted.
- **Self-wiring knowledge graph** — every `put_page` extracts wikilink/typed-link references and writes edges (`attended`, `works_at`, `invested_in`, `founded`, `advises`) with zero LLM calls. Multi-hop traversal via `gbrain graph-query`. +31.4 P@5 lift over vector-only RAG.
- **Dream cycle** — 66 cron jobs: dedup people pages, fix citations, score salience, find contradictions, prep tasks. Runs while you sleep.
- **Schema packs** — customizable page-type taxonomy (default: 15-type `gbrain-base-v2`). `gbrain schema detect` + `gbrain schema suggest` + `gbrain schema review-candidates` let agents evolve the schema on your behalf.
- **43 curated skills** — covers signal capture, ingest, enrichment, querying, brain ops, citation fixing, task management, cron scheduling, reports, voice, skill creation, eval framework, and migrations.
- **Minions (job queue)** — BullMQ-shaped, Postgres-native queue. Durable subagents surviving crashes via two-phase pending→done persistence. Rate leases for outbound providers.
- **MCP server** — 30+ tools over stdio or HTTP with OAuth 2.1. Supports Claude Code, Codex, Cursor, Claude Desktop, Perplexity Computer, and ChatGPT.

## Architecture

**Two engines, one contract.** `BrainEngine` interface (`src/core/engine.ts`, ~47 ops) is implemented by both PGLite (Postgres 17 via WASM, default, personal brains up to ~50K pages) and standard Postgres + pgvector (Supabase or self-hosted, for shared/large/multi-machine).

**Brain repo is the system of record.** Knowledge lives in a regular git repo as markdown files. GBrain syncs the repo into Postgres; git deletes become soft-deletes in DB. Allows publishing public subsets and federated team mounts.

**Two organizational axes.** A *brain* is a database (personal or team mount). A *source* is a repo inside that brain (wiki, gstack, essays). Routing via `.gbrain-source` dotfiles on a documented 6-tier precedence chain.

**Deployment topologies** (`docs/architecture/topologies.md`):
1. Single brain — local PGLite or Supabase
2. Cross-machine thin client — agent on one host, `gbrain serve --http` on another
3. Split-engine — per-worktree code indices for Conductor/agent parallelism

## Example usage

```bash
# query: raw retrieval vs synthesized answer
gbrain search "who's working on AI agents at portfolio companies?"
gbrain think "what did I promise Alice last week?"

# capture to the brain
gbrain capture "the thought I want to remember"
gbrain capture --file ./notes/today.md

# schema operations
gbrain schema detect && gbrain schema suggest && gbrain schema review-candidates --apply

# ops
gbrain doctor          # health check + repair hints
gbrain sync            # sync git repo to DB
gbrain eval longmemeval  # run public LongMemEval benchmark
```

Webhooks for mobile/Zapier/IFTTT:
```bash
curl -X POST https://your-brain/ingest \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: text/markdown" \
  -d "# a thought from a Shortcut"
```

## Maintenance status

Active development (latest push 2026-06-18). 23,293 stars, 3,335 forks. MIT license. No tagged release — version tracked via `VERSION` file. Built and maintained by Garry Tan; community PRs batched into release waves with `Co-Authored-By:` attribution. ZeroEntropy provides default embedding + reranker stack. The sibling [gbrain-evals](https://github.com/garrytan/gbrain-evals) repo holds BrainBench scorecards.

## Ecosystem

- **[[garrytan-gstack]]** — sibling repo from the same author; a Claude Code skills + agent workflow layer that pairs with GBrain as the retrieval backend
- **[[hermes-agent.nousresearch.com]] / [[felix-forever-hermes-agent-desktop]]** — GBrain is the documented production brain for Hermes agent deployments
- **OpenClaw** (`github.com/openclawagents/openclaw`) — the other primary agent platform GBrain is designed to run on (deploy AlphaClaw on Render)
- **[[supermemory.ai]]** — alternative persistent memory API for AI agents; similar knowledge-graph + RAG positioning but API-first and benchmark-oriented rather than self-hosted git-backed
- Integration recipes: Twilio voice, email/calendar webhooks, 16 embedding providers, llama.cpp local reranker, Supabase, Fly.io, Railway
