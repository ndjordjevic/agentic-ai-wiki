---
type: source
category: "Business, career & learning"
source_url: https://github.com/slavingia/skills
tags:
  - minimalist-entrepreneur
  - validate-idea
  - first-customers
  - processize
  - indie-founder
  - agent-skills
  - claude-code-plugin
  - business-validation
related:
  - coreyhaines31-makerskills
  - coreyhaines31-marketingskills
  - phuryn-pm-skills
  - x.com-0xcodez-how-to-become-a-forward-deployed-engineer-in-10
  - go.aiapply.co
product: minimalist-entrepreneur
detail_level: standard
created: 2026-10-27
updated: 2026-10-27
---

slavingia/skills (11,001 stars) is the `minimalist-entrepreneur` Claude Code plugin: ten skills based on Sahil Lavingia's book *The Minimalist Entrepreneur*, covering the founder journey from finding a community through validating an idea, building a manual-first MVP, getting the first 100 customers, pricing, marketing, sustainable growth, company values, and a gut-check review. It targets indie founders rather than marketers, and pairs naturally with [[coreyhaines31-marketingskills]] and [[coreyhaines31-makerskills]].

_All claims below are sourced from ../../raw/github/slavingia-skills.md unless otherwise noted._

## What it does

Each skill is a slash command tied to a stage of the book's progression: **Community → Validate → Build → Processize → Sell → Price → Market → Grow → Culture → Review**. The README's table gives when to use each:

- `/find-community` — looking for a business idea or your community
- `/validate-idea` — testing whether an idea is worth pursuing
- `/mvp` — ready to build a first product, struggling with scope
- `/processize` — have a product idea and want to deliver value by hand before writing code
- `/first-customers` — need to find the first 100 customers
- `/pricing` — setting prices or considering changes
- `/marketing-plan` — product-market fit reached, ready to scale with content
- `/grow-sustainably` — decisions about spending, hiring or scaling
- `/company-values` — defining culture, preparing to hire
- `/minimalist-review` — gut-checking any business decision

## Installation

In Claude Code:

```text
/plugin marketplace add slavingia/skills
/plugin install minimalist-entrepreneur
```

Claude Code fetches the repo and registers all 10 skills. Alternatively clone to `~/.claude/plugins/skills` and add the marketplace from that local path.

## Key features

- **Book-faithful journey** — skills follow the book's ordering, so a founder can enter at the stage they are in.
- **Manual-first "Processize"** — turn a product idea into a manual process you can deliver today before building software.
- **One-by-one customer acquisition** — the `/first-customers` skill targets reaching 100 customers individually; `/pricing` aligns with charging something from day one.
- **Decision filter** — `/minimalist-review` applies minimalist principles to any business decision.
- **Plugin packaging** — one marketplace entry, one install, ten slash commands.

## Architecture

Minimal repository: `.claude-plugin/` (marketplace plugin `minimalist-entrepreneur`), `skills/` with ten folders (`find-community`, `validate-idea`, `mvp`, `processize`, `first-customers`, `pricing`, `marketing-plan`, `grow-sustainably`, `company-values`, `minimalist-review`), and `README.md`. The captured README does not show the skills' internal contents.

## Example usage

```text
/validate-idea
# then describe the business idea and let the skill walk through whether it is worth pursuing
```

The invocation is the slash command from the README table; the follow-up prompt shown here is illustrative.

## Maintenance status

11,001 GitHub stars, 1,111 forks, no license listed on GitHub, no primary language (Markdown), default branch `main`, no tagged releases, most recent push 2026-04-14. Homepage: https://minimalistentrepreneur.com. Small, stable plugin with low churn since spring 2026.
