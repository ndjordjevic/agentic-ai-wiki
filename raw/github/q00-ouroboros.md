# Q00/ouroboros

## Metadata
- Stars: 4555
- Primary language: Python
- Default branch: main
- Latest release: v0.41.0 (2026-06-07)
- License: MIT
- Homepage: (none)
- Fetched: 2026-06-12
- Final URL: https://github.com/Q00/ouroboros

## Description
Agent OS: Stop prompting. Start specifying. A specification-first, replayable AI coding workflow engine for Claude Code, Codex CLI, OpenCode, Hermes, Gemini, Kiro, Copilot, and Pi.

## README

<p align="center">
  <strong>O U R O B O R O S</strong>
  <br/>
  <strong>Stop prompting. Start specifying.</strong>
  <br/>
  <sub>The <strong>Agent OS</strong> for replayable, specification-first AI coding workflows</sub>
</p>

**Turn a vague idea into a verified, working codebase -- across Claude Code, Codex CLI, OpenCode, Hermes, Gemini, Kiro, Copilot, and Pi.**

Ouroboros is an **Agent OS** for AI coding: a local-first runtime layer that turns non-deterministic agent work into a replayable, observable, policy-bound execution contract. It replaces ad-hoc prompting with a structured specification-first workflow: interview, crystallize, execute, evaluate, evolve.

---

### The Ouroboros Agent OS Stack

| Layer | Repo | Role |
| :--- | :--- | :--- |
| **Shell** | `Q00/ourocode` | Native terminal UI for running `ooo` workflows across Claude / Codex / Gemini CLIs |
| **Apps** | `Q00/ouroboros-plugins` | UserLevel plugin contract — composes core primitives into domain programs (PR ops, Jira sync, incidents, releases) |
| **OS** | `Q00/ouroboros` (this repo) | Agent OS core — Seed, Ledger, Runtime, MCP, safety boundaries |

### Why Ouroboros?

Most AI coding fails at the **input**, not the output.

| Problem | Ouroboros Fix |
| :--- | :--- |
| Vague prompts → AI guesses | Socratic interview exposes hidden assumptions |
| No spec → architecture drifts | Immutable seed spec locks intent before code |
| Manual QA | 3-stage automated evaluation gate |

### Quick Start

```bash
# Install
curl -fsSL https://raw.githubusercontent.com/Q00/ouroboros/main/scripts/install.sh | bash

# Claude Code plugin (no Python required)
claude plugin marketplace add Q00/ouroboros
claude plugin install ouroboros@ouroboros

# pip/uv/pipx
pip install ouroboros-ai
pip install 'ouroboros-ai[claude]'
pip install 'ouroboros-ai[all]'   # claude + litellm + mcp + tui
ouroboros setup
```

Inside an AI coding agent session:
```
ooo interview "I want to build a task management CLI"
ooo run
```

One-command A-grade pipeline:
```
ooo auto "Build a local-first habit tracker CLI"
```

Supports: Claude Code, Codex CLI, GitHub Copilot CLI, OpenCode, Hermes, Gemini, Kiro CLI, Pi CLI.

### The Loop

```
    Interview -> Seed -> Execute -> Evaluate
        ^                           |
        +---- Evolutionary Loop ----+
```

| Phase | What Happens |
| :--- | :--- |
| **Interview** | Socratic questioning exposes hidden assumptions |
| **Seed** | Answers crystallize into an immutable specification |
| **Execute** | Double Diamond: Discover → Define → Design → Deliver |
| **Evaluate** | 3-stage gate: Mechanical ($0) → Semantic → Multi-Model Consensus |
| **Evolve** | Wonder → Reflect → next generation |

Convergence is reached when ontology similarity >= 0.95.

**Ralph (`ooo ralph`):** runs the evolutionary loop persistently across session boundaries until convergence. Each step is stateless — the EventStore reconstructs the full lineage, so even if your machine restarts, the serpent picks up where it left off.

### Commands

| Skill (`ooo`) | What It Does |
| :--- | :--- |
| `ooo setup` | Register runtime and configure project |
| `ooo interview` | Socratic questioning — expose hidden assumptions |
| `ooo auto` | Goal → A-grade Seed → execution handoff |
| `ooo seed` | Crystallize into immutable spec |
| `ooo run` | Execute via Double Diamond decomposition |
| `ooo evaluate` | 3-stage verification gate |
| `ooo evolve` | Evolutionary loop until ontology converges |
| `ooo unstuck` | 5 lateral thinking personas when stuck |
| `ooo status` | Session tracking + drift detection |
| `ooo ralph` | Persistent loop until verified |
| `ooo pm` | PM-focused interview + PRD generation |
| `ooo qa` | General-purpose QA verdict |
| `ooo brownfield` | Scan/manage brownfield repo defaults |
| `ooo publish` | Publish a Seed as GitHub Epic/Task issues |

### The Nine Minds

Nine agents, each a different mode of thinking. Loaded on-demand:

| Agent | Core Question |
| :--- | :--- |
| **Socratic Interviewer** | *"What are you assuming?"* |
| **Ontologist** | *"What IS this, really?"* |
| **Seed Architect** | *"Is this complete and unambiguous?"* |
| **Evaluator** | *"Did we build the right thing?"* |
| **Contrarian** | *"What if the opposite were true?"* |
| **Hacker** | *"What constraints are actually real?"* |
| **Simplifier** | *"What's the simplest thing that could work?"* |
| **Researcher** | *"What evidence do we actually have?"* |
| **Architect** | *"If we started over, would we build it this way?"* |

