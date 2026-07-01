---
type: source
source_url: https://retool.com/
tags:
  - internal-tooling
  - low-code
  - ai-agents
  - workflow-automation
  - enterprise-governance
  - app-builder
  - mobile-apps
  - postgres-database
related:
  - n8n.io
  - zapier.com
  - coleam00-agent-control-plane
  - factory.ai
  - lovable.dev
product: retool
detail_level: standard
created: 2026-06-30
updated: 2026-07-01
---

Retool is an enterprise development platform for building, deploying, and governing internal software — admin panels, dashboards, AI agents, workflows, and mobile apps — on top of existing data sources and APIs. Used by 10,000+ companies (Amazon, DoorDash, Ramp, Stripe, OpenAI, Boeing, Pfizer), it sits between fully custom-coded applications and spreadsheet/no-code tools, offering the power and security of the former at the speed of the latter. In the agentic AI space, Retool is directly relevant as both a deployment target for agent dashboards (see [[coleam00-agent-control-plane]]) and as an agent platform in its own right, with first-class AI agent creation, MCP server support, and LLM-integrated workflow automation.

_All claims below are sourced from ../../raw/web/retool.com.md unless otherwise noted._

## What it does

Retool provides a unified "build, automate, deploy, govern" platform across six product areas: **Apps** (web, AI-generated, and classic drag-and-drop), **Agents** (LLM-powered autonomous task runners), **Workflows** (backend automation with visual canvas and code), **Mobile** (native iOS/Android apps for field teams), **Database** (managed PostgreSQL), and **Enterprise** (SSO, RBAC, audit logs, self-hosting). Every artifact built — app, agent, workflow, or mobile app — inherits platform-wide security policies automatically; governance is not configured per tool but enforced by the platform.

## Key features

**App Builder (new AI-native):**
- Prompt full-stack React apps from natural language against live production data (Postgres, Databricks, Salesforce); generated apps respect real schema, roles, and permissions from day one
- Context-aware editing: click any component, @mention a resource, or select app sections to make direct AI-prompted changes
- AI App Generation (`retool.com/ai-app-generation`): generate complete apps from prompts; supports multipage apps, 90+ pre-built UI components (tables, forms, charts, uploads, modals)
- Classic app builder: drag-and-drop visual IDE with JavaScript/SQL customization anywhere
- Version control: Git sync, branching, multi-environment promotion

**Agents:**
- Build autonomous LLM agents that connect to production data sources (Salesforce, Stripe, Databricks, REST APIs, Retool Database, Workflows, MCP servers, or other agents)
- Give agents access to saved queries, pre-built workflows, or custom-built tools; choose any LLM per agent
- Human-in-the-loop controls: agents can request approval, escalate, or pause for review
- Built-in evals for agent quality; real-time monitoring; cost tracking per model; activity audit trail
- Pre-built agent templates: ticket resolution, pre-meeting research, calendar scheduling, fraud detection, logistics intelligence, content review
- Pricing by agent-time × model (like workforce wages)

**Workflows:**
- Visual canvas for multi-step automations: cron-scheduled, webhook-triggered, or API-called; durable execution (jobs run to completion)
- Write logic in JavaScript, SQL, or Python with full library access; built-in branching, looping, filtering
- Connect to 100+ databases, third-party SaaS, REST/GraphQL/gRPC APIs; VPC tunnel for private networks
- AI blocks: generate automations from prompt; inline AI code assistance; generative AI steps (summarize, describe images, generate chat) natively connected to OpenAI, Anthropic, Azure, Amazon Bedrock
- Block-level debugging, historical run inspection, custom retry policies, error notifications

**Mobile:**
- Native iOS and Android app builder for field/warehouse teams (also PWA)
- Native device features: barcode/QR scanning, NFC tag reading, camera, signature capture, GPS; offline editing with sync
- Supports Zebra and Proglove devices; over-the-air updates; bulk user distribution via QR code
- Same governance, SSO, permissions, and audit logging as web apps

