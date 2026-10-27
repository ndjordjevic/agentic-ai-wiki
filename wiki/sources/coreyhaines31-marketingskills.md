---
type: source
category: "Agent Skills & plugins ecosystem"
source_url: https://github.com/coreyhaines31/marketingskills
tags:
  - marketing-skills
  - cro
  - copywriting
  - seo
  - growth-engineering
  - agent-skills
  - claude-code-plugin
  - product-marketing
related:
  - coreyhaines31-makerskills
  - skills.sh
  - anthropics-skills
  - davila7-claude-code-templates
  - phuryn-pm-skills
  - slavingia-skills
product: marketingskills
detail_level: standard
created: 2026-10-27
updated: 2026-10-27
---

coreyhaines31/marketingskills (56,785 stars, MIT) is Corey Haines's library of 52 marketing Agent Skills — CRO, copywriting, SEO, analytics, paid, retention, sales/RevOps and growth engineering — for technical marketers and founders using coding agents. A foundational `product-marketing` skill holds product, audience and positioning context that every other skill reads first. It installs through `npx skills` / [[skills.sh]], Claude Code and Codex plugins, and works with any agent supporting the Agent Skills spec; see also the sibling pack [[coreyhaines31-makerskills]].

_All claims below are sourced from ../../raw/github/coreyhaines31-marketingskills.md unless otherwise noted._

## What it does

The repo gives agents marketing frameworks as markdown skills so they recognize a marketing task and apply the right playbook. Skills are grouped into SEO & content (`seo-audit`, `ai-seo`, `programmatic-seo`, `schema`, `site-architecture`, `link-building`), conversion optimization (`cro`, `signup`, `onboarding`, `popups`, `paywalls`), content & copy (`copywriting`, `copy-editing`, `cold-email`, `emails`, `social`, `video`, `image`), paid & measurement (`ads`, `ad-creative`, `analytics`, `attribution`, `conversion-tracking`, `ab-testing`), growth & retention (`referrals`, `free-tools`, `churn-prevention`, `community-marketing`, `lead-magnets`), sales & GTM (`revops`, `sales-enablement`, `launch`, `pricing`, `prospecting`, `competitors`), and strategy (`marketing-ideas`, `marketing-psychology`, `customer-research`, `marketing-plan`, `marketing-council`, `marketing-loops`). Skills cross-reference each other (e.g. `copywriting` ↔ `cro` ↔ `ab-testing`) via each skill's Related Skills section.

## Installation

```bash
npx skills add coreyhaines31/marketingskills
npx skills add coreyhaines31/marketingskills --skill cro copywriting
```

Other routes: Claude Code (`/plugin marketplace add coreyhaines31/marketingskills`, then `/plugin install marketing-skills`), OpenAI Codex (`codex plugin marketplace add coreyhaines31/marketingskills`), clone-and-copy into `.agents/skills/`, git submodule, fork, SkillKit (`npx skillkit install ...`), or per-skill `<name>-claude-web.zip` archives from Releases. If run from inside an agent session, pass `-a claude-code` or the CLI may install only into `.agents/skills/`, which Claude Code does not read.

## Key features

- **Shared context foundation** — `product-marketing` is read by all other skills first; its file lives at `.agents/product-marketing.md` since v2.0 (with `.claude/` and legacy-name fallbacks).
- **Breadth** — 52 skill folders spanning the funnel from SEO to churn prevention to RevOps.
- **Natural or explicit invocation** — ask "optimize this landing page" (uses `cro`) or call `/cro`, `/emails`, `/seo-audit`.
- **Guided tool connection** — `tools/SETUP.md` covers scoped credentials and a first read-only result so agents can read marketing accounts.
- **Disclosed partner integrations** — Verified Partners (Converly, Ploy, AIsa, Omnia) fund the work, listed alongside neutral options; the README says they never influence core skill recommendations.
- **v2.0 consolidation** — 17 skills renamed and `page-cro` + `form-cro` merged into `cro`, with a documented rename map and cleanup command.

## Architecture

`skills/` holds 52 marketing skill folders; `tools/` has the partner registry, setup and integrations; `docs/skill-release-packaging.md` covers release archives. Also `scripts/` (e.g. `sync-partners.mjs` generating the Partners block from `partners.json`), `tests/`, `AGENTS.md`, `CLAUDE.md`, and plugin manifests in `.claude-plugin/`, `.codex-plugin/` and `.agents/`. Primary language is JavaScript (tooling); the content is Markdown skills.

## Example usage

```text
"Help me optimize this landing page for conversions"  → cro skill
"Write homepage copy for my SaaS"                     → copywriting skill
"Set up GA4 tracking for signups"                     → analytics skill
"Create a 5-email welcome sequence"                   → emails skill
```

## Maintenance status

56,785 GitHub stars, 8,396 forks, MIT licensed, default branch `main`, latest release v2.13.5 (2026-10-26), most recent push 2026-10-26. Very active; contributions via PR and issues welcome, with a companion "Coding for Marketers" guide and the author's agency and training offers linked from the README.
