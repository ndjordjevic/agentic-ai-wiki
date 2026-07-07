# vellum.ai

## Fetch log
- Inbox URL: https://www.vellum.ai/
- Final URL: https://www.vellum.ai/
- Fetched: 2026-07-07
- Pages: 8
- Mode: standard

## llms.txt — https://vellum.ai/llms.txt
# Vellum

> Your personal AI assistant that remembers, learns, and takes real action — across every platform you use.

Vellum is a personal intelligence platform. Unlike chatbots that reset every conversation, Vellum gives you a persistent AI assistant with deep memory, its own identity, and the ability to act autonomously on your behalf — sending emails, managing calendars, browsing the web, controlling your Mac, and more.

It's not a chatbot. It's not an autocomplete engine. It's a separate entity that works for you, learns about you, and takes real actions in the real world.

- It has tools, not just words — browse the web, read files, run code, send emails, manage calendars, control your Mac via accessibility APIs
- It remembers you — across days, weeks, months. Preferences, projects, quirks.
- It has its own identity — its own email, GitHub account, Slack handle. Recipients know they're talking to your assistant.
- Your data stays yours — encrypted Vellum Cloud or on your own machine. Plain-text, exportable, deletable.

Install: `curl -fsSL https://www.vellum.ai/install.sh | bash && . ~/.config/vellum/env`

Repo: https://github.com/vellum-ai/vellum-assistant

Docs: https://www.vellum.ai/docs

Docs LLM index: https://www.vellum.ai/docs/llms.txt

Download: https://www.vellum.ai/downloads

## Hosting Options

- **Vellum Cloud** (default): Always-on sandboxed environment with managed API keys, per-account isolation, reachable from all channels. Sign up at vellum.ai and your assistant is provisioned in seconds.
- **Local**: Desktop app on Mac, workspace at `~/.vellum/workspace/`. The runtime is open source. Bring your own Anthropic API key, stored in macOS Keychain.

---

## The Workspace

Your assistant's identity, personality, and knowledge live in its workspace — a set of plain text files you can open, read, and edit.

### Directory Structure

```
~/.vellum/workspace/
├── IDENTITY.md            # Name, emoji, nature, personality, role
├── SOUL.md                # Principles and behavioral rules (constitution)
├── USER.md                # Learned facts about you
├── NOW.md                 # Working scratchpad (tasks, context, goals)
├── config.json            # Runtime configuration
├── conversations/         # Per-conversation folders with attachments
├── skills/                # Installed and custom skills
│   └── <skill-name>/
│       ├── SKILL.md       # Instructions for when/how to use the skill
│       ├── TOOLS.json     # Tool manifest (inputs, risk levels, execution targets)
│       └── tools/         # Implementation code
├── pkb/                   # Personal Knowledge Base (curated markdown notes)
│   └── INDEX.md           # Browse the knowledge base
├── scratch/               # Working files, exports, generated assets
└── data/
    ├── db/                # Conversation history (SQLite)
    ├── qdrant/            # Memory embeddings (vector DB)
    ├── apps/              # User-built apps
    ├── avatar/            # Avatar image
    ├── browser-profile/   # Headless browser session data
    ├── sounds/            # Custom notification sounds
    └── logs/              # Daemon logs
```

### Core Identity Files

Loaded into every conversation:

1. **IDENTITY.md** — Name, emoji, nature (how it thinks of itself), personality (vibe and conversational style), role (what it does for you)
2. **SOUL.md** — Constitution: core principles (be helpful, be resourceful, have opinions, earn trust), communication style, task approach, boundaries
3. **USER.md** — Everything learned about you: name, pronouns, locale, work role, tools, projects, communication preferences, connected services
4. **NOW.md** — Working scratchpad for in-progress tasks, session context, goals, carry-over between conversations

### Credentials & Secrets

Stored separately from the workspace in an isolated credential vault (encrypted in Vellum Cloud, or macOS Keychain for local). Never included in workspace exports or diagnostic logs. The assistant can use credentials to act on your behalf but cannot read or display them in conversation.

### Sandbox Model (Desktop App)

