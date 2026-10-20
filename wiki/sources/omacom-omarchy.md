---
type: source
category: "Coding agents, IDEs & dev environments"
source_url: https://github.com/omacom/omarchy
tags:
  - agentic-linux
  - hyprland
  - quickshell
  - arch-linux
  - dhh
  - coding-agents
  - mise
  - opinionated-distro
related:
  - aaif-goose-goose
  - warp.dev
  - tmux-tmux
  - hermes-agent.nousresearch.com
product: omarchy
detail_level: standard
created: 2026-10-20
updated: 2026-10-20
---

Omarchy (~45k stars, MIT, v4.0.6 on branch `quattro`) is a beautiful, fun & agentic Linux distribution by DHH — an opinionated Arch-based desktop (Hyprland + Quickshell) that ships coding-agent tooling, Neovim, terminal/shell stacks, and first-class agent skill provisioning out of the box. Homepage: [omarchy.org](https://omarchy.org).

_All claims below are sourced from ../../raw/github/omacom-omarchy.md unless otherwise noted._

## What it does

Omarchy is a full Linux OS experience, not a single app: install from ISO (or dual-boot / unattended paths documented in `manual/`), get a themed Hyprland desktop with an Omarchy CLI (`omarchy …`), and work in a pre-wired developer environment. The repo builds two runtime Arch packages (`omarchy` + `omarchy-settings`) plus related packages in a separate `omarchy-pkgs` tree. User-facing docs live in `manual/` (welcome, navigation, themes, AI, Neovim, terminal, updates, security, dual boot, unattended installs). Contributor docs live in `docs/` and `agents/skills/`.

Agent-facing pieces baked into provision:
- mise wrappers for Claude, Codex, and Grok account dispatch (`omarchy-agent-accounts`)
- skill symlinks into Claude Code, Codex, Pi, Gemini/Antigravity, Hermes, and generic `~/.agents/skills/` pointing at shipped `default/agents/skills/` (currently `omarchy` and `diagnose-crash`)

## Installation

End-user install is via the distribution site and ISO flow described at [omarchy.org](https://omarchy.org) and in the manual (`manual/02-getting-started.md`, dual-boot and unattended chapters). The GitHub README itself points there rather than publishing a one-liner installer.

From source / development checkout:

```bash
git clone https://github.com/omacom/omarchy.git
cd omarchy
# default branch: quattro
```

On an installed system, packages land as `/usr/bin/omarchy-*` with settings seeded via `/etc/skel`. Deferred-provisioning images create the owner on first boot (`omarchy-provision-owner`); hardware deferred for prebuilt images runs through `omarchy-provision-hardware`. Existing users can destructive-resync configs with `omarchy-reinstall-configs`.

## Key features

- **Opinionated agentic desktop** — Hyprland session via uwsm, Quickshell UI (`shell/`), themes, hotkeys, clipboard/history, screenshots, dictation, reminders, and a large application set (terminal, Neovim, browsers, TUIs/GUIs, gaming, Windows VM helpers).
- **Omarchy CLI router** — `bin/omarchy` maps spaced commands onto flat `bin/omarchy-*` binaries (`omarchy theme set foo` → `omarchy-theme-set`); metadata headers control aliases, hidden install plumbing, and help.
- **Agent account + skill wiring** — mise `command-wrappers` for Claude/Codex/Grok; provision symlinks distro skills into multiple agent skill directories (including Hermes profiles when present).
- **ISO / image install orchestration** — `omarchy-apply-system` (config, hardware, login, post-install), Snapper/Limine boot story, platform detection (`x86`, `aarch64`, `aarch64-apple`, Qualcomm, N1x, GB10).
- **i18n** — 50 languages for menu, Quickshell, notifications, and manuals; language switch via Setup > Language / `omarchy language`.
- **Hardware polish** — PipeWire speaker tunings, fingerprint readers, display backlight/DDC hints via optional `/usr/share/omarchy-platform/` files.

## Architecture

Two packages from one repo (PKGBUILDs in `omarchy-pkgs`):

| Package | Role |
| --- | --- |
| `omarchy` | Runtime binaries (`bin/`), `install/`, migrations, themes, Quickshell `shell/` |
| `omarchy-settings` | Pre-useradd seeds: `/etc/skel`, `/etc` drop-ins, fonts, Plymouth/SDDM, Limine/Snapper |

Home population has three layers: **Seed** (`/etc/skel` at `useradd -m`), **Finalize** (`omarchy-provision-user` once per user), **Resync** (`omarchy-reinstall-configs`). Env bootstrap (`default/bash/env-bootstrap`) sets `OMARCHY_PATH` and mise/agent wrapper PATH for login shells and the uwsm Hyprland session. Platform packages may add files under `/usr/share/omarchy-platform/`. Migrations are timestamped scripts under `migrations/` run per-user via `omarchy-migrate`.

## Example usage

```bash
# Spaced CLI (routed to bin/omarchy-*)
omarchy theme set <name>
omarchy audio tuning status
omarchy language list
omarchy commands --all

# Speaker tuning (when hardware matches)
omarchy audio tuning on
omarchy audio tuning off

# Destructive config resync to shipped defaults
omarchy-reinstall-configs

# Dev checkout: link local tree (see docs/file-layout.md / AGENTS.md)
omarchy-dev-link   # writes /etc/omarchy.conf + sudoers secure_path
```

Manual chapters cover day-to-day use (navigation, top bar, AI, development tools). Contributor task guides live under `agents/skills/` (command metadata, install scripts, mise tools, shell-dev, migrations).

## Maintenance status

- **Stars:** 45,279 (fetched 2026-10-20)
- **Latest release:** v4.0.6
- **Default branch:** `quattro` (pushed 2026-10-20)
- **License:** MIT
- **Language:** Shell (primary); Quickshell/QML desktop, extensive bash tooling
- **Homepage:** https://omarchy.org
- Actively developed; ISO package lists and platform package sets live under `install/`
