---
type: source
category: "Agent frameworks & SDKs"
source_url: https://www.agno.com/
companion_urls:
  - https://github.com/agno-agi/agno
raw_files:
  - ../../raw/web/agno.com.md
  - ../../raw/github/agno-agi-agno.md
tags:
  - multi-agent-framework
  - agentos-runtime
  - self-hosted
  - jwt-rbac
  - model-agnostic
  - mcp-integration
  - production-api
  - control-plane
related:
  - crewai.com
  - strandsagents.com
  - pydantic-pydantic-ai
  - microsoft-agent-framework
  - microsoft-autogen
  - langchain.com-langgraph
  - mastra.ai
  - ai-sdk.dev
product: agno
detail_level: standard
created: 2026-07-28
updated: 2026-07-28
---

Agno is an open-source Python framework and runtime (41,000+ GitHub stars, Apache-2.0) for building, running, and managing multi-agent AI platforms, pairing a lightweight SDK for defining agents/teams/workflows with **AgentOS**, a self-hostable, stateless FastAPI runtime that turns those agents into a production service with its own web control plane.

_All claims below are sourced from ../../raw/web/agno.com.md unless otherwise noted._

## What it does

Agno lets developers turn any LLM into an agent with tools, memory, and knowledge using the Agno SDK, then run that agent platform in production via AgentOS — a stateless, secure FastAPI backend exposing 50+ API endpoints for runs, sessions, memory, knowledge, and traces. A third component, the Control Plane, is a web UI for managing and monitoring agents, memory, knowledge, sessions, and evaluations across the deployed platform. The framework is explicitly positioned as **framework-agnostic on the runtime side**: AgentOS can run agents built with Agno itself, the Claude Agent SDK, LangGraph, DSPy, or custom systems, not just Agno-native agents.

## Key features

- **Agent Framework (SDK)**: build agents, teams, and workflows with memory, knowledge, guardrails, and 100+ pre-built tool integrations (GitHub, Slack, Postgres, and more). (../../raw/github/agno-agi-agno.md)
- **AgentOS runtime**: 50+ production API endpoints with SSE and WebSocket support; durability, streaming, background execution, cron-based scheduling, and session monitoring. (../../raw/github/agno-agi-agno.md)
- **Model flexibility**: 30+ model providers across Chat, Responses, and Interactions APIs, configurable via a string form (`model="openai:gpt-5.4"`) or a class form for custom parameters/endpoints/retries.
- **Multi-agent Teams**: agents coordinate via a `TeamMode` parameter with four modes — `broadcast`, `route`, `coordinate` (default, leader-delegates), and `tasks` — supporting nested teams for composition.
- **Governance and security**: JWT-based role-based access control (RBAC), multi-user/multi-tenant isolation, built-in guardrails, human-in-the-loop approval flows, and audit trails/logs.
- **Interfaces**: expose agents via Slack, Telegram, WhatsApp, Discord, AG-UI, and A2A.
- **Observability**: OpenTelemetry tracing, run history, and audit logs built into the runtime.
- **Coding-agent integration**: Agno docs can be added as an MCP server (`docs.agno.com/mcp`) or as an indexed documentation source in Cursor/VS Code/Windsurf via `docs.agno.com/llms-full.txt`. (../../raw/github/agno-agi-agno.md)

## Architecture

The framework layer provides the core agent runtime, orchestration, memory/knowledge management, tool integration, and multi-modal (text/image/audio) support. The workspace/runtime layer (AgentOS) provisions production infrastructure — database, vector storage, API endpoints, authentication — and can be deployed to any container-capable cloud (Docker, Railway, AWS, GCP, Azure, Fly, Kubernetes, Render, Modal). The control plane sits above both, providing real-time monitoring, evaluation, and team-collaboration tooling. Rather than shipping one opinionated deploy target, Agno maintains a family of separate starter-template repos under the `agno-agi` GitHub org (`agentos-railway`, `agentos-docker`, `agentos-aws`, `agentos-gcp`, `agentos-azure`, `agentos-fly`, `agentos-render`, `agentos-modal`, `agentos-helm`) that differ only in deploy scripts — the recommended onboarding path is to hand a coding agent (Claude Code, Cursor, Codex) a prompt that clones the relevant template and follows its setup guide. (../../raw/github/agno-agi-agno.md)

## Installation

```bash
pip install agno
```

```python
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    tools=[DuckDuckGoTools()],
    description="AI assistant with web search capabilities",
    instructions="Always search for current information and cite sources"
)

agent.print_response("What are the latest AI trends in 2025?")
```

For a full production platform (Postgres, MCP server, control plane, REST API), the README recommends handing a coding agent a prompt that clones one of the `agentos-*` deploy-template repos rather than assembling infrastructure by hand. (../../raw/github/agno-agi-agno.md)

## Example usage

The single-agent example above shows the core pattern: instantiate a model, attach tools, and call `agent.print_response(...)`. Teams are built by grouping agents/nested-teams under a `Team` object with a `TeamMode` (default `coordinate`, where a leader agent delegates sub-tasks to member agents based on their roles); each member's response and metrics can be inspected separately. Teams support callable factories for `knowledge`, `tools`, and `members`, enabling dynamic per-run configuration, at the cost of extra model calls (one per leader, one per member) affecting latency and token usage.

## When to use

Agno fits teams that want to own their full agent stack — data, memory, and security posture — on self-hosted infrastructure (including airgapped environments) rather than a managed SaaS platform, and that need a single runtime capable of serving agents built across multiple frameworks (Agno-native, Claude Agent SDK, LangGraph, DSPy). It's a reasonable point of comparison against other production-oriented multi-agent frameworks in this wiki such as [[crewai.com]] (Crews + Flows, also offers a managed enterprise tier) and [[microsoft-agent-framework]] (Microsoft's production successor to AutoGen/Semantic Kernel, deployable to Microsoft Foundry). Use single agents instead of Teams for single-domain tasks where minimizing token cost or coordination overhead matters.

## Maintenance status

Actively developed: latest release v2.8.5 (2026-07-27), with commits pushed as recently as 2026-07-28. 41,460 stars, 5,703 forks, Apache-2.0 licensed. Telemetry is opt-out (`AGNO_TELEMETRY=false`) and explicitly does not send prompts, messages, or outputs. (../../raw/github/agno-agi-agno.md)

## Ecosystem

Agno's pricing model mirrors other open-core agent frameworks in this wiki: the SDK and AgentOS runtime are free/open-source, with a paid "Pro" tier ($95/month per workspace) adding managed workspaces, production monitoring, priority support, and advanced analytics, plus a custom Enterprise tier for SSO and SLAs. Supported vector databases include Pinecone, LanceDB, SingleStore, Qdrant, Weaviate, ChromaDB, and Postgres with pgvector. Because AgentOS is explicitly framework-agnostic, it can serve as a shared production runtime for agents built with [[langchain.com-langgraph]] or other frameworks, positioning Agno as much as an operations layer as an agent-authoring SDK — a different emphasis from purely-authoring-focused frameworks like [[pydantic-pydantic-ai]] and [[strandsagents.com]].
