# playwright.dev-agent-cli

## Fetch log
- Inbox URL: https://playwright.dev/agent-cli/introduction
- Final URL: https://playwright.dev/agent-cli/introduction
- Fetched: 2026-07-14
- Pages: 6
- Mode: standard (llms.txt absent — 404)

## Landing page — https://playwright.dev/agent-cli/introduction

Title: Introduction | Playwright

A command-line interface for browser automation designed for coding agents. Token-efficient commands and installable skills let agents balance browser automation with large codebases and reasoning within limited context windows.

### Example

```
$ playwright-cli open https://demo.playwright.dev/todomvc --headed
$ playwright-cli type "Buy groceries"
$ playwright-cli press Enter
$ playwright-cli type "Water flowers"
$ playwright-cli press Enter
$ playwright-cli check e21
$ playwright-cli screenshot
```

After each command, the CLI outputs the current page state:

```
### Page
- Page URL: https://demo.playwright.dev/todomvc/#/
- Page Title: React - TodoMVC
### Snapshot
[Snapshot](.playwright-cli/page-2026-02-14T19-22-42-679Z.yml)
```

The snapshot file contains the accessibility tree with element refs for the next command.

### Key Features

- **Token-efficient** — concise CLI output avoids loading large tool schemas into the model context
- **Skill-based** — agents discover capabilities through installable skills rather than verbose help text
- **Daemon architecture** — persistent browser process means no startup cost per command
- **Ref-based** — accessibility snapshots with element refs for deterministic interaction
- **Cross-browser** — Chrome, Firefox, WebKit, and Edge support
- **Sessions** — multiple isolated browser instances with separate state

### Playwright CLI vs MCP

| | **Playwright CLI** | **MCP** |
| --- | --- | --- |
| **Best for** | Coding agents (Claude Code, Copilot) working with large codebases | Specialized agentic loops, exploratory automation |
| **How it works** | Agent runs shell commands | LLM calls MCP tools with structured parameters |
| **Token cost** | Lower — concise CLI output, skills loaded on demand | Higher — tool schemas + snapshots in context |
| **Default mode** | Headless | Headed |
| **Setup** | `npm install -g @playwright/cli` | JSON config in MCP client |

### All Commands

**Core:**
```
open [url]                  goto <url>                  close
click <ref>                 dblclick <ref>              fill <ref> <text>
type <text>                 select <ref> <val>          check <ref>
uncheck <ref>               hover <ref>                 drag <start> <end>
upload <file>               snapshot                    screenshot [ref]
pdf                         eval <func> [ref]           resize <w> <h>
dialog-accept [prompt]      dialog-dismiss
```

**Navigation:** `go-back`, `go-forward`, `reload`

**Keyboard & Mouse:**
```
press <key>                 keydown <key>               keyup <key>
mousemove <x> <y>           mousedown [btn]             mouseup [btn]
mousewheel <dx> <dy>
```

**Tabs:** `tab-list`, `tab-new [url]`, `tab-select <idx>`, `tab-close [idx]`

**Storage:**
```
state-save [file]           state-load <file>
cookie-list [--domain]      cookie-get <name>           cookie-set <name> <val>
cookie-delete <name>        cookie-clear
localstorage-list           localstorage-get <key>      localstorage-set <k> <v>
localstorage-delete <key>   localstorage-clear
sessionstorage-list         sessionstorage-get <key>    sessionstorage-set <k> <v>
sessionstorage-delete <k>   sessionstorage-clear
```

**Network:** `network`, `route <pattern> [opts]`, `route-list`, `unroute [pattern]`

**DevTools:**
```
console [min-level]         run-code <code>             tracing-start
tracing-stop                video-start [file]          video-chapter <title>
video-stop                  show
```

**Sessions:** `-s=<name> <cmd>`, `list`, `close-all`, `kill-all`, `delete-data`

**Config:**
```
open --headed               open --browser=firefox      open --persistent
open --profile=<path>       open --config=file.json     attach --extension
install --skills            config-print
```

## Docs nav (full sidebar, from the Skills page)

- Introduction
- **Getting Started**: Installation, Quick Start, Skills
- **Core Concepts**: Snapshots, Capabilities, Vision Mode
- **Browser Automation**: Navigation, Interaction, Keyboard & Mouse, Tabs, Dialogs
- **Network & Storage**: Network & Mocking, Storage & Authentication
- **Developer Tools**: Console & Eval, Screenshots & PDF, Tracing, Test Debugging
- Video Recording
- **Sessions**: Sessions & Dashboard, Attach
- Configuration

