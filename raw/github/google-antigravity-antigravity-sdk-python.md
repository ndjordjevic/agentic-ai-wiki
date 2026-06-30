# google-antigravity/antigravity-sdk-python

## Metadata
- Stars: 2118
- Primary language: Python
- Default branch: main
- Latest release: (see PyPI v0.1.4, 2026-06-18)
- License: Apache License 2.0
- Homepage: https://antigravity.google/product/antigravity-sdk
- Fetched: 2026-06-30
- Final URL: https://github.com/google-antigravity/antigravity-sdk-python

## Description
A Python library for building AI agents that leverage the full power of Google Antigravity.

## README

# Google Antigravity SDK

The Google Antigravity SDK is a Python SDK for building AI agents powered by
Antigravity and Gemini. It provides a secure, scalable, and stateful
infrastructure layer that abstracts the agentic loop, letting you focus on what
your agent *does* rather than how it runs.

## Installation

```sh
pip install google-antigravity
```

> [!IMPORTANT]
> The Google Antigravity SDK relies on a compiled runtime binary that is
> included in the platform-specific wheels published to
> [PyPI](https://pypi.org/project/google-antigravity/). **Cloning this
> repository alone is not sufficient to run the SDK.** Always install from
> PyPI with `pip install google-antigravity` to obtain the binary.

## Quickstart

```sh
export GEMINI_API_KEY="your_api_key_here"
python ./examples/getting_started/hello_world.py
```

## Gemini Enterprise Agent Platform (Vertex AI)

```python
from google.antigravity import Agent, LocalAgentConfig

config = LocalAgentConfig(
    vertex=True,
    project="your-gcp-project",
    location="us-central1",
)
async with Agent(config) as agent:
    response = await agent.chat("Hello!")
```

Authenticate with `gcloud auth application-default login` (ADC).

## Architecture (three layers)

| Layer | Purpose | Key Classes |
|:------|:--------|:------------|
| **Layer 1** — Simplified | High-level entry point | `Agent` |
| **Layer 2** — Session | Stateful session, history | `Conversation`, `ChatResponse`, `Step`, `ToolCall`, `AgentConfig`, `HookRunner`, `ToolRunner`, `TriggerRunner` |
| **Layer 3** — Adapter | Transport/backend abstraction | `Connection`, `ConnectionStrategy`, `LocalConnection` |

## Features (from README)

- **Agent** — async context manager; manages binary discovery, tool wiring, hooks, policy defaults
- **Streaming** — `async for token in response`; `response.thoughts` and `response.tool_calls` streams
- **Multimodal** — `Image`, `from_file()`, mixed prompt lists
- **Custom tools** — register Python callables via `LocalAgentConfig(tools=[...])`
- **MCP** — `McpStdioServer`, SSE, Streamable HTTP
- **Hooks & policies** — `deny`, `allow`, `ask_user`, `enforce`; nine hook points with decorators
- **Triggers** — `every(60, callback)` background tasks via `TriggerRunner`
- **Sub-agents** — child agents with independent tools/instructions
- **Structured output** — Pydantic/JSON schema validation
- **Interactive loop** — `run_interactive_loop(config)`
- **Conversation** — low-level `LocalConnectionStrategy` + step history

Default read-only mode for safety; `capabilities=CapabilitiesConfig()` enables writes.

## Examples

### getting_started/
hello_world, streaming, multimodal, custom_tools, mcp_tools, hooks, policies, subagents, triggers, structured_output, human_in_the_loop, observability, persistence, agent_skills, slash_commands, web_tools, autonomous_shell, cancellation, error_handler, persona_config, app_data_dir_override

### deep_dives/
agent_middleware, async_chat, doc_maintenance_agent, docstring_maintenance_agent, host_tool_hooks, interactive_cli, multimodal_pipeline, observability_otel, round_based_chat

## Top-level structure

| Path | Purpose |
|---|---|
| `google/` | SDK package (agent, connections, conversation, hooks, mcp, tools, triggers) |
| `examples/` | getting_started/ and deep_dives/ example scripts |
| `skills/` | SDK skill packages |
| `pyproject.toml` | Package metadata |
| `.github/` | CI workflows |

## Component docs (in-repo)
- `google/antigravity/agent.py`
- `google/antigravity/connections/README.md`
- `google/antigravity/conversation/README.md`
- `google/antigravity/hooks/README.md`
- `google/antigravity/mcp/README.md`
- `google/antigravity/tools/README.md`
- `google/antigravity/triggers/README.md`
