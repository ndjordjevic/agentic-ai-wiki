# mvanhorn/last30days-skill

## Metadata
- Stars: 52052
- Primary language: Python
- Default branch: main
- Latest release: v3.14.0 (2026-07-13)
- License: MIT License
- Homepage: (none)
- Fetched: 2026-07-14
- Final URL: https://github.com/mvanhorn/last30days-skill

## Description
AI agent skill that researches any topic across Reddit, X, YouTube, HN, Polymarket, and the web - then synthesizes a grounded summary.

## README
# /last30days

**An AI agent-led search engine scored by upvotes, likes, and real money - not editors.**

This README tracks the current v3 pipeline. The runtime skill spec lives in `skills/last30days/SKILL.md`, the source of truth for the latest command and setup behavior.

**Claude Code (recommended — auto-updates via marketplace):**
```
/plugin marketplace add mvanhorn/last30days-skill
/plugin install last30days
```

**Codex, Cursor, Copilot, Gemini CLI, or any of 50+ Agent Skills hosts:**
```
npx skills add mvanhorn/last30days-skill -g
```

Zero config. Reddit, HN, Polymarket, and GitHub work immediately. Run it once and the setup wizard unlocks X, YouTube, TikTok, arXiv, Techmeme, and more in 30 seconds.

Reddit upvotes. X likes. YouTube transcripts. TikTok engagement. Polymarket odds backed by real money and insider information. That's millions of people voting with their attention and their wallets every day. /last30days searches all of it in parallel, scores it by what real people actually engage with, and an AI agent judge synthesizes it into one brief.

Google aggregates editors. /last30days searches people. Each platform (Reddit, X, TikTok, YouTube) is a walled garden with its own API, tokens, and auth — no single AI has native access to all of it — but bringing your own keys and browser sessions lets an agent search all of them at once, score them against each other, and surface what actually matters.

```
/last30days Peter Steinberger
```

## Why this exists

Built to keep up with AI news community discussion the community always surfaces before training data catches up. Now used before sales calls, meetings, trips, and before building anything — to know what problems people are actually hitting.

## Sources, scored by the people

| Source | What the people tell you |
|--------|--------------------------|
| Reddit | Unfiltered take; top comments with real upvote counts, free, no API key |
| X / Twitter | Hot takes, expert threads, breaking reactions |
| YouTube | Full transcripts searched for the quotable sentences that matter |
| TikTok | Creator reach with takes not found on Google |
| Instagram Reels | Influencer perspective with spoken-word transcripts |
| Hacker News | Developer consensus — points and comments |
| Polymarket | Odds backed by real money, not opinions |
| GitHub | PR velocity, top repos by stars, release notes; issues/discussions for topics |
| Digg | Curated story clusters from Digg's AI 1000 leaderboard, no X auth required |
| arXiv | Papers behind the hype, free, no API key |
| Techmeme | Tech-news editorial layer, date-windowed |
| LinkedIn | Professional signal — posts and articles |
| StockTwits | Trader sentiment, auto-activates for tickers/crypto |
| Threads | Post-Twitter text layer |
| Pinterest | Visual discovery — pins, saves, comments |
| Xiaohongshu (RED) | Chinese lifestyle/product/creator signals, opt-in via local browser plugin |
| Bluesky | AT Protocol posts |
| Perplexity | Grounded Sonar synthesis, raw Search API rows, Deep Research |
| Web | Editorial coverage, blog comparisons |

Community contributors keep adding more sources.

## What people actually use it for

- Before a meeting — pull a person's recent activity across platforms into one brief.
- To read hiring signals — `--hiring-signals` turns current job postings into cited evidence for company focus shifts.
- To find the topic before it peaks — discovery mode sweeps Reddit, Hacker News, Digg, and X, returning engagement-velocity-ranked topics.
- To compare tools — side-by-side tables with live GitHub star counts, architecture, memory, security.
- To understand fast-moving world events with cross-source citation counts.
- Before a trip — construction updates, wait times, community sentiment.
- To learn something fast — synthesizes community-tested techniques into a production prompt.

