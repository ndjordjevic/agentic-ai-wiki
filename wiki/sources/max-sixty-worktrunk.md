---
type: source
category: "Terminal, session & parallel-agent runners"
source_url: https://github.com/max-sixty/worktrunk
tags: [git-worktrees, parallel-ai-agents, cli-tool, rust, merge-workflow, llm-commit-messages, hooks]
related: []
product: worktrunk
detail_level: standard
created: 2026-06-16
updated: 2026-06-16
---

Worktrunk is a Rust CLI (5,470 stars, MIT OR Apache-2.0) that wraps git's native worktree feature to make running multiple AI coding agents in parallel as easy as switching branches. It addresses the friction of plain `git worktree` commands — typing the branch name three times, manually computing paths — by addressing worktrees purely by branch name and deriving filesystem paths from a configurable template.

_All claims below are sourced from ../../raw/github/max-sixty-worktrunk.md unless otherwise noted._

## What it does

Three core commands replace the equivalent multi-step git invocations: `wt switch <branch>` (create/switch, optionally with `-c` to create and `-x <cmd>` to launch an agent in the new worktree), `wt list` (status table showing staged changes, commits ahead/behind, ahead/behind remote, age, and last commit message per worktree), and `wt remove` (deletes the worktree and its branch in one step). A typical parallel-agent pattern launches several agents at once: `wt switch -x claude -c feature-a -- 'Add user authentication'` followed by similar calls for `feature-b`, `feature-c`, each spinning up its own worktree and Claude session.

## Installation

Distributed via Homebrew (`brew install worktrunk && wt config shell install`), Cargo (`cargo install worktrunk`), Winget (installed as `git-wt` on Windows to avoid a name collision with Windows Terminal's own `wt` alias), Arch's `pacman`, and community-maintained Conda-forge / Pixi packages. The `wt config shell install` step wires up shell integration so commands can change the calling shell's working directory.

## Key features

- **Hooks** — run commands at create, pre-merge, post-merge, pre-remove, post-remove, post-switch, pre-start, post-start lifecycle points, gated by an approval system since hook commands are arbitrary project-defined code that could otherwise let `git clone && wt switch` trigger remote code execution via a malicious `post-switch` hook.
- **LLM commit messages** — generates commit messages from diffs as part of `wt merge`'s automated commit step.
- **Merge workflow** — `wt merge <target>` squashes, rebases onto the target, fast-forward merges, and removes the worktree/branch in one command.
- **Interactive picker** — browse worktrees with live diff and log previews when switching.
- **Build-cache copying** — `wt step copy-ignored` shares `target/`, `node_modules/`, etc. between worktrees to skip cold starts.
- **`wt list --full`** — adds CI status and AI-generated per-branch summaries to the status table.
- **PR/MR checkout** — `wt switch pr:123` or `mr:123` resolves and checks out a pull/merge request branch directly via the GitHub/GitLab API.
- **Aliases and per-branch state variables** — custom `wt <name>` commands and branch-scoped variables usable inside hook templates.

## Architecture

Worktrunk is local-first: it touches the network only when a command explicitly requires it (CI-status fetches for `wt list --full`/`wt list statusline`, LLM commit/branch-summary generation, PR/MR resolution for `wt switch pr:<n>`, a version check in `wt config show --full`, and a one-time-per-repo `git ls-remote` fallback inside default-branch detection, cached thereafter). All external commands route through a `shell_exec::Cmd` wrapper for consistent debug logging and timing, and command output streams line-by-line rather than buffering, prioritizing responsiveness. The project favors structured output (exit codes, `--porcelain`, `--json`) over parsing human-readable CLI messages, which break across locale, version, and wording changes. Config deprecation is centralized in a single pre-deserialization TOML migration layer so old config keys are rewritten rather than silently dropped, with one idempotent function per deprecation rule driving both detection and migration so the two can't drift apart.

## Example usage

```bash
wt switch --create feature-auth        # create branch + worktree, switch to it
wt list                                # status table across all worktrees
wt step commit                         # commit staged changes (PR workflow)
gh pr create
wt remove                              # after the PR merges

wt merge main                          # local workflow: squash, rebase, ff-merge, cleanup
```

## When to use

Worktrunk targets developers running several AI coding agents (Claude Code, Codex, etc.) concurrently against the same repository, where each agent needs an isolated working directory and the developer needs a fast way to create, monitor, and tear down those directories without memorizing multi-step `git worktree` invocations.

## Maintenance status

5,470 stars, latest release v0.58.0 (2026-06-13), default branch `main`, actively maintained per the project's "Maturing mode" stance: a growing user base means external interface changes (config file format, CLI flags) require justification and prefer deprecation warnings over silent breaks, while internal APIs and output formatting remain flexible. CI, Codecov coverage gating, and Criterion benchmarks run on every change; `codecov/patch` failures block merge despite being marked non-required in GitHub's UI.

## Ecosystem

Ships first-party integration assets for Claude, Codex, and Gemini under `.claude/`, `.claude-plugin/`, `plugins/`, `skills/`, and a `gemini-extension.json`, plus a `docs/` Hugo site (worktrunk.dev) whose `docs/content/worktrunk.md` is the single source of truth that the GitHub README is auto-generated from. The README explicitly cites Anthropic's "Claude Code: Best practices for agentic coding" guide and a Claude Code GitHub issue discussion on the worktree pattern as background reading, positioning Worktrunk as purpose-built tooling for the parallel-agent workflow this wiki tracks elsewhere (e.g. multi-agent terminal/session managers and agent task boards).
