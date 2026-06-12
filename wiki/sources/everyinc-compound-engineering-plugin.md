---
type: source
source_url: https://github.com/EveryInc/compound-engineering-plugin
tags:
  - compound-engineering
  - claude-code-plugin
  - agentic-workflow
  - code-review
  - knowledge-compounding
  - multi-agent
  - codex
  - cursor
  - copilot
  - every.to
related:
  - agent-field-pr-af
  - backnotprop-plannotator
  - garrytan-gstack
  - shadcn-improve
product: compound-engineering-plugin
detail_level: standard
created: 2026-05-25
updated: 2026-06-12
---

Every's Compound Engineering plugin is a comprehensive AI-agent workflow suite for Claude Code, Codex, Cursor, Copilot, and other coding agents that operationalizes the philosophy that each unit of engineering work should make subsequent units easier. With 17k+ stars and 1,300+ forks it is one of the most widely adopted coding-agent plugin packages, shipping 38+ skills and 50+ specialized review, research, and workflow agents in a single installable plugin.

_All claims below are sourced from ../../raw/github/everyinc-compound-engineering-plugin.md unless otherwise noted._

## What it does

The plugin installs a structured engineering loop as slash commands directly inside supported agents. The loop is deliberately front-loaded: 80% planning and review, 20% execution. Skills like `/ce-brainstorm` and `/ce-plan` produce durable artifacts (requirements docs, implementation plans, `STRATEGY.md`) that subsequent agent invocations read as grounding, so every session starts from richer context than the last. After execution, `/ce-code-review` and `/ce-compound` close the loop by catching issues and writing learnings into a searchable knowledge base that agents can retrieve in future runs.

## Key features

- **Full engineering loop** — `/ce-strategy` → `/ce-ideate` → `/ce-brainstorm` → `/ce-plan` → `/ce-work` → `/ce-debug` → `/ce-code-review` → `/ce-compound` → `/ce-compound-refresh`. Each step produces a persisted artifact consumed by the next.
- **38+ skills** covering core workflow, research, git workflow, review and quality, content collaboration, automation, and beta/experimental capabilities.
- **50+ specialized agents** — tiered review agents (correctness, security, performance, maintainability, testing, architecture, adversarial), document review agents, research agents (web, Slack, git history, session historian, learnings search), design agents, and workflow agents.
- **Multi-platform install** — native plugin install for Claude Code, Codex (TUI + Bun agent step), Cursor, GitHub Copilot (VS Code and CLI), Factory Droid, and Qwen Code; Bun/TypeScript converter for OpenCode, Pi, Gemini CLI, and Kiro.
- **`/ce-product-pulse`** — time-windowed usage/performance/error report saved to `docs/pulse-reports/`, forming a browseable timeline of user outcomes that anchors the next `/ce-strategy` update.
- **`/ce-optimize`** — iterative optimization loops with parallel experiments, measurement gates, and LLM-as-judge quality scoring.
- **Session history search** — `/ce-sessions` and the `ce-session-historian` agent query prior Claude Code, Codex, and Cursor sessions for related investigation context, making past work reusable across sessions.

## Architecture and concepts

The repo has three distinct surfaces that can each change independently: the `compound-engineering` plugin under `plugins/compound-engineering/` (skills + agents), the Claude marketplace catalog under `.claude-plugin/`, and the Bun/TypeScript converter CLI in `src/`. Release automation (`release-please`) tracks all three with linked versioning that keeps the CLI and plugin at the same version number.

Skills are self-contained directories under `plugins/compound-engineering/skills/`; agents live under `plugins/compound-engineering/agents/`. Both layers are cached at session start by Claude Code — edits to skill or agent prose don't propagate within an open session. The recommended test loop for behavioral changes uses the `skill-creator` skill, which injects current source into a subagent at dispatch time rather than relying on the cached plugin loader.

The converter CLI (`bunx @every-env/compound-plugin install compound-engineering --to <target>`) translates Claude Code-format plugins into the native formats of Codex, OpenCode, Pi, Gemini CLI, and Kiro. A cleanup command (`--cleanup --target <target>`) sweeps stale flat-install artifacts left by older Bun-only installs.

`STRATEGY.md` is a special anchor file created by `/ce-strategy` at the repo root. It captures the product's target problem, approach, persona, key metrics, and development tracks. Skills `/ce-ideate`, `/ce-brainstorm`, and `/ce-plan` read it as grounding when present, so strategic choices propagate automatically through feature ideation, requirements, and implementation plans without re-stating them each session.

## Main APIs / commands

| Command | Purpose |
|---------|---------|
| `/ce-strategy` | Create/update `STRATEGY.md` anchor |
| `/ce-ideate` | Generate and critically evaluate big-picture ideas before brainstorming |
| `/ce-brainstorm` | Interactive Q&A → right-sized requirements doc |
| `/ce-plan` | Requirements doc → detailed implementation plan with confidence checking |
| `/ce-work` | Execute plan items systematically |
| `/ce-debug` | Reproduce failure → causal chain → test-first fix |
| `/ce-code-review` | Multi-agent tiered review (10+ reviewer agents in parallel) |
| `/ce-compound` | Write solved-problem learning to knowledge base |
| `/ce-compound-refresh` | Refresh stale or drifting learnings |
| `/ce-optimize` | Parallel experiments + LLM-as-judge quality scoring loop |
| `/ce-product-pulse` | Time-windowed usage/error/perf pulse report |
| `/ce-sessions` | Query session history across agents |
| `/ce-setup` | Diagnose environment, install tools, bootstrap project config |

## When to use

Use Compound Engineering when shipping software with AI agents and the primary friction is context loss between sessions, inconsistent review quality, or knowledge that only exists in one person's head. The plugin is most effective on projects where the same codebase is worked on repeatedly — each `/ce-compound` invocation builds a learnings corpus that future agents query, and each `/ce-plan` reads prior plans to calibrate scope and avoid repeating mistakes. The mandatory plan-before-code pattern makes it a poor fit for pure exploratory or throw-away scripting workflows but an excellent fit for production codebases and team engineering workflows.

## Ecosystem

The plugin is published by [Every](https://every.to) and is documented on their engineering blog: [Compound engineering: how Every codes with agents](https://every.to/chain-of-thought/compound-engineering-how-every-codes-with-agents). It does not accept outside contributions (no PR merges), though bug reports are welcome and reviewed by automated agent review via `gh`. Related resources in this wiki: [[openai-codex-plugin-cc]] (Codex plugin for Claude Code), [[anthropics-skills]] (Anthropic's official skills library), [[obra-superpowers]] (skill composition patterns).

## Maintenance status

17,151 stars, 1,326 forks. Latest release: compound-engineering-v3.8.4 (2026-05-22). MIT license. Active development with versioned releases tracked in `plugins/compound-engineering/CHANGELOG.md` and GitHub Releases. The linked-versions release-please setup bumps CLI and plugin together on every release.
