# garrytan/gbrain

## Metadata
- Stars: 23293
- Primary language: TypeScript
- Default branch: master
- Latest release: (none)
- License: MIT
- Homepage: (none)
- Fetched: 2026-06-18
- Final URL: https://github.com/garrytan/gbrain

## Description
Garry's Opinionated OpenClaw/Hermes Agent Brain — a persistent knowledge-graph and hybrid retrieval layer for AI agents. Designed as the production brain for Garry Tan's (YC President/CEO) OpenClaw and Hermes agent deployments: 146,646 pages, 24,585 people, 5,339 companies, 66 cron jobs. Supports personal and team (company-brain) use with per-user access scoping.

## README

# GBrain

**Search gives you raw pages. GBrain gives you the answer.** It's the brain layer your AI agent has been missing — the only one that does synthesis, graph traversal, and gap analysis in one box. Run a full autonomous agent on top of it, or just wire it into Claude Code or Codex as a supercharged retrieval layer in one command; either way your coding agent stops being amnesiac about everything that isn't code.

I'm Garry Tan, President and CEO of Y Combinator. I built GBrain to run my own AI agents. It's the production brain behind my OpenClaw and Hermes deployments: **146,646 pages, 24,585 people, 5,339 companies**, 66 cron jobs running autonomously. My agent ingests meetings, emails, tweets, voice calls, and original ideas while I sleep. It enriches every person and company it encounters. It fixes its own citations and consolidates memory overnight. I wake up smarter than when I went to bed — and so will you.

**And now it works as a company brain too.** Each person on the team gets their own slice of the brain, scoped by login. Drop GBrain in as your team's shared institutional memory.

Lots of personal-knowledge systems give you keyword matching and grep in a box. GBrain does that, and adds two things nobody else ships together:

- **A synthesis layer that gives you the actual answer.** Synthesized, well-cited prose across people, companies, deals, and ideas. Not "here are 10 chunks that mention your query"; an actual answer with citations and an explicit note on what the brain doesn't know yet. The gap analysis is the part that changes how you use the brain.
- **A self-wiring knowledge graph.** Every page write extracts entity refs and creates typed edges (`attended`, `works_at`, `invested_in`, `founded`, `advises`) with zero LLM calls. Benchmarked: **P@5 49.1%, R@5 97.9%** on a 240-page corpus, **+31.4 points P@5** over its graph-disabled variant and over ripgrep-BM25 + vector-only RAG.

### Install

**Have your agent install it (recommended).** Paste this into your agent (Claude Code, Codex, Cursor, OpenClaw, Hermes):

```
Retrieve and follow the instructions at:
https://raw.githubusercontent.com/garrytan/gbrain/master/INSTALL_FOR_AGENTS.md
```

**Quick start: Claude Code or Codex.**

```bash
gbrain init --pglite                     # 2-second local brain (no Docker)
claude mcp add gbrain -- gbrain serve    # or: codex mcp add gbrain -- gbrain serve
```

**Already have a brain on a remote host?**

```bash
gbrain connect https://your-host/mcp --token gbrain_xxx --install               # Claude Code
gbrain connect https://your-host/mcp --token gbrain_xxx --agent codex --install # Codex
```

**CLI standalone (no agent):**

```bash
bun install -g github:garrytan/gbrain
gbrain init --pglite
gbrain doctor
gbrain import ~/notes/
gbrain query "what themes show up across my notes?"
```

### MCP Clients

GBrain exposes 30+ tools over MCP (stdio and HTTP):
- **Claude Code** — `claude mcp add gbrain -- gbrain serve` or `gbrain connect ... --install`
- **Codex** — `gbrain connect ... --agent codex --install`
- **Cursor / Windsurf** — add `{"command": "gbrain", "args": ["serve"]}` to MCP config
- **Claude Desktop** — Settings → Integrations → add HTTP server URL
- **Perplexity Computer** — `gbrain connect ... --agent perplexity --oauth --register`
- **ChatGPT** — OAuth 2.1 with PKCE

### Two ways to query your brain

```bash
gbrain search "who's working on AI agents at portfolio companies?"  # raw retrieval, no LLM cost
gbrain think "who's working on AI agents at portfolio companies?"   # synthesized answer + gap analysis
```

`gbrain think` runs retrieval then composes a synthesized answer with explicit citations to source pages AND an honest note on what the brain doesn't know yet. The gap analysis is the differentiator.

### How to get data in

```bash
gbrain capture "the thought I want to remember"
gbrain capture --file ./notes/today.md
echo "from a pipe" | gbrain capture --stdin
```

For webhook ingestion (Zapier / IFTTT / Apple Shortcuts):
```bash
curl -X POST https://your-brain/ingest \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: text/markdown" \
  -d "# a thought from a Shortcut"
```

### Schema packs

GBrain ships with bundled schema packs and lets you author your own:
- **`gbrain-base-v2`** (default) — 15-type DRY/MECE canonical taxonomy: `person`, `company`, `media`, `tweet`, `social-digest`, `analysis`, `atom`, `concept`, `source`, `deal`, `email`, `slack`, `writing`, `project`, `note`
- **`gbrain-base`** (legacy) — the original 24-type layout
- **`gbrain-recommended`** — extends `gbrain-base` with 13 additional directories
- **Your own pack** — `gbrain schema detect` + `gbrain schema suggest` + `gbrain schema review-candidates --apply`

### Architecture

