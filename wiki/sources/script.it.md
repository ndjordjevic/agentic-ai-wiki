---
type: source
category: "Workflow automation & no-code platforms"
source_url: https://script.it/
tags:
  - ai-automation
  - workflow-builder
  - no-code
  - saas-integration
  - conversational-ai
  - credit-based
  - triggers
  - knowledge-work
related:
  - n8n.io
  - zapier.com
product: script
detail_level: standard
created: 2026-06-15
updated: 2026-06-15
---

Script.it is an AI-powered workflow automation platform that lets non-engineers describe repetitive knowledge-work tasks in plain English and have an AI agent build, validate, and run reusable automations — combining the conversational speed of AI assistants with the integration breadth of workflow platforms like Zapier and n8n. Where visual-node builders require wiring DAGs and AI chat agents produce opaque outputs, Script.it produces "scripts": inspectable, editable, rerunnable sequences of blocks that a user can verify before and after each run.

_All claims below are sourced from ../../raw/web/script.it.md unless otherwise noted._

## What it does

Script.it turns a plain-English description into a working automation workflow without writing code. A user describes their task in the chat interface; the AI agent asks clarifying questions, constructs a script of executable and Markdown blocks, connects the required integrations, and runs the workflow in an isolated execution environment. The result is a named, version-controlled script in the user's workspace that can be triggered manually, on a schedule, via webhook, or on integration events.

The platform positions itself as "the easiest way to build workflows you can trust" — targeting go-to-market, ops, marketing, customer success, and research teams rather than engineers. A switching testimonial from a Flexor Director of Business Operations cites switching from Make (n8n's closest visual competitor) because "every change meant reconnecting nodes and retesting flows."

## Key features

- **AI agent chat** — builds and edits scripts conversationally; the agent maintains transparency about its actions and flags when an integration needs to be connected
- **Scripts** — ordered collections of executable blocks (Python/shell code for API calls, data fetching, file transformation) and Markdown blocks (inline documentation); each script has full version history and is shareable
- **Sessions** — individual conversations with the agent; script changes persist across sessions while each session has its own isolated workspace
- **Triggers** — three automation modes: Schedule (cron or natural-language intervals), Webhook (unique HTTP POST URL), and Integration event (Slack messages, Gmail, Calendly bookings, Linear issues, etc.); trigger actions are either "Send prompt" (judgment tasks) or "Run script" (deterministic execution)
- **600+ integrations** — Slack, Gmail, Notion, HubSpot, Salesforce, Airtable, Google Workspace, Teams, Discord, Shopify, Jira, and more; connected at the account level so all scripts share authorization; custom webhooks cover endpoints outside the catalog
- **Templates** — pre-built workflows across marketing, sales, ops, customer success, research, and engineering roles
- **Credit system** — AI operations and execution time are billed in credits; Free (50/month), Pro ($30/month, 300 credits, $0.10/credit overage), Enterprise (custom)

## Architecture and concepts

The core execution model is **block-based**: every script is a sequence of executable blocks (Python or shell) and Markdown blocks. The agent generates and edits blocks through chat; users can inspect and modify the underlying source files directly. Runs are isolated — multiple executions never interfere with each other — and each run is a new session tied to the script's current block sequence.

The agent layer sits above the block executor and handles intent parsing, integration discovery, clarifying-question generation, and mid-run adaptation. When a needed integration is missing, the agent pauses and prompts the user to authorize it through Settings → Integrations.

Triggers attach to scripts and fire outside the chat interface. Schedule triggers use natural-language intervals or cron expressions with timezone support. Webhook triggers generate a unique URL for external HTTP POST calls. Integration event triggers listen on connected tools (Slack, Gmail, etc.) and can pass event payloads as input values to the script.

Security: data is encrypted in transit (HTTPS/TLS 1.2) and credentials are encrypted at rest. Scripts run in isolated environments on Google Cloud with automatic failover and backups. The enterprise tier is SOC 2 Type II certified with SSO, audit logs, and self-hosting.

## Main APIs

Script.it is a hosted product without a public REST API for external callers. Developer-facing surfaces are:

- **Custom webhook integration** — scripts can send HTTP requests to any external URL from a block, acting as an outbound API client
- **Webhook trigger** — the inbound surface: a unique script URL that fires the script when called by any external service (Zapier, Stripe, etc.)
- **Integration event trigger** — event subscriptions for connected tools
- **`raw/` source files** — scripts expose their underlying Python/shell source files for inspection and direct editing

The technical reference at `docs.script.it/developers/overview` covers trigger payloads, script file structure, and custom system integration patterns.

## When to use

Script.it fits teams where the bottleneck is **non-engineer adoption of automation**: when visual node editors are too technical and pure AI chat agents produce outputs that can't be reliably re-run. Concrete fit signals from the docs:

- Repeatable knowledge-work tasks (reporting, lead enrichment, competitive research, content distribution) with SaaS tool dependencies
- Preference for conversational iteration over DAG rewiring after every change
- Need for on-demand or scheduled execution without engineering involvement
- Requirement to inspect and validate automation steps (not just trust a black-box output)

Not a fit for: custom backend engineering, on-prem-only non-GCP deployments, or ultra-low-latency real-time pipelines.

## Ecosystem

Script.it competes directly with [[n8n.io]] (fair-code visual builder, 500+ integrations, self-hostable, code-when-needed) and [[zapier.com]] (9,000+ app catalog, no-code Zaps, MCP server, enterprise governance). Script.it's differentiation is the conversational iteration model — workflows are built through chat rather than a canvas — and the "scriptable work" thesis (manifesto at scriptable.work) that knowledge-work automations should be verifiable artifacts, not opaque agent sessions.

The company operates under the Bespo.ai brand (support@bespo.ai) and runs on Google Cloud. No public GitHub repo was identified; the platform is closed-source SaaS with enterprise self-hosting available on request.

## Documentation

Documentation lives at `docs.script.it` with six top-level sections: Get Started, Scripts, Sessions, Triggers, Integrations, and Developers. The docs llms.txt at `docs.script.it/llms.txt` enumerates all pages. Key entry points: Quickstart (`docs.script.it/quickstart`) and Core Concepts (`docs.script.it/core-concepts`).
