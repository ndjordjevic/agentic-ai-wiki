---
type: source
category: "MCP servers & integrations"
source_url: https://github.com/modelcontextprotocol/servers/tree/main/src/sequentialthinking
tags:
  - mcp-server
  - sequential-thinking
  - reasoning-tool
  - claude-desktop
  - vscode-mcp
  - codex-cli
related:
  - canva.com
  - zilliztech-claude-context
  - microsoft-playwright-mcp
product: sequentialthinking-mcp
detail_level: brief
created: 2026-04-28
updated: 2026-05-25
---

The Sequential Thinking MCP Server is a focused Model Context Protocol server that exposes one tool, `sequential_thinking`, for stepwise, revisable, branching reasoning inside an MCP-aware host. This source matters because it shows a concrete pattern for packaging deliberation support as a reusable MCP capability rather than as a full agent framework, and it documents how that capability is installed across Claude Desktop, VS Code, and Codex CLI.

_All claims below are sourced from ../../raw/web/sequentialthinking-mcp.md unless otherwise noted._

## What it does

The page describes an MCP server whose purpose is dynamic and reflective problem-solving through a structured thinking process. Rather than exposing a broad suite of tools, it centers on one reasoning-oriented capability that lets a host break a problem into numbered thoughts, continue when more steps are needed, and revise or branch when understanding changes.

## Key features

- Breaks complex problems into smaller thought steps.
- Supports revision as understanding deepens.
- Supports branching into alternative reasoning paths.
- Lets the model adjust the expected number of thoughts dynamically.
- Encourages hypothesis generation and verification during problem-solving.

## Architecture and concepts

The core conceptual design is a single MCP tool named `sequential_thinking`. The host remains in control of when and how often the tool is called, while the tool call payload carries the evolving reasoning state through fields such as the current thought text, the current thought number, the estimated total number of thoughts, and whether another thought is needed.

The page also makes the server's revision model explicit. Optional fields like `isRevision`, `revisesThought`, `branchFromThought`, `branchId`, and `needsMoreThoughts` let the reasoning process revisit earlier steps, split into parallel branches, and extend beyond the initial estimate when the problem turns out to be larger than expected.

## Main APIs

The documented interface is the `sequential_thinking` tool. Its required inputs are `thought`, `nextThoughtNeeded`, `thoughtNumber`, and `totalThoughts`. Optional inputs are `isRevision`, `revisesThought`, `branchFromThought`, `branchId`, and `needsMoreThoughts`.

Operationally, the page treats MCP host configuration as part of the public interface. It provides concrete setup snippets for Claude Desktop, VS Code, and Codex CLI, with NPX and Docker variants, plus a `DISABLE_THOUGHT_LOGGING=true` environment variable for disabling thought logging.

## When to use

- Complex problems that benefit from explicit decomposition into steps.
- Planning and design work where the reasoning may need revision.
- Investigations or debugging sessions that may need course correction.
- Problems where the full scope is unclear at the start.
- Tasks where a host should preserve and inspect multi-step reasoning state.

## Ecosystem

The page situates the server inside the broader MCP host ecosystem rather than as a standalone app. It documents installation paths for Claude Desktop, VS Code, and Codex CLI, provides both NPX and Docker-based setup patterns, includes a Docker build command for the image, and states that the server is released under the MIT License.
