---
type: source
category: "Agent Skills & plugins ecosystem"
source_url: https://github.com/mvanhorn/last30days-skill
tags:
  - research-agent
  - reddit-search
  - social-search
  - engagement-scoring
  - claude-code-plugin
  - agent-skills
  - polymarket
  - cross-source-synthesis
related:
  - voltagent-awesome-agent-skills
  - davila7-claude-code-templates
  - firecrawl.dev
product: last30days-skill
detail_level: standard
created: 2026-07-14
updated: 2026-07-14
---

`/last30days` is an Agent Skill that searches Reddit, X, YouTube, TikTok, Hacker News, Polymarket, GitHub, arXiv, Techmeme, Digg, and a dozen other platforms in parallel for a given topic, then has an AI agent synthesize the results into one cited brief — scored by real engagement (upvotes, likes, prediction-market odds) rather than editorial ranking. It's a large (2,700+ test), actively community-maintained skill distributed across the Claude Code marketplace, Grok Build, Codex/Cursor/Copilot/Gemini CLI via [Agent Skills](https://agentskills.io), claude.ai, Claude Desktop (as an MCP server), and OpenClaw.

_All claims below are sourced from ../../raw/github/mvanhorn-last30days-skill.md unless otherwise noted._

## What it does

Given a topic (a person, company, product, or comparison like "X vs Y"), the skill resolves the relevant handles/subreddits/repos/hashtags, searches every enabled source in parallel with multi-query expansion, scores results by engagement/relevance/freshness, merges same-story mentions across platforms into one cluster, and outputs a single grounded brief with per-claim citations. A topic-less discovery mode (`what's trending in X?`) instead sweeps Reddit/HN/Digg/X for engagement-velocity-ranked emerging topics.

## Installation

Recommended on Claude Code via the plugin marketplace (`/plugin marketplace add mvanhorn/last30days-skill` then `/plugin install last30days`, auto-updating). Cross-host install via `npx skills add mvanhorn/last30days-skill -g` covers Codex, Cursor, Copilot, Gemini CLI, and 50+ other Agent Skills hosts. Also installable on Grok Build, claude.ai (upload a `.skill` file), Claude Desktop (`.mcpb` bundle, requires local Python 3.12+), and OpenClaw (`clawhub install last30days-official`).

## Key features

- **18 parallel sources** — Reddit, X/Twitter, YouTube, TikTok, Instagram Reels, Hacker News, Polymarket, GitHub, Digg, arXiv, Techmeme, LinkedIn, StockTwits, Threads, Pinterest, Xiaohongshu, Bluesky, Perplexity, plus general web — most work with zero API keys.
- **Reddit enrichment pipeline** — an LLM-driven search (OpenAI Responses API with domain-filtered `web_search`) finds candidate threads, then a free, keyless call to Reddit's own JSON API (`/r/{sub}/comments/{id}/{slug}/.json`) pulls ground-truth upvotes, comment counts, and top comments, replacing the model's approximate numbers.
- **Discovery mode** — ranks emerging topics by engagement velocity instead of researching a topic you already know.
- **Trend monitoring** — `--store` persists results to SQLite; `scripts/watchlist.py` runs scheduled checks with Slack/webhook delivery; `scripts/briefing.py` produces daily/weekly digests.
- **Subscribable research library** — saved briefs can be turned into a static `index.html` + Atom `feed.xml` via `library feed --publish`, and searched offline/deterministically via `library search`.
- **`--hiring-signals`** — treats a company's job postings as cited evidence for where it's investing (hiring focus, not roadmap speculation).

## Architecture

Reddit and X searches run concurrently via a `ThreadPoolExecutor(max_workers=2)`. Reddit search calls the OpenAI Responses API with `allowed_domains: ["reddit.com"]` and a model fallback chain (`gpt-5.2 → gpt-5.1 → gpt-5 → gpt-4.1 → gpt-4o → gpt-4o-mini`) triggered on HTTP 400/403 access errors; each returned thread is then enriched against Reddit's free JSON endpoint for real scores. The overall pipeline is search (parallel) → merge → normalize → filter → score → dedupe → output to the skill's agent-facing renderer. X search was rebuilt around FROM/ABOUT lanes (a person's own posts vs. conversation about them) with a single source and automatic backend failover.

## Example usage

```
/last30days Peter Steinberger
/last30days OpenClaw vs Hermes vs Paperclip
/last30days what's exploding in AI agents?
/last30days Listen Labs --hiring-signals
```

## Maintenance status

52,052 stars, 4,520 forks, MIT license, latest release v3.14.0 (2026-07-13), pushed 2026-07-13 — very active, GitHub Trending #1 Repository of the Day. 2,700+ tests; 175 PRs merged since May 2026 (122 from 52 community contributors) across 15 releases, including a community-driven security hardening wave (stored-XSS fixes, supply-chain-hardened CI with OpenSSF Scorecard, build provenance attestation, dependency-review gate, test-coverage floor raised to 84%).
