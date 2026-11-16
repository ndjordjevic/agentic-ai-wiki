---
type: source
category: "Coding agents, IDEs & dev environments"
source_url: https://blog.n8n.io/meet-nod/
companion_urls:
  - https://github.com/n8n-io/nod
raw_files:
  - ../../raw/web/blog.n8n.io.md
  - ../../raw/github/n8n-io-nod.md
tags:
  - personal-agent
  - computer-use
  - local-first
  - trust-check
  - vault-secrets
  - n8n-labs
  - apache-2
  - research-preview
related:
  - n8n.io
  - composio.dev
  - composio-community-open-dot
  - hermes-agent.nousresearch.com
  - browser-use.com
  - pi.dev
  - vercel-labs-agent-browser
product: nod
detail_level: standard
created: 2026-11-16
updated: 2026-11-16
studied: true

---

Nod is an open-source personal agent from n8n Labs (research preview, Apache 2.0) that runs on your machine with its own sandboxed Linux workspace and browser. You talk to it in one conversation (desktop app, web, Telegram, or WhatsApp); it works in connected apps and on arbitrary websites until the job is done, asks before risky actions, and uses the AI provider you choose — separate from [[n8n.io]] and not requiring an n8n account.

_All claims below are sourced from ../../raw/web/blog.n8n.io.md unless otherwise noted._

## What it does

Nod is positioned as the "single player" counterpart to n8n's shared, multiplayer workflows: one person installs it, connects their own accounts, and hands it ongoing personal or solo-operator jobs (cancel a subscription and collect the refund, watch a price, book a hotel after approval, pull invoices from supplier portals, scrape dashboard numbers into a weekly report). It can run several jobs in parallel, offer work it notices in connected apps, and schedule recurring tasks (morning brief, price watch). Long-term memory scored 93.2% on LongMemEval; style learning from sent Gmail is available; task procedures are written down and repaired when sites change.

## Key features

- **Own computer + browser** — private local VM/sandbox with files, commands, and a dedicated browser so chat tools that return to-do lists can instead finish the errand.
- **Connected apps** — Gmail, Calendar, Drive, Slack, Notion, Linear and others via Composio by default; optional link to a user's n8n instance.
- **Trust + Vault** — server-side checks before send/pay/post/delete; passwords and cards entered through private forms the model never sees; Usage logs every sign-in, card use, and app action with costs.
- **BYO model** — OpenAI/ChatGPT Plus·Pro, Anthropic, Gemini, OpenRouter, Bedrock, Vertex, Azure, 20+ other providers, or local OpenAI-compatible servers (Ollama, LM Studio, vLLM, llama.cpp).
- **Channels** — same conversation across desktop, browser, Telegram, WhatsApp.
- **Cost guardrails** — per-task receipts, monthly spending limits, check-in after a configurable spend threshold (default $5), estimated monthly cost per schedule.
- **Open source** — Apache 2.0; latest companion release `nod-v0.8.0` (~1.8k★). (../../raw/github/n8n-io-nod.md)

## Architecture

One Node process serves the React client and runs Fastify API, agent runtime, thread-drain worker, and schedulers; Docker containers run PostgreSQL, the workspace, and the browser. Messages and schedule fires become turns in PostgreSQL with a `thread-drain` job; the worker opens a Pi agent session whose tools act in workspace, browser, and apps. Policy (trust, Vault, payments, spending limits) lives in the server, not only in the model prompt. (../../raw/github/n8n-io-nod.md)

Import boundaries are enforced (`ports` / `providers` / `runtime` / `server` / `shared` / `web`); vendor SDKs (Pi, Docker, agent-browser, Composio) stay under `providers`. Stack: TypeScript on Node.js 24, Fastify, React, PostgreSQL + pg-boss, Electron desktop. (../../raw/github/n8n-io-nod.md)

## Installation

Desktop (fastest path — no Node/Docker required): Mac (macOS 14+, Apple silicon or Intel DMG), Windows 11 x64 preview (WSL 2 + virtualization for local assistant), Linux x64 Flatpak preview. One-line Mac install via `deployment/n8n/install.sh`; Windows via `install.ps1`. (../../raw/github/n8n-io-nod.md)

From source (macOS/Linux): Node.js 24.21+, pnpm, Docker — `git clone` → `corepack enable` → `pnpm start`. Self-host with Docker Compose for always-on schedules while clients are closed. (../../raw/github/n8n-io-nod.md)

## Example usage

```sh
git clone https://github.com/n8n-io/nod.git
cd nod
corepack enable
pnpm start
```

Or download the latest DMG / Windows installer from GitHub Releases, complete onboarding (optional email via Composio, model connection, privacy choices), then ask in chat e.g. "Every weekday at 8:00, summarize my calendar and anything urgent in my inbox." Approvals still apply on each outside action. (../../raw/github/n8n-io-nod.md)

## When to use

Use Nod when you want a local-first personal agent that finishes multi-step errands across apps and websites with human approval gates — not a shared team workflow on [[n8n.io]], and not a chat-only assistant that leaves you a checklist. Best for solo operators and freelancers comfortable connecting a model provider (or ChatGPT Plus/Pro). Keep a machine awake (or self-host) if you rely on schedules; managed hosting and phone calls are on the roadmap. Not for multi-owner shared memory yet (one owner per installation).

## Maintenance status

- **Status:** research preview from n8n Labs; does not change n8n's product direction.
- **Repo:** `n8n-io/nod` — ~1,829 stars, ~247 forks, Apache 2.0, default branch `main`, latest release `nod-v0.8.0` (2026-11-16).
- **Homepage / docs:** https://nod.n8n.io/ · https://nod.n8n.io/docs/
- **Published benchmarks (vendor):** 98% of 226×3 errand runs finished; 0/678 unsafe actions; 93.2% LongMemEval-S; 0/216 WhisperBench false memories (GPT-6.1 Sol, Oct 2026, simulated accounts — not a guarantee).
(../../raw/github/n8n-io-nod.md)

## Ecosystem

- **Sibling platform:** [[n8n.io]] for shared team automations; optional n8n instance connection from Nod.
- **App auth / tools:** Composio (see [[composio.dev]]); MCP tools supported in the runtime.
- **Agent runtime:** Pi (see [[pi.dev]] / earendil-works/pi).
- **Peers:** desktop personal agents like [[composio-community-open-dot]] and [[hermes-agent.nousresearch.com]]; browser-computer peers like [[browser-use.com]] and [[vercel-labs-agent-browser]].
- **Community:** n8n Discord, n8n Labs forum, GitHub Discussions/Issues.

## Documentation

Primary docs at https://nod.n8n.io/docs/ (Starlight): get-started (what-is-nod, install desktop/source, first conversation), connect (models, local models, apps), use (chat, schedules, spending), how-it-works (architecture, agent runtime, memory, benchmarks), trust (principles, approvals, Vault, compare vs Instinct / Meta Muse / OpenAI dots), deploy (self-host, Mac mini), contribute. Launch announcement: https://blog.n8n.io/meet-nod/ (Ophir Prusak, 2026-11-10).
