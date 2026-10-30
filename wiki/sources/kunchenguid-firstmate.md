---
type: source
category: "Terminal, session & parallel-agent runners"
source_url: https://github.com/kunchenguid/firstmate
tags:
  - agent-distro
  - multi-agent-crew
  - git-worktrees
  - tmux-herdr-backends
  - supervision
  - parallel-agents
  - captain-firstmate
related:
  - herdr.dev
  - herdrdev-herdr
  - stablyai-orca
  - tmux-tmux
  - openai-symphony
  - kylon.io
  - kunchenguid-lavish-axi
  - kunchenguid-dotfiles
product: firstmate
detail_level: standard
created: 2026-10-30
updated: 2026-10-30
---

firstmate (~8.4k★, MIT) is an agent distro — a portable repo of `AGENTS.md`, skills, and helper scripts — that turns one primary coding-agent session into a "first mate" who spawns a visible crew of autonomous workers in tmux/Herdr/(experimental) Zellij/Orca/cmux/… backends, each in an isolated git worktree, and returns PRs, approved merges, or scout reports. You talk only to the first mate; it supervises the fleet with near-zero-token bash watchers.

_All claims below are sourced from ../../raw/github/kunchenguid-firstmate.md unless otherwise noted._

## What it does

Instead of juggling multiple agent tabs, you clone firstmate and launch a supported harness inside it. That session becomes the first mate: it clones/registers projects under `projects/`, dispatches ship (authorized changes → PR/merge) or scout (investigation report) tasks, watches crewmates to completion, and escalates only real captain decisions. Optional persistent secondmates run isolated `FM_HOME`s locally or over SSH. Optional Relay answers X/Discord mentions through the same lifecycle.

## Installation

Requirements: verified primary harness (Claude Code, Grok, Pi/`pi-signed`, Oh My Pi, Codex, OpenCode, Cursor Agent CLI, or Antigravity CLI), Git + authenticated `gh`, and a session backend (tmux default). Clone `https://github.com/kunchenguid/firstmate`, `cd firstmate`, then launch e.g. `claude`, `grok --trust`, or `pi`. No separate app install — the checkout is the distro. Backend-specific setup is documented under `docs/*-backend.md`.

## Key features

- One liaison (first mate) + visible crew in backend panes/tabs
- Disposable treehouse (or Orca) worktrees per task; project modes `no-mistakes` / `direct-PR` / `local-only` (+ optional `+yolo`, Gerrit forge, manual PR text)
- Event-driven bash watcher + harness turn-end backstops (no blind stop while work is live)
- Self-repo boundary (won't PR upstream firstmate without maintainer opt-in)
- Optional Relay (X/Discord), voice-relay docs, fleet ledger, usage warner, `/calm` presentation mode, `/bearings` status digests, `/stow` knowledge sweep
- Public `skills/stow` installable standalone; internal `.agents/skills/` marked `metadata.internal: true`

## Architecture

Captain ↔ firstmate home (disk state + routes) ↔ backend-spawned crewmates in worktrees or secondmate homes. Primary harnesses get tracked Stop/session hooks so supervision re-arms without burning tokens. Architecture detail in `docs/architecture.md`; configuration/`FM_HOME`/backends in `docs/configuration.md`. Shell-primary codebase with `bin/` toolbelt and extensive verification docs under `docs/verification/`.

## Example usage

```sh
gh auth login
git clone https://github.com/kunchenguid/firstmate
cd firstmate
claude   # or: grok --trust | pi | omp | ...
# then in chat:
# > ahoy! look at my github project xyz, then fix the flaky login test and add dark mode
```

## Maintenance status

~8,427 stars, ~2,674 forks, MIT, default branch `main`, no GitHub Releases tags at ingest (active tip as of 2026-10-30). Same author ecosystem as [[kunchenguid-lavish-axi]] / [[kunchenguid-dotfiles]]. Discord + X (@kunchenguid). Contributing gated via `.no-mistakes.yaml` / CONTRIBUTING.md.
