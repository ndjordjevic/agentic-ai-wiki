---
type: source
source_url: https://pi.dev/
tags:
  - coding-agent
  - terminal-cli
  - agent-harness
  - multi-provider
  - typescript-extensions
  - skill-support
  - sdk
  - rpc
  - open-source
  - mcp
companion_github: earendil-works/pi
related:
  - wisprflow.ai
  - strandsagents.com
  - crewai.com
  - omnigent-ai-omnigent
product: pi-coding-agent
detail_level: standard
created: 2026-06-08
updated: 2026-06-16
---

Pi is a minimal terminal coding harness (CLI) by Earendil Inc. that prioritizes "primitives, not features" — a lightweight, MIT-licensed agent that stays small by design while supporting deep customization via TypeScript extensions and the SKILL.md ecosystem. The monorepo (60,792 GitHub stars) also provides a unified multi-provider LLM API, a terminal UI library, and an embeddable Node.js SDK.

_All claims below are sourced from ../../raw/web/pi.dev.md and ../../raw/github/earendil-works-pi.md unless otherwise noted._

## What it does

Pi is an interactive terminal coding agent that connects to 15+ AI providers (968 models) and exposes four operating modes: interactive TUI, print/JSON output, JSONL-based RPC, and SDK embedding. It stores conversations as tree-structured JSONL session files and reads project context from `AGENTS.md` / `SYSTEM.md`. Extensions are TypeScript modules installed via `pi install npm:<name>` from a registry of 3,726 packages, enabling sub-agents, plan mode, permission gates, SSH, sandboxing, and MCP tool integration.

## Key features

- **Multi-provider** — 15+ providers (Anthropic, OpenAI, Google, Azure, Bedrock, Mistral, Groq, Cerebras, xAI, HuggingFace, Ant Ling, NVIDIA NIM, MiniMax, and more), 968 models, all configured in `/settings`
- **TypeScript extensions** — loaded from `~/.pi/agent/extensions/` or installed via `pi install`; can use `ctx.mode` and `ctx.getSystemPromptOptions()` to adapt across TUI/RPC/JSON/print modes
- **SKILL.md support** — compatible with the broader agent-skills ecosystem (see [[voltagent-awesome-agent-skills]])
- **Four modes** — interactive TUI, print/JSON, RPC (JSONL stdin/stdout), SDK (`createAgentSession()`)
- **Package registry** — 3,726 packages; top: `context-mode` (131.5K downloads), `pi-subagents` (103.2K downloads)
- **MCP integration** — TypeScript extensions can route built-in tools through MCP
- **Containerization patterns** — OpenShell (policy sandbox), Gondolin extension (local micro-VM), plain Docker
- **Session sharing** — publish OSS coding sessions to Hugging Face via `badlogic/pi-share-hf`

## Architecture

The `earendil-works/pi` monorepo has four packages:

| Package | Role |
|---------|------|
| `@earendil-works/pi-coding-agent` | Interactive coding agent CLI (`pi` binary) |
| `@earendil-works/pi-agent-core` | Agent runtime: tool calling, state management |
| `@earendil-works/pi-ai` | Unified multi-provider LLM API |
| `@earendil-works/pi-tui` | Terminal UI library with differential rendering |

Session history is stored as JSONL files in `~/.pi/sessions/` with tree structure (branching conversations). No built-in permission sandbox — containerization is recommended for production or untrusted contexts.

## Installation

```bash
npm install -g --ignore-scripts @earendil-works/pi-coding-agent
# then:
pi
```

Node.js minimum: v22.19.0 (since v0.75.0).

## Example usage

```bash
pi                    # launch interactive TUI in current project directory
pi --name my-task     # start named session
pi --exclude-tools X  # disable specific built-in tools
pi install npm:context-mode   # install a package/extension
```

RPC mode (for programmatic use):
```bash
pi --rpc   # JSONL events on stdout, commands on stdin
```

## When to use

Pi fits teams and developers who want a minimal, composable agent harness with full provider flexibility and a TypeScript extension model — as opposed to opinionated frameworks with built-in orchestration. Its "primitives, not features" philosophy makes it well-suited for building custom agent workflows or embedding into larger Node.js applications via the SDK.

## Maintenance status

Actively maintained (v0.78.1, June 2026). Weekly releases with provider additions, bug fixes, and extension API improvements. Supply-chain hardened: exact dependency pinning, shrinkwrap for published CLI, CI audit checks.

## Ecosystem

- **npm package registry**: 3,726 installable packages at https://pi.dev/packages
- **Model registry**: 968 models at https://pi.dev/models
- **pi-chat**: [earendil-works/pi-chat](https://github.com/earendil-works/pi-chat) — Slack/chat automation built on pi
- **Session sharing**: [badlogic/pi-share-hf](https://github.com/badlogic/pi-share-hf) for Hugging Face dataset publishing
- **Docs**: https://pi.dev/docs/latest (client-rendered SPA; sub-pages require JS)
- **Discord**: discord.com/invite/3cU7Bz4UPx
