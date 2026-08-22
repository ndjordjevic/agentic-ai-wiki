---
type: source
category: "Model infra, ML & providers"
source_url: https://openrouter.ai/
tags:
  - unified-llm-api
  - model-routing
  - provider-abstraction
  - openai-compatible
  - agent-sdk
  - multi-provider
  - cost-optimization
related: [router.com]
  - abacus.ai
  - agent-field-pr-af
  - karpathy-llm-council
  - litellm.ai
  - kie.ai
  - gitlawb-openclaude
  - nvidia-nemotron-3-ultra
  - mozilla-ai-any-llm
  - router-for-me-CLIProxyAPI
product: openrouter
detail_level: standard
created: 2026-05-18
updated: 2026-08-22
---

OpenRouter is a unified API gateway that gives developers and agents access to 400+ AI models from 60+ providers (Anthropic, OpenAI, Google, DeepSeek, Meta, Mistral, and many more) through a single, OpenAI-compatible endpoint. It handles provider routing, automatic fallback, uptime monitoring, and cost optimization transparently, removing the need to manage individual provider accounts or SDKs. With 8M+ global users and 250k+ apps integrated, OpenRouter has become a default LLM access layer for both direct API consumers and large-scale agentic platforms.

_All claims below are sourced from ../../raw/web/openrouter.ai.md unless otherwise noted._

## What it does

OpenRouter proxies requests to the best available provider for a given model using intelligent load balancing. Developers send one request to `https://openrouter.ai/api/v1/chat/completions` and OpenRouter resolves which provider (or providers, on fallback) fulfils it. It is fully compatible with the OpenAI Chat Completions schema, so any code built on the OpenAI SDK works as a drop-in replacement by changing only `baseURL`.

Beyond simple proxying, OpenRouter provides three integration tiers: a raw HTTP API (language-agnostic), typed Client SDKs for TypeScript/Python/Go, and an Agent SDK (`@openrouter/agent`) for building multi-turn agentic loops with tool calling and stop conditions.

## Key features

- **400+ models, 60+ providers** — single API key covers every major frontier model
- **OpenAI-compatible API** — `POST /api/v1/chat/completions` with identical schema; existing OpenAI SDK code works unchanged
- **Intelligent routing** — default price-based load balancing weighted by inverse square of cost; falls back to secondary providers on outages
- **Provider control** — `provider` object lets callers order providers, whitelist/blacklist, set min-throughput/max-latency thresholds, require Zero Data Retention (ZDR), or restrict to EU in-region endpoints (Enterprise)
- **Model fallbacks** — `models` array in request body specifies ordered fallback model list
- **Structured outputs** — `json_object` and `json_schema` response formats
- **Plugins** — web search, file/PDF parsing, response healing, context compression via `plugins` array
- **Tool calling** — normalized across providers; auto-routes only to tool-supporting providers when `tools` is set
- **Agent SDK** — `callModel` loop with Zod-typed tool definitions, stop conditions (`stepCountIs`, `maxCost`), streaming, and dynamic per-turn parameters
- **Latest aliases** — `~openai/gpt-latest`, `~anthropic/claude-sonnet-latest` resolve to current flagship without code changes

## Architecture and concepts

OpenRouter sits between application code and inference providers. Each request hits the OpenRouter edge, which:
1. Selects the target provider(s) using load-balancing logic (price, uptime, requested sorting)
2. Transforms the unified request schema to the provider's native format
3. Streams or buffers the response back to the caller using the standard schema

The **provider routing layer** supports fine-grained control: `order` (explicit priority list), `only`/`ignore` (allow/deny lists), `sort` (by price, throughput, or latency), `quantizations` (int4/int8 filtering), `data_collection` (deny providers that store prompts), and `zdr` (Zero Data Retention). This makes it suitable for enterprise workflows with strict data-residency or compliance requirements.

The **Agent SDK** (`@openrouter/agent`) adds a higher-level loop on top: `callModel` sends a prompt, receives tool calls, executes them, feeds results back, and repeats until a stop condition fires. This contrasts with the **Client SDKs** (`@openrouter/sdk`), which are thin typed wrappers over the REST API for callers that manage their own state.

## Main APIs

**Core endpoint:**
```
POST https://openrouter.ai/api/v1/chat/completions
Authorization: Bearer <OPENROUTER_API_KEY>
```

**Key request fields:**
- `model` — model slug or latest alias
- `messages` — array of `{role, content}` objects (OpenAI format)
- `models` — fallback model list (OpenRouter-specific)
- `provider` — `ProviderPreferences` object for routing control
- `tools` / `tool_choice` — tool calling (normalized cross-provider)
- `response_format` — structured JSON output
- `plugins` — extend capabilities (web, file-parser, response-healing, context-compression)
- `stream` — SSE streaming

**Agent SDK entry point:**
```typescript
import { callModel, tool, stepCountIs, maxCost } from '@openrouter/agent';
const result = await callModel({ model, messages, tools, stopWhen: [stepCountIs(10)] });
```

**Client SDKs:** `npm install @openrouter/sdk` (TypeScript), Python and Go packages available.

OpenAPI spec: `https://openrouter.ai/docs/api/openapi.json`

## When to use

OpenRouter is the right choice when:
- You need access to multiple frontier models without managing separate API keys and provider accounts
- You want automatic failover when a provider has an outage
- You're building agentic systems and want `callModel`-style loop management without writing your own orchestration
- Your workload requires cost optimization across providers (price-based routing)
- You have compliance requirements around data residency (ZDR, EU routing, data-collection policies)
- You want to use the OpenAI SDK as-is but route to non-OpenAI models

It differs from LiteLLM ([[litellm.ai]]) in being a hosted SaaS gateway rather than a self-hosted proxy; LiteLLM is preferred when you need to run the gateway within your own infrastructure.

## Ecosystem

- **250k+ apps** integrated, including Replit, Hermes Agent, and Kilo Code
- **GitHub org:** https://github.com/OpenRouterTeam (typescript-sdk, python-sdk, spawn)
- **Labs / Fusion:** experimental routing and aggregation features
- **State of AI report:** aggregate usage data published at https://openrouter.ai/state-of-ai
- **Enterprise:** EU in-region routing, custom data policies, org management
- **Community:** Discord, YouTube channel, X/Twitter @openrouter
