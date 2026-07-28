---
type: source
category: "Model infra, ML & providers"
source_url: https://github.com/router-for-me/CLIProxyAPI
tags:
  - cli-oauth-proxy
  - openai-compatible
  - claude-compatible
  - multi-account-load-balancing
  - api-gateway
  - go
  - embeddable-sdk
related:
  - litellm.ai
  - openrouter.ai
  - mozilla-ai-any-llm
product: CLIProxyAPI
detail_level: standard
created: 2026-07-28
updated: 2026-07-28
---

CLIProxyAPI is a Go proxy server (45,200+ stars) that turns OAuth-authenticated CLI subscriptions — Claude Code, ChatGPT Codex, Antigravity (Gemini), Grok Build, and Kimi — into OpenAI/Gemini/Claude/Codex-compatible API endpoints, so any existing OpenAI/Gemini/Claude-compatible client or SDK can call those models locally without separate API keys. It differs from provider-abstraction gateways like [[litellm.ai]] or [[openrouter.ai]] in mechanism, not just API surface: rather than routing paid API-key traffic across providers, it authenticates via each provider's own CLI OAuth flow and load-balances requests across multiple logged-in accounts per provider. See [[router-for-me-CLIProxyAPI]].

_All claims below are sourced from ../../raw/github/router-for-me-CLIProxyAPI.md unless otherwise noted._

## What it does

Provides OpenAI, Gemini, Claude, Codex, and Grok compatible API endpoints backed by CLI-tool OAuth logins rather than API keys — OpenAI Codex support via OAuth, Claude Code support via OAuth, Grok Build support via OAuth, and Kimi via OAuth or compatible API interfaces. Supports streaming, non-streaming, and WebSocket responses where the upstream allows it, function calling/tools, and multimodal (text + image) input. Multiple accounts per provider (Gemini, OpenAI, Claude, Grok) are pooled with round-robin load balancing, and OpenAI-compatible upstream providers (e.g. OpenRouter) can also be configured as additional backends.

## Installation

Distributed as prebuilt releases and a Docker image (`Dockerfile`, `docker-compose.yml`, and a clustered variant `docker-compose.cluster.yml`); configuration lives in `config.yaml` (template `config.example.yaml`), with `.env` auto-loaded from the working directory and OAuth auth material stored under `auths/`. Storage defaults to the filesystem, with optional Postgres/git/object-store backends (`PGSTORE_*`, `GITSTORE_*`, `OBJECTSTORE_*` env prefixes). Full setup guides live at help.router-for.me; the Management API is documented separately.

## Key features

- Multi-account round-robin load balancing per provider (Gemini, OpenAI, Claude, Grok), plus AI Studio Build and OpenAI Codex multi-account load balancing specifically.
- A reusable, embeddable Go SDK (`sdk/cliproxy/`) so other Go programs can embed the proxy directly rather than shelling out to a separate process; documented in `docs/sdk-usage.md`, `docs/sdk-advanced.md` (executors & translators), and `docs/sdk-access.md`.
- Built-in usage statistics were removed as of v6.10.0; the project instead points to third-party companion tools — CPA Usage Keeper (SQLite persistence + dashboard) and CPA-Manager-Plus (request-level monitoring, cost estimation with LiteLLM price sync, Codex account-pool quota/health management).
- A large downstream ecosystem of GUI wrappers and companion tools has grown around it (see Ecosystem), most focused on multi-account quota tracking and one-click OAuth setup for desktop/menu-bar use.

## Architecture

Built as a "canonical representation → per-provider translation" system, most explicit in `internal/thinking/`: `ApplyThinking()` parses reasoning-effort suffixes, normalizes them into a canonical `ThinkingConfig`, validates centrally, then applies provider-specific output via a `ProviderApplier` — a pattern the project's own `AGENTS.md` explicitly protects against being broken. The Gin-based HTTP API lives in `internal/api/` (including an Amp-style integration module); `internal/runtime/executor/` holds per-provider runtime executors (including a Codex WebSocket executor); `internal/translator/` holds the provider protocol translators; `internal/registry/` runs a model registry with a remote updater (disableable via `--local-model`); and `internal/tui/` provides a Bubbletea terminal UI (`--tui`, `--standalone` flags). Timeouts are deliberately restricted to the credential-acquisition phase — the project's coding conventions forbid setting timeouts on already-established upstream connections outside a small, explicitly documented allowlist (Codex websocket liveness, wsrelay session deadlines, one management API call, and one utility script).

## Example usage

```bash
go build -o cli-proxy-api ./cmd/server   # build
go run ./cmd/server                       # run dev server
./cli-proxy-api --config config.yaml --tui   # run with terminal UI
```

Common flags: `--config <path>`, `--tui`, `--standalone`, `--local-model`, `--no-browser`, `--oauth-callback-port <port>`. Once running, any OpenAI/Gemini/Claude-compatible client points at the local endpoint instead of the provider's own API.

## When to use

Fits developers who already pay for CLI-tool subscriptions (Claude Code, ChatGPT Codex, Antigravity, Grok Build, Kimi Code) and want to reuse that access through a standard API surface — for building custom tools, embedding in other coding agents, or pooling several accounts for higher effective throughput — without provisioning separate metered API keys. Less relevant if the goal is provider abstraction over paid API keys across many vendors (see [[litellm.ai]], [[openrouter.ai]], [[mozilla-ai-any-llm]] instead), since CLIProxyAPI's core value is OAuth-based CLI-subscription reuse rather than key management.

## Maintenance status

45,243 stars, 7,041 forks, MIT licensed, Go, default branch `main`, actively released — latest tag v7.2.103 as of 2026-07-27, one day before this fetch. Heavy sponsorship activity (multiple paid API-relay affiliate partners listed in the README) and a large "who is with us" list of downstream GUI/tray/dashboard projects indicate an active, commercially adjacent ecosystem rather than a purely hobbyist project.

## Ecosystem

Spawned a substantial downstream project list documented in the README's "Who is with us?" and "More choices" sections: native desktop/menu-bar wrappers (vibeproxy, Quotio and its Tauri port Quotio Desktop, ZeroLimit, ProxyPal, AIUsage, CLIProxy Pool Watch), Windows tray/PowerShell launchers (CLIProxyAPI Tray, CPA-Tray-Powershell), web dashboards (CLIProxyAPI Dashboard, CPA-XXX Panel), editor integrations (Claude Proxy VSCode, Universal Chat Provider for VS Code/Copilot Chat), an MCP server (Grok Search MCP) built on top of a CLIProxyAPI deployment, and several independent forks/reimplementations (9Router, OmniRoute, Playful Proxy API Panel). Companion projects also cover multi-agent orchestration (Panopticon) and Claude Code model-switching (CCS, Claude Dialects). Positioned in this wiki's provider/gateway cluster alongside [[litellm.ai]], [[openrouter.ai]], and [[mozilla-ai-any-llm]], though its OAuth-CLI-account mechanism (rather than API-key routing) is a distinct architectural approach to the same "one endpoint, many models" problem.
