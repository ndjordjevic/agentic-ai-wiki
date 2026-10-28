---
type: source
category: "Knowledge, RAG, memory & context"
source_url: https://trailhq.com/trail-code
companion_urls:
  - https://github.com/trailhq/Trail-Code
raw_files:
  - ../../raw/web/trailhq.com.md
  - ../../raw/github/trailhq-Trail-Code.md
tags:
  - trail-code
  - graft-map
  - agent-memory
  - code-map
  - tree-sitter
  - learnings
  - claude-code-hooks
  - team-shared-context
related:
  - graphify.net
  - Houseofmvps-codesight
  - coleam00-claude-memory-compiler
  - supermemory.ai
  - zilliztech-claude-context
  - mksglu-context-mode
  - HKUDS-LightRAG
  - how-claude-code-works-in-large-codebases
  - Einsia-agent-git
product: trail-code
detail_level: standard
created: 2026-10-27
updated: 2026-10-28
---

Trail-code (formerly Graft; ~10.8k★, MIT) is Trail's open-source self-learning context layer for coding agents: a local tree-sitter **graft map** of the repo plus **learnings** saved as markdown in `.trail/` and synced through git. The marketing page at trailhq.com/trail-code and the GitHub/npm packages (`@trailhq/trail-code`, legacy `@nanonets/graft`) sit next to Trail's separate enterprise "company brain" product on the same domain. It targets Claude Code (deepest wiring), Cursor, Codex, Kiro, and other file-/MCP-capable agents, and overlaps the code-graph niche of [[graphify.net]] while adding team-shared session memory.

_All claims below are sourced from ../../raw/web/trailhq.com.md unless otherwise noted._

## What it does

Trail-code gives coding agents two persistent inputs that survive session boundaries: (1) a **code map** of every file, function, and caller so the agent is pointed at the right symbols and sees edit blast radius, and (2) **learnings** — short markdown records of fixes, decisions, and ruled-out approaches that the next session (yours or a teammate's) starts from. Learnings about the code live in the repo's `.trail/` and go through normal PRs; personal learnings stay in `~/.trail/`. The site frames the loop as set up → agent saves learnings → commit → teammates' agents pick them up → optional org dashboard. (../../raw/github/trailhq-Trail-Code.md)

## Key features

- **Graft map (Tier 1)** — deterministic tree-sitter parse, no model or API key; 24 languages plus Vue SFCs; incremental refresh on working-tree changes. (../../raw/github/trailhq-Trail-Code.md)
- **Optional deep layer** — `trail build --deep` adds LLM file summaries, concept nodes, and per-symbol cruxes under your own provider key. (../../raw/github/trailhq-Trail-Code.md)
- **Learnings + `trail check`** — session- and review-derived rules; `trail check` flags PR diffs that contradict repo or personal learnings before merge. (../../raw/github/trailhq-Trail-Code.md)
- **Agent wiring** — `trail init` installs hooks/statusline/skill for Claude Code and instruction sections for Cursor, Codex, Gemini CLI, Copilot, Windsurf, Kiro, and others; MCP tools for agents that speak MCP. (../../raw/github/trailhq-Trail-Code.md)
- **Published gains** — across 162 runs: 46% fewer tool calls, 42% fewer uncached input tokens, 60% less time, 32% lower cost; SWE-bench Verified 33/50 vs 27/50 without the map. (../../raw/github/trailhq-Trail-Code.md)
- **Graft rename** — `graft` / `@nanonets/graft` still work; `graft upgrade` adds `trail` alongside. (../../raw/github/trailhq-Trail-Code.md)

## Architecture

Both parts run on the machine. Tier 1 writes `graft/.graph/wiring.json` and per-file wiring cards; `--deep` adds markdown concept nodes under `graft/`. The map cache is gitignored like `node_modules`; learnings in `.trail/` are committed. Queries refresh the structural graph against the working tree (~tens of ms when unchanged) before answering. Anonymous usage telemetry is allowlisted in `TELEMETRY.md` and opt-outable (`DO_NOT_TRACK=1` / `trail telemetry disable`); connecting a Trail workspace is separate and optional. (../../raw/github/trailhq-Trail-Code.md)

## Installation

```bash
npm install -g @trailhq/trail-code
trail init                      # or: trail init --agents claude
trail status
```

Then restart the agent so hooks/skills load. Commit `.claude`, `.mcp.json`, `.trail`, and ignore updates so teammates inherit learnings; leave `graft/` out of git. No sign-in or API key for map, hooks, learnings, or `trail check`. Site docs at `/docs` were "Coming soon" at fetch time; the README is the primary reference. (../../raw/github/trailhq-Trail-Code.md)

## Example usage

```bash
trail ask "where is retry backoff configured?"
trail grep "retryablehttp" -i
trail map
trail note --title "keep default retry count at 4"   # learning on stdin
trail check
trail build --deep                 # optional LLM summaries
trail viz                          # local graph viewer
```

Setup prompt on the product page asks the agent to install, run `trail init --agents claude`, then `trail status`. (../../raw/github/trailhq-Trail-Code.md)

## When to use

Use Trail-code when coding agents re-explore the same repo every session, undo team decisions they never saw, or burn tokens grepping for call sites — especially multi-developer Claude Code / Cursor / Codex setups that can commit `.trail/` learnings. Prefer a hand-maintained CLAUDE.md alone for tiny repos; prefer [[graphify.net]] when you want a general multi-modal knowledge graph skill rather than git-synced team learnings plus a always-on code map. Enterprise Trail (company SOP/policy brain on trailhq.com) is a different product for non-code business context.

## Maintenance status

GitHub `trailhq/Trail-Code`: 10,809 stars, 960 forks, MIT, TypeScript, default branch `main`, pushed 2026-10-27; npm `@trailhq/trail-code` / `@nanonets/graft` at 0.26.0; no GitHub Releases tags listed at fetch. Homepage badge still points at trailhq.com/graft (redirects to /trail-code). Active rename from Nanonets Graft to Trail-code under the Trail / Nanonets brand. (../../raw/github/trailhq-Trail-Code.md)

## Ecosystem

Trail-code is the developer OSS half of Trail's "nobody learns alone" thesis; the paid Trail product is a governed context graph / company brain for enterprise agents (MCP, LangChain, Copilot, Bedrock, etc.). Competes and compares with code-graph tools covered in Trail's own blog (Graphify, Codegraph, Graft). Works beside [[skills.sh]] / agent skills and instruction files without rewriting CLAUDE.md.
