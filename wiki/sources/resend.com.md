---
type: source
source_url: https://resend.com/
companion_urls:
  - https://github.com/resend/resend-cli
raw_files:
  - ../../raw/web/resend.com.md
  - ../../raw/github/resend-resend-cli.md
tags:
  - email-api
  - transactional-email
  - developer-tooling
  - mcp-server
  - agent-skills
  - cli-tools
  - webhooks
  - email-deliverability
related:
  - must-have-clis-2026
  - x.com-ericzakariasson-building-clis-for-agents
  - webhook.site
  - hunter.io
product: resend
detail_level: standard
created: 2026-06-09
updated: 2026-06-15
---

Resend is the email API for developers — a REST service for sending transactional and marketing emails at scale, designed from the ground up for both human developers and AI agents. Its agentic-first design is visible throughout: the official CLI (`resend`) is explicitly built for CI/CD pipelines and agent subprocesses (non-TTY auto-activates JSON output, structured error codes, `--dry-run` support), an official MCP server (`resend/resend-mcp`) wires into Cursor, Claude, and other MCP clients, and five SKILL.md agent skills (Resend API, React Email, Email Best Practices, CLI, Agent Email Inbox) are distributed from `resend/resend-skills` and installable via `npx skills add resend/resend-skills`. Together these make Resend an infrastructure primitive for agent stacks that need to send or receive email programmatically.

_All claims below are sourced from ../../raw/web/resend.com.md unless otherwise noted._

## What it does

Resend provides a REST API at `https://api.resend.com` for sending transactional and marketing emails. Developers authenticate with a Bearer API key (`re_xxxxxxxxx`) and optionally a User-Agent header to avoid 403 responses. The default rate limit is 5 requests per second per team, adjustable for qualified senders. SDK support spans Node.js, Python, PHP, Ruby, Go, Java, Laravel, Rust, and .NET, with a full OpenAPI 3.0 spec (YAML and JSON) for custom client generation. The Broadcasts dashboard feature adds a no-code path for marketing email campaigns — newsletters, product launches, investor updates, promotions, changelogs — with a markdown editor, dynamic placeholders, test sends, scheduled sends, status tracking, and CSV export.

## Key features

- **REST API with OpenAPI spec** — `https://api.resend.com`, Bearer auth, cursor-based pagination, standardised HTTP error codes
- **MCP Server** (`github.com/resend/resend-mcp`) — exposes Resend capabilities to Cursor, Claude Desktop, and any MCP-compatible agent without writing HTTP client code
- **Official CLI** (`resend`) — interactive for humans, fully non-interactive for agents and CI/CD; auto-detects TTY to switch between formatted and JSON output; `resend commands` prints the full command tree as JSON for agent discovery (../../raw/github/resend-resend-cli.md)
- **Agent Skills** — five SKILL.md files covering API usage, React Email, email best practices, CLI operations, and agent email inbox management; discoverable via `https://resend.com/.well-known/agent-skills/index.json`
- **Webhooks** — real-time event delivery via Svix-signed payloads; 14 event types across email, contact, and domain categories; `resend webhooks listen` for local dev tunnel testing
- **Domains** — SPF, DKIM, custom return path, open/click tracking, Enforced TLS; subdomain strategy recommended over root domains
- **Broadcasts** — no-code marketing email editor with template cloning, draft/scheduled/sent status workflow, bulk operations, and CSV export
- **llms.txt + machine-readable content** — landing, docs, blog, changelog, handbook, customers, legal, migrate, and security sections all expose `.md` endpoints and a structured llms.txt catalog for agent consumption

## Architecture

Resend's architecture separates the sending plane (REST API at `api.resend.com`) from the management plane (dashboard, domain config, broadcasts, contact lists). (../../raw/github/resend-resend-cli.md)

The CLI (`resend/resend-cli`, MIT, TypeScript, v2.3.0) resolves its API key through a three-level priority chain — `--api-key` flag > `RESEND_API_KEY` env var > `~/.config/resend/credentials.json` — and stores per-profile credentials at `0600` permissions. The CLI ships its own SKILL.md agent skill and the `skill-evals/` test suite for skill quality assurance. (../../raw/github/resend-resend-cli.md)

Webhook payloads are signed with Svix headers (`svix-id`, `svix-timestamp`, `svix-signature`), verified client-side with `resend.webhooks.verify()`. The `email.received` event is notable for agent workflows: it enables an inbox pattern where an agent is notified when it receives a reply, enabling bidirectional email communication from agent processes. (../../raw/github/resend-resend-cli.md)

## Installation

```bash
# CLI via curl
curl -fsSL https://resend.com/install.sh | bash

# CLI via npm
npm install -g resend-cli

# CLI via Homebrew
brew install resend/cli/resend

# Install agent skills
npx skills add resend/resend-skills
```
(../../raw/github/resend-resend-cli.md)

## Example usage

```bash
# Authenticate (interactive)
resend login

# Send email (all flags, agent-safe)
resend emails send \
  --from "sender@example.com" \
  --to recipient@example.com \
  --subject "Hello" \
  --text "Body text"

# Validate payload without sending
resend emails send --from ... --to ... --subject ... --text ... --dry-run

# Listen for webhooks locally (requires ngrok tunnel)
resend webhooks listen --url https://xxxx.ngrok-free.app

# CI/CD (no login needed)
export RESEND_API_KEY=${{ secrets.RESEND_API_KEY }}
resend emails send --from deploy@example.com --to team@example.com \
  --subject "Deploy complete" --text "Shipped."
```
(../../raw/github/resend-resend-cli.md)

## When to use

Resend is a strong choice when an agent stack needs to send transactional or marketing email programmatically: deployment notifications, user onboarding flows, error alerts, or bidirectional email threads where the agent listens for replies via `email.received` webhooks. Its agent-first design — JSON CLI output, structured error codes, `--dry-run`, SKILL.md skills, MCP server, and OpenAPI spec — means agents can invoke it as a subprocess or MCP tool with minimal friction. The [[must-have-clis-2026]] source profiles Agentmail (a related ephemeral-inbox CLI) in the same category; Resend covers the full production sending path while Agentmail focuses on ephemeral inboxes.

## Maintenance status

372 GitHub stars, MIT license, TypeScript, latest release v2.3.0 (2026-05-28), active development cadence (last push 2026-06-05). (../../raw/github/resend-resend-cli.md)

## Ecosystem

Resend maintains nine official SDK libraries (Node.js, Python, PHP, Ruby, Go, Java, Laravel, Rust, .NET), a public OpenAPI 3.0 spec, and a companion open-source React Email project for building HTML email templates in JSX. The `resend/resend-skills` repository distributes SKILL.md skills compatible with `npx skills add` and the [[skills.sh]] ecosystem. The MCP server at `resend/resend-mcp` wires into the same MCP client ecosystem as other MCP tools in this wiki. Migration guides at `resend.com/migrate` cover transitions from SendGrid, Mailgun, Postmark, and other providers.
