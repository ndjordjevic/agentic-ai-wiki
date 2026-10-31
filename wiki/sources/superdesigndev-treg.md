---
type: source
category: "MCP servers & integrations"
source_url: https://github.com/superdesigndev/treg
tags:
  - tool-registry
  - credential-injecting-proxy
  - agent-tool-catalog
  - mcp-gateway
  - openrouter-for-tools
  - workflow-skills
  - prepaid-metering
  - self-hostable
related:
  - monid.ai
  - openrouter.ai
  - smithery.ai
  - glama.ai
  - skills.sh
  - tavily.com
  - apify-apify-mcp-server
  - anysearch.com
product: treg
detail_level: standard
created: 2026-10-31
updated: 2026-10-31
---

treg (~6.8k★, Apache-2.0 with hosted-service restriction; PyPI `tools-registry` v0.28.0) is Superdesign's "OpenRouter for agent tools": one base URL and one `X-Treg-Token` give agents a curated catalog of thousands of priced endpoints (SEO, enrichment, ads, scraping, media generation, …) plus team-owned tools, skills, and CLIs whose credentials stay on the server. Hosted at [treg.to](https://treg.to); anyone can self-host the registry.

_All claims below are sourced from ../../raw/github/superdesigndev-treg.md unless otherwise noted._

## What it does

Agents discover work by task (`treg catalog search "backlinks for a domain"`), read price and schema, then call through the proxy. Catalog calls use a credential ladder: the team's own tool/key first, else a verified public free route, else treg's prepaid key (billed in fractions of a cent; new eligible teams get $1 free). Team-registered endpoints, CLIs, and `SKILL.md` bundles are never metered when using the org's own secrets. The proxy relays upstream APIs faithfully and injects auth server-side — it does not remodel vendor APIs. Surfaces include CLI, HTTP `/call/...`, MCP (`/mcp/` and Claude Connectors `/mcp/v2/`), Claude Code / Cursor / MiniMax plugins, and `skills.sh` workflow skills (`treg`, `web-access`, `lead-signals`, `recruit`, `make-ugc`, `jev-memory`, …). A newer **tool hub** lets teams publish composable tools (recipe or sandboxed `run.js`) with `per_call` / `per_result` / `percent` pricing for other agents to call.

## Installation

Hosted quickstart: `curl -fsSL https://treg.to/install.sh | sh`, then `treg login` (GitHub, email OTP, or `--token` for agents/CI) and `treg catalog search` / `treg call …`. Claude Code: `/plugin marketplace add superdesigndev/treg` then `/plugin install treg@treg`. Skills CLI: `npx skills add superdesigndev/treg`. Self-host / develop: `scripts/dev-local.sh up` (tmux + uv, SQLite, OTP shown on page) or `pip install "tools-registry[server]"` / `uv run python -m treg` on port 18790. Base `pip install tools-registry` is CLI-only; the `[server]` extra adds FastAPI, DB, encryption, MCP, and hub sandbox.

## Key features

- Task-oriented catalog search and routed capabilities (`treg.web.search`, `treg.people.email.find`, …) with optional multi-provider confirm/decisive headers
- Own-key precedence and unmetered BYOK; anonymous public routes free; prepaid balance with 402 + top-up URL when empty
- Share via `treg scan` / `treg upload` (`.env` keys, skills, catalog CLIs) or manual `tool add` / OAuth connect / multi-binding injectors
- `treg run` / `treg shell` for vendor CLIs with org credentials injected; audit via `treg calls` / `treg runs` / health probes
- Org/teams (owner/admin/member/viewer), invites, per-member tool access, optional WorkOS enterprise SSO
- Hub publish/list/earnings; Enrich Arena and Web Arena for comparing vendors; pinned customer read scopes for restricted agents
- Agent distribution: llms.txt / skill.md entrypoints, marketplace plugins, Discord community

## Architecture

Request flow for `/call`: resolve tool (host + longest `base_url` prefix, or by name) → decrypt secret(s) → apply binding injectors (`env`, `secret_file`, `oauth`, `cli_auth`) → stream upstream → fire-and-forget audit. Faithful-relay contract changes only hop-by-hop headers, treg control headers/cookies (stripped), and injected credentials. Core package under `src/treg/`: `proxy.py` (`relay()`), `injectors.py`, `oauth.py`, `api.py` (brain), thin `cli.py`, SQLModel models, crypto/config/db/audit, plus MCP front door and hub sandbox (QuickJS) in the server extra. Design depth lives in `docs/context/` fragments kept in sync via the `/tools-registry-context` skill. Dashboard/frontend under `frontend/` + `src/treg/web/`.

## Example usage

```bash
curl -fsSL https://treg.to/install.sh | sh
treg login
treg catalog search "find a work email"
treg call hunter.people.email.find --query domain=reddit.com --query full_name="Alexis Ohanian"
treg balance

# Or agent-native HTTP passthrough:
# GET https://treg.to/call/https://api.intercom.io/conversations?per_page=5
# Header: X-Treg-Token: <token>
```

## Maintenance status

~6,825 stars, ~592 forks, default branch `main`, no GitHub Releases tags at ingest (PyPI version 0.28.0; active tip pushed 2026-10-31). License is Apache-2.0 plus additional terms forbidding redistributing a competing hosted/managed registry without written permission; self-hosting for your own org and calling hosted treg.to APIs are encouraged. Changelog Unreleased covers hub tools, jev-memory skill, and email find/verify routing confirm headers. Roadmap notes in README include MCP expansion, finer permissions, and KMS hardening.
