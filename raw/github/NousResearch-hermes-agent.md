# NousResearch/hermes-agent

## Metadata
- Stars: 189,190
- Primary language: Python
- Default branch: main
- Latest release: v2026.6.5 (2026-06-06) — "The Surface Release"
- License: MIT License
- Homepage: https://hermes-agent.nousresearch.com
- Fetched: 2026-06-10
- Final URL: https://github.com/NousResearch/hermes-agent

## Description

The agent that grows with you. The self-improving AI agent built by Nous Research — an autonomous agent with a built-in learning loop that creates skills from experience, improves them during use, and builds a deepening model of who you are across sessions.

## README

<p align="center">
  <img src="assets/banner.png" alt="Hermes Agent" width="100%">
</p>

# Hermes Agent ☤

**The self-improving AI agent built by [Nous Research](https://nousresearch.com).** It's the only agent with a built-in learning loop — it creates skills from experience, improves them during use, nudges itself to persist knowledge, searches its own past conversations, and builds a deepening model of who you are across sessions. Run it on a $5 VPS, a GPU cluster, or serverless infrastructure that costs nearly nothing when idle. It's not tied to your laptop — talk to it from Telegram while it works on a cloud VM.

Use any model you want — Nous Portal, OpenRouter (200+ models), NovitaAI, NVIDIA NIM (Nemotron), Xiaomi MiMo, z.ai/GLM, Kimi/Moonshot, MiniMax, Hugging Face, OpenAI, or your own endpoint. Switch with `hermes model` — no code changes, no lock-in.

| Feature | Description |
|---|---|
| **A real terminal interface** | Full TUI with multiline editing, slash-command autocomplete, conversation history, interrupt-and-redirect, and streaming tool output. |
| **Lives where you do** | Telegram, Discord, Slack, WhatsApp, Signal, and CLI — all from a single gateway process. Voice memo transcription, cross-platform conversation continuity. |
| **A closed learning loop** | Agent-curated memory with periodic nudges. Autonomous skill creation after complex tasks. Skills self-improve during use. FTS5 session search with LLM summarization for cross-session recall. Honcho dialectic user modeling. Compatible with the agentskills.io open standard. |
| **Scheduled automations** | Built-in cron scheduler with delivery to any platform. Daily reports, nightly backups, weekly audits — all in natural language, running unattended. |
| **Delegates and parallelizes** | Spawn isolated subagents for parallel workstreams. Write Python scripts that call tools via RPC, collapsing multi-step pipelines into zero-context-cost turns. |
| **Runs anywhere, not just your laptop** | Six terminal backends — local, Docker, SSH, Singularity, Modal, and Daytona. Daytona and Modal offer serverless persistence — your agent's environment hibernates when idle and wakes on demand. |
| **Research-ready** | Batch trajectory generation, trajectory compression for training the next generation of tool-calling models. |

### Quick Install

**Linux, macOS, WSL2, Termux:**
```bash
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
```

**Windows (native, PowerShell):**
```powershell
iex (irm https://hermes-agent.nousresearch.com/install.ps1)
```

After installation:
```bash
source ~/.bashrc    # reload shell
hermes              # start chatting!
```

### Getting Started

```bash
hermes              # Interactive CLI — start a conversation
hermes model        # Choose your LLM provider and model
hermes tools        # Configure which tools are enabled
hermes config set   # Set individual config values
hermes gateway      # Start the messaging gateway (Telegram, Discord, etc.)
hermes setup        # Run the full setup wizard (configures everything at once)
hermes claw migrate # Migrate from OpenClaw (if coming from OpenClaw)
hermes update       # Update to the latest version
hermes doctor       # Diagnose any issues
```

### Skip the API-key collection — Nous Portal

**Nous Portal** (https://portal.nousresearch.com) provides 300+ models and a Tool Gateway (web search via Firecrawl, image generation via FAL, TTS via OpenAI, cloud browser via Browser Use) under one subscription.

```bash
hermes setup --portal
```

### CLI vs Messaging Quick Reference

| Action | CLI | Messaging platforms |
|---|---|---|
| Start chatting | `hermes` | Run `hermes gateway setup` + `hermes gateway start` |
| Start fresh conversation | `/new` or `/reset` | `/new` or `/reset` |
| Change model | `/model [provider:model]` | `/model [provider:model]` |
| Set a personality | `/personality [name]` | `/personality [name]` |
| Browse skills | `/skills` or `/<skill-name>` | `/<skill-name>` |
| Interrupt current work | `Ctrl+C` or send a new message | `/stop` or send a new message |

### Documentation

All documentation: https://hermes-agent.nousresearch.com/docs/

| Section | What's Covered |
|---|---|
| Quickstart | Install → setup → first conversation in 2 minutes |
| CLI Usage | Commands, keybindings, personalities, sessions |
| Configuration | Config file, providers, models, all options |
| Messaging Gateway | Telegram, Discord, Slack, WhatsApp, Signal, Home Assistant |
| Security | Command approval, DM pairing, container isolation |
| Tools & Toolsets | 40+ tools, toolset system, terminal backends |
| Skills System | Procedural memory, Skills Hub, creating skills |
| Memory | Persistent memory, user profiles, best practices |
| MCP Integration | Connect any MCP server for extended capabilities |
| Cron Scheduling | Scheduled tasks with platform delivery |
| Context Files | Project context that shapes every conversation |
| Architecture | Project structure, agent loop, key classes |

### Migrating from OpenClaw

```bash
hermes claw migrate              # Interactive migration (full preset)
hermes claw migrate --dry-run    # Preview what would be migrated
hermes claw migrate --preset user-data   # Migrate without secrets
```

What gets imported: SOUL.md, memories (MEMORY.md and USER.md), skills, command allowlist, messaging settings, API keys, TTS assets.

## Docs

### AGENTS.md

Hermes Agent is a personal AI agent that runs the same agent core across a CLI, a messaging gateway (24+ platforms), a TUI, and an Electron desktop app. It learns across sessions (memory + skills), delegates to subagents, runs scheduled jobs, and drives a real terminal and browser. Extended primarily through plugins and skills, not by growing the core.

Two properties shape every design decision:
- **Per-conversation prompt caching is sacred.** Anything that mutates past context or rebuilds the system prompt mid-conversation invalidates that cache. The one exception is context compression.
- **The core is a narrow waist; capability lives at the edges.** Every model tool added is sent on every API call. Most new capability should arrive as a CLI command + skill, service-gated tool, or plugin — not as core surface.

Contribution guidelines: prefer fixes, platform adapters, refactoring; new model tools are the expensive exception.

## Top-level structure

| Path | Purpose |
|---|---|
| `agent/` | Core agent loop and orchestration |
| `gateway/` | Messaging platform adapters (24+ platforms) |
| `tools/` | Tool implementations (70+ tools) |
| `providers/` | LLM provider integrations (18+) |
| `skills/` | Built-in and optional skills |
| `cron/` | Scheduled task engine |
| `hermes_cli/` | CLI entry points and TUI |
| `tui_gateway/` | TUI gateway interface |
| `ui-tui/` | Terminal UI components |
| `optional-skills/` | Community/optional skills |
| `optional-mcps/` | Optional MCP server integrations |
| `plugins/` | Plugin system |
| `acp_adapter/` | ACP (Python library) adapter |
| `acp_registry/` | ACP registry |
| `web/` | Web assets |
| `website/` | Documentation website source |
| `run_agent.py` | Core agent orchestration entrypoint |
| `cli.py` | CLI entrypoint |
| `mcp_serve.py` | MCP server entrypoint |
| `batch_runner.py` | Batch trajectory generation |
| `AGENTS.md` | Development guide for AI coding assistants |
| `Dockerfile` | Container build definition |
| `docker-compose.yml` | Docker Compose for deployment |
| `pyproject.toml` | Python package configuration |
| `flake.nix` | Nix flake for reproducible builds |
