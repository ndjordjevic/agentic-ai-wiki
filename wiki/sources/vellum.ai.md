---
type: source
source_url: https://www.vellum.ai/
companion_urls:
  - https://github.com/vellum-ai/vellum-assistant
raw_files:
  - ../../raw/web/vellum.ai.md
  - ../../raw/github/vellum-ai-vellum-assistant.md
tags:
  - personal-ai
  - personal-intelligence
  - persistent-memory
  - omnichannel-agent
  - managed-oauth
  - computer-use
  - skills-system
  - self-hosted
related:
  - hermes-agent.nousresearch.com
  - app.sauna.ai
  - joinoasis.com
  - abacus.ai
  - happy.engineering
  - skills.sh
  - trigger.dev
  - integuru.com
product: vellum
detail_level: standard
created: 2026-07-07
updated: 2026-07-07
---

Vellum is an open-source (MIT) personal intelligence platform — product site plus `vellum-ai/vellum-assistant` runtime — that gives each user a persistent AI assistant with managed memory, its own identity (email, Slack handle, phone), and real-world tool use across Gmail, calendar, Slack, browser automation, macOS computer use, and 28+ bundled skills. Unlike session-scoped chatbots, it runs always-on in Vellum Cloud by default or self-hosted on macOS, reachable from web, iOS, desktop, CLI, Telegram, Slack, email, and voice. The marketing site emphasizes easy setup and managed integrations; the companion repo implements a Bun+TypeScript runtime (`assistant/`), gateway (`gateway/`), credential-executor sidecar, and native macOS client with hybrid memory (workspace files + PKB + vector recall). (../../raw/github/vellum-ai-vellum-assistant.md)

_All claims below are sourced from ../../raw/web/vellum.ai.md unless otherwise noted._

## What it does

Vellum positions itself as "personal intelligence" — a separate entity that works for you, learns your preferences over weeks and months, and takes action (email triage, calendar coordination, meeting prep, delegation, research, travel booking) rather than only answering questions. The landing page contrasts it with Hermes, OpenClaw, and Claude Cowork on setup ease, managed memory, built-in security, managed OAuth connectors, and omnichannel reach (iOS, macOS, web, voice, email, Telegram, Slack, CLI).

Core differentiators from generic chat tools: tools not just words (web, files, code, email, calendar, Mac accessibility APIs); cross-session memory; the assistant's own identity so recipients know they're talking to your assistant; plain-text exportable workspace data in cloud or local mode; single-user personal scope (not a team Slack bot).

## Key features

**Memory:** Three layers — workspace files (`essentials.md`, `threads.md`, `recent.md`, `buffer.md` plus legacy `SOUL.md`/`IDENTITY.md`/`USER.md`/`NOW.md` in llms.txt), curated PKB notes in `pkb/`, and auto-extracted long-term memory with eight kinds (Event, Knowledge, Feeling, Plan, Pattern, Story, Shared, Skill). Hybrid dense+sparse retrieval, spreading activation, injection gate, consolidation every four hours, procedural memory saved as self-authored skills.

**Skills & tools:** 28 bundled skills (Gmail, Slack, Browser, Computer Use, App Builder, Schedule, Phone Calls, etc.) loaded on demand via `skill_load`. Core sandbox tools always on; host tools (`host_bash`, `host_file_*`) require approval. Community skills via skills.sh; custom skills scaffolded from conversation.

**Channels:** One assistant, one memory across web, macOS desktop (computer use + voice), iOS, CLI, Telegram, Slack, Agent Mail email, Twilio phone. Guardian model: you verify channel identities, route approvals, and gate memory extraction.

**Hosting:** Vellum Cloud (default, encrypted isolated workspace) or local macOS self-host with Keychain-stored API keys. Install: `curl -fsSL https://www.vellum.ai/install.sh | bash`. (../../raw/github/vellum-ai-vellum-assistant.md)

## Architecture

