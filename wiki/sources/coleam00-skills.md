---
type: source
category: "Coding-agent harnesses & methodologies"
source_url: https://github.com/coleam00/skills
tags:
  - piv-loop
  - claude-code-plugin
  - lifecycle-hooks
  - worktrees
  - ai-layer
  - meta-skills
related:
  - anthropics-skills
  - skills.sh
  - obra-superpowers
  - gsd-build-get-shit-done
  - coleam00-agent-control-plane
  - coleam00-ai-native-starter-pack
product: skills
detail_level: standard
created: 2026-09-28
updated: 2026-09-28
---

Cole Medin's personal collection of 35 Claude Code Agent Skills, published straight out of his own `.claude/skills/` folder and distributed as a Claude Code plugin. Where [[anthropics-skills]] is Anthropic's own reference set and [[skills.sh]] is a general skills registry, this repo is one practitioner's opinionated, end-to-end coding-agent workflow — the PIV loop (plan, implement, validate) plus the priming, planning, worktree, and meta-skills that surround it — making it a concrete worked example of an "AI Layer" built skill-by-skill rather than as a monolithic rules file.

_All claims below are sourced from ../../raw/github/coleam00-skills.md unless otherwise noted._

## What it does

The repo packages 35 skill folders (each a plain-markdown `SKILL.md`) around one loop the author runs on nearly every ticket: **prime → plan → implement → validate → review → commit → PR**. Skills are grouped into: Prime (`prime-codebase`, `prime-backend`, `prime-frontend`), Plan (`plan-create-prd`, `plan-architecture`, `piv-slice-epic`, `plan-create-stories`), the PIV loop itself (`piv-plan-implementation`, `piv-implement`, `piv-validate`, `piv-review-changes`, `piv-fix-review-findings`, `piv-commit`, `piv-create-pr`, `piv-review-pr`, `piv-run-full-loop`), Issues (`piv-investigate-issue`, `piv-implement-issue`), Parallel work (`worktree-create`, `worktree-merge`), meta-skills for building more of the AI Layer (`rules-create-global`, `rules-check-drift`, `ablate-ai-layer`, `skills-create`, `hooks-create`, `opportunity-scan`, `system-execution-report`, `system-evolution-review`, `second-brain-audit`), an autonomy skill (`build-dark-factory`), and standalone tools (`agent-browser`, `ast-grep`, `drive-screen`, `setup-ai-tutor`). One further folder, `second-brain-fix`, exists in the tree alongside `second-brain-audit` but is not tabulated in the README. The author frames the whole set as "nothing here is a framework" — each skill is a short markdown file meant to be read, disagreed with, and edited rather than adopted wholesale.

## Key features

- **PIV loop as skills, not a framework**: plan → implement → validate → review → commit → PR is decomposed into individually invokable skills rather than one script, so any step can be swapped or skipped.
- **Meta-skills that build more skills**: `skills-create` authors new skills or splits a bloated one into `SKILL.md` + `references/`; `opportunity-scan` reads how the user actually works and recommends what to encode next; `rules-check-drift` checks whether a rules file is still true after recent changes; `ablate-ai-layer` strips rules/skills, reruns the same task, and diffs the two runs to test whether they're earning their place.
- **`build-dark-factory`**: takes a PRD and builds a repo around it that ships validated code with nobody at the keyboard — an autonomy skill that deliberately does not write the PRD itself, expecting one from `plan-create-prd` or elsewhere.
- **Worktree pair**: `worktree-create` spins up N git worktrees, each configured/installed/health-checked, and `worktree-merge` integrates the resulting branches through one safe integration branch — supporting running several PIV loops in parallel.
- **Customization points**: `piv-validate` ships with a placeholder command list meant to be replaced with the project's real test/type-check/lint commands; `piv-commit` and `piv-create-pr` read `.claude/references/conventions.md` (its `## commit` and `## pr` sections) if present; `piv-review-pr` hands its deep pass to a `code-reviewer` subagent when one exists in `.claude/agents/`.

## Architecture

