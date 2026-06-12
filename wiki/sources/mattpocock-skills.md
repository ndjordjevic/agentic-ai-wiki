---
type: source
source_url: https://github.com/mattpocock/skills
tags:
  - agent-skills
  - engineering-process
  - tdd
  - grilling-technique
  - domain-language
  - claude-code-skills
  - coding-agent-workflow
  - skills-sh
related:
  - anthropics-skills
  - skills.sh
  - seangeng.com-plan-optimizer
  - obra-superpowers
  - gsd-build-get-shit-done
  - forrestchang-andrej-karpathy-skills
  - shadcn-improve
product: skills
detail_level: standard
created: 2026-06-12
updated: 2026-06-12
---

Matt Pocock's opinionated skill collection for real-world engineering with AI coding agents, distributed via [skills.sh](https://skills.sh/mattpocock/skills) with 126k+ stars. Built around four diagnosed failure modes of AI-assisted development — misalignment, verbosity, broken code, and software entropy — each addressed by a concrete, composable skill that can be installed with `npx skills@latest add mattpocock/skills`. The philosophy explicitly rejects "process-owning" frameworks (GSD, BMAD, Spec-Kit) in favour of small, hackable skills that keep the developer in control.

_All claims below are sourced from ../../raw/github/mattpocock-skills.md unless otherwise noted._

## What it does

A curated set of agent skills organized into three active buckets — `engineering/` (10 skills for daily code work), `productivity/` (5 general workflow tools), and `misc/` (4 utility skills) — plus `personal/`, `in-progress/`, and `deprecated/` buckets not promoted to end users. Skills are installed per-repo via the skills.sh CLI, and most engineering skills depend on a one-time `/setup-matt-pocock-skills` run that scaffolds the issue tracker config, triage label vocabulary, and domain doc layout.

## Installation

```bash
npx skills@latest add mattpocock/skills
```

Select desired skills and target agents (Claude Code, Codex, etc.), then run `/setup-matt-pocock-skills` once per repo to configure issue tracking (GitHub Issues, Linear, or local files), triage labels, and doc locations.

## Key features

**Engineering skills:**
- `/grill-with-docs` — relentless interview against the project's domain model; updates `CONTEXT.md` and creates ADRs inline; the primary alignment tool before any coding session
- `/tdd` — red-green-refactor loop enforcing vertical slices (one test → one implementation); explicitly guards against "horizontal slicing" (writing all tests before any implementation)
- `/diagnose` — disciplined debugging loop: reproduce → minimise → hypothesise → instrument → fix → regression-test
- `/to-prd` — synthesises conversation context into a PRD GitHub issue without re-interviewing
- `/to-issues` — breaks a PRD into independently-grabbable vertical-slice GitHub issues
- `/triage` — state-machine issue triage with configurable label vocabulary
- `/improve-codebase-architecture` — finds "deepening opportunities" informed by `CONTEXT.md` and `docs/adr/`; recommended to run every few days
- `/zoom-out` — prompts the agent to explain unfamiliar code in the broader system context
- `/prototype` — throwaway prototyping: terminal app (state/logic) or multi-variation UI toggle on one route

**Productivity skills:**
- `/grill-me` — same relentless interview as `/grill-with-docs` but without domain doc updates; for non-code uses
- `/caveman` — ultra-compressed communication mode, ~75% token reduction, full technical accuracy preserved
- `/handoff` — compact conversation into a handoff document for another agent to continue
- `/teach` — teach the user a new skill or concept over multiple sessions, using the current directory as a stateful teaching workspace
- `/write-a-skill` — create new skills with proper structure, progressive disclosure, and bundled resources

**Misc skills:**
- `/git-guardrails-claude-code` — sets up Claude Code hooks to block dangerous git commands (push, reset --hard, clean) before they execute
- `/migrate-to-shoehorn` — migrates test files from `as` type assertions to @total-typescript/shoehorn
- `/scaffold-exercises` — creates exercise directory structures with sections, problems, solutions, and explainers
- `/setup-pre-commit` — sets up Husky pre-commit hooks with lint-staged, Prettier, type checking, and tests

## Architecture

The repo follows a bucket structure enforced by `CLAUDE.md`: every published skill must appear in the top-level `README.md` and in `.claude-plugin/plugin.json`; skills in `personal/`, `in-progress/`, or `deprecated/` must not. Each skill is a directory containing a `SKILL.md` (frontmatter-described trigger + instructions) and optional bundled resource files (e.g. `tdd/` has `tests.md`, `mocking.md`, `deep-modules.md`, `interface-design.md`, `refactoring.md`). The `.claude-plugin/` manifest enables IDE/agent plugin discovery. The skills are designed to compose: `/grill-with-docs` feeds a shared `CONTEXT.md` glossary that subsequent skills (`/tdd`, `/to-prd`, `/improve-codebase-architecture`) reference for consistent terminology.

## Example usage

Typical session flow per the README:
1. `/grill-with-docs` — align on what to build, crystallise domain terms in `CONTEXT.md`
2. `/to-prd` — turn the discussion into a GitHub issue PRD
3. `/to-issues` — break the PRD into vertical-slice issues
4. `/tdd` — implement one issue at a time with red-green-refactor
5. `/improve-codebase-architecture` — run periodically to counter entropy

## Maintenance status

126,065 stars, 11,013 forks, MIT license. Last pushed 2026-06-10. No formal releases (rolling `main` branch). Active newsletter with ~60,000 subscribers at aihero.dev.

## Ecosystem

Distributed via [skills.sh](https://skills.sh/mattpocock/skills) — the same platform used by `[[anthropics-skills]]`. Works with Claude Code, Codex, and other coding agents. Referenced alongside `[[obra-superpowers]]` and `[[gsd-build-get-shit-done]]` as alternatives that differ in approach: GSD/BMAD/Spec-Kit own the process end-to-end, while these skills stay small and composable.
