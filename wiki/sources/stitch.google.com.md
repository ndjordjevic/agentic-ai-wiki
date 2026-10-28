---
type: source
category: "Design & UI generation"
source_url: https://stitch.google.com/docs/cli/overview
companion_urls:
  - https://github.com/google-labs-code/stitch-sdk
raw_files:
  - ../../raw/web/stitch.google.com.md
  - ../../raw/github/google-labs-code-stitch-sdk.md
tags:
  - stitch-cli
  - ui-generation
  - agent-skills
  - mcp-server
  - design-md
  - google-labs
  - vibe-design
  - coding-agents
related:
  - stitch.withgoogle.com
  - designmd.cc
  - voltagent-awesome-design-md
  - open-design.ai
  - aura.build
  - skills.sh
  - leonxlnx-taste-skill
  - Nutlope-hallmark
product: stitch
detail_level: standard
created: 2026-10-28
updated: 2026-10-28
---

Stitch's developer surface (docs at `stitch.google.com` / `stitch.withgoogle.com/docs`, inbox URL: CLI overview) adds a terminal + coding-agent workflow on top of the Google Labs UI generator covered by [[stitch.withgoogle.com]]: the `@google/stitch` CLI, Agent Skills (`/stitch`), MCP server, and `@google/stitch-sdk` for programmatic screen generation. Official docs pages are a JS SPA that did not yield extractable body text at ingest time; CLI/docs detail below is grounded in official `llms.txt`, Google announcements, and a third-party mirror that attributes Original URLs under `stitch.withgoogle.com/docs/`.

_All claims below are sourced from ../../raw/web/stitch.google.com.md unless otherwise noted._

## What it does

Beyond the hosted Canvas UI, Stitch ships tooling so developers and coding agents can:

- Install `@google/stitch` (Node 20+) and drive Canvas projects from the terminal (`stitch login`, `create project`, `generate screen`, `serve`, `open project`).
- Install bundled Agent Skills via `stitch agent-skills add --user` so Claude Code, Cursor, Gemini CLI, Antigravity, and similar agents can invoke `/stitch` workflows.
- Capture live local app routes onto the Canvas (`stitch capture` / `upload`), sync `DESIGN.md`, and run design reviews against a running app.
- Optionally enable workspace/"loop" features (`stitch enable loop`) for repo-connected prototyping, priorities/context, and codebase-driven UI proposals.
- Call the same generation pipeline from TypeScript via `@google/stitch-sdk` (`project.generate`, `getHtml`, `getImage`, variants, edits). (../../raw/github/google-labs-code-stitch-sdk.md)

## Key features

- **CLI quickstart** — `npm install -g @google/stitch` or `npx @google/stitch`; OAuth via `stitch login` or `STITCH_API_KEY` / `stitch config set apiKey … --global` for headless/CI.
- **Prompt → screen** — `stitch generate screen --title … --device DESKTOP|MOBILE --prompt "…"`; pin a project with `stitch config set project <id>`.
- **Local preview** — `stitch serve` for localhost HTML preview; `stitch open project` for Canvas in the browser.
- **Agent bridge** — `stitch agent-skills add --user` plus MCP tooling so agents generate screens, sync DESIGN.md, and audit UI without hand-writing full HTML.
- **Capture & upload** — snapshot local routes and push them onto the Canvas for iterative edit prompts.
- **Workspace loop** — after `stitch enable loop`, connect repositories, set priorities/context, and generate codebase-informed prototypes.
- **SDK** — `@google/stitch-sdk` (~1.8k★, Apache-2.0, npm ~0.4.0) for create/generate/edit/variants and HTML/screenshot artifact URLs; optional Vercel AI SDK helpers. (../../raw/github/google-labs-code-stitch-sdk.md)
- **Related skills repo** — `google-labs-code/stitch-skills` (~8.6k★) packages Agent Skills/plugins for the Stitch MCP server (not the companion raw for this page, but part of the same Labs org).

## Architecture

Stitch's agent-facing design model (from official `llms.txt`) still centers the **3-layer vibe prompt** — Anatomy, Vibe, Content — and an **Agent Protocol** that tells coding agents to formulate that prompt and send users to Stitch rather than emitting full UI code themselves.

