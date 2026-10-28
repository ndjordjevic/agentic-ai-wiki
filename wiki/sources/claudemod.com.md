---
type: source
category: "Agent Skills & plugins ecosystem"
source_url: https://www.claudemod.com/
tags:
  - claude-code
  - mod-directory
  - skill-discovery
  - mcp-directory
  - plugin-marketplace
  - in-process-mods
  - hooks
  - community-catalog
related:
  - claudemarketplaces.com
  - skills.sh
  - anthropics-skills
  - obra-superpowers
  - affaan-m-ECC
  - forrestchang-andrej-karpathy-skills
  - davila7-claude-code-templates
  - voltagent-awesome-agent-skills
product: claudemod
detail_level: standard
created: 2026-10-28
updated: 2026-10-28
---

ClaudeMod (claudemod.com) is a community-maintained directory for Claude Code extensions — in-process TypeScript mods/plugins, Agent Skills, MCP servers, hooks, harnesses, commands, configs, and IDE plugins — positioning itself as "the community hub for Claude Code Mods" with ~172 listed items and no Anthropic affiliation.

_All claims below are sourced from ../../raw/web/claudemod.com.md unless otherwise noted._

## What it does

ClaudeMod indexes community Claude Code extensions into a browsable catalog with:

- A landing page featuring highlighted **Mods** (terminal panes, statuslines, safety hooks, dashboards) with star counts and GitHub links.
- A full **Browse** view (`/browse`) sorted by popularity, mixing skills, MCP servers, harnesses, hooks, and other categories.
- Per-category filters via `/browse?category=<slug>` for: `mod`, `skill`, `mcp-server`, `harness`, `hook`, `plugin`, `agent`, `command`, `config`, `ide-plugin`.
- Per-listing detail pages at `/mods/<slug>` that surface install instructions (often Claude Code `/plugin marketplace add` / `claude plugin install`, curl installers, or Homebrew) plus README-style feature docs when available.
- A **Submit a Mod** entry point (`/submit`) for community additions.
- Footer links to Browse All, Submit, and Anthropic's Claude Code GitHub repo (labeled "Claude Code Docs").

Unlike larger editorial aggregators such as [[claudemarketplaces.com]], ClaudeMod is a smaller, Claude-Code-native hub that especially elevates **in-process mods** — TypeScript plugins that dock panes beside the transcript, pin statuslines, or intercept tool calls — alongside the usual skills/MCP catalog entries (e.g. Superpowers, ECC skills, Anthropic Official Skills, Awesome MCP Servers).

## Key features

- **Mod-first featured grid** — Terminal Browser, Secret Redactor, Launch Codes, Claude Flightdeck, GitHub CI Status, PR Tracker, Agent Flow, Burn Meter, Statuspane, cctop, Context Lens, Effort Cycle.
- **Cross-type catalog** — the same Browse UI covers skills (Superpowers ~306k★ listing metric, ECC skill pack entries, Taste-Skill, Marketing Skills), MCP servers (Awesome MCP Servers, Puppeteer, Sequential Thinking, Context7), and harnesses (e.g. claude-flow / multi-agent orchestration listings).
- **GitHub-backed provenance** — listings link out to author repos (`zenbu-labs/terminal-browser`, `aidojo/*`, `scasella/claude-flightdeck`, `obra/superpowers`, `affaan-m/everything-claude-code`, etc.).
- **Install-oriented detail pages** — e.g. Flightdeck documents `/plugin marketplace add scasella/claude-flightdeck` and Claude Code 2.1.287+ requirements; Terminal Browser documents curl/Homebrew install and kitty-graphics rendering.
- **Community posture** — "Community-maintained," "Not affiliated with Anthropic," ~172 mods and growing; site CSP hints at Supabase + GitHub API for catalog metadata.

## Architecture and concepts

ClaudeMod is a discovery/index site, not a runtime:

- **Categories** map Claude Code extension packaging types (mod vs skill vs MCP vs hook vs harness) rather than end-user domains alone.
- **Mods** in ClaudeMod's sense are early-access Claude Code in-process plugins (often React/TSX hooks + panes) that observe session events (`tool.check`, `agent.spawn`, `session.measure`, etc.) or harden the tool loop (redaction, confirmation codes).
- **Skills / MCP / harness** listings reuse the same card + detail-page pattern but typically deep-link to upstream GitHub README content.
- No public `llms.txt` or dedicated docs subdomain was present at ingest time; discovery is HTML Browse + category filters + submit.

## Main APIs

ClaudeMod itself does not publish a documented public API for third-party clients. Operators interact via:

- Web UI: `/`, `/browse`, `/browse?category=…`, `/mods/<slug>`, `/submit`.
- Upstream install surfaces linked from detail pages (Claude Code plugin marketplace CLI, `npx skills`-style flows for some skill packs, or project-specific installers).

## When to use

Use ClaudeMod when you want a Claude Code–centric shortlist of **mods and session UX plugins** (panes, statuslines, safety gates) alongside popular skills and MCP servers — especially if you care about in-process TypeScript plugins rather than only SKILL.md packs. Prefer [[skills.sh]] or [[claudemarketplaces.com]] when you need a much larger skills/MCP marketplace with install-count ranking and broader editorial coverage.

## Ecosystem

Overlaps heavily with sources already in this wiki:

- Skill packs and catalogs: [[skills.sh]], [[anthropics-skills]], [[obra-superpowers]], [[affaan-m-ECC]], [[forrestchang-andrej-karpathy-skills]], [[voltagent-awesome-agent-skills]], [[davila7-claude-code-templates]].
- Broader Claude Code directory: [[claudemarketplaces.com]].
- Individual mods featured on the landing page live primarily as GitHub repos (not separately ingested here); ClaudeMod is the discovery surface.
