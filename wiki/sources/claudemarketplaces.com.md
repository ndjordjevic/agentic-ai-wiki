---
type: source
source_url: https://claudemarketplaces.com/
tags:
  - claude-code
  - skill-directory
  - plugin-marketplace
  - mcp-directory
  - extension-discovery
  - agent-skills
  - curated-catalog
  - cross-ai-tools
related:
  - skills.sh
  - voltagent-awesome-agent-skills
  - anthropics-skills
  - obra-superpowers
  - producthunt.com
  - getcaveman.dev
  - vercel.com
  - render.com
  - must-have-clis-2026
  - forrestchang-andrej-karpathy-skills
  - mattpocock-skills
  - SnailSploit-Claude-Red
product: claudemarketplaces
detail_level: standard
created: 2026-07-07
updated: 2026-07-08
---

Cross AI Tools (also reachable at claudemarketplaces.com, which redirects to crossaitools.com) is an independent, editor-curated directory of Claude Code extensions — skills, plugin marketplaces, and MCP servers — indexing 21,600+ skills, 2,500+ marketplaces, and 12,500+ MCP servers with ~300,000 monthly visitors. Unlike raw aggregators, it applies quality thresholds (500+ installs for skills, active GitHub repos, community trust signals), manual editorial review, and periodic delisting sweeps. Listings include install commands, editor-written summaries, category browse, a weekly "This week in Claude" digest, and machine-readable `llms.txt` for AI discovery.

_All claims below are sourced from ../../raw/web/claudemarketplaces.com.md unless otherwise noted._

## What it does

Cross AI Tools is a three-catalog discovery hub for Claude Code builders:

- **Skills** (`/skills`) — browsable index of agent skills sourced primarily from skills.sh, filtered to 500+ installs, ranked by installs and stars, organized into 34+ categories (frontend, backend, testing, security, DevOps, AI & agent building, skill development, and more).
- **MCP servers** (`/mcp`) — 12,500+ Model Context Protocol servers aggregated from community directories, categorized across 19+ domains (databases, browser automation, developer tools, communication, search, security, etc.).
- **Plugin marketplaces** (`/marketplaces`) — 2,500+ GitHub-based plugin registries with valid marketplace schemas, browsable across 24+ categories (AI agents, LLM integration, dev tools, memory & context, MCP servers, and more).

Each listing has a detail page with an editor-written summary, install command (typically `npx -y skills add <owner/repo> --skill <name> --agent claude-code` for skills), metadata (installs, stars, categories), and related recommendations. A sitewide search covers all three catalogs (⌘+K). The site also publishes `llms.txt` and `llms-full.txt` for LLM-friendly discovery, a sitemap refreshed daily, and `pricing.md` for machine-readable ad pricing.

## Key features

- **Quality curation** — automated crawlers sweep skills.sh, GitHub, and MCP registries; skills below 500 installs are excluded; abandoned and test entries are filtered; an editor reviews borderline listings and writes summaries; recurring content-policy sweeps remove spam and off-topic entries.
- **Rich metadata** — install counts, GitHub stars, category tags, and featured picks on the homepage surface adoption signals before install.
- **One-command install snippets** — detail pages expose copy-paste install commands for skills (via the skills CLI) and marketplace subscription commands.
- **Category taxonomy** — deep browse paths for skills (34+ categories), MCP servers (19+), and marketplaces (24+) so operators can narrow by domain (e.g. AI & Agent Building, Web & Browser Automation, Memory & Context).
- **Weekly digest** (`/digest`) — "This week in Claude" newsletter covering model updates, releases, and notable tools; archive of past issues back to April 2026.
- **Editorial tools page** (`/tools`) — maintainer-curated affiliate recommendations (Granola, Wispr Flow, Context.dev) for Claude Code builders.
- **Advertising** — clearly labeled sponsorship slots fund editorial work; `pricing.md` exposes structured pricing for AI agents evaluating sponsorship.

