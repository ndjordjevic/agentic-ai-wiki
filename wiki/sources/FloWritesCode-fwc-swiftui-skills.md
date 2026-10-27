---
type: source
category: "Agent Skills & plugins ecosystem"
source_url: https://github.com/FloWritesCode/fwc-swiftui-skills
tags:
  - swiftui
  - ios
  - liquid-glass
  - iphone-duo
  - agent-skills
  - apple
  - foldable
  - claude-code
related:
  - emilkowalski-skills
  - anthropics-skills
  - skills.sh
  - kepano-obsidian-skills
  - davila7-claude-code-templates
product: fwc-swiftui-skills
detail_level: standard
created: 2026-10-27
updated: 2026-10-27
---

FloWritesCode/fwc-swiftui-skills (445 stars, MIT) is a small Agent Skills pack for modern SwiftUI development on iOS 26+, maintained by FloWritesCode. It currently ships two skills, one for Liquid Glass and one for the iPhone Duo foldable form factor, and follows the same Agent Skills folder convention as [[anthropics-skills]] and is installable through the skills CLI used by [[skills.sh]].

_All claims below are sourced from ../../raw/github/FloWritesCode-fwc-swiftui-skills.md unless otherwise noted._

## What it does

The README describes the repo as "Agent Skills for modern SwiftUI development on iOS 26+", working in Cursor, Codex, Claude Code, and any harness supporting the Agent Skills format. Two skills are listed:

| Skill | Description |
|---|---|
| `swiftui-liquid-glass` | Implement and review iOS 26+ Liquid Glass with native APIs, common patterns, and pitfalls |
| `swiftui-iphone-duo` | Adapt SwiftUI apps for iPhone Duo (iOS 27.1 SDK): size-based layout, vertical bars, fold-safe content, arrangement views, hinge interactions, and camera capture accessories |

The README says more skills will be added as separate folders under `skills/`. It does not describe skill internals beyond these one-line descriptions.

## Installation

Install the whole pack or a single skill with the skills CLI:

```bash
npx skills add FloWritesCode/fwc-swiftui-skills
npx skills add FloWritesCode/fwc-swiftui-skills --skill swiftui-liquid-glass
```

Manual install copies one skill folder into the agent's skills directory:

```bash
git clone https://github.com/FloWritesCode/fwc-swiftui-skills.git
cp -R fwc-swiftui-skills/skills/swiftui-liquid-glass ~/.agents/skills/
```

Other target directories: `~/.cursor/skills/`, `~/.claude/skills/`, `~/.codex/skills/`. Liquid Glass APIs require Xcode with the iOS 26 SDK.

## Key features

- **Liquid Glass guidance** — implementation and review of iOS 26+ Liquid Glass using native APIs, with patterns and pitfalls.
- **iPhone Duo adaptation** — layout and interaction guidance for a foldable device: size-based layout, fold-safe content, hinge interactions, vertical bars, arrangement views, camera capture accessories. The README ties this to the iOS 27.1 SDK.
- **Pick one skill or all** — the `--skill` flag installs a single skill.
- **Cross-agent** — Cursor, Codex, Claude Code, and others via the Agent Skills format; the skills CLI copies skills into each agent's directory.

## Architecture

The layout is minimal: `README.md`, `LICENSE`, and `skills/<skill-name>/` folders, each with a `SKILL.md` (YAML frontmatter with `name` and `description`) and an optional `reference.md` for long material. The README advises keeping skills focused and moving long reference content into `reference.md`. The repo also has a `.agents` directory. There is no runtime code and no language is detected by GitHub.

## Example usage

```bash
npx skills add FloWritesCode/fwc-swiftui-skills --skill swiftui-liquid-glass
# then ask the agent to review or implement Liquid Glass in a SwiftUI view
```

To contribute a skill, create `skills/<skill-name>/SKILL.md` with YAML frontmatter and add a row to the README's skills table.

## Maintenance status

445 stars, 23 forks, MIT License, default branch `main`, most recent push 2026-10-08, no tagged releases and no homepage. The pack is early-stage with two skills, but recently updated and targeted at pre-release SDK versions (iOS 26+ and iOS 27.1), so content may shift as Apple finalizes those APIs.
