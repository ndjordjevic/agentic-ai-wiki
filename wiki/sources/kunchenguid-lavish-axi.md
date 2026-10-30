---
type: source
category: "Design & UI generation"
source_url: https://github.com/kunchenguid/lavish-axi
tags:
  - html-artifacts
  - visual-planning
  - axi-cli
  - human-in-the-loop
  - mermaid-whiteboard
  - agent-skills
  - layout-audit
related:
  - axi.md
  - skills.sh
  - backnotprop-plannotator
  - kunchenguid-compact-adviser
  - kunchenguid-firstmate
product: lavish-axi
detail_level: standard
created: 2026-10-30
updated: 2026-10-30
---

lavish-axi (~4.4k★, MIT, v0.1.96) is an AXI CLI that opens agent-generated HTML artifacts in a local browser so humans can annotate elements/text, edit Mermaid whiteboards, queue layout fixes, and poll feedback back to the agent — replacing screenshot-and-prose review loops with pinpointable, interactive HTML.

_All claims below are sourced from ../../raw/github/kunchenguid-lavish-axi.md unless otherwise noted._

## What it does

Agents write rich HTML plans, comparisons, diagrams, and reports; Lavish serves that file locally, injects a small annotation SDK into a sandboxed iframe, and exposes a poll/reply loop so queued human notes become agent prompts. The saved HTML stays the source of truth (identical when opened without Lavish). Optional export inlines local assets; optional `share` publishes to third-party ht-ml.app.

## Installation

Recommended: `npx skills add kunchenguid/lavish-axi --skill lavish` (Agent Skills stub that teaches `npx -y lavish-axi`). Zero-setup: tell any capable agent to run `npx -y lavish-axi`. Global CLI + ambient context: `npm install -g lavish-axi` then `lavish-axi setup hooks` (SessionStart for Claude Code, Codex, OpenCode, Copilot CLI) or `lavish-axi setup plugin` (VS Code / Cursor / Copilot Agent Plugin). From source: clone, `pnpm install --frozen-lockfile`, `pnpm run build`, `pnpm link`.

## Key features

- Element and selected-text annotations; Mermaid whiteboard edits returned as summaries for the agent to apply to source
- Passive layout-issues inbox (escaped content, clipped text, occlusion) with queue-selected-fixes → normal feedback path
- Delivery receipts (Seen / Working / Done) from server-observed poll, file change, and reply
- Opt-in revisions legend (`data-lavish-revisions`) and playbooks via `lavish-axi design` / `playbook`
- Local-first state under `~/.lavish-axi/`; Tailscale-aware bind (loopback + MagicDNS phone URL); self-paint warning for missing page backgrounds
- TOON-oriented AXI ergonomics: long polling, contextual disclosure, skill stub that defers to live `--help`

## Architecture

Node 22+ ESM JavaScript (`src/cli.js`, `server.js`, chrome UI, whiteboard/mermaid, layout-warnings, export/share, playbooks, skill/plugin generators). Sessions keyed by canonical HTML file path; one background server per port serves all sessions. Docs split ownership: README (user contract/CLI), VISION (acceptance policy), `docs/invariants.md` (security/internals), generated `skills/lavish/SKILL.md` stays a stub. Optional browser E2E via `chrome-devtools-axi`.

## Example usage

```sh
npx skills add kunchenguid/lavish-axi --skill lavish
# in Claude Code:
/lavish let's discuss our plan here
# or:
npx -y lavish-axi path/to/plan.html
npx -y lavish-axi poll   # agent waits for queued human prompts
```

## Maintenance status

~4,358 stars, ~401 forks, MIT, default branch `main`, latest release `lavish-axi-v0.1.96` (2026-10-29), active CI + release-please, npm package `lavish-axi`, Discord + X (@kunchenguid). Human PRs gated via `no-mistakes`. Companion ecosystem: AXI design principles at [[axi.md]]; same author as [[kunchenguid-compact-adviser]] / [[kunchenguid-dotfiles]].
