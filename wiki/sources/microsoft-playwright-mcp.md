---
type: source
source_url: https://github.com/microsoft/playwright-mcp
tags: [mcp-server, browser-automation, playwright, accessibility-tree, llm-tool, model-context-protocol, typescript, nodejs, headless-browser, web-scraping]
related: []
product: playwright-mcp
detail_level: standard
created: 2026-04-27
updated: 2026-04-27
---

`microsoft/playwright-mcp` is an official Microsoft MCP (Model Context Protocol) server that gives AI agents full browser automation capabilities via [Playwright](https://playwright.dev), using structured accessibility snapshots rather than pixel-based screenshots. With 31k+ stars and Apache 2.0 license, it is the canonical way to wire browser interaction into any MCP-compatible AI agent, enabling LLMs to click, type, navigate, fill forms, and inspect pages without needing vision models.

_All claims below are sourced from ../../raw/github/microsoft-playwright-mcp.md unless otherwise noted._

## What it does

Playwright MCP exposes Playwright's browser automation as MCP tools. An LLM client (Claude Desktop, VS Code, Cursor, Copilot, Cline, Goose, etc.) connects to the server; the server launches a browser and handles tool calls like `browser_click`, `browser_navigate`, `browser_snapshot`. The accessibility tree is the primary interface — not screenshots — making the system fast, deterministic, and usable without vision models.

Notable distinction: the README explicitly positions MCP for *stateful, exploratory, long-running* agentic workflows, while recommending the CLI+SKILLS pattern (separate package: `microsoft/playwright-cli`) for *coding agents* that need token efficiency.

## Installation

```js
// Standard config (works in most MCP clients)
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["@playwright/mcp@latest"]
    }
  }
}
```

Installable via one-click buttons in VS Code, Cursor, and Goose; via CLI in Claude Code (`claude mcp add playwright npx @playwright/mcp@latest`), Copilot (`/mcp add`), Codex, Factory, and others.

## Key features

- **Accessibility-tree-first** — `browser_snapshot` returns a structured ARIA tree; no screenshots needed for navigation and interaction.
- **Broad client support** — VS Code, Cursor, Windsurf, Claude Desktop, Goose, Junie, Warp, LM Studio, Copilot, Cline, Codex, Kiro, opencode, Gemini CLI, and many others.
- **Multiple browser profiles** — Persistent (default), Isolated (in-memory), or connected to existing browser via Chrome Extension.
- **Extensive configuration** — 30+ CLI options, JSON config file, environment variable overrides for every option.
- **Opt-in capability sets** — Additional tools unlocked via `--caps=vision|pdf|devtools|storage|network|testing|config`.
- **Standalone server mode** — `--port <N>` enables HTTP/SSE transport for headless environments or Docker.
- **Docker support** — Official `mcr.microsoft.com/playwright/mcp` image for containerized deployments.
- **Code generation** — Can generate TypeScript Playwright test code from interactions (`--codegen typescript`).

## Architecture and concepts

The server wraps Playwright's `BrowserContext` in an MCP-compliant tool surface. Key design choices:

- **Accessibility tree over pixels** — all interaction tools reference elements by ARIA role/name or `ref` IDs from `browser_snapshot`, not coordinates (coordinates are opt-in via `--caps=vision`).
- **Deterministic tool application** — element refs are stable within a snapshot, avoiding the ambiguity of coordinate-based clicking.
- **Workspace-scoped profiles** — persistent profile is hashed from the MCP client's workspace root, so different projects automatically get separate browser states.
- **Atomic session model** — isolated mode starts a fresh context per session; persistent mode retains cookies and localStorage across sessions.

## Main APIs (tool groups)

| Group | Example tools |
|---|---|
| Core automation | `browser_navigate`, `browser_click`, `browser_type`, `browser_snapshot`, `browser_fill_form`, `browser_evaluate`, `browser_wait_for` |
| Screenshots | `browser_take_screenshot` |
| Tabs | `browser_tabs` |
| Network (opt-in) | `browser_route` (mock), `browser_network_requests`, `browser_network_state_set` |
| Storage (opt-in) | cookie/localStorage/sessionStorage CRUD, `browser_storage_state` |
| DevTools (opt-in) | tracing, video recording, highlight, pick locator, step debugger |
| Vision (opt-in) | coordinate-based mouse click/drag/move/wheel |
| PDF (opt-in) | `browser_pdf_save` |
| Testing (opt-in) | `browser_generate_locator`, `browser_verify_*` assertions |

## When to use

Use Playwright MCP for AI agents that need:
- Persistent stateful browser sessions (login once, work across many pages)
- Exploratory automation where the agent reasons about page structure
- Self-healing test automation
- Long-running autonomous web workflows

Use the CLI+SKILLS pattern instead when running high-throughput coding agents where token efficiency matters more than rich page introspection.

## Ecosystem

- Published as `@playwright/mcp` on npm
- Companion package: `@playwright/mcp` (programmatic API via `createConnection`)
- Official Docker image: `mcr.microsoft.com/playwright/mcp`
- v0.0.70 (latest release, ~26 days ago); TypeScript; Apache 2.0
