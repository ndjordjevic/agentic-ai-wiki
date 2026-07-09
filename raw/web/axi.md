# axi.md

## Fetch log
- Inbox URL: https://axi.md/
- Final URL: https://axi.md/
- Fetched: 2026-07-08
- Pages: 1
- Mode: standard
- Note: llms.txt not found; no /docs or /documentation discovered (404 responses)

## Landing page — https://axi.md/
AXI: Agent eXperience Interface
AXI — Agent eXperience Interface
Let's build apps that [agents] love.
10 design principles for agent-ergonomic CLI. 100% task success at the lowest cost — validated across two benchmarks and 915 runs.

chrome-devtools-axi — $0.074 avg cost per task
chrome-devtools-axi — 21.5s avg duration per task

Tell your agent to try it out
Run `npx -y gh-axi` for Github operations
Run `npx -y chrome-devtools-axi` for browser automation

Build your own AXI
Install the AXI skill to get the design guidelines and scaffolding:
npx skills add kunchenguid/axi

The [AXI catalog]

AXIs in the wild — official reference implementations maintained by the AXI project, and tools built by the community on the same principles.

Official AXI domains:
gh-axi — GitHub issues/PRs/workflow runs/releases; wraps the official `gh` CLI with agent-ergonomic output.
chrome-devtools-axi — browser automation; navigate/click/fill/extract with combined operations and query filtering (wraps chrome-devtools-mcp).
lavish-axi — human review; turns agent-generated HTML artifacts into collaborative review surfaces (annotate/comment/feedback back to the agent).

Community AXI examples (selected from the catalog):
npm-axi — npm registry search/inspect with token-efficient output.
sqlite-axi — inspect schemas/sample rows and run capped read-only SQLite queries with token-efficient TOON output.
slack-axi — read/search/sweep safely draft Slack messages with token-efficient output.
gws-axi — Google Workspace command that drafts mail (multi-account write safety).
harvest-axi — time tracking (review/log/edit Harvest entries by period).
specops — spec-driven dev for agents; demo of shipping an AXI embedded in a skill.

Premise
Neither CLI nor MCP gives [agents] enough love.

Two dominant paradigms:
- shell-based CLI execution: agent runs commands (e.g. `gh issue list` or `agent-browser navigate`) and parses text output.
- structured tool protocols like MCP: agent invokes typed tool functions via native tool-calling interfaces.

Problems for agents:
- CLI: action and observation are separated; browser CLIs return minimal confirmations (e.g. `navigate` returns only a page title, `click` returns “Done”), forcing extra `snapshot` calls that waste token budget.
- MCP: schema overhead scales with tool count; browser MCP servers expose ~30 tools, their schemas inflate input tokens (MCP conditions average 185K tokens per task vs. 79K for AXI), and overhead compounds across turns.
- Both: poor discoverability (CLI agents must guess subcommands / read `--help`; MCP agents with lazy loading guess wrong tool names and can crash; neither provides in-context guidance for what to do next).

AXI is 10 principles for agent-ergonomic CLI design that treat token budget as a first-class constraint.
AXI achieves the reliability advantages MCP promises (structured output, discoverability) at the cost profile of a CLI.

10 principles (high level descriptions):
- Token-efficient output — Use TOON format for ~40% token savings over JSON.
- Minimal default schemas — 3–4 fields per list item, not 10+.
- Content truncation — Truncate large text fields with size hints and escape hatches.
- Pre-computed aggregates — Include aggregated counts/statuses that eliminate round trips.
- Definitive empty states — Explicit “0 results” rather than ambiguous empty output.
- Structured errors & exit codes — Idempotent mutations, structured errors, no interactive prompts, fail loud on unknown flags.
- Ambient context — Install opt-in session integrations first, then offer an on-demand skill.
- Content first — Prefer showing actual data, not a wall of help text.
- Contextual disclosure — Append relevant next-step commands after output, not all upfront.
- Consistent way to get help — Concise per-subcommand reference for when agents need it.