Top nav also links: Docs (`/docs/intro`), MCP (`/mcp/introduction`), CLI (`/agent-cli/introduction`), API (`/docs/api/class-playwright`). Language variants exist for Node.js (default), Python, Java, .NET.

## Installation — https://playwright.dev/agent-cli/installation

### Prerequisites
- Node.js 20 or newer
- A coding agent: Claude Code, GitHub Copilot, or similar

### Global installation
```
npm install -g @playwright/cli@latest
playwright-cli --help
```

### Local installation (npx)
```
npx playwright-cli --help
```

### Installing browsers
The CLI downloads a browser automatically on first use. To install explicitly:
```
playwright-cli install-browser               # install default (chromium)
playwright-cli install-browser firefox       # install specific browser
playwright-cli install-browser --with-deps   # install with system dependencies
```

Install options: `--with-deps` (install system dependencies, Linux), `--dry-run` (preview), `--list` (list available browsers from all installations), `--force` (force reinstall), `--only-shell` (only Chromium headless shell), `--no-shell` (skip Chromium headless shell).

### Installing skills
Coding agents like Claude Code and GitHub Copilot can use locally installed skills for richer context about available commands:
```
playwright-cli install --skills
```

### Skills-less operation
Point an agent at the CLI directly and let it discover commands on its own:
```
Test the "add todo" flow on https://demo.playwright.dev/todomvc using playwright-cli.
Check playwright-cli --help for available commands.
```

### Environment setup
Configure a coding agent to use a specific session:
```
PLAYWRIGHT_CLI_SESSION=todo-app claude .
```

### Next steps (linked)
Quick Start, Snapshots, Capabilities, Configuration.

## Quick Start — https://playwright.dev/agent-cli/quick-start

### Interactive demo
Try asking a coding agent:
```
Use playwright skills to test https://demo.playwright.dev/todomvc/.
Take screenshots for all successful and failing scenarios.
```

### Manual walkthrough
```
playwright-cli open https://demo.playwright.dev/todomvc/ --headed
playwright-cli type "Buy groceries"
playwright-cli press Enter
playwright-cli type "Water flowers"
playwright-cli press Enter
playwright-cli check e21
playwright-cli screenshot
```

### Understanding the output
After each command, the CLI outputs a snapshot of the current page state (page URL, page title, and a link to a `.playwright-cli/page-<timestamp>.yml` snapshot file). The snapshot file contains the accessibility tree with element refs usable in subsequent commands.

### Core workflow
1. **Open** — `playwright-cli open <url>` opens a URL
2. **Snapshot** — each command returns the accessibility tree with element refs
3. **Interact** — use refs to click, type, or fill
4. **Re-snapshot** — each action returns updated state with new refs

### What's next (linked)
Commands, Snapshots, Sessions.

## Skills — https://playwright.dev/agent-cli/skills

Skills teach coding agents how to use `playwright-cli` effectively, providing structured reference documentation that agents can discover and use.

### Installing skills
```
playwright-cli install --skills
```
This installs skill files locally so a coding agent can reference them for context about available commands and workflows.

### What skills provide
The installed skill includes detailed reference guides for common tasks:
- Running and Debugging Playwright tests — run, debug and manage Playwright test suites
- Request mocking — intercept and mock network requests
- Running Playwright code — execute arbitrary Playwright scripts
- Browser session management — manage multiple browser sessions
- Storage state (cookies, localStorage) — persist and restore browser state
- Test generation — generate Playwright tests from interactions
- Tracing — record and inspect execution traces
- Video recording — capture browser session videos
- Inspecting element attributes — get element attributes not visible in snapshots

### Skills-less operation
`playwright-cli` can be used without installing skills — point an agent at the CLI and let it discover commands:
```
Test the "add todo" flow on https://demo.playwright.dev/todomvc using playwright-cli.
Check playwright-cli --help for available commands.
```

### Supported agents
Skills work with: Claude Code, GitHub Copilot, Cursor, and any coding agent that supports locally installed skills.

## Capabilities — https://playwright.dev/agent-cli/capabilities

