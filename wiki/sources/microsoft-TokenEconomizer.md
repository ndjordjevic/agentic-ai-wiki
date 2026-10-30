---
type: source
category: "Knowledge, RAG, memory & context"
source_url: https://github.com/microsoft/TokenEconomizer
tags:
  - token-cost-control
  - micro-skills
  - tool-pruning
  - loop-guard
  - coding-agent-plugin
  - swe-bench
  - black-box
  - stdlib-only
related:
  - rtk-ai-rtk
  - dietrichgebert-ponytail
  - chopratejas-headroom
  - teamchong-pxpipe
  - getcaveman.dev
  - nadimtuhin-claude-token-optimizer
  - kunchenguid-compact-adviser
product: tokeneconomizer
detail_level: standard
created: 2026-10-30
updated: 2026-10-30
---

microsoft/TokenEconomizer is a UC Berkeley + Microsoft Research/Security plugin that cuts coding-agent cost in repositories you revisit by learning from prior sessions—without modifying the agent. Three black-box mechanisms (micro-skills, tool pruning, failure-loop intervention) plug into Claude Code, Codex, GitHub Copilot CLI, and Pi (experimental opencode). Paper reports 18.4–30.9% lower mean cost on SWE-Bench across five agent–model combinations, cheaper in all 30 repo×combination cells, Pass@1 up in 4 of 5.

_All claims below are sourced from ../../raw/github/microsoft-TokenEconomizer.md unless otherwise noted._

## What it does

TokenEconomizer observes finished sessions in `~/.tokeneconomizer`, then shapes later sessions:

1. **Micro-skills** — learn durable repo facts from repeated failures and a periodic model proposer (default every 3 sessions); inject confirmed facts at `SessionStart` as `additionalContext`; drop when contradicted. Off by default in the plugin (proposer uses the user’s plan); free “envfacts” layer available when enabled.
2. **Tool pruning** — drop tools unused over evidence thresholds (default 10 prompts across ≥2 sessions, or 5 sessions) by writing deny rules into the repo’s agent settings (`.claude/settings.local.json`, Codex `.codex/config.toml`, Copilot `.github/copilot/settings.local.json`); restore via one command. Catalog refresh records which tools a session actually loads.
3. **Loop guard** — mid-turn judge (confidence ≥0.7) when failures repeat; injects a redirect (at most once per turn by default), then a human-facing still-stuck notice; never aborts the turn itself. Judge/nudge run as detached `te judge` jobs charged to the session ledger.

Fails open: hook errors become no-ops and log to `~/.tokeneconomizer/errors.log`. Optimizer/judge calls use the user’s own agent CLI/login (cheapest capable model when configured).

## Installation

Requires Python 3.10+ on `PATH` (or `TE_PYTHON`) and a supported agent version (Claude Code 2.1.300–2.1.310, Codex 0.153.1–0.164.0, Copilot CLI 1.0.83–1.0.102, Pi 1.2.0–1.3.0; opencode experimental). Clone once and keep the path—plugins run from the checkout:

```bash
git clone https://github.com/microsoft/TokenEconomizer.git
# Claude Code
claude plugin marketplace add "$PWD/TokenEconomizer"
claude plugin install tokeneconomizer@tokeneconomizer
# Codex
codex plugin marketplace add "$PWD/TokenEconomizer"
codex plugin add tokeneconomizer@tokeneconomizer
# Copilot CLI
copilot plugin marketplace add "$PWD/TokenEconomizer"
copilot plugin install tokeneconomizer@tokeneconomizer
# Pi
pi install git:github.com/microsoft/TokenEconomizer
```

Then `/tokeneconomizer:status` (Codex: `$tokeneconomizer:status`; Pi: `/te status`) and once per machine `/tokeneconomizer:toolprune refresh-catalog`. One-shot without install: `claude --plugin-dir /path/to/TokenEconomizer/plugin`. Core package is **stdlib-only** (`pip` optional; `te` console script exists).

## Key features

- Experience-driven cost control across sessions in the same repo; state local to the machine.
- Hook-driven plugin packaging under `plugin/` for multiple hosts; shared mechanisms in `tokeneconomizer/{microskills,toolprune,loopguard}`.
- Unified cost ledger (`ledger` + `pricing`) so plugin overhead and experiment aggregation cannot drift.
- Settings per mechanism (`microskills`, `toolprune=auto|propose`, loopguard presets including `aggressive`).
- Documented coexistence with [[rtk-ai-rtk]] (tool-output filtering) in `plugin/README.md`.
- Benchmark reproduction under `experiments/` (SWE-Bench, Web-Bench, security-audit suites)—not part of the installable package.

## Architecture

Mechanisms are agent-agnostic; specificity enters via:

- `tokeneconomizer.trace` — per-agent session-log readers
- `domain.DomainAdapter` — LiveAdapter for the plugin vs benchmark adapters in `experiments/te_bench`
- `stage.Stage` hooks (`before_task`, `build_tools`, `run_kwargs`, `after_task`)

Callers: **plugin** (live hooks + detached `te fold`/`te judge`) and **experiments** (`Economizer` facade). Tests pin that mechanisms never import `plugin` and `tokeneconomizer/` never imports `experiments/`.

## Example usage

```text
# After install, in an agent session:
/tokeneconomizer:status
/tokeneconomizer:toolprune refresh-catalog
/tokeneconomizer:toolprune            # list denied tools + evidence
/tokeneconomizer:toolprune restore
/tokeneconomizer:config set toolprune=propose
```

Or from a repo terminal: `~/.tokeneconomizer/bin/te --host claude status`.

## Maintenance status

954 stars, 75 forks, Python, default branch `main`, latest release v0.1.0 (2026-10-26), Apache-2.0, pushed 2026-10-30. Authors from UC Berkeley, Microsoft Research, and Microsoft Security; arXiv 2610.22732; project site tokeneconomizer.github.io. Supported agent version windows are narrow and explicitly version-gated in the README.
