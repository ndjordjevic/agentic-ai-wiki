---
type: source
source_url: https://supermemory.ai/
tags: [memory-layer, context-engineering, knowledge-graph, rag, mcp-server, ai-agents, typescript-sdk, python-sdk]
related: [reseek.net, runcabinet.com, garrytan-gbrain, tolaria.md, notebooklm.google, HKUDS-RAG-Anything, getcaveman.dev]
product: supermemory
detail_level: standard
created: 2026-06-12
updated: 2026-07-01
---

Supermemory is a research and product lab building the memory and context infrastructure layer for AI agents — a five-component API (User Profiles, Memory Graph, Retrieval, Extractors, Connectors) that gives agents persistent, queryable knowledge about users and their world. It holds state-of-the-art benchmark positions on LongMemEval (85.2%), LoCoMo (#1), and ConvoMem (#1), and ships in three surfaces: an enterprise developer API, a personal consumer app (10,000+ power users), and an MCP server compatible with Claude, Cursor, ChatGPT, and 15+ MCP clients. Integrations cover Vercel AI SDK, LangChain, LangGraph, CrewAI, OpenAI SDK, Mastra, Zapier, and n8n.

_All claims below are sourced from ../../raw/web/supermemory.ai.md unless otherwise noted._

## What it does

Supermemory accepts text, files, and conversations via its REST API or TypeScript/Python SDK, indexes them into a semantic knowledge graph keyed by a `containerTag` (user, document, project, or organization ID), and returns relevant context at query time. Three context modes share the same context pool when using the same `containerTag`: a **Memory API** (real-time extraction and maintenance of evolving user facts), **User Profiles** (static always-know facts combined with dynamic episodic data), and **RAG** (advanced semantic search with metadata filtering and contextual chunking). The personal consumer app at `app.supermemory.ai` provides a one-memory-across-all-AI-tools experience, backed by the same infrastructure.

## Key features

- **User Profiles** — builds deep user profiles from behavioral signals: intent, preferences, and context accumulated over time
- **Memory Graph** — custom vector graph engine with ontology-aware edges; handles knowledge updates, merges, contradictions, and inference
- **Retrieval** — hybrid vector + keyword search with sub-300ms p50 latency and context-aware reranking
- **Extractors** — understands PDFs, web pages, images, and audio with smart chunking that preserves semantic meaning
- **Connectors** — auto-sync from Notion, Google Drive, S3, Gmail, and custom sources; Scale plan adds GitHub and a web crawler
- **SuperRAG filesystem** — Supermemory's RAG layer is also available as a filesystem API at `smfs.ai`
- **MCP server** — `npx -y mcp-remote@latest https://mcp.supermemory.ai/mcp`; OAuth-based, no API key management; universal across Claude, Cursor, VS Code, Windsurf, ChatGPT, Cline

## Architecture and concepts

The core architecture maps entities (users, documents, projects, organizations) to their accumulated knowledge using a `containerTag` as the partition key. When content is submitted via `POST /v3/add`, Supermemory extracts memories, updates the user profile, and writes the resulting graph edges. At query time, `POST /v3/search` performs hybrid vector + keyword retrieval over the container, returning ranked context ready for LLM consumption.

The billing unit is an **SM token**: only unique content is charged; repeated submissions cost nothing (100% prompt-cache discount is baked in). Billed operations are: Memory ($0.005/1K for plain text, $0.010/1K for rich content), SuperRAG ($0.001–$0.002/1K), Search & Traversal ($0.005/1K queries), and Operations ($0.10/1K for re-ranking, aggregation, query rewriting).

Both SDKs support self-hosted deployment via a `baseURL`/`base_url` configuration parameter, enabling fully local deployments without a network round-trip to `api.supermemory.ai`.

## Main APIs

| Operation | Endpoint |
|---|---|
| Add memory | `POST https://api.supermemory.ai/v3/add` |
| Search memories | `POST https://api.supermemory.ai/v3/search` |

Python SDK: `pip install supermemory`
TypeScript SDK: `npm install supermemory`

Core SDK operations: `add()` (with optional metadata and container tags), `search()` (with metadata filtering), `getProfile()` (returns static + dynamic user information), list, delete, and advanced AND-logic metadata filters.

Full REST API reference: `https://docs.supermemory.ai/api-reference`
Developer Console (API Keys): `https://console.supermemory.ai`

## When to use

Supermemory is the right choice when an AI agent or LLM application needs persistent cross-session memory without building the storage, extraction, and retrieval infrastructure from scratch — particularly for user-facing agents that must personalize responses based on accumulated user context. The MCP server path (`mcp.supermemory.ai`) is the fastest integration point for adding shared memory to any MCP-compatible coding agent or personal AI tool. The developer API suits production systems that need enterprise compliance (SOC 2, HIPAA, GDPR), dedicated infrastructure, or self-hosted deployment. For individuals who want a personal memory layer across all their AI tools without building anything, the consumer app at `app.supermemory.ai` is the entry point. Compare with [[reseek.net]] (personal knowledge management with MCP server, no self-hosted option, SaaS-only) and [[runcabinet.com]] (self-hosted markdown-on-disk knowledge base for startup teams, no external API).

## Ecosystem

Pricing tiers: Free ($0/month, $5 usage included, MCP and Hermes Plugin), Pro ($19/month, ~$20 usage, Google Drive + Notion + OneDrive connectors), Max ($100/month, ~$130 usage, Gmail + Granola connectors), Scale ($399/month, ~$600 usage, all connectors including GitHub and web crawler, up to 10 teammates, SOC 2 + HIPAA), Enterprise (custom, air-gapped self-hosting, dedicated infrastructure). A Startup & Research Program provides $1,000 in free credits for 6 months.

Integrations confirmed in the source: TypeScript, Python, REST API, Claude Code, Cursor, OpenClaw, OpenCode, Windsurf, Vercel AI SDK, LangChain, LangGraph, CrewAI, OpenAI SDK, Mastra, Zapier, n8n, Pipecat. GitHub organization: `github.com/supermemoryai` (specific repo not publicly linked from the main site). Benchmark results are tracked on the open evaluation platform at `git.new/membench`; a research paper is available at `supermemory.ai/research`.
