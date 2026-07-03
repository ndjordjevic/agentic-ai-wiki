---
type: source
source_url: https://adk.dev/
companion_urls:
  - https://github.com/google/adk-python
raw_files:
  - ../../raw/web/adk.dev.md
  - ../../raw/github/google-adk-python.md
tags:
  - adk
  - google-adk
  - multi-agent
  - graph-workflows
  - a2a-protocol
  - gemini
  - agent-evaluation
  - model-agnostic
related:
  - agents-cli
  - antigravity.google
  - microsoft-agent-framework
  - langchain.com-langgraph
  - crewai.com
  - strandsagents.com
  - pydantic.dev
  - clickup.com
  - trigger.dev
product: adk
detail_level: standard
created: 2026-06-30
updated: 2026-07-03
---

**Agent Development Kit (ADK)** is Google's open-source, code-first framework for building, evaluating, and deploying production-grade AI agents. Available in Python, TypeScript, Go, Java, and Kotlin, it is model-agnostic and deployment-agnostic — optimized for Gemini and Google Cloud but supporting Claude, Ollama, vLLM, LiteLLM, and hosted enterprise models. ADK 2.0 (Python GA May 2026) adds graph-based `Workflow` runtime and collaborative multi-agent patterns. The docs site and companion Python repo (`google/adk-python`, 20k+ stars, v2.3.0, Apache 2.0) are the canonical references. (../../raw/github/google-adk-python.md)

_All claims below are sourced from ../../raw/web/adk.dev.md unless otherwise noted._

## What it does

ADK provides the primitives and runtime to move from agent prototypes to production systems. Core building blocks: `Agent` (LLM reasoning or deterministic workflow controllers), `Tool` (external APIs, code, services), callbacks, session/state/memory, artifacts, and a `Runner` that orchestrates execution via events. Developers start with simple prompt+tool agents and scale to multi-agent hierarchies, graph workflows, A2A cross-service agents, streaming (Gemini Live), evaluation suites, and GCP deployment — without rewriting agent code.

The framework treats context management as a first-class concern: sessions, memory, tool outputs, and artifacts are assembled into structured views with automatic filtering, summarization, lazy artifact loading, and token tracking.

## Key features

### ADK 2.0 (Python GA)
- **Workflow Runtime** — graph-based execution: routing, fan-out/fan-in, loops, retry, dynamic nodes, HITL, nested workflows
- **Task API** — structured agent-to-agent delegation, multi-turn/single-turn modes, task agents as workflow nodes
- **`Workflow` class** — `edges=[("START", node_a, router), (router, {"route": target})]` syntax with `JoinNode` for parallel assembly

### Agent & orchestration patterns
| Pattern | Description |
|---|---|
| Simple `Agent` | Model + instruction + tools |
| Template workflows | `SequentialAgent`, `ParallelAgent`, `LoopAgent` |
| Graph workflows (2.0) | Explicit node/edge graphs mixing agents, tools, functions |
| Dynamic workflows (2.0) | Full programmatic control flow |
| Collaborative (2.0) | Coordinator agent + specialized subagents |
| Agent routing (experimental) | Runtime router for fallback, A/B, auto-routing |

### Tools & integrations
- **Custom:** `FunctionTool`, OpenAPI tools, MCP tools, authentication, action confirmations
- **Built-in:** code execution, Google Search grounding, computer use
- **Agent-as-tool:** `AgentTool` for hierarchical delegation
- **100+ integration docs:** BigQuery, Spanner, GCS, GitHub/GitLab MCP, observability partners (Cloud Trace, Datadog, Phoenix, MLflow, LangWatch), guardrails, Temporal/Dapr plugins, and more (../../raw/github/google-adk-python.md)

### Cross-agent & streaming
- **A2A Protocol** — expose agents via `A2AServer`, consume via `RemoteA2aAgent` for cross-language/cross-team microservice agents
- **Gemini Live API Toolkit** — bidirectional streaming (text + audio), streaming tools, multimodal dev guide (5 parts)

### Developer experience
- **CLI:** `adk run`, `adk web` (multi-agent dev UI)
- **Visual Builder** — web interface for agent design
- **Code with AI** — ADK developer Skills for vibe-coding agents
- **[[agents-cli]]** — scaffold/eval/deploy ADK agents via coding agents

