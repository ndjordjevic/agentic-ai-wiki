---
type: source
category: "Model infra, ML & providers"
source_url: https://router.com/
tags: [llm-gateway, model-routing, cost-optimization, openai-compatible, multi-provider, fallbacks, byok, inference-spend]
related: [openrouter.ai, litellm.ai, ollama-ollama, vellum.ai]
product: router
detail_level: standard
created: 2026-08-22
updated: 2026-08-22
---

Ramp Router is an LLM gateway from Ramp (the corporate-spend platform) that cuts inference costs by routing each request to the cheapest approved model that still clears your quality bar. It exposes a single OpenAI- and Anthropic-compatible endpoint so existing SDKs and frameworks need only a one-line base-URL swap to switch. Router is built on the same routing technology Ramp uses internally across its own production AI workloads, where it reduced Ramp's AI inference spend by 40%. Free to use through 2026 (you pay list price for tokens only); no Ramp account required.

_All claims below are sourced from ../../raw/web/router.com.md unless otherwise noted._

## What it does

Ramp Router sits between your application and multiple LLM providers. Each request is authenticated, logged (model, provider, cost, latency), and optionally rerouted to a lower-cost model when the quality impact would be negligible. Automatic fallbacks redirect requests to an available model if a provider is down or rate-limiting. The routing decision can be governed by **Router Strategies** — user-defined or Ramp's benchmarked defaults — that set cost and performance priorities per request type. Model comparison is also available: the same prompt can be sent to two models simultaneously for side-by-side latency and quality evaluation.

## Key features

- Single OpenAI- and Anthropic-compatible endpoint (one-line code change to adopt)
- Automatic cost-based routing: routes to cheapest model that clears your quality bar
- Provider fallbacks on 4xx/5xx, rate-limits, network errors, and timeouts
- Router Strategies: configurable cost/performance priority rules per request type
- Bring-your-own API key (BYOK) for OpenAI, Fireworks, and xAI — billed directly to your keys
- Model catalog via `GET /v1/models`; supports OpenAI, Anthropic, Kimi, and open-source models
- Usage logging: per-request cost, model, provider, credential source, and fallback metadata
- Side-by-side model comparison in the dashboard
- U.S.-hosted models with zero data retention (ZDR) option
- Free through 2026; first $26 in credits included

## Architecture and concepts

Router is positioned as an LLM proxy layer. The core routing loop is: (1) receive OpenAI-compatible request; (2) authenticate and log metadata; (3) select the optimal model-provider candidate based on the active Strategy; (4) call the provider and stream back the response; (5) on error, apply key fallback (retry same model with shared key if BYOK fails) then model fallback (advance to next candidate). Key fallback and model fallback are distinct: key fallback retries the same model with different credentials; model fallback advances to a different model entirely. For streaming requests, key fallback can only occur before billable output begins. BYOK keys are stored write-only and encrypted; one key per provider per user.

## Main APIs

- **Endpoint**: OpenAI-compatible base URL (replace `https://api.openai.com` with Router's endpoint)
- **`GET /v1/models`**: authoritative list of callable model IDs available to the caller's API key
- **BYOK management**: via `https://app.router.com/keys` — add/disable/delete provider keys
- Supports `model` parameter using IDs from `/v1/models`; display labels in the model catalog are not valid request IDs

## When to use

Router fits teams already using OpenAI or Anthropic SDKs who want to reduce inference spend without refactoring their application. Its strength is the zero-rewrite migration path and automatic fallbacks for reliability. It is less suited for teams who need on-premise or private deployment, who need provider coverage beyond OpenAI/Anthropic/Fireworks/xAI/Kimi, or who want fine-grained control over per-token routing logic that goes beyond the Strategy abstraction. Enterprise features are listed as coming soon.

## Ecosystem

Router is a commercial product from Ramp, Inc. There is no public GitHub repository. It competes with and overlaps [[openrouter.ai]] (multi-provider LLM gateway with similar one-endpoint model), [[litellm.ai]] (open-source proxy layer with extensive provider support), and [[vellum.ai]] (LLM dev platform with routing and evaluation). Unlike those, Router's differentiation is its grounding in Ramp's own production inference spend data and the SWE-Bench cost-to-quality benchmark used for routing decisions. Ramp also publishes a public [Ramp SWE-Bench](https://labs.ramp.com/swebench) benchmark of agents on software-engineering tasks, which feeds the routing quality signals.
