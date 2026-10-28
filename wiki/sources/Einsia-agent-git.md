---
type: source
category: "Terminal, session & parallel-agent runners"
source_url: https://github.com/Einsia/agent-git
tags:
  - session-version-control
  - agent-sessions
  - agit
  - jsonl-transcripts
  - multi-harness
  - rust-cli
  - publishable-sessions
  - agent-git
related:
  - xhluca-session-migrate
  - trailhq.com
  - tmuxai.dev
  - max-sixty-worktrunk
  - herdr.dev
  - njbrake-agent-of-empires
product: agent-git
detail_level: standard
created: 2026-10-28
updated: 2026-10-28
---

Einsia/agent-git (`agit`, ~414★, MIT, Rust v0.2.28) is lossless version control for coding-agent sessions — snapshots and publishable history on top of Claude Code, Codex, OpenCode, and Cursor JSONL transcripts that would otherwise be overwritten, compacted, or lost. Tagline: "Code is cheap, show me the talk." Complements [[xhluca-session-migrate]] (move a session between harnesses) by versioning and sharing sessions within/across teammates on the AgentGit hub (https://agent-git.com; backend is a separate repo).

_All claims below are sourced from ../../raw/github/Einsia-agent-git.md unless otherwise noted._

## What it does

`agit` treats agent conversations as first-class versioned artifacts: adopt a native runtime session (`agit import`), settle completed turns into git commits (`agit commit`), browse history (`agit log`), publish (`agit push` / `agit share`), and resume or fork from a tag/ref (`agit resume`, `agit run owner/repo@ref`). Bare commands open a human TUI; scripts pass explicit `owner/repo@branch` targets and `--json`. Storage lives under `~/.agit` (links + local agent repos); transcripts stay in the runtime's native paths — agit does not duplicate multi-GB JSONL stores.

## Installation

Users (prebuilt binary, no Rust toolchain):

```sh
npx -y create-agit@latest
# or
npm install -g @einsia/agent-git
agit --version
```

Do **not** install `@einsia/agentgit` (no hyphen) — that is the pre-rewrite CLI. pnpm v10+ skips install scripts; run `agit setup` once after install. Contributors: `git clone` + `./setup.sh` (needs rustc ≥ 1.88 and a C compiler). Linux npm artifacts are musl static-linked.

## Key features

- **Multi-runtime adoption** — Claude Code, Codex, OpenCode, Cursor; explicit runtime + session ID; lineage discovery with `--onto` / `--independent` / `--propose-lineage`.
- **Git-shaped workflow** — `import`, `commit`, `push`, `clone` / `clone --mine`, `run`, `resume`, `log`, `share`, `revert`; never rebase/force-push AgentGit history (per AGENTS.md).
- **Hub publish** — default hub `https://agent-git.com`; self-host via `AGIT_HUB_URL`; backend is separate (AgentGit server).
- **Secrets** — global secret filter + reversible repository secret dictionary; privacy/publication docs in-tree.
- **RC / Workspaces** — remote-control daemon (`agit rc start`) for device registration and collaboration; Windows named-pipe owner RPC.
- **Agent wiring** — `create-agit` / `agit setup` installs skills/hooks/MCP; AGENTS.md embeds an `<!-- agit:begin -->` control block for managed sessions.
- **Daily upgrade check** — reminder only; never auto-upgrades; JSON/quiet/CI/hook paths skip it.

## Architecture

Rust workspace: main `agit` binary (`src/` — adapter, commands, domain, hub, infra, protocol, rc, telemetry, tui, ui) plus crates `agit-controller`, `agit-peer`, `agit-tunnel`; optional `apps/macos-menubar`. Local layout: `~/.agit/credentials/`, `store/<runtime>/<session-id>.json` (links only), `repos/<owner>/<name>/` (agent git repos). npm distributes platform optionalDependencies (`@einsia/agent-git-linux-x64`, etc.) and `create-agit`. Release tags `agit-v*` from mirrored CI; version single-sourced in `Cargo.toml` (currently **0.2.28**).

## Example usage

```sh
npx -y create-agit@latest
agit login
agit import                 # TUI: adopt a runtime conversation
agit commit owner/repo@branch --milestone "cracked the bug"
agit push owner/repo@branch --json
agit run owner/repo@ref     # open a saved source (may fork)
agit resume                 # continue same session, never forks
```

## Maintenance status

414 stars, 37 forks, MIT, Rust, default branch `main`, latest release **agit-v0.2.28** (2026-10-27), pushed 2026-10-28. Homepage: https://agent-git.com. Active docs/RFCs for RC peer transports, privacy envelopes, session storage v2, and CLI JSON schema. Hub/backend shipping is out of this repo.
