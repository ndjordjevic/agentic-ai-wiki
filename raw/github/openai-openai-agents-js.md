# openai/openai-agents-js

## Metadata
- Stars: 3324
- Primary language: TypeScript
- Default branch: main
- Latest release: v0.12.0 (2026-06-24)
- License: MIT License
- Homepage: https://openai.github.io/openai-agents-js/
- Fetched: 2026-07-03
- Final URL: https://github.com/openai/openai-agents-js

## Description
A lightweight, powerful framework for multi-agent workflows and voice agents

## README
# OpenAI Agents SDK (JavaScript/TypeScript)

[![npm version](https://badge.fury.io/js/@openai%2Fagents.svg)](https://badge.fury.io/js/@openai%2Fagents) [![CI](https://github.com/openai/openai-agents-js/actions/workflows/test.yml/badge.svg)](https://github.com/openai/openai-agents-js/actions/workflows/test.yml)

The OpenAI Agents SDK is a lightweight yet powerful framework for building multi-agent workflows in JavaScript/TypeScript. It is provider-agnostic, supporting OpenAI APIs and more.

> [!NOTE] 
> Looking for the Python version? Check out [OpenAI Agents SDK Python](https://github.com/openai/openai-agents-python).

## Core concepts

1. **Agents**: LLMs configured with instructions, tools, guardrails, and handoffs
1. **Sandbox Agents**: Agents paired with a filesystem workspace and sandbox environment for longer-running work
1. **Agents as tools / Handoffs**: Delegating to other agents for specific tasks
1. **Tools**: Functions, MCP, hosted tools
1. **Guardrails**: Configurable safety checks for input and output validation
1. **Human in the loop**: Built-in mechanisms for involving humans across agent runs
1. **Sessions**: Automatic conversation history management across agent runs
1. **Tracing**: Built-in tracking of agent runs
1. **Realtime Agents**: Build powerful voice agents with full features

### Supported environments
- Node.js 22 or later
- Deno
- Bun
- Cloudflare Workers with `nodejs_compat` (experimental)

### Installation
```bash
npm install @openai/agents zod
```

## Top-level structure
- `packages/` — monorepo SDK packages (`@openai/agents`, sandbox, voice)
- `examples/` — runnable agent workflow examples
- `docs/` — documentation source
- `integration-tests/` — cross-package integration tests
- `helpers/` — shared build/test utilities
- `AGENTS.md`, `CLAUDE.md` — agent instruction files for repo contributors
