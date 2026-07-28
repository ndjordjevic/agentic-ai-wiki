# uditakhourii/adhd

## Metadata
- Stars: 2450
- Primary language: TypeScript
- Default branch: main
- Latest release: v0.1.4 (2026-05-30)
- License: MIT License
- Homepage: https://divergent.sh
- Fetched: 2026-07-28
- Final URL: https://github.com/UditAkhourii/adhd

## Description
ADHD — a skill for coding agents. Tree-of-thought with pruning, built on the Claude & Codex Agent SDK. Fans out parallel divergent thoughts under different cognitive frames, scores, prunes traps, deepens the survivors. The no-brainer skill for creative and interdisciplinary work.

## README

<p align="center">
  <a href="https://adhdstack.github.io/">
    <img src="docs/hero.png" alt="ADHD for Claude Code" width="100%">
  </a>
</p>

# ADHD — a skill for agents

[![CI](https://github.com/UditAkhourii/adhd/actions/workflows/ci.yml/badge.svg)](https://github.com/UditAkhourii/adhd/actions/workflows/ci.yml)
[![npm](https://img.shields.io/npm/v/adhd-agent.svg)](https://www.npmjs.com/package/adhd-agent)
[![license](https://img.shields.io/badge/license-MIT-blue.svg)](./LICENSE)
[![Node](https://img.shields.io/badge/node-%3E%3D18-brightgreen)](./documentation/install.md)
[![Paper](https://img.shields.io/badge/paper-preprint-blueviolet)](https://adhdstack.github.io/)
[![Featured: The New Stack](https://img.shields.io/badge/featured-The%20New%20Stack-ff5500)](https://thenewstack.io/claude-code-adhd/)
[![Discord](https://img.shields.io/badge/Discord-Join%20the%20chat-5865F2?logo=discord&logoColor=white)](https://discord.gg/NbWwkwwGw)

> **An architectural fix for premature convergence in autoregressive reasoning.**

Linear Chain-of-Thought anchors on whatever it says first. Tree-of-Thought widens the search but still walks a single shared context, so the anchoring persists across branches. **ADHD treats this as an architectural problem, not a prompting one** — it spawns N isolated reasoning processes under deliberately distorted cognitive frames, with zero shared context during divergence, then runs a separate critic pass to score, cluster, prune traps, and deepen the survivors.

Reach for it on **design decisions, fuzzy debugging, naming, API surface design, strategy, and any prompt of the shape *"give me a few ways to…"***.

📄 **Preprint:** [ADHD: Parallel Divergent Ideation for Coding Agents](https://adhdstack.github.io/) · 👤 **Author:** Udit Akhouri — [@akhouriudit](https://x.com/akhouriudit) · [LinkedIn](https://www.linkedin.com/in/udit-akhouri-10160a168/)

---

## Side-by-side: baseline vs ADHD

One eval problem, same model, two strategies. Full transcripts in [`bench/results.json`](./bench/results.json).

> **Problem.** *"We have a CLI that calls an LLM and it sometimes hangs for 90 seconds. Design the right retry/timeout/UX strategy."*

**Baseline (single-shot):** walks through four textbook patterns (progressive timeout, fast-fail + exponential backoff, hedged parallel requests, streaming with keepalive), lands on a hybrid recommendation (15s first-token / 30s between-token / 90s absolute, one auto-retry). No traps named, no acknowledgement the user might want to bail, no questioning of the "wait then retry same model" frame.

**ADHD:** spawns 6 isolated frames, surfaces 30+ ideas across `economic-incentive`, `async-control-surface`, `gamification`, `perceptual-distortion`, `collective-intelligence`, `redundancy-race` clusters. Non-obvious pick: *"rage-quit = instant abort + branch to cheaper/faster model"* — a button that pulses hotter the longer you wait; one click cancels and re-submits to a Haiku-class model. Plus a shortlist (scout-fork to alternate endpoints at 30s; daemonize the CLI with ticket IDs; race 3 LLM replicas, cache the winner) and 20 traps flagged with one-line reasons.

Independent LLM judge on this problem: breadth 9 vs 6, novelty 8 vs 3, trap detection ~8 vs ~2. Methodology in [documentation/evals.md](./documentation/evals.md).

---

## Featured

- Adopted by [repowire](https://github.com/prassanna-ravishankar/repowire) — first OSS project to officially ship ADHD (mesh-orchestrator port, [PR #313](https://github.com/prassanna-ravishankar/repowire/pull/313), merged).
- [The New Stack](https://thenewstack.io/claude-code-adhd/) ran a feature story on ADHD for Claude Code.
- OpenClaw / multi-agent community independently testing it across agents.
- An independent [evidence-based research review](https://github.com/testdouble/han/blob/adhd-swarm-research/docs/research/adhd-application-to-han.md) (11 sources, 8 validation rounds) published against the method; findings tracked as issues #16–#18.

## Early adopters

Projects that officially ship or integrate ADHD (from README table): **repowire** (mesh-orchestrator primitives), **mstack** (vendored as the `think` plugin), **zk-flow-oss** (adapted `IDEATION_FRAMES` into critique workflow), **han** (research application onto plugin model), **app-library** (yslee5005 — `expert-thinker` MoAI agent), **striatum** (installer scaffold recommends it), **awesome-prompts** (packaged as standalone prompt), **nix-skills** (Nix packaging, pinned commit), **caioniehues/adhd** and **ktg-one/adhd** (forks), **wtfismyrepo** (explanation engine for codebase onboarding — 12 codebase-specific frames), **mythify** (trap-clause guidance, PR #18), **godaudits** (v2.11.0, refutation pass + severity-aware recall metrics, PR #13), **godplans** (v1.8.0, independent audit gate, PR #8), **Claude1.0** (installed skill, PR #16).

---

## Install

One command, auto-detects your agent (Claude Code, Cursor, Antigravity, Codex, Cline, Gemini CLI, Windsurf, and ~50 more):

```bash
npx skills add UditAkhourii/adhd
```

Then invoke explicitly with `/adhd "your problem"`, or let it auto-trigger on ideation intents.

### Codex quick path

```bash
npx skills add UditAkhourii/adhd -a codex -g
```

Or install manually into Codex's skills directory:

```bash
mkdir -p ~/.codex/skills/adhd
curl -fsSL https://raw.githubusercontent.com/UditAkhourii/adhd/main/skills/adhd/SKILL.md \
  -o ~/.codex/skills/adhd/SKILL.md
```

CLI and library installs, manual curl for other agents, and per-platform paths are in [documentation/install.md](./documentation/install.md).

```bash
npm install -g adhd-agent     # CLI
npm install adhd-agent        # library
```

## Quickstart

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

Full reference: [documentation/api.md](./documentation/api.md).

## How it works

A two-phase loop with a hard wall between the phases.

1. **Diverge.** Pick N cognitive frames. Spawn N parallel, isolated Agent calls — each sees the problem plus one frame's vantage prompt, and a system prompt that forbids evaluation. Branches never see each other, so no anchoring.
2. **Focus.** A separate critic call scores every idea (`novelty / viability / fit`), flags traps with reasons, clusters by underlying angle, and deepens the top-K survivors into sketches with risks and first steps.

The generator-critic split is mechanical — separate LLM calls with opposite system prompts — not promised in one prompt. Deep dive: [documentation/how-it-works.md](./documentation/how-it-works.md). How it differs from CoT and ToT: [documentation/vs-cot-and-tot.md](./documentation/vs-cot-and-tot.md).

## Results

Mean scores across 6 open-ended engineering problems (0–10), ADHD vs a single-shot baseline at the same model, judged by an independent LLM with a skeptical-staff-engineer prompt, A/B order randomized.

| Dimension          | ADHD     | Baseline | Δ         | Ratio |
| ------------------ | -------: | -------: | --------: | ----: |
| breadth            | 9.00     | 4.83     | +4.17     | 1.9×  |
| novelty            | 7.83     | 2.67     | +5.17     | 2.9×  |
| trap detection     | 9.50     | 1.83     | +7.67     | 5.2×  |
| actionability      | 9.50     | 6.50     | +3.00     | 1.5×  |
| builder usefulness | 7.67     | 6.83     | +0.83     | 1.1×  |

ADHD wins 5 of 6 problems. Biggest gap is trap detection — baselines rarely name the seductive-but-broken ideas. Methodology, limitations, and how to reproduce: [documentation/evals.md](./documentation/evals.md).

## Documentation

| Page | What's in it |
|---|---|
| [Quickstart](./documentation/quickstart.md) | First skill, CLI, and TypeScript runs with practical commands |
| [Install](./documentation/install.md) | Every install path — skill, CLI, library, Agent SDK, per-platform |
| [How it works](./documentation/how-it-works.md) | The two-phase loop + architecture (context, pruning, orchestration) |
| [vs CoT & ToT](./documentation/vs-cot-and-tot.md) | Structural comparison, the three load-bearing differences, frames vs personas |
| [Frames](./documentation/frames.md) | The 15 cognitive frames, how selection works, how to author your own |
| [When to use](./documentation/when-to-use.md) | Use / don't use, why it shines on creative work, cost & speed |
| [CLI & API](./documentation/api.md) | CLI flags, library types, using ADHD inside your own agent |
| [Evals](./documentation/evals.md) | Methodology, headline numbers, limitations, roadmap |

Also: [SKILL.md](./skills/adhd/SKILL.md) (the runnable skill) · [SOURCE-SPEC.md](./SOURCE-SPEC.md) (original spec) · [CONTRIBUTING.md](./CONTRIBUTING.md) · [the preprint](https://adhdstack.github.io/).

## External reviews

- [Han plugin compatibility analysis](https://github.com/testdouble/han/blob/adhd-swarm-research/docs/research/adhd-application-to-han.md) — evidence-based review using Han's own `/research` skill, 11 sources, 8 validation rounds.
- [A measured duel vs. single-shot](https://miyagadget.page/en/blog/2026/06/03/adhd-coding-agent-skill-en/) by Shichinomiya — independent blind-scored benchmark; ADHD won both problems tested, biggest gains in novelty (4.5→9.0) and trap detection (5.0→9.0), at a real cost of ~2.3× time and ~1.9× output.

## License

MIT License. ADHD operationalizes the *Divergent Ideation* source spec ([SOURCE-SPEC.md](./SOURCE-SPEC.md)). The runnable skill is at [`skills/adhd/SKILL.md`](./skills/adhd/SKILL.md).

## Contact

**Udit Akhouri** — author of the preprint and maintainer. [adhdstack.github.io](https://adhdstack.github.io/) · [@akhouriudit](https://x.com/akhouriudit) · [researchudit@gmail.com](mailto:researchudit@gmail.com) · [@UditAkhourii](https://github.com/UditAkhourii)

## Docs

### documentation/how-it-works.md

A two-phase loop with a hard wall between the phases. Mixing them is what kills idea quality, because the critic strangles the generator.

**Phase 1 — Diverge (ADHD mode).** Pick N cognitive frames from the frame library. Spawn N parallel Agent SDK queries, each a fresh isolated session. Each branch sees: the problem, one frame's vantage prompt (e.g. *"You think in latency, memory layout, and physical constraints. Re-ask this as a hardware problem."*), and a system prompt that forbids evaluation, ranking, or hedging — pure generation, JSON array out, no prose. Branches do not see each other: no anchoring, no shared context, no convergence pressure.

**Phase 2 — Focus.** The critic comes back online, three passes:
1. **Score** every leaf on `novelty / viability / fit`. Tag traps with reasons.
2. **Cluster** by underlying angle, not surface keywords — surfaces the shape of the space.
3. **Deepen top-K**: sketch how it works, name the load-bearing risk, name the first concrete step, generate 3–5 child ideas (variations, hybrids, unlocks).

Output: the wide set clustered; a 2–4 idea shortlist; the non-obvious-but-viable pick flagged explicitly; the trap list with reasons; the deepened branches; one provocation (a wildcard question).

**Architecture.** Each divergent branch is its own `query()` call against the Claude Agent SDK — a fresh, stateless session with no shared KV-cache, no shared message history, no shared system prompt beyond the `claude_code` preset. Only tokens entering a branch: `system = preset + frame_vantage_prompt + "forbid evaluation/ranking/hedging, JSON array out"`, `user = problem + optional_context`. Token cost scales linearly in branches (`O(N × per_branch)`), not quadratically — true concurrent inference, not interleaved decoding on a shared trajectory (see `src/llm.ts`, `src/diverge.ts`).

Convergence is a separate LLM call with an inverted system prompt (critic posture, evaluation mandatory), performing Score / Cluster / Deepen-top-K (see `src/score.ts`, `src/cluster.ts`, `src/deepen.ts`). No heuristic threshold and no logit-bias steering — the critic's structured output is the pruning decision. Default `K=3`; `nonObviousPick` surfaces the highest-novelty viable leaf even if it's not the highest-fit.

Multi-agent orchestration via parallel `query()` calls, gated by a configurable semaphore (`concurrency`, default 4). Frame selection (`src/frames.ts`) is deterministic per-seed with a `codeMode` bias toward engineering vantage points. Each frame is a system-prompt payload that re-poses the entire question, not a logit-level intervention:

```ts
// the load-bearing call shape — bench/run-evals.ts and src/diverge.ts
const branches = await Promise.all(
  frames.map(frame => withSemaphore(concurrency, () => callLLM({
    systemPrompt: `${frame.vantage}\n\nFORBIDDEN: evaluation, ranking, hedging. JSON array out.`,
    userPrompt:   `${problem}\n\n${context ?? ""}`,
  })))
);
// branches[i] never sees branches[j] during divergence — by construction.
```

The generator-critic split is mechanical (different API calls, different system prompts) rather than promised in-prompt to the same session — the load-bearing design choice that distinguishes ADHD from in-context Tree-of-Thought.

### documentation/frames.md

A frame is a vantage operator: a system-prompt payload that re-poses the entire problem from a different cognitive position. Not a persona, not a domain expert — a deliberate distortion that forces the generator into a corner it would not naturally drift toward.

15 built-in frames ship today, biased toward engineering when `codeMode` is on (the default):

| Frame | Vantage | Tags |
|---|---|---|
| Hardware engineer | latency, memory layout, physical constraints | code, wild |
| Regulator / auditor | what must be provable, traceable, refusable? | design, general |
| 10-year-old | ignore convention; the naive, unencumbered approach | general, wild |
| Competitor trying to break it | adversarial; surface ideas by inversion | code, design |
| Biology | immune systems, neural plasticity, cell signaling, gut flora | code, wild |
| Logistics | queues, batching, just-in-time, hub-and-spoke, returns | code, design |
| Game design | loops, rewards, friction, save-states, speedrun tricks | design, general |
| Markets | auctions, futures contracts, clearing houses | design, wild |
| Inversion | ask the opposite question, then negate | code, design, general |
| $0 budget / infinite budget | extremes break anchoring | code, general |
| Remove the load-bearing assumption | what's possible if the framework / DB / network is gone? | code, design, wild |
| Speedrunner | glitches, skips, frame-perfect shortcuts | code, wild |
| Ant colony / swarm | no central planner, local rules, emergent behavior | code, wild |
| 3am on-call | what design would let you not get paged? | code, design |

**How frames are selected:** `codeMode` (default `true`) biases selection toward `code` and `design` tags. A `wild` frame always gets one reserved slot per run so divergence stays weird. Selection is deterministic per-seed so runs are reproducible.

**Authoring your own:** a frame is ~5 lines in `src/frames.ts`. A good frame passes at least two of: distinct vocabulary (concepts no existing frame uses), distinct posture (adversarial vs constructive vs naive vs maximalist — not just a different domain saying the same thing), reproducible distortion (consistently surfaces ideas other frames don't).

## Top-level structure

- `.github/` — CI workflows (boilerplate, not fetched)
- `CODE_OF_CONDUCT.md`, `CONTRIBUTING.md`, `SECURITY.md` — community/governance docs
- `EVALS.md`, `SOURCE-SPEC.md` — evaluation methodology and the original "Divergent Ideation" source spec
- `LICENSE` — MIT
- `README.md` — project overview (fetched above)
- `bench/` — eval harness and results (`bench/results.json`, `bench/run-evals.ts`)
- `docs/` — static site assets (hero image, `index.html`, social preview images)
- `documentation/` — user-facing docs: quickstart, install, how-it-works, vs-cot-and-tot, frames, when-to-use, api, evals (fetched above)
- `skills/adhd/SKILL.md` — the runnable agent skill definition (installed via `npx skills add`)
- `src/` — TypeScript implementation: `cli.ts`, `engine.ts`, `frames.ts`, `index.ts`, `llm.ts`, `render.ts`, `types.ts`
- `tests/` — test suite
- `package.json`, `package-lock.json`, `tsconfig.json`, `tsconfig.bench.json` — Node/TS project config
