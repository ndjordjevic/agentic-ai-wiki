# coleam00/cole-medin-ai-coding

## Metadata
- Stars: 81
- Primary language: Python
- Default branch: main
- Latest release: (none)
- License: (none)
- Homepage: https://www.youtube.com/@ColeMedin
- Fetched: 2026-07-09
- Final URL: https://github.com/coleam00/cole-medin-ai-coding

## Description
An Open Knowledge Format (OKF) bundle of Cole Medin's best AI-coding videos — mount it in any AI second brain and search it deeply. Transcript-verified.

## README
# Cole Medin - AI-Coding Knowledge Bundle

A portable knowledge base of my best AI-coding videos - **Claude Code, context engineering, the PIV loop, the AI layer, and the new Archon harness builder** - in the **Open Knowledge Format (OKF)**: plain markdown any AI agent can read.

## How to use it

Paste this to your AI coding assistant (Claude Code, Cursor, Codex, Gemini CLI, …):

```
Here's a knowledge bundle: https://github.com/coleam00/cole-medin-ai-coding
Read its README and set it up so I can search over it. Then tell me what's inside.
```

That's it - your agent reads the rest of this README, clones the bundle, and you can start asking questions about anything I teach.

---

## Agent setup instructions

This repo is an OKF bundle - a folder of markdown files, each with a small YAML frontmatter block, navigated via `index.md`. Also ships `okf-cli.py` (Python standard library only) for fast navigation and search.

Setup:
```bash
git clone https://github.com/coleam00/cole-medin-ai-coding
cd cole-medin-ai-coding
python okf-cli.py index      # confirm it works - prints table of contents
```

CLI:
- `python okf-cli.py index [subpath]` - print index
- `python okf-cli.py find "<query>"` - ranked keyword search
- `python okf-cli.py read <path>` - read a page

## What's inside

- `index.md` - table of contents
- `videos/` - one page per video (summary, key ideas, tools, link)
- `concepts/` - cross-cutting themes tying the videos together
- `okf-cli.py` - dependency-free navigation/search CLI
- `log.md` - change history

## Docs

### index.md (OKF Bundle Index)

Themes covered:
- **Context Engineering & the PRP Framework** — AI coding assistants fail from missing context, not weak models — engineer the context up front.
- **The PIV Loop (Plan → Implement → Validate)** — you own the planning and validation, the agent owns the implementation.
- **The AI Layer (Rules, Commands, Skills) & System Evolution** — the versioned, reusable layer that turns a coding assistant into a compound system.
- **Archon — the Open-Source Harness Builder** — a workflow/harness engine that sits ABOVE coding agents and orchestrates them with reusable YAML workflows.
- **MCP as the Integration Layer for AI Coding** — standard wiring to plug knowledge, tools, and tasks into any AI coding assistant.

### concepts/

**archon-harness-builder.md:** The new Archon is the first open-source harness builder for AI coding — a workflow engine whose goal is deterministic and repeatable AI coding. Evolution arc: prompt engineering → context engineering → harness engineering. Harnesses mix deterministic steps with AI steps plus human-in-the-loop approval gates. Workflows are YAML files of nodes: either a prompt to a coding-agent session or a deterministic command. Per-node control of provider, model (Haiku for cheap classification, Sonnet default), context injection, and fresh-vs-continued session. Ships default workflows (fix-GitHub-issue, idea-to-PR, PR review, interactive PRD, Ralph loop) and a meta workflow-builder workflow.

**the-piv-loop.md:** Plan → Implement → Validate — the discipline at the center of Cole's system. Planning in two layers: Layer 1 project/PM-level (no code), Layer 2 task-level (find the files to touch). Implement in a fresh session for unbiased eyes; use sub-agents for research to manage context (burn 100k+ tokens, return a few-thousand-token summary). Validate: agent runs tests, linting, type-checking, browser testing; human reviews every artifact. Discipline: keep files small, one feature per prompt, commit working states.

**context-engineering.md:** AI coding assistants almost never fail because the model is too weak — they fail because given too little context. Context engineering is a superset of prompt engineering: hand the assistant everything up front. Central artifact: the **PRP (Product Requirements Prompt)** — "a PRD + curated codebase intelligence + agent runbook," the minimum viable packet to ship production code on the first pass. Arc: prompt engineering → context engineering → harness engineering.

**the-ai-layer.md:** The reusable AI layer in source control: global rules (CLAUDE.md/AGENTS.md, always loaded), commands & skills (reusable workflows — anything prompted more than ~3 times becomes a command/skill). System evolution: inner loop (PIV when it works) + outer loop (after a bug, agent inspects and improves its own AI layer). The AI layer lives in source control and ships via PRs.

**mcp-integration-layer.md:** Model Context Protocol is Cole's standard wiring to plug knowledge, tools, and tasks into any coding assistant. Referenced across all videos as the integration backbone for Archon, Serena, GitHub CLI, and task management tools.

### videos/

**principled-agentic-engineer.md** (watch: https://www.youtube.com/watch?v=luBkbzjo-TA): Full hour-long AI-transformation workshop. Three-phase system: ideation → PIV loop → system evolution. Live build into a poll-builder app using Claude Code + Jira. Key ideas: engineer's role shifted to planning and validating; sub-agents for research; inner + outer system evolution loops; AI layer checked into source control and shared via PRs. Tools: Claude Code, Jira MCP, Confluence, agent-browser (E2E testing).

**complete-guide-to-claude-code.md** (watch: https://www.youtube.com/watch?v=amEUIuBKwvg): Start-to-finish Claude Code masterclass. Covers: CLAUDE.md as system prompt, permissions in settings.local.json, Serena MCP for semantic code retrieval, sub-agents with their own context windows, hooks for deterministic lifecycle control, GitHub CLI for issue-to-PR automation, YOLO mode in dev containers, parallel agents via git worktrees.

**context-engineering-101.md** (watch: https://www.youtube.com/watch?v=Mk87sFlUG28): PRP framework deep-dive with guest interview with Rasmus (creator). Live-builds a PRP Taskmaster MCP server end-to-end (18 working tools after a two-shot build). With Claude 4 reliably runs 500–1500-line PRPs. Companion repo: https://github.com/coleam00/context-engineering-intro.

**harness-engineering-archon.md** (watch: https://www.youtube.com/watch?v=qMnClynCAmM): Official unveiling of rewritten Archon. Cites ~6.7% PR acceptance for bare model vs. ~70% with harness; Stripe's ~1,300 AI-only PRs/week. Demos: <5-min agent-guided setup; issue fixed end-to-end to PR; six workflows in parallel as background processes. Ships Claude Code skill + default workflows (GSD/BMAD/beads importable). GitHub: https://github.com/coleam00/Archon.

**code-100x-faster-with-ai.md:** Covers the PIV loop and context engineering with practical coding acceleration techniques. Emphasizes keeping context small and validation discipline.

## Top-level structure

```
.gitignore         — standard gitignore
README.md          — bundle overview + agent setup instructions
index.md           — OKF bundle table of contents (okf_version: "0.1")
log.md             — change history
okf-cli.py         — dependency-free Python CLI (standard library only) for index/find/read
concepts/          — 5 cross-cutting concept pages
  archon-harness-builder.md
  context-engineering.md
  mcp-integration-layer.md
  the-ai-layer.md
  the-piv-loop.md
  index.md
videos/            — 5 video knowledge pages (transcript-verified)
  code-100x-faster-with-ai.md
  complete-guide-to-claude-code.md
  context-engineering-101.md
  harness-engineering-archon.md
  principled-agentic-engineer.md
  index.md
```
