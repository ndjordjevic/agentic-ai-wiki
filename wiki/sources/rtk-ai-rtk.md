---
type: source
category: "Knowledge, RAG, memory & context"
source_url: https://github.com/rtk-ai/rtk
tags:
  - token-optimization
  - shell-proxy
  - pretooluse-hook
  - command-rewriting
  - output-filtering
  - claude-code-hooks
  - multi-agent-support
related:
  - nadimtuhin-claude-token-optimizer
  - chopratejas-headroom
  - mksglu-context-mode
  - Houseofmvps-codesight
product: rtk
detail_level: standard
created: 2026-07-21
updated: 2026-07-21
---

rtk (Rust Token Killer) is a single-binary Rust CLI proxy that sits between an AI coding agent and everyday dev commands (git, cargo, npm/pnpm, pytest, docker, aws, and 100+ others), filtering and compressing each command's stdout/stderr before it reaches the LLM's context — reporting 60-90% token savings on common operations. Unlike context-management tools that restructure project docs or sandbox MCP tool output, rtk targets raw shell-command noise specifically, via a PreToolUse hook that rewrites Bash calls transparently (`git status` → `rtk git status`) across 15+ supported AI coding tools.

_All claims below are sourced from ../../raw/github/rtk-ai-rtk.md unless otherwise noted._

## What it does

rtk wraps ~100 commands across nine ecosystems (git, JS/TS, Python, Go, Ruby, .NET, cloud/containers, system utilities, Rust) and applies one of twelve named filtering strategies per command type — stats extraction, error-only, grouping by pattern, deduplication, structure-only JSON schemas, language-aware code filtering, failure-focus for test runners, tree compression for directory listings, ANSI progress-bar stripping, JSON/text dual mode, state-machine parsing, and NDJSON streaming — to compress output while preserving the information an agent actually needs (exit codes, failure details, diff stats).

## Installation

Homebrew (`brew install rtk`), a curl-to-shell installer, `cargo install --git`, or pre-built binaries for macOS/Linux/Windows. After installing the binary, `rtk init -g` installs the PreToolUse hook plus an `RTK.md` reference file; flags select the target agent (`--gemini`, `--codex`, `--agent cursor`, `--agent windsurf`, `--agent hermes`, `--agent droid`, etc.). `rtk init --show` verifies the install; `rtk init -g --uninstall` removes it.

## Key features

Six-phase command lifecycle (parse → route → execute → filter → print → track) with a SQLite-backed tracking database (`~/.local/share/rtk/history.db`) recording input/output token estimates and savings percentage per invocation. Meta-commands surface this data: `rtk gain` (summary/graph/daily/JSON stats), `rtk discover` (finds missed savings opportunities across projects), and `rtk session` (adoption tracking). A `tee` mode (default: on failures) saves full unfiltered output to disk so the agent can inspect a failure without re-running the command. Verbosity flags (`-v`/`-vv`/`-vvv`) progressively reveal debug messages, the executed command, and raw pre-filter output.

## Architecture

The codebase is organized into 64 Rust modules: 42 command modules under `src/cmds/` grouped by ecosystem (git, rust, js, python, go, dotnet, cloud, system, ruby), plus 22 infrastructure modules — `src/core/` (utils, filter, tracking, tee, config, toml_filter, telemetry), `src/hooks/` (init, rewrite, permissions, verify, trust, integrity), and `src/analytics/` (gain, cc_economics, ccusage, session). Since v0.37.2 the Claude Code hook runs as a native binary command (`rtk hook claude`) rather than a shell script, so it works on native Windows without WSL or bash. (../../raw/github/rtk-ai-rtk.md)

## Example usage

```bash
rtk init -g              # install hook + RTK.md for Claude Code
git status                # auto-rewritten to `rtk git status` by the hook
rtk cargo test            # explicit invocation; compact failure-only output
rtk gain                  # show token-savings analytics
```
(../../raw/github/rtk-ai-rtk.md)

## When to use

Fits teams running Claude Code, Copilot, Cursor, Gemini CLI, Codex, Windsurf, Cline, OpenCode, Pi, Hermes, Kilo Code, Antigravity, Kimi, or Factory Droid where Bash-tool command output (not MCP tool output or stale project docs) is the dominant context cost — e.g. repeated `git diff`, `cargo test`, or `docker ps` calls during a long dev session. It complements rather than replaces doc-restructuring tools like [[nadimtuhin-claude-token-optimizer]] and MCP-output sandboxes like [[mksglu-context-mode]], since it operates strictly on the Bash-hook path and does not touch built-in `Read`/`Grep`/`Glob` calls.

## Ecosystem

Configurable per-project via `~/.config/rtk/config.toml` (command exclusions, tee mode). Ships opt-in, GDPR-consent-gated anonymous telemetry (aggregate command-category counts, estimated savings) disabled by default and revocable via `rtk telemetry disable`/`forget`. Some Windows filters shell out to ripgrep. Companion integrations exist for OpenClaw (plugin) and Hermes (Python plugin adapter under `hooks/hermes/`).
