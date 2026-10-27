---
type: source
category: "Browser & web automation"
source_url: https://github.com/reticlehq/reticle
tags:
  - runtime-perception
  - agent-verification
  - jev
  - web-testing
  - desktop-apps
  - machine-native
  - browser-check
  - qa-agents
related:
  - typesafe.ai
  - dzhng-jevgrep
  - tamaratran-fast-jev-compaction
  - microsoft-playwright-mcp
  - vercel-labs-agent-browser
  - qa.tech
  - browse.sh
product: reticle
detail_level: standard
created: 2026-10-27
updated: 2026-10-27
---

reticlehq/reticle (1,275 stars, TypeScript) puts a dev-only SDK inside your web or desktop app so a coding agent can look, act, observe and assert against the real running app, then returns a verdict (`yes` / `no` / `unknown`) with evidence and the `file:line` to fix. Its tagline is "Your AI agent says 'done.' Reticle finds out if that is true"; the repo describes it as bringing Jev-style machine-native runtime perception to web and desktop apps, and it positions itself as the in-app complement to outside-in tools such as [[microsoft-playwright-mcp]] and [[vercel-labs-agent-browser]].

_All claims below are sourced from ../../raw/github/reticlehq-reticle.md unless otherwise noted._

## What it does

The README's premise is that coding agents are optimistic by design: they write code, assume it worked, and never open the app, so broken modals, silent `500`s and "Deploy succeeded" over a failed deploy ship. Reticle reads the app from the inside (DOM, network, console, store state, React fibers), as structured events rather than pixels. Each check ends in a verdict: only `yes` is a pass, `unknown` means "cannot tell" with a reason, and `no-fault` means nothing was declared to verify. The verdict includes the request, state change and console line that decided it.

Verified flows can be saved ("save that as a flow") and replayed later with no AI model; `reticle gate --since HEAD~1` fails CI when a change touches a saved flow's code without a new passing run. Beyond agent-built changes, the README lists security-behaviour, accessibility, performance, SEO, and persona/simulation checks.

## Installation

Needs Node 20.11+, a locally run app with a dev server, and an MCP-capable coding agent.

```bash
curl -fsSL https://raw.githubusercontent.com/reticlehq/reticle/main/install/install.sh | sh
npx skills add reticlehq/reticle --skill reticle
```

Windows uses `install.ps1`. The installer runs `npm install -g @reticlehq/server` and `reticle setup install`, registering the MCP server (`npx @reticlehq/server mcp`) with every agent it finds. On Claude Code, `/plugin marketplace add reticlehq/reticle` then `/plugin install reticle@reticlehq` does both. Then restart the agent and run `reticle init` in the app folder (`--dry-run` previews, `--app <dir>` for monorepos).

## Key features

- **Verdict, not a screenshot** — `verified: "yes" | "no" | "unknown"` with network evidence and a source `file:line`.
- **Sees what the screen hides** — network responses tied to the click, real store state (zustand, Redux, TanStack Query, Pinia and more), console errors, request counts, React renders.
- **Deterministic replay** — saved flows re-verify with no model; the README's benchmark claims about 480 tokens versus about 121,000 to re-drive a four-flow suite with an LLM.
- **Benchmark vs Playwright** — an 88-bug registry (86 regressions, 2 false-positive traps): 85/88 for Reticle versus 59/88 for a Playwright script.
- **Harness** (optional, platform) — describe a persona and journey; Reticle drives and verifies each step. Free credits for new accounts, then a 14-day trial.
- **Broad support** — web (React, Next.js, Vue, Svelte, Angular and more), desktop (Electron, Tauri), and 17 auto-configured agents (Claude Code, Cursor, Windsurf, VS Code and more) plus Codex CLI.

## Architecture

Repo is a pnpm/turbo monorepo with `adapters`, `core`, `engine`, `server`, `spec-runner`, `init`, `install`, `plugins`, `skills`, `bench`, and `docs`. The in-page SDK (`@reticlehq/react`, `@reticlehq/browser`, plus `@reticlehq/vite-plugin` or `@reticlehq/next`) connects to a local bridge on `127.0.0.1:4400` with a token stored owner-only in `~/.reticle/`. A `reticle-dev` file registers stores, testids and signals. Production builds drop the SDK unless production mode is opted into. There is no "evaluate arbitrary JavaScript" tool, and secrets are replaced with `[REDACTED]`. Known gaps: IndexedDB, Web Workers, closed shadow roots, cross-origin iframes.

## Example usage

```text
"Verify the sign-up flow with Reticle."
```

The agent uses `reticle_session` and `reticle_act_and_wait` to drive the app and returns a verdict. From a terminal or CI:

```bash
reticle verify http://localhost:5173 --expect '{"kind":"element","query":{"role":"heading","name":"Welcome"},"state":"visible"}'
npx @reticlehq/server gate --since HEAD~1
```

## Maintenance status

1,275 stars, 235 forks, default branch `main`, latest release v3.8.2 (2026-10-26), most recent push 2026-10-27. GitHub metadata lists the license as "Other"; the README states a split: the SDK, adapters, core and engine are Apache-2.0, while the server, CLI, `init` and spec runner (`@reticlehq/test`) are FSL-1.1-ALv2 (Apache-2.0 two years after each release), and enterprise features need a license key in production. Packages are published with npm SLSA provenance and have no install scripts; the repo is scored by OpenSSF Scorecard and runs a Discord community. Anonymous telemetry is on by default (`reticle telemetry disable` or `DO_NOT_TRACK=1` turns it off).
