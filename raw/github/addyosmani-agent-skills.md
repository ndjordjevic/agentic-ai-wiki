# addyosmani/agent-skills

## Metadata
- Stars: 101686
- Primary language: JavaScript
- Default branch: main
- Latest release: 0.6.12 (2026-10-03)
- License: MIT License
- Homepage: https://skills.addy.ie
- Fetched: 2026-10-06
- Final URL: https://github.com/addyosmani/agent-skills

## Description
Production-grade engineering skills for AI coding agents.

## README
# Agent Skills

**Production-grade engineering skills for AI coding agents.**

Skills encode the workflows, quality gates, and best practices that senior engineers use when building software. These ones are packaged so AI agents follow them consistently across every phase of development.

```
  DEFINE          PLAN           BUILD          VERIFY         REVIEW          SHIP
 ┌──────┐      ┌──────┐      ┌──────┐      ┌──────┐      ┌──────┐      ┌──────┐
 │ Idea │ ───▶ │ Spec │ ───▶ │ Code │ ───▶ │ Test │ ───▶ │  QA  │ ───▶ │  Go  │
 │Refine│      │  PRD │      │ Impl │      │Debug │      │ Gate │      │ Live │
 └──────┘      └──────┘      └──────┘      └──────┘      └──────┘      └──────┘
  /spec          /plan          /build        /test         /review       /ship
```

### Commands

9 slash commands map to the development lifecycle; each activates the right skills automatically:

| What you're doing | Command | Key principle |
|-------------------|---------|---------------|
| Define what to build | `/spec` | Spec before code |
| Plan how to build it | `/plan` | Small, atomic tasks |
| Build incrementally | `/build` | One slice at a time |
| Prove it works | `/test` | Tests are proof |
| Set the quality bar | `/constraints` | Decide it once, enforce it everywhere |
| Review before merge | `/review` | Improve code health |
| Audit web performance | `/webperf` | Measure before you optimize |
| Simplify the code | `/code-simplify` | Clarity over cleverness |
| Ship to production | `/ship` | Faster is safer |

`/build auto` generates the plan and implements every task in a single approved pass — the human approves the plan once, then it runs autonomously. Every task is still test-driven and committed individually, and it pauses on failures or risky steps. Skills also activate automatically based on what the agent is doing — designing an API triggers `api-and-interface-design`, building UI triggers `frontend-ui-engineering`, and so on.

### Quick Start

