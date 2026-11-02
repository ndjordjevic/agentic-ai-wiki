# evo-hq/evo

## Metadata
- Stars: 1488
- Forks: 117
- Primary language: Python
- Default branch: main
- Latest release: v0.8.0 (2026-07-17)
- License: Apache License 2.0
- Homepage: https://evo-hq.com
- Created: 2026-04-05
- Pushed: 2026-10-05
- Topics: agent-skills, autonomous-agents, autoresearch, claude-code, code-optimization, codex, evolutionary-algorithms, llm-agents
- Fetched: 2026-11-01
- Final URL: https://github.com/evo-hq/evo

## Description
turns your codebase into an autoresearch loop — discovers what to measure, instruments the benchmark, then runs tree search with parallel subagents.

## README
# evo

<p align="center">
  <img src="assets/banner.png" alt="evo — autoresearch orchestrator for your codebase" width="100%" />
</p>

<div align="center">

[![PyPI](https://img.shields.io/pypi/v/evo-hq-cli)](https://pypi.org/project/evo-hq-cli/)
[![License](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)
[![Tests](https://github.com/evo-hq/evo/actions/workflows/ci.yml/badge.svg)](https://github.com/evo-hq/evo/actions/workflows/ci.yml)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20447923.svg)](https://doi.org/10.5281/zenodo.20447923)

**Get started with autoresearch on any codebase - with two simple commands.**

Do you want to do more with autoresearch or need a custom, hands-on deployment?
[Request access to evo platform](https://evo-hq.com/beta) or email [hello@evo-hq.com](mailto:hello@evo-hq.com).

---
**[Try it](#try-it)** · **[Install](#install)** · **[How it works](#how-it-works)** · **[Dashboard](#dashboard)** · **[Upgrading](#upgrading)**

</div>
A plugin for your agentic framework that optimizes code through experiments

You give it a codebase. It discovers metrics to optimize, sets up the evaluation, and starts running experiments in a loop -- trying things, keeping what improves the score, throwing away what doesn't.

*Inspired by [Karpathy's autoresearch](https://github.com/karpathy/autoresearch)* -- where an LLM runs training experiments autonomously to beat its own best score. Autoresearch is a pure hill climb: try something, keep or revert, repeat on a single branch. Evo adds structure on top of that idea:

- **Tree search over greedy hill climb.** Multiple directions can fork from any committed node, so exploration doesn't collapse to one path.
- **Parallel semi-autonomous agents.** Spawn multiple subagents and run them simultaneously, each in its own git worktree. Each subagent reads traces, formulates hypotheses, and can run multiple iterations within its branch.
- **Shared state.** Failure traces, annotations, and discarded hypotheses are accessible to every agent before it decides what to try next.
- **Gating.** Regression tests or safety checks can be wired up as a gate. Experiments that don't pass get discarded.
- **Observability.** A dashboard to monitor your experiments.
- **Benchmark discovery.** The `discover` skill explores the repo, figures out what to measure, and instruments the evaluation.


Runs on Claude Code, Codex, Cursor, Kimi, OpenClaw, Hermes, Opencode, or Pi. Experiments run locally or on remote sandboxes — Modal, E2B, Daytona, AWS, Azure, SSH.


<p align="center">
  <img src="assets/dashboard.png" alt="evo dashboard" width="100%" />
</p>

## Try it

Two commands:

```
/evo:discover     # one-time code discovery: figures out benchmarks and creates gates against unintended changes
/evo:optimize     # run the loop
```

`discover` asks what to optimize, the benchmark command, and the metric direction. Skip the questions by seeding the answer:

```
/evo:discover make the JSON parser at src/parser.py faster
```

Then run the loop:

```
/evo:optimize
```

evo sizes each round to your benchmark's resource profile — one experiment at a time when a run needs the whole GPU or another exclusive resource, wider when runs are independent — and keeps going until the score stops improving. By default it runs unattended and pushes edits through parallel subagents; say so in plain language if you'd rather it pause after each round or hold to one experiment at a time.

Invocation syntax is host-specific: `/evo:` on Claude Code, `$evo` on Codex, `/` skill menu on Cursor, natural language on Hermes, Opencode, OpenClaw, and Pi.

## Install

```bash
# 1. evo CLI
uv tool install evo-hq-cli

# 2. Host CLI (if you don't already have it)
npm install -g @anthropic-ai/claude-code     # or @openai/codex, openclaw, @earendil-works/pi-coding-agent
# Cursor: install from cursor.com (IDE), or `curl https://cursor.com/install -fsS | bash` for the cursor-agent CLI
# Kimi: `curl -fsSL https://code.kimi.com/install.sh | bash`, or `npm install -g @moonshot-ai/kimi-code`

# 3. Plugin + host hooks
evo install <host>     # claude-code | codex | cursor | hermes | kimi | opencode | openclaw | pi
```

For remote backends, install with the matching provider extra: `uv tool install 'evo-hq-cli[modal]'` (or `[e2b]`, `[daytona]`, `[aws]`, `[azure]`, `[all]`).

### Codex hook trust

`evo install codex` trusts evo's hooks for you. To review them yourself first, pass `--no-trust-hooks`, then approve via `/hooks` inside codex.

## How it works

### Parallel

The orchestrator dispatches subagents in parallel. Each runs in its own isolated workspace, picks up shared state (failure traces, annotations, discarded hypotheses), forms a hypothesis, edits, and runs the benchmark. A subagent with iteration budget remaining continues on its branch within the same round when its prior edit warrants a follow-up.

### Frontier strategy

After each round, the orchestrator selects which committed branch to extend next. Available strategies:

- **argmax** — extend the highest-scoring branch
- **top_k** — round-robin among the K best
- **epsilon_greedy** — best most of the time, random sometimes
- **softmax** — sample weighted by score
- **pareto_per_task** — keep specialists the aggregate hides, inspired by [GEPA](https://arxiv.org/abs/2507.19457)

Configure in the dashboard's Frontier tab, which lists each strategy's parameters.

### Cross-cutting scans

Between rounds, [RLM](https://arxiv.org/abs/2512.24601)-inspired scan subagents read trace batches in parallel and surface compound failure patterns: gate-failure intersections, shared root causes across traces. Findings land in shared state, which the next round's subagents read at startup.

### Gates

evo introduces **gates**: pass/fail checks that run on every experiment. An experiment that fails a gate is discarded even if its score beats the current best. Without gates, the search will find ways to return a constant, skip work, or trade correctness for speed.

Any command that exits zero on pass and non-zero on fail qualifies as a gate: a test suite, an invariant script, a score floor on a held-out slice of the benchmark. Gates inherit down the experiment tree: a gate registered at the root runs on every descendant. Narrower gates can be attached to specific branches.

When `discover` builds a benchmark from scratch, it attaches a held-out-slice score-floor gate automatically. When the benchmark already exists in the repo, gates are opt-in.

## Where experiments run

| Backend | Where | Install |
|---|---|---|
| **worktree** *(default)* | local git worktree per experiment | included |
| **pool** | reuse a fixed set of local workspaces | included |
| **ssh** | your own SSH host | included |
| **modal** | Modal serverless cloud | `uv tool install 'evo-hq-cli[modal]'` |
| **e2b** | E2B cloud sandboxes | `uv tool install 'evo-hq-cli[e2b]'` |
| **daytona** | Daytona cloud workspaces | `uv tool install 'evo-hq-cli[daytona]'` |
| **aws** | AWS EC2 sandboxes | `uv tool install 'evo-hq-cli[aws]'` |
| **azure** | Azure VMs | `uv tool install 'evo-hq-cli[azure]'` |

Pick and configure in the dashboard's Backend tab.

## Dashboard

The dashboard starts automatically with `/evo:discover` (or `evo init`) and prints the URL in chat:

```
Dashboard live: http://127.0.0.1:8080 (pid 12345)
```

If `8080` is in use, evo increments to the next free port (`8081`, `8082`, …) and prints it. Subsequent runs reuse the chosen port. Start it manually with:

```bash
uv run --project /path/to/evo/plugins/evo evo dashboard --port 8080
```

## Upgrading

```bash
evo update                           # update CLI + every installed host
evo update <host>                    # update one host (also bumps CLI to match)
evo update <host> --version 0.4.1    # pin to a release
```

Every `evo install` / `evo update` keeps the CLI on PATH in lockstep with the host plugin version it just installed (`uv tool install --force evo-hq-cli` under the hood). Without a `--version` pin that resolves to the latest **stable** release, so running an unpinned `evo install`/`evo update` against a pre-release pulls the CLI back to stable — pin both sides for an alpha (see [Testing a pre-release](#testing-a-pre-release-alpha)). The CLI binary, the skill files, and the hook protocol share wire formats — letting them drift caused silent failures in earlier versions. Editable installs (`uv tool install --editable`, `pip install -e`) are detected and left untouched.

See `evo update --help` for `--force`, `--scope`, and additional flags.

### Migrating from any pre-0.4.4 version

```bash
uv tool install --force evo-hq-cli && evo update --force
```

`--force` wipes the host plugin cache and reinstalls, working around [anthropics/claude-code#14061](https://github.com/anthropics/claude-code/issues/14061): `/plugin update` returns success but does not replace cached plugin files.

### Hooks failing with exit 127

The host lost evo's hook binary. Fixed in 0.5.1; reinstall the host to repair:

```bash
uv tool install --force evo-hq-cli && evo install codex --force   # or: evo install claude-code --force
```

`evo doctor <host>` confirms the result.

### Testing a pre-release (alpha)

`uv` and `pip` skip pre-releases by default. To install an alpha, pin both the CLI version and the host plugin tag:

```bash
uv tool install --force 'evo-hq-cli==0.4.1a2' && \
  evo update --version 0.4.1-alpha.2 --force
```

Substitute the target alpha version. The CLI uses PEP 440 form (`0.4.1a2`); the marketplace tag uses the dash form (`v0.4.1-alpha.2`).

## Telemetry

evo sends anonymous telemetry and usage stats that helps us improve evo.
Disable it globally anytime:

```bash
evo telemetry off
```

Or for one command/session:

```bash
EVO_TELEMETRY=0 evo ...
```

## Dev install

For development on evo:

```bash
git clone https://github.com/evo-hq/evo
cd evo
uv tool install --editable plugins/evo
```

## License

Apache-2.0. See [LICENSE](LICENSE).

## Citation

If you use evo in your work, please cite it (see [`CITATION.cff`](CITATION.cff)):

```bibtex
@software{bishoyi_evo,
  author = {Bishoyi, Alok Kumar},
  title  = {{evo: an autoresearch orchestrator for codebases}},
  url    = {https://github.com/evo-hq/evo},
  doi    = {10.5281/zenodo.20447923},
  year   = {2026}
}
```

## Docs

### CITATION.cff
cff-version: 1.2.0
message: "If you use evo in your research, please cite it as below."
title: "evo: an autoresearch orchestrator for codebases"
abstract: >-
  evo is a plugin for agentic frameworks that optimizes code through
  experiments. Given a codebase, it discovers metrics to optimize, sets up the
  evaluation, and runs experiments in a loop using tree search over parallel
  semi-autonomous agents, keeping changes that improve the score and discarding
  those that do not.
type: software
authors:
  - family-names: Bishoyi
    given-names: Alok Kumar
repository-code: "https://github.com/evo-hq/evo"
url: "https://github.com/evo-hq/evo"
license: Apache-2.0
version: 0.8.0
date-released: 2026-07-17
keywords:
  - autoresearch
  - code-optimization
  - agentic
  - tree-search
  - experiment-driven-development
# Zenodo concept DOI (resolves to the latest version).
doi: 10.5281/zenodo.20447923

### plugins/evo/.claude-plugin/plugin.json
{
  "name": "evo",
  "version": "0.8.0",
  "description": "Structured experiment-driven code optimization using tree search and parallel subagents"
}

### plugins/evo/pyproject.toml (excerpt)
[project]
name = "evo-hq-cli"
version = "0.8.0"
description = "Structured experiment-driven code optimization with git worktrees, traces, and a local dashboard. CLI for the evo plugin (Claude Code, Codex)."
requires-python = ">=3.10"
license = "Apache-2.0"
license-files = ["LICENSE", "NOTICE"]
readme = "README.md"
dependencies = [
  "flask>=3.0.0",
  "portalocker>=2.8.0",
  "pyyaml>=6.0.0",
  "requests>=2.31.0",
]

[project.optional-dependencies]
# Remote-sandbox provider SDKs. Install with `evo-hq-cli[modal]` or
# `evo-hq-cli[all]`. Each provider's evo adapter lazy-imports its SDK
# inside its module so users who don't want a given provider don't
# carry its deps.
modal = [
    "modal>=0.62.0",
]
e2b = [
    "e2b>=2.20.0",
]
daytona = [
    "daytona>=0.170.0",
]
aws = [
    "boto3>=1.42.66",
]
azure = [
    "azure-identity>=1.17.1",
    "azure-mgmt-resource>=23.1.1",
    "azure-mgmt-network>=28.0.0",
    "azure-mgmt-compute>=34.0.0",
]
all = [
    "modal>=0.62.0",
    "e2b>=2.20.0",
    "daytona>=0.170.0",
    "boto3>=1.42.66",
    "azure-identity>=1.17.1",
    "azure-mgmt-resource>=23.1.1",
    "azure-mgmt-network>=28.0.0",
    "azure-mgmt-compute>=34.0.0",
]
mcp = [
    "mcp>=1.0.0",
]

[project.urls]
Homepage = "https://github.com/evo-hq/evo"
Repository = "https://github.com/evo-hq/evo"
Issues = "https://github.com/evo-hq/evo/issues"

[project.scripts]
evo = "evo.cli:main"
evo-dashboard = "evo.dashboard:main"
evo-drain = "evo.inject.drain:main"

[project.entry-points."hermes_agent.plugins"]
evo = "evo.hermes_plugin"

[build-system]
requires = ["setuptools>=68.0.0"]
build-backend = "setuptools.build_meta"

[tool.setuptools]
package-dir = {"" = "src"}
# evo-hook-drain ships as a per-platform Rust binary fetched at install
# time from the GitHub release. The CLI wheel itself doesn't carry binaries.
script-files = []

[tool.setuptools.packages.find]
where = ["src"]

[tool.setuptools.package-data]
evo = ["static/*", "opencode_plugin/*.js", "openclaw_plugin/*.js", "openclaw_plugin/native/*.js", "openclaw_plugin/native/*.json", "openclaw_plugin/native/*.md"]

### plugins/evo/README.md
# evo

The evo plugin for Claude Code and Codex. Ships the evo:discover and
evo:optimize skills plus a bundled `bin/evo` wrapper.

For installation, usage, and documentation, see the main repo README:
https://github.com/evo-hq/evo

### Skill surface (from plugins/evo/skills/*/SKILL.md headers)

Skills present under `plugins/evo/skills/`: discover, optimize, ship, report, subagent, finetuning, infra-setup, references.

- **discover** — Initialize evo for the current repository: explore codebase, propose optimization dimensions, construct benchmark in a baseline worktree, run first experiment. Invoked as `/evo:discover`.
- **optimize** — Drive structured autoresearch after discover: orchestrator plans/spawns optimization subagents; knobs `subagents=N`, `budget=N`, `stall=N` (default stall 5). Candidate edits belong to subagents, not the orchestrator.
- **ship** — Distill best valid experiment into a mergeable change (PR or merge) + mergeability report.
- **subagent** — Iteration protocol + brief field shape loaded by each optimization subagent on first turn.
- **finetuning** — When task is finetuning / post-training / training a model (references for RL/ART, SFT/Tinker, serving/vLLM).
- **infra-setup** — Remote backends, pooled workspaces, provider auth (provider-matrix.md).
- **report** — Reporting skill (present in tree).

Subagent types referenced: `evo:benchmark-reviewer`, `evo:ideator` (failure_analysis / literature / frontier_extrapolation), `evo:verifier` (mandatory pre and post every evo run).

## Top-level structure

- `.agents/` — agent plugin packaging (plugins)
- `.claude-plugin/` — Claude Code marketplace plugin manifest at repo root
- `.github/workflows/` — CI
- `CITATION.cff` — citation metadata (author Alok Kumar Bishoyi; DOI 10.5281/zenodo.20447923; version 0.8.0)
- `LICENSE` / `NOTICE` — Apache-2.0
- `README.md` — primary product docs
- `assets/` — banner + dashboard screenshots
- `plugins/evo/` — main installable plugin + CLI package (`evo-hq-cli` via uv)
  - `skills/` — discover, optimize, ship, report, subagent, finetuning, infra-setup + shared references
  - `src/evo/` — Python package: backends (worktree/pool/ssh + sandbox_providers), hosts adapters, hermes/openclaw/opencode plugins, inject, static dashboard assets, host_install
  - `hooks/`, `commands/`, `agents/`, `bin/` (incl. Rust `evo-hook-drain-rs`), `npm/` (Cursor/Codex-style skill packaging)
  - `.claude-plugin/`, `.codex-plugin/`, `.kimi-plugin/` — per-host manifests
- `sdk/` — `python` (`evo_agent`) and `node` instrumentation SDKs for benchmarks
- `scripts/` — helpers (cursor_hook_probe, rlm_eval)
- `tests/` — e2e + fixtures (auto_harness_demo, inject_drain)

### backends listing
file	__init__.py
file	gitdir.py
file	pool.py
file	pool_state.py
file	protocol.py
file	remote.py
file	remote_state.py
dir	sandbox_providers
file	state_keys.py
file	worktree.py

### sandbox_providers
file	__init__.py
file	_common.py
file	aws.py
file	azure.py
file	daytona.py
file	e2b.py
file	manual.py
file	modal.py
file	ssh.py

### hosts
file	__init__.py
file	claude_fork.py

### sdk
dir	node
dir	python

### tests
file	_sandbox_agent_fixture.py
file	_sshd_fixture.py
file	conftest.py
dir	e2e
dir	fixtures
dir	live
dir	skills
dir	unit
