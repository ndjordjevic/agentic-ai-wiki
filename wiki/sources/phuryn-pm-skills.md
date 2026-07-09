---
type: source
category: "Agent Skills & plugins ecosystem"
source_url: https://github.com/phuryn/pm-skills
tags:
  - agent-skills
  - plugin-marketplace
  - product-management
  - claude-code-plugins
  - slash-commands
  - pm-workflows
  - discovery-to-shipping
  - codex-plugins
related:
  - anthropics-skills
  - voltagent-awesome-agent-skills
  - skills.sh
  - obra-superpowers
  - everyinc-compound-engineering-plugin
  - github-spec-kit
  - anombyte93-prd-taskmaster
  - openai-codex-plugin-cc
  - mattpocock-skills
  - shareai-lab-learn-claude-code
product: pm-skills
detail_level: standard
created: 2026-07-06
updated: 2026-07-06
---

PM Skills Marketplace (`phuryn/pm-skills`, 22,658 stars, MIT, v2.1.0) is the largest structured product-management skills ecosystem for AI coding assistants — 68 skills and 42 slash commands across 9 installable plugins covering discovery, strategy, execution, market research, analytics, GTM, marketing/growth, PM utilities, and an AI Shipping Kit for vibe-coded apps. Built primarily for Claude Code and Claude Cowork via a single marketplace manifest; individual `SKILL.md` files follow the universal skill format and work in Cursor, Gemini CLI, OpenCode, and Kiro when copied manually, while Codex CLI installs the same marketplace natively.

_All claims below are sourced from ../../raw/github/phuryn-pm-skills.md unless otherwise noted._

## What it does

The repository is a **plugin marketplace**, not a single monolithic skill pack. A root `.claude-plugin/marketplace.json` registers nine independent plugins; each plugin directory (`pm-product-discovery`, `pm-product-strategy`, `pm-execution`, etc.) ships its own `plugin.json`, `skills/{name}/SKILL.md` files, and `commands/{name}.md` slash-command definitions. **Skills** encode PM frameworks (Teresa Torres OST, lean canvas, pre-mortem, North Star metrics, JTBD interviews) as auto-loaded domain knowledge; **commands** chain skills into end-to-end workflows invoked with `/discover`, `/write-prd`, `/plan-launch`, `/north-star`, `/ship-check`, and 37 others. Commands suggest follow-ups in natural language only — no hard cross-plugin command references, because plugins install independently.

## Installation

**Claude Cowork (recommended for non-developers):** Customize → Browse plugins → Personal → Add marketplace from GitHub → `phuryn/pm-skills`. All nine plugins install at once.

**Claude Code CLI:**

```bash
claude plugin marketplace add phuryn/pm-skills
claude plugin install pm-toolkit@pm-skills
# ... repeat for each of the 9 plugins, or install all via Cowork
```

**Codex CLI:** Same marketplace commands (`codex plugin marketplace add phuryn/pm-skills`; `codex plugin add pm-*@pm-skills`). Skills install natively; slash commands ship inside plugins but do not run as Codex slash commands — describe the workflow in plain language or ask Codex to convert command files into Codex skills.

**Other assistants (skills only):** Copy `skills/*/SKILL.md` folders to `.cursor/skills/`, `.gemini/skills/`, `.opencode/skills/`, or `.kiro/skills/`. Commands are Claude-specific.

## Key features

- **Nine domain plugins:** discovery (13 skills, 5 commands), strategy (12/5), execution (PRDs, OKRs, roadmaps, sprints), market research (personas, competitive analysis, sizing), data analytics (SQL, cohorts, A/B tests), go-to-market (beachhead, ICP, battlecards), marketing/growth (positioning, North Star), toolkit (resume, NDA, proofreading), and AI shipping (document vibe-coded apps, security/performance audits, test-coverage maps).
- **Chained PM workflows:** `/discover` runs ideation → assumption mapping → prioritization → experiment design; commands flow into each other with suggested next steps matching real PM lifecycle order.
- **Framework grounding:** Skills encode methods from Teresa Torres, Marty Cagan, Alberto Savoia, Dan Olsen, Roger Martin, Ash Maurya, Strategyzer, Christina Wodtke, Sean Ellis, and others — structured rigor rather than generic AI text generation.
- **Progressive disclosure:** Lean YAML frontmatter (`name`, `description` for skills; `description`, `argument-hint` for commands) with detail in SKILL.md bodies; skills force-loadable via `/plugin-name:skill-name`.
- **AI Shipping Kit (`pm-ai-shipping`):** `/ship-check`, `/document-app`, `/derive-tests`, `/security-audit-static`, `/performance-audit-static` — documents intended behavior then audits the gap between docs and implementation for PMs accountable for AI-built code.
- **Validation and CI:** `validate_plugins.py` plus `tests/` (README count sync, version sync across all manifests, CHANGELOG format) run on every PR; releases auto-tag from CHANGELOG headings via `tag-on-merge.yml`.

## Architecture

Each plugin is self-contained: `.claude-plugin/plugin.json`, `skills/`, `commands/`, and a per-plugin README. Design rules from `CLAUDE.md`: skills are nouns/concepts auto-loaded on topic match; commands are verbs chaining intra-plugin skills only; a skill's `name` must match its directory name; `$ARGUMENTS` is the single command placeholder. Versioning is marketplace-wide — `marketplace.json`, all nine `plugin.json` files, and the newest CHANGELOG heading always share the same semver (currently v2.1.0). Descriptions in `plugin.json` stay aligned with the repo README. Companion projects include [PM Brain](https://github.com/phuryn/pm-brain) (markdown second brain), burnstop, and claude-usage.

## Example usage

Entry-point commands from the README:

```
/discover AI-powered meeting summarizer for remote teams
/strategy
/write-prd
/plan-launch AI code review tool targeting mid-size engineering teams
/north-star Two-sided marketplace connecting freelancers with clients
/ship-check the payments service
```

Skill-only prompts (no slash command): `What are the riskiest assumptions for our AI writing assistant idea?`, `Help me build an Opportunity Solution Tree for improving user activation`, `Where does what this code does diverge from what the docs say it should do?`

## Maintenance status

22,658 stars, 2,277 forks, MIT license, default branch `main`, latest release v2.1.0 (2026-07-03), last push 2026-07-03. Actively maintained by Paweł Huryn (The Product Compass Newsletter); CI badge on README; Windows Cowork VM workaround documented for known Claude Code issue #27010. PRs welcome per CONTRIBUTING.md.
