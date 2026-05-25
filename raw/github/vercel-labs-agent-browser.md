# vercel-labs/agent-browser

## Metadata
- Stars: 34,229
- Forks: 2,144
- Primary language: Rust
- Default branch: main
- Latest release: v0.27.0 (~2026-05-08)
- License: Apache-2.0
- Homepage: https://agent-browser.dev
- Fetched: 2026-05-25
- Final URL: https://github.com/vercel-labs/agent-browser

## Description
Browser automation CLI for AI agents. Fast native Rust CLI.

## README

# agent-browser

Browser automation CLI for AI agents. Fast native Rust CLI.

[![skills.sh](https://skills.sh/b/vercel-labs/agent-browser)](https://skills.sh/vercel-labs/agent-browser)

## Installation

### Global Installation (recommended)

Installs the native Rust binary:

```bash
npm install -g agent-browser
agent-browser install  # Download Chrome from Chrome for Testing (first time only)
```

### Project Installation (local dependency)

For projects that want to pin the version in `package.json`:

```bash
npm install agent-browser
npx agent-browser install
```

## Snapshot / Ref Workflow

The core workflow uses accessibility-tree snapshots with compact `@eN` refs. The browser stays running across commands via a background daemon.

```
# 1. Get a snapshot of the page
agent-browser open example.com
agent-browser snapshot -i          # interactive elements only

# Snapshot output:
# Page: Example Domain
# URL: https://example.com
#
# - heading "Example Domain" [ref=e1] [level=1]
# - button "Submit" [ref=e2]
# - textbox "Email" [ref=e3]
# - link "Learn more" [ref=e4]

# 2. Use refs to interact
agent-browser click @e2                   # Click the button
agent-browser fill @e3 "test@example.com" # Fill the textbox
agent-browser get text @e1                # Get heading text
agent-browser hover @e4                   # Hover the link
```

**Why use refs?**

- **Deterministic**: Ref points to exact element from snapshot
- **Fast**: No DOM re-query needed
- **AI-friendly**: Snapshot + ref workflow is optimal for LLMs (~200–400 tokens vs raw HTML)

### CSS Selectors

```bash
agent-browser click "#id"
agent-browser click ".class"
agent-browser click "div > button"
```

### Text & XPath

```bash
agent-browser click "text=Submit"
agent-browser click "xpath=//button"
```

### Semantic Locators

```bash
agent-browser find role button click --name "Submit"
agent-browser find label "Email" fill "test@test.com"
```

## Agent Mode

Use `--json` for machine-readable output:

```bash
agent-browser snapshot --json
# Returns: {"success":true,"data":{"snapshot":"...","refs":{"e1":{"role":"heading","name":"Title"},...}}}

agent-browser get text @e1 --json
agent-browser is visible @e2 --json
```

### Optimal AI Workflow

```bash
# 1. Navigate and get snapshot
agent-browser open example.com
agent-browser snapshot -i --json   # AI parses tree and refs

# 2. AI identifies target refs from snapshot
# 3. Execute actions using refs
agent-browser click @e2
agent-browser fill @e3 "input text"

# 4. Get new snapshot if page changed
agent-browser snapshot -i --json
```

### Command Chaining

Commands can be chained with `&&` in a single shell invocation. The browser persists via a background daemon, so chaining is safe and more efficient:

```bash
agent-browser open example.com && agent-browser wait --load networkidle && agent-browser snapshot -i
agent-browser fill @e1 "user@example.com" && agent-browser fill @e2 "pass" && agent-browser click @e3
```

## Headed Mode

Show the browser window for debugging:

```bash
agent-browser open example.com --headed
```

## Authenticated Sessions

Use `--headers` to set HTTP headers for a specific origin, enabling authentication without login flows:

```bash
# Headers are scoped to api.example.com only
agent-browser open api.example.com --headers '{"Authorization": "Bearer <token>"}'
agent-browser snapshot -i --json
```

For global headers (all domains), use `set headers`:

```bash
agent-browser set headers '{"X-Custom-Header": "value"}'
```

## Custom Browser Executable

Use a custom browser executable instead of the bundled Chromium:

```bash
# Via flag
agent-browser --executable-path /path/to/chromium open example.com

# Via environment variable
AGENT_BROWSER_EXECUTABLE_PATH=/path/to/chromium agent-browser open example.com
```

### Serverless (Vercel)

Run agent-browser + Chrome in an ephemeral Vercel Sandbox microVM:

```typescript
import { Sandbox } from "@vercel/sandbox";

const sandbox = await Sandbox.create({ runtime: "node24" });
await sandbox.runCommand("agent-browser", ["open", "https://example.com"]);
const result = await sandbox.runCommand("agent-browser", ["screenshot", "--json"]);
await sandbox.stop();
```

### Serverless (AWS Lambda)

```typescript
import chromium from '@sparticuz/chromium';
import { execSync } from 'child_process';

export async function handler() {
  const executablePath = await chromium.executablePath();
  const result = execSync(
    `AGENT_BROWSER_EXECUTABLE_PATH=${executablePath} agent-browser open https://example.com && agent-browser snapshot -i --json`,
    { encoding: 'utf-8' }
  );
  return JSON.parse(result);
}
```

## Local Files

Open and interact with local files (PDFs, HTML, etc.) using `file://` URLs:

