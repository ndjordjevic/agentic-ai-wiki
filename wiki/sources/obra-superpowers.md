---
type: source
source_url: https://github.com/obra/superpowers
tags:
  - agent-skills
  - skill-methodology
  - subagent-driven-development
  - test-driven-development
  - spec-first
  - coding-agent-harness
  - auto-triggering-skills
  - multi-harness
related:
  - gsd-build-get-shit-done
  - anthropics-skills
  - skills.sh
  - github-spec-kit
  - shareai-lab-learn-claude-code
  - forrestchang-andrej-karpathy-skills
  - coleam00-archon
  - snarktank-ralph
  - bmad-code-org-bmad-method
product: superpowers
detail_level: standard
created: 2026-05-14
updated: 2026-05-22
---

Superpowers is a complete software development methodology for AI coding agents built on 14 composable, auto-triggering SKILL.md-based skills — 190,063 stars, MIT license, v5.1.0, maintained by Jesse Vincent and Prime Radiant. Where most agent toolkits require explicit command invocation, Superpowers installs a bootstrap skill (`using-superpowers`) that fires at session start and enforces a rule: invoke relevant skills before any response, including clarifying questions, even with a 1% chance of applicability. The methodology is opinionated: spec before code, TDD always, git worktree isolation, subagent-per-task execution with two-stage review, and human-in-the-loop checkpoints at every major transition. It is a zero-dependency plugin by design and works across Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Factory Droid, and GitHub Copilot CLI.

_All claims below are sourced from ../../raw/github/obra-superpowers.md unless otherwise noted._

## What it does

Superpowers imposes a disciplined software development workflow on top of any AI coding agent by front-loading a series of mandatory skills that auto-trigger at the right moments. When the agent detects that the user wants to build something, it doesn't jump to code — it triggers `brainstorming` to tease out a validated spec first. After spec sign-off, `writing-plans` breaks the work into 2–5 minute tasks with exact file paths, complete code, and verification steps. `subagent-driven-development` then dispatches a fresh subagent per task with a two-stage review (spec compliance, then code quality). `test-driven-development` enforces RED-GREEN-REFACTOR throughout — it deletes code written before tests exist. At each transition, `requesting-code-review` checks against the plan before the next task proceeds. The entire loop is mandatory, not optional: the `using-superpowers` bootstrap skill explicitly instructs the agent that skill invocation is non-negotiable.

## Key features

- **Auto-triggering skill bootstrap** — `using-superpowers` loads at session start and mandates skill invocation before any response (1% threshold rule).
- **14 composable skills** — covering the full development lifecycle: brainstorming, planning, execution, TDD, debugging, code review (requesting and receiving), git worktrees, subagent dispatch, and meta-skill creation.
- **Subagent-driven-development** — fresh subagent per task with two-stage review: first spec compliance, then code quality.
- **Strict TDD enforcement** — `test-driven-development` skill enforces RED-GREEN-REFACTOR and deletes pre-test code.
- **Systematic debugging** — `systematic-debugging` runs a 4-phase root-cause process including root-cause-tracing, defense-in-depth, and condition-based-waiting techniques.
- **Zero external dependencies** — pure SKILL.md files, no third-party tools or services required.
- **Multi-harness availability** — Claude Code (official plugin marketplace), Codex CLI, Codex App, Factory Droid, Gemini CLI, OpenCode, Cursor, GitHub Copilot CLI.
- **Instruction priority model** — user's CLAUDE.md/AGENTS.md/GEMINI.md always overrides Superpowers skills; Superpowers overrides default system behavior.

## Architecture

Superpowers is a `skills/` directory of 14 subdirectories, each containing a `SKILL.md` with YAML frontmatter (`name:`, `description:`) and markdown instructions. The `using-superpowers` skill is the linchpin: installed as a bootstrap that loads at session start, it establishes the skill invocation rule and provides a flowchart (in DOT notation) of when and how to invoke other skills. Skills use Claude Code tool names (`Skill` tool); platform adapters for Copilot CLI, Codex, and Gemini CLI are documented in `references/` within the using-superpowers skill.

