---
type: source
source_url: https://github.com/garrytan/gstack
tags:
  - claude-code-skills
  - virtual-engineering-team
  - agent-workflow
  - browser-automation
  - sprint-methodology
  - multi-agent
  - ios-qa
  - ai-productivity
related:
  - anthropics-skills
  - obra-superpowers
  - gsd-build-get-shit-done
  - forrestchang-andrej-karpathy-skills
  - skills.sh
  - buildermethods-agent-os
  - everyinc-compound-engineering-plugin
product: gstack
detail_level: standard
created: 2026-05-25
updated: 2026-05-25
---

gstack is Garry Tan's (CEO of Y Combinator) open-source software factory — a 101,913-star MIT-licensed collection of 50+ opinionated Claude Code skills that transforms a single developer with AI into a virtual engineering team. Where other skill packs provide isolated utilities, gstack builds a complete sprint pipeline: Think → Plan → Build → Review → Test → Ship → Reflect. Each step feeds into the next; design docs written by `/office-hours` flow into `/plan-ceo-review`, test plans from `/plan-eng-review` are picked up by `/qa`, and bugs found by `/review` are re-verified by `/ship`. The result is a structured workflow, not a bag of prompts.

_All claims below are sourced from ../../raw/github/garrytan-gstack.md unless otherwise noted._

## What it does

gstack gives every Claude Code session a roster of named specialists: a YC partner-style product interrogator (`/office-hours`), a CEO (`/plan-ceo-review`), an eng manager (`/plan-eng-review`), a senior designer (`/plan-design-review`), a DX lead (`/plan-devex-review`), a staff engineer (`/review`), a QA lead (`/qa`), a security officer (`/cso`), a release engineer (`/ship`), and a post-deploy SRE (`/canary`). When these skills run in sequence they reproduce a complete software sprint inside a single AI coding session. Additionally, gstack includes a long-lived Chromium daemon for real browser-based QA, iOS testing via USB CoreDevice tunnels, memory-sync via gbrain, multi-agent browser sharing via `pair-agent`, and a self-update mechanism so teams stay on the same version without manual upgrades.

## Key features

- **Sprint-ordered skill pipeline:** `/autoplan` chains CEO → design → eng → DX review automatically, surfacing only taste decisions for human approval before implementation begins.
- **Persistent headless browser:** A Bun-compiled binary runs a Chromium daemon at `127.0.0.1:PORT` with ~100ms per command after the first call (~3s cold start). Cookies, tabs, and login sessions survive between skill invocations.
- **50+ slash-command skills** covering every phase: planning, code review, design generation, browser QA, iOS QA, security audit, release, deploy monitoring, context save/restore, performance benchmarking, and documentation generation.
- **Multi-host support:** `./setup --host <name>` installs gstack for 10 agents — Claude Code, OpenAI Codex CLI, Cursor, Factory Droid, Slate, Kiro, Hermes, GBrain, OpenCode, and GitHub Copilot.
- **Team mode:** `./setup --team` bootstraps a shared repo so teammates auto-update; the update check runs once per hour, is network-failure-safe, and is completely silent.
- **Cross-agent browser sharing via `/pair-agent`:** Exposes a scoped ngrok tunnel to let OpenClaw, Codex, Cursor, or any agent drive the same browser session. Dual-listener architecture (local port vs tunnel port) ensures root tokens and cookie endpoints never reach the tunnel.
- **iOS QA skills:** `/ios-qa` drives a real iPhone over USB CoreDevice tunnel with StateServer; `/ios-fix` closes the find→fix→verify loop; `/ios-design-review` applies a 10-dimension Apple HIG rubric.
- **Safety skills:** `/careful` warns before destructive commands, `/freeze` locks edits to one directory, `/guard` combines both.
- **ETHOS.md philosophy** is injected into every skill preamble: "Boil the Lake" (do the complete thing — completeness is near-zero cost with AI), and "Search Before Building."

## Architecture