- **Workspace tools** (no approval needed): `file_read`, `file_write`, `file_edit` — restricted to `~/.vellum/workspace/`
- **Host tools** (requires approval): `host_file_read`, `host_file_write`, `host_file_edit` — anywhere on your machine
- **Shell commands**: `bash` (sandboxed to workspace), `host_bash` (on your machine, requires approval)
- Path traversal via `../` is blocked. Symlinks pointing outside the boundary are rejected.

---

## Memory System

Three layers of memory, designed to work like human memory:

### Layer 1: Workspace Files (Baseline)

SOUL.md, IDENTITY.md, USER.md, NOW.md — loaded into every conversation. Your assistant updates them as it learns. You can edit them directly at any time.

### Layer 2: Knowledge Base (Curated)

Lives in `pkb/` — a set of markdown notes the assistant maintains about you, your work, and your projects. Longer-form, organized, human-readable. Open `pkb/INDEX.md` to browse.

### Layer 3: Long-term Memory (Auto-extracted)

Extracted facts and moments from conversations, stored as searchable, categorized items. Each memory has:
- **Confidence score** — how certain the fact is
- **Importance rating** — how significant
- **Source type** — told directly, observed, or inferred
- **Reinforcement count** — grows each time the memory comes up again

### Memory Types

| Type | Description | Example |
|------|-------------|---------|
| Event | Specific things that happened | "Shipped v0.7.0 today" |
| Knowledge | Stable facts | "Marina works at Vellum as a GTM Engineer" |
| Feeling | Emotional moments (fade over time) | "Felt great after the demo went well" |
| Plan | Intentions and goals | "Wants to publish the AI memory article next week" |
| Pattern | Recurring habits and preferences | "Prefers paragraphs over bullet lists" |
| Story | Connected narratives spanning events | "The arc of building Becky over the past month" |
| Shared | Information involving others | "Sidd is the CTO at Vellum" |
| Skill | System-managed: how to do things | (auto-learned) |

### How Memory Recall Works (Hybrid Retrieval Pipeline)

1. **Embed** — your message is converted into dense (semantic meaning) and sparse (keyword) vectors
2. **Search** — both vectors search the memory store; results merged via Reciprocal Rank Fusion
3. **Score** — composite score combining semantic relevance, recency (logarithmic decay), reinforcement count, and extraction confidence
4. **Tier** — high-scoring results get priority injection; moderate results marked "possibly relevant"; lower scores dropped
5. **Stability check** — memories with low stability or past their natural lifetime are demoted
6. **Two-layer injection** — formatted and inserted as structured context, split into identity/preference layer and general context layer

### Memory Behaviors

- **Extraction**: After each message, identifies facts worth keeping. Assigns kind, confidence, importance, source type. Low-value messages ("ok", "thanks") filtered out.
- **Deduplication**: Fingerprint check prevents duplicates — repeats reinforce existing memories instead.
- **Correction**: New facts contradicting older ones supersede them. Explicit corrections replace immediately; inferred contradictions coexist until one wins through reinforcement.
- **Decay**: Memories that go quiet lose stability and get demoted before eventually dropping out.
- **Trust gates**: Memory extraction only runs on messages from trusted actors (the guardian/owner). External parties can't inject false facts.
- **Private conversations**: Isolated memory scope — memories can't leak out to other conversations, but can read from shared memory.

### Context Window Management

When conversations approach 80% of the context limit:
1. Older messages summarized (preserving goals, decisions, constraints, file paths, errors, open questions)
2. Tool results truncated to essentials
3. Images/file contents replaced with text descriptions
4. Memory injection scaled back to recent items only
5. Manual compaction available via `/compact`

---

## Tools & Skills

### Core Tools (Always Available)

