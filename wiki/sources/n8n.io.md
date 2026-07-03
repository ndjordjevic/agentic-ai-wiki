---
type: source
source_url: https://n8n.io/
companion_urls:
  - https://github.com/n8n-io/n8n
raw_files:
  - ../../raw/web/n8n.io.md
  - ../../raw/github/n8n-io-n8n.md
tags:
  - workflow-automation
  - visual-builder
  - ai-agents
  - langchain-nodes
  - self-hosted
  - fair-code
  - no-code
  - enterprise
related:
  - zapier.com
  - webhook.site
  - script.it
  - langchain.com
  - retool.com
  - postiz.com
  - clickup.com
  - trigger.dev
product: n8n
detail_level: standard
created: 2026-06-15
updated: 2026-07-03
---

n8n is a fair-code workflow automation platform for technical teams that combines a visual node-based builder with full JavaScript/Python code access and native LangChain-based AI capabilities. With 192,000+ GitHub stars, 500+ integrations, and self-hosting on Docker or NPX alongside an n8n Cloud offering, it occupies the technical-team segment of the automation space that competitors like Zapier address with pure no-code approaches. The platform gives developers the control and flexibility of code without sacrificing the speed of visual configuration.

_All claims below are sourced from ../../raw/web/n8n.io.md unless otherwise noted._

## What it does

n8n lets users build workflows — called automations — as connected node graphs. Each node represents an action (call an API, filter data, send an email, write to a database, run JavaScript) or a trigger (webhook, schedule, app event). Visual connections define execution order; branches implement conditional logic, merging, and looping. Workflows can be run manually, on a schedule, or triggered by external events. The editor provides real-time input/output visibility on every node and supports re-running individual steps without replaying the whole workflow.

AI workflows extend the standard node palette with LangChain-based cluster nodes: AI Agent, Chat Model, Embeddings, Vector Store, and Retrieval Chain nodes. These give users a no-code path to RAG pipelines, multi-model agent loops, and human-in-the-loop interrupts — powered by connectors to OpenAI, Anthropic, Google Gemini, Ollama, and others.

## Key features

- **500+ integrations**: Built-in action nodes for Salesforce, Slack, Gmail, HubSpot, Airtable, MongoDB, PostgreSQL, MySQL, and hundreds more.
- **Code nodes**: JavaScript and Python code blocks with npm package support in the same workflow graph.
- **AI/LangChain nodes**: First-class AI Agent, Chat Model, Embeddings, Vector Store, and Retrieval Chain nodes for RAG and agentic workflows. (../../raw/github/n8n-io-n8n.md)
- **Re-run single steps**: Debug any node in isolation without replaying earlier steps.
- **Native AI evaluation tools**: Built-in tooling for evaluating AI workflow quality.
- **Git-based version control**: Workflow history tracked through source control.
- **Multi-user collaboration**: Team access with role-based controls.
- **Execution modes**: Manual, partial, scheduled, webhook-triggered, and production executions.

## Architecture

n8n is a pnpm monorepo with Turbo build orchestration, organized into focused packages. (../../raw/github/n8n-io-n8n.md)

Key packages:
- `packages/workflow` — Core workflow interfaces and types
- `packages/core` — Workflow execution engine
- `packages/cli` — Express server, REST API, and CLI commands
- `packages/editor-ui` — Vue 3 frontend (Pinia state management, Vite build)
- `packages/nodes-base` — All built-in integration nodes
- `packages/@n8n/nodes-langchain` — AI/LangChain cluster nodes
- `packages/@n8n/instance-ai` — AI Assistant backend embedded in the UI
- `@n8n/design-system` — Shared Vue component library
- `@n8n/config` — Centralized configuration management

Architectural patterns: dependency injection via `@n8n/di`, Controller-Service-Repository backend, event-driven internal bus, context-based execution model, TypeORM for SQLite/PostgreSQL support. (../../raw/github/n8n-io-n8n.md)

## Installation

**NPX (quickest):**
```
npx n8n
```

**Docker:**
```
docker volume create n8n_data
docker run -it --rm --name n8n -p 5678:5678 -v n8n_data:/home/node/.n8n docker.n8n.io/n8nio/n8n
```

Access the editor at http://localhost:5678. Cloud option: app.n8n.cloud. (../../raw/github/n8n-io-n8n.md)

**Enterprise self-hosted** via Docker with air-gapped deployment support.

## Example usage

Build a basic workflow: add a Schedule Trigger node → HTTP Request node → Slack node to send a daily digest. Add a Code node between steps to transform JSON.

For an AI workflow: Webhook Trigger → AI Agent node (with Chat Model + Vector Store sub-nodes) → HTTP Request node to store results. The AI Agent runs a LangChain loop against the configured model until a stopping condition is met. (../../raw/github/n8n-io-n8n.md)

Workflow templates (900+) are available at n8n.io/workflows covering IT ops (employee onboarding, ticket enrichment), security ops (incident response, threat intelligence), CRM automation, and RAG pipeline patterns.

## When to use

n8n fits teams that need no-code speed for straightforward automations but want code access for data transformation, custom logic, or advanced integrations. The fair-code license allows self-hosting without per-seat charges on the core feature set, making it attractive for organizations with data residency requirements. Its LangChain AI nodes make it a natural choice for teams building agentic pipelines who prefer a visual orchestration layer over writing raw SDK code.

Compare with [[zapier.com]] for pure no-code breadth (9,000+ apps vs. 500+, plus MCP server and TypeScript SDK) and [[langchain.com]] for a code-first approach to the same LangChain-based AI orchestration primitives n8n exposes as visual nodes.

## Ecosystem

- **n8n Cloud**: Fully managed SaaS version at app.n8n.cloud
- **Community**: 200,000+ members at community.n8n.io; 900+ workflow templates
- **Extensions**: Custom node development via dedicated `node-dev` CLI tool
- **MCP**: n8n connects to external MCP tools and can receive MCP-style tool calls from agents via its webhook/HTTP nodes
- **Integrations**: 500+ pre-built nodes; custom HTTP Request node covers anything not pre-built
- **Enterprise tier**: SOC 2, GDPR, SSO/SAML, SIEM integration, RBAC, air-gapped deployment

The GitHub repo (`n8n-io/n8n`) ships a `.claude/plugins/n8n/` directory with `n8n:` namespaced Claude Code skills and agents for contributors working on the platform itself. (../../raw/github/n8n-io-n8n.md)
