---
type: source
category: "Coding-agent harnesses & methodologies"
source_url: https://x.com/0xCodez/status/2062127385923776831?s=20
tags:
  - dynamic-workflows
  - claude-code
  - subagent-orchestration
  - ultracode
  - adversarial-verification
  - workflow-patterns
  - token-budgets
  - prompt-injection-quarantine
related:
  - how-claude-code-works-in-large-codebases
  - shareai-lab-learn-claude-code
  - 9d5bzxVsocw-anthropic-just-dropped-the-new-blueprint
  - x.com-mnilax-karpathys-4-claude-md-rules-cut-claude-mistakes
  - Chachamaru127-claude-code-harness
  - anthropics-skills
product: how-to-master-dynamic-workflows-claude-code-6-patterns-14-steps
detail_level: standard
created: 2026-07-08
updated: 2026-07-08
---

An X article by Codez (@0xCodez) providing a practitioner-oriented guide to Claude Code Dynamic Workflows (shipped May 28, 2026): the mental model for when one context window breaks down, six orchestration patterns Anthropic engineers use (classify-and-act, fan-out-and-synthesize, adversarial verification, generate-and-filter, tournament, loop until done), a use-case composition matrix, and practical controls (`ultracode`, `/goal`, `/loop`, token budgets, quarantine for untrusted inputs, saving workflows as Skills).

_All claims below are sourced from ../../raw/web/how-to-master-dynamic-workflows-claude-code-6-patterns-14-steps.md unless otherwise noted._

## What it does

The article explains Dynamic Workflows — Claude Code's feature where Claude writes a bespoke JavaScript harness on the fly to spawn and coordinate subagents for tasks that exceed a single context window. Unlike static workflows built with the Claude Agent SDK or `claude -p`, dynamic workflows tailor the orchestration to the specific task and codebase context. The guide maps Anthropic's launch writing into actionable patterns for migrations, deep research, triage, root-cause investigation, sorting at scale, and lightweight evals.

## Key features

**Three structural advantages over the default harness:**

- Per-agent isolation — each subagent gets its own context window and focused goal
- Per-agent model choice — Opus for hard reasoning, Haiku for cheap exploration, Sonnet for the middle
- Per-agent isolation level — worktree (isolated git checkout) or remote (no checkout)

**Six orchestration patterns:**

1. **Classify-and-act** — route heterogeneous tasks to different agents or models based on a classifier's output
2. **Fan-out-and-synthesize** — parallel agents on independent work items, then a barrier merge into one report
3. **Adversarial verification** — separate verifier agents with no exposure to the original work (fixes self-preferential bias)
4. **Generate-and-filter** — produce many candidates, then score/verify before committing to one
5. **Tournament** — pairwise comparative judgment instead of absolute scoring (essential for 1,000+ items or taste-based ranking)
6. **Loop until done** — spawn agents until a stop condition is met (no new findings, zero errors, theory verified)

**Activation and controls:**

- Trigger via `ultracode` keyword, natural-language "make a workflow that…", or `/effort ultracode` for session-wide auto-orchestration
- `/deep-research` as a zero-setup entry point to experience workflows
- `/goal` for hard completion requirements; `/loop` for recurring schedules
- Explicit token budgets in prompts ("use 10k tokens") to cap runaway cost
- Save with `s` in the workflow menu to `~/.claude/workflows`; ship as a Skill with template semantics

## Architecture and concepts

**Three failure modes workflows structurally prevent** (from Anthropic launch writing):

- **Agentic laziness** — declaring done after partial progress on multi-part tasks
- **Self-preferential bias** — verifier favoring its own prior output
- **Goal drift** — lossy compaction erasing constraints across many turns

**Core primitives:**

- `agent(prompt, opts?)` — spawn a subagent; optional `schema` for structured JSON output
- `parallel(thunks)` — fan-out with synchronization barrier (wait for all before continuing)
- `pipeline(items, …stages)` — streaming stages (item A can be in stage 3 while item B is in stage 1)

Decision rule: need all results before the next step? → `parallel`. Otherwise → `pipeline` (cheaper, faster).

**Quarantine pattern:** for workflows processing untrusted content (support tickets, scraped pages, user feedback), read-only agents ingest the content; separate privileged agents act — preventing prompt injection from reaching high-privilege operations.

**Static vs dynamic:** static SDK workflows are generic and conservative; dynamic workflows read your actual code and shape themselves (e.g., check billing code against provider docs, run adversarial "why not migrate" pass).

## Main APIs

The workflow runtime exposes JavaScript orchestration primitives used inside generated harness files:

```javascript
const reviews = await parallel(
  files.map(file => () => agent(
    `Review ${file} for security issues`,
    { model: "haiku", schema: IssueList }
  ))
)

const report = await agent(
  `Merge these reviews into one prioritized report:\n${JSON.stringify(reviews)}`,
  { model: "opus" }
)
```

CLI controls referenced throughout: `ultracode`, `/effort ultracode`, `/goal`, `/loop`, `/deep-research`, `/workflows` (monitoring dashboard), `/config` (enable on Pro). Requirements: Claude Code CLI v2.1.154+, paid plan.

## When to use

Reach for a workflow when the task is long-running, massively parallel, highly structured, or adversarial — and suffers from agentic laziness, self-preference, or goal drift in a single session. The article's use-case matrix pairs patterns to scenarios:

- Migrations/refactors → fan-out + adversarial verification + loop until done
- Deep research → fan-out + adversarial verification + synthesize
- Sorting 1,000+ items → tournament (never absolute scoring)
- Triage at scale → classify-and-act + `/loop`
- Taste-based exploration → generate-and-filter + tournament

Do **not** use workflows for tasks a regular Claude Code session finishes in five minutes. Most traditional coding tasks don't need a panel of 5 reviewers. Set explicit token budgets — ambitious workflows can cost 5–10× expectations without caps.

## Ecosystem

Dynamic Workflows sit atop Claude Code's default harness, complementing [[how-claude-code-works-in-large-codebases]] enterprise practices (CLAUDE.md, skills, hooks) and the harness-design patterns in [[9d5bzxVsocw-anthropic-just-dropped-the-new-blueprint]]. Saved workflows can be packaged as [[anthropics-skills]] for distribution. The article references Anthropic's own custom harnesses (Research, Code Review, agent teams) that Dynamic Workflows generalize. Adjacent methodology sources: [[shareai-lab-learn-claude-code]] (harness engineering from scratch), [[x.com-mnilax-karpathys-4-claude-md-rules-cut-claude-mistakes]] (CLAUDE.md behavioral rules), and [[Chachamaru127-claude-code-harness]] (Plan→Work→Review contract harness). Official references: [Anthropic blog on dynamic workflows](https://claude.com/blog/a-harness-for-every-task-dynamic-workflows-in-claude-code), [Claude Code docs](https://code.claude.com/docs/en/workflows).