**Two engines, one contract.** PGLite (Postgres 17 via WASM, zero-config, default) for personal brains up to ~50K pages. Postgres + pgvector (Supabase or self-hosted) for shared/large/multi-machine deployments. The `BrainEngine` interface in `src/core/engine.ts` defines ~47 operations both engines implement.

**Brain repo is the system of record.** Knowledge lives in a regular git repo as markdown files. GBrain syncs the repo into Postgres for retrieval.

**Two organizational axes (brain ⊥ source).** A *brain* is a database. A *source* is a repo inside that brain (wiki, gstack, essays, knowledge base). Routing via `.gbrain-source` dotfiles.

**Hybrid search.** Vector (HNSW on pgvector) + BM25 keyword + reciprocal-rank fusion + source-tier boost + intent-aware query rewriting. Three named search modes (`conservative`, `balanced`, `tokenmax`). Per-query graph signals for adjacency boost, cross-source corroboration, and session demote. `gbrain search "<query>" --explain` shows per-stage attribution.

**Self-wiring knowledge graph.** Every `put_page` extracts entity refs and writes typed edges with zero LLM calls. Multi-hop traversal via `gbrain graph-query`. +31.4 P@5 lift over vector-only RAG.

**Job queue (Minions).** BullMQ-shaped, Postgres-native job queue. Durable subagents surviving crashes via two-phase pending→done persistence. Rate leases for outbound providers.

**43 curated skills.** Covers signal capture, ingest, enrichment, querying, brain ops, citation fixing, daily task management, cron scheduling, reports, voice, soul audit, skill creation, eval framework, and migrations.

**Eval framework.** `gbrain eval longmemeval`, `gbrain eval retrieval-quality` (NamedThingBench), `gbrain eval cross-modal`.

**Dream cycle.** 66 cron jobs running autonomously: dedup people pages, fix citations, score salience, find contradictions, prep tomorrow's tasks.

### Tutorials

- [Set up your personal AI agent + brain from zero](docs/tutorials/personal-brain.md)
- [Set up GBrain as your company brain](docs/tutorials/company-brain.md)
- [Auto-improve a skill with `gbrain skillopt`](docs/tutorials/improving-skills-with-skillopt.md)

### Integrations

- **Voice**: Phone calls → brain pages via Twilio + OpenAI Realtime
- **Email + calendar**: webhook handlers routing to brain signals
- **Embedding providers**: 16 recipes (OpenAI, OpenRouter, Voyage, ZeroEntropy, Gemini, Azure, Ollama, LiteLLM, etc.)
- **Rerankers**: ZeroEntropy `zerank-2` (default) + llama.cpp local reranker
- **MCP clients**: Claude Code, Codex, Cursor, Claude Desktop, Perplexity, ChatGPT

## Docs

Key architecture documents:
- `docs/INSTALL.md` — all install paths end-to-end
- `docs/architecture/topologies.md` — single brain, cross-machine thin client, split-engine
- `docs/architecture/RETRIEVAL.md` — hybrid search, graph traversal, retrieval theory
- `docs/architecture/brains-and-sources.md` — two organizational axes (brain ⊥ source)
- `docs/architecture/schema-packs.md` — schema pack authoring, seven-tier resolution chain
- `docs/what-schemas-unlock.md` — 7 killer use cases for typed page kinds
- `docs/guides/` — how-to runbooks (sub-agent routing, minion deployment, skill development)
- `docs/mcp/` — per-client MCP setup
- `docs/eval/` — eval framework, metric glossary
- `AGENTS.md` — entry point for non-Claude agents
- `CLAUDE.md` — entry point for Claude Code
- `skills/RESOLVER.md` — routing for 43 curated skills

## Top-level structure

```
.
├── AGENTS.md                  # entry point for non-Claude agents
├── CLAUDE.md                  # entry point for Claude Code (deep operating context)
├── CONTRIBUTING.md            # contributor guide, test discipline
├── DESIGN.md                  # design rationale
├── INSTALL_FOR_AGENTS.md      # agent-driven install protocol
├── SECURITY.md                # OAuth threat model, hardening defaults
├── CHANGELOG.md               # versioned release notes
├── README.md
├── VERSION                    # current version
├── gbrain.yml                 # brain config
├── llms.txt                   # documentation map for LLMs
├── llms-full.txt              # same map with core docs inlined
├── openclaw.plugin.json       # OpenClaw plugin manifest
├── package.json               # bun/TypeScript package
├── admin/                     # admin dashboard
├── docs/                      # architecture, guides, MCP setup, eval, tutorials
│   ├── architecture/          # system design docs (topologies, retrieval, schema-packs, ...)
│   ├── guides/                # how-to runbooks
│   ├── integrations/          # external data source connectors
│   ├── mcp/                   # per-client MCP setup
│   ├── eval/                  # eval framework and methodology
│   ├── tutorials/             # step-by-step walkthroughs
│   └── ethos/                 # philosophy and origin story
├── evals/                     # eval runners
├── examples/                  # usage examples
├── recipes/                   # integration recipes (voice, email, etc.)
├── skills/                    # 43 curated agent skills; RESOLVER.md routes them
├── src/                       # TypeScript source
│   └── core/engine.ts         # BrainEngine interface (~47 ops, both PGLite + Postgres)
├── templates/                 # page and schema templates
├── test/ & tests/             # test suites
└── tools/                     # developer tools
```
