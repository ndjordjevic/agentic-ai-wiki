# coleam00/cole-medin-knowledge-base

## Metadata
- Stars: 25
- Primary language: JavaScript
- Default branch: main
- Latest release: none published
- License: none declared
- Homepage: (none)
- Fetched: 2026-07-30
- Final URL: https://github.com/coleam00/cole-medin-knowledge-base

## Description

An OKF (Open Knowledge Format) knowledge base + Karpathy-style LLM wiki synthesized from Cole Medin's entire long-form YouTube catalog. Drop it next to any project for agent-ready, cited reference. No database, no embeddings.

## README

---
type: overview
title: "Cole Medin AI Knowledge Base"
description: "An Open Knowledge Format (OKF) wiki mined from Cole Medin's entire long-form YouTube catalog, built to be dropped next to any project as agent-ready reference."
tags: [readme, overview]
updated: 2026-07-21
---

# Cole Medin - AI Knowledge Base

A synthesized, densely cross-linked knowledge base mined from [Cole Medin's](https://www.youtube.com/@ColeMedin) **entire long-form YouTube catalog** - agentic coding, AI engineering, RAG, harnesses, memory systems, and more. It is an [Open Knowledge Format](https://github.com/GoogleCloudPlatform/knowledge-catalog) (OKF v0.1) bundle and a Karpathy-style [LLM wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f): plain markdown + YAML frontmatter, navigated by index and relative links, no database and no embeddings required.

**The point:** drop this folder next to your project and any coding agent can answer questions from Cole's videos with citations back to the exact video and timestamp - zero integration, no RAG stack, no API keys.

## What's inside

- **`concepts/`** - the ideas, techniques, patterns, and mental models (the PIV loop, context engineering, agentic search, and so on), each synthesizing every video that discusses it.
- **`entities/`** - the tools, people, and organizations (Claude Code, Archon, MCP, Anthropic, …).
- **`sources/`** - one summary page per video, with provenance to the raw transcript.
- **`raw/`** - the immutable, timestamped transcripts (the source of truth).
- **`index.md`** - start here (after `SCHEMA.md`). The compiled wiki *is* the search index.

## Use it with an agent (copy-paste)

Point your coding agent at this bundle with a prompt like:

```
Use the Cole Medin AI Knowledge Base as a reference:

1. Clone it next to my project (skip if I already have it):
   git clone https://github.com/coleam00/cole-medin-knowledge-base.git

2. Read `cole-medin-knowledge-base/index.md`, then `cole-medin-knowledge-base/SCHEMA.md`.
   This is an Open Knowledge Format (OKF) bundle - a linked wiki of concepts and entities
   mined from Cole Medin's videos. Navigate it the OKF way: read the index, follow the
   relative links into `concepts/`, `entities/`, and `sources/`, and open only the pages a
   question needs. Do not load the whole folder.

3. When I ask a question, answer from the knowledge base and cite the concept/entity pages
   you used and the source video(s) they came from (each page ends with a `## Sources`
   section listing the videos and timestamps). If something is not covered, tell me instead
   of guessing.
