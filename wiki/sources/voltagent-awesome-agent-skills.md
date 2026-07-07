---
type: source
source_url: https://github.com/VoltAgent/awesome-agent-skills
tags:
  - agent-skills
  - skills-ecosystem
  - skill-directory
  - curated-list
  - multi-agent-compatibility
  - awesome-list
  - official-skills
  - community-skills
related:
  - anthropics-skills
  - skills.sh
  - obra-superpowers
  - getcaveman.dev
  - teng-lin-notebooklm-py
  - voltagent-awesome-design-md
  - kepano-obsidian-skills
  - phuryn-pm-skills
  - davidondrej-skills
product: awesome-agent-skills
detail_level: standard
created: 2026-06-08
updated: 2026-07-07
---

Awesome Agent Skills is the most-contributed curated list of agent skills in the ecosystem (24,603 stars, MIT), aggregating 1,424+ hand-picked SKILL.md-based capability modules from official development teams and the community. Unlike bulk-generated repositories, every entry is a real-world skill created and used by actual engineering teams. It covers official skills from Anthropic, Google Labs, Vercel, Stripe, Cloudflare, Netlify, Expo, Hugging Face, Trail of Bits, Sentry, Microsoft, OpenAI, Figma, and 50+ other vendors, plus hundreds of community-authored skills organized by domain. All skills are compatible with Claude Code, Codex, Gemini CLI, Cursor, GitHub Copilot, OpenCode, Windsurf, and Antigravity; the companion site officialskills.sh provides a browsable registry.

_All claims below are sourced from ../../raw/github/voltagent-awesome-agent-skills.md unless otherwise noted._

## What it does

Awesome Agent Skills is a curated Awesome-list that serves as the definitive discovery layer for the agent skills ecosystem. The README (225KB) catalogs every notable official and community SKILL.md-based skill with a one-line description and link. Sections are organized by vendor (for official skills) and by domain or theme (for community skills). The companion platform officialskills.sh mirrors the registry as a searchable web directory. No SDK, no runtime — this is a pure knowledge aggregation and discovery resource.

## Key features

- **1,424+ curated skills** across 50+ official development teams and hundreds of community contributors; badge-verified counts updated with each commit.
- **Official skills coverage:** Anthropic (17 skills), Microsoft (133 skills across 6 languages), Google Gemini (4), Google Labs Stitch (6), Google Workspace CLI (17), OpenAI (37), Sentry (27+), Flutter (22), Auth0 (14), Cloudflare (8), Netlify (12), Expo (11), Hugging Face (13), Trail of Bits security (21), Apollo GraphQL (13), WordPress (13), Firebase (12), HashiCorp Terraform (11), fal.ai (15), Vercel (3), and more.
- **Community skills coverage:** organized into thematic sections — Context Engineering, Specialized Domains, n8n Automation, and a general Community Skills section — with notable collections from obra/superpowers, deanpeters/Product-Manager-Skills (46 PM skills), mattpocock/skills (17 dev workflow skills), mukul975 (753 cybersecurity skills), hamelsmu (7 LLM eval skills), and mcollina/skills (11 Node.js/Fastify skills).
- **Multi-agent path reference table:** canonical installation paths for 8 AI coding tools (Claude Code `.claude/skills/`, Codex `.agents/skills/`, Cursor `.cursor/skills/`, Gemini CLI `.gemini/skills/`, GitHub Copilot `.github/skills/`, OpenCode `.opencode/skills/`, Windsurf `.windsurf/skills/`, Antigravity `.agent/skills/`).
- **Skill quality standards:** documented criteria for description clarity, progressive disclosure (metadata under 100 tokens, body under 500 lines), no absolute paths, and scoped tool declarations.
- **Security guidance:** explicit notice that skills are curated, not audited; recommends Synk Skill Security Scanner and Agent Trust Hub before production use.

## Architecture

The repository is a single-file Awesome-list (`README.md`, 225KB) with no source code or package. Skills are organized as collapsible `<details>` sections per vendor, each containing bullet-pointed entries in the form `[org/skill-name](url) — description`. The companion officialskills.sh platform is maintained by VoltAgent and provides the same data in a web-browsable format with per-org filtering. VoltAgent's own TypeScript agent framework (`github.com/VoltAgent/voltagent`) is featured as an ecosystem tool, and the repository encourages sponsorship for product placement.

## Example usage

To find and install skills referenced in this list:

```bash
# Claude Code — install a skill from the registry (via skills.sh or direct path)
npx skills install anthropics/skill-creator

# Or manually copy a SKILL.md from any listed GitHub repo into:
# Project-level: .claude/skills/<skill-name>/SKILL.md
# Global:        ~/.claude/skills/<skill-name>/SKILL.md
```

The path table in the README covers all 8 supported agents. Skills discovered here are typically installable via the agent's native skill command or by cloning the source repo.

## When to use

Use this repository as the starting point when:
- Searching for official skills published by a specific technology vendor (Stripe, Cloudflare, Firebase, Auth0, etc.) for use in AI coding agents.
- Discovering community skills for niche domains (context engineering, cybersecurity, product management, advertising, music production, color science, Solana development, etc.).
- Verifying which agent tools (Claude Code, Cursor, Copilot, Codex, Windsurf, etc.) a given skill is compatible with.
- Building a skill distribution inventory across teams.

Not appropriate as a quality guarantee — each skill must be individually reviewed before production use.

## Maintenance status

24,603 stars, 2,639 forks, MIT License, actively maintained (last pushed 2026-06-05). No versioned releases; the list is updated continuously via community PRs. Contribution policy: skills should be community-adopted and proven in real-world usage, not freshly created. The project is backed by VoltAgent, which also maintains the officialskills.sh platform and the VoltAgent TypeScript framework.

## Ecosystem

- [[anthropics-skills]] — Anthropic's official 17-skill reference repository, fully listed here; the most-starred skills repo in the ecosystem before this list aggregated the broader space.
- [[obra-superpowers]] — one of the most prominent community skill collections listed here (190k+ stars); included in the Community Skills section.
- [[skills.sh]] — the Vercel-built distribution layer and leaderboard for the broader skills ecosystem; Awesome Agent Skills serves as a discovery catalog while skills.sh provides the install CLI and telemetry.
- VoltAgent framework (github.com/VoltAgent/voltagent) — the TypeScript multi-agent framework by the same org; featured as an ecosystem tool in this repository.
- officialskills.sh — companion web registry maintained by VoltAgent, mirroring this list with a browsable per-org UI.
