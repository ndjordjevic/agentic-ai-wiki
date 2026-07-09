---
type: source
category: "Knowledge, RAG, memory & context"
source_url: https://github.com/cocoindex-io/cocoindex
tags:
  - incremental-indexing
  - rag-pipeline
  - agent-context
  - vector-database
  - data-engineering
  - rust-core
  - python-sdk
  - long-horizon-agents
related:
  - HKUDS-RAG-Anything
  - zilliztech-claude-context
  - GoogleCloudPlatform-knowledge-catalog
product: cocoindex
detail_level: standard
created: 2026-07-06
updated: 2026-07-06
---

CocoIndex is an open-source incremental data pipeline engine (10,613 stars, Apache 2.0, Rust core with Python API) that keeps AI agent context continuously fresh by reprocessing only the delta whenever source data or pipeline code changes — turning codebases, PDFs, Slack, meeting notes, inboxes, and videos into always-current vector indexes, knowledge graphs, and structured targets in seconds rather than hours.

_All claims below are sourced from ../../raw/github/cocoindex-io-cocoindex.md unless otherwise noted._

## What it does

CocoIndex takes a declarative, React-inspired approach to data engineering: you declare `TargetState = Transform(SourceState)` in Python, and the Rust engine figures out the minimal set of changes needed to keep that target in sync whenever anything upstream shifts. There is no delta logic to write, no backfill scaffolding to maintain. The engine tracks fine-grained per-row provenance so it can invalidate exactly the affected records — both when source files change and when pipeline code changes — without touching anything else.

## Key features

- **Incremental at two levels:** component-level (skip unchanged source items entirely) and function-level (`@coco.fn(memo=True)` caches expensive transforms by `hash(input) + hash(code)`)
- **Sub-second freshness:** source change → target update in under a second at any corpus size
- **10× cost reduction at scale:** on a 10,000-row corpus, only the Δ ~0.1% re-embeds; the rest is cached
- **Full lineage:** every vector or row in the target traces back to its exact source byte — satisfies EU AI Act auditability requirements
- **Python-first API:** write batch-style `async def` functions; the engine handles all incrementality
- **Open connector model:** sources (local FS, S3, Google Drive, Postgres, Kafka) and targets (pgvector, LanceDB, Qdrant, Neo4j, Kuzu, Kafka, Snowflake) plug in via a standard interface

## Architecture

CocoIndex's architecture separates a Rust core (`rust/core`) — which owns change detection, state tracking, memoization, retries, and target reconciliation — from a Python layer (`python/cocoindex`) that exposes the declarative API. The `rust/py` crate bridges them via PyO3, offering both async and blocking entry points so the same pipeline runs from a script or a long-running daemon. (../../raw/github/cocoindex-io-cocoindex.md)

Key abstractions:
- **App:** the top-level pipeline entity; reads sources, transforms data, declares target states
- **Processing Component:** groups one source item's transforms + target states; runs independently and commits atomically
- **`@coco.fn(memo=True)`:** hash-gated memoization; skip when `hash(input)` and `hash(code)` match a previous run
- **Connectors:** pluggable source/target adapters (`connectors/` package) — no vendor lock-in (../../raw/github/cocoindex-io-cocoindex.md)

## Installation

```sh
pip install -U cocoindex
```

Requires Python 3.10–3.13 and a PostgreSQL instance (for state storage). The Rust engine ships as a pre-built wheel. (../../raw/github/cocoindex-io-cocoindex.md)

## Example usage

```python
import cocoindex as coco
from cocoindex.connectors import localfs, postgres
from cocoindex.ops.text import RecursiveSplitter

@coco.fn(memo=True)
async def index_file(file, table):
    for chunk in RecursiveSplitter().split(await file.read_text()):
        table.declare_row(text=chunk.text, embedding=embed(chunk.text))

@coco.fn
async def main(src):
    table = await postgres.mount_table_target(PG, table_name="docs")
    table.declare_vector_index(column="embedding")
    await coco.mount_each(index_file, localfs.walk_dir(src).items(), table)

coco.App(coco.AppConfig(name="docs"), main, src="./docs").update_blocking()
```

Run once to backfill; re-run anytime — only changed files re-embed. The repo ships 20+ ready-to-run examples covering code embedding, PDF → RAG, HN trending topics (Gemini 2.5 Flash), conversation → knowledge graph (Neo4j/Kuzu), multi-repo summarization, structured extraction (BAML/DSPy), podcast knowledge graph, and CSV → Kafka. (../../raw/github/cocoindex-io-cocoindex.md)

## When to use

CocoIndex is the right layer when your AI agent needs context that must stay current as source data evolves — not a one-off batch index that goes stale. Ideal for: production RAG apps where documents are edited daily; coding agents that need fresh semantic search over an evolving codebase; knowledge graphs that grow as conversations or issues accumulate; any pipeline where re-embedding everything on each run is too slow or too expensive.

## Maintenance status

Active and rapidly growing — 10,613 stars, v1.0.15 released 2026-07-04, latest commit 2026-07-06. Apache 2.0 license. The repo is a fundamental redesign (v1 on `main`); v0 is preserved on the `v0` branch. Enterprise tier available at cocoindex.io/enterprise for PB-scale deployments. (../../raw/github/cocoindex-io-cocoindex.md)

## Ecosystem

**Flagship product — CocoIndex-code:** an MCP server built on CocoIndex that gives AI coding agents (Claude Code, Cursor) AST-aware, incremental, semantic code search with call graphs, symbol lookup, and blast-radius analysis. Install with `uv tool install 'cocoindex-code[full]'` and query via the `ccc search` CLI. (../../raw/github/cocoindex-io-cocoindex.md)

**Community:** Discord (discord.com/invite/zpA9S2DR7s), YouTube (@cocoindex-io), blog (cocoindex.io/blogs), X (@cocoindex_io).

Related ingested sources: [[HKUDS-RAG-Anything]] covers multimodal RAG pipelines that CocoIndex can power as the incremental data layer; [[zilliztech-claude-context]] covers Milvus-backed semantic code search as an MCP plugin — a narrower alternative to the CocoIndex-code flagship.