```

## Build your own (from any YouTube channel)

Three Claude Code skills are included that replicate the full pipeline - just point them at a channel. Each fetches transcripts using a different method, then walks you through the extract-canonicalize-write process described below.

| Skill | Method | API Key | Cost | Best for |
|-------|--------|---------|------|----------|
| `/channel-to-kb` | pytubefix + youtube_transcript_api | None | Free | Quick setup, local machines |
| `/channel-to-kb-ytdlp` | yt-dlp | None | Free | Most reliable, captures publish dates |
| `/channel-to-kb-supadata` | Supadata API | Required | $17+/mo | No IP issues, AI fallback for uncaptioned videos |

```bash
# Example: build a KB from 3blue1brown's channel using yt-dlp
/channel-to-kb-ytdlp @3blue1brown
```

Each skill fetches all transcripts as `raw/*.md` files, then guides Claude through the same pipeline used to build this bundle: extract concepts from each transcript, canonicalize (merge duplicates into single canonical pages), write cross-linked concept/entity/source pages, and validate with `lint.py`. The full pipeline reference is at `.claude/references/pipeline-guide.md`.

For small channels (under ~30 videos), the whole build fits in one Claude Code session. For larger channels, the skill batches the work and you can resume across sessions.

## How it was built (reproducible)

1. **Source.** Full transcripts for every long-form video are pulled from the source database and written as immutable `raw/<slug>.md` files (timestamped), plus `raw/manifest.json`.
2. **Extract.** Each transcript is mined for the concepts and entities it teaches, with timestamped quotes.
3. **Canonicalize.** All candidates are deduplicated into one taxonomy so each durable idea is a single page synthesizing every video that covers it (synthesis, not one-page-per-video).
4. **Write & link.** Concept/entity/source pages are written and cross-linked with typed relationship headings.
5. **Validate.** `python scripts/build_indexes.py` regenerates the indexes; `python lint.py` gates conformance, link integrity, index coverage, and orphans.

For the full story - the two-pass agent architecture, the tooling, and the validation results (citation integrity, adversarial QA, recall) - see [`docs/MAKING-OF.md`](docs/MAKING-OF.md) and [`tools/`](tools).

See [`SCHEMA.md`](SCHEMA.md) for the full contract and [`docs/ingestion-workflow.md`](docs/ingestion-workflow.md) for the step-by-step. Coverage and growth model are in [`roadmap.md`](roadmap.md).

## License / provenance

Knowledge is synthesized from publicly available YouTube videos by Cole Medin; each page cites its sources. Raw transcripts are included under `raw/` for provenance and auditability.

## Docs

### SCHEMA.md (excerpt — the maintainer contract)

This bundle is an Open Knowledge Format (OKF v0.1) bundle **and** a Karpathy-style LLM wiki: a synthesized, densely cross-linked graph of concepts and entities mined from Cole Medin's YouTube videos, not raw transcripts. Raw transcripts are kept immutable under `raw/` for provenance; the knowledge lives in `concepts/`, `entities/`, and `sources/`.

**OKF conformance (hard rules):**
1. Every OKF concept document carries YAML frontmatter with a non-empty `type` — the only strictly required field.
2. Reserved filenames: `index.md` (directory listing) and `log.md` (update history) — not concept documents, no frontmatter (except the bundle-root `index.md`, which MAY declare `okf_version`).
3. A concept's ID is its path within the bundle minus `.md` (`concepts/the-piv-loop.md` → `concepts/the-piv-loop`); filenames are stable and never renamed casually.
4. Cross-links are ordinary relative markdown links, never `[[wikilinks]]`; the *kind* of relationship is carried by the section heading it sits under.
5. The bundle aims for zero broken links and full index coverage, enforced by `lint.py`.

**Directory layout:**
```
cole-medin-knowledge-base/
├── index.md            # OKF root catalog (declares okf_version); read first after SCHEMA
├── roadmap.md           # scope + coverage + growth model
├── SCHEMA.md            # the maintainer contract
├── README.md            # human entry point + copy-paste consume prompt
├── log.md               # append-only ingestion history (reserved)
├── lint.py              # conformance + graph-health checker (run before every commit)
├── docs/
│   ├── ingestion-workflow.md   # how one transcript becomes pages (reproducible)
│   └── query-guide.md          # how to ask this bundle questions
├── scripts/
│   ├── build_indexes.py        # regenerate every index.md from the taxonomy + frontmatter
│   └── taxonomy.json           # theme -> slug groupings that drive the indexes
├── concepts/            # ideas, techniques, patterns, mental models
├── entities/            # tools/, people/, organizations/
├── sources/             # one synthesized summary page per video (provenance)
└── raw/                 # immutable timestamped transcripts + manifest.json
```

**Page types & frontmatter:** `concept` (`type: concept`, `videos: [...]` provenance list), `entity` (`type: entity`, `subtype: tool|person|organization`, optional `resource:` URL), `source` (`type: source`, one per video with `youtube_id`, `url`, `slug`, `published`, `duration`, `recency_rank`, `raw:` path), `raw-transcript` (`type: raw-transcript`, `immutable: true`).

**Typed relationship headings** (recovers semantics from untyped OKF links): `## Prerequisites`, `## Builds on` / `## Part of`, `## Contrasts with`, `## Implemented by` / `## Tools`, `## Related`, `## Sources` (every page ends with this, citing the video(s) that taught it).

**Atomicity rule:** one topic per page (split past ~800-1000 words of distinct subtopics); mine, don't mirror — never one page per video, each durable concept/entity is one page synthesizing all videos discussing it. Page-creation threshold = link-worthiness/reuse: linked from >=2 places or recurring across >=2 videos. Contradictions are flagged with a `> **Contradiction:**` note citing both sources, never silently resolved.

**Validation (`lint.py`)**: every non-reserved `.md` has frontmatter with non-empty `type`; every relative link resolves to a file in the bundle; every concept/entity/source page appears in its directory `index.md`; every `sources/<slug>.md` has a matching `raw/<slug>.md` and vice versa; no orphan concept/entity pages.

### docs/MAKING-OF.md (excerpt — pipeline and validation)

How 198 long-form YouTube videos became this knowledge base, built by AI agents orchestrated in **Claude Code Workflows** (JavaScript scripts that fan out subagents with real control flow), with human review at each checkpoint — roughly 700 agent runs across 8 workflows.

**The core problem: synthesis, not accretion.** One page per video produces a transcript archive, not a wiki — the PIV loop appears in 20+ videos, RAG in 40+. Parallel independent agents processing videos would each invent their own page name for the same idea (`piv-loop`, `the-piv-loop`, `plan-implement-validate-loop`), producing duplicates with divergent content; fully sequential processing (so each agent sees the growing wiki) is too slow and later agents drown in context. **The fix is a two-pass architecture with a canonicalization barrier in the middle.**

**The pipeline:**
```
[1] SOURCE          198 transcripts + publish dates -> raw/*.md (immutable, timestamped)
[2] EXTRACT         198 agents in parallel, one per transcript -> candidate concepts/entities + timestamped quotes (JSON, no prose)
[3] CANONICALIZE    aggregate -> cluster -> per-cluster dedup -> cross-cluster merge -> FROZEN manifest.json + taxonomy.json
[4] WRITE           ~70 agents in parallel against the frozen manifest -> concepts/, entities/, sources/ pages, cross-linked
[5] POLISH          ASR proper-noun normalization + typed Related sections
[6] VALIDATE        lint + audit + citation integrity + dedup + QA + recall
[7] GAP SWEEP       detect uncovered durable ideas -> notability triage -> fill
```

- **[1] Source:** transcripts came from the production database of Cole's AI Tutor app (syncs the full channel daily **via Supadata**), with per-chunk `start_seconds` reconstructing timestamped transcripts (196/198; 2 videos got a paragraph-only fallback). Publish dates enriched separately from each watch page's `datePublished` microformat. Tooling: `tools/export_transcripts.py`. Equivalent from scratch: `yt-dlp --flat-playlist -J` plus a captions pull, or a managed transcript API.
- **[2] Extract:** one agent per transcript, all in parallel, emitting structured JSON only (candidate concepts/entities, proposed slug, one-line definition, 2-3 verbatim timestamped quotes) — no prose yet. Agents were seeded with canonical slugs from an earlier 20-video build so independent agents converge on the same names. Result: 785 concept candidates, 340 entity candidates across 198 videos.
- **[3] Canonicalize — the barrier that makes synthesis work:** aggregate all extractions, group by normalized slug, cluster by dominant tag (14 clusters); per-cluster dedup (parallel, one agent per cluster) merges same-meaning candidates, applies the page-creation threshold (>=2 videos or one clearly substantial deep-dive), assigns a theme; a single cross-cluster merge agent resolves duplicates across clusters and freezes `scripts/manifest.json` (every page + description + related slugs + per-video quotes) and `scripts/taxonomy.json` (theme groupings). 785 candidates collapsed to 186 canonical concepts — a ~4x compression that *is* the synthesis.
- **[4] Write:** because slugs/sources/quotes are frozen, writing agents make no structural decisions — they fan out (batched 5-8 pages each) and write prose against the manifest, resolving every link through a precomputed `slug_index.json` so no agent can miscompute or invent a link.
- **[5] Polish:** ASR proper-noun normalization (YouTube auto-captions garble names like "Enthropic", "pantic Ai", "Lang graph", "canban" — swept against a canonical glossary while preserving quote meaning/timestamps exactly; `raw/` deliberately left untouched so verbatim provenance stays auditable) plus typed-relationship rewriting (`## Realizes`, `## Contrasts with`, `## Works with`, `## Related`).
- **[7] Gap sweep:** the recall test showed 88% pre-sweep coverage, triggering a dedicated sweep finding 342 gap mentions with no page, canonicalized into an add-list, then **notability-triaged** rather than filled blindly — 30 single-video candidates were rejected as sponsor reads or obscure micro-tools ("thin pages about things nobody will ask about actively degrade a knowledge base"); the surviving 155 pages were written with cited quotes and reciprocal backlinks.

**Validation results (six independent checks, all re-runnable from a clone):**

| Check | What it proves | Result |
|---|---|---|
| `lint.py` | OKF conformance, link integrity, index coverage, source/raw parity, orphans | 0 errors, 0 warnings (1,050+ files) |
| `audit.py` | Per-type frontmatter completeness, `videos:` cross-refs, thin pages, duplicate titles, taxonomy consistency | 0 problems |
| `citation_integrity.py` | Every quote actually appears in the transcript it cites, near the claimed timestamp | 99% verified (2,562 / 2,567) |
| `semantic_dedup.py` | No two pages are near-copies (local embeddings, cosine >= 0.86) | 0 duplicate pairs |
| `04-qa-answerability.mjs` | 40 questions answered by navigation, independently judged | 30/30 answerable, 10/10 traps declined, 0 hallucinations |
| `05-recall-coverage.mjs` | Do videos' core ideas actually have pages? | 88% pre-sweep, gaps then closed |

Adversarial QA included 10 deliberately out-of-scope questions ("What did Cole say about Claude 5 Opus?", "Which crypto token did he launch?") — the bundle declined all 10.

**Lessons worth stealing:** (1) put a barrier where the duplication risk is — only canonicalization is serial, everything else fans out; (2) separate structure from prose — freezing the manifest first removes a whole class of divergence bugs; (3) precompute link targets so writers can't produce broken links by construction; (4) test recall, not just precision — "is anything missing?" found 155 pages of real gaps; (5) curate the gap list — the sweep proposed 185 pages, 30 were noise; (6) keep the raw layer immutable so polishing the synthesized layer never risks the verbatim provenance.

**Refreshing:** new videos land in the source database automatically; refreshing is incremental (new `raw/` files, ingest per `ingestion-workflow.md` extending existing pages and creating new ones only for genuinely new link-worthy ideas, then rebuild indexes + lint).

### roadmap.md (excerpt — scope)

**In scope:** every long-form video on the channel (agentic coding, AI engineering, RAG and retrieval, harnesses and workflow engineering, memory/knowledge systems, tooling walkthroughs). **Out of scope by design:** YouTube Shorts and livestreams (too brief to synthesize durable concepts from / largely re-cover long-form material). Transcripts sourced from the AI Tutor (DynaChat) production database, which syncs the full channel daily via Supadata; publish dates enriched from the YouTube Data API. A monthly refresh keeps the bundle current. Explicit non-goals: not a transcript search box or vector database (the compiled wiki is the index), not a per-video blog, not a course/tutorial.

## Top-level structure

- `.claude/skills/` — three Claude Code skills that replicate the full pipeline for any YouTube channel: `channel-to-kb` (pytubefix + youtube_transcript_api, free), `channel-to-kb-ytdlp` (yt-dlp, free, most reliable), `channel-to-kb-supadata` (Supadata API, $17+/mo, no IP issues + AI fallback for uncaptioned videos)
- `.claude/references/` — `pipeline-guide.md`, the full reproducible pipeline reference used by the skills
- `concepts/` — flat directory of ~186 canonical concept pages (ideas, techniques, patterns), grouped thematically in `concepts/index.md`
- `entities/` — subdivided into `tools/`, `people/`, `organizations/`
- `sources/` — one summary page per video (198 videos), each citing its `raw/` transcript
- `raw/` — immutable, timestamped transcripts + `manifest.json`
- `docs/` — `MAKING-OF.md` (pipeline + validation), `ingestion-workflow.md` (step-by-step for one transcript), `query-guide.md` (how to query the bundle), `pipeline.png` (architecture diagram)
- `scripts/` — `build_indexes.py` (regenerates every `index.md` from taxonomy + frontmatter), `taxonomy.json` (theme → slug groupings)
- `tools/` — the actual build tooling: `export_transcripts.py`, `workflows/01-extract-canonicalize.mjs`, `workflows/02-write-pages.mjs`, `workflows/03-polish.mjs`, `workflows/04-qa-answerability.mjs`, `workflows/05-recall-coverage.mjs`, `workflows/07-notability-triage.mjs`, `validation/audit.py`, `validation/citation_integrity.py`, `validation/semantic_dedup.py`
- `index.md`, `SCHEMA.md`, `README.md`, `roadmap.md`, `log.md`, `lint.py` — bundle root (OKF catalog, maintainer contract, human entry point, scope/coverage, append-only history, conformance checker)
