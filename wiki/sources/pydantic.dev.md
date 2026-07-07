---
type: source
source_url: https://pydantic.dev/
companion_urls:
  - https://github.com/pydantic/pydantic
raw_files:
  - ../../raw/web/pydantic.dev.md
  - ../../raw/github/pydantic-pydantic.md
tags: [data-validation, agent-framework, observability, opentelemetry, type-safety, llm-proxy, python, pydantic-ai]
related: [langchain.com, litellm.ai, crewai.com, strandsagents.com, adk.dev, google-adk-go, developers.openai.com, ollama-ollama, vercel.com, render.com]
product: pydantic
detail_level: standard
created: 2026-05-22
updated: 2026-07-07
---

Pydantic is an end-to-end AI engineering stack for Python teams, built on a foundation of the world's most widely used data validation library. It covers the full product cycle — validate data with Pydantic Validation (550M downloads/month, MIT), build type-safe agents with Pydantic AI, route model calls with Pydantic AI Gateway, evaluate systematically with Pydantic Evals, and observe everything in production with Pydantic Logfire. All products share the same type-hints-first design philosophy and tight OpenTelemetry integration.

_All claims below are sourced from ../../raw/web/pydantic.dev.md unless otherwise noted._

## What it does

Pydantic provides five interlocking products that span the entire lifecycle of a Python AI application:

1. **Pydantic Validation** — runtime data validation and serialization via Python type annotations. The foundational library used by FastAPI, LangChain, OpenAI SDK, Anthropic SDK, CrewAI, LlamaIndex, AutoGPT, Transformers, and ~8,000 other PyPI packages. Core written in Rust; ~550M monthly downloads.
2. **Pydantic AI** — production-grade agent framework. Model-agnostic (OpenAI, Anthropic, Gemini, Ollama, LiteLLM, and 20+ other providers), fully type-safe, with first-class MCP support, multi-agent orchestration, durable execution, and composable capabilities.
3. **Pydantic Logfire** — SaaS and self-hosted AI observability platform built on OpenTelemetry. Ingests from Python, TypeScript/JavaScript, Rust, and any OTel-compatible language. Features traces, logs, metrics, LLM cost tracking, online evals, and an MCP server.
4. **Pydantic Evals** — code-first evaluation framework for LLM apps and agents. Ships inside `pydantic-ai` (Python) and the Logfire JS SDK; integrates with Logfire for visualization and comparison.
5. **Pydantic AI Gateway** — unified LLM proxy (AGPL-3.0 core). Passes requests in each provider's native format with no schema translation, granular spend caps, and an OTel audit trail. Consolidating into Logfire.

## Key features

- **Type-safety throughout** — Pydantic Validation's BaseModel and type-hint enforcement extends naturally into Pydantic AI's structured outputs, making entire categories of runtime errors catch-able at write time. (../../raw/github/pydantic-pydantic.md)
- **Model-agnostic** — Pydantic AI supports 20+ providers and model families; swapping models requires changing one constructor argument.
- **Composable capabilities** — Pydantic AI agents are assembled from reusable capabilities (bundles of tools, hooks, instructions, model settings) installable as third-party packages.
- **No-code agents** — define Pydantic AI agents entirely in YAML/JSON via the AgentSpec format.
- **Durable execution** — Pydantic AI integrates with durable execution backends to preserve agent progress across transient failures and long-running human-in-the-loop workflows.
- **OpenTelemetry-native** — every product emits OTel traces by default; Logfire is the first-party dashboard but any OTel backend works.
- **Native format LLM proxy** — AI Gateway forwards requests in each provider's native schema, so new provider features (streaming modes, extended thinking, etc.) are accessible the day they ship.
- **Evals in CI** — `pydantic-evals` runs as Python code in test suites; Logfire surfaces results as visual dashboards. (../../raw/github/pydantic-pydantic.md)

## Architecture and concepts

**Pydantic Validation** uses a dual-layer architecture: a Python API that accepts type-annotated BaseModel subclasses, and a Rust core (`pydantic-core`) that executes validation at high speed. Validation can run in lax mode (coercing compatible types) or strict mode (no coercion). Output modes include Python objects, dicts, JSON strings, and JSON Schema. (../../raw/github/pydantic-pydantic.md)

