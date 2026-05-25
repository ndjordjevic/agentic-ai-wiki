---
type: source
source_url: https://www.taskmaster.one/
tags:
  - ai-task-management
  - prd-to-tasks
  - mcp-integration
  - saas
  - task-dependencies
  - multi-model
  - cli-tool
  - agent-workflow
related:
  - eyaltoledano-claude-task-master
  - anombyte93-prd-taskmaster
  - vibekanban.com
  - gsd-build-get-shit-done
  - backnotprop-plannotator
  - tryhamster.com
product: taskmaster
detail_level: standard
created: 2026-05-25
updated: 2026-05-25
---

TaskMaster AI (taskmaster.one) is a commercial SaaS product by TaskMaster AI LLC that acts as a "project manager for AI coding agents" — it ingests Product Requirements Documents, breaks them into structured dependency-aware tasks, and synchronises those tasks across a CLI, MCP server, and web dashboard. It targets developer teams using AI-powered editors (Cursor, Windsurf, VS Code) and provides hosted API key management so teams can adopt multi-model AI without managing `.env` files per engineer.

_All claims below are sourced from ../../raw/web/www.taskmaster.one.md unless otherwise noted._

## What it does

TaskMaster AI accepts a PRD, parses it into a hierarchical task graph with stable IDs, priorities, dependencies, and complexity scores, and exposes that graph through a CLI (`taskmaster`), an MCP server, and a web dashboard. All three surfaces stay in sync: CLI edits appear in the dashboard; agent runs update task statuses visible in the browser. The system is model-agnostic — the operator assigns a main model, a research model, and a fallback model from any supported provider.

## Key features

- **PRD parsing** — Ingest a product requirements document to auto-generate structured tasks with IDs, statuses, dependencies, and subtasks in one pass.
- **Dependency-aware "next task"** — Dependency graph ensures agents and developers always know which task to tackle next without guessing.
- **Complexity scoring** — Tasks are scored 1–10 to guide subtask expansion; `task-master analyze-complexity` produces a report with AI-generated expansion prompts.
- **Task expansion** — `task-master expand` turns high-complexity tasks into subtasks using complexity report recommendations.
- **Research mode** — Integrated research command fetches fresh external information with project context before answering.
- **Multi-model roles** — Assign separate models to main, research, and fallback slots; supports Anthropic, OpenAI, Google Gemini, Perplexity, xAI, Mistral, OpenRouter, Ollama, Azure, Zhipu AI, Meta.
- **Hosted API keys (Pro/Enterprise)** — Team API keys are managed in the platform vault; no per-engineer `.env` setup.
- **Dashboard & usage tracking** — Web dashboard shows task activity, usage against monthly plan, and recent agent operations.

## Architecture and concepts

The product is built around three integration surfaces that share the same task graph:

1. **CLI** — `@taskmasterai/cli` npm package; `taskmaster` binary. Commands include `parse-prd`, `list`, `next`, `show`, `expand`, `analyze-complexity`, `research`, `move`, and `models --setup`.
2. **MCP server** — Exposes the task graph as MCP tools to any MCP-compatible editor (Cursor, Windsurf, VS Code, Q CLI). Installed via `npx @taskmasterai/cli taskmaster-mcp` or one-click Cursor deeplink.
3. **Web dashboard** — Subscription-gated UI showing tasks, usage metrics, license status, and API key vault.

Configuration is stored in environment variables or a setup wizard (`taskmaster models --setup`). Models are assigned per role (main, research, fallback) and can be changed via CLI or AI chat.

**Important distinction:** TaskMaster AI (`taskmaster.one`, npm: `@taskmasterai/cli`) is a **separate commercial product** from the open-source `claude-task-master` project (npm: `task-master-ai`) by @eyaltoledano — see [[eyaltoledano-claude-task-master]]. Both solve the same problem space but differ in ownership, licensing, and npm package names.

## Main APIs

CLI commands (from `@taskmasterai/cli`):
```bash
taskmaster models --setup              # Interactive model configuration
taskmaster models --set-main <model>   # Set main AI model
taskmaster models --set-research <m>   # Set research model
taskmaster models --set-fallback <m>   # Set fallback model
```

MCP config for Cursor/Windsurf:
```json
{
  "mcpServers": {
    "taskmasterai": {
      "command": "npx",
      "args": ["-y", "@taskmasterai/cli", "taskmaster-mcp"],
      "env": { "ANTHROPIC_API_KEY": "..." }
    }
  }
}
```

## When to use

- Teams using Cursor, Windsurf, or VS Code who want a hosted, subscription-managed task management layer across multiple agents and developers.
- Projects where managing API keys per developer is a friction point — Pro/Enterprise plans provide shared hosted keys.
- Situations where a web dashboard is needed to track AI agent activity, usage costs, and task progress at a glance.
- Workflows that start from formal PRDs and need systematic task breakdown with dependency tracking before agent execution.

Choose the open-source alternative [[eyaltoledano-claude-task-master]] when you prefer MIT-licensed tooling, self-managed API keys, and want the full community ecosystem of plugins and integrations.

## Ecosystem

- **Supported editors:** Cursor, Windsurf, VS Code, Q Developer CLI (any MCP host)
- **AI providers:** Anthropic, OpenAI, Google, Perplexity, xAI, Mistral, OpenRouter, Ollama, Azure, Zhipu AI, Meta
- **Related tools:** [[anombyte93-prd-taskmaster]] (Claude Code skill that generates PRDs and wires them to Taskmaster AI), [[vibekanban.com]] (Kanban board for AI agent task tracking)
- **Pricing tiers:** Plus $29/mo (100 tasks, BYOK), Pro $199/mo (1,000 tasks, hosted keys), Enterprise $599+/mo (5,000+ tasks, team management, SLAs)
