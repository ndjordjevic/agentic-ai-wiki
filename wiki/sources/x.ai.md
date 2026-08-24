---
type: source
category: "Model infra, ML & providers"
source_url: https://x.ai/bot
tags:
  - grok
  - ai-models
  - coding-agent
  - voice-api
  - image-generation
  - openai-compatible
  - agentic-bots
  - multi-modal
related:
  - ai-sdk.dev
  - developers.openai.com
  - pydantic-pydantic-ai
  - deepseek-ai-deepseek-harness
product: x.ai
detail_level: standard
created: 2026-08-24
updated: 2026-08-24
---

xAI (x.ai) is the company behind Grok — a family of frontier AI models covering text, code, voice, images, and video — and Grok Bot, a persistent AI teammate that runs on a dedicated cloud computer to complete end-to-end tasks autonomously. The platform is relevant to this wiki as both a model API that powers agentic systems and as a first-class agentic product (Grok Bot, Grok Build) that demonstrates the state of the art in AI-native automation.

_All claims below are sourced from ../../raw/web/x.ai.md unless otherwise noted._

## What it does

xAI provides frontier models via the xAI API and builds end-user products on top of them. The platform has three distinct surfaces:

1. **xAI API** — OpenAI-compatible HTTP API at `https://api.x.ai/v1` serving Grok text, image, and video models. Existing OpenAI or Anthropic SDK users can point the base URL to xAI with no other code changes.
2. **Grok Bot** — Persistent named AI teammates that run on a shared cloud VM (browser, filesystem, terminal). Bots accept natural-language tasks, use MCP connectors or computer-use for apps without APIs, collaborate with other Bots in parallel, and learn repeatable workflows via live demonstration.
3. **Grok Build** — An agentic coding CLI/TUI (`grok` command) powered by `grok-build-0.1`; supports headless scripting, custom model overrides, skills/plugins, and the Agent Client Protocol (ACP) for embedding in other tools.

## Key features

- **OpenAI-compatible API** — any OpenAI SDK works against `https://api.x.ai/v1`; no client-side migration required.
- **Multi-modal model family** — Responses API (text/code/reasoning), Imagine API (image + video generation), Voice API (speech-to-speech, TTS, STT).
- **Grok Bot computer use** — each Bot runs on a persistent cloud VM; multiple Bots share one user-scoped computer, enabling parallel execution and direct file/session handoff.
- **Grok Build CLI** — interactive TUI or headless `grok -p "..."` mode; supports MCP servers, skills, hooks, and enterprise deployment.
- **Server-side tools** — Web Search, X Search, Code Execution, Image Generation, File Attachments, Collections Search, Remote MCP all billable per invocation.
- **Batch API and Priority Processing** — async batch requests at a discount; priority tier at 2× rates for lower latency.

## Architecture and concepts

xAI's stack is layered: raw model inference (Responses API) at the base, server-side tools that let the model call web/code/image services within a single API call, and then agent-layer products (Grok Bot, Grok Build) on top. All surfaces share one API key from `console.x.ai`.

Grok Bot's architecture is notable for agentic design: named Bots hold persistent state (memory, files, browser sessions) across turns rather than resetting. All Bots share **one** user-scoped computer, so file and session handoffs between Bots require no re-setup. A Bot can learn a multi-step workflow once ("routine") and replay it on demand or on schedule.

Grok Build implements the Agent Client Protocol (ACP), which allows it to embed inside other tools (IDEs, CI, scripts) and receive or delegate tasks programmatically.

## Main APIs

| API | Endpoint | Primary use |
|---|---|---|
| Responses | `POST /v1/responses` | Text, code, multi-turn, function calling |
| Chat Completions | `POST /v1/chat/completions` | OpenAI-compatible chat |
| Imagine (Images) | `/v1/images/...` | Text-to-image, image editing |
| Imagine (Video) | `/v1/video/...` | Text-to-video |
| Voice | Speech-to-speech, TTS, STT | Real-time voice agents, transcription |
| Batch | `POST /v1/batches` | Async high-volume at discounted rates |

**Flagship models (as of 2026-08-24):** `grok-4.6` (500k context, $2/$6 per M tokens in/out for <200k prompt), `grok-build-0.1` (coding), `grok-imagine-image-2.0`, `grok-imagine-video-1.5`, `grok-voice-think-fast-2.0`.

## When to use

- When you need an OpenAI-compatible drop-in that offers strong reasoning, coding, and multimodal capabilities under one API key.
- For agentic products that benefit from **Grok Bot**: long-running tasks requiring real-tool use (browser, CLI, files), multi-agent parallelism, and workflow persistence without a custom orchestration layer.
- For coding workflows: **Grok Build** pairs well with Claude Code–style agent harness patterns (skills, hooks, MCP) and integrates directly into CI/scripts via headless mode.
- When voice is part of the UX: the Grok Voice API is ranked #1 on the Tau Voice Leaderboard, supports 25+ languages, and prices at $0.05/min.

## Ecosystem

- **xAI API** is offered directly and through cloud provider catalogs (Microsoft Azure, Oracle, Google, Amazon).
- **Grok Build** supports custom model configs, so you can swap in any `/v1`-compatible provider while keeping the TUI and skill system.
- **MCP support** is native: Grok Bot uses MCP connectors where available and falls back to computer-use otherwise. Remote MCP tools are also available as server-side tools in the Responses API.
- **Docs:** `https://docs.x.ai` — structured by API family (Responses, Voice, Imagine, Grok Build, Grok Bot) with a quickstart, pricing, and API reference.
