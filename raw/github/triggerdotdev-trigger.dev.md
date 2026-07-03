# triggerdotdev/trigger.dev

## Metadata
- Stars: 15545
- Primary language: TypeScript
- Default branch: main
- Latest release: v4.5.0 (2026-07-02)
- License: Apache License 2.0
- Homepage: https://trigger.dev/changelog
- Fetched: 2026-07-03
- Final URL: https://github.com/triggerdotdev/trigger.dev

## Description
Trigger.dev – build and deploy fully‑managed AI agents and workflows

## README

Trigger.dev is the open-source platform for building AI workflows in TypeScript. Long-running tasks with retries, queues, observability, and elastic scaling.

### The platform designed for building AI agents

Build AI agents using all the frameworks, services and LLMs you're used to, deploy them to Trigger.dev and get durable, long-running tasks with retries, queues, observability, and elastic scaling out of the box.

- **Long-running without timeouts**: Execute your tasks with absolutely no timeouts, unlike AWS Lambda, Vercel, and other serverless platforms.
- **Durability, retries & queues**: Build rock solid agents and AI applications using our durable tasks, retries, queues and idempotency.
- **True runtime freedom**: Customize your deployed tasks with system packages – run browsers, Python scripts, FFmpeg and more.
- **Human-in-the-loop**: Programmatically pause your tasks until a human can approve, reject or give feedback.
- **Realtime apps & streaming**: Move your background jobs to the foreground by subscribing to runs or streaming AI responses to your app.
- **Observability & monitoring**: Each run has full tracing and logs. Configure error alerts to catch bugs fast.

### Key features

- JavaScript and TypeScript SDK — Build background tasks using familiar programming models
- Long-running tasks — Handle resource-heavy tasks without timeouts
- Durable cron schedules — Create and attach recurring schedules of up to a year
- Trigger.dev Realtime — Trigger, subscribe to, and get real-time updates for runs, with LLM streaming support
- Build extensions — Hook directly into the build system and customize the build process. Run Python scripts, FFmpeg, browsers, and more.
- React hooks — Interact with the Trigger.dev API on your frontend using our React hooks package
- Batch triggering — Use batchTrigger() to initiate multiple runs of a task with custom payloads and options
- Structured inputs / outputs — Define precise data schemas for your tasks with runtime payload validation
- Waits — Add waits to your tasks to pause execution for a specified duration
- Preview branches — Create isolated environments for testing and development. Integrates with Vercel and git workflows
- Waitpoints — Add human-in-the-loop judgment at critical decision points without disrupting workflow
- Concurrency & queues — Set concurrency rules to manage how multiple tasks execute
- Multiple environments — Support for DEV, PREVIEW, STAGING, and PROD environments
- No infrastructure to manage — Auto-scaling infrastructure that eliminates timeouts and server management
- Automatic retries — If your task encounters an uncaught error, we automatically attempt to run it again
- Checkpointing — Tasks are inherently durable, thanks to our checkpointing feature
- Versioning — Atomic versioning allows you to deploy new versions without affecting running tasks
- Machines — Configure the number of vCPUs and GBs of RAM you want the task to use
- Observability & monitoring — Monitor every aspect of your tasks' performance with comprehensive logging and visualization tools
- Logging & tracing — Comprehensive logging and tracing for all your tasks
- Tags — Attach up to ten tags to each run, allowing you to filter via the dashboard, realtime, and the SDK
- Run metadata — Attach metadata to runs which updates as the run progresses and is available to use in your frontend for live updates
- Bulk actions — Perform actions on multiple runs simultaneously, including replaying and cancelling
- Real-time alerts — Choose your preferred notification method for run failures and deployments

### Write tasks in your codebase

```ts
import { task } from "@trigger.dev/sdk";

export const helloWorld = task({
  id: "hello-world",
  run: async (payload: { message: string }) => {
    console.log(payload.message);
  },
});
```

### Deployment

Use our SDK to write tasks in your codebase. There's no infrastructure to manage, your tasks automatically scale and connect to our cloud. Or you can always self-host.

### Environments

We support `Development`, `Staging`, `Preview`, and `Production` environments, allowing you to test your tasks before deploying them to production.

### Self-hosting

- Docker self-hosting guide — use Docker Compose to spin up a Trigger.dev instance
- Kubernetes self-hosting guide — use our official Helm chart to deploy Trigger.dev to your Kubernetes cluster

## Top-level structure

| Path | Type | Notes |
|---|---|---|
| `apps/` | dir | Application packages (dashboard, webapp, etc.) |
| `packages/` | dir | Core SDK, CLI, and shared libraries (`@trigger.dev/sdk`) |
| `internal-packages/` | dir | Internal shared packages |
| `docs/` | dir | Documentation source |
| `hosting/` | dir | Self-hosting configs (Docker, Kubernetes) |
| `docker/` | dir | Docker build assets |
| `ai/` | dir | AI-related packages/examples |
| `AGENTS.md` | file | Agent instructions for contributors |
| `CLAUDE.md` | file | Claude-specific contributor guidance |
| `CONTRIBUTING.md` | file | Local development setup guide |
| `package.json` | file | Monorepo root (pnpm workspace) |
