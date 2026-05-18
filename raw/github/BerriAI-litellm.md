# BerriAI/litellm

## Metadata
- Stars: 47,411
- Primary language: Python
- Default branch: litellm_internal_staging
- Latest release: v1.86.0-rc.1 (pre-release, ~2026-05-17)
- License: Other (source-available)
- Homepage: https://docs.litellm.ai/docs/
- Fetched: 2026-05-18
- Final URL: https://github.com/BerriAI/litellm

## Description

Python SDK, Proxy Server (AI Gateway) to call 100+ LLM APIs in OpenAI (or native) format, with cost tracking, guardrails, loadbalancing and logging. [Bedrock, Azure, OpenAI, VertexAI, Cohere, Anthropic, Sagemaker, HuggingFace, VLLM, NVIDIA NIM]

## README

# 🚅 LiteLLM

LiteLLM AI Gateway — Open Source AI Gateway for 100+ LLMs. Self-hosted. Enterprise-ready. Call any LLM in OpenAI format.

[Y Combinator W23]

## What is LiteLLM

LiteLLM is an open source AI Gateway that gives you a single, unified interface to call 100+ LLM providers — OpenAI, Anthropic, Gemini, Bedrock, Azure, and more — using the OpenAI format.

Use it as a **Python SDK** for direct library integration, or deploy the **AI Gateway (Proxy Server)** as a centralized service for your team or organization.

## Why LiteLLM

Managing LLM calls across providers gets complicated fast — different SDKs, auth patterns, request formats, and error types for every model. LiteLLM removes that friction:

- **Unified API** — one interface for 100+ LLMs, no provider-specific SDK juggling
- **Drop-in OpenAI compatibility** — swap providers without rewriting your code
- **Production-ready gateway** — virtual keys, spend tracking, guardrails, load balancing, and an admin dashboard out of the box
- **8ms P95 latency** at 1k RPS

### OSS Adopters

Stripe, Google ADK, Greptile, OpenHands, Netflix, OpenAI Agents SDK

## Features

### LLMs — Call 100+ LLMs (Python SDK + AI Gateway)

All Supported Endpoints: /chat/completions, /responses, /embeddings, /images, /audio, /batches, /rerank, /a2a, /messages and more.

#### Python SDK

```shell
uv add litellm
```

```python
from litellm import completion
import os

os.environ["OPENAI_API_KEY"] = "your-openai-key"
os.environ["ANTHROPIC_API_KEY"] = "your-anthropic-key"

# OpenAI
response = completion(model="openai/gpt-4o", messages=[{"role": "user", "content": "Hello!"}])

# Anthropic
response = completion(model="anthropic/claude-sonnet-4-20250514", messages=[{"role": "user", "content": "Hello!"}])
```

#### AI Gateway (Proxy Server)

```shell
uv tool install 'litellm[proxy]'
litellm --model gpt-4o
```

```python
import openai

client = openai.OpenAI(api_key="anything", base_url="http://0.0.0.0:4000")
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "Hello!"}]
)
```

### Agents — Invoke A2A Agents (Python SDK + AI Gateway)

Supported Providers: LangGraph, Vertex AI Agent Engine, Azure AI Foundry, Bedrock AgentCore, Pydantic AI

#### Python SDK - A2A Protocol

```python
from litellm.a2a_protocol import A2AClient
from a2a.types import SendMessageRequest, MessageSendParams
from uuid import uuid4

client = A2AClient(base_url="http://localhost:10001")

request = SendMessageRequest(
    id=str(uuid4()),
    params=MessageSendParams(
        message={
            "role": "user",
            "parts": [{"kind": "text", "text": "Hello!"}],
            "messageId": uuid4().hex,
        }
    )
)
response = await client.send_message(request)
```

### MCP Tools — Connect MCP servers to any LLM (Python SDK + AI Gateway)

LiteLLM acts as an MCP gateway, exposing MCP tools to any LLM or agent.

### Cost Tracking & Budgets

Track spend per virtual key, user, and team. Set hard budget limits. All via PostgreSQL-backed storage.

### Guardrails

Integrate with Aporia, Lakera, Presidio, Bedrock guardrails, and more. Run pre-call and post-call content filtering and PII masking.

### Observability

Send logs to Langfuse, MLflow, Helicone, Lunary, Arize Phoenix, and 20+ more via a single `success_callback` line.

## Docs

### AGENTS.md (excerpt)

## OVERVIEW

LiteLLM is a unified interface for 100+ LLMs that:
- Translates inputs to provider-specific completion, embedding, and image generation endpoints
- Provides consistent OpenAI-format output across all providers
- Includes retry/fallback logic across multiple deployments (Router)
- Offers a proxy server (LLM Gateway) with budgets, rate limits, and authentication
- Supports advanced features like function calling, streaming, caching, and observability

## REPOSITORY STRUCTURE

### Core Components
- `litellm/` - Main library code
  - `llms/` - Provider-specific implementations (OpenAI, Anthropic, Azure, etc.)
  - `proxy/` - Proxy server implementation (LLM Gateway)
  - `router_utils/` - Load balancing and fallback logic
  - `types/` - Type definitions and schemas
  - `integrations/` - Third-party integrations (observability, caching, etc.)

### Key Directories
- `tests/` - Comprehensive test suites
- `ui/litellm-dashboard/` - Admin dashboard UI
- `enterprise/` - Enterprise-specific features

Documentation lives in the separate BerriAI/litellm-docs repository and is served at docs.litellm.ai.

## Top-level structure

```
.github/            — CI/CD workflows, issue templates
AGENTS.md           — AI agent instructions for LiteLLM repo
ARCHITECTURE.md     — architectural overview document
CLAUDE.md           — Claude-specific agent instructions
GEMINI.md           — Gemini-specific agent instructions
CONTRIBUTING.md     — contribution guide
Dockerfile          — Docker image definition
docker-compose.yml  — Docker Compose setup
litellm/            — core Python library
  llms/             — provider-specific adapters
  proxy/            — proxy server (LLM Gateway)
  router_utils/     — load balancing, fallback logic
  integrations/     — observability, caching integrations
  types/            — Pydantic type definitions
enterprise/         — enterprise-only features
ui/litellm-dashboard/  — React admin dashboard (antd)
backend/            — backend services
tests/              — test suites
cookbook/           — example notebooks
docs/               — documentation source
deploy/             — deployment configs (Helm, k8s, etc.)
helm/               — Helm chart
gateway/            — gateway-specific code
```
