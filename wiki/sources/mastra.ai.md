---
type: source
category: "Agent frameworks & SDKs"
source_url: https://mastra.ai/
companion_urls:
  - https://github.com/mastra-ai/mastra
raw_files:
  - ../../raw/web/mastra.ai.md
  - ../../raw/github/mastra-ai-mastra.md
tags:
  - typescript-agent-framework
  - graph-based-workflows
  - observational-memory
  - mcp-servers
  - human-in-the-loop
  - model-router
  - agent-studio
  - dual-license
related:
  - crewai.com
  - strandsagents.com
  - agno.com
  - langchain.com-langgraph
  - microsoft-agent-framework
  - pydantic-pydantic-ai
  - ai-sdk.dev
product: mastra
detail_level: standard
created: 2026-07-28
updated: 2026-07-28
---

Mastra is a Y Combinator-backed, open-source TypeScript framework (26,600+ GitHub stars, dual Apache-2.0/Enterprise license) for building AI agents and applications, distinguishing itself in this wiki's largely Python-centric agent-framework landscape as a purpose-built TypeScript-native stack with agents, graph-based workflows, durable memory, and a local visual "Studio" UI built in from the start.

_All claims below are sourced from ../../raw/web/mastra.ai.md unless otherwise noted._

## What it does

Mastra provides typed `Agent` and workflow primitives for building AI-powered applications on a modern TypeScript stack, deployable standalone or embedded into React, Next.js, and Node apps. Agents are instantiated from `@mastra/core/agent` with `id`, `name`, `instructions`, and a `model` string in `provider/model` format (e.g. `openai/gpt-5.5`); tools must be created via `createTool()` (plain object tool definitions silently fail to execute) and are passed to the agent constructor. Agents connect to 90+ (per landing page) / 40+ (per README) model providers through a unified model-routing interface, and can be invoked via `.generate()` (full response with `text`, `toolCalls`, `toolResults`, `steps`, token usage) or `.stream()` (real-time token streaming via `textStream`).

## Key features

- **Agents**: reason about goals, decide which tools to apply, and iterate until a final answer — used for open-ended tasks where the steps aren't known in advance; explicit-control-flow processes should use Workflows instead.
- **Workflows**: graph-based orchestration engine with an intuitive control-flow syntax (`.then()`, `.branch()`, `.parallel()`) for composing typed steps, retries, and branches into production pipelines. (../../raw/github/mastra-ai-mastra.md)
- **Memory**: durable context via conversation history, Observational Memory, semantic recall, working memory, memory processors, and multi-user threads.
- **Human-in-the-loop**: suspend an agent or workflow and await user input/approval before resuming, backed by persistent storage so pauses can last indefinitely.
- **Harness**: coordinates multi-mode agents with shared state and storage.
- **MCP servers**: author Model Context Protocol servers that expose agents, tools, and other structured resources to any MCP-compatible client.
- **Studio**: a local developer UI (`http://localhost:4111` by default) for building, testing, and managing agents, workflows, and tools, including an "Agent Builder" sub-system (configuration, access control, model policy, workspace, browser, channels, tool providers, skill registries, deploying) and an "Editor" (tools, prompts).
- **Observability and evals**: built-in evaluation scoring, performance metrics tracking, versioned datasets, and searchable execution traces for production monitoring.
- **Workspaces and capabilities**: filesystem, sandbox, LSP inspection, skills, and search/indexing primitives (per the `llms.txt` docs catalog) supporting file-based agent workflows.

## Architecture

Mastra's docs catalog (`llms.txt`) organizes the framework into Essentials (manual install, build-with-AI, storage, file-based agents), Core (Agents, Workflows, Memory, Studio), Capabilities (Workspaces — filesystem/sandbox/LSP/skills/search), and further sections covering connections (A2A, ACP, SDK Agents, MCP) and agent-builder tooling. The framework is a monorepo built around `packages/core` (published as `@mastra/core`), with enterprise-only functionality isolated into `ee/`-named subdirectories throughout the tree under a separate Mastra Enterprise License — the rest of the codebase is Apache-2.0. (../../raw/github/mastra-ai-mastra.md)

## Installation

```bash
npm create mastra@latest
```

Setup requires a `package.json` with `{ "type": "module" }`, dependencies `@mastra/core@latest`, `zod@latest`, `typescript@latest`, `@types/node@latest`, and a `tsconfig.json` targeting ES2022. Model API keys are set as environment variables (`OPENAI_API_KEY`, `ANTHROPIC_API_KEY`, etc.).

## Example usage

The docs' pre-built onboarding prompt for coding agents illustrates the intended flow: create a project via `npm create mastra@latest <project-name> -- --llm <provider>` (choosing among `openai`, `anthropic`, `google`, `xai`), start the dev server with `npx bgproc start -n <project-name> -w -- npm run dev`, and open Mastra Studio at `http://localhost:4111` to build, test, and manage agents, workflows, and tools interactively. (../../raw/github/mastra-ai-mastra.md)

## When to use

Mastra is the natural choice for teams building agent applications inside a TypeScript/Node stack — particularly ones already using React, Next.js, or Vercel's AI SDK UI / CopilotKit for the frontend — where a Python-first framework like [[crewai.com]], [[pydantic-pydantic-ai]], or [[agno.com]] would require a separate service boundary. Its graph-based Workflows plus explicit human-in-the-loop suspend/resume make it comparable to [[langchain.com-langgraph]]'s state-graph model, while its built-in Studio and Agent Builder aim to reduce the need for external tooling to inspect and iterate on agents during development.

## Maintenance status

Actively developed: latest release `@mastra/core@1.52.0` (2026-07-27), with commits pushed as recently as 2026-07-28. 26,626 stars, 2,523 forks, Y Combinator W25 batch. Dual-licensed: core framework under Apache-2.0, `ee/`-named directories under a separate Mastra Enterprise License requiring a paid license for production use (free for development/testing). (../../raw/github/mastra-ai-mastra.md)

## Ecosystem

Mastra integrates with Vercel's AI SDK UI and CopilotKit for building web-based agent UIs, and supports MCP servers both as an authoring surface and (implicitly, via its Connections docs section covering A2A, ACP, SDK Agents, MCP) as a consumer of external agent/tool protocols. Customer case studies referenced on the landing page include Replit, Sanity, SoftBank, WorkOS, and Factorial. Model access is provided through a unified router (branded "Mastra models") fronting 40+ (README) to 90+ (landing page) providers including OpenAI, Anthropic, and Google Gemini — comparable in role to the multi-provider routing found in [[strandsagents.com]] and [[microsoft-agent-framework]].
