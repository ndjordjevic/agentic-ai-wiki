---
type: source
category: "Media, voice & content"
source_url: https://github.com/latent-spaces/brag
tags:
  - launch-video
  - agent-skill
  - hyperframes
  - brag-slim
  - social-share
  - motion
  - claude-code-plugin
related:
  - ParthJadhav-app-store-screenshots
  - skills.sh
  - higgsfield.ai
  - bradautomates-claude-video
product: brag
detail_level: standard
created: 2026-10-28
updated: 2026-10-28
---

/brag (~19.2k★, MIT, Python skill pack) turns a project you just built into a short shareable launch video (~20s) with music, motion, and share copy — classic mode via Hyperframes, plus `/brag-slim` rebuilt lean for Opus 5.5 without Hyperframes. Hosted shortcut: letsbrag.app.

_All claims below are sourced from ../../raw/github/latent-spaces-brag.md unless otherwise noted._

## What it does

One agent command reads the project and produces a launch video + cover image + short post. Slim mode auto-selects on Opus 5.5 (`/brag --full` keeps Hyperframes). Optional web path pastes a site URL at letsbrag.app.

## Installation

```bash
# Codex marketplace / plugin, or:
npx skills add https://github.com/latent-spaces/brag --skill brag-slim
# Claude Code plugin: marketplace add + install brag@brag; update for slim from 0.4.0
```

## Key features

- Full Hyperframes-powered `/brag` with soundtrack and motion
- `/brag-slim` for large models without bundled Hyperframes assets
- letsbrag.app hosted runner (skill remains OSS)
- Outputs video + cover + share copy

## Architecture

Agent skill/plugin wrapping Hyperframes (full) or model-native generation (slim). Docs site at https://latent-spaces.github.io/brag/.

## Example usage

After shipping a feature: run `/brag` (or slim) in Claude Code/Codex and post the generated clip.

## Maintenance status

~19,163 stars, 1,477 forks, MIT, `main`, release tag `brag`, homepage GitHub Pages docs.