**Pydantic AI** implements an agentic loop: Agent → LLM call → tool selection → tool execution → back to LLM → final response. The loop is type-safe at each step (input types, output types, tool argument types, dependency injection types). Capabilities package tools and hooks into reusable, installable units. Graphs provide typed directed-graph execution for complex control flows.

**Pydantic Logfire** is built on the OpenTelemetry collector stack. The Python SDK wraps standard `logfire.configure()` + `logfire.info()`/`logfire.span()` calls; auto-instrumentation patches popular libraries (FastAPI, SQLAlchemy, httpx, OpenAI, Anthropic, etc.) with a single import. Online evals run as Logfire evaluators against live traffic traces.

**Pydantic AI Gateway** proxies provider APIs without schema translation — requests travel in native provider format and responses come back in native provider format. Spend caps and audit trails are enforced as a middleware layer. The self-hosted core is open-source (AGPL-3.0); the cloud dashboard runs inside Logfire.

## Main APIs

**Pydantic Validation:**
```python
from pydantic import BaseModel, Field, ValidationError

class User(BaseModel):
    id: int
    name: str = 'John Doe'

user = User(id='123')   # '123' coerced to int
user.model_dump()       # {'id': 123, 'name': 'John Doe'}
user.model_json_schema()  # JSON Schema dict
```

**Pydantic AI:**
```python
from pydantic_ai import Agent

agent = Agent(
    'anthropic:claude-sonnet-4-6',
    instructions='Be concise, reply with one sentence.',
)
result = agent.run_sync('Where does "hello world" come from?')
print(result.output)
```

**Pydantic Logfire:**
```python
import logfire
logfire.configure()
logfire.info('Hello, {name}!', name='world')
```

**Pydantic Evals:**
```python
from pydantic_evals import Case, Dataset

dataset = Dataset(cases=[
    Case(name='capitals', inputs='Capital of France?', expected_output='Paris')
])
await dataset.evaluate(my_agent_task)
```

## When to use

- **Pydantic Validation** — any Python project needing runtime type enforcement, JSON Schema generation, settings management (`pydantic-settings`), or validating LLM structured outputs. The standard choice when working with FastAPI or any project that already pulls Pydantic as a dependency.
- **Pydantic AI** — Python-first teams building production agents who want type-safety, model-portability, and OpenTelemetry observability without heavy framework overhead. Best fit when the team already uses Pydantic Validation; not suitable for non-Python languages.
- **Pydantic Logfire** — observing AI apps in production: LLM cost tracking, distributed tracing, latency monitoring, online evals. Strong choice for OpenTelemetry-first shops. Not a prompt playground or annotation-workflow tool.
- **Pydantic Evals** — systematic LLM/agent evaluation in CI; integrates directly with Pydantic AI and Logfire. Use when evaluation logic needs to live in code, not a web UI.
- **Pydantic AI Gateway** — unified LLM proxy with spend caps and audit trails; prefer when needing native-format routing without vendor lock-in. New users should consider Logfire directly since Gateway is consolidating there.

## Ecosystem

- **GitHub org** — `github.com/pydantic`: `pydantic`, `pydantic-ai`, `logfire`, and related repos (../../raw/github/pydantic-pydantic.md)
- **PyPI** — `pydantic`, `pydantic-ai`, `logfire`, `pydantic-evals`, `pydantic-settings`
- **NPM** — `@pydantic/logfire-node` (JavaScript/TypeScript SDK for Logfire)
- **MCP server** — `https://logfire.pydantic.dev/mcp` (OAuth, streamable-http); described at `/.well-known/mcp/server-card.json`
- **A2A agent card** — `https://pydantic.dev/.well-known/agent-card.json`
- **Agent-readable docs** — `https://pydantic.dev/agents.md`, `https://pydantic.dev/llms.txt`, `https://pydantic.dev/llms-full.txt`
- **Used by** — FastAPI, LangChain, OpenAI SDK, Anthropic SDK, CrewAI, LlamaIndex, AutoGPT, HuggingFace Transformers, and ~8,000 other packages
