---
type: source
source_url: https://www.litellm.ai/
companion_urls:
  - https://github.com/BerriAI/litellm
raw_files:
  - ../../raw/web/litellm.ai.md
  - ../../raw/github/BerriAI-litellm.md
tags:
  - llm-gateway
  - ai-gateway
  - llm-routing
  - openai-compatible
  - provider-adapter
  - spend-tracking
  - load-balancing
  - guardrails
related:
  - langchain.com
  - huggingface.co
  - openrouter.ai
  - strandsagents.com
  - pydantic.dev
product: litellm
detail_level: standard
created: 2026-05-18
updated: 2026-05-21
---

LiteLLM is an open-source AI Gateway (Y Combinator W23) that gives teams a single, OpenAI-compatible interface to 100+ LLM providers — OpenAI, Anthropic, Bedrock, Gemini, Azure, Vertex AI, HuggingFace, VLLM, NVIDIA NIM, and more. It is used both as a **Python SDK** for direct in-process integration and as a self-hosted **Proxy Server (AI Gateway)** for centralized access control, spend tracking, load balancing, and guardrails across an entire organization. Adopters include Stripe, Netflix, Google ADK, OpenHands, and OpenAI Agents SDK, and the project has 47,000+ GitHub stars.

_All claims below are sourced from ../../raw/web/litellm.ai.md unless otherwise noted._

## What it does

LiteLLM removes per-provider SDK complexity by normalizing all LLM API calls into the OpenAI Chat Completions format. Developers call one `completion()` function regardless of whether the model is running on Anthropic, Bedrock, Vertex AI, or a local Ollama instance. The same codebase then works against any provider with a single config change.

Beyond the SDK, the **LiteLLM Proxy Server** (LLM Gateway) is a self-hosted HTTP service that accepts any OpenAI-format client and routes requests to the configured providers. No existing client code needs modification — swap the `base_url` to point at the proxy and everything else continues unchanged. The proxy also serves as a unified gateway for **A2A agents** (LangGraph, Vertex AI Agent Engine, Bedrock AgentCore, Pydantic AI) and **MCP tools**, consolidating LLM, agent, and MCP traffic through one endpoint.

## Key features

- **100+ provider integrations:** Bedrock, Azure, OpenAI, VertexAI, Cohere, Anthropic, Sagemaker, HuggingFace, VLLM, NVIDIA NIM, and more — all accessed via the same `completion()` call.
- **Router with routing strategies:** weighted pick (default, recommended for production), rate-limit-aware, latency-based, least-busy, lowest-cost, and custom strategies. Routing groups allow per-model strategy overrides within a single router instance.
- **Traffic mirroring:** shadow a production model with a secondary silent model for A/B testing and evaluation without affecting response latency.
- **Virtual keys:** PostgreSQL-backed key management with per-key model access control, RPM/TPM limits, budget caps, expiry, and model aliases for transparent upgrade/downgrade routing.
- **Spend tracking:** automatic cost calculation across all known models stored in a model cost map. Per-key, per-user, per-team, and daily granular breakdowns available via REST API and admin UI.
- **Guardrails:** pre-call and post-call content filtering and PII masking via Aporia, Lakera, Presidio, AIM, Bedrock guardrails, or a generic guardrail API. Supports load balancing across multiple guardrail instances and regions.
- **Observability:** single-line integration with Langfuse, MLflow, Helicone, Lunary, Arize Phoenix, OTEL, and 20+ other observability backends via `litellm.success_callback`.
- **Enterprise features:** JWT Auth, SSO/SAML, audit logs, custom SLAs.
- **8ms P95 latency** at 1k RPS (per published benchmarks). (../../raw/github/BerriAI-litellm.md)

## Architecture

LiteLLM follows a translation-layer architecture, implemented in `litellm/llms/` with provider-specific adapter classes that inherit from `BaseConfig`. Each adapter handles request format translation, response normalization, error mapping to OpenAI exception types, and streaming chunk conversion. (../../raw/github/BerriAI-litellm.md)

