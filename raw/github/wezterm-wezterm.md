# wezterm/wezterm

## Metadata
- Stars: 27,461
- Primary language: Rust
- Default branch: main
- Latest release: 20240203-110809-5046fc22 (2024-02-03)
- License: Other (see LICENSE.md)
- Homepage: https://wezterm.org/
- Fetched: 2026-07-09
- Final URL: https://github.com/wezterm/wezterm

## Description
A GPU-accelerated cross-platform terminal emulator and multiplexer written by @wez and implemented in Rust

## README
# Wez's Terminal

A GPU-accelerated cross-platform terminal emulator and multiplexer written by @wez and implemented in Rust.

User facing docs and guide at: https://wezterm.org/

## Installation

https://wezterm.org/installation

## Getting help

Support channels:
- GitHub issue tracker: https://github.com/wezterm/wezterm/issues
- GitHub Discussions: https://github.com/wezterm/wezterm/discussions
- Matrix room via Element.io: https://matrix.to/#/#wezterm:matrix.org

## Supporting the Project

Sponsorship available via:
- GitHub Sponsors: https://github.com/sponsors/wez
- Patreon: https://patreon.com/WezFurlong
- Ko-Fi: https://ko-fi.com/wezfurlong
- Liberapay: https://liberapay.com/wez

## Top-level structure
- `wezterm/` — main GUI application crate
- `wezterm-gui/` — GUI rendering (OpenGL / Metal / Vulkan)
- `wezterm-mux-server/` — multiplexer server
- `wezterm-ssh/` — SSH client implementation
- `wezterm-client/` — multiplexer client
- `wezterm-font/` — font loading and shaping
- `term/` — terminal emulation core
- `termwiz/` — terminal widget library (also published as standalone crate)
- `mux/` — core multiplexer domain logic
- `config/` — configuration loading and validation
- `lua-api-crates/` — Lua bindings for the wezterm API
- `docs/` — MkDocs documentation source (matches wezterm.org)
- `assets/` — icons, color schemes
- `ci/` — CI scripts