gstack is structured as a Bun/TypeScript monorepo where each top-level directory is a self-contained skill — a SKILL.md file generated from a `.tmpl` template. The browse daemon is the only compiled binary (~58MB), built with `bun build --compile`. It exposes a JSON-over-HTTP API on a random localhost port (10000–60000) and communicates with Chromium via CDP.

The state file `.gstack/browse.json` (atomic write, mode 0o600) stores the running daemon's PID, port, auth token, and binary hash. On each CLI invocation the CLI checks the binary hash against the running server's hash and auto-restarts on mismatch — preventing the "stale binary" class of bugs.

Security boundaries are enforced by physical port separation rather than header inference: the full API surface listens on the local port only; an optional tunnel port (bound lazily via `/tunnel/start`) serves a locked allowlist of three paths. ngrok forwards only the tunnel port.

SKILL.md files are not hand-edited — they are regenerated from `*.tmpl` templates via `bun run gen:skill-docs`. The `hosts/` directory holds per-agent format rules so one template generates correct output for all 10 supported agents.

## Installation

```bash
# Personal install (Claude Code)
git clone --single-branch --depth 1 https://github.com/garrytan/gstack.git ~/.claude/skills/gstack
cd ~/.claude/skills/gstack && ./setup

# Team mode (shared repo, auto-update)
(cd ~/.claude/skills/gstack && ./setup --team)
~/.claude/skills/gstack/bin/gstack-team-init required
git add .claude/ CLAUDE.md && git commit -m "require gstack for AI-assisted work"

# Other agents
./setup --host codex     # OpenAI Codex CLI
./setup --host cursor    # Cursor
./setup --host factory   # Factory Droid
```

Or ask Claude Code directly: paste the one-line install prompt from the README into a Claude Code session and Claude handles the clone, setup, and CLAUDE.md registration automatically.

## Example usage

```
You: /office-hours
Claude: [six forcing questions about your pain, not your feature request]
        [challenges the framing, extracts what you're actually building]
        [writes design doc to disk]

You: /plan-ceo-review
Claude: [reads design doc, applies CEO-lens, runs 10-section review]
        [four scope modes: Expansion / Selective Expansion / Hold Scope / Reduction]

You: /plan-eng-review
Claude: [ASCII diagrams for data flow, state machines, error paths]
        [test matrix, failure modes, security concerns]

You: Approve plan. Exit plan mode.
Claude: [writes 2,400 lines across 11 files — ~8 minutes]

You: /review
Claude: [AUTO-FIXED] 2 issues. [ASK] Race condition → you approve fix.

You: /qa https://staging.myapp.com
Claude: [opens real Chromium, clicks through flows, finds and fixes a bug]

You: /ship
Claude: Tests: 42 → 51 (+9 new). PR: github.com/you/app/pull/42
```

## Maintenance status

101,913 stars, 15,217 forks. Version 1.44.0.0 (May 2026). Active daily development by Garry Tan, with 1,237+ GitHub contributions in 2026 alone. MIT license. No formal releases — version tracked in a `VERSION` file updated with each commit. Active changelog (742KB). Community contributions in `contrib/`.

## Ecosystem

gstack integrates with gbrain for cross-machine session memory sync, OpenClaw (ACP-based agent spawner) for autonomous task delegation, ngrok for remote agent browser sharing, Fly.io/Render/Vercel for deploy automation, Supabase for database integrations, and ClawHub for distributing four native OpenClaw methodology skills. The `/codex` skill integrates OpenAI Codex CLI for a second-opinion code review in cross-model setups. In the broader agent-skills ecosystem it stands alongside [[anthropics-skills]] (Anthropic's official skills library), [[obra-superpowers]] (spec-first subagent skills), and [[gsd-build-get-shit-done]] (context-engineering commands) as the most comprehensive opinionated Claude Code workflow packs; it is distinguished from these by its persistent browser daemon, iOS QA capabilities, and the explicit sprint methodology that chains skills into a complete software development lifecycle.
