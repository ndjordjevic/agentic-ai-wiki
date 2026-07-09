---
type: source
category: "Workflow automation & no-code platforms"
source_url: https://zapier.com/
companion_urls:
  - https://github.com/zapier/sdk
raw_files:
  - ../../raw/web/zapier.com.md
  - ../../raw/github/zapier-sdk.md
tags:
  - no-code-automation
  - mcp-server
  - ai-agents
  - workflow-orchestration
  - app-integration
  - enterprise-governance
  - typescript-sdk
  - multi-model
related:
  - crewai.com
  - langchain.com
  - script.it
  - strandsagents.com
  - n8n.io
  - pipedrive.com
  - retool.com
  - postiz.com
  - clickup.com
  - trigger.dev
product: zapier
detail_level: standard
created: 2026-06-15
updated: 2026-07-03
---

Zapier is a no-code AI orchestration platform and governance layer that connects 9,000+ applications to AI agents, workflows, and developer tools. It sits between AI models (Claude, ChatGPT, Gemini, Cursor) and enterprise app stacks, providing credential management, action-level controls, audit trails, and workflow logic that persist regardless of which AI surface a team uses. Alongside the no-code Zaps and hosted Agents products, Zapier exposes a TypeScript SDK (`@zapier/zapier-sdk`) for coding agents and a Model Context Protocol server for MCP-aware clients — making it both a citizen-automation tool and a programmable integration backbone for agentic AI systems.

_All claims below are sourced from ../../raw/web/zapier.com.md unless otherwise noted._

## What it does

Zapier automates work by connecting apps through triggers and actions (Zaps), running hosted AI agents that take actions across 9,000+ apps on behalf of users, and exposing those same app connections to external AI tools via MCP and a TypeScript SDK. Three primitives cover the full range of use: **Zaps** (event-driven workflows), **Agents** (AI teammates that work autonomously), and **MCP / SDK** (developer access points for AI clients and backend code). Zapier Tables provide structured storage that all three can read and write, and Zapier Forms generate the trigger inputs for workflow-based use cases.

## Key features

- **9,000+ app integrations with 30,000+ actions** — pre-built connectors spanning SaaS, databases, email, calendar, CRM, ticketing, and developer tools
- **Zapier MCP server** — connects Claude, ChatGPT, Cursor, VS Code, Windsurf, and other MCP-aware clients to the full integration catalog using natural language; 195,000+ servers deployed, 4.6 million tool calls completed
- **Hosted AI Agents** — build specialized agents from templates (lead enrichment, support ticket routing, content creation, IT helpdesk); monitor activity and chat when needed; no-code setup
- **Zapier SDK (TypeScript, open beta)** — `@zapier/zapier-sdk` gives coding agents and backends programmatic access to all app actions; type-safe generated types per app, runtime discovery via `listApps` / `listActions` / `getActionInputFieldsSchema`, auth and token refresh managed automatically (../../raw/github/zapier-sdk.md)
- **Enterprise governance** — action-level restrictions, domain restrictions, VPC Peering, SCIM provisioning, role-based workspaces, immutable audit records, real-time log streaming, SOC 2 Type II / SOC 3 / GDPR / CCPA compliance
- **AI governance layer** — credentials, access controls, and workflow context persist across AI model switches; teams can swap between Claude, ChatGPT, Gemini without rebuilding automations
- **Powered by Zapier (embedding)** — Workflow API, embedded Zap editor, White Label, and MCP embedding allow SaaS products to bring Zapier's automation inside their own interfaces

## Architecture

Zapier's platform separates concerns into distinct surfaces that share the same auth and integration layer: (../../raw/github/zapier-sdk.md)

