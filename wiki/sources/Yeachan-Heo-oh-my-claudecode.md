---
type: source
category: "Coding-agent harnesses & methodologies"
source_url: https://github.com/Yeachan-Heo/oh-my-claudecode
tags: [claude-code-plugin, multi-agent-orchestration, hook-based-routing, skill-based-routing, team-orchestration, magic-keywords, model-routing]
related: [obra-superpowers, gsd-build-get-shit-done, ruvnet-ruflo, frankbria-ralph-claude-code, snarktank-ralph, tmuxai.dev, Chachamaru127-claude-code-harness]
product: oh-my-claudecode
detail_level: standard
created: 2026-07-06
updated: 2026-07-08
---

oh-my-claudecode (OMC, npm package `oh-my-claude-sisyphus`, 37k+ stars, MIT, TypeScript, v4.15.2) is a Claude Code plugin that turns natural-language prompts and magic keywords into structured multi-agent orchestration with zero configuration. It layers hooks, skills, agents, and compaction-resistant state on top of a stock Claude Code session so that phrases like `autopilot build me a todo app` or `ralph: refactor auth` trigger full pipelines automatically, without the user learning any command syntax.

_All claims below are sourced from ../../raw/github/Yeachan-Heo-oh-my-claudecode.md unless otherwise noted._

## What it does

OMC installs as a Claude Code plugin (`/plugin marketplace add` + `/plugin install oh-my-claudecode`) or as a global npm CLI (`npm i -g oh-my-claude-sisyphus`, exposing both `oh-my-claudecode` and the `omc` alias). A `UserPromptSubmit` hook scans every prompt for magic keywords and injects the matching skill; a `Stop` hook enforces persistent modes (ralph/ultrawork) so Claude cannot end a session with unverified work. Team is the canonical multi-agent surface as of v4.1.7 (the legacy `swarm` keyword was removed): `/team 3:executor "fix all TypeScript errors"` runs a staged `team-plan → team-prd → team-exec → team-verify → team-fix` pipeline of in-session Claude agents, while `omc team N:codex|gemini|antigravity|grok|cursor|claude "..."` spawns real tmux-pane CLI workers for the equivalent provider, dying on completion with no idle resource usage.

## Installation

```bash
/plugin marketplace add https://github.com/Yeachan-Heo/oh-my-claudecode
/plugin install oh-my-claudecode
# or: npm i -g oh-my-claude-sisyphus@latest
/setup            # or: omc setup
```

If launched via `omc --plugin-dir <path>` or `claude --plugin-dir <path>`, `omc setup --plugin-dir-mode` (or `OMC_PLUGIN_ROOT`) avoids duplicating skills/agents the plugin already provides at runtime. Requires the Claude Code CLI plus a Claude Max/Pro subscription or API key; `omc team` and rate-limit auto-resume additionally require tmux (native on macOS/Linux, `psmux` on Windows without WSL).

## Key features