**Database:**
- Fully managed PostgreSQL instance embedded in Retool; no database administration required
- Spreadsheet-like editing UI: add tables/columns/fields, filter/sort/search, import/export
- PostgreSQL field types, auto-incrementing keys, data validation

**Integrations:**
- 100+ connectors: Postgres, MySQL, MongoDB, Snowflake, BigQuery, Databricks, Salesforce, Google Sheets, Stripe, Slack, GitHub, Linear, REST, GraphQL, gRPC, and more
- Any LLM provider: OpenAI, Anthropic, Google, AWS Bedrock, Azure OpenAI, bring-your-own model
- MCP server: Retool can be connected to AI agents as an MCP server (external agents call Retool tools via MCP)

## Architecture and concepts

Every Retool artifact shares a **unified resource layer**: connect a database or API once as a "resource," and all apps, agents, and workflows in the org can reference it with the same credentials, governed by the same RBAC policies. Queries (JavaScript, SQL, GraphQL) are authored once and reused across products — an agent can call the same query that powers a dashboard table.

The platform is multi-environment by default (development → staging → production) with Git-based source control for all changes. Deployment options: Retool Cloud (multi-tenant SaaS) or self-hosted in a customer-owned VPC (Docker, Kubernetes, or cloud provider-managed). Self-hosted keeps all data in the customer's network — the Retool backend runs on-premises; only usage telemetry leaves the VPC.

Security model: every app, agent, and workflow inherits org-wide SSO (SAML/OIDC), RBAC (user and group level), data-level permissions, audit logging, and secrets management. Permissions are not configured per app — they are enforced by the platform. SOC 2 Type II certified, HIPAA-ready.

The **new app builder** (2026) generates full React apps from natural language, grounded in the user's production data schema and org permissions. Unlike code generators that produce static stubs, Retool's generated apps are live-connected to data and immediately deployable. The React importer accepts source-code zips (as used by [[coleam00-agent-control-plane]] for its frontend deployment).

## Main APIs

- REST API for programmatic org management (users, groups, permissions, secrets)
- Retool as MCP server (`retool.com/blog/retool-mcp-server`): exposes Retool resources and queries as MCP tools callable by external AI agents
- Webhooks and cron triggers for workflows
- Retool AI API: embed LLM calls (OpenAI, Anthropic, Google, Bedrock, custom) directly in queries and workflow blocks
- Source Control API: Git sync for apps and workflows

## When to use

Retool is the right choice when an engineering or ops team needs: (1) custom internal tooling faster than building from scratch but more powerful than spreadsheets or no-code tools; (2) enterprise security and governance baked in rather than bolted on; (3) a single platform that can deploy both human-operated dashboards and autonomous AI agents against the same data. It is especially strong for organizations already running multiple data systems (Postgres + Salesforce + Stripe + internal APIs) that need a single query/permissions layer. It competes with [[n8n.io]] and [[zapier.com]] on workflow automation but covers a much wider surface (full app UIs, mobile, AI agents). For agent-loop harnesses like [[coleam00-agent-control-plane]] that need a governed React dashboard without full frontend engineering, Retool's React importer provides a natural deployment target.

## Ecosystem

- **MCP**: Retool exposes itself as an MCP server so external AI agents (Claude Code, OpenAI Codex, etc.) can call Retool queries and workflows as tools
- **Vibe-coding / AI-generated apps**: new app builder explicitly targets teams shipping AI-generated ("vibe-coded") apps to production with enterprise controls
- **Templates**: 100+ pre-built app templates covering admin panels, dashboards, approval workflows, customer portals, internal search, CRUD apps
- **Community**: active user forum; customer stories from Fortune 500s (Amazon, Ramp, DoorDash, OrangeTheory, UTMB Health, Zeus)
- **Pricing**: free tier → Team → Business → Enterprise (custom); agents priced separately by model × time
