---
type: source
category: "Agent frameworks & SDKs"
source_url: https://github.com/microsoft/semantic-kernel
tags:
  - agent-orchestration-sdk
  - plugin-ecosystem
  - kernel-functions
  - prompt-templates
  - multi-agent-systems
  - deprecated-successor-maf
  - dotnet-python-java
related:
  - microsoft-agent-framework
  - microsoft-autogen
  - crewai.com
  - strandsagents.com
  - pydantic-pydantic-ai
product: semantic-kernel
detail_level: standard
created: 2026-07-28
updated: 2026-07-28
---

Semantic Kernel (SK) is Microsoft's model-agnostic SDK for building, orchestrating, and deploying AI agents and multi-agent systems in .NET, Python, and Java, built around a "kernel" that composes native code functions and natural-language prompt templates ("plugins") into pipelines. As of this ingest, the project's README marks it deprecated in favor of [[microsoft-agent-framework]] (MAF), positioned as SK's enterprise-ready 1.0 successor — SK remains relevant to this wiki chiefly as the historical/architectural precursor to MAF and for teams still on its stable APIs during migration.

_All claims below are sourced from ../../raw/github/microsoft-semantic-kernel.md unless otherwise noted._

## What it does

SK lets developers assemble AI agents (`ChatCompletionAgent` and others) from an LLM connection, instructions, and a set of plugins — reusable collections of "kernel functions" that can be native code, prompt templates written in SK's own template language, OpenAPI specs, or MCP tools. The `Kernel` object is the central orchestrator that resolves and invokes these functions, handles function-choice/tool-calling behavior, and supports structured output via response-format schemas (e.g. Pydantic models in Python). Multiple agents can be composed hierarchically, with a "triage" agent exposing other agents as plugins to route and synthesize sub-agent responses into one answer.

## Key features

- **Model flexibility**: built-in connectors for OpenAI, Azure OpenAI, Hugging Face, NVIDIA NIM, and other providers, plus local deployment via Ollama, LM Studio, or ONNX.
- **Plugin ecosystem**: native code functions, prompt-template ("semantic") functions, OpenAPI-spec-derived functions, or MCP tools — all invocable uniformly through the kernel.
- **Multi-agent systems**: specialist agents (e.g. billing, refunds) can be exposed as plugins to a triage/orchestrator agent for collaborative workflows.
- **Vector DB support**: integrations with Azure AI Search, Elasticsearch, Chroma, and others for retrieval/memory.
- **Multimodal support**: text, vision, and audio inputs.
- **Process Framework**: models structured, multi-step business processes as workflows.
- **Enterprise-oriented**: built with observability, security, and API stability as explicit goals (per the pre-deprecation README).

## Architecture

The repo is a polyglot monorepo split by language: `dotnet/` (primary/most actively maintained implementation — `src/`, `samples/`, `notebooks/`), `python/` (`semantic_kernel/` package, `samples/`, `tests/`, built with `uv`/`pyproject.toml`), and `java/` (this repo's `java/` directory is just a pointer — actual Java sources and build docs live in the separate `microsoft/semantic-kernel-java` repo). `prompt_template_samples/` holds example plugin folders (`ChatPlugin`, `CalendarPlugin`, `CodingPlugin`, `SummarizePlugin`, etc.) demonstrating prompt-template-language ("semantic function") plugins rather than native code. Most conceptual documentation (plugins, planners, feature matrix) has migrated off-repo to learn.microsoft.com; the in-repo `docs/` folder retains a glossary, embedding/similarity-math references, and architecture decision records (`docs/decisions/`), with the rest reduced to stub redirects.

## Installation

```bash
# Python
pip install semantic-kernel

# .NET
dotnet add package Microsoft.SemanticKernel
dotnet add package Microsoft.SemanticKernel.Agents.Core

# Java — see microsoft/semantic-kernel-java build docs
```

Requires Python 3.10+, .NET 10.0+, or JDK 17+; supports Windows, macOS, and Linux. An LLM API key (e.g. `AZURE_OPENAI_API_KEY` or `OPENAI_API_KEY`) must be set as an environment variable.

## Example usage

```python
import asyncio
from semantic_kernel.agents import ChatCompletionAgent
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion

async def main():
    agent = ChatCompletionAgent(
        service=AzureChatCompletion(),
        name="SK-Assistant",
        instructions="You are a helpful assistant.",
    )
    response = await agent.get_response(messages="Write a haiku about Semantic Kernel.")
    print(response.content)

asyncio.run(main())
```

Plugins are added as native Python classes decorated with `@kernel_function`, and agents can be composed of other agents (used as plugins) to build multi-agent triage systems — see the raw file for the full billing/refund triage example.

## Maintenance status

The project is functionally superseded: the README's top banner states Semantic Kernel "is now [[microsoft-agent-framework]]" and points to an official migration guide. It still receives releases (latest `dotnet-1.78.0`, 2026-07-07) and remains widely used (28,378 stars, MIT licensed), but new investment is directed at MAF. Treat SK as a maintenance-mode/legacy dependency for existing projects rather than a recommended starting point for new agent work.

## Ecosystem

SK's plugin model (native + semantic functions, OpenAPI, MCP) and multi-agent composition pattern carried forward conceptually into [[microsoft-agent-framework]], which explicitly ships an "from Semantic Kernel" migration guide. Positioned alongside other agent SDKs in this wiki such as [[microsoft-autogen]] (Microsoft's other predecessor framework, also merged into MAF), [[crewai.com]], [[strandsagents.com]], and [[pydantic-pydantic-ai]].
