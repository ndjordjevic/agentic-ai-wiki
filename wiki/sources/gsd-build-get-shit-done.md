---
type: source
tags: [meta-prompting, context-engineering, spec-driven-development, claude-code, copilot, cursor, codex, sub-agents, quality-gates, workflow-automation, prompt-templates]
related:
  - "[[hilash-cabinet]]"
  - "[[coleam00-claude-memory-compiler]]"
product: null
detail_level: standard
created: 2026-04-25
updated: 2026-04-27
---

GET SHIT DONE (GSD) is a high-adoption (57k+ stars) meta-prompting, context engineering, and spec-driven development system that wraps AI coding assistants — Claude Code, Copilot, Cursor, Codex, Gemini CLI, and a dozen others — in a structured workflow that solves context rot and enforces quality gates. Built by solo developer TÂCHES, it is the closest thing the Agentic AI ecosystem has to a universal project-management layer for AI-assisted software development.

_All claims below are sourced from ../../raw/github/gsd-build-get-shit-done.md unless otherwise noted._

## What It Does

GSD sits as a meta-prompting layer between the developer and an AI coding tool. Commands (markdown files with XML prompt templates) are read by the AI at invocation time; the AI then executes the embedded workflow. GSD solves three core problems:

1. **Context rot** — as Claude fills its context window, output quality degrades. GSD counteracts this with context window monitoring hooks, prompt thinning, and session management.
2. **Unstructured vibecoding** — without a planning layer, AI-generated code is inconsistent and falls apart at scale. GSD enforces a structured phase-driven lifecycle with requirements traceability.
3. **Silent quality degradation** — AI tools skip requirements, drop scope, and miss edge cases. GSD's quality gates (Nyquist validation, schema drift detection, scope reduction detection, security enforcement) fail loudly rather than silently degrade.

## Installation

```bash
npx get-shit-done-cc@latest
```

Interactive installer prompts for runtime (Claude Code, Copilot, Cursor, Codex, Gemini CLI, Windsurf, and 10+ others) and scope (global or local). Non-interactive flags:

```bash
npx get-shit-done-cc --claude --global    # Claude Code, global
npx get-shit-done-cc --copilot --global   # GitHub Copilot, global
npx get-shit-done-cc --all --global       # All runtimes
```

Recommended invocation: `claude --dangerously-skip-permissions` for frictionless automation.

## Key Features

GSD imposes a structured lifecycle of six phases per project:

| Step | Command | Purpose |
|------|---------|---------|
| 1. Initialize | `/gsd-new-project` | Question-driven scope extraction → requirements → phased roadmap |
| 2. Discuss | `/gsd-discuss-phase N` | Capture implementation decisions (gray areas) before planning |
| 3. Plan | `/gsd-plan-phase N` | Domain research + milestone breakdown + plan verification |
| 4. Execute | `/gsd-next` | Execute next milestone with parallel subagents |
| 5. Verify | `/gsd-verify-phase N` | Strict requirements-coverage verification |
| 6. UI | `/gsd-ui-phase N` | (Optional) Frontend design contract generation |

**Project state** lives in `.planning/` as plain markdown files: `PROJECT.md`, `REQUIREMENTS.md`, `ROADMAP.md`, `STATE.md`, `config.json`, and per-phase artifacts (`{phase}-CONTEXT.md`, `{phase}-RESEARCH.md`, `{phase}-PLAN.md`, `{phase}-VERIFICATION.md`).

**Agent orchestration:** GSD ships 33 specialized sub-agents in `agents/` covering research, planning, quality assurance, code review, UI, documentation, and analysis. Heavy workflows spawn parallel subagents rather than running in one long context. Agent size-budget enforcement (v1.37) limits agent prompts to 500 / 1,000 / 1,600 lines by tier.

