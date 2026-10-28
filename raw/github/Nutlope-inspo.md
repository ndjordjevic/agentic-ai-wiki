# Nutlope/inspo

## Metadata
- Stars: 941
- Forks: 62
- Primary language: TypeScript
- Default branch: main
- Latest release: none
- License: MIT License
- Homepage: https://inspomcp.dev
- Pushed at: 2026-10-27T15:17:23Z
- Fetched: 2026-10-28
- Final URL: https://github.com/Nutlope/inspo

## Description
Real websites for your coding agent to learn design from, searchable over MCP.

## README
<p align="center">
  <a href="https://inspomcp.dev"><img alt="Inspo" src="docs/img/og.png"></a>
</p>

<h1 align="center">Inspo</h1>

<p align="center">Real production websites your coding agent can study, over MCP, before it writes UI. <a href="https://inspomcp.dev">inspomcp.dev</a></p>

## With and without

Same brief, same model, no design skill on either run. The only difference: the page on the right was built with Inspo MCP on the session.

<p>
  <img alt="The bare agent's page: dark theme, neon accent, gradient app mock" src="docs/img/without-inspo.jpg" width="49.5%">
  <img alt="The page built with Inspo: warm paper, editorial type, detailed product mock" src="docs/img/with-inspo.jpg" width="49.5%">
</p>

That gap is the product. Agents have tools but not taste, and the open web already holds every reference they need: Inspo assembles, tags, and addresses it.

## What's inside

- **2,320 pages across 832 real sites**, each captured on desktop and mobile, with traced palettes, real fonts, detected tech, and a fold-by-fold autopsy on every page.
- **68 canonical reference components** (heroes, pricing, footers, navs, and more), each demonstrating one named macrostructure, with copy-pasteable JSX.
- **A DESIGN.md for every site**, extracted from its DOM: semantic palette roles, type ramp, spacing scale, CSS variables, container width.

Fifteen tools expose all of it; `recommend(brief)` composes most of them into one call. The full tool table lives in [apps/mcp/README.md](apps/mcp/README.md).

## Tech stack

- TypeScript MCP server with two transports: stdio via npm, and Streamable HTTP served by the site's own Vercel deployment. No database at query time; the catalogue ships as a static seed.
- Next.js 16 + Tailwind v4 gallery: the archive browser and the curator dashboard.
- Playwright capture worker: desktop and mobile shots, palette, type ramp and CSS variable extraction, tag and autopsy passes via Together AI.
- Together AI embeddings behind semantic search and `find_similar`.
- A smoke harness that boots the server in-process and exercises the core tools.

## Cloning & running

1. One command, any client: `npx -y inspo-mcp install` (detects Claude Code, Cursor, Codex, VS Code, Windsurf, Zed, Claude Desktop and writes the config; `--dry-run` shows the plan)
2. Or point a client at the hosted endpoint yourself: `claude mcp add --transport http inspo https://inspomcp.dev/api/mcp`
3. Or clone: `git clone https://github.com/Nutlope/inspo.git && cd inspo && pnpm install`
4. Gallery: `pnpm dev`, then open `localhost:3000`
5. Dev loop: `pnpm --filter @inspo/mcp test`

