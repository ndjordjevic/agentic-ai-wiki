# microsoft/autogen

## Metadata
- Stars: 58823
- Primary language: Python
- Default branch: main
- Latest release: python-v0.7.5 (2025-09-30)
- License: Creative Commons Attribution 4.0 International (cc-by-4.0)
- Homepage: https://microsoft.github.io/autogen/
- Fetched: 2026-06-10
- Final URL: https://github.com/microsoft/autogen

## Description
A programming framework for agentic AI

## README
<a name="readme-top"></a>

# AutoGen [![Maintenance Mode](https://img.shields.io/badge/status-maintenance%20mode-orange)](https://github.com/microsoft/agent-framework)

**AutoGen** is a framework for creating multi-agent AI applications that can act autonomously or work alongside humans.

> [!CAUTION]
> **⚠️ Maintenance Mode**
>
> AutoGen is now in maintenance mode. It will not receive new features or enhancements and is community managed going forward.
>
> New users should start with [Microsoft Agent Framework](https://github.com/microsoft/agent-framework). Existing users are encouraged to migrate using the [AutoGen → Microsoft Agent Framework migration guide](https://learn.microsoft.com/en-us/agent-framework/migration-guide/from-autogen/).
>
> Microsoft Agent Framework (MAF) is the enterprise‑ready successor to AutoGen. MAF is now available as a production-ready release: stable APIs, and a commitment to long-term support. Whether you're building a single assistant or orchestrating a fleet of specialized agents, Microsoft Agent Framework 1.0 gives you enterprise-grade multi-agent orchestration, multi-provider model support, and cross-runtime interoperability via A2A and MCP.

## Installation

AutoGen requires **Python 3.10 or later**.

```bash
# Install AgentChat and OpenAI client from Extensions
pip install -U "autogen-agentchat" "autogen-ext[openai]"
```

The current stable version can be found in the [releases](https://github.com/microsoft/autogen/releases). If you are upgrading from AutoGen v0.2, please refer to the [Migration Guide](https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/migration-guide.html) for detailed instructions on how to update your code and configurations.

```bash
# Install AutoGen Studio for no-code GUI
pip install -U "autogenstudio"
```

## Quickstart

The following samples call OpenAI API, so you first need to create an account and export your key as `export OPENAI_API_KEY="sk-..."`.

### Hello World

Create an assistant agent using OpenAI's GPT-4o model. See [other supported models](https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/tutorial/models.html).

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

### MCP Server

Create a web browsing assistant agent that uses the Playwright MCP server.

```python
# First run `npm install -g @playwright/mcp@latest` to install the MCP server.
import asyncio
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_ext.tools.mcp import McpWorkbench, StdioServerParams


async def main() -> None:
    model_client = OpenAIChatCompletionClient(model="gpt-4.1")
    server_params = StdioServerParams(
        command="npx",
        args=[
            "@playwright/mcp@latest",
            "--headless",
        ],
    )
    async with McpWorkbench(server_params) as mcp:
        agent = AssistantAgent(
            "web_browsing_assistant",
            model_client=model_client,
            workbench=mcp,
            model_client_stream=True,
            max_tool_iterations=10,
        )
        await Console(agent.run_stream(task="Find out how many contributors for the microsoft/autogen repository"))


asyncio.run(main())
```

### Multi-Agent Orchestration

```python
import asyncio
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.tools import AgentTool
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient


async def main() -> None:
    model_client = OpenAIChatCompletionClient(model="gpt-4.1")

    math_agent = AssistantAgent(
        "math_expert",
        model_client=model_client,
        system_message="You are a math expert.",
        description="A math expert assistant.",
        model_client_stream=True,
    )
    math_agent_tool = AgentTool(math_agent, return_value_as_last_message=True)

    chemistry_agent = AssistantAgent(
        "chemistry_expert",
        model_client=model_client,
        system_message="You are a chemistry expert.",
        description="A chemistry expert assistant.",
        model_client_stream=True,
    )
    chemistry_agent_tool = AgentTool(chemistry_agent, return_value_as_last_message=True)

    agent = AssistantAgent(
        "assistant",
        system_message="You are a general assistant. Use expert tools when needed.",
        model_client=model_client,
        model_client_stream=True,
        tools=[math_agent_tool, chemistry_agent_tool],
        max_tool_iterations=10,
    )
    await Console(agent.run_stream(task="What is the integral of x^2?"))
    await Console(agent.run_stream(task="What is the molecular weight of water?"))


asyncio.run(main())
```

## Architecture

AutoGen uses a layered and extensible design with clearly divided responsibilities:

- **Core API** (`autogen-core`): implements message passing, event-driven agents, and local and distributed runtime for flexibility and power. Supports cross-language support for .NET and Python.
- **AgentChat API** (`autogen-agentchat`): implements a simpler but opinionated API for rapid prototyping. Built on top of the Core API; supports common multi-agent patterns such as two-agent chat or group chats.
- **Extensions API** (`autogen-ext`): enables first- and third-party extensions expanding framework capabilities. Supports specific LLM clients (OpenAI, AzureOpenAI) and capabilities such as code execution.

Developer tools:
- **AutoGen Studio** (`autogen-studio`): no-code GUI for building multi-agent applications.
- **AutoGen Bench** (`agbench`): benchmarking suite for evaluating agent performance.

## Top-level structure
```
.azure/               — Azure deployment configs
.devcontainer/        — Dev container setup
.github/              — CI/CD workflows, issue templates
docs/                 — Documentation source
dotnet/               — .NET implementation of AutoGen Core
protos/               — Protocol buffer definitions for distributed runtime
python/               — Python implementation (main codebase)
  packages/
    agbench/                  — benchmarking suite
    autogen-agentchat/        — high-level multi-agent API
    autogen-core/             — event-driven runtime core
    autogen-ext/              — extensions (OpenAI, Azure, MCP, Docker, gRPC)
    autogen-magentic-one/     — Magentic-One multi-agent team implementation
    autogen-studio/           — no-code visual agent builder
    autogen-test-utils/       — test utilities
    magentic-one-cli/         — CLI wrapper for Magentic-One
    pyautogen/                — legacy compatibility shim
README.md
FAQ.md
CONTRIBUTING.md
TRANSPARENCY_FAQS.md
```
