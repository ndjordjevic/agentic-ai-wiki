# Agentic AI Frameworks wiki — agent instructions

> **Created:** 2026-04-28 | **Detail level:** standard (default; per-source overrides via `<!-- detail:X -->` inbox tags)

---

## For AI agents working in this repo

Before answering **any question** about Agentic AI Frameworks, you MUST:

1. Read `wiki/index.md` to identify relevant pages.
2. Follow `[[wikilinks]]` to drill into relevant source pages.
3. Cite wiki page names in your answer.
4. If the answer is not in the wiki, say so clearly, then fetch current information online instead of relying on training data alone.

This wiki is the authoritative local source for this domain. Start with the wiki, use it whenever it covers the question, and go online for gaps or newer information rather than filling them from training data alone.

> **Phase 1 note:** In Claude Code, use the `/pin-llm-wiki` subcommands (`init`, `add`, `run`, `lint`, `remove`, `queue`) to automate this workflow. In **Cursor** (pin-llm-wiki installed as a [Cursor skill](https://cursor.com/docs/context/skills) under `~/.cursor/skills/pin-llm-wiki` or `.cursor/skills/pin-llm-wiki`), the same `SKILL.md` applies — use `/pin-llm-wiki` in Agent chat or follow the workflow steps below. In **GitHub Copilot** and other tools without the skill, follow the workflow steps below directly — they are fully self-contained.

---

## Git — never auto-commit

**Do not** run `git commit` or `git push` after ingest, refresh, `run`, `lint`, `remove`, initial wiki scaffold, or any other file change in this repo—**unless the human explicitly asked you to commit or push in this conversation.**

When work is done, list what changed and stop; the human reviews diffs and runs `git commit` / `git push` when ready.

---

## Wiki structure

```
wiki/
  index.md          ← start here; lists every page, counts sources
  overview.md       ← rolling cross-source overview (cites [[source pages]])
  log.md            ← append-only record of every ingest/refresh
  sources/          ← one page per ingested source (<slug>.md)
  .archive/         ← soft-deleted sources (ignore unless needed)

raw/
  README.md
  [github/]         ← immutable GitHub repo captures
  [youtube/]        ← immutable YouTube video captures (transcript + metadata)
  [web/]            ← immutable web page/site captures
  assets/           ← downloaded media/binaries

inbox.md            ← agents may add to ## Pending via `queue`; all other edits are human-driven
.pin-llm-wiki.yml   ← config (detail level, source types, lint cadence, etc.)
```

**Load order for any question:** `wiki/index.md` → relevant source pages → raw files only for direct citation.

---

## Ingest workflow

Run this workflow when ingesting a source (via `add` or `run`). Execute steps in order.

**Step 1 — Read the raw file(s).**
The raw file is in `raw/<type>/<slug>...md`. Read it fully before writing any wiki content.

For unified web+github pages: if a `companion_raw_file_path` is passed by the caller (non-null), also read it fully. Hold both in memory. The companion raw supplies content for the github-sourced sections.

For deep multi-product web sources: the caller passes a `products` list with ≥2 entries. The single web raw file contains `## Product: <Name>` sections per product — these drive the umbrella + sub-page output described below.

**Step 2 — Create or update `wiki/sources/<slug>.md`.** Pick the shape that fits this ingest:

| Shape | Trigger | Output |
|---|---|---|
| **Standalone** | github / youtube / single-product web | one source page at `wiki/sources/<slug>.md` |
| **Unified web+github** | `type=web`, companion fetch succeeded, `products` empty | one source page with `companion_urls:` + `raw_files:` |
| **Multi-product** | `type=web`, `effective_detail_level=deep`, `len(products) >= 2` | umbrella `wiki/sources/<slug>.md` + one sub `wiki/sources/<slug>-<product>.md` per product |

See **Frontmatter rules** below for the exact yaml shape per page type. Key constraints:
- `subpages:`, `parent_slug:`, `companion_urls:`, and `raw_files:` are **mutually exclusive**. Lint check #7 enforces this.
- Source pages **never** include `sources:` — they do not cite themselves.
- `product:` is always populated. Derive from the repo (strip author prefix: `obra-superpowers` → `superpowers`) or the domain (strip TLDs: `runcabinet.com` → `cabinet`). Multi-product umbrellas use the umbrella slug itself (e.g. `langchain.com`). Multi-product subs use the product's own slug. Resolved in Step 2b for standalone/unified; explicit in Step 2c for multi-product.

Body conventions (apply to every shape):
- **No H1 heading.** The slug `[[<slug>]]` in `wiki/index.md` is the title. Body starts with a summary paragraph.
- **No `---` horizontal rules** between sections.
- Second line is a **banner citation**: `_All claims below are sourced from ../../raw/<type>/<file>.md unless otherwise noted._` Unified pages cite the **web** raw only; github material is cited inline. Multi-product subs cite the **umbrella's** raw file.
- Per-paragraph inline citations only when a **second** raw file contributes; otherwise the banner covers everything.
- `tags`: 4–8 short kebab-case terms, specific over generic (`claude-code-hooks` > `ai`).
- `related`: slugs of existing pages with substantial overlap. **Bidirectional:** when adding `Y` to this page's `related`, append this page's slug to `Y`'s `related` and bump `Y`'s `updated:` date.

Per-shape body sections (in order — extra top-level sections allowed only for substantial subsystems):
- **GitHub:** What it does · Installation · Key features · Architecture · Example usage · Maintenance status
- **YouTube:** What the video is about (1 paragraph, replaces watching) · Key points by chapter · Notable quotes · Speaker context
- **Web/product (no companion):** What it does · Key features · Architecture / concepts · Main APIs · When to use · Ecosystem
- **Web/product (unified):** see **Unified body structure** below
- **Multi-product umbrella:** see **Multi-product body structure** below
- **Multi-product sub:** same as Web/product (no companion), but banner cites umbrella's raw file

**Unified body structure** (web + companion github). Canonical sections in order:

`What it does` (web) · `Key features` (web + github) · `Architecture` (github) · `Installation` (github) · `Example usage` (github, required even if minimal) · `When to use` (web) · `Maintenance status` (github — stars, release, license) · `Ecosystem` (web) · `Documentation` (web, optional)

Banner cites the **web** raw. Every github-sourced paragraph ends with the inline citation `(../../raw/github/<org>-<repo>.md)`. Do not invent ad-hoc sections (e.g. "Agent integration") — fold into Architecture / Example usage / Ecosystem.

**Multi-product body structure** (deep web, `len(products) >= 2`). One ingest writes the umbrella + one sub per product; all pages cite the **same** raw file at `raw/web/<slug>.md`.

Umbrella sections: `## Products` (bullet list of `[[<slug>-<product>]]` wikilinks, one sentence each) · `## Architecture` (how products fit together) · `## When to use the platform` · `## Documentation`. The umbrella is a **hub** — link to subs, do not duplicate their feature lists.

Sub frontmatter has `parent_slug: <slug>`, `product: <product-slug>`, and `source_url:` set to the product's deep-link page (fallback: umbrella URL). Body uses the Web/product (no companion) sections. Banner cites the umbrella's raw file. If a sub was discovered via repo URL only (no docs subsection), it may be sparse — note that fuller detail requires ingesting the product's repo separately.

**Step 2b — Detect product grouping.** (Multi-product flow assigns `product:` explicitly in Step 2c — skip 2b in that case.) After writing a standalone or unified source page, scan existing `wiki/sources/*.md` to set `product:` such that pages describing the same product share the same slug:
- **GitHub source** → use the homepage hostname from the raw's `## Metadata` block if it matches an existing web slug; otherwise strip the author prefix (`obra-superpowers` → `superpowers`).
- **Web source** → if the raw body contains a `github.com/<org>/<repo>` URL whose `<org>-<repo>` matches an existing github slug, share the web slug as `product:`; otherwise derive from the domain (`runcabinet.com` → `cabinet`). GitHub non-root web pages use the repo segment (`servers` for `/modelcontextprotocol/servers/...`).
- **YouTube** → kebab-case video title or channel name; never auto-grouped.

`product:` must be populated — never `null`. Report any grouping in the post-ingest confirmation.

**Step 3 — No extra cross-source pages.** Ingest writes source pages + `wiki/overview.md` only. The umbrella + subs in multi-product flow are still source pages, not synthesis pages.

**Step 4 — Update `wiki/index.md`.**
- If `<slug>` already has a row in the Sources table: update the date and `detail_level` in-place. Do not add a second row or change the count.
- If no row exists: add `| <slug> | <type> | standard | <YYYY-MM-DD> | |` and increment the source count in the `_N sources ingested._` line.
- **Multi-product:** add a row for the umbrella AND for every sub-page. Increment the count by the number of newly-created rows.

**Step 5 — Update `wiki/overview.md`.** **Invariant:** body paragraph count == `len(sources)`, same order, one paragraph per entry. Verify before writing. The page cites `[[source page slugs]]`, not raw files.

Per slug being ingested:
- Slug already in `sources:` (refresh) → update `updated:` only. Stop.
- `sources: []` (first source) → replace the `_No sources ingested yet..._` placeholder with an opening paragraph citing `[[<slug>]]`; set `sources: ["[[<slug>]]"]`.
- New slug → append a dedicated paragraph (don't merge) describing what this source adds; append `- "[[<slug>]]"` to `sources:`.

**Multi-product:** umbrella and each sub are separate entries. Umbrella first, subs in `subpages:` order. Umbrella's paragraph may wikilink each sub; sub paragraphs link back to the umbrella.

**Step 6 — Append to `wiki/log.md`** (newest at top):
```
## YYYY-MM-DD | ingest | <slug> | <one-line summary>

- Created: wiki/sources/<slug>.md
- Updated: wiki/index.md, wiki/overview.md, wiki/log.md, raw/<type>/README.md, inbox.md
```

Variants:
- **Unified:** Updated line includes both `raw/web/README.md` and `raw/github/README.md`. Add `- Companion: raw/github/<companion-slug>.md` (required).
- **Multi-product:** title is `multi-product (<N> products): <names>`; Created line lists umbrella + every sub.

**Step 7 — Update `raw/<type>/README.md`** — update the row in-place if it exists, else append using the row format from the type's protocol. Multi-product still produces one raw web file → one row.

**Step 8 — Move inbox line** from `## Pending` to `## Completed`. Append `<!-- ingested YYYY-MM-DD -->`. If `auto_mark_complete: true`, also flip `[ ]` → `[x]`.

**Step 9 — Git** — skip. See SKILL.md Git policy.

### Merge rules (overview.md)

Add new facts; don't duplicate. On conflict: insert a `> **Conflict:**` block citing both sources. Source authority: official docs > GitHub README > YouTube (official channel) > blogs / secondary.

---

## Source type protocols

### GitHub fetch protocol

**Trigger:** inbox URL matches `github.com/<org>/<repo>`.
**Tool:** `gh` CLI.

Steps:

1. `gh repo view <org>/<repo> --json name,description,url,homepageUrl,stargazerCount,forkCount,pushedAt,primaryLanguage,licenseInfo,defaultBranchRef` — capture metadata and default branch name.
2. `gh release list --repo <org>/<repo> --limit 1` — capture latest release tag.
3. `gh api repos/<org>/<repo>/readme` — base64-decode and capture full README.
4. `gh api repos/<org>/<repo>/contents/` — top-level structure listing.
5. If `docs/` exists: list contents + fetch key files (guides, architecture, testing, overview).
6. If `examples/` exists: list structure only (do not fetch full example files unless `deep`).
7. Skim other top-level folders; annotate important ones (source/lib, plugin manifests, tests, agent instruction files `CLAUDE.md` / `AGENTS.md` / `GEMINI.md`); skip boilerplate (`.github/`, `node_modules/`, lock files).
8. Compile into a single file and save to `raw/github/<org>-<repo>.md`.
9. Use `defaultBranchRef.name` from step 1 as the branch. **Never assume `main`.** Override with `<!-- branch:X -->` inbox tag if present.
10. At `deep` detail with `<!-- clone -->` inbox tag: `git clone https://github.com/<org>/<repo>.git raw/github/<org>-<repo>/` (this path is gitignored; full clone tree for deep citation).

**Guard:** if the repo fetch would exceed 200k input tokens, halt and surface to the user before proceeding.

**Raw file format** (`raw/github/<org>-<repo>.md`):
```
# <org>/<repo>

## Metadata
- Stars: <N>
- Primary language: <lang>
- Default branch: <branch>
- Latest release: <tag> (<date>)
- License: <license>
- Homepage: <url>
- Fetched: <YYYY-MM-DD>
- Final URL: <url>

## Description
<description>

## README
<full readme content>

## Docs
<fetched doc files, one section each>

## Top-level structure
<annotated directory listing>
```

Notes:
- `## README` is the fetched README content itself, not a paraphrase, rewrite, or condensed summary.
- `## Docs` is required whenever docs or other key repo docs were fetched during the protocol. Include the fetched content you relied on, organized one section per file/listing.
- `## Top-level structure` should remain an annotated directory listing, but annotation must stay grounded in the fetched listing.

**README.md row format** (`raw/github/README.md`):
`| raw/github/<org>-<repo>.md | <org>/<repo> | <stars> | <default-branch> | <latest-release> | <YYYY-MM-DD> | |`

### YouTube fetch protocol

**Trigger:** inbox URL matches `youtube.com/watch?v=` or `youtu.be/`.
**Tool:** `yt-dlp`.

Steps:

1. `yt-dlp --dump-json <url>` — one call; captures description, chapters, title, channel, duration, upload date, video ID. No download.
2. Transcript: `yt-dlp --write-auto-sub --skip-download --sub-lang en-orig <url>`
   - Prefer `--sub-format srt` when available.
   - Fall back to `--sub-format vtt` if SRT unavailable.
   - Prefer `en-orig` (unprocessed captions) over `en` (auto-translated).
3. Parse subtitles:
   - **SRT format:** use standard cue text per block. Join consecutive cues that belong to the same sentence.
   - **VTT rolling-caption format:** each cue has 2 lines; the last line is live/partial. Strategy: take the **first clean line per cue** (strip `<c>` timing tags). Deduplicate consecutive identical lines. Group transcript text by chapter heading (from step 1 `--dump-json` chapters array).
4. Save to `raw/youtube/<video-id>-<slug>.md`.
5. **Fallback:** if no transcript track exists at all, flag the inbox line `<!-- fetch-failed:no-transcript -->` and skip (do not mark `[x]` or move to Completed).

**Guard:** if the video transcript would exceed 200k input tokens during ingest, surface to user before proceeding.

**Slug generation:** lowercase title, replace spaces/special chars with hyphens, truncate at 40 chars.

**Raw file format** (`raw/youtube/<video-id>-<slug>.md`):
```
# <title>

## Metadata
- Video ID: <id>
- Channel: <channel>
- Duration: <MM:SS or HH:MM:SS>
- Upload date: <YYYY-MM-DD>
- URL: <url>
- Fetched: <YYYY-MM-DD>

## Description
<full description text>

## Chapters
| # | Title | Timestamp |
|---|---|---|
<chapter rows>

## Transcript

### <Chapter 1 Title> (0:00)
<cleaned transcript text>

### <Chapter 2 Title> (MM:SS)
<cleaned transcript text>
...
```

**README.md row format** (`raw/youtube/README.md`):
`| raw/youtube/<video-id>-<slug>.md | <title> | <channel> | <duration> | <upload-date> | <YYYY-MM-DD> | |`

### Web fetch protocol

**Trigger:** inbox URL does not match github.com or youtube patterns.
**Tool:** `WebFetch` (primary). Fallbacks: Jina Reader (`r.jina.ai/<url>`) or headless browser only if WebFetch returns a content-free skeleton.

**Verbatim-capture rule (critical for product discovery):** WebFetch passes the page through a small summarizer model. Even with explicit "do not summarize" instructions, it may still paraphrase prose and silently drop "redundant" entries from product menus, nav lists, and structured catalogs — the exact signals product discovery (Step 5) depends on. The directive helps but is not a guarantee. Two rules follow:

1. **For HTML pages (landing page, docs index, individual docs pages):** every WebFetch prompt **must** include: *"Return the page content verbatim. Preserve every product name, navigation entry, link, and list item exactly as it appears. Do not summarize, paraphrase, deduplicate, or filter for relevance."*
2. **For plain-text structural catalogs (`llms.txt`, `sitemap.xml`):** do **not** use WebFetch — its summarizer will mangle the catalog. Fetch with `curl -sL <url>` via Bash and store the raw response. These files are the only fully reliable product-enumeration source, so they must survive intact.

**Special case — GitHub non-root pages:** when the URL is `github.com/<org>/<repo>/<...>` (for example `/tree/...`, `/blob/...`, `/issues/...`), this protocol runs in **single-page mode**. The intent is to capture only the requested GitHub page, not the whole repository.

Steps:

1. **Check whether the URL is a GitHub non-root page.**
   - **If yes:** skip steps 2–6 below entirely. Fetch only the exact URL and store it as a one-page raw capture. Do **not** fetch `llms.txt`, do **not** discover docs pages, and do **not** discover a companion GitHub repo or run product discovery. Return `companion_github_url = null`, `products = []`. Skip ahead to step 8 (write).
   - **If no:** continue with step 2.
2. **Check `<domain>/llms.txt`** — fetch with: `curl -sL https://<domain>/llms.txt -o /tmp/pin-llm-wiki-llmstxt-<slug>.txt`. **Do not** invoke WebFetch on llms.txt — the WebFetch summarizer mangles it. Always go through the on-disk file.

   After curl, `cat /tmp/pin-llm-wiki-llmstxt-<slug>.txt | wc -c` to verify a non-empty response. If empty / 404 / not-found-style HTML, treat llms.txt as absent and skip to step 3.

   **The on-disk file is the canonical capture.** When step 8 assembles the raw file, the `## llms.txt — <url>` section is produced by **reading** `/tmp/pin-llm-wiki-llmstxt-<slug>.txt` and inserting its contents verbatim. Do not retype the content from memory; do not summarize; do not "list relevant entries." If you find yourself paraphrasing the catalog, stop — read the on-disk file again and paste those bytes literally. Step 5 discovery operates on this raw section; if it has been summarized, DeepAgents-class entries are silently dropped and discovery can never recover them.

   llms.txt is the primary product-discovery signal in Step 5; every line must reach Step 5 unfiltered. llms.txt supplements but does **not** replace steps 3–5.
3. **Fetch the landing page** (`<final-url>`). Capture verbatim. In particular, preserve the literal text of the hero section, primary nav, "Products" / "Frameworks" menus, product cards, and footer link blocks — these enumerate products that may not appear anywhere else. Paraphrased summaries of these elements are insufficient for Step 5.
4. **Discover docs pages** — always, regardless of whether llms.txt was found. Try `/docs`, `/documentation`, `/guide`, `sitemap.xml`, and the conventional subdomain `docs.<domain>` (in that order). Stop at the first that returns real content. For `sitemap.xml`, fetch with `curl -sL` (it is a structural catalog like llms.txt). For HTML docs pages, use WebFetch with the verbatim directive — capture the full top-level navigation tree, every section heading and link, not a paraphrase. Top-level docs sections are the strongest product-discovery signal.
   - At `brief`: skip docs entirely.
   - At `standard`: fetch the docs index page and ~4–10 key pages (product overviews, getting-started, architecture, reference).
   - At `deep`: fetch the docs index page and ~10–25 key pages, then run product discovery (step 5) and per-product docs fetch (step 6).
5. **Product discovery** (`deep` only — skipped at `brief`/`standard` and in single-page mode). The goal is to determine whether this site presents **multiple distinct products** that each merit their own wiki source page.

   Scan, in priority order:
   a. The docs nav/landing of the docs site discovered in step 4 — top-level sections that point to distinct product subsections (for example `docs.langchain.com/langchain/...`, `docs.langchain.com/langgraph/...`, `docs.langchain.com/langsmith/...`).
   b. The landing page hero/nav and footer for product-card lists, "Products" menus, or repeated `<product>.<domain>` subdomains.
   c. The llms.txt content from step 2 — distinct product entries point to distinct products.
   d. GitHub repo URLs referenced anywhere in the captured content — multiple repo-root URLs under the same `<org>` are strong evidence of multiple products (for example `github.com/langchain-ai/langchain`, `github.com/langchain-ai/langgraph`, `github.com/langchain-ai/langsmith`, `github.com/langchain-ai/deepagents`).

   **Acceptance threshold (must hold for a candidate to count as a product):**
   - The candidate has its own dedicated docs subsection (its own URL path under the docs site or its own subdomain), **OR** its own distinct repo-root GitHub URL under the same org.
   - The candidate is **not** a generic site section like `Pricing`, `Features`, `Solutions`, `Customers`, `Blog`, `About`, `Careers`, `Contact`, `Login`, `Sign up`, `Changelog`, `Roadmap`, `Status`, `Legal`, `Terms`, `Privacy`. Reject these by name even if they appear in nav.

   **Output:** a list `products`, each entry: `{ name, slug, deep_link_url?, docs_url?, repo_url? }`.
   - `name` — display name, e.g. `LangGraph`.
   - `slug` — kebab-case product identifier, e.g. `langgraph`. Used in sub-page slug `<domain>-<slug>`.
   - `deep_link_url` — product-specific page on the source site if one exists (e.g. `https://www.langchain.com/langgraph`); null otherwise.
   - `docs_url` — entry point into this product's docs subsection if discovered.
   - `repo_url` — companion GitHub repo URL if one was matched.

   **Sanity check (mandatory before accepting `products`).** This step is what protects against missed products. Skipping or shortcutting it is the most common cause of incomplete ingests. Run it explicitly:

   **Step 5a — Build the candidate set from llms.txt and sitemap.xml** (the curl-fetched ground truth):
   - Parse the curl output of `llms.txt` and `sitemap.xml`. Collect every URL.
   - For every URL on the docs host (`docs.<domain>` or `<domain>/docs/`), extract its path segments and emit candidates at **depths 1, 2, and 3** simultaneously. For example, the URL `https://docs.langchain.com/oss/python/deepagents/quickstart` emits three candidates: `oss`, `oss/python`, and `oss/python/deepagents`. Many sites nest products under generic prefixes like `/oss/`, `/api/`, `/docs/`, `/products/` — depth-1 enumeration alone will miss them.
   - For every URL on a separate `docs.<subdomain>.<domain>` or `<subdomain>.<domain>` host, the subdomain is also a candidate.
   - Also collect: section headings (lines starting with `## ` or `# `) from llms.txt — these are the curated product list and outrank any URL heuristic, every product-card / framework-card name from the landing page capture, every `github.com/<org>/<repo>` repo-root URL.

   **Step 5b — Identify product nodes.** A path candidate is a **product node** when it satisfies any of:
   - It appears as a `## ` or `# ` heading in llms.txt with associated URLs underneath (the strongest signal — trust llms.txt section headings as products by default).
   - It has its own coherent docs cluster: ≥3 distinct child URLs underneath, or includes conventional docs-page names like `/overview`, `/quickstart`, `/getting-started`, `/home`, `/concepts`, `/reference`.
   - It appears as a product card / framework card on the landing page.
   - It corresponds to a `github.com/<org>/<repo>` repo-root URL under the same org as other discovered products.

   Generic intermediate path nodes (`oss`, `python`, `javascript`, `api`, `docs`, `guide`) are **not** products on their own — they are namespace containers. Products live one or more levels under them.

   **Step 5c — Classify every candidate.** For each candidate from step 5a, classify as exactly one of:
   - **Product** — passes step 5b. Must appear in `products`. If absent, add it (derive `slug`, `docs_url`, `repo_url`, `deep_link_url` from where it appeared in the captures).
   - **Excluded section** — matches the rejection list by name (Pricing, Features, Solutions, Customers, Blog, About, Careers, Contact, Login, Sign up, Changelog, Roadmap, Status, Legal, Terms, Privacy, plus generic namespace containers like `oss`, `api`, `docs`).
   - **Sub-section of an existing product** — lives under a path already represented in `products` (e.g. `oss/python/langgraph/interrupts` lives under `oss/python/langgraph` which is the LangGraph product node).

   If any candidate falls into none of these three buckets, it was missed: add it to `products`. Repeat until every candidate is accounted for.

   **Step 5d — Audit trail (mandatory).** Append a `## Discovery audit` section to memory (will be written to the raw file in step 8) listing every candidate from step 5a and its classification. The audit makes the enumeration verifiable instead of "the agent says it ran the check." If the audit lists fewer products than llms.txt has top-level section headings, something was skipped.

   If the verbatim captures are too thin to enumerate (e.g. the landing page returned paraphrased prose despite the verbatim directive, or llms.txt was summarized away in step 2), refetch with a stricter prompt before continuing — do not classify candidates from a paraphrase.

   **Multi-product trigger:** `len(products) >= 2`. If `len(products) < 2`, set `products = []` and proceed in single-product deep mode (step 6 skipped, step 7 simplified).
6. **Per-product docs fetch** (deep multi-product only — runs only when `len(products) >= 2`).

   For each entry in `products`, fetch ~5–10 key docs pages from its `docs_url` subsection: overview / getting started / key concepts / API or reference / when-to-use. Hold each set in memory keyed by product slug.

   If a product was discovered via repo URL only (no `docs_url`), skip per-product docs fetch for that product — its sub-page will be sparser, and the human can promote it to a full unified ingest later via `companion:` override on a separate `add` call.
7. **Companion GitHub repo discovery.**

   **Skipped entirely in deep multi-product mode** (`len(products) >= 2` from step 5): immediately set `companion_github_url = null` and proceed to step 8. The umbrella does not get a single companion repo; each product's `repo_url` (if any) is recorded in `products[*].repo_url` for the human to ingest separately if desired.

   In all other modes (brief, standard, single-product deep), scan the collected content in this priority order:
   a. The llms.txt content captured in step 2 (look for any `github.com/<org>/<repo>` line).
   b. The landing page's first ~500 characters (hero section, navigation bar).
   c. Any anchor text on the landing page containing `github.com/<org>/<repo>` (footer, "open source", "view on GitHub" links).

   Accept a URL only when it has exactly two non-empty path segments after `github.com/` and is a repo root — reject `/tree/`, `/blob/`, `/orgs/`, `/issues/`, `/pulls/`, etc.

   **Tie-break:** when multiple repo URLs appear, prefer the one whose `<org>` is most similar to the domain root (e.g. `paperclip.ing` → prefer `paperclipai/*`). If still tied, take the first in priority order.

   Return the result as `companion_github_url` (a full URL string or `null`). **Do not fetch the repo here** — the caller (`add.md` / `run.md`) decides whether to fetch, applying any inbox-line tag overrides (`<!-- companion:... -->`, `<!-- no-companion -->`) before doing so.
8. **Compile and write the raw file.** Always one file per ingest at `raw/web/<slug>.md` — no per-page directories. The file format is described below; deep multi-product mode adds `## Product: <name>` sections.

   **Mandatory post-write integrity check (deep mode only).** After writing the raw file, re-read it and verify:
   - Contains a `## Discovery audit` section with non-empty candidate lists. **If absent, the discovery sanity check (step 5d) was skipped — abort the ingest with the error: "Discovery audit missing in raw file `<path>` — Step 5 sanity check was skipped or output was lost. Re-run after fixing the discovery flow." Do not proceed to ingest. Surface the error to the user.**
   - Contains a `## llms.txt — <url>` section (if llms.txt was non-empty in step 2) whose body is the verbatim curl output. Spot-check by computing `wc -l` of the section body vs `wc -l` of `/tmp/pin-llm-wiki-llmstxt-<slug>.txt`; if the section is significantly shorter (e.g. <50% of the line count), it was summarized — abort with: "llms.txt section in `<path>` is paraphrased, not verbatim. Re-fetch and paste the curl output literally."
   - In `deep-multi-product` mode: `Products discovered: N` in the fetch log equals the number of `## Product:` sections in the body. If they disagree, abort with a structural-mismatch error.

   These checks are load-bearing. They convert step 5d ("write the audit") from an instruction the agent can ignore into a hard precondition for ingest. A skipped check fails the run loudly.
9. **Follow redirects; log the final URL** to the raw file — not the original inbox URL. Stale domains silently redirect.
10. Respect `robots.txt`. Set a descriptive user agent. Rate-limit between requests.

**Returned to caller:** `companion_github_url`, `products` (list, possibly empty), `final_url`, `pages_count`. The caller (`add.md` / `run.md` / refresh) reads `products` and `companion_github_url` to decide which ingest branch to use.

**Guard:** if the cumulative crawl would exceed 200k input tokens, halt and surface to user before proceeding. In deep multi-product mode this is especially important — 4 products × 10 docs pages each will brush the limit; if the budget is tight, prefer fewer pages per product over fewer products.

**Raw file format** (`raw/web/<slug>.md`):
```
# <slug>

## Fetch log
- Inbox URL: <original url>
- Final URL: <final url after redirects>
- Fetched: <YYYY-MM-DD>
- Pages: <N>
- Mode: <single-page | brief | standard | deep | deep-multi-product>
- Products discovered: <N>     ← present only when Mode is deep or deep-multi-product
- Products: <comma-separated slugs>     ← present only when N >= 1

## llms.txt — <https://<domain>/llms.txt>     ← present if curl returned a non-empty catalog response
<verbatim curl response — every line, every section heading, every URL — DO NOT summarize, DO NOT list "relevant entries"; the curl bytes go here>

## Discovery audit     ← present at deep mode only; written from Step 5d
- Candidates from llms.txt (depth 1/2/3): <list>
- Candidates from landing page: <list>
- Candidates from sitemap.xml: <list>
- Candidates from GitHub URLs: <list>
- Classified as products: <list>
- Classified as excluded: <list — and why>
- Classified as sub-section of existing product: <list — and which parent>

## Landing page — <final-url>
<page content>

## Docs — <docs-index-url>     ← present at standard and deep
<docs index page content>

## <Page title> — <url>     ← additional docs/key pages at standard and deep (single-product)
<page content>
...

## Product: <Product Name>     ← present per-product in deep multi-product mode only
- Slug: <product-slug>
- Deep link: <deep_link_url or "n/a">
- Docs URL: <docs_url or "n/a">
- Companion repo: <repo_url or "n/a">

### About
<short description from landing/hero/docs intro for this product>

### Docs — <docs_url>
<fetched docs index for this product>

### <Doc page title> — <url>
<fetched docs page content>
...
```

`Pages: <N>` counts every captured item in the compiled raw file, including `llms.txt` when present. For example, `llms.txt + landing page + 4 docs pages` means `Pages: 6`. In deep multi-product mode, sum across all `## Product:` sections too.

In **GitHub non-root single-page mode**, the compiled raw file contains only:
```
# <slug>

## Fetch log
- Inbox URL: <original url>
- Final URL: <final url after redirects>
- Fetched: <YYYY-MM-DD>
- Pages: 1
- Mode: single-page

## Page — <final-url>
<page content>
```

**README.md row format** (`raw/web/README.md`):
`| raw/web/<slug>.md | <slug> | <pages-fetched> | <YYYY-MM-DD> | |`

---

## Citation rules

1. **Every factual claim must have a citation chain to a raw file.** No citation → no claim.
2. **Source pages** use a banner citation at the top. Add per-paragraph inline citations only when a second raw file contributes to the page.
3. **`wiki/overview.md`** lists contributing source pages in `sources:` frontmatter and cites `[[source pages]]` via wikilinks — not raw files directly.
4. **Citation path format:** always relative-from-file.
   - From `wiki/sources/`: `../../raw/<type>/<file>.md`
   - Never root-relative (`/raw/...` or `raw/...` without `../` prefix).
5. **Obsidian compatibility:** wikilinks in frontmatter use list form — `- "[[slug]]"`, not inline `[[slug]]` arrays.

---

## Frontmatter rules

**All source pages** (`wiki/sources/*.md`) carry these fields. **MUST NOT** include `sources:` — source pages do not cite themselves.

```yaml
---
type: source
source_url: <canonical URL of the source>
tags: []
related: []
product: <product-slug>      # see Step 2 derivation rules
detail_level: standard
created: YYYY-MM-DD
updated: YYYY-MM-DD
---
```

**Shape-specific additions** (mutually exclusive — lint Check #7 enforces):

| Shape | Add |
|---|---|
| Standalone | nothing |
| Unified web+github | `companion_urls: [https://github.com/<org>/<repo>]` and `raw_files: [../../raw/web/<domain>.md, ../../raw/github/<org>-<repo>.md]` |
| Multi-product umbrella | `subpages: [<slug>-<product1>, <slug>-<product2>, ...]`. Umbrella's `product:` is the umbrella slug itself (e.g. `langchain.com`). |
| Multi-product sub | `parent_slug: <umbrella-slug>`. Sub's `product:` is the product's own slug (e.g. `langgraph`). |

**Overview page** (`wiki/overview.md`):
```yaml
---
type: overview
domain: "<domain>"
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources:
  - "[[source-slug-1]]"
  - "[[source-slug-2]]"
---
```

---

## Refresh workflow

Add `<!-- refresh -->` to a source's `## Completed` line in `inbox.md`, then run `/pin-llm-wiki run`. The run command re-fetches each tagged source, compares (after stripping date-shaped frontmatter), and re-renders if changed.

Refresh shape rules (additive within shape):
- **Multi-product umbrella** can gain new sub-pages when discovery finds a new product. Existing subs are never auto-dropped (use `remove <sub-slug>`).
- **Sub-page** refresh is rejected — refresh the umbrella instead.
- **Standalone / unified** pages are not auto-promoted to multi-product even if discovery returns ≥2 products. That shape change requires `remove + re-add`.
- **Unified** pages do not gain or lose companions on refresh.

For exact mechanics (companion-context reconstruction, products-list merge with stale-entry preservation, partial-failure handling) see `skill/run.md` Pass 2.

---

## Lint checks

Run `/pin-llm-wiki lint` to check wiki health.

| # | Check | Severity |
|---|---|---|
| 1 | Citation coverage — every factual claim has a chain to a raw file | ERROR (WARN on overview.md) |
| 2 | Contradictions — conflicting claims across pages | WARN |
| 3 | Orphan pages — no inbound `[[wikilinks]]` (includes overview.md and log.md) | WARN |
| 4 | Missing cross-references — page mentions a wiki-known entity without linking | WARN |
| 5 | Stale sources — last refresh > 30 days | INFO |
| 6 | Terminology collisions — same term used for different concepts across sources | WARN |
| 7 | Frontmatter shape — source pages must NOT have `sources:` | ERROR |
| 8 | Citation path format — must be relative-from-file, not root-relative | ERROR |
| 9 | Inbox consistency — inbox line marked [x] but still under ## Pending | WARN |
| 10 | Adapter sync — `.cursor/rules/wiki-instructions.mdc` body and `.github/copilot-instructions.md` must match `AGENTS.md` | WARN (auto-fixed) |
| 11 | Split-product sources — web and github source pages share `product:` but lack `companion_urls` (skipped for multi-product subs, which downgrade to INFO) | WARN |
| 12 | Parent-child consistency — every umbrella's `subpages:` entry has a matching sub with the right `parent_slug:`, and vice versa | ERROR |

Auto-fixes applied on every lint run:
- Missing `overview.md` / `log.md` links in `wiki/index.md`.
- Re-sync `.cursor/rules/wiki-instructions.mdc` and `.github/copilot-instructions.md` from `AGENTS.md` when Check #10 detects drift (preserves the Cursor file's YAML frontmatter).

Checks #2 (contradictions) and #6 (terminology collisions) are deferred in Phase 1 — reported as informational notes only.

---

## Queue workflow

Agents (human-directed or autonomous) may suggest URLs for later ingest without immediately fetching them.

`/pin-llm-wiki queue <url> [<url> ...]` — adds one or more URLs to `inbox.md`'s `## Pending` section and stops. No fetch, no ingest, no wiki pages touched. The human reviews the list and triggers ingest when ready via `/pin-llm-wiki run` or `/pin-llm-wiki add <url>`.

**When to use `queue` vs `add`:**
- **`queue`**: you discovered a potentially relevant source mid-task and want to surface it for human review without interrupting the current flow.
- **`add`**: you have been explicitly asked to ingest a specific source right now.

**Rules:**
- `queue` is the **only** inbox mutation an agent may perform outside of the `add`, `run`, and `remove` workflows.
- Supported inline tags (appended after the URL, same syntax as the inbox header):
  - `<!-- detail:brief|standard|deep -->` — override detail level for this source
  - `<!-- branch:X -->` — GitHub: use this branch instead of default
  - `<!-- clone -->` — GitHub deep: full git clone
  - `<!-- skip -->` — queue the URL but skip it on the next `run`
  - `<!-- companion:github.com/<org>/<repo> -->` — web only; skip GitHub discovery, use this exact repo as the companion
  - `<!-- no-companion -->` — web only; suppress companion GitHub fetch even if a repo is found
  - `<!-- note: <text> -->` — freeform rationale visible to the human reviewer (ignored by all other subcommands)
- Never run `git commit` after `queue` — see **Git — never auto-commit**.

---

## Remove workflow

`/pin-llm-wiki remove <slug>`:
1. Validate slug exists in `wiki/index.md` Sources table.
2. Determine the page shape from frontmatter (`raw_files:` → unified; `subpages:` → multi-product umbrella; `parent_slug:` → multi-product sub; otherwise standalone).
3. Soft-delete:
   - **Standalone:** move `wiki/sources/<slug>.md` to `wiki/.archive/sources/`. Archive `raw/<type>/<slug>.md` and `raw/<type>/<slug>/` (deep clone directory) only.
   - **Unified:** archive every raw file listed in `raw_files:` plus a sibling deep-clone directory if present.
   - **Multi-product umbrella (cascade):** also archive every sub-page listed in `subpages:`. The single web raw file is archived once (it backed the umbrella + all subs).
   - **Multi-product sub:** archive only the sub's wiki page. The raw file stays (it still backs the umbrella + remaining subs). Update the umbrella: remove this sub from its `subpages:` list and from any `## Products` bullet, bump its `updated:` date.
4. Update `wiki/index.md` (remove row(s), decrement count by the number of pages archived) and `wiki/overview.md` (remove each archived slug from `sources:` and delete its paragraph; the invariant `len(sources) == paragraph_count` must still hold). Append to `wiki/log.md`.
5. Scan surviving pages for dangling `[[wikilinks]]` and raw citations that still reference any archived slug.
6. Report findings to the user; do not auto-rewrite the surviving pages. Run `/pin-llm-wiki lint` afterward for full wiki validation.
7. **To undo:** files are in `wiki/.archive/`. Move them back to their original paths and restore the index.md rows, the overview.md frontmatter entries, and the overview.md body paragraphs manually.

---

## Consolidating split-product sources

If lint Check #11 fires (web + github source pages share `product:` but are not unified): `/pin-llm-wiki remove <github-slug>`, then re-add the web URL with `/pin-llm-wiki run`. The unified-ingest flow regenerates a single source page citing both raw files. Run `/pin-llm-wiki lint` afterward to confirm no dangling `[[<github-slug>]]` references remain. Manual consolidation steps (without re-fetching) are documented in `skill/lint.md`.
