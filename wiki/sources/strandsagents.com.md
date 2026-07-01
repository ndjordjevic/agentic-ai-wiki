---
type: source
source_url: https://strandsagents.com/
companion_urls:
  - https://github.com/strands-agents/sdk-python
raw_files:
  - ../../raw/web/strandsagents.com.md
  - ../../raw/github/strands-agents-sdk-python.md
tags: [agent-sdk, agent-loop, tool-calling, multi-agent, model-agnostic, hooks, mcp, amazon-bedrock]
related: [langchain.com, litellm.ai, crewai.com, pydantic.dev, factory.ai, microsoft-playwright-mcp, pi.dev, microsoft-autogen, microsoft-agent-framework, aaif-goose-goose, zapier.com, joinoasis.com, agentixlabs.com, adk.dev, warp.dev]
product: strandsagents
detail_level: standard
created: 2026-05-21
updated: 2026-07-01
---

Strands Agents is an open-source, model-driven agent harness SDK built by AWS that lets developers build and run AI agents in a few lines of code. It provides a complete agentic loop — reasoning, tool execution, conversation management, streaming, hooks, and multi-agent orchestration — for both Python and TypeScript. It defaults to Amazon Bedrock but is fully model-agnostic, supporting Anthropic, OpenAI, Google Gemini, Ollama, LiteLLM, and 10+ other providers through a common interface.

_All claims below are sourced from ../../raw/web/strandsagents.com.md unless otherwise noted._

## What it does

Strands Agents provides an agent harness: a runtime loop that invokes a model, intercepts tool requests, executes them, feeds results back into the model, and repeats until the model produces a final response. The "harness" framing emphasises that the developer retains end-to-end control — context window management, execution limits, guardrails, observability, and tool registration are all first-class primitives rather than afterthoughts.

Installation is `pip install strands-agents` (Python 3.10+) or `npm install @strands-agents/sdk` (TypeScript). An agent is instantiated with `Agent(tools=[...])` and invoked with `agent("your prompt")`.

## Key features

- **Lifecycle hooks** (`BeforeToolCallEvent`, `AfterToolCallEvent`, etc.) — intercept any step to log, validate, or cancel tool calls; the primary mechanism for guardrails and observability.
- **Steering handlers** — a plugin-based policy layer that inspects pending tool calls and returns `Guide(reason=...)` or `Proceed(...)` decisions; benchmark shows 100% task accuracy vs 82.5% prompt-only.
- **Conversation managers** — Null (stateless), SlidingWindow (token cap), and Summarizing (auto-condense history) keep the context window under control without agent code changes. (../../raw/github/strands-agents-sdk-python.md)
- **MCP support** — native `MCPClient` integration connects to any MCP server, including the project's own `strands-agents/mcp-server` for IDE-assisted development (Kiro, Cursor, Claude, Cline). (../../raw/github/strands-agents-sdk-python.md)
- **Structured output** and **streaming responses** (sync and async iterators / callback handlers).
- **Session management** — file, S3, and repository-backed session stores for durable state across runs.
- **OpenTelemetry integration** — built-in tracing with `trace_attributes` support; no additional setup required.
- **Bidirectional streaming (experimental)** — `BidiAgent` for real-time voice/WebSocket use-cases (Python only).

## Architecture

The agent loop is a simple recursive structure: Input & Context → Reasoning (LLM) → Tool Selection → Tool Execution → back to Reasoning → Response. Each pass accumulates conversation history (user messages with text/tool-results/media and assistant messages with text/tool-use/reasoning traces). The model sees the full accumulation, enabling multi-step reasoning. (../../raw/github/strands-agents-sdk-python.md)

**Stop reasons** determine loop exit: `end_turn` (success), `tool_use` (continue), `cancelled` (via `agent.cancel()`), `max_tokens` (unrecoverable error), `content_filtered`, `guardrail_intervention`.

**Multi-agent orchestration patterns** — three built-in approaches: (../../raw/github/strands-agents-sdk-python.md)

- **Graph** — developer-defined directed graph; LLM decides which edge to follow at each node; supports cycles; full conversation history in shared state; good for conditional business workflows.
- **Swarm** — pool of specialist agents that autonomously hand off; supports cycles; shared working memory; good for exploration and multi-perspective synthesis.
- **Workflow** — deterministic DAG executed as a single tool; no cycles; independent tasks run in parallel; inputs flow from dependency outputs; good for repeatable data pipelines.

**Model providers** are adapter classes (`BedrockModel`, `GeminiModel`, `OllamaModel`, etc.) passed at `Agent(model=...)`. Swapping providers requires changing one constructor argument; tool and hook code is unchanged. (../../raw/github/strands-agents-sdk-python.md)

## Installation

```bash
pip install strands-agents strands-agents-tools
```

```python
from strands import Agent, tool
from strands_tools import calculator

@tool
def word_count(text: str) -> int:
    """Count words in text."""
    return len(text.split())

agent = Agent(tools=[calculator, word_count])
agent("What is the square root of 1764?")
```
(../../raw/github/strands-agents-sdk-python.md)

## Example usage

**Guardrail via hook:**
```python
from strands import Agent
from strands.hooks import BeforeToolCallEvent

def require_sources(event: BeforeToolCallEvent):
    if event.tool_use["name"] == "save_report":
        if "[source]" not in str(event.tool_use["input"]):
            event.cancel_tool = "Add source citations."

agent = Agent(tools=[save_report], hooks=[require_sources])
agent("Research AI agent frameworks")
```

**MCP integration:**
```python
from strands.tools.mcp import MCPClient
from mcp import stdio_client, StdioServerParameters

client = MCPClient(lambda: stdio_client(StdioServerParameters(command="uvx", args=["awslabs.aws-documentation-mcp-server@latest"])))
with client:
    agent = Agent(tools=client.list_tools_sync())
    agent("Tell me about Amazon Bedrock")
```
(../../raw/github/strands-agents-sdk-python.md)

## When to use

Strands Agents suits teams building production AI agents that need end-to-end control without framework lock-in, especially when:
- Running on AWS / Amazon Bedrock (native integration, IAM credentials, Bedrock Guardrails).
- Requiring fine-grained tool-call interception (hooks, steering) for safety or compliance.
- Needing multi-agent patterns (Graph/Swarm/Workflow) without a separate orchestration layer.
- Wanting a single codebase that works locally (Ollama, llama.cpp) and in production (Bedrock, OpenAI) by swapping the model parameter.

## Maintenance status

5,910 stars, 844 forks, Apache 2.0 license, released by AWS. Latest: v1.40.0 (2026-05-15). Active development with monthly releases. Enterprise adoption at Smartsheet, Swisscom, Eightcap, Zafran Security, Verisk Analytics, and others. (../../raw/github/strands-agents-sdk-python.md)

## Ecosystem

- **Python SDK** — `strands-agents` (PyPI) / `strands-agents/sdk-python` (GitHub) — primary SDK
- **TypeScript SDK** — `@strands-agents/sdk` (npm) / `strands-agents/sdk-typescript` — TypeScript parity (most features, no Ollama/LiteLLM/bidirectional streaming)
- **Community tools** — `strands-agents-tools` (PyPI) / `strands-agents/tools` — 30+ pre-built tools
- **MCP server** — `strands-agents/mcp-server` — IDE assistant for Kiro, Cursor, Claude Code, Cline
- **Agent Builder** — `strands-agents/agent-builder` — meta-agent that helps build Strands agents
- **Samples** — `strands-agents/samples` — reference implementations
- **AgentCore Runtime** (AWS) — managed deployment target for Strands agents on AWS infrastructure