The open [skills CLI](https://github.com/vercel-labs/skills) installs into 70+ agents (Claude Code, Cursor, Codex, Copilot, Cline, and more):

```bash
npx skills add addyosmani/agent-skills            # install all 25 skills
npx skills add addyosmani/agent-skills --list     # browse before installing
npx skills add addyosmani/agent-skills --skill code-review-and-quality
```

> Installing a single skill via `npx` copies only `skills/<name>/`, not the repo-level `references/` directory — the skill still works, but paths to shared checklists are unavailable unless you do a whole-repo integration.

Native integrations exist for: Claude Code (marketplace plugin `/plugin marketplace add addyosmani/agent-skills` + `/plugin install agent-skills@addy-agent-skills`, or local `claude --plugin-dir`), Cursor (`.cursor/skills/` + short policies in `.cursor/rules/*.mdc`), Antigravity CLI (`agy plugin install`), Gemini CLI (`gemini skills install`), Windsurf (rules config), OpenCode (`.opencode/skills/`), GitHub Copilot (agent personas from `agents/` + `.github/copilot-instructions.md`, or the standalone `copilot` CLI as a plugin), Kiro IDE/CLI (`.kiro/skills/`), Codex (native plugin via `codex plugin marketplace add` / `codex plugin add`, invoked with `@skill-name`), and Command Code (`cmd skills add`). Any other agent that accepts Markdown instruction files can use the skills directly as plain files.

### Adoption

The pack ships an **Adoption Guide** (`docs/adoption-guide.md`) covering two paths: full lifecycle adoption from day one on a greenfield project, or an incremental, verification-first rollout for an established codebase.

### All 25 Skills

25 skills total — 24 lifecycle skills plus the `using-agent-skills` meta-skill. Each is a structured workflow with steps, verification gates, and anti-rationalization tables.

**Meta — discover which skill applies:**
- `using-agent-skills` — maps incoming work to the right skill workflow and defines shared operating rules. Use when starting a session or deciding which skill applies.

**Define — clarify what to build:**
- `interview-me` — one-question-at-a-time interview extracting what the user actually wants, to ~95% confidence. Triggered by underspecified asks or "interview me"/"grill me".
- `idea-refine` — structured divergent/convergent thinking turning vague ideas into concrete proposals.
- `spec-driven-development` — write a PRD (objectives, commands, structure, code style, testing, boundaries) before any code. Use when starting a new project, feature, or significant change.
- `constraint-driven-development` — interviews for a quality bar with sane default thresholds, writes CONSTRAINTS.md, places each check by cost, and catches agents silencing checks or skipping tests to get green.

**Plan — break it down:**
- `planning-and-task-breakdown` — decompose specs into small, verifiable tasks with acceptance criteria and dependency ordering.

**Build — write the code:**
- `incremental-implementation` — thin vertical slices: implement, test, verify, commit. Feature flags, safe defaults, rollback-friendly changes.
- `test-driven-development` — Red-Green-Refactor, test pyramid (80/15/5), test sizes, DAMP over DRY, Beyonce Rule, browser testing.
- `context-engineering` — feed agents the right information at the right time: rules files, context packing, MCP integrations.
- `source-driven-development` — ground every framework decision in official documentation; verify, cite sources, flag what's unverified.
- `doubt-driven-development` — adversarial fresh-context review of every non-trivial decision in-flight (CLAIM → EXTRACT → DOUBT → RECONCILE → STOP), with optional user-authorized cross-model escalation. Use for high-stakes (production, security, irreversible) or unfamiliar-code work.
- `frontend-ui-engineering` — component architecture, design systems, state management, responsive design, WCAG 2.1 AA accessibility.
- `api-and-interface-design` — contract-first design, Hyrum's Law, One-Version Rule, error semantics, boundary validation.

**Verify — prove it works:**
- `browser-testing-with-devtools` — Chrome DevTools MCP for live runtime data: DOM inspection, console logs, network traces, performance profiling.
- `debugging-and-error-recovery` — five-step triage (reproduce, localize, reduce, fix, guard), stop-the-line rule, safe fallbacks.

**Review — quality gates before merge:**
- `code-review-and-quality` — five-axis review, change sizing (~100 lines), severity labels (Nit/Optional/FYI), review speed norms, splitting strategies.
- `code-simplification` — Chesterton's Fence, Rule of 500, reduce complexity while preserving exact behavior.
- `security-and-hardening` — OWASP Top 10 prevention, auth patterns, secrets management, dependency auditing, three-tier boundary system.
- `performance-optimization` — measure-first approach: Core Web Vitals targets, profiling workflows, bundle analysis, anti-pattern detection.

**Ship — deploy with confidence:**
- `git-workflow-and-versioning` — trunk-based development, atomic commits, change sizing (~100 lines), commit-as-save-point pattern.
- `ci-cd-and-automation` — Shift Left, Faster is Safer, feature flags, quality gate pipelines, failure feedback loops.
- `deprecation-and-migration` — code-as-liability mindset, compulsory vs advisory deprecation, migration patterns, zombie code removal.
- `documentation-and-adrs` — Architecture Decision Records, API docs, inline documentation standards — document the *why*.
- `observability-and-instrumentation` — structured logging, RED metrics, OpenTelemetry tracing, symptom-based alerting.
- `shipping-and-launch` — pre-launch checklists, feature flag lifecycle, staged rollouts, rollback procedures, monitoring setup.

### Agent Personas

Pre-configured specialist personas for targeted reviews, in `agents/`:

| Agent | Role | Perspective |
|-------|------|-------------|
| `code-reviewer` | Senior Staff Engineer | Five-axis code review with "would a staff engineer approve this?" standard |
| `test-engineer` | QA Specialist | Test strategy, coverage analysis, and the Prove-It pattern |
| `security-auditor` | Security Engineer | Vulnerability detection, threat modeling, OWASP assessment |
| `web-performance-auditor` | Web Performance Engineer | Core Web Vitals audit with Quick/Deep modes and a metric-honesty rule; run via `/webperf` |

`docs/agents.md` covers the decision matrix, orchestration rules, and how personas compose with skills and slash commands.

### Reference Checklists

Quick-reference material in `references/` that skills pull in when needed: `definition-of-done.md`, `testing-patterns.md`, `security-checklist.md`, `performance-checklist.md`, `accessibility-checklist.md`, `observability-checklist.md`, `orchestration-patterns.md`.

### How Skills Work

Every skill follows a consistent anatomy: frontmatter (`name`, `description` with "Use when…" triggers), then Overview, When to Use, Process, Rationalizations, Red Flags, Verification. Key design choices:
- **Process, not prose** — skills are workflows agents follow, not reference docs they read, with steps, checkpoints, and exit criteria.
- **Anti-rationalization** — every skill includes a table of common excuses agents use to skip steps (e.g. "I'll add tests later") with documented counter-arguments.
- **Verification is non-negotiable** — every skill ends with evidence requirements: tests passing, build output, runtime data. "Seems right" is never sufficient.
- **Progressive disclosure** — `SKILL.md` is the entry point; supporting references load only when needed, keeping token usage minimal.

### Project Structure

| Layer / consumer | Repository paths | Purpose |
|---|---|---|
| Shared workflow core | `skills/` (25 skills) | Portable `SKILL.md` workflows used by every integration |
| Shared review material | `agents/` (4 personas), `references/` (7 checklists) | Specialist reviewers and pack-level checklists carried by whole-repo installs |
| Claude Code adapter | `.claude/commands/` (9 commands), `.claude-plugin/`, `hooks/` | Slash-command wrappers, marketplace metadata, lifecycle hooks |
| Gemini CLI adapter | `.gemini/commands/` (9 commands) | Gemini-native TOML command wrappers |
| Antigravity CLI adapter | `commands/` (9 commands), `plugin.json` | Legacy TOML wrappers and the root plugin manifest |
| Codex adapter | `.codex-plugin/`, `.agents/plugins/` | Codex plugin metadata and marketplace registration; Codex consumes `skills/` directly |
| GitHub Copilot CLI adapter | `plugin.json` | Root plugin metadata; Copilot CLI discovers `skills/` by convention |
| Contributor tooling | `scripts/` (13 scripts), `evals/` (25 case files), `.github/workflows/` | Validation, routing evals, and CI |
| Documentation | `docs/` | Universal guidance and per-tool setup guides |

### Why Agent Skills?

AI coding agents default to the shortest path — often skipping specs, tests, security reviews, and the practices that make software reliable. Agent Skills gives agents structured workflows that enforce the same discipline senior engineers bring to production code. Skills bake in best practices from Google's engineering culture (Software Engineering at Google, Google's engineering practices guide) — Hyrum's Law in API design, the Beyonce Rule and test pyramid in testing, change sizing and review speed norms in code review, Chesterton's Fence in simplification, trunk-based development in git workflow, Shift Left and feature flags in CI/CD, and a dedicated deprecation skill treating code as a liability.

