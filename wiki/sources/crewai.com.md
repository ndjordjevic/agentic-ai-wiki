---
type: source
category: "Agent frameworks & SDKs"
source_url: https://crewai.com/
companion_urls:
  - https://github.com/crewAIInc/crewAI
raw_files:
  - ../../raw/web/crewai.com.md
  - ../../raw/github/crewaiinc-crewai.md
tags:
  - multi-agent-framework
  - agent-orchestration
  - role-playing-agents
  - flows
  - crews
  - enterprise-agents
  - agentic-ai
  - python
related:
  - abacus.ai
  - langchain.com
  - strandsagents.com
  - developers.openai.com
  - litellm.ai
  - pydantic.dev
  - warp.dev
  - joinoasis.com
  - factory.ai
  - pi.dev
  - microsoft-autogen
  - zapier.com
  - trigger.dev
  - microsoft-agent-framework
  - ruvnet-ruflo
  - ollama-ollama
  - adk.dev
  - google-adk-go
  - agentixlabs.com
  - clickup.com
  - pydantic-pydantic-ai
  - Shubhamsaboo-awesome-llm-apps
product: crewai
detail_level: standard
created: 2026-05-22
updated: 2026-07-17
---

CrewAI is the leading open-source multi-agent orchestration framework, offering both a Python library (CrewAI OSS) and an enterprise platform (CrewAI AMP) for building, deploying, and managing production AI agent systems. It introduces a two-layer architecture — **Crews** (teams of role-playing autonomous agents) nested inside **Flows** (event-driven orchestration backbone) — that balances autonomy with deterministic control. With 51,000+ GitHub stars, 100,000+ certified developers, and adoption across 60% of the Fortune 500, it has become a de-facto standard for enterprise agentic automation.

_All claims below are sourced from ../../raw/web/crewai.com.md unless otherwise noted._

## What it does

CrewAI lets developers define teams of AI agents that collaborate on complex multi-step tasks. Each agent has a `role`, `goal`, and `backstory`, and is equipped with tools and optional memory. Agents in a Crew communicate, delegate, and produce structured outputs that flow between tasks. Crews are embedded inside Flows — structured event-driven programs that manage state, control execution order, and handle conditional branching. The platform (CrewAI AMP) adds a visual Studio editor, enterprise integrations (Gmail, Slack, Salesforce, Teams), observability tracing, RBAC, SSO, secrets management, and serverless auto-scaling.

## Key features

- **Crews**: Teams of agents with `role`/`goal`/`backstory`, supporting sequential and hierarchical processes, planning mode (AgentPlanner), and checkpointing for resumable execution.
- **Flows**: Event-driven orchestration with `@start()`, `@listen()`, and `@router()` decorators; built-in state management and `flow.plot()` visualization.
- **Memory**: Unified `Memory` class with LLM-inferred scope/importance and composite recall scoring (semantic + recency + importance). (../../raw/github/crewaiinc-crewai.md)
- **Tools**: 30+ built-in tools (SerperDevTool, WebsiteSearchTool, CodeInterpreterTool, DALL-E, GitHub, PDF/CSV/JSON search, etc.) plus LangChain tool compatibility; all with caching and async support.
- **Skills**: Filesystem-based skill packages (`npx skills add crewaiinc/skills`) that inject domain instructions into agent prompts. (../../raw/github/crewaiinc-crewai.md)
- **AMP Enterprise features**: CrewAI Studio (no-code visual editor), real-time tracing, human-in-the-loop HITL flows, hallucination guardrail, PII redaction, A2A (Agent-to-Agent) communication, RBAC, SSO, and 20+ integration triggers.

## Architecture

CrewAI is built entirely from scratch in Python, independent of LangChain or any other agent framework, prioritizing speed and minimal resource usage. (../../raw/github/crewaiinc-crewai.md)

**Core layers:**

1. **Flows** — the execution backbone. A Flow is a Python class with `@start()` entry points and `@listen()` steps. State is a dict (or Pydantic model) that persists across steps; each run gets a UUID. Flows can delegate to Crews at any step and aggregate results.

