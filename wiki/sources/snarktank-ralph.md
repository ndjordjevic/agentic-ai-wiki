---
type: source
category: "Coding-agent harnesses & methodologies"
source_url: https://github.com/snarktank/ralph
tags:
  - autonomous-agent-loop
  - prd-driven-development
  - claude-code
  - amp-code
  - agentic-coding
  - iterative-agent
  - fresh-context-spawning
  - agent-skills
related:
  - coleam00-harness-engineering-demo
  - gsd-build-get-shit-done
  - obra-superpowers
  - coleam00-archon
  - anthropic.com-managed-agents
  - njbrake-agent-of-empires
  - openai-codex-plugin-cc
  - gitlawb-openclaude
  - q00-ouroboros
  - coleam00-agent-control-plane
  - frankbria-ralph-claude-code
  - Yeachan-Heo-oh-my-claudecode
  - Chachamaru127-claude-code-harness
product: ralph
detail_level: standard
created: 2026-05-20
updated: 2026-07-08
---

Ralph is an open-source autonomous AI agent loop (19,297 stars, MIT, TypeScript) that runs AI coding tools — Amp or Claude Code — repeatedly against a `prd.json` task list until all stories have `passes: true`. Each iteration spawns a fresh agent instance with a clean context window; cross-iteration memory lives only in git history, an append-only `progress.txt`, and the `prd.json` status flags. Based on Geoffrey Huntley's Ralph pattern, it was authored by Ryan Carson and is available both as a direct file copy and as a Claude Code marketplace plugin.

_All claims below are sourced from ../../raw/github/snarktank-ralph.md unless otherwise noted._

## What it does

Ralph automates the outer loop of AI-assisted software development. The developer writes a Product Requirements Document (PRD) in markdown using the `/prd` skill, converts it to a structured `prd.json` with the `/ralph` skill, then hands control to `ralph.sh`. The script selects the highest-priority user story where `passes: false`, invokes a fresh Amp or Claude Code instance with a prompt that instructs it to implement exactly one story, run quality checks (typecheck, lint, tests), commit if passing, update `prd.json`, and append learnings to `progress.txt`. The loop repeats — up to a configurable `max_iterations`, default 10 — until the agent emits `<promise>COMPLETE</promise>` (all stories pass) or the iteration cap is reached. On branch change (different `branchName` in `prd.json`), previous run artifacts are automatically archived to `archive/YYYY-MM-DD-feature-name/`.

## Key features

- **Dual-tool support** — `--tool amp` (default, uses `prompt.md`) or `--tool claude` (uses `CLAUDE.md`); switchable per invocation.
- **Fresh-context spawning** — every iteration is a completely new agent instance; no context accumulation or degradation across stories.
- **Three-file memory model** — git history (code state), `progress.txt` (learnings and discovered patterns), `prd.json` (story completion status); no external database or API required.
- **Claude Code marketplace** — installable via `/plugin marketplace add snarktank/ralph` and `/plugin install ralph-skills@ralph-marketplace`; two skills published (`/prd`, `/ralph`).
- **Auto-handoff for Amp** — with `"amp.experimental.autoHandoff": { "context": 90 }`, Amp automatically hands off when context fills, enabling stories larger than one context window.
- **Amp thread linking** — `prompt.md` records the Amp thread URL in `progress.txt` so future iterations can use `read_thread` to reference prior work.
- **AGENTS.md discipline** — each iteration's prompt instructs the agent to update the nearest `AGENTS.md` with reusable patterns and gotchas, creating a growing project knowledge base.
- **Feedback-loop requirement** — quality checks (typecheck, tests, lint) must pass before commit; broken code is never committed across iteration boundaries.
- **Browser verification** — frontend stories must include "Verify in browser using dev-browser skill" in acceptance criteria; Ralph enforces this via the iteration prompt.
- **Automatic archiving** — detects branch changes via `.last-branch` file and archives previous `prd.json` + `progress.txt` before resetting for the new feature run.

## Architecture

Ralph's architecture is deliberately minimal: a bash script (`ralph.sh`) as the orchestrator, two per-tool prompt files as the agent instructions, and two JSON files as shared state. The bash loop reads no LLM APIs directly — it simply pipes a prompt into the selected tool and inspects stdout for the completion signal. Coordination happens through the filesystem: `prd.json` (task graph with `passes` flags), `progress.txt` (append-only log with a `## Codebase Patterns` section at the top), and `AGENTS.md`/`CLAUDE.md` files updated by each iteration.

