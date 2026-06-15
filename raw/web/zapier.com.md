# zapier.com

## Fetch log
- Inbox URL: https://zapier.com/
- Final URL: https://zapier.com/
- Fetched: 2026-06-15
- Pages: 9
- Mode: standard

## llms.txt — https://zapier.com/llms.txt

# Zapier

> Root map for AI agents and developer tools. Per-surface indexes live in [Surfaces](#surfaces); topic-keyed cross-references live in [Topics](#topics). Section anchors are stable — safe to deep-link (e.g. `https://zapier.com/llms.txt#mcp`).

## What is Zapier

Zapier is a no-code AI orchestration platform where teams connect thousands of apps and AI tools to run automations and AI-assisted work, including workflows, Agents, MCP-connected assistants, and chatbots. Teams from SMBs to global enterprises use Zapier to wire together sprawling stacks, add AI where it fits, and apply admin and security controls at scale. Control, delegation, and visibility are built in so teams build safely without IT as a bottleneck.

---

## Surfaces

Zapier spans multiple subdomains. Where a subdomain publishes its own `llms.txt`, the link below points to that index — fetch it for the full page listing of that surface.

- [docs.zapier.com/llms.txt](https://docs.zapier.com/llms.txt): Developer documentation — SDK, MCP, integration building, embedding, White Label, Workflow API.
- [help.zapier.com](https://help.zapier.com): End-user Help Center — troubleshooting, how-tos, account management.
- [community.zapier.com](https://community.zapier.com): User community — forums, discussions, tips.

---

## Topics

### #mcp — Zapier MCP

The Model Context Protocol server for Zapier. Connects MCP-aware clients (Claude, Cursor, VS Code, Windsurf, ChatGPT, etc.) to Zapier's app integration layer so agents can take actions across thousands of apps.

- Product overview: [zapier.com/mcp](https://zapier.com/mcp)
- Documentation home: [docs.zapier.com/mcp/home](https://docs.zapier.com/mcp/home.md)
- Quickstart (5 min): [docs.zapier.com/mcp/quickstart](https://docs.zapier.com/mcp/quickstart.md)
- Supported clients: [docs.zapier.com/mcp/clients](https://docs.zapier.com/mcp/clients.md)
- Usage and billing: [docs.zapier.com/mcp/usage](https://docs.zapier.com/mcp/usage.md)
- Embedding MCP in your product: [docs.zapier.com — Embedding Zapier MCP](https://docs.zapier.com/powered-by-zapier/embedding-zapier-mcp/getting-started.md)
- Connecting your agent to embedded MCP: [docs.zapier.com — Connecting Your Agent](https://docs.zapier.com/powered-by-zapier/embedding-zapier-mcp/guides/connecting-your-agent.md)
- White Label for MCP agents: [docs.zapier.com — AI agent connections](https://docs.zapier.com/white-label/use-cases/ai-agent-connections.md)
- npm package: [`@zapier/zapier-sdk-mcp`](https://www.npmjs.com/package/@zapier/zapier-sdk-mcp)
- Related topics: [#sdk](#sdk), [#embed](#embed), [#auth](#auth), [#integrations](#integrations)

### #sdk — Zapier SDK (TypeScript)

The TypeScript SDK and CLI for building agent tools and integrations against Zapier's connection layer. The primary surface for coding agents that need programmatic access to Zapier actions.

- SDK overview: [docs.zapier.com/sdk](https://docs.zapier.com/sdk/index.md)
- Quickstart (5 min): [docs.zapier.com/sdk/quickstart](https://docs.zapier.com/sdk/quickstart.md)
- API reference (all methods): [docs.zapier.com/sdk/reference](https://docs.zapier.com/sdk/reference.md)
- CLI reference (all commands): [docs.zapier.com/sdk/cli-reference](https://docs.zapier.com/sdk/cli-reference.md)
- Using the CLI: [docs.zapier.com/sdk/using-the-cli](https://docs.zapier.com/sdk/using-the-cli.md)
- Changelog: [docs.zapier.com/sdk/changelog](https://docs.zapier.com/sdk/changelog.md)
- npm packages: [`@zapier/zapier-sdk`](https://www.npmjs.com/package/@zapier/zapier-sdk), [`@zapier/zapier-sdk-cli`](https://www.npmjs.com/package/@zapier/zapier-sdk-cli), [`@zapier/zapier-sdk-core`](https://www.npmjs.com/package/@zapier/zapier-sdk-core)
- Source: [github.com/zapier/sdk](https://github.com/zapier/sdk)
- Related topics: [#mcp](#mcp), [#auth](#auth), [#integrations](#integrations)

### #agents — AI Agents

Zapier's hosted AI agent product. Agents use Zapier's app connections to take actions on behalf of users without writing code.

- Product overview: [zapier.com/agents](https://zapier.com/agents)
- AI hub (all AI capabilities): [zapier.com/ai](https://zapier.com/ai)
- Chatbots: [zapier.com/ai/chatbot](https://zapier.com/ai/chatbot)
- Related topics: [#workflows](#workflows), [#mcp](#mcp), [#integrations](#integrations)

### #workflows — Zaps and workflows

The original Zapier primitive: a trigger in one app fires actions in others. The backbone of Zapier automation.

- Product overview: [zapier.com/workflows](https://zapier.com/workflows)
- Templates (pre-built): [zapier.com/templates](https://zapier.com/templates)
- Forms (workflow inputs): [zapier.com/forms](https://zapier.com/forms)
- Related topics: [#integrations](#integrations), [#tables](#tables), [#agents](#agents)

### #integrations — The app catalog

Every app Zapier connects to. Use this when an agent needs to know whether Zapier supports a given app or what actions are available.

- Full catalog: [zapier.com/apps](https://zapier.com/apps)
- Per-app pages: `zapier.com/apps/{slug}/integrations`
- AI actions reference: [docs.zapier.com — AI Actions](https://docs.zapier.com/integrations/reference/ai-actions.md)
- Related topics: [#mcp](#mcp), [#sdk](#sdk), [#auth](#auth)

### #auth — Authentication and connections

How agents and users authenticate to Zapier and to the third-party apps Zapier proxies. Relevant for both SDK consumers and integration builders.

- User connection management: [zapier.com/app/assets/connections](https://zapier.com/app/assets/connections)
- Authentication concepts (for integration builders): [docs.zapier.com — Authentication](https://docs.zapier.com/integrations/build/auth.md)
- White Label token exchange (for embed partners): [docs.zapier.com — Token exchange](https://docs.zapier.com/white-label/token-exchange.md)
- Related topics: [#sdk](#sdk), [#mcp](#mcp), [#embed](#embed)

### #tables — Zapier Tables

Storage primitive for workflows and agents. Structured data that Zaps, agents, and interfaces can read and write.

- Product overview: [zapier.com/tables](https://zapier.com/tables)
- Related topics: [#workflows](#workflows), [#agents](#agents)

### #embed — Powered by Zapier (embedding)

For developers who want to embed Zapier's automation, MCP, or connections inside their own product. Covers the Workflow API, embedded editors, MCP embedding, and White Label.

- Embed overview: [docs.zapier.com — Powered by Zapier](https://docs.zapier.com/powered-by-zapier/index.md)
- Embedded MCP: [docs.zapier.com — Embedding Zapier MCP](https://docs.zapier.com/powered-by-zapier/embedding-zapier-mcp/getting-started.md)
- Workflow API (Zap creation): [docs.zapier.com — Zap creation](https://docs.zapier.com/powered-by-zapier/zap-creation/getting-started.md)
- Embedded Zap editor: [docs.zapier.com — Embedded editor](https://docs.zapier.com/powered-by-zapier/embedding-zapier/getting-started.md)
- White Label (branded connections): [docs.zapier.com — White Label](https://docs.zapier.com/white-label/getting-started.md)
- Workflow API authentication: [docs.zapier.com — API auth](https://docs.zapier.com/powered-by-zapier/authentication/getting-started.md)
- OpenAPI spec: [api.zapier.com/schema](https://api.zapier.com/schema)
- Related topics: [#mcp](#mcp), [#sdk](#sdk), [#auth](#auth), [#developers](#developers)

### #developers — Developer platform (integration builders)

For developers publishing apps to the Zapier directory. Distinct from [#sdk](#sdk) (which is for consumers building with Zapier's API) and [#embed](#embed) (which is for embedding Zapier in your product).

- Documentation home: [docs.zapier.com/integrations](https://docs.zapier.com/integrations/index.md)
- Build an integration: [docs.zapier.com — Build guide](https://docs.zapier.com/integrations/quickstart/build-integration.md)
- Platform UI tutorial: [docs.zapier.com — UI tutorial](https://docs.zapier.com/integrations/quickstart/ui-tutorial.md)
- Platform CLI tutorial: [docs.zapier.com — CLI tutorial](https://docs.zapier.com/integrations/quickstart/cli-tutorial.md)
- Publishing requirements: [docs.zapier.com — Publishing](https://docs.zapier.com/integrations/publish/integration-publishing-requirements.md)
- Partner Program: [docs.zapier.com — Partner Program](https://docs.zapier.com/integrations/publish/partner-program.md)
- Platform CLI npm: [`zapier-platform-cli`](https://www.npmjs.com/package/zapier-platform-cli), [`zapier-platform-core`](https://www.npmjs.com/package/zapier-platform-core)
- Source: [github.com/zapier/zapier-platform](https://github.com/zapier/zapier-platform)
- Powered by Zapier (embedding your integration): [docs.zapier.com — Powered by Zapier](https://docs.zapier.com/integrations/embed/powered-by-zapier.md)
- Related topics: [#auth](#auth), [#integrations](#integrations), [#embed](#embed)

---

## Start here

- [Zapier home](https://zapier.com/): Product entry and positioning.
- [Apps directory](https://zapier.com/apps): Canonical list of connectable apps.
- [Pricing](https://zapier.com/pricing): Plans and packaging.
- [Sign up](https://zapier.com/sign-up): Create a free Zapier account.
- [Contact Sales](https://zapier.com/l/contact-sales): Team and enterprise sales inquiries.
- [Enterprise](https://zapier.com/enterprise): Enterprise positioning, workspaces, organizational use.
- [Use cases](https://zapier.com/use-cases): Solution-oriented overviews by scenario.
- [Customer stories](https://zapier.com/customer-stories): Case studies and proof points.
- [Guides](https://zapier.com/resources/guides): Long-form educational content.

## Security, legal, and compliance

- [Security & compliance](https://zapier.com/security-compliance): Data security, privacy, certifications, compliance.
- [Legal](https://zapier.com/legal): Terms, policies, related documents.
- [Privacy policy](https://zapier.com/privacy): Data practices.

## Support

- [Contact Support](https://zapier.com/app/get-help): Official support routing.

---

## Notes for automated fetchers

- This file is the canonical agent-readable map for Zapier. For expanded inline content on every topic, fetch [/llms-full.txt](https://zapier.com/llms-full.txt). The developer docs index at [docs.zapier.com/llms.txt](https://docs.zapier.com/llms.txt) has full page listings organized by section.
- **Section anchors are stable.** `#mcp`, `#sdk`, `#agents`, `#workflows`, `#integrations`, `#auth`, `#tables`, `#embed`, `#developers` will not be renamed without coordinated updates across all linking files.
- Do not treat this file as a complete product or pricing spec. Confirm GA status, limits, and plan entitlements on zapier.com, Help, and Developer Docs.
- Site sitemaps: [zapier.com/robots.txt](https://zapier.com/robots.txt).

## Landing page — https://zapier.com/

Zapier: Build and Govern AI Workflows, Agents, and Apps

Zapier positions itself as a control plane for AI automation that operates across 9,000+ applications. The platform serves 3 million+ businesses with capabilities spanning workflow creation, agent deployment, and governance infrastructure.

**Integration & Automation**
The platform enables connection of "any AI to 9,000+ apps" through MCP support for assistants like Claude and ChatGPT, plus Zapier SDK for custom applications.

**Team Delegation**
Workspaces allow organizations to create dedicated team environments with role-based access controls and inherited guardrails. The system includes guided templates and SCIM provisioning for automated user management.

**Security & Compliance**
Features include:
- Action-level restrictions and endpoint-level controls
- Domain restrictions preventing personal account connections
- VPC Peering for secure internal data access
- SOC 2 Type II, SOC 3, GDPR, and CCPA compliance
- Immutable audit records and real-time log streaming

**Visibility**
The platform provides "Every AI action logged. Every model call is tracked" with programmatic API access to audit data, built-in safety checks for sensitive data detection, and automatic workflow documentation.

Zapier emphasizes offering governance that works across multiple AI models regardless of which provider creates them, positioning itself between AI providers and enterprise applications.

## Docs — https://docs.zapier.com/

Zapier Developer Documentation

Four main product categories for developers:

**Integrations**: Build a Zapier integration — design triggers and actions for your product, wire up authentication, then publish to the App Directory.

**Powered by Zapier**: Bring Zapier's automation into your own product so customers can build workflows and run actions without leaving your app.

**Zapier MCP**: Connect AI assistants to Zapier through MCP so they can call any app action on the platform using natural language.

**Zapier SDK**: Use the Zapier SDK to run actions and manage connections from your backend or agents, all in a few lines of code.

Complete documentation index: https://docs.zapier.com/llms.txt

## Agents — https://zapier.com/agents

Zapier Agents is a platform for creating AI-powered teammates that automate work across 9,000+ apps. Trusted by over 2.2 million companies worldwide.

Core capabilities:
- **Build your agent** — Create specialized agents with help from Zapier Copilot to connect business data and perform tasks
- **Monitor activity** — Track agent performance and actions
- **Chat when needed** — Interact with agents as required
- **Work on the web** — Agents operate across integrated applications

Knowledge Integration: enhance chatbot accuracy by adding FAQs, docs, and public links.

Pre-built templates:
- Sales & Leads: Lead Enrichment Agent, Enterprise Lead Qualification Agent, Sales Email Writer
- Customer Support: Support Email Agent, Zendesk Ticket Agent, IT Helpdesk Slack Responder
- Content & Marketing: Viral Content Creator Agent, SEO Blog Writer
- Operations: Candidate Ranking System, Expense Classifier, Github PR Slack Notifier, Slack Thread Insights Extractor

Free signup at agents.zapier.com/login.

## MCP — https://zapier.com/mcp

Zapier MCP: "Your AI can talk. Zapier MCP makes it act."

Connects AI tools like Claude, ChatGPT, and Cursor to over 9,000 applications including Gmail, Slack, and Salesforce without technical setup — no terminal access or configuration files needed.

Current usage: 195,000+ MCP servers powered, 4.6 million tool calls completed, 250,000+ apps connected.

Setup:
1. Connect Zapier MCP to your chosen AI client
2. Existing app connections are automatically imported
3. Request actions using plain language

Use cases:
- Executive assistants scheduling meetings automatically
- Team leads summarizing Slack channels daily
- Sales representatives preparing meeting documents

Pricing: Included in existing Zapier plans using the same task quota as standard Zaps. SOC 2 Type II compliant.

Difference from Zapier Agents: MCP suits developers and Claude users requiring direct LLM integration; Agents serves non-technical users needing complex background-executing workflows.

## Workflows — https://zapier.com/workflows

Connect AI to over 9,000 tools, without waiting on a developer. 3.4 million+ users automate workflows within minutes.

Primary applications:
- Answer tickets — Customer support automation
- Enrich leads — Sales pipeline enhancement
- Sell smarter — Sales enablement

Template categories: customer service, lead management, content creation, operations.

Customer results:
- "$1M in pipeline" recovered through automation
- Remote.com's three-person IT team resolved "28% of company requests automatically with AI"
- Organizations reported 3x growth "with zero new headcount" and "2,219 days saved each month"

## AI Hub — https://zapier.com/ai

Zapier as a governance layer above individual AI models.

"Zapier is that layer: credential management, action-level controls, and workflow logic that run regardless of which AI surface your team is in."

Four main capabilities:
- Connect any AI (Claude, ChatGPT, Cursor) with access to 30,000+ actions across 9,000+ apps
- Build agents that perform operational tasks like lead qualification and ticket routing
- Implement safety checks for sensitive data before processing
- Switch between models without rebuilding workflows

Portability framework:
1. **App portability** — tool connections function across multiple AI surfaces
2. **Context portability** — workflows remain in Zapier rather than within individual models
3. **Governance portability** — access controls and audit trails apply universally

Customer examples: JBGoodwin Realtors (25% workload reduction), Portland Trail Blazers (94% time savings), Author.inc (20x productivity increase).

## MCP Docs — https://docs.zapier.com/mcp/home

Zapier MCP enables AI assistants to connect with thousands of applications through the Model Context Protocol.

Two pathways:
- **For Non-Developers**: Connect Anthropic's Claude to Zapier's 9,000+ app integrations without writing code.
- **For Developers**: Direct access to Zapier's ecosystem through APIs and developer tools like Cursor and Windsurf.

Core capabilities: 9,000+ App Connections and 30,000+ Actions. Zapier manages authentication, encryption, and rate limiting.

Popular integrations: Slack, Google Sheets, Gmail, Jira, Asana, GitHub, HubSpot, Discord.

## SDK Docs — https://docs.zapier.com/sdk/index

The Zapier SDK provides programmatic access to 9,000+ app integrations.

"The SDK gives coding agents and builders programmatic access to Zapier's full app ecosystem. Any API call, on behalf of a user, with no OAuth setup required."

Core features:
- 9,000+ pre-built integrations across Slack, Google Sheets, Salesforce, GitHub
- Type-safe TypeScript support with generated types for every app and action
- Authentication handled automatically — no manual OAuth flows needed
- Built-in action syntax like `apps.slack.write.channel_message()`
- Custom API requests via `.fetch()` for calls beyond pre-built actions
- Token refresh and retries managed automatically

SDK vs MCP:

| Aspect | MCP | SDK |
|--------|-----|-----|
| Best for | Chat agents | Coding agents |
| Interface | Curated pre-built actions | Any API call in code |
| Use when | You want governed tools | You need loops and complex logic |

Current status: Open Beta — free during early phase. Full action catalog, raw API calls to ~3,600 app APIs, app governance.

Setup: Node.js 20+, install `@zapier/zapier-sdk`, authenticate via CLI, list connected apps.
