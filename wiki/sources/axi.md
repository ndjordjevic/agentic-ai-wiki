---
type: source
category: "Coding agents, IDEs & dev environments"
source_url: https://axi.md/
tags:
  - agent-ergonomic-cli
  - toon-format
  - token-budget-first
  - browser-automation
  - github-automation
  - mcp-vs-cli
related: []
product: axi
detail_level: standard
created: 2026-07-08
updated: 2026-07-08
---

AXI (Agent eXperience Interface) is a design framework and ecosystem for building agent-first command-line interfaces where token budget is treated as a first-class constraint. It matters because it aims to preserve the reliability and discoverability advantages that agents often associate with structured protocols like MCP, while keeping the operational cost profile closer to CLI workflows.

_All claims below are sourced from ../../raw/web/axi.md unless otherwise noted._

## What it does
AXI provides 10 design principles for agent-ergonomic CLI tools, alongside reference implementations (notably `gh-axi` for GitHub and `chrome-devtools-axi` for browser automation). Together, the principles and reference tools are meant to make agent-tool interactions more reliable, more discoverable, and more token-efficient than typical “run a shell command and parse text” interfaces.

## Key features
- Token-efficient structured output using TOON (Token-Optimized Object Notation), targeting about ~40% token savings over JSON.
- Minimal default schemas (3–4 fields per list item, not 10+), reducing tool-call and context overhead.
- Content truncation with explicit escape hatches to prevent verbose responses from consuming the agent’s context budget.
- Pre-computed aggregates (counts/statuses) to eliminate extra round trips.
- Definitive empty states (“0 results” instead of ambiguous blank output) so agents can distinguish “no data” from silent failures.
- Structured errors and exit codes designed for idempotent mutations (fail loud on unknown flags; no interactive prompts).
- Ambient context via opt-in session integrations and an on-demand skill option.
- Contextual disclosure by appending relevant next-step commands after output.
- Consistent discoverability via concise per-subcommand `--help`.

## Architecture and concepts
AXI frames the core agent-tool tradeoff as a design problem rather than “MCP vs CLI” itself. It contrasts:
- shell-based CLI execution (agent runs commands like `gh issue list` and parses output; browser CLIs often force extra `snapshot` calls), versus
- structured tool protocols like MCP (schema overhead scales with tool count; browser MCP servers expose many tools and their schemas inflate per-task input tokens).

Its thesis is that an agent-tool interface becomes effective when it embeds reliability and guidance into the interface shape itself—especially by controlling token budget and providing structured, actionable output with minimal schema overhead.

## Main APIs
AXI is primarily distributed and used as CLI skill wrappers and reference tools, including:
- `npx -y gh-axi` for GitHub operations (wrapping the official `gh` CLI with agent-ergonomic output).
- `npx -y chrome-devtools-axi` for browser automation (wrapping chrome-devtools-mcp with combined operations and query filtering).
- installing the AXI guidance/scaffolding via `npx skills add kunchenguid/axi`.

## When to use
AXI is a good fit when you’re building tools that agents need to operate reliably and efficiently—especially for GitHub workflows and browser automation—where typical CLI parsing can waste turns/tokens, and MCP tool schema overhead can be too expensive or too hard to navigate.

## Ecosystem
The AXI catalog includes both official AXIs and community-built tools on the same principles. Official examples include `gh-axi`, `chrome-devtools-axi`, and `lavish-axi` (human review for agent-generated HTML artifacts). Community examples called out on the landing page include `npm-axi`, `sqlite-axi`, `slack-axi`, `gws-axi`, `harvest-axi`, and `specops`.

