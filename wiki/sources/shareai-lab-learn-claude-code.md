---
type: source
source_url: https://github.com/shareAI-lab/learn-claude-code
tags:
  - harness-engineering
  - agent-loop
  - claude-code
  - skill-loading
  - context-compression
  - subagents
  - task-graph
  - agent-teams
related:
  - njbrake-agent-of-empires
  - skills.sh
  - x.com-mnilax-karpathys-4-claude-md-rules-cut-claude-mistakes
  - anthropics-skills
  - forrestchang-andrej-karpathy-skills
  - how-claude-code-works-in-large-codebases
  - gsd-build-get-shit-done
  - obra-superpowers
  - openvibe.sh
  - x.com-ericzakariasson-building-clis-for-agents
  - nadimtuhin-claude-token-optimizer
  - kepano-obsidian-skills
  - ruvnet-ruflo
  - coleam00-claude-memory-compiler
  - happy.engineering
  - using-claude-code-unreasonable-effectiveness-html
  - phuryn-pm-skills
  - coleam00-helpline
  - Chachamaru127-claude-code-harness
product: learn-claude-code
detail_level: standard
created: 2026-05-05
updated: 2026-07-08
---

`learn-claude-code` (58,143 stars, MIT) is a hands-on curriculum that reverse-engineers Claude Code by building its architecture from scratch in 12 progressive Python sessions. Authored by shareAI-lab, it frames agent development not as model training but as *harness engineering* — constructing the tools, knowledge injection, context management, and permission infrastructure that let a model operate effectively in a specific domain. Each session adds exactly one harness mechanism, from a 30-line `while True` loop (s01) to full multi-agent teams with JSONL mailboxes and worktree-isolated parallel execution (s12). The repo is an authoritative ground-up explanation of the architecture underlying Claude Code and a transferable pattern library for any agent harness in any domain.

_All claims below are sourced from ../../raw/github/shareai-lab-learn-claude-code.md unless otherwise noted._

## What it does

`learn-claude-code` teaches harness engineering through 12 incremental Python programs (`agents/s01_agent_loop.py` through `s_full.py`) that together reproduce the architecture of Claude Code. The core thesis: "agency — the ability to perceive, reason, and act — comes from model training, not from external code orchestration." Harness engineers don't write intelligence; they build the environment the intelligence inhabits. The loop itself never changes across the 12 sessions; every addition layers a new harness mechanism on top without touching it. A companion Next.js web platform provides interactive visualizations, step-through diagrams, and a source viewer.

## Installation

Prerequisites: Python, an Anthropic API key, Node.js (for the web platform only).

```bash
git clone https://github.com/shareAI-lab/learn-claude-code
cd learn-claude-code
pip install -r requirements.txt
cp .env.example .env          # add ANTHROPIC_API_KEY

python agents/s01_agent_loop.py   # start here
python agents/s_full.py           # capstone: all mechanisms combined

# Optional interactive web platform
cd web && npm install && npm run dev   # http://localhost:3000
```

## Key features

