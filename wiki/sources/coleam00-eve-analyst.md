---
type: source
category: "Coding-agent harnesses & methodologies"
source_url: https://github.com/coleam00/eve-analyst
tags:
  - eve-framework
  - data-analyst-agent
  - read-only-sql
  - human-approval-gates
  - sandboxed-python-analysis
  - subagent-delegation
  - slack-channel
  - eval-gated-behavior
related:
  - coleam00-harness-engineering-demo
  - coleam00-archon
  - coleam00-helpline
  - pydantic-pydantic-ai
  - eve.dev
product: eve-analyst
detail_level: standard
created: 2026-07-21
updated: 2026-07-21
---

`coleam00/eve-analyst` is a compact but production-shaped Eve reference app for building a data analyst agent: the user asks business questions in plain English, the agent answers with auditable read-only SQL, enforces domain-specific revenue definitions, routes expensive scans through approval gates, runs deeper numeric work in a sandbox, and delegates open-ended diagnosis to a specialized subagent. It is designed as a full-stack teaching artifact that exercises the complete Eve primitive set in one coherent workflow.

_All claims below are sourced from ../../raw/github/coleam00-eve-analyst.md unless otherwise noted._

## What it does

The project packages a realistic analytics assistant over a deterministic e-commerce dataset (`customers`, `products`, `orders`, `order_items`, `refunds`). Core flow: discover schema, run guarded SQL, apply revenue policy, escalate computation to a sandbox when needed, and return concise answers with the SQL shown. For “why did metric X change?” prompts, it delegates to an `investigator` subagent with fresh context instead of forcing a fragile single-thread chain-of-thought.

## Installation

Requirements: Node 24+, pnpm 10+, and an `ANTHROPIC_API_KEY`.

```bash
pnpm install
export ANTHROPIC_API_KEY=sk-ant-...
pnpm dev
```

Optional channel/deploy paths are included for Vercel HTTP and Slack wiring via Vercel Connect.

## Key features

- Eve-native agent structure (`agent/`), markdown instructions, typed tools, skills, subagents, channels, and evals.
- Strict read-only SQL toolchain (`run_sql`) with single-SELECT enforcement and approval-required expensive/full-scan detection.
- Domain skill injection (`revenue-rules`) to force net-of-refunds and test-account exclusion before revenue reasoning.
- Sandboxed analysis tool (`run_analysis`) for Python-based charting/statistics in isolated execution (network denied in design notes).
- Dedicated investigation subagent for root-cause prompts with explicit evidence-and-SQL output expectations.
- Eval suite (`evals/*.eval.ts`) and test suite (`test/*.test.ts`, E2E/prod checks) to lock behavior before release.

## Architecture

`agent/agent.ts` defines the Eve agent and model wiring (`@ai-sdk/anthropic`). `agent/tools/` provides the operational surface (`list_tables`, `describe_table`, `run_sql`, `run_analysis`), while `agent/lib/sql-guard.ts` and `agent/lib/run-select.ts` centralize read-only constraints. `agent/instructions.md` encodes analyst behavior and mandatory skill/delegation policies; `agent/skills/revenue-rules.md` holds accounting semantics; `agent/subagents/investigator/` isolates multi-step diagnostic work. Channel adapters live in `agent/channels/eve.ts` (HTTP) and `agent/channels/slack.ts`.

## Example usage

```bash
curl -X POST http://127.0.0.1:2000/eve/v1/session \
  -H 'content-type: application/json' \
  -d '{"message":"What was our total revenue, broken down by product category?"}'
```

Common scenario prompts include schema inspection, revenue computation under business rules, approval-gated broad scans, sandbox-generated weekly trend charts, and delegated “why did revenue drop?” investigations.

## Maintenance status

Stars: 9 | Forks: 8 | Language: TypeScript | Branch: `main` | Last push: 2026-07-09 | Latest release: none | License metadata: none declared at repo metadata level (README states demo code under MIT, Eve under Apache-2.0).
