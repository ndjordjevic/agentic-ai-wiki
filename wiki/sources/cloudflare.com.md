---
type: source
category: "Infra, hosting, DB & observability"
source_url: https://www.cloudflare.com/
tags:
  - edge-compute
  - serverless-platform
  - zero-cold-start
  - workers-ai
  - vector-database
  - waf
  - zero-trust
  - global-network
related:
  - vercel.com
  - render.com
  - supabase.com
product: cloudflare
detail_level: standard
created: 2026-10-08
updated: 2026-10-08
---

Cloudflare is a global cloud connectivity company (NYSE: NET) operating a network spanning 335+ cities and 125+ countries, powering roughly 20% of web traffic. For the agentic-AI domain it matters as an edge compute and AI-inference platform: **Workers** (V8-isolate serverless functions with no cold starts), **Workers AI** (100+ open-source models on serverless GPUs across 220+ cities), **Vectorize** (vector database for RAG), **AI Gateway** (observability/caching/fallback for any AI provider), and **Agents** (SDK for stateful AI agents with memory, scheduling, and tool calling) sit alongside its long-standing CDN, DNS, DDoS protection, and WAF security products.

_All claims below are sourced from ../../raw/web/cloudflare.com.md unless otherwise noted._

## What it does

Cloudflare operates three product pillars on one global network: a **developer platform** (compute, storage, AI, media), **application security** (WAF, DDoS, bot management, API Shield), and a **Zero Trust / SASE** platform (Cloudflare One, replacing legacy VPN). Workers deploy code to 335+ cities with zero cold starts using V8 isolates rather than containers; Containers handle heavier workloads needing any language or Docker image without Kubernetes or fixed regions. The platform integrates compute with storage (R2, D1, KV, Hyperdrive, Queues) and AI (Workers AI, Vectorize, AI Gateway, AI Search) so agentic applications can run inference, store vectors, and call tools from the same edge runtime that serves their traffic.

## Key features

- **Workers** — serverless functions in JS/TS/Python/Rust/WASM with zero cold starts, deployed globally by default
- **Containers / Workers for Platforms** — any-language workloads and multi-tenant compute for customers running sandboxed code on your platform
- **Durable Objects** — stateful serverless primitives with built-in WebSockets and embedded SQLite, used for real-time/multiplayer apps and agent state
- **Sandboxes** — isolated environments for running untrusted or AI-generated code
- **Workflows** — durable multi-step execution engine with automatic retries and state persistence
- **Workers AI** — 100+ models (Llama 3, Gemma, Whisper, FLUX, BGE) via an OpenAI-compatible API, run serverlessly on GPUs across 220+ cities
- **Agents SDK** — stateful AI agents with memory, scheduling, WebSockets, and tool calling
- **AI Gateway** — observability, caching, rate limiting, and model fallback across any AI provider
- **Vectorize** — globally replicated vector database pairing natively with Workers AI for RAG
- **AI Search** — managed RAG with automatic indexing for AI-powered search and chat
- **R2 / D1 / KV / Hyperdrive** — egress-free object storage, serverless SQLite, globally distributed key-value store, and connection pooling/acceleration for existing Postgres/MySQL
- **WAF / DDoS Protection / Bot Management** — OWASP Top 10 protection, sub-3-second DDoS mitigation (largest attack mitigated: 31.4 Tbps), and ML-based bot scoring in under 1 ms
- **Cloudflare One** — Zero Trust Network Access, Secure Web Gateway, Browser Isolation, DLP, and Email Security unified in one control plane

## Architecture and concepts

Everything runs on Cloudflare's anycast network rather than region-pinned data centers — deploying a Worker or Container is global by default, not a regional choice. Durable Objects provide the platform's consistency primitive: each object is a single-threaded, strongly consistent actor with its own embedded SQLite storage, used for coordination (chat rooms, agent session state, rate limiters). Workflows layer durable, retryable multi-step orchestration on top of Workers for longer-running agent or business processes. On the AI side, Workers AI (inference), Vectorize (vector storage), and AI Gateway (provider-agnostic observability/caching layer) are designed to compose: a typical agent stack runs inference and embedding calls through AI Gateway, stores vectors in Vectorize, and persists state in Durable Objects or D1 — all colocated with Workers compute at the edge.

## Main APIs

- **Workers runtime API** — `fetch`, bindings, and the CLI (`wrangler`) for deploying/managing Workers, Durable Objects, and D1/KV/R2 bindings
- **Workers AI API** — OpenAI-compatible inference endpoint for the hosted model catalog, invocable from Workers, Pages, or the Cloudflare REST API
- **Cloudflare API** — general REST API (e.g. `api.cloudflare.com/client/v4/...`) underlying products like Images, used directly or via Terraform
- **Agents SDK** — library for building stateful agents with scheduling, memory, and tool-calling hooks on top of Durable Objects

## When to use

Cloudflare's developer platform fits teams that want **edge-colocated compute, storage, and AI inference** under one network rather than assembling separate hosting, vector-DB, and model-serving vendors — particularly when low-latency global reach or zero-cold-start execution matters (interactive agents, real-time multiplayer, high-request-volume APIs). The **Agents SDK + Workers AI + Vectorize** combination is a natural fit for building and hosting AI agents with memory and RAG entirely at the edge. It is less suited to workloads needing long-running, resource-heavy background compute uninterrupted by Workers' execution model (though Containers and Workflows close part of that gap), or teams already standardized on another cloud's managed database/ML stack. Compare [[vercel.com]] and [[render.com]] for app-deployment-first platforms with their own AI/agent tooling, or [[supabase.com]] for a Postgres-first backend with edge functions and pgvector.

## Ecosystem

Cloudflare publishes open-source tooling on GitHub (`cloudflare` org), including `workerd` (the open-source Workers runtime), `wrangler` (CLI), and `workers-sdk`; the llms.txt catalog also lists a Go client library (`cloudflare-go`) and Terraform provider support. Workers AI and AI Gateway are explicitly provider-agnostic, integrating with third-party model providers (OpenAI, Anthropic) rather than locking agent workloads to Cloudflare-hosted models only. Related platforms in this wiki covering adjacent deployment/edge/backend ground: [[vercel.com]], [[render.com]], and [[supabase.com]].
