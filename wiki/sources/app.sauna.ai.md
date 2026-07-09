---
type: source
category: "Workflow automation & no-code platforms"
source_url: https://app.sauna.ai/
tags:
  - ai-coworker
  - multiplayer-agent
  - scheduled-tasks
  - workspace-memory
  - mcp-connectors
  - omnichannel-agent
  - just-in-time-apps
  - operator-workspace
related:
  - paperclip.ing
  - runcabinet.com
  - hilash-cabinet
  - happy.engineering
  - joinoasis.com
  - supermemory.ai
  - trigger.dev
  - abacus.ai
  - vellum.ai
product: sauna
detail_level: standard
created: 2026-07-07
updated: 2026-07-07
---

Sauna is a hosted, multiplayer AI coworker and workspace — marketed as "the first multiplayer AI" — that connects to 3,000+ tools (Linear, GitHub, Notion, Gmail, Slack, Stripe, HubSpot, custom MCP servers), learns how individuals and teams work, remembers context across sessions, and acts autonomously in the cloud on scheduled timers or on demand from the web app, iOS, iMessage, Slack, email, or Superhuman. YC- and Spark Capital-backed; SOC 2 compliant. A newer "Apps" layer lets operators vibe-code just-in-time personal SaaS UIs (CRM, email client, mission-control dashboards) orchestrated by the same agent that already holds their business context.

_All claims below are sourced from ../../raw/web/app.sauna.ai.md unless otherwise noted._

## What it does

Sauna positions itself as an AI coworker, not a chatbot: it ingests emails, documents, Slack threads, calendar, tickets, and files, builds a durable picture of how you operate, and takes work off your plate the way a chief-of-staff would — drafting in your voice, filing tickets, delivering briefings, chasing signatures, and running recurring ops on a schedule while you sleep. The web app (`app.sauna.ai`) is the default deep-work surface with Home, Dashboard (all sessions), Knowledge (files, Memory, Skills), Scheduled jobs, and cross-session Search. The same agent and memory follow you to iMessage (`(360) 228-5583`), Slack DMs and @mentions, email forwards to `hey@sauna.ai`, and Superhuman comment tags.

Multiplayer is first-class: teammates can share Spaces (project workspaces with shared knowledge, skills, schedules, connections), grant Brain Access (read-only or full access to someone's entire Sauna), or share specific folders with read or read-write permissions. Peer-to-peer "ask a colleague's Sauna" lets you query another person's agent without interrupting them.

## Key features

- **3,000+ integrations** plus custom MCP connectors and API keys for anything outside the catalog (Linear, GitHub, Notion, Gmail, Google Calendar, Jira, HubSpot, Stripe, PostHog, etc.).
- **Dual memory model** — workspace memory (`memory/` files, curated `documents/`) for durable rules and identity; session memory for episodic conversation history with automatic skims and deeper archive search on demand.
- **Scheduled work** — recurring jobs (daily briefings, weekly reports, PR review queues every 30 minutes, monthly investor updates) that compound into Skills when refined in chat.
- **Skills** — learned behaviors stored in Knowledge; scheduled tasks can bake Slack-thread feedback back into future runs.
- **Omnichannel surfaces** — one agent, same memory on web, iOS, iMessage, Slack, email, Superhuman.
- **Cloud autonomy** — agent keeps working offline; drafts messages, tracks priorities, files tickets, delivers briefings around the clock.
- **Apps (just-in-time personal SaaS)** — vibe-code bespoke interfaces (Superhuman-style inbox, Stripe CRM, mission-control dashboards) that inherit Sauna's credentials and intelligence; buttons for speed, docked chat for edge cases; apps share data without Zapier.
- **20 starter use-case prompts** across Comms, Operations, Admin, Growth, and Insights with surface-specific invocation patterns.
- **SOC 2 compliance**; data not used for model training; encrypted, private context.

## Architecture and concepts

Sauna's architecture centers on a persistent cloud agent with a file-system-like Knowledge layer (My Files, Memory, Skills), session-based work on the Dashboard, and timer-driven Scheduled jobs. Workspace memory and session memory are deliberately separate: curated files answer "what should stay true," while conversation history and retrieval answer "what was literally said." Live chat always wins over stale session reminders.

Connections hold OAuth credentials centrally — Apps and scheduled tasks inherit them, so a Zero Desk CRM can pull Stripe and draft Superhuman emails without per-app integration wiring. Spaces add a multiplayer boundary: shared knowledge, skills, schedules, and connections with granular teammate permissions.

The Apps layer introduces a chat-to-UI crystallization pattern: start in natural language, repeat a workflow, and Sauna generates a focused interface (split inbox, CRM table, mission-control charts) backed by the same agent. Mission Control dashboards assemble live views over connected tools and self-refresh.

Pricing is credit-metered on flat monthly plans (Basic $99/6k credits, Pro $299/24k, Team $999/60k shared) with top-up packs; every plan includes all integrations, surfaces, and top-tier models.

## Main APIs

No public developer SDK or open HTTP API is documented at this ingest. The integration surface for builders is:

- **MCP connectors** — add custom MCP servers for tools outside the 3,000-app catalog.
- **API keys** — connect arbitrary services not in the connections list.
- **Email** — forward threads to `hey@sauna.ai` with instructions above the forward.
- **Slack** — `/login` OAuth binding; DM and @mention invocation.
- **iMessage** — text `(360) 228-5583`; `/new`, `/unlink` commands.
- **Superhuman** — tag `@hey@sauna.ai` in comments.

Apps are generated and hosted within Sauna's platform (`desk.sauna.new/shared` style URLs for shared Spaces) rather than exported as standalone deployable code.

## When to use

Use Sauna when you want a single AI coworker that already knows your business context and can act across your real tools — especially if work should continue on timers (morning briefings, changelog drafts, PR queues, vendor renewal radar) or arrive on the channel you already live in (Slack DM, iMessage, email) without opening another app.

Strong fits: founder/operator workflows spanning inbox + calendar + tickets + payments; team coordination where shared memory beats per-person blank-slate agents; replacing Zapier chains with an agent that holds credentials and judgment; prototyping bespoke internal tools (CRM, triage inbox, dashboards) without a separate eng sprint.

Less suited when you need a self-hosted or open-source agent runtime, a code-first SDK to embed in your product, or fine-grained programmatic control over agent loops — Sauna is a closed, hosted product (no public GitHub repo found). Compare [[paperclip.ing]] if you need an org-chart control plane over bring-your-own agents, [[runcabinet.com]] / [[hilash-cabinet]] for self-hosted markdown-as-database agent OS, or [[happy.engineering]] if the goal is extending Claude Code from mobile while execution stays on your machine.

## Ecosystem

Backed by Y Combinator and Spark Capital; makers of Product Hunt's #1 product of all time. Competes in the "AI coworker / operator workspace" category alongside [[joinoasis.com]], [[abacus.ai]], and self-hosted alternatives [[runcabinet.com]]. The memory split (workspace files vs session recall) parallels patterns in [[coleam00-claude-memory-compiler]] and hosted memory APIs like [[supermemory.ai]]. Scheduled autonomous work overlaps [[trigger.dev]]-style job runners but with agent judgment baked in. Skills and MCP connector support align with the broader agentskills ecosystem cataloged in [[skills.sh]]. Omnichannel reach (Slack, iMessage, email) is comparable to notification primitives like [[pushover.net]] but with full agent execution, not just alerts.