| Tool | Description |
|------|-------------|
| `file_read` | Read a file in the workspace |
| `file_write` | Create or overwrite a file in the workspace |
| `file_edit` | Surgical find-and-replace edit |
| `bash` | Run a shell command (sandboxed to workspace) |
| `web_search` | Search the internet |
| `web_fetch` | Fetch and extract content from a URL |
| `memory_manage` | Save, update, or delete facts in long-term memory |
| `memory_recall` | Search long-term memory |
| `skill_load` | Activate a skill for the current conversation |
| `skill_execute` | Run a tool provided by a loaded skill |
| `credential_store` | Manage credentials (prompt, store, connect OAuth) |
| `request_system_permission` | Ask for a macOS system permission |

### Host Tools (Requires Approval)

| Tool | Description |
|------|-------------|
| `host_file_read` | Read any file on your computer |
| `host_file_write` | Write to any file on your computer |
| `host_file_edit` | Edit any file on your computer |
| `host_bash` | Run a shell command on your machine (unsandboxed) |

### How Skills Load

Skills aren't all active at once. The assistant sees a catalog of available skills (names, descriptions, activation hints) in every conversation. When a skill is relevant, it calls `skill_load` to activate it:
1. Full instructions (SKILL.md) injected into conversation context
2. Tools become available for use
3. Stays active for the rest of the conversation

### Custom Skills

Describe what you want and the assistant scaffolds a full skill:
- `SKILL.md` — instructions
- `TOOLS.json` — tool definitions with inputs, risk levels, execution targets
- `tools/` — TypeScript executors

