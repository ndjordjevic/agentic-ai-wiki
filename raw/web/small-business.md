# small-business

## Fetch log
- Inbox URL: https://github.com/anthropics/knowledge-work-plugins/tree/main/small-business
- Final URL: https://github.com/anthropics/knowledge-work-plugins/tree/main/small-business
- Fetched: 2026-10-30
- Pages: 1
- Mode: single-page

## Page — https://github.com/anthropics/knowledge-work-plugins/tree/main/small-business
# Anthropic Small Business plugin (knowledge-work-plugins/small-business)

Source tree: https://github.com/anthropics/knowledge-work-plugins/tree/main/small-business

## Directory listing
- .claude-plugin/plugin.json
- .mcp.json
- README.md
- shared/ (safety/style/connector reference docs)
- skills/ (44 skill directories): ad-manager, ap-processor, brand-style, build-agent, build-connector, business-pulse, call-list, canva-creator, cash-flow-snapshot, close-month, content-strategy, contract-review, crm-autopilot, grant-rfp-writer, grow-pipeline, growth-pulse, hiring-screener, inbox-manager, inventory-planner, invoice-chase, job-post-builder, lead-finder, lead-triage, marketing-monday, monday-brief, month-end-prep, outreach-composer, pay-the-bills, payroll-prep, plan-payroll, proposal-builder, reactivate, report-builder, report-pack, restock, review-reputation, seo-ai-visibility, smb-onboard, smb-router, social-content-engine, speed-to-lead, tax-prep, tax-season-organizer, ticket-deflector

## plugin.json
```json
{
  "name": "small-business",
  "displayName": "Small Business",
  "version": "1.35.1",
  "description": "Pre-built small business workflows to help you run and grow your business. Supports a majority of the tools you already use. You approve every step that touches money or customers. Install and then ask Claude to help you get onboarded.",
  "author": {
    "name": "Anthropic"
  },
  "keywords": [
    "all-in-one",
    "automation",
    "finance",
    "growth",
    "hr",
    "marketing",
    "operations",
    "sales",
    "small-business",
    "smb",
    "taxes",
    "workflow",
    "zapier"
  ]
}

```

## .mcp.json
```json
{
  "mcpServers": {
    "airwallex-agentos": {
      "type": "http",
      "url": "https://mcp.airwallex.com/mcp"
    },
    "apollo-io": {
      "type": "http",
      "url": "https://mcp.apollo.io/mcp"
    },
    "atlassian-rovo": {
      "type": "http",
      "url": "https://mcp.atlassian.com/v1/mcp"
    },
    "canva": {
      "type": "http",
      "url": "https://mcp.canva.com/mcp"
    },
    "clay": {
      "type": "http",
      "url": "https://api.clay.com/v3/mcp"
    },
    "docusign": {
      "type": "http",
      "url": "https://mcp.docusign.com/mcp"
    },
    "emergent": {
      "type": "http",
      "url": "https://mcp.emergent.sh"
    },
    "expensify": {
      "type": "http",
      "url": "https://www.expensify.com/mcp"
    },
    "gmail": {
      "type": "http",
      "url": "https://gmailmcp.googleapis.com/mcp/v1"
    },
    "google-calendar": {
      "type": "http",
      "url": "https://calendarmcp.googleapis.com/mcp/v1"
    },
    "google-drive": {
      "type": "http",
      "url": "https://drivemcp.googleapis.com/mcp/v1"
    },
    "gusto": {
      "type": "http",
      "url": "https://mcp.api.gusto.com/anthropic"
    },
    "hubspot": {
      "type": "http",
      "url": "https://mcp.hubspot.com/anthropic"
    },
    "intuit-mailchimp": {
      "type": "http",
      "url": "https://ai-inc.mailchimp.com/claude/mcp/v2"
    },
    "intuit-quickbooks": {
      "type": "http",
      "url": "https://ai-inc.quickbooks.intuit.com/v1/mcp"
    },
    "monday-com": {
      "type": "http",
      "url": "https://mcp.monday.com/mcp"
    },
    "myob": {
      "type": "http",
      "url": "https://mcp.myob.com/mcp"
    },
    "notion": {
      "type": "http",
      "url": "https://mcp.notion.com/mcp"
    },
    "paypal": {
      "type": "http",
      "url": "https://mcp.paypal.com/mcp"
    },
    "ramp": {
      "type": "http",
      "url": "https://mcp.ramp.com/mcp"
    },
    "ringex-chat": {
      "type": "http",
      "url": "https://mcp.labs.ringcentral.com/ringex/v1.1.0/team-chat"
    },
    "shopify": {
      "type": "http",
      "url": "https://setup.shopify.com/mcp"
    },
    "slack": {
      "type": "http",
      "url": "https://mcp.slack.com/mcp",
      "oauth": {
        "clientId": "1601185624273.8899143856786",
        "callbackPort": 3118
      }
    },
    "square": {
      "type": "http",
      "url": "https://mcp.squareup.com/mcp"
    },
    "stripe": {
      "type": "http",
      "url": "https://mcp.stripe.com"
    },
    "tiktok": {
      "type": "http",
      "url": "https://business-api.tiktok.com/open_mcp/tt-ads-mcp-layer"
    },
    "trello": {
      "type": "http",
      "url": "https://mcp.trello.com/v1"
    },
    "wix": {
      "type": "http",
      "url": "https://mcp.wix.com/mcp"
    },
    "xero": {
      "type": "http",
      "url": "https://mcp.xero.com/mcp"
    },
    "zapier": {
      "type": "http",
      "url": "https://mcp.zapier.com/api/v1/connect"
    },
    "zoho-books": {
      "type": "http",
      "url": "https://claude-zohobooks.zohomcp.com/mcp/message"
    },
    "zoho-crm": {
      "type": "http",
      "url": "https://claude-zohocrm.zohomcp.com/mcp/message"
    },
    "zoho-desk": {
      "type": "http",
      "url": "https://claude-zohodesk.zohomcp.com/mcp/message"
    },
    "zoho-projects": {
      "type": "http",
      "url": "https://claude-zohoprojects.zohomcp.com/mcp/message"
    },
    "zoom": {
      "type": "http",
      "url": "https://mcp.zoom.us/mcp/zoom/streamable"
    }
  }
}

```

