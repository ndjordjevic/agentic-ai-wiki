---
type: source
category: "Coding-agent harnesses & methodologies"
source_url: https://github.com/DietrichGebert/ponytail
tags:
  - claude-md
  - agent-skills
  - yagni
  - over-engineering
  - multi-harness
  - benchmark
  - always-on-ruleset
  - code-minimalism
related:
  - obra-superpowers
  - x.com-mnilax-karpathys-4-claude-md-rules-cut-claude-mistakes
  - shadcn-improve
  - forrestchang-andrej-karpathy-skills
product: ponytail
detail_level: standard
created: 2026-07-14
updated: 2026-07-14
---

Ponytail (82,500+ stars, MIT) is a behavioral ruleset and skill bundle that pushes coding agents to stop at the first "rung" of an escalation ladder — YAGNI, reuse, stdlib, native platform feature, existing dependency, one-liner, only then custom code — before writing anything. It's distinguished from most CLAUDE.md-style guidance in this wiki by shipping its own reproducible agentic benchmark (a headless Claude Code session against a real FastAPI+React repo) showing measurable cuts in lines of code, tokens, cost, and time versus a no-skill baseline, while explicitly holding safety-critical code (validation, error handling, security, accessibility) exempt from the laziness rule.

_All claims below are sourced from ../../raw/github/dietrichgebert-ponytail.md unless otherwise noted._

## What it does

Before writing code, the agent stops at the first rung that holds: (1) does this need to exist at all — YAGNI; (2) is it already in this codebase — reuse it; (3) does the standard library do this; (4) does a native platform feature cover it; (5) does an installed dependency solve it; (6) can it be one line; (7) only then, the minimum code that works. The ladder runs *after* the agent reads the code the change touches and traces the real flow — it is lazy about the solution, not about understanding the problem. Bug fixes are required to address root cause: every caller of a touched function must be checked, not just the path the ticket names. Deliberate corner-cuts (a global lock, an O(n²) scan, a naive heuristic) must be marked with a `ponytail:` comment naming the ceiling and upgrade path, and non-trivial logic must leave one runnable check behind (assert-based demo or a small test file — no framework, no fixtures).

## Installation

Ships adapters for roughly 20 agent hosts, split into two tiers. **Plugin-tier** hosts get lifecycle hooks plus slash commands: Claude Code (`/plugin marketplace add DietrichGebert/ponytail` then `/plugin install ponytail@ponytail`, two separate prompts), Codex (`codex plugin marketplace add` / `codex plugin add`, plus trusting two lifecycle hooks via `/hooks`), GitHub Copilot CLI (`copilot plugin marketplace add` / `copilot plugin install`, commands namespaced as `/ponytail:ponytail-review`), Pi agent harness (`pi install git:github.com/DietrichGebert/ponytail`), OpenCode (`opencode.json` plugin entry, adds `lite/full/ultra/off` levels), Gemini CLI / Antigravity CLI (`gemini extensions install` or `agy plugin install`, same `gemini-extension.json`), Qoder (auto-loads `AGENTS.md`; full hook support via `hooks/qoder-hooks.json`), Hermes Agent (`hermes plugins install --enable`), Devin CLI, Swival, and OpenClaw (via ClawHub: `clawhub install ponytail`). **Instruction-only** hosts (Cursor, Windsurf, Cline, GitHub Copilot Chat, Aider, Kiro, Zed, CodeWhale, JetBrains Junie, Amp, Jules) get the always-on ruleset by copying or auto-loading a rules file (`.cursor/rules/`, `.windsurf/rules/`, `.clinerules/`, `.github/copilot-instructions.md`, `AGENTS.md`, `.kiro/steering/`) with no plugin mode switches or hooks. (../../raw/github/dietrichgebert-ponytail.md)

## Key features

