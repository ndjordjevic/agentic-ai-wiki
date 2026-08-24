---
type: source
category: "Agent frameworks & SDKs"
source_url: https://ai-sdk.dev/
companion_urls:
  - https://github.com/vercel/ai
raw_files:
  - ../../raw/web/ai-sdk.dev.md
  - ../../raw/github/vercel-ai.md
tags:
  - typescript-ai-toolkit
  - tool-loop-agent
  - unified-provider-api
  - ai-sdk-ui
  - vercel-ai-gateway
  - agent-skill
  - devtools-tracing
  - streaming
related:
  - vercel.com
  - mastra.ai
  - x.ai
  - strandsagents.com
  - crewai.com
  - agno.com
  - developers.openai.com
product: ai-sdk
detail_level: standard
created: 2026-07-28
updated: 2026-08-24
---

The AI SDK (`ai-sdk.dev`, GitHub `vercel/ai`, 25,800+ stars, 18.7M weekly npm downloads) is Vercel's provider-agnostic TypeScript toolkit for building AI-powered applications and agents. It is the lower-level, npm-package sibling to the broader [[vercel.com]] platform overview already in this wiki — where that page covers Vercel's whole agentic-infrastructure stack (Sandbox, AI Gateway, Workflows, MCP), this page focuses specifically on the `ai` package's programming model: unified model calls, structured output, tool calling, and the `ToolLoopAgent` agent class.

_All claims below are sourced from ../../raw/web/ai-sdk.dev.md unless otherwise noted._

## What it does

The AI SDK gives developers a single API surface — `generateText`, `streamText`, structured `Output.object()` generation, and tool calling — that works across 100+ models from 16+ providers (OpenAI, Anthropic, Google, Grok, Mistral, Meta, and more), selectable by passing a model string (e.g. `'anthropic/claude-opus-4.6'`) rather than switching SDKs. By default it routes through the Vercel AI Gateway for zero-config multi-provider access; provider packages (`@ai-sdk/openai`, `@ai-sdk/anthropic`, `@ai-sdk/google`) can be installed for direct connections instead. `AI SDK UI` supplies framework-agnostic hooks (`useChat`, etc.) for building chat and generative interfaces on top of these calls, usable in Next.js, React, Svelte, and Vue.

## Key features

- **Unified model API**: single-line provider switching via model strings, with real-time streaming and built-in fallback mechanisms.
- **`ToolLoopAgent`**: the SDK's agent primitive — instantiate with a `model`, `system` prompt, and a `tools` object; the agent loop executes tool calls (e.g. shell commands via a Vercel Sandbox) and returns/streams results. (../../raw/github/vercel-ai.md)
- **Multimodal generation**: text, structured objects (via Zod schemas), image, speech, and video generation from the same core API.
- **AI SDK UI**: framework-agnostic React/Svelte/Vue hooks, plus helpers like `createAgentUIStreamResponse` and `InferAgentUIMessage` for wiring a `ToolLoopAgent` directly into a chat UI, including per-tool custom UI components keyed on `part.type` (e.g. `tool-generateImage`). (../../raw/github/vercel-ai.md)
- **MCP support**: MCP Apps and tool/runtime context integration are documented as first-class AI SDK Core capabilities.
- **Agent Skills integration**: `npx skills add vercel/ai` installs an official AI SDK skill (progressive-disclosure format per agentskills.io) so coding agents like Claude Code, Cursor, Codex, or OpenCode get on-demand AI SDK expertise; installing the `ai` npm package also makes source and docs available locally under `node_modules/ai/` for offline agent reference.
- **DevTools**: an experimental local web UI (`@ai-sdk/devtools`, `npx @ai-sdk/devtools@latest`, served at `localhost:4983`) that captures every AI SDK call — inputs, outputs, tool calls, token usage, timing, raw provider payloads — grouped into "runs" and "steps" for tracing multi-step agent behavior during development.
- **Ecosystem tools**: Vercel AI Gateway (100+ models, one API key), Vercel Sandbox (secure code execution), Workflows (long-running agents with resumable streams), and AI Elements (a UI component library for AI-native apps).

## Architecture and concepts

The SDK is organized into layered modules: **AI SDK Core** (model calls, structured output, tool calling, embeddings, image/video/speech generation, middleware, telemetry, testing — the provider-agnostic runtime layer), **AI SDK UI** (chat/generative-UI hooks), and **AI SDK RSC** (React Server Components streaming and multistep interfaces). The repo (`vercel/ai`) is a monorepo of scoped `@ai-sdk/*` packages (`@ai-sdk/openai`, `@ai-sdk/anthropic`, `@ai-sdk/google`, `@ai-sdk/react`, `@ai-sdk/devtools`, `@ai-sdk/workflow-harness`) published alongside the core `ai` package. (../../raw/github/vercel-ai.md)

## Main APIs

`generateText({ model, prompt })` / `streamText(...)` for text generation; `Output.object({ schema })` passed to `generateText` for Zod-validated structured output; `tool({ description, inputSchema, execute })` for defining callable tools; `new ToolLoopAgent({ model, system, tools })` for the core agent class; `createAgentUIStreamResponse({ agent, messages })` and `useChat()` (`@ai-sdk/react`) for wiring an agent into a streaming chat UI; `InferAgentUIMessage<typeof agent>` for typed message inference. (../../raw/github/vercel-ai.md)

## When to use

The AI SDK is the natural default for TypeScript/JavaScript teams — especially those already on Next.js/Vercel — who want one API across many model providers plus first-class UI hooks, without adopting a separate Python-first agent framework. It occupies similar territory to [[mastra.ai]] (also TypeScript-native, also ships a dedicated agent primitive and UI layer) but is narrower in scope: the AI SDK's core focus is the model-call/tool-call/UI layer, while Workflows, Sandbox, and multi-agent orchestration live in adjacent Vercel products ([[vercel.com]]) rather than the `ai` package itself. Compare against [[crewai.com]], [[agno.com]], and [[strandsagents.com]] for Python-first alternatives, and [[developers.openai.com]] for OpenAI's own vendor SDK.

## Maintenance status

Actively developed: latest package release `@ai-sdk/workflow-harness@1.0.46` (2026-07-28), with commits pushed the same day. 25,844 stars, 4,866 forks, 683+ contributors, 18.7M weekly npm downloads for the `ai` package. License is a custom "Other" license (see repo `LICENSE`), not a standard OSI license. Built and maintained by Vercel/Next.js team members with open-source community contributions.

## Ecosystem

The AI SDK is the SDK layer of Vercel's broader agentic stack documented on [[vercel.com]]: AI Gateway (default model routing), Sandbox (tool-execution runtime referenced directly in the `ToolLoopAgent` shell example), Workflows (`useworkflow.dev`), and AI Elements (`elements.ai-sdk.dev`, a UI component library). Related sibling Vercel developer tools surfaced on the landing page include `flags-sdk.dev` (feature flags) and `chat-sdk.dev` (a reference chat app built on the AI SDK). The Agent Skills format it ships (`npx skills add vercel/ai`) is the same specification (agentskills.io) used elsewhere in this wiki's coding-agent-harness sources.