- **12 progressive sessions** — each session introduces exactly one harness concept; the core loop is never modified, only extended via the dispatch map.
- **Mental-model-first docs** — every session doc (`docs/en/s01-s12`) follows the same structure: Problem → ASCII solution diagram → minimal code → what changed table → try-it examples. Available in English, Chinese, and Japanese.
- **s01 — The Agent Loop** — 30-line `while True` loop with a single bash tool; exit condition is `stop_reason != "tool_use"`.
- **s02 — Tool Use** — adds a name-to-handler dispatch map; adding a new tool is one dict entry.
- **s03 — TodoWrite** — in-memory `TodoManager` with a reminder nag; reduces agent drift by forcing upfront planning.
- **s04 — Subagents** — fresh, isolated `messages[]` per subagent; prevents context noise from leaking into the main conversation.
- **s05 — Skills** — SKILL.md two-layer system: skill *names* in the system prompt (~100 tokens); full *body* injected via `tool_result` on demand (~2,000 tokens). Identical SKILL.md pattern to that used by [[skills.sh]].
- **s06 — Context Compact** — three-layer compression strategy for infinite sessions; preserves task state across context resets.
- **s07 — Task System** — file-based task graph (`.tasks/task_N.json`) with `pending → in_progress → completed` statuses and `blockedBy` dependency edges; foundation for all multi-agent work in s09–s12.
- **s08 — Background Tasks** — daemon threads run shell commands; completion events are injected as messages when the main loop polls.
- **s09 — Agent Teams** — `TeammateManager` spawns persistent agent loops in threads; `MessageBus` uses append-only JSONL inboxes per teammate.
- **s10 — Team Protocols** — request-response FSM governs shutdown and plan-approval negotiation between teammates.
- **s11 — Autonomous Agents** — idle teammates scan the task board and self-claim ready tasks without lead assignment.
- **s12 — Worktree Isolation** — git worktrees bound to task IDs give each agent its own directory; task coordination and optional isolated execution lanes.
- **Capstone (`s_full.py`)** — all mechanisms combined in one runnable agent.

## Architecture

The repo is a TypeScript-fronted (Next.js), Python-backed monorepo:

- `agents/` — 13 Python reference implementations (`s01`–`s12` + `s_full`). Each is standalone and self-contained; the tool dispatch map (`TOOL_HANDLERS`) is the sole extension point across all sessions.
- `docs/{en,zh,ja}/` — one `.md` per session per language; mental-model-first structure (Problem/Solution/How-It-Works/What-Changed/Try-It).
- `skills/` — sample `SKILL.md` files for the s05 demo; each skill is a directory with a YAML-frontmatter `SKILL.md` that `SkillLoader` discovers at runtime.
- `web/` — Next.js interactive platform with step-through session diagrams, side-by-side source viewer, and a live architecture overview.
- `.github/workflows/ci.yml` — TypeScript typecheck + Next.js build CI.

The central abstraction is `TOOL_HANDLERS: dict[str, callable]`. Every session adds tool names as keys and handler functions as values. The loop (`while True: respond → check stop_reason → dispatch tools → append results`) never changes.

The task-graph pattern from s07 (`.tasks/` JSON files with `blockedBy` edges) propagates forward into s08, s09, s10, s11, and s12, becoming the coordination backbone for multi-agent teams. Similarly, the SKILL.md loading pattern from s05 is the same two-layer mechanism found in [[skills.sh]] and [[tmuxai.dev]].

## Example usage

```python
# s01: minimal loop — the entire agent in ~30 lines
python agents/s01_agent_loop.py
# → "Create a file called hello.py that prints Hello, World!"

# s05: skill loading
python agents/s05_skill_loading.py
# → "What skills are available?"
# → "Load the agent-builder skill and follow its instructions"

# s07: task graph
python agents/s07_task_system.py
# → "Create 3 tasks: Setup project, Write code, Write tests. Make them depend on each other in order."

# s09: agent teams
python agents/s09_agent_teams.py
# → "Spawn alice (coder) and bob (tester). Have alice send bob a message."

# s12: worktree isolation
python agents/s12_worktree_task_isolation.py
```

## Maintenance status

- **Stars**: 58,143 | **Forks**: 9,535 — very high adoption for an educational repo.
- **Latest release**: none (educational; the capstone `s_full.py` serves as the versioned artifact).
- Last pushed: 2026-04-14 — actively developed.
- **License**: MIT.
- **Languages**: TypeScript (Next.js platform), Python (agent implementations).
- CI via GitHub Actions (typecheck + build).
- Related companion products: [Kode Agent CLI](https://github.com/shareAI-lab/Kode-cli) (`npm i -g @shareai-lab/kode`) and [Kode Agent SDK](https://github.com/shareAI-lab/Kode-agent-sdk) for embedding agent capabilities.
- Sister repo [claw0](https://github.com/shareAI-lab/claw0) deconstructs the "always-on" harness variant: heartbeat loop, cron scheduling, IM routing, persistent memory, and a soul personality system layered on top of the same agent core.
