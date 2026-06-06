---
type: source
source_url: https://github.com/eyaltoledano/claude-task-master
tags:
  - ai-task-management
  - prd-to-tasks
  - mcp-integration
  - open-source
  - task-dependencies
  - multi-model
  - cli-tool
  - agent-workflow
related:
  - www.taskmaster.one
  - anombyte93-prd-taskmaster
  - vibekanban.com
  - gsd-build-get-shit-done
  - backnotprop-plannotator
  - buildermethods-agent-os
  - tryhamster.com
product: claude-task-master
detail_level: standard
created: 2026-05-25
updated: 2026-05-25
---

Taskmaster (`claude-task-master`, npm: `task-master-ai`) is an open-source AI-powered task management system by @eyaltoledano and @RalphEcom with 27,000+ stars, designed to work seamlessly with any AI chat interface or coding agent. It converts Product Requirements Documents into structured, dependency-aware task graphs and exposes them through a CLI and MCP server — making it a drop-in planning layer for Cursor, Lovable, Windsurf, Roo, and other AI-driven editors. The project is now maintained under the Hamster platform at [[tryhamster.com]], with full Taskmaster documentation on [[tryhamster.com]].

_All claims below are sourced from ../../raw/github/eyaltoledano-claude-task-master.md unless otherwise noted._

## What it does

Taskmaster takes a PRD (`.taskmaster/docs/prd.txt` or `scripts/prd.txt`) and generates a structured task graph stored in the repository as JSON. Tasks include IDs, titles, descriptions, statuses, priorities, dependency lists, detailed implementation notes, and test strategies. The system then provides AI-assisted commands to navigate the task graph: finding the next unblocked task, expanding complex tasks into subtasks using AI, researching external information with project context, and moving tasks between tagged workstreams. All operations work through CLI or through MCP tools exposed to the editor's AI chat.

## Installation

**Via MCP (recommended):**
```json
{
  "mcpServers": {
    "task-master-ai": {
      "command": "npx",
      "args": ["-y", "task-master-ai"],
      "env": {
        "ANTHROPIC_API_KEY": "YOUR_KEY_HERE",
        "OPENAI_API_KEY": "YOUR_KEY_HERE"
      }
    }
  }
}
```

**Claude Code:**
```bash
claude mcp add taskmaster-ai -- npx -y task-master-ai
```

**Via CLI:**
```bash
npm install -g task-master-ai
task-master init
```

At least one API key is required (Anthropic, OpenAI, Gemini, Perplexity, xAI, OpenRouter, or use Claude Code/Codex CLI with OAuth — no API key needed).

## Key features

- **PRD parsing** — `task-master parse-prd <file>` generates a complete task graph from a requirements document.
- **Dependency-aware task navigation** — `task-master next` identifies the highest-priority task with all dependencies met.
- **Complexity analysis** — `task-master analyze-complexity` scores each task 1–10 and generates AI tailored subtask-expansion prompts; report saved to `scripts/task-complexity-report.json`.
- **Smart task expansion** — `task-master expand --id=<n>` uses the complexity report to auto-expand tasks into the recommended number of subtasks.
- **Research mode** — `task-master research "<query>"` fetches fresh external information grounded in the project's existing codebase and task context.
- **Tags & workstreams** — Tasks live in named tag namespaces (default: `master`); `task-master move` shifts tasks between tags (e.g., `backlog` → `in-progress` → `done`).
- **Loop (automation)** — `task-master loop` command for continuous autonomous task execution.
- **Multi-model roles** — Separate model slots for main, research, and fallback; model per role is configured in `.taskmaster/config.json`.
- **36 MCP tools** — Configurable tool loading via `TASK_MASTER_TOOLS` env var (`core` = 7 tools, `standard` = 15, `all` = 36).

## Architecture

Taskmaster is structured as a JavaScript monorepo (Turborepo):

- **`src/`** — Core logic: task parsing, AI providers, dependency resolution, complexity analysis
- **`mcp-server/`** — MCP server implementation exposing task operations as tools
- **`packages/`** — Shared utilities (monorepo)
- **`apps/`** — Application packages
- **`bin/`** — CLI entrypoints (`task-master` binary)
- **`docs/`** — Documentation: command reference, configuration guide, task structure spec, models table, tutorial, examples, MCP provider guide, migration guide
- **`.taskmaster/`** — The project's own Taskmaster config (dogfooding)

Configuration lives in `.taskmaster/config.json` (created by `task-master init` or `task-master models --setup`). Three model roles are configured: `main`, `research`, `fallback`. The config supports per-provider base URLs (for Azure, Ollama, Vertex AI).

MCP tool loading is optimized via `TASK_MASTER_TOOLS` environment variable to reduce token overhead — `core` mode loads only 7 essential tools at ~5,000 tokens (70% reduction vs. `all`).

The repo includes agent instruction files (`CLAUDE.md`, `CLAUDE_CODE_PLUGIN.md`, `.cursor/`, `.kiro/`, `.vscode/`) demonstrating integration patterns.

## Example usage

```bash
# Initialize a new project
task-master init --rules cursor,windsurf,vscode

# Parse a PRD to generate tasks
task-master parse-prd .taskmaster/docs/prd.txt

# Analyze complexity and expand complex tasks
task-master analyze-complexity --research
task-master expand --all

# Navigate the task graph
task-master list
task-master next
task-master show 1,3,5

# Research with project context
task-master research "Best practices for JWT auth with Node.js"

# Tag-based workstream management
task-master move --from=5 --from-tag=backlog --to-tag=in-progress
task-master move --from=5,6,7 --from-tag=backlog --to-tag=done --with-dependencies

# Migrate old config
task-master migrate
```

In AI chat (MCP mode):
- "Parse my PRD at scripts/prd.txt"
- "What's the next task I should work on?"
- "Help me implement task 3"
- "Expand task 4"
- "Research React Query v5 migration for our API in src/api.js"

## Maintenance status

- **Stars:** 27,242 | **Forks:** 2,538 (as of 2026-05-25)
- **Latest release:** `task-master-ai@0.43.1` (2026-03-31)
- **License:** MIT with Commons Clause (allows use; restricts commercial resale of the tool itself)
- **CI:** GitHub Actions (`ci.yml`)
- **Actively maintained** — part of the Hamster platform ([[tryhamster.com]]); monorepo structure with Turborepo; 50+ documented CLI commands and 36 MCP tools

## Ecosystem

- **Supported editors:** Cursor, Windsurf, VS Code, Q Developer CLI, Lovable, Roo, Claude Code, and any MCP-compatible host
- **AI providers:** Anthropic (Claude), OpenAI (GPT), Google (Gemini), Perplexity, xAI (Grok), Mistral, OpenRouter, Ollama, Azure, Vertex AI, Zhipu AI, Moonshot AI, Meta
- **Discord:** https://discord.gg/taskmasterai
- **Related tools:**
  - [[anombyte93-prd-taskmaster]] — Claude Code skill that generates PRDs and wires them directly into Taskmaster
  - [[www.taskmaster.one]] — Separate commercial SaaS product using the same concept but different codebase/company
  - [[buildermethods-agent-os]] — Agent OS methodology that complements task management
  - [[gsd-build-get-shit-done]] — Spec-driven development methodology using AI agents
