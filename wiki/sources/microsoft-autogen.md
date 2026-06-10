---
type: source
source_url: https://microsoft.github.io/autogen/stable/index.html
companion_urls:
  - https://github.com/microsoft/autogen
raw_files:
  - ../../raw/web/microsoft-autogen.md
  - ../../raw/github/microsoft-autogen.md
tags:
  - multi-agent-framework
  - event-driven-agents
  - agentchat
  - actor-model
  - mcp-integration
  - python-framework
  - no-code-agent-builder
related:
  - microsoft-agent-framework
  - crewai.com
  - strandsagents.com
  - langchain.com-langgraph
product: autogen
detail_level: standard
created: 2026-06-10
updated: 2026-06-10
---

AutoGen is Microsoft Research's open-source framework for building multi-agent AI applications that can act autonomously or work alongside humans. It provides a layered architecture spanning event-driven distributed runtimes (Core), a high-level conversational agent API (AgentChat), a no-code visual builder (Studio), and a growing library of extensions for MCP, OpenAI, Azure, Docker, and gRPC. As of 2026, AutoGen is in maintenance mode — Microsoft recommends new projects start with [Microsoft Agent Framework](https://github.com/microsoft/agent-framework), the enterprise-grade successor — but AutoGen 0.4.x remains widely used and fully functional for existing deployments and research.

_All claims below are sourced from ../../raw/web/microsoft-autogen.md unless otherwise noted._

## What it does

AutoGen enables developers to compose multi-agent systems from four building blocks: **AgentChat** (high-level agent and team primitives), **Core** (event-driven actor runtime), **Extensions** (model clients, tool integrations, code executors), and **Studio** (visual no-code team builder). Agents communicate through asynchronous messages, can invoke tools, call LLM model clients, execute code in sandboxed environments, and hand off work between one another using a range of predefined design patterns including group chat, swarms, sequential workflows, handoffs, and reflection.

## Key features

- **AgentChat API**: `AssistantAgent`, `UserProxyAgent`, and team classes (`RoundRobinGroupChat`, `SelectorGroupChat`, `Swarm`, `MagenticOneGroupChat`) with preset behaviors for rapid prototyping.
- **Multi-agent design patterns**: Concurrent agents, sequential workflow, group chat, handoffs, mixture of agents, multi-agent debate, reflection, and code execution — all implemented via message protocols. (../../raw/github/microsoft-autogen.md)
- **MCP integration**: `McpWorkbench` connects any MCP-compatible server to an agent as a tool workbench; `mcp_server_tools()` for function-style tool injection.
- **Code execution**: `DockerCommandLineCodeExecutor` runs model-generated code safely in isolated containers.
- **AutoGen Studio**: Low-code Team Builder with drag-and-drop agent configuration, an interactive Playground, a community Gallery, and one-click Deployment to Python or Docker.
- **Extensions**: `OpenAIChatCompletionClient`, Azure adapters, `MultimodalWebSurfer`, GraphRAG tools, `GrpcWorkerAgentRuntime` for distributed agents.
- **Migration path**: 0.2 → 0.4 migration guide covers all breaking changes; enterprise successor is Microsoft Agent Framework.

## Architecture

AutoGen uses a layered design where each layer builds on the one below: (../../raw/github/microsoft-autogen.md)

1. **Core** (`autogen-core`): Actor-model runtime with asynchronous message passing, local and distributed execution, Python + .NET cross-language support, built-in tracing and debugging.
2. **AgentChat** (`autogen-agentchat`): Opinionated high-level API layered on Core. Provides `AssistantAgent`, team orchestrators, and serializable state. Closest to the AutoGen 0.2 experience for existing users.
3. **Extensions** (`autogen-ext`): First- and third-party plug-ins — LLM clients, code executors, runtimes. Intended to expand continuously without touching Core or AgentChat. (../../raw/github/microsoft-autogen.md)
4. **Studio** (`autogen-studio`): Full-stack TypeScript+Python app that exposes the AgentChat API through a visual UI and a REST deployment endpoint.
5. **Protos/gRPC**: Protocol buffer definitions power `GrpcWorkerAgentRuntime` for distributed multi-process agent execution. (../../raw/github/microsoft-autogen.md)

## Installation

```bash
# AgentChat + OpenAI extensions (most common starting point)
pip install -U "autogen-agentchat" "autogen-ext[openai]"

# AutoGen Studio no-code UI
pip install -U "autogenstudio"
autogenstudio ui --port 8080 --appdir ./my-app
```

Requires Python 3.10 or later. (../../raw/github/microsoft-autogen.md)

## Example usage

**Single agent with tool:**

```python
import asyncio
from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient

async def main() -> None:
    model_client = OpenAIChatCompletionClient(model="gpt-4.1")
    agent = AssistantAgent("assistant", model_client=model_client)
    print(await agent.run(task="Say 'Hello World!'"))
    await model_client.close()

asyncio.run(main())
```

**Multi-agent orchestration using AgentTool:**

```python
math_agent = AssistantAgent("math_expert", model_client=model_client,
    system_message="You are a math expert.")
math_agent_tool = AgentTool(math_agent, return_value_as_last_message=True)

orchestrator = AssistantAgent("assistant", model_client=model_client,
    tools=[math_agent_tool, chemistry_agent_tool], max_tool_iterations=10)
await Console(orchestrator.run_stream(task="What is the integral of x^2?"))
```

(../../raw/github/microsoft-autogen.md)

## When to use

AutoGen 0.4.x is a strong fit when: your team already has AutoGen 0.2/0.4 code in production and needs to continue iterating; you need Python + .NET cross-language agent runtimes; you want a proven research-backed framework with 58k+ GitHub stars and broad community examples. For new projects with enterprise support requirements, consider migrating to Microsoft Agent Framework (the official successor) or evaluating [[crewai.com]] and [[strandsagents.com]] for actively maintained alternatives.

## Maintenance status

AutoGen entered maintenance mode in 2026. Community-managed going forward; new features will not be added to the AutoGen repo. (../../raw/github/microsoft-autogen.md)

- Stars: 58,823 | Forks: 8,874
- License: CC-BY-4.0
- Latest release: python-v0.7.5 (2025-09-30)
- Successor: [Microsoft Agent Framework](https://github.com/microsoft/agent-framework)
- Community: [Discord](https://aka.ms/autogen-discord) | [GitHub Discussions](https://github.com/microsoft/autogen/discussions)

## Ecosystem

AutoGen sits within the Microsoft AI open-source ecosystem alongside Microsoft Agent Framework (its enterprise successor). The framework influenced patterns used across [[crewai.com]], [[strandsagents.com]], and [[langchain.com-langgraph]]. Extensions integrate directly with [[microsoft-playwright-mcp]] for web browsing agents, and the MCP workbench pattern makes it compatible with any MCP server. Community-contributed extensions and third-party integrations are encouraged via the `autogen-ext` package model.