### Ambiguity Score Gate

Ambiguity = 1 - Sum(clarity_i × weight_i). Threshold: **Ambiguity <= 0.2** before a Seed can be generated.

| Dimension | Greenfield weight | Brownfield weight |
| :--- | :---: | :---: |
| Goal Clarity | 40% | 35% |
| Constraint Clarity | 30% | 25% |
| Success Criteria | 30% | 25% |
| Context Clarity | — | 15% |

### Ontology Convergence

Evolutionary loop stops at Similarity >= 0.95: `0.5 × name_overlap + 0.3 × type_match + 0.2 × exact_match`. Hard cap: 30 generations.

### Contributing

```bash
git clone https://github.com/Q00/ouroboros
cd ouroboros
uv sync --all-groups && uv run pytest
```

Python >= 3.12 required.

## Docs

### docs/architecture.md (excerpt)

Ouroboros is a **specification-first AI workflow engine** built on event sourcing with a rich TUI interface.

**Architecture layers:**

1. **Skills & Agents Registry** — 14 core workflow skills, 9 specialized agents, hot-reload capabilities, magic prefix detection (`/ouroboros:`)
2. **Core Layer** — Seed (immutable frozen Pydantic model), Acceptance Criteria Tree (recursive MECE decomposition), Ontology schema, version tracking and ambiguity scoring
3. **Execution Layer** — Self-referential persistence loop with verification, dependency-aware parallel execution, automatic scaling
4. **State Layer** — SQLite event store (append-only), full replay capability, checkpoint system with compression, 5 optimized indexes
5. **Orchestration Layer** — 6-phase pipeline, PAL Router (Frugal 1× → Standard 10× → Frontier 30×) with auto-escalation on failure
6. **Presentation Layer** — Textual-based TUI dashboard, Typer-based CLI
7. **UserLevel Programs Layer** — Installable plugins (`ouroboros-plugins`) with declared manifest contract

**Key internals:**
- **PAL Router** — cost-tiered model routing: auto-escalates on failure, auto-downgrades on success
- **Drift** — Goal (50%) + Constraint (30%) + Ontology (20%) weighted measurement, threshold <= 0.3
- **Brownfield** — auto-detects config files across multiple language ecosystems
- **Stagnation detection** — spinning, oscillation, no-drift, and diminishing returns patterns
- **Runtime backends** — pluggable abstraction layer with first-class support for Claude Code, Codex CLI, OpenCode, Hermes, Gemini, Goose, Kiro, Copilot, and Pi

### docs/getting-started.md (excerpt)

**Recommended: Claude Code (`ooo`)** — No Python install required.

```bash
claude plugin marketplace add Q00/ouroboros
claude plugin install ouroboros@ouroboros
```

Then inside a Claude Code session:
```
ooo setup
ooo auto "Build a task management CLI"
```

`ooo auto` runs bounded Socratic interview rounds, generates an A-grade Seed, repairs B/C Seeds when possible, and starts execution only after the A-grade gate passes.

**Alternative: Standalone CLI** — requires Python >= 3.12.

```bash
pip install ouroboros-ai
ouroboros setup
ouroboros run ~/.ouroboros/seeds/seed_abc123.yaml
```

## Top-level structure

```
.claude-plugin/     — Claude Code plugin manifest and registry
.claude/            — CLAUDE.md with ooo command dispatch table
.codex/             — Codex CLI config
.ouroboros/         — project-level ouroboros config
.mcp.json           — MCP server registration
AGENTS.md           — dev-mode ooo command dispatch table (maps ooo <cmd> → skills/<cmd>/SKILL.md)
CLAUDE.md           — Claude-specific instructions
CHANGELOG.md        — release history (v0.41.0 latest)
CONTRIBUTING.md     — development guide
Code-Review-Claude.md   — Claude Code review workflow
Code-Review-Codex.md    — Codex review workflow
HANDOFF.md          — session handoff protocol
SECURITY.md         — vulnerability disclosure policy
commands/           — CLI command implementations
crates/             — Rust crates (performance-critical components)
docs/               — architecture, CLI reference, runtime guides, config reference, getting-started
examples/           — usage examples (structure only; not fetched)
hooks/              — lifecycle hook definitions
llms.txt            — compact LLM context summary
llms-full.txt       — full LLM context (21kb)
project-context.md  — project context for agents
pyproject.toml      — Python package config (Python >= 3.12; extras: claude, litellm, mcp, tui, all)
scripts/            — install.sh and utility scripts
skills/             — 20 skill directories: auto, brownfield, cancel, evaluate, evolve, help,
                      interview, pm, publish, qa, ralph, resume-session, run, seed, setup,
                      status, tutorial, unstuck, update, welcome
src/ouroboros/      — Python source: bigbang/, routing/, execution/, evaluation/, evolution/,
                      resilience/, observability/, persistence/, orchestrator/, core/,
                      providers/, mcp/, plugin/, tui/, cli/, agents/
tests/              — pytest test suite
tools/              — tool definitions
uv.lock             — locked dependency tree
```
