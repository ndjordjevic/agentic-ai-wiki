# anthropics/claude-agent-sdk-python

## Metadata
- Stars: 7905
- Primary language: Python
- Default branch: main
- Latest release: v0.2.139 (2026-08-14)
- License: MIT License
- Homepage: https://platform.claude.com/docs/en/agent-sdk/python
- Fetched: 2026-08-17
- Final URL: https://github.com/anthropics/claude-agent-sdk-python

## Description
Python SDK for Claude Agent. The official SDK for programmatically controlling Claude Code (Claude's agentic coding tool), enabling developers to embed Claude Code as a library in their own applications, scripts, and agents.

## README
# Claude Agent SDK for Python

Python SDK for Claude Agent. See the [Claude Agent SDK documentation](https://platform.claude.com/docs/en/agent-sdk/python) for more information.

## Installation

```bash
pip install claude-agent-sdk
```

**Prerequisites:**

- Python 3.10+

**Note:** The Claude Code CLI is automatically bundled with the package - no separate installation required! The SDK will use the bundled CLI by default. If you prefer to use a system-wide installation or a specific version, you can:

- Install Claude Code separately: `curl -fsSL https://claude.ai/install.sh | bash`
- Specify a custom path: `ClaudeAgentOptions(cli_path="/path/to/claude")`

## Quick Start

```python
import anyio
from claude_agent_sdk import query

async def main():
    async for message in query(prompt="What is 2 + 2?"):
        print(message)

anyio.run(main)
```

## Basic Usage: query()

`query()` is an async function for querying Claude Code. It returns an `AsyncIterator` of response messages. See [src/claude_agent_sdk/query.py](src/claude_agent_sdk/query.py).

```python
from claude_agent_sdk import query, ClaudeAgentOptions, AssistantMessage, TextBlock

# Simple query
async for message in query(prompt="Hello Claude"):
    if isinstance(message, AssistantMessage):
        for block in message.content:
            if isinstance(block, TextBlock):
                print(block.text)

# With options
options = ClaudeAgentOptions(
    system_prompt="You are a helpful assistant",
    max_turns=1
)

async for message in query(prompt="Tell me a joke", options=options):
    print(message)
```

### Using Tools

By default, Claude has access to the full [Claude Code toolset](https://code.claude.com/docs/en/settings#tools-available-to-claude) (Read, Write, Edit, Bash, and others). `allowed_tools` is a permission allowlist: listed tools are auto-approved, and unlisted tools fall through to `permission_mode` and `can_use_tool` for a decision. It does not remove tools from Claude's toolset. To block specific tools, use `disallowed_tools`. See the [permissions guide](https://platform.claude.com/docs/en/agent-sdk/permissions) for the full evaluation order.

```python
options = ClaudeAgentOptions(
    allowed_tools=["Read", "Write", "Bash"],  # auto-approve these tools
    permission_mode='acceptEdits'  # auto-accept file edits
)

async for message in query(
    prompt="Create a hello.py file",
    options=options
):
    # Process tool use and results
    pass
```

### Working Directory

```python
from pathlib import Path

options = ClaudeAgentOptions(
    cwd="/path/to/project"  # or Path("/path/to/project")
)
```

## ClaudeSDKClient

`ClaudeSDKClient` supports bidirectional, interactive conversations with Claude Code. Unlike `query()`, `ClaudeSDKClient` additionally enables **custom tools** and **hooks**, both of which can be defined as Python functions.

### Custom Tools (as In-Process SDK MCP Servers)

A **custom tool** is a Python function that you can offer to Claude, for Claude to invoke as needed. Custom tools are implemented as in-process MCP servers that run directly within your Python application, eliminating the need for separate processes.

```python
from claude_agent_sdk import tool, create_sdk_mcp_server, ClaudeAgentOptions, ClaudeSDKClient

@tool("greet", "Greet a user", {"name": str})
async def greet_user(args):
    return {
        "content": [
            {"type": "text", "text": f"Hello, {args['name']}!"}
        ]
    }

server = create_sdk_mcp_server(
    name="my-tools",
    version="1.0.0",
    tools=[greet_user]
)

options = ClaudeAgentOptions(
    mcp_servers={"tools": server},
    allowed_tools=["mcp__tools__greet"]
)

async with ClaudeSDKClient(options=options) as client:
    await client.query("Greet Alice")
    async for msg in client.receive_response():
        print(msg)
```

### Benefits Over External MCP Servers

- No subprocess management — runs in the same process
- Better performance — no IPC overhead for tool calls
- Simpler deployment — single Python process
- Easier debugging — all code in the same process
- Type safety — direct Python function calls with type hints

### Hooks

A **hook** is a Python function invoked by the Claude Code application (not Claude) at specific points of the agent loop. Hooks can provide deterministic processing and automated feedback.

```python
from claude_agent_sdk import ClaudeAgentOptions, ClaudeSDKClient, HookMatcher

async def check_bash_command(input_data, tool_use_id, context):
    tool_name = input_data["tool_name"]
    tool_input = input_data["tool_input"]
    if tool_name != "Bash":
        return {}
    command = tool_input.get("command", "")
    block_patterns = ["foo.sh"]
    for pattern in block_patterns:
        if pattern in command:
            return {
                "hookSpecificOutput": {
                    "hookEventName": "PreToolUse",
                    "permissionDecision": "deny",
                    "permissionDecisionReason": f"Command contains invalid pattern: {pattern}",
                }
            }
    return {}

options = ClaudeAgentOptions(
    allowed_tools=["Bash"],
    hooks={
        "PreToolUse": [
            HookMatcher(matcher="Bash", hooks=[check_bash_command]),
        ],
    }
)
```

## Types

Key types in `src/claude_agent_sdk/types.py`:

- `ClaudeAgentOptions` — Configuration options (system_prompt, max_turns, allowed_tools, disallowed_tools, permission_mode, cwd, mcp_servers, hooks, cli_path)
- `AssistantMessage`, `UserMessage`, `SystemMessage`, `ResultMessage` — Message types
- `TextBlock`, `ToolUseBlock`, `ToolResultBlock` — Content blocks

## Error Handling

```python
from claude_agent_sdk import (
    ClaudeSDKError,      # Base error
    CLINotFoundError,    # Claude Code not installed
    CLIConnectionError,  # Connection issues
    ProcessError,        # Process failed
    CLIJSONDecodeError,  # JSON parsing issues
)
```

## Top-level structure

```
.claude/           — Agent instruction files for the repo itself
CHANGELOG.md       — Detailed version history with breaking changes
CLAUDE.md          — Development workflow: lint (ruff), typecheck (mypy), test (pytest)
Dockerfile.test    — Docker test environment
e2e-tests/         — End-to-end tests
examples/          — Rich example set (quick_start, streaming_mode, hooks, mcp_calculator, agents, plugins, session_stores, etc.)
pyproject.toml     — Package manifest, dependencies (anyio, trio support)
scripts/           — Initial-setup and helper scripts
src/
  claude_agent_sdk/
    __init__.py          — Public API exports
    client.py            — ClaudeSDKClient (interactive, multi-turn)
    query.py             — query() one-shot async function
    types.py             — All type definitions
    _errors.py           — Error hierarchy
    _internal/
      transport/
        subprocess_cli.py — CLI subprocess management, JSON stream parsing
      message_parser.py   — Message parsing logic
    _bundled/            — Bundled Claude Code CLI binary
    testing/             — Test helpers/mocks
tests/             — Unit tests
```
