---
type: source
category: "Agent Skills & plugins ecosystem"
source_url: https://github.com/coreyhaines31/makerskills
tags:
  - agent-skills
  - personal-operator
  - decision-framework
  - second-brain
  - skill-plugin
  - karpathy-llm-wiki
  - indie-founder
  - claude-code-plugin
related:
  - anthropics-skills
  - obra-superpowers
  - cursor-plugins
  - forrestchang-andrej-karpathy-skills
  - phuryn-pm-skills
  - davila7-claude-code-templates
  - coleam00-cole-medin-knowledge-base
product: makerskills
detail_level: standard
created: 2026-08-20
updated: 2026-08-20
---

makerskills is a Claude Code plugin containing 20 agent skills purpose-built for the **personal operator** — founders, indie builders, and solo decision-makers who run multiple businesses or projects and want agentic AI integrated into their weekly operating cadence. Where most agent skill packs in this wiki target software engineering workflows (CI/CD, PR review, code generation), makerskills targets the craft of operating a business: structured decisions via 37signals' 38-question framework, a simulated board of advisor "council" (Fried, Musk, Bezos, Naval et al.), a Karpathy-style `second-brain` skill over any markdown vault, scenario-based personal and company CFO workflows, domain hunting with multi-tool availability checks, and a trifecta of meta-skills (`skillify`, `toolify`, `loopify`) for extending Claude Code itself. With 669 stars and v1.5.0 tagged in August 2026, it is one of the most comprehensive single-author skill packs in the ecosystem.

_All claims below are sourced from ../../raw/github/coreyhaines31-makerskills.md unless otherwise noted._

## What it does

makerskills installs as a Claude Code plugin (`/plugin marketplace add coreyhaines31/makerskills`) and exposes 20 slash-command skills. Each skill is a structured multi-step workflow encoded in a `SKILL.md` file: the agent reads the workflow description, follows the steps, and writes structured outputs to disk (archives, vault notes, slide decks, or financial projections). The plugin is documentation-first — every skill can be read and executed by hand without Claude, making the workflows transparent and auditable. Skills route intelligently to each other (`watch-video` calls `second-brain` for capture; `business-brainstorm` calls `deep-research` and `domain`), forming a composable operating system for solo operators.

## Key features

- **20 skills across 5 families:** Meta (`skillify`, `toolify`, `loopify`), Decision & strategy (`decide`, `business-brainstorm`, `domain`, `deep-research`, `unstuck`, `maker-council`), Knowledge (`second-brain`, `company-brain`, `read-book`, `watch-video`), Output (`jab-hook`, `slide-deck`), and Operations (`pm`, `personal-cfo`, `company-cfo`, `paste`, `social-fetch`).
- **`decide`:** 37signals 38-question decision framework + house additions (Q39 opportunity cost); triages to 6–8 questions per decision; archives with revisit date.
- **`maker-council`:** simulates a personal board (Fried, Musk, Bezos, Jensen, Iger, Graham, Naval, Blakely); seats 3–5 by question type with a designated dissenter; grounds takes in documented frameworks; custom members via config dir.
- **`second-brain`:** Karpathy LLM Wiki workflow (capture / compile / query / lint / connect / search) over any local markdown vault; personal-scope; path configured via `$SECOND_BRAIN_VAULT`.
- **`company-brain`:** team-scope sibling with structured raw dirs (people / meetings / SOPs / decisions / customer-language / sales-objections), sensitivity tagging, trust levels, and a `/cb review` culling pass to prevent stale info from poisoning answers; optional auto-sync from Fathom / Gong / Granola / CRM.
- **`domain`:** 11-step .com hunt via Vercel CLI + whois + Domainr + Namecheap + rdap.org + `agent-browser` for USPTO trademark screening + aftermarket click-throughs (HugeDomains / Afternic / Sedo / Dan).
- **`-ify` trifecta:** `skillify` creates/adapts/updates skills with semver discipline and cross-skill propagation; `toolify` wires integrations/APIs/MCPs into Next.js or Rails; `loopify` sets up agent loops and cron jobs with idempotency guards.
- **Skill composition:** the 54-reference `watch-video`, 51-reference `skillify`, and 48-reference `second-brain` are the "hub" skills — most workflows pass through at least one of them.
- **Personal config separation:** the repo is public and generic; all personal data lives in `~/.config/makerskills/` (gitignored), pointed to via env vars.
- **Cross-plugin references:** skills reference siblings in `marketingskills` (46 marketing skills) by the `marketingskills:cro` prefix convention.

## Architecture

Each of the 20 skills lives in `skills/<name>/SKILL.md`. The `.claude-plugin/` directory holds `marketplace.json` and `plugin.json` for Claude Code's plugin marketplace. There is no runtime binary or compiled code — the plugin is entirely SKILL.md documentation loaded by the agent host. Personal configuration paths (`$MAKERSKILLS_CONFIG`, `$SECOND_BRAIN_VAULT`, `$COMPANY_BRAIN_VAULT`, `$COMPANY_CFO_ROOT`, `$SLIDE_DECK_REPO`) decouple personal data from the public repo. The architecture document (`ARCHITECTURE.md`) describes skill families, cross-plugin conventions, and the personal-config pattern in detail.

## Installation

```bash
# Claude Code marketplace
/plugin marketplace add coreyhaines31/makerskills
/plugin install makerskills@makerskills

# Or symlink for local dev
git clone https://github.com/coreyhaines31/makerskills ~/code/makerskills
ln -s ~/code/makerskills ~/.claude/plugins/makerskills

# Set env vars in ~/.zshenv
export MAKERSKILLS_CONFIG="$HOME/.config/makerskills"
export SECOND_BRAIN_VAULT="$HOME/Documents/SecondBrain"
```

## Example usage

```
/decide
→ "What decision are you facing?"
→ Asks 6–8 triaged 37signals questions
→ Writes structured decision log to ~/.config/makerskills/decide/archive/
→ Sets a revisit reminder

/maker-council
→ "What question do you want the council to weigh in on?"
→ Seats 3–5 advisors by question type (e.g. product → Fried + Jobs + Graham)
→ Each delivers their perspective in their documented framework style
→ Synthesizes a recommended call with mapped disagreements

/second-brain query "agent orchestration patterns"
→ Searches $SECOND_BRAIN_VAULT for relevant notes
→ Returns cited summary with wikilinks to source files
```

## Maintenance status

- **Stars**: 669
- **Latest release**: v1.5.0 (2026-08-12) — includes `maker-council` v0.2.0 and `domain` v0.2.0
- **Last pushed**: 2026-08-18
- **License**: MIT
- **Built by**: Corey Haines (Conversion Factory + Magister Marketing)
- **Related plugin**: `marketingskills` (46 marketing skills — CRO, copywriting, SEO, ads)
