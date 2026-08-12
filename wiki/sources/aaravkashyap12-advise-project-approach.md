---
type: source
category: "Agent Skills & plugins ecosystem"
source_url: https://github.com/AaravKashyap12/advise-project-approach
tags: [project-advice, evidence-driven, comparative-analysis, stack-selection, skill, workflow]
related: [uditakhourii-neuroarxiv]
product: advise-project-approach
detail_level: standard
created: 2026-08-12
updated: 2026-08-12
---

`advise-project-approach` is an evidence-driven agent skill that researches comparable projects, analyzes tradeoffs, and provides grounded advice before teams commit to architecture, stack, vendor, or refactor decisions. It operates in three modes—pre-build (planning), mid-build (course correction), and post-build (launch review)—each tied to actual project constraints and real-world comparable implementations rather than generic recommendations.

_All claims below are sourced from ../../raw/github/AaravKashyap12-advise-project-approach.md unless otherwise noted._

## What it does

The skill enforces an evidence-first methodology for project decisions. Before recommending a stack, architecture choice, or vendor, it:

- Captures actual project constraints (scale, team skills, deployment target, timeline, budget)
- Researches comparable real-world projects (star count, maintenance status, adoption signals)
- Identifies what transfers from comparables and what does not
- Evaluates tradeoffs: what you gain, what you give up, what becomes harder later
- Prices out vendor and hosting scenarios with realistic operating-cost breakdowns
- Flags when a recommendation becomes wrong (growth thresholds, team scaling, regulatory changes)
- Delivers a prioritized action plan with evidence citations

The skill is portable across Claude Code, Codex, pi, and other Agent Skills-compatible harnesses via its `SKILL.md` file.

## Installation

**One-line npm install:**

```bash
npx skills@latest add AaravKashyap12/advise-project-approach --skill advise-project-approach
```

**Manual installation** from the packaged `.skill` archive or by copying the skill folder to your agent's local skills directory:

| Harness | Location |
|---|---|
| Claude Code | `~/.claude/skills/advise-project-approach/` |
| Codex | `~/.codex/skills/advise-project-approach/` |
| pi | `~/.agents/skills/advise-project-approach/` or `~/.pi/agent/skills/` |
| Other Agent Skills runners | Point loader at the skill folder or `SKILL.md` |

```bash
cp -r skills/advise-project-approach <your-agent-skill-directory>/
```

## Architecture

The skill separates runtime behavior from distribution metadata:

- **Runtime source:** `skills/advise-project-approach/SKILL.md` — the portable specification agents execute (no dependencies)
- **Compatibility layers:** `.claude-plugin/plugin.json` (Claude), `agents/openai.yaml` (Codex), and packaged `.skill` archive for plugin-aware installers
- **Harness bindings:** agent-specific metadata in the host environment; the core skill remains agnostic

The workflow enforces:

- **Intake gating:** vague project ideas trigger a lightweight question-and-answer phase before research begins
- **Evidence scoping:** research stays bounded (first-pass repo inspection, 200k token guard, external-signal stopping rules)
- **Permission gates:** explicit user approval before running tests, builds, linters, audits, or dependency audits
- **Output shape:** fixed sections (TL;DR, constraints, comparables, tradeoffs, recommendation, failure conditions) ensure structured, auditable advice

## Key features

- **Multi-mode operation:** pre-build (green-field planning), mid-build (live repo analysis and course correction), post-build (launch readiness and gap analysis)
- **Comparable-project research:** discovers and compares real GitHub projects, avoids popularity bias, evaluates adoption signals and maintenance status
- **Vendor and pricing analysis:** distinguishes "free to start" from "cheap to operate," enumerates lock-in and migration costs, surfaces hidden usage limits
- **Stack decision methodology:** constraints → comparables → transferable patterns → tradeoffs → recommendation → failure modes
- **Cross-harness portability:** one `SKILL.md` source runs on Claude, Codex, pi, and generic Agent Skills runners without modification
- **Evidence discipline:** every claim ties back to verified sources (GitHub stars, release dates, repo inspection, pricing pages); no invented metrics or "trending" recommendations
- **Extensible evaluation:** includes reusable test cases, forward-test results, and behavioral rubric for validating and improving skill accuracy

## Example usage

**Pre-build (planning from a rough idea):**
```
You: "I want to build a self-hosted bookmark manager. Solo dev, Python background, want tags and full-text search."

Skill: researches linkding, Linkwarden, LinkAce, Django/Flask docs, SQLite FTS5 vs. Postgres full-text-search, hosting options.

Delivers: TL;DR recommendation (Django + SQLite FTS5), comparable projects with transferable patterns, tradeoffs (simplicity vs. scale), cost breakdown, and when to revisit the decision.
```

**Mid-build (course correction on an in-progress repo):**
```
You: "I'm halfway through building a Node/Express API. Is my approach right?"

Skill: inspects your repo structure, compares against recent Express best practices and comparable projects, identifies what works and what should change, prioritizes fixes by impact (breaking vs. polish).

Delivers: gap analysis, comparable projects doing similar things well, recommended changes ordered by leverage, and what to defer.
```

**Post-build (pre-launch review):**
```
You: "Review my finished project at github.com/owner/repo."

Skill: analyzes the codebase, checks against comparable mature projects, surfaces missing patterns (auth hardening, observability, error handling), flags vendor risks, estimates operating cost.

Delivers: launch readiness assessment, high/medium/low change priorities, cost reality check, and dependencies before production.
```

## When to use

- You have a rough project idea and need to move from vibes to evidence before starting
- Your repo is drifting and you need prioritized course correction (not a linter, not generic advice)
- You are comparing stacks (Django vs. FastAPI), vendors (Supabase vs. Neon vs. PlanetScale), or hosting (self-hosted vs. managed)
- You want evidence before shipping (gap analysis, comparable audits, cost reality)
- You need the agent to explain what not to build yet (constraints, dependencies, sequencing)

## Maintenance status

- **Stars:** 160 (as of 2026-08-12)
- **Latest release:** v0.6.0 (2026-08-11) — cross-harness portability
- **Default branch:** main
- **License:** MIT
- **Repository:** https://github.com/AaravKashyap12/advise-project-approach
- **Last update:** 2026-08-11

The project is actively maintained with a clear release discipline: version-synchronized across `VERSION`, plugin metadata, and README. v0.6.0 adds cross-harness support (pi, generic Agent Skills runners) alongside existing Claude and Codex compatibility.

## Ecosystem

Designed to fit into agent workflows where research, planning, and decision-making happen before or during code work:

- Complements research skills (discovering what exists) with evaluation (deciding whether to use it)
- Bridges generic web search with project-specific constraints and comparable analysis
- Integrates with skill systems (Claude Code, Codex, pi) as a distributable, portable workflow module
- Outputs are audit trails (evidence + decision) rather than stand-alone recommendations

The skill is one piece of an agent stack; pair it with web-search, repo-inspection, cost-modeling, and release-planning skills for full project lifecycle support.

## Documentation

Full skill source, test cases, and examples live in the repository:

- **Skill source:** `skills/advise-project-approach/SKILL.md` — portable runtime specification
- **Repository guidance:** `AGENTS.md` — cross-harness compatibility and maintenance discipline
- **Examples:** `examples/` — pre-build, mid-build, post-build scenarios with real output
- **Evaluation:** `evals/` — behavioral test cases, forward-test results, portability matrix
- **Contributing:** `CONTRIBUTING.md` — guidance for improving evidence discipline and test coverage
- **Changelog:** `CHANGELOG.md` — full version history from v0.1 onward
