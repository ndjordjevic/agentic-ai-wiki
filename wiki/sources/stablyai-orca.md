---
type: source
category: "Coding agents, IDEs & dev environments"
source_url: https://github.com/stablyai/orca
tags:
  - agent-orchestrator
  - electron-ide
  - git-worktrees
  - parallel-agents
  - mobile-companion
  - design-mode
  - terminal-splits
  - coding-agents
related:
  - herdr.dev
  - vibekanban.com
  - warp.dev
  - factory.ai
  - herdrdev-herdr
product: orca
detail_level: standard
created: 2026-10-20
updated: 2026-10-20
---

Orca is an open-source AI orchestrator / agent development environment (ADE) for running fleets of coding agents — Codex, Claude Code, OpenCode, Pi, and any other terminal CLI agent — each in its own git worktree, tracked in one desktop app with terminal splits, an embedded Chromium design mode, native GitHub/Linear task flows, SSH remotes, and an iOS/Android mobile companion. With ~98.7k GitHub stars (MIT, TypeScript/Electron, latest release v1.4.232 as of October 2026), it is one of the largest open agent-IDE projects; product site and docs live at [onorca.dev](https://www.onorca.dev).

_All claims below are sourced from ../../raw/github/stablyai-orca.md unless otherwise noted._

## What it does

Orca is a desktop app (macOS, Windows, Linux) that turns parallel coding-agent work into a first-class workflow. You run agents on your existing subscriptions; Orca isolates each run in a worktree (or folder workspace), hosts Ghostty-class WebGL terminals with infinite splits, and keeps agent status, diffs, PRs, and notifications in one UI. A paired mobile companion monitors and steers agents away from the desk. Agents can also drive Orca via CLI (`orca worktree create`, `snapshot`, `click`, `fill`).

Supported agents include Claude Code, Codex, Grok, Cursor, GitHub Copilot, Muse, DeepSeek Harness, ZCode, OpenCode, Pi, oh-my-pi, Hermes Agent, Devin, Goose, Amp, and many more — any CLI that runs in a terminal.

## Installation

**Desktop** — download from [onorca.dev/download](https://onorca.dev/download), or grab platform builds from GitHub Releases (macOS arm64/x64 DMG, Windows setup exe, Linux AppImage).

```bash
# macOS (Homebrew)
brew install --cask stablyai/orca/orca

# Arch Linux (AUR)
yay -S stably-orca-bin
```

**Mobile companion** — iOS App Store (`orca-ide`) or Android APK from onorca.dev. Pair with the desktop host; the mobile↔desktop relay lives under `cloud/` in the same repo.

Local development follows `.github/CONTRIBUTING.md` (pnpm workspace, Electron).

## Key features

- **Parallel worktrees** — fan one prompt across multiple agents, each in an isolated git worktree; compare results and merge the winner.
- **Terminal splits** — WebGL terminals with infinite splits and scrollback that survives restarts.
- **Design mode** — click UI elements in an embedded Chromium window to send HTML, CSS, and a cropped screenshot into the agent prompt.
- **GitHub & Linear native** — browse PRs, issues, and boards in-app; open a worktree from a task and review without leaving Orca.
- **SSH worktrees** — run agents on a remote box with file editing, git, terminals, auto-reconnect, and port forwarding.
- **Annotate AI diffs** — comment on diff lines and ship feedback back to the agent; review, edit, and commit in-app.
- **Editor + drag-to-prompt** — VS Code-style editor with autosave; drag files or images into agent prompts.
- **Orca CLI / Computer Use** — script worktrees and UI actions; optionally let agents operate desktop apps.
- **Account switcher & usage tracking** — Claude/Codex usage and rate-limit resets; hot-swap accounts.
- **Notifications / unread state** — know when an agent finishes or needs attention.

## Architecture

Orca is an **Electron** desktop app (TypeScript, `electron.vite.config.ts`, pnpm workspaces) whose UI is intentionally quiet chrome around Monaco, xterm, and Markdown previews. Layout highlights from the repo:

- `src/` — main/renderer application code
- `native/` — native modules and helpers
- `mobile/` — mobile companion sources
- `cloud/` — separate pnpm workspace for the mobile↔desktop relay
- `skills/`, `skill-guides/`, `skill-stubs/` — agent skill packaging
- `docs/site/` — product docs published at onorca.dev

Operationally, the **execution host** owns agent status in one store (hook server); sidebar, `worktree ps`, mobile, and dashboard all subscribe. Workspaces may be git worktrees or plain folder workspaces. Remote/SSH peers update independently — wire changes must stay backward-compatible. Git baseline is treated as Git 2.25 across native, WSL, and SSH hosts.

## Example usage

Typical flow after install:

1. Download/open Orca and open a repo (or multi-repo parent folder).
2. Spawn agents (e.g. Claude Code + Codex) each in its own worktree from one prompt or from a GitHub/Linear task.
3. Split terminals, use Design Mode on a running local UI, annotate diffs, and merge the winning worktree.
4. Pair the mobile app to get notified when agents finish and send follow-ups remotely.
5. Script repeats with the CLI, e.g. `orca worktree create` and related commands documented at onorca.dev/docs/cli.

## Maintenance status

- **Stars:** 98,679 (fetched 2026-10-20)
- **Latest release:** v1.4.232
- **License:** MIT
- **Language:** TypeScript (Electron desktop; mobile companion; `cloud/` relay)
- **Activity:** actively developed — pushed 2026-10-20; daily ships called out in README/changelog
- **Homepage:** https://orca.dev (README/docs brand as [onorca.dev](https://www.onorca.dev))
- **Community:** Discord, X (@orca_build), WeChat groups; Windows signing via SignPath
