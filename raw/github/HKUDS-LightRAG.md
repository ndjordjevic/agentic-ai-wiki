# HKUDS/LightRAG

## Metadata
- Stars: 37654
- Primary language: Python
- Default branch: main
- Latest release: v1.5.5rc1 (2026-07-13)
- License: MIT License
- Homepage: https://arxiv.org/abs/2410.05779
- Fetched: 2026-07-14
- Final URL: https://github.com/HKUDS/LightRAG

## Description
[EMNLP2025] "LightRAG: Simple and Fast Retrieval-Augmented Generation"

## README
# LightRAG: Simple and Fast Retrieval-Augmented Generation

## News (selected, recent)
- [2026.05] Merged RagAnything into LightRAG — multimodal content parsing/extraction via MinerU/Docling services.
- [2026.05] Four selectable text chunking strategies: `Fix`, `Recursive`, `Vector`, `Paragraph`.
- [2026.05] Role-specific LLM configuration: 4 distinct roles (EXTRACT, QUERY, KEYWORDS, VLM) with independent LLM settings.
- [2026.03] Integrated OpenSearch as a unified storage backend for all four LightRAG storage types.
- [2026.03] Setup wizard for local deployment of embedding, reranking, and storage backends via Docker.
- [2025.11] Integrated RAGAS for Evaluation and Langfuse for Tracing; API returns retrieved contexts for context-precision metrics.
- [2025.10] Eliminated processing bottlenecks for large-scale datasets.
- [2025.08] Reranker support (default query mode boost for mixed queries); Document Deletion with automatic KG regeneration.
- [2025.06] Released RAG-Anything — an all-in-one multimodal RAG system; LightRAG gained multimodal handling via RAG-Anything integration (PDFs, images, Office docs, tables, formulas).
- [2025.03] Citation functionality for source attribution and document traceability.
- [2025.01] Released MiniRAG (simpler RAG with small models) and VideoRAG (long-context video RAG); PostgreSQL as unified storage.
- [2024.11] LightRAG WebUI for insert/query/visualize; Neo4J storage support.

## Installation

**Using uv for package management** (recommended): `curl -LsSf https://astral.sh/uv/install.sh | sh` (Unix/macOS) or the PowerShell equivalent on Windows. pip also works.

### Install LightRAG Server

```bash
# Install from PyPI as a tool (recommended)
uv tool install "lightrag-hku[api]"

# Build front-end artifacts
cd lightrag_webui
bun install --frozen-lockfile
bun run build
cd ..

# Setup env file
cp env.example .env  # Update with LLM and embedding configurations
# SECURITY: binds to 0.0.0.0 by default. Configure LIGHTRAG_API_KEY or
# AUTH_ACCOUNTS + TOKEN_SECRET before exposing on a network, or bind to
# 127.0.0.1 for local-only access — without auth every endpoint is public.
# The Ollama-compatible /api/* routes stay open by default for client
# compatibility; set WHITELIST_PATHS=/health to require auth on them too.
lightrag-server
```

Installation from source uses `make dev` (bootstraps venv, test toolchain, full offline stack, builds frontend) or manual `uv sync --extra test --extra offline`. Docker Compose: `git clone`, `cp env.example .env`, `docker compose up`. Official GHCR images are signed with Sigstore Cosign via GitHub OIDC.

### Create .env File With Setup Tool

```bash
make env-base           # Required first step: LLM, embedding, reranker
make env-storage        # Optional: storage backends and database services
make env-server         # Optional: server port, auth, and SSL
make env-security-check # Optional: audit the current .env for security risks
```

### Optional: spaCy Models for docx smart_heading

The native docx parser's opt-in `smart_heading` engine uses spaCy for sentence/NER heuristics. Two pinned language models (`zh_core_web_sm`/`en_core_web_sm` 3.8.0, GitHub release wheels) install via `lightrag-download-cache --spacy --spacy-install`. Main Docker image ships them pre-installed (lite image does not).

