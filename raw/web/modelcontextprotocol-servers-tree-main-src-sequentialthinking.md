# modelcontextprotocol-servers-tree-main-src-sequentialthinking

## Fetch log
- Inbox URL: https://github.com/modelcontextprotocol/servers/tree/main/src/sequentialthinking
- Final URL: https://github.com/modelcontextprotocol/servers/tree/main/src/sequentialthinking
- Fetched: 2026-04-28
- Pages: 1

## Page — https://github.com/modelcontextprotocol/servers/tree/main/src/sequentialthinking
## Sequential Thinking MCP Server

An MCP server implementation that provides a tool for dynamic and reflective problem-solving through a structured thinking process.

## Features

- Break down complex problems into manageable steps
- Revise and refine thoughts as understanding deepens
- Branch into alternative paths of reasoning
- Adjust the total number of thoughts dynamically
- Generate and verify solution hypotheses

## Tool

### sequential_thinking

Facilitates a detailed, step-by-step thinking process for problem-solving and analysis.

**Inputs:**

- `thought` (string): The current thinking step
- `nextThoughtNeeded` (boolean): Whether another thought step is needed
- `thoughtNumber` (integer): Current thought number
- `totalThoughts` (integer): Estimated total thoughts needed
- `isRevision` (boolean, optional): Whether this revises previous thinking
- `revisesThought` (integer, optional): Which thought is being reconsidered
- `branchFromThought` (integer, optional): Branching point thought number
- `branchId` (string, optional): Branch identifier
- `needsMoreThoughts` (boolean, optional): If more thoughts are needed

## Usage

The Sequential Thinking tool is designed for:

- Breaking down complex problems into steps
- Planning and design with room for revision
- Analysis that might need course correction
- Problems where the full scope might not be clear initially
- Tasks that need to maintain context over multiple steps
- Situations where irrelevant information needs to be filtered out

In practice, you do not call `sequential_thinking` directly by hand unless your client exposes raw tool calls. Instead, connect the server to an MCP-aware host and ask the model to think through a problem step by step. The host can then decide to call the tool one or more times while it works.

### What it looks like in use

Example prompts that typically benefit from this tool:

- `Plan a database migration from PostgreSQL 14 to 16, list risks, and revise the plan if downtime exceeds 5 minutes.`
- `Debug why this deployment only fails in production and show your reasoning step by step.`
- `Compare three architecture options for a file sync engine and branch if one assumption turns out to be wrong.`

### How to tell it is working

If your host or inspector shows tool activity, you should see repeated calls to `sequential_thinking` with fields such as:

- `thought`
- `thoughtNumber`
- `totalThoughts`
- `nextThoughtNeeded`

When the reasoning changes course, you may also see revision or branching fields like `isRevision`, `revisesThought`, `branchFromThought`, or `branchId`.

### Quick manual verification

After installing the server in your MCP host:

1. Restart or reload the host so it reconnects to the server.
2. Confirm the `sequential_thinking` tool appears in the host's MCP tool list or inspector.
3. Ask the host to solve a non-trivial problem in a step-by-step way.
4. Verify that the host invokes the tool multiple times instead of returning a one-shot answer.

## Configuration

### Usage with Claude Desktop

Add this to your `claude_desktop_config.json`:

#### npx

```json
{
  "mcpServers": {
    "sequential-thinking": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-sequential-thinking"
      ]
    }
  }
}
```

On Windows, use `cmd /c` to launch `npx`:

```json
{
  "mcpServers": {
    "sequential-thinking": {
      "command": "cmd",
      "args": [
        "/c",
        "npx",
        "-y",
        "@modelcontextprotocol/server-sequential-thinking"
      ]
    }
  }
}
```

#### docker

```json
{
  "mcpServers": {
    "sequentialthinking": {
      "command": "docker",
      "args": [
        "run",
        "--rm",
        "-i",
        "mcp/sequentialthinking"
      ]
    }
  }
}
```

To disable logging of thought information set env var `DISABLE_THOUGHT_LOGGING` to `true`.

### Usage with VS Code

For manual installation, add the server to user-level MCP configuration via `MCP: Open User Configuration`, or to workspace `.vscode/mcp.json`.

For NPX installation:

```json
{
  "servers": {
    "sequential-thinking": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-sequential-thinking"
      ]
    }
  }
}
```

On Windows, use:

```json
{
  "servers": {
    "sequential-thinking": {
      "command": "cmd",
      "args": [
        "/c",
        "npx",
        "-y",
        "@modelcontextprotocol/server-sequential-thinking"
      ]
    }
  }
}
```

For Docker installation:

```json
{
  "servers": {
    "sequential-thinking": {
      "command": "docker",
      "args": [
        "run",
        "--rm",
        "-i",
        "mcp/sequentialthinking"
      ]
    }
  }
}
```

### Usage with Codex CLI

Run the following:

#### npx

```bash
codex mcp add sequential-thinking npx -y @modelcontextprotocol/server-sequential-thinking
```

## Building

Docker:

```bash
docker build -t mcp/sequentialthinking -f src/sequentialthinking/Dockerfile .
```

## License

This MCP server is licensed under the MIT License. This means you are free to use, modify, and distribute the software, subject to the terms and conditions of the MIT License. For more details, please see the LICENSE file in the project repository.
