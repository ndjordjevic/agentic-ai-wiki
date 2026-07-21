---
type: source
category: "Knowledge, RAG, memory & context"
source_url: https://github.com/topoteretes/cognee
tags:
  - ai-memory-platform
  - knowledge-graph
  - vector-embeddings
  - postgres-unified-backend
  - session-memory
  - ontology-grounding
  - claude-code-plugin
  - multi-language-clients
related:
  - supermemory.ai
  - garrytan-gbrain
  - HKUDS-LightRAG
  - HKUDS-RAG-Anything
product: cognee
detail_level: standard
created: 2026-07-21
updated: 2026-07-21
---

Cognee (28,990+ stars, Apache 2.0, Python) is an open-source AI memory platform that ingests data in any format and continuously builds a self-hosted knowledge graph, giving AI agents persistent long-term memory across sessions. It combines vector embeddings, graph reasoning, and cognitive-science-grounded ontology generation so stored content is both searchable by meaning and connected by relationships that evolve over time — with a distinctive architectural claim of running the entire memory layer (graph, vectors, sessions, metadata) on a single Postgres instance instead of a multi-service stack.

_All claims below are sourced from ../../raw/github/topoteretes-cognee.md unless otherwise noted._

## What it does

The core SDK exposes four operations: `remember` (store permanently, running add + cognify + improve), a session-scoped variant of `remember` (fast cache that syncs to the graph in the background), `recall` (query with auto-routing that picks the best search strategy automatically, or session-first with graph fallback), and `forget` (delete a dataset). A CLI (`cognee-cli remember|recall|forget`) and local UI (`cognee-cli -ui`, launching a Dockerized MCP server) wrap the same operations for non-code use.

## Installation

`uv pip install cognee` (also supports pip/poetry), Python 3.10–3.14. LLM configuration via `LLM_API_KEY` env var or a `.env` file from `.env.template`. Prebuilt Docker images ship to Docker Hub on every push to `main`: `cognee/cognee` (API server, port 8000) and `cognee/cognee-mcp` (MCP server, port 8001) — runnable individually or via `docker compose` with `ui`/`mcp`/`postgres`/`neo4j` profiles. One-click deploys are documented for Modal, Railway, Fly.io, Render, Daytona, and Islo sandboxes, alongside a fully managed Cognee Cloud option.

## Key features

- **Postgres-unified memory layer**: relationships (custom Postgres graph backend instead of Neo4j), embeddings (pgvector), sessions (SQL cache instead of Redis), and metadata all in one Postgres instance — reported ~10% faster in CI benchmarks than a separate graph-plus-vector setup, while still supporting dedicated backends (Neo4j, Neptune, Redis, LanceDB, Qdrant, ChromaDB, Weaviate, Milvus) when a workload needs them, and fully embedded local dev (SQLite, LanceDB, Kuzudb) with no extra services.
- **Claude Code plugin** (`cognee-integrations`, marketplace-installed): hooks the full session lifecycle — `SessionStart` bootstraps identity, `UserPromptSubmit` injects dataset-scoped context, `PostToolUse` captures tool traces, `Stop` writes the assistant's answer, `PreCompact` preserves memory across context resets, and `SessionEnd` syncs into the permanent graph. Runs against a local Cognee API by default (`LLM_API_KEY` only) or a remote/Cognee Cloud instance (`COGNEE_BASE_URL` + `COGNEE_API_KEY`).
- **Multi-language clients**: official Rust (`cognee-rs`) and TypeScript (`@cognee/cognee-ts`) clients alongside the primary Python SDK, plus an OpenClaw plugin (`cognee-openclaw`).

## Architecture and concepts

The Python package (`cognee/`) is organized into `api/`, `cli/`, `pipelines/`, `modules/`, `tasks/`, `infrastructure/`, `memory/`, `migration/` (with Alembic), and `eval_framework/` (home of the BEAM benchmark harness). `cognee-mcp/` is a separate MCP server package with its own SSE/stdio transport docs; `cognee-frontend/` is the local UI served by the `ui` Compose profile; `distributed/` and `deployment/` hold worker configs and deploy scripts for the cloud targets above. The repo carries its own `AGENTS.md` and `CLAUDE.md` at the root, dogfooding agent-instruction conventions for contributors. (../../raw/github/topoteretes-cognee.md)

## Main APIs

`cognee.remember(text, session_id=None)`, `cognee.recall(query, session_id=None)`, `cognee.forget(dataset=...)`, and `cognee.improve()` (implicit in `remember`'s add + cognify + improve pipeline) form the primary Python surface. `cognee.serve(url=..., api_key=...)` / `cognee.disconnect()` route SDK calls to a managed Cognee Cloud or self-hosted remote instance instead of local storage.

## When to use

Fits teams building agents that need durable, queryable memory across sessions rather than a single conversation's context window — e.g. a customer-support agent recalling past resolved cases, or an SQL copilot reusing expert query patterns from prior sessions (both documented as worked examples in the repo). The Postgres-unified deployment model is aimed at teams that want graph + vector + session memory without standing up a multi-service stack (Neo4j, Redis, a separate vector DB) first.

## Ecosystem

Benchmarked against BEAM (a long-context conversation-tracking benchmark, chosen as more representative of agent memory than needle-in-a-haystack tests): cognee's default settings beat the prior state of the art at 100K tokens (0.79 vs 0.735) and matched it at 10M tokens (0.67 vs 0.641), against an Obsidian/RAG baseline of ~0.33 at both settings — numbers the repo itself frames as directional rather than definitive. Backed by a research paper on optimizing knowledge-graph/LLM interfaces (Markovic et al., 2025, arXiv:2505.24478). As a knowledge-graph-plus-vector memory layer, it sits alongside [[garrytan-gbrain]] and [[HKUDS-LightRAG]] in this wiki's memory/RAG space, and alongside [[supermemory.ai]] as a persistent cross-session memory layer for agents — differentiating on its Postgres-unification claim and native Claude Code session-lifecycle plugin.
