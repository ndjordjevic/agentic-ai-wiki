---
type: source
category: "Coding-agent harnesses & methodologies"
source_url: https://github.com/deepseek-ai/deepseek-harness
tags:
  - agent-harness
  - plugin-architecture
  - cordis
  - capability-seams
  - acp-server
  - multi-agent
  - self-modification
  - openai-compatible
related:
  - coleam00-harness-engineering-demo
  - openai-symphony
  - anthropics-claude-agent-sdk-python
  - x.ai
  - agno.com
product: deepseek-harness
detail_level: standard
created: 2026-08-24
updated: 2026-08-24
---

DeepSeek Harness (`dsh`) is an open-source agent harness from DeepSeek AI built on the radical principle that **everything is a plugin** — the model adapter, tool registry, session log, approval policy, shell executor, and even the agent loop itself are all Cordis plugins, making every part of the harness replaceable through configuration. With 189k stars on GitHub (developer preview, v0.1.1-rc.2 as of August 2026), it is one of the most-starred agent harness projects and represents a serious architectural reference for composable, extensible agentic systems.

_All claims below are sourced from ../../raw/github/deepseek-ai-deepseek-harness.md unless otherwise noted._

## What it does

`dsh` is a TypeScript/Node.js agent harness that runs as a local server with a Web UI (`npx @deepseek-ai/dsh web`) or headless (`dsh --profile headless "task"`). It drives an LLM agent through a structured turn/step loop, manages tool execution, persists session logs, and exposes itself as an Agent Client Protocol (ACP) automation server for embedding in other tools. A Python SDK is also bundled (`python/`).

Key surfaces:
- **Web UI** — browser-based chat interface at `http://127.0.0.1:3080`
- **Headless** — one-shot task runner with no server, ideal for CI/scripts
- **ACP server** — automation-only `packages/acp/` server for programmatic control
- **JSON-RPC SDK** — `packages/sdk/` protocol, server, and TypeScript client for custom integrations

## Key features

- **Everything is a plugin (Cordis)** — no privileged core; any component can be replaced by mounting a different plugin in `cordis.yml`. Model adapters, filesystem providers, shell executors, subagent backends, telemetry, credentials — all swappable via config.
- **Capability seams** — every swappable capability has three explicit roles: Service Definition (interface), Service Provider (implementation), Consumer (model-facing tool). Swapping a filesystem provider to a remote sandbox automatically migrates Bash, PTY, and LSP with zero provider forks.
- **Rich tool suite** — `bash`, `pwsh`, `str_replace_editor`, `edit/read/write`, `glob/grep`, `web_search/web_fetch`, `subagent`/`subagent_fork`, `workflow`, `skill`, `lsp`, `run_code`, `todo_write`, `schedule_*`, `terminal_*`, `job_*`, `cordis_*` (self-modification, experimental).
- **Subagents** — continuable background subagents with `send_message`, `interrupt_agent`, `list_agents`; also one-shot fork-based subagents. Experimental Agent Teams feature for durable multi-agent coordination with task boards and mailboxes.
- **Self-modification** — the `cordis_define/run/stop` toolset lets the agent install and unload its own plugins at runtime (opt-in, deliberate security boundary).
- **Plan mode** — `exit_plan_mode` tool; plan is logged state with approval flow over the `ask_user_question` seam.
- **Hook bridges** — `packages/hooks/` integrates Claude Code and Codex hook protocols.
- **Durable session log** — append-only `SessionEvent` log; everything model-visible is reconstructable from it. Fork, resume, transcripts, telemetry all derive from this stream.

## Architecture

The core is a **Cordis plugin tree** composed at boot from ordered layers:

1. **Profile** — named composition listing bundles + user `cordis.patch.yml`
2. **Bundle** — distribution format for Cordis config rows + code (e.g. `dsh-base`, `dsh-web-app`, `dsh-headless`)
3. **Patches** — profile patch → home-level patch → `--patch` overlay; each targets a row by id and replaces or inserts config

The **turn/step loop**:
```
turn/start
  claim next-step input + queued message
  assemble prompt sections + tool schemas
  → agent/pre-step  [reject | rewrite]
    step/start
    agent/request → llm/stream → assistant/message
    tool/call* → tools/pre-execute → tools/execute → tools/post-execute → tool/result*
    step/end
  → agent/turn-stopping
turn/end
```

**Extension mechanism:** every capability is a seam — register on `ctx.llm` to add a model provider, `ctx.tools` to add a model-facing capability, `ctx.shell` for shell execution, `ctx.fs` for filesystem, `ctx.subagents` for delegation backends, etc. The architecture doc (`docs/architecture.md`) provides a full table of goals → mechanisms.

The **Typert** subsystem (`packages/typert/`) generates, loads, and runs a runtime type registry from TypeScript AST — the API gateway is built on this to provide strongly-typed RPC without hand-written schemas.

## Installation

```sh
# Quickest start
npx @deepseek-ai/dsh web

# From source
git clone https://github.com/deepseek-ai/deepseek-harness.git
cd deepseek-harness
pnpm install
pnpm run build
pnpm dsh web

# Requires Node.js ^22.19 || >=24 and pnpm workspaces
```

Set `DEEPSEEK_API_KEY` for real-API tests and headless runs. The `dsh --profile web --dump-config` command shows the full plugin tree your instance boots.

## Example usage

```sh
# One-shot headless task
pnpm dsh --profile headless "Explain this codebase"

# Inspect config tree
dsh --profile web --dump-config

# ACP automation server demo
pnpm run demo:acp   # needs DEEPSEEK_API_KEY

# Self-modification demo (agent mounts its own plugins)
pnpm run demo:cordis
```

The `examples/` directory contains runnable `cordis.yml` leaves for: `acp-agent`, `headless-agent`, `jsonrpc-agent`, `mcp-memory`, `web-cordis`, and `web-schedule`.

## When to use

- When you want a **fully composable harness** where model, tools, sandbox, session storage, and approval policy are all pluggable — no forks, just config patches.
- When building custom agent shells that need to reuse the capability seam abstraction (e.g. swapping local subprocess for E2B sandbox transparently).
- For **multi-agent workflows** where continuable background subagents, fork-based delegation, and ACP automation are first-class requirements.
- When you want a **reference implementation** of a production-grade agent loop with a rich session log, hook bridges (Claude Code, Codex), plan mode, and tool-timeout/loop-hygiene guards.
- Note: still in developer preview with compatibility-breaking changes expected.

## Maintenance status

- **Stars:** 189,060 (August 2026) — extremely high for a developer preview
- **Latest release:** v0.1.1-rc.2 (2026-08-21, pre-release)
- **License:** MIT
- **Language:** TypeScript (Node.js ≥22.19); Python SDK bundled
- **Activity:** actively developed, pushed 2026-08-21
- Community: GitHub Discussions + `dsh-plugin` topic for plugin discoverability + Discord
