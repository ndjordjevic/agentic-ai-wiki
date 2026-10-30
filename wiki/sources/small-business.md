---
type: source
category: "Agent Skills & plugins ecosystem"
source_url: https://github.com/anthropics/knowledge-work-plugins/tree/main/small-business
tags:
  - anthropic-plugin
  - small-business-skills
  - approval-gates
  - finance-sales-marketing
  - claude-code-cowork
  - skill-router
related:
  - anthropics-skills
  - buildpartner.ai
  - canva.com
  - claudemarketplaces.com
product: small-business
detail_level: standard
created: 2026-10-30
updated: 2026-10-30
---

Anthropic's **Small Business** plugin (`anthropics/knowledge-work-plugins`, v1.35.1) ships 44 Claude skills spanning finance, sales, marketing, customers, ops/hiring, briefings, and setup — plus an `smb-router` that maps plain-English requests to the right skill with approval gates before any send/pay/post.

_All claims below are sourced from ../../raw/web/small-business.md unless otherwise noted._

## What it does

Install from claude.com/plugins (Cowork) or Claude Code (`claude plugin marketplace add anthropics/knowledge-work-plugins` then `claude plugin install small-business@knowledge-work-plugins`). Say "get me started" for a ~15-minute onboard that connects tools, runs one real task, and captures brand. Skills work from CSV/email/PDF/chat without connectors; connectors deepen integrations. Explicit disclaimer: not financial/tax/legal/HR advice.

## Key features

- 44 skills: 12 finance, 8 sales/leads, 8 marketing, 4 customers/proposals, 5 ops/hiring, 2 briefings, 5 setup/building (`smb-onboard`, `smb-router`, `brand-style`, `build-agent`, `build-connector`)
- Eleven multi-skill workflows (e.g. close-month, plan-payroll) with per-step approvals
- Safety: no invented numbers; no outbound actions without explicit yes; data scoped to the run
- Shared reference docs under `shared/` (QuickBooks traps, Gmail traps, untrusted content, currency/locale, etc.)
- `.mcp.json` + plugin manifest for Connectors tab tooling

## Architecture and concepts

Plugin package under `small-business/` with `.claude-plugin/plugin.json`, per-skill `skills/<name>/SKILL.md` (+ reference/), and shared policy markdown. Router skill selects workflows from natural language. Connectors optional and dedupe-aware if also connected outside the plugin.

## Main APIs

- Claude Code / Cowork plugin install surface
- Per-skill Agent Skills (SKILL.md) invoked via router or direct ask
- MCP connectors declared in `.mcp.json` (tool-specific; capture lists config presence)

## When to use

- Owner-operators wanting Anthropic-maintained SMB workflows inside Claude rather than ad-hoc prompting
- Teams needing approval-gated finance/sales/marketing ops with brand-consistent artifacts
- Learning how Anthropic structures production skill packs (as highlighted in the Austin Marchese roundup)

## Ecosystem

Lives in `anthropics/knowledge-work-plugins` alongside other knowledge-work plugins. Adjacent: [[anthropics-skills]], marketplace hubs [[claudemarketplaces.com]], founder coaching alternative [[buildpartner.ai]], Canva skill path [[canva.com]].
