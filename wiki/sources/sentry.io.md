---
type: source
category: "Infra, hosting, DB & observability"
source_url: https://sentry.io/welcome/
companion_urls:
  - https://github.com/getsentry/sentry
raw_files:
  - ../../raw/web/sentry.io.md
  - ../../raw/github/getsentry-sentry.md
tags:
  - error-monitoring
  - distributed-tracing
  - ai-observability
  - llm-monitoring
  - seer
  - mcp-server
  - agent-debugging
  - session-replay
related:
  - greptile.com
  - qa.tech
  - coleam00-agent-control-plane
  - hermes-agent.nousresearch.com
  - microsoft-playwright-mcp
  - mcp.sentry.dev
  - coderabbit.ai
product: sentry
detail_level: standard
created: 2026-06-30
updated: 2026-08-25
---

Sentry is a developer-first application monitoring platform used by millions of developers and teams including Anthropic, Disney+, and Instacart. It unifies error monitoring, distributed tracing, session replay, logs, profiling, cron/uptime monitoring, and AI-native debugging (Seer) into one trace-connected observability stack. For agentic AI workflows, Sentry is especially relevant as an **observability and verification layer**: it instruments LLM agents and MCP servers (OpenAI Agents, Vercel AI SDK), exposes production context to coding agents via an MCP server (`mcp.sentry.dev`) and agent skills, and uses Seer to auto-investigate issues, draft merge-ready fixes, and review PRs against real production failure patterns.

_All claims below are sourced from ../../raw/web/sentry.io.md unless otherwise noted._

## What it does

Sentry captures errors, performance spans, logs, replays, and metrics from applications across 100+ language/framework SDKs, then correlates them on a shared trace so developers can move from alert → full context → fix without switching tools. The platform's marketing positioning is "code breaks, fix it faster" — SDK install is typically a few lines (`npx @sentry/wizard`, `pip install sentry-sdk`, etc.) with no separate agent daemon. Issues surface with stack traces, breadcrumbs, release/commit attribution, user impact counts, and assignment to the engineer who introduced the regression.

For AI-powered applications, Sentry adds **LLM observability**: track agent runs, model calls, token usage/cost, tool executions, and failures with prompt/response context in trace waterfalls. Seer extends this into an autonomous debugging agent that investigates new issues, answers natural-language questions against production telemetry, generates Autofix PRs, and performs AI code review on open PRs using historical error and performance data from the connected repo.

## Key features

- **Error monitoring** — stack traces with local variables, breadcrumbs, frequency trends, user-impact counts, Slack/email alerts, auto-assignment to commit authors, and release health (crash-free sessions, adoption, failure rate).
- **Distributed tracing** — end-to-end trace waterfalls connecting frontend actions, API calls, database queries, and background jobs; Trace Explorer for slow endpoints, N+1 detection, and span-level metric alerts.
- **Session replay** — visual reproduction of user sessions tied to errors and performance issues.
- **Logs, profiling, cron/uptime monitoring** — additional signal types connected on the same trace (per product nav and docs index).
- **Seer (AI debugger)** — Autofix (root-cause analysis + merge-ready patches), Seer Agent (natural-language Q&A over production data), AI code review on PRs against real production history; integrates with Claude, Copilot, Cursor via MCP; $40/active contributor/month on paid plans.
- **AI / LLM observability** — `OpenAIAgentsIntegration()` (Python), `vercelAIIntegration()` (JavaScript) with token/cost tracking, tool-call monitoring, and deep trace analysis of prompts and responses.
- **Sentry MCP server** ([[mcp.sentry.dev]]) — exposes issues, traces, and logs to coding agents in Claude Code, Cursor, and other MCP clients; documented workflows for weekly performance triage and production debugging from the IDE.
- **Agent skills** — Sentry publishes agent skills for AI coding assistants (documented under docs.sentry.io/ai/).
- **Integrations** — GitHub (source linking, PR comments, Seer), Slack, Jira, Linear, and broad platform SDK coverage. (../../raw/github/getsentry-sentry.md)

## Architecture

