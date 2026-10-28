---
type: source
category: "Business, career & learning"
source_url: https://github.com/AienTech/dossier
tags:
  - self-hosted-job-search
  - resume-tailoring
  - cover-letter
  - job-agent
  - claude-mcp-connector
  - fact-guard
  - local-llm
  - nextjs
related:
  - go.aiapply.co
  - santifer-career-ops
  - parakeet-ai.com
product: dossier
detail_level: standard
created: 2026-10-28
updated: 2026-10-28
---

Dossier is a self-hosted, single-user job-search app (AGPL-3.0, TypeScript/Next.js 16, ~2.7k★, v1.9.2) that keeps one career profile on your own PostgreSQL and turns it into tailored resumes and cover letters per posting — with an optional daily **job agent** and a remote **Claude connector** (Streamable HTTP MCP at `/api/mcp`). It matters for this wiki as a privacy-first vertical agent product: bring-your-own model (Ollama / LM Studio / OpenAI-compatible / Anthropic / Mistral), fact-guarded drafts that refuse to invent experience, and MCP tools that search and draft but never send or delete. Contrasts with hosted auto-apply stacks like [[go.aiapply.co]] and coding-agent skill packs like [[santifer-career-ops]].

_All claims below are sourced from ../../raw/github/AienTech-dossier.md unless otherwise noted._

## What it does

You run Dossier on a laptop (Docker Compose) or a small server. One password, one profile, your data in Postgres plus a local data directory. For each application you paste or pick a posting; Dossier extracts requirements, scores fit against the profile, and drafts a tailored resume and cover letter using only profile facts (gaps are shown, not fabricated). You refine in chat, download PDFs, optionally compose an application email, and track status on a board/dashboard. Optional layers: Find jobs (JSearch / Adzuna / German Arbeitsagentur), a daily job agent that scores and can pre-draft for review, Gmail/Calendar, YC/HN startups, and a Claude connector so Claude on your plan can drive search/score/draft through MCP without leaving your install.

## Installation

Needs Docker (Desktop or Engine + Compose) and ~2 GB free memory. Quick local path from the README:

```bash
mkdir ~/dossier && cd ~/dossier
curl -fsSL -o compose.yml https://raw.githubusercontent.com/AienTech/dossier/main/compose.production.yml
echo "POSTGRES_PASSWORD=$(openssl rand -hex 24)" > .env
echo "DOSSIER_SECRET=$(openssl rand -base64 32)" >> .env
docker run --rm -it --platform linux/amd64 ghcr.io/aientech/dossier hash-password
# add DOSSIER_PASSWORD=argon2id:… to .env, then:
docker compose up -d
```

Open `http://localhost:3000`, sign in, set **Settings → AI provider**. Self-host (Ubuntu + Caddy, CapRover, Coolify, Dokploy) and provider/job-source guides live in the project wiki. Dev stack: `docker compose` + `docker/bin/yarn` against Next.js 16 App Router, Prisma 7, PostgreSQL 18 — nothing runs on the host.

## Key features

- **Profile + base resume** — skills, experience, projects, education, publications, references; twelve themes + theme builder; PDF render on the server (Playwright Chromium).
- **Tailored applications** — extract posting → match requirements → resume + cover letter + optional email; refine chat with undo/version history; "Never invent experience" / fact guard by default.
- **Find jobs** — JSearch, Adzuna, or unofficial Bundesagentur für Arbeit; save/dismiss/score; start an application from a posting.
- **Job agent (optional)** — at most one scheduled search/day (caps on scores/drafts); scores new postings; can prepare `origin: AGENT` drafts that stay off the board until Approve; never sends or applies.
- **Claude connector (optional)** — remote MCP server for Claude.ai / Desktop / CLI; tools include `get_profile`, `search_jobs`, `more_jobs`, `get_posting`, `save_job_scores`, `list_applications`, `get_application`, `save_application`, `draft_application`, `check_draft`, `set_application_status`; never sends or deletes.
- **Gmail & Calendar (optional)** — own Google OAuth client; send with PDF attach on confirm; inbox replies classified/drafted by AI; interview sync.
- **Startups** — YC hiring posts + HN "Who is hiring?", ranked to your location/remote prefs.
- **Your data** — export/import JSON, nightly backups, delete-everything; keys encrypted from `DOSSIER_SECRET`.

## Architecture

Next.js App Router UI (`src/app`) over Prisma/`src/lib/*`. AI work is task-shaped (`src/lib/ai/tasks`: extract-posting, match-requirements, tailor-resume, write-cover-letter, score-posting, refine-chat, classify/draft-reply, …) behind provider adapters (`ollama`, `lmstudio`, `openai-compatible`, `anthropic`, `mistral`) with structured outputs and a fact guard. Long runs go through `src/lib/jobs` background jobs with retention tied to Settings. Job search adapters live under `src/lib/job-search`; the agent under `src/lib/agent` (scan → score → optional draft + in-process schedule). The Claude connector (`src/lib/connector` + `src/app/api/mcp`) is Streamable HTTP MCP with Dossier's own OAuth bearer tokens — 404 while the connector is off. Single-instance assumptions: nightly backups, AI job queue, and PDF browser live in-process.

## Example usage

After Compose is up and an AI provider is configured: open **New application**, paste a posting (or start from Find jobs), review the match gaps, generate documents, refine in chat, download PDFs. Enable **Settings → Job agent** for a daily scored shortlist; enable **Claude connector** and point Claude at your `/api/mcp` URL so Claude can `search_jobs` / `save_application` against the same profile. Live provider tests: `AI_LIVE=ollama` (or `mistral` / `lmstudio`) Vitest suites inside the app container.

## Maintenance status

Active: latest release **v1.9.2** (2026-10-27), default branch `main`, ~2,671 stars / 559 forks, primary language TypeScript, license **AGPL-3.0**. Images publish to `ghcr.io/aientech/dossier`; CI runs lint, typecheck, Vitest (+ Postgres), and Playwright e2e. Homepage: https://dossier.aien.me. Known limits: desktop browser only, single user, English UI, one app instance per database.