The repository ships separate plugin manifests per harness: `.claude-plugin/` (Claude Code), `.codex-plugin/` (Codex), `.cursor-plugin/` (Cursor), `.opencode/` (OpenCode), and `gemini-extension.json` (Gemini CLI). This allows Superpowers to install cleanly into each harness's native plugin system without modification. The `hooks/` directory provides git lifecycle hooks; `tests/` provides a test suite for the methodology itself. The project is zero-dependency by design — PRs adding third-party dependencies are rejected.

## Installation

**Claude Code — official marketplace (recommended):**
```bash
/plugin install superpowers@claude-plugins-official
```

**Claude Code — Superpowers marketplace:**
```bash
/plugin marketplace add obra/superpowers-marketplace
/plugin install superpowers@superpowers-marketplace
```

**Gemini CLI:**
```bash
gemini extensions install https://github.com/obra/superpowers
```

**OpenCode:**
```
Fetch and follow instructions from https://raw.githubusercontent.com/obra/superpowers/refs/heads/main/.opencode/INSTALL.md
```

**Cursor:** `/add-plugin superpowers` or search in the plugin marketplace.

**GitHub Copilot CLI:**
```bash
copilot plugin marketplace add obra/superpowers-marketplace
copilot plugin install superpowers@superpowers-marketplace
```

## Example usage

Once installed, Superpowers is invisible — skills auto-trigger without user invocation. A new session might look like:

```
User: Let's make a React todo list

Agent: [brainstorming skill auto-triggers]
"What problem is this solving? Who are the users? What does 'done' mean here?"
[... spec refinement conversation ...]
[Design saved to design document]

[using-git-worktrees triggers]
[Fresh branch + clean test baseline established]

[writing-plans triggers]
[Tasks created: each with exact file path, complete code, verification step]

[subagent-driven-development triggers]
[Subagent dispatched for Task 1; two-stage review; Task 2; ...]

[test-driven-development enforces RED-GREEN-REFACTOR throughout]
```

## When to use

Superpowers is the right choice when you want your AI coding agent to follow a rigorous, disciplined software engineering methodology without having to enforce it yourself. It is especially valuable for: projects requiring high code quality and real TDD discipline, teams working across multiple AI harnesses (Superpowers installs into all major ones), and developers who want the agent to slow down before coding rather than jumping straight to implementation. It is more prescriptive than command-driven systems like [[gsd-build-get-shit-done]] — if you want the agent to follow a methodology automatically rather than being explicitly invoked, Superpowers is the better fit.

## Maintenance status

190,063 stars, 16,919 forks, Shell primary language, last pushed 2026-05-14. Latest release v5.1.0 (2026-05-04). MIT License. Actively maintained by Jesse Vincent (Jesse@fsck.com) and Prime Radiant; the project explicitly states a 94% PR rejection rate and has detailed contribution guidelines to maintain quality. Available on the official Claude plugin marketplace and multiple third-party harness registries.

## Ecosystem

Superpowers sits at the intersection of two patterns well-represented in this wiki: the SKILL.md-based capability module pattern (shared with [[anthropics-skills]], [[skills.sh]], [[nidhinjs-prompt-master]]) and the subagent orchestration pattern (shared with [[gsd-build-get-shit-done]], [[shareai-lab-learn-claude-code]], [[anthropic.com-managed-agents]]). Its `writing-skills` skill is a meta-skill in the same tradition as `skill-creator` from [[anthropics-skills]]. The `using-superpowers` bootstrap approach — loading a mandatory skill dispatch rule at session start — is related to the behavioral instruction techniques documented in [[forrestchang-andrej-karpathy-skills]] and tested empirically in [[x.com-mnilax-karpathys-4-claude-md-rules-cut-claude-mistakes]].
