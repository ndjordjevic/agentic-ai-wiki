# ai-sdk.dev

## Fetch log
- Inbox URL: https://ai-sdk.dev/
- Final URL: https://ai-sdk.dev/
- Fetched: 2026-07-28
- Pages: 4
- Mode: standard

## llms.txt — https://ai-sdk.dev/llms.txt
# AI SDK

> The AI SDK is a provider-agnostic TypeScript toolkit for building AI-powered applications and agents with React, Next.js, Vue, Svelte, Node.js, and other JavaScript runtimes.

Use this page to find current AI SDK documentation. Prefer search results and targeted Markdown pages over loading the full documentation bundle.

## Web Access

If you can fetch URLs, search the docs first:

- Search endpoint: https://ai-sdk.dev/api/search-docs?q=your+query

Examples:

- https://ai-sdk.dev/api/search-docs?q=building+agents
- https://ai-sdk.dev/api/search-docs?q=ToolLoopAgent
- https://ai-sdk.dev/api/search-docs?q=prepareStep
- https://ai-sdk.dev/api/search-docs?q=generating+structured+output

The search endpoint returns JSON with documentation URLs. Fetch the returned URLs with `.md` appended to get Markdown content.

## Local Coding Agents

If you are working inside a local coding project with filesystem access, install the AI SDK skill first:

```sh
npx skills add vercel/ai
```

Then follow the skill instructions before changing code.

## Common Starting Points

