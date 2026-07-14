# oso95/scroll-world

## Metadata
- Stars: 1757
- Primary language: JavaScript
- Default branch: main
- Latest release: (none)
- License: MIT License
- Homepage: (none)
- Fetched: 2026-07-14
- Final URL: https://github.com/oso95/scroll-world

## Description
A skill that turn any brand into a scrollable 3D world

## README

# scroll-world

An agent skill — for Claude Code, Codex, and any `SKILL.md`-compatible agent — that builds an immersive, **scroll-scrubbed "fly through the world" landing page** for any industry or brand — the kind where, as you scroll, a camera flies from *outside* each scene *into* its interior, then flows on to the next scene with **no cuts**. One continuous connected flight through a little generated world (think the Emons logistics site, applied to whatever you want).

### Install

**Claude Code — as a plugin (recommended):**
```
/plugin marketplace add oso95/scroll-world
/plugin install scroll-world@scroll-world
```
Then ask for a scroll-through world landing page, or invoke `/scroll-world`.

**Codex & other agents — via the skills CLI** (Vercel's `skills` CLI, installs into Codex, Claude Code, Cursor, and 20+ other agents):
```bash
npx skills add oso95/scroll-world            # pick your agent(s) when prompted
npx skills add oso95/scroll-world -a codex   # or target Codex directly
```
In Codex, invoke with `$scroll-world` (or `/skills` to browse), or just ask for a scroll-through world landing page.

**Manually (drop-in skill):**
```bash
git clone https://github.com/oso95/scroll-world
cp -R scroll-world/skills/scroll-world ~/.claude/skills/   # Claude Code
cp -R scroll-world/skills/scroll-world ~/.codex/skills/    # Codex
```

### Requirements

- The Higgsfield CLI (higgsfield.ai), authenticated (`higgsfield auth login`), with credits.
- `ffmpeg` / `ffprobe` for frame extraction and encoding.
- Python 3 with Pillow (optional — only for the transparent-scene knockout).

### What it does

It leans on Higgsfield for the art: cohesive isometric diorama scenes (GPT Image 2) and the camera flights themselves (Seedance image-to-video), scrubbed by scroll position — the same technique behind Apple's scroll-through product pages. The camera genuinely moves; scroll only drives time. It's **framework-agnostic**: you get the Higgsfield pipeline, the prompt templates, and a portable vanilla-JS scrub engine that drops into plain HTML, Next.js, Vue, or a Python-served page — nothing assumes a stack.

When invoked, the skill:

1. **Interviews you** — the subject/industry + pitch, a brand kit (import from a URL, hand it over, or have it proposed), art direction, and the ordered scenes the camera visits.
2. **Generates the assets** with Higgsfield — one still per scene, one "dive-in" camera clip per scene, and the **connector** clips that join consecutive scenes, generated from the actual rendered frames of their neighbours so every seam is frame-identical.
3. **Wires it up** — a config-driven scroll engine that plays the whole chain as one flight.

### What's in the skill

```
skills/scroll-world/
├── SKILL.md                    the procedure + the seam rule + gotchas
└── references/
    ├── prompts.md              intake checklist + every Higgsfield prompt template
    ├── pipeline.md             copy-paste batch scripts (generate → frames → connectors → encode)
    ├── scrub-engine.js         portable, config-driven scrub engine (blob-seek, lazy load, seam crossfade)
    ├── index-template.html     a minimal standalone page that mounts the engine
    └── knockout.py             background knockout for floating scenes
```

### Notes

- Asset generation costs Higgsfield credits (~N image gens + ~2N-1 video gens for N scenes) and takes a while — the skill runs generations in the background and polls.
- The generated `.mp4`/`.webp` assets are produced per project; they're not shipped here.

### License

MIT.

## Top-level structure

- `skills/scroll-world/` — the self-contained skill: `SKILL.md` (procedure, seam rule, gotchas) plus `references/` (`prompts.md`, `pipeline.md`, `scrub-engine.js`, `index-template.html`, `knockout.py`)
- `.claude-plugin/` — plugin manifest for Claude Code marketplace distribution
- `README.md`, `LICENSE` (MIT)
