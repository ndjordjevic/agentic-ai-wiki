---
type: source
category: "Coding-agent harnesses & methodologies"
source_url: https://github.com/JayPokale/Chisle
tags:
  - token-savings
  - terse-prose
  - yagni
  - tool-output-compression
  - claude-code
  - multi-harness
  - zero-deps
  - agent-brevity
related:
  - rtk-ai-rtk
  - teamchong-pxpipe
  - nadimtuhin-claude-token-optimizer
  - chopratejas-headroom
  - obra-superpowers
  - Leonxlnx-unlazy
  - skills.sh
product: chisle
detail_level: standard
created: 2026-10-27
updated: 2026-10-28
---

JayPokale/Chisle (719 stars, MIT) is a Claude Code plugin, also shipped to 12 other agents, that cuts an AI coding agent's token bill on three axes: terse prose, YAGNI-first code, and tool-output compression. It began as a merge of caveman (terse prose) and ponytail (lazy-senior-dev code rules), claims shorter answers than both with no accuracy loss, and publishes benchmark runs "including the runs where it lost". On the input side it overlaps with tools like [[rtk-ai-rtk]] and [[chopratejas-headroom]].

_All claims below are sourced from ../../raw/github/JayPokale-Chisle.md unless otherwise noted._

## What it does

Chisle injects a zero-fluff ruleset at session start so the agent drops filler, hedging and manufactured structure, and builds the smallest code that works. Code symbols, API names and error strings stay verbatim. Separately, a `PostToolUse` hook trims oversized tool output by about 46% before it re-enters the context window, where it would be re-billed on every later request. `Read`, `Edit` and `Write` are deliberately never touched, so exact bytes feed later edits.

The README's worked example: an order-state-machine prompt yields 125 lines / 1,342 answer tokens from the bare model versus 54 lines / 450 tokens with Chisle (caveman 1,140, ponytail 842).

## Installation

One command auto-detects agents (Claude Code, Pi, Cursor, Windsurf, Cline, Kiro, Antigravity, Codex, Gemini, Copilot, Copilot CLI, OpenCode, Hermes) and wires each one:

```bash
npx chisle
```

Alternatives are `install.sh` (curl) and `install.ps1` (Windows). `--dry-run` previews, `--only claude` or `--only pi` scopes it, `--uninstall` restores everything, and `npx chisle mcp wrap` proxies stdio MCP servers (Cursor, Windsurf, Cline, Kiro, Gemini, Qwen Code, Copilot CLI) to compress their output.

## Key features

- **Prose axis** — zero-fluff ruleset, injected once per active session.
- **Code axis (YAGNI ladder)** — after reading the problem, the agent stops at the first rung that holds: skip it, reuse existing code, use the stdlib, use a native platform feature, use an installed dependency, write one line, else the minimum code. It must note what it skipped; deliberate simplifications get `// chisle:` comments. Trust-boundary validation, data-loss handling, security and accessibility are never cut.
- **Input axis** — Claude `PostToolUse`, Pi `tool_result`, OpenCode plugin, and Copilot CLI `postToolUse` hooks scrub, elide and dedup tool output; the README cites a 30 KB log losing 87% of fresh input tokens on OpenCode.
- **Published benchmarks** — Claude Code (Haiku 4.5, 26 prompts): answer length 56% of bare vs caveman 65% and ponytail 58%. Pi (GPT-5.5, 6 tasks): 37% vs 56% and 49%. Accuracy: 156/156 vs 155/156 on auto-graded tasks; 48/60 vs 49/60 on agentic hidden-test repos; no judge model.
- **Zero dependencies** across 13 supported agents.

## Architecture

Top-level folders include `skills`, `rules`, `hooks`, `commands`, `bin`, `pi-extension`, `benchmarks`, `docs`, `tests`, and per-agent configs (`.claude-plugin`, `.codex-plugin`, `.cursor`, `.kiro`, `.opencode`, `.windsurf`, `.clinerules`, `GEMINI.md`, `gemini-extension.json`). Hooks attach in three places: ruleset injection at session start, mode tracking each turn (Claude and Pi), and a scrub → elide → dedup pipeline on every tool call, whose output is rebuilt in the tool's own shape.

## Example usage

| Command | Effect |
|---|---|
| (nothing) | On automatically every session after install |
| `/chisle` | Re-activate |
| `/chisle off`, `stop chisle`, `normal mode` | Deactivate (ruleset and input compression) |

Natural language also works ("activate chisle", "chislify this"). `npx chisle --stats` and config are documented in `docs/usage.md`.

## Maintenance status

719 stars, 50 forks, MIT, primary language JavaScript, default branch `main`, latest release v3.8.1 (2026-10-18), most recent push 2026-10-24. CI badge present; the author credits Claude, Codex and Antigravity as co-engineers. caveman and ponytail MIT notices are kept in `NOTICE`.
