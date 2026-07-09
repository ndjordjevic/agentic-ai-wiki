---
type: source
category: "MCP servers & integrations"
source_url: https://mcp.sentry.dev/
companion_urls:
  - https://github.com/getsentry/sentry-mcp
raw_files:
  - ../../raw/web/mcp.sentry.dev.md
  - ../../raw/github/getsentry-sentry-mcp.md
tags:
  - mcp-server
  - sentry-integration
  - production-debugging
  - coding-agents
  - oauth-mcp
  - seer
  - remote-mcp
  - agent-tools
related:
  - sentry.io
  - microsoft-playwright-mcp
  - greptile.com
  - qa.tech
  - skills.sh
  - deepwiki.com
product: sentry
detail_level: standard
created: 2026-06-30
updated: 2026-07-03
---

Sentry MCP is Sentry's official **remote Model Context Protocol server** that connects coding agents (Cursor, Claude Code, VS Code, Codex, Windsurf, Zed, etc.) to live Sentry production data via OAuth — no local clone or API token juggling for the hosted path. The endpoint `https://mcp.sentry.dev/mcp` exposes tools for fetching issues, searching errors and events, analyzing traces, invoking Seer root-cause analysis, and reading Sentry docs — so agents debug with real stack traces and user impact instead of pasted screenshots. The open-source implementation lives in `getsentry/sentry-mcp` (748 stars, TypeScript, Cloudflare Workers deployment + optional `@sentry/mcp-server` stdio package for self-hosted Sentry).

_All claims below are sourced from ../../raw/web/mcp.sentry.dev.md unless otherwise noted._

## What it does

Sentry MCP is middleware between an LLM-powered coding agent and the Sentry API, scoped specifically for **human-in-the-loop developer debugging workflows** — not a general-purpose MCP surface for every Sentry admin function. A developer connects their editor or CLI agent to the remote HTTP endpoint (or runs stdio locally), authenticates via OAuth on first connect, and then asks natural-language questions: "what's breaking in production?", "fix this Sentry issue URL", "why is checkout slow?". The agent calls MCP tools (`get_sentry_resource`, `search_issues`, `analyze_issue_with_seer`, etc.) to pull structured issue, trace, and Seer analysis data, then applies fixes in the local codebase.

The landing page demos a full loop: paste an issue URL → fetch details → Seer analyzes stack trace → LLM proposes and applies a patch → run tests to validate.

## Key features

- **Remote hosted MCP (recommended)** — `https://mcp.sentry.dev/mcp` with OAuth; no `npx` clone, no manual API token for SaaS users; works with Cursor 1.0+ HTTP Streamable transport, Claude Code, VS Code MCP, Codex, Gemini CLI, OpenCode, Warp, Windsurf, Zed.
- **Path scoping** — `.../mcp/{org}` or `.../mcp/{org}/{project}` auto-limits scope and hides discovery tools (`find_organizations`, `find_projects`) for tighter agent context.
- **Agent mode** (`?agent=1`) — collapses to a single `use_sentry` tool; embedded AI chains sub-tool calls from natural language (~2x latency).
- **Experimental mode** (`?experimental=1`) — forward-looking tool variants.
- **Seer integration** — `analyze_issue_with_seer` tool brings Sentry's AI debugger into the agent loop for root-cause analysis and fix suggestions.
- **Claude Code plugin** — `claude plugin install sentry-mcp@sentry-mcp` registers a `sentry-mcp` subagent auto-delegated for errors, issues, traces, and performance questions.
- **Stdio / self-hosted** — `@sentry/mcp-server` npm package for self-hosted Sentry (`--host`, `--insecure-http`, `--disable-skills=seer`); requires User Auth Token with org/project/team/event scopes. (../../raw/github/getsentry-sentry-mcp.md)
- **AI-powered search tools** — `search_events`, `search_issues` translate natural language to Sentry query syntax via embedded LLM (OpenAI, Anthropic, OpenRouter, Azure OpenAI); configurable via `EMBEDDED_AGENT_PROVIDER`.