The `skills/` directory ships two SKILL.md-based capability modules: `skills/prd/` (generates a structured markdown PRD from a feature description via Q&A) and `skills/ralph/` (converts a markdown PRD to `prd.json` with user stories, acceptance criteria, and `branchName`). These skills work identically in both Amp and Claude Code because they follow the standard SKILL.md format. The `.claude-plugin/marketplace.json` and `.claude-plugin/plugin.json` manifests expose Ralph to the Claude Code plugin discovery system.

The `flowchart/` subdirectory is a standalone Next.js + React Flow application (`npm run dev`) that renders an interactive, click-through animated diagram of the Ralph loop — intended for presentations and onboarding.

## Installation

**Claude Code marketplace (recommended):**
```bash
/plugin marketplace add snarktank/ralph
/plugin install ralph-skills@ralph-marketplace
```

**Copy to project (manual):**
```bash
mkdir -p scripts/ralph
cp /path/to/ralph/ralph.sh scripts/ralph/
cp /path/to/ralph/CLAUDE.md scripts/ralph/CLAUDE.md   # for Claude Code
# OR
cp /path/to/ralph/prompt.md scripts/ralph/prompt.md   # for Amp
chmod +x scripts/ralph/ralph.sh
```

**Amp skills (global):**
```bash
cp -r skills/prd ~/.config/amp/skills/
cp -r skills/ralph ~/.config/amp/skills/
```

**Claude Code skills (global):**
```bash
cp -r skills/prd ~/.claude/skills/
cp -r skills/ralph ~/.claude/skills/
```

## Example usage

```bash
# 1. Generate PRD (via Claude Code skill)
# "Load the prd skill and create a PRD for adding user authentication"
# → saves tasks/prd-user-authentication.md

# 2. Convert PRD to prd.json
# "Load the ralph skill and convert tasks/prd-user-authentication.md to prd.json"
# → creates prd.json with userStories[], branchName, passes fields

# 3. Run the loop (Claude Code)
./scripts/ralph/ralph.sh --tool claude 15

# Each iteration prints:
# ========================================================
#   Ralph Iteration 3 of 15 (claude)
# ========================================================
# [agent implements story S-003, runs typecheck + tests, commits, updates prd.json]
# Iteration 3 complete. Continuing...

# When all stories pass:
# Ralph completed all tasks!
# Completed at iteration 7 of 15
```

## When to use

Ralph is the right choice when you have a well-scoped feature that can be decomposed into 5–20 small, independently verifiable user stories and you want an agent to work through them autonomously without human steering between stories. It works best when stories are right-sized — small enough to complete in a single context window (examples: "add a database column and migration," "add a UI component to an existing page") and when the project has reliable quality checks that catch regressions. Ralph is less suitable for exploratory work with loosely defined requirements, or for codebases without automated quality gates, since broken code compounds silently across iterations. Compare with [[gsd-build-get-shit-done]] (explicit command-driven loop, finer-grained human control) and [[coleam00-archon]] (YAML-defined DAG workflow with multi-platform adapters and explicit approval gates).

## Maintenance status

19,297 stars, 1,924 forks, TypeScript, last pushed 2026-02-02. No release tags — distributed as a copy-to-project pattern or via the Claude Code plugin marketplace. MIT License. Authored by Ryan Carson; based on Geoffrey Huntley's Ralph pattern.

## Ecosystem

Ralph sits at the intersection of PRD-driven development and fresh-context agent looping, a pattern pioneered by Huntley and operationalized here. Its skills (`/prd`, `/ralph`) follow the SKILL.md format used across [[obra-superpowers]] and the broader [[skills.sh]] ecosystem. The fresh-context-per-iteration architecture directly addresses the context anxiety failure mode documented in [[anthropic.com-managed-agents]] — instead of managing a long-running context, Ralph discards it and starts clean. The `prd.json` task graph with `passes` status flags is a simplified variant of the structured task tracking seen in [[coleam00-archon]] (DAG-based YAML) and [[gastownhall-beads]] (distributed graph issue tracker). The `progress.txt` + `AGENTS.md` memory model mirrors the cross-iteration knowledge accumulation pattern advocated in [[gsd-build-get-shit-done]]'s context engineering approach. Ralph's session orchestration layer — spawning isolated agent instances per story — shares architectural intent with [[njbrake-agent-of-empires]]'s per-agent tmux session model.