## What's new (as of v3.11.1, July 2026)

Since the v3.3 announcement in May: 175 merged PRs (122 from 52 community contributors) across 15 releases.

- **First-class on OpenAI Codex** — native Codex plugin with guided setup; renderer-aware citations; same engine runs on Claude Code, Cursor, Copilot, Gemini CLI, Claude Desktop, OpenClaw, and 50+ Agent Skills hosts.
- **arXiv, Techmeme, and Digg** — free, no API keys; first-run setup auto-installs their CLIs.
- **Free Reddit improvements** — keyless RSS + shreddit scraping after the public `.json` API died; dedicated-subreddit discovery with real upvote counts via arctic-shift; relevance floor against off-topic hijacking.
- **Comments as a default-on layer** — Instagram comments with rank-based diversity, YouTube comments plus ScrapeCreators transcript backup, crowd-voted comments weighted into Best Takes scoring.
- **One doctor command** — health check across every source with exact fixes for missing keys/CLIs/expired cookies.
- **X search rebuilt** — FROM/ABOUT lanes, person-aware subquery disambiguation, first-party authorship grounding, single source with automatic backend failover, honest `--diagnose`.
- **More sources**: LinkedIn (ScrapeCreators), StockTwits (ticker/crypto auto-activation), Perplexity (direct API + async Deep Research).
- **Security hardening** (community-driven): stored-XSS fixes in the HTML renderer, locked-down cookie temp files, supply-chain-hardened CI with OpenSSF Scorecard and build provenance attestation, Semgrep/OSV-Scanner scans, PR dependency-review gate, test-coverage floor raised to 84%, Hermes security scan cleared of CRITICAL findings.
- **Reach**: Hebrew/non-Latin language support, CJK-aware tokenization, Windows compatibility, cookie extraction across the Chromium family plus macOS Keychain/Linux pass(1), `--as-of` historical lookback, auto-provisioned Python 3.12 via uv, `--hiring-signals`, watchlist deltas between runs.

### Still in the box from v3

Pre-research brain resolving handles/subreddits/hashtags before API calls; Best Takes scoring; cross-source cluster merging; single-pass comparisons; auto-discovered `--competitors`; GitHub person-mode (`--github-user=`); ELI5 mode; shareable self-contained HTML briefs (`--emit=html`).

## Install

| Surface | Install | Updates |
|---------|---------|---------|
| Claude Code (recommended) | `/plugin marketplace add mvanhorn/last30days-skill` | Auto via marketplace |
| Grok (xAI Build CLI) | `grok plugin marketplace add mvanhorn/last30days-skill` then `grok plugin install last30days` | `grok plugin update last30days` |
| Codex/Cursor/Copilot/Gemini CLI/50+ Agent Skills hosts | `npx skills add mvanhorn/last30days-skill -g` | `npx skills update last30days -g` |
| claude.ai (web) | Download `.skill` and upload via Customize > Skills | Re-download and re-upload |
| Claude Desktop | Download `.mcpb` and drag into Settings > Extensions | Re-download and drag in |
| OpenClaw | `clawhub install last30days-official` | `clawhub update last30days-official` |

Claude Desktop installs `/last30days` as an MCP server via `.mcpb` bundle; requires Python 3.12+ on PATH locally. Credential stores are separate between Claude Desktop and Claude Code.

Manual (developer):
```bash
git clone https://github.com/mvanhorn/last30days-skill.git
ln -s "$(pwd)/last30days-skill/skills/last30days" ~/.claude/skills/last30days
```

## Bring your own keys

