---
type: source
category: "Agent Skills & plugins ecosystem"
source_url: https://github.com/UditAkhourii/adhd
tags:
  - divergent-ideation
  - cognitive-frames
  - tree-of-thought
  - generator-critic-split
  - claude-agent-sdk
  - agent-skill
  - parallel-agents
related:
  - anthropics-skills
  - karpathy-llm-council
  - uditakhourii-neuroarxiv
product: adhd
detail_level: standard
created: 2026-07-28
updated: 2026-08-12
---

ADHD is an open-source agent skill and TypeScript library that treats premature convergence in LLM reasoning as an architectural problem rather than a prompting one. Instead of Chain-of-Thought (which anchors on its first idea) or in-context Tree-of-Thought (which still shares one context across branches), ADHD spawns N fully isolated Agent SDK sessions under distinct "cognitive frame" system prompts, forbids evaluation during generation, then runs a separate critic pass to score, cluster, prune traps, and deepen the survivors. It installs as a skill (`npx skills add UditAkhourii/adhd`) into Claude Code, Codex, Cursor, and ~50 other agents, and ships as a standalone CLI/library (`adhd-agent` on npm). See [[uditakhourii-adhd]].

_All claims below are sourced from ../../raw/github/uditakhourii-adhd.md unless otherwise noted._

## What it does

ADHD is a two-phase ideation method for agents facing open-ended, "give me a few ways to…" problems — design decisions, fuzzy debugging, naming, API surface design, strategy. Phase 1 (Diverge) picks N cognitive frames and spawns N parallel, stateless `query()` calls against the Claude Agent SDK, each seeing only the problem plus one frame's vantage prompt and a system prompt that forbids evaluation, ranking, or hedging — pure JSON-array generation. Branches never see each other, so there is no shared context and no anchoring. Phase 2 (Focus) runs a separate critic call with an inverted, evaluation-mandatory system prompt: it scores every idea on novelty/viability/fit, tags traps with mechanistic reasons, clusters ideas by underlying angle (not surface keywords), and deepens the top-K survivors into sketches with a load-bearing risk, a first concrete step, and 3-5 child ideas. Output includes the clustered wide set, a shortlist, an explicitly flagged non-obvious-but-viable pick, the trap list, the deepened branches, and one wildcard provocation question.

## Installation

Auto-detecting installer: `npx skills add UditAkhourii/adhd`, which registers the skill across Claude Code, Cursor, Antigravity, Codex, Cline, Gemini CLI, Windsurf, and roughly 50 other agents; invoke with `/adhd "your problem"` or let it auto-trigger on ideation intents. Codex has a documented fallback path (`npx skills add UditAkhourii/adhd -a codex -g`, or a manual `curl` of `skills/adhd/SKILL.md` into `~/.codex/skills/adhd/`) because some Codex builds discover skills from a fixed path and truncate multi-line YAML descriptions. It is also distributed as a standalone CLI (`npm install -g adhd-agent`) and library (`npm install adhd-agent`).

## Key features

- 15 built-in "cognitive frames" (hardware engineer, regulator/auditor, 10-year-old, adversarial competitor, biology, logistics, game design, markets, inversion, $0/infinite budget, remove-the-load-bearing-assumption, speedrunner, ant colony/swarm, 3am on-call) — each a ~5-line vantage-prompt payload tagged `code`/`design`/`general`/`wild`, selectable and authorable in `src/frames.ts`.
- Deterministic per-seed frame selection: `codeMode` (default on) biases toward `code`/`design` tags, and one `wild` frame slot is always reserved per run to keep divergence weird.
- Mechanical generator-critic split — different API calls with opposite system prompts, not a single prompt asked to role-play both — is the design choice the project argues distinguishes it from in-context Tree-of-Thought.
- Configurable concurrency semaphore (default 4) gates the parallel `query()` fan-out; token cost scales linearly (`O(N × per_branch)`), not quadratically, since branches never see each other's output.
- Published benchmark: on 6 open-ended engineering problems judged by an independent LLM (skeptical-staff-engineer prompt, A/B order randomized), ADHD scored 9.00 vs 4.83 breadth, 7.83 vs 2.67 novelty, and 9.50 vs 1.83 trap detection against a single-shot baseline at the same model, winning 5 of 6 problems, at a real cost (per an independent third-party benchmark) of roughly 2.3x time and 1.9x output tokens.

## Architecture

Each divergent branch is an independent, stateless `query()` call — no shared KV-cache, no shared message history beyond the `claude_code` preset. A branch receives only `system = preset + frame_vantage_prompt + "forbid evaluation/ranking/hedging, JSON array out"` and `user = problem + optional_context`. Convergence is a second, separate LLM call (critic posture, evaluation mandatory) that runs three structured passes — score, cluster, deepen top-K (`src/score.ts`, `src/cluster.ts`, `src/deepen.ts`) — with no heuristic threshold or logit-bias steering; the critic's structured JSON output *is* the pruning decision. Default `K=3`, and a `nonObviousPick` field explicitly surfaces the highest-novelty viable leaf even when it isn't the highest-fit one.

## Example usage

```bash
adhd "design a rate limiter that survives a leader election"
adhd "name this function" --frames 3 --ideas 8 --top 2
```

```ts
import { run, renderText } from "adhd-agent";

const result = await run({ problem: "How should we shard this queue under bursty load?", framesPerRun: 5, topK: 3 });
console.log(renderText(result));
// result.shortlist · result.nonObviousPick · result.traps · result.deepened · result.clusters
```

## Maintenance status

2,450 stars, 199 forks, MIT licensed, TypeScript, latest release v0.1.4 (2026-05-30), default branch `main`. Actively adopted downstream: repowire ported it onto its own mesh-orchestrator primitives (merged PR), mstack vendored it as a `think` plugin, and several other projects (zk-flow-oss, han, wtfismyrepo, mythify, godaudits, godplans) have shipped adaptations or independent research reviews of the method, tracked openly as upstream GitHub issues. Featured in a The New Stack article on ADHD for Claude Code.

## When to use

Suited to problems of the shape "give me a few ways to…" — design decisions, fuzzy debugging, naming, API surface design, and strategy — where breadth and trap-avoidance matter more than a single fast answer. Not a fit for problems with one clearly correct mechanical answer, where the added latency and token cost (roughly 2x baseline, per third-party benchmarking) buys no real dispersion of ideas.

## Ecosystem

Operationalizes a "Divergent Ideation" source spec (`SOURCE-SPEC.md`) and has an accompanying preprint. Positions itself explicitly against Chain-of-Thought and in-context Tree-of-Thought, arguing the generator-critic split must be mechanical (separate API calls) rather than promised within one prompt/session — see [[uditakhourii-adhd]] for the full architecture discussion. Builds directly on the [Claude Agent SDK](https://docs.claude.com/en/api/agent-sdk) for its parallel `query()` fan-out.