- [Getting Started](https://ai-sdk.dev/docs/getting-started.md): Installation and first usage.
- [Navigating the Library](https://ai-sdk.dev/docs/getting-started/navigating-the-library.md): How the AI SDK packages fit together.
- [AI SDK Core](https://ai-sdk.dev/docs/ai-sdk-core.md): Core model calls like `generateText`, `streamText`, structured output, tools, embeddings, and providers.
- [AI SDK UI](https://ai-sdk.dev/docs/ai-sdk-ui.md): Framework-agnostic hooks for chatbots and generative UIs.
- [Agents](https://ai-sdk.dev/docs/agents.md): Building agents with `ToolLoopAgent` and related APIs.
- [AI Gateway](https://ai-sdk.dev/providers/ai-sdk-providers/ai-gateway.md): Default provider access through Vercel AI Gateway.
- [Providers](https://ai-sdk.dev/providers/ai-sdk-providers.md): Supported model providers.
- [Reference](https://ai-sdk.dev/docs/reference.md): API reference.
- [Sitemap](https://ai-sdk.dev/sitemap.md): Full documentation index.

## Full Documentation

- [llms-full.txt](https://ai-sdk.dev/llms-full.txt): A concatenated Markdown copy of the AI SDK documentation for models with large context windows.

## Landing page — https://ai-sdk.dev/

# AI SDK - Vercel's Universal AI Layer

## Overview
The AI SDK is a unified TypeScript toolkit by Vercel for building AI applications with "modern streaming, fallbacks, and multi-model support." It supports over 100 LLM models across 16+ providers including Anthropic, OpenAI, Google, Grok, Mistral, Meta, and others.

## Key Statistics
- 18.7M weekly downloads
- 25.8K GitHub stars
- 683+ contributors
- 100+ supported models

## Core Components

**AI SDK Core**: Unified API for text generation, structured objects, tool calls, and agent building.

**AI SDK UI**: Framework-agnostic hooks for chat and generative interfaces.

## Installation
```
npm install ai
```

## Key Features
- Multi-provider support with single-line switching
- Real-time streaming responses
- Built-in fallback mechanisms
- Support for text, image, speech, and video generation
- Tool calling and error handling capabilities

## Ecosystem Tools
- **Vercel AI Gateway**: Access 100+ models without managing multiple API keys
- **Vercel Sandbox**: Secure code execution at scale
- **Workflows**: Long-running agents with resumable streams
- **AI Elements**: UI component library for AI-native applications

## Framework Support
Works with React, Next.js, Vue, Svelte, and Node.js applications.

**Notable hyperlinks captured on landing page (Vercel product-family links, filtered to AI-relevant ones):** https://ai-sdk.dev, https://ai-python.dev/, https://vercel.com/ai-gateway, https://vercel.com/ai-gateway/models, https://vercel.com/sandbox, https://vercel.com/workflow, https://elements.ai-sdk.dev/, https://useworkflow.dev, https://flags-sdk.dev, https://chat-sdk.dev, https://streamdown.ai, https://eve.dev/, https://vercel.com/agent, https://github.com/vercel (org page only — no repo-root GitHub link found directly on this page; companion repo `vercel/ai` confirmed independently via `homepageUrl` match, see raw/github/vercel-ai.md).

## Docs — https://ai-sdk.dev/docs/getting-started.md

# Getting Started

The following guides are intended to provide you with an introduction to some of the core features provided by the AI SDK.

## Backend Framework Examples

You can also use AI SDK Core and AI SDK UI with the following backend frameworks:

- **Node.js HTTP Server** - Send AI responses from a Node.js HTTP server.
- **Express** - Send AI responses from an Express server.
- **Hono** - Send AI responses from a Hono server.
- **Fastify** - Send AI responses from a Fastify server.
- **Nest.js** - Send AI responses from a Nest.js server.

## Navigation

The documentation includes comprehensive sections on:

- **Foundations** - Providers and Models, Prompts, Tools, Streaming, Provider Options
- **Getting Started** - Provider selection, library navigation, framework-specific guides (Next.js, Svelte, Vue.js, Node.js, Expo, TanStack Start), and Coding Agents
- **Agents** - Overview, building agents, workflow patterns, loop control, memory, tool approvals, subagents, and Terminal UI
- **AI SDK Core** - Text generation, structured data, tool calling, MCP, embeddings, image generation, realtime features, transcription, translation, speech, video generation, file uploads, middleware, error handling, testing, telemetry, and DevTools
- **AI SDK UI** - Chatbot implementation, message persistence, tool usage, generative interfaces, completion, object generation, error handling, and transport
- **AI SDK RSC** - React Server Components for streaming, state management, multistep interfaces, and authentication
- **Advanced Topics** - Prompt engineering, stream control, caching, rate limiting, UI rendering, model routing, and deployment
- **Reference** - Complete API documentation for all SDK modules and error types
- **Migration Guides** - Upgrade paths across versions
- **Troubleshooting** - Solutions for common issues

## AI SDK Core — https://ai-sdk.dev/docs/ai-sdk-core.md

# AI SDK Core Documentation Overview

This page presents the **AI SDK Core** documentation hub, organized around key capabilities for working with Large Language Models and related AI services.

## Main Content Areas

The page features index cards covering 16 primary topics:

- **Core Functions**: Text generation, structured data generation, and tool calling
- **Advanced Features**: Realtime voice conversations, MCP Apps, runtime/tool context
- **Optimization**: Prompt engineering, settings, reasoning controls
- **Multimodal Capabilities**: Embeddings, image generation, video generation
- **Audio Services**: Transcription, translation, speech synthesis
- **Infrastructure**: File uploads, provider management, middleware, error handling, testing, telemetry

## Navigation Structure

The page includes a comprehensive sidebar navigation covering:

- **Foundations** (5 sections)
- **Getting Started** (9 framework/platform options)
- **Agents** (10 subsections)
- **AI SDK Core** (25+ reference topics)
- **AI SDK UI/RSC/Harnesses/Workflow** (multiple sections each)
- **Advanced Topics** (11 sections)
- **Complete Reference** (100+ API references)
- **Migration Guides** (version-specific)
- **Troubleshooting** (25+ common issues)

This structure enables developers to navigate from introductory concepts through advanced implementations and detailed API documentation.

## Coding Agents guide — https://ai-sdk.dev/docs/agents.md

Note: this URL (listed in llms.txt as the "Agents" entry point, described there as "Building agents with `ToolLoopAgent` and related APIs") actually resolved to the SDK's "Getting Started with Coding Agents" page rather than the agent-building conceptual overview — captured verbatim below since it is what the URL returned. Agent-building API details (`ToolLoopAgent`, tool definitions, streaming) are covered instead in `raw/github/vercel-ai.md`'s README usage examples.

# Getting Started with Coding Agents

This page explains how to get the most out of the AI SDK when working inside a coding agent (such as Claude Code, Codex, OpenCode, Cursor, or any other AI-assisted development environment).

## Install the AI SDK Skill

The fastest way to give your coding agent deep knowledge of the AI SDK is to install the official AI SDK skill. Skills are lightweight markdown files that load specialized instructions into your agent's context on demand — so your agent knows exactly how to use the SDK without you needing to explain it.

Install the AI SDK skill using `npx skills add`:

```bash
npx skills add vercel/ai
```

This installs the skill into your agent's specific skills directory (e.g., `.claude/skills`, `.codex/skills`). If you select more than one agent, the CLI creates symlinks so each agent can discover the skill. Use `-a` to specify agents directly — for example, `-a amp` installs into the universal `.agents/skills` directory. Use `-y` for non-interactive installation.

Once installed, any agent that supports the Agent Skills format (agentskills.io) will automatically discover and load the skill when working on AI SDK tasks.

Agent Skills use **progressive disclosure**: your agent loads only the skill's name and description at startup. The full instructions are only pulled into context when the task calls for it, keeping your agent fast and focused.

## Docs and Source Code in `node_modules`

Once you've installed the `ai` package, you already have the full AI SDK documentation and source code available locally inside `node_modules`. Your coding agent can read these directly — no internet access required.

After installation, your agent can reference the bundled source code and documentation at paths like:

```
node_modules/ai/src/              # Full source code organized by module
node_modules/ai/docs/             # Official documentation with examples
```

This means your agent can look up accurate API signatures, implementations, and usage examples directly from the installed package — ensuring it always uses the version of the SDK that's actually installed in your project.

## Install DevTools

AI SDK DevTools gives you full visibility into your AI SDK calls during development. It captures LLM requests, responses, tool calls, token usage, and multi-step interactions, and displays them in a local web UI. (Experimental, local development only.)

```ts
import { registerTelemetry } from 'ai';
import { DevToolsTelemetry } from '@ai-sdk/devtools';

registerTelemetry(DevToolsTelemetry());
```

```bash
npx @ai-sdk/devtools@latest
```

Open http://localhost:4983 to inspect AI SDK interactions in real time. DevTools groups multi-step agent interactions into **runs** (a complete interaction) and **steps** (each individual LLM call within it). Tool results can also be logged directly in code via an `onStepEnd` callback during a `streamText`/`stopWhen: isStepCount(5)` call.

DevTools stores all AI interactions in a local `.devtools/generations.json` file and automatically adds `.devtools` to `.gitignore`.

## Navigation (sidebar, partial)

- Choosing a Provider
- Navigating the Library
- Next.js App Router
- Next.js Pages Router
- Svelte
- Vue.js (Nuxt)
- Node.js
- Expo
- TanStack Start
- Coding Agents