## About LightRAG

### A Lightweight, Graph-Based RAG Framework

LightRAG is a lightweight knowledge-graph RAG framework, positioned as an efficient alternative to Microsoft GraphRAG. It uses a dual-layer architecture managing both knowledge graphs (KGs) and vector embeddings, bridging traditional vector-based RAG and graph-based RAG. Designed for high scalability, it addresses computational overhead, slow response times, and high incremental-update costs in large-scale graph indexing/retrieval, while still delivering high RAG quality even paired with a 30B open-source LLM.

### Features & Advantages

- **Deep Contextual Understanding**: graph-structured indexing captures complex semantic dependencies between entities, overcoming fragmented-context limitations of chunk-based retrieval; particularly strong in vertical domains (legal, financial) needing global comprehension.
- **Exceptional Comprehensiveness & Diversity**: dual-level retrieval integrates detailed facts and abstract concepts concurrently, effective for complex cross-document queries.
- **Extreme Retrieval Efficiency & Low Cost**: avoids inefficient community reports or multi-hop reasoning, drastically reducing LLM calls during indexing and querying.
- **Rapid Adaptation to Dynamic Data**: supports seamless incremental updates — new data generates a local graph merged directly into the existing graph via set merging, without rebuilding the global index. Deletions leverage LLM caching from construction to rapidly rebuild affected entity relationships.

### Multimodal Capability Upgrades (from v1.5)

- **Multi-Engine Document Parsing**: MinerU, Docling, and Native engines extract text, tables, formulas, images.
- **Cross-Modal Entity & Relation Mapping**: unified cross-modal extraction and relationship mapping.
- **Enhanced Application Scenarios**: improved RAG quality for multimodal-content-rich documents (operation manuals, academic papers).

### LightRAG API Server

Offers a web-based UI plus a comprehensive REST API (see `docs/LightRAG-API-Server.md`).

## Key Configuration Guide

### Selecting LLM Models

LightRAG requires LLM/VLMs for four roles:
- **Extraction LLM (`EXTRACT`)**: runs on every text chunk — fast, cost-effective, non-thinking model recommended (e.g. GPT-5.6-luna, Claude Haiku, Gemini-mini; DeepSeek-V4-lite/Kimi in China; Qwen3-30B-A3B-Instruct for local minimum).
- **Query LLM (`QUERY`)**: writes the final answer from long, noisy retrieved context — should be stronger than the extraction model; a thinking-capable model is fine.
- **Keyword LLM (`KEYWORD`)**: lightweight, latency-sensitive — must be non-thinking.
- **VLM (`VLM`)**: any mainstream multimodal model with image input (e.g. Qwen3.6-35B-A3B for local).

### Selecting Query Modes

Five query modes: **local** (precise entity matching), **global** (macro themes, cross-document reasoning), **hybrid** (merges local + global), **naive** (traditional vector-similarity RAG, no KG), **mix** (default; merges local + global + naive for the most comprehensive results, slightly slower than naive).

### Embedding Models

Recommend low-dimensional, fast, multilingual-capable models; `BAAI/bge-m3` for local deployment. The embedding model cannot be changed after document indexing without re-embedding everything (LightRAG has no built-in re-embedding tool); some backends (e.g. PostgreSQL) require the vector dimension fixed at table creation.

### Enabling Reranking

Improves query quality at a 1–2s latency cost; recommend local deployment (`BAAI/bge-reranker-v2-m3`). Unlike embedding models, the reranker can be changed at any time.

### Document Processing Pipeline

Recommended: `LIGHTRAG_PARSER=*:native-iteP,*:mineru-iteP,*:legacy-R` with `VLM_PROCESS_ENABLE=true` for image analysis. Locally deployed MinerU recommended over the rate-limited cloud service.

### Concurrency Optimization

