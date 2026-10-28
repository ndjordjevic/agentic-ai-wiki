---
type: source
category: "Design & UI generation"
source_url: https://github.com/ibelick/ui-skills
tags:
  - design-skills
  - mcp
  - skills-catalog
  - ui-engineering
  - agent-skills
  - design-engineers
  - skill-discovery
  - terminal
related:
  - skills.sh
  - emilkowalski-skills
  - leonxlnx-taste-skill
  - Owl-Listener-designer-skills
  - jakubkrehel-skills
  - anthropics-skills
  - davila7-claude-code-templates
  - Nutlope-inspo
  - ui-skills.com
product: ui-skills.com
detail_level: standard
created: 2026-10-27
updated: 2026-10-28
---

ibelick/ui-skills (10,241 stars, MIT) is "Skills for Design Engineers": a registry of UI-focused agent skills at ui-skills.com that can be browsed and fetched from the terminal (`npx ui-skills`) or by agents over a Model Context Protocol endpoint. It works as a curated discovery layer over design-skill packs comparable to [[emilkowalski-skills]] and [[leonxlnx-taste-skill]], with a distilled "Playbook" of lessons from them.

_All claims below are sourced from ../../raw/github/ibelick-ui-skills.md unless otherwise noted._

## What it does

The README is short. It describes three surfaces over the same skills registry: a CLI to browse and fetch skills from your terminal, an MCP server so agents can connect to the registry, and a Playbook of "distilled UI lessons from the best design engineering skills" at ui-skills.com/playbook. The repo does not list individual skills in the README; the catalog lives in the `skills/` directory and on the website. The sample command `npx ui-skills get baseline-ui` and the `--category motion` filter show that skills are organized by category, but the README does not enumerate the categories or skills.

## Installation

No install is required for the CLI; it runs through `npx`:

```bash
npx ui-skills start
```

For agents, add the remote MCP endpoint:

```
https://www.ui-skills.com/mcp
```

The README gives no client-specific MCP configuration snippets.

## Key features

- **Terminal discovery** — `start`, `categories`, `list --category <name>`, and `get <skill>` commands (README examples: `npx ui-skills categories`, `npx ui-skills list --category motion`, `npx ui-skills get baseline-ui`).
- **MCP registry** — remote server at `https://www.ui-skills.com/mcp` exposing two tools, `list_skills` and `get_skill`.
- **Playbook** — distilled lessons from top design-engineering skills, published on the site.
- **Website** — ui-skills.com is the main browsing surface; the repo's OG image is `public/UI-OG.png`.

## Architecture

The top-level structure suggests an Astro site deployed on Cloudflare: `astro.config.mjs`, `wrangler.jsonc`, `.dev.vars.example`, `migrations/` (database migrations), `src/`, `public/`, `bin/` (CLI entry), `scripts/`, `tests/`, and `skills/` (skill content). `AGENTS.md`, `DESIGN.md`, and `SECURITY.md` are also present. These are inferences from file names; the README does not describe the architecture, and primary language is TypeScript.

## Example usage

```bash
npx ui-skills start
npx ui-skills categories
npx ui-skills list --category motion
npx ui-skills get baseline-ui
```

An agent connected to the MCP endpoint would call `list_skills` to see what is available and `get_skill` to pull a skill into context (tool names from the README; their parameters are not documented there).

## Maintenance status

10,241 stars, 481 forks, MIT License, primary language TypeScript, default branch `main`, latest release v0.2.3 (2026-06-22), most recent push 2026-10-25. The version number is pre-1.0, so the CLI and MCP surface may still change. Homepage: https://www.ui-skills.com/.
