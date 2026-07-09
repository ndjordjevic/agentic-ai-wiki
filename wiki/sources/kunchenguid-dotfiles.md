---
type: source
source_url: https://github.com/kunchenguid/dotfiles
tags: [nix-darwin, home-manager, dotfiles, nix-flakes, agentic-engineering, macos-setup, agents-md]
related: [determinate.systems, wezterm.org, herdr.dev]
product: dotfiles
detail_level: standard
created: 2026-07-09
updated: 2026-07-09
---

`kunchenguid/dotfiles` is a complete, reproducible macOS developer environment managed with nix-darwin, home-manager, and nix-homebrew — designed specifically for agentic engineering workflows. A single `./bootstrap.sh` command brings a fresh Apple Silicon Mac to a fully configured state: macOS system preferences, Homebrew casks, Nix user packages, zsh shell with aliases, Neovim with Lua config, WezTerm, and — notably — a shared `AGENTS.md` symlinked into Claude, Codex, and opencode simultaneously. The repo is a readable, forkable reference implementation of the "one repo, one command" dotfiles pattern using Nix flakes.

_All claims below are sourced from ../../raw/github/kunchenguid-dotfiles.md unless otherwise noted._

## What it does

The repo manages the entire Mac environment declaratively. Running `./bootstrap.sh` on a fresh machine installs Determinate Nix, symlinks the repo to `~/.dotfiles`, verifies the username in `flake.nix`, and runs the first `darwin-rebuild switch`. After that, daily changes are applied with `./rebuild.sh`. The config covers:

- macOS system defaults (dark mode, key repeat, auto-hide dock and menu bar, Finder list view, tap-to-click)
- Homebrew casks (`wezterm`, `claude-code`) and brews (`herdr`) managed declaratively with `cleanup = "zap"` — any unlisted package is removed on every switch
- Nix user packages: `ripgrep`, `fd`, `fzf`, `jq`, `lazygit`, `neovim`, `nerd-fonts.hack`
- zsh with autosuggestion, syntax highlighting, and starship prompt
- Shell aliases including `cc = "claude --dangerously-skip-permissions"` and `co = "codex --full-auto"`

## Key features

- **Single-command bootstrap**: `./bootstrap.sh` handles everything on a fresh machine — Nix install, repo symlink, username check, and first switch.
- **Unified agent instructions**: `home/AGENTS.md` is symlinked to `~/.claude/CLAUDE.md`, `~/.codex/AGENTS.md`, and `~/.config/opencode/AGENTS.md` — one file governs all three agents.
- **Edit-in-place symlinks**: `home.nix` uses `mkOutOfStoreSymlink` so editing config files in the repo (Neovim, WezTerm, herdr, Claude settings) immediately updates the live config without a rebuild.
- **`cleanup = "zap"`**: `homebrew.onActivation.cleanup` is set to `"zap"` intentionally, enforcing declarative Homebrew management. The `AGENTS.md` at the repo root explicitly instructs agents never to soften this setting.
- **Nix flake pinning**: `flake.lock` pins nixpkgs 26.05, nix-darwin 26.05, home-manager 26.05, and nix-homebrew for fully reproducible builds.
- **Intel Mac support**: one line change in `configuration.nix` (`nixpkgs.hostPlatform = "x86_64-darwin"`) switches from Apple Silicon to Intel.

## Architecture

The flake wires four inputs: `nixpkgs`, `nix-darwin`, `home-manager`, and `nix-homebrew`. The single `darwinConfigurations."mac"` system pulls in three modules: `configuration.nix` (system-level, macOS defaults + Homebrew), the `nix-homebrew` module, and `home-manager` (which imports `home.nix` for user-level config). A single `user` variable in `flake.nix` threads through all modules so renaming just that one variable adapts everything.

The `home/` directory holds the actual config files. `home.nix` uses `mkOutOfStoreSymlink` to point `~/.config/nvim`, `~/.config/wezterm`, `~/.config/herdr`, and `~/.claude/settings.json` directly at `home/<path>` in the cloned repo — so editing in the repo is editing the live config. Only package lists and system defaults require a rebuild.

## Installation

```sh
git clone https://github.com/kunchenguid/dotfiles.git
cd dotfiles
./bootstrap.sh
```

Customise before running: update `user = "kunchen"` in `flake.nix`, the three `"mac"` host label occurrences (in `flake.nix`, `rebuild.sh`, and `bootstrap.sh`), and review `brews`/`casks` in `configuration.nix` before the first switch to avoid unexpected Homebrew cleanup.

## Example usage

Daily workflow after initial bootstrap:

```sh
# edit any config file in the repo (e.g. home/.config/nvim/init.lua) — live immediately
# when changing packages, brews, or system defaults:
./rebuild.sh
```

Validate without applying:

```sh
nix flake check --no-build
nix build .#darwinConfigurations.mac.system --dry-run
```

## Maintenance status

- 98 stars, 46 forks
- License: MIT No Attribution
- No releases — main branch is the stable artifact; changes push directly to `main`
- Last commit: 2026-07-08
- Contributions not accepted (PRs auto-closed); bugs via GitHub Issues only

## Ecosystem

The dotfiles install and configure WezTerm (`casks = ["wezterm"]`; `home/.config/wezterm` symlinked) and depend on Determinate Nix for the installer. Claude Code is installed as a Homebrew cask (`"claude-code"`). The `home/AGENTS.md` shared instruction file connects this repo to all three agentic coding tools (Claude, Codex, opencode) simultaneously — see [[determinate.systems]] for the Nix installer and [[wezterm.org]] for WezTerm terminal documentation.
