---
type: source
source_url: https://github.com/gsd-build/get-shit-done
tags:
  - meta-prompting
  - context-engineering
  - spec-driven-development
  - subagent-orchestration
  - context-rot
  - multi-agent
  - claude-code
  - skill-commands
related:
  - obra-superpowers
  - shareai-lab-learn-claude-code
  - anthropic.com-managed-agents
  - github-spec-kit
  - langchain.com-langgraph
  - forrestchang-andrej-karpathy-skills
  - coleam00-archon
  - gastownhall-beads
  - snarktank-ralph
  - bmad-code-org-bmad-method
  - othmanadi-planning-with-files
product: gsd
detail_level: standard
created: 2026-05-14
updated: 2026-05-25
---

GSD (Get Shit Done) is a lightweight meta-prompting, context engineering, and spec-driven development system for AI coding agents — with 62,040 stars and MIT license, it is one of the highest-starred agent harness toolkits in the ecosystem. Built by TÂCHES for solo developers who rely entirely on Claude Code and similar agents, it solves *context rot*: the quality degradation that accumulates as an agent's context window fills up. The core mechanism is a six-command loop that keeps the main context clean by delegating all heavy work to fresh-context subagents — researchers, planners, executors, and verifiers that each start with a full 200k-token window and nothing else.

_All claims below are sourced from ../../raw/github/gsd-build-get-shit-done.md unless otherwise noted._

## What it does

GSD sits between the user and AI coding agents (Claude Code, OpenCode, Gemini CLI, Kilo, Codex, Copilot, Cursor, Windsurf) and imposes a structured development pipeline on top of them. It replaces ad-hoc prompting with a mandatory sequence: initialize a project (questions → research → requirements → roadmap), discuss implementation decisions phase by phase, plan each phase (research → plan → verify in a loop), execute plans in parallel waves via subagents, verify what was built, then ship. Each phase produces structured Markdown artifacts — `PROJECT.md`, `REQUIREMENTS.md`, `ROADMAP.md`, `STATE.md`, `CONTEXT.md` — that persist across sessions and context resets.

## Key features

- **Six-command core loop** — `/gsd-new-project`, `/gsd-discuss-phase`, `/gsd-plan-phase`, `/gsd-execute-phase`, `/gsd-verify-work`, `/gsd-ship` map to discrete pipeline stages with no manual wiring.
- **Fresh-context subagents** — every researcher, planner, executor, and verifier gets a clean 200k-token window; the orchestrating session stays at 30–40% utilization.
- **Parallel execution waves** — independent plans run concurrently; each task produces one atomic git commit.
- **Persistent structured state** — all state lives in `.planning/` as human-readable Markdown and JSON; survives `/clear` and session restarts.
- **Two-stage hierarchical routing (v1.40)** — six namespace meta-skills (`gsd-workflow`, `gsd-project`, `gsd-quality`, `gsd-context`, `gsd-manage`, `gsd-ideate`) reduce eager skill-listing token cost from ~2,150 to ~120 tokens per turn.
- **Configurable quality gates** — `config.json` toggles the research agent, plan-checker, and verifier independently; `mode: yolo` auto-approves every gate.
- **Install profiles** — `--profile=core` (6 commands), `--profile=standard` (core + phase management), or full install; profiles compose.
- **Runtime surface control** — `/gsd:surface` enables/disables skill clusters at runtime without reinstall.
- **Multi-runtime support** — installs to Claude Code, OpenCode, Gemini CLI, Kilo, Codex, Copilot, Cursor, Windsurf, Antigravity, Trae, Cline, Augment Code.

## Architecture

GSD is layered into four tiers. The **Command Layer** (`commands/gsd/*.md`) holds user-facing slash commands installed as custom slash commands (Claude Code / OpenCode / Copilot / Kilo), skills (Codex), or namespaced commands under `gsd:` (Gemini CLI). The **Workflow Layer** (`get-shit-done/workflows/*.md`) contains thin orchestrators that load context via `gsd-sdk query`, spawn specialized subagents with focused prompts, collect results, and update state. The **CLI Tools Layer** (`sdk/`) bridges Markdown prompts to a programmatic TypeScript SDK (`GSDTools/query-runtime-bridge.ts`), providing stable init handlers and query endpoints regardless of which AI runtime is invoking a workflow. The **File System** (`.planning/`) stores all persistent project state as human-readable Markdown and JSON — no database, no external service.

The v1.40 two-stage routing model adds six namespace meta-skills above the ~86 concrete sub-skills: the model sees only the 6 namespace routers at call time, selects a namespace, then routes to the concrete sub-skill via an embedded routing table. This approach was validated by Tool Attention research showing keyword-dense tags outperform prose at ~40% the token cost for routing decisions.

## Installation

```bash
npx get-shit-done-cc@latest
```

Works on Mac, Windows, and Linux. The interactive installer prompts for runtime and scope (global or local). Non-interactive flags are available for all 15 supported runtimes. For containers or Docker, set `CLAUDE_CONFIG_DIR` before installing:

```bash
CLAUDE_CONFIG_DIR=/home/youruser/.claude npx get-shit-done-cc --global
```

After install, restart the runtime. Commands appear as `/gsd-*` (Claude Code, Copilot), `$gsd-*` (Codex), or `/gsd:*` (Gemini CLI).

## Example usage

```
# Start a new project
/gsd-new-project

# Capture design decisions for phase 1
/gsd-discuss-phase 1

# Plan phase 1 (research → plan → verify loop)
/gsd-plan-phase 1

# Execute all plans for phase 1 in parallel waves
/gsd-execute-phase 1

# Walk through what was built; diagnose and fix failures
/gsd-verify-work 1

# Ship phase 1 as a PR
/gsd-ship 1
```

For existing codebases, run `/gsd-map-codebase` first to index the stack, architecture, and conventions before `/gsd-new-project`.

## When to use

GSD is the right choice for developers — especially solo or small-team — who want to build entire features or products using AI coding agents as the primary implementers. It is most valuable when: (a) sessions grow long enough for context rot to degrade output quality, (b) you need results to survive across multiple sessions, or (c) you want parallel execution of independent tasks without manually managing multiple agent windows. It is overkill for small one-off scripts or fixes where a single prompt suffices.

## Maintenance status

62,040 stars, 5,261 forks, JavaScript/TypeScript, last pushed 2026-05-14. Latest release v1.42.0-rc4 (pre-release). MIT License. Actively maintained by the TÂCHES / gsd-build team; the project ships frequent RC releases with a full CHANGELOG, ADR library, and a Vitest test suite including workflow size-budget enforcement. Community via Discord and X (@gsd_foundation).

## Ecosystem

GSD ships as an npm package (`get-shit-done-cc`) and installs into the same `~/.claude/skills/` path used by [[anthropics-skills]] and [[skills.sh]]. Its two-stage routing research connects directly to the Tool Attention literature on skill-listing token costs. The project's context-rot framing echoes the harness failure modes documented in [[anthropic.com-managed-agents]] (context anxiety) and the multi-agent orchestration patterns in [[langchain.com-langgraph]]. The `.planning/` file-based state model is the same pattern described in [[shareai-lab-learn-claude-code]] (file-based task graphs, session 7). [[obra-superpowers]] takes a complementary approach — skills that auto-trigger rather than explicit commands — and the two are often compared by users choosing between them.
