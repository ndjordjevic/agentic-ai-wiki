---
type: source
source_url: https://github.com/vercel-labs/agent-browser
tags:
  - browser-automation
  - ai-agents
  - rust-cli
  - accessibility-tree
  - cdp
  - snapshot-ref-workflow
  - agent-skills
  - serverless
related:
  - microsoft-playwright-mcp
  - browse.sh
  - qa.tech
  - skills.sh
product: agent-browser
detail_level: standard
created: 2026-05-25
updated: 2026-05-25
---

agent-browser is Vercel Labs' open-source, native Rust CLI for browser automation built specifically for AI agents (34,229 stars, Apache-2.0, v0.27.0). Rather than wrapping Playwright or Puppeteer, it implements its own CDP client in pure Rust, launching a background daemon that persists across commands so agents pay zero startup overhead per interaction. Its central abstraction is the **snapshot/ref workflow**: a single `agent-browser snapshot -i` call returns an accessibility-tree summary with compact `@eN` ref handles (~200–400 tokens vs raw HTML), which the agent then uses in deterministic `click @e2` or `fill @e3 "text"` calls. Refs are stable within a page state and deliberately stale across navigations, forcing a re-snapshot pattern that prevents stale-element errors.

_All claims below are sourced from ../../raw/github/vercel-labs-agent-browser.md unless otherwise noted._

## What it does

agent-browser provides a command-line interface that AI agents invoke with shell tool calls to control a Chrome/Chromium browser. The daemon starts automatically on first command and remains running between commands for fast subsequent operations. The key agent-facing primitives are:

- **Snapshot** (`snapshot -i`, `snapshot -i --json`) — dumps accessible interactive elements as `@eN` ref handles; the JSON form is designed for LLM parsing
- **Navigation** (`open <url>`, `wait --load networkidle`) — page load with configurable wait strategies
- **Interaction** (`click`, `fill`, `type`, `select`, `hover`, `drag`, `press`, `check`, `uncheck`, `upload`) — all take `@eN` refs or CSS/XPath/semantic locators
- **Extraction** (`get text/html/attr/value/title/url/count`) — read page state without screenshots
- **Screenshots** (`screenshot <file>`) — PNG capture for visual inspection
- **Tabs** (`tab new`, `tab list`, `tab close`, `click --new-tab`) — multi-tab sessions
- **Streaming** (`stream status/enable/disable`) — WebSocket viewport stream on an OS-assigned port for live "pair browsing" alongside an agent

## Key features

- **Zero Playwright/Puppeteer dependency** — direct CDP (Chrome DevTools Protocol) in Rust; ~684 MB Chrome for Testing download is a one-time `agent-browser install` step
- **Snapshot/ref workflow** — accessibility tree in ~200–400 tokens; refs become stale on page change, enforcing correct re-snapshot discipline
- **`--json` flag on every command** — machine-readable output for all commands, enabling clean LLM tool-call integration
- **Headed mode** (`--headed`) — visible browser window for debugging
- **Authenticated sessions** — per-origin `--headers` for auth token injection without UI login; `set headers` for global headers
- **Custom executable** — `AGENT_BROWSER_EXECUTABLE_PATH` / `--executable-path` for @sparticuz/chromium (serverless ~50 MB), system Chrome, or custom builds
- **CDP connect / auto-connect** — attach to any running Chrome by port, WebSocket URL, or automatic discovery from `DevToolsActivePort`
- **Local file access** — `--allow-file-access` flag for `file://` URLs (PDFs, local HTML)
- **iOS Simulator** — `agent-browser -p ios` provider using Appium + XCUITest for real Mobile Safari testing
- **AWS AgentCore** — `agent-browser -p agentcore` connects to Bedrock-managed cloud browser sessions with persistent profiles
- **SKILL.md integration** — `npx skills add vercel-labs/agent-browser` installs a runtime-loaded skill (Claude Code, Cursor, Codex, GitHub Copilot, Gemini CLI, Goose, OpenCode, Windsurf)

## Architecture

agent-browser is a Rust monorepo using a client-daemon architecture. The **Rust CLI** (`cli/`) parses commands and communicates with the daemon over a local socket. The **Rust daemon** (`cli/src/native/`) manages the Chrome browser via direct CDP — no Node.js runtime in the hot path. The daemon starts automatically and persists between commands; `AGENT_BROWSER_IDLE_TIMEOUT_MS` sets an inactivity shutdown timer.

