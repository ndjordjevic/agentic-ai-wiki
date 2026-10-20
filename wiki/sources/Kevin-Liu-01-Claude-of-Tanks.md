---
type: source
category: "Business, career & learning"
source_url: https://github.com/Kevin-Liu-01/Claude-of-Tanks
tags:
  - multi-agent-showcase
  - claude-codex-pipeline
  - three-js
  - browser-game
  - procedural-vehicles
  - harness-case-study
  - dark-factory
related:
  - software-factory-claude-code
  - coleam00-harness-engineering-demo
  - dark-factory-autonomous-ai-codebase
product: claude-of-tanks
detail_level: standard
created: 2026-10-20
updated: 2026-10-20
---

Claude of Tanks is a World of Tanks-style browser combat simulator (Three.js + Vite) with 220 procedural vehicles, 33 destructible battlefields, and 13 modes — built end-to-end with a multi-agent Claude/Codex pipeline under human direction. Play at [cot.kevinliu.studio](https://cot.kevinliu.studio). With ~489 GitHub stars (MIT; Reserved Content on vehicles/maps/media), it matters to this wiki less as a framework and more as a concrete case study of multi-agent production of a large interactive app.

_All claims below are sourced from ../../raw/github/Kevin-Liu-01-Claude-of-Tanks.md unless otherwise noted._

## What it does

A full armored-combat product in the browser: fight (solo bots or browser-hosted multiplayer), inspect vehicles in Tank Gallery (armor, modules, exact-surface review packets), and direct shots in Scene Studio (deterministic timelines, stills, video). Combat includes plate-level armor, ballistics, internal modules, spotting/concealment, physics, and destructible worlds. English and Simplified Chinese UI; mouse/keyboard and touch controls.

## Installation

```bash
npm install
npx vite
npm test
npm run build
```

Play without building at https://cot.kevinliu.studio. Production deploys are **manual per round** (prebuilt Vercel CLI; git auto-deploys disabled). Verification scripts include `npm run test:net:v2:p2p` and `npm run tank:native:check`.

## Key features

- **Fleet & worlds** — 220 first-party procedural playables (0 GLB-sourced); 33 authored battlefields with shared destruction/collision kits; provenance gate strips comparison assets from public builds.
- **13 battle modes** — Standard, CTF, Zone Control, Turbo Ball, Gravity, Endless Horde, Frontline Assault campaign, Juggernaut, Infected, Realistic, Gun Game, Drone, AC-130; fixed **60 Hz** authority.
- **Vehicle-specific systems** — magazine autoloaders, guided missiles, hydropneumatic aim, shared specs across garage/Gallery/Studio/bots.
- **Presentation** — Three.js/WebGL with adaptive quality, measured 120 FPS test path, SMAA/FSR, GPU recovery.
- **Multiplayer** — LAN/private rooms over WebRTC in the host browser; small rooms Worker for internet signaling; no dedicated game DB required for private rooms.
- **Production tooling** — Scene Studio, deterministic capture harness, tank-generation handbook with agent briefs and review gates.

## Architecture

Runtime split: controls → **deterministic authority** (movement, ballistics, armor, spotting, bots, results) → filtered state/events → **presentation** (procedural vehicles, FX, HUD, Three.js, Studio).

```text
src/engine/   renderer, camera, lighting, post, quality
src/world/    maps, terrain, props, collision, destruction
src/vehicles/ specs, procedural geometry, verification
src/sim/      DOM-free movement, aim, ballistics, armor, damage, spotting
src/game/     bots, input, killcam, Scene Studio composition
src/mp/       rooms, wire, transports, browser host
src/ui/       garage, HUD, settings, touch
```

**Multi-agent provenance:** historical `docs/ARCHITECTURE.md` locked a **nine-module parallel builder** plan (engine, world, vehicles, movement, combat, ai, hud, fx, audio + integration) where agents implemented modules **without talking to each other**, sharing only that contract. Credits: Kevin B. Liu created/directed; Claude and Codex assisted as tools, not co-authors.

## Example usage

```bash
# Local play
npx vite

# Regenerate public media archive (capture harness)
npm run shots:battle:generate
npm run shots:battle:grade -- --root shots/marketing-battles-r3
npm run studio:action:render
npm run showcase:publish
```

Field manual / docs: https://cot.kevinliu.studio/docs · engineering index in-repo at `docs/INDEX.md`.

## Maintenance status

- **Stars:** 489 (fetched 2026-10-20)
- **Latest release:** none tagged
- **License:** MIT (gameplay code); procedural vehicles, maps, generated assets, and branding are proprietary Reserved Content
- **Language:** TypeScript (Vite + Three.js)
- **Activity:** actively developed (pushed 2026-10-20)
- **Homepage:** https://cot.kevinliu.studio