- **Zaps (trigger → action chains)** are the foundational automation primitive, event-driven and no-code.
- **Agents** run on top of the same integration layer; they use Zapier's app connections and can invoke any Zap action as a tool call. Agents have long-term memory (via knowledge sources), multi-turn conversation, and activity monitoring.
- **Zapier MCP** exposes the integration catalog as MCP tools, letting an MCP-aware AI client call any action using natural language. Zapier manages authentication, rate limiting, and encryption — the client just describes what it wants.
- **Zapier SDK** is the TypeScript surface for coding agents and backends: `createZapierSdk()` → `findFirstConnection()` → `zapier.apps.<app>({ connection })` → `<app>.write.<action>({ inputs })`. Chained multi-app workflows (the "Zapier superpower") are covered in `examples/chained/`. (../../raw/github/zapier-sdk.md)
- **Zapier Tables** provide the storage primitive — structured data readable and writable by Zaps, agents, and embedded interfaces alike.
- All surfaces share a single **governance layer**: credential vault, audit log, action-level controls, and workspace-scoped policies. (../../raw/github/zapier-sdk.md)

## Installation

Zapier MCP requires no terminal access — connect it to an AI client from zapier.com/mcp and describe actions in plain language.

For the TypeScript SDK: (../../raw/github/zapier-sdk.md)

```bash
npm install @zapier/zapier-sdk
npm install -D @zapier/zapier-sdk-cli @types/node typescript
npx zapier-sdk login
```

A skill can also be installed into an agent runtime: `npx skills add zapier/sdk` — adds `skills/zapier-sdk/SKILL.md` to the local skills directory. (../../raw/github/zapier-sdk.md)

## Example usage

Basic SDK call — send a Slack message as an authenticated user: (../../raw/github/zapier-sdk.md)

```typescript
import { createZapierSdk } from "@zapier/zapier-sdk";

const zapier = createZapierSdk();

const { data: connection } = await zapier.findFirstConnection({
  app: "slack",
  owner: "me",
});

const slack = zapier.apps.slack({ connection: connection.id });

await slack.write.direct_message({
  inputs: { channel: "U12345", text: "Hello from Zapier SDK" },
});
```

Runtime action discovery when the action key is unknown: (../../raw/github/zapier-sdk.md)

```typescript
// Enumerate available actions
for await (const action of zapier.listActions({ app: "slack" }).items()) {
  console.log(action.key, action.type, action.label);
}

// Inspect input schema for dynamic fields (e.g. Notion DB columns)
const { data: schema } = await zapier.getActionInputFieldsSchema({
  app: "notion",
  actionType: "write",
  action: "create_page",
});
```

The `examples/chained/` directory in the SDK repo covers multi-app orchestration patterns (inbound lead orchestration, daily revenue summary, HubSpot contacts mirror). (../../raw/github/zapier-sdk.md)

## When to use

- **No-code teams** that need to wire apps and add AI without engineering involvement — Agents and Zaps cover this path end-to-end.
- **Developers building AI agents or backends** that need authenticated access to SaaS APIs without managing OAuth flows — the SDK is the right surface.
- **MCP-client users (Claude Desktop, Cursor, VS Code)** that want to trigger real-world app actions from chat — Zapier MCP requires no code.
- **Enterprises that need AI governance** across multiple models and teams — the audit trail, action-level controls, and workspace policies are the differentiated layer.
- **SaaS products** wanting to embed automation or MCP into their own interface — Powered by Zapier provides the Workflow API, White Label, and embedded MCP.

## Maintenance status

SDK repo (`zapier/sdk`) has 234 stars, MIT license, active development (last push 2026-06-12), no formal releases yet (open beta). The core SDK npm package is `@zapier/zapier-sdk`; companion packages include `@zapier/zapier-sdk-cli` and `@zapier/zapier-sdk-core`. The `zapier/zapier-platform` repo (for integration builders) is a separate codebase. (../../raw/github/zapier-sdk.md)

## Ecosystem

Zapier MCP is a sibling product to the SDK, using `@zapier/zapier-sdk-mcp`: both access the same 9,000+ integration catalog but through different interfaces (natural language vs. code). The `zapier/zapier-mcp` GitHub repo hosts the MCP server implementation. Integration builders publish apps to the Zapier directory through the developer platform (`docs.zapier.com/integrations`) using `zapier-platform-cli` and `zapier-platform-core`. The Zapier community (community.zapier.com) and Help Center (help.zapier.com) serve end-users and troubleshooting. For agent-framework context in this wiki, see [[crewai.com]] (multi-agent orchestration), [[langchain.com]] (orchestration platform), and [[strandsagents.com]] (model-driven agent SDK).