- **Escalation-ladder ruleset** (`AGENTS.md`, verbatim, auto-loaded by OpenCode, Qoder, CodeWhale, the Codex VS Code extension, Amp, and Jules) is the canonical, portable source of truth shared across every host adapter.
- **Six bundled skills**: `ponytail` (the core mode), `ponytail-review` (reviews the current diff for over-engineering, hands back a delete-list), `ponytail-audit` (audits the whole repo, not just the diff), `ponytail-debt` (harvests deferred `ponytail:` corner-cut comments into a ledger), `ponytail-gain` (shows the measured benchmark scoreboard), and `ponytail-help`.
- **Intensity levels** — `lite`/`full`/`ultra`/`off`, settable per-session with `/ponytail <level>` or globally via `PONYTAIL_DEFAULT_MODE` env var or `~/.config/ponytail/config.json`; default is `full`.
- **Subagent propagation** — the ruleset injects into every subagent spawned via the Agent tool by default, scopable with a `PONYTAIL_SUBAGENT_MATCHER` regex against `agent_type` (e.g. to exempt read-only search agents).
- **Reproducible benchmark suite** (`benchmarks/`) — both the agentic (headless Claude Code session, real repo, `git diff`-scored) and older single-shot (`npx promptfoo eval`) benchmarks ship in-repo for independent reproduction, not just published numbers.

## Architecture

The repo is organized as one canonical ruleset (`AGENTS.md`) plus per-host adapter directories that translate it into each platform's native format: `.claude-plugin/` and `.codex-plugin/` for plugin-tier hooks, `.cursor/rules/`, `.windsurf/rules/`, `.clinerules/`, `.kiro/steering/`, `.qoder/`, `.qoder-plugin/`, `.opencode/`, `.devin-plugin/`, `.openclaw/skills/`, `.github/copilot-instructions.md`, `.agents/rules/`, `gemini-extension.json`, and `pi-extension/` for the rest. `hooks/` holds the Node.js lifecycle hooks that drive plugin-tier activation (Claude/Codex-style event names); `commands/` holds slash-command definitions; `skills/` holds the six skill implementations, from which the OpenClaw package is auto-generated (`node scripts/build-openclaw-skills.js`, checked for staleness by the test suite). A `ponytail-mcp/` directory suggests an MCP-server distribution path as well. (../../raw/github/dietrichgebert-ponytail.md)

## Example usage

```
/plugin marketplace add DietrichGebert/ponytail
/plugin install ponytail@ponytail
```
Then, mid-session:
```
/ponytail ultra          # maximum laziness, for when the codebase has wronged you personally
/ponytail-review          # review the current diff for over-engineering
/ponytail-debt            # collect deferred corner-cuts into a ledger
```
(../../raw/github/dietrichgebert-ponytail.md)

## Maintenance status

82,558 GitHub stars, 4,481 forks, MIT licensed, default branch `main`, latest release v4.8.4 "lazy in Hermes now" (2026-06-29), most recent push 2026-07-10 — very actively maintained, with releases tracking new host-adapter support (the v4.8.4 name references the Hermes Agent integration). Sponsored by GreenPT. Published to npm as `@dietrichgebert/ponytail`. README ships Spanish and Korean translations. (../../raw/github/dietrichgebert-ponytail.md)

## Ecosystem

Positions itself against a "caveman" terse-prose control (JuliusBrussee/caveman) and a bare "YAGNI + one-liners" prompt in its own benchmark, outperforming both on every measured axis (LOC, tokens, cost, time) while being the only arm that stays 100% safe. Complements CLAUDE.md-rules-based approaches already in this wiki like [[x.com-mnilax-karpathys-4-claude-md-rules-cut-claude-mistakes]] and [[forrestchang-andrej-karpathy-skills]] (which target "simplicity first" and "surgical changes" as behavioral rules) but goes further by codifying a specific, ordered decision ladder and backing it with a reproducible benchmark rather than anecdote. Distinct from [[shadcn-improve]] and [[obra-superpowers]], which are broader development-methodology skill bundles (audit-and-plan, spec-first TDD) rather than a single always-on minimalism ruleset — ponytail is narrowly scoped to "write less code" and is portable across roughly 20 agent hosts via per-platform adapters rather than being Claude-Code-specific.
