---
type: source
category: "Design & UI generation"
source_url: https://github.com/elayadesign/ai-design-skills
tags:
  - agent-skills
  - landing-page
  - design-to-motion
  - anti-slop
  - multi-host
  - claude-code
  - cursor-rules
related:
  - leonxlnx-taste-skill
  - emilkowalski-skills
  - Owl-Listener-designer-skills
  - skills.sh
  - ConardLi-garden-skills
  - jakubkrehel-skills
  - codeswithroh-tastemaker
  - MengTo-Skills
product: ai-design-skills
detail_level: standard
created: 2026-10-27
updated: 2026-10-27
---

elayadesign/ai-design-skills (8,362 stars, MIT) is a small, growing collection of self-contained design Agent Skills for Claude Code, Cursor, Codex, Windsurf, and other markdown-rules hosts. It currently ships two skills — `landing-page-design` (intake → structure → conversion copy → visual system) and `design-to-motion` (static design → looping pixel-exact animated showcase exported as MP4/GIF) — and points redesign work to a separate sibling repo. Credits explicitly adapt ideas from [[leonxlnx-taste-skill]], [[emilkowalski-skills]], and [[Owl-Listener-designer-skills]].

_All claims below are sourced from ../../raw/github/elayadesign-ai-design-skills.md unless otherwise noted._

## What it does

| Skill | Job |
|---|---|
| `landing-page-design` | Build a landing page from scratch: intake questions, page structure, conversion copy, and a full visual system (type, spacing, radius, motion). |
| `design-to-motion` | Turn a static design into a pixel-exact animated showcase (empty → loaded, looping story beats, background untouched) exported as MP4 for X/site and 800×500 GIFs. |

Design values (fonts, colors, spacing, motion) live in one editable section near the bottom of each `SKILL.md` so forks can re-theme without rewriting the workflow. Redesign-of-existing-site work is deferred to https://github.com/elayadesign/redesign-skill.

## Installation

Claude Code (copy one skill folder):

```bash
mkdir -p .claude/skills
git clone https://github.com/elayadesign/ai-design-skills.git /tmp/ai-design-skills
cp -r /tmp/ai-design-skills/skills/<skill-name> .claude/skills/
```

Cursor (rules file):

```bash
mkdir -p .cursor/rules
curl -o .cursor/rules/<skill-name>.md \
  https://raw.githubusercontent.com/elayadesign/ai-design-skills/main/skills/<skill-name>/SKILL.md
```

Codex / Windsurf / Cline: copy `SKILL.md` into `AGENTS.md`, `.windsurfrules`, `.clinerules`, or the system prompt. Claude.ai: upload/attach the `SKILL.md` and say "follow this."

## Key features

- **Two focused skills** rather than a large catalog — landing page generation and design-to-motion export.
- **Multi-host install recipes** documented for Claude Code, Cursor, Codex, Windsurf, Cline, and Claude.ai.
- **Forkable design values** — one section per skill drives fonts/colors/spacing/motion for the rest of the playbook.
- **Explicit upstream credits** — content realism/motion ideas from taste-skill; motion rules from Emil Kowalski, Owl-Listener designer-skills, and dylantarre/animation-principles.

## Architecture

Minimal repo: `skills/landing-page-design/` and `skills/design-to-motion/` (each a self-contained skill folder with `SKILL.md`), plus LICENSE and README. No plugin marketplace manifest in the capture — distribution is clone/copy/curl.

## Example usage

```bash
cp -r /tmp/ai-design-skills/skills/landing-page-design .claude/skills/
# then ask: "build a landing page following the landing-page-design skill"
```

## Maintenance status

8,362 GitHub stars, 598 forks, MIT licensed, default branch `main`, most recent push 2026-10-26, no tagged releases. Primary language unset in GitHub metadata (Markdown skill pack). README states "More on the way."
