# supabase/cli

## Metadata
- Stars: 2346
- Primary language: TypeScript
- Default branch: develop
- Latest release: v2.110.0-beta.27 (2026-07-14, pre-release)
- License: MIT (per README; no LICENSE key returned by GitHub API)
- Homepage: https://supabase.com/docs/reference/cli/about
- Fetched: 2026-07-14
- Final URL: https://github.com/supabase/cli

## Description
Supabase CLI. Manage postgres migrations, run Supabase locally, deploy edge functions. Postgres backups. Generating types from your database schema.

## README
<p align="center">Supabase CLI wordmark</p>
<p align="center">Develop locally and deploy to the Supabase Platform from your terminal.</p>

---

Supabase CLI brings the Supabase Platform to your terminal. Run the full local stack, manage database migrations, deploy Edge Functions, generate types, and automate project workflows.

## Installation

```sh
# YOLO
curl -fsSL https://raw.githubusercontent.com/supabase/cli/main/install | bash

# npm
npm install -D supabase                   # or bun/pnpm/yarn add -D supabase
npm install -D supabase@beta              # beta channel

# macOS and Linux
brew install supabase/tap/supabase        # always up to date
brew install supabase                     # official formula, may be delayed
brew install supabase/tap/supabase-beta   # beta channel

# Windows
scoop bucket add supabase https://github.com/supabase/scoop-bucket.git
scoop install supabase
scoop install supabase-beta               # beta channel

# Linux packages
# Download .apk, .deb, .rpm, or .pkg.tar.zst from GitHub Releases.
```

Linux packages are available from Releases. Community-maintained packages also available through pkgx and Nixpkgs.

## Start Local Development

```sh
supabase init
supabase start
supabase status
```

The local stack includes Postgres, Auth, Realtime, Storage, Edge Functions, and the Supabase APIs.

Start from a template:

```sh
supabase bootstrap
```

## Link A Project

```sh
supabase login
supabase link
```

## Manage Your Database

```sh
supabase migration new create_profiles
supabase db diff
supabase db push
supabase db reset
```

## Deploy Edge Functions

```sh
supabase functions new hello-world
supabase functions serve
supabase functions deploy hello-world
```

## Generate Types

```sh
supabase gen types --local
supabase gen types --linked
```

## Reference

```sh
supabase db --help
supabase functions deploy --help
```

- CLI reference: https://supabase.com/docs/reference/cli/about
- Local development guide: https://supabase.com/docs/guides/local-development
- Supabase docs: https://supabase.com/docs

## Developing

This repository is a pnpm monorepo. The published package lives in `apps/cli`.

```sh
pnpm install
cd apps/cli

pnpm dev:next -- --help
pnpm check:all
pnpm test:core
```

Useful source entry points:

| Path              | Purpose                                |
| ----------------- | --------------------------------------- |
| `apps/cli`        | TypeScript/Bun CLI package             |
| `apps/cli-go`     | Go CLI source used by the legacy shell |
| `packages/stack`  | Local Supabase stack runtime           |
| `packages/config` | Config schema and generated types      |
| `packages/api`    | Typed Supabase Management API client   |

After a fresh clone, install the reference repositories used for agent and developer inspection: `pnpm repos:install`.

## Contributing

Focused pull requests with a clear problem, a small surface area, and tests that match the user-facing behavior. Open an issue first and wait for a maintainer to add the `open-for-contribution` label before starting work — external pull requests that don't link a labeled, open issue are closed automatically.

```sh
pnpm check:all
pnpm test
```

PR titles must use conventional commits, e.g. `fix(cli): handle linked projects without cached service versions`.

## License

Supabase CLI packages are released under the MIT license.

## Docs

### docs/cli/dev-alpha-command-structure.md

Internal design note on the CLI's command structure (alpha/dev-stage document tracked alongside the TypeScript rewrite of the CLI).

## Top-level structure
- `apps/cli` — TypeScript/Bun CLI package (the primary published `supabase` command)
- `apps/cli-go` — Go CLI source used by the legacy shell
- `packages/stack` — local Supabase stack runtime (Postgres, Auth, Realtime, Storage, Edge Functions)
- `packages/config` — config schema and generated types
- `packages/api` — typed Supabase Management API client
- `docs/` — CLI design docs, ADRs, telemetry, self-documenting-cli notes
- `install` — install script served from `raw.githubusercontent.com`
- `.repos` — reference repositories used for agent/developer inspection (populated via `pnpm repos:install`)
- `tools/` — internal build/dev tooling
- `mise.toml`/`mise.lock` — toolchain version pinning
- `nx.json` — Nx monorepo task orchestration
- `pnpm-workspace.yaml`/`pnpm-lock.yaml` — pnpm monorepo config
- `CLAUDE.md`, `AGENTS.md` — agent instruction files
- `verdaccio.yaml` — local npm registry config for package testing
