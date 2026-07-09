---
type: source
source_url: https://herdr.dev/
companion_urls:
  - https://github.com/ogulcancelik/herdr
raw_files:
  - ../../raw/web/herdr.dev.md
  - ../../raw/github/ogulcancelik-herdr.md
tags: [agent-multiplexer, terminal, tmux-alternative, coding-agents, rust, pane-management, session-persistence, socket-api]
related: [tmux-tmux, tmuxai.dev, kunchenguid-dotfiles]
product: herdr
detail_level: standard
created: 2026-07-09
updated: 2026-07-09
---

Herdr is an agent multiplexer for the terminal — "to coding agents what tmux is to terminals." It runs a persistent background server that keeps every coding agent alive across detach, SSH reconnects, and laptop lid closes. A single `herdr` command attaches to (or creates) a session with workspaces, tabs, and panes; each pane runs a real terminal process and Herdr tracks its agent state (blocked, working, done, idle) in a sidebar across all workspaces. Written in Rust with 14,500+ GitHub stars, Herdr ships as a single binary with no Electron, no account, and no telemetry, and supports 18+ coding agents including Claude Code, Codex, GitHub Copilot CLI, Pi, OpenCode, and Hermes Agent.

_All claims below are sourced from ../../raw/web/herdr.dev.md unless otherwise noted._

## What it does

Herdr wraps your coding agent workflow in a persistent terminal session. Running `herdr` in a project directory launches or attaches to a background server; any agent started in a pane (Claude Code, Codex, Pi, opencode…) keeps running if you close the terminal window. The sidebar shows every agent's state across every workspace so you see at a glance which project needs your attention without polling terminals by hand.

Key behaviors:
- **Detach + reattach**: `ctrl+b q` detaches; `herdr` reattaches from any terminal, including over SSH from a phone.
- **Session persistence**: the server owns panes — layout, workspaces, tabs, focus, and (optionally) recent screen history survive client disconnects.
- **Native agent resume**: after a server restart, Herdr can resume supported agent conversations using their official session IDs (Claude Code: `claude --resume <id>`, Codex: `codex resume <id>`, and 12 other agents with minimum integration versions).
- **Mouse-first UX**: click panes, drag borders, split via right-click — no prefix key required to start.

## Key features

- **Multi-agent dashboard**: blocked/working/done/idle state rolls up per workspace from any mix of supported agents. Screen manifests (TOML) detect state from the bottom-buffer snapshot; lifecycle hooks from integrations provide authoritative state for Pi, OMP, Kimi, Hermes, OpenCode, and others. (../../raw/github/ogulcancelik-herdr.md)
- **Remote manifest updates**: agent detection manifests update from herdr.dev in the background without restart; local overrides at `~/.config/herdr/agent-detection/<agent>.toml` always win.
- **Socket API + CLI wrappers**: a local socket API lets scripts and agents create workspaces, split panes, run commands, wait on agent state, and subscribe to events. Schema: `herdr api schema --output herdr-api.schema.json`. (../../raw/github/ogulcancelik-herdr.md)
- **Plugin system**: executable workflow plugins with manifest actions and event hooks; publishable to a community marketplace via GitHub repo tags.
- **tmux-style keybindings**: prefix key `ctrl+b`, pane splits, tabs, detach — familiar to tmux users; Herdr also supports full mouse control.
- **Live server handoff**: `herdr update --handoff` attempts to keep running agent panes alive during compatible updates.

## Architecture

Herdr follows a strict server/client split. (../../raw/github/ogulcancelik-herdr.md)

The **server** owns all persistent state: workspaces, tabs, panes, process trees, agent session references, socket API, and event streams. `AppState` is pure data testable without PTYs. The **TUI client** attaches to the server and handles rendering, keyboard/mouse input, and presentation state (sidebar layout, colors, modals). New features should go into server state exposed through the JSON API, not the private TUI socket.

The **detection engine** (`src/detect/`) reads a screen snapshot of the live bottom-buffer (not the user-scrolled viewport) and evaluates per-agent TOML manifests with AND/OR gates on invariant visible controls. Agents with lifecycle integrations report state directly; screen manifests are the fallback. Agent code is in `src/detect/manifests/<agent>.toml` — hot-reloadable from both remote updates and local overrides.

The **terminal parser** is a vendored `libghostty-vt` (Rust); `src/platform/` isolates all OS-specific PTY and process code so core modules never use `#[cfg(target_os)]`.

## Installation

```bash
# Recommended (Linux/macOS)
curl -fsSL https://herdr.dev/install.sh | sh

# Package managers
brew install herdr          # Homebrew
mise use -g herdr           # mise
nix run github:ogulcancelik/herdr/v0.7.3   # Nix flake

# Windows (preview beta)
irm https://herdr.dev/install.ps1 | iex
```

Update: `herdr update` (script installs); package-manager installs update through their own tool. Latest stable: v0.7.3. (../../raw/github/ogulcancelik-herdr.md)

## Example usage

```bash
herdr                        # launch or attach
claude                       # start Claude Code in a pane — Herdr detects it
ctrl+b v                     # split right (prefix+v)
codex                        # start Codex in the new pane
ctrl+b q                     # detach (server + agents keep running)
herdr                        # reattach from anywhere

# CLI control from scripts or other agents
herdr workspace create --cwd ~/project --label api
herdr pane split w1:p1 --direction right
herdr pane run w1:p2 "npm test"
herdr wait agent-status w1:p1 --status done
herdr pane read w1:p2 --source recent --lines 50
```

## When to use

Use Herdr when running multiple coding agents in parallel and you need:
- Persistent agent sessions that survive terminal close and SSH reconnect
- A unified view of all agent states across projects
- Script/agent automation over a socket API to orchestrate panes programmatically
- A tmux-like workflow purpose-built for coding agents rather than a generic multiplexer

Not needed if you run a single agent in a single terminal and never close the laptop while it works.

## Maintenance status

- 14,553 GitHub stars, 831 forks (../../raw/github/ogulcancelik-herdr.md)
- License: AGPL-3.0 (open source); commercial licenses available at hey@herdr.dev
- Latest stable: v0.7.3 (2026-07-07), released regularly; active development on `master`
- Sponsors: Terminal Trove (gold); GitHub Sponsors open for individuals and enterprises

## Ecosystem

Herdr integrates with all major coding agents: Claude Code, Codex, GitHub Copilot CLI, Pi, OpenCode, Hermes Agent, Kimi Code, MastraCode, Devin CLI, Cursor Agent CLI, Qoder CLI, Kilo Code CLI, Antigravity CLI, Grok CLI, Amp, Droid, OMP. It is commonly installed alongside these agents rather than instead of them — it wraps and multiplexes them.

Herdr ships a `SKILL.md` that teaches coding agents how to use it from inside a pane, and an `agent-guide.md` at `herdr.dev/agent-guide.md` for the same purpose.

Related tools: [[tmux-tmux]] (the terminal multiplexer Herdr is conceptually modeled after), [[tmuxai.dev]] (AI-enhanced tmux), [[kunchenguid-dotfiles]] (macOS dotfiles that install Herdr via Homebrew and configure it with symlinked config).
