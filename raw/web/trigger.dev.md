# trigger.dev

## Fetch log
- Inbox URL: https://trigger.dev/
- Final URL: https://trigger.dev/
- Fetched: 2026-07-03
- Pages: 8
- Mode: standard

## llms.txt — https://trigger.dev/llms.txt
# Trigger.dev

> Build AI agents and workflows in TypeScript. Open source platform for durable, long-running tasks. Write normal async/await code, deploy with one command, run for hours or days without timeouts. Apache 2.0 licensed. Self-host or use Trigger.dev Cloud.

Last updated: 2026-06-12

Trigger.dev is the TypeScript platform for building AI agents and workflows. Tasks are plain async functions with no workflow DSL and no determinism rules, so adopting it means moving your code, not rewriting it. Checkpoint-resume snapshots (via CRIU) capture full process state during waits: paused agents release compute, use no resources and aren't billed while waiting, and resume exactly where they left off. Tool calling, human-in-the-loop, realtime LLM token streaming, automatic retries, queues, and OpenTelemetry observability are built in. No workers to provision, no servers to manage.

What makes Trigger.dev different:

- **Normal TypeScript, no DSL**: Plain async/await code with no determinism constraints and no replay semantics (compared to Temporal, Restate, and DBOS, which require deterministic workflow code). You keep writing the TypeScript you already write, with any npm package.
- **Checkpoint-resume durable execution**: CRIU-based snapshots capture memory, CPU registers, and file descriptors. On retry, successful prior work is not re-run; tasks resume from where they stopped.
- **No timeout**: Tasks run for hours, days, or weeks. Long jobs ship as one function instead of being split into chunks to fit a serverless window. Paused time uses no resources and isn't billed.
- **Elastic scaling without workers**: Concurrency scales from 0 to your plan limit automatically. Adding capacity is a billing change, not an infra change.
- **Open source**: Apache 2.0. The full stack (dashboard, orchestrator, workers) self-hosts via Docker Compose or Kubernetes. Same codebase on Cloud and self-hosted, so there is no lock-in.
- **Realtime to frontend AND backend**: Stream run state and LLM tokens to React hooks or backend subscribers. Build streaming AI UIs without polling or running your own realtime infrastructure.

Primary use cases: AI agents, multi-step LLM workflows, and RAG pipelines; long-running background jobs that exceed serverless limits; video, audio, image, and document processing; scheduled tasks and managed cron; multi-tenant SaaS background jobs with per-customer concurrency.

## Documentation

