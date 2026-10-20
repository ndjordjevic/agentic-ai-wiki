---
type: source
category: "Agent Skills & plugins ecosystem"
source_url: https://github.com/tt-a1i/archify
tags:
  - agent-skill
  - interactive-diagrams
  - architecture-visualization
  - skills-sh
  - typed-json-ir
  - claude-code
  - codex
  - cursor
related:
  - skills.sh
  - anthropics-skills
  - graphify.net
product: archify
detail_level: standard
created: 2026-10-20
updated: 2026-10-20
---

Archify is an open-source agent skill (MIT, v3.2.0) that turns ideas, plans, or codebases into self-contained interactive HTML diagrams and explainer pages. Installed via [skills.sh](https://skills.sh/tt-a1i/archify/archify) (`npx skills add`), it works with Claude Code, Codex, Cursor, and OpenCode (plus community Hermes / DeepSeek Harness integrations). With ~86k GitHub stars and 130K+ skills.sh installs (as of October 2026), homepage [archify.si](https://archify.si).

_All claims below are sourced from ../../raw/github/tt-a1i-archify.md unless otherwise noted._

## What it does

Describe a system or ask the agent to read a repo; Archify authors typed JSON IR, validates layout and schema, then delivers a portable HTML artifact you can explore (focus, reach, routes, lenses), customize in chat, and share without a server. Besides diagrams it can build **explainer** pages — conclusion first, then panels with tables, steps, charts, and validated diagrams. No repository is required for description-only diagrams; source-backed Architecture nodes can pin Git-verified file ranges when requested.

## Installation

```bash
npx skills add tt-a1i/archify -g
```

Explicit Cursor install: `npx -y skills add tt-a1i/archify --skill archify --agent cursor --global --copy --yes`. Try without installing: `npx skills use tt-a1i/archify@archify --agent codex`. Skill lands under `~/.claude/skills/`, `~/.agents/skills/`, or OpenCode skill paths depending on the agent. Optional: Hermes (`hermes skills install skills-sh/tt-a1i/archify/archify -y`), DeepSeek Harness (`dsh plugin --profile web add @tt-a1i/archify-dsh@1.0.0`).

## Key features

- **Ten diagram types** — Architecture, Workflow, Sequence, Data Flow, Lifecycle, ERD, Class, Tree, Timeline, Waterfall (ERD/Class/Tree/Timeline/Waterfall since 3.1).
- **Architecture Delta** — compare Before/Delta/After snapshots with a machine receipt (`archify.mjs compare`).
- **Atomic delivery** — schema, layout, HTML/SVG, and clearance checks must pass before replacing the last known-good file; failures return machine-readable repair receipts.
- **Interactive viewer** — focus/reach, route probe, role lens, presentation stage, themes/styles, PNG/WebP/JPG/PDF export; stable URL hashes (`#focus=`, `#route=`, `#lens=`).
- **Explainer pages** — one-page answers with cited sources and per-panel follow-up edits.
- **Optional update reminder** — may GET a stable manifest; never auto-installs updates (`ARCHIFY_UPDATE_CHECK_DISABLED=1` to disable).

## Architecture

Generation pipeline: **Generate** (typed JSON IR) → **Validate** (bundled validators + layout rules) → optional **Preview** (loopback watch of one JSON file, last-good on failure) → **Deliver** (atomic replace of the HTML target) → **Iterate** in chat while unrelated structure stays stable.

Contract and schemas live under `archify/` (`SKILL.md`, `schemas/`, `bin/archify.mjs`). Layout judgment is agent-authored rather than generic Mermaid auto-layout; ordinary artifacts stay source-free unless evidence-backed Architecture mode is requested.

## Example usage

```text
Use Archify to diagram a web request: Browser calls the API,
the API checks Redis, and a cache miss queries PostgreSQL and fills the cache.
```

```bash
cd archify
node bin/archify.mjs doctor
node bin/archify.mjs guide "Show an API request with Redis cache miss"
node bin/archify.mjs validate workflow examples/agent-tool-call.workflow.json --quality showcase --json
node bin/archify.mjs deliver workflow examples/agent-tool-call.workflow.json /tmp/workflow.html --quality showcase --open --json
```

Gallery / Proof Lab: https://archify.si/gallery.html · scenario guide: https://archify.si/guide.html

## Maintenance status

- **Stars:** 85,989 (fetched 2026-10-20)
- **Latest release:** v3.2.0 (2026-10-18)
- **License:** MIT
- **Language:** JavaScript (skill + Node CLI under `archify/`)
- **Activity:** actively developed (pushed 2026-10-20)
- **Community:** Discord, WeChat/QQ groups; homepage https://archify.si
- **Distribution:** skills.sh installs reported at 130K+; agent switcher covers cursor, codex, claude-code, opencode
