# kunchenguid/dotfiles

## Metadata
- Stars: 98
- Primary language: Nix
- Default branch: main
- Latest release: (none)
- License: MIT No Attribution
- Homepage: (none)
- Fetched: 2026-07-09
- Final URL: https://github.com/kunchenguid/dotfiles

## Description
Kun's dotfiles for agentic engineering

## README

# dotfiles

Watch the walkthrough: https://youtu.be/5N-okeDdIuI

My personal Mac setup, managed with nix-darwin and home-manager.
One repo, one command, and a fresh Mac ends up configured the same way every time.

## Contributing / Using This Repo

These are my personal dotfiles, shared publicly so people can read them, learn from them, and fork them freely.
Feature requests and pull requests are not accepted here, and PRs are auto-closed.
If you find a bug, please open a GitHub Issue using the bug report template.

## What you get

Running the switch builds:

- System settings (dark mode, key repeat, dock, Finder, trackpad)
- Homebrew apps (casks and CLI tools)
- Nix user packages (ripgrep, fd, fzf, jq, lazygit, Neovim, Hack Nerd Font)
- Shell (zsh, aliases, starship prompt)
- Editor (Neovim config with the rose-pine moon theme)
- Terminal (WezTerm config with the rose-pine moon theme)
- Agent configs (Claude, Codex, opencode all share one AGENTS.md)

## Prerequisites

- Apple Silicon Mac, by default.
- Intel Mac: change one line.
  In `configuration.nix`, set `nixpkgs.hostPlatform = "x86_64-darwin";`

## Fresh-machine setup

On a brand new Mac, from a bare clone of this repo:

```sh
git clone https://github.com/kunchenguid/dotfiles.git
cd dotfiles
```

Before you run it: review "Make it yours" below. `bootstrap.sh` applies the config to your machine.

```sh
./bootstrap.sh
```

`bootstrap.sh` does four things, in order:

1. Installs Determinate Nix, if it isn't already installed.
2. Symlinks this repo to `~/.dotfiles`.
3. Checks the `user` configured in `flake.nix` against your actual macOS username, and offers to fix it for you if they differ.
4. Runs the first `darwin-rebuild switch`.

After that, `darwin-rebuild` exists and you're on the normal workflow.

### Validate without applying

```sh
nix flake check --no-build
nix build .#darwinConfigurations.mac.system --dry-run
```

## Daily use

```sh
./rebuild.sh
```

## Make it yours

- **Username**: run `./bootstrap.sh` (detects your macOS username and offers to set it) OR change the single `user = "kunchen"` line in `flake.nix`.
- **Host label** `"mac"`, in three places: `flake.nix`, `rebuild.sh:5`, and `bootstrap.sh`'s first-switch command.
- **CPU architecture**, `hostPlatform` in `configuration.nix`.
- **Git identity:** not set declaratively — Git will prompt you on first commit.
- **Homebrew cleanup warning:** `cleanup = "zap"` removes any Homebrew package not listed in `configuration.nix`.

**Heads-up:**
- `home/AGENTS.md` is installed for Claude, Codex, and opencode — edit or delete if you don't want to inherit these agent instructions.
- The `cc` and `co` shell aliases are high-agency shortcuts: `claude --dangerously-skip-permissions` and `codex --full-auto`.

## Repo tour

- `flake.nix` — entry point; wires nixpkgs, nix-darwin, home-manager, nix-homebrew, declares the `mac` machine.
- `configuration.nix` — system-level config: macOS defaults, Homebrew.
- `home.nix` — user-level config: shell, packages, prompt, and symlinks.
- `rebuild.sh` — re-applies the config after the first switch.
- `home/` — the actual config files that get symlinked into place (Neovim, WezTerm, herdr, Claude settings, shared `AGENTS.md`).

## How the symlinks work

Files under `home/` are the real files. `home.nix` uses `mkOutOfStoreSymlink` to point paths like `~/.config/nvim` straight at `home/.config/nvim` in this repo. You only run `./rebuild.sh` when changing non-symlinked things like a package list or a system default.

## License

MIT No Attribution. See `LICENSE`.

## Docs

### AGENTS.md (root — project policy for agents)

```
# Project notes for agents

Deliberate decisions in this repo - do NOT silently revert them:

- `homebrew.onActivation.cleanup = "zap"` in `configuration.nix` is intentional.
  It forces the good habit of declaring every Homebrew package in the Nix config
  instead of installing things ad-hoc, which keeps the machine reproducible.
  Do not soften it to `uninstall` or `none`. Users are warned about its effect in
  README.md; this note is for anyone tempted to change the setting itself.
- Never commit `.no-mistakes/` validation evidence to this public repo.
  `.no-mistakes/` is gitignored; if a validation pipeline stages evidence into
  a branch, drop it before merging.
```

### home/AGENTS.md (shared global agent instructions)

```
# global agent instructions

- Never use the em dash "—". Use plain dash "-" instead
- When writing commit messages, NEVER auto-add your agent name as co-author
- Never manually modify CHANGELOG.md files or any files that are marked as auto-generated
- When making technical decisions, do not give much weight to development cost.
  Instead, prefer quality, simplicity, robustness, scalability, and long term maintainability.
- When doing bug fixes, always start with reproducing the bug in an E2E setting as closely
  aligned with how an end user would experience it as possible.
- When end-to-end testing a product, be picky about the UI you see and be obsessed with
  pixel perfection. If something clearly looks off, even if it is not directly related to
  what you are doing, try to get it fixed along the way.
- Apply that same high standard to engineering excellence: lint, test failures, and test
  flakiness. If you see one, even if it is not caused by what you are working on right now,
  still get it fixed.
```

