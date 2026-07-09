---
type: source
category: "MCP servers & integrations"
source_url: https://hunter.io/
tags:
  - email-finder
  - email-verification
  - outreach-automation
  - domain-search
  - cold-email
  - rest-api
  - b2b-leads
  - lead-generation
related:
  - resend.com
  - pipedrive.com
product: hunter
detail_level: standard
created: 2026-06-15
updated: 2026-06-18
---

Hunter is an all-in-one email outreach platform that lets individuals and teams find verified professional email addresses, validate them, and run personalized cold email sequences — serving over 7 million users across sales, marketing, and recruiting workflows.

_All claims below are sourced from ../../raw/web/hunter.io.md unless otherwise noted._

## What it does

Hunter addresses the prospecting half of outbound sales: given a company domain or a person's name, it surfaces verified email addresses drawn from a database of over 100 million professional contacts. Users can then build sequences — multi-step cold email campaigns — sent through their own Gmail, Google Workspace, or Outlook accounts. The platform combines contact discovery, email validation, and lightweight campaign management in one product.

## Key features

- **Domain Search** — returns all known email addresses for a company's domain with confidence scores, source attribution, and department filters; supports bulk lookups and API access.
- **Email Finder** — given a name and company domain, finds the single most probable verified address.
- **Email Verifier** — performs format, DNS, SMTP, and catch-all checks without requiring signup; bulk verification and Google Sheets / CRM integrations (HubSpot, Pipedrive) also available.
- **B2B Database (Discover)** — company-level prospecting that returns matching targets from natural-language or structured filter queries; free via the API.
- **Email Sequences** — personalized cold email campaigns with multi-step follow-ups sent from the user's own email account; free plan supports up to 500 recipients per sequence.
- **Browser Extension** — Chrome extension with 600 000+ users for in-context contact lookup while browsing LinkedIn or company websites.
- **AI Writing Assistant** — included on paid plans for drafting sequence copy.

## Architecture and concepts

Hunter's core is a contact intelligence layer built from publicly sourced web data. Every address in the database carries a discovery date, source references, and a verification status — either actively verified (SMTP-confirmed) or confidence-scored (pattern-derived). Domain Search returns up to 100 addresses per request; bulk access is available via the REST API or the enterprise data platform for high-volume programmatic use.

The REST API (`https://api.hunter.io/v2/`) is the developer-facing interface. All endpoints share a JSON envelope with `data`, `meta`, and optional `error` fields. Authentication accepts an API key as a query parameter (`api_key`), header (`X-API-KEY`), or Bearer token. A test key (`test-api-key`) returns synthetic responses for parameter validation. The API also exposes full CRUD for leads, lead lists, custom attributes, and email sequences — all at no per-request charge.

## Main APIs

| Endpoint | Method | Purpose |
|---|---|---|
| `/v2/domain-search` | GET | All emails for a domain (up to 100 per request) |
| `/v2/email-finder` | GET | Single best email for a name + domain |
| `/v2/email-verifier` | GET | Deliverability and validity check for an address |
| `/v2/companies/discover` | POST | Company discovery by natural-language or filter query |
| `/v2/people/enrichment` | GET | Full profile enrichment for a person |
| `/v2/companies/enrichment` | GET | Company profile enrichment |

Rate limits: Discover (5 req/s, 50/min), Domain Search & Email Finder (15 req/s, 500/min), Email Verifier (10 req/s, 300/min).

## When to use

Hunter fits outbound sales, link-building, PR outreach, and recruiting where the key bottleneck is finding and validating a contact's email before reaching out. It is not a transactional email sender (see [[resend.com]] for that); it is the contact-discovery layer that feeds outreach tooling. Agentic workflows that need to resolve a person's email from a name + company, or that need to bulk-validate a lead list before an automated sequence, can integrate directly via the REST API.

## Ecosystem

- **CRM integrations**: HubSpot, Pipedrive (native); Salesforce, others via Zapier.
- **Productivity add-ons**: Google Sheets add-on, Gmail extension for in-context lookup.
- **Pricing tiers**: Free (50 credits/month), Starter (€34/mo yearly, 2 000 credits), Growth (€104/mo yearly, 10 000 credits), Scale (€209/mo yearly, 25 000 credits), Enterprise (custom). All paid plans include auto-verification, lead enrichment, unlimited users, and CSV export.
- **Compliance**: GDPR-aligned; data sourced exclusively from public web content.
