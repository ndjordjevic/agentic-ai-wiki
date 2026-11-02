---
type: source
category: "Coding-agent harnesses & methodologies"
source_url: https://github.com/evo-hq/evo
tags:
  - autoresearch
  - tree-search
  - parallel-subagents
  - experiment-gates
  - code-optimization
  - git-worktrees
  - agent-skills
  - benchmark-discovery
related:
  - karpathy-autoresearch
  - snarktank-ralph
  - frankbria-ralph-claude-code
  - openai-symphony
  - coleam00-agent-control-plane
product: evo
detail_level: standard
created: 2026-11-01
updated: 2026-11-01
---

`evo` (evo-hq/evo) is an autoresearch orchestrator plugin that turns an arbitrary codebase into a scored experiment loop: `/evo:discover` figures out what to measure and instruments a benchmark, then `/evo:optimize` runs tree search with parallel semi-autonomous subagents — keeping edits that improve the metric and discarding those that don't (or that fail correctness gates). It generalizes [[karpathy-autoresearch]]'s single-branch hill climb into multi-branch search with shared failure traces, a local dashboard, and installable host plugins for Claude Code, Codex, Cursor, Hermes, Kimi, OpenCode, OpenClaw, and Pi.

_All claims below are sourced from ../../raw/github/evo-hq-evo.md unless otherwise noted._

## What it does

You install the `evo-hq-cli` tool and an `evo install <host>` plugin, then run two skills. `discover` explores the repo, proposes optimization dimensions, builds or wires a benchmark (with optional held-out score-floor gates), and commits a baseline. `optimize` is the post-discover loop: the orchestrator writes briefs and spawns N subagents (each in its own backend workspace); subagents form hypotheses, edit, run `evo run`, and may iterate within a branch. Between rounds, RLM-inspired scan subagents surface compound failure patterns into shared state. When the loop stalls, `ship` distills the best valid experiment into a mergeable PR/merge plus a mergeability report. A Flask dashboard (default `http://127.0.0.1:8080`) starts with discover for frontier/backend monitoring. A hosted platform is offered at evo-hq.com (beta access).

## Installation

```bash
uv tool install evo-hq-cli
# optional remote backends: uv tool install 'evo-hq-cli[modal]'  # or e2b, daytona, aws, azure, all
npm install -g @anthropic-ai/claude-code   # or Codex / OpenClaw / Pi / Kimi host CLIs
evo install <host>   # claude-code | codex | cursor | hermes | kimi | opencode | openclaw | pi
```

Then in a target repo: `/evo:discover` (optionally with a seeded goal) → `/evo:optimize`. Host invocation differs (`/evo:` on Claude Code, `$evo` on Codex, skill menu on Cursor, natural language on Hermes/OpenCode/OpenClaw/Pi). Upgrade with `evo update`; telemetry can be disabled via `evo telemetry off` or `EVO_TELEMETRY=0`.

## Key features

- **Tree search over hill climb** — forks from any committed node so exploration isn't collapsed to one path; frontier strategies include argmax, top_k, epsilon_greedy, softmax, and GEPA-inspired pareto_per_task.
- **Parallel semi-autonomous subagents** — each gets a brief, isolated workspace, shared traces/annotations/discarded hypotheses, and an iteration budget within its branch; orchestrator must not run candidate experiments itself when subagents are available.
- **Gates** — pass/fail checks (tests, invariants, held-out score floors) discard experiments that "cheat" the metric even if the score rises; gates inherit down the experiment tree.
- **Benchmark discovery & instrumentation** — discover skill + Python/Node `evo_agent` SDKs (with inline-instrumentation fallback) define the result/trace contract evo reads.
- **Sizing-aware rounds** — round width follows resource profile (e.g. `subagents=1` for exclusive GPU); stall default 5 rounds with no improvement.
- **Multi-backend execution** — local worktree (default) or pool; SSH; Modal, E2B, Daytona, AWS EC2, Azure VMs via optional extras.
- **Cross-host packaging** — Claude/Codex/Kimi plugin manifests, hooks (incl. Rust `evo-hook-drain-rs`), npm skill copies for Cursor-style hosts, plus Hermes/OpenClaw/OpenCode adapters.

## Architecture

Core package lives under `plugins/evo/` (`evo-hq-cli` on PyPI, v0.8.0): skills (`discover`, `optimize`, `ship`, `report`, `subagent`, `finetuning`, `infra-setup`), Python `src/evo` (backends, sandbox_providers, host_install, inject, static dashboard), and host-specific plugin dirs. Experiment state is git-backed across worktrees/sandboxes; `evo new` / `evo run` allocate and score candidates. Mandatory `evo:verifier` subagents run pre (static analysis) and post (result-validity) every experiment; `evo:ideator` and `evo:benchmark-reviewer` support stall recovery and harness changes. Finetuning path adds train.py I/O contracts and references for ART (RL), Tinker (SFT), and vLLM serving. Author Alok Kumar Bishoyi; citable via Zenodo DOI `10.5281/zenodo.20447923`.

## Example usage

```
/evo:discover make the JSON parser at src/parser.py faster
/evo:optimize
# or: /evo:optimize subagents=4 budget=2 stall=5
```

After the loop: `/evo:ship`. Dashboard URL is printed when discover starts (`evo dashboard --port 8080` to restart).

## Maintenance status

1,488 stars, 117 forks, Apache-2.0, primary language Python (also JS/TS, Rust hook binary, CSS/HTML for dashboard). Latest release **v0.8.0** (2026-07-17); default branch `main`, last push 2026-10-05. CI badge present; PyPI package `evo-hq-cli`. Active multi-host plugin surface with documented migration notes for pre-0.4.4 installs and hook-repair via `evo doctor` / reinstall.
