# AienTech/dossier

## Metadata
- Stars: 2671
- Forks: 559
- Primary language: TypeScript
- Default branch: main
- Latest release: v1.9.2 (2026-10-27)
- License: GNU Affero General Public License v3.0 (AGPL-3.0)
- Homepage: https://dossier.aien.me
- Fetched: 2026-10-28
- Final URL: https://github.com/AienTech/dossier

## Description
A self-hosted job search app that writes tailored resumes and cover letters from your profile.

## README
<p align="center">
  <img src="src/app/icon.svg" alt="" width="80" height="80">
</p>

<h1 align="center">Dossier</h1>

<p align="center">
  Your job search, on your own server: one profile, a tailored resume and cover letter for every job, and every application tracked from draft to offer.
</p>

<p align="center">
  <a href="https://github.com/AienTech/dossier/releases/latest"><img alt="Latest release" src="https://img.shields.io/github/v/release/AienTech/dossier?label=release"></a>
  <a href="https://github.com/AienTech/dossier/actions/workflows/ci.yml"><img alt="CI" src="https://github.com/AienTech/dossier/actions/workflows/ci.yml/badge.svg"></a>
  <a href="LICENSE"><img alt="License: AGPL-3.0" src="https://img.shields.io/badge/license-AGPL--3.0-blue"></a>
  <a href="https://github.com/AienTech/dossier/pkgs/container/dossier"><img alt="Docker image: ghcr.io/aientech/dossier" src="https://img.shields.io/badge/image-ghcr.io%2Faientech%2Fdossier-2496ED?logo=docker&logoColor=white"></a>
  <img alt="Next.js 16" src="https://img.shields.io/badge/Next.js-16-000000?logo=nextdotjs">
  <img alt="PostgreSQL 18" src="https://img.shields.io/badge/PostgreSQL-18-4169E1?logo=postgresql&logoColor=white">
</p>

Dossier keeps your career history in one profile and turns it into a clean resume. For every job you apply to, it reads the posting, shows how you match, and drafts a tailored resume and cover letter that only use facts from your profile. You refine them in a chat, download them as PDFs and track each application from draft to offer.

It's for one person on a small server: one password, your data in your own PostgreSQL database, and an AI model of your choice. That can be a local model through Ollama or LM Studio, so your profile and documents stay on your own hardware, or a hosted one (any OpenAI-compatible API, Anthropic or Mistral), which then receives what it writes from. [Privacy](https://github.com/AienTech/dossier/wiki/Privacy) says what goes where.