Key env vars: `MAX_ASYNC_LLM`/`EXTRACT_ASYNC_LLM` (LLM concurrency), `MAX_PARALLEL_INSERT` (files processed in parallel, ~1/3 of `MAX_ASYNC_LLM`), `MAX_PARALLEL_PARSE_MINERU`/`MAX_PARALLEL_PARSE_DOCLING`, `EMBEDDING_FUNC_MAX_ASYNC`, `EMBEDDING_BATCH_NUM`.

### Selecting Backend Storage

Four storage types: KV_STORAGE, VECTOR_STORAGE, GRAPH_STORAGE, DOC_STATUS_STORAGE. Defaults are file-persisted in-memory stores (dev/debug only). Production options: PostgreSQL, MongoDB, or OpenSearch for a single unified backend, or specialized stores (Milvus/Qdrant for vectors, Neo4j/Memgraph for graphs).

### Resolving LLM Timeouts During Entity-Relation Extraction

Three usual causes with matching remedies (combinable): slow model → raise `*_LLM_TIMEOUT` (effective execution timeout is 2× the configured value); chunk produces too many entities/relations (e.g. bibliography chunks) → cap output length via `OPENAI_LLM_MAX_TOKENS`/`OPENAI_LLM_MAX_COMPLETION_TOKENS`; model stuck in an output loop (notably some local Qwen models) → re-process the document once; references specifically under paragraph-semantic (`P`) chunking → set `CHUNK_P_DROP_REFERENCES=true` to auto-drop the trailing reference section before chunking (also settable per-file via filename hint).

## Using LightRAG As SDK

The REST API (via LightRAG Server) is the recommended integration path; the SDK is intended for embedded applications or academic research/evaluation.

```bash
cd LightRAG
export OPENAI_API_KEY="sk-...your_openai_key..."
curl https://raw.githubusercontent.com/gusye1234/nano-graphrag/main/tests/mock_data.txt > ./book.txt
python examples/lightrag_openai_demo.py
```

Only `lightrag_openai_demo.py` and `lightrag_openai_compatible_demo.py` are officially supported sample scripts; other examples are community contributions.

## Replicating Findings in the Paper

LightRAG consistently outperforms NaiveRAG, RQ-RAG, HyDE, and GraphRAG across agriculture, computer science, legal, and mixed domains in comprehensiveness, diversity, empowerment, and overall score (full evaluation methodology in `docs/Reproduce.md`).

## Related Projects

- RAG-Anything — multimodal RAG
- VideoRAG — extreme long-context video RAG
- MiniRAG — extremely simple RAG

## Citation

```
@article{guo2024lightrag,
title={LightRAG: Simple and Fast Retrieval-Augmented Generation},
author={Zirui Guo and Lianghao Xia and Yanhua Yu and Tu Ao and Chao Huang},
year={2024},
eprint={2410.05779},
archivePrefix={arXiv},
primaryClass={cs.IR}
}
```

## Top-level structure
- `lightrag/` — core Python package (indexing, retrieval, storage backends)
- `lightrag_webui/` — web UI frontend (built with bun)
- `docs/` — extensive docs: API server, deployment (Docker/K8s/offline/multi-site), chunking strategies, role-specific LLM config, third-party parsers, sidecar format, reproduce guide (English + Chinese/Japanese variants)
- `examples/` — SDK usage demos (`lightrag_openai_demo.py`, `lightrag_openai_compatible_demo.py`, community-contributed others)
- `prompts/` — LLM prompt templates for extraction/query/keyword roles
- `reproduce/` — scripts to reproduce the paper's benchmark results
- `scripts/` — dev/ops scripts
- `tests/` — test suite
- `k8s-deploy/` — Kubernetes deployment manifests
- `Dockerfile`, `Dockerfile.lite`, `Dockerfile.postgres`, `docker-compose*.yml` — container build/deploy variants
- `setup.py`/`pyproject.toml`/`uv.lock` — Python packaging
- `CLAUDE.md`, `AGENTS.md` — agent instruction files
- `README-zh.md`, `README-ja.md` — localized READMEs
