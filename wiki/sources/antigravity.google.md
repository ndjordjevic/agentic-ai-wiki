---
type: source
source_url: https://antigravity.google/product/antigravity-sdk
companion_urls:
  - https://github.com/google-antigravity/antigravity-sdk-python
raw_files:
  - ../../raw/web/antigravity.google.md
  - ../../raw/github/google-antigravity-antigravity-sdk-python.md
tags:
  - antigravity-sdk
  - google-antigravity
  - gemini
  - agent-runtime
  - mcp
  - agent-skills
  - safety-policies
  - multimodal-agents
related:
  - agents-cli
  - adk.dev
  - x.com-ericzakariasson-building-clis-for-agents
  - skills.sh
  - langchain.com-deepagents
  - pi.dev
  - the-new-sdlc-with-vibe-coding
product: antigravity-sdk
detail_level: standard
created: 2026-06-30
updated: 2026-06-30
---

The **Google Antigravity SDK** (`google-antigravity` on PyPI) is a Python library that exposes the same agent runtime powering Antigravity 2.0 and the Antigravity CLI — file I/O, code editing, shell execution, MCP, skills, safety policies, hooks, sub-agents, and stateful sessions — as programmable infrastructure for custom agentic applications. It is a tool *for building agents*, not a coding agent itself; most developers need only `Agent` + `LocalAgentConfig` in an async `with` block. The product page and companion repo (`google-antigravity/antigravity-sdk-python`, 2.1k+ stars, Apache 2.0) document operator positioning and API/examples respectively. (../../raw/github/google-antigravity-antigravity-sdk-python.md)

_All claims below are sourced from ../../raw/web/antigravity.google.md unless otherwise noted._

## What it does

The SDK abstracts the agentic loop — state management, tool execution, backend communication, context compaction — so developers focus on agent behavior. Agents inherit Antigravity's built-in toolset and can be extended with custom Python functions, MCP servers (stdio/SSE/HTTP), and agent skills (`skills_paths`). Logic is decoupled from execution location: build locally today; remote harness on Google Cloud (Interactions API) is on the roadmap.

Runs against Gemini via `GEMINI_API_KEY` or Gemini Enterprise Agent Platform / Vertex AI (`LocalAgentConfig(vertex=True, project=..., location=...)` with ADC). Default model is Gemini 3.5 Flash. **Critical install note:** the SDK requires a compiled runtime binary shipped in PyPI wheels — cloning the GitHub repo alone is insufficient; always `pip install google-antigravity`.

## Key features

**Unified tool pipeline** — four tool sources share one execution pipeline, streaming infrastructure, and safety policies:
1. Built-in tools (file I/O, code editing, shell, directory search, image generation, sub-agent delegation)
2. Custom Python callables
3. MCP servers
4. Agent skills packages

**Declarative safety policies** — `LocalAgentConfig` enables builtins but applies `confirm_run_command()` by default (shell denied unless approved). Fully autonomous: `policies=[policy.allow_all()]`. Fine-grained: `deny("*")`, `allow("view_file")`, `ask_user("run_command")`.

**Lifecycle hooks** (nine points) in three categories:
- **Inspect** — read-only logging/metrics/audit
- **Decide** — blocking approve/deny (policies built on this)
- **Transform** — modify data in transit, error recovery

**I/O and execution:**
- Streaming output and model reasoning (`async for chunk in response`, `response.thoughts`, `response.tool_calls`)
- Multimodal prompts (images, PDFs, audio, video via `from_file()` or content classes)
- Sub-agents with independent tools/instructions/contexts
- Thinking levels per request: `MINIMAL`, `LOW`, `MEDIUM`, `HIGH`
- Triggers for background event-driven tasks (`every(60, callback)`)

**State and control:**
- Session persistence via `conversation_id`
- Structured output (Pydantic/JSON schema → `response.structured_output()`)
- Human-in-the-loop with structured questions and branching

**Observability:** per-turn and cumulative token usage (`usage_metadata`); reasoning/thinking traces.

**Three-layer API:** Layer 1 `Agent` (batteries-included) → Layer 2 `Conversation`/`ChatResponse`/`Step` → Layer 3 `Connection`/`ConnectionStrategy`. (../../raw/github/google-antigravity-antigravity-sdk-python.md)