2. **Crews** — the intelligence units. A Crew is a `@CrewBase` Python class referencing YAML `agents.yaml` and `tasks.yaml` configs. The crew's `process` controls execution order: `sequential` (each task feeds the next) or `hierarchical` (a manager LLM delegates). A `planning` flag adds a pre-run AgentPlanner pass. (../../raw/github/crewaiinc-crewai.md)

3. **Agents** — role-playing autonomous units. Each agent uses a configurable LLM, has a tool set, and can reason (pre-task planning), use memory, execute code in Docker or direct mode, and handle multimodal inputs. (../../raw/github/crewaiinc-crewai.md)

4. **Memory** — the unified `Memory` class replaces separate short-term/long-term/entity types with one API. Uses an LLM to infer scope and importance at write time; retrieval uses composite scoring (semantic + recency + importance). Scoped views let agents have private vs. shared memory. (../../raw/github/crewaiinc-crewai.md)

## Installation

Requires Python ≥ 3.10 and `uv` for dependency management. (../../raw/github/crewaiinc-crewai.md)

```bash
pip install uv
uv tool install crewai             # installs CLI
crewai create crew my_project      # scaffolds project
cd my_project
crewai run                         # runs crew
```

For tools: `pip install 'crewai[tools]'`. Secrets and LLM provider keys go in `.env`. YAML configs (`agents.yaml`, `tasks.yaml`) define agent roles and task descriptions.

## Example usage

A minimal crew with YAML-configured agents: (../../raw/github/crewaiinc-crewai.md)

```python
from crewai import Agent, Task, Crew, Process

researcher = Agent(
    role='Senior Research Analyst',
    goal='Uncover cutting-edge developments in {topic}',
    backstory='A seasoned researcher with a knack for finding relevant information.',
    tools=[search_tool],
    verbose=True
)

task = Task(
    description='Research the latest trends in {topic}',
    expected_output='A summary of top 3 developments',
    agent=researcher
)

crew = Crew(agents=[researcher], tasks=[task], process=Process.sequential)
result = crew.kickoff(inputs={'topic': 'AI agents'})
```

A Flow wrapping a crew step:

```python
from crewai.flow.flow import Flow, listen, start

class ResearchFlow(Flow):
    @start()
    def gather_topic(self):
        self.state['topic'] = 'AI agents'
        return self.state['topic']

    @listen(gather_topic)
    def run_crew(self, topic):
        return research_crew.kickoff(inputs={'topic': topic})

flow = ResearchFlow()
result = flow.kickoff()
```

## When to use

CrewAI excels at automating complex, multi-step workflows where different roles require different expertise: research pipelines, document generation, lead enrichment, code generation, customer support, and process automation. Choose CrewAI OSS for open-source Python projects needing full low-level control. Use CrewAI AMP Cloud for hosted enterprise deployments with monitoring and integrations. Use CrewAI AMP Factory for on-prem or private cloud deployments (AWS, Azure, GCP).

## Maintenance status

51,928 GitHub stars, 7,199 forks, MIT license, actively maintained by CrewAI Inc. Latest release `1.14.6a1` published 2026-05-21. Repository pushed to 2026-05-22. Community at `community.crewai.com`; 100,000+ certified developers via `learn.crewai.com`. (../../raw/github/crewaiinc-crewai.md)

## Ecosystem

CrewAI tools are compatible with LangChain tools (see [[langchain.com]]). CrewAI OSS can use any LiteLLM-supported model (see [[litellm.ai]]), making it model-agnostic across OpenAI, Anthropic, Google, Ollama, and others. CrewAI AMP has a Marketplace for reusable agent assets, and the `crewaiinc/skills` skill packages work across Claude Code, Cursor, Codex, and Windsurf. Enterprise integrations cover Gmail, Google Drive, Google Calendar, HubSpot, Jira, Slack, Salesforce, Microsoft Teams, OneDrive, Outlook, SharePoint, ClickUp, Asana, Linear, Box, GitHub, and Zapier.

For comparable multi-agent frameworks, see [[strandsagents.com]] (AWS/Bedrock-centric, model-driven SDK) and [[langchain.com]] (LangGraph for graph-based agent control).