**Quality gates:** Nyquist Validation (verification frequency matches implementation complexity), Schema Drift Detection v1.31 (flags ORM changes missing migrations), Security Enforcement v1.31 (ASVS-anchored threat model gates), Scope Reduction Detection v1.31 (prevents silent requirement dropping), Cross-Phase Regression Gate (blocks phases from breaking prior verified work), Requirements Coverage Gate (ensures all REQ-XX IDs are addressed in verification).

**Context engineering:** Context Window Monitor Hook (real-time fill tracking), Context-Window-Aware Prompt Thinning v1.36, Persistent Context Threads v1.27 (context strands spanning phases), Model Profiles (`quality` / `balanced` / `budget` / `adaptive` / `inherit`), Session Management (state save/restore).

**Recent capabilities:** Spike v1.37 (`/gsd-spike` — time-boxed experiments with Given/When/Then verdicts), Sketch v1.37 (`/gsd-sketch` — 2–3 interactive HTML mockup variants), Plan Bounce v1.36 (external validation in the planning loop), Cross-AI Execution Delegation v1.36, TDD Pipeline v1.36, GSD SDK v1.30 (queryable codebase intelligence via `gsd-sdk` CLI), Global Learnings Store v1.34 (cross-project knowledge base), Safe Undo v1.34, Workspace Support (multi-repo isolated workspaces via `/gsd-new-workspace`).

Configuration lives in `.planning/config.json`, managed via `/gsd-settings`. Key settings: `mode` (`interactive` default; `yolo` for auto-approve), `granularity` (`coarse` 3–5 phases / `standard` 5–8 / `fine` 8–12), `model_profile` (default `balanced`), `workflow.research` (default `true`), `workflow.nyquist_validation` (default `true`), `workflow.tdd_mode` (default `false`), `parallelization.max_concurrent_agents` (default `3`), `context_window` (default `200000` tokens).

## Architecture

GSD is a meta-prompting system — not a framework with runtime code. The commands in `commands/` and `get-shit-done/workflows/` are markdown files with XML-formatted prompt templates that the AI reads and executes. JavaScript/TypeScript code exists only in the installer (`bin/`), hook scripts (`hooks/`), and SDK (`sdk/`).

```
gsd-build/get-shit-done/
├── agents/           # 33 sub-agent markdown definitions
├── commands/         # Legacy command format (older Claude Code)
├── get-shit-done/    # Core: contexts/, references/, templates/, workflows/
├── hooks/            # Hook scripts (compiled to hooks/dist/)
├── docs/             # Documentation (ARCHITECTURE, FEATURES, COMMANDS, CONFIGURATION)
└── sdk/              # GSD SDK (TypeScript)
```

**Hook system** integrates with Claude Code's native hook mechanism: context monitor, workflow guard (optional), read-before-edit guard, commit-docs guard, and community hooks.

**Install targets** vary by runtime: `~/.claude/skills/` (Claude Code 2.1.88+), `~/.github/` (Copilot), `~/.cursor/` (Cursor), `~/.codex/skills/` (Codex), `~/.gemini/` (Gemini CLI), `~/.codeium/windsurf/` (Windsurf), and more.

## Example Usage

```bash
npx get-shit-done-cc@latest                # install (interactive)
claude --dangerously-skip-permissions      # recommended invocation
/gsd-new-project                           # initialize: scope → requirements → roadmap
/gsd-plan-phase 1                          # plan a phase (research + milestones + verification)
/gsd-next                                  # execute next milestone with parallel subagents
/gsd-verify-phase 1                        # strict requirements-coverage verification
/gsd-spike "evaluate library X for use case Y"   # time-boxed experiment
/gsd-settings                              # view/edit .planning/config.json
```

## Maintenance Status

Actively maintained. Latest release v1.38.3 as of 2026-04-22 (hotfix). The project releases frequently — a major version (1.3x) roughly every 2–4 weeks — and maintains a detailed `CHANGELOG.md`. Community: Discord, X (@gsd_foundation). Internationalized docs available in pt-BR, zh-CN, ja-JP, ko-KR.