## Architecture

Same harness as Antigravity 2.0 and CLI — hooks, sub-agents, and policies configured in code instead of UI. Research preview (pre-v1.0); runtime improvements upstream flow to SDK agents automatically.

Component modules: `agent`, `connections`, `conversation`, `hooks`, `mcp`, `tools`, `triggers`. Examples split into `getting_started/` (20+ single-feature scripts) and `deep_dives/` (middleware, OTel observability, doc maintenance agents, interactive CLI, multimodal pipelines). (../../raw/github/google-antigravity-antigravity-sdk-python.md)

## Installation

```bash
pip install google-antigravity
export GEMINI_API_KEY="your_api_key_here"
python ./examples/getting_started/hello_world.py
```

Requirements: Python ≥3.10. PyPI package `google-antigravity` (alpha, Apache 2.0). For Vertex: `gcloud auth application-default login`. Platform wheels include the compiled runtime binary. (../../raw/github/google-antigravity-antigravity-sdk-python.md)

## Example usage

**Minimal agent:**

```python
import asyncio
from google.antigravity import Agent, LocalAgentConfig

async def main():
    config = LocalAgentConfig()
    async with Agent(config) as agent:
        response = await agent.chat("What files are in the current directory?")
        print(await response.text())

asyncio.run(main())
```

**Custom tool + policies:**

```python
def get_weather(city: str) -> str:
    return f"It's sunny in {city}."

config = LocalAgentConfig(tools=[get_weather])
```

**MCP integration:**

```python
from google.antigravity.types import McpStdioServer
config = LocalAgentConfig(
    mcp_servers=[McpStdioServer(name="my_server", command="npx", args=["my-mcp-server"])],
)
```

**Interactive REPL:** `run_interactive_loop(config)` with `CapabilitiesConfig()` for write access. (../../raw/github/google-antigravity-antigravity-sdk-python.md)

## When to use

- You want programmatic access to Antigravity's agent runtime (same tools/loop as CLI and 2.0) inside your own Python apps.
- You need governed extensibility: MCP + skills + custom tools under one policy engine.
- You're building multimodal agents, sub-agent teams, triggered background agents, or structured-output pipelines on Gemini.
- You plan to migrate local SDK agents to cloud-hosted harness (roadmap).
- **Not the right fit** if you need a terminal coding agent (use Antigravity CLI), a GUI manager (use Antigravity 2.0), or ADK/GCP deployment lifecycle (use [[agents-cli]]). Repo clone without PyPI install won't run.

## Maintenance status

Actively developed preview: GitHub 2,118 stars, 745 forks, last push 2026-06-25, Apache 2.0. PyPI releases through v0.1.4 (2026-06-18). Research preview seeking feedback. Roadmap: remote GCP harness, TypeScript/Go SDKs, Gemma support, plugins, deeper observability. (../../raw/github/google-antigravity-antigravity-sdk-python.md)

## Ecosystem

- **Antigravity platform** — SDK sits alongside Antigravity 2.0 (agent manager GUI), Antigravity IDE (editor), and Antigravity CLI (terminal); all share the same runtime primitives.
- **[[agents-cli]]** — complementary Google tool for coding agents building ADK agents on GCP; agents-cli lists Antigravity CLI as a supported host.
- **MCP and skills** — first-class extension paths; platform docs cover MCP/skills for CLI/IDE; SDK loads skills via `skills_paths`.
- **Gemini Enterprise / Vertex AI** — enterprise auth and hosting path via `vertex=True`.
- **PyPI:** `google-antigravity` · **Docs:** [antigravity.google/docs/sdk/overview](https://antigravity.google/docs/sdk/overview)

## Documentation

Official docs: SDK overview (core pillars, quick start, capabilities). Blog: [Introducing Google Antigravity SDK](https://antigravity.google/blog/introducing-google-antigravity-sdk). Platform use-case pages (enterprise, frontend, fullstack, science, marketer) describe workloads the broader Antigravity stack targets — browser-in-the-loop UI testing, artifact verification, science database skills (AlphaGenome, AlphaFold, UniProt, etc.), scheduled marketing audits. Full API surface documented in-repo and via examples.
