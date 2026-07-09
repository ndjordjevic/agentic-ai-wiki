---
type: source
category: "Business, career & learning"
source_url: https://www.pipedrive.com/
tags: [crm, sales-automation, pipeline-management, ai-sales-assistant, email-marketing, rest-api, saas, workflow-automation]
related: [hunter.io, zapier.com]
product: pipedrive
detail_level: standard
created: 2026-06-18
updated: 2026-06-18
---

Pipedrive is a web-based Sales CRM and pipeline management platform serving 100,000+ companies across 179 countries. Built around activity-based selling — "you can't control results, but you can control the actions that close deals" — it provides a kanban-style deal pipeline, AI-assisted selling, email marketing, and project management under one subscription. For agentic AI workflows, Pipedrive matters primarily as a data source and automation target: its REST API exposes the full CRM surface (deals, contacts, activities, leads, organizations, products, webhooks) and an official developer portal enables app integrations distributed through the Pipedrive Marketplace.

_All claims below are sourced from ../../raw/web/pipedrive.com.md unless otherwise noted._

## What it does

Pipedrive organizes sales activity as a visual pipeline where deals move through user-defined stages. Each deal aggregates contacts, organizations, activities, emails, and notes in one place. Teams configure custom pipelines per product line or market segment; the AI Sales Assistant surfaces next-best actions and risk alerts within those pipelines. Email two-way sync, call logging, and calendar integration eliminate context-switching between Pipedrive and communication tools.

Beyond the core CRM, Pipedrive bundles three adjacent products: **Campaigns** (email marketing with a drag-and-drop builder, audience segmentation, and marketing automation), **Projects** (a kanban-style project board for post-sales delivery), and **Pulse** (AI-powered lead scoring and conversion prioritization).

## Key features

- **Pipeline Management** — customizable kanban stages, drag-and-drop deal movement, rotting-deal alerts
- **Lead Management** — LeadBooster add-on with chatbot, live chat, web forms, and prospector tools; Web Visitors add-on for site-to-CRM identification
- **AI Sales Assistant** — personalized action recommendations, deal health scoring, win probability predictions
- **AI Email Writer/Summarizer** — drafts and summarizes emails in-context; 15+ prompt templates for AI-generated reports
- **Sales Automation** — workflow automations triggered by deal stage changes, activity completions, or time-based conditions; open API and webhooks for custom automation
- **Smart Docs** — shareable document templates with e-signature tracking and view notifications
- **Insights & Reporting** — real-time revenue dashboards, forecasting, team performance leaderboards, goal tracking
- **Integrations** — 500+ app connections through Pipedrive Marketplace; official integrations include Google Workspace, Zapier, Slack, QuickBooks, Asana, and Kixie
- **Mobile Apps** — iOS and Android with offline access, call tracking, and activity scheduling

## Architecture and concepts

Pipedrive organizes its data model around five core entities: **Deals** (the primary unit), **Persons** (contacts), **Organizations**, **Activities** (tasks/calls/meetings), and **Products** (catalog items linkable to deals). A sixth entity, **Leads**, sits in an inbox-style queue separate from the pipeline until qualified.

The platform is a hosted SaaS; there is no self-hosted option. The REST API (v1, with an OpenAPI 3 spec for both v1 and v2) uses token-based authentication, returns JSON, and supports CORS — making it usable from browser-based workflows. The developer portal provides a sandbox environment, official client libraries (Node.js, PHP), community libraries (Python, .NET, Ruby), and example apps (`create-pipedrive-app`, `pipedrive-laravel`).

Webhooks cover the real-time event surface: any CRUD event on any entity can trigger an outbound POST to a configured endpoint, enabling Pipedrive to push state changes into downstream automation pipelines (n8n, Zapier, or custom agents).

## Main APIs

The Pipedrive API (`developers.pipedrive.com/docs/api/v1`) exposes 60+ endpoint groups:

- **Deals** — CRUD, pipeline and stage filtering, deal fields, participants, followers
- **Persons / Organizations / Leads** — contact CRUD, merge, search, notes, files
- **Activities** — schedule and log calls, tasks, meetings; activity types
- **Products** — product catalog CRUD, deal-product linking
- **Pipelines / Stages** — pipeline configuration, stage ordering
- **Webhooks** — subscribe to entity-level events with retry and delivery tracking
- **Users / Teams** — user management, permission sets, role-based access

All requests authenticate via a personal API token or OAuth 2.0. Rate limits apply per token; the developer sandbox account allows testing without touching production data.

## When to use

Pipedrive is a strong fit when:
- A team needs a lightweight CRM focused on pipeline visibility rather than a full enterprise suite (Salesforce, HubSpot)
- An agentic workflow needs to create, read, or update deals/contacts/activities from external triggers (web forms, email events, meeting outcomes)
- Outbound sales automation pipelines (e.g., hunter.io → Pipedrive → Campaigns) need a structured data backbone
- Webhook-driven automations need CRM state to propagate to external systems (Zapier, n8n, Slack)

It is less suited to complex enterprise workflows requiring custom objects, deep CPQ, or native AI-agent execution environments.

## Ecosystem

Pipedrive integrates bidirectionally with [[zapier.com]] (9,000+ apps via Zapier's catalog) and [[n8n.io]] (node-based workflow builder). For contact discovery upstream of Pipedrive, [[hunter.io]] provides domain search and email verification that pairs naturally with Pipedrive lead ingestion. Outbound email can be supplemented with transactional delivery infrastructure (see Resend, in this wiki at [[resend.com]]).

The Pipedrive Marketplace lists 500+ apps. The developer portal at `developers.pipedrive.com` provides sandbox accounts, OpenAPI specs, and community library support for building custom integrations. An official MCP integration is not listed at the time of this ingest; agents consume Pipedrive via its REST API directly or via Zapier's MCP server action catalog.
