---
type: source
category: "Knowledge, RAG, memory & context"
source_url: https://redis.io/iris/
tags: [context-engine, agent-memory, semantic-cache, change-data-capture, vector-search, redis, langcache]
related: [supermemory.ai, zilliztech-claude-context, HKUDS-RAG-Anything, cocoindex-io-cocoindex, coleam00-redis-iris-agent]
product: redis
detail_level: standard
created: 2026-07-09
updated: 2026-07-09
---

Redis Iris is Redis's unified, real-time context engine for AI agents, bundling four previously separate Redis capabilities — Data Integration (RDI), Context Retriever, Agent Memory, and LangCache — under one positioning aimed at fixing why "unreliable agents fail in production": data that is fragmented, stale, and slow to reach. It matters for this wiki as a concrete example of an incumbent infrastructure vendor (Redis) repackaging existing primitives (CDC pipelines, vector/schema retrieval, semantic caching) specifically as agent-context plumbing rather than as generic database features.

_All claims below are sourced from ../../raw/web/redis.io.md unless otherwise noted._

## What it does

Redis Iris positions Redis as the "context layer" an agent stack is missing: instead of querying isolated data silos, agents get a navigable path through connected business entities (customers, orders, tickets) backed by sub-millisecond retrieval and a stated <250ms P95 query latency across production workloads. The pitch is explicitly about agent reliability at scale, not general-purpose caching — reflecting a broader trend of infra vendors re-marketing existing product lines as "for agents."

## Key features

- **Redis Data Integration (RDI)** — a change-data-capture (CDC) pipeline that syncs Redis with a primary system of record (Oracle, PostgreSQL, MySQL, MongoDB, SQL Server, Spanner, Snowflake, and more) in near real time, using a no-code declarative transformation config rather than hand-written pipeline code. Also offered as a fully managed Redis Cloud service for AWS-hosted sources, MongoDB Atlas, and Snowflake.
- **Redis Context Retriever** — schema-first, navigable retrieval across business entities, aimed at replacing ad hoc multi-tool querying with a single connected-data path agents can reason over.
- **Redis Agent Memory** — combined working memory (tight, active conversation context) and long-term recall (user preferences, past decisions) that compounds across sessions, channels, and agents.
- **Redis LangCache** — a fully managed semantic caching REST API that returns cached responses for semantically similar prompts instead of re-invoking the LLM, marketed at up to 90% API cost savings and reported ~70% cache-hit / 4x latency improvement in a customer case (Mangoes.ai).

## Architecture and concepts

RDI relies on CDC to capture row-level changes at the source and ship them in micro-batches for near-real-time freshness, with an at-least-once delivery guarantee, per-key change ordering, TLS/mTLS in-flight encryption (no data ever persisted to disk in-transit), and a backpressure mechanism that lets Redis fall behind gracefully during disconnects and catch up afterward via the source's still-intact change log. A single processor core handles roughly 10,000 records/second on ~1KB records, and RDI auto-scales processing units during the initial full-snapshot load. Recovery from a fully lost cache is done by reconstructing from a dataset snapshot rather than replaying history.

LangCache's caching layer sits on a vector database for similarity matching, with adaptive controls to tune precision/recall over time and pluggable embedding models (default or bring-your-own).

## Main APIs

LangCache is exposed as a managed REST API (with CLI, Python, and JavaScript client support) rather than a self-hosted module — `docs/latest/develop/ai/langcache/` is the entry point. RDI is operated primarily via a self-documenting CLI plus Redis Insight for no-code pipeline authoring; the Redis Cloud variant is configured through the Cloud console instead of self-managed infrastructure.

## When to use

RDI fits teams whose system of record is a slower relational or document database that can't scale to agent-workload read volumes and where introducing a full custom data-pipeline stack would be overkill — it explicitly is not meant as a general-purpose data integration tool for every case. LangCache fits high-repeat-query agent/chat workloads (the page cites agents using ~4x more tokens than chat) where caching semantically similar — not just identical — prompts meaningfully cuts spend and latency. The combined Iris bundle is aimed at teams already running Redis who want one vendor covering freshness, retrieval, memory, and caching rather than assembling those from separate point solutions.

## Ecosystem

Iris sits alongside Redis's existing product line — Redis Search, Redis Flex, and Redis Cloud/Software/open-source deployment tiers — and is cross-promoted with LangChain's LangSmith Context Hub per a customer quote from LangChain's CEO (positioned as a structured way to version and evolve agent memory across environments). The `redis-for-ai` marketing URL that previously covered RAG/vector/semantic-cache positioning now redirects to this Iris page, suggesting Redis has consolidated its AI-agent messaging under the Iris name. No public GitHub companion repo is referenced for Iris itself — it is delivered as a hosted/enterprise Redis capability rather than an open-source library, unlike this wiki's other memory/RAG entries such as [[supermemory.ai]], [[zilliztech-claude-context]], and [[HKUDS-RAG-Anything]].
