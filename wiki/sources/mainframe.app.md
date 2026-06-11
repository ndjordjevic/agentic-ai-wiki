---
type: source
source_url: https://mainframe.app/
tags: [agent-video-generation, mcp-compatible, team-collaboration, agent-observability, ai-coding-agent, video-recap]
related: []
product: mainframe
detail_level: standard
created: 2026-06-11
updated: 2026-06-11
---

Mainframe is a video generation platform designed specifically for AI agent workflows: it turns agent work sessions into shareable, watchable videos that teams can keep up with without needing to be present during execution. Positioned as "MCP + skill compatible," it integrates with Claude Code, Cursor, Codex, and other AI coding tools, making it straightforward to capture and distribute agent output as video recaps.

_All claims below are sourced from ../../raw/web/mainframe.app.md unless otherwise noted._

## What it does

Mainframe converts AI agent work sessions into short videos that can be generated automatically or uploaded manually. Each video can be customized with an avatar persona, voice narration, and the team's brand palette and typeface before being shared via a link. The intended audience is teams where only some members run agents directly — Mainframe gives passive team members a way to stay current through a format that requires no terminal access.

## Key features

- **Agent-native integration** — Works as an MCP server or skill, compatible with Claude Code, Cursor, Codex, and OpenAI-compatible tools; agents can trigger video generation directly from their workflow
- **Generate or upload** — Teams can auto-generate videos from live agent sessions or upload their own recordings for narration and branding treatment
- **Shareable links** — Each video gets a link suitable for Slack, PR comments, async standups, or documentation
- **Custom avatars and voice** — Videos feature a configurable avatar persona and AI voice narration, not just a raw terminal recording
- **Brand palette and typeface** — Outputs can carry team or company styling for professional-looking distribution

## Architecture and concepts

Mainframe is a SaaS platform with a web app at `mainframe.app` and an MCP/skill integration layer that hooks into AI coding environments. The workflow is: agent runs → Mainframe captures or receives session data → video is generated with narration and avatar → shareable link is produced. No local infrastructure is required; the rendering and hosting are cloud-side.

## Main APIs

Mainframe exposes an MCP server and skill-based interface for agent integrations. Direct API documentation is not publicly accessible at `mainframe.app/docs` (returns 404), so integration details are available through the Discord community (`discord.gg/c2fxzJUr5F`).

## When to use

Use Mainframe when your team runs AI coding agents (Claude Code, Cursor, Codex) and needs a lightweight way to broadcast what the agent did — merged PRs, shipped features, blocked items — without requiring teammates to tail logs or sit in a terminal session. It is particularly well-suited for async teams, daily standups driven by agent work, and documenting complex agentic coding sessions for future review.

## Ecosystem

- **Claude Code** — Primary integration target; Mainframe is MCP + skill compatible
- **Cursor / Codex / OpenAI tools** — Also supported
- **Discord** — Primary support and community channel (discord.gg/c2fxzJUr5F)
- **Pricing** — Starter (free, 10 generations/month, unlimited uploads); Pro ($20/user/month, 25 generations/month, $0.50 per additional, no watermark, team invites)
