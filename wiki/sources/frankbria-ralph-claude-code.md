---
type: source
source_url: https://github.com/frankbria/ralph-claude-code
tags:
  - autonomous-agent-loop
  - claude-code
  - exit-detection
  - circuit-breaker
  - rate-limiting
  - docker-sandbox
  - github-issues-import
  - shell-scripting
related:
  - snarktank-ralph
  - gsd-build-get-shit-done
  - coleam00-archon
  - q00-ouroboros
  - obra-superpowers
  - coleam00-harness-engineering-demo
  - coleam00-agent-control-plane
  - Yeachan-Heo-oh-my-claudecode
  - Chachamaru127-claude-code-harness
product: ralph-claude-code
detail_level: standard
created: 2026-06-18
updated: 2026-07-08
---

Ralph for Claude Code (9,380 stars, MIT, Shell) is a battle-tested autonomous development loop built specifically for the Claude Code CLI. Inspired by Geoffrey Huntley's Ralph pattern, this implementation by frankbria extends the concept well beyond a simple loop: it adds a dual-condition exit gate requiring both heuristic completion indicators and Claude's explicit EXIT_SIGNAL, a configurable circuit breaker with auto-recovery, session continuity across iterations, Docker and E2B cloud sandbox execution, GitHub issue lifecycle management, batch queue processing, and 784 BATS tests at 100% pass rate. It installs globally as a system-wide `ralph` command and can be enabled in any existing project via an interactive wizard.

_All claims below are sourced from ../../raw/github/frankbria-ralph-claude-code.md unless otherwise noted._

## What it does

Ralph runs Claude Code in a loop against a project defined by a `.ralph/PROMPT.md` (high-level goals), `.ralph/fix_plan.md` (prioritized task list), and `.ralph/AGENT.md` (build/run commands). Each iteration invokes the Claude Code CLI, reads the response, checks for completion signals, updates task state, and repeats. The loop exits only when both a heuristic threshold (`completion_indicators >= 2`) and Claude's explicit `EXIT_SIGNAL: true` are satisfied — preventing premature exits during productive iterations where Claude signals "phase complete" but intends to continue. Additional exit triggers include all tasks in `fix_plan.md` checked off (except items under `## Optional` / `## Future` / `## Nice to Have` headings), multiple consecutive "done" signals, and the Claude API 5-hour usage limit.

## Key features

- **Dual-condition exit gate** — exit requires both `completion_indicators >= 2` (natural language pattern detection) AND Claude's explicit `EXIT_SIGNAL: true` in its RALPH_STATUS block; `EXIT_SIGNAL: false` overrides even a high completion score.
- **Circuit breaker** — opens after 3 no-progress loops or 5 same-error loops; auto-recovers via OPEN → HALF_OPEN → CLOSED after a 30-minute cooldown; thresholds are configurable via `.ralphrc`.
- **Rate limiting** — 100 API calls/hour by default; optional `MAX_TOKENS_PER_HOUR` cap for cost control; both reset hourly with countdown timers visible in the monitor.
- **Session continuity** — persists Claude session ID across iterations via `--resume`; session expires after 24 hours with configurable timeout; auto-reset on circuit breaker open, completion, or Ctrl+C.
- **`.ralphrc` configuration** — per-project settings for project type, tool permissions (`ALLOWED_TOOLS`), Claude command, timeouts, circuit breaker thresholds, and sandbox provider.
- **`ralph-enable` wizard** — interactive 5-phase setup for existing projects: detects project type (TypeScript, Python, Rust, Go, Next.js, FastAPI), selects task source (beads, GitHub Issues, PRD), configures permissions, generates `.ralph/` directory; `ralph-enable-ci` for non-interactive/CI use.
- **GitHub issue import** — converts GitHub issue bodies (with completeness scoring 0–100) into Ralph format; auto-generates an implementation plan if the issue scores below 60; supports metadata filters (label, assignee, milestone, title pattern, state) and selection strategies (first, interactive, priority); `--include-comments` flag for plan-in-comments workflows.
- **GitHub issue lifecycle** — during development: post progress comments every N loops; on completion: close the issue, post summary, create a PR (optionally as draft), add labels, open follow-up issues for TODO/FIXME markers.
- **Batch queue** — `ralph-queue` builds a persistent queue from GitHub issues or local PRDs, respecting P0–P9 priority labels and `depends on #N` dependency syntax; `ralph --process-queue` works through items sequentially with halt-on-failure option.
- **Sandbox execution** — `--sandbox docker` binds the project directory into an isolated container (4 GB RAM, 2 CPUs, bridge network by default; credentials passed via env-file, never logged); `--sandbox e2b` uses E2B cloud with file upload/download per iteration, cost tracking (`--sandbox-max-cost`), and `--sync-include`/`--sync-exclude` filtering.
- **Live monitoring** — `ralph --monitor` opens a tmux split with `ralph-monitor` dashboard showing loop count, API calls, rate-limit countdown, and log tail; `--live` flag streams Claude's real-time output.
- **Observability** — `ralph-stats` analytics from `.ralph/logs/metrics.jsonl` (JSON Lines per-loop metrics); `--notify` for desktop notifications; `--dry-run` to simulate without API calls; log rotation at 10 MB.