Developer architecture adds layered surfaces:

| Surface | Role |
|---|---|
| Canvas web app | Hosted generation UI (`stitch.withgoogle.com`) |
| Docs SPA | `stitch.google.com/docs/*` (Nemo / appcompanion shell; content not SSR-extractable at ingest) |
| CLI `@google/stitch` | Resource verbs (`find`/`get`/`create`/`edit`/`delete`/`generate`) + serve/capture/upload/config/login + MCP/agent-skills |
| MCP + Skills | Agent-native tool/skill layer for the same workflows |
| SDK `@google/stitch-sdk` | Programmatic TypeScript client over the generation API | (../../raw/github/google-labs-code-stitch-sdk.md)

`DESIGN.md` remains the portable design-system contract (see [[designmd.cc]] / [[voltagent-awesome-design-md]]); CLI flows include `stitch upload design` and design-review against a running app.

## Installation

```bash
npm install -g @google/stitch   # Node.js 20+
stitch --version
stitch login
# or: export STITCH_API_KEY=… / stitch config set apiKey "…" --global
stitch agent-skills add --user
```

SDK:

```bash
npm install @google/stitch-sdk
# optional: npm install ai   # for Vercel AI SDK stitchTools()
```

(../../raw/github/google-labs-code-stitch-sdk.md)

## Example usage

CLI (from mirrored CLI overview attributed to `stitch.withgoogle.com/docs/cli/overview/`):

```bash
stitch create project --title "Checkout Redesign"
stitch config set project <project-id>
stitch generate screen \
  --title "Order Summary" \
  --device DESKTOP \
  --prompt "A clean two-column checkout summary on warm paper (#FAF8F5) with itemized billing, shipping selector, and a primary payment button"
stitch serve
stitch open project
```

SDK: (../../raw/github/google-labs-code-stitch-sdk.md)

```ts
import { stitch } from "@google/stitch-sdk";
const project = stitch.project("your-project-id");
const screen = await project.generate("A login page with email and password fields");
const html = await screen.getHtml();
const imageUrl = await screen.getImage();
```

## When to use

- You already use [[stitch.withgoogle.com]] in the browser and want the same generation loop from a terminal or coding agent.
- You need **DESIGN.md-aware** agent workflows (skills/MCP/CLI) rather than one-off Canvas sessions.
- You want programmatic batch generation or integration tests via `@google/stitch-sdk`.
- Prefer the Canvas-only product page [[stitch.withgoogle.com]] for vibe-design concepts, Figma paste, and the original agent protocol narrative; use this page for CLI/MCP/SDK command surfaces.

## Maintenance status

`google-labs-code/stitch-sdk` is Apache-2.0, ~1,836 stars, default branch `main`, package.json version 0.4.0, latest git tag seen at ingest `v0.4.0-canary.1`, homepage `https://stitch.withgoogle.com/docs`. (../../raw/github/google-labs-code-stitch-sdk.md)

## Ecosystem

Pairs with [[stitch.withgoogle.com]] (same `product: stitch`), DESIGN.md tooling ([[designmd.cc]], [[voltagent-awesome-design-md]]), taste/anti-slop design skills ([[leonxlnx-taste-skill]], [[Nutlope-hallmark]]), and agent skill distribution ([[skills.sh]]). Adjacent AI builders ([[aura.build]], [[open-design.ai]]) solve overlapping design-to-UI problems with different hosting and agent models.

## Documentation

Official docs live under `https://stitch.google.com/docs/…` (also linked as `stitch.withgoogle.com/docs/…`). At ingest, those routes required a client-rendered SPA and returned no extractable article body; use the in-product docs UI, npm READMEs, `stitch.google.com/llms.txt`, and the attributed mirror at `stitchprompt.com/docs/` (pages end with `Original: https://stitch.withgoogle.com/docs/…`) for offline capture. Key mirrored topics: CLI overview & command reference, MCP setup, skills get-started, learn/prompting, device types, DESIGN.md overview.
