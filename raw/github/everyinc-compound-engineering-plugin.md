# EveryInc/compound-engineering-plugin

## Metadata
- Stars: 17151
- Primary language: TypeScript
- Default branch: main
- Latest release: compound-engineering-v3.8.4 (2026-05-22)
- License: MIT
- Homepage: https://every.to/guides/compound-engineering
- Fetched: 2026-05-25
- Final URL: https://github.com/EveryInc/compound-engineering-plugin

## Description
Official Compound Engineering plugin for Claude Code, Codex, Cursor, and more

## README
# Compound Engineering

[![Build Status](https://github.com/EveryInc/compound-engineering-plugin/actions/workflows/ci.yml/badge.svg)](https://github.com/EveryInc/compound-engineering-plugin/actions/workflows/ci.yml)
[![npm](https://img.shields.io/npm/v/@every-env/compound-plugin)](https://www.npmjs.com/package/@every-env/compound-plugin)

AI skills and agents that make each unit of engineering work easier than the last.

## Philosophy

**Each unit of engineering work should make subsequent units easier -- not harder.**

Traditional development accumulates technical debt. Every feature adds complexity. Every bug fix leaves behind a little more local knowledge that someone has to rediscover later. The codebase gets larger, the context gets harder to hold, and the next change becomes slower.

Compound engineering inverts this. 80% is in planning and review, 20% is in execution:

- Plan thoroughly before writing code with `/ce-brainstorm` and `/ce-plan`
- Review to catch issues and calibrate judgment with `/ce-code-review` and `/ce-doc-review`
- Codify knowledge so it is reusable with `/ce-compound`
- Keep quality high so future changes are easy

The point is not ceremony. The point is leverage. A good brainstorm makes the plan sharper. A good plan makes execution smaller. A good review catches the pattern, not just the bug. A good compound note means the next agent does not have to learn the same lesson from scratch.

**Learn more**

- [Full component reference](plugins/compound-engineering/README.md) - all agents and skills
- [Compound engineering: how Every codes with agents](https://every.to/chain-of-thought/compound-engineering-how-every-codes-with-agents)
- [The story behind compounding engineering](https://every.to/source-code/my-ai-had-already-fixed-the-code-before-i-saw-it)

## Workflow

`/ce-strategy` is upstream of the loop -- it captures the product's target problem, approach, persona, metrics, and tracks as a short durable anchor at `STRATEGY.md`. Ideate, brainstorm, and plan read it as grounding when present, so strategy choices flow into feature conception, prioritization, and spec.

The core loop is: brainstorm the requirements, plan the implementation, work through the plan, review the result, compound the learning, then repeat with better context.

Use `/ce-ideate` before the loop when you want the agent to generate and critique bigger ideas before choosing one to brainstorm. It produces a ranked ideation artifact, not requirements, plans, or code.

| Skill | Purpose |
|-------|---------|
| `/ce-strategy` | Create or maintain `STRATEGY.md` -- the product's target problem, approach, persona, key metrics, and tracks. Read as grounding by ideate, brainstorm, and plan |
| `/ce-ideate` | Optional big-picture ideation: generate and critically evaluate grounded ideas, then route the strongest one into brainstorming |
| `/ce-brainstorm` | Interactive Q&A to think through a feature or problem and write a right-sized requirements doc before planning |
| `/ce-plan` | Turn feature ideas into detailed implementation plans |
| `/ce-work` | Execute plans with worktrees and task tracking |
| `/ce-debug` | Systematically reproduce failures, trace root cause, and implement fixes |
| `/ce-code-review` | Multi-agent code review before merging |
| `/ce-compound` | Document learnings to make future work easier |
| `/ce-product-pulse` | Generate a single-page, time-windowed pulse report on usage, performance, errors, and followups. Saves to `docs/pulse-reports/` |

`/ce-product-pulse` is the read-side companion -- a time-windowed report on what users actually experienced and how the product performed over a given window (24h, 7d, etc.), saved to `docs/pulse-reports/` so past pulses form a browseable timeline of user outcomes. The next strategy update and the next brainstorm get real signal to anchor to.

Each cycle compounds: brainstorms sharpen plans, plans inform future plans, reviews catch more issues, patterns get documented.

## Quick Example

A typical cycle starts by turning a rough idea into a requirements doc, then planning from that doc before handing execution to `/ce-work`:

```text
/ce-brainstorm "make background job retries safer"
/ce-plan docs/brainstorms/background-job-retry-safety-requirements.md
/ce-work
/ce-code-review
/ce-compound
```

For a focused bug investigation:

```text
/ce-debug "the checkout webhook sometimes creates duplicate invoices"
/ce-code-review
/ce-compound
```

## Getting Started

After installing, run `/ce-setup` in any project. It checks your environment, installs missing tools, and bootstraps project config.

The `compound-engineering` plugin currently ships 37 skills and 51 agents. See the [full component reference](plugins/compound-engineering/README.md) for the complete inventory.

---

## Install

### Claude Code

```text
/plugin marketplace add EveryInc/compound-engineering-plugin
/plugin install compound-engineering
```

### Cursor

In Cursor Agent chat, install from the plugin marketplace:

```text
/add-plugin compound-engineering
```

Or search for "compound engineering" in the plugin marketplace.

### Codex

Three steps: register the marketplace, install the agent set, then install the plugin through Codex's TUI.

1. **Register the marketplace with Codex:**

   ```bash
   codex plugin marketplace add EveryInc/compound-engineering-plugin
   ```

2. **Install the Compound Engineering agents** (Codex's plugin spec does not register custom agents yet):

   ```bash
   bunx @every-env/compound-plugin install compound-engineering --to codex
   ```

3. **Install the plugin through Codex's TUI:** launch `codex`, run `/plugins`, find the **Compound Engineering** marketplace, select the **compound-engineering** plugin, and choose **Install**. Restart Codex after install completes. Codex's CLI can register marketplaces, but it does not currently expose a plugin-install subcommand for plugins from an added marketplace -- the `/plugins` TUI install is required for CE skills.

### GitHub Copilot

For **VS Code Copilot Agent Plugins**:

1. Run `Chat: Install Plugin from Source` from the VS Code command palette
2. Use `EveryInc/compound-engineering-plugin` for the repo
3. Select `compound-engineering` when VS Code shows the plugins in this repository

For **Copilot CLI**, use:

```text
/plugin marketplace add EveryInc/compound-engineering-plugin
/plugin install compound-engineering@compound-engineering-plugin
```

### Factory Droid

```bash
droid plugin marketplace add https://github.com/EveryInc/compound-engineering-plugin
droid plugin install compound-engineering@compound-engineering-plugin
```

### Qwen Code

```bash
qwen extensions install EveryInc/compound-engineering-plugin:compound-engineering
```

### OpenCode, Pi, Gemini, and Kiro

```bash
bunx @every-env/compound-plugin install compound-engineering --to opencode
bunx @every-env/compound-plugin install compound-engineering --to pi
bunx @every-env/compound-plugin install compound-engineering --to gemini
bunx @every-env/compound-plugin install compound-engineering --to kiro
```

To auto-detect and install to all:

```bash
bunx @every-env/compound-plugin install compound-engineering --to all
```

## Local Development

```bash
bun install
bun test
bun run release:validate
```

## License

[MIT](LICENSE)

## Docs
### plugins/compound-engineering — structure
Subdirectories: `.claude-plugin/`, `.codex-plugin/`, `.cursor-plugin/`, `agents/`, `skills/`
Key files: `AGENTS.md`, `CLAUDE.md`, `CHANGELOG.md`, `LICENSE`, `README.md`

### plugins/compound-engineering/README.md (excerpt)
# Compounding Engineering Plugin

AI-powered development tools that get smarter with every use. Make each unit of engineering work easier than the last.

## Components

| Component | Count |
|-----------|-------|
| Agents | 50+ |
| Skills | 38+ |

### Core Workflow Skills
| Skill | Description |
|-------|-------------|
| `/ce-strategy` | Create or maintain `STRATEGY.md` — product problem, approach, persona, key metrics, and tracks |
| `/ce-ideate` | Optional big-picture ideation: generate and critically evaluate grounded ideas |
| `/ce-brainstorm` | Interactive Q&A to produce a right-sized requirements doc before planning |
| `/ce-plan` | Create structured plans for any multi-step task with automatic confidence checking |
| `/ce-code-review` | Structured code review with tiered persona agents, confidence gating, and dedup pipeline |
| `/ce-work` | Execute work items systematically |
| `/ce-debug` | Systematically find root causes and fix bugs — traces causal chains, forms testable hypotheses |
| `/ce-compound` | Document solved problems to compound team knowledge |
| `/ce-compound-refresh` | Refresh stale or drifting learnings |
| `/ce-optimize` | Run iterative optimization loops with parallel experiments and LLM-as-judge quality scoring |
| `/ce-product-pulse` | Generate time-windowed report on usage, performance, errors, followups |

### Research & Context Skills
| Skill | Description |
|-------|-------------|
| `/ce-sessions` | Ask questions about session history across Claude Code, Codex, and Cursor |
| `/ce-slack-research` | Search Slack for interpreted organizational context |

### Git Workflow Skills
| Skill | Description |
|-------|-------------|
| `ce-commit` | Create a git commit with a value-communicating message |
| `ce-commit-push-pr` | Commit, push, and open a PR with adaptive description |
| `ce-worktree` | Manage Git worktrees for parallel development |

### Review Agents (selected)
| Agent | Description |
|-------|-------------|
| `ce-correctness-reviewer` | Logic errors, edge cases, state bugs |
| `ce-security-reviewer` | Exploitable vulnerabilities with confidence calibration |
| `ce-performance-reviewer` | Runtime performance with confidence calibration |
| `ce-maintainability-reviewer` | Coupling, complexity, naming, dead code |
| `ce-testing-reviewer` | Test coverage gaps, weak assertions |
| `ce-architecture-strategist` | Analyze architectural decisions and compliance |
| `ce-adversarial-reviewer` | Construct failure scenarios to break implementations |

### Research Agents (selected)
| Agent | Description |
|-------|-------------|
| `ce-learnings-researcher` | Search institutional learnings for relevant past solutions |
| `ce-web-researcher` | Iterative web research with structured external grounding |
| `ce-session-historian` | Search prior Claude Code, Codex, and Cursor sessions |
| `ce-git-history-analyzer` | Analyze git history and code evolution |

## Top-level structure
```
.agents/               Agent instruction files (Copilot/generic)
.claude-plugin/        Claude marketplace catalog metadata
.claude/               Claude-specific config
.compound-engineering/ Compound engineering config
.cursor-plugin/        Cursor plugin config
.github/               CI workflows
AGENTS.md              Canonical repo instruction file (authoritative)
CLAUDE.md              Compatibility shim for tools that look for CLAUDE.md
CHANGELOG.md           Pointer to GitHub Releases (canonical release notes)
LICENSE                MIT
PRIVACY.md             Privacy policy
README.md              Primary documentation
SECURITY.md            Security policy
bun.lock               Bun lockfile
docs/                  brainstorms/, plans/, skills/, solutions/, specs/
favicon.png            Branding
package.json           npm package (TypeScript/Bun CLI)
plugins/               compound-engineering/, coding-tutor/ plugin workspaces
scripts/               Release and tooling scripts
src/                   CLI entry point, parsers, converters, target writers
tests/                 Converter, writer, and CLI tests + fixtures
```

## AGENTS.md (key sections)
- **Canonical instruction file**: `AGENTS.md` is authoritative; `CLAUDE.md` is a compatibility shim only.
- **Branching**: feature branch for any non-trivial change; all changes to `main` via pull requests.
- **Testing**: `bun test` after changes affecting parsing, conversion, or output; `bun run release:validate` for plugin/marketplace consistency.
- **Release versioning**: owned by release automation (release-please); `linked-versions` keeps `cli` and `compound-engineering` at the same version. Do not hand-bump.
- **Scratch space**: OS temp by default; `.context/` only for user-curated or repo-inseparable artifacts; `docs/` for durable outputs.
- **Commit conventions**: conventional prefixes (`feat:`, `fix:`, etc.) classified by intent; never use `!` or `BREAKING CHANGE:` without explicit user confirmation.
- **Plugin validation**: use `skill-creator` skill to test agent/skill behavioral changes; plugin agents and skills cache at session start — edits don't propagate within the same Claude Code session.
- **Directory layout**: `src/` CLI, `plugins/` plugin workspaces, `.claude-plugin/` catalog, `tests/` fixtures, `docs/` requirements/plans/solutions/specs.
