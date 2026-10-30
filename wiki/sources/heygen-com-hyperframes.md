---
type: source
category: "Media, voice & content"
source_url: https://github.com/heygen-com/hyperframes
tags:
  - html-to-video
  - agent-skills
  - deterministic-render
  - headless-chrome
  - ffmpeg
  - motion-graphics
  - remotion-alternative
  - frame-md
related:
  - open-design.ai
  - calesthio-OpenMontage
  - bradautomates-claude-video
  - latent-spaces-brag
product: hyperframes
detail_level: standard
created: 2026-10-30
updated: 2026-10-30
---

HyperFrames is an open-source Apache 2.0 framework from HeyGen that turns HTML, CSS, media, and seekable animations into deterministic MP4 videos — designed for AI coding agents as much as humans. Compositions are plain HTML with data attributes (no React requirement, no build step); a headless Chrome + FFmpeg pipeline seeks each frame and encodes the same input to the same output for CI and automated rendering. The repo ships a CLI, ~450-block catalog, agent skills/plugins, Studio UI, AWS Lambda rendering, and `frame.md` design-system templates for video.

_All claims below are sourced from ../../raw/github/heygen-com-hyperframes.md unless otherwise noted._

## What it does

Authors define a video as an HTML composition: timing and tracks via `data-start`, `data-duration`, and `data-track-index`, with seekable animation from GSAP, CSS, Lottie, Three.js, Anime.js, WAAPI, or a custom frame adapter. Preview runs in the browser with live reload; render runs locally, in Docker, or on AWS Lambda. The renderer seeks each frame in headless Chrome and encodes with FFmpeg so output is deterministic.

Intended outputs include product launch videos, PR walkthroughs with animated diffs and captions, chart races and map animations, social videos with kinetic captions, docs/PDF/site-tour explainers, and reusable motion graphics for automated pipelines. Compared with Remotion, HyperFrames bets on plain HTML that agents already write instead of React components and a bundler.

## Installation

**Requirements:** Node.js 22+, FFmpeg. Desktop apps are also offered for macOS, Windows, and Linux (.deb).

**Claude Code plugin:**

```bash
claude plugin marketplace add heygen-com/hyperframes
claude plugin install hyperframes@hyperframes
```

**Standalone skills** (including OpenCode):

```bash
npx skills add heygen-com/hyperframes
```

For non-interactive / agent installs of the core skill set from current `main`:

```bash
npx hyperframes skills update
```

**Manual CLI project:**

```bash
npx hyperframes init my-video
cd my-video
npx hyperframes preview
npx hyperframes render
```

## Key features

- **HTML-native compositions** — `index.html` plays as-is; no proprietary timeline format and no required build step
- **Agent skills (7 published)** — core set `/hyperframes`, `/hyperframes-cli`, `/hyperframes-registry`, `/media-use`; on-demand `/figma`, `/slideshow`, `/remotion-to-hyperframes`
- **Catalog** — about 450 editable blocks/components (`npx hyperframes add …`) for transitions, overlays, titles, kinetic type, captions, charts, maps, 3D, camera moves
- **frame.md** — invert a web design system for the camera as a `DESIGN.md` superset agents can compose from; templates browsable at hyperframes.studio/design
- **Deterministic rendering** — same input → same frames → same MP4, aimed at CI, regression tests, and automated pipelines
- **Adapter-based animation** — GSAP, CSS, Lottie, Three.js, Anime.js, WAAPI, or custom runtimes registered as seekable timelines
- **Multi-surface stack** — CLI, core/engine/producer packages, Studio editor, embeddable player web component, shader transitions, AWS Lambda SDK
- **Agent plugin packaging** — Claude Code marketplace plugin; `bun run package:codex-plugin` builds a Codex-upload ZIP under 100 MB

## Architecture

Monorepo packages:

| Package | Role |
| --- | --- |
| `hyperframes` | CLI — scaffold, preview, lint, inspect, render |
| `@hyperframes/core` | Types, parsers, generators, linter, runtime, frame adapters |
| `@hyperframes/engine` | Seekable page-to-video capture via Puppeteer and FFmpeg |
| `@hyperframes/producer` | Full pipeline: capture, encode, audio mix |
| `@hyperframes/studio` | Browser composition editor UI |
| `@hyperframes/player` | Embeddable `<hyperframes-player>` web component |
| `@hyperframes/shader-transitions` | WebGL shader transitions |
| `@hyperframes/aws-lambda` | Distributed render deploy/SDK |

Composition model: a stage `div` with `data-composition-id` / dimensions holds media and overlays as timed clips; animation libraries register paused timelines on `window.__timelines` so the engine can seek by composition id. Skills live under `skills/` (and agent plugin dirs `.claude-plugin/`, `.codex-plugin/`, `.cursor-plugin/`, `.agents/`). Golden regression MP4 baselines under `packages/producer/tests/` use Git LFS (~240 MB).

## Example usage

Agent prompt after skills install:

> Using `/hyperframes`, create a 10-second product intro with a fade-in title, a background video, and subtle background music.

CLI and catalog:

```bash
npx hyperframes init my-video
cd my-video
npx hyperframes preview
npx hyperframes render
npx hyperframes add flash-through-white
npx hyperframes add instagram-follow
npx hyperframes add data-chart
```

Minimal composition shape (HTML + GSAP timeline registered for seeking):

```html
<div id="stage" data-composition-id="launch" data-start="0" data-width="1920" data-height="1080">
  <video class="clip" data-start="0" data-duration="6" data-track-index="0" src="intro.mp4" muted playsinline></video>
  <h1 id="title" class="clip" data-start="1" data-duration="4" data-track-index="1">Launch day</h1>
  <audio data-start="0" data-duration="6" data-track-index="2" data-volume="0.5" src="music.wav"></audio>
  <script>
    const tl = gsap.timeline({ paused: true });
    tl.from("#title", { opacity: 0, y: 40, duration: 0.8 }, 1);
    window.__timelines = window.__timelines || {};
    window.__timelines.launch = tl;
  </script>
</div>
```

## Maintenance status

75,715 GitHub stars, 6,897 forks, TypeScript, Apache License 2.0, default branch `main`, latest release v0.8.221 (2026-10-30), homepage https://hyperframes.heygen.com. Used in production at HeyGen; community adopters noted include tldraw and TanStack. Docs at hyperframes.heygen.com; Discord for community; npm package `hyperframes`.