### How it compares (docs/comparison.md)

An honest comparison against Superpowers (obra) and Matt Pocock's skills, framed as optimizing for different moments:
- **agent-skills** — organizes the whole product lifecycle (Define, Plan, Build, Verify, Review, Ship) behind a meta-skill router, with review personas, anti-rationalization guards, and an in-repo eval framework checking that skills actually route and behave correctly. 25 skills spanning the whole lifecycle. Entry points are slash commands mapped 1:1 to phases (`/spec` `/plan` `/build` `/test` `/review` `/code-simplify` `/ship`, plus `/webperf`), with `/build auto` for a full-plan autonomous mode.
- **Superpowers** — a complete development *methodology* betting on autonomy and upfront reasoning: Socratic brainstorming → a dated spec → detailed plans written for "an enthusiastic junior engineer with poor taste and no context" → subagent-driven execution with a task reviewer and fix loop → whole-branch review on the most capable model. Git worktrees isolate parallel work; its `writing-skills` skill applies TDD to documentation itself. ~14 skills, deep on the inner build loop, narrower lifecycle coverage.
- **Matt Pocock's skills** — a sharp, opinionated Claude Code toolkit distilled from one expert's daily workflow (~30 skills: engineering/productivity/in-progress/deprecated), with a signature "grill me" interrogation loop and slash commands like `/grill-me`, `/tdd`, `/to-prd`, `/diagnosing-bugs`, `/grill-with-docs`.

None is "best" in the abstract — it depends on the work in front of you; all three share a lot of DNA and are worth learning from.