Community skills are published on [skills.sh](https://skills.sh). The assistant can search, inspect, audit, and install them.

---

## Skills Reference (Full)

### Gmail

Full Gmail management via OAuth2. Say "Connect my Gmail" for one-time setup.

**Capabilities**: Read, search, triage inbox. Draft and send emails (sending requires approval). Archive, label, trash. Bulk unsubscribe. Create filters. Manage attachments. Vacation auto-responder. Sender digest analysis. Cold outreach detection.

**Example prompts**:
- "Archive everything from newsletters"
- "Unsubscribe me from marketing emails"
- "Draft a reply to Sarah's last email"
- "What emails need my attention?"
- "Set up a filter for Jira notifications"
- "Who's been emailing me the most?"

### Agent Mail (Email)

Gives your assistant its own email address (e.g. `gigi@agentmail.vellum.ai`). Say "Set up your email" for one-time setup.

**Capabilities**: Send, receive, read, search email independently. Thread-aware conversations. Custom domain support (assistant handles DNS setup and verification). Bulk inbox management.

**Key detail**: This is the assistant's own email, not yours. Recipients see the assistant's address. For your inbox, set up forwarding to the assistant's AgentMail address.

**Example prompts**:
- "Check my email"
- "Send an email to alex@example.com about the deadline"
- "Search my email for anything from Stripe"

### Slack

Slack integration via Socket Mode (no public webhook URL needed). Say "Set up Slack" to connect.

**Capabilities**: Scan channels, summarize threads with attribution. Reply to threads. Manage reactions. Per-channel permission profiles control which tools are available in which channels.

**Privacy guardrails**: Won't share Slack context outside Slack without explicit instruction.

**Example prompts**:
- "What happened in #engineering today?"
- "Summarize that thread about the API migration"
- "Set up channel permissions for #general"

### Phone Calls

Twilio-based outbound/inbound voice calls. Real-time voice conversation with transcripts stored as conversation history.

### Contacts

Manage communication channels and access control for people your assistant interacts with.

### Notifications

Unified notification routing across all platforms.

### Google Calendar

Full calendar management via Google OAuth.

**Capabilities**: View, create, coordinate events. Conflict detection. Daily briefing integration.

**Example prompts**:
- "What's on my calendar today?"
- "Schedule a meeting with Alex next Tuesday at 2pm"
- "Do I have any conflicts this week?"

### Tasks

Reusable task templates and work queues for structured task management.

### Schedule

Recurring and one-shot scheduled actions. Persistent across conversations.

**Supports**: Cron syntax, RRULE (RFC 5545) for complex recurrence, ISO 8601 timestamps for one-time events. Two modes: "execute" (run a task) or "notify" (send a notification). Timezone-aware.

**Key detail**: Scheduled actions run with the same permission rules as interactive actions.

**Example prompts**:
- "Remind me to check my email every morning at 9am"
- "Every Friday at 5pm, summarize my week"
- "Show me my active schedules"

### Followups

Track messages awaiting responses. Automatically monitors for replies and alerts you.

### Playbooks

Trigger-action automation for incoming messages. Define rules for how the assistant should handle specific types of messages automatically.

### Document

Write and edit long-form content in a dedicated document editor. Not for interactive apps — use App Builder for those.

### Start the Day

Personalized daily briefing. Compiles calendar, email, Slack, and task updates into a morning summary.

### Computer Use

Controls your Mac directly through accessibility APIs and screenshots. macOS only.

**Capabilities**: Observe screen via accessibility tree and screenshots. Click elements, type, scroll, drag, open apps, run AppleScript.

**Permissions required**: Accessibility (mouse/keyboard control), Screen Recording (seeing screen content). Each action prompted individually.

**Configuration**: Step limit of 50 actions per session with loop detection. Uses both accessibility tree (same API screen readers use) AND screenshots. Prefers clicking by element name over coordinates.

**Example prompts**:
- "Open Safari and go to my bank's website"
- "Fill out this form with my info"
- "Switch to Slack and check my DMs"

### Browser

Headless browser for web interaction. No setup required, runs in the sandbox.

**Capabilities**: Navigate pages, extract text, fill forms, click buttons, take visual screenshots, handle authentication via stored credentials.

**Key detail**: Starts fresh every time — no cookies, no logged-in sessions. Store credentials in the vault for login: "Store my GitHub login". Credentials are domain-scoped. If a direct API/CLI exists (GitHub, Jira), the assistant prefers that over browser automation.

**Example prompts**:
- "Go to example.com and tell me what's on the page"
- "Search for flights from JFK to Lisbon in June"
- "Log into my Jira and check my open tickets"

### Screen Watch

OCR-based screen monitoring at configurable intervals. Watches for changes and alerts you.

### Watcher

Polls external sources for changes. Configurable polling intervals and trigger conditions.

### Subagent

Spawns autonomous background agents for parallel work. Each subagent has its own conversation context but shares the workspace.

### App Builder

Creates fully interactive web applications from natural language. No setup required.

**App types**:
- **App** (default): Interactive tools with state and logic — calculators, dashboards, trackers, games, kanban boards
- **Site**: Presentational pages — portfolios, landing pages, resumes

**What apps include**: Open in their own panel. Fully interactive (buttons, inputs, animations, state). Persistent. Follow a design system. Iterable after creation.

**Home Base**: A special app serving as your dashboard. Customizable: "Add a button to my dashboard for checking email."

**Example prompts**:
- "Build me a habit tracker"
- "Make a pomodoro timer"
- "Create a budget dashboard"
- "Add a dark mode toggle" (iterating on existing app)

### Frontend Design

Production-grade interface generation with proper hover states, animations, typography, and responsive layouts.

### ACP (Agent Client Protocol)

Delegate tasks to external coding agents. Protocol for inter-agent communication and task handoff.

### Image Studio

Generate and edit images. Supports iterative refinement.

### Media Processing

Video, audio, and image pipelines. Conversion, resizing, editing.

### Transcribe

Whisper-based audio/video transcription. Supports multiple languages.

### Amazon

Shopping assistance — search products, compare prices, track orders.

### DoorDash

Food and grocery ordering.

### Weather

Current conditions and forecasts.

### Skill Management

Create, delete, and manage custom skills programmatically.

### ChatGPT Import

Import conversation history from ChatGPT for continuity.

---

## Channels

Your assistant is the same everywhere — same personality, same memories, same skills. Only the channel capabilities differ.

### Available Channels

| Channel | Setup | Key Capabilities |
|---------|-------|------------------|
| **Web** | Sign in at vellum.ai | Chat, voice input, document editor, app viewer, approvals |
| **macOS Desktop** | Install .dmg | All features: computer use, host file/shell access, screen watch, voice |
| **iOS** | App Store | Chat, mobile UI, cloud-only |
| **CLI** | `vellum` command | Streaming SSE, permission prompts, all sandbox skills |
| **Telegram** | Create bot via BotFather | Text, images, documents, inline button approvals |
| **Slack** | Socket Mode app | Channel scanning, threaded conversations, per-channel permissions |
| **Email** | Gmail OAuth or AgentMail | Full inbox management or assistant's own address |
| **Phone** | Twilio provisioning | Real-time voice, transcripts stored |

### Capability Matrix

| Capability | Web | Desktop | iOS | CLI | Telegram | Slack | Email | Phone |
|---|---|---|---|---|---|---|---|---|
| Chat | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Voice |
| Computer use | — | Yes | — | — | — | — | — | — |
| Host file/shell | — | Yes | — | — | — | — | — | — |
| Screen watch | — | Yes | — | — | — | — | — | — |
| Voice input | Yes | Yes | — | — | — | — | — | Yes |
| Approvals | Native | Native | Native | Native | Inline buttons | Interactive buttons | Plain text | — |
| Notifications | Yes | Yes | Yes | Yes | Yes | Yes | — | — |

### The Guardian

The guardian is you — the primary owner. Three responsibilities:
1. **Verifies who's talking** — challenge-response flow links channel identities to your account
2. **Routes approvals** — sensitive actions require your explicit allow/deny
3. **Gates memory extraction** — only your messages create long-term memories

---

## Developer Guide

### Architecture

Three main components:

1. **Assistant Runtime** (`assistant/`) — Bun + TypeScript. Owns conversation history, attachment storage, channel delivery state in SQLite. Exposes Unix domain socket for native client + HTTP API for the gateway.
2. **Gateway** (`gateway/`) — Bun + TypeScript. Public ingress boundary for webhooks and callbacks. Handles Telegram webhooks, Twilio voice, OAuth callbacks. Authenticated reverse proxy for the runtime API.
3. **Credential Execution Service** (`credential-executor/`) — Isolated service for credential storage and execution. Keeps API keys and OAuth tokens separate from the LLM.

### API

The assistant runtime exposes an HTTP API. Default ports by component:

| Component | Default Port | Description |
|-----------|-------------|-------------|
| Gateway | 3001 | Public ingress — SSE streams, webhooks, reverse proxy |
| Assistant daemon | 7821 | Direct runtime API — conversations, messages, tools |

In most setups, clients connect through the **gateway** (port 3001), which authenticates and proxies to the daemon.

#### SSE Event Stream

```
GET /v1/events?conversationKey=<key>
Authorization: Bearer <jwt>
```

Long-lived server-sent events stream. When `conversationKey` is omitted, subscribes to all conversations.

**Connection limits**: Up to 100 concurrent SSE connections; oldest evicted at cap. Slow consumers closed at 16 queued events. Heartbeat comments every 30 seconds.

**Event types**:

| Event | Description |
|-------|-------------|
| `assistant_text_delta` | Incremental text token from the model |
| `assistant_thinking_delta` | Reasoning token |
| `tool_use_start` | Tool invocation starting |
| `tool_input_delta` | Streaming tool input chunk |
| `tool_output_chunk` | Streaming tool output chunk |
| `tool_result` | Tool execution result |
| `message_complete` | Turn complete with full message + attachments |
| `confirmation_request` | User approval needed before action executes |
| `generation_handoff` | Sub-agent handoff |
| `generation_cancelled` | Run cancelled |

**JavaScript example** (connecting via the gateway on port 3001):

```javascript
const TOKEN = '<jwt>';
const res = await fetch(
  'http://localhost:3001/v1/events?conversationKey=my-conversation',
  { headers: { Authorization: `Bearer ${TOKEN}` } },
);

const reader = res.body.getReader();
const decoder = new TextDecoder();
let buf = '';

while (true) {
  const { done, value } = await reader.read();
  if (done) break;
  buf += decoder.decode(value, { stream: true });
  const frames = buf.split('\n\n');
  buf = frames.pop() ?? '';

  for (const frame of frames) {
    const dataLine = frame.split('\n').find((l) => l.startsWith('data: '));
    if (!dataLine) continue;
    const event = JSON.parse(dataLine.slice(6));
    console.log(event.message.type, event.message);
  }
}
```

#### REST Endpoints

Examples using the daemon directly (port 7821):

```bash
# List conversations
curl -H "Authorization: Bearer $VELLUM_JWT" \
     http://127.0.0.1:7821/v1/conversations

# Post a message
curl -X POST \
     -H "Authorization: Bearer $VELLUM_JWT" \
     -H "Content-Type: application/json" \
     -d '{"text": "hello"}' \
     http://127.0.0.1:7821/v1/messages
```

#### CLI

```bash
vellum message "summarize today's calendar"   # send message, stream response
vellum events                                  # tail the live event stream
vellum ps                                      # inspect process state
vellum logs                                    # view daemon logs
vellum doctor                                  # full diagnostic check
```

Subcommands: `login`, `setup`, `hatch`, `message`, `events`, `logs`, `ps`, `terminal`, `retire`.

#### Remote Access

Forward the daemon port over SSH to access a remote assistant locally:

```bash
ssh -L 8741:localhost:8741 user@remote-host -N &
VELLUM_DAEMON_URL=http://localhost:8741 vellum
```

### Managed OAuth

Declarative OAuth provider integration via `provider_registry.json`. Currently supported: Twitter/X, Google, Outlook/Microsoft, Linear, GitHub, Notion, Asana, Todoist, Dropbox, Discord, Airtable, HubSpot, Salesforce.

**Endpoints**:
- `POST /v1/assistants/{id}/oauth/{provider}/start/` — Start OAuth flow
- `GET /v1/oauth/callback/` — OAuth callback (public)
- `GET /v1/assistants/{id}/oauth/connections/` — List connections
- `POST /v1/assistants/{id}/oauth/connections/{conn_id}/disconnect/` — Disconnect
- `GET /v1/assistants/{id}/oauth/managed/catalog/` — Provider catalog
- `POST /v1/assistants/{id}/oauth/managed/materialize/` — Token materialize

### LLM Providers

Default: Anthropic Claude. Bring-your-own supported for OpenAI, Google Gemini, OpenRouter, Fireworks, and local Ollama.

---

## Security Model

### Single-Owner Trust Boundary

Each assistant pod belongs to exactly one user. All containers (assistant, gateway, credential-executor sidecars) serve only that owner. Per-instance credentials scoped to a single assistant. No cross-tenant isolation concerns within a pod.

### Permissions Model

- Sensitive actions always require explicit user approval
- Trust rules can be configured per-action and per-channel
- Risk tolerance tiers control when approval is needed
- Allow button creates persistent trust rules for repeated actions

### Credential Isolation

The Credential Execution Service (CES) isolates API keys and OAuth tokens from the LLM:
- Credentials stored in a separate, isolated vault
- The LLM never sees raw credential values
- CES executes authenticated requests on behalf of the assistant
- Credentials are encrypted at rest (Vellum Cloud) or stored in macOS Keychain (local)

### Data Privacy

- No message content in analytics (only anonymous token counts)
- Data is plain-text, exportable, and deletable
- Memories stored in your private workspace (SQLite + Qdrant vector store)
- Not shared with other users or used to train AI models
- Included in context sent to AI model only when relevant

---

## Documentation

- [What Is Vellum](https://www.vellum.ai/docs/getting-started/what-is-vellum)
- [Quick Start](https://www.vellum.ai/docs/getting-started/quick-start)
- [Installation](https://www.vellum.ai/docs/getting-started/installation)
- [Key Concepts](https://www.vellum.ai/docs/key-concepts/the-workspace)
- [Memory & Context](https://www.vellum.ai/docs/key-concepts/memory-and-context)
- [Channels](https://www.vellum.ai/docs/key-concepts/channels)
- [Skills & Tools](https://www.vellum.ai/docs/key-concepts/skills-and-tools)
- [Skills Reference](https://www.vellum.ai/docs/skills-reference)
- [Developer Guide](https://www.vellum.ai/docs/developer-guide/get-started)
- [API](https://www.vellum.ai/docs/developer-guide/api)
- [Architecture](https://www.vellum.ai/docs/developer-guide/architecture)
- [Hosting Options](https://www.vellum.ai/docs/hosting-options/cloud-hosting)
- [Trust & Security](https://www.vellum.ai/docs/trust-security/privacy-and-data)
- [Roadmap](https://www.vellum.ai/docs/roadmap)
- [Releases](https://www.vellum.ai/releases)

## Landing page — https://www.vellum.ai/
# Vellum: Your Personal Intelligence

wake up — Today, 9:30 AM — Get Started

## The AI layer for your life

### Easy to set up
Create your assistant in minutes. Add your apps, share your goals, and it's ready to help.

### Self-improving
It learns how you like things done, remembers your preferences, and improves over time.

### Always on
It keeps running in the background, so work can move forward even when you're away.

## A memory system built for Personal AI
Your assistant learns your preferences, improves its skills over time, and gradually takes over the work you shouldn't be doing yourself.

Example skill outputs shown on site:
- EMAIL TRIAGE: Scanned 47 emails overnight. Flagged 3 that need your input, drafted replies for the rest, and archived the noise. (SKILL·EM01)
- Calendar rescheduling, meeting prep drafts, delegation, research briefings, Slack thread summaries, project tracking, travel booking

Categories highlighted: email triage, calendar, meeting prep, delegation, research, comms, project tracking, travel

## How to become AI-native and 10x yourself
Read more on site blog/resources.

## Comparison table (site positions Vellum vs Hermes, OpenClaw, Claude Cowork)
| Dimension | Vellum | Hermes | OpenClaw | Claude Cowork |
|---|---|---|---|---|
| Open source | MIT | MIT | Apache 2.0 | Proprietary |
| Time to set up | Easy | Moderate | Difficult | Easy |
| Native channels | iOS, MacOS, Web, Voice, Email, Telegram, Slack, CLI | CLI / TUI | CLI, MacOS, Web | CLI, MacOS, Windows, Web |
| Memory | Managed memory | SQLite + markdown — you build the memory stack | Basic memory, context loss | Limited |
| Security | Built-in security | DIY | DIY | No sandboxing |
| Hosting | Cloud or self-hosted | Self-hosted only | Self-hosted only | Anthropic cloud |
| Native integrations | Managed OAuth connections | No managed connectors | No managed connectors | MCP only |
| Schedules | Cron + Heartbeat | Cron + Heartbeat | Cron + Heartbeat | Cron only |
| Pricing | Free + API costs, Paid plans available | Free + DIY Hosting Costs + API costs | Free + DIY Hosting Costs + API costs | Paid plans available + API costs |

Links: Documentation, Discord community, GitHub source, Product features
Tagline: "The Personal AI you were promised"

## Docs — https://www.vellum.ai/docs
# Meet Vellum

Your personal AI assistant. For real this time.

Not another chatbot in a browser tab. Vellum is a personal AI assistant that lives in the secure Vellum Cloud, has its own identity, and actually does things in the world. It can have its own email, its own accounts, its own presence, set up in minutes, not hours. It works for you, but it isn't you.

## Built on four principles: inviting, yours, not you, needs to earn your trust

## So what can it actually do? (sample prompts)
- Start my day — weather, calendar, news briefing
- Build me a habit tracker — interactive web app in conversation
- Check my email — triage, summarize, draft replies
- Read this page and summarize it — browser extension
- Voice: calendar queries
- Call the dentist and reschedule — Twilio phone calls
- Post tweet / Slack message / Linear ticket updates
- Write blog post in document editor
- Remember preferences (PKB)
- Order coffee via DoorDash

## Get started in 5 minutes
1. Sign up at vellum.ai (free, no credit card)
2. Meet your assistant in browser
3. Have a conversation — name, personality, tell it about yourself
4. Do something useful

## Trust notes
- Every sensitive action asks permission (Allow/Deny with risk badge)
- Data is yours — exportable, deletable
- Prompts reach an AI model (transparency)
- You can always say no

## For LLMs and coding agents
- /docs/llms.txt — curated docs index
- /llms.txt — broader product overview

Doc sections: Getting Started, Key Concepts, Skills Reference, Trust & Security, Developer Guide, Roadmap, Help

## What is Vellum? — https://www.vellum.ai/docs/getting-started/what-is-vellum
Personal AI assistant in Vellum Cloud with its own identity, email, accounts. Not a chatbot — has tools, remembers across sessions, separate identity, your data stays yours, personal (not team).

Capabilities by category: Communication (Gmail, Agent Mail, Slack, phone, contacts), Productivity (Calendar, Tasks, Schedule, Followups, Playbooks, Document, Start the Day), Automation (Computer Use, Browser, Screen Watch, Watcher, Subagent), Development (App Builder, Frontend Design, ACP), Media (Image Studio, Media Processing, Transcribe), Services (Amazon, DoorDash, Weather), Knowledge (Memory, SOUL/IDENTITY/USER files, Skill Management), Integrations (OAuth, MCP, ChatGPT Import, Voice).

Hosting: Vellum Cloud (default), Web app, macOS desktop (Sequoia+), Channels (Telegram, Slack, Phone).

How it works: talk → think (context + cloud model) → act (tools, permission-gated) → learn (workspace memory).

Safety: trust system, explicit approvals, encrypted credentials.

## Memory & Context — https://www.vellum.ai/docs/key-concepts/memory-and-context
Three layers: (1) workspace files — essentials.md, threads.md, recent.md, buffer.md loaded every conversation; (2) knowledge base pkb/ curated markdown; (3) long-term auto-extracted memory with kinds Event/Knowledge/Feeling/Plan/Pattern/Story/Shared/Skill.

Extraction after each message with confidence, importance, source type; fingerprint dedup; consolidation every 4 hours; supersession for corrections; procedural memory saved as self-authored skills.

Context assembly: working memory files + PKB + conversation history + memory recall + active skill + user message.

Hybrid retrieval: dense + sparse embeddings, BM25, spreading activation, summaries-first, composite scoring, stability check, two-layer injection, injection gate (rolling out).

Compaction at 80% context window; private conversations with isolated memory scope; guardian trust gates memory extraction.

Storage: SQLite + Qdrant in ~/.vellum/workspace/data/ or encrypted cloud workspace.

## Tools & Skills — https://www.vellum.ai/docs/key-concepts/skills-and-tools
Tools = atomic actions. Core: file_read/write/edit, bash, web_search/fetch, memory_manage/recall, skill_load/execute, credential_store, request_system_permission. Host tools (approval): host_file_*, host_bash.

Skills = bundles (SKILL.md + optional TOOLS.json + tools/). 28 bundled skills across Communication, Research & content, Productivity, Computer use, Monitoring, Development, System.

skill_load activates per conversation. Custom skills scaffolded on request; community via skills.sh. Voice configurable (TTS provider, voice ID, push-to-talk).

## Quick Start — https://www.vellum.ai/docs/getting-started/quick-start
After install: blank slate assistant, no onboarding wizard — just chat.

Surfaces: Web (vellum.ai), iOS App Store, Mac desktop (local file/computer control), plus Telegram/Slack/email/phone channels.

First moves: name it, tell it about yourself, ask capabilities, shape style.

Real tasks: draft email, calendar summary, build browser app, reminders. Approvals on sensitive actions; trust rules available.

Memories persist across conversations. Connect channels with verification handshake.

## Architecture — https://www.vellum.ai/docs/developer-guide/architecture
Three platform domains:
1. Assistant Runtime (assistant/) — Bun+TypeScript, SQLite, Unix socket + HTTP API
2. Native Clients (clients/) — macOS Swift menu bar app, computer use, chat
3. Gateway (gateway/) — public ingress: Telegram, Twilio voice, OAuth callbacks, reverse proxy

Also: credential-executor/, packages/, cli/, skills/, benchmarking/, scripts/, meta/

Architecture docs in repo: ARCHITECTURE.md, assistant/ARCHITECTURE.md, gateway/ARCHITECTURE.md, clients/ARCHITECTURE.md, security.md, memory.md, credential-execution-service.md
