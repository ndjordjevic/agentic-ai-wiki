---
type: source
category: "Coding-agent harnesses & methodologies"
source_url: https://github.com/coleam00/cole-medin-ai-coding
tags:
  - okf-bundle
  - cole-medin
  - context-engineering
  - piv-loop
  - ai-layer
  - archon
  - harness-engineering
  - prp-framework
  - claude-code
  - mcp
related:
  - coleam00-archon
  - coleam00-harness-engineering-demo
  - GoogleCloudPlatform-knowledge-catalog
product: cole-medin-ai-coding
detail_level: standard
created: 2026-07-09
updated: 2026-07-09
---

`coleam00/cole-medin-ai-coding` is an **Open Knowledge Format (OKF) bundle** — a portable, agent-readable knowledge base of Cole Medin's best AI-coding videos, transcript-verified and organized into five concept pages and five video summary pages. It is designed to be cloned directly into any AI second brain (Claude Code, Cursor, Codex, Gemini CLI) so agents can search Cole's teaching on principled agentic engineering without going to YouTube. The bundle ships a zero-dependency Python CLI (`okf-cli.py`) for index, keyword search, and page reading, and uses the OKF v0.1 format pioneered by [[GoogleCloudPlatform-knowledge-catalog]].

_All claims below are sourced from ../../raw/github/coleam00-cole-medin-ai-coding.md unless otherwise noted._

## What it does

The bundle covers five interlocking themes Cole teaches across his channel:

1. **Context Engineering & the PRP Framework** — AI coding assistants fail from missing context, not weak models. The PRP (Product Requirements Prompt) is "a PRD + curated codebase intelligence + agent runbook" — the minimum viable packet to ship production code on the first pass. With Claude 4, PRP runs of 500–1,500 lines are reliable.
2. **The PIV Loop (Plan → Implement → Validate)** — the core operating discipline: engineer owns planning and validation; agent owns implementation. Planning splits into Layer 1 (project/PM-level, no code) and Layer 2 (task-level, find the files). Implementation runs in a fresh session; sub-agents handle research to manage context.
3. **The AI Layer (Rules, Commands, Skills) & System Evolution** — a versioned set of global rules (CLAUDE.md/AGENTS.md), commands, and skills checked into source control. Anything prompted more than ~3 times becomes a command/skill. System evolution = inner loop (PIV when working) + outer loop (after a bug, agent inspects and improves its own AI layer and shares improvements via PRs).
4. **Archon — the Open-Source Harness Builder** — a YAML workflow engine that sits above coding agents and orchestrates them. Workflows mix deterministic nodes (context creation, validation, git ops) with AI nodes and human-in-the-loop gates. Per-node model selection (Haiku for cheap steps, Sonnet for default) and context injection. Ships default workflows (fix-GitHub-issue, idea-to-PR, PR review, Ralph loop). Cited stat: ~6.7% PR acceptance for bare model vs. ~70% with a good harness; Stripe ~1,300 AI-only PRs/week. See [[coleam00-archon]].
5. **MCP as the Integration Layer** — Model Context Protocol wires knowledge, tools, and tasks into any coding assistant; referenced across all videos as the standard integration backbone.

## Key features

- **OKF format** — plain markdown + YAML frontmatter; no database, no embeddings, no API; agents read it directly via `git clone`.
- **`okf-cli.py`** — zero-dependency Python CLI (standard library only): `index [subpath]` (table of contents), `find "<query>"` (ranked keyword search), `read <path>` (print a page). Progressive disclosure: start at root index, follow links.
- **Transcript-verified** — all video pages verified against the full video transcript; not summaries from titles or descriptions.
- **Cross-linked concepts ↔ videos** — each concept page lists the videos that teach it; each video page lists its related concepts, enabling graph-style navigation.
- **Self-describing agent setup** — README contains step-by-step agent setup instructions so an agent receiving just the GitHub URL can clone and configure itself autonomously.

## Architecture

```
index.md              ← OKF bundle root (okf_version: "0.1")
concepts/             ← 5 cross-cutting concept pages
  archon-harness-builder.md
  context-engineering.md
  mcp-integration-layer.md
  the-ai-layer.md
  the-piv-loop.md
videos/               ← 5 transcript-verified video knowledge pages
  principled-agentic-engineer.md    (youtube.com/watch?v=luBkbzjo-TA)
  complete-guide-to-claude-code.md  (youtube.com/watch?v=amEUIuBKwvg)
  context-engineering-101.md        (youtube.com/watch?v=Mk87sFlUG28)
  harness-engineering-archon.md     (youtube.com/watch?v=qMnClynCAmM)
  code-100x-faster-with-ai.md
okf-cli.py            ← zero-dependency search/navigation CLI
log.md                ← change history
```

## Installation

```bash
git clone https://github.com/coleam00/cole-medin-ai-coding
cd cole-medin-ai-coding
python okf-cli.py index      # verify — prints table of contents
```

Or paste the repo URL directly to any AI coding assistant and let it read the README and self-configure.

## Example usage

```bash
python okf-cli.py find "piv loop"           # ranked keyword search
python okf-cli.py read concepts/the-piv-loop
python okf-cli.py read videos/harness-engineering-archon
python okf-cli.py index videos              # list videos subdir
```

## When to use

- Onboarding an AI coding assistant to Cole Medin's principled agentic engineering methodology without sending it to YouTube.
- Looking up the canonical definition of the PIV loop, PRP framework, AI layer, or Archon harness model during a coding session.
- Using as a reference bundle to understand how OKF bundles are structured before building your own (good companion to [[GoogleCloudPlatform-knowledge-catalog]]).
- Adding as context for any project that uses Claude Code, Cursor, Codex, or Gemini CLI where Cole's conventions are in use.

## Maintenance status

81 stars · No license · Primary language: Python · No formal releases · Last pushed June 2026. Actively maintained by Cole Medin. Bundle generated 2026-06-25; OKF format v0.1.

## Ecosystem

This bundle is a consumer of OKF, which was specified by [[GoogleCloudPlatform-knowledge-catalog]]. The Archon harness builder content directly relates to [[coleam00-archon]] (the repo itself) and [[coleam00-harness-engineering-demo]]. For Cole's other tools in this wiki see [[coleam00-helpline]] (AI Layer reference implementation), [[coleam00-claude-memory-compiler]], and [[coleam00-agent-control-plane]].