## Architecture

pnpm monorepo (`getsentry/sentry-mcp`):
- **`mcp-core`** (private) — MCP protocol, Sentry API client, tool implementations, `buildServer()`.
- **`mcp-server`** — published as `@sentry/mcp-server`; stdio CLI bundling mcp-core.
- **`mcp-cloudflare`** — Cloudflare Workers deployment powering the remote `mcp.sentry.dev` service and live demo UI.
- **`mcp-server-evals`**, **`mcp-server-mocks`**, **`mcp-test-client`** — evals, fixtures, and CLI test harness.

Remote server is based on Cloudflare's remote MCP pattern. Contributor docs live in `docs/` (architecture, testing, operations, integrations). Agent skills installed via `npx @sentry/dotagents install` from `getsentry/skills`. (../../raw/github/getsentry-sentry-mcp.md)

## Installation

**Cursor / VS Code / generic HTTP client:**
```json
{
  "mcpServers": {
    "sentry": {
      "url": "https://mcp.sentry.dev/mcp/my-org/my-project"
    }
  }
}
```

**Claude Code:**
```bash
claude mcp add --transport http sentry https://mcp.sentry.dev/mcp
```

**One-liner (MCP-compatible clients):**
```bash
npx add-mcp https://mcp.sentry.dev/mcp
```

**Self-hosted Sentry (stdio):**
```bash
npx @sentry/mcp-server@latest --access-token=TOKEN --host=sentry.example.com
```

(../../raw/github/getsentry-sentry-mcp.md)

## Example usage

Paste `https://sentry.io/issues/...` into Cursor chat with Sentry MCP connected. Cursor calls `find_organizations` → `find_projects` → `search_issues` (or `get_sentry_resource` on the URL), returns issue title, culprit, stack trace, and user impact. Ask "analyze with Seer" → `analyze_issue_with_seer` returns root cause. Agent edits the flagged file, runs `pnpm test`, and validates the fix — all without leaving the IDE or manually copying stack traces.

For automation: Sentry alert webhooks can trigger a coding agent (e.g. Cursor Automations) that uses Sentry MCP to investigate regressed issues and open draft PRs.

## When to use

Use Sentry MCP when your agentic workflow needs **live production context** from Sentry — not just code generation. Ideal for: investigating specific production errors in Cursor/Claude Code; wiring alert → agent → fix pipelines; giving agents Seer-powered root-cause analysis; scoping an agent to one org/project for safer autonomous debugging.

Use stdio `@sentry/mcp-server` instead of remote when running against **self-hosted Sentry** or air-gapped environments. The broader [[sentry.io]] platform (SDK instrumentation, dashboards, Seer UI) is complementary — MCP is the **agent access layer** on top.

## Maintenance status

Actively maintained: 748 GitHub stars, last push 2026-06-29, latest release 0.36.0 (2026-06-08), TypeScript 98.6%, homepage https://mcp.sentry.dev. Hosted service operated by Sentry (Functional Software, Inc.). (../../raw/github/getsentry-sentry-mcp.md)

## Ecosystem

Pairs with [[sentry.io]] (underlying observability platform and Seer). Sits alongside other MCP servers in this wiki: [[microsoft-playwright-mcp]] (browser automation), [[skills.sh]] (skill distribution). Complements pre-merge quality tools [[greptile.com]] and [[qa.tech]] by supplying **post-deploy production evidence** to the same coding agents. Claude Code plugin marketplace entry: `getsentry/sentry-mcp`.

## Documentation

- Live docs/setup: https://mcp.sentry.dev/ (includes `llms.txt` catalog)
- GitHub: https://github.com/getsentry/sentry-mcp (`docs/` folder, `AGENTS.md` / `CLAUDE.md`)
- Sentry product docs: https://docs.sentry.io/ai/ (broader AI + MCP integration guide)
