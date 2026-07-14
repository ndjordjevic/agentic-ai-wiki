---
type: source
category: "Infra, hosting, DB & observability"
source_url: https://github.com/supabase/cli
tags:
  - supabase-cli
  - postgres-migrations
  - edge-functions
  - local-dev-stack
  - type-generation
  - pnpm-monorepo
  - developer-tooling
related:
  - supabase.com
product: supabase
detail_level: standard
created: 2026-07-14
updated: 2026-07-14
---

The Supabase CLI brings the Supabase Platform to the terminal: it runs the full local stack (Postgres, Auth, Realtime, Storage, Edge Functions, and the Supabase APIs), manages Postgres migrations, deploys Edge Functions, generates types from the database schema, and links a local workspace to a hosted project. It's the primary companion tool to [[supabase.com]] — the same `product:` grouping as the main platform page, since this repo backs the `supabase` command referenced throughout supabase.com's docs.

_All claims below are sourced from ../../raw/github/supabase-cli.md unless otherwise noted._

## What it does

`supabase init` / `supabase start` / `supabase status` stand up a local Postgres + Auth + Realtime + Storage + Edge Functions stack; `supabase bootstrap` scaffolds from a template. `supabase login` / `supabase link` connect that local workspace to a hosted Supabase project so migrations and functions can be pushed live.

## Installation

```sh
curl -fsSL https://raw.githubusercontent.com/supabase/cli/main/install | bash   # YOLO installer
npm install -D supabase          # or bun/pnpm/yarn add -D supabase
brew install supabase/tap/supabase   # macOS/Linux, always up to date
scoop install supabase           # Windows
```
Linux `.apk`/`.deb`/`.rpm`/`.pkg.tar.zst` packages are published to GitHub Releases; community packages also exist via pkgx and Nixpkgs.

## Key features

- **Full local Supabase stack** in one command (`supabase start`), covering Postgres, Auth, Realtime, Storage, Edge Functions, and the Supabase APIs — not just a thin database-migration wrapper.
- **Migration + schema-diff workflow** — `supabase migration new`, `supabase db diff`, `supabase db push`, `supabase db reset`.
- **Edge Functions lifecycle** — `supabase functions new/serve/deploy` covers scaffold, local serve, and deploy in one CLI surface.
- **Type generation** — `supabase gen types --local` / `--linked` generates TypeScript types directly from the live schema (local or linked hosted project).

## Architecture

The repo is a pnpm monorepo: `apps/cli` is the published TypeScript/Bun CLI package (the current `supabase` command); `apps/cli-go` is the older Go CLI source used by a legacy shell wrapper — the project is mid-migration from Go to TypeScript. `packages/stack` runs the local stack, `packages/config` holds config schema and generated types, and `packages/api` is a typed client for the Supabase Management API. Nx orchestrates monorepo tasks (`nx.json`).

## Example usage

```sh
supabase init
supabase start
supabase migration new create_profiles
supabase db diff
supabase db push
supabase functions deploy hello-world
supabase gen types --linked
```

## Maintenance status

2,346 stars, 495 forks, MIT license (per README; GitHub API returned no `licenseInfo` for the repo), latest release v2.110.0-beta.27 (2026-07-14, pre-release channel), pushed same day — actively developed, with the `develop` branch as default. Contribution requires an issue labeled `open-for-contribution` before a PR is accepted; PR titles must follow Conventional Commits.
