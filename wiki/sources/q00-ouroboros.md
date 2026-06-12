---
type: source
source_url: https://github.com/Q00/ouroboros
tags: [agent-os, specification-first, socratic-interview, evolutionary-loop, mcp, python, multi-runtime, ambiguity-scoring]
related: [buildermethods-agent-os, obra-superpowers, snarktank-ralph, github-spec-kit, seangeng.com]
product: ouroboros
detail_level: standard
created: 2026-06-12
updated: 2026-06-12
---

Ouroboros (Q00/ouroboros, 4,555 stars, MIT, Python, v0.41.0) is an Agent OS and specification-first workflow engine that replaces ad-hoc AI prompting with a structured interview → crystallize → execute → evaluate → evolve cycle. Its central claim is that most AI coding fails at the input: vague prompts produce architecture drift and rework. Ouroboros fixes this by enforcing a Socratic interview that mathematically gates on ambiguity before generating an immutable Seed spec, then evaluates output through a three-stage verification pipeline. It runs across Claude Code, Codex CLI, OpenCode, Hermes, Gemini, Kiro, Copilot, and Pi — making it the most multi-runtime specification-first system in this wiki.

_All claims below are sourced from ../../raw/github/q00-ouroboros.md unless otherwise noted._

## What it does

Ouroboros structures AI coding work into five phases — Interview, Seed, Execute, Evaluate, and Evolve — and locks each transition with a mathematical gate. The Interview phase exposes hidden assumptions through Socratic questioning, scoring ambiguity across goal clarity, constraint clarity, success criteria, and (for brownfield projects) context clarity. A Seed spec can only be generated once ambiguity drops below 0.2. Execution uses a Double Diamond decomposition (Discover → Define → Design → Deliver). Evaluation runs three stages — Mechanical ($0, deterministic checks), Semantic (LLM-judged), and Multi-Model Consensus (multiple models vote). The Evolve phase feeds evaluation output back as the next generation's Seed input, running up to 30 generations until ontology similarity hits 0.95 or the loop detects stagnation. The `ooo ralph` skill runs this loop persistently across session boundaries using SQLite event sourcing for full state reconstruction on restart.

## Key features

- **Ambiguity gate** — quantitative score `Ambiguity = 1 − Σ(clarity_i × weight_i)` with threshold ≤ 0.2; blocks premature code generation
- **Immutable Seed spec** — frozen Pydantic model; locks requirements before execution starts
- **PAL Router** — three-tier cost optimization: Frugal (1×) → Standard (10×) → Frontier (30×), auto-escalates on failure, auto-downgrades on success
- **Nine on-demand agents** — Socratic Interviewer, Ontologist, Seed Architect, Evaluator, Contrarian, Hacker, Simplifier, Researcher, Architect; loaded when needed, never preloaded
- **Stagnation detection** — four patterns: spinning, oscillation (period-2 cycle), repetitive feedback, hard cap at 30 generations
- **Drift measurement** — Goal (50%) + Constraint (30%) + Ontology (20%) weighted; threshold ≤ 0.3
- **`ooo auto`** — A-grade pipeline: bounded interview rounds, Seed quality scoring, B/C Seed repair, execution handoff with `auto_session_id` for resumption
- **UserLevel plugin layer** — `ouroboros-plugins` repo provides scoped domain programs (PR ops, Jira sync, incidents) with plugin manifest contract above the core kernel
- **`ooo pm`** — PM-focused interview + PRD generation for product-oriented teams
- **`ooo publish`** — converts a Seed into GitHub Epic/Task issues for team workflows via the `gh` CLI

## Architecture

The repo is organized as three-layer Agent OS stack. The kernel (`ouroboros`) owns the execution contract: every action is Seed-bound, ledger-recorded, and replayable. Plugins (`ouroboros-plugins`) declare scoped capabilities against that contract. The terminal shell (`ourocode`) surfaces MCP state, interview questions, and wonderTool decisions as a TUI.

