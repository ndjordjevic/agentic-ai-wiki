---
type: source
category: "Browser & web automation"
source_url: https://playwright.dev/agent-cli/introduction
tags:
  - playwright
  - browser-automation
  - cli-tool
  - accessibility-tree
  - token-efficient
  - daemon-architecture
  - agent-skills
  - session-isolation
related:
  - microsoft-playwright-mcp
  - browser-use.com
  - browserbase.com
  - vercel-labs-agent-browser
product: playwright-cli
detail_level: standard
created: 2026-07-14
updated: 2026-07-14
---

Playwright CLI is Microsoft's shell-first alternative to [[microsoft-playwright-mcp|Playwright MCP]] for coding agents: instead of an LLM calling structured MCP tools with schemas and snapshots loaded into context, the agent runs `playwright-cli` shell commands directly, gets back a concise text page-state summary, and picks up an accessibility-tree snapshot file for the next command. Both share the same underlying Playwright automation primitives (organized into the same capability groups), so this is a distribution/interface choice — command-line for large-codebase coding agents versus structured tool calls for exploratory agentic loops — not a competing automation engine.

_All claims below are sourced from ../../raw/web/playwright.dev-agent-cli.md unless otherwise noted._

## What it does

`playwright-cli` runs commands like `open`, `click <ref>`, `type <text>`, `press Enter`, and `screenshot` against a persistent, daemon-managed browser process. After every command it prints the current page state (URL, title) plus a link to a `.playwright-cli/page-<timestamp>.yml` snapshot file containing the accessibility tree with element refs (`e21`-style) for the next interaction — the same ref-based, deterministic-interaction model as Playwright MCP, but delivered as compact CLI output rather than a full snapshot dumped into the model's context on every call. Commands span nine categories: Core (open/click/type/fill/snapshot/screenshot/etc.), Navigation, Keyboard & Mouse, Tabs, Storage (cookies/localStorage/sessionStorage plus full state save/load), Network (request listing and mocking), DevTools (console, tracing, video recording, visual dashboard, test debugging), Sessions, and Config.

## Installation

```bash
npm install -g @playwright/cli@latest       # global
npx playwright-cli --help                    # or run via npx
playwright-cli install-browser --with-deps   # explicit browser install (auto-installs on first use otherwise)
playwright-cli install --skills              # install reference skill files for the coding agent
```
Prerequisites: Node.js 20+ and a coding agent (Claude Code, GitHub Copilot, or similar — Cursor is also listed as a supported skill consumer). The CLI can be used entirely "skills-less" by pointing an agent at `playwright-cli --help` and letting it discover commands on its own, or with the installed skill files for richer structured reference guides. Session targeting is set via `PLAYWRIGHT_CLI_SESSION=<name> claude .` at the environment level. (../../raw/web/playwright.dev-agent-cli.md)

## Key features

- **Token efficiency by design** — concise CLI output avoids loading large tool schemas into the model's context window; skills are loaded on demand rather than always-resident, which the docs position as the core reason to prefer CLI over MCP for coding agents working in large codebases.
- **Daemon architecture** — a persistent browser process means no per-command startup cost, unlike spawning a fresh browser each invocation.
- **Named, isolated sessions** — `playwright-cli -s=<name> open <url>` runs multiple simultaneous browser instances, each with its own cookies, localStorage, navigation history, and console log; useful for parallel admin/user test flows in one agent run.
- **Visual dashboard** (`playwright-cli show`) — a session grid with live screencast per session plus a zoomed-in detail view with full remote mouse/keyboard control, explicitly intended for a human to watch an agent automate in the background and take over when it's stuck on a CAPTCHA or 2FA prompt.
- **Vision mode** — coordinate-based mouse interaction (`mousemove`, `mousedown`, `mousewheel`) using pixel positions from screenshots, for canvas apps, maps, and custom widgets that don't expose accessible elements.
- **Profile persistence options** — in-memory (default, lost on browser close), persistent-to-disk (survives restarts, same default locations as Playwright MCP's persistent mode), or a custom `--profile=<path>` directory.
- **Testing primitives built in** — `verify-element-visible`, `verify-text-visible`, `verify-list-visible`, `verify-value`, and `generate-locator` (Playwright locator generation from an interaction) ship as first-class commands, not a separate add-on.

## Architecture and concepts

The CLI and MCP share the same underlying Playwright tools; the docs explicitly note the CLI exposes them all with no capability gating (MCP-style clients often scope which capability groups are available). The core interaction loop is open → snapshot → interact-by-ref → re-snapshot: every state-changing command returns a fresh accessibility-tree snapshot with new refs, so the agent never has to guess whether a previous ref is stale. Skills are the discovery mechanism — `playwright-cli install --skills` drops structured reference guides (covering test running/debugging, request mocking, running arbitrary Playwright code, session management, storage state, test generation, tracing, video recording, and element-attribute inspection) into the agent's skill directory, separate from the CLI binary itself. (../../raw/web/playwright.dev-agent-cli.md)

## Main APIs

There is no HTTP/RPC API — the interface is the `playwright-cli` shell command itself, organized by capability group: Core (`open`, `click`, `type`, `fill`, `snapshot`, `screenshot`, `eval`/`run-code`, `resize`, dialog handling), Network (`network`, `route`, `route-list`, `unroute`), Storage (`state-save`/`state-load`, cookie/localStorage/sessionStorage CRUD), Vision (`mousemove`, `mousedown`/`mouseup`, `mousewheel`), DevTools (`console`, `tracing-start`/`tracing-stop`, `video-start`/`video-stop`, `show`, `pause-at`/`resume`/`step-over`), PDF (`pdf`), and Testing (`verify-*`, `generate-locator`). Full command reference at `playwright.dev/agent-cli/commands/*`. (../../raw/web/playwright.dev-agent-cli.md)

## When to use

The docs' own comparison table frames it directly: prefer **Playwright CLI** for coding agents (Claude Code, GitHub Copilot) working inside large codebases where token budget matters and headless-by-default execution is fine; prefer **[[microsoft-playwright-mcp|Playwright MCP]]** for specialized agentic loops and exploratory automation where structured tool-call parameters and headed-by-default behavior are more useful. Both are viable for the same underlying browser-automation tasks — the choice is about how the agent's runtime prefers to consume tools (shell commands vs. MCP tool calls) and how much context budget is available.

## Ecosystem

Sits directly beside [[microsoft-playwright-mcp]] as a second interface onto the same Playwright automation engine from the same vendor, rather than competing with browser-automation platforms like [[browser-use.com]] or [[browserbase.com]] (which target different automation models — Python-agent-driven and cloud-hosted-browser respectively). The accessibility-tree-snapshot approach and ref-based interaction model matches [[microsoft-playwright-mcp]]'s design closely enough that documentation, capability groups, and even default persistent-profile paths are explicitly shared between the two.
