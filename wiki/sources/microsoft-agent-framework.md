---
type: source
source_url: https://github.com/microsoft/agent-framework
tags:
  - multi-agent-framework
  - production-grade
  - graph-based-workflows
  - dotnet-python
  - microsoft-foundry
  - observability
  - declarative-agents
  - a2a-protocol
related:
  - microsoft-autogen
  - crewai.com
  - aaif-goose-goose
  - strandsagents.com
  - langchain.com-langgraph
  - omnigent-ai-omnigent
  - agents-cli
  - antigravity.google
  - adk.dev
  - google-adk-go
  - trigger.dev
  - ollama-ollama
product: agent-framework
detail_level: standard
created: 2026-06-10
updated: 2026-07-07
---

Microsoft Agent Framework (MAF) is Microsoft's production-grade successor to AutoGen — an open-source, multi-language framework for building, orchestrating, and deploying AI agents and multi-agent workflows in Python and .NET. Where [[microsoft-autogen]] pioneered experimental multi-agent research patterns, MAF is designed for teams taking agents from prototype to production, offering stable APIs, long-term support, graph-based workflow orchestration, durability, observability, and a wide provider ecosystem including Microsoft Foundry, Azure OpenAI, OpenAI, GitHub Copilot SDK, Anthropic, Gemini, Mistral, Bedrock, and Ollama.

_All claims below are sourced from ../../raw/github/microsoft-agent-framework.md unless otherwise noted._

## What it does

MAF provides a consistent foundation for building, orchestrating, and operating agent systems across Python and .NET. Agents are composed with a chosen LLM provider client, instructions, and tools; they can be wired into multi-agent workflows using graph-based patterns (sequential, concurrent, handoff, group collaboration). The framework handles durability and restartability via Durable Task, streaming, human-in-the-loop interrupts, time-travel (re-run from checkpoint), and OpenTelemetry-based observability. Agents can be deployed locally or hosted on Microsoft Foundry infrastructure with two extra lines of code.

## Key features

- **Provider flexibility**: 10+ LLM providers with consistent `Agent` API — swap providers without rewriting orchestration logic. Providers include Microsoft Foundry, Azure OpenAI, OpenAI, GitHub Copilot SDK, Anthropic (Claude), Google Gemini, Mistral, Amazon Bedrock, Ollama, Foundry Local.
- **Graph-based workflow orchestration**: Sequential, concurrent, handoff, and group collaboration patterns with checkpointing, streaming, human-in-the-loop, and time-travel.
- **Middleware pipeline**: Request/response interceptors for exception handling, logging, rate limiting, and custom processing.
- **Declarative agents**: Define agents in YAML for faster setup, versioning, and infrastructure-as-code workflows.
- **Agent Skills**: Domain-specific knowledge bases built from files, inline code, or class libraries that agents discover and use at runtime.
- **Foundry Hosted Agents**: Deploy agents to Microsoft Foundry with 2 additional lines of code.
- **A2A protocol**: Agent-to-Agent cross-agent communication for distributed multi-agent systems.
- **Durable Task hosting**: Long-running durable workflows via Azure Durable Task — survives crashes, restarts from checkpoint.
- **DevUI**: Interactive developer UI for building, testing, and debugging workflows.
- **Observability**: Built-in OpenTelemetry for distributed tracing, monitoring, and debugging.
- **AF Labs**: Experimental packages for benchmarking, reinforcement learning, and research.

## Architecture

MAF is a Python monorepo (`python/packages/`) with 30+ focused packages, each a provider or integration point:

- **`core`** — agent runtime, `Agent` class, tool calling, message passing
- **`orchestrations`** — graph-based multi-agent workflow engine
- **`foundry`** — Microsoft Foundry integration (`FoundryChatClient`)
- **`durabletask`** — Azure Durable Task for long-running persistent workflows
- **`declarative`** — YAML agent definition support
- **`devui`** — developer UI
- **`a2a`** — Agent-to-Agent protocol
- **`ag-ui`** — AG-UI streaming protocol
- **Provider packages**: `openai`, `anthropic`, `claude`, `gemini`, `mistral`, `bedrock`, `ollama`, `copilotstudio`, `github_copilot`
- **Storage/state packages**: `azure-cosmos`, `redis`, `mem0`, `azure-ai-search`
- **Hosting packages**: `azurefunctions`, `foundry_hosting`, `foundry_local`, `hyperlight`
- **`lab`** — experimental: benchmarking, reinforcement learning, research

The .NET implementation (`dotnet/src/`, `Microsoft.Agents.AI` NuGet) mirrors the Python API surface for teams building cross-language agent systems.

## Installation

```bash
# Python — installs all sub-packages
pip install agent-framework

# .NET
dotnet add package Microsoft.Agents.AI
# For Foundry integration:
dotnet add package Microsoft.Agents.AI.Foundry
```

## Example usage

**Python — basic agent with Microsoft Foundry:**

```python
from agent_framework import Agent
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

agent = Agent(
    client=FoundryChatClient(credential=AzureCliCredential()),
    name="MyAgent",
    instructions="You are a helpful assistant.",
)
print(await agent.run("Summarize the latest news on AI agents."))
```

**.NET — basic agent:**

```csharp
AIAgent agent =
    new AIProjectClient(new Uri(endpoint), new DefaultAzureCredential())
    .AsAIAgent(model: deploymentName, instructions: "...", name: "MyAgent");

Console.WriteLine(await agent.RunAsync("Summarize the latest news on AI agents."));
```

## When to use

MAF is the right choice when: you are building agents for production (stable APIs, LTS commitment, enterprise support); you need Python + .NET parity; you require durability and restartability for long-running workflows; you want to deploy to Microsoft Foundry with minimal code changes; or you are migrating from AutoGen or Semantic Kernel (both have official migration guides). For research or experimental multi-agent patterns where maintenance mode is acceptable, the predecessor [[microsoft-autogen]] remains viable. For lighter, open-source alternatives, see [[crewai.com]] and [[strandsagents.com]].

## Maintenance status

Actively developed with production-ready 1.x releases. Latest: python-1.8.1 (2026-06-09). MIT licensed.

- Stars: 11,206 | Forks: 1,877
- Official docs: https://learn.microsoft.com/en-us/agent-framework/
- Community: [Discord](https://discord.gg/b5zjErwbQM) | [GitHub Discussions](https://github.com/microsoft/agent-framework/discussions)
- Migration from AutoGen: https://learn.microsoft.com/en-us/agent-framework/migration-guide/from-autogen
- Migration from Semantic Kernel: https://learn.microsoft.com/en-us/agent-framework/migration-guide/from-semantic-kernel

## Ecosystem

MAF is the enterprise successor to [[microsoft-autogen]] (AutoGen → MAF migration guide included). It integrates natively with Microsoft Foundry, Azure Functions, Azure Durable Task, Azure Cosmos DB, Azure AI Search, and Microsoft Purview. The provider model makes it compatible with the same LLM backends used by [[crewai.com]], [[strandsagents.com]], and [[langchain.com-langgraph]]. The A2A protocol enables cross-framework agent communication, and the AG-UI streaming protocol connects to web-based agent UIs.