```bash
agent-browser --allow-file-access open file:///path/to/document.pdf
agent-browser screenshot report.png
```

## CDP Mode

Connect to an existing browser via Chrome DevTools Protocol:

```bash
# Connect once, then run commands without --cdp
agent-browser connect 9222
agent-browser snapshot

# Or pass --cdp on each command
agent-browser --cdp 9222 snapshot

# Connect to remote browser via WebSocket URL
agent-browser --cdp "wss://your-browser-service.com/cdp?token=..." snapshot
```

### Auto-Connect

Use `--auto-connect` to automatically discover and connect to a running Chrome instance:

```bash
agent-browser --auto-connect open example.com
# Or via environment variable
AGENT_BROWSER_AUTO_CONNECT=1 agent-browser snapshot
```

## Streaming (Browser Preview)

Every session automatically starts a WebSocket stream server. Use `stream status` to see the bound port:

```bash
agent-browser stream status
AGENT_BROWSER_STREAM_PORT=9223 agent-browser open example.com
agent-browser stream enable --port 9223
agent-browser stream disable
```

The WebSocket server streams the browser viewport and accepts input events (mouse, keyboard, touch).

## Architecture

agent-browser uses a client-daemon architecture:

1. **Rust CLI** — Parses commands, communicates with daemon
2. **Rust Daemon** — Pure Rust daemon using direct CDP, no Node.js required

The daemon starts automatically on first command and persists between commands for fast subsequent operations. Set `AGENT_BROWSER_IDLE_TIMEOUT_MS` to auto-shutdown after inactivity.

**Browser Engine:** Uses Chrome (from Chrome for Testing) by default. The `--engine` flag selects between `chrome` and `lightpanda`. Supports Chromium/Chrome (via CDP) and Safari (via WebDriver for iOS).

## Platforms

| Platform    | Binary      |
| ----------- | ----------- |
| macOS ARM64 | Native Rust |
| macOS x64   | Native Rust |
| Linux ARM64 | Native Rust |
| Linux x64   | Native Rust |
| Windows x64 | Native Rust |

## Usage with AI Agents

### Just ask the agent

```
Use agent-browser to test the login flow. Run agent-browser --help to see available commands.
```

### AI Coding Assistants (recommended)

Add the skill to your AI coding assistant for richer context:

```bash
npx skills add vercel-labs/agent-browser
```

This works with Claude Code, Codex, Cursor, Gemini CLI, GitHub Copilot, Goose, OpenCode, and Windsurf. The skill is fetched from the repository, so it stays up to date automatically.

### AGENTS.md / CLAUDE.md

For more consistent results, add to your project or global instructions file:

```markdown
## Browser Automation

Use `agent-browser` for web automation. Run `agent-browser --help` for all commands.

Core workflow:
1. `agent-browser open <url>` - Navigate to page
2. `agent-browser snapshot -i` - Get interactive elements with refs (@e1, @e2)
3. `agent-browser click @e1` / `fill @e2 "text"` - Interact using refs
4. Re-snapshot after page changes
```

## Integrations

### iOS Simulator