| Sources | What you need | Cost |
|---------|---------------|------|
| Reddit + HN + Polymarket + GitHub + StockTwits | Nothing | Free |
| arXiv + Techmeme | Free CLIs, auto-installed | Free |
| X / Twitter | Browser login or `XQUIK_API_KEY`/`XAI_API_KEY` | Free cookies; provider-specific keys |
| YouTube | `brew install yt-dlp` | Free |
| Bluesky | App password from bsky.app | Free |
| TikTok/Instagram/Threads/Pinterest/LinkedIn/YouTube comments | ScrapeCreators key | 10,000 free calls, then PAYG |
| Xiaohongshu (RED) | Local browser-session service, opt-in | No last30days key |
| Perplexity | Perplexity key or OpenRouter fallback | Pay as you go |
| Web search | Brave Search key | 2,000 free queries/month |

macOS Keychain storage supported as a lowest-priority credential source via `skills/last30days/scripts/setup-keychain.sh`.

## Configuration

- Research files save to `LAST30DAYS_MEMORY_DIR` (default `~/Documents/Last30Days/`); override with `--save-dir` or `--output`.
- Structured JSON output for agents via `--emit=json`.
- Topic-less discovery mode via `--discover` / "what's trending in X?" phrasing.
- Trend monitoring: `--store` persists to SQLite; `scripts/watchlist.py` for scheduled runs with Slack/webhook delivery; `scripts/briefing.py` for digests.
- Subscribable research library: `library feed` generates `index.html` + Atom `feed.xml`; `--publish` is explicit opt-in.
- Offline, deterministic library search via `library search`.

## How it works

1. User types a topic.
2. Agent resolves who matters — X handles, GitHub repos, subreddits, hashtags, channels.
3. All sources searched in parallel with multi-query expansion; results scored by engagement, relevance, freshness.
4. Full transcripts, top comments with upvote counts, captions, odds — not just titles/links.
5. Same story merged into one cluster across platforms.
6. Synthesized into one brief, grounded and cited, ranked by engagement rather than SEO.
7. The agent session retains the research for follow-up questions, prompts, drafts, plans.

## Open source

MIT license. No tracking, no analytics — research stays local. 2,700+ tests. Built with Python 3.12+, yt-dlp, Node.js (vendored Bird client for X search), and ScrapeCreators API. v3 engine architecture by @j-sperling.

## Docs

### docs/how-search-works.md — Reddit & X search architecture

Both Reddit and X searches run **in parallel** using Python's `ThreadPoolExecutor(max_workers=2)`.

**Reddit search**: uses the OpenAI Responses API with the `web_search` tool, domain-filtered to `reddit.com`. Model fallback chain: `gpt-5.2 → gpt-5.1 → gpt-5 → gpt-4.1 → gpt-4o → gpt-4o-mini`, triggered on HTTP 400/403 access errors. Prompt asks the model to extract the core subject, search three query patterns, and return JSON (`title`, `url`, `subreddit`, `date`, `relevance`); URLs must contain `/r/` and `/comments/`.

**Enrichment** ("the secret sauce"): after search, each thread is enriched by hitting Reddit's free JSON API (`GET https://reddit.com/r/{sub}/comments/{id}/{slug}/.json`, no key needed) to pull actual upvotes, comment count, upvote ratio, top 10 comments, and post date — replacing the LLM's approximate numbers with ground truth.

Overall pipeline: search (parallel) → merge → normalize → filter → score → dedupe → output to the SKILL.md agent.

## Top-level structure
- `skills/` — the `last30days` Agent Skill package (`SKILL.md` is the source of truth for runtime behavior)
- `mcp/` — Claude Desktop MCP server bundle source
- `hooks/` — install/update hook scripts
- `docs/` — architecture notes, configuration reference, release notes, solutions
- `fixtures/`, `tests/` — test suite and fixtures (2,700+ tests)
- `.claude-plugin/`, `.codex-plugin/`, `.grok-plugin/`, `.agents/` — per-harness plugin manifests
- `gemini-extension.json` — Gemini CLI extension manifest
- `CLAUDE.md`, `AGENTS.md`, `CONCEPTS.md`, `CONFIGURATION.md`, `CONTRIBUTORS.md`, `HERMES_SETUP.md` — project/agent docs
- `pyproject.toml`/`uv.lock` — Python packaging (uv-managed)
- `media/` — README assets
