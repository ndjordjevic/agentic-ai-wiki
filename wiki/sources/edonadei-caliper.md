---
type: source
category: "Coding-agent harnesses & methodologies"
source_url: https://github.com/edonadei/caliper
tags:
  - skill-eval
  - ab-testing
  - token-cost
  - agent-benchmark
  - mcp-eval
  - claude-code
  - hermes
  - codex
related:
  - nvidia-skillspector
  - skills.sh
  - anthropics-skills
  - obra-superpowers
  - addyosmani-agent-skills
  - coleam00-skills
product: caliper
detail_level: standard
created: 2026-10-27
updated: 2026-10-28
---

edonadei/caliper (223 stars, MIT) is a Python eval tool, published as `caliper-eval` on PyPI, that runs your real agent with and without your skills, MCPs, and rules to show which ones actually help and what they cost in tokens. Tagline: "Know if your agent skill actually works." It supports Claude Code, Codex, Pi, and Hermes, and is a measurement companion to skill packs like [[anthropics-skills]], [[obra-superpowers]] and [[addyosmani-agent-skills]].

_All claims below are sourced from ../../raw/github/edonadei-caliper.md unless otherwise noted._

## What it does

A spec (`.eval.yaml`) beside a skill lists the skills to install (the one under test plus "neighbours" that may compete for the same prompts) and tasks to run. Each task has a prompt, optional `setup:`, and at least one check: `expect:` (LLM-judged), `assert:` (local Python, 30-second limit), or `activates:` (which skills the agent chose to load, no judge needed). Each task runs k times (default 3), each attempt in a fresh temporary home and empty workdir, and Caliper reports success rate, a separate activation scoreboard, tokens, and wall time per attempt. The README's example: ablating `inbox-triage` took the bare agent from 80% to 100% with 30% fewer tokens and 28% less wall time.

## Installation

```bash
npx skills@latest add edonadei/caliper     # agent skills: grill-skill, evaluate-skill
pipx install caliper-eval                  # CLI
```

Each backend CLI must be installed and authenticated separately (`claude-code`, `codex`, `pi`, `hermes`); Caliper does not install or update them. There is no direct-API backend, so API billing means configuring one of those CLIs with a key. `caliper login chatgpt` lets Codex attempts run on a ChatGPT plan.

## Key features

- **Real installs** — skills are installed where the agent looks, never pasted into the prompt.
- **Activation scoreboard** — whether the agent picked the skill is scored apart from whether it worked; neighbourhoods let you assert which skill should win each prompt.
- **Ablation** — `--ablate <skill>` or `--ablate mcp:<server>` re-runs without it; same score means it is not earning its context.
- **Honest numbers** — single-run success rate first; `pass@k` and `pass^k` appear under `--verbose`. Dollar cost is not tracked because it is inconsistent across backends.
- **Portable scores** — `--no-user-customizations` isolates a run from your own skills, plugins and connectors.
- **Other spec features** — git-pinned neighbour skills, `mcp:` servers, mid-conversation `history:`, `sandbox:` file forbidding, silence assertions (`activates: []`).
- **Exit codes** — `2` means the eval could not run cleanly; `3` is reserved for a declared bar not being met; `caliper compare` never fails on regression.

## Architecture

Pipeline: spec → harness (runs each task k times in the chosen agent) → judge (LLM reads the transcript for `expect:`, Python for `assert:`) → success rate plus results JSON under `.caliper/results/<spec>/`. The engine is chosen at run time via `--model` (`backend` or `backend:model`) and `--judge-model`; the judge follows the evaluated backend by default. Repo contents: `caliper/` package, `skills/`, `examples/`, `docs/` (spec reference, backends, results, glossary, ADRs), `tests/`, `pyproject.toml`, `uv.lock`.

## Example usage

```bash
SPEC=inbox-triage/inbox-triage.eval.yaml
caliper run $SPEC --ablate inbox-triage
caliper run $SPEC
caliper compare .caliper/results/inbox-triage/RUN_ID.json inbox-triage
```

Inside an agent, `/grill-skill ./inbox-triage/SKILL.md` interviews you, writes the spec, and runs it with and without the skill; `/evaluate-skill run <spec> --k 3` runs evals without a separate terminal.

## Maintenance status

223 stars, 24 forks, MIT License (© Emrick Donadei), primary language Python, default branch `main`, latest release v0.21.0 (2026-10-27), most recent push the same day. Pre-1.0 and fast-moving: spec key `skill:` became `skills:` in v0.10. Listed on [[skills.sh]]; has CONTRIBUTING guidance and pre-commit setup.
