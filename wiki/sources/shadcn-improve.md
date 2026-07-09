---
type: source
category: "Coding agents, IDEs & dev environments"
source_url: https://github.com/shadcn/improve
tags:
  - code-audit
  - codebase-planning
  - agentic-coding
  - claude-code-plugin
  - agent-skills
  - cost-optimization
  - spec-driven-development
  - multi-agent-orchestration
related:
  - obra-superpowers
  - gsd-build-get-shit-done
  - seangeng.com-plan-optimizer
  - everyinc-compound-engineering-plugin
  - mattpocock-skills
product: improve
detail_level: standard
created: 2026-06-12
updated: 2026-06-12
---

`shadcn/improve` is a Claude Code plugin skill (1,977 stars, MIT, v1.0.0) that separates the two cognitive tasks in AI-assisted development — *judging what's worth doing* and *doing it* — across models priced for each job. The capable model audits the codebase and writes self-contained, machine-checkable plans; cheaper models execute. The skill never touches source code itself.

_All claims below are sourced from ../../raw/github/shadcn-improve.md unless otherwise noted._

## What it does

`/improve` maps a codebase (stack, conventions, build/test/lint commands), fans out parallel subagents across nine audit categories (correctness, security, performance, test coverage, tech debt, dependencies, DX, docs, and feature direction), vets every finding by re-reading cited file locations to prune false positives, and delivers a prioritized findings table ordered by leverage (impact ÷ effort × confidence). The user selects findings; the skill writes one self-contained plan file per finding into `plans/` with an index and dependency graph.

## Installation

```bash
npx skills add shadcn/improve
```

Works in any agent that supports the Agent Skills / SKILL.md format (Claude Code, Cursor, Codex, and compatible runtimes). The plugin manifest is registered at `.claude-plugin/plugin.json` for the Claude Code marketplace.

## Key features

- **Nine audit categories** — correctness, security, performance, test coverage, tech debt, dependency migrations, DX, docs, and feature direction; each finding carries `file:line` evidence, impact, effort, and confidence.
- **Vet step** — the advisor re-reads every cited location before surfacing findings; false positives are dropped, not just filtered.
- **Executable plans** — each plan inlines current code excerpts, exact file paths, repo conventions with an exemplar, verified commands as step-gating checks, explicit out-of-scope lists, and STOP conditions. Stamped against the git commit it was written on so executors run a drift check before touching code.
- **`/improve execute <plan>`** — spawns a cheaper model subagent in an isolated git worktree, reviews the diff against plan intent (re-runs all done criteria, checks scope compliance), and returns a verdict: approve, send back for revision (max 2 rounds), or block.
- **`/improve reconcile`** — maintenance sweep: verify DONE plans still hold, investigate BLOCKED ones and rewrite around obstacles, refresh drifted plans, retire findings fixed independently.
- **`--issues` flag** — publish plans as GitHub issues with the same self-contained body.
- **Scoped modes** — `/improve quick` (cheap hotspot pass), `/improve deep` (exhaustive), `/improve branch` (diff-only), `/improve security` and other focused audits, `/improve next` (feature suggestions, evidence-required, no idea-slop), `/improve plan <description>` (skip audit, spec one thing), `/improve review-plan <file>` (critique an existing plan).
- **Hard rules** — the skill never modifies source code, never runs mutating commands, never reproduces secret values.

## Architecture

The skill implements a four-stage pipeline in `skills/improve/SKILL.md` with supporting reference files in `skills/improve/references/`:

1. **Recon** — maps stack, conventions, and the verified build/test/lint commands that become gates in every plan.
2. **Audit** — parallel subagent fan-out across nine categories; each subagent operates independently with no shared state.
3. **Vet** — the advisor agent re-reads every cited file:line location, drops unsubstantiated claims, corrects wrong attributions, records rejections so they don't resurface.
4. **Plan** — one Markdown file per selected finding, written to `plans/`, with an index ordering by dependency and priority.

The executor subagent pattern (step 5 of the typical workflow) runs in a git worktree isolation boundary, receives the plan as its sole context, and is reviewed by the advisor model — not the user — before the result is surfaced. This mirrors the GAN-inspired evaluator pattern documented in the Anthropic managed-agents harness.

## Example usage

```
/improve                        # full audit → findings table → user selects → plans written
/improve quick                  # cheap hotspot pass only
/improve branch                 # scope to current branch diff only
/improve security               # focused security audit
/improve plan "extract shadow config resolution into shared utility"
/improve execute 001            # dispatch cheaper model, review result
/improve reconcile              # refresh backlog after several sessions
```

Example output plan: `examples/001-extract-shadow-config-resolution.md` — a plan against shadcn/ui that inlines the duplicated shadow-config code from `search.ts` and `view.ts`, exact refactor steps, the repo's own test/lint commands as verification gates, and STOP conditions for when file state doesn't match expectations.

## Maintenance status

1,977 stars; MIT license; active as of June 2026 (pushed 2026-06-10). No formal releases; distributed through the Agent Skills ecosystem. Author is shadcn (creator of shadcn/ui, the dominant React component library).
