---
type: source
category: "Browser & web automation"
source_url: https://github.com/microsoft/playwright-mcp
tags:
  - mcp-server
  - browser-automation
  - playwright
  - accessibility-tree
  - llm-tools
  - typescript
  - microsoft
  - web-testing
related:
  - sequentialthinking-mcp
  - strandsagents.com
  - qa.tech
  - vercel-labs-agent-browser
  - browserbase.com
  - browser-use.com
  - deepwiki.com
  - usestrix-strix
  - sentry.io
  - mcp.sentry.dev
  - teng-lin-notebooklm-py
  - firecrawl.dev
  - integuru.com
  - playwright.dev-agent-cli
product: playwright-mcp
detail_level: standard
created: 2026-05-25
updated: 2026-07-14
---

Playwright MCP is Microsoft's official Model Context Protocol server that gives LLMs structured browser automation capabilities — navigating pages, clicking elements, filling forms, taking snapshots, running scripts, and generating tests — without requiring vision models or screenshot parsing. Instead of pixel-based input, it exposes Playwright's accessibility tree as a deterministic structured representation that any LLM can reason over reliably. With 32,980 stars and active development (v0.0.75, Apache-2.0), it is the dominant MCP tool for web automation in agentic pipelines.

_All claims below are sourced from ../../raw/github/microsoft-playwright-mcp.md unless otherwise noted._

## What it does

Playwright MCP exposes browser control as a set of MCP tools that an LLM can call: navigate to URLs, click and type on elements, take accessibility-tree snapshots, run JavaScript, upload files, manage browser state, capture console messages, record network activity, generate test locators, assert element visibility, record video and traces, and save PDFs. The server runs as an `npx @playwright/mcp@latest` process and connects to any MCP-compatible client over stdio or HTTP/SSE transport.

The fundamental design choice is to use Playwright's accessibility tree rather than screenshots. This makes tool calls deterministic (element targets come from the tree's stable node references), LLM-friendly (no vision model required), and token-efficient (a structured tree is far smaller than a screenshot blob). Coordinate-based input (`--caps=vision`) is opt-in for cases where the accessibility tree is insufficient.

## Installation

The standard one-liner installs it into any MCP client:

```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["@playwright/mcp@latest"]
    }
  }
}
```

Client-specific setup is documented in the README for VS Code, Cursor, Windsurf, Claude Code (`claude mcp add playwright npx @playwright/mcp@latest`), Claude Desktop, Cline, Copilot CLI (`/mcp add`), Codex, Goose, Warp, Junie, Factory, Gemini CLI, LM Studio, and 15+ others. A Docker image (`mcr.microsoft.com/playwright/mcp`) provides a headless-Chromium deployment for containerised pipelines.

## Key features

- **Accessibility-tree-first interaction** — default mode operates on structured ARIA data; no vision model needed; deterministic element targeting via page snapshot node references.
- **Core automation tools** — `browser_click`, `browser_type`, `browser_navigate`, `browser_snapshot`, `browser_evaluate`, `browser_scroll`, `browser_hover`, `browser_drag`, `browser_select_option`, `browser_file_upload`, and more (~40 tools total in core capability set).
- **Opt-in capability tiers** — `--caps=vision` adds coordinate-based tools (`browser_mouse_click_xy`, `browser_mouse_drag_xy`, etc.); `--caps=pdf` adds `browser_pdf_save`; `--caps=testing` adds `browser_generate_locator` and assertion tools (`browser_verify_element_visible`, `browser_verify_text_visible`, `browser_verify_value`); `--caps=devtools` adds developer tools access.
- **Browser choice** — Chromium (default), Firefox, WebKit, Chrome, and msEdge via `--browser` flag; attach to an existing browser via CDP endpoint or the Playwright Extension.
- **Profile management** — persistent per-workspace profiles (derived from workspace hash), isolated ephemeral contexts (`--isolated`), or preloaded storage state (`--storage-state`); profiles auto-separate by workspace to avoid concurrent-client conflicts.
- **Standalone server mode** — `--port 8931` binds an SSE HTTP endpoint for deployment in headless/remote environments where the MCP client cannot spawn the process directly.
- **Programmatic API** — `createConnection()` from `@playwright/mcp` for embedding in Node.js HTTP servers with custom transports.
- **Code generation** — `--codegen typescript` generates Playwright test code from actions taken during the session.
- **Security controls** — allowed/blocked origin lists, `--allow-unrestricted-file-access` guard, secrets substitution in tool responses (prevents LLM from seeing sensitive values in page content).

## Architecture

Playwright MCP is a thin orchestration layer over Playwright rather than a standalone browser engine. The actual browser automation source lives in the [Playwright monorepo](https://github.com/microsoft/playwright/blob/main/packages/playwright-core/src/tools/mcp); this repo publishes the MCP server wrapper as `@playwright/mcp` on npm. The `roll.js` script keeps the Playwright dependency in sync with upstream releases.

At runtime, the server maintains one browser context per MCP connection (or a shared context with `--shared-browser-context`). Each tool call is synchronous from the LLM's perspective: the server executes the Playwright action, waits for completion, and returns an updated accessibility snapshot. The snapshot captures the full page ARIA tree in a compact text format that fits in LLM context.

The `CLAUDE.md` agent instruction file specifies semantic commit conventions, the Playwright rolling procedure (bump deps, regenerate README via `update-readme.js`, run tests, PR), and release preparation steps — indicating active CI-integrated maintenance.

## Example usage

Connect via Claude Code and navigate to a page:

```bash
claude mcp add playwright npx @playwright/mcp@latest
```

Then in a Claude session the agent can call tools like:
- `browser_navigate({ url: "https://example.com" })` — opens the page
- `browser_snapshot()` — returns the current accessibility tree
- `browser_click({ target: "button[name='Submit']" })` — clicks a specific element
- `browser_type({ target: "input[name='q']", text: "playwright mcp" })` — fills a form field
- `browser_generate_locator({ target: "submit-btn" })` — generates a stable test locator

Docker headless deployment:

```json
{
  "mcpServers": {
    "playwright": {
      "command": "docker",
      "args": ["run", "-i", "--rm", "--init", "--pull=always", "mcr.microsoft.com/playwright/mcp"]
    }
  }
}
```

## Maintenance status

32,980 stars, 2,706 forks. Latest release v0.0.75 (May 2026). Apache-2.0 license. Published by Microsoft with active release cadence tracked as patch increments (v0.0.x). The core browser automation implementation lives upstream in the Playwright monorepo — this repo is the MCP adapter layer. npm package `@playwright/mcp@latest` ships from the same Microsoft org that maintains Playwright itself.

## Ecosystem

Playwright MCP is the primary entry point for adding Playwright browser automation to any MCP-capable agent. It complements the broader MCP tool ecosystem — [[sequentialthinking-mcp]] is a reasoning-focused MCP server in the same ecosystem, and agent SDKs like [[strandsagents.com]] (Strands Agents, which supports MCP as a first-class tool integration layer) can register `@playwright/mcp` as a tool provider. The Playwright CLI+SKILLS alternative (`github.com/microsoft/playwright-cli`) is positioned for coding agents that prefer CLI-based workflows over MCP for token efficiency.
