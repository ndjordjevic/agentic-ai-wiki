# wezterm.org

## Fetch log
- Inbox URL: https://wezterm.org/index.html
- Final URL: https://wezterm.org/index.html
- Fetched: 2026-07-09
- Pages: 5
- Mode: standard

## Landing page — https://wezterm.org/index.html

# WezTerm

_WezTerm is a powerful cross-platform terminal emulator and multiplexer written by @wez and implemented in Rust_

GitHub repo: https://github.com/wezterm/wezterm

## Features

Navigation tree:
- Features: https://wezterm.org/features.html
- Scrollback: https://wezterm.org/scrollback.html
- Quick Select Mode: https://wezterm.org/quickselect.html
- Copy Mode: https://wezterm.org/copymode.html
- Hyperlinks: https://wezterm.org/hyperlinks.html
- Shell Integration: https://wezterm.org/shell-integration.html
- iTerm Image Protocol: https://wezterm.org/imgcat.html
- SSH: https://wezterm.org/ssh.html
- Serial Ports & Arduino: https://wezterm.org/serial.html
- Multiplexing: https://wezterm.org/multiplexing.html

Download:
- Windows: https://wezterm.org/install/windows.html
- macOS: https://wezterm.org/install/macos.html
- Linux: https://wezterm.org/install/linux.html
- FreeBSD: https://wezterm.org/install/freebsd.html
- NetBSD: https://wezterm.org/install/netbsd.html
- Build from source: https://wezterm.org/install/source.html

Configuration:
- Configuration files: https://wezterm.org/config/files.html
- Colors & Appearance: https://wezterm.org/config/appearance.html
- Fonts: https://wezterm.org/config/fonts.html
- Key Binding: https://wezterm.org/config/keys.html
- Key Tables: https://wezterm.org/config/key-tables.html
- Mouse Binding: https://wezterm.org/config/mouse.html
- Plugins: https://wezterm.org/config/plugins.html
- Color Schemes: https://wezterm.org/colorschemes/index.html
- Recipes: https://wezterm.org/recipes/index.html

Full Config & Lua Reference: https://wezterm.org/config/lua/general.html
CLI Reference: https://wezterm.org/cli/general.html
Change Log: https://wezterm.org/changelog.html

## Features page — https://wezterm.org/features.html

Key terminal features (from the features listing):

**Tabs:**
- Tabs (Hotkey: `Super-T`, next/prev: `Super-Shift-[` and `Super-Shift-]`, go-to: `Super-[1-9]`)
- Supports the Mouse and Kitty graphics protocol for rich terminal graphics
- Live configuration reloading (no restart needed)
- Extensive color scheme support (hundreds of built-in themes)

**Additional features visible from docs navigation:**
- Scrollback with configurable size
- Quick Select Mode: pattern-based text selection with keyboard
- Copy Mode: vim-like keyboard-driven text selection
- Clickable Hyperlinks with customizable matchers
- Shell Integration: OSC 7 (cwd), semantic zones, prompt marking
- iTerm Image Protocol: display images inline in the terminal
- SSH: built-in SSH client using libssh2
- Serial Ports & Arduino support
- Multiplexing: local tabs/windows + remote mux via SSH/Unix/TLS domains

## Installation — https://wezterm.org/installation.html

WezTerm is available pre-built for major platforms:
- Windows: installer and zip packages available
- macOS: .dmg for Apple Silicon and Intel
- Linux: AppImage, .deb/.rpm packages, and Homebrew
- FreeBSD and NetBSD packages
- Build from source with Rust toolchain

## Multiplexing — https://wezterm.org/multiplexing.html

The multiplexing subsystem allows wezterm to manage multiple windows and tabs across local and remote _domains_. When wezterm starts, it creates a default local domain; additional remote domains can be configured.

**SSH Domains** — connect to a remote wezterm mux daemon over SSH (requires wezterm on the remote host):

```lua
config.ssh_domains = {
  {
    name = 'my.server',
    remote_address = '192.168.1.1',
    username = 'wez',
  },
}
```

SSH domains auto-populate from `~/.ssh/config`. Connect with:

```sh
wezterm connect SSHMUX:my.server
# or spawn into a new tab in existing GUI:
wezterm cli spawn --domain-name SSHMUX:my.server
```

**Unix Domains** — connect via a unix socket (supported on all platforms including Windows via AF_UNIX):

```lua
config.unix_domains = {
  {
    name = 'unix',
  },
}
-- Connect automatically on startup:
config.default_gui_startup_args = { 'connect', 'unix' }
```

Unix domains support `proxy_command`, `local_echo_threshold_ms` for predictive local echo, and can bridge WSL 1 into the Windows native GUI.

**Workspaces** — named groups of tabs/panes; switch between them with `CTRL-SHIFT-$` (default) or via the Lua API.

## Configuration — https://wezterm.org/config/files.html

WezTerm is configured entirely in Lua via a `.wezterm.lua` file (located at `~/.wezterm.lua` or `~/.config/wezterm/wezterm.lua`). Configuration reloads live on save.

Quick start:

```lua
-- Pull in the wezterm API
local wezterm = require 'wezterm'
local config = wezterm.config_builder()

-- Customize:
config.font = wezterm.font 'JetBrains Mono'
config.font_size = 14.0
config.color_scheme = 'Batman'

return config
```

Key config areas:
- `config.font` / `config.font_size` — font selection via `wezterm.font()`
- `config.color_scheme` — choose from hundreds of built-in color schemes
- `config.keys` — custom key bindings (KeyAssignment table)
- `config.key_tables` — modal key tables
- `config.mouse_bindings` — mouse button customization
- `config.default_prog` — shell or program to launch
- `config.ssh_domains` / `config.unix_domains` — multiplexing
- `config.plugins` — loadable Lua plugins from git URLs

All options documented at https://wezterm.org/config/lua/config/index.html (100+ options).
