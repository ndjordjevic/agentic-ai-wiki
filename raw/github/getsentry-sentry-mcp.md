# getsentry/sentry-mcp

## Metadata
- Stars: 748
- Primary language: TypeScript
- Default branch: main
- Latest release: 0.36.0 (2026-06-08)
- License: Other
- Homepage: https://mcp.sentry.dev
- Fetched: 2026-06-30
- Final URL: https://github.com/getsentry/sentry-mcp

## Description
An MCP server for interacting with Sentry via LLMs.

## README

Sentry's MCP service is primarily designed for human-in-the-loop coding agents. Tool selection prioritizes developer workflows and debugging use cases, not a general-purpose MCP server for all Sentry functionality.

This remote MCP server acts as middleware to the upstream Sentry API, optimized for coding assistants like Cursor, Claude Code, and similar development tools. Based on Cloudflare's remote MCP work.

### Claude Code Plugin

```shell
claude plugin marketplace add getsentry/sentry-mcp
claude plugin install sentry-mcp@sentry-mcp
```

Provides a `sentry-mcp` subagent Claude delegates to for Sentry errors, issues, traces, or performance.

Experimental: `claude plugin install sentry-mcp@sentry-mcp-experimental`

### Stdio transport (self-hosted Sentry)

```shell
npx @sentry/mcp-server@latest --access-token=sentry-user-token
```

Required token scopes: org:read, project:read, project:write, team:read, team:write, event:write

Self-hosted: `--host=sentry.example.com` (optional `--insecure-http`)

Disable unsupported skills: `--disable-skills=seer`

AI-powered search tools (`search_events`, `search_issues`, etc.) require an LLM provider (OpenAI, Azure OpenAI, Anthropic, OpenRouter) via `EMBEDDED_AGENT_PROVIDER`.

### Example stdio MCP config

```json
{
  "mcpServers": {
    "sentry": {
      "command": "npx",
      "args": ["@sentry/mcp-server"],
      "env": {
        "SENTRY_ACCESS_TOKEN": "your-token",
        "EMBEDDED_AGENT_PROVIDER": "openai",
        "OPENAI_API_KEY": "sk-..."
      }
    }
  }
}
```

### Local development

```shell
make setup-env
pnpm dev   # http://localhost:5173/mcp
pnpm test
pnpm eval
pnpm -w run cli "who am I?"
```

## Docs

### Architecture overview

pnpm monorepo packages:
- `mcp-core` — private core (tools, API client, `buildServer()`)
- `mcp-server` — published `@sentry/mcp-server` stdio CLI
- `mcp-cloudflare` — Cloudflare Workers remote deployment
- `mcp-server-evals`, `mcp-server-mocks`, `mcp-test-client`

### Claude Code plugin structure

| Plugin | MCP URL | Purpose |
|--------|---------|---------|
| `sentry-mcp` | `https://mcp.sentry.dev/mcp` | Default catalog |
| `sentry-mcp-experimental` | `https://mcp.sentry.dev/mcp?experimental=1` | Forward-looking flags |

Agent `allowedTools` includes: `analyze_issue_with_seer`, `search_issues`, `get_sentry_resource`, and others auto-generated from tool definitions.

## Top-level structure

| Type | Name | Notes |
|---|---|---|
| dir | packages/ | mcp-core, mcp-server, mcp-cloudflare, evals, mocks, test-client |
| dir | docs/ | Contributor docs (architecture, testing, operations, integrations) |
| dir | plugins/ | Claude Code plugin variants |
| dir | .claude-plugin/ | Plugin marketplace registry |
| file | AGENTS.md | Contributor agent instructions |
| file | CLAUDE.md | Symlink to AGENTS.md |
| file | .mcp.json | MCP server config |
| file | package.json | pnpm workspace root |