The open-source monorepo splits into three platform domains: **Assistant Runtime** (`assistant/`) — Bun+TypeScript, SQLite conversation store, Unix socket + HTTP API; **Gateway** (`gateway/`) — public ingress for Telegram webhooks, Twilio voice, OAuth callbacks, authenticated reverse proxy; **Native Clients** (`clients/`) — Swift macOS menu bar app with accessibility-based computer use. A separate **Credential Execution Service** (`credential-executor/`) isolates API keys and OAuth tokens from the LLM. Default ports: gateway 3001, daemon 7821. SSE event stream at `GET /v1/events` with types like `assistant_text_delta`, `tool_use_start`, `confirmation_request`. (../../raw/github/vellum-ai-vellum-assistant.md)

## Installation

```bash
# One-line install (site + llms.txt)
curl -fsSL https://www.vellum.ai/install.sh | bash && . ~/.config/vellum/env

# CLI via npm/bun
bun install -g vellum
vellum hatch

# From source
git clone https://github.com/vellum-ai/vellum-assistant.git
cd vellum-assistant && ./setup.sh && source ~/.bashrc
vellum hatch
```

Cloud path: sign up at vellum.ai (free, no credit card), meet assistant in browser. Desktop: DMG for macOS 15+. Managed mode needs no local runtime; local mode runs everything on your Mac. (../../raw/github/vellum-ai-vellum-assistant.md)

## Example usage

```bash
vellum message "summarize today's calendar"   # send message, stream response
vellum events                                  # tail live SSE stream
vellum ps                                      # inspect process state
vellum doctor                                  # diagnostic check
vellum wake / vellum sleep                     # start/stop services
```

Operator prompts from docs: "Start my day" (briefing), "Archive everything from newsletters", "Build me a habit tracker" (App Builder), "Remind me at 4pm to drink water" (Schedule/cron), "Remember that I hate cilantro" (PKB/memory). First sensitive action surfaces Allow/Deny with risk badge; trust rules can persist approvals. (../../raw/github/vellum-ai-vellum-assistant.md)

## When to use

- You want a **personal** (not team) AI that remembers you across channels without building your own memory stack (contrast Hermes/OpenClaw DIY markdown+SQLite patterns).
- You need **managed OAuth** to Gmail, Google Calendar, Slack, Linear, Notion, etc. without wiring connectors yourself.
- You want **omnichannel reach** (phone, email, Slack, Telegram, desktop computer use) from one assistant identity.
- You're comparing **hosted personal AI** products (vs coding harnesses like Claude Code) and value MIT-licensed self-host escape hatch.

Less fit when you need multi-agent org charts ([[paperclip.ing]]), pure coding-agent CLI depth, or team-shared coworker spaces without personal isolation.

## Maintenance status

Actively maintained: `vellum-ai/vellum-assistant` — 841 stars, 124 forks, TypeScript, default branch `main`, latest release **v0.10.6** (2026-07-06), pushed 2026-07-07. MIT license. Homepage https://vellum.ai. Docs at vellum.ai/docs with `/llms.txt` and `/docs/llms.txt` machine-readable indexes. Discord community linked from repo. Vellum (for-profit) offers managed Vellum Cloud while keeping the runtime open source. (../../raw/github/vellum-ai-vellum-assistant.md)

## Ecosystem

Compares itself directly to Hermes Agent and OpenClaw on the marketing site; integrates with skills.sh for community skill installs; supports MCP servers for extended tools; multi-provider LLM support (Anthropic default, plus OpenAI, Gemini, OpenRouter, Fireworks, Ollama). OAuth providers include Google, Slack, Linear, GitHub, Notion, HubSpot, Salesforce, Twitter/X, and more via managed registry. ACP skill delegates to external coding agents. ChatGPT import skill for migration continuity.

## Documentation

Docs site sections: Getting Started (install, quick start, first skill), Key Concepts (workspace, memory, channels, skills), Skills Reference (28+ capabilities), Trust & Security, Developer Guide (architecture, API/SSE, security, contributing). Site publishes `llms.txt` (product overview) and `docs/llms.txt` (per-page index with Markdown mirrors).
