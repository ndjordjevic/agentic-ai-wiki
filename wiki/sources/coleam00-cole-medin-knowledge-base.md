---
type: source
category: "Knowledge, RAG, memory & context"
source_url: https://github.com/coleam00/cole-medin-knowledge-base
tags:
  - llm-wiki
  - karpathy-pattern
  - okf
  - youtube-transcript-mining
  - knowledge-synthesis
  - claude-code-workflows
  - canonicalization
  - citation-integrity
related:
  - 6eanut-llm-wiki
  - supadata.ai
product: cole-medin-knowledge-base
detail_level: standard
created: 2026-07-30
updated: 2026-07-30
---

`coleam00/cole-medin-knowledge-base` is a Karpathy-style LLM wiki — and simultaneously an Open Knowledge Format (OKF v0.1) bundle — synthesized entirely from Cole Medin's long-form YouTube catalog (198 videos): plain markdown + YAML frontmatter, navigated by index and relative links, no database or embeddings required. It is a directly relevant sibling project to this very wiki's own `pin-llm-wiki` methodology, and its documented build pipeline — two-pass extraction/canonicalization with a frozen manifest barrier, plus six independent validation checks including 99% citation-integrity verification — is a concrete, reproducible answer to the exact synthesis and provenance problems this wiki's own ingest process has to solve by hand.

_All claims below are sourced from ../../raw/github/coleam00-cole-medin-knowledge-base.md unless otherwise noted._

## What it does

The bundle mines Cole Medin's entire long-form YouTube catalog (agentic coding, AI engineering, RAG, harnesses, memory systems) into a densely cross-linked graph of three page types: `concepts/` (ideas/techniques/patterns, each synthesizing every video that discusses it — not one page per video), `entities/` (tools, people, organizations, subdivided into `tools/`/`people/`/`organizations/`), and `sources/` (one summary page per video with provenance to its transcript). Immutable, timestamped transcripts live under `raw/`. The explicit design goal: drop the folder next to any project and a coding agent can answer questions from Cole's videos with citations back to the exact video and timestamp — zero integration, no RAG stack, no API keys.

## Installation

```bash
git clone https://github.com/coleam00/cole-medin-knowledge-base.git
```

No build step or dependencies are required to *consume* the bundle — it is plain markdown. To *rebuild* it (or build an equivalent bundle from a different YouTube channel), three bundled Claude Code skills replicate the full pipeline:

| Skill | Transcript method | API key | Cost | Best for |
|-------|--------|---------|------|----------|
| `/channel-to-kb` | pytubefix + youtube_transcript_api | None | Free | Quick setup, local machines |
| `/channel-to-kb-ytdlp` | yt-dlp | None | Free | Most reliable, captures publish dates |
| `/channel-to-kb-supadata` | [[supadata.ai]] API | Required | $17+/mo | No IP issues, AI fallback for uncaptioned videos |

```bash
/channel-to-kb-ytdlp @3blue1brown
```

## Key features

- **OKF v0.1 conformance** — every concept document carries YAML frontmatter with a non-empty `type`; cross-links are ordinary relative markdown links (never `[[wikilinks]]`), with the relationship *kind* carried by the section heading (`## Prerequisites`, `## Builds on`/`## Part of`, `## Contrasts with`, `## Implemented by`/`## Tools`, `## Related`, `## Sources`)
- **Synthesis over accretion** — one page per durable concept/entity, not per video; a concept mentioned in 20+ videos still gets exactly one canonical page
- **Immutable raw layer** — timestamped transcripts under `raw/` are never hand-edited, preserving verbatim provenance even as the synthesized layer is polished
- **`lint.py`** conformance gate — checks every non-reserved file has frontmatter, every relative link resolves, every page appears in its directory index, every source has a matching raw transcript, and no page is an orphan
- **Contradiction-flagging, not silent resolution** — conflicting claims across videos get a `> **Contradiction:**` note citing both sources rather than being merged into one "correct" answer
- **Reproducible, incremental refresh** — new videos extend existing pages and add new ones only for genuinely new link-worthy ideas, rather than triggering a full rebuild

## Architecture

The build pipeline (documented in `docs/MAKING-OF.md`) is a two-pass architecture with a canonicalization barrier in the middle, designed specifically to avoid the failure mode of naive parallel extraction: `[1] Source` → `[2] Extract` (198 agents in parallel, one per transcript, emitting structured JSON candidates only — no prose) → `[3] Canonicalize` (aggregate, cluster by theme, per-cluster dedup, cross-cluster merge, **freeze** `manifest.json` + `taxonomy.json` as the contract) → `[4] Write` (~70 agents in parallel against the frozen manifest, resolving links through a precomputed `slug_index.json` so no agent can invent a broken link) → `[5] Polish` (ASR proper-noun normalization + typed-relationship rewriting) → `[6] Validate` → `[7] Gap sweep` (notability-triaged, not filled blindly). The core insight: parallel extraction alone produces divergent duplicate pages for the same idea (`piv-loop` vs `the-piv-loop` vs `plan-implement-validate-loop`); a single serial canonicalization barrier between extraction and writing removes that whole class of divergence bug while keeping everything else parallel. 785 concept candidates and 340 entity candidates collapsed to 186 canonical concepts — a ~4x compression that the author describes as *being* the synthesis.

## Example usage

To consume the bundle, an agent is pointed at it with a scripted prompt (from the README): clone it next to the project, read `index.md` then `SCHEMA.md`, then navigate the OKF way — follow relative links into `concepts/`, `entities/`, and `sources/`, opening only the pages a question needs rather than loading the whole folder — and answer with citations to the concept/entity pages used and the source video(s)/timestamps they came from, declining to guess if something isn't covered.

## Maintenance status

25 stars, JavaScript (workflow tooling), no declared license, no published release — versioned by direct commit history instead. Last pushed 2026-07-28. The bundle's own validation numbers (re-runnable from a clone): `lint.py` reports 0 errors/0 warnings across 1,050+ files; `citation_integrity.py` verifies 99% (2,562/2,567) of quoted claims actually appear in their cited transcript near the claimed timestamp; `semantic_dedup.py` finds 0 near-duplicate page pairs; an adversarial QA pass answered 30/30 in-scope questions correctly with 0 hallucinations and declined all 10 deliberately out-of-scope trap questions; recall coverage reached 88% pre-gap-sweep, with gaps subsequently closed by a curated (not blind) fill pass. A monthly refresh is the stated cadence, sourced from Cole's AI Tutor app's production database (which itself syncs the channel daily via [[supadata.ai]]).

## Ecosystem

This is a directly relevant methodological sibling to [[6eanut-llm-wiki]] and to this wiki's own `pin-llm-wiki` skill — all three implement variants of Andrej Karpathy's LLM-wiki pattern (plain markdown, index + links, no embeddings), but this one is unusual in publishing a fully reproducible build pipeline and validation suite (citation integrity, semantic dedup, adversarial QA, recall coverage) rather than just the output bundle. It uses [[supadata.ai]] as its underlying transcript-sync mechanism, making that source's "video transcript API" role concrete rather than abstract. The included Claude Code skills (`channel-to-kb`, `channel-to-kb-ytdlp`, `channel-to-kb-supadata`) let anyone reproduce the same pipeline against a different YouTube channel.
