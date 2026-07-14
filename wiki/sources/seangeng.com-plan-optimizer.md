---
type: source
category: "Spec-driven dev, planning & tasks"
source_url: https://seangeng.com-plan-optimizer/freebies/plan-optimizer
tags: [claude-code-skill, plan-optimization, iterative-refinement, rubric-scoring, hill-climbing, best-of-n, agentic-tools, plateau-detection]
related: [obra-superpowers, anthropics-skills, mattpocock-skills, shadcn-improve, skills.sh, q00-ouroboros, chaseai-yt-grill-me-codex]
product: seangeng
detail_level: standard
created: 2026-06-12
updated: 2026-07-14
---

Sean Geng's plan-optimizer is a downloadable Claude Code skill that treats planning as a search problem: generate an initial plan, score it against a weighted rubric, identify the highest-impact weaknesses, rewrite to address them, and halt when scores stop advancing beyond a meaningful margin. Built and dog-fooded by Sean Geng (co-founder & CTO at B3, formerly Coinbase engineering), the skill is available via a single curl install to `~/.claude/skills/plan-optimizer/` and activates whenever a user asks to improve, harden, or stress-test any plan — project launches, code migrations, research initiatives, strategy documents, or any other high-stakes planning artifact.

_All claims below are sourced from ../../raw/web/seangeng.com-plan-optimizer.md unless otherwise noted._

## What it does

The plan-optimizer skill installs into Claude Code and drives an iterative plan-improvement loop. The user supplies a plan and (optionally) a domain context; the skill builds a scoring rubric, generates an initial scored plan, then cycles through critique → targeted rewrite → score comparison steps until the score plateaus. The loop terminates automatically: new versions are accepted only when they exceed the previous score by a configurable margin, preventing noise-driven churn. The final output is the highest-scoring plan, its per-criterion breakdown, the full score trajectory across rounds, and a summary of what substantively changed between the first and final version.

## Key features

- **Rubric-first design** — the rubric is built before any writing starts, making the quality ceiling explicit and preventing the model from optimizing for the wrong thing.
- **Critique-then-rewrite cycle** — weaknesses are identified against the rubric, ranked by impact, and addressed in targeted rewrites rather than vague "make it better" loops.
- **Margin-based acceptance** — new plan versions replace the best only when they exceed the previous score by a meaningful threshold, filtering out noise improvements.
- **Plateau detection** — the loop exits when score gains consistently fall below the margin, telling the user when more iteration is just noise.
- **Two search strategies** — hill-climbing (incremental per-round improvements) and best-of-N (multiple structurally distinct variants generated simultaneously when hill-climbing stalls in a local optimum).
- **Reward-hacking guard** — the skill explicitly warns against gaming metrics without genuine plan improvement, a common failure mode in optimization loops.
- **Single-command install** — `curl`-based install to `~/.claude/skills/plan-optimizer/`; no configuration beyond invoking Claude Code.

## Architecture and concepts

The core insight is that planning is a search problem, not a drafting problem. The three separable subtasks — scoring, critique, and rewriting — are kept distinct so each can be improved independently. Separation also prevents the common failure mode where the model that wrote the plan also evaluates it (self-serving scores).

The rubric acts as the search objective. Its quality determines the ceiling of the output: a vague rubric produces vague plans regardless of how many iterations run. Geng recommends investing heavily in rubric construction before the loop starts.

The margin-based acceptance rule is the key convergence mechanism. Without it, stochastic variation in LLM outputs can produce endless micro-improvements that do not represent real progress. The plateau detector measures the running gain across recent rounds; once gains stabilize below the threshold, the loop exits.

When hill-climbing stalls (a sign of a local optimum), the skill shifts to best-of-N generation — producing several structurally different plan variants in parallel and selecting the highest-scoring one as the new starting point. Geng notes that using a more capable model for the best-of-N step provides disproportionate leverage, as the stronger model both generates better alternatives and perceives flaws that weaker scorers miss.

## Main APIs

The skill installs as a Claude Code skill directory. Invocation is natural-language: ask Claude Code to "improve this plan," "harden this plan," or "stress-test this plan" with the plan in context. The skill's trigger description covers those phrases. No programmatic API surface; the interface is the Claude Code skill activation mechanism.

## When to use

Use the plan-optimizer when a plan needs maximum quality before execution — project launch plans, code migration strategies, research outlines, strategy documents, or any artifact where a suboptimal plan has high downstream cost. The skill is especially valuable when you have a clear rubric for what "good" means but lack the time or discipline to manually iterate, or when you want an objective stopping criterion rather than a subjective "good enough" judgment.

Not suited for quick exploratory plans where the cost of excessive refinement outweighs the benefit, or for plans where the quality criteria are genuinely unknown and a rubric cannot be constructed upfront.

## Ecosystem

Sean Geng's site (`seangeng.com-plan-optimizer`) bundles the plan-optimizer alongside a collection of other free tools: a "boil the ocean" agent prompt (Garry Tan's SOUL.md entry for shipping complete solutions), a "write like a human" system prompt, a disposable-email blocker, a Cloudflare WAF leaky-path rule generator, and a DevTools freeze bookmarklet. The plan-optimizer skill itself is the primary agentic AI artifact in the collection; the rest are standalone prompts and utilities.

The skills distribution ecosystem context: [[skills.sh]] and [[anthropics-skills]] cover the broader Claude Code skills catalog; [[obra-superpowers]] provides a comprehensive superpowers framework. [[mattpocock-skills]] takes a complementary approach — rubric-guided discipline (TDD, shared domain language, architecture audits) rather than a scoring loop. [[shadcn-improve]] applies a similar plan-file pattern for codebase audits, separating the capable planner from the cheaper executor. [[q00-ouroboros]] shares the iterative-refinement-with-scoring concept but applies it to full specification/development workflows rather than a standalone planning artifact.
