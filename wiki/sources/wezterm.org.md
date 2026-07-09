---
type: source
source_url: https://wezterm.org/index.html
companion_urls:
  - https://github.com/wezterm/wezterm
raw_files:
  - ../../raw/web/wezterm.org.md
  - ../../raw/github/wezterm-wezterm.md
tags: [terminal-emulator, multiplexer, gpu-accelerated, lua-config, rust, cross-platform, ssh, wezterm]
related: [tmux-tmux, tmuxai.dev, kunchenguid-dotfiles]
product: wezterm
detail_level: standard
created: 2026-07-09
updated: 2026-07-09
---

WezTerm is a GPU-accelerated, cross-platform terminal emulator and multiplexer written in Rust by Wez Furlong. It combines the rendering power of a GPU-native terminal (Metal, Vulkan, OpenGL) with built-in multiplexing, a full SSH client, and a Lua-based configuration system. With 27,000+ GitHub stars, WezTerm is one of the most feature-rich terminal emulators available, notable for its strong cross-platform story (macOS, Windows, Linux, FreeBSD, NetBSD) and its ability to multiplex sessions both locally and across remote machines over SSH or Unix domains.

_All claims below are sourced from ../../raw/web/wezterm.org.md unless otherwise noted._

## What it does

WezTerm serves as both a terminal emulator and a terminal multiplexer in a single binary. It renders terminal output using the GPU for smooth, high-DPI display; manages tabs and panes locally; and can connect to remote multiplexer daemons over SSH or Unix sockets. Configuration is done entirely in Lua, enabling powerful programmatic customization without any separate config DSL.

## Key features

- **GPU-accelerated rendering**: uses Metal (macOS), Vulkan, or OpenGL for GPU compositing — smooth even at high DPI, with configurable animation.
- **Lua configuration**: all settings, key bindings, and event handlers are defined in a Lua script that live-reloads on save. No restart needed. (../../raw/github/wezterm-wezterm.md)
- **Tabs and panes**: native tab bar with keyboard shortcuts (`Super-T` new, `Super-Shift-[/]` prev/next, `Super-1..9` go-to).
- **Built-in multiplexing**: local tabs + remote SSH/Unix/TLS multiplexer domains — attach native GUI windows to remote sessions.
- **SSH client**: built-in libssh2-based SSH; connects directly to remote hosts without needing a local SSH binary. Reads `~/.ssh/config` automatically. (../../raw/github/wezterm-wezterm.md)
- **Scrollback and Quick Select**: configurable scrollback buffer; Quick Select Mode for keyboard-driven regex-based text capture; Copy Mode (vim-style navigation).
- **Shell Integration**: OSC 7 (cwd tracking), semantic prompt zones, marks in scrollback for prompt navigation.
- **Image display**: iTerm Image Protocol support for inline image rendering.
- **Hyperlinks**: clickable URLs and user-defined regex-matched hyperlinks.
- **Extensive color schemes**: hundreds of built-in color schemes; fully customizable.
- **Plugin system**: Lua plugins loaded from git URLs; `config.plugins`.
- **Serial port & Arduino support**.
- **Key Tables**: modal key binding modes (like Vim leader keys).

## Architecture

WezTerm is a Rust workspace with many crates. Key subsystems: (../../raw/github/wezterm-wezterm.md)

- **`wezterm-gui`** — GPU rendering layer (Metal/Vulkan/OpenGL via WebGPU-style abstraction)
- **`term` / `termwiz`** — terminal emulation core and terminal widget library (published separately on crates.io)
- **`mux`** — multiplexer domain abstraction: local domain, SSH domain, Unix domain, TLS domain
- **`wezterm-ssh`** — async libssh2 SSH client
- **`wezterm-font`** — font discovery, loading, and HarfBuzz text shaping
- **`lua-api-crates`** — Lua bindings exposing the wezterm API (events, windows, panes, config)
- **`config`** — Lua config loading, validation, and live-reload watcher
- **`wezterm-mux-server`** — daemon mode for remote multiplexing

The multiplexer uses a domain concept: each domain is an independent set of windows/tabs. The GUI attaches to any domain transparently, so a local window can host a mix of local panes and panes from a remote SSH session.

## Installation

Available as pre-built binaries for all major platforms:

- **macOS**: `.dmg` (Apple Silicon + Intel) or Homebrew
- **Windows**: `.exe` installer or zip
- **Linux**: AppImage, `.deb`, `.rpm`, Flatpak, Homebrew
- **FreeBSD / NetBSD**: packages
- **Build from source**: standard `cargo build --release` with Rust toolchain

Download page: https://wezterm.org/installation.html

## Example usage

**Quick start config** (`~/.wezterm.lua`):

```lua
local wezterm = require 'wezterm'
local config = wezterm.config_builder()

config.font = wezterm.font 'JetBrains Mono'
config.font_size = 14.0
config.color_scheme = 'Batman'
config.hide_tab_bar_if_only_one_tab = true

return config
```

**Remote multiplexing via SSH** (add to `.wezterm.lua`):

```lua
config.ssh_domains = {
  { name = 'my.server', remote_address = '192.168.1.1', username = 'wez' },
}
```

Then connect with: `wezterm connect SSHMUX:my.server`

**Unix domain mux** (for persistent local sessions):

```lua
config.unix_domains = { { name = 'unix' } }
config.default_gui_startup_args = { 'connect', 'unix' }
```

## When to use

WezTerm is a strong choice when you want:

- A single GPU-accelerated terminal that also handles multiplexing (no separate tmux/screen needed, though they remain compatible).
- Lua-programmable configuration — event-driven customization, dynamic tab bar, per-domain key tables.
- Native SSH multiplexing to remote hosts with GUI-quality rendering, without keeping a tmux session.
- Cross-platform consistency: same binary and config works on macOS, Windows, and Linux.
- Rich font and ligature support with HarfBuzz shaping and the Kitty/iTerm2 graphics protocols.

For users who prefer a standalone multiplexer (e.g. in headless/SSH-only workflows), [[tmux-tmux]] remains the standard; [[tmuxai.dev]] wraps tmux with AI assistance.

## Maintenance status

Active community project. 27,461 GitHub stars, 1,556 forks. Latest release: `20240203-110809-5046fc22` (Feb 2024). Ongoing development on `main` branch. Sponsorship via GitHub Sponsors, Patreon, Ko-Fi, and Liberapay. (../../raw/github/wezterm-wezterm.md)

## Ecosystem

- **termwiz** — WezTerm's terminal widget library, available as a standalone crate for building TUI apps.
- **Color schemes** — 500+ built-in color schemes at https://wezterm.org/colorschemes/index.html
- **Lua plugins** — community plugins loaded via `config.plugins` from git repos.
- **Shell integration scripts** — available for bash, zsh, fish, and nushell.
- Related terminal multiplexers: [[tmux-tmux]] (the classic CLI multiplexer); [[tmuxai.dev]] (AI-enhanced tmux wrapper).