## Docs
### docs/getting-started.md (excerpt)
agent-skills works with any AI coding agent that accepts Markdown instructions. Each skill is a Markdown file (`SKILL.md`) describing a specific engineering workflow; when loaded into an agent's context, the agent follows the workflow — including verification steps, anti-patterns to avoid, and exit criteria. Skills are not reference docs — they're step-by-step processes the agent follows.

Quick start for any agent: clone the repo, browse `skills/` (each subdirectory has a `SKILL.md` with When to Use / Process / Verification / Common rationalizations / Red flags), then load the skill content into the agent's system prompt, rules file (CLAUDE.md, .cursorrules, etc.), or reference it directly in conversation ("Follow the test-driven-development process for this change").

If the host agent does not route skills natively, load the `using-agent-skills` meta-skill — it contains a flowchart mapping task types to the right skill. If the host already discovers and activates skills from their descriptions, do not also paste `using-agent-skills` into an always-on system prompt — that creates two routers for the same task.

Existing projects need no migration: install the pack from the project root using the normal setup path, and skills activate for matching tasks without requiring a new repository layout. Do not copy the repo's root `AGENTS.md`/`CLAUDE.md` into a consuming project — those configure contributors to agent-skills itself, not downstream users.

### docs/skill-anatomy.md (excerpt)
Every skill lives in its own directory under `skills/<skill-name>/`, with `SKILL.md` as the only required file (`scripts/` and `references/` are optional, added only when needed).

Required frontmatter: `name` (lowercase, hyphen-separated, must match the directory name) and `description` (third-person statement of what the skill does, plus one or more "Use when" trigger conditions, max 1024 characters). Top-level frontmatter keys are limited to the Agent Skills specification fields (`name`, `description`, `license`, `compatibility`, `metadata`, `allowed-tools`); vendor/runtime controls like `model`, `tools`, `max_turns`, or `context` go under `metadata` or a per-agent adapter file — the validator rejects any other top-level key.

Published skill names are compatibility identifiers (e.g. `browser-testing-with-devtools` is the stable upstream name other skills refer to directly); downstream catalogs own their own aliasing.

Recommended (not rigid) section layout: `# Skill Title`, `## Overview`, `## When to Use` (including exclusions), the core process (numbered steps/phases, with ASCII flowcharts for decision points), specific techniques/patterns, rationalizations table, red flags, and verification/evidence requirements.

## Top-level structure
- `.agents/`, `.claude/`, `.claude-plugin/`, `.codex-plugin/`, `.gemini/`, `.opencode/` — per-host adapter directories (marketplace metadata, command wrappers, plugin manifests).
- `.github/` — CI workflows.
- `AGENTS.md`, `CLAUDE.md` — contributor-facing instructions for working on the agent-skills repo itself (not meant to be copied into consuming projects).
- `CONTRIBUTING.md`, `LICENSE`, `README.md`, `plugin.json` — standard repo metadata plus the Copilot CLI/root plugin manifest.
- `agents/` — 4 specialist review personas (`code-reviewer.md`, `security-auditor.md`, `test-engineer.md`, `web-performance-auditor.md`).
- `commands/` — 9 legacy/Antigravity TOML command wrappers (`build.toml`, `code-simplify.toml`, `constraints.toml`, `planning.toml`, `review.toml`, `ship.toml`, `spec.toml`, `test.toml`, `webperf.toml`).
- `docs/` — 17 universal guidance and per-tool setup docs (getting-started, skill-anatomy, adoption-guide, comparison, agents, advanced-per-agent-configuration, other-hosts, and one setup guide per host: antigravity, codex, commandcode, copilot, copilot-cli, cursor, gemini-cli, opencode, windsurf).
- `evals/` — 25 routing/behavior eval case files exercised by CI.
- `hooks/` — Claude Code lifecycle hooks (`SDD-CACHE.md`, `SIMPLIFY-IGNORE.md`, `sdd-cache-pre.sh`, `sdd-cache-post.sh`, `sdd-cache-test.sh`, `session-start.sh`, `session-start-test.sh`, `simplify-ignore.sh`, `simplify-ignore-test.sh`).
- `references/` — 7 shared checklists (definition-of-done, testing-patterns, security-checklist, performance-checklist, accessibility-checklist, observability-checklist, orchestration-patterns).
- `scripts/` — 13 contributor-tooling/validation scripts.
- `skills/` — 24 lifecycle skill directories plus `using-agent-skills` (25 total), each with its own `SKILL.md`.