- [Getting Started](https://trigger.dev/docs): Install, write your first task, deploy in ~5 minutes
- [How It Works](https://trigger.dev/docs/how-it-works): Architecture, checkpoint-resume, durable execution
- [AI Agents Guide](https://trigger.dev/docs/guides/ai-agents): Patterns for autonomous agents, orchestration, evaluator-optimizer
- [Realtime](https://trigger.dev/docs/realtime/overview): Run subscriptions, streams, React hooks
- [Waitpoints](https://trigger.dev/docs/wait-for-token): Pause for approvals, webhooks, and external events at zero compute cost
- [Build Extensions](https://trigger.dev/docs/config/extensions/overview): Prisma, FFmpeg, Playwright, Python, Puppeteer, custom Docker layers with one config line
- [Self-Hosting](https://trigger.dev/docs/self-hosting/overview): Docker Compose or Kubernetes
- [Management API](https://trigger.dev/docs/management/overview): REST API for triggering and managing runs
- [MCP Server](https://trigger.dev/docs/mcp-introduction): Connect AI editors (Claude Code, Cursor, Windsurf, etc.) to Trigger.dev
- [Examples](https://trigger.dev/docs/examples/overview): Production-ready task examples

## Product

- [AI Agents](https://trigger.dev/product/ai-agents): Drop-in infrastructure for AI agents with tool calling, human-in-the-loop, and structured I/O
- [Realtime](https://trigger.dev/product/realtime): Stream run status, metadata, and LLM tokens to frontend (React hooks) and backend
- [Observability and Monitoring](https://trigger.dev/product/observability-and-monitoring): OpenTelemetry traces, TRQL (ClickHouse-backed query language), custom dashboards, alerting
- [Concurrency and Queues](https://trigger.dev/product/concurrency-and-queues): Per-queue and per-tenant concurrency limits, named queues, runtime overrides
- [Scheduled Tasks](https://trigger.dev/product/scheduled-tasks): Managed cron, per-environment, multi-tenant dynamic schedules
- [Security and Compliance](https://trigger.dev/security): SOC 2 Type II, GDPR, HIPAA Business Associate Agreement (Enterprise)

## Resources

- [GitHub](https://github.com/triggerdotdev/trigger.dev): Apache 2.0 source code, 15,000+ stars
- [Pricing](https://trigger.dev/pricing): Free plan with $5 usage credit, Hobby $10/month, Pro $50/month. Usage billed as compute-seconds + a per-run fee; paused time isn't billed
- [Blog](https://trigger.dev/blog): Engineering deep-dives and tutorials
- [Changelog](https://trigger.dev/changelog): Latest releases and features
- [Discord](https://trigger.dev/discord): Community support
- [Customers](https://trigger.dev/customers): Case studies from Magic Patterns, Midday, MagicSchool AI, GovSignals, and more

## Comparisons

- [vs Temporal](https://trigger.dev/vs/temporal): No DSL, no determinism rules, TypeScript-native
- [vs BullMQ](https://trigger.dev/vs/bullmq): Managed infrastructure, durable execution, no Redis to operate
- [vs n8n](https://trigger.dev/vs/n8n): Code-first instead of visual workflow builder

## Optional

- [llms-full.txt](https://trigger.dev/llms-full.txt): Extended technical documentation

## Landing page — https://trigger.dev/

Trigger.dev | Build and deploy fully-managed AI agents and workflows.

v4.5.0 GA: AI Agents are GA

# Build and deploy fully‑managed AI agents and workflows

Trigger.dev is the platform for building AI workflows in TypeScript. Long-running tasks with retries, queues, observability, and elastic scaling.

15.5k | Open source

Product areas: AI agents, Media processing, Media generation, Human in the loop, Streaming, Run Python, Marketing, Browser automation, Scheduled tasks, Concurrency, Retries, Semantic search, Email sequences.

Example durable AI chat agent with tools (searchDocs, refundOrder with needsApproval for HITL), streamText with anthropic claude-sonnet-4-5, stepCountIs(15).

## How it works (marketing)
- No timeouts — simple reliable code, never hit a timeout
- Pay for what you use — only pay when code is executing
- No servers to manage — deploy and scale handled by platform

## AI agent patterns
- Autonomous agent, Prompt chaining, Routing, Parallelization, Orchestrator, Evaluator-optimizer

## Realtime
- Trigger.dev Realtime: display run status in app UI
- Realtime streams: stream LLM responses from runs to users via Realtime API

## Runtime freedom
Build extensions: Python, Prisma, Puppeteer, esbuild, FFmpeg, apt-get, additionalPackages, audioWaveform, custom build extensions.

## Features (development)
Write tasks in regular code, Durable cron schedules, Realtime updates & streaming, React hooks, MCP Server, Python support, Max duration, Batch triggering, Structured inputs/outputs, Waits, Wait for HTTP callback, Preview branches, Input Streams.

## Features (production)
Multi-region workers, Static IPs, AWS PrivateLink, Concurrency & queues, Human-in-the-loop, Multiple environments, Elastic infrastructure, Automatic retries, Build extensions, Checkpointing, Machines, Vercel integration, GitHub integration.

## Features (observability)
Observability & monitoring, Logging & tracing, Tags, Advanced run filters, Run metadata, Bulk actions, Real-time alerts, Query, Dashboards.

## Open source
Apache 2.0 licensed. 15.5k+ stars. Self-hostable.

## Docs — https://trigger.dev/docs

Welcome to the Trigger.dev docs.

What is Trigger.dev? Open source background jobs framework for reliable workflows in plain async code. Run long-running AI tasks, complex background jobs, AI agents with queuing, automatic retries, real-time monitoring. No timeouts, elastic scaling, zero infrastructure management.

Provides CLI and SDK, regular and scheduled tasks, dashboard observability, Realtime API with React hooks. Cloud or self-host.

Concepts: Writing tasks, Triggering tasks, Runs, API keys.

Features: Scheduled tasks (cron), Realtime API, React hooks, Waits, Errors and retries, Concurrency & Queues, Wait for token (human-in-the-loop), Build extensions.

Build extensions table: prismaExtension, pythonExtension, playwright, puppeteer, lightpanda, ffmpeg, aptGet, additionalFiles, additionalPackages, syncEnvVars, esbuildPlugin, emitDecoratorMetadata, audioWaveform.

## How it works — https://trigger.dev/docs/how-it-works

Trigger.dev v3 integrates long-running async tasks into your application and runs them in the background.

Architecture: serverless architecture without timeouts. `npx trigger.dev@latest deploy` builds and deploys task code. Trigger from app → task handle returned → task runs in isolated environment.

### Checkpoint-Resume System
1. Task Execution in isolated environment
2. Subtask Handling via triggerAndWait
3. State Checkpointing via CRIU (memory, CPU registers, file descriptors)
4. Resource Release after checkpoint
5. Efficient Storage of compressed checkpoint on disk
6. Event-Driven Resumption
7. State Restoration into new execution environment
8. Seamless Continuation

Paused time and subtask wait time not billed on Trigger.dev Cloud.

### Durable execution
Task breakdown into subtasks with idempotency keys. Result caching. Intelligent retries — only failed subtask and subsequent tasks retried.

### Build system
esbuild-powered. Bundled by default. Build extensions. ESM output. `--dry-run` for Containerfile inspection.

### Dev mode
`npx trigger.dev@latest dev` runs task code locally; scheduling on server. Auto-detects changes. Separate process per task. No offline dev mode.

### Environments
prod and staging via `--env`. Preview branches for isolated per-branch environments.

### OpenTelemetry
Logging and dashboard powered by OTEL traces/logs. Auto-correlate parent/subtask logs. Configurable instrumentations (Prisma, AWS SDK, etc.).

## Realtime overview — https://trigger.dev/docs/realtime/overview

Realtime covers run state updates and streaming continuous data (AI tokens) from tasks to frontend/backend via `@trigger.dev/react-hooks`.

| | Run updates | Streaming |
|---|---|---|
| What | Run state: status, metadata, tags | Continuous data (AI tokens, file chunks, progress) |
| Hook | useRealtimeRun | useRealtimeStream |
| Setup in task | No, automatic | Yes, streams.define() |
| Infrastructure | Electric SQL (PostgreSQL sync) | Streams transport |

Subscribe to runs by ID, tags, batch runs. Streaming via streams.define() in task code.

Authentication required for all Realtime hooks/functions.

## Writing tasks: Overview — https://trigger.dev/docs/writing-tasks-introduction

Tasks are long-running processes triggered by events. Topics: Logging, Errors & retrying, Wait, Concurrency & Queues, Realtime notifications, Versioning, Machines, Idempotency, Replaying, Max duration, Tags, Metadata, Usage, Context, Bulk actions, Priority, Hidden tasks.

## Wait for token — https://trigger.dev/docs/wait-for-token

Waitpoint tokens pause task runs until completed. Used for approval workflows and human-in-the-loop.

- wait.createToken({ timeout }) — create token anywhere in codebase
- wait.forToken(tokenId) — wait inside task run
- wait.completeToken(tokenId, output) — complete from anywhere
- publicAccessToken for browser completion with CORS-enabled endpoint
- token.url webhook callback for server-to-server (no CORS)
- wait.listTokens, wait.retrieveToken for management
- Idempotency keys supported

## MCP Introduction — https://trigger.dev/docs/mcp-introduction

Trigger.dev MCP Server enables AI assistants to interact with Trigger.dev projects.

Tools: search docs, initialize projects, list projects/orgs, get task info, trigger runs, deploy, monitor runs, TRQL queries, dashboard metrics.

Install: `npx trigger.dev@latest install-mcp` (supports Claude Code, Cursor, Windsurf, VS Code, Zed, Cline, Gemini CLI, Codex CLI, etc.)

Authentication: search_docs works without auth; other tools require CLI login.

Options: --project-ref, --dev-only, --readonly, --scope user|project|local.

Skills: portable instruction sets for Trigger.dev patterns.

