---
type: source
category: "Terminal, session & parallel-agent runners"
source_url: https://github.com/herdrdev/herdr
tags:
  - agent-multiplexer
  - terminal-runtime
  - rust
  - coding-agents
  - session-persistence
  - socket-api
  - tmux-alternative
  - pane-management
related:
  - herdr.dev
  - tmux-tmux
  - tmuxai.dev
  - stablyai-orca
  - zenbu-labs-terminal-browser
product: herdr.dev
detail_level: standard
created: 2026-10-20
updated: 2026-10-28
---

herdr (~45k stars, Apache-2.0, v0.9.5) is a Rust agent multiplexer / terminal runtime — "the runtime your coding agents live on" — that keeps coding-agent panes running in a background server across detach and SSH drops, marks each pane working/blocked/idle, and lets agents drive panes via CLI and socket API without wrapping Claude Code, Codex, Cursor, OpenCode, Grok, or other tools they already use.

_All claims below are sourced from ../../raw/github/herdrdev-herdr.md unless otherwise noted._

## What it does

herdr owns the terminals your agents run in. Closing the client or losing SSH does not stop work: a background server keeps panes alive; after a server/machine restart it restores saved layout and can resume supported agent sessions (original processes do not survive). Local work and saved SSH machines share one window with a combined agent list and independent reconnects. Every pane is marked working, blocked, or idle so you do not hunt for the stuck agent. Agents can spawn panes, prompt each other, and wait until another agent is genuinely blocked. Keyboard (tmux-style prefix) and mouse (click, drag, split) are both first-class; plugins extend panes/workflows. One Rust binary, no Electron — runs in whatever terminal you already use. Docs: [[herdr.dev]] ([docs](https://herdr.dev/docs/)).

## Installation

```bash
curl -fsSL https://herdr.dev/install.sh | sh
# or: brew install herdr
# or: mise use -g herdr
# Windows: powershell -ExecutionPolicy Bypass -c "irm https://herdr.dev/install.ps1 | iex"
```

Binaries also ship on GitHub Releases. Then:

```bash
herdr                 # start where the work lives
# ctrl+b q            # detach
# herdr               # reattach
```

From source:

```bash
git clone https://github.com/herdrdev/herdr
cd herdr
cargo build --release
just test             # unit tests
just check            # formatting, tests, maintenance checks
```

## Key features

- **Detach without stopping work** — background server owns terminals; reconnect restores layout; supported agents can resume after restart ([session state](https://herdr.dev/docs/session-state/)).
- **Several machines, one window** — local + saved SSH machines, combined agent list, independent reconnects.
- **Agent status at a glance** — panes marked working / blocked / idle; blocked agents that need an answer are surfaced.
- **Agent-native control** — CLI + socket API for spawning panes, cross-agent prompts, wait-until-blocked ([agent skill](https://herdr.dev/docs/agent-skill/)).
- **Runs existing agents** — does not wrap or replace Claude Code, Codex, Cursor, OpenCode, Grok, etc.; optional [add herdr support](https://herdr.dev/docs/add-herdr-support/) for agent authors.
- **Keyboard + mouse** — tmux-style prefix keys and click/drag/split.
- **Plugins** — extend panes and workflows ([marketplace](https://herdr.dev/plugins/)).
- **Channels** — stable by default; opt into preview with `herdr channel set preview` then `herdr update`.

## Architecture

Design principles from project agent docs:

- **State separated from runtime** — `AppState` is pure data (testable without PTYs); `PaneState` separate from `PaneRuntime`.
- **Pure render** — `compute_view()` for geometry/mutations; `render()` takes `&AppState` and only draws.
- **Detection decoupled** — detector reads a screen snapshot (evidence-based manifests under `src/detect/manifests/`), never parser/viewport state; agents read panes with `herdr agent read <pane> --source detection`.
- **Platform isolation** — OS-specific code in `src/platform/<os>.rs`.
- **Server/client boundary** — migrating toward a server-owned runtime protocol with the TUI as one client; shared facts via JSON API/events, presentation state client-only. Stable client endpoint generation 1 is the compatibility floor for Local, SSH, and Cloud.
- **Performance** — view/render/PTY/detection paths treated as multiplicative (per event × panes × clients); hidden panes parse without presentation work.

Release model: one `master` branch, stable + preview channels; stable promotes a published preview tag, never raw `master` tip.

## Example usage

```bash
herdr
# run agents in panes, split as needed
# ctrl+b q   → detach
herdr        # reattach

herdr channel set preview
herdr update
herdr channel set stable

# Agent/debug helpers (from project docs)
herdr agent read <pane> --source detection --format text
herdr agent explain <pane> --json
herdr server reload-agent-manifests
```

Install the agent skill from the stable skill path when needed (`npx skills add herdrdev/herdr --skill herdr -g` installs from `master` per project notes; `skills/herdr/SKILL.md` tracks the latest stable release).

## Maintenance status

- **Stars:** 44,870 (fetched 2026-10-20)
- **Latest release:** v0.9.5
- **Default branch:** `master` (pushed 2026-10-18)
- **License:** Apache License 2.0
- **Language:** Rust
- **Homepage:** https://herdr.dev
- Homebrew formula available; multi-arch release assets (linux/macOS x86_64+aarch64, Windows zip with ConPTY). External contributions gated via `CONTRIBUTING.md` / maintainer agent workflow.
