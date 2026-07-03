---
type: source
source_url: https://github.com/kepano/obsidian-skills
tags:
  - agent-skills
  - obsidian-skills
  - obsidian-cli
  - json-canvas
  - defuddle
  - claude-code-plugin
  - pkm
  - skill-ecosystem
related:
  - skills.sh
  - anthropics-skills
  - voltagent-awesome-agent-skills
  - runcabinet.com
  - 6eanut-llm-wiki
  - teng-lin-notebooklm-py
  - forrestchang-andrej-karpathy-skills
  - shareai-lab-learn-claude-code
  - coleam00-claude-memory-compiler
product: obsidian-skills
detail_level: standard
created: 2026-07-02
updated: 2026-07-03
---

`kepano/obsidian-skills` is Steph Ango's official Agent Skills collection for Obsidian — five SKILL.md modules that teach coding agents to create and edit Obsidian Flavored Markdown, Bases (`.base`), JSON Canvas (`.canvas`), and vault operations via the Obsidian CLI, plus a Defuddle skill for clean web-page extraction. With 39,000+ stars and MIT licensing, it is the canonical skills pack for agents working inside Obsidian vaults and connects directly to the broader SKILL.md ecosystem distributed through [[skills.sh]].

_All claims below are sourced from ../../raw/github/kepano-obsidian-skills.md unless otherwise noted._

## What it does

The repository packages Obsidian-specific agent capabilities as five self-contained skills following the [Agent Skills specification](https://agentskills.io/specification). Each skill is a folder with a `SKILL.md` (YAML frontmatter + markdown instructions) and optional `references/` subfolder. Together they cover the full Obsidian open-format surface area: note authoring (`obsidian-markdown`), database-like note views (`obsidian-bases`), visual canvases (`json-canvas`), command-line vault automation (`obsidian-cli`), and token-efficient web reading (`defuddle`). A `.claude-plugin/` manifest bundles all skills as the `obsidian@obsidian-skills` Claude Code plugin (v1.0.1).

## Installation

Three distribution paths are documented:

**Claude Code marketplace:**
```
/plugin marketplace add kepano/obsidian-skills
/plugin install obsidian@obsidian-skills
```

**`npx skills` (cross-agent):**
```
npx skills add https://github.com/kepano/obsidian-skills
```

**Manual per platform:**
- **Claude Code** — copy repo contents into `/.claude` in the vault root.
- **Codex** — copy `skills/` into `~/.codex/skills`.
- **OpenCode** — clone the full repo to `~/.opencode/skills/obsidian-skills` (preserve `skills/<name>/SKILL.md` structure; restart to discover).

## Key features

| Skill | Trigger | What it teaches agents |
|---|---|---|
| `obsidian-markdown` | `.md` files, wikilinks, callouts, embeds | Obsidian Flavored Markdown: `[[wikilinks]]`, `![[embeds]]`, `> [!callout]` syntax, YAML properties, tags, comments (`%%`), highlights, Mermaid, LaTeX |
| `obsidian-bases` | `.base` files, table/card views | Obsidian Bases YAML schema: global/view filters (`and`/`or`/`not`), formulas, properties, summaries, table/cards/list/map views |
| `json-canvas` | `.canvas` files | JSON Canvas 1.0 spec: text/file/link/group nodes, edges, colors, ID generation, layout guidelines, validation checklist |
| `obsidian-cli` | vault operations, plugin dev | `obsidian` CLI: read/create/search notes, daily notes, properties, tasks, tags, backlinks; plugin reload → `dev:errors` → screenshot/DOM verification cycle |
| `defuddle` | URLs to read/analyze | `defuddle parse <url> --md` for clean markdown extraction; prefer over WebFetch for standard web pages (not `.md` URLs) |

- **Agent Skills spec compliance** — skills work in Claude Code, Codex, Open Code, and any skills-compatible agent.
- **Reference subfolders** — `obsidian-markdown`, `obsidian-bases`, and `json-canvas` ship detailed reference docs (PROPERTIES.md, CALLOUTS.md, EMBEDS.md, EXAMPLES.md) that agents load on demand.
- **Plugin development workflow** — `obsidian-cli` documents a reload → error-check → screenshot → console cycle for Obsidian plugin/theme development.

## Architecture

The repo follows the standard Agent Skills layout: one folder per skill under `skills/`, each with a `SKILL.md` containing `name:` and `description:` frontmatter that drives on-demand loading (the same progressive-disclosure pattern covered in [[shareai-lab-learn-claude-code]] s05 and [[anthropics-skills]]). The `.claude-plugin/` directory provides marketplace metadata so Claude Code users can install all five skills as a single plugin bundle rather than copying files manually.

`obsidian-markdown` extends CommonMark/GFM with Obsidian-specific syntax — wikilinks for internal vault connections (Obsidian tracks renames), embeds for transclusion, and callouts for highlighted blocks. `obsidian-bases` treats `.base` files as YAML-defined query views over vault notes with a formula expression language. `json-canvas` implements the open [JSON Canvas](https://jsoncanvas.org/) format for spatial note layouts. `obsidian-cli` bridges agents to a running Obsidian instance via CLI commands (requires Obsidian open). `defuddle` is a thin wrapper around the separate [Defuddle](https://github.com/kepano/defuddle) npm CLI for web content extraction.

## Example usage

Install via skills CLI and use in any supported agent:

```bash
npx skills add https://github.com/kepano/obsidian-skills
```

Create a note from the CLI (once `obsidian-cli` skill is loaded):

```bash
obsidian create name="New Note" content="# Hello" template="Template" silent
obsidian search query="search term" limit=10
obsidian daily:append content="- [ ] New task"
```

Extract a web page for agent reading (via `defuddle` skill):

```bash
defuddle parse https://help.obsidian.md/cli --md
```

## Maintenance status

39,337 stars, 2,791 forks, MIT License, default branch `main`, last pushed 2026-06-08. No GitHub releases published. Author: Steph Ango (kepano), creator of the Minimal theme and Obsidian CEO. The repo is actively maintained and is the reference implementation for Obsidian-specific agent skills in the ecosystem indexed by [[skills.sh]] and catalogs like [[voltagent-awesome-agent-skills]].
