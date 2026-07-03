---
type: source
source_url: https://hermes-agent.nousresearch.com/
companion_urls:
  - https://github.com/NousResearch/hermes-agent
raw_files:
  - ../../raw/web/hermes-agent.nousresearch.com.md
  - ../../raw/github/NousResearch-hermes-agent.md
tags:
  - autonomous-agent
  - persistent-memory
  - self-improving-agent
  - multi-platform-messaging
  - agent-skills
  - terminal-backends
  - nous-research
  - open-source
related:
  - skills.sh
  - obra-superpowers
  - felix-forever-hermes-agent-desktop
  - garrytan-gbrain
  - sentry.io
  - ruvnet-ruflo
product: hermes-agent
detail_level: standard
created: 2026-06-10
updated: 2026-07-03
---

Hermes Agent is an open-source autonomous agent developed by Nous Research (MIT License, v0.16.0, 189k GitHub stars) that distinguishes itself through a built-in closed learning loop: it autonomously creates skills from complex tasks, self-improves them during use, and maintains bounded persistent memory across sessions. Unlike session-scoped agents, Hermes is designed to run persistently on a remote server and be accessed from 24+ messaging platforms (Telegram, Discord, Slack, WhatsApp, Signal, and more) or directly via CLI — making the agent location-independent from the user's device.

_All claims below are sourced from ../../raw/web/hermes-agent.nousresearch.com.md unless otherwise noted._

## What it does

Hermes Agent provides a persistent, self-improving autonomous agent runtime that learns from experience. Core capabilities: multi-platform messaging gateway for 24+ platforms, a skill system compatible with the agentskills.io open standard, persistent cross-session memory (MEMORY.md + USER.md), natural language cron scheduling, subagent delegation with parallel workstreams, six terminal execution backends, voice mode, and 60+ built-in tools including web search, browser automation, image generation, and TTS.

## Key features

- **Closed learning loop:** Agent autonomously creates SKILL.md files after completing complex tasks; skills self-improve during subsequent uses. Compatible with agentskills.io standard.
- **Persistent memory:** Two bounded files (MEMORY.md, 2,200 chars; USER.md, 1,375 chars) injected into the system prompt at session start using a frozen-snapshot pattern that preserves LLM prefix cache.
- **Session search:** All conversations stored in SQLite with FTS5 full-text search (`~/.hermes/state.db`); `session_search` tool queries past conversations without LLM calls.
- **24+ platform gateway:** Single gateway process serving Telegram, Discord, Slack, WhatsApp, Signal, SMS, Email, Matrix, Teams, and 15 more; configurable per-platform session reset policies.
- **Six terminal backends:** local, Docker, SSH, Singularity, Modal (serverless), and Daytona (serverless with hibernation).
- **Nous Portal integration:** One-command setup (`hermes setup --portal`) wires in 300+ models plus web search, image generation, TTS, and cloud browser under one subscription.
- **External memory providers:** 8 plugins (Honcho, Mem0, OpenViking, and others) running alongside built-in memory for knowledge graphs and semantic search. (../../raw/github/NousResearch-hermes-agent.md)
- **MCP integration:** Connect any MCP server for extended tool capabilities.
- **ACP adapter:** Python library entry point for programmatic agent use.

## Architecture

The core is organized around a narrow-waist principle: the AIAgent orchestration engine in `run_agent.py` handles provider selection, prompt construction, tool execution, retries, compression, and persistence — but capabilities are added at the edges via plugins, skills, and service-gated tools, not by growing the core model tool schema. (../../raw/github/NousResearch-hermes-agent.md)

Three entry points (CLI, Gateway API Server, ACP library) feed into the same AIAgent engine. The agent loop enforces two invariants: prompt caching is sacred (no mid-conversation system-prompt mutations except context compression), and strict message role alternation (never two same-role messages in a row). (../../raw/github/NousResearch-hermes-agent.md)

Prompt assembly uses a multi-tier system: stable identity/tool guidance + context files (SOUL.md, AGENTS.md) + volatile memory blocks. Provider resolution maps across 18+ LLM providers with OAuth support. The Tool Registry manages 70+ tools across ~28 toolsets with 6 terminal backends.

Three data flow patterns: CLI (user input → API → tool dispatch → display), Gateway (platform event → auth → AIAgent → platform delivery), and Cron (scheduled job → fresh agent → skill injection → platform targeting).

## Installation

```bash
# Linux, macOS, WSL2, Android Termux
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash

# Windows (PowerShell)
iex (irm https://hermes-agent.nousresearch.com/install.ps1)
```

After install: `hermes setup` (full wizard) or `hermes setup --portal` (Nous Portal). (../../raw/github/NousResearch-hermes-agent.md)

## Example usage

```bash
hermes              # start interactive CLI
hermes model        # choose provider and model
hermes gateway      # start messaging gateway
hermes setup        # full setup wizard
hermes doctor       # diagnose issues
hermes update       # update to latest version
```

Common slash commands (CLI and messaging): `/new`, `/reset`, `/model`, `/personality`, `/compress`, `/usage`, `/skills`. (../../raw/github/NousResearch-hermes-agent.md)

## When to use

Hermes fits best when you want a persistent, self-improving agent that is independent of your laptop (runs on a $5 VPS or cloud server), accessible from messaging apps, and that builds up procedural knowledge over time. It is a strong choice for: long-running automation (cron jobs, nightly reports, scheduled backups), teams that want to share agent skills via agentskills.io or custom taps, and users coming from OpenClaw (first-class migration support via `hermes claw migrate`). Less appropriate if you need a purely session-scoped coding assistant without a persistent server footprint.

## Ecosystem

Hermes integrates with: agentskills.io (skills open standard), skills.sh (third-party skills directory), Nous Portal (hosted LLM + tool gateway subscription), Honcho (dialectic user modeling), Browser Use (cloud browser tool), Firecrawl (web search), FAL (image generation). Related projects in the NousResearch GitHub org include `hermes-agent-self-evolution` (DSPy + GEPA optimization), `hermes-paperclip-adapter` (Paperclip company integration), and `autonovel` (autonomous novel-writing pipeline). (../../raw/github/NousResearch-hermes-agent.md)

## Documentation

Full documentation at https://hermes-agent.nousresearch.com/docs/ organized into: Getting Started, User Guide (CLI, Configuration, Messaging, Security, Tools, Skills, Memory, MCP, Cron, Context Files), Developer Guide (Architecture, Contributing), and Reference (CLI Commands, Environment Variables). Machine-readable indexes available at `/llms.txt` (~17 KB) and `/llms-full.txt` (~1.8 MB).
