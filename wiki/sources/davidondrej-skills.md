---
type: source
source_url: https://github.com/davidondrej/skills
tags:
  - agent-skills
  - agent-orchestration
  - cmux
  - multi-agent-delegation
  - skill-authoring
  - deep-research
  - personal-skill-collection
related:
  - anthropics-skills
  - mattpocock-skills
  - forrestchang-andrej-karpathy-skills
  - voltagent-awesome-agent-skills
  - obra-superpowers
  - pi.dev
product: skills
detail_level: standard
created: 2026-07-07
updated: 2026-07-07
---

David Ondrej's personal Agent Skills repository (1.5k+ stars, MIT, 211 forks) — 31 skills across five category folders, distinguishing itself from other public skill collections by leaning heavily into multi-agent orchestration (cmux terminal control, delegating to Pi/Codex/Claude Code/Hermes, self-scheduling loops) alongside the more common skill-authoring and research-workflow content.

_All claims below are sourced from ../../raw/github/davidondrej-skills.md unless otherwise noted._

## What it does

Packages 31 reusable, narrowly-scoped skills under `skills/<category>/<skill-name>/SKILL.md`, each triggered by an agent recognizing a task pattern in its `description:` frontmatter (long, keyword-dense trigger phrases rather than short summaries). No installer or CLI — an agent (or a human via `distribute-skill-to-all-agents`) copies or symlinks the relevant `SKILL.md` folders into its own skills directory.

## Installation

No build step. Clone the repo and copy/symlink individual `skills/<category>/<name>/` folders into an agent's skills path (Claude Code `~/.claude/skills/`, Codex, Pi's `~/.pi/agent/skills`, or Hermes). The `distribute-skill-to-all-agents` skill formalizes this as a repeatable symlink layout across all four agent runtimes and calls out a specific gotcha: Pi's `~/.pi/agent/skills` trap where a naive copy breaks Pi's own skill discovery.

## Key features

- **Agent orchestration (9 skills)** — `cmux` (native macOS multi-pane terminal control via CLI + Unix-socket JSON-RPC, pane/workspace/surface management, agent-to-agent delegation inside panes), `delegating-to-agents` (choosing and prompting Pi/Codex/Claude Code/Hermes as sub-agents), `codex-subagent` (launching OpenAI Codex CLI via ChatGPT subscription auth, no API key), `agent-self-scheduling` (cron/heartbeat/loop patterns distinguishing external-clock agents from Hermes's built-in scheduler), `goal-loop` (writing `/goal` instructions for the plan→act→test→review→iterate loop, aka "Ralph loop"), `handoff` (compacting a conversation into a copy-pasteable handoff message for a fresh session), `run-deep-swe` (scoring any model on the 113-task DeepSWE coding benchmark via OpenRouter), `fable-safe-prompt` (rewriting dual-use prompts to avoid tripping Claude Fable 5's safety classifiers), `markdown-rendering` (working around a cmux right-pane blank-render bug).
- **Skill authoring (4 skills)** — `effective-agent-skills` (a full guide to SKILL.md anatomy, progressive disclosure, anti-patterns, and testing), `distribute-skill-to-all-agents`, `push-skill-to-github` (commit/push flow to a private `~/.agents` skills repo), `folder-specific-claude-and-agents-md` (scoped CLAUDE.md + AGENTS.md symlink generation for a specific folder).
- **Research and web (6 skills)** — `deep-research` and `research-prompt` (building a rigorous one-paragraph research brief and firing it at DeepAPI's `/v1/research/deep` endpoint), `deepapi` (raw DeepAPI scraping/email access), `youtube-transcript` (DeepAPI primary, yt-dlp fallback), `browser-harness` (direct CDP control of the user's already-running Chrome), `pi-web-search` (Pi-specific web access package).
- **Thinking and docs (7 skills)** — `copywriting` (David Ondrej's own two writing styles, used for all copy written on his behalf), `brain-to-docs` and `interview-style-doc-building` (Q&A-driven extraction into README/ADRs or structured strategic documents), `grill-me` (relentless interview-style plan stress-testing), `teach`, `short` (forces answer compression), `read-all-adrs`.
- **Ops and setup (5 skills)** — `vps-server-management`, `cyber-audit` (read-only CVE/breach exposure scan of the user's Mac, writing a report to `~/Documents/security-audits/`), `anti-sleep` (macOS `caffeinate` wrapper), `setup-help` (one-step-at-a-time guided setup), `pi-custom-model` (registering OpenRouter model-variant slugs like `:nitro`/`:floor`/`:exacto` in Pi so they don't silently fall back).

## Architecture

Flat convention: `skills/<category>/<skill-name>/SKILL.md`, no shared runtime or plugin manifest — each skill is self-contained instructions plus, in a few cases (`grill-me`), an inline directive with no separate body. Several skills carry `disable-model-invocation: true` in frontmatter, meaning they only fire on an explicit user trigger phrase rather than being auto-selected by the agent — used for higher-risk or highly personal skills like `cyber-audit`, `fable-safe-prompt`, `handoff`, `codex-subagent`, and `copywriting`-adjacent utility skills (`teach`, `short`, `setup-help`, `read-all-adrs`, `grill-me`).

## Example usage

No example commands in the README; usage is implicit — an agent whose skills directory includes one of these folders reads the `SKILL.md` when its `description:` trigger phrase matches the current task (e.g. any message mentioning "cmux" loads `cmux/SKILL.md` first).

## When to use

Most directly useful for people already running David Ondrej's stack (cmux, Pi Agent, Hermes Agent) or wanting concrete patterns for agent-to-agent delegation and self-scheduling — areas most public skill collections (e.g. [[anthropics-skills]], [[voltagent-awesome-agent-skills]]) cover thinly. The `effective-agent-skills` guide and `distribute-skill-to-all-agents` skill are portable to any Claude Code / Codex / Pi setup regardless of the rest of the collection.

## Maintenance status

1,546 stars, 211 forks, MIT license, no tagged releases (rolling `main` branch), last pushed 2026-07-07. (../../raw/github/davidondrej-skills.md)

## Ecosystem

Depends on DeepAPI (deepapi.co) for `deep-research`, `deepapi`, and `youtube-transcript`; on OpenRouter for `run-deep-swe` and `pi-custom-model`; and on cmux, Pi Agent, and Hermes Agent as the orchestration targets for most of the `agent-orchestration` category. Compare general-purpose skill guides in [[anthropics-skills]] and personal collections in [[mattpocock-skills]], [[forrestchang-andrej-karpathy-skills]], and [[kepano-obsidian-skills]]; skill distribution/marketplace mechanics parallel [[skills.sh]]; the terminal-agent orchestration angle (cmux, delegating-to-agents) overlaps with [[pi.dev]]'s own multi-provider harness design.
