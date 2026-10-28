---
type: source
category: "Browser & web automation"
source_url: https://github.com/Ying-Kai-Liao/jev-browser
tags:
  - browser-automation
  - jev-model
  - playwright
  - mcp-server
  - webmcp
  - claude-code-plugin
  - typesafe
related:
  - typesafe.ai
  - browse.sh
  - microsoft-playwright-mcp
  - vercel-labs-agent-browser
  - browser-use.com
  - AgriciDaniel-jev-seo
product: jev-browser
detail_level: standard
created: 2026-10-28
updated: 2026-10-28
---

jev-browser is an unofficial MIT-licensed JavaScript library, CLI, and MCP server for browser automation where a calling LLM (typically Claude via MCP) states one outcome per step and Typesafe's Jev (System One) decides which element and action to take — Playwright executes locally, and the LLM never reads page snapshots unless it chooses to take over. Each round settles the page, describes elements/labels/state/visible text, asks Jev several probability questions at once (~300 ms), then acts; Jev never writes free-form text, so strings to type come from caller-supplied `values` candidates.

_All claims below are sourced from ../../raw/github/Ying-Kai-Liao-jev-browser.md unless otherwise noted._

## What it does

The calling LLM invokes tools such as `browser_do(goal, values?)` with one observable outcome (e.g. "Log in") and any secrets or strings in `values`. Code loops until done, stuck, or needing confirmation: settle (network + DOM quiet) → describe the page → one Jev request covering done/error/irreversible/tool/target/value → Playwright act. Statuses include `done`, `likely_done`, `needs_login`, `needs_confirmation` (pause before irreversible actions), `error`, `stuck`/`max_actions`, `ambiguous`, and `blocked`. Companion tools cover open/close, yes/no checks, multi-option choose, compact snapshots for takeover, direct `browser_act` without a model, question-scoped `browser_read`, screenshots, and WebMCP tool list/call. On live-site benchmarks the README reports 40/42 correct with 0 false "done" claims, median ~5× less page content to the caller than a Playwright-MCP-style loop (estimate), with known limits around ordered multi-sub-goal steps, open-ended goals, and multi-value judgements.

## Installation

Claude Code plugin:

```
/plugin install jev-browser --marketplace Ying-Kai-Liao/jev-browser
```

MCP from npm (any MCP client):

```bash
npx playwright install chromium
claude mcp add jev-browser -e TYPESAFE_API_KEY=your-key -- npx -y -p jev-browser jev-browser-mcp
```

From source: clone the repo, `npm install`, `npm run setup`, copy `.env.example` to `.env` with `TYPESAFE_API_KEY` or `OPENROUTER_API_KEY`. OpenRouter works without a TypeSafe account; when both keys are set, `TYPESAFE_API_KEY` wins. Optional env includes `JEV_BROWSER_HEADED`, `JEV_BROWSER` / profile path, and `JEV_API_URL` / `JEV_MODEL` (ignored when using OpenRouter).

## Key features

- **LLM plans, Jev decides** — caller supplies goals and candidate values; Jev answers only distributions (`noul` / `choice` / `score`); low confidence becomes actionable statuses.
- **Token shift off the caller** — page reading moves to Jev; MCP results stay small vs full aria snapshots on large pages (with measured caveats on small pages).
- **Irreversible-action pause** — rounds ask whether the next action is hard to undo; re-call with `allow_irreversible: true` only if the user wants it.
- **WebMCP** — pages registering `document.modelContext` tools are offered alongside clicks; Jev fills args from `values` / enums; non-`readOnlyHint` tools are guarded like irreversible clicks.
- **`browser_read` vs `browser_snapshot`** — snapshot is numbered elements + viewport text for acting; read ranks full-document blocks against a question (fail-open on unrateable blocks).
- **Library, CLI, and MCP** — `JevBrowser` npm API, `bin/jev-browser.mjs` for one-shot/flows, plugin skill for writing steps and handling statuses.
- **Privacy locally** — no project telemetry; page context goes to TypeSafe or OpenRouter; secret-named `values` keys and password fields are redacted from API payloads; Playwright types real values locally.

## Architecture

Core lives under `src/`: `session.mjs` (`JevBrowser` settle/snapshot/decide/act/do/check/choose), `page-script.mjs` (in-frame element/label/state extraction), `page-model.mjs` (diff, counts, compact render), `webmcp.mjs` (init-script tool recording), `prune.mjs` (`browser_read` block split/batch/rank), `jev.mjs` (System One client), and `flow.mjs` (JSON flow runner). `bin/` holds the CLI and MCP server; `.claude-plugin/` and `skills/jev-browser/` ship the Claude Code marketplace plugin; `bench/` and `bin/jev-cost.mjs` measure task correctness and two-sided caller-vs-Jev token cost. Large pages can use two-stage element selection (pages with 2,000+ elements).

## Example usage

Library:

```js
import { JevBrowser } from "jev-browser";

const b = await JevBrowser.launch({ headed: true });
await b.open("https://www.saucedemo.com/");
await b.do("Log in", { values: { username: "standard_user", password: "secret_sauce" } });
await b.do("Add the Sauce Labs Backpack to the cart");
const p = await b.check("Does the cart badge show 1 item?");
await b.close();
```

CLI:

```bash
node bin/jev-browser.mjs do https://the-internet.herokuapp.com/login "Log in" username=tomsmith 'password=SuperSecretPassword!'
node bin/jev-browser.mjs run examples/flows/todomvc.json --headed
```

## Maintenance status

MIT License; default branch `main`; latest release **v0.2.1** at ingest (126 stars, primary language JavaScript). CI runs offline tests on push/PR; tagging via `npm version` publishes to npm with provenance and a GitHub release, keeping `.claude-plugin/plugin.json` and `.mcp.json` version-pinned in sync. Unofficial project, not affiliated with TypeSafe; calls the TypeSafe System One API (or OpenRouter's Jev listing) with the user's own key.