The `skill-data/core/` directory contains the agent-facing SKILL.md and eight reference files (`commands.md`, `snapshot-refs.md`, `authentication.md`, `session-management.md`, `proxy-support.md`, `trust-boundaries.md`, `video-recording.md`, `profiling.md`). The skill is intentionally split into a thin discovery stub (installed via `npx skills add`) that redirects agents to `agent-browser skills get core` at runtime, ensuring instructions always match the installed CLI version. The `packages/dashboard/` monorepo package adds a Web UI (shadcn/ui, TypeScript) for interactive monitoring.

Engine selection (`--engine chrome|lightpanda`) and the `--cdp` flag (port or `wss://…` WebSocket) give operators flexibility to attach to any Chromium-compatible backend — including Electron apps, WebView2 applications, and remote cloud browser services. The WebSocket streaming server runs on every session for live viewport previews.

## Installation

```bash
npm install -g agent-browser
agent-browser install  # one-time Chrome download

# Or project-local:
npm install agent-browser
npx agent-browser install
```

For serverless environments, supply a lightweight Chromium:

```bash
# Vercel Sandbox (microVM, no binary install needed)
# AWS Lambda with @sparticuz/chromium (~50 MB):
AGENT_BROWSER_EXECUTABLE_PATH=$(node -e "require('@sparticuz/chromium').executablePath().then(console.log)") \
  agent-browser open https://example.com
```

For AI coding assistants:

```bash
npx skills add vercel-labs/agent-browser
```

## Example usage

```bash
# Core snapshot-and-ref loop
agent-browser open https://example.com
agent-browser snapshot -i                          # discover refs
agent-browser fill @e3 "user@example.com"
agent-browser click @e5
agent-browser wait --load networkidle
agent-browser snapshot -i --json                   # re-snapshot for LLM

# Chain commands (daemon persists across &&)
agent-browser open https://example.com && agent-browser wait --load networkidle && agent-browser screenshot page.png

# Authenticated session
agent-browser open api.example.com --headers '{"Authorization": "Bearer <token>"}'
agent-browser snapshot -i --json

# CDP connect to running Chrome
agent-browser connect 9222
agent-browser snapshot -i

# iOS Simulator
agent-browser -p ios --device "iPhone 16 Pro" open https://example.com
agent-browser -p ios snapshot -i
agent-browser -p ios tap @e1

# AgentCore cloud browser
export AGENT_BROWSER_PROVIDER=agentcore
agent-browser open https://example.com
```

## When to use

Use agent-browser when an AI agent needs to interact with a live web browser — login flows, form submission, SPA navigation, screenshot capture, or multi-tab workflows — particularly in environments where a lightweight native Rust binary is preferred over Node.js-based Playwright. It is well suited to:

- AI coding agents (Claude Code, Cursor, Codex) that need browser testing in CI or a sandbox
- Serverless functions on Vercel or AWS Lambda where binary size matters (`@sparticuz/chromium` support)
- Electron app automation via CDP attach
- Mobile Safari testing via iOS Simulator provider
- "Pair browsing" scenarios where a human watches via WebSocket stream while an agent drives

Prefer [[microsoft-playwright-mcp]] when the agent runtime already speaks MCP and you want Playwright's full cross-browser (Chromium, Firefox, WebKit) and test-generation tooling. Prefer [[browse.sh]] when working with a catalog of site-specific skills that encode domain-specific API shortcuts to avoid browser rendering entirely.

## Ecosystem

- **skills.sh / npx skills**: agent-browser publishes its SKILL.md through the [[skills.sh]] ecosystem; it appears on the skills.sh leaderboard
- **AWS AgentCore**: first-party `agentcore` provider integrates with Amazon Bedrock's cloud browser service
- **Vercel Sandbox**: first-party `vercel-sandbox` skill and examples for deploying browser automation in Vercel's serverless microVMs
- **Electron**: dedicated `skill-data/electron/` for CDP-based Electron app control
- **Slack automation**: `skill-data/slack/` provides a site-specific skill for Slack web UI interaction
- **evals/**: evaluation harness included in the repo for benchmarking agent task completion with agent-browser