The **Router** (`litellm/router_utils/`) manages load balancing across multiple deployments of the same model alias, applying cooldown, retry (fixed and exponential backoff), and fallback logic. Redis is supported for distributed cooldown tracking in production clusters. (../../raw/github/BerriAI-litellm.md)

The **Proxy Server** (`litellm/proxy/`) is a FastAPI application that exposes OpenAI-compatible endpoints (`/v1/chat/completions`, `/v1/embeddings`, `/v1/images/generations`, `/a2a`, etc.), manages virtual keys in PostgreSQL, runs the guardrail pipeline, and ships a React admin dashboard (`ui/litellm-dashboard/`, built with `antd`). The proxy supports Docker, Railway, and Render one-click deployments. (../../raw/github/BerriAI-litellm.md)

## Installation

**Python SDK:**

```shell
uv add litellm
```

**Proxy Server (LLM Gateway):**

```shell
uv tool install 'litellm[proxy]'
litellm --model gpt-4o
```

**Docker:**

```shell
docker-compose up
```

Full Docker quickstart: https://docs.litellm.ai/docs/proxy/docker_quick_start (../../raw/github/BerriAI-litellm.md)

## Example usage

**Python SDK — unified provider calls:**

```python
from litellm import completion
import os

os.environ["OPENAI_API_KEY"] = "your-openai-key"
os.environ["ANTHROPIC_API_KEY"] = "your-anthropic-key"

# OpenAI
response = completion(model="openai/gpt-4o", messages=[{"role": "user", "content": "Hello!"}])

# Anthropic — same interface
response = completion(model="anthropic/claude-sonnet-4-20250514", messages=[{"role": "user", "content": "Hello!"}])
```

**Proxy — drop-in OpenAI replacement:**

```python
import openai
client = openai.OpenAI(api_key="sk-virtual-key", base_url="http://0.0.0.0:4000")
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "Hello!"}]
)
```

**Observability — single line:**

```python
import litellm
litellm.success_callback = ["langfuse", "mlflow", "helicone"]
response = litellm.completion(model="gpt-4o", messages=[{"role": "user", "content": "Hi!"}])
```

(../../raw/github/BerriAI-litellm.md)

## When to use

LiteLLM is the right choice when:
- You need to call multiple LLM providers from a single codebase without managing separate SDKs.
- You are building a team or organization gateway where access control, budget enforcement, and spend visibility matter.
- You want to switch providers or run A/B experiments without code changes (model aliases and traffic mirroring).
- You need guardrails (PII masking, content filtering) at the infrastructure level rather than per-application.
- You are integrating agents or MCP tools and want a single endpoint rather than per-provider agent gateways.

## Maintenance status

47,411 stars, active development (latest pre-release v1.86.0-rc.1 as of 2026-05-18). Python primary language. License is source-available (not standard OSS). Y Combinator W23 company (BerriAI). Hosted enterprise tier available at litellm.ai/enterprise. (../../raw/github/BerriAI-litellm.md)

## Ecosystem

LiteLLM integrates with the broader agentic AI stack at multiple levels:
- **Provider layer:** 100+ LLM providers including all major cloud providers and self-hosted models.
- **Framework layer:** works with LangChain, LlamaIndex, OpenAI Agents SDK, and any OpenAI-compatible client.
- **Observability layer:** Langfuse, MLflow, Helicone, Arize Phoenix, Lunary, OTEL, and more.
- **Guardrail layer:** Aporia, Lakera, Presidio, Bedrock guardrails, AIM, and custom webhook-based guardrails.
- **Agent/MCP layer:** A2A protocol agents (LangGraph, Vertex AI, Bedrock AgentCore, Pydantic AI) and MCP servers routed through the same gateway.

## Documentation

Full documentation at https://docs.litellm.ai/docs/ — covers SDK quickstart, routing strategies, proxy Docker setup, virtual key management, spend tracking, guardrails, observability integrations, and enterprise features. Interactive Swagger API at https://litellm-api.up.railway.app/.
