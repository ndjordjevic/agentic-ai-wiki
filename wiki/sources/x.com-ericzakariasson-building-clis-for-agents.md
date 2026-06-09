---
type: source
source_url: https://x.com/ericzakariasson/status/2036762680401223946?s=20
tags:
  - agent-cli-design
  - non-interactive-cli
  - agent-tooling
  - stdin-flags
  - dry-run
  - idempotent-commands
  - help-examples
  - token-efficiency
related:
  - must-have-clis-2026
  - shareai-lab-learn-claude-code
  - resend.com
  - github-spec-kit
  - gsd-build-get-shit-done
  - x.com-mnilax-karpathys-4-claude-md-rules-cut-claude-mistakes
product: x
detail_level: standard
created: 2026-06-06
updated: 2026-06-09
---

An X article by Eric Zakariasson (@ericzakariasson) cataloging ten CLI design patterns that make command-line tools usable by AI coding agents — non-interactive flags, progressive `--help` discovery, stdin pipelines, actionable errors, idempotency, dry-run previews, confirmation bypass flags, predictable resource+verb structure, and structured success output. The post addresses the gap between human-oriented CLIs (interactive prompts, prose-heavy help) and agent execution constraints (no keyboard input, pattern-matching from examples, constant retries).

_All claims below are sourced from ../../raw/web/x.com-ericzakariasson-building-clis-for-agents.md unless otherwise noted._

## What it does

Documents practical CLI ergonomics for agent consumers. The core observation: most CLIs assume a human at the keyboard, so agents get stuck on interactive prompts they cannot answer or waste context parsing help pages without runnable examples. The article reframes CLI design as an agent-accessibility problem and lists concrete interface patterns — each illustrated with before/after shell snippets — that let agents discover, invoke, retry, and chain commands without human intervention.

## Key features

**Ten agent-friendly CLI patterns:**

1. **Non-interactive by default** — every input passable as a flag; interactive prompts only as fallback when flags are missing.
2. **Progressive discovery** — don't dump full docs upfront; agents run root command → subcommand → `--help` on demand, conserving context.
3. **Example-rich `--help`** — every subcommand has `--help` with copy-pasteable examples; agents pattern-match faster from examples than prose descriptions.
4. **Flags and stdin for everything** — support pipelines (`cat config.json | mycli config import --stdin`) and command substitution; avoid positional-arg ordering traps.
5. **Fail fast with actionable errors** — missing required flags error immediately with the correct invocation and hints (e.g. where to list available values).
6. **Idempotent commands** — retries (from timeouts or lost context) should no-op safely rather than create duplicates.
7. **`--dry-run` for destructive actions** — agents preview deploy/delete impact, validate the plan, then execute.
8. **`--yes` / `--force` bypass** — safe path as default, but agents can skip confirmation prompts explicitly.
9. **Predictable command structure** — consistent resource+verb pattern (`mycli service list` → `mycli deploy list` → `mycli config list`) so agents generalize from one command to others.
10. **Structured success output** — return machine-parseable data (deploy ID, URL, duration) rather than emoji-only confirmation.

## Architecture and concepts

**Agent CLI failure modes the patterns address:**

- **Interactive deadlock** — arrow-key prompts and mid-execution "y/n" confirmations block agents that cannot send timed keyboard input.
- **Context waste** — dumping entire command trees into agent context upfront crowds out task-relevant material; progressive `--help` discovery mirrors how agents actually explore tools.
- **Pattern-matching over reading** — LLM agents infer invocation syntax from concrete examples faster than from option descriptions; example blocks in `--help` are the highest-leverage documentation surface.
- **Retry fragility** — agents retry after network failures and context resets; non-idempotent commands compound errors across retries.
- **Silent partial success** — destructive operations without `--dry-run` force agents to commit before validating; confirmation prompts without `--yes`/`--force` create the same interactive deadlock as step 1.

**Design philosophy:** make explicit what human CLI users figured out implicitly — flags for every input, discoverable help, pipeline-friendly I/O, and structured output.

## Main APIs

The article does not document a specific CLI binary; it defines an **agent-accessible CLI contract** that tool authors can implement:

| Pattern | Agent-facing surface |
|---|---|
| Input | All parameters as flags; `--stdin` for piped input; interactive mode as fallback only |
| Discovery | Root → subcommand → `--help`; no upfront full-doc dump |
| Help format | Options list + `Examples:` block with 2–3 runnable invocations per subcommand |
| Errors | Immediate exit on missing required input; error message includes correct syntax and discovery hints |
| Safety | `--dry-run` preview; `--yes`/`--force` confirmation bypass; safe defaults |
| Execution | Idempotent semantics on state-changing commands |
| Output | Structured key-value lines on success (URL, ID, duration) — parseable, not emoji-only |
| Naming | Consistent `<resource> <verb>` pattern across all command groups |

## When to use

Apply these patterns when building or evaluating CLIs that AI coding agents will invoke via shell tools — whether as first-party developer CLIs (`gh`, `stripe`, `vercel`) or custom project scripts. The guidance is especially relevant when:

- Agents repeatedly fail on interactive prompts during automated workflows
- `--help` output exists but agents still hallucinate flag syntax
- Destructive operations lack preview or idempotency guarantees
- Command naming is inconsistent across subcommands, forcing agents to re-discover structure each time

For the ecosystem-level argument that CLIs outperform MCP for many agent tool-use cases (token cost, reliability), see [[must-have-clis-2026]]. For harness-level patterns where agents invoke shell commands as their primary tool interface, see [[shareai-lab-learn-claude-code]] and [[gsd-build-get-shit-done]].

## Ecosystem

This post complements [[must-have-clis-2026]], which catalogs ten production CLIs agents should install and argues CLI-over-MCP on cost and reliability grounds. Where that article answers *which* CLIs to use, Zakariasson's post answers *how to design* CLIs so agents can actually use them. The progressive-discovery pattern (`root → subcommand → --help`) aligns with how structured workflow CLIs like [[github-spec-kit]]'s `specify` and [[gsd-build-get-shit-done]]'s staged slash commands expose capabilities incrementally rather than all at once. The non-interactive and fail-loud themes connect to behavioral rules in [[x.com-mnilax-karpathys-4-claude-md-rules-cut-claude-mistakes]] (Rule 12 — fail loud) applied at the tool-design layer rather than the CLAUDE.md layer.
