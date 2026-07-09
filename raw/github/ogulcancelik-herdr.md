# ogulcancelik/herdr

## Metadata
- Stars: 14,553
- Primary language: Rust
- Default branch: master
- Latest release: v0.7.3 (2026-07-07)
- License: AGPL-3.0 (dual-licensed; commercial licenses available)
- Homepage: https://herdr.dev
- Fetched: 2026-07-09
- Final URL: https://github.com/ogulcancelik/herdr

## Description
agent multiplexer that lives in your terminal.

## README

# herdr

**agent multiplexer that lives in your terminal.**

- **every agent at a glance** — blocked, working, done. real terminal views, not a wrapped interpretation.
- **detach, agents keep running** — reattach from any terminal, or over ssh. sessions survive restarts.
- **agents can use herdr too** — a pure socket api: agents spawn panes, read output, wait on each other.
- **keyboard and mouse, both first-class** — tmux-style prefix keys *and* click, drag, split.
- **plugins** — extend panes and workflows.
- **one rust binary, no electron** — runs in whatever terminal you already use.

## install

```bash
curl -fsSL https://herdr.dev/install.sh | sh
```

or `brew install herdr` · `mise use -g herdr` · windows beta: `powershell -ExecutionPolicy Bypass -c "irm https://herdr.dev/install.ps1 | iex"` · [binaries](https://github.com/ogulcancelik/herdr/releases)

then start it where the work lives:

```bash
herdr
```

run your agents, split panes, walk away. `ctrl+b q` detaches, `herdr` reattaches.

## development

```bash
git clone https://github.com/ogulcancelik/herdr
cd herdr
cargo build --release

just test        # unit tests
just check       # formatting, tests, and maintenance checks
```

## license

Herdr is dual-licensed:

1. Open source: GNU Affero General Public License v3.0 or later (AGPL-3.0-or-later).
2. Commercial: commercial licenses are available for organizations that cannot comply with AGPL.

Contact: hey@herdr.dev

## Docs

### AGENTS.md (key architecture principles)

Key universal project rules:
- **State is separated from runtime.** `AppState` is pure data, testable without PTYs or async.
- **Render is pure.** `compute_view()` handles geometry, `render()` draws from `&AppState` only.
- **No god objects.** `app/` is split into state, actions, and input — keep it that way.
- **Platform code is isolated.** OS-specific behavior lives in `src/platform/<os>.rs`.
- **Detection is decoupled.** The detector reads a screen snapshot, never touches the parser or viewport state.
- **Screen detection is evidence-based.** Manifests use AND/OR gates on invariant visible controls from the bottom-buffer snapshot.

Architecture: migrating toward server-owned runtime protocol with TUI as one client. New state/API fields should go in server state exposed through JSON API; TUI-only presentation state goes in client layer.

### Top-level structure

```
.codex/          - Codex configuration
.pi/             - Pi agent configuration
.zed/            - Zed editor configuration
AGENTS.md        - agent instructions (architecture, testing, detection, release)
CLAUDE.md        - Claude instructions
SKILL.md         - Herdr skill for coding agents
CONTRIBUTING.md  - contribution guidelines
CHANGELOG.md     - release notes
src/             - Rust source
  detect/        - agent detection engine + TOML manifests per agent
  platform/      - OS-specific code (macos, linux, windows)
  app/           - state, actions, input subsystems
  protocol/      - wire protocol
docs/next/       - unreleased docs (staged for next release)
website/         - herdr.dev site source (Astro)
  src/content/docs/  - stable public docs
vendor/          - vendored libghostty-vt (Rust terminal parser)
nix/             - Nix flake package
scripts/         - release and maintenance scripts
tests/           - integration tests
justfile         - `just test`, `just check`, `just release`
```
