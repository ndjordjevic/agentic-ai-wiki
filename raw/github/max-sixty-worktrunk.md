# max-sixty/worktrunk

## Metadata
- Stars: 5470
- Primary language: Rust
- Default branch: main
- Latest release: v0.58.0 (2026-06-13)
- License: Other (MIT OR Apache-2.0)
- Homepage: https://worktrunk.dev
- Fetched: 2026-06-16
- Final URL: https://github.com/max-sixty/worktrunk

## Description
Worktrunk is a CLI for Git worktree management, designed for parallel AI agent workflows

## README
<!-- markdownlint-disable MD033 -->

<h1><img src="docs/static/logo.png" alt="Worktrunk logo" width="50" align="absmiddle">&nbsp;&nbsp;Worktrunk</h1>

[![Docs](https://img.shields.io/badge/docs-worktrunk.dev-blue?style=for-the-badge&logo=gitbook)](https://worktrunk.dev)
[![Crates.io](https://img.shields.io/crates/v/worktrunk?style=for-the-badge&logo=rust)](https://crates.io/crates/worktrunk)
[![License: MIT OR Apache-2.0](https://img.shields.io/badge/license-MIT%20OR%20Apache--2.0-blue?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![CI](https://img.shields.io/github/actions/workflow/status/max-sixty/worktrunk/ci.yaml?event=push&branch=main&style=for-the-badge&logo=github)](https://github.com/max-sixty/worktrunk/actions?query=branch%3Amain+workflow%3Aci)
[![Codecov](https://img.shields.io/codecov/c/github/max-sixty/worktrunk?style=for-the-badge&logo=codecov)](https://codecov.io/gh/max-sixty/worktrunk)
[![Stars](https://img.shields.io/github/stars/max-sixty/worktrunk?style=for-the-badge&logo=github)](https://github.com/max-sixty/worktrunk/stargazers)
[![maintained with tend](https://img.shields.io/badge/maintained_with-tend-bba580?style=for-the-badge&logo=data:image/svg%2bxml;base64,...)](https://github.com/max-sixty/tend)

> **June 2026**: Worktrunk was [released](https://x.com/max_sixty/status/2006077845391724739?s=20) at the start of the year, and has quickly become the most popular git worktree manager. It's built with love (there's no slop!). Please let me know any frictions at all; I'm intensely focused on continuing to make Worktrunk excellent, and the biggest help is folks posting problems they perceive.

Worktrunk is a CLI for git worktree management, designed for running AI agents in parallel.

Worktrunk's three core commands make worktrees as easy as branches. Plus, Worktrunk has a bunch of quality-of-life features to simplify working with many parallel changes, including hooks to automate local workflows.

> ### 📚 Full documentation at [worktrunk.dev](https://worktrunk.dev) 📚

## Context: git worktrees

AI agents like Claude Code and Codex can handle longer tasks without
supervision, such that it's possible to manage 5-10+ in parallel. Git's native
worktree feature give each agent its own working directory, so they don't step
on each other's changes.

But the git worktree UX is clunky. Even a task as small as starting a new
worktree requires typing the branch name three times: `git worktree add -b feat
../repo.feat`, then `cd ../repo.feat`.

## Worktrunk makes git worktrees as easy as branches

Worktrees are addressed by branch name; paths are computed from a configurable template.

**Core commands** (vs. plain git):
- Switch worktrees: `wt switch feat` vs `cd ../repo.feat`
- Create + start Claude: `wt switch -c -x claude feat` vs `git worktree add -b feat ../repo.feat && cd ../repo.feat && claude`
- Clean up: `wt remove` vs `cd ../repo && git worktree remove ../repo.feat && git branch -d feat`
- List with status: `wt list` vs `git worktree list` (paths only)

**Workflow automation:**

- **Hooks** — run commands on create, pre-merge, post-merge, etc
- **LLM commit messages** — generate commit messages from diffs
- **Merge workflow** — squash, rebase, merge, clean up in one command
- **Interactive picker** — browse worktrees with live diff and log previews
- **Copy build caches** — skip cold starts by sharing `target/`, `node_modules/`, etc between worktrees
- **`wt list --full`** — CI status and AI-generated summaries per branch
- **PR checkout** — `wt switch pr:123` to jump straight to a PR's branch
- **Dev server per worktree** — `hash_port` template filter gives each worktree a unique port
- **Aliases & per-branch variables** — custom `wt <name>` commands and branch-scoped state for hook templates
- ...and lots more

## Install

**Homebrew (macOS & Linux):**
```bash
brew install worktrunk && wt config shell install
```
Shell integration allows commands to change directories.

**Cargo:**
```bash
cargo install worktrunk && wt config shell install
```

**Windows:** `wt` defaults to Windows Terminal's command, so Winget additionally installs Worktrunk as `git-wt` to avoid the conflict:
```bash
winget install max-sixty.worktrunk
git-wt config shell install
```
Alternatively, disable Windows Terminal's alias (Settings → Privacy & security → For developers → App Execution Aliases → disable "Windows Terminal") to use `wt` directly.

**Arch Linux:** `sudo pacman -S worktrunk && wt config shell install`

**Conda / Pixi** (community-maintained feedstock): `conda install -c conda-forge worktrunk && wt config shell install`, or `pixi global install worktrunk && wt config shell install`.

## Quick start

Create a worktree for a new feature:
```console
$ wt switch --create feature-auth
✓ Created branch feature-auth from main and worktree @ ~/repo.feature-auth
```

This creates a new branch and worktree, then switches to it. Check all worktrees with `wt list`:
```console
$ wt list
  Branch        Status        HEAD±    main↕  Remote⇅  Commit    Age   Message
@ feature-auth  +   ↑      +27   -8   ↑1               4bc72dc9  2h    Add authentication module
^ main              ^⇡                         ⇡1      0e631add  1d    Initial commit

○ Showing 2 worktrees, 1 with changes, 1 ahead, 1 column hidden
```
The `@` marks the current worktree. `+` means staged changes, `↑1` means 1 commit ahead of main, `⇡` means unpushed commits.

**PR workflow** — commit, push, open a PR, merge via GitHub/GitLab, then clean up:
```bash
wt step commit                    # commit staged changes
gh pr create                      # or glab mr create
wt remove                         # after PR is merged
```

**Local merge** — squash, rebase onto main, fast-forward merge, clean up:
```console
$ wt merge main
◎ Generating commit message and committing changes... (2 files, +53, no squashing needed)
  Add authentication module
✓ Committed changes @ a1b2c3d
◎ Merging 1 commit to main @ a1b2c3d (no rebase needed)
✓ Merged to main (1 commit, 2 files, +53)
◎ Removing feature-auth worktree & branch in background (same commit as main, _)
○ Switched to worktree for main @ ~/repo
```

For parallel agents, create multiple worktrees and launch an agent in each:
```bash
wt switch -x claude -c feature-a -- 'Add user authentication'
wt switch -x claude -c feature-b -- 'Fix the pagination bug'
wt switch -x claude -c feature-c -- 'Write tests for the API'
```
The `-x` flag runs a command after switching; arguments after `--` are passed to it. Configure post-start hooks to automate setup (install deps, start dev servers).

## Next steps

- Learn the core commands: `wt switch`, `wt list`, `wt merge`, `wt remove`
- Set up hooks for automated setup
- Explore LLM commit messages, interactive picker, Claude Code integration, CI status & PR links
- Browse tips & patterns for recipes: aliases, dev servers, databases, agent handoffs, and more
- Extending Worktrunk — customize workflows with hooks & aliases
- Run `wt --help` or `wt <command> --help` for quick CLI reference

## Further reading

- Claude Code: Best practices for agentic coding — Anthropic's official guide, including the worktree pattern
- Shipping faster with Claude Code and Git Worktrees — incident.io's workflow for parallel agents
- Git worktree pattern discussion — Community discussion in the Claude Code repo
- @DevOpsToolbox's video on Worktrunk
- git-worktree documentation — Official git reference

## Docs (project AGENTS.md — development guidelines, included for architecture/design context)

### Project Status
Maturing mode: a growing user base, so balance clean design with compatibility.
- External-interface breaks need justification (a real improvement, not cleanup); prefer deprecation warnings over silent breaks.
- **Protected interfaces:** config file format (`wt.toml`, user config) and CLI flags/arguments. Everything else (internal APIs, output formatting, log locations) is flexible.
- No Rust library compatibility concerns (CLI tool only).

### Terminology
- **main worktree** — the original git directory (from clone/init); bare repos have none
- **linked worktree** — created via `git worktree add` (git's term)
- **primary worktree** — the "home" worktree: main worktree for normal repos, default-branch worktree for bare repos
- **default branch** — the branch (main, master, …), not "main branch"
- **target** — destination for merge/rebase/push ("merge target"). Never use "target" for worktrees; say "worktree"

### Worktree Model
- Worktrees are **addressed by branch name**, not filesystem path.
- Each worktree maps to **exactly one branch**.
- **Never retarget an existing worktree** to a different branch; create/switch/remove instead. (Sole exception: `wt step promote`, experimental, exchanges branches between two worktrees.)

### Data Safety
Never risk data loss without explicit user consent. A failed command that preserves data beats a "successful" one that silently destroys work.
- **Prefer failure over silent loss** — if an operation might destroy untracked files, uncommitted changes, or user data, fail with an error.
- **Explicit consent for destructive ops** — force-removing data (e.g. `--force` on remove) requires the user to explicitly request it.
- **No implicit destructive side effects** — never silently delete/overwrite as a side effect of an unrelated operation; make cleanup a separate explicit action the user chooses.
- **Favor the failing variant on races** — `git reset --keep` (fails if tracked files were modified) over `--hard`; `git checkout --merge` over `--force`.

### Command Execution Principles
- **All commands through `shell_exec::Cmd`** for consistent debug logging and timing.
- **Real-time output streaming** — line-by-line rather than buffering.
- **Structured output over error-message parsing** — prefer exit codes / `--porcelain` / `--json` over parsing human-readable messages, which break on locale, version, and rewording changes.
- **Network access** — worktrunk is local-first: network is touched only when the user asked for it. What currently reaches the wire: `wt list --full` / `wt list statusline` (CI status), LLM commit/branch-summary generation, `wt switch pr:<n>`/`mr:<n>` (host API + git fetch), `wt config show --full` (version check), first `Repository::default_branch()` per repo (`git ls-remote`, cached after).
- **Signal handling** — Ctrl-C cancels the current command: every loop in the foreground execution path aborts rather than continuing to the next iteration when a child exits from SIGINT/SIGTERM.
- **Project commands run only after approval** — hooks (`pre-*`/`post-*`), `[aliases]`, and `--execute` bodies from project config are arbitrary code from a possibly-just-cloned repo, gated by an approval system before running. This is the only thing standing between `git clone && wt switch` and a `post-switch` hook running `curl … | sh`.

### Code Quality
- Don't suppress warnings with `#[allow(dead_code)]` — delete the code or add a `// TODO(topic)`.
- Complex systems (state machines, cached state, cross-module coordination) get a module-level spec docstring.
- No test code in library code — no `#[cfg(test)]` convenience methods on library types.
- `anyhow` with context; `bail!` for business-logic errors, `.context()` for I/O/external-command wrapping. Never `.expect()`/`.unwrap()` in a function returning `Result`.

### Config Deprecation
All config deprecation lives in one layer: pre-deserialization TOML migration in `src/config/deprecation.rs`. Never silently drop an old config key — migrate it. Each deprecation is one row in a `DEPRECATION_RULES` table: a single idempotent function rewrites the pattern and reports what changed, so detection and migration can't drift.

## Top-level structure
- `.agents/`, `.claude/`, `.claude-plugin/` — agent/Claude Code integration assets
- `.config/`, `.cargo/` — tooling config
- `.github/` — CI workflows
- `AGENTS.md` — development guidelines (captured above); `CLAUDE.md` (17,988 bytes) — additional Claude-specific guidance
- `CHANGELOG.md` — release history (337,652 bytes)
- `Cargo.toml` / `Cargo.lock` — Rust package manifest and lockfile
- `Taskfile.yaml` — task runner definitions (18,002 bytes)
- `benches/` — Criterion benchmarks (`cargo bench --bench list`)
- `build.rs` — build script
- `dev/` — developer scripts
- `dist-workspace.toml` — `cargo-dist` release packaging config
- `docs/` — Hugo-based documentation site source (served at worktrunk.dev); `docs/content/` holds the docs pages: `_index.md`, `claude-code.md`, `config.md`, `extending.md`, `faq.md`, `hook.md`, `list.md`, `llm-commits.md`, `merge.md`, `remove.md`, `step.md`, `switch.md`, `tips-patterns.md`, `worktrunk.md` (README is auto-generated from `worktrunk.md`)
- `flake.nix` / `flake.lock` / `nix/` — Nix dev environment
- `gemini-extension.json` — Gemini CLI extension manifest
- `hooks/` — hook script examples/templates
- `plugins/` — per-tool plugin layout (Claude/Codex/Gemini)
- `rust-toolchain.toml` — pinned Rust toolchain
- `skills/` — agent skill definitions (e.g. `skills/worktrunk/`)
- `src/` — Rust source (CLI in `src/cli/mod.rs`, commands in `src/commands/`, git logic in `src/git/`)
- `templates/` — built-in templates
- `tests/` — integration tests
- `vendor/` — vendored dependencies
