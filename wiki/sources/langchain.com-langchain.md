---
type: source
source_url: https://www.langchain.com/
parent_slug: langchain.com
tags:
  - agent-framework
  - create-agent
  - tool-calling
  - middleware
  - model-routing
related:
  - langchain.com-deepagents
product: langchain
detail_level: deep
created: 2026-04-29
updated: 2026-04-29
---

LangChain is the higher-level open-source framework in the LangChain stack. It focuses on getting working agents and LLM applications built quickly by combining model integrations, tools, prompts, memory, and middleware behind a production-ready `create_agent` abstraction while still leaving room for more advanced runtime customization.

_All claims below are sourced from ../../raw/web/langchain.com.md unless otherwise noted._

## What it does

LangChain helps developers build custom agents and LLM-powered applications with minimal setup. The overview and quickstart emphasize prebuilt agent architecture, provider integrations, and a fast path from installation to a tool-using agent that can be extended with richer prompts, memory, testing, tracing, and optional [[langchain.com-deepagents]] features.

## Key features

- Production-ready `create_agent` entry point.
- Model-provider integrations across multiple vendors.
- Tool calling and multi-step agent loops.
- Middleware for dynamic model and tool selection.
- Optional LangSmith tracing for inspection and debugging.

## Architecture and concepts

LangChain's agent model combines language models and tools into continuous loops that stop when a final answer or iteration limit is reached. The agents docs distinguish static and dynamic model selection, static and dynamic tool registration, and runtime adaptation based on state, permissions, feature flags, or other context.

The framework also positions itself above lower-level orchestration. LangGraph docs recommend LangChain components for models and tools, while LangChain quickstarts point advanced users toward LangGraph deployment and deeper agent patterns when they need more runtime control.

## Main APIs

The most prominent public API in the captured docs is `create_agent`. Around that, the docs surface model objects such as `ChatOpenAI`, middleware hooks such as `wrap_model_call` and `wrap_tool_call`, tool definitions via decorators, and request/context-driven overrides for dynamic model or tool routing.

## When to use

- You want a faster, batteries-included path to building agents than a graph-first runtime.
- You need model integrations, tools, and middleware in one framework.
- You want a production-ready agent abstraction with room for dynamic behavior.
- You are comfortable moving to LangGraph later for more explicit orchestration when needed.

## Ecosystem

LangChain is one of the open-source pillars of the LangChain platform. It points users to LangSmith for tracing, pairs naturally with LangGraph for durable orchestration and deployment, and shares the same docs site and agent-engineering narrative as the commercial LangSmith and Fleet products.