The kernel itself has seven internal layers: Skills & Agents Registry (14 workflow skills, 9 agents, hot-reload, `/ouroboros:` prefix magic), Core Layer (immutable Seed, Acceptance Criteria Tree with MECE decomposition, Ontology schema), Execution Layer (self-referential persistence loop, dependency-aware parallel execution), State Layer (append-only SQLite event store, full replay, checkpoint compression), Orchestration Layer (6-phase pipeline, PAL Router), Presentation Layer (Textual TUI, Typer CLI), and UserLevel Programs Layer above the kernel. The Python source in `src/ouroboros/` spans `bigbang/` (interview, ambiguity scoring, brownfield detection), `routing/` (PAL Router), `execution/` (Double Diamond, AC decomposition), `evaluation/` (three-stage gate), `evolution/` (Wonder/Reflect cycle), `resilience/` (stagnation detection, 5 lateral personas), `observability/` (3-component drift measurement, auto-retrospective), `persistence/` (SQLAlchemy + aiosqlite event store), `orchestrator/` (runtime abstraction layer), and `providers/` (LiteLLM adapter for 100+ models). Rust crates in `crates/` handle performance-critical components.

The AGENTS.md maps `ooo <cmd>` to `skills/<cmd>/SKILL.md` files, following the same two-layer skill-loading pattern seen in `[[anthropics-skills]]` and `[[skills.sh]]`.

## Installation

```bash
# Claude Code plugin — no Python required (recommended)
claude plugin marketplace add Q00/ouroboros
claude plugin install ouroboros@ouroboros
# Then inside Claude Code:
ooo setup
ooo auto "Build a task management CLI"

# pip / uv / pipx
pip install ouroboros-ai
pip install 'ouroboros-ai[claude]'    # + Claude Code deps
pip install 'ouroboros-ai[litellm]'   # + LiteLLM multi-provider
pip install 'ouroboros-ai[mcp]'       # + MCP server/client
pip install 'ouroboros-ai[all]'       # everything
ouroboros setup

# curl installer (auto-detects Claude Code, Codex CLI, Hermes)
curl -fsSL https://raw.githubusercontent.com/Q00/ouroboros/main/scripts/install.sh | bash
```

Python >= 3.12 required for the standalone CLI path. The plugin path has no Python requirement.

## Example usage

```
# Interview-then-run (manual path)
ooo interview "Build a task management CLI"
ooo run

# One-command A-grade pipeline
ooo auto "Build a local-first habit tracker CLI"

# Persistent evolutionary loop until convergence
ooo ralph

# When stuck — spawns 5 lateral thinking personas
ooo unstuck

# Check session state and drift
ooo status
```

From the terminal (standalone CLI):
```bash
ouroboros init start "your goal"
ouroboros run ~/.ouroboros/seeds/seed_abc123.yaml
ouroboros status executions
ouroboros cancel execution --all
```

## When to use

Ouroboros fits teams where AI coding sessions repeatedly drift from intent — especially for non-trivial features where the requirement itself is underspecified. The ambiguity gate is the key differentiator: if you find yourself reworking AI-generated code because the agent misunderstood the problem, the Socratic interview phase pays for its overhead. The `ooo auto` command offers a fully automated path for users who want minimal friction. For brownfield projects, `ooo brownfield` auto-detects config files across language ecosystems and seeds the Context Clarity dimension. The multi-runtime adapter (Claude Code, Codex, Gemini, Hermes, Kiro, Copilot, Pi) means teams can use it without being locked to one provider.

## Maintenance status

4,555 stars, MIT license, v0.41.0 released 2026-06-07, actively maintained with frequent releases. The repo ships with `SECURITY.md`, a full CONTRIBUTING.md guide, `Code-Review-Claude.md` and `Code-Review-Codex.md` for PR workflows, and a CHANGELOG. The related three-repo stack (`ouroboros` kernel + `ouroboros-plugins` + `ourocode` TUI) suggests an active multi-product roadmap. The disclaimer in the README explicitly disavows any cryptocurrency/token association.

## Ecosystem

Ouroboros connects to the broader wiki ecosystem at several points: its SKILL.md-based `skills/` directory is compatible with the `[[skills.sh]]` distribution platform and `[[voltagent-awesome-agent-skills]]` catalog; the `ooo ralph` persistent loop shares the evolutionary iteration concept with `[[snarktank-ralph]]`; the specification-first Seed mechanism is philosophically aligned with `[[github-spec-kit]]` and `[[openspec.dev]]`; and the multi-agent 9-minds architecture parallels the role-based crew model in `[[crewai.com]]`. The plugin marketplace integration (`claude plugin marketplace add`) connects it to `[[anthropics-skills]]` as a first-class Claude Code plugin. The LiteLLM provider adapter in `providers/` makes it compatible with the full routing stack in `[[litellm.ai]]` and `[[openrouter.ai]]`.
