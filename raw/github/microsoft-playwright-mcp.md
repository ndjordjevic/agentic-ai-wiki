# microsoft/playwright-mcp

## Metadata
- Stars: 31485
- Primary language: TypeScript
- Default branch: main
- Latest release: v0.0.70 (about 26 days ago)
- License: Apache License 2.0
- Homepage: https://www.npmjs.com/package/@playwright/mcp
- Fetched: 2026-04-27
- Final URL: https://github.com/microsoft/playwright-mcp

## Description
Playwright MCP server

## README

## Playwright MCP

A Model Context Protocol (MCP) server that provides browser automation capabilities using [Playwright](https://playwright.dev). This server enables LLMs to interact with web pages through structured accessibility snapshots, bypassing the need for screenshots or visually-tuned models.

### Playwright MCP vs Playwright CLI

This package provides MCP interface into Playwright. If you are using a **coding agent**, you might benefit from using the [CLI+SKILLS](https://github.com/microsoft/playwright-cli) instead.

- **CLI**: Modern **coding agents** increasingly favor CLI–based workflows exposed as SKILLs over MCP because CLI invocations are more token-efficient: they avoid loading large tool schemas and verbose accessibility trees into the model context, allowing agents to act through concise, purpose-built commands. This makes CLI + SKILLs better suited for high-throughput coding agents that must balance browser automation with large codebases, tests, and reasoning within limited context windows.

- **MCP**: MCP remains relevant for specialized agentic loops that benefit from persistent state, rich introspection, and iterative reasoning over page structure, such as exploratory automation, self-healing tests, or long-running autonomous workflows where maintaining continuous browser context outweighs token cost concerns.

### Key Features

- **Fast and lightweight**. Uses Playwright's accessibility tree, not pixel-based input.
- **LLM-friendly**. No vision models needed, operates purely on structured data.
- **Deterministic tool application**. Avoids ambiguity common with screenshot-based approaches.

### Requirements
- Node.js 18 or newer
- VS Code, Cursor, Windsurf, Claude Desktop, Goose, Junie or any other MCP client

### Getting started

Install via npx (standard config):

```js
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["@playwright/mcp@latest"]
    }
  }
}
```

Also installable via Claude Code CLI (`claude mcp add playwright npx @playwright/mcp@latest`), Copilot CLI (`/mcp add`), Cursor (button or manual), VS Code (button or CLI), and many other MCP clients.

### Configuration

Supports extensive CLI arguments and a JSON config file (`--config`). Key options:

| Option | Description |
|--------|-------------|
| `--browser <browser>` | chrome, firefox, webkit, msedge |
| `--headless` | run browser in headless mode (headed by default) |
| `--caps <caps>` | additional capabilities: vision, pdf, devtools |
| `--port <port>` | port to listen on for SSE transport |
| `--isolated` | keep browser profile in memory, do not save to disk |
| `--storage-state <path>` | path to storage state file for isolated sessions |
| `--config <path>` | path to JSON configuration file |
| `--codegen <lang>` | code generation language (typescript, none) |
| `--user-data-dir <path>` | path to user data directory for persistence |

### User profile

Three modes:
- **Persistent profile** — all logged-in information stored in persistent profile, workspace-hashed per project.
- **Isolated** — each session in isolated profile; storage lost when browser closes.
- **Browser Extension** — connect to existing Chrome/Edge tabs using the Playwright Extension.

### Standalone MCP server

For headless environments without display:

```bash
npx @playwright/mcp@latest --port 8931
```

Then connect MCP client to `http://localhost:8931/mcp`.

Docker support:
```js
{
  "mcpServers": {
    "playwright": {
      "command": "docker",
      "args": ["run", "-i", "--rm", "--init", "--pull=always", "mcr.microsoft.com/playwright/mcp"]
    }
  }
}
```

### Tools

**Core automation** (always available):
- `browser_click` — Click on a web page element
- `browser_close` — Close the page
- `browser_console_messages` — Returns all console messages
- `browser_drag` — Drag and drop between two elements
- `browser_evaluate` — Evaluate JavaScript expression on page
- `browser_file_upload` — Upload one or multiple files
- `browser_fill_form` — Fill multiple form fields
- `browser_handle_dialog` — Handle a dialog
- `browser_hover` — Hover over element
- `browser_navigate` — Navigate to a URL
- `browser_navigate_back` — Go back to previous page
- `browser_network_requests` — Returns all network requests since loading the page
- `browser_press_key` — Press a key on the keyboard
- `browser_resize` — Resize browser window
- `browser_run_code` — Run Playwright code snippet
- `browser_select_option` — Select an option in a dropdown
- `browser_snapshot` — Capture accessibility snapshot of the current page (preferred over screenshot)
- `browser_take_screenshot` — Take a screenshot
- `browser_type` — Type text into editable element
- `browser_wait_for` — Wait for text to appear/disappear or a time to pass

**Tab management:** `browser_tabs` — List, create, close, or select a browser tab.

**Opt-in capabilities (via --caps=...):**
- `network`: `browser_network_state_set`, `browser_route` (mock requests), `browser_route_list`, `browser_unroute`
- `storage`: Full cookie, localStorage, sessionStorage read/write/clear tools; `browser_storage_state`, `browser_set_storage_state`
- `devtools`: highlight, pick locator, resume, tracing, video recording
- `vision`: coordinate-based mouse click/drag/move/wheel (for screenshot-based interactions)
- `pdf`: `browser_pdf_save`
- `testing`: generate locator, verify element/text/list/value visible
- `config`: `browser_get_config`

### Programmatic usage

```js
import { createConnection } from '@playwright/mcp';
import { SSEServerTransport } from '@modelcontextprotocol/sdk/server/sse.js';

const connection = await createConnection({ browser: { launchOptions: { headless: true } } });
const transport = new SSEServerTransport('/messages', res);
await connection.connect(transport);
```

### Security

Playwright MCP is **not** a security boundary. See MCP Security Best Practices for guidance.

## Top-level structure

```
src/          — TypeScript source code
tests/        — test suite
CLAUDE.md     — commit and contribution conventions (semantic commits, branch naming)
Dockerfile    — Docker image definition
package.json  — npm package (@playwright/mcp)
playwright.config.ts — test configuration
```

Key note from CLAUDE.md: never add Co-Authored-By agents in commit messages; use semantic commits (`fix`, `feat`, `chore`, `docs`, `test`, `devops`).
