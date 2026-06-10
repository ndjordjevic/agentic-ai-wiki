# microsoft-autogen

## Fetch log
- Inbox URL: https://microsoft.github.io/autogen/stable//index.html#
- Final URL: https://microsoft.github.io/autogen/stable/index.html
- Fetched: 2026-06-10
- Pages: 7
- Mode: standard

## Landing page — https://microsoft.github.io/autogen/stable/index.html

AutoGen is a framework for building AI agents and applications. It presents four main components:

**Studio** — A web-based UI for prototyping agents without coding. Install via `pip install -U autogenstudio`. Provides Team Builder (visual drag-and-drop agent team configuration), Playground (interactive testing with live message streaming), Gallery (community-created component hub), and Deployment (export as Python code, set up endpoints, run in Docker).

**AgentChat** — A high-level programming framework for building conversational agent applications built on `autogen-core`. Recommended starting point for beginners. Provides agents with preset behaviors and teams with predefined multi-agent design patterns. Install via `pip install -U "autogen-agentchat" "autogen-ext[openai,azure]"`. Requires Python 3.10+.

**Core** — An event-driven programming framework for scalable multi-agent AI systems. Suited for deterministic workflows, research collaboration, and distributed applications. Uses the Actor model for asynchronous messaging, scalable distributed multi-agent networks, multi-language support (Python and .NET), modular and extensible architecture, and built-in observability and debugging.

**Extensions** — Implementations interfacing with external services, including McpWorkbench for Model-Context Protocol servers, OpenAIAssistantAgent for the Assistant API, DockerCommandLineCodeExecutor for containerized code execution, and GrpcWorkerAgentRuntime for distributed agents. Package: `autogen-ext`.

Navigation: user guides for Studio, AgentChat, Core, Extensions; API reference documentation; .NET resources; GitHub; Discord; Twitter. Migration guide available for users coming from AutoGen 0.2.

**Important:** AutoGen is now in maintenance mode. New users should start with [Microsoft Agent Framework](https://github.com/microsoft/agent-framework). Existing users are encouraged to migrate.

## Docs — https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/index.html

**AgentChat** is a high-level API for building multi-agent applications built on `autogen-core`. It is the recommended starting point for beginners.

Documentation sections:
- **Getting Started**: Installation and Quickstart guides
- **Tutorial**: Models, Messages, Agents, Teams, Human-in-the-loop interaction, Termination, State management
- **Advanced Topics**: Custom agents, Selector group chat, Swarm patterns, Magentic-One, GraphFlow workflows, Memory/RAG, Logging, Serialization, Tracing
- **Examples**: Travel planning, Company research, Literature review use cases

Additional resources: API Reference, PyPI package, GitHub source repository, `autogen-core` for users needing event-driven programming, migration guide from version 0.2.x to 0.4.x.

## Quickstart — https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/quickstart.html

**Installation:**
```bash
pip install -U "autogen-agentchat" "autogen-ext[openai,azure]"
```

**Core concept:** Build a single agent that can use tools by creating an `AssistantAgent` with OpenAI's GPT-4o model.

Key code components:
- `OpenAIChatCompletionClient` for model configuration
- `AssistantAgent` class for agent creation
- Async tool functions (e.g., `get_weather()`)
- `Console()` for streaming output to users

Features demonstrated:
- Tool integration for agents
- System message customization
- Tool reflection capability (`reflect_on_tool_use=True`)
- Token streaming from models

Next: Tutorial section for walkthrough of AgentChat features.

## Core — https://microsoft.github.io/autogen/stable/user-guide/core-user-guide/index.html

AutoGen Core is a system for building event-driven, distributed, scalable, resilient AI agent systems using the Actor model.

Six capabilities:
1. **Asynchronous Messaging** — Agents communicate through asynchronous messages, enabling event-driven and request/response communication models.
2. **Scalable & Distributed** — Supporting complex multi-agent networks across organizational boundaries.
3. **Multi-Language Support** — Currently Python and .NET with plans for additional languages.
4. **Modular & Extensible** — Customizable through agents, memory services, tools, and model libraries.
5. **Observable & Debuggable** — Built-in tracing and debugging capabilities.
6. **Event-Driven Architecture** — Overall system design approach.

Sidebar sections: Core Concepts, Framework Guide, Components Guide, Multi-Agent Design Patterns, Cookbook with practical examples.

## Design Patterns — https://microsoft.github.io/autogen/stable/user-guide/core-user-guide/design-patterns/intro.html

Multi-agent design patterns guide for AutoGen Core. "A multi-agent design pattern is a structure that emerges from message protocols: it describes how agents interact with each other to solve problems."

Research works like AutoGen, MetaGPT, and ChatDev have shown multi-agent systems out-performing single agent systems at complex tasks like software development.

Design patterns listed:
- Concurrent Agents
- Sequential Workflow
- Group Chat
- Handoffs
- Mixture of Agents
- Multi-Agent Debate
- Reflection
- Code Execution

Navigation includes Installation, Quick Start, Core Concepts, Framework Guide, Components Guide, and Cookbook sections.

## Studio — https://microsoft.github.io/autogen/stable/user-guide/autogenstudio-user-guide/index.html

AutoGen Studio is a low-code interface for prototyping AI agents, equipping them with tools, organizing them into teams, and interacting with them to complete tasks. Built upon AutoGen AgentChat.

Four primary interfaces:
1. **Team Builder** — Visual tool for creating agent teams via JSON specification or drag-and-drop. Supports configuration of teams, agents, tools, models, and termination conditions.
2. **Playground** — Interactive testing environment with live message streaming, visual control transition graphs, and full execution control.
3. **Gallery** — Hub for discovering and importing community-created components for third-party integration.
4. **Deployment** — Export teams as Python code, set up endpoints, run teams in Docker containers.

**Security note:** AutoGen Studio is "a research prototype and is **not meant to be used** in a production environment." Organizations building production applications should implement the underlying AutoGen framework with necessary security measures. Public roadmap maintained on GitHub.

## Extensions — https://microsoft.github.io/autogen/stable/user-guide/extensions-user-guide/index.html

The `autogen-ext` package contains built-in component implementations maintained by the AutoGen project.

Component categories:
- **Agents**: `MultimodalWebSurfer` for web interactions
- **Models**: `OpenAIChatCompletionClient` and adapters for hosted/local models
- **Tools**: GraphRAG tools and `mcp_server_tools()`
- **Executors**: Docker and Azure-based code execution options
- **Runtimes**: `GrpcWorkerAgentRuntime` for agent orchestration

"We strongly encourage developers to build their own components and publish them as part of the ecosystem."

Actions: Discover community extensions and samples; Create your own extension. API Reference for comprehensive component documentation; PyPI for package distribution.
