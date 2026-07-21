# coleam00/eve-analyst

## Metadata
- Stars: 9
- Primary language: TypeScript
- Default branch: main
- Latest release: (none)
- License: (none)
- Homepage: (none)
- Fetched: 2026-07-21
- Final URL: https://github.com/coleam00/eve-analyst

## Description
(none)

## README
# eve-analyst

A production-shaped **data analyst agent** built on [Vercel's **Eve** framework](https://github.com/vercel/eve).
You ask questions about a company's data in plain English; the agent writes read-only SQL,
follows the business's own revenue rules, guards expensive queries behind human approval, runs
deeper analysis in an isolated sandbox, and hands open-ended investigations to a subagent. It
runs over HTTP and Slack, and its behavior is locked in by an evals suite.

Built from scratch as the companion project for a video on Eve. It mirrors Vercel's own
flagship internal agent `d0` (a Slack data analyst answering 30k+ questions a month), but is
fully self-contained: the dataset is seeded in memory, so it runs offline and deploys in one
command.

## What it demonstrates (every core Eve primitive)

| Eve primitive | Where |
|---|---|
| An agent is a directory | the whole `agent/` folder |
| Model config | `agent/agent.ts` (`defineAgent`) |
| System prompt in markdown | `agent/instructions.md` |
| Typed tools | `agent/tools/` (`list_tables`, `describe_table`, `run_sql`, `run_analysis`) |
| Human-in-the-loop approval | `run_sql` pauses on an unbounded full-table scan |
| Skills loaded on demand | `agent/skills/revenue-rules.md` |
| Subagents | `agent/subagents/investigator/` |
| Sandbox (isolated code) | `run_analysis` runs Python in Vercel Sandbox (Docker locally) |
| Channels | `agent/channels/eve.ts` (HTTP) + `agent/channels/slack.ts` |
| Durable sessions | pause-for-approval then resume is a durable workflow |
| Evals as a deploy gate | `evals/*.eval.ts` |

## The dataset

A tiny e-commerce warehouse (`customers`, `products`, `orders`, `order_items`, `refunds`)
seeded deterministically into an in-memory SQLite database via `node:sqlite` (built into
Node 24, zero dependencies). It includes test/internal accounts and refunds, so the
`revenue-rules` skill actually changes the answer. See `agent/lib/db.ts`.

## Requirements

- **Node 24+** (Eve requires it) and **pnpm 10+**
- An **`ANTHROPIC_API_KEY`** (the agent uses `@ai-sdk/anthropic` with `claude-sonnet-5`)

## Run it locally

```bash
pnpm install
export ANTHROPIC_API_KEY=sk-ant-...      # or put it in .env.local
pnpm dev                                 # starts the eve dev TUI
```

Then talk to it in the TUI, or drive it over HTTP:

```bash
# create a session
curl -X POST http://127.0.0.1:2000/eve/v1/session \
  -H 'content-type: application/json' \
  -d '{"message":"What was our total revenue, broken down by product category?"}'
# stream the reply (use the sessionId from the response)
curl -N http://127.0.0.1:2000/eve/v1/session/<sessionId>/stream
```

Try these to see each feature:
- "What tables are in the warehouse?" → schema discovery
- "What was our total revenue?" → loads the `revenue-rules` skill, answers net of refunds
- "Run this exact query: `SELECT * FROM order_items`" → pauses for your approval, then resumes
- "Use run_analysis to chart weekly revenue" → runs Python in the sandbox
- "Revenue dropped last week, why?" → delegates to the `investigator` subagent

## Test it

```bash
node --test test/*.test.ts             # unit tests (SQL guard + dataset)
pnpm exec eve eval --strict            # agent evals (deploy gate)
node test/e2e.mjs                      # end-to-end multi-turn conversation (needs `pnpm dev` running)
node test/prod-checks.mjs              # correctness + edge cases + sandbox network isolation (defaults to prod URL)
pnpm typecheck                         # tsc
```

## Deploy it

```bash
vercel login          # one-time
pnpm exec eve deploy  # links a Vercel project and deploys to Vercel Functions
```

Set `ANTHROPIC_API_KEY` in the Vercel project's Environment Variables so the deployed agent
can reach the model.

## Enable Slack (optional)

The Slack channel (`agent/channels/slack.ts`) is authored and ready; credentials flow through
Vercel Connect (no bot token in code). To activate:

```bash
export FF_CONNECT_ENABLED=1
vercel connect create slack --triggers
vercel connect attach <uid> --triggers --trigger-path /eve/v1/slack --yes
VERCEL_USE_EXPERIMENTAL_FRAMEWORKS=1 vercel deploy --prod
```

## Design notes

- **Read-only by construction.** `agent/lib/sql-guard.ts` rejects anything that is not a single
  `SELECT`; both the primary agent and the subagent go through it (`agent/lib/run-select.ts`).
- **Approval lives on the human-facing agent, not the subagent.** The primary `run_sql` pauses
  on expensive scans; the autonomous `investigator` runs read-only SQL without prompts.
- **No filesystem writes.** The dataset is in-memory and seeded per process, so it behaves the
  same on a laptop and on Vercel's read-only serverless filesystem.
- **The sandbox has no network.** `agent/sandbox.ts` pins `networkPolicy: "deny-all"` (Eve's
  default is allow-all), so model-written code runs isolated with no egress. Verified by
  `test/prod-checks.mjs`.

## License

MIT (this demo). Eve itself is Apache-2.0.

## Docs

### AGENTS.md

- Enforces an `eve`-docs-first workflow: consult installed `node_modules/eve/docs/` (or `https://eve.dev/docs`) before implementation decisions.

### CLAUDE.md

- Delegates directly to `AGENTS.md` via `@AGENTS.md`, so the repository keeps a single agent-instruction source of truth.

### SPEC.md

- Defines the product as a production-shaped Eve data analyst app that demonstrates all major Eve primitives in one cohesive use case.
- Documents architecture expectations: read-only SQL, approval gating for expensive scans, sandboxed Python analysis, delegated root-cause subagent flow, HTTP+Slack channels, and eval-driven release safety.

### agent/instructions.md

- Captures runtime operating policy for the assistant persona: schema discovery before querying, strict SELECT-only queries, mandatory revenue-rules skill for revenue metrics, sandbox use for analysis/charting, and subagent delegation for open-ended investigation.

## Top-level structure

- `.claude/` — Claude-specific local settings.
- `AGENTS.md` / `CLAUDE.md` — agent instruction policy and alias.
- `SPEC.md` — high-level architecture and behavioral specification.
- `agent/` — Eve app core: agent definition, channels, tools, sandbox, skills, subagents, SQL guard libraries.
- `agent/tools/` — typed tools: `list_tables`, `describe_table`, `run_sql`, `run_analysis`.
- `agent/subagents/investigator/` — delegated investigation agent with its own instructions and tool surface.
- `evals/` — behavior-locking eval suite (`approval`, `count`, `delegate`, `revenue`, `schema`).
- `test/` — unit/E2E/prod-oriented verification scripts.
- `package.json` / `pnpm-workspace.yaml` / `tsconfig.json` — Node 24 + TypeScript workspace config and scripts.
