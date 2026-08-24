---
type: source
category: "Agent frameworks & SDKs"
source_url: https://github.com/anthropics/claude-agent-sdk-python
tags:
  - claude-code
  - agent-sdk
  - python-sdk
  - mcp-servers
  - in-process-tools
  - hooks
  - async-python
  - claude-agent
related:
  - anthropic.com
  - anthropic.com-managed-agents
  - anthropic.com-messages
  - anthropics-skills
  - deepseek-ai-deepseek-harness
product: claude-agent-sdk-python
detail_level: standard
created: 2026-08-17
updated: 2026-08-24
---

The Claude Agent SDK for Python is Anthropic's official library for programmatically embedding Claude Code (the agentic coding tool) as a library inside Python applications, scripts, and multi-agent systems — turning a CLI-driven tool into a composable, async-native SDK. It ships with the Claude Code CLI bundled inside the pip package, requiring zero separate installation, and exposes two primary interfaces: the `query()` fire-and-forget async iterator for one-shot tasks and the `ClaudeSDKClient` class for interactive, bidirectional, multi-turn conversations. Its standout capability is **in-process MCP servers**: rather than launching a separate subprocess per tool, custom Python functions can be registered as SDK MCP servers that run in the same process, eliminating IPC overhead and subprocess management.

_All claims below are sourced from ../../raw/github/anthropics-claude-agent-sdk-python.md unless otherwise noted._

## What it does

The SDK wraps Claude Code in a Python-native async API so that developers can automate, orchestrate, and extend Claude's agentic capabilities from within their own code. The `query()` function streams back an `AsyncIterator[Message]` — `AssistantMessage`, `UserMessage`, `SystemMessage`, and `ResultMessage` — for simple scripting. The `ClaudeSDKClient` context manager enables full interactive control: sending follow-up prompts, registering custom tools as in-process MCP servers, and attaching hooks that fire at named lifecycle points (`PreToolUse`, etc.) to intercept, approve, or block tool calls without leaving the Python process.

## Key features

- **Bundled CLI**: `pip install claude-agent-sdk` ships the Claude Code CLI inside the wheel — no external dependency.
- **`query()` async iterator**: one-shot prompt → streaming `Message` responses; configurable via `ClaudeAgentOptions` (system prompt, max turns, cwd, allowed/disallowed tools, permission mode).
- **`ClaudeSDKClient`**: full bidirectional session; supports `await client.query(...)` + `async for msg in client.receive_response()` for multi-turn conversations.
- **SDK MCP servers (`create_sdk_mcp_server`)**: register Python `@tool`-decorated async functions as named MCP servers using `ClaudeAgentOptions(mcp_servers={"name": server})`; no subprocess needed.
- **Hooks system**: attach async Python callbacks to lifecycle events (`PreToolUse`) via `HookMatcher`; hook can approve, deny, or modify tool calls deterministically before Claude's response.
- **Tool permission model**: `allowed_tools` is an auto-approval allowlist (does not remove tools); `disallowed_tools` blocks tools entirely; `permission_mode` and `can_use_tool` callback handle the fallthrough decision.
- **Mixed MCP support**: SDK in-process servers and external stdio MCP servers can coexist in the same `mcp_servers` dict.

## Architecture

The package lives under `src/claude_agent_sdk/` with these key modules: `query.py` (one-shot function), `client.py` (interactive client), `types.py` (full type hierarchy), `_errors.py` (error hierarchy), and `_internal/transport/subprocess_cli.py` (CLI subprocess management and JSON-stream parsing). The bundled CLI binary is stored in `_bundled/`. A `testing/` subpackage provides test helpers and mocks. End-to-end tests live in `e2e-tests/`; unit tests in `tests/`. The `examples/` directory contains a rich set of runnable examples covering hooks, MCP calculator, streaming, plugins, session stores, and tool permission callbacks.

## Installation

```bash
pip install claude-agent-sdk  # Python 3.10+; Claude Code CLI bundled
```

To use a specific CLI path: `ClaudeAgentOptions(cli_path="/path/to/claude")`.

## Example usage

```python
import anyio
from claude_agent_sdk import query

async def main():
    async for message in query(prompt="What is 2 + 2?"):
        print(message)

anyio.run(main)
```

Custom in-process tool:

```python
from claude_agent_sdk import tool, create_sdk_mcp_server, ClaudeAgentOptions, ClaudeSDKClient

@tool("greet", "Greet a user", {"name": str})
async def greet_user(args):
    return {"content": [{"type": "text", "text": f"Hello, {args['name']}!"}]}

server = create_sdk_mcp_server(name="my-tools", version="1.0.0", tools=[greet_user])
options = ClaudeAgentOptions(mcp_servers={"tools": server}, allowed_tools=["mcp__tools__greet"])

async with ClaudeSDKClient(options=options) as client:
    await client.query("Greet Alice")
    async for msg in client.receive_response():
        print(msg)
```

## Maintenance status

7,905 stars, MIT license, latest release v0.2.139 (2026-08-14), actively maintained by Anthropic with frequent patch releases. Migrated from the earlier `claude-code-sdk` package (versions < 0.1.0), renaming `ClaudeCodeOptions` → `ClaudeAgentOptions` and introducing programmatic subagents and session forking in v0.1.0.

## Ecosystem

Builds on top of [[anthropic.com-managed-agents]] (the hosted managed-agent harness) and [[anthropic.com-messages]] (the underlying Messages API). The in-process MCP server pattern complements [[obra-superpowers]]'s skills system and any framework that can host MCP tools. Compared to [[coleam00-archon]] (an agent-builder UI for constructing and deploying agents), the SDK targets developers who want programmatic, library-level control rather than a visual or config-driven approach.
