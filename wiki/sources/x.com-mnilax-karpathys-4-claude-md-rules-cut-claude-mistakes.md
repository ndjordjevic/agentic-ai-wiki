---
type: source
source_url: https://x.com/mnilax/status/2053116311132155938?s=43&t=5l2OHSF10JbahgpENs1smw
tags: [claude-md, behavioral-rules, agent-orchestration, claude-code, token-budgets, checkpointing, test-quality, coding-conventions]
related: [forrestchang-andrej-karpathy-skills, anthropics-skills, shareai-lab-learn-claude-code]
product: x
detail_level: standard
created: 2026-05-11
updated: 2026-05-11
---

An X article by Mnimiy (@mnilax) reporting on 6 weeks of empirical testing of Andrej Karpathy's 4-rule CLAUDE.md template across 30 codebases, then extending it with 8 additional rules targeting the May 2026 Claude Code landscape — agent orchestration, token budgets, multi-step checkpointing, test intent, convention conformance, and loud failure signaling. The 12-rule template brings the mistake rate from 41% down to 3% while preserving ~76% compliance.

_All claims below are sourced from ../../raw/web/x.com-mnilax-karpathys-4-claude-md-rules-cut-claude-mistakes.md unless otherwise noted._

## What it does

The article validates and extends the [[forrestchang-andrej-karpathy-skills]] CLAUDE.md template. The original 4 rules — Think Before Coding, Simplicity First, Surgical Changes, Goal-Driven Execution — addressed Claude's January 2026 failure modes (silent assumptions, over-engineering, untargeted edits, vague success criteria). The author tested these on 30 codebases over 6 weeks, confirmed they cut mistakes from ~41% to ~11%, then identified 8 new failure modes specific to May 2026's agent-driven workflows and added corresponding rules. The combined 12-rule CLAUDE.md is provided as a ready-to-paste template.

## Key features

**The 8 new rules and the failure modes they close:**

- **Rule 5 — Model for judgment calls only:** Use Claude for classification, drafting, summarization, extraction. Never for routing, retries, or deterministic transforms. Prevents flaky nondeterministic behavior in logic that should be plain code.
- **Rule 6 — Token budgets are not advisory:** Hard limits of 4,000 tokens per task and 30,000 per session. If the budget is approached, summarize and start fresh rather than silently overrunning. Prevents context drift and circular debugging loops.
- **Rule 7 — Surface conflicts, don't average them:** When two codebase patterns contradict, pick one (the more recent/tested), explain why, and flag the other for cleanup. Prevents incoherent "average" code that satisfies both patterns and breaks both.
- **Rule 8 — Read before you write:** Before adding code, read the file's exports, immediate caller, and shared utilities. Prevents duplicate implementations and import-order bugs from writing next to code that was never read.
- **Rule 9 — Tests verify intent, not behavior:** Tests must encode WHY behavior matters, not just WHAT it does. A test that cannot fail when business logic changes is not a real test. Prevents hollow passing test suites that miss production regressions.
- **Rule 10 — Checkpoint after every significant step:** After each step in a multi-step task, summarize what was done, what was verified, and what remains. Prevents bad state from compounding across subsequent steps in long refactors.
- **Rule 11 — Match codebase conventions:** Conformance over taste inside an existing codebase. If a convention is genuinely harmful, surface it rather than forking it silently. Prevents pattern fragmentation in codebases with established styles.
- **Rule 12 — Fail loud:** "Completed," "tests pass," and "feature works" are wrong if anything was skipped silently. Default to surfacing uncertainty. Prevents silent partial successes (skipped migration records, untested edge cases) that surface days later.

**Empirical findings:**
- 4-rule template: mistake rate ~41% → ~11%; compliance 78%
- 12-rule template: mistake rate ~41% → ~3%; compliance 76%
- Adding 8 rules added almost no compliance overhead (78% → 76%) but cut mistakes by another 8 points
- Compliance drops sharply past 14 rules (76% → 52% at 18 rules); 200-line ceiling is confirmed

## Architecture and concepts

**Where Karpathy's 4 rules are silent (the 4 gaps):**

1. **Long-running agent tasks** — Rules 1–4 target single code-writing moments. They say nothing about multi-step pipelines: no budget rule, no checkpoint rule, no fail-loud rule. Pipelines drift without these.
2. **Multi-codebase consistency** — "Match existing style" assumes one style. In a monorepo with 12 services, Claude picks randomly or averages. Rules 7 and 11 address this.
3. **Test quality** — Goal-Driven Execution treats "tests pass" as success but doesn't require tests to be meaningful. Rule 9 closes this.
4. **Production vs. prototype** — Simplicity First overfires on early-stage exploratory code that legitimately needs scaffolding to discover a direction.

