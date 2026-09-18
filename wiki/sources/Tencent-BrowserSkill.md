---
type: source
category: "Browser & web automation"
source_url: https://github.com/Tencent/BrowserSkill
tags: [browser-automation, agent-skill, logged-in-browser, shell-cli, human-in-the-loop, chromium-extension, tab-borrowing, deepseek-harness-plugin]
related: [browserbase.com, browser-use.com, playwright.dev-agent-cli, microsoft-playwright-mcp]
product: browserskill
detail_level: standard
created: 2026-09-18
updated: 2026-09-18
---

BrowserSkill (Tencent, 4.4k+ stars, MIT) lets a shell-capable AI agent drive the user's own already-logged-in Chromium browser instead of a fresh, cookie-less automation profile. A local `bsk` CLI/daemon talks to a browser extension over a loopback WebSocket; the extension runs agent tasks in a dedicated, visible **Agent Window** so the human can keep using their normal windows at the same time, and can explicitly "borrow" a specific existing tab and return it when done. It matters to this wiki as a distinct design point in the browser-automation-for-agents space: rather than a headless-cloud-browser API ([[browserbase.com]]) or an in-process automation library ([[browser-use.com]]), it is a locally-installed skill + CLI + extension triple that any harness capable of running shell commands can adopt, with built-in human-in-the-loop handoff for captchas, logins, and confirmations.

_All claims below are sourced from ../../raw/github/Tencent-BrowserSkill.md unless otherwise noted._

## What it does

BrowserSkill gives an agent a `bsk` CLI that opens, observes, and interacts with web pages inside a per-session Agent Window backed by the user's real browser profile — reusing existing logins without separate test accounts. The agent never talks to the browser directly: it shells out to `bsk`, which speaks JSON Lines to a local `bsk daemon`, which forwards `tool.*` RPCs over WebSocket to a WXT/MV3 Chromium extension that executes them via Chrome DevTools Protocol. Sessions are sandboxed by default — write tools require tabs inside the Agent Window unless a user tab was explicitly borrowed and returned — and every session must be stopped when the task ends. Support spans Cursor, Claude Code, Codex, OpenClaw, CodeBuddy, WorkBuddy, Pi, Hermes Agent, and (via a dedicated plugin) DeepSeek Harness.

## Installation

Local, agent-directed setup is one line handed to any shell-capable agent: *"Set up browser-skill on this machine by following `https://raw.githubusercontent.com/Tencent/BrowserSkill/main/AGENT_INSTALL.md`"*. Manually: install the `bsk` CLI via `curl ... | sh` (macOS/Linux) or an equivalent PowerShell one-liner (Windows), install the browser extension from the Chrome Web Store or Edge Add-ons, then run `bsk install-skill` (interactively, or `--harness <id> --json` non-interactively) to drop the bundled `skill/SKILL.md` into the target harness's skills directory. `bsk doctor` verifies CLI/daemon/extension health and skill discovery; a fresh install where only "extension connected" fails is expected until the user finishes the extension-side pairing. DeepSeek Harness instead adds the npm plugin `@wxg-prc-cpg/browser-skill-dsh-plugin` to a `dsh` profile, which supplies its own skill and native `browser_*` tools. `AGENT_INSTALL.md` frames the whole flow as agent-executed instructions with a strict "done" bar: harness loads the skill, `bsk doctor` shows no `fail` rows, and a real test task (open a page, summarize it, stop the session) succeeds.

## Key features

- **Reuses real login state** — agents act inside sites the user is already signed into, with no separate test accounts.
- **Non-interrupting Agent Window** — browser tasks run in a separate visible window so the user keeps working in their own browser meanwhile; a specific user tab can be explicitly borrowed and returned.
- **Harness-agnostic** — any agent that can call a shell reaches BrowserSkill through `bsk`, with no lock-in to a specific model or framework; supports at least nine named harnesses plus a DeepSeek Harness-specific plugin exposing native `browser_*` tools.
- **Built-in human-in-the-loop** — `bsk request-help` lets the agent hand off captcha, login, OTP, payment confirmation, or consent steps to the user, then resume.
- **Automation settings toggle two independent controls** — confirm-before-borrowing and allow-human-help-requests — both on by default and enforced by the extension regardless of deprecated CLI flags (`--unattended`, `--no-confirm`, `BSK_REQUEST_HELP=off`) that no longer bypass them as of 0.3.0.
- **Rich interaction surface** — `observe`/`snapshot`/`get-html`/`screenshot` for reading state, `click`/`fill`/`select`/`press`/`hover`/`scroll-to`/`wheel` for acting, `upload`/`download` for files, `console`/`network` for read-only diagnostics, `emulate --device` for device emulation, and `record start` for capturing user actions (explicitly excluding banking/SSO/password-manager pages).
- **Full-page screenshots and Canvas support**, including coordinate-accurate clicks on canvas content via a short-lived capture ID.
- **Cross-platform** — macOS (Apple Silicon and Intel), Linux (x64/ARM64), Windows x64; Chrome and Edge supported today, other Chromium-based browsers expected to work, Firefox planned.