Control real Mobile Safari in the iOS Simulator for authentic mobile web testing. Requires macOS with Xcode and Appium XCUITest driver.

```bash
agent-browser device list
agent-browser -p ios --device "iPhone 16 Pro" open https://example.com
agent-browser -p ios snapshot -i
agent-browser -p ios tap @e1
agent-browser -p ios fill @e2 "text"
agent-browser -p ios screenshot mobile.png
agent-browser -p ios swipe up
```

### AWS AgentCore

Connect to an AWS Bedrock-managed cloud browser session:

```bash
agent-browser -p agentcore open https://example.com
export AGENT_BROWSER_PROVIDER=agentcore
```

Optional AgentCore variables: `AGENTCORE_REGION`, `AGENTCORE_BROWSER_ID`, `AGENTCORE_PROFILE_ID`, `AGENTCORE_SESSION_TIMEOUT`, `AWS_PROFILE`.

## License

Apache-2.0

## Docs

### skill-data/core/SKILL.md (excerpt)

```
---
name: core
description: Core agent-browser usage guide. Read this before running any agent-browser commands.
  Covers snapshot-and-ref workflow, navigating pages, interacting with elements (click, fill,
  type, select), extracting text and data, taking screenshots, managing tabs, handling forms
  and auth, waiting for content, running multiple browser sessions in parallel, and
  troubleshooting common failures.
allowed-tools: Bash(agent-browser:*), Bash(npx agent-browser:*)
---
```

The skill data is organized as `skill-data/core/SKILL.md` + 8 reference files:
`authentication.md`, `commands.md`, `profiling.md`, `proxy-support.md`,
`session-management.md`, `snapshot-refs.md`, `trust-boundaries.md`, `video-recording.md`.

### AGENTS.md (key sections)

- **Package Manager:** pnpm only; `pnpm install`, `pnpm run build`
- **Architecture:** Rust CLI in `cli/src/`, daemon in `cli/src/native/`, dashboard in `packages/dashboard/`
- **Testing:** `cd cli && cargo test` (unit, ~320 tests); `cargo test e2e -- --ignored --test-threads=1` (18 e2e tests requiring Chrome)
- **Code style:** No emojis, no double hyphens, CLI flags in kebab-case, color via `cli/src/color.rs` respecting `NO_COLOR`
- **Documentation:** Feature changes require updating `cli/src/output.rs`, `README.md`, `skill-data/core/SKILL.md`, and `docs/src/app/` MDX files
- **Releasing:** Manual single-PR releases; CI builds 7 platform binaries and publishes to npm when `package.json` version differs from npm

## Top-level structure

```
.claude-plugin/      — Claude Code plugin manifest (agent skills integration)
.github/             — CI workflows (build, publish, e2e tests, Windows debug)
AGENTS.md            — AI agent coding instructions (package manager, code style, arch, testing, releasing)
CHANGELOG.md         — Version history (56KB)
README.md            — Full usage documentation (61KB)
agent-browser.schema.json — JSON schema for configuration
benchmarks/          — Performance benchmarks
bin/                 — npm bin entry points
cli/                 — Rust source (CLI parser, daemon, CDP client, snapshot engine, native actions)
  src/
    native/          — daemon, actions, browser, CDP client, snapshot, state
    color.rs         — NO_COLOR-respecting terminal color module
    output.rs        — --help output (flags, examples, env vars)
docker/              — Docker image configuration
docs/                — Next.js documentation site (MDX, deployed to agent-browser.dev)
evals/               — Agent evaluation harness
examples/            — Working demos (agentcore, core, dogfood, electron, slack, vercel-sandbox)
package.json         — npm package root (monorepo via pnpm-workspace)
packages/
  dashboard/         — Web dashboard (shadcn/ui, TypeScript)
scripts/             — Release automation, Windows debug scripts
skill-data/
  core/              — SKILL.md + 8 reference files for AI agent usage
  agentcore/         — AgentCore-specific skill data
  dogfood/           — Internal dogfooding skill
  electron/          — Electron CDP integration skill
  slack/             — Slack automation skill
  vercel-sandbox/    — Vercel Sandbox integration skill
skills/              — npx skills integration stubs
```