The CLI and MCP share the same underlying Playwright tools, organized into capability groups. In the CLI all capabilities are always available — there's no gating. This page maps commands to their capability groups for reference.

**Core** (always available, basic browser automation): `open`/`goto`/`close`, `go-back`/`go-forward`/`reload`, `click`/`dblclick`/`hover`/`drag`, `type`/`fill`/`select`, `check`/`uncheck`, `press`/`keydown`/`keyup`, `snapshot`, `screenshot`, `upload`, `dialog-accept`/`dialog-dismiss`, `resize`, `eval`/`run-code`.

**Network** (inspection and mocking): `network` (list requests since page load), `route` (mock requests matching a URL pattern), `route-list`, `unroute`, `network-state-set` (online/offline).

**Storage** (cookie/localStorage/sessionStorage management plus state persistence): `state-save`/`state-load`, `cookie-list/get/set/delete/clear`, `localstorage-list/get/set/delete/clear`, `sessionstorage-list/get/set/delete/clear`.

**Vision** (coordinate-based mouse interaction using pixel positions from screenshots — useful for canvas apps, maps, and custom widgets without accessible elements): `mousemove <x> <y>`, `mousedown [button]`, `mouseup [button]`, `mousewheel <dx> <dy>`, `screenshot`.

**DevTools** (tracing, video recording, test debugging): `console`, `tracing-start`/`tracing-stop`, `video-start`/`video-stop`/`video-chapter`, `show` (visual dashboard), `pause-at`/`resume`/`step-over`.

**PDF**: `pdf` (export page as PDF).

**Testing** (assertions and test generation): `verify-element-visible`, `verify-text-visible`, `verify-list-visible`, `verify-value`, `generate-locator`.

## Sessions & Dashboard — https://playwright.dev/agent-cli/sessions

The CLI keeps the browser profile in memory by default — cookies and storage state are preserved between CLI calls within a session but lost when the browser closes.

### Named sessions
```
playwright-cli open https://playwright.dev
playwright-cli -s=example open https://example.com --persistent
playwright-cli list
# Active sessions:
# -> default (https://playwright.dev)
#    example (https://example.com) [persistent]
```
Each session has its own browser instance, cookies, localStorage, navigation history, and console log.

### Environment variable
```
PLAYWRIGHT_CLI_SESSION=todo-app claude .
```
All `playwright-cli` commands in that agent session use the `todo-app` browser instance.

### Profile persistence
- **In-memory (default)** — cookies/storage persist between commands within a session but lost when the browser closes: `playwright-cli open https://example.com`
- **Persistent to disk** — profile saved to disk, survives browser restarts, equivalent to Playwright MCP's default persistent mode: `playwright-cli open https://example.com --persistent`. Default persistent profile locations — macOS: `~/Library/Caches/ms-playwright/mcp-{channel}-profile`; Linux: `~/.cache/ms-playwright/mcp-{channel}-profile`; Windows: `%LOCALAPPDATA%\ms-playwright\mcp-{channel}-profile`.
- **Custom directory**: `playwright-cli open https://example.com --profile=./my-profile`

### Session management
```
playwright-cli list                     # list all sessions
playwright-cli -s=name close            # close a specific session
playwright-cli close-all                # close all browsers
playwright-cli kill-all                 # force kill (for unresponsive browsers)
playwright-cli -s=name delete-data      # delete stored profile data
```

### Dashboard
```
playwright-cli show
```
Provides a **session grid** (all active sessions with live screencast, name, URL, and title — click to zoom) and **session detail** (live viewport with tab bar, navigation controls, and full remote mouse/keyboard input; press Escape to release). Use cases: watch coding agents automate browsers in the background, take over when an agent gets stuck on a CAPTCHA or 2FA, close stale sessions or delete data from the UI.

### Saving and restoring state
```
# Login, then save state
playwright-cli state-save auth-state.json
# Later: restore state in a new session
playwright-cli state-load auth-state.json
```

### Workflow: isolated testing
```
# Admin session
playwright-cli -s=admin open https://app.example.com --persistent
playwright-cli -s=admin state-load admin-auth.json
playwright-cli -s=admin goto /admin/settings
# User session
playwright-cli -s=user open https://app.example.com --persistent
playwright-cli -s=user state-load user-auth.json
playwright-cli -s=user goto /dashboard
# Monitor both
playwright-cli show
```