**CLAUDE.md compliance model:**
- CLAUDE.md is advisory: ~80% compliance at any rule count
- Past 200 lines, compliance drops sharply (important rules get buried)
- Rules outperform examples (examples cost ~3× more context, cause overfitting)
- Imperative rules ("state assumptions explicitly") outperform identity prompts ("be senior")
- Capability-agnostic phrasings ("match the codebase's enforced style") survive missing tooling better than tool-specific rules ("use eslint")

## Installation

Two-step setup at your repo root:

```bash
# 1. Append Karpathy's 4-rule baseline to your CLAUDE.md
curl https://raw.githubusercontent.com/forrestchang/andrej-karpathy-skills/main/CLAUDE.md >> CLAUDE.md

# 2. Paste rules 5–12 from the template below into the same file
```

The `>>` matters — it appends to your existing CLAUDE.md instead of overwriting any project-specific rules already there. Add project-specific rules (stack, test commands, error patterns) below the 12. Keep the total under 200 lines — past that, compliance falls off sharply.

## Full 12-rule CLAUDE.md (copy-paste ready)

```markdown
# CLAUDE.md — 12-rule template

These rules apply to every task in this project unless explicitly overridden.
Bias: caution over speed on non-trivial work. Use judgment on trivial tasks.

## Rule 1 — Think Before Coding
State assumptions explicitly. If uncertain, ask rather than guess.
Present multiple interpretations when ambiguity exists.
Push back when a simpler approach exists.
Stop when confused. Name what's unclear.

## Rule 2 — Simplicity First
Minimum code that solves the problem. Nothing speculative.
No features beyond what was asked. No abstractions for single-use code.
Test: would a senior engineer say this is overcomplicated? If yes, simplify.

## Rule 3 — Surgical Changes
Touch only what you must. Clean up only your own mess.
Don't "improve" adjacent code, comments, or formatting.
Don't refactor what isn't broken. Match existing style.

## Rule 4 — Goal-Driven Execution
Define success criteria. Loop until verified.
Don't follow steps. Define success and iterate.
Strong success criteria let you loop independently.

## Rule 5 — Use the model only for judgment calls
Use me for: classification, drafting, summarization, extraction.
Do NOT use me for: routing, retries, deterministic transforms.
If code can answer, code answers.

## Rule 6 — Token budgets are not advisory
Per-task: 4,000 tokens. Per-session: 30,000 tokens.
If approaching budget, summarize and start fresh.
Surface the breach. Do not silently overrun.

## Rule 7 — Surface conflicts, don't average them
If two patterns contradict, pick one (more recent / more tested).
Explain why. Flag the other for cleanup.
Don't blend conflicting patterns.

## Rule 8 — Read before you write
Before adding code, read exports, immediate callers, shared utilities.
"Looks orthogonal" is dangerous. If unsure why code is structured a way, ask.

## Rule 9 — Tests verify intent, not just behavior
Tests must encode WHY behavior matters, not just WHAT it does.
A test that can't fail when business logic changes is wrong.

## Rule 10 — Checkpoint after every significant step
Summarize what was done, what's verified, what's left.
Don't continue from a state you can't describe back.
If you lose track, stop and restate.

## Rule 11 — Match the codebase's conventions, even if you disagree
Conformance > taste inside the codebase.
If you genuinely think a convention is harmful, surface it. Don't fork silently.

## Rule 12 — Fail loud
"Completed" is wrong if anything was skipped silently.
"Tests pass" is wrong if any were skipped.
Default to surfacing uncertainty, not hiding it.
```

## When to use

Apply the full 12-rule template when running multi-step agent workflows, working across multiple codebases or services, maintaining production systems where silent failures are expensive, or debugging long-running Claude Code sessions. Drop individual rules that don't map to observed failure modes — a 6-rule CLAUDE.md tuned to real mistakes beats a 12-rule one with 6 unused rules.

The 4-rule [[forrestchang-andrej-karpathy-skills]] baseline remains sufficient for short-session, single-file, autocomplete-style interactions where agent orchestration problems don't arise.

## Ecosystem

The article sits at the intersection of several sources in this wiki. It validates [[forrestchang-andrej-karpathy-skills]] (the 4-rule template it extends) and connects to [[anthropics-skills]] (Anthropic's official skills ecosystem for Claude Code) and [[shareai-lab-learn-claude-code]] (the harness engineering curriculum that articulates why agent behavior is shaped by environment and instructions). The empirical testing methodology — 50 tasks × 30 codebases × 6 weeks — makes this one of the more data-grounded CLAUDE.md practice guides in the ecosystem.