## README.md
# Small Business — Your AI Business Assistant

**By Anthropic**

One plugin that gives Claude everything it needs to help run your small
business: 44 skills spanning finance, sales, marketing, operations, and
hiring, plus a router that understands plain English.

You don't need to memorize anything. Just tell Claude what you need — "I'm
stressed about making payroll," "a customer is angry," "who owes me money?" —
and it picks the right skill and walks you through it. Every skill pauses
before taking action: nothing sends, posts, or gets paid without your say-so.

> **Important**: This plugin assists with small business workflows but does not
> provide financial, tax, legal, or HR advice. All outputs should be reviewed by
> you (and where appropriate, a qualified professional) before use.

---

## Getting started

1. Install the plugin. In Cowork, install it from
   [claude.com/plugins](https://claude.com/plugins/). In Claude Code:

   ```bash
   claude plugin marketplace add anthropics/knowledge-work-plugins
   claude plugin install small-business@knowledge-work-plugins
   ```
2. Say **"get me started"** — a 15-minute setup connects your first two
   tools, proves value with one real run, learns your business, and captures
   your brand so every report comes out in your colors.
3. From then on, just describe what you need.

No tools connected yet? Every skill still works — from a CSV export, a
pasted email, an uploaded PDF, or plain conversation. Connectors make it
deeper, never mandatory.

Already connected a tool before installing? You may see it listed twice:
once under your own connectors and once on this plugin's Connectors tab.
It is the same tool. Either entry works, the plugin uses whichever is
authorized, and you never need to connect both.

---

## What you can say

**Money & cash**
- "Can I make payroll?" · "Cash forecast" · "Close the books"
- "Pay the bills" · "Who owes me money?" · "Taxes" / "1099s"
- "Build me a report" · "My recurring reports, on schedule"

**Sales & growth**
- "Find me customers" · "Who should I call?" · "Call list"
- "Write this outreach" · "Fill my funnel" · "Win back quiet customers"
- "Quote this job" / "proposal" / "RFP" · "Update the CRM"

**Marketing**
- "Is my marketing working?" · "Weekly growth brief"
- "Make the content" · "Run this brief" · "My ads" · "SEO"
- "What should I promote?"

**Customers & reputation**
- "What are customers saying?" · "A customer is upset"
- "Check my orders — anything about to blow up?"

**Operations & people**
- "Go through my email" · "Brief me" · "Monday brief"
- "Reorder" / "stock" · "Write a job post" · "Screen these applications"
- "Review this contract" · "Grants" / "government bids"

**Make it yours**
- "Update my brand" — your colors and logo on every page, from one link
- "Automate this" — turn a task you repeat into a named skill
- "Connect to my ERP" — connect a tool that has no official connector

## The 44 skills

**Finance (12):** ap-processor · cash-flow-snapshot · close-month ·
invoice-chase · month-end-prep · pay-the-bills · payroll-prep · plan-payroll
· report-builder · report-pack · tax-prep · tax-season-organizer

**Sales & leads (8):** call-list · crm-autopilot · grow-pipeline ·
lead-finder · lead-triage · outreach-composer · reactivate · speed-to-lead

**Marketing (8):** ad-manager · canva-creator · content-strategy ·
growth-pulse · marketing-monday · review-reputation · seo-ai-visibility ·
social-content-engine

**Customers & proposals (4):** contract-review · grant-rfp-writer ·
proposal-builder · ticket-deflector

**Operations & hiring (5):** hiring-screener · inbox-manager ·
inventory-planner · job-post-builder · restock

**Briefings (2):** business-pulse · monday-brief

**Setup & building (5):** smb-onboard · smb-router · brand-style ·
build-agent · build-connector

Eleven of these (like close-month and plan-payroll) are workflows that chain
other skills together with an approval checkpoint at every step.

---

## How it keeps you safe

- **Approval gates everywhere.** Nothing is sent, posted, paid, or written
  to your systems without an explicit yes. Coding bills and paying bills are
  two separate approvals. Payroll is staged; you press the button.
- **No invented numbers.** A figure that can't be read is reported as
  unreadable, never guessed.
- **Your data stays yours.** Skills read what they need for the run and
  write only what you approve.

---

**Current version:** 1.35.1 — 2026-09-15


