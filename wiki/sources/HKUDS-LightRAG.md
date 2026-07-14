---
type: source
category: "Knowledge, RAG, memory & context"
source_url: https://github.com/HKUDS/LightRAG
tags:
  - graph-rag
  - knowledge-graph
  - dual-layer-retrieval
  - incremental-indexing
  - multimodal-parsing
  - role-specific-llm-config
  - lightrag-server
related:
  - HKUDS-RAG-Anything
  - zilliztech-claude-context
product: lightrag
detail_level: standard
created: 2026-07-14
updated: 2026-07-14
---

LightRAG (EMNLP 2025) is a lightweight, graph-based Retrieval-Augmented Generation framework positioned as an efficient alternative to Microsoft GraphRAG. It combines a knowledge-graph layer with vector embeddings in a dual-layer architecture, aiming to keep both indexing cost and query latency low while still capturing the cross-entity relationships that pure chunk-based RAG misses. It's the base framework behind [[HKUDS-RAG-Anything]], the same lab's multimodal extension (PDFs, images, tables, formulas via MinerU/Docling), which was merged back into this repo as of the 2026.05 release.

_All claims below are sourced from ../../raw/github/HKUDS-LightRAG.md unless otherwise noted._

## What it does

Indexes documents into a combined knowledge graph + vector store, then answers queries by retrieving both specific entities/relations (graph layer) and semantically similar chunks (vector layer). New documents are merged incrementally into the existing graph via set merging rather than triggering a full rebuild; deletions reuse cached LLM extraction results from construction time to rapidly recompute affected entity/relation descriptions.

## Installation

```bash
uv tool install "lightrag-hku[api]"      # LightRAG Server, recommended via uv
cd lightrag_webui && bun install --frozen-lockfile && bun run build && cd ..
cp env.example .env                       # configure LLM + embedding providers
lightrag-server                            # binds 0.0.0.0 by default — configure
                                            # LIGHTRAG_API_KEY or AUTH_ACCOUNTS+TOKEN_SECRET
                                            # (or bind 127.0.0.1) before exposing on a network
```
Also installable via `git clone` + `make dev`, or Docker Compose (`docker compose up`); official GHCR images are signed with Sigstore Cosign via GitHub OIDC.

## Key features

- **Four query modes** — `local` (precise entity matching), `global` (macro/cross-document themes), `hybrid` (merges local+global), `naive` (plain vector RAG, no graph), and the default `mix` (all three combined, slightly slower than `naive` but the most comprehensive).
- **Role-specific LLM configuration** — four independently configurable roles: `EXTRACT` (fast, non-thinking model recommended — runs per chunk), `QUERY` (should be the strongest model, writes the final answer from noisy retrieved context), `KEYWORD` (lightweight, must be non-thinking to keep latency low), and `VLM` (any multimodal model with image input).
- **Multi-engine multimodal document parsing** — Native, MinerU, and Docling engines extract text, tables, formulas, and images, with cross-modal entity/relation mapping into the same graph.
- **Incremental updates without full rebuilds** — the standout architectural claim: new data is indexed once and merged into the existing graph via set merging, and deletions rebuild only the affected entity/relation descriptions using cached LLM extraction output.
- **Pluggable storage backends** — four storage roles (KV, vector, graph, doc-status), each independently swappable; single-backend options are PostgreSQL, MongoDB, or OpenSearch, or specialized stores (Milvus/Qdrant for vectors, Neo4j/Memgraph for graphs). Defaults are file-persisted in-memory stores, explicitly dev/debug-only.

## Architecture

Dual-layer design: a knowledge-graph index built via LLM-driven entity/relation extraction over text chunks, plus a parallel vector index over the same chunks/entities/relations. `LightRAG Server` exposes both a web UI and a full REST API (recommended integration path); an embedded Python SDK exists for research/evaluation use but some features are SDK-only and considered experimental. Concurrency is tuned via `MAX_ASYNC_LLM`/`MAX_PARALLEL_INSERT` (files processed in parallel, ideally ~1/3 of `MAX_ASYNC_LLM`)/`MAX_PARALLEL_PARSE_MINERU`/`MAX_PARALLEL_PARSE_DOCLING`/`EMBEDDING_FUNC_MAX_ASYNC`/`EMBEDDING_BATCH_NUM`.

## Example usage

```bash
export OPENAI_API_KEY="sk-...your_openai_key..."
curl https://raw.githubusercontent.com/gusye1234/nano-graphrag/main/tests/mock_data.txt > ./book.txt
python examples/lightrag_openai_demo.py
```
Only `lightrag_openai_demo.py` and `lightrag_openai_compatible_demo.py` are officially supported example scripts; the rest of `examples/` are untested community contributions.

## Maintenance status

37,654 stars, 5,300 forks, MIT license, latest release v1.5.5rc1 (2026-07-13), pushed 2026-07-13 — very active (GitHub Trending). The paper (arXiv:2410.05779) reports LightRAG beating NaiveRAG, RQ-RAG, HyDE, and GraphRAG on comprehensiveness, diversity, empowerment, and overall quality across agriculture, CS, legal, and mixed-domain evaluation sets; the maintaining lab (HKUDS) also publishes RAG-Anything, VideoRAG, and MiniRAG as related projects.
