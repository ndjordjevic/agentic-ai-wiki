---
type: source
category: "Agent frameworks & SDKs"
source_url: https://github.com/pydantic/pydantic-ai
tags:
  - agent-framework
  - type-safe-agents
  - model-agnostic
  - capabilities
  - mcp
  - durable-execution
  - dependency-injection
  - structured-output
related:
  - pydantic.dev
  - langchain.com
  - x.ai
  - strandsagents.com
  - adk.dev
  - crewai.com
  - Shubhamsaboo-awesome-llm-apps
  - eve.dev
  - mozilla-ai-any-llm
  - microsoft-semantic-kernel
  - agno.com
  - mastra.ai
product: pydantic-ai
detail_level: standard
created: 2026-07-13
updated: 2026-08-24
---

Pydantic AI is the Pydantic team's Python agent framework (18,400+ stars, MIT) — the flagship product of the wider [[pydantic.dev]] stack, brought to FastAPI-style ergonomics: type-safe agents, model-agnostic providers, dependency injection, and structured output validated by Pydantic itself. This page goes deeper than [[pydantic.dev]]'s stack-wide overview, covering the framework's agent loop, capabilities system, tool model, and its separately-versioned "Harness" capability library.

_All claims below are sourced from ../../raw/github/pydantic-pydantic-ai.md unless otherwise noted._

## What it does

Provides an `Agent` abstraction that wraps a conversational loop with an LLM: send instructions and a prompt, let the model call registered tools, validate structured output against a Pydantic model, and retry automatically on validation failure ("reflection and self-correction"). Agents are generic over their dependency type and output type, so static type checkers catch mismatches between tool signatures, dependency injection, and declared output schemas before runtime.

## Installation

```bash
pip install pydantic-ai
# or the slim core-only package:
pip install pydantic-ai-slim
```

## Key features

- **Model-agnostic** — first-class support for OpenAI, Anthropic, Gemini, DeepSeek, Grok, Cohere, Mistral, Perplexity, plus Azure AI Foundry, Amazon Bedrock, Google Cloud, Ollama, LiteLLM, Groq, OpenRouter, Together AI, Fireworks AI, Cerebras, Hugging Face, and more; custom models are a documented extension point.
- **Composable capabilities** — reusable bundles of tools, hooks, instructions, and model settings. Built-in capabilities cover web search, thinking, and MCP; the separate **Pydantic AI Harness** package (`pydantic-ai-harness`, its own GitHub repo) adds context management, memory, guardrails, filesystem access, code execution, and multi-agent orchestration as capabilities that "graduate" into core once they stabilize.
- **No-code agents** — agents can be defined entirely in YAML/JSON via the AgentSpec format, no Python required.
- **MCP and UI event streams** — integrates the Model Context Protocol for external tool/data access and various UI event-stream standards for interactive streaming applications.
- **Human-in-the-loop tool approval** — tool calls can be flagged to require approval before executing, conditioned on arguments, conversation history, or user preference.
- **Durable execution** — agents can preserve progress across transient API failures, restarts, and long-running human-in-the-loop workflows.
- **Streamed structured output** — output streams incrementally with immediate validation rather than waiting for a complete response.
- **Graph support** — `pydantic_graph` provides typed directed-graph execution for control flow too complex for plain agent loops.
- **Deep observability** — tight integration with Pydantic Logfire (OpenTelemetry) for tracing, evals-based performance monitoring, and cost tracking; any OTel backend works as an alternative.

## Architecture

The core agent loop is: instructions + prompt → LLM call → tool selection → tool execution → back to the LLM → final response, validated against the declared output type. Dependencies (database connections, config, auth context) are injected via a typed `RunContext`, keeping tool functions and dynamic instructions statically checkable against the `deps_type` declared on the `Agent`. Static instructions are keyword arguments; dynamic instructions are registered with the `@agent.instructions` decorator and can read from `RunContext`. Tools are registered with `@agent.tool`; their docstrings and parameter descriptions are extracted automatically into the tool schema sent to the model, and validation errors are passed back to the LLM so it can retry rather than failing the run outright.

Capabilities are the framework's extension mechanism: a capability bundles tools, hooks, instructions, and model settings into one reusable, installable unit (`capabilities=[Thinking(), WebSearch()]` on the `Agent` constructor). The split between core and the separate **Pydantic AI Harness** package is deliberate: core carries only capabilities that require deep model/provider integration (native tool support, provider-specific compaction APIs) or that are considered fundamental to nearly every agent (web search, tool search, thinking); everything else — memory, guardrails, filesystem access, code execution, multi-agent orchestration — starts life in the Harness package so it can iterate without core's backward-compatibility guarantees, then "graduates" into core once broadly proven (code mode is cited as an early graduation candidate). Many capabilities follow a "fall up" pattern: a local implementation that works with every model, upgraded automatically to a provider-native implementation when the active model supports it.

`pydantic_graph` provides typed directed-graph execution for control flows too complex for a plain agent loop, and durable-execution backends let agents preserve progress across transient failures and long-running human-in-the-loop workflows.

## Example usage

```python
from pydantic_ai import Agent

agent = Agent(
    'anthropic:claude-sonnet-4-6',
    instructions='Be concise, reply with one sentence.',
)
result = agent.run_sync('Where does "hello world" come from?')
print(result.output)
```

Dependency injection and structured output:

```python
from dataclasses import dataclass
from pydantic import BaseModel, Field
from pydantic_ai import Agent, RunContext

@dataclass
class SupportDependencies:
    customer_id: int
    db: DatabaseConn

class SupportOutput(BaseModel):
    support_advice: str = Field(description='Advice returned to the customer')
    block_card: bool = Field(description="Whether to block the customer's card")
    risk: int = Field(description='Risk level of query', ge=0, le=10)

support_agent = Agent(
    'openai:gpt-5.2',
    deps_type=SupportDependencies,
    output_type=SupportOutput,
    instructions='You are a support agent in our bank...',
)

@support_agent.tool
async def customer_balance(ctx: RunContext[SupportDependencies], include_pending: bool) -> float:
    """Returns the customer's current account balance."""
    return await ctx.deps.db.customer_balance(id=ctx.deps.customer_id, include_pending=include_pending)
```

Capabilities are added at construction time: `Agent(model, capabilities=[Thinking(), WebSearch(local='duckduckgo')])`.

## Maintenance status

18,459 stars, 2,350 forks, MIT license, actively maintained (pushed 2026-07-13). Latest release `v1.107.1` (2026-07-10). Ships repo-level `AGENTS.md` and `CLAUDE.md` plus per-tool `.agents/`, `.claude/`, `.gemini/` directories — the project dogfoods multiple coding-agent harnesses on itself. Part of the same [[pydantic.dev]] product family as Pydantic Validation, Pydantic Logfire, and Pydantic Evals (which ships inside the `pydantic-ai` package). The dedicated **Pydantic AI Harness** repo (`github.com/pydantic/pydantic-ai-harness`) is the official extended-capability library — a candidate for separate ingest if deeper coverage of individual capabilities is needed. Comparable framework alternatives already in this wiki include [[langchain.com]], [[strandsagents.com]], [[adk.dev]], and [[crewai.com]] — Pydantic AI differentiates primarily on static type-safety and tight Pydantic-ecosystem integration over a from-scratch abstraction layer.
