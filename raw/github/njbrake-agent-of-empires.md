# njbrake/agent-of-empires

## Metadata
- Stars: 1868
- Forks: 153
- Primary language: Rust
- Default branch: main
- Latest release: v1.5.0 (2026-04-30)
- License: MIT
- Homepage: http://www.agent-of-empires.com/
- Fetched: 2026-05-02
- Final URL: https://github.com/njbrake/agent-of-empires

## Description

Manage multiple Claude Code, OpenCode agents from either TUI or Web for easy access on mobile. Also supports Mistral Vibe, Codex CLI, Gemini CLI, Pi.dev, Copilot CLI, Factory Droid Coding. Uses tmux and git worktrees.

## README

<p align="center">
  <img src="assets/logo.png" alt="Agent of Empires" width="128">
  <h1 align="center">Agent of Empires (AoE)</h1>
</p>

A session manager for AI coding agents on Linux and macOS. Use it from the terminal (TUI) or from any browser (web dashboard).

Run multiple AI agents in parallel across different branches of your codebase, each in its own isolated session with optional Docker sandboxing. Access your agents from your laptop, phone, or tablet.

## Why AoE?

Running one AI agent is easy. Running five of them across different branches, keeping track of which is stuck, which is waiting on input, and which just made a mess of your working tree, becomes a part-time job. AoE makes it a glance: one dashboard, one status column, git worktrees and Docker sandboxes set up for you, and sessions that outlive your terminal.

## Features

- **Multi-agent support**: Claude Code, OpenCode, Mistral Vibe, Codex CLI, Gemini CLI, Cursor CLI, Copilot CLI, Pi.dev, Factory Droid, and Hermes
- **TUI app**: visual interface to create, monitor, and manage sessions
- **Web app** (Beta): create, monitor, and control your agents from any browser, installable as a PWA
- **CLI app**: create, monitor, and control agents from the command line (integrates with tools like OpenClaw)
- **Remote access from your phone**: press `R` in the TUI to expose the web dashboard over HTTPS with QR + passphrase auth. Uses Tailscale Funnel when available or Cloudflare Tunnel as a fallback
- **Status detection**: see which agents are running, waiting for input, or idle
- **Git worktrees**: run parallel agents on different branches of the same repo
- **Docker sandboxing**: isolate agents in containers with shared auth volumes
- **Diff view**: review git changes and edit files without leaving the TUI
- **Profiles**: separate workspaces for different projects or clients

## Web Dashboard (Beta)

Access your agents from any browser. The real agent terminal renders in the page; switch sessions, type into the terminal, and review diffs without leaving the tab. Press `R` in the TUI to start the server. Stack: React 19, TypeScript, Vite, Tailwind v4, xterm.js v6. Installable as a PWA.

## How It Works

Each agent runs in its own tmux session, so your agents keep running when you close the TUI, disconnect SSH, or your terminal crashes. Reopen `aoe` and everything is exactly where you left it.

## Installation

**Prerequisites:** tmux (required), Docker (optional, for sandboxing)

```bash
# Quick install (Linux & macOS)
curl -fsSL \
  https://raw.githubusercontent.com/njbrake/agent-of-empires/main/scripts/install.sh \
  | bash

# Homebrew
brew install aoe

# Nix
nix run github:njbrake/agent-of-empires

# Build from source
git clone https://github.com/njbrake/agent-of-empires
cd agent-of-empires && cargo build --release
```

## Quick Start

```bash
aoe                          # Launch the TUI
aoe add --cmd claude         # Create a session running Claude Code
aoe serve                    # Start the web dashboard
```

In the TUI, press `?` for help.

## Documentation links

- Installation: https://www.agent-of-empires.com/docs/installation/
- Quick Start: https://www.agent-of-empires.com/docs/quick-start/
- Remote Phone Access: https://www.agent-of-empires.com/guides/remote-phone-access/
- Git Worktrees: https://www.agent-of-empires.com/guides/worktrees/
- Docker Sandbox: https://www.agent-of-empires.com/guides/sandbox/
- Repo Config & Hooks: https://www.agent-of-empires.com/guides/repo-config/
- Diff View: https://www.agent-of-empires.com/guides/diff-view/
- Configuration Reference: https://www.agent-of-empires.com/docs/guides/configuration/
- CLI Reference: https://www.agent-of-empires.com/docs/cli/reference/

## FAQ

**What happens when I close aoe?** Nothing. Sessions are tmux sessions running in the background. Sessions only get removed when you explicitly delete them.

**Which AI tools are supported?** Claude Code, OpenCode, Mistral Vibe, Codex CLI, Gemini CLI, Cursor CLI, Copilot CLI, Pi.dev, Factory Droid, and Hermes. AoE auto-detects which are installed on your system.

**Can I use AoE over SSH?** Yes. Sessions persist across disconnects. See mobile SSH clients section for one extra step needed on mobile.

**Does it work on Windows?** Only through WSL2. AoE depends on tmux and POSIX process handling.

**How is this different from just using tmux directly?** tmux gives you persistent sessions. AoE adds agent-aware status detection, git worktree management, Docker sandboxing, a web dashboard, remote phone access, and a diff viewer.

