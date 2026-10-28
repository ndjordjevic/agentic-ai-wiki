---
type: source
category: "Design & UI generation"
source_url: https://github.com/ParthJadhav/app-store-screenshots
tags:
  - app-store
  - screenshots
  - agent-skill
  - nextjs-editor
  - marketing-assets
  - google-play
  - device-frames
related:
  - latent-spaces-brag
  - skills.sh
  - dembrandt-dembrandt-skills
  - AThevon-genjutsu
product: app-store-screenshots
detail_level: standard
created: 2026-10-28
updated: 2026-10-28
---

App Store Screenshots (~7.7k★, MIT, TypeScript) is an Agent Skill that scaffolds a production Next.js editor for App Store and Google Play marketing screenshots — connected canvas, device frames, inspector, git-trackable project state, and zip export at store-ready sizes.

_All claims below are sourced from ../../raw/github/ParthJadhav-app-store-screenshots.md unless otherwise noted._

## What it does

Turns raw app captures into ad-style slides with big copy; supports iPhone/Duo/iPad/Watch/TV/CarPlay/Mac/Android/feature graphic decks, locales/RTL, themes, and exact PNG bundles for required store sizes. Example decks accepted for a live App Store listing (Bloom).

## Installation

Install via skills.sh / `npx skills` for `parthjadhav/app-store-screenshots` (README cites skills.sh install badges). The skill scaffolds the Next.js editor into your project.

## Key features

- Connected-canvas editor with cross-screen elements + isolated legacy mode
- Device frames across Apple/Google form factors + Play feature graphic
- Persistent `app-store-screenshots.json` + uploaded assets under `public/screenshots/`
- 18 named visual styles and headline copy library
- One-click export zips at exact store dimensions

## Architecture

Skill → scaffolds a Next.js app that owns editing state and exports; agent-editable whenever the app UI changes.

## Example usage

Install the skill, feed it screenshots, edit on the canvas, export store-sized PNGs as a zip.

## Maintenance status

~7,670 stars, 554 forks, MIT, `main`, homepage product page on parthjadhav.com; strong skills.sh install traction per README badges.