## Architecture

Three local components connected in a strict chain: **bsk CLI** (`crates/bsk-cli`, Rust) parses verb-noun subcommands and speaks JSON Lines over a Unix domain socket (or named pipe on Windows) to the **bsk daemon** (same binary), which listens on a loopback WebSocket (default port 52800) for the **bsk extension** (`apps/extension`, WXT/MV3, React popup + service-worker background). The daemon maintains `browsers` (connected extensions) and `sessions` (Agent Window bindings), serializes tool calls per session via a per-session queue, and validates the extension's `Origin: chrome-extension://…` header at handshake. `bsk-protocol` (`crates/bsk-protocol`) defines shared Rust wire types and JSON Schemas, mirrored into the extension's TypeScript transport layer and kept in sync via tests. (../../raw/github/Tencent-BrowserSkill.md)

A session is an opaque 4-letter ID plus a dedicated Agent Window, a session-scoped ref-store (`@e1`-style element references), and a borrow table; sandbox mode confines write tools to the Agent Window unless a tab was explicitly borrowed. `tab_list` exposes three scopes (`user`, `agent`, `all`). Remote mode moves the CLI and daemon to a server, with the extension connecting over authenticated WSS while CLI-to-daemon traffic stays local IPC; local mode binds strictly to loopback. File transfers (upload/download) are local-only — remote sessions return `unsupported` — and the daemon alone owns storage capability limits, staged file validation, and the agent-local vs. browser-internal path boundary; the extension only ever performs the browser-side click/drop/download transaction and reports a three-state `effect_state` (`none`/`committed`/`unknown`) so a timed-out transfer is never blindly retried. (../../raw/github/Tencent-BrowserSkill.md)

## Example usage

Typical agent-driven session, per the bundled `skill/SKILL.md`:

```sh
bsk session start --json                      # retain session_id
bsk navigate https://example.com --session <id>
bsk observe --session <id>                    # get text/controls/@eN refs
bsk click @e3 --session <id>                  # act on a fresh ref
bsk session stop <id>                         # mandatory on success and failure
```

Borrowing an existing user tab instead of navigating fresh:

```sh
bsk tab list --scope user --session <id>
bsk tab borrow <tab-id> --session <id>
bsk tab return <tab-id> --session <id>
```

Handing a blocker to the human:

```sh
bsk request-help --session <id> --prompt "Please complete sign-in" --target @e3
```

(../../raw/github/Tencent-BrowserSkill.md)

## Maintenance status

4,454 stars, 315 forks, MIT license, TypeScript as the primary language (with a Rust CLI/daemon and TypeScript extension). Actively released: latest tag `cli-v0.3.0` (2026-09-17), pushed as recently as 2026-09-18. Ships localization for English, Simplified Chinese, and Korean, and a dedicated `evals/browser` suite for deterministic, agent-neutral browser capability evaluation. (../../raw/github/Tencent-BrowserSkill.md)

## Ecosystem

BrowserSkill sits alongside this wiki's other browser-automation-for-agents entries as a third approach: where [[browserbase.com]] sells hosted headless browser infrastructure and [[browser-use.com]] is an in-process Python/JS automation library, BrowserSkill is a locally-running CLI + daemon + Chromium extension that any shell-capable harness can call, deliberately reusing the user's own logged-in session rather than a clean automation profile. Its shell-first CLI surface and bundled agent skill make it conceptually closest to [[playwright.dev-agent-cli]] (a shell-first Playwright interface built for the same reason — agents that call commands, not APIs) and to [[microsoft-playwright-mcp]] as an alternative integration shape (CLI + extension vs. MCP server) for giving agents browser control. It ships a first-class plugin for `deepseek-ai/deepseek-harness`, this wiki's [[deepseek-ai-deepseek-harness]].
