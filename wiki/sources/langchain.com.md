---
type: source
category: "Agent frameworks & SDKs"
source_url: https://www.langchain.com/
subpages:
  - langchain.com-langsmith
  - langchain.com-fleet
  - langchain.com-langchain
  - langchain.com-langgraph
  - langchain.com-deepagents
tags:
  - agent-engineering
  - langsmith
  - langgraph
  - langchain
  - fleet
  - deepagents
  - agent-harness
related:
  - huggingface.co
  - litellm.ai
  - zapier.com
  - crewai.com
  - strandsagents.com
  - factory.ai
  - pydantic.dev
  - n8n.io
  - langchain-ai-openwiki
  - ollama-ollama
  - vercel.com
  - neon.com
  - chopratejas-headroom
  - pydantic-pydantic-ai
product: langchain.com
detail_level: deep
created: 2026-04-29
updated: 2026-07-13
---

LangChain's main website and docs now describe a multi-product agent-engineering platform rather than a single framework. The umbrella spans LangSmith for observability, evaluation, and deployment; Fleet for no-code business agents; and the open-source LangChain and LangGraph frameworks for higher-level and lower-level agent construction. This source matters because it shows how those products fit together as one stack for building, operating, and scaling agents.

_All claims below are sourced from ../../raw/web/langchain.com.md unless otherwise noted._

## Products

- [[langchain.com-langsmith]] — framework-agnostic agent observability, evaluation, and deployment tooling.
- [[langchain.com-fleet]] — no-code agents with approvals, integrations, memory, and templates for everyday business workflows.
- [[langchain.com-langchain]] — higher-level open-source framework for model, tool, and middleware-driven agent construction.
- [[langchain.com-langgraph]] — lower-level orchestration framework and runtime for durable, stateful, long-running agents.
- [[langchain.com-deepagents]] — batteries-included agent harness with built-in planning, file-system context management, subagent spawning, and a terminal coding agent.

## Architecture

At the platform level, LangChain splits cleanly into commercial and open-source layers. LangSmith provides the operational plane for tracing, evaluation, deployment, and production runtime infrastructure; Fleet sits on top of that operational plane as a no-code agent surface for business users; LangChain and LangGraph provide the open-source building blocks for developers who want to assemble agents directly in code.

The docs also show that the layers are intentionally interoperable rather than isolated. LangChain quickstarts point users to LangSmith for tracing, LangGraph docs recommend LangChain components for models and tools while remaining usable without them, and LangSmith Deployment advertises support for LangGraph, other frameworks, RemoteGraph composition, MCP, and A2A.

## When to use the platform

- You want one stack that covers both developer-built agents and operator-facing production tooling.
- You need to move from prototyping to observability, evaluation, and deployment without swapping ecosystems.
- You want open-source frameworks for custom agent logic but also managed tooling for runtime operations.
- You need both code-first and no-code paths for different teams inside the same organization.

## Documentation

The docs are organized as one site with distinct product subsections and an explicit `llms.txt` index. The top-level docs split into `langsmith`, `oss`, and `api-reference`; Fleet lives under the LangSmith tree, while the open-source frameworks live under `docs.langchain.com/oss/...` with separate LangChain and LangGraph branches. That catalog structure makes the product boundaries explicit enough to treat the site as a multi-product source rather than a single-product marketing page.
