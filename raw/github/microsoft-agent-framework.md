# microsoft/agent-framework

## Metadata
- Stars: 11206
- Primary language: Python
- Default branch: main
- Latest release: python-1.8.1 (2026-06-09)
- License: MIT
- Homepage: https://aka.ms/agent-framework
- Fetched: 2026-06-10
- Final URL: https://github.com/microsoft/agent-framework

## Description
A framework for building, orchestrating and deploying AI agents and multi-agent workflows with support for Python and .NET.

## README
# Welcome to Microsoft Agent Framework!

Microsoft Agent Framework (MAF) is an open, multi-language framework for building **production-grade AI agents and multi-agent workflows** in **.NET and Python**.

Microsoft Agent Framework is built for teams taking agents from prototype to production. It provides a consistent foundation for building, orchestrating, and operating agent systems across Python and .NET, while keeping architecture choices open as requirements evolve, and supports a broad ecosystem including Microsoft Foundry, Azure OpenAI, OpenAI, and the GitHub Copilot SDK, with samples and hosting patterns for both local development and cloud deployment.

## Is this the right framework for you?

MAF is a strong fit if you:
- are building agents and workflows you expect to run in production,
- need orchestration beyond a single prompt or stateless chat loop,
- want graph-based patterns such as sequential, concurrent, handoff, and group collaboration,
- care about durability, restartability, observability, governance, or human-in-the-loop control,
- need provider flexibility so your architecture can evolve without major rewrites.

## Key Features

- **Python and C#/.NET Support**: Full framework support for both Python and C#/.NET implementations with consistent APIs
- **Multiple Agent Provider Support**: Microsoft Foundry, Azure OpenAI, OpenAI, GitHub Copilot SDK, Anthropic (Claude), Google Gemini, Mistral, Bedrock, Ollama, and more
- **Middleware**: Flexible middleware system for request/response processing, exception handling, and custom pipelines
- **Orchestration Patterns & Workflows**: Graph-based workflows supporting sequential, concurrent, handoff, and group collaboration patterns; includes checkpointing, streaming, human-in-the-loop, and time-travel
- **Foundry Hosted Agents (new)**: Deploy and host agents to Microsoft Foundry-hosted infrastructure with just 2 additional lines of code
- **Observability**: Built-in OpenTelemetry integration for distributed tracing, monitoring, and debugging
- **Declarative Agents**: Define agents using YAML for faster setup and versioning
- **Agent Skills**: Build domain-specific knowledge bases from multiple sources — files, inline code, class libraries — for agents to discover and use
- **AF Labs**: Experimental packages for benchmarking, reinforcement learning, and research
- **DevUI**: Interactive developer UI for agent development, testing, and debugging workflows
- **A2A support**: Agent-to-Agent protocol for cross-agent communication
- **Durable Task hosting**: Long-running durable workflows via Azure Durable Task

## Installation

```bash
# Python
pip install agent-framework

# .NET
dotnet add package Microsoft.Agents.AI
```

## Quickstart (Python)

```python
import asyncio
from agent_framework import Agent
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

async def main():
    agent = Agent(
      client=FoundryChatClient(credential=AzureCliCredential()),
      name="HaikuAgent",
      instructions="You are an upbeat assistant that writes beautifully.",
    )
    print(await agent.run("Write a haiku about Microsoft Agent Framework."))

asyncio.run(main())
```

## Quickstart (.NET)

```csharp
using Azure.AI.Projects;
using Azure.Identity;
using Microsoft.Agents.AI;

AIAgent agent =
    new AIProjectClient(new Uri(endpoint), new DefaultAzureCredential())
    .AsAIAgent(model: deploymentName, instructions: "...", name: "HaikuAgent");

Console.WriteLine(await agent.RunAsync("Write a haiku about Microsoft Agent Framework."));
```

## Migration guides
- From AutoGen: https://learn.microsoft.com/en-us/agent-framework/migration-guide/from-autogen
- From Semantic Kernel: https://learn.microsoft.com/en-us/agent-framework/migration-guide/from-semantic-kernel

## Top-level structure

```
python/
  packages/
    a2a/                  — Agent-to-Agent protocol
    ag-ui/                — AG-UI streaming protocol
    anthropic/            — Claude / Anthropic provider
    azure-ai-search/      — Azure AI Search integration
    azure-contentunderstanding/
    azure-cosmos/         — Azure Cosmos DB state
    azurefunctions/       — Azure Functions hosting
    bedrock/              — Amazon Bedrock provider
    chatkit/              — Chat UI components
    claude/               — Claude integration
    copilotstudio/        — GitHub Copilot Studio integration
    core/                 — Core agent runtime
    declarative/          — YAML declarative agent support
    devui/                — Developer UI
    durabletask/          — Durable Task (long-running workflows)
    foundry/              — Microsoft Foundry integration + hosted agents
    foundry_hosting/      — Foundry hosting helpers
    foundry_local/        — Local Foundry development
    gemini/               — Google Gemini provider
    github_copilot/       — GitHub Copilot SDK provider
    hyperlight/           — Hyperlight micro-VM integration
    lab/                  — Experimental: benchmarking, RL, research
    mem0/                 — mem0 memory integration
    mistral/              — Mistral AI provider
    monty/                — Internal tooling
    ollama/               — Ollama local LLM provider
    openai/               — OpenAI provider
    orchestrations/       — Workflow orchestration engine
    purview/              — Microsoft Purview governance
    redis/                — Redis state/cache
    tools/                — Tool/function calling utilities
  samples/
    01-get-started/       — Progressive tutorial (hello world → hosting)
    02-agents/            — Deep-dive by topic (tools, middleware, providers, observability)
    03-workflows/         — Sequential, concurrent, handoff, group collaboration
    04-hosting/           — A2A, Azure Functions, Durable Task, Foundry Hosted Agents
    05-end-to-end/        — Full applications, evaluation, demos

dotnet/
  src/                    — .NET source (Microsoft.Agents.AI NuGet package)
  samples/                — .NET samples mirroring Python structure

declarative-agents/       — YAML declarative agent samples
docs/
  decisions/              — Architectural Decision Records
  design/                 — Design docs
  features/               — Feature specs
  specs/
schemas/                  — JSON schemas
```
