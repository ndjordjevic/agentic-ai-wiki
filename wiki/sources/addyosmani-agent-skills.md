---
type: source
category: "Coding-agent harnesses & methodologies"
source_url: https://github.com/addyosmani/agent-skills
tags:
  - agent-skills
  - sdlc-lifecycle
  - anti-rationalization
  - review-personas
  - skill-methodology
  - slash-commands
  - eval-framework
  - multi-harness
related:
  - obra-superpowers
  - mattpocock-skills
  - voltagent-awesome-agent-skills
product: agent-skills
detail_level: standard
created: 2026-10-06
updated: 2026-10-06
---

Agent Skills, created by Addy Osmani, is a pack of 25 production-grade engineering skills (24 lifecycle skills plus a `using-agent-skills` meta-skill) that encode the workflows, quality gates, and best practices senior engineers use, organized around the full software development lifecycle — Define, Plan, Build, Verify, Review, Ship.

_All claims below are sourced from ../../raw/github/addyosmani-agent-skills.md unless otherwise noted._

## What it does

Each skill is a `SKILL.md` Markdown workflow with steps, verification gates, and an anti-rationalization table of excuses agents use to skip discipline (e.g. "I'll add tests later") paired with counter-arguments. Nine slash commands (`/spec`, `/plan`, `/build`, `/test`, `/constraints`, `/review`, `/webperf`, `/code-simplify`, `/ship`) map 1:1 to lifecycle phases and auto-activate the right skills; `/build auto` runs the full generate-plan-then-implement-every-task pass after a single human approval, while still enforcing test-driven, individually committed tasks and pausing on failures.

## Installation

Install via the open [skills CLI](https://github.com/vercel-labs/skills) (`npx skills add addyosmani/agent-skills`, works across 70+ agents) or a native per-host adapter: Claude Code marketplace plugin, Cursor (`.cursor/skills/`), Antigravity CLI (`agy plugin install`), Gemini CLI (`gemini skills install`), Windsurf, OpenCode (`.opencode/skills/`), GitHub Copilot (persona + instructions file, or standalone `copilot` CLI plugin), Kiro IDE/CLI, Codex (native plugin, invoked with `@skill-name`), and Command Code (`cmd skills add`). A single-skill `npx` install copies only `skills/<name>/`, losing access to shared `references/` checklists unless done as a whole-repo integration.

## Key features

- **25 skills across six phases**: `using-agent-skills` (meta-router); Define (`interview-me`, `idea-refine`, `spec-driven-development`, `constraint-driven-development`); Plan (`planning-and-task-breakdown`); Build (`incremental-implementation`, `test-driven-development`, `context-engineering`, `source-driven-development`, `doubt-driven-development`, `frontend-ui-engineering`, `api-and-interface-design`); Verify (`browser-testing-with-devtools`, `debugging-and-error-recovery`); Review (`code-review-and-quality`, `code-simplification`, `security-and-hardening`, `performance-optimization`); Ship (`git-workflow-and-versioning`, `ci-cd-and-automation`, `deprecation-and-migration`, `documentation-and-adrs`, `observability-and-instrumentation`, `shipping-and-launch`).
- **4 review personas** (`agents/`): `code-reviewer` (Senior Staff Engineer, five-axis review), `test-engineer` (QA Specialist, Prove-It pattern), `security-auditor` (OWASP threat modeling), `web-performance-auditor` (Core Web Vitals, Quick/Deep modes, run via `/webperf`).
- **7 shared reference checklists** (`references/`): definition-of-done, testing-patterns, security-checklist, performance-checklist, accessibility-checklist, observability-checklist, orchestration-patterns.
- **In-repo eval framework** (`evals/`, 25 case files) that verifies skills actually route and behave correctly in CI — a differentiator the project calls out explicitly versus comparable packs.
- Engineering principles embedded directly into workflows: Hyrum's Law (API design), the Beyonce Rule and test pyramid (testing), change sizing and review speed norms (code review), Chesterton's Fence (simplification), trunk-based development (git), Shift Left and feature flags (CI/CD), code-as-liability (deprecation).

## Architecture

The portable core is the `skills/` directory (25 `SKILL.md` workflows), consumed directly by hosts like Codex. Per-host adapters live alongside it without altering the core: Claude Code (`.claude/commands/`, `.claude-plugin/`, `hooks/` lifecycle hooks), Gemini CLI (`.gemini/commands/` TOML wrappers), Antigravity CLI (`commands/` TOML wrappers + root `plugin.json`), Codex (`.codex-plugin/`, `.agents/plugins/`), and GitHub Copilot CLI (root `plugin.json`, discovers `skills/` by convention). Each `SKILL.md` follows a consistent anatomy: frontmatter (`name`, `description` with "Use when…" triggers, max 1024 chars) restricted to Agent Skills spec fields, then Overview, When to Use, Process, Rationalizations, Red Flags, Verification — progressive disclosure keeps the entry-point file small while supporting references load on demand.

## Example usage

```bash
# Install all 25 skills into any supported agent
npx skills add addyosmani/agent-skills

# Install a single skill
npx skills add addyosmani/agent-skills --skill test-driven-development

# Claude Code marketplace install
/plugin marketplace add addyosmani/agent-skills
/plugin install agent-skills@addy-agent-skills
```
Once installed, the agent activates skills automatically by task type (e.g. designing an API triggers `api-and-interface-design`), or they can be invoked explicitly via the mapped slash command or by name.

## When to use

Reach for Agent Skills when a team wants one pack covering the *entire* SDLC — from requirements interviews through shipping — with built-in anti-rationalization guards and measurable CI evals proving the skills route correctly, rather than assembling point skills piecemeal. It suits teams that want phase-mapped slash commands (`/spec` → `/plan` → `/build` → `/test` → `/review` → `/ship`) as explicit entry points alongside automatic activation.

## Maintenance status

101,686 stars, 10,662 forks, JavaScript primary language, last pushed 2026-10-03. Latest release 0.6.12 (2026-10-03). MIT License. Built and maintained by Addy Osmani (creator) with collaborators Federico Bartoli and Joan León. (../../raw/github/addyosmani-agent-skills.md)

## Ecosystem

The project's own `docs/comparison.md` positions it against two other skills collections already in this wiki: [[obra-superpowers]], which bets on autonomous, reasoning-heavy runs with subagent-driven execution, git-worktree isolation, and a narrower ~14-skill inner-build-loop focus; and [[mattpocock-skills]], a sharper ~30-skill opinionated toolkit distilled from one engineer's daily Claude Code workflow, centered on a "grill me" interrogation loop. Agent Skills instead organizes the *whole* lifecycle behind a meta-skill router with review personas and an in-repo eval framework. It is also catalogued alongside peers in [[voltagent-awesome-agent-skills]]. Installation is powered by the third-party [skills CLI](https://github.com/vercel-labs/skills) (vercel-labs/skills), which the project recommends as the fastest cross-agent install path.