## Architecture

Ralph's core is `ralph_loop.sh`, a Shell script (~800+ lines) that executes Claude Code via the CLI, parses JSON or text output to detect signals, maintains rate-limit counters and circuit breaker state in ephemeral variables, and writes state to `.ralph/` files between iterations. No LLM API is called directly — Ralph is a shell orchestrator around the `claude` CLI. The circuit breaker state machine (CLOSED/OPEN/HALF_OPEN) and session lifecycle are implemented in pure Shell.

The `.ralph/` directory separates Ralph's runtime state from the user's source code:
- `PROMPT.md` — high-level goals (Claude reads this every iteration)
- `fix_plan.md` — checkbox task list (Ralph scans for unchecked items; optional sections excluded)
- `AGENT.md` — build/test commands (auto-maintained by Ralph as it discovers project tooling)
- `specs/` — detailed requirements and reusable conventions in `specs/stdlib/`
- `logs/ralph.log` — rotating execution log; `metrics.jsonl` for per-loop analytics
- `.ralph_session` — current Claude session ID; `.ralph_session_history` — last 50 transitions
- `queue.json` — persistent batch queue

Library components live in `lib/` (`enable_core.sh`, `wizard_utils.sh`, `task_sources.sh`). The multi-provider abstraction is in-progress (ADR 0001/0002): the plan decouples Ralph from `claude` so any headless coding CLI (Codex, Gemini, OpenCode) can drive the loop via an agent adapter contract.

## Installation

```bash
git clone https://github.com/frankbria/ralph-claude-code.git
cd ralph-claude-code
./install.sh
```

Adds `ralph`, `ralph-monitor`, `ralph-setup`, `ralph-import`, `ralph-queue`, `ralph-migrate`, `ralph-enable`, and `ralph-enable-ci` to PATH. One-time system installation; then per-project setup via `ralph-enable` or `ralph-setup`.

## Example usage

```bash
# Enable Ralph in an existing project
cd my-project
ralph-enable                        # Interactive wizard

# Start the autonomous loop with monitoring
ralph --monitor

# Import from a GitHub issue (auto-scores for completeness, generates plan if needed)
ralph-import --github-issue 42 --generate-plan

# Batch: queue high-priority bugs, process sequentially
ralph-queue add --github-label "bug,P0"
ralph --process-queue

# Run in Docker sandbox with cost-controlled E2B
ralph --sandbox docker
ralph --sandbox e2b --sandbox-max-cost 5.00
```

## When to use

Ralph for Claude Code is the right choice when you want an always-on autonomous development loop for Claude Code with production-grade safeguards: you need the dual exit gate to prevent premature stops, a circuit breaker to catch stuck loops, Docker/E2B sandboxing for security isolation, or GitHub issue lifecycle automation (progress comments, PR creation, follow-up tracking). It is better suited than [[snarktank-ralph]] (the original TypeScript/Amp/Claude Code variant) when you need a richer feature set (session management, sandbox execution, GitHub integration) and are working exclusively with Claude Code rather than Amp. Compare with [[gsd-build-get-shit-done]] (explicit command-driven loop with finer human control) and [[coleam00-archon]] (DAG-based YAML workflow with multi-platform adapters and explicit approval gates).

## Maintenance status

9,380 stars, 720 forks, Shell, last pushed 2026-06-15. Active development (v0.11.5); no formal release tags but version tracked via README badges and IMPLEMENTATION_STATUS.md. MIT License. 784 tests at 100% pass rate across 34 BATS test files.

## Ecosystem

Ralph for Claude Code builds directly on Geoffrey Huntley's Ralph pattern, the same conceptual foundation as [[snarktank-ralph]] — but whereas `snarktank-ralph` is a minimal TypeScript/bash reference implementation supporting both Amp and Claude Code, `frankbria-ralph-claude-code` is a full-featured Shell system exclusively for Claude Code. The `.ralph/PROMPT.md` + `fix_plan.md` architecture is a richer variant of the `prd.json` approach in `snarktank-ralph` and the `CONTEXT.md` pattern in [[gsd-build-get-shit-done]]. The circuit breaker and session lifecycle patterns parallel the harness design discussed in [[coleam00-harness-engineering-demo]]. The `ralph-enable` wizard for project onboarding is analogous to the `os-install` flow in [[buildermethods-agent-os]]. The batch queue with priority labels and dependency parsing overlaps conceptually with [[q00-ouroboros]]'s autonomous iterative loop and [[eyaltoledano-claude-task-master]]'s task management approach. The sandbox execution feature (Docker and E2B) is unique among Ralph-pattern implementations and positions the tool for security-sensitive autonomous coding environments.
