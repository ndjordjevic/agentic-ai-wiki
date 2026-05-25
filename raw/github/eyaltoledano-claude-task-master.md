# eyaltoledano/claude-task-master

## Metadata
- Stars: 27,242
- Forks: 2,538
- Primary language: JavaScript
- Default branch: main
- Latest release: task-master-ai@0.43.1 (2026-03-31)
- License: MIT with Commons Clause
- Homepage: https://tryhamster.com
- Fetched: 2026-05-25
- Final URL: https://github.com/eyaltoledano/claude-task-master

## Description

A task management system for AI-driven development, designed to work seamlessly with any AI chat. An AI-powered task-management system you can drop into Cursor, Lovable, Windsurf, Roo, and others. By @eyaltoledano & @RalphEcom.

## README

### Taskmaster — A task management system for AI-driven development

Taskmaster: A task management system for AI-driven development, designed to work seamlessly with any AI chat.

**npm package:** `task-master-ai`

#### Documentation

Full Documentation: https://tryhamster.com/docs/taskmaster

Quick Links:
- Quick Start Guide: https://tryhamster.com/docs/taskmaster/getting-started/quick-start/quick-start
- Installation: https://tryhamster.com/docs/taskmaster/getting-started/quick-start/installation
- API Keys & Providers: https://tryhamster.com/docs/taskmaster/getting-started/api-keys
- Supported Editors: https://tryhamster.com/docs/taskmaster/ide-setup/supported-editors
- MCP Tools Reference: https://tryhamster.com/docs/taskmaster/capabilities/mcp
- CLI Commands Reference: https://tryhamster.com/docs/taskmaster/capabilities/cli-root-commands
- Task Structure: https://tryhamster.com/docs/taskmaster/capabilities/task-structure
- Task Dependencies: https://tryhamster.com/docs/taskmaster/task-workflow/dependencies
- Tags & Workstreams: https://tryhamster.com/docs/taskmaster/task-workflow/tags
- Research Command: https://tryhamster.com/docs/taskmaster/task-workflow/research
- Loop Command: https://tryhamster.com/docs/taskmaster/automation/loop
- AI Providers Overview: https://tryhamster.com/docs/taskmaster/ai-providers/overview
- Team Collaboration: https://tryhamster.com/docs/taskmaster/team/overview
- Best Practices: https://tryhamster.com/docs/taskmaster/best-practices/index
- FAQ: https://tryhamster.com/docs/taskmaster/getting-started/faq
- Changelog: CHANGELOG.md

More from Hamster:
- Hamster Studio: https://tryhamster.com/product/studio
- Product & Engineering Methods: https://tryhamster.com/methods
- Hamster Pricing: https://tryhamster.com/pricing

#### Requirements

At least one (1) of the following:
- Anthropic API key (Claude API)
- OpenAI API key
- Google Gemini API key
- Perplexity API key (for research model)
- xAI API Key (for research or main model)
- OpenRouter API Key (for research or main model)
- Claude Code (no API key required — requires Claude Code CLI)
- Codex CLI (OAuth via ChatGPT subscription — requires Codex CLI)

You can define 3 types of models: main model, research model, and fallback model. Whatever model you use, its provider API key must be present in either `mcp.json` or `.env`.

#### Quick Start — Option 1: MCP (Recommended)

MCP (Model Control Protocol) lets you run Task Master directly from your editor.

**Supported editors + config paths:**

| Editor | Scope | Linux/macOS Path | Key |
|---|---|---|---|
| Cursor | Global | `~/.cursor/mcp.json` | `mcpServers` |
| Cursor | Project | `<project>/.cursor/mcp.json` | `mcpServers` |
| Windsurf | Global | `~/.codeium/windsurf/mcp_config.json` | `mcpServers` |
| VS Code | Project | `<project>/.vscode/mcp.json` | `servers` |
| Q CLI | Global | `~/.aws/amazonq/mcp.json` | `mcpServers` |

**MCP Config example (Cursor/Windsurf):**
```json
{
  "mcpServers": {
    "task-master-ai": {
      "command": "npx",
      "args": ["-y", "task-master-ai"],
      "env": {
        "ANTHROPIC_API_KEY": "YOUR_KEY_HERE",
        "OPENAI_API_KEY": "YOUR_KEY_HERE",
        "GOOGLE_API_KEY": "YOUR_KEY_HERE"
      }
    }
  }
}
```

**Claude Code Quick Install:**
```bash
claude mcp add taskmaster-ai -- npx -y task-master-ai
```

#### Quick Start — Option 2: CLI

```bash
# Install globally
npm install -g task-master-ai

# Initialize project
task-master init

# Parse a PRD and generate tasks
task-master parse-prd your-prd.txt

# List all tasks
task-master list

# Show the next task to work on
task-master next

# Research fresh information
task-master research "What are the latest best practices for JWT authentication?"

# Move tasks between tags
task-master move --from=5 --from-tag=backlog --to-tag=in-progress
```

