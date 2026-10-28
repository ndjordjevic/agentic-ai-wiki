---
type: source
category: "Coding agents, IDEs & dev environments"
source_url: https://github.com/Larkspur-Wang/Jev_steer_or_queue
tags:
  - mid-turn-steering
  - message-queue
  - jev-model
  - claude-code-plugin
  - interrupt
  - codex-cli
  - fails-open
related:
  - typesafe.ai
  - RiskAverseTech-toolgate
  - valentynkit-jev-belay
  - njbrake-agent-of-empires
product: jev-steer-or-queue
detail_level: standard
created: 2026-10-28
updated: 2026-10-28
---

jev-steer-or-queue is a Claude Code plugin (Codex CLI support in testing) that asks TypeSafe Jev whether a message you send mid-turn should **steer** the running task, **queue** for after the turn, or **interrupt** and stop — instead of treating every mid-turn message the same way. Classification runs in about half a second; idle messages are never sent to Jev. Queue and interrupt only apply when Jev is confident (probability ≥ 0.9, and interrupt also needs an explicit stop signal); otherwise the client's native behaviour wins. Failures (missing key, network error, timeout) fail open and pass the message through.

_All claims below are sourced from ../../raw/github/Larkspur-Wang-Jev_steer_or_queue.md unless otherwise noted._

## What it does

Coding agents often inject every mid-turn message into the running turn immediately. That suits course corrections like "use the simpler approach," but mixes follow-ups such as "when you're done, update the changelog" into the current task, and "stop" only works if the model chooses to stop. This project classifies each mid-turn message into one of three timings: **steer** (let through for native injection at the next tool boundary), **queue** (hold in a per-session FIFO and replay when the turn ends via the Stop hook), or **interrupt** (swallow the message and end the turn at the next tool boundary with `continue:false`). Mid-turn detection on Claude Code uses the running turn's `prompt_id`; a new turn gets a fresh one.

## Installation

Claude Code:

```text
/plugin marketplace add Larkspur-Wang/Jev_steer_or_queue
/plugin install jev-steer-or-queue@jev-steer-or-queue
```

Claude Code then prompts for a TypeSafe API key (from [console.typesafe.ai](https://console.typesafe.ai/), stored in the system keychain, or leave empty to use `TYPESAFE_API_KEY`) and a mode: `shadow` (default, log only) or `active` (queue and stop for real). Start in `shadow`, then switch to `active` via `/config`. Codex CLI has a separate `codex/` adapter; API key for Codex lives in `~/.jev-steer-or-queue/config.json`.

## Key features

- **Three-way mid-turn routing** — steer / queue / interrupt via Jev, with queue and interrupt gated at probability ≥ 0.9 (interrupt also needs an explicit stop signal).
- **Fails open** — missing key, network error, or timeout (default 2 s) leaves the message untouched.
- **Shadow vs active modes** — shadow only logs decisions; active applies queue and interrupt.
- **Per-session FIFO queue** — held messages replay after the turn as Stop hook feedback; Esc-cancelled queue contents are listed and dropped on the next prompt.
- **Privacy-bounded Jev payload** — mid-turn only: message up to 2,000 characters plus task start up to 500 characters; no transcript, files, or tool output. Logs stay local; `JEV_ROUTER_LOG_PROMPTS=false` keeps message text out of them.
- **Dual client layout** — self-contained `claude-code/` (tested end-to-end on 2.1.280) and `codex/` (tested on 0.156.1; Codex can only be nudged, not blocked — blocking hangs the turn).

## Architecture

A `UserPromptSubmit` hook fires when you type while the agent works. Idle messages pass through without calling Jev. Mid-turn messages go to Jev (~0.5 s typical; measured ~438–660 ms). Steer allows native injection; queue blocks and enqueues for Stop-hook replay; interrupt blocks and flags the next tool hook to return `continue:false`. Unsure / error / timeout falls back to allow. The hook can only stop at tool boundaries — a running command finishes first, and a text-only turn can't be stopped. Python 3.8+, no declared dependencies beyond the router script; MIT licensed, not affiliated with TypeSafe, Anthropic, or OpenAI. (../../raw/github/Larkspur-Wang-Jev_steer_or_queue.md)

## Example usage

After install, leave mode on `shadow` and watch the local decision log while you send mid-turn messages during long tool runs (e.g. course corrections, follow-ups, or "stop"). When the classifications look right, switch to `active` in `/config`. Typical outcomes from the project's e2e notes: queue completes the current turn then replays the held request as Stop hook feedback; steer injects at the next tool boundary; interrupt stops after the current tool without starting a new turn. On Codex, the adapter never returns `decision:block` (that hangs the TUI); it soft-prompts instead and filters internal Codex prompts via `INTERNAL_MARKERS`. (../../raw/github/Larkspur-Wang-Jev_steer_or_queue.md)

## Maintenance status

MIT License © 2026 Larkspur-Wang; default branch `main`; no tagged GitHub releases at ingest time; 17 stars. Claude Code plugin is the primary, e2e-tested path; Codex CLI is supported soft (nudge-only). README invites PRs for misclassified mid-turn messages, Codex results, and adapters for other clients (Cursor, Grok Build, OpenClaw). Prior art cited: OpenClaw queue modes and other Jev-based routers. (../../raw/github/Larkspur-Wang-Jev_steer_or_queue.md)
