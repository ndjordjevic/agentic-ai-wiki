---
type: source
source_url: https://postiz.com/
companion_urls:
  - https://github.com/gitroomhq/postiz-app
raw_files:
  - ../../raw/web/postiz.com.md
  - ../../raw/github/gitroomhq-postiz-app.md
tags:
  - social-media-scheduling
  - agentic-posting
  - mcp-server
  - public-api
  - ai-content-generation
  - self-hosted
  - cross-posting
related:
  - n8n.io
  - zapier.com
  - producthunt.com
product: postiz
detail_level: standard
created: 2026-07-01
updated: 2026-07-01
---

Postiz is an open-source, self-hostable social media scheduling platform that positions itself as "agentic" — built to be driven by AI agents (Claude, ChatGPT, OpenClaw, Codex) through a CLI and MCP server, in addition to its own visual calendar UI. It cross-posts to 30+ networks, ships a built-in AI content assistant for text/image/video generation, and exposes a public REST API plus native n8n, Make.com, and Zapier integrations for automation teams.

_All claims below are sourced from ../../raw/web/postiz.com.md unless otherwise noted._

## What it does

Postiz lets users plan, generate, and schedule posts to 30+ social networks (Instagram, TikTok, LinkedIn, X, Facebook, YouTube, Discord, Bluesky, Mastodon, Reddit, Slack, Telegram, and more) through a visual calendar for review and editing. AI agents can drive the same workflow via the CLI or MCP server instead of the web UI, drafting and scheduling posts end-to-end from natural-language prompts.

## Key features

- Cross-posting to 30+ platforms with per-channel post previews before scheduling
- Built-in AI agent for drafting post text, generating images, and producing short AI videos, all from one chat window
- Evergreen/recurring posts on a configurable cadence, plus RSS-based auto-posting (Team plan and up)
- Public REST API and webhooks for programmatic post creation, media upload, and integration management (../../raw/github/gitroomhq-postiz-app.md)
- Team collaboration with unlimited members and role-based access (Admin / Member) on paid plans, plus customer-group workspaces for agencies managing multiple brands
- Per-channel and per-post analytics pulled from each network's official insights API
- Official NodeJS SDK, n8n custom node, and Make.com integration for automation pipelines (../../raw/github/gitroomhq-postiz-app.md)

## Architecture

Postiz runs as a pnpm-workspace monorepo (TypeScript, NextJS frontend, NestJS backend) with a three-service architecture inside a single Docker container, plus four external dependencies: Temporal (durable workflow engine), Redis (session/caching), a SQL database (Postgres by default via Prisma), and file storage (local filesystem or Cloudflare R2). The Backend service coordinates scheduling, analytics, and user management, and triggers Temporal workflows for async work; the Orchestrator service runs those Temporal workflows — posting scheduled content, refreshing OAuth tokens per platform, and sending digest/notification emails. Temporal provides the reliability primitives (task queues, workflow visibility, durable state) so scheduled posts survive service restarts. (../../raw/github/gitroomhq-postiz-app.md)

## Installation

Self-hosting is the primary distribution path. Docker Compose is the recommended route for users (`docker-compose.yaml` at the repo root); a Development setup is recommended for contributors. Docker (standalone) and a Kubernetes Helm chart are also documented as advanced alternatives. Reverse-proxy guides exist for Caddy, Nginx, and Traefik, and there's a dedicated guide for running behind ngrok / dev tunnels with WebSocket support. Environment variables are the sole configuration mechanism — no providers are enabled by default, and each social provider must be configured via env vars, with a container restart (or `docker compose down && up`) required after changes. (../../raw/github/gitroomhq-postiz-app.md)

## Example usage

CLI (`postiz`, installed via npm/pnpm) wraps the Public API for scripted posting: authenticate with `postiz auth:login` (OAuth2 device flow) or a `POSTIZ_API_KEY` env var, then use commands like `posts:create`, `posts:list`, `integrations:list`, and `analytics:platform` — every command outputs JSON for use in scripts and CI pipelines. The MCP server (`https://api.postiz.com/mcp`, Bearer-token or URL-embedded-key auth) exposes nine tools — `integrationList`, `groupList`, `integrationSchema`, `triggerTool`, `schedulePostTool`, `generateImageTool`, `generateVideoOptions`, `videoFunctionTool`, `generateVideoTool` — so any MCP-aware client (Claude, ChatGPT, Cursor) can discover connected channels and schedule a post end-to-end from a prompt like "write me a LinkedIn post about X, make a matching image, schedule it for Tuesday at 9am." Programmatic post creation via the Public API requires a two-step image upload (POST to `/upload` for an image ID, then reference that ID in the post payload) followed by a `POST` to the create-post endpoint with schedule date, integration IDs, content, and per-platform settings. (../../raw/github/gitroomhq-postiz-app.md)

## When to use

Postiz fits three overlapping audiences: solo creators and small teams wanting a self-hostable Buffer/Hypefury alternative with a visual calendar; developers who want to build a custom posting app on Postiz's OAuth2 + public API + NodeJS SDK rather than integrating 30 platform APIs individually; and automation teams wiring social publishing into n8n, Make.com, or Zapier workflows. Its "agentic" positioning — CLI + MCP server as first-class interfaces — also makes it a natural target when an AI agent (not a human) needs to draft and publish content directly, which distinguishes it from purely human-facing schedulers.

## Maintenance status

The companion repo `gitroomhq/postiz-app` has 32,528 stars, 6,060 forks, and is actively maintained (latest push 2026-07-01, latest release v2.21.10 on 2026-06-22). Licensed AGPL-3.0. Primary language TypeScript; default branch `main`. The repo ships a root-level `CLAUDE.md` with agent instructions, and a `.claude/` config directory, indicating active Claude Code usage in its own development. (../../raw/github/gitroomhq-postiz-app.md)

## Ecosystem

Postiz has a hosted cloud offering (platform.postiz.com, 7-day $0 trial) with four paid tiers (Standard $29/mo–5 channels, Team $39/mo–10 channels, Pro $49/mo–30 channels, Ultimate $99/mo–100 channels) scaling AI image/video allowances and webhook counts per plan; self-hosting has the same feature set as the hosted version. A separate "Postiz agent CLI" project (`gitroomhq/postiz-agent`) is referenced from the main README as purpose-built for OpenClaw and other agents. Community channels: Discord (discord.postiz.com, developer-focused) and a YouTube tutorial channel (youtube.com/@postizofficial). Compare with [[n8n.io]] and [[zapier.com]], both of which Postiz lists as first-class automation integrations (native n8n node, Make.com app, and Zapier compatibility via its public API) rather than competitors — Postiz is the content-scheduling leaf node those platforms' workflows can call into.

## Documentation

Docs live at docs.postiz.com (Mintlify-hosted, own `llms.txt` catalog) and are organized by section: CLI reference, MCP reference, per-provider setup guides (one page per social network), Public API reference (analytics, integrations, posts, providers, uploads, video), installation guides (Docker, Docker Compose, Helm, Dev Container, local development), configuration reference (env vars, R2 storage, OIDC, Chrome extension, Polotno image/video editor), reverse-proxy guides, and a troubleshooting section covering activation/login, billing, channel limits, and self-host-specific gotchas.
