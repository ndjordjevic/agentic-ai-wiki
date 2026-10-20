---
type: source
category: "Media, voice & content"
source_url: https://github.com/calesthio/OpenMontage
tags:
  - agentic-video
  - production-pipelines
  - remotion
  - skill-files
  - tool-registry
  - documentary-montage
  - open-source
  - agplv3
related:
  - storytold
  - elevenlabs.io
  - bradautomates-claude-video
product: openmontage
detail_level: standard
created: 2026-10-20
updated: 2026-10-20
---

OpenMontage is an open-source agentic video production system that turns an AI coding assistant (Claude Code, Cursor, Copilot, Windsurf, Codex, etc.) into a full production studio: **12 pipelines**, **100+ tools**, **700+ skill/production-knowledge files**, scored provider selection, Backlot live storyboard, and Remotion/HyperFrames/FFmpeg composition. ~70k GitHub stars, AGPLv3, homepage [openmontage.video](https://www.openmontage.video/). It can generate motion from stills *or* cut real footage from free/open archives into finished timelines — not only “Ken Burns over images.”

_All claims below are sourced from ../../raw/github/calesthio-OpenMontage.md unless otherwise noted._

## What it does

Describe a video in plain language (or paste a YouTube/Short/Reel/TikTok/local reference). The agent selects a pipeline, researches the topic, proposes concepts with cost estimates, scripts and scene-plans, generates or retrieves assets, edits, composes, and self-reviews before presenting a final render. Creative gates (script, storyboard contact sheets) pause for human approval. **Backlot** (`python -m backlot open`) is a local living storyboard that mirrors project files as stages light up.

Named pipelines include Animated Explainer, Animation, Avatar Spokesperson, Cinematic, Clip Factory, Documentary Montage (CLIP-indexed free stock / Archive.org / NASA / Wikimedia / optional Pexels·Unsplash), Hybrid, Localization & Dub, Podcast Repurpose, Screen Demo, Talking Head, plus character-animation / HyperFrames paths called out in docs.

## Installation

**Prerequisites:** Python 3.10+, FFmpeg, Node.js 18+, and an AI coding assistant that can read files and run code.

```bash
git clone https://github.com/calesthio/OpenMontage.git
cd OpenMontage
make setup
```

Without `make` (macOS/Linux): create a venv, `pip install -r requirements.txt`, `npm install` in `remotion-composer/`, optional `piper-tts`, copy `.env.example` → `.env`. API keys in `.env` are optional — more keys unlock more providers (FAL, Kling, Pexels, etc.); zero-key paths still support real-footage documentary and local tooling per README.

Open the repo in your coding agent and prompt, e.g. a 60s explainer or a real-footage-only montage.

## Key features

- **End-to-end pipelines** — shared stage flow `research → proposal → script → scene_plan → assets → edit → compose`, each with a director skill and human approval points.
- **100+ tools / 60+ providers** — video, image, TTS, music, subtitles, enhancement, analysis, avatars; scored selection across 7 dimensions with auditable decision logs.
- **700+ skills** — pipeline directors, creative techniques, quality checklists, and Layer-3 technology packs under `.agents/skills/`.
- **Reference-driven starts** — analyze a loved video’s pacing/structure, then propose differentiated concepts with cost and tool-path honesty.
- **Real-footage documentary path** — build corpora from free/open motion sources and edit true B-roll timelines without paid generation APIs.
- **Backlot** — live board, storyboard approval gate, library of productions, scrubable run replay.
- **Render runtimes** — Remotion (default for data-driven React scenes) vs HyperFrames (HTML+GSAP / character-animation); choice locked as `render_runtime`.
- **Governance** — delivery-promise / slideshow-risk gates, pre-compose validation, post-render ffprobe + frame/audio review, budget caps and approval thresholds.

## Architecture

**Agent-first:** there is no Python orchestrator process — the coding assistant *is* the control plane. Python supplies tools, persistence, and registries; YAML manifests + Markdown skills hold creative/orchestration logic.

```
tools/              # registered production tools (video/audio/graphics/…)
pipeline_defs/      # YAML pipeline manifests
skills/             # Layer 2 OpenMontage conventions
  pipelines/        # per-stage director skills
  creative/ core/ meta/
.agents/skills/     # Layer 3 external tech knowledge packs
schemas/ styles/    # contracts + visual playbooks
remotion-composer/  # React/Remotion engine
lib/ backlot/       # checkpoints, pipeline loader, living storyboard
```

Three-layer knowledge: Layer 1 = what exists (tools + manifests); Layer 2 = how OpenMontage wants it used; Layer 3 = deep tech packs declared by tools.

## Example usage

```text
"Make a 60-second animated explainer about how neural networks learn"
"Make a 75-second documentary montage about city life in the rain. Use real footage only, no narration, elegiac tone, with music."
"Here's a YouTube Short I love. Make me something like this, but about quantum computing."
```

```bash
python -m backlot open                  # library of local productions
python -m backlot open <project-id>     # live board for one run
python -c "from tools.tool_registry import registry; import json; registry.discover(); print(json.dumps(registry.support_envelope(), indent=2))"
```

Agents should start from `AGENT_GUIDE.md` / `PROJECT_CONTEXT.md`, pick a pipeline, then follow manifest + stage skills rather than improvising workflow.

## Maintenance status

- **Stars:** 70,064 (fetched 2026-10-20)
- **Latest release:** none tagged
- **License:** GNU Affero General Public License v3.0 (AGPLv3)
- **Language:** Python (tools/lib) + Node/Remotion + Markdown/YAML skills
- **Activity:** pushed 2026-10-16; GitHub Discussions + YouTube @OpenMontage (prompts, pipelines, costs published per video)
- **Homepage:** https://www.openmontage.video/
