# cocoindex-io/cocoindex

## Metadata
- Stars: 10,613
- Primary language: Rust (Python API layer)
- Default branch: main
- Latest release: v1.0.15 (2026-07-04)
- License: Apache License 2.0
- Homepage: https://cocoindex.io
- Fetched: 2026-07-06
- Final URL: https://github.com/cocoindex-io/cocoindex

## Description
Incremental engine for long horizon agents 🌟 — CocoIndex turns codebases, meeting notes, inboxes, Slack, PDFs, and videos into live, continuously fresh context for AI agents and LLM apps, with minimal incremental processing.

## README

CocoIndex is an ultra-performant framework for building data processing pipelines for AI workloads, with built-in incremental processing.

**Key properties:**
- **Incremental**: only the delta — recomputes only changed data, not the whole corpus
- **Any scale**: parallel by default
- **Declarative**: Python, 5 min to production

### Install

```sh
pip install -U cocoindex
```

### Quick example

```python
import cocoindex as coco
from cocoindex.connectors import localfs, postgres
from cocoindex.ops.text import RecursiveSplitter

@coco.fn(memo=True)                          # cached by hash(input) + hash(code)
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

Run once to backfill. Re-run anytime — only the changed files re-embed.

### The React Mental Model for Data Engineering

CocoIndex uses a declarative, state-driven programming model: `TargetState = Transform(SourceState)`. You declare *what* your target should look like as a function of your source data — CocoIndex handles change detection and applies only the necessary updates automatically.

Analogy:
- **React**: declare UI as a function of state → React re-renders what changed
- **Spreadsheets**: declare formulas → cells recompute when inputs change
- **CocoIndex**: declare target states as a function of source → CocoIndex syncs what changed

### Why incremental?

1. **Sub-second freshness** — source changes propagate in under a second
2. **10× cheaper at scale** — on a 10,000-row corpus, only the Δ 0.1% re-runs; 99.9% stays cached
3. **Explainable by default** — every vector/row traces back to its exact source byte; compliant with EU AI Act auditing
4. **Production-grade Rust core** — retries, back-off, dead-letter queues, no data loss

### What you can build (20+ examples)

- Real-time code index (git repo → pgvector/LanceDB, AST-aware chunking)
- PDF → RAG index (local/S3/Google Drive → pgvector/LanceDB)
- HN trending topics (Algolia API + Gemini 2.5 Flash LLM extraction → Postgres)
- Conversation → knowledge graph (meeting transcripts/Slack/podcasts → Neo4j/Kuzu)
- Multi-repo summarization (N git repos → rolled-up summary)
- Structured extraction (forms/PDFs/invoices → typed schema via BAML/DSPy)
- Podcast → knowledge graph (YouTube audio, speaker diarization, → SurrealDB/Neo4j)
- CSV → Kafka live (folder of CSVs → Kafka topic on StreamNative/Confluent)

### CocoIndex-code (flagship product)

Built on CocoIndex: an MCP server for AI coding agents providing AST-aware, incremental, semantic code indexing. Features call graphs, symbol lookup, blast-radius analysis, and vector embeddings. Supports Python, TypeScript, Rust, and Go. Sub-second freshness, 80–90% cache hits on re-index.

### Enterprise

PB-scale incremental indexing: 10× fewer LLM/embedding calls vs. full recompute, 100% lineage coverage, Δ-only processing.

### Community

- Discord: https://discord.com/invite/zpA9S2DR7s
- YouTube: https://www.youtube.com/@cocoindex-io
- Blog: https://cocoindex.io/blogs/
- X: https://x.com/cocoindex_io

## Docs

### Getting Started Overview

CocoIndex is an ultra-performant framework for building data processing pipelines for AI workloads, with built-in incremental processing.

**Programming model:** Declarative, state-driven. You specify *what* your target should look like as a function of your source data — not *how* to incrementally update it. CocoIndex handles change detection and applies only the necessary updates automatically.

**Features:**
- High-performance Rust 🦀 engine
- Easy to code (Python, no new DSLs, batch-style code without delta logic)
- Incremental & low-latency (hours/days → seconds)
- Full lineage & explainability (EU AI Act compliant)
- Open integration model (no vendor lock-in, full Python ecosystem)
- High throughput + controlled concurrency (automatic parallelization)
- Fault-tolerant runtime (retries, resume from progress)
- Low operational overhead

**Incremental processing mechanisms:**
- Component level: only reprocess source items with changes
- Function level: memoize expensive function calls, reuse when possible
- Target level: apply minimum necessary changes (insertions, updates, deletions)

### Core Concepts

**Incremental processing:** When processing data and storing results for AI agents, both data and code evolve over time. Reprocessing everything is expensive. CocoIndex solves by tracking fine-grained dependencies: `TargetState = Transform(SourceState)`.

**App:** The top-level executable entity. Reads state from sources, transforms data, declares target states. CocoIndex syncs these to external systems (Postgres, vector DBs, etc.).

**Processing Component:** Groups an item's processing together with its target states. Each component runs independently and applies its target states as a unit (atomically when the backend supports transactions). Example: process one file → split into chunks → embed each chunk → upsert all vectors in one transaction.

**Function Memoization (`@coco.fn(memo=True)`):** Skip a function when its input AND code are unchanged from a previous run. Two levels:
- *Processing component level*: entire component skipped if file + logic unchanged
- *Transform level*: individual embed calls skipped if chunk text + model unchanged

On code change: all components reprocess, but memoized intermediate results (e.g., embeddings of unchanged chunks) are still reused.

## Top-level structure

```
cocoindex/
├── rust/               ← Rust workspace (core engine, PyO3 bindings, utilities)
│   ├── core/           ← Core engine (engine/, state/, inspect/)
│   ├── py/             ← Python bindings (PyO3)
│   ├── py_utils/       ← Python-Rust utility helpers
│   ├── utils/          ← General utilities (error, batching, fingerprint)
│   └── ops_text/       ← Text processing ops (splitter, language detection)
├── python/
│   └── cocoindex/      ← Python package
│       ├── __init__.py
│       ├── cli.py
│       ├── _internal/  ← Core API (api.py, app.py, function.py, target_state.py)
│       ├── connectors/ ← localfs, postgres, qdrant, lancedb, google_drive
│       ├── resources/  ← FileLike, Chunk, schema
│       └── ops/        ← text.py (RecursiveSplitter), sentence_transformers.py
├── examples/           ← 20+ example apps (code_embedding, pdf_embedding, hn_trending_topics, conversation_to_knowledge, csv_to_kafka, patient_intake_extraction_baml, ...)
├── docs/               ← Astro-based documentation site
├── skills/             ← CocoIndex agent skill (SKILL.md for AI coding agents)
├── .agents/            ← Agent skills symlinks
├── .claude/            ← Claude Code hooks and skills
├── AGENTS.md           ← Coding agent guide (build commands, code structure, conventions)
├── CLAUDE.md           ← Claude Code compatibility (imports AGENTS.md)
├── Cargo.toml          ← Rust workspace manifest
├── pyproject.toml      ← Python project manifest (uv)
└── dev/                ← Development utilities and agent playbooks
```

**Key notes:**
- Rust core (`rust/core`, `rust/utils`) is **async-first** with Tokio
- `rust/py` bridges Rust async to Python; Python API is **async-first** with sync wrappers available
- CocoIndex v1 (main branch) is a fundamental redesign from v0 (preserved on `v0` branch)
- All diagrams are inline Astro components under `docs/src/components/diagrams/`

**Build and test:**
```bash
uv run maturin develop   # Build Rust + install Python (required after Rust changes)
cargo test               # Run Rust tests
uv run pytest python/    # Run Python tests
uv run mypy              # Type check Python
uv run ruff format .     # Format Python
uv run ruff check .      # Lint Python
```

**Agent tooling:** Uses `ccc` CLI (cocoindex-code) for semantic search over the repo codebase. Agent playbooks under `dev/agent-skills/`.
