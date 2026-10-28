---
type: source
category: "Business, career & learning"
source_url: https://github.com/AgriciDaniel/jev-seo
tags:
  - seo-audit
  - jev-model
  - pdf-report
  - ai-search-readiness
  - claude-code-skill
  - core-web-vitals
  - dataforseo
related:
  - typesafe.ai
  - Ying-Kai-Liao-jev-browser
  - firecrawl.dev
product: jev-seo
detail_level: standard
created: 2026-10-28
updated: 2026-10-28
---

jev-seo is a live SEO audit for any website from one homepage URL: it crawls the site, runs 52 deterministic rules tied to Google Search Central, measures Core Web Vitals via PageSpeed Insights, and asks Jev (TypeSafe's System One model) typed questions about every page. Code scores and ranks fixes; exports are a designed PDF, an Excel action tracker, and Markdown, all from one `audit.json`. It runs as a Claude Code skill (`/jev-seo https://example.com`) or CLI; standard mode needs no SEO data subscription and costs about a cent in Jev per site, with optional `--full` DataForSEO rankings/keywords/backlinks for about $0.30.

_All claims below are sourced from ../../raw/github/AgriciDaniel-jev-seo.md unless otherwise noted._

## What it does

From a single public homepage URL, jev-seo performs a polite live crawl (robots.txt, sitemaps, redirects, broken links, canonicals, structured data, JavaScript-only pages when Playwright is available), applies 52 rules across crawl/indexing, on-page, content, links, structured data, AI crawler access, performance and security, and sends batched typed Jev judgments (page type, intent, importance, helpfulness, specificity, trust, citability, title/meta fit, competing pairs; in `--full`, keyword relevance and best-page mapping). Scores rank work and never predict rankings or traffic; missing data stays missing; heuristics are labelled. It is an evidence tool, not a Search Console replacement or time-series rank tracker. Large sites are sampled at a page cap (60 by default).

## Installation

Python 3.10+. WeasyPrint needs Pango (e.g. `libpango-1.0-0` / `libpangoft2-1.0-0` on Debian/Ubuntu, `brew install pango` on macOS).

```sh
git clone https://github.com/AgriciDaniel/jev-seo.git
cd jev-seo
python3 -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env                           # TYPESAFE_API_KEY; optional keys listed inside
bin/jevseo doctor
bin/jevseo run https://example.com
```

Optional: `pip install playwright && playwright install chromium` for JS-rendered pages; without it those pages are audited from raw HTML. In Claude Code: `ln -s "$PWD" ~/.claude/skills/jev-seo` then `/jev-seo https://example.com`. Offline tests: `python -m unittest discover -s tests -v` (no keys, no spend).

## Key features

- **Three report formats from one source** — PDF (cover, summary, plan, scorecard, impact/effort, Jev cards, heatmap, findings, method), XLSX (Actions tracker with dropdowns plus Summary, Pages, raw Jev probabilities, Technical, Performance, Rankings, etc.), and Markdown with charts/Mermaid; reports land under `jev-seo-reports/<domain>-<stamp>/`.
- **Cost and budgets** — crawl/rules/scoring/charts/PDF/XLSX/MD run locally (free); PageSpeed Insights free; Jev ~$0.042/M input tokens (~$0.00015/page); `--full` DataForSEO ~$0.30/site. Hard caps `--jev-budget` (default $0.25) and `--dfs-budget` (default $1.00); every call in a cost ledger. Without `TYPESAFE_API_KEY` the audit still runs with Jev sections "not assessed" and a partial score.
- **Claude Code skill workflow** — background audit with staged progress, digest review, agent-written `narrative.json` grounded in evidence, then render; operating rule: source finds, code decides, Jev judges, Claude writes. Narrative checks refuse unknown action IDs and flag numbers not in the audit.
- **Evaluation notes** — README cites 2026-09-22 checks (rule/crawl facts re-verified; DataForSEO internal consistency; PageSpeed match; Jev repeatability and blind second-judge agreement on decisive answers), with non-decisive answers flagged "to verify".

## Architecture

Pipeline: homepage URL → `crawl.py` → `checks.py` (52 rules) → `jev.py` (site/page/pair judgments; budget ledger) → optional `dfs.py` + further Jev keyword judgments in `--full` → `psi.py` (PageSpeed) → `score.py` → `audit.json` → optional `narrative.json` → `report/` (view model → PDF via WeasyPrint, XLSX, MD). Package layout: `SKILL.md`, `bin/jevseo`, `jevseo/` (crawl, parse, checks, jev, dfs, psi, score, cli, report, templates), `references/` (judgments, method, evaluation, narrative), `examples/`, `tests/`. Jev calls go to `POST https://api.typesafe.ai/v1/systemone` with `model: jev-latest` (resolved to `jev-1.13.0` on 2026-09-21 per judgments docs). (../../raw/github/AgriciDaniel-jev-seo.md)

## Example usage

```sh
bin/jevseo audit https://example.com
bin/jevseo render jev-seo-reports/<dir>
bin/jevseo audit https://example.com --full
bin/jevseo audit https://example.com --full --reuse-dfs <dir>
bin/jevseo rescore jev-seo-reports/<dir>
bin/jevseo run https://example.com
```

Claude Code: `/jev-seo https://example.com` (skill runs audit, relays progress, writes narrative, renders PDF/XLSX/MD). (../../raw/github/AgriciDaniel-jev-seo.md)

## Maintenance status

MIT licensed (bundled Inter / JetBrains Mono fonts under SIL OFL); primary language Python; default branch `main`; version badge 0.1.1; no tagged GitHub releases at ingest time (fetched 2026-10-28); ~720 stars; homepage skool.com/ai-marketing-hub-pro; CI workflow badge on `main`. Jev, DataForSEO, and PageSpeed Insights are third-party services with their own terms. (../../raw/github/AgriciDaniel-jev-seo.md)
