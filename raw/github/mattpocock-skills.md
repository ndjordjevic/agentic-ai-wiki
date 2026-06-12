# mattpocock/skills

## Metadata
- Stars: 126,065
- Primary language: Shell
- Default branch: main
- Latest release: none
- License: MIT
- Homepage: (none)
- Fetched: 2026-06-12
- Final URL: https://github.com/mattpocock/skills

## Description
Skills for Real Engineers. Straight from my .claude directory.

## README
<p>
  <a href="https://www.aihero.dev/s/skills-newsletter">
    Skills
  </a>
</p>

# Skills For Real Engineers

[![skills.sh](https://skills.sh/b/mattpocock/skills)](https://skills.sh/mattpocock/skills)

My agent skills that I use every day to do real engineering - not vibe coding.

Developing real applications is hard. Approaches like GSD, BMAD, and Spec-Kit try to help by owning the process. But while doing so, they take away your control and make bugs in the process hard to resolve.

These skills are designed to be small, easy to adapt, and composable. They work with any model. They're based on decades of engineering experience. Hack around with them. Make them your own. Enjoy.

If you want to keep up with changes to these skills, and any new ones I create, you can join ~60,000 other devs on my newsletter: https://www.aihero.dev/s/skills-newsletter

## Quickstart (30-second setup)

1. Run the skills.sh installer:

```bash
npx skills@latest add mattpocock/skills
```

2. Pick the skills you want, and which coding agents you want to install them on. Make sure you select `/setup-matt-pocock-skills`.

3. Run `/setup-matt-pocock-skills` in your agent. It will:
   - Ask you which issue tracker you want to use (GitHub, Linear, or local files)
   - Ask you what labels you apply to tickets when you triage them (`/triage` uses labels)
   - Ask you where you want to save any docs we create

4. Bam - you're ready to go.

## Why These Skills Exist

Built to fix common failure modes with Claude Code, Codex, and other coding agents.

### #1: The Agent Didn't Do What I Want

**The Problem**: The most common failure mode in software development is misalignment. There is a communication gap between you and the agent.

**The Fix**: A **grilling session** — getting the agent to ask you detailed questions about what you're building.

- `/grill-me` — for non-code uses
- `/grill-with-docs` — same as `/grill-me`, but adds more goodies

### #2: The Agent Is Way Too Verbose

**The Problem**: Agents are usually dropped into a project and asked to figure out the jargon as they go, using 20 words where 1 will do.

**The Fix**: A shared language (`CONTEXT.md`) document that helps agents decode the jargon used in the project. Built into `/grill-with-docs`.

### #3: The Code Doesn't Work

**The Problem**: Without feedback on how the code it produces actually runs, the agent flies blind.

**The Fix**: Red-green-refactor loop via `/tdd` skill. Also `/diagnose` for debugging.

### #4: We Built A Ball Of Mud

**The Problem**: Agents accelerate software entropy. Codebases get more complex at an unprecedented rate.

**The Fix**: Caring about code design. `/to-prd`, `/zoom-out`, `/improve-codebase-architecture`.

## Reference

### Engineering

Skills I use daily for code work.

- **diagnose** — Disciplined diagnosis loop for hard bugs and performance regressions: reproduce → minimise → hypothesise → instrument → fix → regression-test.
- **grill-with-docs** — Grilling session that challenges your plan against the existing domain model, sharpens terminology, and updates `CONTEXT.md` and ADRs inline.
- **triage** — Triage issues through a state machine of triage roles.
- **improve-codebase-architecture** — Find deepening opportunities in a codebase, informed by domain language in `CONTEXT.md` and decisions in `docs/adr/`.
- **setup-matt-pocock-skills** — Scaffold the per-repo config (issue tracker, triage label vocabulary, domain doc layout) that other engineering skills consume. Run once per repo.
- **tdd** — Test-driven development with a red-green-refactor loop. Builds features or fixes bugs one vertical slice at a time.
- **to-issues** — Break any plan, spec, or PRD into independently-grabbable GitHub issues using vertical slices.
- **to-prd** — Turn the current conversation context into a PRD and submit it as a GitHub issue.
- **zoom-out** — Tell the agent to zoom out and give broader context or a higher-level perspective on an unfamiliar section of code.
- **prototype** — Build a throwaway prototype to flesh out a design — terminal app for state/business-logic questions, or several radically different UI variations.

### Productivity

General workflow tools, not code-specific.

- **caveman** — Ultra-compressed communication mode. Cuts token usage ~75% by dropping filler while keeping full technical accuracy.
- **grill-me** — Get relentlessly interviewed about a plan or design until every branch of the decision tree is resolved.
- **handoff** — Compact the current conversation into a handoff document so another agent can continue the work.
- **teach** — Teach the user a new skill or concept over multiple sessions, using the current directory as a stateful teaching workspace.
- **write-a-skill** — Create new skills with proper structure, progressive disclosure, and bundled resources.

### Misc

- **git-guardrails-claude-code** — Set up Claude Code hooks to block dangerous git commands (push, reset --hard, clean, etc.) before they execute.
- **migrate-to-shoehorn** — Migrate test files from `as` type assertions to @total-typescript/shoehorn.
- **scaffold-exercises** — Create exercise directory structures with sections, problems, solutions, and explainers.
- **setup-pre-commit** — Set up Husky pre-commit hooks with lint-staged, Prettier, type checking, and tests.

## Docs

### skills/engineering/tdd/SKILL.md
```
---
name: tdd
description: Test-driven development with red-green-refactor loop. Use when user wants to build features or fix bugs using TDD, mentions "red-green-refactor", wants integration tests, or asks for test-first development.
---

# Test-Driven Development

## Philosophy

Core principle: Tests should verify behavior through public interfaces, not implementation details. Code can change entirely; tests shouldn't.

Good tests are integration-style: they exercise real code paths through public APIs. They describe _what_ the system does, not _how_ it does it.

Bad tests are coupled to implementation. They mock internal collaborators, test private methods, or verify through external means.

## Anti-Pattern: Horizontal Slices

DO NOT write all tests first, then all implementation ("horizontal slicing").

Correct approach: Vertical slices via tracer bullets. One test → one implementation → repeat.

WRONG (horizontal): RED: test1, test2, test3... GREEN: impl1, impl2, impl3...
RIGHT (vertical):   RED→GREEN: test1→impl1 / RED→GREEN: test2→impl2 ...

## Workflow

1. Planning: Confirm interface changes, behaviors to test, design for testability. Get user approval.
2. Tracer Bullet: Write ONE test → confirms ONE thing. RED→GREEN.
3. Incremental Loop: For each remaining behavior, one test at a time, minimal code to pass.
4. Refactor: After all tests pass, extract duplication, deepen modules, apply SOLID where natural.

Never refactor while RED. Get to GREEN first.
```

### skills/engineering/grill-with-docs/SKILL.md
```
---
name: grill-with-docs
description: Grilling session that challenges your plan against the existing domain model, sharpens terminology, and updates documentation (CONTEXT.md, ADRs) inline as decisions crystallise.
---

Interview me relentlessly about every aspect of this plan until we reach a shared understanding. Walk down each branch of the design tree, resolving dependencies between decisions one-by-one. For each question, provide your recommended answer. Ask questions one at a time, waiting for feedback.

Domain awareness: look for CONTEXT.md (glossary), docs/adr/ (architecture decisions), CONTEXT-MAP.md (multi-context repos).

During the session:
- Challenge against the glossary: call out term conflicts with CONTEXT.md
- Sharpen fuzzy language: propose precise canonical terms
- Cross-reference with code: surface contradictions between stated intent and implementation
- Update CONTEXT.md inline when a term is resolved (glossary only, no implementation details)
- Offer ADRs sparingly: only when hard to reverse + surprising without context + result of real trade-off
```

## Top-level structure

```
.claude-plugin/      ← Claude Code plugin manifest (plugin.json)
.out-of-scope/       ← ideas/stubs not yet promoted to a named category
CLAUDE.md            ← agent instructions for repo structure conventions
CONTEXT.md           ← project glossary (domain language)
LICENSE              ← MIT
README.md            ← full reference for all published skills
docs/adr/            ← architecture decision records
scripts/             ← tooling scripts (presumably for skill management)
skills/
  engineering/       ← daily code work: tdd, grill-with-docs, diagnose, to-prd, to-issues, triage, zoom-out, improve-codebase-architecture, prototype, setup-matt-pocock-skills
  productivity/      ← non-code workflow: grill-me, caveman, handoff, teach, write-a-skill
  misc/              ← kept but rarely used: git-guardrails-claude-code, migrate-to-shoehorn, scaffold-exercises, setup-pre-commit
  personal/          ← author-specific, not promoted
  in-progress/       ← drafts not ready to ship
  deprecated/        ← no longer used
```