#### Tool Loading Configuration (TASK_MASTER_TOOLS)

Controls which MCP tools are loaded:
- `core` (default): 7 essential tools, ~5,000 tokens (70% reduction) — `get_tasks`, `next_task`, `get_task`, `set_task_status`, `update_subtask`, `parse_prd`, `expand_task`
- `standard`: 15 tools, ~10,000 tokens (50% reduction)
- `all`: 36 tools, ~21,000 tokens
- Custom list: comma-separated specific tool names

## Docs

### Configuration

Taskmaster uses two primary config methods:

1. **`.taskmaster/config.json` (Recommended)** — Stores AI model selections, parameters, logging levels, project defaults. Created by `task-master models --setup` or `task-master init`. Migration: `task-master migrate`.

   Example structure:
   ```json
   {
     "models": {
       "main": { "provider": "anthropic", "modelId": "claude-3-7-sonnet-20250219", "maxTokens": 64000, "temperature": 0.2 },
       "research": { "provider": "perplexity", "modelId": "sonar-pro", "maxTokens": 8700, "temperature": 0.1 },
       "fallback": { "provider": "anthropic", "modelId": "claude-3-5-sonnet", "maxTokens": 64000, "temperature": 0.2 }
     },
     "global": {
       "logLevel": "info", "debug": false, "defaultNumTasks": 10, "defaultSubtasks": 5,
       "defaultPriority": "medium", "defaultTag": "master", "projectName": "Your Project Name"
     }
   }
   ```

2. **Legacy `.taskmasterconfig`** — Backward compatible; use `task-master migrate` to upgrade.

### Task Structure

Tasks in `tasks.json` have fields:
- `id`: Unique identifier (e.g. `1`)
- `title`: Brief, descriptive title
- `description`: Concise description of what the task involves
- `status`: `"pending"`, `"done"`, `"deferred"`, `"in-progress"`
- `dependencies`: IDs of prerequisite tasks (displayed with ✅/⏱️ indicators)
- `priority`: `"high"`, `"medium"`, `"low"`
- `details`: In-depth implementation instructions
- `testStrategy`: Verification approach
- `subtasks`: List of smaller sub-tasks

### Key Commands

**Task lifecycle:**
```bash
task-master parse-prd <file>         # Parse PRD → generate tasks
task-master analyze-complexity       # Score complexity 1–10 per task
task-master expand --id=<n>          # Expand task into subtasks
task-master expand --all             # Expand all tasks by complexity
task-master list                     # List all tasks
task-master next                     # Find next task with deps satisfied
task-master show 1,3,5               # Show specific tasks
task-master set-status --id=<n> --status=done
task-master research "<query>"       # Research with project context
task-master move --from=5 --from-tag=backlog --to-tag=in-progress
```

**Project setup:**
```bash
task-master init                     # Initialize project
task-master init --rules cursor,windsurf,vscode
task-master migrate                  # Migrate old config to new structure
task-master rules add windsurf,roo,vscode
```

### Docs Directory Structure

- `CLI-COMMANDER-PATTERN.md` — CLI architecture pattern
- `command-reference.md` — Full CLI command reference
- `configuration.md` — Configuration guide
- `task-structure.md` — Task format specification
- `tutorial.md` — Tutorial walkthrough
- `examples.md` — Usage examples
- `models.md` — Table of available AI models
- `mcp-provider.md` — MCP provider guide
- `migration-guide.md` — Migration to new config structure
- `cross-tag-task-movement.md` — Cross-tag task movement

### CLAUDE.md / Agent instruction files
The repo includes `CLAUDE.md` (Claude Code integration), `CLAUDE_CODE_PLUGIN.md`, `.cursor/`, `.kiro/`, `.vscode/` — the project itself uses Taskmaster for its own development.

## Top-level structure

```
.changeset/          — Changesets for versioning
.claude-plugin/      — Claude plugin configuration
.claude/             — Claude Code settings
.cursor/             — Cursor IDE settings
.kiro/               — Kiro IDE settings
.taskmaster/         — Taskmaster project configuration (dogfooding)
.vscode/             — VS Code settings
apps/                — Application packages (monorepo)
bin/                 — CLI entrypoints
context/             — Context files for AI agents
docs/                — Documentation (CLI reference, config, task structure, examples, models)
mcp-server/          — MCP server implementation
packages/            — Shared packages (monorepo via Turborepo)
src/                 — Core source code
tests/               — Test suite (Jest + Vitest)
CHANGELOG.md         — Full release history
CLAUDE.md            — Claude Code integration instructions
LICENSE              — MIT with Commons Clause
README.md            — Main readme (this file)
index.js             — Entry point
manifest.json        — MCP server manifest
turbo.json           — Turborepo configuration
```
