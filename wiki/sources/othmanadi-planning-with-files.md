---
type: source
category: "Spec-driven dev, planning & tasks"
source_url: https://github.com/OthmanAdi/planning-with-files
tags:
  - context-engineering
  - persistent-memory
  - manus-pattern
  - claude-code-skill
  - task-planning
  - agent-hooks
  - multi-ide
  - filesystem-as-memory
related:
  - anthropics-skills
  - obra-superpowers
  - bmad-code-org-bmad-method
  - anombyte93-prd-taskmaster
  - gsd-build-get-shit-done
  - forrestchang-andrej-karpathy-skills
  - backnotprop-plannotator
  - the-new-sdlc-with-vibe-coding
product: planning-with-files
detail_level: standard
created: 2026-05-25
updated: 2026-06-30
---

Planning with Files is the most-starred agent-skill implementation of Manus-style persistent markdown planning (22k+ stars, 1,954 forks), packaged as a multi-IDE SKILL.md skill that teaches AI coding agents to use three markdown files — `task_plan.md`, `findings.md`, and `progress.md` — as persistent working memory across context resets. It operationalises the core principle from Manus AI ("markdown is my working memory on disk") that underpinned Meta's $2B acquisition, and benchmarks show a jump from 6.7% to 96.7% task-completion pass rate when the skill is active versus baseline Claude Code.

_All claims below are sourced from ../../raw/github/othmanadi-planning-with-files.md unless otherwise noted._

## What it does

Planning with Files installs as a Claude Code plugin and/or SKILL.md skill and enforces a three-file planning discipline on every multi-step task. On session start it creates `task_plan.md` (phases + checkboxes), `findings.md` (accumulated research), and `progress.md` (session log + error history). A PreToolUse hook re-reads the plan before major tool calls (attention manipulation), a PostToolUse hook reminds the agent to update progress after file writes, and a Stop hook verifies all plan phases are checked off before the session terminates. The skill ships in six languages (English, Arabic, German, Spanish, Simplified and Traditional Chinese) and includes parallel plan isolation (slug-mode directories under `.planning/YYYY-MM-DD-slug/`) introduced in v2.36.0 for multi-session workflows.

## Key features

- **3-file pattern**: `task_plan.md` (phases/checkboxes), `findings.md` (knowledge store), `progress.md` (session log + error tracking) — filesystem as persistent RAM
- **Lifecycle hooks**: PreToolUse (re-read plan), PostToolUse (update progress reminder), Stop (completion verification), PreCompact (flush before `/compact`)
- **Hash attestation** (v2.37.0+): `/plan-attest` locks `task_plan.md` with SHA-256; hooks block injection on tamper
- **Parallel plan isolation** (v2.36.0+): `init-session.sh` slug mode, `set-active-plan.sh`, `resolve-plan-dir.sh` support concurrent plan directories
- **17+ IDE support**: full hook parity on Claude Code, Cursor, Codex, Gemini CLI, Kiro, Hermes, CodeBuddy, FactoryAI, OpenCode, Mastra Code, GitHub Copilot; standard skill install on Continue, Pi, OpenClaw, Antigravity, Kilocode, AdaL CLI
- **Slash commands**: `/planning-with-files:plan` (`/plan` autocomplete), `/plan:status`, `/plan-goal`, `/plan-loop`
- **Multi-language**: English, Arabic, German, Spanish, Chinese Simplified, Chinese Traditional skill variants
- **Security hardening** (v2.36.1+): stop hook cache search removed, PowerShell ExecutionPolicy tightened, prompt injection delimiters

## Architecture

The skill is structured as a Claude Code plugin (`/.claude-plugin/`) that delivers a SKILL.md file, hook scripts, and planning templates. The canonical English skill lives in `skills/planning-with-files/` with `SKILL.md`, `examples.md`, `reference.md`, `templates/`, and `scripts/` (init-session.sh, check-complete.sh, set-active-plan.sh, resolve-plan-dir.sh, attest-plan.sh). Fourteen IDE-specific adapter directories (`.cursor/`, `.codex/`, `.gemini/`, `.github/`, `.kiro/`, `.mastracode/`, `.opencode/`, `.pi/`, `.codebuddy/`, `.factory/`, `.continue/`, `.hermes/`, `.claude-plugin/`, `.pi/`) each carry their own SKILL.md variant pinned to the same version string — a 19-file version bump is required per release. The `scripts/` shell and PowerShell scripts map to IDE lifecycle events; the `templates/` directory holds starter `task_plan.md`, `findings.md`, and `progress.md` files. A `tests/` suite runs 130 tests with `pytest`.

## Installation

```bash
# Universal (npx skills, works on 40+ agents)
npx skills add OthmanAdi/planning-with-files --skill planning-with-files -g

# Claude Code plugin (adds /plan autocomplete commands)
/plugin marketplace add OthmanAdi/planning-with-files
/plugin install planning-with-files@planning-with-files
```

For non-plugin usage, copy the skill to `~/.claude/skills/planning-with-files/` (macOS/Linux: `cp -r ~/.claude/plugins/cache/planning-with-files/planning-with-files/*/skills/planning-with-files ~/.claude/skills/`).

## Example usage

```
# After install, start a task:
/plan         → triggers /planning-with-files:plan — creates task_plan.md, findings.md, progress.md

# Check progress:
/plan:status  → shows current phase completion at a glance

# Attest a locked plan:
/plan-attest  → writes SHA-256 to .attestation; hooks reject tampered task_plan.md

# Session recovery after /clear:
# The SessionStart hook auto-detects previous session data and shows a catchup report
```

## When to use

Use this skill for any task with 3+ steps, research tasks, project builds, or anything spanning many tool calls. The pattern is counterproductive for simple single-turn questions, single-file edits, or quick lookups — the overhead of maintaining three planning files exceeds the benefit. It is most effective when context resets (`/clear`, `/compact`, autoCompact) are likely, since the persistent markdown files survive context loss while the in-memory TodoWrite tool does not.

## Maintenance status

22,015 stars, 1,954 forks as of May 2026; v2.41.0 released 2026-05-24. Actively maintained with a community of contributors (see `CONTRIBUTORS.md`). A `scripts/bump-version.py` ensures parity across all 19 SKILL.md variants. The AGENTS.md includes a strict 12-step release checklist and prohibits auto-commit Co-Authored-By trailers. Community forks include devis (interview workflow), multi-manus-planning (multi-project), and plan-cascade (multi-level orchestration). Licensed MIT.

## Ecosystem

The skill distributes via `npx skills add` ([[skills.sh]] / vercel-labs/skills registry), via the Anthropic Claude Code plugin marketplace, and via ClawHub (manual upload required after each release). It is part of the same SKILL.md ecosystem as [[anthropics-skills]], [[obra-superpowers]], and [[gsd-build-get-shit-done]]. The Manus-pattern planning discipline it encodes is conceptually related to the phase-driven methodology of [[bmad-code-org-bmad-method]] and the PRD-first task management of [[anombyte93-prd-taskmaster]]. [[forrestchang-andrej-karpathy-skills]] documents Karpathy's own Claude Code context-engineering notes, which overlap with the filesystem-as-memory principle this skill operationalises.
