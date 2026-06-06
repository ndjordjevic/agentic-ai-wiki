---
type: source
source_url: https://github.com/tmux/tmux
tags:
  - terminal-multiplexer
  - session-management
  - tui
  - c
  - unix
  - detach-reattach
  - pane-splitting
  - scripting
related:
  - njbrake-agent-of-empires
  - tmuxai.dev
product: tmux
detail_level: standard
created: 2026-05-02
updated: 2026-06-06
---

tmux is the canonical Unix terminal multiplexer: a C program that lets a single screen host multiple terminal sessions, each of which can be detached from the display and later reattached from any other client. With 45,000+ stars and 30+ years of active development, tmux has become the foundational infrastructure layer for developer workflows, remote server management, and—increasingly—AI-agent session orchestration. Tools like [[njbrake-agent-of-empires]] and [[tmuxai.dev]] are built directly on top of its session/window/pane model.

_All claims below are sourced from ../../raw/github/tmux-tmux.md unless otherwise noted._

## What it does

tmux creates a server process that manages a tree of sessions, windows, and panes. Clients connect to that server over a Unix socket; detaching a client leaves all sessions running. Any number of clients can attach to the same session simultaneously. The result is persistent terminal state that survives disconnections, is shareable between users, and is fully scriptable from shell commands.

## Key features

- **Session / window / pane hierarchy** — sessions group windows, windows group panes; each pane is an independent terminal.
- **Detach and reattach** — `tmux detach` / `tmux attach` preserves all running processes across disconnects (essential for SSH and remote work).
- **Split panes** — horizontal and vertical splits within a single window; layouts can be saved and restored.
- **Copy mode** — scroll back, search, and copy terminal output with vi or emacs keybindings.
- **Status bar** — fully configurable format-string status line with per-session and per-window info.
- **Key bindings** — composable prefix-key system; all bindings reconfigurable via `bind-key`.
- **Scripting** — all tmux features callable from shell: `tmux new-session`, `tmux send-keys`, `tmux capture-pane`, etc.
- **Hooks** — run arbitrary commands on session/window/pane lifecycle events.
- **Popup windows** — floating overlay terminals inside a session.
- **Named buffers** — paste buffer system with multiple named slots.
- **Server ACLs** — access control for shared-socket multi-user scenarios.

## Architecture

The codebase follows a client/server split: the server process (`server.c`, `server-client.c`) owns all sessions and talks to clients over a Unix socket. Each `cmd-*.c` file implements one tmux command; ~50 such files cover the full feature set. Terminal I/O is handled by the `tty-*.c` layer with per-OS shims in `osdep-*.c` (Linux, macOS, OpenBSD, FreeBSD, NetBSD, Solaris, Cygwin). The `format.c` engine evaluates format strings for status lines and titles. The `grid.c` family maintains the terminal grid model, and `input.c` parses VT escape sequences. Platform compatibility is isolated in `compat/`.

## Installation

Binary packages are available on most distributions (may lag latest release). From release tarball:

```bash
./configure && make
sudo make install
```

From version control (requires `autoconf`, `automake`, `pkg-config`, `bison`):

```bash
git clone https://github.com/tmux/tmux.git
cd tmux && sh autogen.sh && ./configure && make
```

Dependencies: **libevent 2.x**, **ncurses**, a C compiler, make, pkg-config, yacc/bison. Detailed platform-specific instructions at https://github.com/tmux/tmux/wiki/Installing.

## Example usage

```bash
# Start a new named session
tmux new-session -s work

# Detach (leave running)
Ctrl-b d

# Reattach
tmux attach -t work

# Split pane horizontally
Ctrl-b %

# Send a command to a pane from shell (scriptable)
tmux send-keys -t work:0.1 'ls -la' Enter

# Capture pane output (used by AI tools like TmuxAI and Agent of Empires)
tmux capture-pane -t work:0.0 -p

# Example tmux.conf snippet
set -g mouse on
set -g history-limit 50000
bind | split-window -h
bind - split-window -v
```

## Maintenance status

Actively maintained; latest release 3.6a (January 2026). ISC License. 45,066 stars, 2,598 forks. Mailing list: tmux-users@googlegroups.com. Contributing guide in CONTRIBUTING.md; suggestions listed at https://github.com/tmux/tmux/wiki/Contributing.

## Ecosystem

tmux's `capture-pane`, `send-keys`, and socket-based control mode are the integration points for higher-level tooling:
- [[njbrake-agent-of-empires]] — Rust session manager that wraps tmux to run multiple AI coding agents in parallel, each in an isolated session.
- [[tmuxai.dev]] — AI terminal assistant that observes all tmux panes and executes commands in a dedicated exec pane.
- [tmux Plugin Manager (TPM)](https://github.com/tmux-plugins/tpm) — community plugin ecosystem.
- [Oh My Tmux!](https://github.com/gpakosz/.tmux) — popular configuration framework.
- [Awesome Tmux](https://github.com/rothgar/awesome-tmux) — curated list of plugins, themes, and integrations.