**Get started:** [run it on your computer](#run-it-on-your-computer) in a few minutes, or [self-host it](#self-hosting) on a server. The [installation guide](https://github.com/AienTech/dossier/wiki) covers every way: Docker with or without Compose, Node.js, a plain Ubuntu server, CapRover, Coolify and Dokploy.

## Demo

![Dossier in use: the dashboard, dragging a card on the board, a new application from a pasted posting, refining the tailored resume in the chat, the cover letter, and switching resume themes](.github/images/demo.gif)

<sub>Recorded with the demo data (Jane Doe is made up) and a stand-in AI server that answers at once, played at 1.2× speed. With a real model, reading a posting and writing the documents takes from a few seconds to a few minutes.</sub>

## Features

- **Profile:** basics, skills and languages, experience, projects, education, publications and references, in the order you choose, with a strength meter that counts only what a profile needs. Projects (side, open-source, course or thesis work) show what you can do where your job titles don't yet. Publications are cited in your own style, with bold and italics, and go on resumes word for word. Start it from an existing resume (PDF, Word or Markdown) if you like.
- **Base resume:** twelve themes and a theme builder, previewed live and printed to PDF on the server. Duplicate themes, or share them as files.
- **Find jobs:** search postings near your city, or anywhere you choose, through JSearch (LinkedIn, Indeed and more) or Adzuna. Save the good ones, dismiss the rest, score any of them against your profile, and start an application from a posting with one click.
- **Startups:** startups that are hiring, from YC startups' job posts and Hacker News' monthly “Who is hiring?” thread, kept to the ones that hire where you live or remotely from your country and ranked against your profile, with the address each one publishes for applications. Dossier reads their sites politely and follows their robots.txt. Start an application to one with a click; you decide whom to write to.
- **Job agent (optional):** once a day it runs one search for you, skips what you've seen, scores the new postings against your profile and keeps the best on the Agent screen, with its reasons. It can prepare tailored drafts too, which wait for your review. It never sends or applies.
- **New application:** paste a posting; Dossier pulls out the details and requirements, matches them against your profile, and writes a tailored resume and cover letter in the tone you pick.
- **Never invents experience:** drafts only use facts from your profile. What the posting asks for and your profile doesn't have is shown as a gap, not made up.
- **Refine:** ask for changes in a chat, edit or regenerate any part (every part of the cover letter too: sender, date, recipient, greeting and sign-off, written in the letter's language), undo AI changes or go back to any earlier version, keep private notes.
- **Send:** an email to go with each application, to whoever the posting says to send it to, ready to copy or open in your mail app, with the resume and cover letter PDFs to attach. Edit, rewrite or refine it like the documents.
- **Claude connector (optional):** use Dossier from Claude, on claude.ai, in the Desktop and mobile apps or in Claude's command-line app, on your own Claude plan. Claude can search for jobs, score them against your profile, read your profile and applications, and save the resume and cover letter it writes as a Draft, checked like Dossier's own. It never sends or deletes anything. Without an AI model of Dossier's own, **Write it with Claude** hands a posting to a new Claude chat. Turn it on in Settings → Claude connector (see [Connecting Claude](https://github.com/AienTech/dossier/wiki/Connecting-Claude)).
- **Gmail and Calendar (optional):** connect your Google account to send an application from your own address with its PDFs attached, see employers' replies next to each application, have the AI read what they ask and draft your answer from your profile, offer interview times you're free, and see your month and the week ahead on the dashboard, with interviews kept in step with Google Calendar both ways. Nothing is sent without your confirmation. Set it up by entering your Google OAuth client in Settings → Google, or with `DOSSIER_GOOGLE_CLIENT_ID` and `DOSSIER_GOOGLE_CLIENT_SECRET` (see [Connecting Gmail and Calendar](https://github.com/AienTech/dossier/wiki/Connecting-Gmail-and-Calendar)).
- **Track:** a board and a table of every application, and a dashboard with your funnel (last 30 days, 90 days or all time), a week-by-week chart, what's worth a look next, upcoming interviews included, and a calendar.
- **Your data:** export and import everything as one file, nightly backups, and Delete everything.

## Screenshots

![The dashboard: your funnel, a week-by-week chart and what's worth a look next](.github/images/dashboard.png)

<table>
  <tr>
    <td width="50%"><img src=".github/images/application.png" alt="An application with its tailored resume and the chat that refines it"><br>An application: the tailored resume, and a chat to refine it</td>
    <td width="50%"><img src=".github/images/new-application.png" alt="A new application, showing how the profile matches the posting's requirements"><br>A new application: how you match the posting</td>
  </tr>
  <tr>
    <td><img src=".github/images/applications.png" alt="The applications board, with columns from draft to offer"><br>Every application on a board, from draft to offer</td>
    <td><img src=".github/images/find-jobs.png" alt="Find jobs: postings near the profile's city, with one open"><br>Find jobs and start an application from a posting</td>
  </tr>
  <tr>
    <td><img src=".github/images/resume.png" alt="The base resume next to its themes"><br>The base resume, with twelve themes and a theme builder</td>
    <td><img src=".github/images/profile.png" alt="The profile editor, with its sections and strength meter"><br>One profile that every resume and letter comes from</td>
  </tr>
  <tr>
    <td><img src=".github/images/inbox.png" alt="The inbox: employers' replies from Gmail, what each one asks, and mail to link to an application"><br>Replies from Gmail, read by the AI, with answers it drafts</td>
    <td><img src=".github/images/calendar.png" alt="The dashboard on a wide window, with the calendar beside the cards: the month, and the week ahead with an interview among the Google Calendar's events"><br>Your interviews and Google Calendar on the dashboard, kept in step</td>
  </tr>
</table>

<sub>The screenshots show the demo data: Jane Doe is made up.</sub>

## Run it on your computer

All you need is [Docker Desktop](https://docs.docker.com/desktop/) on macOS or Windows, or Docker Engine with its Compose plugin on Linux, and about 2 GB of free memory. Run the commands in a terminal: macOS's Terminal, Linux, or WSL on Windows.

**1. Fetch the Compose file** into a folder of its own, and make the secrets Dossier needs:

```bash
mkdir ~/dossier && cd ~/dossier
curl -fsSL -o compose.yml https://raw.githubusercontent.com/AienTech/dossier/main/compose.production.yml
echo "POSTGRES_PASSWORD=$(openssl rand -hex 24)" > .env
echo "DOSSIER_SECRET=$(openssl rand -base64 32)" >> .env
```

On an Apple Silicon Mac, also run `printf 'services:\n  app:\n    platform: linux/amd64\n' > compose.override.yml`: the image is built for Intel and AMD processors, and Docker Desktop runs it under emulation.

**2. Choose your password.** This asks for it twice and prints a hash of it, one line that starts with `argon2id:`:

```bash
docker run --rm -it --platform linux/amd64 ghcr.io/aientech/dossier hash-password
```

Add that line to `.env` as `DOSSIER_PASSWORD=argon2id:…`, with any text editor. Dossier only keeps the hash, never the password.

**3. Start it:**

```bash
docker compose up -d
```

The first start downloads the image (about 1.7 GB) and sets up the database. Open [http://localhost:3000](http://localhost:3000), sign in with your password, and pick an AI model in **Settings → AI provider** (see [Choosing an AI provider](https://github.com/AienTech/dossier/wiki/Choosing-an-AI-provider)).

`docker compose stop` stops it and `docker compose start` starts it again, with your data kept. It's only reachable from your own computer. The [installation guide's Docker Compose page](https://github.com/AienTech/dossier/wiki/Run-locally-with-Docker-Compose) has more: another port, your time zone, upgrades and removing it.

## Self-hosting

To put Dossier on a server, on your own domain with HTTPS, follow the [installation guide](https://github.com/AienTech/dossier/wiki#self-host-on-a-server): a plain Ubuntu server with Docker Compose and Caddy (or Node.js, without Docker), CapRover, Coolify or Dokploy. Give the server at least 2 vCPUs and 2 GB of memory (see [Performance and sizing](#performance-and-sizing)).

## Documentation

The [wiki](https://github.com/AienTech/dossier/wiki) has what comes after installing:

- [Choosing an AI provider](https://github.com/AienTech/dossier/wiki/Choosing-an-AI-provider): a hosted model, or a local one with Ollama or LM Studio.
- [Choosing a job source](https://github.com/AienTech/dossier/wiki/Choosing-a-job-source): JSearch or Adzuna (and an unofficial one for Germany), and the job agent.
- [Connecting Gmail and Calendar](https://github.com/AienTech/dossier/wiki/Connecting-Gmail-and-Calendar): your own Google OAuth client, step by step.
- [Connecting Claude](https://github.com/AienTech/dossier/wiki/Connecting-Claude): the Claude connector, in Claude's apps and on the command line.
- [Backups and restore](https://github.com/AienTech/dossier/wiki/Backups-and-restore): exports, nightly backups and database dumps.
- <a name="upgrading"></a>[Upgrading](https://github.com/AienTech/dossier/wiki/Upgrading) to a new version.
- [Troubleshooting](https://github.com/AienTech/dossier/wiki/Troubleshooting): what the common errors mean, and what to do about them.
- [Privacy](https://github.com/AienTech/dossier/wiki/Privacy): what stays on your server and what leaves it. [PRIVACY.md](PRIVACY.md) has the details.
- [Environment variables](https://github.com/AienTech/dossier/wiki/Environment-variables): every setting the server reads.

## Known limitations

- **Desktop only:** made for a laptop or desktop browser, not for phones.
- **Single user:** one password and one profile; there are no accounts.
- **English interface:** the app itself is in English. Documents can be written in other languages; in the 21 built-in ones, their headings, dates and language levels are in that language too, and in one added with **Other language…** those stay in English.
- **One instance:** run a single copy of the app per database. The nightly backups, the AI job queue and the PDF browser live inside the app's process.

## Performance and sizing

Measured on 28 September 2026 with the production build in a container limited to 2 vCPUs and 1 GB:

- **PDFs:** the base resume renders in about 0.25 s, or 1 s when Chromium has to start first (it closes after five idle minutes). Two render at a time and the rest queue: six requested at once are done in 1.4 s. Dossier used at most about 520 MB, Chromium included, so give the container at least 768 MB.
- **Screens:** with ten times the demo data (90 applications), the dashboard and the applications list answer in 20–90 ms, and every query takes under a millisecond. With 900 applications they take up to about 0.2 s, mostly rendering; the tables are indexed for the queries they get.
- **Interactions** (changing a status, moving a card, switching tabs, opening an editor, typing, picking a theme) respond within 32 ms, and within about 100 ms on a CPU four times slower.

## Security

What protects your data, how to run Dossier safely and how to report a problem: see [SECURITY.md](SECURITY.md).

## Development

Working on Dossier itself: see [DEVELOPMENT.md](DEVELOPMENT.md).

## License

Dossier is free software under the [GNU Affero General Public License v3.0](LICENSE). You may use, change and share it; if you run a changed version for others over a network, you must offer them its source code.


## Docs

### DEVELOPMENT.md
# Developing Dossier

Next.js 16 (App Router) + Prisma 7 + PostgreSQL 18, run with Docker Compose and Yarn 4. Nothing runs on the host: every command goes through the containers. For installing and running Dossier, see the [README](README.md); for how it's secured, [SECURITY.md](SECURITY.md).

## Getting started

```bash
cp .env.example .env
docker compose build
docker/bin/yarn hash-password   # set DOSSIER_PASSWORD in .env to what it prints
# set DOSSIER_SECRET (openssl rand -base64 32) in .env
docker compose up
```

Open [http://localhost:3000](http://localhost:3000). Source is bind-mounted, so edits hot-reload.

`.env.example` documents every variable. The server refuses to start while `DOSSIER_PASSWORD` or `DOSSIER_SECRET` is missing, `DOSSIER_PASSWORD` isn't a password hash, or the secret is shorter than 32 characters, and logs which variable to fix.
Server code reads configuration from the validated `env` object instead of `process.env`:

```ts
import { env } from "@/lib/env";
```

On every start the `app` container runs `prisma generate`, `prisma migrate deploy`, then `next dev`.
Postgres is also exposed on `localhost:5432` for host tools, using `DATABASE_URL` from `.env`.

## Yarn

Dependencies live in the container (a named `node_modules` volume), not on the host.
Run yarn through `docker/bin/yarn`, which uses the running `app` container or, if it's stopped, a one-off one:

```bash
docker/bin/yarn add <package>
docker/bin/yarn install   # after pulling changes to yarn.lock
docker/bin/yarn lint
```

## Database

Define models in `prisma/schema.prisma`, then create and apply a migration:

```bash
docker/bin/yarn prisma migrate dev --name <migration-name>
docker compose restart app
```

The restart regenerates the Prisma Client and picks it up; since Prisma 7, `migrate dev` no longer runs `prisma generate` on its own.

To browse and edit rows in Prisma Studio, start it on demand (plain `docker compose up` leaves it off) and open [http://localhost:5555](http://localhost:5555):

```bash
docker compose up -d studio
docker compose stop studio   # when you're done
```

Query the database from server code with the shared client:

```ts
import { prisma } from "@/lib/prisma";
```

JSON columns (document units, the posting's extracted details, the match, chat edits) are validated with the zod schemas in `src/lib/application-data.ts`.
Change an application's status only through `setStatus` in `src/lib/status-actions.ts` (or `changeStatus()` in client code, which adds the Undo toast), so the funnel figures stay consistent.

### Seed data

Each start runs `prisma db seed`, which creates the six built-in themes, an empty profile and default settings. It never overwrites your profile or settings. To load the prototype's sample data (Jane Doe and nine applications):

```bash
docker/bin/yarn prisma db seed -- --demo           # refuses if you already have a profile or applications
docker/bin/yarn prisma db seed -- --demo --reset   # deletes your profile and applications first
```

## Mutations and private routes

Every mutation goes through one of two helpers. Both check the session first, keep unexpected errors out of responses (they're logged on the server without the data involved), and let `redirect()` and `notFound()` work as usual.

**Server Actions** are the default. Define them with `action(schema, handler)` in a `"use server"` file: the input is validated with zod, and the action returns `{ ok: true, data, toast? } | { ok: false, error, fieldErrors? }`, with messages written for the user.

```ts
// src/app/(app)/settings/actions.ts
"use server";

import { z } from "zod";

import { action, ActionError } from "@/lib/action";
import { prisma } from "@/lib/prisma";

export const renameTheme = action(
  z.object({ id: z.string(), name: z.string().trim().min(1, "Give the theme a name.") }),
  async ({ id, name }, { toast }) => {
    const theme = await prisma.theme.findUnique({ where: { id } });
    if (!theme) throw new ActionError("That theme no longer exists."); // shown to the user
    await prisma.theme.update({ where: { id }, data: { name } });
    toast(`Renamed to “${name}”.`);
    return { id, name };
  },
);
```

On the client, `toastResult()` from `@/components/toast` shows the action's `toast` or its error, and `toast("…")` shows any other message:

```tsx
const result = toastResult(await renameTheme({ id, name }));
```

Next.js already refuses Server Actions whose `Origin` doesn't match the host (or `X-Forwarded-Host` behind a proxy), so keep `experimental.serverActions.allowedOrigins` empty unless the proxy rewrites the host. Action bodies are limited to 1 MB, so large uploads such as imports go through a route handler.

**Route handlers** are for responses a Server Action can't give: files (PDFs, exports), uploads and progress streams. Wrap them in `route()`, which also refuses cross-origin requests (403) and signed-out ones (401), and marks responses `Cache-Control: private, no-store` unless the handler sets its own.

```ts
// src/app/api/pdf/[id]/route.ts
import { route } from "@/lib/route";

export const GET = route<RouteContext<"/api/pdf/[id]">>(async (request, { params }) => {
  const { id } = await params;
  const pdf = await renderPdf(id);
  return new Response(pdf, { headers: { "content-type": "application/pdf" } });
});
```

Both get the session from `getSession()` in `src/lib/auth/session.ts` (see [Sign-in](#sign-in)).

## Sign-in

Dossier has one user and no accounts: you sign in with the password that `DOSSIER_PASSWORD` is a hash of. The session is an encrypted token (JWE, keyed from `DOSSIER_SECRET`) in an HttpOnly, SameSite=Lax cookie, so nothing is stored on the server. It lasts until the browser closes, but at most 24 hours; with "Keep me signed in", 30 days.

The hash is argon2id with OWASP's settings (19 MiB, 2 passes, 1 lane) from Node's own `crypto.argon2`, made by `docker/bin/yarn hash-password` (`scripts/hash-password.ts`, which the image bundles as the `hash-password` command). Checking a password against it is in `src/lib/auth/password-hash.ts`, and `src/lib/env.ts` refuses anything that isn't a hash. It's written as `argon2id:m=19456,t=2,p=1:<salt>:<hash>` rather than the usual `$argon2id$v=19$…`, because Next.js and Docker Compose expand `$` in `.env` files, even inside quotes. The settings are part of each hash, so stronger ones can come later without breaking existing hashes.

Sign out from the sidebar ends the session in that browser. To sign out everywhere, set `DOSSIER_PASSWORD` to a new hash (even of the same password, since each has its own salt) or rotate `DOSSIER_SECRET` and restart: every session carries a fingerprint of the password and is encrypted with a key from the secret, so all existing sessions stop working. Rotating the secret also means API keys saved in Settings have to be entered again, since they're encrypted with it too.

In server code, `getSession()` returns the session or null, and `verifySession()` (for pages and layouts) sends the visitor to `/login` when there is none. `action()` and `route()` already check it.

Failed sign-ins are rate-limited in Postgres: after 5 failures within a minute from one IP, attempts are refused for 30 seconds, then 60, 120 and so on up to 15 minutes. The IP is the last `X-Forwarded-For` entry, which is the real client behind a reverse proxy but can be faked when the app is exposed directly, so 30 failures within 10 minutes from all IPs together also trigger the backoff. If you lock yourself out while developing, clear the counters with `docker compose exec db psql -U postgres -d dossier -c 'DELETE FROM "LoginThrottle"'`.

## AI provider

Dossier reads job postings and writes drafts with the model you choose in Settings → AI provider: a local model through Ollama or llama.cpp, LM Studio, any OpenAI-compatible server, Anthropic or Mistral. Until you save a choice there, the `DOSSIER_AI_*` variables decide (see `.env.example`). API keys are stored encrypted with a key derived from `DOSSIER_SECRET`, and never sent back to the browser.

Long AI tasks run as background jobs (`src/lib/jobs`): the page follows their named steps as they happen and picks them up again after a reload. A job's input and result hold personal data, so they don't last: a job that works on an application names it (`startJob(…, { applicationId })`) and is deleted with it, and finished jobs are deleted once they're older than **Keep task data for** in Settings → Your data (`src/lib/jobs/retention.ts`). Keep nothing in a job that has to outlast that; Undo on a toast and a page reattaching after a reload are fine. The prompts live in `src/lib/ai/tasks`; in strict mode ("Never invent experience", on by default) a fact guard flags names and numbers that aren't in the profile or the posting.

To try the AI features without a hosted provider, run a small model in Docker:

```bash
docker compose up -d ollama
docker compose exec ollama ollama pull qwen2.5:3b   # about 2 GB
```

Then pick Local model in Settings with the address `http://ollama:11434` (inside Docker, `localhost` is the app's own container). The Ollama image takes about 9 GB of disk, and a 3B model about 3 GB of memory while it runs; `docker compose stop ollama` when you're done.

The tests use a mock provider. To check the providers and prompts against real models, run the live tests, which are skipped otherwise:

```bash
docker compose exec -e AI_LIVE=ollama app yarn vitest run src/lib/ai/providers.live.test.ts src/lib/ai/tasks/tasks.live.test.ts
```

`AI_LIVE=mistral` checks Mistral instead, with the key saved in Settings → AI provider while Mistral is chosen there, or with `DOSSIER_AI_KEY` (and `DOSSIER_AI_MODEL`) passed with `-e`.

`AI_LIVE=lmstudio` checks LM Studio, with the model saved in Settings while LM Studio is chosen there, or with `-e DOSSIER_AI_MODEL=…` (and `DOSSIER_AI_URL`, by default `http://host.docker.internal:1234`). A model that isn't loaded gets loaded and stays loaded until you eject it.

## Job search

Find jobs (`/jobs`) searches the job source chosen in Settings → Job search: JSearch, Adzuna or the Bundesagentur für Arbeit. Until a choice is saved, `DOSSIER_JOBS_SOURCE` and the key variables decide (see `.env.example`). In the code, "job" already means a background task (`Job`, `src/lib/jobs`), so a job ad is a "posting", and job search lives in `src/lib/job-search`:

- `search.ts` and `sources.ts`: the query and posting shapes every source maps to, the URL format, and what each source covers. Shared with the browser.
- One adapter per source (`jsearch.ts`, `adzuna.ts`, `arbeitsagentur.ts`), behind `index.ts`, which checks the country, caches answers in memory for 30 minutes and logs a source that changed or isn't answering, without the search. Failures are a `JobSearchError` with a message for the screen.
- `config.ts`: which source and key are in effect. Job source keys are encrypted like the AI key, each kind of secret under its own derived key (`src/lib/secrets.ts`).
- `src/lib/postings.ts`: the `Posting` table holds what the user saved, dismissed or started an application from. `src/lib/posting-searches.ts`: every search, kept with what it found (`PostingSearch`) until the user removes it, so opening one again asks the source nothing.

The tests use answers in each source's shape (`src/test/job-search-fixtures.ts`). The live tests check the real services, and are skipped otherwise. JSearch and Adzuna spend searches from your plan; the Arbeitsagentur is free:

```bash
docker compose exec -e JOBS_LIVE=jsearch -e JSEARCH_TEST_KEY=… app yarn vitest run src/lib/job-search/jsearch.live.test.ts
docker compose exec -e JOBS_LIVE=arbeitsagentur app yarn vitest run src/lib/job-search/sources.live.test.ts
docker compose exec -e JOBS_LIVE=adzuna -e ADZUNA_TEST_APP_ID=… -e ADZUNA_TEST_KEY=… app yarn vitest run src/lib/job-search/sources.live.test.ts
```

## Your data

Settings → Your data exports everything (profile, custom themes, settings, applications with their history, documents, chat and notes, and the postings kept from Find jobs) as one JSON file, and imports such a file to restore it. An import replaces all data in one transaction, after writing a backup of the current data to `DOSSIER_DATA_DIR/backups` (default `/data`; `./data` in development, which git ignores). "Download all PDFs" zips every tailored document there too, in `downloads`, and removes the zip once it's downloaded.

With "Nightly backups" on (the default), the app writes the same export to `backups` every night at 03:00 server time and deletes backups older than `DOSSIER_BACKUP_RETENTION_DAYS` (14 by default). The timer runs inside the app process, so run a single instance of the app. These are the app's own backups: back up the PostgreSQL database itself too, the way your host does it (for example `pg_dump` on a schedule).

### Import size limit

Import files are capped at 10 MB, roughly 500 applications. The limit comes from Next.js, which buffers request bodies up to [`experimental.proxyClientMaxBodySize`](https://nextjs.org/docs/app/api-reference/config/next-config-js/proxyClientMaxBodySize) (10 MB by default) because `src/proxy.ts` runs on every request; larger bodies are cut off, so the app refuses them up front. To accept bigger files, raise that option in `next.config.ts` and `IMPORT_MAX_BYTES` in `src/lib/import-limits.ts`. Behind a reverse proxy, its own limit applies as well: with nginx, raise `client_max_body_size` (see [Troubleshooting](https://github.com/AienTech/dossier/wiki/Troubleshooting) in the wiki).

## Job agent

The job agent (`src/lib/agent`, the `/agent` screen and Settings → Job agent) runs one saved search a day, scores what's new and can prepare drafts:

- **`agent-scan`** (`run.ts`, defined in `jobs.ts` with the key `agent`): one run. It asks the source for the first page only, drops what Find jobs has saved, dismissed or applied for and what the agent has seen (`newPostings()`, by source and id or by `agentDedupeKey()`, a hash of the link without tracking parameters, else of company, title and place), scores the newest of the rest with `score-posting` and keeps each as an `AgentCandidate`.
- **`agent-draft`** (`draft.ts`, keyed `agent-candidate:<id>`): one draft. The candidate is claimed (SCORED → DRAFTING → DRAFTED) so nothing makes two, and the documents are written by `createApplicationFromDocuments()` in `src/lib/application-create.ts`, which New application uses too. The draft is `origin: AGENT` with `awaitingReview` set, which keeps it off Applications, the board, the dashboard, the inbox and Find jobs until Approve.
- **Limits** (`runs.ts`): runs are recorded in the `agentRuns` setting, not as Job rows, which the task-data sweep deletes. At most 3 runs in 24 hours, Run now at most an hour after the last run, and the caps `agentMaxScores` and `agentMaxDrafts` in Settings.
- **Schedule** (`schedule.ts`): a timer in the process, like the nightly backups, that checks every 15 minutes and starts the day's run after `agentHour` in `lastKnownTimeZone()`. It only works with one instance. At startup, candidates left DRAFTING go back to SCORED.

The end-to-end spec `e2e/agent.spec.ts` runs it against the fake JSearch and the fake AI, which scores by title (`posting_score` in `e2e/fake-ai.mts`).

## Usage ping

The usage ping is opt-in. A production server asks once after sign-in (`src/app/(app)/usage-ping-dialog.tsx`, shown by the signed-in layout while nobody has answered and `DOSSIER_TELEMETRY` isn't set) and sends nothing before a yes. After one, on each day someone signed in opens a page, it sends `https://telemetry.dossier.aien.me/ping` the install's random ID and the version, once (`src/lib/usage-ping.ts`, called with `after()` from the signed-in layout). `DOSSIER_TELEMETRY=on` or `off` answers in advance and wins while it's set.

The answer, when it was given and the version of the question's text are the settings `usagePingChoice`, `usagePingChoiceAt` and `usagePingChoiceText`; the ID and the day of the last ping are `usagePingId` and `usagePingDay`. Exports leave them all out and imports keep them (`INSTALL_SETTINGS` in `src/lib/data-export.ts`). A no deletes the ID. When the question's text changes, raise `USAGE_PING_TEXT_VERSION`, and everyone is asked again. Development servers and tests never ask or send it (`NODE_ENV` isn't `production`). The end-to-end run is a production build: `resetData()` answers no, `e2e/usage-ping.spec.ts` asks, and a yes goes to the fake job sources (`DOSSIER_USAGE_PING_TEST_URL`), never the project.

The receiving end is a small service on the project's own server that isn't published with the app. Change what the ping sends only together with it, the wiki's [Privacy](https://github.com/AienTech/dossier/wiki/Privacy) page and Settings → About.

## Tests and checks

Tests use [Vitest](https://vitest.dev) and run inside the container like everything else:

```bash
docker/bin/yarn test          # run all tests once
docker/bin/yarn test:watch    # re-run tests on change
docker/bin/yarn test:coverage # run once with coverage (report in coverage/index.html)
docker/bin/yarn lint
docker/bin/yarn typecheck     # generates Next.js route types, then runs tsc
```

Put tests next to the code they cover. `*.test.ts` files run in Node (server code, pure logic);
`*.test.tsx` files run in jsdom with [Testing Library](https://testing-library.com) and its `jest-dom` matchers (components and hooks).
`*.db.test.ts` files run against a real Postgres database: `dossier_test` on the same server (or `TEST_DATABASE_URL`), which is created and migrated at the start of each run, and which each test empties with `resetDatabase()` from `src/test/db.ts`.
They refuse to run against a database whose name doesn't end in `_test`, so your development data is never touched.

GitHub Actions (`.github/workflows/ci.yml`) runs lint, type-check and tests with coverage, with a Postgres service for the database tests, on every pull request and push to `main`, and shows the coverage in the job summary. A newer push to the same branch or pull request cancels the run it replaces. On `main`, a pull request's merge commit isn't checked a second time when it holds exactly the code its pull request's run checked (the branch was up to date with `main`); every other push to `main` is. The coverage thresholds in `vitest.config.mts` ratchet: they sit a few points below the coverage when they were set, and CI fails if coverage drops below them. Raise them when you add tests.

### End-to-end tests

[Playwright](https://playwright.dev) tests in `e2e/` click through the main flows in headless Chromium: signing in, the profile, the theme builder and PDFs, finding a job and applying from it, a new application, refining and undoing, the application email, the board and table, the dashboard, and export, delete and import. `e2e/accessibility.spec.ts` runs [axe](https://github.com/dequelabs/axe-core) on every screen and its open menus and dialogs (no serious or critical WCAG 2.2 AA violations allowed) and checks where keyboard focus goes. They run against a production build, on the standalone server the image uses, so build first:

```bash
docker/bin/yarn build && docker/bin/yarn test:e2e
```

The run starts its own server on port 3100 with a separate `dossier_e2e` database (created and migrated on the way, reset to the demo data before the specs that change data), a fake OpenAI-compatible server on port 3999 (`e2e/fake-ai.mts`) that answers each AI task with plausible output, fake job sources on port 3998 (`e2e/fake-jobs.mts`), which the app reaches through `DOSSIER_JOBS_TEST_BASE_URL`, a variable for the tests only, and a fake Google on port 3997 (`e2e/fake-google.mts`) for sign-in, Gmail and Calendar (`DOSSIER_GOOGLE_TEST_BASE_URL`), which only comes into play once a spec enters an OAuth client in Settings → Google. The daily update check asks the same fake instead of GitHub (`DOSSIER_UPDATES_TEST_BASE_URL`), which says no release is out, so a spec can store the latest release itself. Your development server and data are never touched: the tests refuse any database whose name doesn't end in `_e2e`. CI runs them in a job of their own and keeps the report of a failed run as an artifact.

## The production image

The `Dockerfile`'s last stage is the production image (the `dev` stage is what Compose runs here). It holds the standalone Next.js server, Playwright's Chromium for PDFs, and Prisma's CLI for migrations, runs as `node`, and starts with `docker/start.sh`: `prisma migrate deploy`, the seed (compiled with esbuild at build time), then the server. To build and try it next to the development stack:

```bash
docker build -t dossier:local .
DOSSIER_IMAGE=dossier:local DOSSIER_PORT=3300 docker compose -f compose.production.yml -p dossier-local up -d
```

CI pushes an image for every commit on `main` to `ghcr.io/<owner>/<repository>:<sha>` (lower case), once the checks and the end-to-end tests pass, on `main` or in the commit's pull request. A version tag (`v1.0.0`) then tags that commit's image with the version and `latest`.

## The website

`site/` is the project's website, plain HTML, CSS and a little JavaScript. `site/build.sh` puts it together in `_site/` with the README's screenshots (`.github/images/`), the app's icons and three of its fonts, so there's one copy of each. To look at it, serve `_site/` with any static server, for example `docker run --rm -p 8080:80 -v "$PWD/_site:/usr/share/nginx/html:ro" nginx:alpine`, then open http://localhost:8080. The public repository's Pages workflow publishes it when any of those change on `main`. When the README's screenshots change, the site's change with them.

## Reset

```bash
docker compose down -v   # stops everything and deletes the database and node_modules volumes
```


### SECURITY.md
# Security

Dossier is a single-user app you run on your own server. It holds your career history, your job applications and, if you use a hosted model, an AI provider's API key. This page covers what protects that data, what it expects from your setup, and how to report a problem. What Dossier keeps, for how long and who receives what is in [PRIVACY.md](PRIVACY.md).

## Reporting a vulnerability

Please report it privately through GitHub: on the repository's **Security** tab, choose **Report a vulnerability**. Don't open a public issue for it.

## What Dossier does

- **Sign-in.** One password, kept only as an argon2id hash in `DOSSIER_PASSWORD`, so the environment doesn't reveal it; the server won't start with the password itself there. The session is an encrypted, HttpOnly, SameSite=Lax cookie, marked Secure over HTTPS. Failed sign-ins are rate-limited per IP and overall. See [Sign-in](DEVELOPMENT.md#sign-in).
- **Every request checks the session.** The proxy only does a quick check before a page renders, so each page, Server Action and route handler checks the session again next to the data. Server Actions go through `action()`, route handlers through `route()`, and a test (`src/lib/session-audit.test.ts`) fails when one doesn't. The only exceptions are signing in and signing out.
- **Cross-site requests.** Next.js refuses Server Actions from another origin, and `route()` does the same for route handlers.
- **Content-Security-Policy.** Every page gets a policy with a fresh nonce: scripts run only when they carry it, nothing loads from other hosts, and no other site may frame Dossier. `next.config.ts` adds `X-Content-Type-Options`, `X-Frame-Options`, `Referrer-Policy`, `Cross-Origin-Opener-Policy` and `Permissions-Policy` to every response.
- **API keys.** Stored encrypted with a key derived from `DOSSIER_SECRET`, never sent to the browser, never logged. The AI provider's key and the job sources' keys each have their own derived key, and each job source's key only goes to that source. The AI server's address is yours to set, so when a request carries a key, Dossier doesn't follow a redirect to another host.
- **Job sources.** Find jobs is off until a source is chosen. Searches go from the server to that source's fixed address only, with a time and size limit; the browser never talks to a job source. A link in a result is kept only when it's `http(s)`, and postings sent back from the browser are checked the same way. Fetching the rest of a posting goes through the same guarded fetcher as Fetch, so it never reaches the server's own network.
- **Google.** Gmail and Calendar are off until you enter your own OAuth client and connect. Signing in is OAuth's authorization code flow with a `state` signed by a key derived from `DOSSIER_SECRET`, valid for 10 minutes, and the callback needs your session too. The refresh token and the client's secret are stored encrypted, each with its own derived key, and never sent to the browser or logged; access tokens stay in the server's memory. Dossier asks only for the permissions of the features you choose (sending, reading, free/busy and events), and every send needs your confirmation.
- **Errors.** Unexpected errors are logged on the server without the data involved; the browser only gets a generic message.

## AI and untrusted text

A job posting, or a reply from Gmail, is text someone else wrote, and it goes into prompts. It could try to steer the model ("ignore your instructions and…"). What limits the damage:

- The model has no tools: it can't read your other data, browse or change anything. It only returns text.
- What it returns is shown as plain text, never as HTML, and checked against a schema before it's saved.
- The fact guard flags claims in a draft that your profile doesn't back up.
- You read every document before you send it, and a drafted answer to a mail only goes out when you confirm it.
- Reading a mail only suggests a status for its application, which you take up or not.

So the worst a hostile posting or mail can do is get odd wording into its own draft, or suggest the wrong status.

## Running it safely

- **Use HTTPS.** Put Dossier behind a reverse proxy that ends TLS (Caddy, Traefik, nginx). Set `Strict-Transport-Security` there. Dossier adds `upgrade-insecure-requests` to its policy when the proxy says the request came over HTTPS (`X-Forwarded-Proto`).
- **Don't expose port 3000 directly.** Rate limiting trusts the last `X-Forwarded-For` entry, which is only the real client behind a proxy.
- **Pick a long `DOSSIER_SECRET`** and keep it with your backups: without it, saved API keys can't be read. Changing it or the password signs out every session.
- **Keep it updated.** Settings → About tells you when a new version is out.

## Dependencies

Dependabot proposes updates once a week, for the npm packages, GitHub Actions and Docker images. Advisories that `yarn npm audit --all --recursive` still reports, checked on 28 September 2026:

| Package | Advisory | Why it's accepted |
|---|---|---|
| `deepmerge-ts` 7.1.5, from `@prisma/config` | Stack exhaustion on recursive objects ([GHSA-ggr8-5vv4-36mx](https://github.com/advisories/GHSA-ggr8-5vv4-36mx)) | Only merges Prisma's own config when its CLI starts; no user input reaches it. The fix is in 8.x, which Prisma doesn't support yet. |
| `eslint` 9 | Version no longer supported | Development only. Waits for `eslint-config-next` to support ESLint 10. |

`mysql2`, which Prisma's CLI ships but Dossier never loads (it uses PostgreSQL), is pinned to a patched release in `package.json` `resolutions`. Remove the pin once Prisma updates it.


### PRIVACY.md
# Privacy

Dossier is a single-user app you run on your own server. This page is for whoever runs it: what Dossier keeps and for how long, what leaves your server and who receives it, and what deleting something removes. For how the data is protected, see [SECURITY.md](SECURITY.md).

In short: everything you enter is kept in your own PostgreSQL database and data directory. What leaves your server goes to the AI provider and job source you choose, to Google if you connect Gmail and Calendar, to Hacker News and startups' own sites once you use Startups, to Anthropic through Claude if you turn on the Claude connector, plus an update check you can turn off and a daily usage ping, only if you agree to it. With a local model, your profile, postings and documents never leave your server. With a hosted one, keeping the database on your server covers only part of where your data goes.

## What Dossier keeps

| What | Where | Kept until |
|---|---|---|
| Your profile: basics with contact details and your photo, skills, languages, roles, projects, education, publications, references with their email and phone, and your facts about you | Database | You change or delete it |
| Each application: the posting, what was read from it, the match, the facts you gave for it, its status history | Database | You delete the application |
| Each application's resume, cover letter and email, every earlier version of them, the refine chat and your private notes | Database | You delete the application |
| Postings you saved or dismissed in Find jobs, and your past searches with what they found | Database | You remove them. A posting stays, unlinked, when you delete the application made from it |
| The job agent's finds: each posting it scored, with its score, reasons and red flags, and the drafts it prepared. Of a posting you dismissed, only its source's ID, its title and company, and a fingerprint of its link, so it never comes back | Database | Dismissing a posting trims it at once and deletes its draft. Delete everything removes them all |
| The scores of postings you scored with **Score** in Find jobs, or the job agent scored: each score with its reasons and red flags | Database | Scoring again replaces one. Importing a file or Delete everything removes them; exports leave them out, since they can be made again |
| Startups: each startup a refresh found (the hiring post or job post as published, its links, place and roles), its match with the reasons, the email addresses it publishes for applications with where each was found, and your status and notes. People's own addresses only after you press **Look for people's addresses**. Of a startup you removed for good, only SHA-256 hashes of its post, its site's domain and its name, so it doesn't come back | Database | Ones you didn't save, contact or write to go once no refresh has found them for 45 days. People's own addresses go after 14 days, unless you started an application to that startup. **Remove for good** deletes a startup at once. Delete everything removes them all |
| Postings you hand to Claude chat from New application, with **Write it with Claude**, for the Claude connector to read | Database | 14 days, or Delete everything |
| Task data: what each AI task was given and wrote, such as a posting being read, a resume's text and what was read from it, drafts you didn't turn into an application, and a rewrite kept for Undo | Database | The task's application is deleted, or it's older than **Keep task data for** (Settings → Your data: 1 hour, 24 hours, 7 days or 30 days; 24 hours by default), whichever comes first. A resume reading goes as soon as you merge, replace or choose another file |
| Mail from Gmail about your applications, once you connect Google: who it's from and to, the subject, the date and the text (without quoted earlier mail, up to 20,000 characters, never attachments), what the AI read in it, and the answer it drafted. Also what you sent through Dossier, and your own mail in those threads | Database | You delete its application. Mail Dossier couldn't link (**Needs a look**) stays until you link it or mark it **Not job-related**, which keeps only its Gmail IDs and date, so it isn't fetched again |
| The connected Google account: its address, the permissions you gave, and Google's refresh token, encrypted with `DOSSIER_SECRET`. Where the inbox check carries on from, and when it last ran. For each interview Dossier added to your calendar, the event's ID | Database | **Disconnect** in Settings → Google, or Delete everything. An interview's event ID goes when its date does |
| Settings, and your API keys and the Google OAuth client's secret, encrypted with `DOSSIER_SECRET`. While the Claude connector is on, when it was turned on or Claude last disconnected; Claude's sign-in itself keeps nothing: its tokens are signed with `DOSSIER_SECRET` | Database | You change them |
| Nightly backups and the backup taken before each import: full exports, in plain JSON | Data directory, `backups` | `DOSSIER_BACKUP_RETENTION_DAYS`, 14 days by default |
| Zips from **Download all PDFs** | Data directory, `downloads` | Downloaded, or an hour |
| Failed sign-ins: the client IP and how many failed | Database | A successful sign-in from that IP. Otherwise, once they're a day old, the next failed sign-in clears them |
| Your answer to whether to send the usage ping, when you gave it and to which version of the question, the usage ping's random install ID and the day of the last ping, the latest release the update check found, your browser's time zone, so the inbox check reads times in it, and when you last opened Startups and what its last refresh found | Database | Delete everything |

Exports you download and database dumps you take are copies outside Dossier's reach: keep them safe, and delete them yourself. Dossier logs errors without the data involved; what your server, Docker or reverse proxy log otherwise is up to your setup.

## What deleting removes

- **Deleting an application** removes it at once with its documents and their versions, the chat, notes, status history, task data and its mail from Gmail (which stays in Gmail). Nightly backups taken before still hold it until they expire, and so do exports you downloaded.
- **Delete everything** (Settings → Your data) removes the profile, every application, postings and searches, the job agent's finds, Startups, custom themes, settings, task data, backups and zips, the mail from Gmail and the Google account, after revoking Dossier's access at Google. It can't reach your own exports and dumps, what's in your Gmail and calendar, or what a hosted AI provider kept.
- **Disconnect** (Settings → Google) revokes Dossier's access at Google and forgets the account. Mail already in Dossier stays, with its applications.
- **Disconnect Claude** (Settings → Claude connector) signs every Claude out, and so do turning the connector off, a new `DOSSIER_PASSWORD` or a new `DOSSIER_SECRET`. What Claude read before stays in your Claude chats, under your Claude account.

## What leaves your server

| Who receives it | When | What |
|---|---|---|
| A hosted AI provider (OpenAI-compatible, Anthropic or Mistral) | Each AI task, while one is chosen in Settings → AI provider | See [below](#what-a-hosted-ai-provider-receives) |
| Google | While a Google account is connected (Settings → Google) | Signing in: your OAuth client's ID and secret, and the tokens. **Gmail:** the application emails and answers you send, with their PDFs, and a request for new mail on each check (every 10 minutes by default). **Calendar:** the next 14 days, to find your free times; each interview you add, change or remove: its time and a title with the role and company; and requests for the events in the months you look at in the dashboard's calendar, which Dossier shows and doesn't keep. Google already holds your mail and calendar; Dossier only asks for the permissions you give |
| The job source you chose (JSearch, Adzuna or the Bundesagentur für Arbeit) | Each search in Find jobs, which is off until you choose a source, and the job agent's search, at most three times in 24 hours while it's on (never on the Bundesagentur für Arbeit) | What you search for: keywords, place, country, radius and filters. Nothing from your profile: it only fills in the form. The Bundesagentur für Arbeit has no official API: Dossier uses the access its own job search uses, without its permission, so it's searched only after you tick "I understand" under that note, and `DOSSIER_JOBS_ARBEITSAGENTUR=off` takes it out |
| Hacker News (its official API, and Algolia's search of it) | When you press **Refresh** in Startups, then once a day while you open Startups at least every 14 days | Requests for YC startups' job posts and this month's “Who is hiring?” thread. Nothing about you: which posts suit your city and country is worked out on your server |
| Startups' own sites | Each Startups refresh, for the 12 best new matches with a site of their own, and when you press **Find addresses on their site** or **Look for people's addresses** | Requests for the site's robots.txt and a few public pages. See [Startups](#startups) |
| Anthropic, through Claude | Only while the Claude connector is on (Settings → Claude connector, off by default), and only for the Claude you signed in and allowed: each time Claude uses one of Dossier's tools | What that tool answers. See [Claude connector](#claude-connector) |
| The site a posting is on | When you press **Fetch** on a new application, and for a Find jobs posting that came with only its start | A request for the posting's page, from your server, never to an address on your own network |
| GitHub | Once on each day Dossier is used, while **Check for updates daily** is on in Settings → About (it is by default), and when you press **Check for updates** | A request for the latest release, from your server. Nothing about you or your install, though GitHub sees your server's address, as with any request |
| `telemetry.dossier.aien.me` | Once on each day Dossier is used, only after you agree (Dossier asks once, after you sign in) or set `DOSSIER_TELEMETRY=on` | A random install ID and the version number. See [Usage ping](#usage-ping) |

Nothing else is sent. Your browser loads nothing from other sites (the Content-Security-Policy forbids it), and Next.js telemetry is off in the image.

### What a hosted AI provider receives

| Task | What's sent |
|---|---|
| Reading a posting | The posting's text, up to 20,000 characters |
| Matching it against your profile | The posting's requirements, and the names of your skills and languages |
| Writing the resume, cover letter and email | Your profile without contact details: your name, headline, city and country, summary, skills, languages, roles with their companies, dates and bullet points, projects with their dates and bullet points (not their links), education, the publications you show on resumes (not their links), and your facts about you. Also the job's details and the match, the letter's tone, and the facts you gave for the application. The email also gets the posting and the letter's paragraphs |
| Rewriting a part, or refining in the chat | The same, with the drafts (never a letter's sender or signature) and, in the chat, your request and the recent messages before it |
| Importing a resume | The whole text of the file, contact details and references included. The import page says so first |
| Scoring a posting, with **Score** in Find jobs or by the job agent | The posting's text, with its title, company, place and salary, and your profile without contact details or references, as for writing. Score in Find jobs fetches the rest of a posting the source sent only the start of. Each time you press Score, and up to the number of postings an agent run scores (Settings → Job agent) |
| The job agent's drafts | The same as reading a posting and writing its resume and cover letter, for each draft you prepare or, with Prepare drafts on its own on, up to the number a run prepares |
| Reading a reply from Gmail | The mail's sender, subject, date and text (up to 8,000 characters), the application's role and company, and your time zone. With **Every new email** in Settings → Google, that's each new mail outside Promotions and Social |
| Drafting an answer to it | Your profile without contact details, as for the documents, the job's details and the facts you gave for it, the mail and up to four earlier ones in its thread (up to 2,000 characters each), the times to offer, and what you tell the AI |

Never sent in a prompt: your email, phone, address, date of birth and links, your references, the notes you keep on an application, and the addresses Startups finds: a startup's text reaches New application without them, and the email's recipient is filled in on your server. A posting may name a contact person, a mail from an employer has its sender's name and address, and what you write in the chat may mention people, so other people's details can still be sent.

What happens to the data then depends on the provider and your account with them: how long they keep it, whether they use it to train models, and where it's processed. Read their terms for API use, and check the settings your account offers, before you send them a resume. LM Studio or an OpenAI-compatible server on your own network keeps everything on it.

### Usage ping

Dossier asks once, after you first sign in, whether to send a usage ping, and sends nothing until you agree. If you do, on each day you use Dossier your server sends `telemetry.dossier.aien.me` a random install ID and the version number, once, so the project knows how many installs are in use and how often. The ID is made at random and kept in your database. It isn't derived from anything about you or your server, and exports leave it out. Nothing else is sent: no profile, documents, applications, settings, server address or time of day. Dossier works the same either way.

The receiver runs on the project's own server. It keeps the ID, the day and the version, and deletes them after a year. It doesn't keep the address the ping came from, and no other service handles the ping on the way.

- **Change your answer:** the switch in Settings → About, at any time. Saying no forgets the install ID, so what was sent before and anything sent after a later yes can't be linked. `DOSSIER_TELEMETRY=on` or `off` answers for the server and hides the question; while it's set, it decides.
- **Delete what was sent:** note the install ID in Settings → About, switch the ping off, then send the ID to `dossier.app@pm.me`. Everything kept under it is deleted, and you get a confirmation.

Unlike everything else on this page, what the usage ping sends is received by the project, not by you, so the project is responsible for it under the GDPR:

- **Controller:** the maintainer of the Dossier project, reachable at `dossier.app@pm.me`.
- **Purpose and lawful basis:** counting the installs in use and how often they're used, with your consent (Art. 6(1)(a) GDPR), given in the question after sign-in, with the switch in Settings → About, or with `DOSSIER_TELEMETRY=on`. Reading the install ID on your server to send it rests on the same consent (§ 25(1) TDDDG). Dossier keeps your answer, when you gave it and which version of the question you answered.
- **Pings from before 1.8.0:** until 1.8.0, the ping was sent unless `DOSSIER_TELEMETRY=off`. What those pings left is kept until its year is up, on the basis of the project's legitimate interest in knowing how many installs are in use (Art. 6(1)(f) GDPR). You can object to that and have it deleted as above.
- **Recipients:** Hetzner Online GmbH hosts the receiver's server in Germany, as a processor. Nobody else receives the data, and it doesn't leave the EEA.
- **How long:** a year from the day of each ping.
- **Your rights:** you can withdraw your consent at any time, which doesn't affect what was sent before (Art. 7(3) GDPR), and ask for access to what's kept under your install ID, for its erasure, or object to its use (Art. 15, 17 and 21). You can also complain to a data protection authority (Art. 77), for example the one where you live.
- No decisions are made automatically from the ping, and it isn't used for profiling.

### Startups

Startups lists startups that are hiring: YC startups' job posts from Hacker News' official API, and the posts in Hacker News' monthly “Who is hiring?” thread. It keeps the ones that hire where your profile says you live, or remotely and open to your country, ranks them against your profile on your server, without AI, and shows the address each one publishes for applications. Dossier sends nothing: you decide whom to write to, from New application or your own mail.

**If you run a website** and see requests from `Dossier/<version>`: they come from one person's own Dossier, looking for the address you publish for job applications. The Dossier project doesn't receive anything it reads. It reads your robots.txt first and follows it, under the product token `Dossier`. Then it reads at most your home, `/careers`, `/jobs` and `/contact` pages, and `/about` and `/team` only when that person asks for people's addresses. It reads one page at a time and stops when your site answers 403 or 429. It keeps only the email addresses on your own domain and the page each was on, never the pages, and doesn't decode addresses written to hide them. When a page says you take no unsolicited applications, Dossier shows that and doesn't start an application. To keep it out:

```
User-agent: Dossier
Disallow: /
```

**If you use it:** Startups is for applying for jobs. Offering your services as a freelancer by email is advertising in many countries: in Germany and the rest of the EU it needs the company's consent first, even when the company published the address, and in the US, Canada and Australia such an email needs a way to opt out. Dossier doesn't support that use. Whether the GDPR's exemption for personal activities covers your own job search hasn't been settled, so Dossier treats the addresses as personal data: it looks up people's own addresses only when you ask, drops them after 14 days unless you write to that startup, keeps every address out of what the AI receives, and **Remove for good** deletes a startup and keeps only hashes so it doesn't come back. If someone asks you to delete their address, that's the button.

### Claude connector

The Claude connector lets you use Dossier from Claude: in chats on claude.ai, in the Desktop and mobile apps, and in Claude's command-line app. It's off until you turn it on in Settings → Claude connector. Then Claude can use it once you've signed in to Dossier and pressed **Allow**; while it's off, its addresses answer as if they didn't exist.

What Claude reads through it goes to Anthropic, under your own Claude account and its terms, as anything you put in a chat does:

- **Your profile,** without contact details, links or references: the same as a hosted AI provider gets for writing.
- **Postings:** what Find jobs searches find for Claude (the searches are kept in Find jobs, like your own), the postings you hand over, and the text of a posting Claude asks for by its link, fetched from your server.
- **Your applications:** their details and status, the posting and the match, and the resume and cover letter as text. Never your private notes, or a letter's sender and signature.

Claude also writes through it: an application it wrote, saved as a Draft and checked like Dossier's own AI's; the fit scores it gives postings; and an application's status. No tool deletes, archives or sends anything. With **Write it with Claude** in New application, the posting you pasted is kept for Claude to read for 14 days; Score and Write it with Claude open a new chat on claude.ai with a short prompt that names the posting by its ID, and nothing else.

Anthropic is the controller of what reaches it through your Claude account; the Dossier project receives nothing from the connector. Dossier keeps no tokens: Claude's sign-in is signed with `DOSSIER_SECRET`, and **Disconnect Claude** ends it.

## GDPR and similar laws

What applies depends on who you run Dossier for, and this isn't legal advice.

- **For your own job search:** the GDPR doesn't apply to processing for purely personal or household activities (Article 2(2)(c)), though no court has said yet whether a job search counts. Other privacy laws often exempt personal use too.
- **For other people**, such as a career coach, an agency or a service: you decide what happens to their data, so you're responsible for it under the GDPR. Among other things, that means a lawful basis for each use, telling them what this page says (who receives their data, for what, and for how long), a data processing agreement with a hosted AI provider, and safeguards when it processes the data outside the EEA. Resumes can reveal special category data, such as health or religion, and hold other people's details, such as references.

Self-hosting alone doesn't make a deployment compliant. Dossier's code shows what it stores and sends. It can't tell you whether your provider, its terms or your account settings meet what you need.

When someone asks for their data, **Export** in Settings → Your data gives everything Dossier keeps except task data and failed sign-ins, which expire on their own, and the mail from Gmail and the Google account, which belong to the mailbox: the mail is still in Gmail. Deleting an application or **Delete everything** removes data as described [above](#what-deleting-removes).


## Top-level structure
- `.dockerignore`, `.env.example`, `.github/`, `.gitignore`, `.yarnrc.yml` — Docker/env/CI/Yarn 4 config
- `DEVELOPMENT.md` — Next.js 16 + Prisma 7 + PostgreSQL 18 Docker Compose developer guide (AI providers, job search, job agent, Claude connector notes, tests)
- `Dockerfile`, `compose.yml`, `compose.production.yml`, `captain-definition`, `docker/` — production + CapRover images; `docker/bin/yarn`, `docker/start.sh`
- `LICENSE` — AGPL-3.0
- `PRIVACY.md`, `SECURITY.md` — data leaving the server; auth, CSP, AI prompt injection limits
- `README.md` — product overview, Docker Desktop quick start, self-host links to wiki
- `e2e/` — Playwright flows including `agent.spec.ts`, `connector.spec.ts`; fake AI/jobs/Google servers
- `eslint.config.mjs`, `next.config.ts`, `package.json` (name `dossier.aien.me`, v1.9.2), `playwright.config.ts`, `postcss.config.mjs`, `tsconfig.json`, `vitest.config.mts`, `yarn.lock`
- `prisma/` — schema + migrations (job agent, Claude pastes) + seed/demo data
- `public/`, `scripts/hash-password.ts`, `site/` — static marketing site assets
- `src/app/` — Next.js App Router UI + `src/app/api/mcp` Claude connector (Streamable HTTP MCP)
- `src/lib/ai/` — provider adapters (Ollama, LM Studio, OpenAI-compatible, Anthropic, Mistral) + `tasks/` (extract-posting, match-requirements, tailor-resume, write-cover-letter, score-posting, refine-chat, …) + fact-guard
- `src/lib/agent/` — daily job agent (scan/score/draft/schedule)
- `src/lib/connector/` — Claude MCP tools + OAuth (`get_profile`, `search_jobs`, `save_application`, …)
- `src/lib/job-search/`, `src/lib/jobs/`, `src/lib/google/`, `src/lib/startups/` — job sources, background jobs, Gmail/Calendar, YC/HN startups
