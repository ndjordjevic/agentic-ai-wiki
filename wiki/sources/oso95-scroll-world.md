---
type: source
category: "Design & UI generation"
source_url: https://github.com/oso95/scroll-world
tags:
  - agent-skill
  - scroll-scrubbed-video
  - higgsfield
  - landing-page-generation
  - isometric-diorama
  - camera-flight
  - framework-agnostic
  - multi-harness
related:
  - higgsfield.ai
  - motionsites.ai
  - stitch.withgoogle.com
  - davila7-claude-code-templates
product: scroll-world
detail_level: standard
created: 2026-07-14
updated: 2026-07-14
---

`scroll-world` (1,757 stars, MIT) is an Agent Skill that builds Apple-style scroll-scrubbed "fly through the world" landing pages for any brand or industry: a camera flies from outside each generated scene into its interior, then continues into the next scene with no cuts, driven entirely by scroll position. It's a thin orchestration layer over the Higgsfield generative-media API — the skill contributes the interview flow, prompt templates, seam-matching procedure, and a portable vanilla-JS scrub engine, not a custom rendering or generation model.

_All claims below are sourced from ../../raw/github/oso95-scroll-world.md unless otherwise noted._

## What it does

When invoked, the skill interviews the user for the subject/industry and pitch, a brand kit (imported from a URL, handed over directly, or proposed by the skill), art direction, and the ordered sequence of scenes the camera should visit. It then generates assets via Higgsfield: one still per scene (GPT Image 2, isometric diorama style), one "dive-in" camera clip per scene (Seedance image-to-video), and — the key technical move — **connector clips** generated from the actual rendered end-frames of neighbouring scenes, so every transition seam is frame-identical rather than a cut or crossfade. Finally it wires the generated assets into a config-driven scroll engine that plays the whole chain as one continuous flight, scroll position mapping directly to playback time while the camera motion itself is baked into the pre-rendered video.

## Installation

**Claude Code** (recommended, plugin marketplace):
```
/plugin marketplace add oso95/scroll-world
/plugin install scroll-world@scroll-world
```
Then ask for a scroll-through world landing page, or invoke `/scroll-world`. **Codex and 20+ other agents** via Vercel's `skills` CLI:
```bash
npx skills add oso95/scroll-world -a codex
```
invoked in Codex as `$scroll-world`. **Manual/drop-in**: clone the repo and copy `skills/scroll-world` into the target agent's skills directory (`~/.claude/skills/`, `~/.codex/skills/`, etc.). Requires the Higgsfield CLI authenticated with credits (`higgsfield auth login`), `ffmpeg`/`ffprobe` for frame extraction and encoding, and optionally Python 3 + Pillow for transparent-scene background knockout. (../../raw/github/oso95-scroll-world.md)

## Key features

- **Frame-identical seam matching** — connector clips between consecutive scenes are generated from the real rendered end-frame of one scene and start-frame of the next, rather than a generic transition, which is what makes the flight read as one continuous camera move instead of a slideshow.
- **Framework-agnostic delivery** — output is a portable vanilla-JS scrub engine (`scrub-engine.js`) with blob-seek, lazy loading, and seam crossfade, plus a minimal `index-template.html` — drops into plain HTML, Next.js, Vue, or a Python-served page with no assumed stack.
- **Full prompt-template library shipped in-repo** — `references/prompts.md` (intake checklist + every Higgsfield prompt template) and `references/pipeline.md` (copy-paste batch scripts for generate → frames → connectors → encode) make the generation procedure inspectable and editable rather than opaque.
- **Background knockout** — `knockout.py` optionally removes scene backgrounds for floating-scene compositions.
- **Background/async generation** — asset generation is long-running and costly (Higgsfield credits: roughly N image generations + 2N-1 video generations for N scenes), so the skill runs generations in the background and polls rather than blocking the session.

## Architecture

The entire skill is one self-contained folder, `skills/scroll-world/`: `SKILL.md` holds the procedure, the seam-matching rule, and known gotchas; `references/` holds everything else — prompt templates, batch pipeline scripts, the scrub engine, the HTML mount template, and the knockout script. A `.claude-plugin/` manifest handles Claude Code marketplace distribution; the same skill folder installs unmodified into Codex, Cursor, and other `SKILL.md`-compatible hosts via Vercel's skills CLI. There is no custom generation model or rendering engine in the repo — all art and video generation is delegated to Higgsfield's API (GPT Image 2 for stills, Seedance for image-to-video), and the repo's own code is limited to orchestration (prompt construction, batch scripts) and the client-side playback engine. Generated `.mp4`/`.webp` assets are produced per-project and are not shipped in the repo. (../../raw/github/oso95-scroll-world.md)

## Example usage

```
/plugin marketplace add oso95/scroll-world
/plugin install scroll-world@scroll-world
/scroll-world
```
Then answer the skill's interview prompts (subject/industry, brand kit, art direction, ordered scene list) and let it run the Higgsfield generation pipeline in the background. (../../raw/github/oso95-scroll-world.md)

## Maintenance status

1,757 GitHub stars, 224 forks, MIT licensed, default branch `main`, most recent push 2026-07-10, no tagged releases. Small, single-purpose repo (JavaScript primary language — the scrub engine and templates). (../../raw/github/oso95-scroll-world.md)

## Ecosystem

Built entirely on top of [[higgsfield.ai]] (both the still-image and video-generation legs of the pipeline require an authenticated, credited Higgsfield account) — scroll-world is best understood as a packaged, repeatable *workflow* over Higgsfield's generative primitives rather than a competing product. Sits in the same "AI generates a marketing/landing surface" niche as [[motionsites.ai]] (prompt-template library for AI website builders) and [[stitch.withgoogle.com]] (AI UI generation), but is distinguished by producing pre-rendered, scroll-scrubbed video rather than live-rendered UI or copy-paste prompts — the output is closer to an Apple product-page microsite than a typical AI-generated web page. Installable through the same multi-host skill-distribution mechanisms as [[davila7-claude-code-templates]] catalogs (Claude Code plugin marketplace, Vercel's skills CLI).
