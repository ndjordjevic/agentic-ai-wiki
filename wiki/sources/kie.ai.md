---
type: source
category: "Model infra, ML & providers"
source_url: https://kie.ai/
tags:
  - unified-ai-api
  - multimodal-gateway
  - video-generation
  - image-generation
  - llm-proxy
  - async-tasks
  - credit-billing
  - webhook-callbacks
related:
  - openrouter.ai
  - litellm.ai
  - huggingface.co
  - brave.com
product: kie
detail_level: standard
created: 2026-07-02
updated: 2026-07-02
---

Kie.ai is a unified multimodal API platform that gives developers access to 100+ leading video, image, audio, and LLM models through one credit-based gateway at `https://api.kie.ai`. Positioned as "the multimodel layer," it aggregates upstream providers — Veo, Kling, Seedance, Runway, GPT Image, Nano Banana, Suno, ElevenLabs, Claude, GPT, Gemini, and many more — behind consistent async task flows, webhook callbacks, and a shared `model_id` parameter schema. Pricing is typically 30–50% below official APIs (up to ~84% on selected models), with a zero-charge policy for failed generations. The platform targets production teams that need lower-cost multimodal generation without integrating each provider separately.

_All claims below are sourced from ../../raw/web/kie.ai.md unless otherwise noted._

## What it does

Kie.ai acts as a reseller and abstraction layer over frontier generative AI APIs. Developers create an API key at `kie.ai/api-key`, top up credits via a transparent wallet, and dispatch generation tasks to `https://api.kie.ai` using model-specific endpoints documented at `docs.kie.ai`. All generation is asynchronous: a successful HTTP 200 returns a `task_id`, and the final result arrives via webhook callback or by polling the task-detail API. The marketplace at `kie.ai/market` lists every supported model with per-model playgrounds for pre-integration testing; new users receive 80 free credits.

## Key features

- **Unified multimodal catalog** — video (Veo 3.1, Kling 3.0, Seedance 2, Grok Imagine, Runway), image (GPT Image 2, Nano Banana 2, Flux, Imagen4, Ideogram), audio (Suno v5.5, ElevenLabs), and LLMs (Claude Opus/Sonnet 4.x, GPT-5.x, Gemini 3.x) through one account and API key
- **Credit-based pricing** — transparent per-image, per-second, per-video, or per-million-token billing; failed tasks are not charged
- **Async task model** — every generation returns `task_id`; completion via webhook URL in request or polling `market/common/get-task-detail`
- **Playground per model** — test prompts and parameters in the browser before writing production code
- **Rate limits and IP whitelist** — per-key hourly/daily/total caps; server-side IP allowlisting to protect keys
- **Common utility APIs** — `GET /api/v1/chat/credit` for balance checks; temporary download-link generation for generated media (20-minute validity)
- **File upload API** — upload input assets before image/video generation tasks
- **24/7 monitoring** — platform claims 99.9% uptime, async task tracking, webhook delivery, and smart fallback routing across providers
- **Private support** — dedicated 1-on-1 Discord/Telegram channels for API users (UTC 21:00–17:00 coverage)

## Architecture and concepts

Kie.ai's architecture is a **gateway + task queue** pattern rather than a framework or agent runtime. Client applications send authenticated requests to `api.kie.ai`; the platform routes each task to the appropriate upstream model provider, tracks state, stores generated media temporarily (14-day retention for media files, 2-month retention for log metadata), and exposes task history at `kie.ai/logs`. Model switching is a parameter change (`model_id`) rather than a backend rewrite — the docs emphasize a unified parameter schema across categories.

The docs site (`docs.kie.ai`) organizes APIs into families: **Market** (per-model generation endpoints for image/video/audio/LLM/chat), legacy grouped APIs (4o Image, Flux Kontext, Veo3.1, Suno, Runway), **File Upload API**, and **Common API** (credits, downloads, webhook verification). Callback/webhook endpoints are documented per API family for push-based completion instead of polling.

Concurrency defaults: up to 20 new generation requests per 10 seconds per account (typically 100+ concurrent running tasks). HTTP 429 on exceed; higher limits available on request.

## Main APIs

**Base URL:** `https://api.kie.ai`

**Authentication:** Bearer token via `Authorization: Bearer <API_KEY>` header (keys from `kie.ai/api-key`; never expose in frontend code).

**Common endpoints:**
- `GET /api/v1/chat/credit` — current credit balance
- Task creation — model-specific POST endpoints under Market or grouped API paths (e.g. Veo3.1, Flux Kontext, Suno)
- Task status — poll via Market common get-task-detail; or register `callBackUrl` / webhook in the creation request

**Typical async flow:**
1. POST generation request with model parameters and optional `callBackUrl`
2. Receive HTTP 200 + `task_id` (task created, not completed)
3. Await webhook callback or poll task-detail API until status is terminal
4. Fetch result URL; use Common API download-link endpoint if a temporary signed URL is needed (valid 20 minutes)

**Docs entry points:** `docs.kie.ai` (getting started), `docs.kie.ai/market/quickstart`, per-model pages under `docs.kie.ai/market/<provider>/<model>`.

## When to use

Kie.ai fits teams building **multimodal AI products** (video SaaS, image editors, music tools, agent backends needing generation) who want a single billing relationship and API surface instead of negotiating with Google, OpenAI, Anthropic, ByteDance, and audio providers individually. It is especially attractive when official API pricing is a bottleneck — the landing page highlights 40–86% savings on image models and 60–84% on video/audio versus official rates.

Compared with [[openrouter.ai]] (LLM-focused unified gateway) or [[litellm.ai]] (self-hosted LLM proxy), Kie.ai's differentiator is **breadth across media modalities**, not just chat completions. It is less suitable when you need self-hosted infrastructure, open-source gateway code, or guaranteed upstream SLA parity — Kie.ai explicitly notes its stability may be slightly lower than official providers as a trade-off for aggressive pricing.

## Ecosystem

- **Marketplace:** `kie.ai/market` — browse models, pricing, and playgrounds
- **Pricing:** `kie.ai/pricing` — per-model billing units
- **Billing/top-up:** `kie.ai/billing` — wallet credits; bonus credits on larger top-ups (e.g. 10% on $1,250)
- **Status:** live platform status linked from the landing page
- **Support:** `kie.ai/vip-support` for Discord/Telegram onboarding; `support@kie.ai` for email
- **Documentation:** `docs.kie.ai` with English and Chinese locales; `docs.kie.ai/llms.txt` catalog for doc discovery
- No public companion GitHub repository was identified in the captured material
