---
type: source
source_url: https://github.com/omnigent-ai/omnigent
tags:
  - meta-harness
  - multi-agent-orchestration
  - agent-yaml-spec
  - policy-engine
  - sandboxing
  - remote-sessions
  - mcp
  - open-source
related:
  - pi.dev
  - aaif-goose-goose
  - microsoft-agent-framework
  - njbrake-agent-of-empires
product: omnigent
detail_level: standard
created: 2026-06-16
updated: 2026-06-16
---

Omnigent (2,073 stars, Apache-2.0) is an open-source meta-harness that sits above coding-agent CLIs — Claude Code, Codex, Cursor, Pi, and custom agents you write yourself — rather than replacing them. It is most relevant to the wiki's coverage of agent orchestration and governance: instead of building one more agent runtime, Omnigent standardizes how multiple existing harnesses are launched, supervised, sandboxed, and policed, and makes a single session follow the user across terminal, browser, and phone.

_All claims below are sourced from ../../raw/github/omnigent-ai-omnigent.md unless otherwise noted._

## What it does

Omnigent provides a common layer over Claude Code, Codex, Cursor, and Pi (plus custom YAML-defined agents): swap or combine harnesses without rewriting agent logic, keep them in check with policies and sandboxing, and collaborate in real time on one live session from any device. A session started in a terminal continues in a local web UI (`http://localhost:6767`) or on a phone on the same network, with messages, sub-agents, terminals, and files staying in sync; a macOS desktop app wraps the same UI with OS notifications.

## Installation

A single installer script (`curl -fsSL .../install_oss.sh | sh`) sets up Omnigent and its toolchain. Manual installs use `uv tool install omnigent`, `pip install omnigent`, Homebrew (`omnigent-ai/tap/omnigent`), or a direct `git+https://...` install via `uv`. Requirements: Python 3.12+, `uv`, `git`, Node.js 22 LTS+/`npm` (each coding harness's own CLI is installed on first use), `tmux` (native Claude/Codex/Pi wrappers), and on Linux, `bubblewrap` for the mandatory OS-sandbox (macOS uses the built-in `seatbelt` sandbox instead). `omni upgrade` detects the install method and updates in place, draining in-flight sessions first.

## Key features

- **Multi-harness sessions** — `omnigent claude`, `omnigent codex`, or `omnigent run path/to/agent.yaml` launch a chosen harness or a custom agent; sub-agents within one session can each pick a different harness, so an orchestrator can delegate to Claude Code, Codex, or Pi sub-agents and route diffs to a reviewer from a different vendor.
- **Bundled example agents** — **Polly**, a multi-agent coding orchestrator that writes no code itself, plans and delegates to coding sub-agents in parallel git worktrees, then cross-reviews; **Debby**, a dual-headed brainstorming partner (one Claude, one GPT) that answers every question from both models side by side and can `/debate` to converge.
- **Any model, any credential** — first-party API keys, a Claude Pro/Max or ChatGPT subscription via the official CLIs, an OpenAI/Anthropic-compatible gateway (OpenRouter, LiteLLM, Ollama, vLLM, Azure), or a Databricks workspace profile; defaults are scoped per agent and switchable mid-session with `/model`.
- **Remote and cloud sessions** — `omnigent server start` plus `omnigent host` exposes a machine to the web UI; a deployed server with a stable URL (Docker, Render, Fly.io, Railway, Hugging Face Spaces, Modal) makes sessions reachable from a phone anywhere; *managed hosts* can provision a disposable Modal, Daytona, or Islo sandbox per session so no laptop has to stay online.
- **Real-time collaboration** — sessions can be shared (teammates watch and chat live), co-driven (`omnigent attach <session_id>`, a teammate's messages execute on the host machine), or forked (`omnigent run --fork <session_id>`, an independent continuation from the fork point); multi-user accounts with invite-only signup and OIDC SSO (Google/GitHub/Okta/Microsoft) are available on deployed servers.

## Architecture

Omnigent's policy engine evaluates agent actions at specific enforcement points and returns **ALLOW**, **DENY**, or **ASK** (paused for user approval); policies compose and are checked in declaration order, with any DENY short-circuiting the rest. Policies are configurable at three levels with a fixed evaluation order — session (end user, UI settings panel, evaluated first and able to short-circuit) — agent spec (developer, `policies:` in agent YAML, evaluated middle) — server-wide (admin, server config YAML or REST API, evaluated last). Each policy entry is `type: function` with a dotted `handler` import path and optional `factory_params`; builtins cover shell/file-write approval gates, per-session tool-call caps, and hard/soft spend budgets. Users can also just ask the agent in chat to add a policy — Omnigent exposes a built-in `sys_add_policy` tool for this.

The agent unit of configuration is a short YAML file (the **Agent YAML spec**): `name`, `prompt`/`instructions`, `executor` (harness + model + auth), `tools` (MCP servers, Python function tools, or nested sub-agent tools with their own `executor`), `policies`, `os_env` (enables local file/shell tools, scoped by a `sandbox:` block that defaults to the platform-native sandbox — `linux_bwrap` or `darwin_seatbelt`), and optional `terminals`/`async`/`timers` toggles. Sub-agent tools can each select a different harness, which is how Polly mixes Claude Code, Codex, and Pi coders under one orchestrator.

## Example usage

```bash
omnigent run examples/polly/                       # multi-agent coding orchestrator
omnigent run examples/polly/ --harness pi           # same orchestrator, sub-agents on Pi
omnigent run examples/debby/ --harness openai-agents
```

A minimal custom agent:

```yaml
name: hello_agent
prompt: |
  You are a concise assistant. Answer directly and ask a follow-up question when
  the request is ambiguous.

executor:
  harness: claude-sdk
  model: databricks-claude-sonnet-4-6
  auth:
    type: databricks
    profile: oss
```

run with `omnigent run path/to/agent.yaml`.

## When to use

Omnigent fits teams or individuals already using multiple coding-agent CLIs (Claude Code, Codex, Cursor, Pi) who want one governed, device-portable session layer instead of separate ad hoc setups per tool — particularly when cross-vendor code review (one harness writes, a different vendor's harness reviews), phone-reachable sessions, or organization-wide spend/tool policies matter. It is less relevant for a single-harness, single-device workflow with no governance or collaboration requirements, where the underlying CLI alone is simpler.

## Maintenance status

2,073 stars and 257 forks as of fetch, Apache 2.0 licensed, status badge marked "alpha" in the README, no GitHub Releases published yet — development tracked via the `main` branch. Default branch `main`.

## Ecosystem

Built atop existing harnesses rather than competing with them: Claude Code, Codex, Cursor (`cursor-agent`), Pi, and Google's Antigravity SDK (Gemini-native, no Databricks/gateway path) are all first-class `executor.harness` choices. Model access spans first-party API keys, CLI subscriptions, OpenAI/Anthropic-compatible gateways (OpenRouter, LiteLLM, Ollama, vLLM, Azure), and Databricks workspaces. Deployment targets include Docker, Render, Fly.io, Railway, Hugging Face Spaces, and Modal, plus Modal/Daytona/Islo as cloud sandbox providers for *managed hosts*.
