---
type: source
category: "Browser & web automation"
source_url: https://github.com/zenbu-labs/terminal-browser
tags: [kitty-graphics-protocol, electron-offscreen-rendering, terminal-embedded-browser, agent-browser-cli, claude-code-plugin, ssh-proxy, rust-graphics-engine, chromium-embed]
related: [vercel-labs-agent-browser, herdr.dev, Tencent-BrowserSkill]
product: terminal-browser
detail_level: standard
created: 2026-09-19
updated: 2026-09-19
---

terminal-browser (zenbu-labs, 3.1k+ stars, MIT) is a real Chromium-based browser that renders inside the terminal itself, using the kitty graphics protocol to display live pixels rather than a text/DOM approximation. It matters to this wiki as a way to give a terminal-bound coding agent direct, visual access to the web in the same tab or pane the agent is already running in — the agent can drive open terminal-browsers through a CLI (`terminal-browser action`) that is explicitly compatible with the [[vercel-labs-agent-browser]] interface, letting an agent open plans rendered as HTML, preview locally-running sites over SSH, or hand a human a live browser window to interact with mid-task.

_All claims below are sourced from ../../raw/github/zenbu-labs-terminal-browser.md unless otherwise noted._

## What it does
Launches a full Chromium browser rendered as pixels inside a compatible terminal (kitty graphics protocol support required — ghostty, kitty, and libghostty-based terminals like cmux and supacode). `terminal-browser open <url>` opens a page, `--split right` opens it in a split pane next to a coding agent, `ls` lists open browser instances, and `action` exposes an agent-browser-compatible CLI so an agent can programmatically inspect and control any open terminal-browser. A dedicated Claude Code plugin adds a `/browser` slash command and a plugin-facing API (`browser.open` / `browser.close`) that other Claude Code plugins can call to open URLs in a split pane.

## Installation
Install via `curl -fsSL https://terminal-browser.sh/install | bash` or `brew install terminal-browser`; `terminal-browser upgrade` updates in place. The Claude Code plugin is installed separately through `claude plugin marketplace add zenbu-labs/terminal-browser` then `claude plugin install terminal-browser@terminal-browser`, and requires enabling Claude Code's experimental function-hooks API (`CLAUDE_CODE_ENABLE_FUNCTION_HOOKS`) plus a terminal with kitty-graphics support — it does not work through most multiplexers, and performance inside `herdr` (see [[herdr.dev]]) is currently poor.

## Key features
- Full trackpad-quality scrolling and input: terminal-browser reads mouse/keyboard events from the terminal for what it can, and falls back to a background macOS Swift helper app for events the terminal can't surface, enabling smooth scrolling and infinite-canvas websites.
- SSH mode (`terminal-browser open --ssh <user@host> <url>`): renders locally but proxies all network requests through the remote host over SSH, so a website running on a remote machine's `localhost` can be previewed on the local device without shipping every frame over the network.
- Embedded mode for building terminal-browser into other TUIs (see `examples/embedded`).
- An agent-tool option in the Claude Code plugin (`agentTool`, off by default) that gives Claude a direct tool for opening the browser, as an alternative to shelling out to the `terminal-browser` CLI.
- An Agent Skill definition (`skill/terminal-browser/`, `SKILL.template.md` + `overlays/`) for driving terminal-browser from agent harnesses beyond Claude Code.

## Architecture
The outer browser UI is a graphics engine written in Rust; the UI itself is authored in React via a custom React renderer, and both the outer UI and the embedded Chromium content are composited onto one shared canvas inside the Rust engine, which is what lets terminal-browser layer its own UI chrome on top of live browser pixels. Chromium pixels are captured via Electron's offscreen-rendering API, read directly off the GPU, and pushed into the terminal using the kitty graphics protocol's unicode-placeholder mechanism — the same low-level approach the Claude Code plugin uses to draw into Claude Code's own TTY via its experimental function-hooks API. This entire pixel-streaming layer has been extracted into a standalone library, [pixel](https://github.com/zenbu-labs/pixel), for building other terminal-native graphical applications.

## Example usage
```
terminal-browser                              # launches the browser
terminal-browser open <url>                   # opens the browser at a url
terminal-browser --split right                # opens the browser in a split pane
terminal-browser open --ssh <user@host> <url> # proxies requests through a remote host
terminal-browser ls                           # lists open browsers
terminal-browser action                       # agent-browser-compatible CLI for scripted control
```
Inside Claude Code, once the plugin is installed, `/browser` opens the browser directly in a split pane next to the agent.

## Maintenance status
3.1k+ GitHub stars, 145 forks, MIT license, actively released (latest tag `v0.11.1`, pushed 2026-09-17). The maintainers explicitly require PR descriptions to be human-authored and well-motivated, and ask that PRs stay minimal. Public roadmap: Linux support (done), Chrome extensions, and a "design mode." Contributing itself is agent-assisted: the README recommends using a coding agent to set up a local dev environment.

## Ecosystem
Companion pieces in the same repo: a `herdr-plugin/` for the [[herdr.dev]] terminal multiplexer, and a Claude Code plugin exposing both a `/browser` command and a programmatic `browser.open`/`browser.close` API for other plugins to build on (example: a hypothetical `/tldraw` or `/open-pr` command that opens a page in the same split). The `terminal-browser action` CLI's agent-browser compatibility connects it to the broader agent-driven-browser-automation space alongside [[vercel-labs-agent-browser]] and [[Tencent-BrowserSkill]], though terminal-browser's own angle is rendering a real browser's pixels directly inside the terminal rather than exposing an accessibility-tree or CDP-based automation surface.