The repo is a Claude Code plugin: `.claude-plugin/plugin.json` declares it as plugin `skills` (currently version `1.3.1`) pointing at `./.claude/skills`, and `.claude-plugin/marketplace.json` publishes it under marketplace `cole-medin`. (../../raw/github/coleam00-skills.md) All 35 skills together cost roughly 4,400 tokens of always-on context (just the descriptions; each skill's body loads only when it fires), inspectable per-skill via `claude plugin details skills`. (../../raw/github/coleam00-skills.md) Skills are plain markdown with no Claude-specific runtime, so the author frames most of them as portable to any agent that can read files — the `npx skills` CLI installs the set into 75+ agents (Codex, Cursor, Copilot, Cline, Windsurf, OpenCode, Continue, etc.), adjusting only slash-command syntax and `allowed-tools` frontmatter, which other agents ignore harmlessly. (../../raw/github/coleam00-skills.md)

A separate `hooks/` directory supplies the deterministic half of the same "AI Layer" idea: six copy-in Python scripts (`pre_tool_use_secrets.py`, `pre_tool_use_dependencies.py`, `post_tool_use_log.py`, `session_start_context.py`, `stop_tests_must_pass.py`, `stop_notify.py`) that fire on Claude Code lifecycle events (PreToolUse, PostToolUse, SessionStart, Stop) regardless of whether the model "remembers" to follow a rule. (../../raw/github/coleam00-skills.md) The hooks README frames the split explicitly: rules *ask* the agent to behave, hooks *guarantee* it, citing a study (arXiv:2604.25850, "Agentic Harness Engineering") in which a self-rewritten 9KB system prompt alone scored *below* doing nothing, with the entire measured gain coming from memory/tools/middleware — i.e. enforcement rather than instruction. (../../raw/github/coleam00-skills.md) The README documents six operational gotchas for anyone wiring these hooks up (a `uv run` sandboxed venv trap, `@file` mentions bypassing `PreToolUse` entirely, `additionalContext` needing to nest under `hookSpecificOutput`, exit code 2 — not 1 — being the actual block signal, an eight-block spin cap on `Stop` hooks without a loop guard, and hooks running in a non-interactive shell with no profile). (../../raw/github/coleam00-skills.md) It also notes hook portability: Codex and Cursor use the same script/stdin-JSON/exit-2 shape, Gemini CLI reads a structured JSON decision instead of the exit code, and Pi/opencode run hooks in-process as plugins. (../../raw/github/coleam00-skills.md)

## Installation

Three ways to bring the skills in, from most to least managed. (../../raw/github/coleam00-skills.md)

As a Claude Code plugin (stays updated automatically):
```
/plugin marketplace add coleam00/skills
/plugin install skills@cole-medin
```
If the marketplace add fails with `Permission denied (publickey)` (the `owner/repo` shorthand prefers SSH), pass the HTTPS URL directly instead: `/plugin marketplace add https://github.com/coleam00/skills.git`, or set `CLAUDE_CODE_PLUGIN_PREFER_HTTPS=1` permanently. (../../raw/github/coleam00-skills.md)

As editable files, in any agent, via the `npx skills` CLI:
```bash
npx skills add coleam00/skills                             # everything
npx skills add coleam00/skills --list                      # preview first
npx skills add coleam00/skills --skill piv-plan-implementation piv-implement piv-validate
```
Add `-g` to install globally into `~/.claude/skills/` instead of the current project; this route writes real, editable files. (../../raw/github/coleam00-skills.md)

Hooks install separately:
```bash
mkdir -p .claude/hooks
cp hooks/*.py .claude/hooks/
cp hooks/settings.json.example .claude/settings.json   # or merge the "hooks" block
```
(../../raw/github/coleam00-skills.md)

## Example usage

The README's suggested one-shot prompt for pulling in a curated subset without the CLI: "Clone https://github.com/coleam00/skills, look at the skills in `.claude/skills/`, and copy the ones that fit this project into my `.claude/skills/` folder. Tell me which ones you picked and why." (../../raw/github/coleam00-skills.md) For hooks, `stop_tests_must_pass.py` requires setting `TEST_COMMAND` to the project's real test command, and `pre_tool_use_dependencies.py` requires copying `dependencies.example.json` to `.claude/hooks/dependencies.json` and declaring real file couplings — until that file exists the dependency hook allows everything, so it is safe to install unconfigured. (../../raw/github/coleam00-skills.md) The README recommends proving each hook works rather than trusting it on sight, e.g.: `echo '{"session_id":"t","cwd":".","tool_name":"Read","tool_input":{"file_path":".env"}}' | uv run .claude/hooks/pre_tool_use_secrets.py; echo "exit=$?"` should exit 2 (block). (../../raw/github/coleam00-skills.md)

## When to use

Fits teams already running (or wanting to run) Claude Code's Agent Skills mechanism who want a working, opinionated PIV loop rather than building prime/plan/implement/validate/review/commit skills from scratch — read each skill in minutes, keep what fits, rewrite the rest. The worktree pair and `piv-run-full-loop` particularly suit teams running several tickets through the loop in parallel. `build-dark-factory` is aimed at teams wanting to hand an entire feature (from an existing PRD) to an unattended agent run. Compare against [[anthropics-skills]] (a broader, less workflow-specific reference set) and [[obra-superpowers]] or [[gsd-build-get-shit-done]] for other opinionated coding-agent skill/workflow collections.

## Maintenance status

635 stars, 176 forks, MIT license, primary language Python (the hook scripts), default branch `main`. No tagged GitHub releases; the plugin manifest tracks its own semver (`1.3.1`) independent of repo releases. Most recently pushed 2026-09-17. Actively authored by Cole Medin (coleam00), tied to his "Agentic Coding" course. (../../raw/github/coleam00-skills.md)
