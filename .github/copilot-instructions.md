# Agentic AI wiki — agent instructions

> **Created:** 2026-04-25 | **Detail level:** standard (default; per-source overrides via `<!-- detail:X -->` inbox tags)

---

## For AI agents working in this repo

Before answering **any question** about Agentic AI, you MUST:

1. Read `wiki/index.md` to identify relevant pages.
2. Follow `[[wikilinks]]` to drill into relevant source, topic, and synthesis pages.
3. Cite wiki page names in your answer.
4. If the answer is not in the wiki, say so clearly — **do not infer from training data**.

This wiki is the authoritative source for this domain. Training-data knowledge about Agentic AI is noise here; the wiki is signal.

> **Phase 1 note:** In Claude Code, use the `/pin-llm-wiki` subcommands (`init`, `add`, `run`, `lint`, `remove`) to automate this workflow. In **Cursor** (pin-llm-wiki installed as a [Cursor skill](https://cursor.com/docs/context/skills) under `~/.cursor/skills/pin-llm-wiki` or `.cursor/skills/pin-llm-wiki`), the same `SKILL.md` applies — use `/pin-llm-wiki` in Agent chat or follow the workflow steps below. In **GitHub Copilot** and other tools without the skill, follow the workflow steps below directly — they are fully self-contained.

---

## Git — never auto-commit

**Do not** run `git commit` or `git push` after ingest, refresh, `run`, `lint`, `remove`, initial wiki scaffold, or any other file change in this repo—**unless the human explicitly asked you to commit or push in this conversation.**

When work is done, list what changed and stop; the human reviews diffs and runs `git commit` / `git push` when ready.

---

## Wiki structure

```
wiki/
  index.md          ← start here; lists every page, counts sources
  overview.md       ← rolling synthesis of all sources (cites [[source pages]])
  log.md            ← append-only record of every ingest/refresh
  sources/          ← one page per ingested source (<slug>.md)
  topics/           ← cross-source concept pages (created at lint time)
  syntheses/        ← deep-dive documents (manual, human-driven)
  .archive/         ← soft-deleted sources (ignore unless needed)

raw/
  README.md
  [github/]         ← immutable GitHub repo captures
  [youtube/]        ← immutable YouTube video captures (transcript + metadata)
  [web/]            ← immutable web page/site captures
  assets/           ← downloaded media/binaries

inbox.md            ← human-owned; agent only touches it within defined workflows
.pin-llm-wiki.yml   ← config (detail level, source types, lint cadence, etc.)
```

**Load order for any question:** `wiki/index.md` → relevant source/topic pages → raw files only for direct citation.

---

## Ingest workflow

Run this workflow when ingesting a source (via `add` or `run`). Execute steps in order.

**Step 1 — Read the raw file.**
The raw file is in `raw/<type>/<slug>...md`. Read it fully before writing any wiki content.

**Step 2 — Create or update `wiki/sources/<slug>.md`.**

Frontmatter:
```yaml
---
type: source
tags: []
related: []
detail_level: standard
created: YYYY-MM-DD
updated: YYYY-MM-DD
---
```

Rules:
- **MUST NOT include a `sources:` field.** Source pages do not cite themselves.
- First line of body: summary paragraph (what this source is and why it matters).
- Second line: banner citation — `_All claims below are sourced from ../../raw/<type>/<file>.md unless otherwise noted._`
- Then: sectioned body. Per-type structure:
  - **GitHub:** what it does, installation, key features, architecture, example usage, maintenance status.
  - **YouTube:** what the video is about (1 paragraph — sufficient to replace watching), key points by chapter, notable quotes, speaker context.
  - **Web/product:** what it does, key features, architecture/concepts, main APIs, when to use, ecosystem.
- Add per-paragraph citations only when a **second** raw file contributes to this page; otherwise the banner covers it.

**Step 3 — Do NOT create topic pages.** Topic page creation happens at lint time only.

**Step 4 — Update `wiki/index.md`.**
- If `<slug>` already has a row in the Sources table: update the date and `detail_level` in-place. Do not add a second row or change the count.
- If no row exists: add `| <slug> | <type> | standard | <YYYY-MM-DD> | |` and increment the source count in the `_N sources ingested._` line.

**Step 5 — Update `wiki/overview.md`.**
Read `wiki/overview.md` and check the `sources:` frontmatter list:
- **If `[[<slug>]]` is already in `sources:`** (refresh case): update the `updated:` date only. Write the file. Stop — do not add another entry or another paragraph.
- **If `sources: []` (first source ever ingested):** replace the placeholder body (the `_No sources ingested yet..._` paragraph) with an opening synthesis paragraph describing this source and what it contributes. Cite `[[<slug>]]`. Update `sources:` to `sources:\n  - "[[<slug>]]"`.
- **If `sources:` already has entries but does not include `[[<slug>]]`:** add a new paragraph covering what the new source contributes relative to existing ones. Cite `[[<slug>]]`. Append `  - "[[<slug>]]"` to the `sources:` list.
Update the `updated:` date. Write the file. This page cites `[[source page slugs]]`, not raw files directly.

**Step 6 — Append to `wiki/log.md`** (newest at top):
```
## YYYY-MM-DD | ingest | <slug> | <one-line summary>

- Created: wiki/sources/<slug>.md
- Updated: wiki/index.md, wiki/overview.md, wiki/log.md, raw/<type>/README.md, inbox.md
```

**Step 7 — Update `raw/<type>/README.md`.**
- If a row for `<slug>` already exists: update the fetch date in-place. Do not add a second row.
- If no row exists: append the new row using the row format from the source type protocol below.

**Step 8 — Move inbox line.**
Move the URL from `## Pending` to `## Completed`. Append `<!-- ingested YYYY-MM-DD -->`.
If `auto_mark_complete: true`, also flip `[ ]` → `[x]`.

**Step 9 — Git (no agent commits)**  
Skip. Do not run `git commit` for this ingest. See **Git — never auto-commit** above.

### Merge rules (updating an existing topic page)

- Add new facts; do not duplicate.
- On a conflict: insert a `> **Conflict:**` block citing both sources. Source authority order: official docs > GitHub README > YouTube (official channel) > blogs/secondary. Do not silently overwrite.

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

Steps:

1. **Check `<domain>/llms.txt` first** (fetch `https://<domain>/llms.txt`). If present, it provides a structured concept index for the site — this often replaces the full crawl.
2. If no `llms.txt`: fetch the landing page and discover docs via `/docs`, `/documentation`, `/guide`, `sitemap.xml` links.
3. Depth by detail level:
   - `brief`: landing page only (or llms.txt if present).
   - `standard`: llms.txt (if any) + landing + docs index + ~4–10 key pages (product overviews, getting-started, architecture).
   - `deep`: full crawl within domain; one file per page at `raw/web/<domain>/<page-slug>.md`.
4. **Follow redirects; log the final URL** to the raw file — not the original inbox URL. Stale domains silently redirect.
5. Respect `robots.txt`. Set a descriptive user agent. Rate-limit between requests.
6. Save to `raw/web/<domain>.md` (one compiled file at `brief`/`standard`). At `deep`, use `raw/web/<domain>/<page-slug>.md` per-page.

**Guard:** if the full crawl would exceed 200k input tokens, halt and surface to user before proceeding.

**Raw file format** (`raw/web/<domain>.md`):
```
# <domain>

## Fetch log
- Inbox URL: <original url>
- Final URL: <final url after redirects>
- Fetched: <YYYY-MM-DD>
- Pages: <N>

## llms.txt (if present)
<full content>

## Landing page — <final-url>
<page content>

## <Page title> — <url>
<page content>
...
```

**README.md row format** (`raw/web/README.md`):
`| raw/web/<domain>.md | <domain> | <pages-fetched> | <YYYY-MM-DD> | |`

---

## Citation rules

1. **Every factual claim must have a citation chain to a raw file.** No citation → no claim.
2. **Source pages** use a banner citation at the top. Add per-paragraph inline citations only when a second raw file contributes to the page.
3. **Topic and synthesis pages** list contributing source pages in `sources:` frontmatter. Inline citations point to specific raw files.
4. **`wiki/overview.md`** cites `[[source pages]]` via wikilinks — not raw files directly.
5. **Citation path format:** always relative-from-file.
   - From `wiki/sources/`: `../../raw/<type>/<file>.md`
   - From `wiki/topics/` or `wiki/syntheses/`: `../raw/<type>/<file>.md`
   - Never root-relative (`/raw/...` or `raw/...` without `../` prefix).
6. **Obsidian compatibility:** wikilinks in frontmatter use list form — `- "[[slug]]"`, not inline `[[slug]]` arrays.

---

## Frontmatter rules

**Source pages** (`wiki/sources/*.md`) — MUST NOT include `sources:`:
```yaml
---
type: source
tags: []
related: []
detail_level: standard
created: YYYY-MM-DD
updated: YYYY-MM-DD
---
```

**Topic pages** (`wiki/topics/*.md`):
```yaml
---
type: topic
tags: []
sources:
  - "[[source-slug-1]]"
  - "[[source-slug-2]]"
related: []
created: YYYY-MM-DD
updated: YYYY-MM-DD
---
```

**Synthesis pages** (`wiki/syntheses/*.md`) — same shape as topic pages but `type: synthesis`.

**Overview page** (`wiki/overview.md`) — `type: synthesis`; `sources:` updated as sources are added.

---

## Refresh workflow

To re-fetch an already-ingested source:

1. Add `<!-- refresh -->` to its `## Completed` line in `inbox.md`.
2. Run `/pin-llm-wiki run`.

The run command scans `## Completed` for `<!-- refresh -->` and:
1. Re-fetches the source using the same protocol.
2. Strips any frontmatter field whose value matches `YYYY-MM-DD` or an ISO 8601 timestamp pattern from both copies before comparing. If unchanged, logs `refresh: <slug> (no change)` and stops.
3. If changed: overwrites the raw file, re-runs ingest steps 2–5 and 7 (updates wiki pages; skips step 6 log, inbox-move, and commit), appends a log entry `refresh: <slug> | content updated`.
4. Removes `<!-- refresh -->` from the inbox line, appends `<!-- refreshed YYYY-MM-DD -->`, preserves `[ ]`/`[x]` state. Do not run `git commit` (see **Git — never auto-commit**).

---

## Lint checks

Run `/pin-llm-wiki lint` to check wiki health.

| # | Check | Severity |
|---|---|---|
| 1 | Citation coverage — every factual claim has a chain to a raw file | ERROR (WARN on overview.md) |
| 2 | Contradictions — conflicting claims across pages | WARN |
| 3 | Orphan pages — no inbound `[[wikilinks]]` (includes overview.md and log.md) | WARN |
| 4 | Data gaps — concept in ≥2 source pages with no topic page | INFO |
| 5 | Missing cross-references — page mentions a wiki-known entity without linking | WARN |
| 6 | Stale sources — last refresh > 30 days | INFO |
| 7 | Terminology collisions — same term used for different concepts across sources | WARN |
| 8 | Frontmatter shape — source pages must NOT have `sources:` | ERROR |
| 9 | Citation path format — must be relative-from-file, not root-relative | ERROR |
| 10 | Inbox consistency — inbox line marked [x] but still under ## Pending | WARN |

Auto-fixes applied on every lint run:
- Missing `overview.md` / `log.md` links in `wiki/index.md`.
- Stub topic pages for concepts flagged by Check #4 (scaffold only; body left for human or next `add`).

Checks #2 (contradictions) and #7 (terminology collisions) are deferred in Phase 1 — reported as informational notes only.

---

## Manual harvest

When a cross-source answer is worth keeping permanently, promote it to a topic or synthesis stub:

1. Create `wiki/topics/<slug>.md` or `wiki/syntheses/<slug>.md`.
2. Frontmatter: `type: topic` (or `synthesis`), `sources:` list as wikilinks, `tags`, `created`.
3. Body: opening paragraph citing `[[source pages]]` (not raw files). Add inline raw-file citations for specific claims.
4. Run `/pin-llm-wiki lint` to verify citation coverage and cross-references.

Do not auto-generate topic body content. The stub names the concept and links it; fill body when you have adequate sources.

A formal `/pin-llm-wiki harvest` command is deferred. This manual flow is the MVP path.

---

## Remove workflow

`/pin-llm-wiki remove <slug>`:
1. Validate slug exists in `wiki/index.md` Sources table.
2. Soft-delete: move `wiki/sources/<slug>.md` to `wiki/.archive/wiki/sources/`. For raw files, check these exact paths only — `raw/<type>/<slug>.md` (single file) and `raw/<type>/<slug>/` (deep clone directory) — and move whichever exists to `wiki/.archive/raw/<type>/` (preserving structure). Do not glob or prefix-match. Update `wiki/index.md` (remove row, decrement count) and append to `wiki/log.md`.
3. Run lint immediately: flags orphaned `[[wikilinks]]` and pages whose `sources:` frontmatter still references `[[<slug>]]`.
4. Report to user; do not auto-rewrite.
5. **To undo:** files are in `wiki/.archive/`. Move them back to their original paths and restore the index.md row manually.
