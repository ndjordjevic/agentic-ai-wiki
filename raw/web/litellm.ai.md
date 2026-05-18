# litellm.ai

## Fetch log
- Inbox URL: https://www.litellm.ai/
- Final URL: https://www.litellm.ai/
- Fetched: 2026-05-18
- Pages: 6
- Mode: standard

## Landing page — https://www.litellm.ai/

#### 🚅 LiteLLM

AI Gateway to provide model access, fallbacks and spend tracking across 100+ LLMs. All in the OpenAI format.

### Features

Free

- 100+ LLM Provider Integrations
- Langfuse, Arize Phoenix, Langsmith, OTEL Logging
- Virtual Keys, Budgets, Teams
- Load Balancing, RPM/TPM limits
- LLM Guardrails

Cloud or Self-Hosted

For giving LLM access to a large number of developers and projects.

- Everything in OSS
- Enterprise Support + Custom SLAs
- JWT Auth, SSO, Audit Logs
- All Enterprise Features

### What is LiteLLM?

LiteLLM simplifies **model access**, **spend tracking** and **fallbacks** across 100+ LLMs.

## Docs — https://docs.litellm.ai/docs/

**LiteLLM** is an open-source library that gives you a single, unified interface to call 100+ LLMs — OpenAI, Anthropic, Vertex AI, Bedrock, and more — using the OpenAI format.

- Call any provider using the same `completion()` interface — no re-learning the API for each one
- Consistent output format regardless of which provider or model you use
- Built-in retry / fallback logic across multiple deployments via the Router
- Self-hosted LLM Gateway (Proxy) with virtual keys, cost tracking, and an admin UI

### Installation

```
uv add litellm
```

To run the full Proxy Server (LLM Gateway):

```
uv tool install 'litellm[proxy]'
```

### Quick Start

```python
from litellm import completion
import os

os.environ["OPENAI_API_KEY"] = "your-api-key"

response = completion(
  model="openai/gpt-4o",
  messages=[{"role": "user", "content": "Hello, how are you?"}]
)
print(response.choices[0].message.content)
```

Every response follows the OpenAI Chat Completions format, regardless of provider.

### LiteLLM Proxy Server (LLM Gateway)

The proxy is a self-hosted OpenAI-compatible gateway. Any client that works with OpenAI works with the proxy — no code changes needed.

Step 1 — Start the proxy:

```
litellm --model huggingface/bigcode/starcoder
# Proxy running on http://0.0.0.0:4000
```

Step 2 — Call it with the OpenAI client:

```python
import openai
client = openai.OpenAI(api_key="anything", base_url="http://0.0.0.0:4000")
response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[{"role": "user", "content": "Write a short poem"}]
)
```

### Agent & MCP Gateway

LiteLLM is a unified gateway for **LLMs, agents, and MCP** — you don't need a separate agent or MCP gateway. One endpoint for 100+ models, A2A agents, and MCP tools.

### What to Explore Next

- Routing & Load Balancing — Load balance across deployments and set automatic fallbacks.
- Virtual Keys — Manage access, budgets, and rate limits per team or user.
- Spend Tracking — Track costs per key, team, and user across all providers.
- Guardrails — Add content filtering, PII masking, and safety checks.
- Observability — Integrate with Langfuse, MLflow, Helicone, and more.
- Enterprise — SSO/SAML, audit logs, and advanced security for production.

## Routing & Load Balancing — https://docs.litellm.ai/docs/routing

LiteLLM manages:

- Load-balance across multiple deployments (e.g. Azure/OpenAI)
- Prioritizing important requests to ensure they don't fail (i.e. Queueing)
- Basic reliability logic - cooldowns, fallbacks, timeouts and retries (fixed + exponential backoff) across multiple deployments/providers.

In production, litellm supports using Redis as a way to track cooldown server and usage (managing tpm/rpm limits).

### Routing Strategies

- (Default) Weighted Pick (simple-shuffle) — RECOMMENDED
- Rate-Limit Aware v2 (ASYNC)
- Latency-Based
- Least-Busy
- Custom Routing Strategy
- Lowest Cost Routing (Async)

### Routing Groups - Per-Model Strategies

Apply different routing strategies to different models in the same router. A routing group binds a list of model_names to a strategy. Models not claimed by any group fall back to the router's top-level routing_strategy.

### Traffic Mirroring / Silent Experiments

Traffic mirroring allows you to "mimic" production traffic to a secondary (silent) model for evaluation purposes. The silent model's response is gathered in the background and does not affect the latency or result of the primary request.

## Virtual Keys — https://docs.litellm.ai/docs/proxy/virtual_keys

Track Spend, and control model access via virtual keys for the proxy.

Requirements:
- Need a postgres database
- Set DATABASE_URL in env
- Set a master key (must start with sk-)

Virtual keys support:
- Model access control per key
- Budget limits and expiry
- RPM/TPM limits
- Team and user tracking
- Model aliases (upgrade/downgrade requests transparently)
- Custom key generation logic via `custom_generate_key_fn`

## Spend Tracking — https://docs.litellm.ai/docs/proxy/cost_tracking

Track spend for keys, users, and teams across 100+ LLMs.

LiteLLM automatically tracks spend for all known models via a stored model cost map.

Spend tracked per:
- key — via /key/info
- user — via /user/info
- team — via /team/info

Daily Spend Breakdown API available at `/user/daily/activity` with per-model, per-provider, and per-API-key breakdown.

## Guardrails — https://docs.litellm.ai/docs/proxy/guardrails/quick_start

Setup Prompt Injection Detection, PII Masking on LiteLLM Proxy (AI Gateway).

Supported guardrail providers: Aporia, Lakera, Presidio, AIM, generic_guardrail_api, and more.

Modes:
- `pre_call` — Run before LLM call, on input
- `post_call` — Run after LLM call, on input & output
- `during_call` — Run during LLM call, on input (parallel to LLM call)

Supports load balancing across multiple guardrail instances/regions and per-request guardrail specification via the `guardrails` field in the request body.