## Development

```bash
cargo check          # Type-check
cargo test           # Run tests
cargo fmt            # Format
cargo clippy         # Lint
cargo build --release  # Release build

# Debug logging
AGENT_OF_EMPIRES_DEBUG=1 cargo run
```

## Acknowledgments

Inspired by agent-deck (Go + Bubble Tea). Created by Nate Brake (@natebrake), Machine Learning Engineer at Mozilla.ai.

## Docs

### AGENTS.md (repository guidelines)

## Project Structure & Module Organization

- `src/main.rs`: binary entrypoint (`aoe`).
- `src/lib.rs`: shared library code used by the CLI/TUI.
- `src/cli/`: clap command handlers (e.g., `src/cli/add.rs`, `src/cli/session.rs`).
- `src/tui/`: ratatui UI and input handling.
- `src/session/`: session storage, configuration, and group management.
- `src/tmux/`: tmux integration and status detection.
- `src/process/`: OS-specific process handling (`macos.rs`, `linux.rs`).
- `src/docker/`: Docker sandboxing and container management.
- `src/git/`: git worktree operations and template resolution.
- `src/server/`: web dashboard backend (axum server, REST API, WebSocket PTY relay, auth).
- `src/update/`: version checking against GitHub releases.
- `web/`: React + TypeScript frontend for the web dashboard (built with Vite + Tailwind CSS).
- `src/migrations/`: versioned data migrations for breaking changes.
- `tests/`: integration tests (`tests/*.rs`).
- `tests/e2e/`: end-to-end tests exercising the full `aoe` binary.
- `docs/`: user-facing documentation and guides.
- `scripts/`: installation and utility scripts.
- `xtask/`: build automation workspace.
- `contrib/`: community-maintained integration files (e.g., OpenClaw skill).

## Build, Test, and Development Commands

- `cargo build` / `cargo build --release`: TUI-only (release binary at `target/release/aoe`).
- `cargo build --features serve`: includes the web dashboard (needs Node.js + npm).
- `cargo test`: unit + integration tests (some skip if `tmux` unavailable).
- Debug logging: `AGENT_OF_EMPIRES_DEBUG=1 cargo run` (writes `debug.log` in app data dir).

### Web Dashboard

Stack: React 19, TypeScript, Vite, Tailwind v4, xterm.js v6. Installable as a PWA.
- Build: `cargo build --features serve`
- Run: `aoe serve --host 0.0.0.0` (token-based auth by default)
- Frontend dev: `cd web && npm run dev`

### Local Data Locations

- **Linux**: `$XDG_CONFIG_HOME/agent-of-empires/` (defaults to `~/.config/agent-of-empires/`)
- **macOS/Windows**: `~/.agent-of-empires/`

### Data Migrations

Breaking changes go through `src/migrations/`. A `.schema_version` file tracks state; `migrations::run_migrations()` runs pending ones on startup.

### Cargo.toml (version 1.5.0)

```toml
[package]
name = "agent-of-empires"
version = "1.5.0"
edition = "2021"
rust-version = "1.85"
description = "Terminal session manager for AI coding agents"
license = "MIT"
repository = "https://github.com/njbrake/agent-of-empires"
keywords = ["tmux", "tui", "ai", "claude", "terminal"]
categories = ["command-line-utilities", "development-tools"]

[dependencies]
clap = { version = "4.6", features = ["derive", "env"] }
ratatui = { version = "0.30", features = ["crossterm"] }
crossterm = { version = "0.29", features = ["event-stream"] }
tokio = { version = "1.50", features = ["full"] }
serde = { version = "1.0", features = ["derive"] }
serde_json = "1.0"
notify = "8.2"
```

## Top-level structure

```
.cargo/              — Cargo configuration
.claude/             — Claude Code agent config
.github/             — CI workflows, PR template
AGENTS.md            — Repository guidelines for AI agents (CLAUDE.md is a symlink to this)
CLAUDE.md            — Symlink to AGENTS.md
CODE_OF_CONDUCT.md   — Contributor code of conduct
CONTRIBUTING.md      — Contribution guide
Cargo.lock           — Locked dependency versions
Cargo.toml           — Workspace + package manifest (v1.5.0)
DESIGN.md            — Design system (TUI theme, web dashboard, typography, colors)
LICENSE              — MIT License
README.md            — Main documentation
assets/              — Logo and demo GIFs
build.rs             — Build script (web dashboard bundling)
bundled_sounds/      — Bundled audio files for agent status notifications
contrib/             — Community integrations (OpenClaw skill)
deny.toml            — cargo-deny license/advisory policy
docker/              — Docker sandboxing configs and Dockerfiles
docs/                — User-facing documentation (api.md, installation.md, quick-start.md,
                       development.md, sounds.md, push-notifications.md, guides/, cli/)
scripts/             — Install scripts (install.sh)
src/                 — Rust source (cli/, tui/, session/, tmux/, process/, docker/, git/,
                       server/, update/, migrations/)
web/                 — React + TypeScript web dashboard frontend
website/             — Astro static site (agent-of-empires.com)
xtask/               — Build automation workspace
```