The open-source Sentry server (`getsentry/sentry`, 44k+ stars, Python/Django, default branch `master`, latest release 26.6.0) is the backend for the hosted SaaS at sentry.io. The monorepo includes `AGENTS.md`, `CLAUDE.md`, and `.mcp.json` for contributor agent workflows. Official SDKs live in separate repos under the `getsentry` GitHub org (sentry-javascript, sentry-python, sentry-go, sentry-cocoa, etc. — 20+ language SDKs listed in the README). Events flow from instrumented applications → Sentry ingest → issue grouping, trace correlation, and alerting; Seer layers generative AI on top of this telemetry for investigation and fix generation. (../../raw/github/getsentry-sentry.md)

## Installation

**Application SDK (typical):**
```bash
npx @sentry/wizard@latest -i nextjs   # or -i react, python, etc.
pip install --upgrade sentry-sdk
npm install @sentry/node
```

**AI agent observability (Python OpenAI Agents):**
```python
import sentry_sdk
from sentry_sdk.integrations.openai_agents import OpenAIAgentsIntegration

sentry_sdk.init(
    dsn="https://examplePublicKey@o0.ingest.sentry.io/0",
    send_default_pii=True,
    integrations=[OpenAIAgentsIntegration()],
)
```

**AI agent observability (Vercel AI SDK):**
```javascript
Sentry.init({
  dsn: 'https://<key>@sentry.io/<project>',
  tracesSampleRate: 1.0,
  integrations: [Sentry.vercelAIIntegration({ recordInputs: true, recordOutputs: true })],
});
```

**MCP for coding agents:** connect to `https://mcp.sentry.dev/` per Sentry's AI docs. (../../raw/github/getsentry-sentry.md)

## Example usage

A team shipping an agentic feature instruments their Vercel AI `generateText` calls with `experimental_telemetry: { isEnabled: true }` and Sentry's `vercelAIIntegration`. When a tool call fails or token costs spike, Sentry surfaces the full agent run in a trace — model calls, tool executions, latencies, and costs on one pane. A new production error triggers Seer Autofix, which reads the stack trace, correlates commits and traces, and opens a PR before the on-call engineer finishes reading the alert. In the IDE, a developer connects Sentry MCP to Claude Code and asks "what's causing the slow checkout span this week?" — Seer Agent pulls live production signals instead of guessing from training data.

## When to use

Sentry fits teams building production software (web, mobile, backend, games) who need unified error + performance + log observability with minimal SDK friction. For agentic AI specifically, use it when you need to **monitor LLM agents and MCP servers in production** (token costs, tool failures, latency), **feed production context into coding agents** via MCP/skills, or **automate incident response** with Seer Autofix and AI PR review. It complements test-generation tools ([[qa.tech]]) and PR review agents ([[greptile.com]]) by covering runtime production behavior that tests and static review cannot see.

## Maintenance status

Hosted SaaS at sentry.io (freemium + Team/Business/Enterprise paid tiers). Open-source server actively maintained: 44,196 GitHub stars, pushed 2026-06-30, latest release 26.6.0 (2026-06-15), Python primary language, homepage https://sentry.io. SDK ecosystem maintained across 20+ language repos under `getsentry/*`. (../../raw/github/getsentry-sentry.md)

## Ecosystem

Sentry integrates with GitHub (issues, releases, Seer PR review), Slack (alerts, incident threads), Jira, Linear, and CI/CD via `sentry-cli`. The MCP server and agent skills target the same coding-agent ecosystem as [[microsoft-playwright-mcp]] (browser testing) and harness tools like [[coleam00-agent-control-plane]] (run observability). Production agent deployments like [[hermes-agent.nousresearch.com]] benefit from Sentry's tracing and Seer for long-running agent failures. Greptile's REST API docs mention Sentry as an integration target for PR workflow automation.

## Documentation

Primary docs at https://docs.sentry.io/ — platform guides per language, product docs (Error Monitoring, Tracing, Session Replay, Logs, Seer), AI section (`/ai/` — MCP, agent skills, LLM monitoring), integrations, API reference, CLI (`sentry-cli`), and concepts. `llms.txt` at sentry.io catalogs products and key doc entry points.