## Architecture and concepts

The platform separates three extension types that Claude Code users encounter:

| Type | What it is | Discovery source | Quality signal |
|---|---|---|---|
| **Skill** | Single SKILL.md instruction set | skills.sh crawl | 500+ installs minimum |
| **Plugin** | Bundle of skills, MCP servers, commands, hooks, or agents | GitHub marketplace schemas | Stars, plugin count, active repo |
| **Marketplace** | GitHub repo distributing multiple plugins | GitHub discovery | Stars, plugin count, schema validity |
| **MCP server** | Model Context Protocol tool server | Community MCP directories | Stars, registry signals |

The ingestion pipeline is crawler-driven with human editorial gates: crawlers refresh metadata on a schedule; thresholds filter low-signal entries; editors write the prose summaries on detail pages and curate homepage featured picks; delisting sweeps maintain catalog hygiene. The site is explicitly **not** affiliated with Anthropic — users are advised to review plugin code before installation.

Domain note: the inbox URL `claudemarketplaces.com` redirects to `crossaitools.com`; `llms.txt` and all canonical links use the crossaitools.com hostname.

## Main APIs

Cross AI Tools is a browse-and-install directory, not a programmatic API platform. Machine-readable surfaces for agents:

- `https://crossaitools.com/llms.txt` — concise catalog index with top skills, MCP servers, marketplaces, categories, and FAQ
- `https://crossaitools.com/llms-full.txt` — long-form context file
- `https://crossaitools.com/sitemap.xml` — all indexable URLs, refreshed daily
- `https://crossaitools.com/pricing.md` — structured ad pricing
- `robots.txt` — allows all major AI crawlers

Install actions delegate to upstream tools: skills install via `npx skills add` (skills.sh / vercel-labs/skills CLI); marketplaces via `/plugin marketplace add <owner/repo>` in Claude Code.

## When to use

Use Cross AI Tools when you want a **curated, quality-filtered** view of the Claude Code extension ecosystem rather than raw leaderboard data. It complements [[skills.sh]] (which ranks all skills by anonymous install telemetry without a 500-install floor) by surfacing only proven extensions with editor context. Good for:

- Discovering popular skills, MCP servers, or marketplaces by category
- Finding install commands without hunting GitHub READMEs
- Browsing MCP servers beyond the official MCP servers monorepo
- Staying current via the weekly digest
- Letting agents consume `llms.txt` for structured catalog awareness

Prefer [[skills.sh]] when you need the full unfiltered leaderboard, security audits, or the open-source `npx skills` CLI docs. Prefer [[voltagent-awesome-agent-skills]] or domain-specific awesome-lists when you want curated lists tied to a specific agent runtime rather than Claude Code specifically.

## Ecosystem

Cross AI Tools sits in the Claude Code extension discovery layer alongside:

- [[skills.sh]] — primary upstream for skill install counts and the `npx skills` CLI; Cross AI Tools crawls skills.sh as its main skill source
- Official Anthropic marketplaces — [[anthropics-skills]], [[anthropics/claude-code]] plugins (both heavily featured)
- Community methodology marketplaces — [[obra-superpowers]], affaan-m/everything-claude-code, gsd-build/get-shit-done (all top marketplaces)
- MCP ecosystem — overlaps with servers listed in modelcontextprotocol/servers and community registries; featured entries include Context7, GitHub MCP, Supabase MCP, Linear MCP
- Vendor agent infrastructure — [[vercel.com]], [[render.com]] publish their own Agent Skills discoverable in broader catalogs
- CLI roundups — [[must-have-clis-2026]] covers complementary terminal tools for agent workflows

Featured skills on the homepage (caveman, grill-me, systematic-debugging, karpathy-guidelines, find-skills) map to existing wiki sources including [[getcaveman.dev]], [[mattpocock-skills]], [[obra-superpowers]], [[forrestchang-andrej-karpathy-skills]], and [[skills.sh]].
