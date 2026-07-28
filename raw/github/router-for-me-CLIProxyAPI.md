# router-for-me/CLIProxyAPI

## Metadata
- Stars: 45243
- Primary language: Go
- Default branch: main
- Latest release: v7.2.103 (2026-07-27)
- License: MIT License
- Homepage: (none listed)
- Fetched: 2026-07-28
- Final URL: https://github.com/router-for-me/CLIProxyAPI

## Description
Wrap Antigravity, ChatGPT Codex, Claude Code, Grok Build as an OpenAI/Gemini/Claude/Codex compatible API service, allowing you to enjoy the free Gemini 3.1 Pro, GPT 5.5, Grok 4.3, Claude model through API

## README

# CLI Proxy API

A proxy server that provides OpenAI/Gemini/Claude/Codex/Grok compatible API interfaces for CLI.

You can access the following providers locally and with multiple CLI accounts through any OpenAI (including Responses), Gemini (including Interactions), or Claude-compatible client or SDK.

Supported providers (per the README's provider table):
- **Kimi** — Kimi series models (Kimi K3, Kimi K2.7 Code, etc.), via OAuth or compatible API interfaces.
- **OpenAI** — GPT series models (GPT 5.6, GPT 5.5, etc.).
- **Anthropic** — Claude series models (Claude Fable, Claude Opus, Claude Sonnet, etc.).
- **Google (Antigravity)** — Gemini series models (Gemini 3.5 Flash, Gemini 3.1 Pro, etc.).
- **xAI** — Grok series models (Grok 4.5, Grok Composer 2.5 Fast, etc.).

The README lists a large number of paid sponsor/relay-service ads (PackyCode, AICodeMirror, BmoPlus, VisionCoder, APIKEY.FUN, RunAPI, CyberPay, Claude API, code0, FennoAI, Qiniu Cloud AI, Cubence, FastAIToken) — commercial third-party API relay/account providers, omitted here as non-substantive to the project's own functionality.

### Overview

- OpenAI/Gemini/Claude/Grok compatible API endpoints for CLI models
- OpenAI Codex support (GPT models) via OAuth login
- Claude Code support via OAuth login
- Grok Build support via OAuth login
- Streaming, non-streaming, and WebSocket responses where supported
- Function calling/tools support
- Multimodal input support (text and images)
- Multiple accounts with round-robin load balancing (Gemini, OpenAI, Claude, Grok)
- Simple CLI authentication flows (Gemini, OpenAI, Claude, Grok)
- Generative Language API Key support
- AI Studio Build multi-account load balancing
- Claude Code multi-account load balancing
- OpenAI Codex multi-account load balancing
- Grok Build multi-account load balancing
- OpenAI-compatible upstream providers via config (e.g., OpenRouter)
- Reusable Go SDK for embedding the proxy (see `docs/sdk-usage.md`)

### Getting Started

CLIProxyAPI Guides: https://help.router-for.me/

### Management API

See https://help.router-for.me/management/api

### Usage Statistics

Since v6.10.0, CLIProxyAPI and CPAMC (Cli-Proxy-API-Management-Center) no longer ship built-in usage statistics. Third-party options:

- **CPA Usage Keeper** (github.com/Willxup/cpa-usage-keeper) — standalone persistence and visualization service, periodic data sync, SQLite storage, aggregate APIs, built-in dashboard.
- **CPA-Manager-Plus** (github.com/seakee/CPA-Manager-Plus) — full management center with request-level monitoring and cost estimates, tracks by account/model/channel/latency/status/tokens, editable model prices with one-click LiteLLM price sync, SQLite persistence, Codex account-pool operations (batch inspection, quota detection, unhealthy-account discovery, cleanup).

### SDK Docs

- Usage: `docs/sdk-usage.md`
- Advanced (executors & translators): `docs/sdk-advanced.md`
- Access: `docs/sdk-access.md`
- Watcher: `docs/sdk-watcher.md`
- Custom Provider Example: `examples/custom-provider`

### Who is with us? (downstream projects built on CLIProxyAPI)

- **vibeproxy** — native macOS menu bar app for Claude Code & ChatGPT subscriptions with AI coding tools, no API keys.
- **Subtitle Translator** — cross-platform SRT subtitle translation/validation via existing LLM subscriptions.
- **CCS (Claude Code Switch)** — CLI wrapper for instant switching between multiple Claude accounts and alternative models (Gemini, Codex, Antigravity) via OAuth.
- **Quotio** — native macOS menu bar app unifying Claude/Gemini/OpenAI/Antigravity subscriptions with real-time quota tracking and smart auto-failover.
- **ProxyPilot** — Windows-native fork with TUI, system tray, multi-provider OAuth.
- **Claude Proxy VSCode** — VSCode extension for switching Claude Code models with integrated CLIProxyAPI backend.
- **ZeroLimit** — Windows desktop app (Tauri + React) for monitoring AI coding-assistant quotas across Gemini, Claude, OpenAI Codex, Antigravity.
- **CPA-XXX Panel** — lightweight web admin panel with health checks, resource monitoring, real-time logs, auto-update, request stats, pricing display.
- **CLIProxyAPI Tray** — Windows PowerShell tray app: shortcuts, silent running, password management, channel switching, auto-update.
- **霖君 (LinJun)** — cross-platform desktop app for unified management of Claude Code, Gemini, OpenAI Codex with local proxy multi-account quota tracking.
- **CLIProxyAPI Dashboard** — Next.js/React/PostgreSQL web dashboard: real-time log streaming, config editing, API key management, OAuth integration, usage analytics, container management.
- **All API Hub** — browser extension for New API-compatible relay-site account management, integrates via the Management API.
- **Shadow AI** — AI assistant tool for restricted environments, stealthy operation, cross-device Q&A via LAN.
- **ProxyPal** — cross-platform desktop app (macOS/Windows/Linux) wrapping CLIProxyAPI with native GUI, usage analytics, auto-configuration.
- **CLIProxyAPI Quota Inspector** — cross-platform quota inspector: per-account Codex 5h/7d quota windows, plan-based sorting, status coloring.
- **CLIProxy Pool Watch** — native macOS SwiftUI app for monitoring ChatGPT/Codex account quotas in pools.
- **Panopticon** — multi-agent orchestration for AI coding assistants, runs CLIProxyAPI as a local sidecar.
- **Tunnel Agent** — Windows desktop UI managing CLIProxyAPI and a Perplexity WebUI scraper from one interface.
- **Quotio Desktop** — cross-platform (Tauri) port of Quotio; manages a pool of AI accounts across many providers with quota bars, rate-limit reset credits, smart scheduling.
- **Universal Chat Provider** — VS Code extension bringing Claude/ChatGPT-Codex/Antigravity/Grok/Kimi subscriptions into GitHub Copilot Chat as native language models; runs CLIProxyAPI in a managed background lifecycle.
- **CPA-Tray-Powershell** — PowerShell Windows system-tray launcher with background running, update checking, SHA-256 verification/rollback.
- **Grok Search MCP** — HTTP-only MCP server using a CLIProxyAPI deployment for Grok-powered web/X search and model discovery.
- **AIUsage** — native macOS SwiftUI dashboard managing official CLIProxyAPI releases end to end, unifies OAuth accounts and live models.
- **Claude Dialects** — runs multiple native-feeling Claude Code commands each powered by a different model (Codex, GLM, Kimi, Gemini, Grok, MiniMax, DeepSeek, Cursor, Copilot, Claude) via an embedded CLIProxyAPI instance linked through the Go SDK; macOS only.

### More choices (ports of / projects inspired by CLIProxyAPI)

- **9Router** — Next.js implementation inspired by CLIProxyAPI: format translation (OpenAI/Claude/Gemini/Ollama), combo system with auto-fallback, multi-account management with exponential backoff, web dashboard.
- **OmniRoute** — AI gateway for multi-provider LLMs with smart routing, load balancing, retries, fallbacks, policies, rate limits, caching, observability.
- **Playful Proxy API Panel (PPAP)** — public CLIProxyAPI-compatible fork with bundled management panel, restores built-in usage statistics, cache hit rate, first-byte latency, TPS tracking.
- **Codex Switch** — Tauri 2 + Vue 3 tool for managing multiple OpenAI Codex desktop accounts, quota checking, token health verification.

### License

MIT License.

## Docs

### AGENTS.md (agent-instructions file, fetched in full)

Go 1.26+ proxy server providing OpenAI/Gemini/Claude/Codex compatible APIs with OAuth and round-robin load balancing.

**Commands:**
```bash
gofmt -w . # Format (required after Go changes)
go build -o cli-proxy-api ./cmd/server # Build
go run ./cmd/server # Run dev server
go test ./... # Run all tests
go test -v -run TestName ./path/to/pkg # Run single test
go build -o test-output ./cmd/server && rm test-output # Verify compile (REQUIRED after changes)
```
Common flags: `--config <path>`, `--tui`, `--standalone`, `--local-model`, `--no-browser`, `--oauth-callback-port <port>`.

**Config:** default config `config.yaml` (template `config.example.yaml`); `.env` auto-loaded from the working directory; auth material defaults under `auths/`; storage backends are file-based by default with optional Postgres/git/object-store backends (`PGSTORE_*`, `GITSTORE_*`, `OBJECTSTORE_*`).

**Architecture:**
- `cmd/server/` — server entrypoint
- `internal/api/` — Gin HTTP API (routes, middleware, modules), including `internal/api/modules/amp/` for Amp-style routes + reverse proxy
- `internal/thinking/` — main thinking/reasoning pipeline: `ApplyThinking()` parses suffixes, normalizes to a canonical `ThinkingConfig`, validates centrally, then applies provider-specific output via a `ProviderApplier` — a "canonical representation → per-provider translation" architecture the project explicitly protects
- `internal/runtime/executor/` — per-provider runtime executors (including a Codex WebSocket executor)
- `internal/translator/` — provider protocol translators (plus shared `common`)
- `internal/registry/` — model registry + remote updater (`StartModelsUpdater`); `--local-model` disables remote updates
- `internal/store/` — storage implementations and secret resolution
- `internal/managementasset/` — config snapshots and management assets
- `internal/cache/` — request signature caching
- `internal/watcher/` — config hot-reload and watchers
- `internal/wsrelay/` — WebSocket relay sessions
- `internal/usage/` — usage and token accounting
- `internal/tui/` — Bubbletea terminal UI (`--tui`, `--standalone`)
- `sdk/cliproxy/` — embeddable SDK entry (service/builder/watchers/pipeline)
- `test/` — cross-module integration tests

**Code conventions:** keep changes small and simple (KISS); comments in English only (translate existing non-English comments when touched, don't add new ones); user-visible strings keep the file's existing language; new Markdown docs in English unless the file is explicitly language-specific (e.g. `README_CN.md`); no standalone changes to `internal/translator/` without write/maintain/admin permission (otherwise file an issue instead); `internal/runtime/executor/` holds only executors and their unit tests, helpers go under `internal/runtime/executor/helps/`; follow `gofmt`/goimports; wrap errors with context; never `log.Fatal`/`log.Fatalf` in request paths (return errors, log via logrus); shadowed variables use a method suffix (`errStart := server.Start()`); wrap defer errors; use structured logrus logging without leaking secrets/tokens; avoid panics in HTTP handlers; timeouts are allowed only during credential acquisition — no timeouts on established upstream connections except a documented, explicit allowlist (Codex websocket liveness deadlines, wsrelay session deadlines, the management API-call timeout, and the `cmd/fetch_antigravity_models` utility).

## Top-level structure

- `.dockerignore`, `.env.cluster.example`, `.env.example`, `.gitignore` — config/boilerplate
- `.github/` — CI workflows (boilerplate, not fetched)
- `AGENTS.md`, `CLAUDE.md` — agent-instructions files (AGENTS.md fetched in full above; CLAUDE.md not separately fetched — likely a companion pointer file)
- `Dockerfile`, `docker-build.ps1`, `docker-build.sh`, `docker-compose.cluster.yml`, `docker-compose.yml` — containerized deployment (including a clustered compose variant)
- `LICENSE` — MIT
- `README.md`, `README_CN.md`, `README_JA.md` — English/Chinese/Japanese project overviews
- `assets/` — logos and sponsor images
- `auths/` — default location for OAuth/auth material
- `cmd/` — entrypoints (`cmd/server/` is the main server binary)
- `config.example.yaml` — configuration template
- `docs/` — SDK usage/advanced/access/watcher guides (English + Chinese variants)
- `examples/` — including `examples/custom-provider`
- `go.mod`, `go.sum` — Go module files
- `internal/` — the bulk of the implementation (api, thinking, runtime/executor, translator, registry, store, managementasset, cache, watcher, wsrelay, usage, tui — see AGENTS.md architecture notes above)
- `sdk/` — `sdk/cliproxy/`, the embeddable Go SDK
- `test/` — cross-module integration tests
