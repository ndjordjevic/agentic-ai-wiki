# www.taskmaster.one

## Fetch log
- Inbox URL: https://www.taskmaster.one/
- Final URL: https://www.taskmaster.one/
- Fetched: 2026-05-25
- Pages: 6
- Mode: standard

## Landing page — https://www.taskmaster.one/

### Title & Hero

**TaskMaster AI — The PM for your AI Agent**

"The PM for your AI coding agents. TaskMaster AI turns PRDs into structured, dependency-aware tasks—so your CLI, MCP, and dashboard stay in sync from plan to merge. Built for Cursor, Windsurf, VS Code, and every workflow that ships with AI."

### AI Providers Supported

ChatGPT (OpenAI), Gemini (Google), Mistral, Azure, OpenRouter, Ollama, Zhipu AI, Meta, Anthropic (Claude), Perplexity, xAI (Grok), DeepSeek

### How it works — From PRD to tasks your agents can run

Parse requirements, break work into steps, and track dependencies in one place—then drive it from the terminal, your editor, or the web app. No more lost context between your spec and your AI tools.

**Plan & parse** — Ingest PRDs and generate a clear task hierarchy with IDs, statuses, and dependencies your whole team can follow.

**CLI & MCP** — Run `taskmaster` in the terminal and wire Cursor, Windsurf, and other MCP hosts — same tasks everywhere.

**Dashboard sync** — Watch usage, license status, and task activity in the web dashboard — aligned with what your agents do locally.

### Platform features — Everything your agents need to stay on track

- **Task hierarchy** — Nested tasks and subtasks with stable IDs so agents, humans, and your PRD all reference the same work.
- **Dashboard & sync** — See tasks and usage in the browser while the CLI keeps your repo as the source of truth.
- **Next task & deps** — Dependency-aware "what's next" so agents stop guessing which task to implement first.
- **PRD parsing & planning** — Go from product doc to structured tasks in one pass—ready for breakdown and implementation.
- **Models per role** — Point main, research, and fallback models at the providers you trust—OpenAI, Anthropic, Gemini, and more.
- **Usage & activity** — Transparent usage and recent operations so you know what your agents consumed this month.
- **Complexity scoring** — Complexity scoring, task expansion, research mode.
- **Hosted or BYOK** — Hosted or bring-your-own API keys.

### Featured capabilities (from JSON-LD structured data)
- AI-Powered Task Generation from PRDs
- Intelligent Task Breakdown
- Complexity Analysis
- Task Dependency Management
- Multi-Model AI Support (Claude, GPT, Gemini, DeepSeek)
- CLI and MCP Integration
- Real-time Usage Dashboard
- API Key Management
- npm package: `@taskmasterai/cli`

### Provider/Organization
- Company: TaskMaster AI LLC
- Support email: taskmasteroneai@gmail.com
- Software version: 1.0.1

## Docs — https://www.taskmaster.one/docs

Welcome to v1 of the TaskMaster AI Docs. Expect weekly updates as we expand and refine each section.

Documentation is organized into three sections:
- **Getting Started** — Quick Start (subscription required), Requirements, Installation, Configuration, PRD Creation and Parsing, Tasks Setup, Executing Tasks, API Keys, License & Usage, FAQ, Feedback & Support
- **Best Practices** — Advanced Usage, Advanced Configuration, Advanced Tasks
- **Technical Capabilities** — MCP Tools, CLI Commands, Task Structure, TDD Workflow (Autopilot)

## Getting Started — https://www.taskmaster.one/docs/getting-started/quick-start

This guide is for new subscribers. Requires: Node.js, active subscription, and an AI model API Key.

Steps:
1. Requirements — Node.js, active subscription, API Key
2. Installation — Install and login to TaskMaster AI
3. Configuration — Set up API Key, MCP, and subscription
4. PRD — Write and parse your first PRD
5. Task Setup — Prepare tasks for execution
6. Executing Tasks — Use TaskMaster AI to execute tasks
7. Rules & Context — Build context in your project over time

**Note:** Each task processed counts toward your monthly plan limit.

## Installation — https://www.taskmaster.one/docs/getting-started/installation

**Subscription Required:** Must have an active TaskMaster AI subscription before installing.

**Quick Install for Cursor 1.0+ (One-Click)** — via Cursor deeplink installing `@taskmasterai/cli`.

The MCP server command: `npx @taskmasterai/cli taskmaster-mcp`

npm package: `@taskmasterai/cli`

## Configuration — https://www.taskmaster.one/docs/getting-started/configuration

### Environment Variables (.env file)
```
ANTHROPIC_API_KEY=your_anthropic_key_here
PERPLEXITY_API_KEY=your_perplexity_key_here
OPENAI_API_KEY=your_openai_key_here
```

### Configure Models
```bash
taskmaster models --setup   # interactive setup
taskmaster models --set-main claude-sonnet-4-20250514
taskmaster models --set-research sonar-pro
taskmaster models --set-fallback gpt-4o-mini
```

## Pricing — https://www.taskmaster.one/pricing

### Plans
- **Plus** — $29/month: Up to 100 tasks/month, $0.20/extra task, BYOK (bring your own API keys), Secure API key vault, All AI providers, Task expansion & analysis, Research mode, Email support
- **Pro** — $199/month: Everything in Plus + Hosted API keys included, Up to 1,000 tasks/month, $0.15/extra task, No API key management, Priority support, Advanced analytics, Usage insights
- **Enterprise** — $599+/month: Everything in Pro + 5,000+ tasks/month, Volume discounts, Dedicated support, Custom integrations, Team management, SLA guarantees

### FAQ
- A "task" is counted each time TaskMaster AI processes a request (parsing PRDs, expanding tasks, analyzing complexity, generating updates). Subtasks count separately.
- Pro and Enterprise include hosted API keys. Plus plan users bring their own keys.
- Supported AI providers: Anthropic (Claude), OpenAI (GPT-4), Google (Gemini), Perplexity, xAI (Grok), Mistral, OpenRouter, and Ollama (local models).