- **19 specialized agents** in four lanes — Build/Analysis (`explore`, `analyst`, `planner`, `architect`, `debugger`, `executor`, `verifier`, `tracer`), Review (`security-reviewer`, `code-reviewer`), Domain (`test-engineer`, `designer`, `writer`, `qa-tester`, `scientist`, `git-master`, `document-specialist`, `code-simplifier`), and Coordination (`critic`) — each invoked as `oh-my-claudecode:<agent-name>` with a default model tier (haiku for lookups/docs, sonnet for implementation/debugging/testing, opus for architecture/planning/review).
- **31 skills** (28 user-invocable + 3 internal) compose in three layers — an optional guarantee layer (`ralph`: cannot stop until verified done), 0–N enhancement skills (`ultrawork` for parallelism, `git-master` for atomic commits, `frontend-ui-ux`), and one execution skill (`default`, `orchestrate`, `planner`). Core workflow skills: `autopilot` (full 5-stage autonomous pipeline), `ralph` (loop until verified complete), `ultrawork`/`ulw` (maximum parallelism), `team` (staged multi-agent pipeline), `ccg` (fans out to Codex + Antigravity, Claude synthesizes; Gemini kept as enterprise/API-key fallback), and `ralplan` (Planner/Architect/Critic consensus loop).
- **Magic keywords** — natural-language triggers detected without slash commands: `ultrawork`/`ulw`/`uw`, `autopilot`/`build me`/`I want a`, `ralph`/`don't stop`/`must complete`, `ccg`, `ralplan`, `deep interview`/`ouroboros`, `code review`, `security review`, `deepsearch`, `ultrathink`, `tdd`, `deslop`, `cancelomc`/`stopomc`. Keywords route through two sources: the configurable `config.jsonc` `magicKeywords` block (4 categories) and a hardcoded `keyword-detector` hook (11+ triggers including autopilot/ralph/ccg, not user-configurable).
- **Provider Advisor (`omc ask` / `/ask`)** — runs local CLIs for `claude`, `codex`, `gemini`, `antigravity`, `grok`, `cursor`, saving artifacts under `.omc/artifacts/ask/`; supports `--agent-prompt` to route through a specific OMC agent persona (e.g. `executor`) before asking.
- **HUD statusline**, session friction reports (`omc session friction report --since 24h`), analytics/cost tracking, and skill learning (`/skillify` extracts reusable patterns from a session into `.omc/skills/` or `~/.omc/skills/`, auto-injected when triggers match).
- **Notification routing** to Telegram/Discord/Slack stop callbacks with per-channel tag syntax, plus an OpenClaw gateway bridge forwarding 6 session lifecycle events (`session-start`, `stop`, `keyword-detector`, `ask-user-question`, `pre-tool-use`, `post-tool-use`) to external automation endpoints.
- **GEO visibility benchmark** — ships its own `geobench/oh-my-claudecode.yaml` product spec (via the separate [`geobench`](https://github.com/NomaDamas/geobench) tool) for measuring LLM hit rate, MRR, share of voice, and citations of the project itself.

## Architecture

Four interlocking systems, chained per prompt: **Hooks** (lifecycle event detection) → **Skills** (behavior injection) → **Agents** (specialized execution) → **State** (progress tracking across context resets). Claude Code exposes 11 lifecycle events; OMC hooks into `UserPromptSubmit` (keyword detection), `Stop` (persistent-mode enforcement, optional code-simplifier), `PreCompact` (notepad/project-memory preservation before compaction), `SubagentStart`/`SubagentStop` (agent tracking and output validation), and others, declared in `hooks.json` as timeout-bound Node.js command hooks. Hooks communicate back to Claude via `<system-reminder>` tag injections (e.g. `[MAGIC KEYWORD: ...]`, `The boulder never stops` while ralph/ultrawork is active). All hooks can be disabled globally (`DISABLE_OMC=1`) or selectively (`OMC_SKIP_HOOKS="keyword-detector,persistent-mode"`).

State lives under `.omc/` — per-mode state (`autopilot-state.json`, `ralph-state.json`, `team/`, `interop/`, per-session dirs), a compaction-resistant `notepad.md` (written via MCP tools `notepad_write_priority`/`notepad_write_working`/`notepad_write_manual`, re-injected after compaction), a cross-session `project-memory.json` (MCP tools `project_memory_read/write/add_note/add_directive`), per-plan `notepads/{plan}/{learnings,decisions,issues,problems}.md`, and `plans/`/`prompts/`/`research/`/`logs/`. State separates a **control plane** (queue/session/task-message metadata under `.omc/state/**`) from a **data plane** (plans, prompts, results, traces under `.omc/plans/`, `.omc/notepads/`, `.omc/state/interop/artifacts/**`), using descriptor objects (`kind`, `path`, `contentHash?`, `createdAt`, `producer`, `sizeBytes?`, `retention`, `expiresAt?`) rather than inlining large payloads. By default `.omc/` lives inside the current worktree and is deleted with it; `OMC_STATE_DIR` centralizes state at `~/.claude/omc/{project-hash}/` so it survives worktree deletion, and a `.omc-workspace` marker at a parent directory shares one state root across sibling repos. `<remember>` / `<remember priority>` tags give ad hoc 7-day or permanent memory retention independent of the notepad system.

A verification module gates completion claims on evidence freshness (within 5 minutes) across BUILD, TEST, LINT, FUNCTIONALITY, ARCHITECT (opus-tier review), TODO, and ERROR_FREE checks, rather than accepting an agent's unverified self-report.

## Example usage

```bash
# Marketplace/plugin path (recommended)
/plugin marketplace add https://github.com/Yeachan-Heo/oh-my-claudecode
/plugin install oh-my-claudecode
/setup

# Natural language — no slash command needed
autopilot build me a REST API for managing tasks
ralph: refactor the authentication module
ultrawork implement OAuth

# Team orchestration (in-session vs terminal CLI workers)
/team 3:executor "fix all TypeScript errors"
omc team 2:codex "review auth module for security issues"
omc team 2:antigravity "redesign UI components for accessibility"

# Cross-provider advisor
/ask codex "review this migration plan"
omc ask claude --agent-prompt executor --prompt "draft implementation steps"
```

## Maintenance status

37,438 stars, MIT license, active development (latest push 2026-07-06, latest release v4.15.2 on 2026-07-03). Core team is a small named group (creator/lead Yeachan Heo, one ambassador, one document specialist) plus five top collaborators by commit count; a `Featured by OmC Contributors` section auto-lists high-star personal repos from all-time contributors. Recent version history shows active deprecation churn — `swarm` removed for `/team` at v4.1.7, Codex/Gemini MCP servers removed at v4.4.0 in favor of tmux CLI workers, `omc autoresearch` hard-deprecated in favor of `/deep-interview --autoresearch` + `/oh-my-claudecode:autoresearch` — and a documented dependency warning (`prebuild-install@7.1.3` via `better-sqlite3`, tracked in issue #2913) with no available fix yet.

## Ecosystem

OMC explicitly credits [oh-my-opencode](https://github.com/code-yeongyu/oh-my-opencode), claude-hud, [[obra-superpowers]] (Superpowers), everything-claude-code, and [[Q00-ouroboros]] (Ouroboros) as inspirations, and ships a parallel sibling project `oh-my-codex` for OpenAI Codex CLI users seeking the same orchestration experience. It integrates optionally with the Antigravity CLI (`agy` — Google's successor to the Gemini CLI), Gemini CLI, Codex CLI, and Grok Build, positioning itself as a superset that requires none of them (~$60/month covers all three subscriptions when combined). Compared to methodology-and-skill packs like [[obra-superpowers]] and [[gsd-build-get-shit-done]], which encode disciplined workflows as SKILL.md files without a hook-driven keyword layer, OMC adds automatic prompt-level routing, persistent multi-mode state, and its own agent roster — closer in spirit to the orchestration-harness category occupied by [[ruvnet-ruflo]] (Ruflo/Claude Flow), though OMC stays Claude-Code-plugin-first rather than a standalone multi-provider daemon. Its `ralph` mode is a persistent verify-until-done loop in the same lineage as [[frankbria-ralph-claude-code]] and [[snarktank-ralph]]. `omc team`'s tmux CLI workers parallel the terminal-session-multiplexing approach seen in [[tmuxai.dev]] and [[tmux-tmux]].