### Evaluation & safety
- Trajectory + final-response evaluation (`.test.json` unit tests, Eval Set/Eval Case schemas)
- Groundtruth and rubric-based tool-use metrics
- User simulation, environment simulation, custom metrics, prompt optimization
- Safety and security docs; guardrail plugins (ATR, Cisco AI Defense)

### Models supported
Gemini, Gemma, Claude, Agent Platform hosted, Apigee AI Gateway, Ollama, vLLM, LiteLLM, LiteRT-LM, model routing

## Architecture

Three-layer mental model in Python 2.0:
1. **Agents/Tools/Functions** as graph nodes (`BaseNode`)
2. **Workflow graph engine** — deterministic routing, event emission, retries, HITL pauses
3. **Session/Event store** — conversation history with 2.0 `node_info`/`output` fields

Multi-language SDKs share concepts; Python is the reference. Related repos: `google/adk-samples`, `google/adk-web`, `google/adk-docs`. (../../raw/github/google-adk-python.md)

## Installation

```bash
# Python (primary)
pip install google-adk
pip install "google-adk[extensions]"

# Other languages
npm install @google/adk
go get google.golang.org/adk
# Java: com.google.adk:google-adk
# Kotlin: com.google.adk:google-adk-kotlin-core
```

Python 3.10+. Stay on 1.x: `pip install "google-adk~=1.0"`. (../../raw/github/google-adk-python.md)

## Example usage

```python
from google.adk import Agent
from google.adk.tools import google_search

agent = Agent(
    name="researcher",
    model="gemini-flash-latest",
    instruction="You help users research topics thoroughly.",
    tools=[google_search],
)
```

```python
from google.adk import Agent, Workflow

root_agent = Workflow(
    name="root_agent",
    edges=[("START", generate_fruit_agent, generate_benefit_agent)],
)
```

```bash
adk run path/to/my_agent
adk web path/to/agents_dir
```

Deploy: Agent Runtime (Agent Platform), Cloud Run, GKE, or any container runtime. (../../raw/github/google-adk-python.md)

## When to use

- You need a **production-grade agent framework** with evaluation, deployment, observability, and multi-agent orchestration built in
- You want **graph-based workflows** (ADK 2.0) combining deterministic code paths with LLM reasoning
- You need **model flexibility** (Gemini-first but not locked) and **deploy-anywhere** (self-hosted or GCP)
- You're building on Google Cloud Agent Platform / Gemini Enterprise and want native Agent Runtime integration
- Pair with **[[agents-cli]]** when you want a coding agent to scaffold/eval/deploy ADK projects
- **vs [[antigravity.google]]:** ADK is the agent *framework*; Antigravity SDK is a separate harness for Antigravity's coding-agent runtime — complementary layers in Google's stack
- **vs [[langchain.com-langgraph]] / [[crewai.com]]:** ADK is Google's native alternative with A2A, Agent Platform deployment, and Gemini Live streaming

## Maintenance status

Actively maintained by Google: `google/adk-python` 20,339 stars, 3,622 forks, latest v2.3.0 (2026-06-18), pushed 2026-06-30, Apache 2.0, ~bi-weekly releases. ADK 2.0 GA since May 2026. ADK Kotlin newly announced. Community calls, contributing guide, 350+ contributors on Python repo. (../../raw/github/google-adk-python.md)

## Ecosystem

- **[[agents-cli]]** — lifecycle tooling around ADK (scaffold, eval, deploy, observability skills)
- **Antigravity platform** — separate coding-agent product; references ADK in Google's agent stack
- **A2A Protocol** — open standard for cross-framework agent communication
- **Agent Platform / Gemini Enterprise** — Agent Runtime, Memory Bank, managed sessions, eval SDK
- **Integration partners** — 100+ documented connectors (observability, databases, MCP, guardrails)
- **Samples:** [github.com/google/adk-samples](https://github.com/google/adk-samples)

## Documentation

Docs at [adk.dev](https://adk.dev/) organized into Build Agents (get started, tutorials, agents, graphs, workflows, models), Run Agents (runtime, deploy, observability, evaluate, safety), Components (tools, skills, sessions, callbacks, MCP, A2A, streaming, grounding), Integrations (100+ pages), Reference (API per language, release notes), and ADK 2.0 migration guide. `llms.txt` provides full URL catalog for LLM ingestion.
