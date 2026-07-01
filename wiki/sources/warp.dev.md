---
type: source
source_url: https://www.warp.dev/
companion_urls:
  - https://github.com/warpdotdev/warp
raw_files:
  - ../../raw/web/warp.dev.md
  - ../../raw/github/warpdotdev-warp.md
tags:
  - agentic-development-environment
  - terminal
  - cloud-agents
  - multi-agent-orchestration
  - oz-platform
  - mcp
  - cli-agents
  - rust
related:
  - tmuxai.dev
  - cognition.ai
  - aaif-goose-goose
  - strandsagents.com
  - crewai.com
  - factory.ai
  - producthunt.com
product: warp
detail_level: standard
created: 2026-07-01
updated: 2026-07-01
---

Warp is an open-source Agentic Development Environment (ADE) built in Rust that unites a high-performance, modern terminal with a cloud agent orchestration platform called Oz. Unlike AI coding assistants that sit alongside a conventional terminal, Warp re-imagines the terminal itself as the control plane for local and cloud agents: developers can run Warp's own agent, Claude Code, Codex, Gemini CLI, or OpenCode inside a single UI that provides rich input, interactive code review, planning, task tracking, and MCP tool connectivity. The companion `warpdotdev/warp` repo (62k+ stars, AGPL-3.0, with MIT for the UI crates) hosts the open-source client and is actively maintained by a mix of engineers and Oz-powered automated agents. (../../raw/github/warpdotdev-warp.md)

_All claims below are sourced from ../../raw/web/warp.dev.md unless otherwise noted._

## What it does

Warp provides two integrated layers of agentic development. The **Warp Terminal** is a modern, block-based terminal built for agent workflows: it supports multi-turn agent conversations alongside shell commands, has a built-in code editor with LSP support and interactive diff review, and wraps any third-party CLI agent (Claude Code, Codex, OpenCode, Gemini) in a rich toolbelt that adds notifications, code review, and structured input. The **Oz Agent Platform** adds cloud-level orchestration: cloud agents react to events from Slack, Linear, GitHub, or webhooks; run on schedules; fan out across repos; and produce auditable run transcripts that the whole team can inspect and share.

## Key features

- **Multi-harness:** run Warp Agent, Claude Code, Codex, or Gemini CLI interchangeably — switch harnesses on any cloud agent run (../../raw/github/warpdotdev-warp.md)
- **Terminal and Agent modes:** seamlessly switch between a clean terminal prompt and a multi-turn agent conversation in the same window
- **Interactive Code Review:** review agent-generated diffs, leave inline comments, send back to the agent for refinement
- **Planning and Task Lists:** agents produce editable execution plans and real-time task checklists for complex multi-step work
- **Skills and Rules:** define reusable, scoped instructions that teach agents how to perform specific tasks in your codebase; set global and project-level behavioral rules
- **MCP integration:** connect any MCP server to agents for tool access (files, APIs, databases, CI, etc.)
- **Codebase Context:** semantic indexing of Git-tracked files gives agents deep code understanding
- **Computer Use:** agents can interact with desktop environments (screenshots, clicking, typing)
- **Multi-agent orchestration:** coordinate a parent Warp Agent with Claude Code and Codex subagents in parallel for supervisor/worker, fan-out, DAG, and swarm workflows
- **Agent Memory:** cross-harness memory system (research preview) that persists learnings across sessions for Claude Code, Codex, and Warp Agent
- **Warp Drive:** shared team context (rules, saved prompts, MCP configs) available to both local and cloud agents

## Architecture

Warp is a Rust codebase organized as a Cargo workspace. The UI framework (`warpui_core` and `warpui` crates) is MIT-licensed; the rest is AGPL-3.0. The client is open-source at `warpdotdev/warp` on GitHub; the server-side Oz orchestration platform is closed-source but exposed via the Oz CLI and REST API. (../../raw/github/warpdotdev-warp.md)

The agent execution model has two layers: **Local agents** run interactively inside the Warp terminal with full access to the user's shell, codebase, and connected MCP tools; the human reviews and approves actions mid-session. **Cloud agents** run on Warp-hosted or self-hosted infrastructure (Docker/Kubernetes sandboxes), triggered by integrations, schedules, or the CLI, and produce persistent audit records. Both share the same underlying agent capabilities, Warp Drive context, rules, and MCP configuration. (../../raw/github/warpdotdev-warp.md)

Self-hosting supports two architectures: a managed worker daemon where Oz orchestrates agents in Docker containers on your own machines, and an unmanaged mode where you run `oz agent run` directly in CI, Kubernetes, or a dev environment.

## Installation

Download Warp at https://www.warp.dev/download (macOS, Linux; Windows in preview). (../../raw/github/warpdotdev-warp.md)

To build from source: (../../raw/github/warpdotdev-warp.md)

```bash
./script/bootstrap   # platform-specific setup
./script/run         # build and run Warp
./script/presubmit   # fmt, clippy, and tests
```

See `AGENTS.md` in the repo for the full engineering guide covering coding style, testing, and platform-specific notes.

## Example usage

Starting a local agent session: open Warp, press the agent hotkey (or switch to Agent Mode), and type a prompt. The agent produces a plan, executes commands with your approval, and shows diffs for review. For cloud agent runs, use the Oz CLI: (../../raw/github/warpdotdev-warp.md)

```bash
oz agent run --prompt "Triage all open GitHub issues and label them" \
  --harness claude-code \
  --env my-repo-env
```

Integrations (Slack, Linear, GitHub) allow cloud agents to be triggered automatically — for example, `@warp` in a Slack thread starts an agent on the described task.

## When to use

Warp fits teams who want a unified terminal + agent environment rather than a standalone AI coding assistant bolted on to an existing terminal. It is particularly strong for:
- Teams who use Claude Code, Codex, or multiple CLI agents and want a single host environment with richer UX
- Engineering orgs that want to run autonomous cloud agents on PR review, issue triage, refactors, or incident response without setting up separate CI/CD agent infrastructure
- Projects where agent auditability and team-level observability matter (every Oz run produces a shareable transcript)
- Organizations with compliance requirements: Warp is SOC 2 compliant with Zero Data Retention policies on all contracted LLM providers

## Ecosystem

Warp integrates with: Slack, Linear, GitHub, Amazon Bedrock, LiteLLM, OpenRouter, and custom inference endpoints. The Oz API and SDKs allow programmatic task creation and querying. Warp Drive provides shared team context. The companion open-source repo (`warpdotdev/warp`) has an active contributor community (62k stars) and an `oz-for-oss` program that applies the same automated triage/PR-review workflows to partner OSS projects.

Related agentic tools in this wiki: [[cognition.ai]] (autonomous AI coding agent), [[aaif-goose-goose]] (open-source MCP agent), [[tmuxai.dev]] (terminal-native AI assistant), [[strandsagents.com]] and [[crewai.com]] (cloud multi-agent orchestration), [[factory.ai]] (AI-powered developer workflows).

## Documentation

Docs live at https://docs.warp.dev/ with separate documentation sets for Terminal, Agent Platform, Oz Platform, Code, Enterprise, Getting Started, Knowledge & Collaboration, Reference, Support, Guides, and Changelog. Full-text LLM-optimized docs are at `docs.warp.dev/llms-full.txt`; the Oz Agent API has an OpenAPI spec at `docs.warp.dev/openapi.yaml`.
