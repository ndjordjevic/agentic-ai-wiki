---
type: source
category: "Agent Skills & plugins ecosystem"
source_url: https://www.buildpartner.ai/social
tags:
  - claude-code-plugin
  - guided-builds
  - expert-frameworks
  - social-research
  - mcp-server
  - founder-workflows
related:
  - anthropics-skills
  - claudemarketplaces.com
  - skills.sh
  - supadata.ai
  - small-business
product: buildpartner
detail_level: standard
created: 2026-10-30
updated: 2026-10-30
---

BuildPartner.ai is Austin Marchese's Claude Code marketplace plugin (plus `buildpartner` MCP) that runs project-context guided builds (`/buildpartner:build`), expert-framework Q&A (`/buildpartner:expert-advice`), system-improvement reviews, and a dashboard — with a `/social` product surface for researching X/Instagram/YouTube creators (breakout posts, transcripts, comments) from inside Claude Code.

_All claims below are sourced from ../../raw/web/buildpartner.ai.md unless otherwise noted._

## What it does

Install via `curl -fsSL buildpartner.ai/install.sh | bash` (adds marketplace, plugin, MCP). Skills walk builds one step at a time filled with the user's real project context, match questions to named expert frameworks (Hormozi, Naval, Nikita Bier, Gary Vee, etc.), and open a signed-in web dashboard. The social page focuses on creator research prompts (breakouts, hooks, comment mining, topic tops, creator compares) using credit-metered lookups.

## Key features

- `/buildpartner:build` — premium guided builds tuned to the open project
- `/buildpartner:expert-advice` — premium expert-framework matching
- `/buildpartner:improve-system` — free reviews; credit-using self-improve runs on free plan
- `/buildpartner:open-dashboard` — free unlimited dashboard open
- Social research: Instagram/X/YouTube pull metrics, transcripts, comments via Claude prompts
- Plans: Free (5 premium credits), Pro $49.99/mo unlimited premium, Collaboration $249/mo unlimited coaching, Team contact-us
- Social signup bonus: 25 free credits (~250 lookups at 0.1 credit each) vs default 5

## Architecture and concepts

Claude Code plugin marketplace distribution; npm `buildpartner` MCP server invoked by skills. Web dashboard for builds, coaching, account. Training feed syncs creator content into expert library. llms.txt / llms-full.txt advertise install, skills, plans, and expanded expert/build indexes.

## Main APIs

- Claude Code slash commands (`/buildpartner:*`)
- MCP server packaged as npm `buildpartner`
- Install scripts: `buildpartner.ai/install.sh`, Windows `install.ps1`
- No separate public REST docs emphasized on captured pages; product is CLI/plugin-first

## When to use

- Founders/operators who want structured Claude Code builds and expert playbooks in-repo
- Content operators researching competitor creators from Claude (social surface)
- Teams wanting orientation + private knowledge skill (Team tier)

## Ecosystem

Created by Austin Marchese (YouTube Claude Code channel; Anthropic partnership claimed on home). Adjacent wiki: marketplace catalogs [[claudemarketplaces.com]] / [[skills.sh]]; social/transcript APIs like [[supadata.ai]].
