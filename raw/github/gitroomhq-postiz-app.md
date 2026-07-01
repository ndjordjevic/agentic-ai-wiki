# gitroomhq/postiz-app

## Metadata
- Stars: 32528
- Primary language: TypeScript
- Default branch: main
- Latest release: v2.21.10 (2026-06-22)
- License: GNU Affero General Public License v3.0 (AGPL-3.0)
- Homepage: https://postiz.com
- Fetched: 2026-07-01
- Final URL: https://github.com/gitroomhq/postiz-app

## Description
📨 The ultimate agentic social media scheduling tool 🤖

## README
<p align="center">
  <a href="https://postiz.com/" target="_blank">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://github.com/user-attachments/assets/765e9d72-3ee7-4a56-9d59-a2c9befe2311">
    <img alt="Postiz Logo" src="https://github.com/user-attachments/assets/f0d30d70-dddb-4142-8876-e9aa6ed1cb99" width="280"/>
  </picture>
  </a>
</p>

<p align="center">
<a href="https://opensource.org/license/agpl-v3">
  <img src="https://img.shields.io/badge/License-AGPL%203.0-blue.svg" alt="License">
</a>
</p>

<h3 align="center"><strong><a href="https://github.com/gitroomhq/postiz-agent">NEW: check out Postiz agent CLI! perfect for OpenClaw and other agents</a></strong></h3>
<div align="center">
  <strong>
  <h2>Your ultimate AI social media scheduling tool</h2><br />
  <a href="https://postiz.com">Postiz</a>: An alternative to: Buffer.com, Hypefury, Twitter Hunter, etc...<br /><br />
  </strong>
  Postiz offers everything you need to manage your social media posts,<br />build an audience, capture leads, and grow your business.
</div>

<p align="center">
  <br />
  <a href="https://docs.postiz.com" rel="dofollow"><strong>Explore the docs »</strong></a>
  <br />

  <br />
  <a href="https://youtube.com/@postizofficial" rel="dofollow"><strong>Watch the YouTube Tutorials»</strong></a>
  <br />
</p>

<p align="center">
  <a href="https://platform.postiz.com">Register</a>
  ·
  <a href="https://discord.postiz.com">Join Our Discord (devs only)</a>
  ·
  <a href="https://docs.postiz.com/public-api">Public API</a><br />
</p>
<p align="center">
  <a href="https://www.npmjs.com/package/@postiz/node">NodeJS SDK</a>
  ·
  <a href="https://www.npmjs.com/package/n8n-nodes-postiz">N8N custom node</a>
  ·
  <a href="https://apps.make.com/postiz">Make.com integration</a>
</p>

## 🔌 See the leading Postiz features

## ✨ Features

### Our Sponsors

| Sponsor |                                  Logo                                   | Description     |
|---------|:-----------------------------------------------------------------------:|-----------------|
| [Hostinger](https://www.hostinger.com/vps/docker/postiz?ref=postiz) | (logo) | Hostinger is on a mission to make online success possible for anyone – from developers to aspiring bloggers and business owners |
| [Virlo](https://dev.virlo.ai/?ref=postiz) | (logo) | Virlo is the #1 social media trend spotting and all-in-one GTM tool for teams leveraging short-form video |
| [ChatbotX](https://chatbotx.io/?ref=postiz) | (logo) | The ManyChat alternative that you can self-host, white-label, and resell to your clients. Bring your own OpenClaw, Hermes, or Claude agents! |

# Intro

- Schedule all your social media posts (many AI features)
- Measure your work with analytics.
- Collaborate with other team members to exchange or buy posts.
- Invite your team members to collaborate, comment, and schedule posts.
- At the moment, there is no difference between the hosted version and the self-hosted version
- Perfect for automation (API) with platforms like N8N, Make.com, Zapier, etc.

## Tech Stack

- Pnpm workspaces (Monorepo)
- NextJS (React)
- NestJS
- Prisma (Default to PostgreSQL)
- Temporal
- Resend (email notifications)

## Quick Start

To have the project up and running, please follow the [Quick Start Guide](https://docs.postiz.com/quickstart)

## Sponsor Postiz

We now give a few options to Sponsor Postiz:
- Just a donation: You like what we are building, and want to buy us some coffee so we can build faster.
- Main repository: Get your logo with a backlink from the main Postiz repository. Postiz has almost 6m downloads and 20k views per month.

Link: https://opencollective.com/postiz

## Postiz Compliance

- Postiz is an open-source, self-hosted social media scheduling tool that supports platforms like X (formerly Twitter), Bluesky, Mastodon, Discord, and others.
- Postiz hosted service uses official, platform-approved OAuth flows.
- Postiz does not automate or scrape content from social media platforms.
- Postiz does not collect, store, or proxy API keys or access tokens from users.
- Postiz never asks users to paste API keys into our hosted product.
- Postiz users always authenticate directly with the social platform (e.g., X, Discord, etc.), ensuring platform compliance and data privacy.

## License

This repository's source code is available under the [AGPL-3.0 license](LICENSE).

## Top-level structure
- `.claude/` — Claude Code agent config directory
- `.coderabbit.yaml` — CodeRabbit review-bot config
- `.devcontainer/` — VS Code dev container config
- `.dockerignore`, `.env.example`, `.eslintignore`
- `.github/` — GitHub Actions workflows
- `.gitignore`, `.gitmodules`, `.npmrc`, `.prettierignore`, `.prettierrc`
- `CCLA.md`, `ICLA.md` — contributor license agreements
- `CLAUDE.md` — Claude Code agent instructions (present at repo root)
- `CODE_OF_CONDUCT.md`, `CONTRIBUTING.md`, `SECURITY.md`
- `Dockerfile.dev`
- `Jenkins/` — CI pipeline config
- `LICENSE` — AGPL-3.0
- `README.md`
- `apps/` — monorepo apps: `backend/`, `commands/` (CLI), `extension/` (browser extension), `frontend/`, `orchestrator/` (Temporal workflows), `sdk/`
- `docker-compose.dev.yaml`, `docker-compose.yaml`
- `dynamicconfig/` — Temporal dynamic config
- `eslint.config.mjs`, `i18n.json`, `i18n.lock`
- `jest.config.ts`, `jest.preset.js`
- `libraries/` — shared internal packages
- `package.json`, `pnpm-lock.yaml`, `pnpm-workspace.yaml`
- `railway.toml`
- `reports/`
- `sonar-project.properties`
- `tsconfig.base.json`, `tsconfig.json`
- `var/`
- `version.txt`