Per-client snippets (Cursor, Windsurf, Zed, Claude Desktop) are on [the MCP page](https://inspomcp.dev/mcp); the self-host runbook is [DEPLOY.md](DEPLOY.md).

## Roadmap

- [ ] show the desktop and mobile capture side by side on every screen page
- [ ] backfill component crops so `find_components` returns a crop for every hit
- [ ] paginate the list tools instead of capping them
- [ ] re-shoot the mobile set at retina scale
- Accounts and paywalls are skipped on purpose: the archive is more useful free.

Want a site in the archive? Append it to [apps/worker/src/seed-urls.ts](apps/worker/src/seed-urls.ts) and open a PR. The bar: does it make the archive better for someone building a website?

## Security

Every tool is read-only. The one path that touches the outside world - `get_design_system(live:true)`, which supplements thin captured tokens from the screen's own source - passes each URL and redirect through an SSRF guard: public named hosts only, ports 80 and 443, byte-capped body, no JS execution. The hosted endpoint logs tool name, success and duration per call, never IPs or query text.

MIT, copyright Together AI and contributors. The screenshots remain the work of their designers: every screen credits and links its source, and takedowns are honoured at [/dmca](https://inspomcp.dev/dmca).


## Docs

### DEPLOY.md
# Deploy

Inspo ships to two surfaces, each picked for the runtime its workload actually needs.

| Surface | Where | Runs on | Why |
|---|---|---|---|
| Gallery + hosted MCP | Vercel | `apps/web` | Next.js 16 SSR; the MCP endpoint is a route handler in the same app |
| Capture worker | Fly.io | `apps/worker` | Real Chromium needs a real VM |

The gallery and the MCP read the catalogue from a static seed (`packages/db/src/static-screens.json`), so neither needs a database at query time. Postgres is optional: the capture worker can persist to it, and the curator dashboard reads it.

---

## 1. Postgres (Neon, optional)

1. Create a Neon project at <https://neon.tech>.
2. Copy the **pooled** connection string.
3. In your local `.env`:
   ```
   DATABASE_URL=postgres://…
   ```
4. Bootstrap the schema:
   ```bash
   pnpm db:migrate    # enables pgvector
   pnpm db:push       # pushes Drizzle schema
   pnpm db:seed       # loads the 16 fixtures
   ```

---

## 2. Gallery: Vercel

The gallery is the only piece your users see directly, and it serves the hosted MCP endpoint too.

```bash
cd /path/to/inspo
npx vercel link            # follow prompts; pick "apps/web" as root
npx vercel env add BETTER_AUTH_SECRET    production   # any random 32+ chars
npx vercel env add BETTER_AUTH_URL       production   # e.g. https://inspo.example.com
npx vercel env add TOGETHER_API_KEY      production   # optional, see below
npx vercel deploy --prod
```

`vercel.json` at [`apps/web/vercel.json`](apps/web/vercel.json) tells Vercel to build the workspace correctly via `pnpm --filter web... build`.

**Environment variables (production):**

| Variable | Notes |
|---|---|
| `BETTER_AUTH_SECRET` | Required. The app refuses to boot in production without it, even though no sign-in page is exposed today |
| `BETTER_AUTH_URL` | Required, for the same reason: your production origin |
| `INSPO_BASE_URL` | Optional override. Defaults to `https://inspomcp.dev` on Vercel (used by `metadataBase`, sitemap, MCP image URLs) |
| `TOGETHER_API_KEY` | Optional. Turns on semantic ranking for hosted MCP callers and powers `/api/extract` |
| `INSPO_CATALOGUE_URL` | Optional. Where the MCP route fetches the embedding sidecar from; defaults to the public Blob store |
| `DATABASE_URL` | Optional. Only the curator dashboard reads it; everything else reads the static seed |

**About images.** Every row in the static seed carries absolute Vercel Blob URLs for its screenshots and their AVIF/WebP variants, so a fresh deploy shows real images with no extra setup. New captures reach Blob with `pnpm --filter @inspo/worker capture:upload-to-blob` (needs `BLOB_READ_WRITE_TOKEN`).

---

## 3. MCP: hosted with the site on Vercel

The hosted MCP is a Next.js Route Handler (`apps/web/src/app/api/mcp/route.ts`), so deploying the gallery deploys the endpoint too: there is no separate service. The route serves the seed bundled into the web build and fetches the embedding sidecar from the CDN once per lambda (`INSPO_CATALOGUE_URL` overrides the store). Optional env on the Vercel project: `TOGETHER_API_KEY` turns on semantic ranking for hosted callers.

After any seed change, re-publish the catalogue sidecar:
```bash
pnpm --filter @inspo/worker exec tsx src/publish-catalogue-to-blob.ts --go
```

Test:
```bash
curl -X POST https://<your-domain>/api/mcp \
  -H 'content-type: application/json' \
  -H 'accept: application/json, text/event-stream' \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/list"}'
```

---

## 4. Capture worker: Fly.io

The worker needs a real Chromium and persistent disk for raw PNGs. We don't expose an HTTP port: you `fly ssh` in to run captures (or wire it to a queue later).

```bash
cd /path/to/inspo
brew install flyctl
fly auth login
fly launch --config apps/worker/fly.toml --no-deploy
fly secrets set \
  TOGETHER_API_KEY="$TOGETHER_API_KEY" \
  BLOB_READ_WRITE_TOKEN="$BLOB_READ_WRITE_TOKEN" \
  DATABASE_URL="$DATABASE_URL"   # optional
fly deploy --config apps/worker/fly.toml
```

Run a capture:
```bash
fly ssh console --app inspo-worker -C "cd /app/apps/worker && pnpm capture https://linear.app"
```

Captures persist in the mounted `captures` Fly volume; upload them to Vercel Blob with `pnpm --filter @inspo/worker capture:upload-to-blob`. [SEEDING.md](SEEDING.md) walks through the whole path from a URL list to a published catalogue.

---

## 5. Wire up clients

Point any MCP client at `https://<your-domain>/api/mcp`, for example:

```bash
claude mcp add --transport http inspo https://<your-domain>/api/mcp
```

(`npx -y inspo-mcp install` always writes the public inspomcp.dev endpoint.)

---

## CI / preview deploys

Every push to main triggers a Vercel build of `apps/web`, which redeploys the site and the hosted MCP endpoint together (the endpoint lives inside the web app, so never ignore `apps/mcp` changes in Vercel build filters).

For the capture worker, add a step that runs `flyctl deploy --config apps/worker/fly.toml --remote-only` with `FLY_API_TOKEN`.

---

## Cost ballpark (low-traffic)

| Surface | Free tier covers | Beyond that |
|---|---|---|
| Vercel | 100 GB-hours / mo | $20 / mo Pro |
| Fly.io | 3× shared 256MB VMs | $0.0000022 / s of `shared-cpu-2x@2gb` (~$15 / mo if always-on) |
| Neon (optional) | 0.5 GB storage, 191.9 compute-hours | $19 / mo Launch tier |
| Together AI | Pay as you go | Tagging, autopsies and embeddings cost well under a cent per page |

Realistic monthly cost while seeding the catalogue (a few hundred captures): **~$0 to $25**.


### SEEDING.md
# Seeding the catalogue

How a site gets into the archive: capture it to disk, look at the captures, then run the enrichment and publish steps. Everything runs from `apps/worker` and needs no database; Together AI does the tagging, autopsies and embeddings.

Candidate sites are proposed in [`apps/worker/src/seed-urls.ts`](apps/worker/src/seed-urls.ts). The bar: does the site make the archive better for someone building a website?

## Prerequisites

```bash
pnpm install
pnpm --filter @inspo/worker run playwright:install   # Chromium
```

Create `.env` at the repo root (`.env.example` lists every variable):

```env
TOGETHER_API_KEY=        # tags, descriptions, northstars, autopsies, quality scores, embeddings
BLOB_READ_WRITE_TOKEN=   # uploads screenshots and publishes the catalogue
```

Without `TOGETHER_API_KEY` the worker still captures pages, palettes, fonts and tech, but tags, descriptions and embeddings stay empty.

## 1. Capture landing pages

Put one URL per line in a file, then:

```bash
cd apps/worker
pnpm exec tsx src/add-sites-disk.ts urls.txt --concurrency=2
```

Each site lands in `captures/<slug>/`: desktop hero and full page, a phone view, the extracted palette, fonts, type ramp and CSS variables, and a `meta.json` sidecar with the tags. Cookie notices, popups and chat bubbles are cleared before every shot. The run is idempotent: a slug that already has a `meta.json` is skipped, so a stopped run resumes where it left off.

## 2. Capture more pages per site (optional)

```bash
pnpm exec tsx src/capture-pages-disk.ts sites.txt --max=3 --concurrency=3
```

Discovers public pages (pricing, about, docs, blog, changelog and so on) and captures each into `captures/<site>--<path>/`. Sign-in, account, checkout and legal pages are never picked, and pages that answer with an error, a not-found page or a bot check are dropped.

## 3. Look before you merge

```bash
pnpm exec tsx src/qa-sheet.ts slugs.txt
```

Writes contact sheets to `captures/_reports/qa/`: desktop and phone heroes, and whole pages as columns. Leave out any page that shows a cookie notice, a modal, a login wall, a blank band, or a copy of the landing page. `qa-captures.ts` runs a vision pass over the same captures as a first filter; the sheets are the real check.

## 4. Merge and enrich

With `slugs.txt` listing every capture dir that goes in (each site's landing page first), run these stages in order. Each one is idempotent, so a failed stage can be re-run on its own.

```bash
pnpm exec tsx src/encode-existing.ts --go --from-file=slugs.txt                 # AVIF/WebP variants
pnpm exec tsx src/upload-to-blob.ts --go --from-file=slugs.txt                  # PNGs + variants to Blob
pnpm exec tsx src/merge-disk-captures-to-seed.ts --from-file=slugs.txt --apply  # rows into the seed
pnpm exec tsx src/add-mobile-to-seed.ts --write --from-file=slugs.txt           # phone views
pnpm exec tsx src/add-desktop-variants-to-seed.ts --write --from-file=slugs.txt # full-page variants
pnpm exec tsx src/backfill-axes.ts                                              # measured axes + light/dark mode
pnpm exec tsx src/generate-northstars.ts --go                                   # one-line design summary
pnpm exec tsx src/generate-autopsies.ts --go                                    # fold-by-fold autopsy
pnpm exec tsx src/generate-quality.ts --go                                      # capture quality score
pnpm exec tsx src/build-row-embeddings.ts --go --missing-only
pnpm exec tsx src/rebuild-site-embeddings.ts --go
pnpm exec tsx src/build-umap-layout.ts --apply
```

`merge-disk-captures-to-seed.ts` also takes `--site-meta=site-meta.json` (`{"<siteSlug>": {"title": "Relume", "industry": ["saas", "ai"]}}`) for curated site names and industries. It cleans font names and takes em and en dashes out of every row on the way in.

## 5. Publish

```bash
pnpm exec tsx src/publish-catalogue-to-blob.ts --go
```

Uploads the seed and both embedding sidecars to Blob, where `npx inspo-mcp` reads them. Commit the seed files too: the next deploy of `apps/web` serves the new rows in the gallery and through the hosted MCP.

## Removing pages or sites

```bash
pnpm exec tsx src/delete-screens.ts --from-file=pages.txt           # dry run
pnpm exec tsx src/delete-screens.ts --from-file=pages.txt --apply
```

List page slugs, one per line; a whole site means its landing slug plus every `<site>--*` slug. The script also updates both embedding sidecars and reports any collection or example write-up that still names a removed page. Rebuild the map layout afterwards (`build-umap-layout.ts --apply`) and publish again.

## Tags

The allow-lists in [`packages/taxonomy/src/index.ts`](packages/taxonomy/src/index.ts) are the single source of truth. The tagger picks only from these enums and every value is validated before it is written. Add a missing tag there and both the worker prompt and the gallery filter rail pick it up.

## Models

Defaults live in code; each can be overridden from `.env`.

| Stage | Default | Override |
|---|---|---|
| Tags, descriptions, northstars | `google/gemma-4-31B-it` | `INSPO_VISION_MODEL` |
| Quality scores | `google/gemma-4-31B-it` | `INSPO_QUALITY_MODEL` |
| Autopsies | `moonshotai/Kimi-K2.6` (a dedicated Together deployment) | `INSPO_AUTOPSY_MODEL`, e.g. `google/gemma-4-31B-it` |
| Embeddings | `intfloat/multilingual-e5-large-instruct` (1024-dim) | `INSPO_EMBED_MODEL` |


### apps/mcp/README.md
# Inspo MCP

**A curated archive of 832 production sites (2,320 captured pages) - queryable over MCP - that gives coding agents visual taste before they write UI.**

Every result is grounded in a real, shipped site: real fonts, frequency-ranked palettes traced to source, detected tech, named macrostructures, component crops, and - now - **desktop + mobile pairs** so an agent learns responsiveness, not just the desktop look.

This is, and stays, a standard **MCP server** - packaging it for one-line install just makes the same server trivially addable to any MCP client (Cursor, Claude Code, Claude Desktop, …). Two transports, same tools:

- **stdio** - `npx -y inspo-mcp` (`src/server-npm.ts`) fetches the catalogue from the CDN; from a clone, `src/server.ts` reads the bundled static seed (no DB needed).
- **Streamable HTTP** - a Next.js Route Handler (`apps/web/src/app/api/mcp/route.ts`) that ships with the site's Vercel deployment.

## Tools

| Tool | What it does |
|---|---|
| `search_screens(query, style?, industry?, macrostructure?, mode?, vibe?, color?, pageType?, paperBand?, displayClass?, accentHue?, device?, limit?)` | Hybrid lexical + vector search across the archive (vector ranking needs `TOGETHER_API_KEY`). Returns palette, fonts, tech, tags, **desktop + mobile** image URLs, inline thumbnails. |
| `recommend(brief, macrostructure?, pageType?, mode?, vibe?, color?, device?)` | One-call moodboard: a macrostructure pick plus shortlist, 5 exemplars, up to 3 matching reference components (fetch source with `get_reference_jsx`), a palette suggestion, an `evidence` packet, and **`heroGuidance`** + **`spacingGuidance`**. Start here. |
| `get_design_system(slug, live?)` | Full DESIGN.md for a site - real fonts, palette + CSS vars, type ramp, detected tech. Thin rows are supplemented by a live fetch of the source (on by default; `live:false` skips it). |
| `compare(slugs[])` | 2-4 sites side by side: shared style tags, distinct macrostructures, register agreement. |
| `find_by_color(hex, tolerance?, limit?)` | Real sites whose palette sits near a target colour (OKLAB distance). |
| `find_similar(slug, limit?, sameSite?)` | A site's visual + structural neighbours. |
| `find_examples_for_macrostructure(name, limit?)` | Exemplars of one of the 19 named macrostructures (`Bento Grid`, `Specimen`, …). |
| `find_components(type, …)` / `find_reference_components(type?, macro?)` / `get_reference_jsx(type, id)` | Real component crops, an index of the canonical reference components, and the JSX source for one. |
| `get_filters()` | Zero input: lists every accepted filter / enum value (styles, industries, macrostructures, vibes, page types) so the agent can pick valid arguments in one call. |
| `get_site_pages(siteSlug?)` | A site's captured pages in reading order; with no argument, the directory of multi-page sites. |
| `get_screen(slug)` / `list_collections()` / `get_collection(slug)` | Single record · editor-curated issues. |

Screenshot URLs are absolute Vercel Blob URLs, and component-crop URLs are built on `INSPO_BASE_URL` (default `https://inspomcp.dev`), so an agent can fetch them or hand them to a vision model directly.

**Baked-in guidance:** the server instructions + `recommend()` carry two composition rules to every agent. `heroGuidance`: *compose the hero to fit the first viewport (~1280×800 / `100svh`) - never overflow it* - which kills the most common "AI-built page" failure (an oversized hero cut off below the fold). And `spacingGuidance`: *separate sections with real block space (production sites run 80-160px between sections) and keep all copy inside a centered, padded column* - which kills the second most common one (sections crammed into one block, text touching the viewport edge). The spacing numbers are measured from the archive, not invented.

## Install (one line per client)

### Hosted (recommended - no clone, no deps)

A hosted endpoint is **live and free** (no auth): `https://inspomcp.dev/api/mcp`. Add it as a remote MCP server:

```bash
# Claude Code
claude mcp add --transport http inspo https://inspomcp.dev/api/mcp
```

```jsonc
// Cursor - ~/.cursor/mcp.json (Claude Desktop: add the URL under Settings > Connectors, or use the npx form below)
{ "mcpServers": { "inspo": { "url": "https://inspomcp.dev/api/mcp" } } }
```

### One command, any client

`inspo-mcp install` detects the MCP clients on the machine (Claude Code,
Codex, VS Code, Cursor, Windsurf, Claude Desktop, Zed) and writes the
config for each, pointed at the hosted endpoint:

```bash
npx -y inspo-mcp install
```

It shows the plan and asks before touching anything. `--dry-run` prints
the plan and writes nothing, `--client <id>` targets one client,
`--local` wires the npx stdio form instead of the hosted URL, and `-y`
skips the prompt. Config files it edits are backed up alongside
(`mcp.json.inspo-backup`); Zed's JSONC settings are printed for you to
paste rather than rewritten, so your comments survive.

### `npx` (zero-config)

No clone and no hosting - the stdio server (`inspo-mcp`) runs straight
from npm via `npx -y inspo-mcp` and fetches the catalogue from the CDN:

```jsonc
// Claude Code: ~/.claude.json  ·  Cursor: ~/.cursor/mcp.json  ·  Claude Desktop: config
{ "mcpServers": { "inspo": { "command": "npx", "args": ["-y", "inspo-mcp"] } } }
```

Optional `env`: `TOGETHER_API_KEY` (enables query-embedding semantic search),
`INSPO_CATALOGUE_URL` (point at a self-hosted catalogue), and `INSPO_PROFILE` /
`INSPO_IMAGES` / `INSPO_MAX_TOKENS` (see Open-source models below).

> Running `npx -y inspo-mcp` by hand looks like it does nothing: an MCP server
> speaks JSON-RPC on stdin/stdout and prints nothing on its own. From a
> terminal it now prints these install instructions instead (`--help`,
> `--version`; `--stdio` forces the server). It is meant to be *launched by a
> client*, so add it with one of:
>
> ```bash
> claude mcp add inspo -- npx -y inspo-mcp
> ```

### Local (stdio, from a clone)

The bin shim boots the TS server via `tsx` - no build step.

```jsonc
// Claude Code: ~/.claude.json  ·  Cursor: ~/.cursor/mcp.json  ·  Claude Desktop: config
{
  "mcpServers": {
    "inspo": {
      "command": "node",
      "args": ["/absolute/path/to/inspo/apps/mcp/bin/inspo-mcp.js"]
    }
  }
}
```

Restart the client; the agent gains all the tools above.

## MCP registry

The server is described by [`server.json`](./server.json) for the official
MCP registry (name: `io.github.nutlope/inspo`), covering both the npm
stdio package and the hosted streamable-http endpoint. To publish or
update the listing (needs the GitHub account that owns the repo):

```bash
brew install mcp-publisher
cd apps/mcp
mcp-publisher login github
mcp-publisher publish
```

Note: the npm package must be published with the matching `mcpName`
field first (build-npm.mjs stamps it), and `server.json`'s versions
should match the published package version.

Telemetry: the hosted endpoint writes one log line per tool call (tool
name, success, duration) to the Vercel logs; no IPs and no query text
are recorded. Local stdio/npx servers emit zero telemetry.

## Open-source models (Kimi K2.7, GLM 5.2, Qwen, DeepSeek V4, MiniMax)

The server ships a second profile tuned to the harnesses OSS models
actually run in. Two independent knobs:

| Env var | Values | What it does |
|---|---|---|
| `INSPO_PROFILE` | `full` (default) / `lite` | `full` exposes 15 tools; `lite` exposes the 9 highest-leverage tools (`recommend`, `search_screens`, `get_screen`, `get_design_system`, `find_examples_for_macrostructure`, `find_reference_components`, `get_reference_jsx`, `get_site_pages`, `get_filters`). Small models pick tools more reliably from a short list. |
| `INSPO_IMAGES` | `thumbs` (default) / `none` | `none` returns text-only responses: no inline image blocks. Use it when the harness drops MCP images (Cline, OpenCode with a non-vision model) or the model is text-only (MiniMax, DeepSeek). Each result still carries the `autopsy` text (fold-composition breakdown), `northstar`, palette, and fonts, so the model "sees" through text. On the text-only profile (`images=none`) the list tools return a lean shape (`northstar` + palette + fonts); pass `detail:"full"` or call `get_screen` for the full autopsy. Inline images are PNG / JPEG / WebP (never AVIF). |
| `INSPO_MAX_TOKENS` | unset (default) / an integer, 300-200000 | Hard ceiling on what one tool response may spend. Results are formatted concise, then the ranked tail is dropped, then inline thumbnails, until the response fits; the top result and every scalar field (tips, filters, hero guidance) always survive, and trimmed responses carry a `budgetNote` saying how many entries were dropped. Set this when the context window is tight. Every list tool also takes a per-call `maxTokens` argument, which wins over the env var. On the hosted endpoint, pass `?maxTokens=` in the URL instead. |

### Why a budget matters more here than for a text-only MCP

Tool results do not cost you once: they stay in the conversation and are
re-read on every subsequent turn. In our own A/B evaluation, cache reads
ran 3.3x cache writes, so a result pulled early is paid for many times
over. Inline images are the dominant term - one `recommend` call is
~10 KB of text with images off and ~41 KB with thumbnails on - which is
why the cheapest lever is fewer, better-targeted calls, and the second
cheapest is `images=none`. `INSPO_MAX_TOKENS` is the backstop for when
neither is under your control.

**Zero-config defaults:** when neither knob is set, the server reads the
client name from the MCP handshake. Kimi CLI, OpenCode, Cline, Roo,
Crush, Goose, Aider, Continue, Droid, and iFlow get `lite` + text-only;
Kilo and Qwen Code get `lite` + thumbnails (their image path works);
everything else (Claude Code, Cursor, ...) keeps `full` + thumbnails.
Env vars always win. The hosted endpoint defaults to `full` + `images=thumbs`, matching the clients `inspo-mcp install` actually wires up (Claude Code, Cursor, VS Code, Windsurf, Zed, Claude Desktop - all of which read images). The stateless HTTP transport can't read the client name, so text-only harnesses opt DOWN explicitly: `https://inspomcp.dev/api/mcp?profile=lite&images=none`. Over stdio, clientInfo auto-detection still does this for you.

Schemas are flat (no `$ref`, no `$schema`, no `additionalProperties`)
to satisfy strict validators (Moonshot's API, Together's
function-calling layer, vLLM/xgrammar constrained decoding), and
argument parsing is tolerant: `"Dark"`, `"Bento Grid"`, `limit: "8"`,
out-of-range limits, and bare domains (`stripe.com`) are all accepted.
Slug misses return `didYouMean` suggestions so the model can
self-correct in one step.

```jsonc
// Example: Kimi CLI (~/.kimi/mcp.json), explicit; auto-detection
// would land on the same settings
{
  "mcpServers": {
    "inspo": {
      "command": "npx",
      "args": ["-y", "inspo-mcp"],
      "env": { "INSPO_PROFILE": "lite", "INSPO_IMAGES": "none" }
    }
  }
}
```

## Run / develop

```bash
pnpm --filter @inspo/mcp start            # stdio server
pnpm --filter @inspo/mcp test             # smoke test - boots in-process, lists the tools and exercises the core ones
pnpm --filter @inspo/mcp inspect          # MCP Inspector UI
```

### Deploy the hosted endpoint

The MCP is exposed as a Next.js Route Handler in the web app, so it ships with
the site's Vercel deployment - deploying `apps/web` deploys the endpoint too.
Once the site is up, point clients at:

```
https://<your-domain>/api/mcp
```

The route serves the seed bundled into the web build and fetches the embedding
sidecar from the CDN once per lambda for the vector tools (`INSPO_CATALOGUE_URL`
overrides the store). Re-run `publish-catalogue-to-blob.ts` after seed changes:

```bash
pnpm --filter @inspo/worker exec tsx src/publish-catalogue-to-blob.ts --go
```

## Security

- **Read-only.** No write/mutate tools; the server only reads the curated catalogue.
- **No secrets in the response surface.** The hosted route serves the static seed and reads only optional keys (`TOGETHER_API_KEY`, `INSPO_CATALOGUE_URL`) from Vercel environment variables; none are returned to clients. `.env` is gitignored; only `.env.example` is tracked.
- **Free + unauthenticated, abuse-resistant.** The hosted endpoint needs no auth or API key; abuse is contained by a per-IP rate limit (120 requests a minute per warm instance) and a 256 KB request body cap.
- **`get_design_system(live:true)` fetches the screen's own source URL server-side** (HTML + linked CSS only, no JS execution). Every URL (and every redirect) is validated by an SSRF guard before fetch: public http(s) named hosts only, no private / loopback / link-local / cloud-metadata or IP-literal targets, ports 80/443 only. The response body is byte-capped while streaming, and the hosted route adds a request body cap plus a per-IP rate limit.

## Publishing `npx inspo-mcp`

The build esbuild-bundles the stdio server into one self-contained file with a
clean, dependency-free `package.json` - the ~16MB seed is **not** bundled (it's
fetched from the CDN at runtime), so the package stays ~1.5MB.

```bash
pnpm --filter @inspo/mcp build:npm   # → apps/mcp/dist/ (inspo-mcp.mjs + package.json)
node apps/mcp/dist/inspo-mcp.mjs     # optional: smoke-test (speaks MCP on stdio)
cd apps/mcp/dist && npm publish       # needs `npm login`; publishes the public package
```

The monorepo `package.json` stays `private` - only the generated `dist/`
artifact is published, so nothing here leaks. Re-run `build:npm` (and
`publish-catalogue-to-blob.ts`) after seed changes, then bump `VERSION` in
`scripts/build-npm.mjs` and re-publish.

## Files

- `src/server.ts` - stdio entry (monorepo)
- `src/server-npm.ts` - standalone stdio entry for the published package (CDN catalogue)
- `src/install.ts` - `inspo-mcp install`, the per-client config writer
- `src/http-handler.ts` - shared Streamable-HTTP handler (used by the Vercel route)
- `src/tools.ts` - all tool registrations + `HERO_GUIDANCE` (shared by all transports)
- `src/profile.ts` - the lite / full tool surfaces and the images mode
- `src/format.ts` - wire format (absolute URLs, inline image blocks, mobile fields)
- `src/call.ts` - one-shot CLI client (`tsx src/call.ts <tool> '<json>'`)
- `src/smoke.ts` - `pnpm test` · `scripts/build-npm.mjs` - `npx` bundle builder


### apps/mcp/server.json
```json
{
  "$schema": "https://static.modelcontextprotocol.io/schemas/2025-09-29/server.schema.json",
  "name": "io.github.nutlope/inspo",
  "description": "Real production websites for coding agents: palettes, fonts, fold autopsies and reference JSX.",
  "repository": {
    "url": "https://github.com/Nutlope/inspo",
    "source": "github"
  },
  "version": "0.1.15",
  "packages": [
    {
      "registryType": "npm",
      "registryBaseUrl": "https://registry.npmjs.org",
      "identifier": "inspo-mcp",
      "version": "0.1.15",
      "transport": { "type": "stdio" }
    }
  ],
  "remotes": [
    {
      "type": "streamable-http",
      "url": "https://inspomcp.dev/api/mcp"
    }
  ]
}
```

### Root package.json (scripts)
```json
{
  "name": "inspo",
  "private": true,
  "version": "0.0.0",
  "packageManager": "pnpm@9.15.0",
  "scripts": {
    "dev": "turbo run dev",
    "build": "turbo run build",
    "lint": "turbo run lint",
    "typecheck": "turbo run typecheck",
    "capture": "pnpm --filter @inspo/worker capture",
    "capture:seed": "pnpm --filter @inspo/worker capture:seed",
    "capture:retry": "pnpm --filter @inspo/worker capture:retry",
    "db:migrate": "pnpm --filter @inspo/db db:migrate",
    "db:push": "pnpm --filter @inspo/db db:push",
    "db:seed": "pnpm --filter @inspo/db db:seed",
    "db:studio": "pnpm --filter @inspo/db db:studio"
  },
  "engines": { "node": ">=20" }
}
```

## Top-level structure
- `.env.example` — env vars for Together AI, Blob, Postgres, auth
- `.github/` — CI (boilerplate; skipped detail)
- `DEPLOY.md` — Vercel gallery+MCP, Fly.io worker, optional Neon
- `LICENSE` — MIT
- `README.md` — product overview and install paths
- `SEEDING.md` — capture → enrich → publish catalogue pipeline
- `apps/` — monorepo apps:
  - `apps/cli/` — CLI package
  - `apps/mcp/` — TypeScript MCP server (stdio + shared HTTP handler); `src/tools.ts`, `profile.ts`, `server.ts`, `server-npm.ts`, `install.ts`; npm package `inspo-mcp` v0.1.15; registry name `io.github.nutlope/inspo`
  - `apps/web/` — Next.js 16 gallery + hosted MCP route (`/api/mcp`); includes `AGENTS.md` / `CLAUDE.md` (Next.js agent rules)
  - `apps/worker/` — Playwright capture worker (Fly.io); seed/enrich/publish scripts
- `docs/` — `docs/img/` only (OG + with/without comparison images)
- `packages/`:
  - `packages/db/` — Drizzle schema, static seed, optional Postgres/pgvector
  - `packages/shared/` — shared types/utils
  - `packages/taxonomy/` — tag allow-lists (styles, industries, macrostructures, etc.)
- `teaser/` — marketing/teaser assets
- `package.json` / `pnpm-workspace.yaml` / `turbo.json` / `pnpm-lock.yaml` — pnpm + Turborepo workspace
