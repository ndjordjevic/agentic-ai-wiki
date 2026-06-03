---
type: source
source_url: https://browse.sh/
tags:
  - web-automation
  - browser-cli
  - agent-skills
  - open-web-catalog
  - browserbase
  - skill-distribution
  - ai-agents
related:
  - skills.sh
  - anthropics-skills
  - vercel-labs-agent-browser
  - must-have-clis-2026
product: browse
detail_level: standard
created: 2026-05-20
updated: 2026-05-30
---

browse.sh is the open web skill catalog and browser CLI for AI agents, built by Browserbase. It pairs a public skill registry at browse.sh with the `browse` CLI (`npm install -g browse`), enabling agents to install pre-built web automation skills for hundreds of specific websites and then drive those sites using browser primitives — all with a claimed 50× token-cost reduction via suggested DOM selectors and XHR patterns.

_All claims below are sourced from ../../raw/web/browse.sh.md unless otherwise noted._

## What it does

browse.sh provides two complementary layers for AI agent web automation. The **skill catalog** is an open registry of 200+ site-specific skills covering travel, e-commerce, food, finance, government, sports, and many other domains — each skill is a structured SKILL.md file describing the optimal API path, browser workflow, credentials, filters, and output schema for one specific website task. The **CLI** (`browse`) lets agents install any skill from the catalog, drive browser sessions using primitives, tail network/console output for debugging, and switch between local and Browserbase cloud sessions.

## Key features

- **Skill catalog** — 200+ site skills covering domains such as Airbnb, Amazon, AllTrails, Booking.com, weather.gov, arxiv.org, Yelp, Zillow, YouTube, Wikipedia, and GitHub. Each skill specifies a `recommended_method` (`api`, `browser`, `hybrid`, `cli`, `url-param`) and includes authentication patterns, filter-parameter mappings, and structured output shapes.
- **Token efficiency** — skills encode domain-specific API shortcuts (e.g. the public Algolia search index behind AllTrails, XHR endpoints embedded in Next.js hydration JSON, undocumented public APIs) so agents skip browser rendering and CSS parsing; claimed 50× token reduction versus open-ended browsing.
- **Browser primitives** — `browse` exposes click, scroll, type, hover, press, eval, fetch, open, and session management commands for when direct API calls are insufficient.
- **Cloud sessions** — `browse cloud` subcommands delegate to Browserbase's remote browser pool with built-in CAPTCHA solving, residential proxies (`--proxies`), and verified stealth (`--verified`) for bot-detection-protected sites.
- **llms.txt + llms-full.txt** — the catalog is machine-readable via `browse.sh/llms.txt` (compact skill index) and `browse.sh/llms-full.txt` (full SKILL.md content for all loaded skills), designed for agent discovery without scraping.
- **Per-skill `.md` endpoints** — each skill is addressable at `browse.sh/skills/<domain>/<skill-id>.md`, exposing structured YAML frontmatter (name, description, website, category, tags, source, updated, recommended_method, verified, proxies) followed by purpose, when-to-use, and detailed workflow sections.

## Architecture and concepts

The skill system is the atomic unit: a SKILL.md file with a machine-readable header and a human+agent-readable workflow body. Skills are categorized by `recommended_method`:
- **api** — the target site exposes a public or semi-public JSON/REST endpoint that can be called directly, no browser rendering needed.
- **browser** — the site requires a rendered browser session; uses Browserbase remote sessions.
- **hybrid** — combines a direct API call and a browser session (e.g., authenticate once in browser, then call API in session context).
- **cli** — wraps a command-line tool or SDK rather than driving a website.
- **url-param** — query-string-driven pages where structured URLs are sufficient.

The `browse` CLI installs skills from the catalog, exposes individual browser commands (`browse open <url> --remote`, `browse eval "..." --remote`, `browse cloud fetch <url>`), and manages session state. Browserbase cloud sessions add proxy pools and bot-detection countermeasures for sites like Amazon (Perimeter X), 12306.cn (Alibaba nc.js), and DataDome-protected sites.

## Main APIs

- `browse skills add <domain>` — install a skill from the catalog.
- `browse open <url> [--remote]` — open a URL in a local or cloud browser.
- `browse eval "<js>" [--remote]` — execute JavaScript in a live browser context; used to call in-page APIs with authenticated cookies.
- `browse cloud sessions create [--keep-alive] [--verified] [--proxies]` — create a persistent Browserbase cloud session.
- `browse cloud fetch <url> [--proxies]` — fetch a page via Browserbase's Fetch API (bypasses IP blocks).
- `GET https://browse.sh/llms.txt` — machine-readable catalog for agent discovery.
- `GET https://browse.sh/skills/<domain>/<skill-id>.md` — individual skill SKILL.md document.

## When to use

- An AI agent needs to interact with a specific consumer or business website (book a reservation, search listings, extract structured data) and a pre-built skill exists for that domain — use the catalog skill instead of open-ended browsing to minimize tokens and avoid bot detection.
- Automating sites that are DataDome, PerimeterX, or Akamai protected — use `browse cloud` sessions with `--proxies` and `--verified` flags.
- Building agentic workflows that span multiple websites (e.g. road trip planning combining weather.gov, AllTrails, recreation.gov, and a payment service) — install the relevant skills and compose agent instructions around them.
- When an operator wants to expose web capabilities to a coding agent without hand-crafting browser automation — the skill catalog covers the discovery and implementation.

## Ecosystem

browse.sh is built by Browserbase, whose remote browser infrastructure powers all `browse cloud` sessions. The catalog overlaps with broader skill-distribution platforms: [[skills.sh]] (Vercel's open skill directory for coding agents, SKILL.md-compatible) and [[anthropics-skills]] (Anthropic's official skills across many use cases). browse.sh's specific contribution is site-specific web automation skills with embedded API credentials and anti-bot countermeasures, rather than general-purpose agent capabilities.