### flake.nix

```nix
{
  description = "dotfiles";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-26.05-darwin";
    nix-darwin.url = "github:nix-darwin/nix-darwin/nix-darwin-26.05";
    nix-darwin.inputs.nixpkgs.follows = "nixpkgs";
    home-manager.url = "github:nix-community/home-manager/release-26.05";
    home-manager.inputs.nixpkgs.follows = "nixpkgs";
    nix-homebrew.url = "github:zhaofengli/nix-homebrew";
  };

  outputs = inputs@{ self, nix-darwin, nix-homebrew, home-manager, nixpkgs }:
    let
      user = "kunchen";  # the one username line to change
    in
    {
      darwinConfigurations."mac" = nix-darwin.lib.darwinSystem {
        specialArgs = { inherit user; };
        modules = [
          ./configuration.nix
          nix-homebrew.darwinModules.nix-homebrew
          home-manager.darwinModules.home-manager
          {
            home-manager.useGlobalPkgs = true;
            home-manager.useUserPackages = true;
            home-manager.extraSpecialArgs = { inherit user; };
            home-manager.users.${user} = import ./home.nix;
          }
        ];
      };
    };
}
```

### configuration.nix

```nix
{ user, ... }:
{
  nix.enable = false;   # Determinate manages the Nix daemon
  nixpkgs.config.allowUnfree = true;
  nixpkgs.hostPlatform = "aarch64-darwin";  # use x86_64-darwin for Intel
  system.primaryUser = user;
  users.users.${user} = { home = "/Users/${user}"; };
  system.stateVersion = 6;
  system.defaults = {
    NSGlobalDomain = {
      AppleInterfaceStyle = "Dark";
      KeyRepeat = 2;
      InitialKeyRepeat = 15;
      _HIHideMenuBar = true;
      AppleShowAllExtensions = true;
    };
    dock.autohide = true;
    finder.FXPreferredViewStyle = "Nlsv";
    finder.CreateDesktop = false;
    trackpad.Clicking = true;
  };
  nix-homebrew = { enable = true; inherit user; };
  homebrew = {
    enable = true;
    onActivation.cleanup = "zap";  # remove anything not listed here
    onActivation.autoUpdate = true;
    onActivation.extraFlags = [ "--force" ];
    brews = [ "herdr" ];
    casks = [ "wezterm" "claude-code" ];
  };
}
```

### home.nix (key sections)

```nix
{ config, pkgs, user, ... }:
let
  dotfiles = "${config.home.homeDirectory}/.dotfiles";
in
{
  home.username = user;
  home.homeDirectory = "/Users/${user}";
  home.stateVersion = "24.11";
  home.packages = with pkgs; [
    ripgrep fd fzf jq lazygit neovim nerd-fonts.hack
  ];
  home.sessionVariables.EDITOR = "nvim";
  programs.zsh = {
    enable = true;
    autosuggestion.enable = true;
    syntaxHighlighting.enable = true;
    shellAliases = {
      ".." = "cd .."; add = "git add ."; push = "git push"; pull = "git pull";
      m = "git switch main";
      cc = "claude --dangerously-skip-permissions";
      co = "codex --full-auto";
    };
  };
  programs.starship.enable = true;
  # Edit-in-place symlinks — editing here edits the live config
  home.file.".config/wezterm".source =
    config.lib.file.mkOutOfStoreSymlink "${dotfiles}/home/.config/wezterm";
  home.file.".config/nvim".source =
    config.lib.file.mkOutOfStoreSymlink "${dotfiles}/home/.config/nvim";
  home.file.".claude/CLAUDE.md".source =
    config.lib.file.mkOutOfStoreSymlink "${dotfiles}/home/AGENTS.md";
  home.file.".codex/AGENTS.md".source =
    config.lib.file.mkOutOfStoreSymlink "${dotfiles}/home/AGENTS.md";
  home.file.".config/opencode/AGENTS.md".source =
    config.lib.file.mkOutOfStoreSymlink "${dotfiles}/home/AGENTS.md";
}
```

## Top-level structure

```
.github/           - GitHub Actions / issue templates
.gitignore
AGENTS.md          - agent policy for this repo (guards cleanup=zap, no .no-mistakes/ commits)
CONTRIBUTING.md    - contribution policy (PRs auto-closed; bug reports via Issues only)
LICENSE            - MIT No Attribution
README.md          - full setup guide
bootstrap.sh       - one-shot fresh-machine bootstrap (installs Nix, symlinks repo, runs first switch)
configuration.nix  - system-level Nix: macOS defaults, Homebrew casks/brews
flake.lock         - pinned inputs
flake.nix          - entry point: inputs, darwinConfigurations."mac"
home.nix           - user-level Nix: packages, shell, starship, symlinks
home/              - actual config files symlinked into ~/.config etc.
  .claude/         - Claude settings.json
  .config/
    wezterm/       - WezTerm config (rose-pine moon theme)
    nvim/          - Neovim config (lazy.nvim, rose-pine moon, transparent bg)
    herdr/         - herdr config
  AGENTS.md        - shared agent instructions (symlinked to Claude, Codex, opencode)
rebuild.sh         - daily driver: re-runs darwin-rebuild switch
```
