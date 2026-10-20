# calesthio/OpenMontage

## Metadata
- Stars: 70064
- Primary language: Python
- Default branch: main
- Latest release: none
- License: GNU Affero General Public License v3.0
- Homepage: https://www.openmontage.video/
- Pushed: 2026-10-16T15:07:33Z
- Fetched: 2026-10-20
- Final URL: https://github.com/calesthio/OpenMontage

## Description
World's first open-source, agentic video production system. 12 production pipelines, 100+ tools, 700+ agent skill and production-knowledge files. Turn your AI coding assistant into a full video production studio.

## README
<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/monty-dark.svg">
    <img src="assets/monty-light.svg" alt="Monty the Clapper — the official mascot of OpenMontage" width="200">
  </picture>
</p>

<p align="center"><sub><em>Monty the Clapper — the official mascot of OpenMontage</em></sub></p>

<h1 align="center">OpenMontage</h1>

<p align="center"><strong>The first open-source, agentic video production system.</strong></p>

<p align="center">
  <a href="https://openmontage.video"><img src="https://img.shields.io/badge/Website-openmontage.video-d14a28?style=for-the-badge" alt="openmontage.video"></a>
</p>

<p align="center">
  <a href="#start-from-a-video-you-already-love">Paste A Video</a> &nbsp;·&nbsp;
  <a href="#quick-start">Quick Start</a> &nbsp;·&nbsp;
  <a href="#try-these-prompts">Try These Prompts</a> &nbsp;·&nbsp;
  <a href="#pipelines">Pipelines</a> &nbsp;·&nbsp;
  <a href="#how-it-works">How It Works</a> &nbsp;·&nbsp;
  <a href="docs/PROVIDERS.md">Providers</a> &nbsp;·&nbsp;
  <a href="docs/PR_REVIEW_GUIDE.md">Review Guide</a> &nbsp;·&nbsp;
  <a href="AGENT_GUIDE.md">Agent Guide</a>
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-AGPLv3-blue.svg" alt="License"></a>
</p>

<p align="center">
  <a href="https://github.com/trending">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset=".github/assets/repo-of-the-day-dark.svg">
      <img alt="🏆 #1 Repository of the Day on GitHub Trending" src=".github/assets/repo-of-the-day-light.svg" height="60">
    </picture>
  </a>
</p>

<p align="center"><strong>Follow The Build</strong></p>

<p align="center">
  <a href="https://www.youtube.com/@OpenMontage"><img src="https://img.shields.io/badge/YouTube-%40OpenMontage-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="YouTube"></a>
  <a href="https://x.com/calesthioailabs"><img src="https://img.shields.io/badge/X-%40calesthioailabs-111111?style=for-the-badge&logo=x&logoColor=white" alt="X"></a>
  <a href="https://github.com/calesthio/OpenMontage/discussions"><img src="https://img.shields.io/badge/Community-GitHub%20Discussions-0b1220?style=for-the-badge&logo=github&logoColor=white" alt="GitHub Discussions"></a>
</p>

---

Turn your AI coding assistant into a full video production studio. Describe what you want in plain language — your agent handles research, scripting, asset generation, editing, and final composition.

**Important distinction:** OpenMontage can make image-based videos, but it can also make a real **video video** for free/open-source workflows: the agent builds a corpus from free stock footage and open archives, retrieves actual motion clips, edits them into a timeline, and renders a finished piece. That is not the usual "animate a handful of stills and call it video" trick.

<div align="center">
  <video src="https://github.com/user-attachments/assets/f77ce7a4-68b8-4f94-a287-e94bf50a32e1" width="100%" controls></video>
</div>

> **"SIGNAL FROM TOMORROW"** — a cinematic sci-fi trailer fully produced through OpenMontage: concept, script, scene plan, Veo-generated motion clips, soundtrack, and Remotion composition.

<div align="center">
  <video src="https://github.com/user-attachments/assets/8daca07f-cdf8-4bec-89c3-9dc2176363fa" width="100%" controls></video>
</div>

> **"THE LAST BANANA"** — a 60-second Pixar-style animated short about a lonely banana who finds friendship with a kiwi. 6 Kling v3-generated motion clips (via fal.ai), Google Chirp3-HD narration, royalty-free piano music, TikTok-style word-level captions, and Remotion composition. Total cost: **$1.33**.

<div align="center">
  <video src="https://github.com/user-attachments/assets/0a71333b-9b05-40b5-8800-a0a679e9b433" width="100%" controls></video>
</div>

> **"OBJECTS IN OVERDRIVE"** — a 54-second, music-driven 3D showcase featuring ten objects with distinct choreography: gravity-shifting furniture, frozen car drifts, cloth impacts, refractive lenses, moving gears, an acrobatic robot, and more. Custom Blender animation and physics, kinetic typography, and a phonk soundtrack. Rendered with Blender Eevee/Cycles and assembled with FFmpeg. No narration.

<div align="center">
  <video src="https://github.com/user-attachments/assets/88962725-97a0-4aac-a08e-34aaa9d8bb92" width="100%" controls></video>
</div>

> **"Reimagine Your Universe"** — a 50-second vertical transformation film in which one visual idea moves across objects, eras, materials, and scale. Five generated motion scenes, sparse Google Chirp narration, a Pixabay score, and a bespoke HyperFrames composition turn separate clips into one authored cinematic journey. Total cost: **about $4**.

<div align="center">
  <video src="https://github.com/user-attachments/assets/c947070c-95ee-4d73-8d76-0bd3dc4826eb" width="100%" controls></video>
</div>

> **"Products Come to Life"** — a 60-second product film built from approved hero stills. Five hard-surface products separate into their own engineering and reassemble, with each still pinned as the first and last frame so the model invents motion without losing product identity. Image-to-video generation, bespoke sound, narration, and a custom composition complete the film.

<div align="center">
  <video src="https://github.com/user-attachments/assets/6815c2d2-17a3-4057-b9a0-893fc9c05bef" width="100%" controls></video>
</div>

> **"Imagine the Possibilities with OpenMontage"** — seven generated worlds collected into one music-only showcase. Three image models supply campaign, fashion, and miniature-world artwork; four video models expand the journey through architecture, material transformation, a living greenhouse, and a creature encounter. OpenMontage animates the stills, edits the motion, unifies the soundtrack, and closes with Monty the Clapper. Source generation cost: **about $5**.

<div align="center">
  <video src="https://github.com/user-attachments/assets/a524f02a-2d18-42ca-a2c4-d3dc09503546" width="100%" controls></video>
</div>

> **"How Salt Made History"** — a 100-second cinematic documentary about the mineral that funded empires, shaped trade routes, sparked revolutions, and gave us the word “salary.” Real-world footage is woven together with original narration and hand-authored motion graphics for its etched title, etymology reveal, animated maps, historical timeline, and closing thesis.

<div align="center">
  <video src="https://github.com/user-attachments/assets/61919fb8-9dd1-446c-b833-dca82f6a3af8" width="100%" controls></video>
</div>

> **"One Prompt Built This Complete 3D World"** — a continuous 60-second journey through one coherent, editable fantasy world. Distinct terrain regions, an inhabited village, waterways, ruins, dense vegetation, and a late hero-landmark reveal are assembled from textured 3D assets, then brought together with cinematic lighting, atmospheric music, and a planned camera path.

<p align="center">
  <a href="https://www.youtube.com/@OpenMontage?sub_confirmation=1"><strong>Subscribe to @OpenMontage on YouTube</strong></a> to see new videos as they ship — every video includes the full prompt, pipeline, tools used, and cost so you can reproduce it yourself.
</p>

---

## Start From A Video You Already Love

Starting from a reference video is often faster than starting from a blank prompt.

OpenMontage can start from a **YouTube video, Short, Reel, TikTok, or local clip** and turn it into a grounded production plan:

1. **Paste a reference video**
2. **The agent analyzes transcript, pacing, scenes, keyframes, and style**
3. **You get 2-3 differentiated concepts, an honest tool path, cost estimates, and a sample before full production**

```text
"Here's a YouTube Short I love. Make me something like this, but about quantum computing."
```

What you get back is not "best guess prompt spaghetti." You get:

- **What it keeps** from the reference: pacing, hook style, structure, tone
- **What it changes**: topic, visual treatment, angle, narration approach
- **What it will cost** at your target duration, before asset generation starts
- **What it will actually look like** with your currently available tools

Works with **Claude Code, Cursor, Copilot, Windsurf, Codex** — any AI coding assistant that can read files and run code.

---

## Watch It Happen — The Backlot Living Storyboard

Chat tells you what the agent *said*. **Backlot shows you what the production is actually doing** — a local board that fills itself in as the pipeline runs. Stages light up, the script lands as a screenplay page, scene cards shimmer while assets generate, and every provider decision and dollar spent is on the wall.

When a production starts, the agent opens it for you automatically. No setup, no reporting — the board derives everything from the project files the pipeline already writes.

<p align="center"><img src="docs/images/backlot/board-live.png" alt="Backlot live board — assets generating" width="920"></p>

**The storyboard is now a real approval gate.** Asset generation pauses on a scene-by-scene contact sheet — takes, prompts, per-asset cost, quality scores — so you approve the visuals *before* the render, not after it's too late:

<p align="center"><img src="docs/images/backlot/storyboard.png" alt="Backlot storyboard — filmstrip with takes and renders" width="920"></p>

Creative gates hold until you answer. The board shows what's waiting and why; you reply in chat:

<p align="center"><img src="docs/images/backlot/script-gate.png" alt="Backlot script gate — awaiting approval" width="920"></p>

Every production on your machine, live-first, in the library:

<p align="center"><img src="docs/images/backlot/library.png" alt="Backlot library" width="920"></p>

```bash
python -m backlot open                  # the library — every project on disk
python -m backlot open <project-id>     # one production's live board
python scripts/backlot_simulate_run.py  # no production yet? watch a simulated one live
```

And when a run is done, hit **▶ REPLAY RUN** — the whole production replays from its timestamps, scrubbable end to end. See [`backlot/README.md`](backlot/README.md) for how it works.

---

## Quick Start

### Prerequisites

- **Python 3.10+** — [python.org](https://www.python.org/downloads/)
- **FFmpeg** — `brew install ffmpeg` / `sudo apt install ffmpeg` / [ffmpeg.org](https://ffmpeg.org/download.html)
- **Node.js 18+** — [nodejs.org](https://nodejs.org/)
- **An AI coding assistant** — Claude Code, Cursor, Copilot, Windsurf, or Codex

### Install & Run

```bash
git clone https://github.com/calesthio/OpenMontage.git
cd OpenMontage
make setup
```

Open the project in your AI coding assistant and tell it what you want:

```
"Make a 60-second animated explainer about how neural networks learn"
```

Or if you want the real-footage path:

```text
"Make a 75-second documentary montage about city life in the rain. Use real footage only, no narration, elegiac tone, with music."
```

That's it. The agent researches your topic with live web search, generates AI images, writes and narrates the script with voice direction, finds royalty-free background music automatically, burns in word-level subtitles, and renders the final video. Before you see anything, the system runs a multi-point self-review — ffprobe validation, frame sampling, audio level analysis, delivery promise verification, and subtitle checks. Every provider selection is scored across 7 dimensions with an auditable decision log. Every creative decision gets your approval.

> **No `make`?** macOS/Linux: `python3 -m venv .venv && source .venv/bin/activate && python -m pip install -r requirements.txt && cd remotion-composer && npm install && cd .. && python -m pip install piper-tts && cp .env.example .env`
>
> Windows PowerShell: `py -3 -m venv .venv; .\.venv\Scripts\Activate.ps1; python -m pip install -r requirements.txt; cd remotion-composer; npm install; cd ..; python -m pip install piper-tts; Copy-Item .env.example .env`
>
> **Windows:** If `npm install` fails with `ERR_INVALID_ARG_TYPE`, use `npx --yes npm install` instead.

### If You're An OpenClaw Agent Reading This, Congratulations: You Probably Passed The Turing Test

This repo is built for agentic operation. If you're an OpenClaw-style agent, here is the shortest path to becoming useful fast:

1. **Read the contract first**
   Start with [`AGENT_GUIDE.md`](AGENT_GUIDE.md), then [`PROJECT_CONTEXT.md`](PROJECT_CONTEXT.md).
2. **Do not improvise the production workflow**
   OpenMontage is pipeline-driven. Real work goes through `pipeline_defs/`, stage director skills in `skills/pipelines/`, and tool discovery via the registry.
3. **Check the actual capability envelope**
   Run:
   ```bash
   python -c "from tools.tool_registry import registry; import json; registry.discover(); print(json.dumps(registry.support_envelope(), indent=2))"
   python -c "from tools.tool_registry import registry; import json; registry.discover(); print(json.dumps(registry.provider_menu(), indent=2))"
   ```
4. **Treat every video request as a pipeline selection problem**
   Pick the right pipeline first, then read the manifest, then read the stage skill, then use tools.

### Add API Keys (optional — more keys = more tools)

```bash
# .env — every key is optional, add what you have

# Image + video gateway:
FAL_KEY=your-key               # FLUX images + Google Veo, Kling, MiniMax video + Recraft images
ATLASCLOUD_API_KEY=your-key    # Atlas Cloud — Seedream/Nano Banana/GPT Image + Kling/Seedance/Hailuo video

# Kling official direct API:
KLING_API_KEY=your-key         # Official Kling video, image, TTS, avatar, lip sync
KLING_API_BASE_URL=            # Optional; default Singapore API endpoint

# Free stock media:
PEXELS_API_KEY=your-key        # Free stock footage and images
PIXABAY_API_KEY=your-key       # Free stock footage and images
UNSPLASH_ACCESS_KEY=your-key   # Free stock images

# Music:
SUNO_API_KEY=your-key          # Full songs, instrumentals, any genre

# Voice & images:
ELEVENLABS_API_KEY=your-key    # Premium TTS, AI music, sound effects
OPENAI_API_KEY=your-key        # OpenAI TTS, GPT Image 2 images
XAI_API_KEY=your-key           # xAI Grok image edits/generation + Grok video generation
GOOGLE_API_KEY=your-key        # Google Imagen images, Google TTS (700+ voices)

# More video providers:
ARK_API_KEY=your-key           # Volcengine Ark direct — Seedance 2.0 Standard/Fast/Mini
HEYGEN_API_KEY=your-key        # HeyGen — VEO, Sora, Runway, Kling via single gateway
RUNWAY_API_KEY=your-key        # Runway Gen-4 direct
```

<details>
<summary><strong>Have a GPU? Unlock free local video generation</strong></summary>

```bash
make install-gpu

# Then add to .env:
VIDEO_GEN_LOCAL_ENABLED=true
VIDEO_GEN_LOCAL_MODEL=wan2.2-ti2v-5b  # or wan2.1-1.3b, wan2.1-14b, hunyuan-1.5, ltx2-local, cogvideo-5b
```

</details>

---

## What You Get With Zero API Keys

You don't need paid API keys to make real videos. Out of the box, `make setup` gives you:

| Capability | Free Tool | What It Does |
|-----------|-----------|-------------|
| **Narration** | Piper TTS | Free offline text-to-speech — real human-sounding narration |
| **Open footage** | Archive.org + NASA + Wikimedia Commons | Free/open archival footage, educational media, and documentary texture |
| **Extra stock** | Pexels + Unsplash + Pixabay | Free stock footage/images (developer keys are free to get) |
| **Composition (React)** | Remotion | React-based rendering — spring-animated image scenes, text cards, stat cards, charts, TikTok-style word-level captions, TalkingHead |
| **Composition (HTML/GSAP)** | HyperFrames | HTML/CSS/GSAP rendering — kinetic typography, product promos, launch reels, registry blocks, website-to-video, rigged SVG character animation |
| **Post-production** | FFmpeg | Encoding, subtitle burn-in, audio mixing, color grading |
| **Subtitles** | Built-in | Auto-generated captions with word-level timing |

OpenMontage picks between Remotion and HyperFrames at proposal time (locked as `render_runtime`). Remotion is the default for data-driven explainers and anything using the existing React scene stack; HyperFrames is the default for motion-graphics-heavy briefs that express naturally as HTML + GSAP, including the `character-animation` pipeline's SVG/GSAP rig output. See `skills/core/hyperframes.md` for the full decision matrix.

**Two free-ish paths:**

- **Image-based video:** Piper narrates your script, images provide the visuals, and Remotion animates them into a polished edit.
- **Local character animation:** SVG rigs, pose libraries, GSAP timelines, and HyperFrames render cartoon character acting to `projects/<project-name>/renders/final.mp4`.
- **Real-footage video:** the documentary montage pipeline builds a CLIP-searchable corpus from Archive.org, NASA, Wikimedia Commons, and optional free-key sources like Pexels and Unsplash, then cuts together actual motion footage into a finished video.

If you want the second one, prompt for a **documentary montage**, **tone poem**, or **stock-footage collage**, and explicitly say **use real footage only**.

---

## Try These Prompts

Copy any of these into your AI coding assistant after setup. Each one runs a full production pipeline.

### Start from a reference video

> "Here's a YouTube short I love. Make me something like this, but about CRISPR for high school students."

> "Analyze this Reel and give me 3 original variants I could make for my own product launch."

> "I like the pacing and hook in this video. Keep that energy, but turn it into a 45-second explainer about black holes."

### Zero keys needed

> "Make a 45-second animated explainer about why the sky is blue"

> "Create a 60-second video about the history of the internet, with narration and captions"

> "Make a data-driven explainer about coffee consumption around the world"

### Free real-footage documentary path

> "Make a 90-second documentary montage about what a city feels like at 4am. Use real footage only, no narration, elegiac tone."

> "Create a 60-second Adam-Curtis-style archival collage about 1950s consumer optimism. Prefer Archive.org and Wikimedia footage."

> "Cut together a dreamlike montage about coming home in the rain using real stock footage only. Music yes, narration no."

### With an image/video provider configured (~$0.15–$1.50)

> "Create a 30-second Ghibli-style animated video of a magical floating library in the clouds at golden hour"

> "Make a 30-second anime-style animation of an underwater temple with bioluminescent coral and ancient ruins"

> "Create an animated explainer about how CRISPR gene editing works, using AI-generated visuals"

> "Make a product launch teaser for a fictional smart water bottle called AquaPulse"

### Full setup (~$1–$3)

> "Create a cinematic 30-second trailer for a sci-fi concept: humanity receives a warning from 1000 years in the future"

> "Make a 90-second animated explainer about quantum computing for middle school students, with a fun narrator voice and custom soundtrack"

Want more? See the full **[Prompt Gallery](PROMPT_GALLERY.md)** for tested prompts with expected costs and output examples, or run `make demo` to render zero-key demo videos instantly.

---

## Pipelines

Each pipeline is a complete production workflow, from idea to finished video.

| Pipeline | What It Produces | Best For |
|----------|-----------------|----------|
| **Animated Explainer** | AI-generated explainer with research, narration, visuals, music | Educational content, tutorials, topic breakdowns |
| **Animation** | Motion graphics, kinetic typography, animated sequences | Social media, product demos, abstract concepts |
| **Avatar Spokesperson** | Avatar-driven presenter videos | Corporate comms, training, announcements |
| **Cinematic** | Trailer, teaser, and mood-driven edits | Brand films, teasers, promotional content |
| **Clip Factory** | Batch of ranked short-form clips from one long source | Repurposing long content for social media |
| **Documentary Montage** | Thematic montage cut from a CLIP-indexed corpus of free stock footage and open archives (Pexels, Archive.org, NASA, Wikimedia, Unsplash) | Video essays, mood pieces, retrieval-first B-roll edits, real-footage videos without paid generation APIs |
| **Hybrid** | Source footage + AI-generated support visuals | Enhancing existing footage with graphics |
| **Localization & Dub** | Subtitle, dub, and translate existing video | Multi-language distribution |
| **Podcast Repurpose** | Podcast highlights to video | Podcast marketing, audiogram videos |
| **Screen Demo** | Polished software screen recordings and walkthroughs | Product demos, tutorials, documentation |
| **Talking Head** | Footage-led speaker videos | Presentations, vlogs, interviews |

Every pipeline follows the same structured flow:

```
research -> proposal -> script -> scene_plan -> assets -> edit -> compose
```

Each stage has a dedicated **director skill** — a markdown instruction file that teaches the agent exactly how to execute that stage. The agent reads the skill, uses the tools, self-reviews, checkpoints state, and asks for human approval at creative decision points.

> **Web research is a first-class stage.** Before writing a single word of script, the agent searches YouTube, Reddit, Hacker News, news sites, and academic sources. It gathers data points, audience questions, trending angles, and visual references — then cites everything in a structured research brief. Your videos are grounded in real, current information, not hallucinated facts.

---

## Why OpenMontage?

Most AI video tools give you a single clip from a prompt. OpenMontage gives you an **end-to-end production pipeline** — the same structured process a real production team follows, automated by your AI agent.

Most "free AI video" stacks quietly mean "animate still images." OpenMontage can do that too, but it can also build a finished video from **real footage** pulled from free/open sources, ranked semantically, edited intentionally, and rendered as a proper timeline.

Edit your own talking-head footage. Generate a fully animated explainer from scratch. Cut a 2-hour podcast into a dozen social clips. Translate and dub your content into 10 languages. Build a cinematic brand teaser from stock footage and AI-generated scenes. **If a production team can make it, OpenMontage can orchestrate it.**

- **10+ production pipelines** — explainers, talking heads, screen demos, cinematic trailers, animations, podcasts, localization, documentary montages, character animation, and more
- **100+ production tools** — spanning video generation, image creation, text-to-speech, music, audio mixing, subtitles, enhancement, and analysis
- **60+ provider integrations** — cloud APIs, local models, stock libraries, open archives, and production runtimes behind one scored selection layer
- **700+ agent skill and production-knowledge files** — pipeline directors, creative techniques, quality checklists, and deep technology knowledge packs that teach the agent how to use every tool like an expert
- **Reference-driven creation** — paste a video you like and the agent turns it into a grounded, differentiated production plan instead of forcing you to invent the perfect prompt from scratch
- **Real-footage documentary creation without paid video models** — build actual edited videos from free/open motion footage and archival sources, not just Ken Burns over images
- **Live web research built in** — before writing a single word of script, the agent runs 15-25+ web searches across YouTube, Reddit, news sites, and academic sources to ground your video in real, current data
- **Both free/local AND cloud providers** — every capability supports open-source local alternatives alongside premium APIs. Use what you have.
- **No vendor lock-in** — swap providers freely. The scored selector ranks every provider across 7 dimensions (task fit, output quality, control, reliability, cost efficiency, latency, continuity) and picks the best match automatically.
- **Production-grade quality gates** — delivery promise enforcement blocks slideshow-looking renders, pre-compose validation catches broken plans before wasting GPU time, and mandatory post-render self-review (ffprobe + frame extraction + audio analysis) ensures the agent never presents garbage. Every provider choice, style decision, and fallback gets logged in an auditable decision trail.
- **Budget governance built in** — cost estimation before execution, spend caps, per-action approval thresholds. No surprise bills.

---

## How It Works

OpenMontage uses an **agent-first architecture**. There is no code orchestrator. Your AI coding assistant IS the orchestrator.

```
You: "Make an explainer video about how black holes form"
 |
 v
Agent reads pipeline manifest (YAML) -- stages, tools, review criteria, success gates
 |
 v
Agent reads stage director skill (Markdown) -- HOW to execute each stage
 |
 v
Agent calls Python tools -- scored provider selection ranks every tool across 7 dimensions
 |
 v
Agent self-reviews using reviewer skill -- schema validation, playbook compliance, quality checks
 |
 v
Agent checkpoints state (JSON) -- resumable, with decision log and cost snapshot
 |
 v
Agent presents for your approval -- you stay in control at every creative decision
 |
 v
Pre-compose validation gate -- delivery promise, slideshow risk, renderer governance
 |
 v
Render (Remotion or FFmpeg) -- composition engine matched to visual grammar
 |
 v
Post-render self-review -- ffprobe, frame extraction, audio analysis, promise verification
 |
 v
Final video output -- only if self-review passes
```

**Python provides tools and persistence.** All creative decisions, orchestration logic, review criteria, and quality standards live in readable instruction files (YAML manifests + Markdown skills) that you can inspect and customize. Every decision is logged with alternatives considered, confidence scores, and the reasoning behind each choice.

---

## Architecture

```
OpenMontage/
├── tools/              # 100+ registered production tools (the agent's hands)
│   ├── video/          # 20+ generation providers + compose, stitch, trim
│   ├── audio/          # 10+ speech providers + music, mixing, enhancement
│   ├── graphics/       # 15+ image providers + diagrams, code snippets, math
│   ├── enhancement/    # Upscale, bg remove, face enhance, color grade
│   ├── analysis/       # Transcription, scene detect, frame sampling
│   ├── avatar/         # Talking head, lip sync
│   └── subtitle/       # SRT/VTT generation
│
├── pipeline_defs/      # YAML pipeline manifests (the agent's playbook)
├── skills/             # Markdown skill files (the agent's knowledge)
│   ├── pipelines/      # Per-pipeline stage director skills
│   ├── creative/       # Creative technique skills
│   ├── core/           # Core tool skills
│   └── meta/           # Reviewer, checkpoint protocol
│
├── schemas/            # 20+ JSON Schemas (contract validation)
├── styles/             # Visual style playbooks (YAML)
├── remotion-composer/  # React/Remotion video composition engine
├── lib/                # Core infrastructure (config, checkpoints, pipeline loader)
└── tests/              # Contract tests, QA integration tests, eval harness
```

### Three-Layer Knowledge Architecture

```
Layer 1: tools/ + pipeline_defs/     "What exists" — executable capabilities + orchestration
Layer 2: skills/                     "How to use it" — OpenMontage conventions and quality bars
Layer 3: .agents/skills/             "How it works" — external technology knowledge packs
```

Each tool declares which Layer 3 skills it relies on. The agent reads Layer 1 to know what's available, Layer 2 to know how OpenMontage wants it used, and Layer 3 for deep technical knowledge when needed.

---

## Supported Providers

> **Full setup guide with pricing and free tiers:** [`docs/PROVIDERS.md`](docs/PROVIDERS.md)

<details>
<summary><strong>Video Generation — 20+ providers</strong></summary>

| Provider | Type | Notes |
|----------|------|-------|
| **Kling (fal.ai)** | Cloud API | High quality, fast via fal.ai gateway |
| **Kling Official** | Cloud API | Official direct API with separate `kling_official` provider |
| **Atlas Cloud** | Cloud API | Unified gateway for Seedance, MiniMax, Hunyuan, and other multimodal models |
| **Seedance 2.0 (Volcengine Ark)** | Cloud API | Official direct API with separate `seedance_ark` provider |
| **Seedance 2.5 / 2.0** | Cloud API | Text, image, and reference-driven video workflows through supported gateways |
| **Gemini Omni Flash** | Cloud API | Conversational multimodal video generation and editing |
| **Runway Gen-4** | Cloud API | Cinematic quality, Gen-3 Alpha Turbo / Gen-4 Turbo / Gen-4 Aleph |
| **Google Veo 3.1** | Cloud API | Premium cinematic video via Google GenAI or fal.ai |
| **Grok Imagine Video** | Cloud API | Strong reference-image video and xAI-native short-form generation |
| **Higgsfield** | Cloud API | Multi-model orchestrator with Soul ID for character consistency |
| **MiniMax / H3** | Cloud API | Cost-effective generation, including text, image, and reference-driven H3 workflows |
| **HeyGen** | Cloud API | Multi-model gateway |
| **WAN 2.1 / 2.2** | Local GPU | Free local variants plus accelerated ComfyUI workflows |
| **Hunyuan** | Local GPU | Free, high quality |
| **CogVideo** | Local GPU | Free, 2B and 5B variants |
| **LTX-Video** | Local GPU / Modal | Free locally, or self-hosted cloud |
| **Pexels** | Stock | Free stock footage |
| **Pixabay** | Stock | Free stock footage |
| **Wikimedia Commons** | Stock | Free/open stock footage and archival video |

</details>

<details>
<summary><strong>Image Generation — 15+ providers</strong></summary>

| Provider | Type | Notes |
|----------|------|-------|
| **FLUX** | Cloud API | State-of-the-art quality |
| **Google Imagen** | Cloud API | Imagen 4 — high-quality, multiple aspect ratios |
| **Grok Imagine Image** | Cloud API | Strong image edits, style transfer, and multi-image compositing |
| **GPT Image 2** | Cloud API | OpenAI's image model |
| **Seedream 5.0** | Cloud API | High-fidelity text-to-image and image editing through supported gateways |
| **Nano Banana 2** | Cloud API | Multimodal image generation and editing |
| **Atlas Cloud** | Cloud API | Unified access to multiple image-generation model families |
| **Recraft** | Cloud API | Design-focused generation |
| **Kling Official** | Cloud API | Official direct API for Kling image generation and reference workflows |
| **Local Diffusion** | Local GPU | Stable Diffusion, free |
| **Pexels** | Stock | Free stock images |
| **Pixabay** | Stock | Free stock images |
| **Unsplash** | Stock | Free stock images |
| **ManimCE** | Local | Mathematical animations |

</details>

<details>
<summary><strong>Text-to-Speech — 10+ providers</strong></summary>

| Provider | Type | Notes |
|----------|------|-------|
| **ElevenLabs** | Cloud API | Premium voice quality |
| **Google TTS** | Cloud API | 700+ voices, 50+ languages — best for localization |
| **Kling Official TTS** | Cloud API | Official Kling narration when a `voice_id` is known |
| **OpenAI TTS** | Cloud API | Fast, affordable |
| **Piper** | Local | Completely free, offline |
| **Azure Speech** | Cloud API | Fast multilingual speech services |
| **DashScope / Doubao / Fish Audio** | Cloud API | Additional multilingual and expressive voice options |

</details>

<details>
<summary><strong>Music, Sound & Post-Production</strong></summary>

**Music & Sound:**

| Provider | Type | Notes |
|----------|------|-------|
| **Suno AI** | Cloud API | Full song generation with vocals, lyrics, any genre. Up to 8 minutes. |
| **ElevenLabs Music** | Cloud API | AI music generation |
| **ElevenLabs SFX** | Cloud API | Sound effect generation |

**Post-Production (always available, always free):**

| Tool | What It Does |
|------|-------------|
| **FFmpeg** | Video composition, encoding, subtitle burn-in, audio muxing |
| **Video Stitch** | Multi-clip assembly, crossfades, picture-in-picture, spatial layouts |
| **Video Trimmer** | Precision cutting and extraction |
| **Audio Mixer** | Multi-track mixing, ducking, fades |
| **Audio Enhance** | Noise reduction, normalization |
| **Color Grade** | LUT-based color grading |
| **Subtitle Gen** | SRT/VTT generation from timestamps |

**Enhancement:**

| Tool | What It Does |
|------|-------------|
| **Upscale** | Real-ESRGAN image/video upscaling |
| **Background Remove** | rembg / U2Net background removal |
| **Face Enhance** | Face quality enhancement |
| **Face Restore** | CodeFormer / GFPGAN face restoration |

**Analysis:**

| Tool | What It Does |
|------|-------------|
| **Transcriber** | WhisperX speech-to-text with word-level timestamps |
| **Scene Detect** | Automatic scene boundary detection |
| **Frame Sampler** | Intelligent frame extraction |
| **Video Understand** | CLIP/BLIP-2 vision-language analysis |

**Avatar & Lip Sync:**

| Tool | What It Does |
|------|-------------|
| **Talking Head** | SadTalker / MuseTalk avatar animation |
| **Lip Sync** | Wav2Lip audio-driven lip synchronization |
| **Kling Avatar** | Official Kling cloud avatar presenter generation |
| **Kling Lip Sync** | Official Kling cloud lip-sync with explicit face selection |

**Composition & Rendering:**

| Engine | Type | What It Does |
|--------|------|-------------|
| **Remotion** | Local (Node.js) | React-based programmatic video — spring-animated image scenes, stat reveals, section titles, hero cards, TikTok-style word-by-word captions, scene transitions (fade/slide/wipe/flip), Google Fonts, audio with fade curves, and the TalkingHead avatar composition. **When no video generation providers are configured, the agent generates still images and Remotion turns them into fully animated video.** |
| **HyperFrames** | Local (Node.js ≥ 22) | HTML/CSS/GSAP programmatic video — kinetic typography, product promos, launch reels, custom motion graphics, registry blocks (data charts, grain overlays, shader transitions), website-to-video workflows, and rigged SVG character animation. Consumed via `npx hyperframes`; no monorepo checkout needed. |
| **FFmpeg** | Local | Core video assembly, encoding, subtitle burn, audio muxing, color grading |

Runtime is chosen at proposal (`render_runtime`) and locked through `edit_decisions`. Silent swaps between runtimes are a governance violation — see `skills/core/hyperframes.md`.

</details>

---

## Style System

Style playbooks define the visual language for your productions:

| Playbook | Best For |
|----------|----------|
| **Clean Professional** | Corporate, educational, SaaS |
| **Flat Motion Graphics** | Social media, TikTok, startups |
| **Minimalist Diagram** | Technical deep-dives, architecture |

Playbooks control typography, color palettes, motion styles, audio profiles, and quality rules. The agent reads the playbook and applies it consistently across all generated assets.

---

## Platform Output Profiles

Built-in render profiles for every major platform:

| Profile | Resolution | Aspect Ratio |
|---------|-----------|--------------|
| YouTube Landscape | 1920x1080 | 16:9 |
| YouTube 4K | 3840x2160 | 16:9 |
| YouTube Shorts | 1080x1920 | 9:16 |
| Instagram Reels | 1080x1920 | 9:16 |
| Instagram Feed | 1080x1080 | 1:1 |
| TikTok | 1080x1920 | 9:16 |
| LinkedIn | 1920x1080 | 16:9 |
| Cinematic | 2560x1080 | 21:9 |

---

## Production Governance

OpenMontage treats video production like real engineering — with quality gates, audit trails, and enforcement at every stage.

### Quality Gates

- **Human approval gates are enforced, not suggested** — proposal, script, scene plan, generated assets, and publish all pause for your sign-off. The checkpoint writer rejects a "completed" gated stage without recorded approval, and every superseded checkpoint is archived so the audit trail (including gate transitions) survives revisions. Review happens visually on the [Backlot board](#watch-it-happen--the-backlot-living-storyboard).
- **Pre-compose validation** — blocks render if the delivery promise is violated (e.g. "motion-led" video with 80% still images), slideshow risk score is critical, or renderer family is missing. Catches broken plans before wasting GPU time.
- **Post-render self-review** — after every render, the runtime runs ffprobe validation, extracts frames at 4 positions to check for black frames and broken overlays, analyzes audio levels for silence and clipping, verifies the delivery promise was honored, and checks subtitle presence. If the review fails, the video is not presented.
- **Slideshow risk scoring** — 6-dimension analysis (repetition, decorative visuals, weak motion, shot intent, typography overreliance, unsupported cinematic claims) prevents "animated PowerPoint" outputs.
- **Source media inspection** — when users supply their own footage, the system probes every file (resolution, codec, audio channels, duration) and builds planning implications before a single creative decision is made. No hallucinating content from filenames.

### Scored Provider Selection

Every tool selection (video generation, image generation, TTS, music) runs through a 7-dimension scoring engine: task fit (30%), output quality (20%), control features (15%), reliability (15%), cost efficiency (10%), latency (5%), continuity (5%). The winning provider and its score are logged in the decision trail with all alternatives considered.

Selectors normalize loose brief context before scoring. If the agent only knows something like "Pixar-style animated short with character consistency," the selector expands that into scorer-friendly intent and style signals instead of requiring a perfectly pre-shaped `task_context`.

Selector outputs also surface the chosen provider's `agent_skills`, so the agent can immediately read the right Layer 3 provider skill before writing prompts.

### Decision Audit Trail

Every major creative and technical choice — provider selection, style/playbook choice, music track, voice selection, renderer family, any fallback or downgrade — is logged with alternatives considered, confidence scores, and reasoning. The cumulative decision log persists across all stages so you can trace exactly why the output looks the way it does.

### Budget Controls

- **Estimate** before execution — see what it will cost
- **Reserve** budget — lock funds before the call
- **Reconcile** after — record actual spend
- **Configurable modes** — `observe` (track only), `warn` (log overruns), `cap` (hard limit)
- **Per-action approval** — pause for confirmation above a threshold (default: $0.50)
- **Total budget cap** — default $10, fully configurable

No surprise bills. The agent tells you what it will cost before it spends.

---

## Agent Compatibility

OpenMontage works with any AI coding assistant that can read files and execute Python. Dedicated instruction files are included for:

| Platform | Config File |
|----------|------------|
| **Claude Code** | `CLAUDE.md` |
| **Cursor** | `CURSOR.md` + `.cursor/rules/` |
| **GitHub Copilot** | `COPILOT.md` + `.github/copilot-instructions.md` |
| **Codex** | `CODEX.md` |
| **Windsurf** | `.windsurfrules` |

All platform files point to the shared `AGENT_GUIDE.md` (operating guide and agent contract) and `PROJECT_CONTEXT.md` (architecture reference).

> **Coming soon:** Local LLM support via **Ollama** and **LM Studio** — run the full production pipeline without any cloud LLM.

---

## Contributing

OpenMontage is built to be extended. The two most common contributions:

### Adding a New Tool

1. Create a Python file in the appropriate `tools/` subdirectory
2. Inherit from `BaseTool` and implement the tool contract
3. The registry auto-discovers it — no manual registration needed
4. Add a skill file if the tool needs usage guidance

### Adding a New Pipeline

1. Create a YAML manifest in `pipeline_defs/`
2. Create stage director skills in `skills/pipelines/<your-pipeline>/`
3. Reference existing tools — or add new ones if needed

See `docs/ARCHITECTURE.md` for the full technical reference, `docs/PROVIDERS.md` for the complete provider guide (setup, pricing, free tiers), and `AGENT_GUIDE.md` for the agent contract.

### Join the Community

We use [GitHub Discussions](https://github.com/calesthio/OpenMontage/discussions) to share work and ideas:

- **[Show and Tell](https://github.com/calesthio/OpenMontage/discussions/categories/show-and-tell)** — Share videos you've made, prompts that worked well, or creative workflows you've discovered
- **[Ideas](https://github.com/calesthio/OpenMontage/discussions/categories/ideas)** — Suggest new pipelines, tools, style playbooks, or integrations
- **[Q&A](https://github.com/calesthio/OpenMontage/discussions/categories/q-a)** — Ask questions about setup, pipelines, or troubleshooting

Made something cool? Post it in Show and Tell — we'd love to see what you build.

---

## Contact

For updates, releases, and behind-the-scenes build notes, follow [@calesthioailabs](https://x.com/calesthioailabs).

For bugs, feature requests, and workflow discussions, use [GitHub Issues](https://github.com/calesthio/OpenMontage/issues) and [GitHub Discussions](https://github.com/calesthio/OpenMontage/discussions) so everything stays visible and actionable.

---

## Testing

```bash
# Run contract tests (no API keys needed)
make test-contracts

# Run all tests
make test
```

---

## Star History

<a href="https://star-history.dera.page/#calesthio/OpenMontage&type=date&legend=top-left">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://star-history.dera.page/svg?repos=calesthio/OpenMontage&type=date&theme=dark&legend=top-left" />
    <source media="(prefers-color-scheme: light)" srcset="https://star-history.dera.page/svg?repos=calesthio/OpenMontage&type=date&legend=top-left" />
    <img alt="Star History Chart" src="https://star-history.dera.page/svg?repos=calesthio/OpenMontage&type=date&legend=top-left" />
  </picture>
</a>

---

## License

[GNU AGPLv3](LICENSE)

---

**OpenMontage** — Production-grade video with real quality enforcement, orchestrated by your AI assistant.

If this project looks useful to you, a ⭐ would really mean a lot — it helps others discover it too.

If you'd like to go further, [sponsor the project](https://github.com/sponsors/calesthio) — OpenMontage is built nights and weekends, and your support makes that sustainable.

## Docs
### docs/ listing
```
file	ARCHITECTURE.md
file	PROVIDERS.md
file	PR_REVIEW_GUIDE.md
file	SPONSORS.md
file	apple-silicon-mps.md
file	bgm-montage-lite.md
file	comfyui-adapter-plan.md
dir	images
file	provider-update-plan-2026-10-03.md
dir	stage-gates
```

### docs/ARCHITECTURE.md
```
# OpenMontage Architecture

> Last updated: 2026-03-28 | Derived from code exploration, not prior documentation.

OpenMontage is an **agent-orchestrated video production platform**. An LLM coding assistant (Claude Code, Cursor, Copilot, etc.) acts as the orchestrator — reading pipeline manifests, following skill instructions, calling Python tools, and checkpointing state. There is no runtime Python orchestrator; the agent _is_ the control plane.

---

## High-Level Flow

```
User gives topic/idea
        |
        v
Agent reads pipeline manifest (YAML)
        |
        v
For each stage:
   1. Agent reads stage-director skill (Markdown)
   2. Agent calls Python tools via tool registry
   3. Agent writes checkpoint (JSON) with artifacts
   4. Agent self-reviews using meta/reviewer skill
   5. Human approval gate (if configured)
        |
        v
Final video output
```

---

## Repository Layout

```
OpenMontage/
├── lib/                    # Core runtime infrastructure (Python)
│   ├── config_model.py     # Pydantic config: LLM, budget, checkpoint, output, paths
│   ├── checkpoint.py       # Pipeline state persistence & stage transitions
│   ├── pipeline_loader.py  # YAML manifest loading & validation
│   ├── media_profiles.py   # Platform-specific render profiles (YouTube, TikTok, etc.)
│   ├── env_loader.py       # .env variable management
│   └── providers/          # (Reserved for future provider abstractions)
│
├── tools/                  # 57+ Python tool implementations
│   ├── base_tool.py        # Abstract base class — the tool contract
│   ├── tool_registry.py    # Auto-discovery singleton registry
│   ├── cost_tracker.py     # Budget governance (estimate → reserve → reconcile)
│   ├── analysis/           # Transcription, scene detection, frame sampling, video understanding
│   ├── audio/              # TTS (ElevenLabs, OpenAI, Piper, Azure, Google), music gen, mixing, enhancement
│   ├── avatar/             # Talking head animation, lip sync
│   ├── enhancement/        # Upscale, bg removal, face enhance/restore, color grading
│   ├── graphics/           # Image gen (FLUX, GPT Image, Recraft, local diffusion), stock, diagrams, code snippets, math animation
│   ├── publishers/         # (Reserved)
│   ├── subtitle/           # SRT/VTT generation from timestamps
│   └── video/              # 13 video gen providers, composition, stitching, trimming
│
├── pipeline_defs/          # YAML pipeline manifests
├── schemas/                # JSON Schema definitions for validation
│   ├── artifacts/          # 11 artifact schemas (brief → publish_log)
│   ├── checkpoints/        # Checkpoint state schema
│   ├── pipelines/          # Pipeline manifest schema
│   ├── styles/             # Style playbook schema
│   └── tools/              # Tool-specific schemas
│
├── skills/                 # Layer 2: OpenMontage-specific agent instructions
│   ├── core/               # FFmpeg, Remotion, WhisperX, color grading skills
│   ├── creative/           # Video editing, enhancement, data viz, prompt engineering
│   ├── meta/               # reviewer, checkpoint-protocol, skill-creator
│   └── pipelines/          # Per-pipeline stage-director skills
│
├── .agents/skills/         # Layer 3: external technology skills (FFmpeg, HyperFrames, GSAP, etc.)
├── styles/                 # Visual style playbooks (YAML) + loader
├── remotion-composer/      # Node.js/React — Remotion video composition renderer
├── tests/                  # Contract tests, QA integration tests, eval harness
├── docs/                   # Best-practices guides, session handoffs, audits
└── config.yaml             # Global runtime configuration
```

---

## Core Architectural Principles

### 1. Agent-First Orchestration

There is **no Python orchestrator**. The LLM agent:
- Reads the pipeline manifest to know the stage order
- Reads each stage-director skill for detailed instructions
- Calls tools, evaluates results, makes creative decisions
- Writes checkpoints to persist state between stages

Python provides **tools and persistence only**. All intelligence lives in skill instructions (Markdown) and pipeline manifests (YAML).

### 2. No LLM API Key in Runtime

OpenMontage does not call LLM APIs at runtime. The coding assistant running in the user's IDE _is_ the LLM. Tools that need generation (images, video, TTS) call domain-specific APIs directly (ElevenLabs, fal.ai, HeyGen, etc.), not general-purpose LLM endpoints.

### 3. Dual-Provider Support

Every capability must support both **API providers** (cloud, paid) and **local/open-source alternatives** (free, GPU-dependent). The selector pattern enforces this by routing to whatever is available.

---

## The Tool System

### BaseTool Contract

All tools inherit from `BaseTool` (ABC) and declare:

| Field | Purpose |
|-------|---------|
| `name`, `version` | Identity |
| `tier` | CORE, VOICE, ENHANCE, GENERATE, SOURCE, ANALYZE, PUBLISH |
| `capability` | What it does (e.g., `tts`, `image_generation`, `video_post`) |
| `provider` | Which service (e.g., `elevenlabs`, `ffmpeg`, `selector`) |
| `runtime` | LOCAL, LOCAL_GPU, API, HYBRID |
| `stability` | EXPERIMENTAL, BETA, PRODUCTION |
| `dependencies` | Required binaries (`cmd:ffmpeg`), env vars (`env:ELEVENLABS_API_KEY`), Python packages (`python:torch`) |
| `input_schema`, `output_schema` | JSON Schema for inputs/outputs |
| `fallback_tools` | Ordered fallback chain |
| `agent_skills` | Links to Layer 3 knowledge skills |
| `resource_profile` | CPU, RAM, VRAM, disk, network requirements |
| `retry_policy` | Max retries, backoff strategy |

**Required method:** `execute(inputs) -> ToolResult`

`ToolResult` carries: `success`, `data`, `artifacts` (file paths), `error`, `cost_usd`, `duration_seconds`, `seed`, `model`.

### Tool Registry

`ToolRegistry` is a singleton that auto-discovers all `BaseTool` subclasses via `pkgutil.walk_packages()`. No manual registration.

Key queries:
- `get_by_capability("tts")` — all TTS tools
- `get_by_provider("elevenlabs")` — all ElevenLabs tools
- `get_available()` — tools whose dependencies are satisfied
- `find_fallback("elevenlabs_tts")` — resolve fallback chain
- `support_envelope()` — full capability report for agent consumption
- `gpu_required_tools()`, `network_required_tools()`

### Selector Pattern

Three selector tools abstract multi-provider capabilities:

| Selector | Capability | How selection works |
|----------|-----------|---------------------|
| `tts_selector` | Text-to-speech | Ranks discovered providers by task fit, quality, control, reliability, cost, latency, and continuity |
| `image_selector` | Image generation | Ranks discovered providers from the live registry; no hardcoded provider order |
| `video_selector` | Video generation | Ranks discovered providers from the live registry; user preference is respected when explicitly provided |
| `atlas_image` / `atlas_video` | Atlas Cloud generation | Exposes exact per-model route catalogs for image generation/editing and text/image/reference/video-edit generation |

Selectors route based on: user preference when explicitly set, then scored ranking across available providers. They adapt input schemas between providers transparently.

### Tool Inventory by Category

**Analysis (5):** transcriber (WhisperX), azure_stt, scene_detect, frame_sampler, video_understand (CLIP/BLIP-2)

**Audio (9):** elevenlabs_tts, google_tts, openai_tts, piper_tts, azure_tts, tts_selector, music_gen, audio_mixer, audio_enhance

**Avatar (2):** talking_head (SadTalker/MuseTalk), lip_sync (Wav2Lip)

**Enhancement (5):** upscale (Real-ESRGAN), bg_remove (rembg/U2Net), face_enhance, face_restore (CodeFormer/GFPGAN), color_grade (FFmpeg LUTs)

**Graphics (13):** flux_image, grok_image, google_imagen, openai_image, recraft_image, local_diffusion, pexels_image, pixabay_image, image_selector, code_snippet, diagram_gen, math_animate (ManimCE), image_gen (deprecated)

**Subtitle (1):** subtitle_gen

**Video (18):** grok_video, heygen_video, higgsfield_video, veo_video, kling_video, runway_video, minimax_video, wan_video, hunyuan_video, cogvideo_video, ltx_video_local, ltx_video_modal, pexels_video, pixabay_video, video_selector, video_compose (FFmpeg), video_stitch, video_trimmer

---

## Pipeline System

### Pipeline Manifests

Each pipeline is a YAML file in `pipeline_defs/` defining:

```yaml
name: animated-explainer
version: "2.0"
category: generated          # talking_head | generated | hybrid | screen_recording | animation | cinematic | custom
default_checkpoint_policy: guided

orchestration:
  mode: executive-producer
  skill: pipelines/explainer/executive-producer
  budget_default_usd: 2.00
  max_revisions_per_stage: 3

compatible_playbooks:
  - clean-professional
  - flat-motion-graphics

stages:
  - name: research
    skill: pipelines/explainer/research-director
    produces: [research_brief]
    tools_available: []
    checkpoint_required: false
    human_approval_default: false
    review_focus: [...]
    success_criteria: [...]
  # ... through publish
```

### Available Pipelines

| Pipeline | Category | Description |
|----------|----------|-------------|
| `animated-explainer` | generated | AI-produced explainer with research, narration, visuals, music |
| `animation` | animation | Motion graphics, kinetic typography |
| `avatar-spokesperson` | talking_head | Avatar-driven presenter videos |
| `character-animation` | animation | Local rigged cartoon characters with SVG rigs, pose libraries, GSAP timelines, and HyperFrames rendering |
| `cinematic` | cinematic | Trailer, teaser, mood-driven edits |
| `clip-factory` | custom | Batch short-form clips from long source |
| `hybrid` | hybrid | Source footage + AI-generated support visuals |
| `localization-dub` | custom | Subtitle, dub, and translate existing video |
| `podcast-repurpose` | hybrid | Podcast highlights to video |
| `screen-demo` | screen_recording | Software screen recordings and walkthroughs |
| `talking-head` | talking_head | Footage-led speaker videos |
| `framework-smoke` | custom | Minimal smoke test for framework validation |

### Standard Stage Progression

Most production pipelines follow a canonical 8-stage flow:

```
research → proposal → script → scene_plan → assets → edit → compose → publish
```

Each stage:
1. Has a **stage-director skill** (Markdown instructions for the agent)
2. Declares **tools_available** (what the agent can call)
3. **Produces** one or more canonical artifacts
4. Has **review_focus** criteria and **success_criteria**
5. Can require **human approval** before proceeding

Specialized pipelines may insert domain-specific stages. For example,
`character-animation` adds `character_design` and `rig_plan` before
`scene_plan`, then emits a HyperFrames workspace and final deliverable at
`projects/<project-name>/renders/final.mp4`.

---

## Checkpoint System

Checkpoints persist pipeline state as JSON in the project's `pipeline/` directory.

```json
{
  "version": "1.0",
  "project_id": "my-video",
  "stage": "script",
  "status": "completed",
  "timestamp": "2026-03-28T10:00:00Z",
  "checkpoint_policy": "guided",
  "human_approval_required": false,
  "human_approved": true,
  "artifacts": { "script": { ... } },
  "review": { ... },
  "cost_snapshot": { ... }
}
```

**Status values:** `pending` | `in_progress` | `awaiting_human` | `completed` | `failed`

**Checkpoint policies:**
- `guided` — checkpoint at key creative stages, auto-proceed on mechanical ones
- `manual_all` — human approval at every stage
- `auto_noncreative` — auto-proceed unless stage is creative (assets, edit)

**Functions:** `write_checkpoint()`, `read_checkpoint()`, `get_latest_checkpoint()`, `get_completed_stages()`, `get_next_stage()`

### Canonical Artifacts (11 types, all JSON-schema validated)

| Artifact | Stage | Contains |
|----------|-------|----------|
| `research_brief` | research | Landscape analysis, data points, audience insights, angles |
| `proposal_packet` | proposal | Concept options, production plan, cost estimates, approval gate |
| `brief` | idea | Title, hook, key points, tone, style, platform, duration |
| `script` | script | Timestamped sections with enhancement cues, pronunciation guides |
| `scene_plan` | scene_plan | Scene definitions with type, description, timing |
| `asset_manifest` | assets | Generated assets with path, source tool, scene association |
| `edit_decisions` | edit | Editorial cuts with in/out timings |
| `render_report` | compose | Output metadata (format, resolution, duration) |
| `publish_log` | publish | Platform publication entries with status |
| `review` | (any) | Reviewer feedback and approval records |
| `cost_log` | (any) | Budget tracking entries |

---

## Budget Governance

The `CostTracker` enforces spending controls across the pipeline.

### Lifecycle

```
estimate(tool, operation, $) → entry_id
        |
reserve(entry_id)          # locks budget
        |
reconcile(entry_id, $)     # records actual spend
```

### Budget Modes

| Mode | Behavior |
|------|----------|
| `observe` | Track costs, no enforcement |
| `warn` | Log warnings on overruns, allow execution |
| `cap` | Reject operations that exceed remaining budget |

### Controls
- **Total budget** (default: $10.00)
- **Reserve holdback** (default: 10%) — kept as safety margin
- **Single-action approval threshold** (default: $0.50) — pause for approval above this
- **New paid tool approval** — first-time use of any paid tool requires confirmation
- Persists to `cost_log.json` per project

---

## 3-Layer Knowledge Architecture

```
Layer 3: .agents/skills/          External technology knowledge (47 skills)
         "How the technology works"    FFmpeg, ElevenLabs API, FLUX, Remotion, Three.js, etc.
              ^
              | agent_skills[] references
              |
Layer 2: skills/                  OpenMontage conventions
         "How this project uses the tech"  Pipeline integration, quality checklists, artifact mappings
              ^
              | stage skill references
              |
Layer 1: tools/ + pipeline_defs/  Executable capabilities + orchestration definitions
         "What exists and when to use it"  BaseTool contracts, pipeline manifests
```

Each tool's `agent_skills[]` field links Layer 1 to Layers 2 and 3. For example:
- `video_compose.agent_skills = ["remotion-best-practices", "remotion", "ffmpeg"]`
- `tts_selector.agent_skills = ["text-to-speech", "elevenlabs", "openai-docs"]`

---

## Configuration

### config.yaml

```yaml
llm:
  provider: anthropic
  temperature: 0.7
  max_tokens: 4096

budget:
  mode: warn
  total_usd: 10.00
  reserve_pct: 0.10
  single_action_approval_usd: 0.50

checkpoint:
  policy: guided
  storage_dir: pipeline

output:
  default_format: mp4
  default_codec: libx264
  default_audio_codec: aac
  default_resolution: 1920x1080
  default_fps: 30
  default_crf: 23

paths:
  pipeline_dir: pipeline
  library_dir: library
  styles_dir: styles
  skills_dir: skills
  output_dir: output
```

All config is validated via Pydantic models in `lib/config_model.py`.

### Environment Variables (.env)

| Variable | Used By | Purpose |
|----------|---------|---------|
| `ELEVENLABS_API_KEY` | elevenlabs_tts, music_gen | TTS, music, sound effects |
| `AZURE_SPEECH_KEY` + `AZURE_SPEECH_REGION` | azure_stt, azure_tts | Azure AI Speech cloud transcription + neural TTS (one resource, both directions) |
| `OPENAI_API_KEY` | openai_tts, openai_image | TTS fallback, GPT Image 2 |
| `XAI_API_KEY` | grok_image, grok_video | Grok image editing/generation, Grok video generation |
| `FAL_KEY` | flux_image, kling_video, veo_video, minimax_video, recraft_image | fal.ai hosted models (FLUX, Veo, Kling, MiniMax, Recraft) |
| `KLING_API_KEY` | kling_official_video, kling_official_image, kling_tts, kling_avatar, kling_lip_sync | Official Kling direct API for video, image, TTS, avatar, and lip sync |
| `KLING_API_BASE_URL` | kling_official_video, kling_official_image, kling_tts, kling_avatar, kling_lip_sync | Optional official Kling API endpoint override |
| `HEYGEN_API_KEY` | heygen_video | Multi-provider video generation |
| `PEXELS_API_KEY` | pexels_image, pexels_video | Stock media |
| `PIXABAY_API_KEY` | pixabay_image, pixabay_video | Stock media |
| `GOOGLE_API_KEY` | google_imagen, google_tts | Google Imagen images, Google Cloud TTS |
| `RUNWAY_API_KEY` | runway_video | Runway Gen-3/Gen-4 direct |
| `HIGGSFIELD_API_KEY` + `HIGGSFIELD_API_SECRET` | higgsfield_video | Higgsfield multi-model video |
| `MODAL_LTX2_ENDPOINT_URL` | ltx_video_modal | Self-hosted LTX-2 |
| `VIDEO_GEN_LOCAL_ENABLED` | local video tools | Enable local GPU generation |
| `VIDEO_GEN_LOCAL_MODEL` | wan, hunyuan, ltx, cogvideo | Select local model |

Kling Official support stays inside the existing provider and capability model.
`kling_official_video` and `kling_official_image` handle Classic, Turbo, and Omni
request shapes, while Elements and Account Usage live under `tools/_kling/` as
internal helpers for element ID references and low-frequency account diagnostics;
they are not separate pipeline stages, selectors, or generated-asset capabilities.

Kling Official also adds provider tools only where OpenMontage already has a
matching capability slot: `kling_tts` for `tts`, plus `kling_avatar` and
`kling_lip_sync` for `avatar`. Official Kling audio effects and video effects are
not registered as tools because current pipelines do not define stable
`sound_effects` or `video_effects` capability routing.

---

## Visual Style System

Style playbooks in `styles/` define visual language for pipelines:

- `clean-professional.yaml` — Corporate, polished look
- `flat-motion-graphics.yaml` — Modern flat design
- `minimalist-diagram.yaml` — Technical, minimal diagrams

Loaded by `styles/playbook_loader.py`. Each pipeline declares `compatible_playbooks` in its manifest. Validated against `schemas/styles/playbook.schema.json`.

---

## Media Profiles

Platform-specific render configurations in `lib/media_profiles.py`:

| Profile | Resolution | Aspect | Notes |
|---------|-----------|--------|-------|
| `youtube_landscape` | 1920x1080 | 16:9 | Standard YouTube |
| `youtube_4k` | 3840x2160 | 16:9 | 4K YouTube |
| `youtube_shorts` | 1080x1920 | 9:16 | Max 60s |
| `instagram_reels` | 1080x1920 | 9:16 | Max 90s |
| `instagram_feed` | 1080x1080 | 1:1 | Square |
| `tiktok` | 1080x1920 | 9:16 | Vertical |
| `linkedin` | 1920x1080 | 16:9 | Landscape |
| `cinematic` | 2560x1080 | 21:9 | Ultrawide |

Each profile specifies codec, audio codec, CRF, pixel format, max file size, max duration, and caption format. `ffmpeg_output_args(profile)` generates the corresponding FFmpeg flags.

---

## Composition Runtimes

OpenMontage has a multi-runtime composition layer. Three engines live behind `video_compose`, chosen at proposal and locked in `edit_decisions.render_runtime`:

### Remotion (React-based)

A standalone Node.js/React subproject in `remotion-composer/` using [Remotion](https://www.remotion.dev/).

- **React 18** + **Remotion 4.0** + **TypeScript 5.3**
- Handles the existing scene-component stack (`text_card`, `stat_card`, charts, captions, `TalkingHead`, `CinematicRenderer`)
- Scripts: `start` (studio), `build` (render), `upgrade`

### HyperFrames (HTML/CSS/GSAP)

Consumed via `npx hyperframes` (no monorepo checkout needed). Runtime floor: Node.js ≥ 22, FFmpeg, `npx`.

- Handles kinetic typography, product promos, launch reels, website-to-video, registry blocks, and SVG/GSAP character rigs
- Driver: `tools/video/hyperframes_compose.py` materializes a workspace under `projects/<name>/hyperframes/`, then runs `lint → validate → render`
- Layer 3 skills vendored at `.agents/skills/hyperframes*/`; Layer 2 guide at `skills/core/hyperframes.md`
- The `character-animation` pipeline uses HyperFrames as the production render package. Browser previews are QA/debug artifacts only, not the render path.

### FFmpeg (fallback / simple cuts)

- Handles pure concat/trim when no composition is needed
- Also handles subtitle burn-in as a post-hoc operation

`video_compose` reads `edit_decisions.render_runtime` and dispatches via `_render_via_hyperframes`, `_remotion_render`, or `_render_via_ffmpeg`. Silent runtime swaps are forbidden — the tool returns a structured blocker when the chosen runtime is unavailable. See `AGENT_GUIDE.md` → "Composition Runtimes (Inside video_compose)" and `skills/core/hyperframes.md` for the full decision matrix.

---

## Test Architecture

```
tests/
├── contracts/              # Phase 0-3: tool contract validation, schema checks, registry tests
├── qa/                     # Integration tests: TTS, image gen, music, audio mix, video compose/stitch, E2E
├── eval/                   # Golden scenario replay harness for regression testing
├── pipelines/              # Pipeline-level tests
├── tools/                  # Individual tool tests
└── styles/                 # Style playbook tests
```

**Contract tests** verify every tool satisfies the `BaseTool` contract: identity fields, schemas, dependency declarations, inheritance.

**QA tests** call real tools (with real APIs/binaries) and inspect output quality.

**Eval harness** (`tests/eval/replay_harness/`) replays golden scenarios with tolerance-based comparison for stochastic outputs.

---

## System Dependencies

**Required:**
- Python >= 3.10
- FFmpeg (used by ~15 tools)

**Optional (extend capabilities):**
- Node.js (for Remotion composer)
- GPU + CUDA (for local video/image generation)
- Piper (offline TTS)
- ManimCE (math animations)
- Mermaid CLI (diagram generation)

**Python packages:** pyyaml, pydantic, jsonschema, python-dotenv (core); pytest, pytest-asyncio (dev); torch, torchvision, torchaudio (GPU)

---

## Key Design Decisions

1. **No runtime orchestrator** — The LLM agent reads YAML + Markdown and drives everything. This makes the system debuggable (just read the skill) and model-agnostic.

2. **Checkpoint-based resumption** — Any stage can fail and the pipeline resumes from the last checkpoint. No re-running completed stages.

3. **Schema-validated artifacts** — Every stage output is validated against a JSON Schema before the checkpoint is written. Prevents garbage propagation.

4. **Budget as a first-class concept** — Cost estimation before execution, budget reservation, and reconciliation. The agent cannot silently overspend.

5. **Selector pattern over hard-coded providers** — Capabilities degrade gracefully. Missing an API key? The selector falls through to the next provider or a local alternative.

6. **Skills over code for intelligence** — Creative decisions, quality checklists, review criteria, and prompt templates live in Markdown skills, not Python. This means the agent's behavior can be tuned by editing text files, not code.
```

### docs/PROVIDERS.md
```
# OpenMontage Provider Guide

Everything you need to know about every provider in OpenMontage — setup instructions, pricing, free tiers, and what each unlocks.

## October 2026 provider refresh

See [implementation status and verified model map](provider-update-plan-2026-10-03.md)
and [adapter usage](../.agents/skills/provider-model-refresh/SKILL.md).

New routes cover HeyGen Avatar V, Eleven v4/Turbo, Wan 3.0 on fal/Atlas/Replicate,
GPT Image 2.5 Flare/Sunburst, Gemini 3 Pro Image (Nano Banana Pro), Ideogram 4.5
and Precise Edit, H3 Max, Gemini 3.8 TTS, Lyria 3.5, LTX-2.5, Sonic 3.6,
Inworld TTS-2/Flash and local Qwen Image 2.1. Each model uses the exact API host's
contract; an API key does not establish account entitlement.

For image/video selectors use `model`, `hosting_provider`, and optionally
`preferred_tool`. Speech uses `model_id`. Explicit tool, host and model constraints
never silently fall back. Legacy `preferred_provider` remains a ranking preference.
Several tools may share a host; ranking selects the actual tool name.

New asynchronous video/image tools return `resume_job` and optionally save
`job_path`. Resume the same job after a polling timeout instead of submitting
another paid request. Unpriced calls return `cost_usd: null` with `cost_status`,
not zero. Ideogram direct supports an unbilled `dry_run` price quote.

Kling 4/Flash stays gated pending verified public schemas and account access.
LTX-2.5 local execution requires a supplied ComfyUI API workflow and installed
weights; the direct LTX API is implemented separately. GPU and paid API output
quality require live validation in the intended environment.

---

## Quick Start: What Should I Set Up?

**Start free, add paid providers as you need them.** Here's the recommended order:

| Step | Cost | What to set up | What it unlocks |
|------|------|----------------|-----------------|
| 1 | **$0** | Pexels + Pixabay | Stock photos and videos — enough to produce basic videos |
| 2 | **$0** | Google API key | TTS with 700+ voices (1M chars/month free) + $300 new account credit |
| 3 | **$0** | ElevenLabs | Premium TTS + music + SFX (10K chars/month free) |
| 4 | **$0** | Piper (local install) | Fully offline TTS — no API key, no cost, no network |
| 5 | **~$0.03/image** | fal.ai | FLUX images + Kling/Veo/MiniMax video + Recraft — broad single-key image + video coverage |
| 6 | **~$0.05/image** | OpenAI | GPT Image 2 images + OpenAI TTS |
| 7 | **~$0.04/image** | Google Imagen | Imagen 4 images (shares the Google API key) |
| 8 | **pay-as-you-go** | Kling Official | Official direct Kling video, image, TTS, avatar, and lip-sync API, separate from fal.ai Kling |
| 9 | **pay-as-you-go** | Volcengine Ark | Official direct Seedance 2.0 Standard/Fast/Mini API |
| 10 | **$12/month** | Runway | Gen-4 video — highest quality AI video |
| 11 | **pay-as-you-go** | Hunyuan cloud video | Chinese-friendly T2V + I2V |
| 12 | **pay-as-you-go** | HeyGen | Avatar videos, multi-model video gateway |
| 13 | **pay-as-you-go** | Suno | Full song generation with vocals and lyrics |
| 14 | **$0 + GPU** | Local video gen | WAN 2.1, Hunyuan, CogVideo, LTX — free, offline |
| 15 | **$0 + GPU** | Local Diffusion | Stable Diffusion images — free, offline |

### Environment Variable Summary

```bash
# .env — add your keys here

# FREE (no cost, ever)
PEXELS_API_KEY=              # Stock photos + videos
PIXABAY_API_KEY=             # Stock photos + videos

# GOOGLE (one key, multiple tools, generous TTS free tier)
GOOGLE_API_KEY=              # Google TTS + Imagen + Lyria music + Gemini Omni/Veo video

# VOICE + MUSIC
ELEVENLABS_API_KEY=          # TTS, music, sound effects (10K chars/month free)
FISH_AUDIO_API_KEY=          # fish.audio TTS (voice cloning via reference_id, inline emotion tags)
OPENAI_API_KEY=              # OpenAI TTS + GPT Image 2 images
XAI_API_KEY=                 # xAI Grok image generation/editing + Grok video generation
DOUBAO_SPEECH_API_KEY=       # Volcengine Doubao Speech TTS (strong Mandarin narration)
DOUBAO_SPEECH_VOICE_TYPE=    # Default Doubao speaker/voice type
DASHSCOPE_API_KEY=           # Alibaba DashScope (Qwen image gen, TTS, ASR with word timestamps)

# AZURE AI SPEECH (optional cloud STT + TTS; one key unlocks both directions)
AZURE_SPEECH_KEY=            # Azure AI Speech — azure_stt (Fast Transcription) + azure_tts (neural narration)
AZURE_SPEECH_REGION=         # Speech resource region, e.g. eastus

# MULTI-MODEL GATEWAY (one key, 6+ tools)
FAL_KEY=                     # FLUX, Recraft, Kling, Veo, MiniMax video
MINIMAX_API_KEY=             # MiniMax first-party image + MiniMax H3 video generation
ATLASCLOUD_API_KEY=          # Atlas Cloud image/video gateway

# KLING OFFICIAL DIRECT API
KLING_API_KEY=               # Official Kling video, image, TTS, avatar, lip sync
KLING_API_BASE_URL=          # Optional; default https://api-singapore.klingai.com

# VOLCENGINE ARK DIRECT SEEDANCE 2.0 / 2.5 API
ARK_API_KEY=                 # API key body only; do not include the "Bearer " prefix

# VIDEO
HEYGEN_API_KEY=              # HeyGen avatar video gateway
RUNWAY_API_KEY=              # Runway native + Seedance 2.5, Gemini Omni, MiniMax H3
SUNO_API_KEY=                # Suno music generation

# TENCLOUD HUNYUAN VIDEO
TENCENT_TOKENHUB_API_KEY=    # Tencent Hunyuan cloud video via TokenHub API

# LOCAL (no keys needed — just GPU + install)
VIDEO_GEN_LOCAL_ENABLED=     # Set to "true" for local video gen
VIDEO_GEN_LOCAL_MODEL=       # wan2.2-ti2v-5b, wan2.1-1.3b, wan2.1-14b, hunyuan-1.5, ltx2-local, cogvideo-5b

# COMFYUI (optional overrides; localhost:8188 is the default)
COMFYUI_SERVER_URL=          # Local ComfyUI server for shared workflows
COMFYUI_VIDEO_SERVER_URL=    # Optional video-specific ComfyUI server
```

---

## Current Video Model Coverage

The following integrations are based on documented, currently exposed model
identifiers. Provider pages without a public API contract were not given
speculative model strings.

| Model | Direct provider | fal.ai | Runway | ComfyUI Partner Nodes | Local ComfyUI |
|-------|-----------------|--------|--------|-----------------------|---------------|
| **Gemini Omni Flash** | Google `gemini_omni_video` | `gemini_omni_fal` (T2V, I2V, references, editing) | `runway_video` model `gemini_omni_flash` | `GeminiVideoOmni` (hosted, paid credits) | Not available as local weights |
| **Seedance 2.5** | Volcengine `seedance_ark` model variant `2.5` | `seedance_video` model version `2.5` | `runway_video` model `seedance2_5` | `ByteDance2TextToVideoNode` (hosted, paid credits) | Not available as local weights |
| **MiniMax H3** | `minimax_video` model `MiniMax-H3` | `minimax_fal_video` (`hailuo-03`) | `runway_video` model `hailuo3` | `MinimaxHailuo03TextToVideoNode` (hosted, paid credits) | Supported with official open weights and an exported API workflow |

ComfyUI Partner Nodes run inside the ComfyUI graph but call hosted services;
they require network access, a logged-in Comfy account, and prepaid credits.
Only the MiniMax H3 open-weight workflow in this table is a local model path.

Replicate, HeyGen, and Higgsfield were not updated for these exact model
versions because their public API documentation did not expose a current,
stable contract for them at the time of this update.

---

## Cloud Providers

### xAI — Grok Image + Video

> **Best if you want one provider for image edits and reference-conditioned short video.** Grok covers both image generation/editing and video generation under one key.

**Tools unlocked:** `grok_image`, `grok_video`
**Env var:** `XAI_API_KEY`

#### Setup

1. Create an xAI developer account
2. Generate an API key in the xAI developer console
3. Add to `.env`: `XAI_API_KEY=xai-...`

#### What it's best for

- Image editing and style transfer
- Multi-image composites into one generated frame
- Short reference-image videos where a person, garment, or product must carry into motion

#### Pricing

Current xAI docs pricing for the Grok media models:

| Model | Price |
|------|-------|
| `grok-imagine-image` | $0.02 per generated image |
| `grok-imagine-image` input images (edits/composites) | $0.002 per input image |
| `grok-imagine-video` at 480p | $0.05/sec |
| `grok-imagine-video` at 720p | $0.07/sec |
| `grok-imagine-video` input images | $0.002 per input image |

OpenMontage now uses those published rates in the Grok tool estimators.

---

### Volcengine Jimeng — 即梦 AI Video Generation

> **Direct ByteDance API via V4 signing.** Calls the Volcengine visual API (visual.volcengineapi.com) with HMAC-SHA256 request signing using IAM AK/SK credentials. Supports text-to-video and image-to-video via Jimeng 3.0 Pro.

**Tools unlocked:** `jimeng_video`
**Env vars:** `VOLC_ACCESSKEY` (Access Key ID) + `VOLC_SECRETKEY` (Secret Access Key)

#### Setup

1. Go to [console.volcengine.com/iam/keymanage](https://console.volcengine.com/iam/keymanage)
2. Create a Volcengine account if you don't have one
3. Create an Access Key pair (AK + SK)
4. Ensure your account has access to Jimeng AI (即梦) video generation service
5. Add to `.env`: `VOLC_ACCESSKEY=...` and `VOLC_SECRETKEY=...`

#### What it's best for

- Direct ByteDance/Volcengine API quota usage
- Jimeng 3.0 Pro text-to-video and image-to-video
- Chinese-language prompt understanding
- Configurable frame count (121=5s, 241=10s) and aspect ratio

#### API notes

Authentication uses Volcengine IAM V4 signing (HMAC-SHA256), not a Bearer token. The signing process builds a canonical request, derives a signing key from SK → date → region → service, and signs the request.

API flow: `POST ?Action=CVSync2AsyncSubmitTask` → poll `POST ?Action=CVSync2AsyncGetResult` → download `video_url`.

The implementation uses the compatible generic `CVSync2Async*` route (API version `2022-08-31`) rather than the model-specific `2024-06-06` actions presented in the public API explorer. This is intentional — the generic route supports the same Jimeng 3.0 Pro model via `req_key` while remaining stable across model updates.

The `req_key` for video is `jimeng_ti2v_v30_pro`. Success code is `10000`. Task statuses: `in_queue`, `generating`, `done`, `not_found`, `expired`.

**Authoritative API reference:** [Jimeng TI2V V30 Pro SubmitTask](https://api.volcengine.com/api-docs/view?action=JimengTI2VV30PROSubmitTask&serviceCode=cv&version=2024-06-06)

**Schema constraints** (enforced by `input_schema` to prevent paid-call failures):
- `prompt`: max 800 characters
- `frames`: must be exactly `121` (5s) or `241` (10s) at 24fps
- `seed`: `-1` for random, or any non-negative integer

#### Pricing

| Model | Price |
|------|-------|
| Jimeng 3.0 Pro (video) | ~$0.05/sec (check Volcengine console for actual rate) |

---

### Volcengine Ark — Direct Seedance 2.0 and 2.5 Video Generation

> **Official direct Seedance API.** Calls Volcengine Ark without routing through fal.ai or Replicate, while keeping those existing provider paths available as independent fallbacks.

**Tool unlocked:** `seedance_ark`

**Env var:** `ARK_API_KEY`

#### Setup

1. Open the [Volcengine Ark API key console](https://console.volcengine.com/ark/region:cn-beijing/apiKey)
2. Enable the Seedance model family and confirm that the account has balance or a valid resource package
3. Create a long-lived API key
4. Add the key body to `.env`: `ARK_API_KEY=...`

Do not include the `Bearer ` prefix in the environment value. The tool adds the authorization scheme when it sends a request.

Optional overrides:

```bash
ARK_SEEDANCE_MODEL=doubao-seedance-2-0-260128
ARK_BASE_URL=https://ark.cn-beijing.volces.com/api/v3
ARK_CNY_PER_USD=7.2
```

#### Models and capabilities

| Variant | Default model ID | Output |
|---------|------------------|--------|
| 2.5 | `doubao-seedance-2-5-260628` | 480p or 720p; 4–30 seconds |
| Standard | `doubao-seedance-2-0-260128` | 480p, 720p, 1080p, or 4K |
| Fast | `doubao-seedance-2-0-fast-260128` | 480p or 720p |
| Mini | `doubao-seedance-2-0-mini-260615` | 480p or 720p |

The adapter supports:

- text-to-video, first-frame image-to-video, and multimodal reference-to-video
- local image and audio inputs encoded as validated Data URIs
- remote reference image, video, and audio URLs
- task create, query, cancel, and bounded polling
- synchronized audio, optional last-frame return, web search for text-only requests, and output download
- pre-submit dry-run and token-based cost estimates

Seedance 2.5 accepts up to 30 image, 10 video, and 10 audio references.
Select it with `model: "2.5"` (or its exact model ID). Because the public
documentation does not establish a stable default token price for this model,
OpenMontage requires `custom_price_cny_per_million_tokens` before presenting a
cost estimate; unknown pricing is never reported as free.

Local reference videos are intentionally rejected because the public API does not document video Data URI support. Use a provider-accessible HTTPS URL or an Ark asset reference instead.

#### API and billing notes

The asynchronous API flow is:

`POST /contents/generations/tasks` → `GET /contents/generations/tasks/{id}` → download the successful result URL.

Queued tasks can be cancelled with `DELETE /contents/generations/tasks/{id}`. Task records are retained for a limited period, and successful result URLs are short-lived, so the tool downloads outputs promptly.

Ark bills Seedance by completion tokens. Rates vary by model, resolution, and whether the request includes reference video. OpenMontage estimates cost before submission and reconciles against provider-returned usage when available. Check the Ark console for current rates before a paid run; custom endpoint IDs and Seedance 2.5 require an explicit custom price so unknown pricing is never treated as free.

Official references: [Seedance model list](https://www.volcengine.com/docs/82379/1366799), [create task](https://www.volcengine.com/docs/82379/1520757?lang=zh), [query task](https://www.volcengine.com/docs/82379/1521309?lang=zh).

---

### Alibaba DashScope — Qwen Image + TTS + ASR

> **Best for Chinese-language production.** One key unlocks Qwen-Image generation, Qwen-TTS Mandarin narration, and Qwen-ASR with word-level timestamps — the only DashScope path that provides word-level granularity for subtitle alignment.

**Tools unlocked:** `dashscope_image`, `dashscope_tts`, `dashscope_asr`
**Env var:** `DASHSCOPE_API_KEY`

#### Setup

1. Go to [dashscope.aliyun.com](https://dashscope.aliyun.com/)
2. Create an Alibaba Cloud account if you don't have one
3. Generate an API key in the DashScope console
4. Add to `.env`: `DASHSCOPE_API_KEY=sk-...`

#### What it's best for

- Chinese-language image generation with strong prompt understanding (Qwen-Image)
- Natural Mandarin narration (Qwen-TTS, Cherry voice)
- Word-level timestamp transcription for subtitle alignment (Qwen-ASR filetrans)
- Replacing the broken `whisperx` slot for ASR

#### API notes

DashScope's `/compatible-mode/v1/` only supports `/chat/completions` and `/embeddings`. Image gen, TTS, and ASR all use DashScope-native endpoints with nested `{model, input, parameters}` request shape — not OpenAI-compatible paths.

The ASR tool (`qwen3-asr-flash-filetrans`) uses an async submit-poll pattern. Audio must be at a publicly accessible URL (local files are not supported). Word timestamps are in milliseconds, normalized to seconds by the tool.

#### Pricing

| Model | Price |
|------|-------|
| `qwen-image-2.0-pro` | ~$0.02 per image (check console for current rates) |
| `qwen3-tts-flash` | ~$0.000015 per character |
| `qwen3-asr-flash-filetrans` | Per-minute billing (check console) |

---

### Tencent Hunyuan Cloud — Image Generation

> **Chinese-friendly first-party image generation.** `hunyuan_image` accesses
> Hunyuan Image 3.0 through Tencent TokenHub with Bearer-token authentication.
> It supports seeded text-to-image, up to three reference images, custom
> resolutions, prompt rewriting, and watermark controls.

**Tool unlocked:** `hunyuan_image`

**Env var:** `TENCENT_TOKENHUB_API_KEY`

Generate an API key in the Tencent Cloud TokenHub console and add it to
`.env`. The tool reports approximately $0.08 per generated image based on
TokenHub's credit price. It is available through `image_selector`; shared
reference-image inputs are normalized to the provider's `images` array.

---

### fal.ai — Multi-Model Gateway

> **Broad single-key coverage.** One API key unlocks image and video providers across multiple models.

**Tools unlocked:** `flux_image`, `recraft_image`, `seedream_image`,
`kling_video`, `veo_video`, `seedance_video`, `gemini_omni_fal`,
`minimax_fal_video`, `fal_elevenlabs_tts`, `fal_elevenlabs_music`
**Env var:** `FAL_KEY`

#### Setup

1. Go to [fal.ai](https://fal.ai/) and click **Sign up** (GitHub or Google)
2. Navigate to [fal.ai/dashboard/keys](https://fal.ai/dashboard/keys)
3. Click **Create Key**, copy it
4. Add to `.env`: `FAL_KEY=your-key-here`

#### Pricing

No subscription — pure pay-as-you-go, no minimum spend.

**Image generation:**

| Model | Price | Per $1 |
|-------|-------|--------|
| FLUX Pro v1.1 | $0.05/image | 20 images |
| FLUX Dev | $0.03/image | 33 images |
| Recraft v3 | ~$0.04/image | 25 images |
| Seedream 5 Pro (up to 1536x1536) | $0.0675/image | ~14 images |
| Seedream 5 Pro (up to 2048x2048) | $0.135/image | ~7 images |

**Video generation:**

| Model | Price | Per $1 |
|-------|-------|--------|
| Kling 2.5 Turbo Pro | $0.07/sec | 14 seconds |
| Seedance 2.5 | endpoint-dependent | 4–30 seconds |
| Gemini Omni Flash | endpoint-dependent | 3–10 seconds |
| MiniMax H3 (`hailuo-03`) | endpoint-dependent | 4–15 seconds |
| Veo 3 | $0.40/sec | 2.5 seconds |
| WAN 2.5 | $0.05/sec | 20 seconds |

**Free tier:** None — but $0 to start, you only pay for what you use.

The same key can also access ElevenLabs speech and music through fal.ai. Use
`fal_elevenlabs_tts` when direct ElevenLabs credentials are unavailable, or
select it through `tts_selector` with `preferred_provider: "fal.ai"`.

---

### MiniMax — Official Direct Image and Video API

> **First-party image and video generation.** The direct MiniMax API supports
> seeded image generation plus MiniMax H3 video generation with text, first/last
> frames, image/video/audio references, and global or mainland-China routing.

**Tools unlocked:** `minimax_image`, `minimax_video`

**Env var:** `MINIMAX_API_KEY`

**Optional region:** `MINIMAX_REGION=global` (default) or `cn`

#### Setup

1. Create a MiniMax Open Platform account.
2. Generate an API key in the account's API-key page.
3. Add `MINIMAX_API_KEY=...` to `.env`.
4. For a mainland-China account, also set `MINIMAX_REGION=cn`.

`MINIMAX_BASE_URL` may be used for a documented private/enterprise endpoint
override. The default global and mainland-China hosts are selected from
`MINIMAX_REGION`.

#### MiniMax H3 video

Use `minimax_video` with `model: "MiniMax-H3"`. The tool uses the v2 task
contract (`POST /v2/video_generation`, then
`GET /v2/query/video_generation/{task_id}`) and supports 4–15 second 2K clips.
Older Hailuo models continue to use the v1 API. MiniMax H3 reference generation
can combine images, video, and audio; reference audio requires a visual
reference.

#### Pricing

| Models | Global pay-as-you-go price |
|--------|----------------------------|
| `image-01`, `image-01-live` | $0.0035 per generated image |

MiniMax also offers subscription token plans with included daily image quota.
OpenMontage conservatively reports the standard pay-as-you-go amount in cost
estimates and generation results.

The tools are automatically discoverable through the image and video selectors;
choose them with `preferred_provider: "minimax"`.

---

### Atlas Cloud — Image and Video Gateway

**Tools:** `atlas_image`, `atlas_video`
**Env var:** `ATLASCLOUD_API_KEY` (aliases: `ATLAS_CLOUD_API_KEY`, `ATLAS_API_KEY`)
**Skill:** `.agents/skills/atlas-cloud/SKILL.md`

Atlas Cloud provides one endpoint and key for the following explicitly cataloged
routes. OpenMontage validates each model's real schema instead of treating task
suffixes or parameter names as interchangeable.

| Family | Supported routes | Current Atlas rate |
|---|---|---:|
| Seedance 2.5 | text/image/reference to video | $0.134/sec |
| Seedance 2.0 | text/image/reference to video | $0.112/sec |
| Gemini Omni Flash | text/image/reference to video; video edit; developer text/image/reference | $0.112–0.140/sec |
| MiniMax H3 | text/image/reference to video | $0.100/sec |
| Seedream 5.0 Pro | text to image; edit; layer decomposition | $0.022–0.045/image |
| GPT Image 2 | text to image; edit | $0.009–0.010/image |
| Nano Banana 2 | text to image; edit | $0.080/image |

Inspect `get_info()["model_catalog"]` for exact IDs, operations, media shapes,
durations, and resolutions. Prices are estimates sourced from each model's
machine-readable Atlas page and should be reconfirmed before a paid batch.

---

### Kling Official — Direct API

> **Official Kling path.** This is separate from `kling_video` via fal.ai: it uses Kling's official `Authorization: Bearer <KLING_API_KEY>` API, provider name `kling_official`, and direct Classic/Turbo/Omni task protocols.

**Tools unlocked:** `kling_official_video`, `kling_official_image`, `kling_tts`, `kling_avatar`, `kling_lip_sync`
**Env vars:** `KLING_API_KEY`, optional `KLING_API_BASE_URL`

#### Setup

1. Create or open a Kling AI Open Platform account.
2. Generate an official API key in the Kling API console.
3. Add to `.env`:
   ```bash
   KLING_API_KEY=your-key-here
   # Optional, defaults to Singapore:
   KLING_API_BASE_URL=https://api-singapore.klingai.com
   ```

#### What It Is Best For

- Direct official Kling API provenance rather than fal.ai gateway routing
- Text-to-video, image-to-video, and deep Video Omni reference workflows via `kling_official_video`
- Text-to-image, image edit/reference, and Image Omni multi-reference or series workflows via `kling_official_image`
- Text-to-speech via `kling_tts` when you already know the official Kling `voice_id`
- Cloud avatar presenter clips via `kling_avatar`, without replacing local `talking_head`
- Cloud lip-sync via `kling_lip_sync`, with explicit face selection for multi-person videos
- Accounts that need to use official Kling model permissions, resource packs, or regional endpoints

#### Notes

- `provider="kling_official"` is intentionally different from fal.ai's `provider="kling"`.
- Official Kling is a paid remote API. OpenMontage uses conservative cost estimates and includes high-cost factors such as Omni references, series output, 4k mode, and native sound.
- Local image paths are sent as raw base64 for supported Classic/image-generation fields. Turbo image-to-video requires a URL and will not silently upload through fal.ai.
- Video Omni and Image Omni can pass official `element_id` references through `element_list`; Elements remain an internal Kling Official helper, not a standalone OpenMontage capability.
- Account Usage is available as a low-frequency diagnostic helper under `tools/_kling/account.py`; it is not a selector or pipeline tool.
- `callback_url` is passed through and recorded when supplied, but OpenMontage still polls tasks by default.
- `kling_tts` requires an explicit `voice_id`; OpenMontage does not guess a default official voice.
- `kling_avatar` and `kling_lip_sync` register under the existing `avatar` capability and coexist with local SadTalker/Wav2Lip tools. Current avatar pipelines must opt into them explicitly; registry discovery alone does not replace local tools.
- Official Kling audio effects and video effects are documented but intentionally not registered as OpenMontage tools yet, because current pipelines do not have a stable sound-effects or video-effects capability slot for them.

---

### ElevenLabs — Voice, Music, Sound Effects

> **Premium voice quality.** Best TTS for narration-heavy videos. Also generates music and sound effects.

**Tools unlocked:** `elevenlabs_tts`, `music_gen`
**Env var:** `ELEVENLABS_API_KEY`

#### Setup

1. Go to [elevenlabs.io](https://elevenlabs.io) and click **Sign up**
2. Go to **Profile** (bottom-left) > **API Keys**, or visit [elevenlabs.io/app/settings/api-keys](https://elevenlabs.io/app/settings/api-keys)
3. Click **Create API Key**, name it, copy it
4. Add to `.env`: `ELEVENLABS_API_KEY=xi_your-key-here`

#### Pricing

| Plan | Price | Characters/month | Key features |
|------|-------|-------------------|--------------|
| **Free** | $0 | 10,000 | 3 custom voices, API access, attribution required |
| Starter | $5/mo | 30,000 | No attribution |
| Creator | $22/mo | 100,000 | Professional voice cloning |
| Pro | $99/mo | 500,000 | 96kbps audio, usage analytics |
| Scale | $330/mo | 2,000,000 | Priority support |

**Free tier:** 10,000 characters/month (roughly 2-3 minutes of narration). API access included. Music generation and sound effects also available on free tier with limited credits.

---

### fish.audio — Expressive TTS + Voice Cloning

> **High-emotion narration and reusable cloned voices.** S2-generation models support inline emotion tags (`[laugh]`, `[whispers]`) and 80+ languages. Voices created in the fish.audio playground are reused across runs via `reference_id`.

**Tools unlocked:** `fish_audio_tts`
**Env var:** `FISH_AUDIO_API_KEY`

#### Setup

1. Sign up at [fish.audio](https://fish.audio)
2. Create an API key at [fish.audio/go-api/api-keys](https://fish.audio/go-api/api-keys/)
3. Add to `.env`: `FISH_AUDIO_API_KEY=your-key-here`
4. (Optional) Build or pick a voice model in the fish.audio playground and pass its id as `reference_id` to reuse a cloned voice

#### Backend models

`model` is **required — there is no default**. Pass one of:

| Model | Best for |
|-------|----------|
| `s2.1-pro` | Latest flagship — inline emotion tags, 80+ languages, hero narration |
| `s2.1-pro-free` | Promotional free access to s2.1-pro — drafts, samples, validation runs (see caveats below) |
| `s2-pro` | First S2 generation — stable high quality with emotion-tag support |
| `s1` | Previous flagship, kept for compatibility (no emotion tags) |

**`s2.1-pro-free` caveats — promotional, not a durable free tier.** Per the [fish.audio announcement](https://fish.audio/ko/blog/s2-1-pro-free-api/?articleLocale=en), free API access runs **through August 31, 2026** and is subject to Fair Use limits, carries **no SLA or latency guarantee**, requests **may be retained** by fish.audio, and **commercial use is restricted**. Don't route client work or production narration through it, and don't plan long-term costs at $0 — `fish_audio_tts.estimate_cost()` falls back to the paid `s2.1-pro` rate after the promotional window ends.

The legacy `speech-1.x` tier and `s1-mini` have been removed from the fish.audio API and are not supported.

#### Pricing

Billing is **per UTF-8 byte of input text** (not per character) — CJK text and emoji cost 3-4x an ASCII character of the same visible length. Current list pricing: `s1` / `s2-pro` / `s2.1-pro` = $15 per 1M bytes; `s2.1-pro-free` is $0 only during the promotional window (through August 31, 2026 — see caveats above). Verify current pricing in the [official pricing guide](https://docs.fish.audio/developer-guide/models-pricing/pricing-and-rate-limits) before large batches.

---

### Doubao Speech — Mandarin TTS

> **Strong Mandarin narration.** Volcengine Doubao Speech is a good choice for Chinese explainer voiceovers and long-form narration that needs subtitle timing metadata.

**Tools unlocked:** `doubao_tts`
**Env vars:** `DOUBAO_SPEECH_API_KEY`, `DOUBAO_SPEECH_VOICE_TYPE`

#### Setup

1. Open the Volcengine Doubao Speech console and enable Speech Synthesis 2.0.
2. Create a new-console API Key.
3. Choose a Speech 2.0 voice type, for example `zh_female_vv_uranus_bigtts`.
4. Add to `.env`:
   ```bash
   DOUBAO_SPEECH_API_KEY=your-api-key
   DOUBAO_SPEECH_VOICE_TYPE=zh_female_vv_uranus_bigtts
   ```

#### API Notes

OpenMontage uses the new-console API key flow:

```text
X-Api-Key: ${DOUBAO_SPEECH_API_KEY}
X-Api-Resource-Id: seed-tts-2.0
```

Do not pass a new-console API Key as `X-Api-App-Id` or `X-Api-Access-Key`. That mismatch can produce `load grant: requested grant not found`.

#### What It Is Best For

- Natural Mandarin narration for Chinese-language explainers
- Async long-form narration via `/api/v3/tts/submit` and `/api/v3/tts/query`
- Character-level timing metadata for subtitle alignment
- Calm educational pacing where the video duration can follow the approved voice rhythm

#### Pacing

Start with `speech_rate: 0` for natural Mandarin delivery. If the approved format needs a tighter runtime, compare short samples at `speech_rate: 25` or `50` before generating the full narration. Do not force Doubao to match another provider's duration unless the user explicitly wants that tradeoff.

#### Pricing

Doubao Speech 2.0 is billed by character package or usage in Volcengine. OpenMontage estimates cost from text length and prefers provider-returned usage metadata when available.

---

### Tencent Hunyuan Cloud — Video Generation

> **Tencent Hunyuan (腾讯混元) cloud video generation via TokenHub API.** Generates
> videos from text or images using Tencent's Hunyuan models through the Tencent
> TokenHub API — an OpenAI-compatible gateway (tokenhub.tencentmaas.com) with
> simple Bearer-token authentication. No TC3-HMAC-SHA256 signing required.

**Tools unlocked:** `hunyuan_cloud_video`
**Env var:** `TENCENT_TOKENHUB_API_KEY`

#### Setup

1. Go to the [Tencent Cloud TokenHub console](https://console.cloud.tencent.com/tokenhub).
2. Create an application or navigate to the **API Key** section.
3. Generate an API key and copy its value.
4. Add to `.env`:
   ```bash
   TENCENT_TOKENHUB_API_KEY=your-tokenhub-api-key
   ```

#### What It's Best For

- **Chinese-friendly prompt understanding** — Hunyuan models natively understand Chinese prompts better than most Western APIs
- **Simple auth** — Bearer token, no complex signing (just an HTTP Authorization header)
- **Direct Tencent Cloud quota** — uses your own Tencent Cloud credits, not a third-party gateway mark-up
- **Both T2V and I2V** — one API key unlocks text-to-video and image-to-video

#### API Notes

TokenHub uses a **submit-then-poll** pattern:

```text
# Submit a generation task
POST https://tokenhub.tencentmaas.com/v1/api/video/submit
Authorization: Bearer ${TENCENT_TOKENHUB_API_KEY}

# Poll for results
POST https://tokenhub.tencentmaas.com/v1/api/video/query
Authorization: Bearer ${TENCENT_TOKENHUB_API_KEY}
```

| Model | Type | Pricing |
|-------|------|---------|
| `hy-video-1.5` | Text-to-video | 1.5 credits (~$0.25) |
| `yt-video-2.0` | Image-to-video | 2–5 credits (~$0.33–0.83) |

Resolution options: **720p** (default) or **1080p**.

A watermark (`logo_add`) is added by default. Set `logo_add: 0` to disable it (requires console approval from Tencent).

**Schema constraints:**
- **Prompt:** max 200 UTF-8 characters
- **Image:** max 10MB, 50–5000 px per side, aspect ratio 1:4 to 4:1
- **Formats:** jpg, png, jpeg, webp, bmp, tiff

#### Fallback Tools

If `hunyuan_cloud_video` returns an error, the agent may retry with: `jimeng_video`, `kling_official_video`, `minimax_video`

#### Pricing

Tencent TokenHub uses a credit-based pricing system (1 credit = 1.2 RMB ≈ $0.167 USD):

| Model | Resolution | Credits | Estimated USD |
|-------|-----------|---------|---------------|
| HY-Video-1.5 | any | 1.5 | ~$0.25 |
| YT-Video-2.0 | 480p | 2 | ~$0.33 |
| YT-Video-2.0 | 720p / 1080p | 5 | ~$0.83 |

> **Free tier:** Tencent occasionally offers new-user credits for TokenHub. Check the [TokenHub console](https://console.cloud.tencent.com/tokenhub) for current promotions.

---

### Azure AI Speech — Speech-to-Text

> **Cloud transcription.** Azure AI Speech Fast Transcription turns local audio into text with word-level timestamps, speaker diarization, and multi-language identification — no GPU required. Optional: the local faster-whisper `transcriber` remains the default offline STT path. When `AZURE_SPEECH_KEY` is set, the agent prefers `azure_stt` for cloud transcription.

**Tools unlocked:** `azure_stt`
**Env vars:** `AZURE_SPEECH_KEY`, `AZURE_SPEECH_REGION` (or `AZURE_SPEECH_ENDPOINT`)

#### Setup

1. In the [Azure portal](https://portal.azure.com), create a **Speech** resource (Azure AI services → Speech service).
2. Open the resource's **Keys and Endpoint** page.
3. Copy **KEY 1** and the **Location/Region** (e.g. `eastus`).
4. Add to `.env`:
   ```bash
   AZURE_SPEECH_KEY=your-speech-resource-key
   AZURE_SPEECH_REGION=eastus
   # AZURE_SPEECH_ENDPOINT=https://<custom>...  # optional, overrides region
   ```

#### API Notes

OpenMontage uses the **Fast Transcription** REST endpoint, which accepts a local
audio file directly (multipart upload) and returns a synchronous result — no
Azure Blob storage, SAS URLs, or async job polling:

```text
POST https://{region}.api.cognitive.microsoft.com/speechtotext/transcriptions:transcribe?api-version=2024-11-15
Ocp-Apim-Subscription-Key: ${AZURE_SPEECH_KEY}
```

For files longer than ~2 hours or bulk jobs, use Azure Batch Transcription instead (not wired into OpenMontage).

#### What It Is Best For

- Cloud transcription with word-level timestamps and no local GPU
- Multi-language auto-detection across a candidate locale set
- Speaker diarization without a HuggingFace token
- Subtitle timing metadata that flows straight into `subtitle_gen`

#### Pricing

Azure AI Speech Standard (S0) bills speech-to-text by audio-hour (roughly
$1.00/audio-hour at time of writing; a free F0 tier includes a limited monthly
allowance). OpenMontage estimates cost from the transcribed audio duration. See
[Azure AI Speech pricing](https://azure.microsoft.com/pricing/details/cognitive-services/speech-services/) for current rates.

---

### Azure AI Speech — Text-to-Speech

> **Cloud neural narration.** Azure neural TTS delivers high-quality multilingual voices with SSML prosody control and express-as styles — same Speech resource as `azure_stt`, so one key/region unlocks both directions. Optional: the local `piper_tts` remains the default offline TTS path. When `AZURE_SPEECH_KEY` is set, the agent may prefer `azure_tts` for cloud narration.

**Tools unlocked:** `azure_tts`
**Env vars:** `AZURE_SPEECH_KEY`, `AZURE_SPEECH_REGION` (or `AZURE_TTS_ENDPOINT`)

#### Setup

Identical to the STT setup above — the same Speech resource key and region work
for both. If you already configured `azure_stt`, `azure_tts` is available now.

```bash
AZURE_SPEECH_KEY=your-speech-resource-key
AZURE_SPEECH_REGION=eastus
# AZURE_TTS_ENDPOINT=https://<region>.tts.speech.microsoft.com  # optional, overrides region
```

Note: the TTS host (`<region>.tts.speech.microsoft.com`) differs from the STT
endpoint, so the optional override var is `AZURE_TTS_ENDPOINT`, not
`AZURE_SPEECH_ENDPOINT`.

#### API Notes

OpenMontage uses the synchronous REST v1 endpoint with an SSML body — no token
exchange, Blob storage, or job polling:

```text
POST https://{region}.tts.speech.microsoft.com/cognitiveservices/v1
Ocp-Apim-Subscription-Key: ${AZURE_SPEECH_KEY}
Content-Type: application/ssml+xml
X-Microsoft-OutputFormat: audio-48khz-192kbitrate-mono-mp3
```

Voice shortlist aliases: `andrew` (default — warm, confident), `brandon`
(deeper), `ava` (bright female), `guy` (authoritative), `jenny` (friendly). Any
Azure voice short name is accepted verbatim. See the `azure-text-to-speech`
skill for SSML `rate`/`pitch`/`style` guidance.

#### What It Is Best For

- High-quality neural narration on existing Azure credentials
- Calm, confident explainer / founder-register delivery
- Multilingual narration via the *Multilingual* voice family
- Deterministic re-renders (fixed voice + SSML → identical audio)

Not for: fully offline production (use `piper_tts`) or voice cloning (use
`elevenlabs_tts`).

#### Pricing

Azure neural TTS Standard (S0) bills roughly **$16 per 1M characters** (a free
F0 tier includes a limited monthly allowance). A 150-word narration segment
costs about $0.015. OpenMontage estimates cost from character count. See
[Azure AI Speech pricing](https://azure.microsoft.com/pricing/details/cognitive-services/speech-services/) for current rates.

---

### Google — TTS + Imagen + Music + Video (Shared Key)

> **One key, five tools.** Google Cloud TTS has 700+ voices in 50+ languages — the strongest localization option. `google_imagen` supports both Imagen 4 and Gemini 2.5 Flash Image, including projects without Imagen catalog access. Google Lyria generates high-quality background music. Gemini Omni Flash supports conversational video editing, and direct Veo generation covers premium short video clips.

**Tools unlocked:** `google_tts`, `google_imagen`, `google_music`, `gemini_omni_video`, `veo_video`
**Env var:** `GOOGLE_API_KEY` (or `GEMINI_API_KEY` — either works; `GEMINI_API_KEY` takes precedence)

#### Setup

1. Go to [Google AI Studio](https://aistudio.google.com/) and sign in
2. Navigate to [aistudio.google.com/apikey](https://aistudio.google.com/apikey)
3. Click **Create API Key**, select a Google Cloud project
4. Copy the key
5. Add to `.env`: `GOOGLE_API_KEY=AIza...` (or `GEMINI_API_KEY=AIza...`)

**For TTS specifically**, you also need to enable the Text-to-Speech API:
1. Visit [console.cloud.google.com/apis/library/texttospeech.googleapis.com](https://console.cloud.google.com/apis/library/texttospeech.googleapis.com)
2. Click **Enable**
3. Make sure your API key's restrictions allow the Text-to-Speech API

**For Imagen, Lyria Music, Gemini Omni video, and direct Veo video**, enable the Generative Language API:
1. Visit [console.cloud.google.com/apis/library/generativelanguage.googleapis.com](https://console.cloud.google.com/apis/library/generativelanguage.googleapis.com)
2. Click **Enable**

#### Google TTS Pricing

| Voice Type | Free tier | Paid (per 1M chars) | Notes |
|-----------|-----------|---------------------|-------|
| **Standard** | 1M chars/month | $4.00 | Basic quality, fast |
| **WaveNet** | 1M chars/month | $16.00 | Natural-sounding |
| **Neural2** | 1M chars/month | $16.00 | Best quality |
| **Studio** | — | $24.00 | Professional studio voices |
| **Chirp** | — | $4.00 | Conversational style |

The free tiers apply *independently* — you get 1M Standard AND 1M WaveNet AND 1M Neural2 characters per month free. That's roughly 250+ minutes of narration per month at zero cost.

#### Google Imagen Pricing

| Model | Price per image |
|-------|----------------|
| Imagen 4 Fast | $0.02 |
| Imagen 4 Standard | $0.04 |
| Imagen 4 Ultra | $0.06 |
| Gemini 2.5 Flash Image (`gemini-2.5-flash-image`) | $0.039 |

**Free tier for Imagen:** None. Paid tier only.

To select the Gemini backend through the governed `image_selector`, pass
`preferred_provider: "google_imagen"` and
`model_name: "gemini-2.5-flash-image"`. The selector maps its neutral
`model_name` field to the provider's `model` input.

#### Gemini Omni Video Pricing

| Model | Price | Notes |
|-------|-------|-------|
| `gemini-omni-flash-preview` | ~$0.10 per second of video | Billed as 5,792 output tokens/sec of 720p video at $17.50/1M tokens |

Generates 3–10 second clips at 720p/24fps with synthesized audio, plus stateful conversational editing (`edit_video` via `previous_interaction_id`). **Paid tier only — no free tier.** A typical 8-second clip costs ~$0.80; each edit turn generates a new clip and bills again.

#### Google Music (Lyria) Pricing

| Model | Price per generation request |
|-------|-----------------------------|
| `lyria-3-pro-preview` | $0.08 (flat rate, up to 184s duration) |

**Free tier for Music:** None. Paid tier only.

**New account bonus:** Google Cloud offers **$300 in free credits** for new accounts (90-day trial), applicable to TTS, Imagen, Music, Gemini Omni video, and direct Veo video.

#### Google TTS Voice Types

Google TTS offers 700+ voices across 50+ languages. Voice names follow the pattern `{language}-{type}-{letter}`:

| Type | Example | Quality | Cost |
|------|---------|---------|------|
| **Chirp 3 HD** | `en-US-Chirp3-HD-Orus` | **Best (2024, most natural)** | **Mid — default** |
| Standard | `en-US-Standard-A` | Good | Cheapest |
| WaveNet | `en-US-WaveNet-D` | Very good | Mid |
| Neural2 | `en-US-Neural2-D` | Excellent | Mid |
| Studio | `en-US-Studio-O` | Professional | Highest |
| Journey | `en-US-Journey-D` | Conversational (long-form) | Mid |

**Recommended voices:** `en-US-Chirp3-HD-Orus` (male, rich/cinematic), `en-US-Chirp3-HD-Aoede` (female, warm). These are Google's newest tier — most natural-sounding, uses the v1beta1 endpoint automatically.

**Languages include:** English (US, UK, AU, IN), Spanish, French, German, Italian, Portuguese, Japanese, Korean, Chinese (Mandarin, Cantonese), Arabic, Hindi, Russian, Dutch, Polish, Turkish, Vietnamese, Thai, Indonesian, and 30+ more.

---

### OpenAI — TTS + Image Generation

> **Solid all-rounder.** GPT Image 2 handles complex multi-element compositions and in-image text well. TTS is fast and affordable.

**Tools unlocked:** `openai_tts`, `openai_image`
**Env var:** `OPENAI_API_KEY`

#### Setup

1. Go to [platform.openai.com/signup](https://platform.openai.com/signup) and create an account
2. Add a payment method at [platform.openai.com/account/billing](https://platform.openai.com/account/billing)
3. Navigate to [platform.openai.com/api-keys](https://platform.openai.com/api-keys)
4. Click **Create new secret key**, name it, copy it
5. Add to `.env`: `OPENAI_API_KEY=sk-...`

#### TTS Pricing

| Model | Price per 1M characters |
|-------|------------------------|
| tts-1 | $15.00 |
| tts-1-hd | $30.00 |
| gpt-4o-mini-tts | $12.00 |

#### Image Pricing

| Model | Size | Quality | Price per image |
|-------|------|---------|----------------|
| GPT Image 2 | 1024x1024 | low | $0.006 |
| GPT Image 2 | 1024x1024 | medium | $0.053 |
| GPT Image 2 | 1024x1024 | high | $0.211 |
| GPT Image 2 | 1024x1536 / 1536x1024 | low | $0.005 |
| GPT Image 2 | 1024x1536 / 1536x1024 | medium | $0.041 |
| GPT Image 2 | 1024x1536 / 1536x1024 | high | $0.165 |

> **Note:** DALL-E 2/3 were shut down by OpenAI on 2026-05-12, and the `gpt-image-1` family (`gpt-image-1-mini`, `gpt-image-1.5`) retires 2026-12-01 — `gpt-image-2` is OpenAI's recommended replacement ([deprecations](https://developers.openai.com/api/docs/deprecations)).

**Free tier:** None. Requires prepaid billing. Previously offered $5 in free credits for new accounts (discontinued for most signups).

---

### Runway — Native and Third-Party Video Models

> **Multi-model production API.** OpenMontage supports current Runway-native
> models plus documented third-party Seedance 2.5, Gemini Omni Flash, and
> MiniMax H3/Hailuo 3.0 routes.

**Tools unlocked:** `runway_video`
**Env var:** `RUNWAY_API_KEY`

#### Setup

1. Go to [dev.runwayml.com](https://dev.runwayml.com/) and create a developer account
2. Subscribe to a paid plan (Standard or above — API requires subscription)
3. Generate an API key from the developer portal
4. Add to `.env`: `RUNWAY_API_KEY=key_...`

#### Pricing

| Plan | Price | Credits/month | Video capacity |
|------|-------|---------------|----------------|
| **Free** | $0 | 125 one-time | ~5 seconds Gen-4 |
| Standard | $12/mo | 625 | ~25 seconds Gen-4 |
| Pro | $28/mo | 2,250 | ~90 seconds Gen-4 |
| Unlimited | $76/mo | Unlimited (Explore Mode) | Unlimited Gen-4 Turbo |

**API pricing (Runway credits are $0.01 each):**

| Model | Price per second |
|-------|-----------------|
| Gen-4 Turbo | ~$0.05 |
| Gen-4.5 | ~$0.12 |
| Seedance 2.5 | ~$0.20 at 480p / ~$0.30 at 720p |
| Gemini Omni Flash | ~$0.10 generation / ~$0.11 video editing |
| MiniMax H3 (`hailuo3`) | ~$0.10 at 768P / ~$0.15 at 2K |

Seedance 2.5 supports text, image, and video inputs, 4–30 second outputs, and
up to 30 image, 10 video, and 10 audio references. Gemini Omni Flash supports
3–10 second text/image generation plus video editing with up to five image
references. Hailuo 3.0 is Runway's MiniMax H3 route and supports 5–15 second
outputs at 768P or 2K. The adapter maps each model to its exact request field
names instead of sending a generic payload.

Gen-3 Alpha Turbo and Gen-4 Aleph were removed from the Runway API on
2026-07-30 and are not offered by the tool.

**Free tier:** 125 one-time credits (no monthly renewal). Enough for about 5 seconds of Gen-4 video. API access requires a paid subscription.

---

### Higgsfield — Multi-Model Video Orchestrator

> **Multi-model video platform.** Routes to Kling 3.0, Veo 3.1, Sora 2, WAN 2.5, and proprietary Soul Cinema through a single API. Includes Soul ID for character consistency across clips.

**Tools unlocked:** `higgsfield_video`
**Env vars:** `HIGGSFIELD_API_KEY` + `HIGGSFIELD_API_SECRET` (or combined `HIGGSFIELD_KEY=key:secret`)

#### Setup

1. Go to [cloud.higgsfield.ai](https://cloud.higgsfield.ai/) and create an account
2. Subscribe to a plan (Starter or above for API access)
3. Navigate to API Keys section at [cloud.higgsfield.ai/api-keys](https://cloud.higgsfield.ai/api-keys)
4. Generate an API key and secret
5. Add to `.env`:
   ```
   HIGGSFIELD_API_KEY=your-api-key
   HIGGSFIELD_API_SECRET=your-api-secret
   ```

#### Pricing

| Plan | Price | Notes |
|------|-------|-------|
| Free | $0 | Limited credits |
| Starter | $15/mo | Basic allocation |
| Plus | $34/mo | Mid-tier, ~33-56 Kling 3.0 clips |
| Ultra | $84/mo | High volume |

**Per-generation costs (approximate, via credits):**

| Model | Cost per clip |
|-------|--------------|
| Kling 3.0 | ~$0.10 (cheapest) |
| WAN 2.5 | ~$0.10 |
| Soul Cinema | ~$0.15 |
| Veo 3.1 | ~$0.50 |
| Sora 2 | ~$0.50 |

**Free tier:** Limited credits on signup. No monthly renewal on free plan.

---

### HeyGen — Avatar Video Gateway

> **Multi-model video gateway.** Access VEO, Sora, Runway, Kling, and Seedance through a single API.

**Tools unlocked:** `heygen_video`
**Env var:** `HEYGEN_API_KEY`

#### Setup

1. Go to [app.heygen.com/register](https://app.heygen.com/register) and create an account
2. Navigate to the API section in settings
3. Generate your API key
4. Add API balance (prepaid, separate from web plan credits)
5. Add to `.env`: `HEYGEN_API_KEY=your-key-here`

#### Pricing

| Service | Price |
|---------|-------|
| Avatar video (Engine III) | $0.017/sec |
| Avatar video (Engine IV) | $0.10/sec |
| Prompt to Video | $0.033/sec |
| Video Translation (Speed) | $0.05/sec |
| Video Translation (Precision) | $0.10/sec |

**Web plans:**

| Plan | Price | Notes |
|------|-------|-------|
| Free | $0 | 1 credit (demo) |
| Creator | $24/mo | Limited credits |
| Business | $72/mo | API access, more credits |

**Free tier:** 1 credit on web platform. API is pay-as-you-go with prepaid balance.

---

### Suno — AI Music Generation

> **Full songs with vocals and lyrics.** Any genre, up to 8 minutes. Instrumentals or vocal tracks.

**Tools unlocked:** `suno_music`
**Env var:** `SUNO_API_KEY`

#### Setup

1. Go to [suno.com](https://suno.com) and create a Suno account
2. For API access, go to [sunoapi.org](https://sunoapi.org) and create an account
3. Navigate to the dashboard and copy your API key
4. Add credits (1 credit = $0.005 USD)
5. Add to `.env`: `SUNO_API_KEY=your-key-here`

#### Pricing

**Suno platform:**

| Plan | Price | Credits | Notes |
|------|-------|---------|-------|
| Free | $0 | 50/day | ~10 songs/day, non-commercial only |
| Pro | $10/mo | 2,500/mo | Commercial license |
| Premier | $30/mo | 10,000/mo | Commercial license |

**API (via sunoapi.org):** Pay-as-you-go, 1 credit = $0.005. Each generation produces 2 tracks.

---

### Pexels — Free Stock Media

> **Completely free.** No cost, no attribution required, commercial use allowed.

**Tools unlocked:** `pexels_image`, `pexels_video`
**Env var:** `PEXELS_API_KEY`

#### Setup

1. Go to [pexels.com/join](https://www.pexels.com/join/) and create a free account
2. Navigate to [pexels.com/api](https://www.pexels.com/api/)
3. Click **Your API Key** or request API access
4. Copy your key from the dashboard
5. Add to `.env`: `PEXELS_API_KEY=your-key-here`

#### Pricing

**Completely free.** No paid tiers. No attribution required. Commercial use allowed.

- 200 requests/hour
- 20,000 requests/month
- Photo and video search + download

---

### Pixabay — Free Stock Media

> **Completely free.** 5M+ royalty-free images and videos.

**Tools unlocked:** `pixabay_image`, `pixabay_video`
**Env var:** `PIXABAY_API_KEY`

#### Setup

1. Go to [pixabay.com/accounts/register](https://pixabay.com/accounts/register/) and create a free account
2. Navigate to [pixabay.com/api/docs](https://pixabay.com/api/docs/)
3. Your API key is displayed at the top of the docs page (after login)
4. Copy the key
5. Add to `.env`: `PIXABAY_API_KEY=your-key-here`

#### Pricing

**Completely free.** No paid tiers. No attribution required. Commercial use allowed.

- ~100 requests/minute
- 5,000 requests/hour
- Photo and video search + download
- Standard API limited to 1280px images (full resolution requires editorial API)

---

## Local Providers (Free, No API Key)

These providers run entirely on your machine. No network, no API key, no cost. Some require a GPU.

### Remotion — Programmatic Video Composition

> **React-based video rendering.** Turns still images into animated video with spring physics, animated text cards, stat cards, charts, and transitions. **This is the key fallback when no video generation providers are configured** — the agent generates images and Remotion animates them into professional-looking video.

**Tool:** `video_compose` (with `operation="render"` — auto-routes to Remotion when needed)
**Runtime:** CPU (Node.js required)
**
```

### docs/PR_REVIEW_GUIDE.md
```
# Pull Request Review Guide

This guide is for community reviewers, maintainers, and AI assistants reviewing
OpenMontage pull requests. It is a review framework, not a closed checklist.
Use it to structure the review, then keep looking for issues that are specific
to the PR in front of you.

OpenMontage is an agent-orchestrated video production system. Many PRs affect
more than the file they edit: a provider change can affect tool discovery,
selector routing, setup instructions, pipeline decisions, cost reporting, and
the user-visible production flow. Good reviews protect those contracts.

## Review Mindset

Start with these questions:

- Does this PR move OpenMontage in the right direction?
- Is the scope focused, or is it mixing unrelated changes?
- Can a user, maintainer, or agent understand the behavior after this lands?
- Does the PR preserve the agent-first architecture?
- Does it introduce regressions in provider discovery, pipeline artifacts, or
  rendering behavior?
- Are tests and docs updated at the same level as the behavior change?
- Are there security, privacy, dependency, or supply-chain concerns?

The answer can be "useful, but not merge-ready." That is a good review outcome
when the idea is aligned but the implementation needs cleanup.

## Review Outputs

A useful review should usually produce one of these outcomes:

- **Approve**: the PR is useful, focused, tested, and low-risk enough to merge.
- **Comment**: the PR is promising but needs cleanup before approval.
- **Request changes**: the PR has blockers that would create regressions,
  break contracts, or mislead users.
- **Close or redirect**: the PR is not aligned, mostly noise, or belongs in an
  issue/discussion before code.

Avoid rubber-stamp approvals. Also avoid turning every concern into a blocker.
Name the actual severity and explain the impact.

## General Review Areas

### Project Direction

Check whether the PR solves a real OpenMontage problem.

- Does it improve video production quality, reliability, speed, portability,
  provider coverage, local execution, docs, tests, or contributor experience?
- Does it duplicate an existing path without improving it?
- Is it a speculative feature with no clear user workflow?
- Does it introduce maintenance burden disproportionate to the value?

### Scope Hygiene

Noise makes reviews unsafe.

- Are unrelated files changed?
- Are lockfiles changed only when dependencies actually changed?
- Are generated files, screenshots, binary assets, or local artifacts included
  without reason?
- Are docs/test fixes bundled with feature work in a way that hides risk?
- Is the branch stale against latest `main`?

If a PR is useful but noisy, ask for a narrower diff before deep approval.

### Regression Risk

Look beyond the changed file.

- Does the change affect existing users or only add a new optional path?
- Does it alter default provider selection, fallback behavior, or setup menus?
- Does it change schemas, artifacts, or pipeline stage contracts?
- Does it change rendering output, timing, audio, captions, or file paths?
- Does it create silent fallback behavior where the user should be told?

### Security and Supply Chain

Review security issues factually and with evidence. Do not make public claims
about a contributor's intent. If you see suspicious code, describe the behavior
and risk.

Check for:

- New network calls, uploads, telemetry, or background processes
- Secret exfiltration risks, `.env` reads, token logging, or unsafe debug output
- Shell execution, `subprocess`, dynamic imports, `eval`, `exec`, or generated
  code execution
- Dependency additions, install scripts, package-lock churn, or broad version
  ranges
- Unsafe file deletion, path traversal, archive extraction, or writes outside
  the expected project directory
- Remote model downloads or provider calls that are not surfaced in metadata
- Prompt injection surfaces where external content could instruct the agent

Use language like:

- "I found a security blocker: this command executes user-controlled input."
- "This dependency change needs justification before merge."
- "I did not find an actionable security issue in the reviewed diff."

Avoid public phrasing like:

- "No malicious intent."
- "This author is safe."
- "This is definitely harmless."

### Performance and Resource Use

OpenMontage works with video, audio, image generation, and local models. Small
code changes can create large runtime costs.

- Does the PR add repeated model loads instead of reusing state?
- Does it download large files without clear setup/status messaging?
- Does it increase render time, memory, VRAM, disk, or network use?
- Does it change frame extraction, composition, encoding, or audio processing
  in a way that could slow common paths?
- Are resource profiles and cost estimates realistic?

## OpenMontage Architecture Checks

### Agent-First Architecture

OpenMontage's control plane is the agent following markdown skills and YAML
manifests. Python should provide tools and persistence, not hidden orchestration.

Flag PRs that:

- Add Python orchestrators for creative decisions, stage transitions, or review
  policy
- Hide provider/model/runtime decisions inside code without user visibility
- Bypass pipeline manifests, stage director skills, checkpoints, or review
- Move quality policy into ad hoc code instead of documented instructions

Good PRs keep intelligence in instructions and contracts, with Python handling
well-bounded execution.

### Tool Contract

Every tool should inherit from `tools/base_tool.py` and satisfy the `BaseTool`
contract.

For new or changed tools, review:

- `name`, `version`, `tier`, `capability`, `provider`
- `runtime`, `stability`, `execution_mode`, `determinism`
- `dependencies` using supported prefixes such as `cmd:`, `env:`, `python:`
- `install_instructions`
- `input_schema`, `output_schema`, and artifact behavior
- `supports`, `best_for`, `not_good_for`
- `resource_profile`
- `retry_policy`
- `fallback` and `fallback_tools`
- `agent_skills`
- `user_visible_verification`
- `estimate_cost()` and `estimate_runtime()` where relevant
- `execute()` returning a `ToolResult`

Metadata is user-facing. If setup, offline behavior, cost, model downloads, or
hardware requirements are inaccurate, the provider menu and agent planning will
mislead users.

### Tool Registry and Discovery

Tool discovery flows through `tools/tool_registry.py`. Avoid hardcoded tool
lists unless there is a strong reason.

Check:

- Does the tool register through normal package discovery?
- Does it use the right `capability` so selectors can find it?
- Does `get_status()` report availability accurately?
- Does an import failure in one optional provider break unrelated discovery?
- Does the provider menu show useful setup instructions?
- Does the PR accidentally make unavailable tools look configured?

Useful commands:

```bash
python -c "from tools.tool_registry import registry; import json; registry.discover(); print(json.dumps(registry.capability_catalog(), indent=2))"
python -c "from tools.tool_registry import registry; import json; registry.discover(); print(json.dumps(registry.provider_menu_summary(), indent=2))"
```

### Selectors and Providers

Selectors route capability-level requests to provider tools:

- `tts_selector`
- `image_selector`
- `video_selector`

When reviewing selector or provider changes:

- Confirm the provider has the correct `capability`.
- Confirm selector input names map to provider input names.
- Confirm provider-specific options do not get silently ignored.
- Confirm user preference is respected when explicit.
- Confirm unavailable providers do not block available alternatives.
- Confirm ranking/fallback changes are tested.
- Confirm the selector still returns useful alternatives and reasoning.

Adding a provider should usually not require selector code changes. If it does,
the PR should explain why.

### Pipeline Manifests and Stage Skills

Pipeline manifests live in `pipeline_defs/`. Stage instructions live in
`skills/pipelines/`.

For pipeline changes, check:

- Manifest schema validity
- Stage order and stage names
- `produces` artifacts
- `tools_available`
- `review_focus`
- `success_criteria`
- `checkpoint_required`
- `human_approval_default`
- Matching stage director skills
- Tests in `tests/contracts/` or `tests/pipelines/`

The manifest and the stage skill must agree. If the manifest says a stage
produces `scene_plan`, the director skill should actually guide creation of a
valid `scene_plan`.

### Canonical Artifacts and Schemas

Artifacts in `schemas/artifacts/` are contracts between stages.

When reviewing schema or artifact changes:

- Does every producer still write valid artifacts?
- Does every consumer still understand the artifact?
- Are required fields justified?
- Are migrations or backward compatibility needed?
- Do tests cover valid and invalid examples?
- Does the checkpoint protocol still work with the changed artifact?

Schema changes are high-impact. Treat them as cross-pipeline changes unless the
PR proves otherwise.

### Checkpoints and Review Policy

OpenMontage uses checkpoints for resume, human approval, audit trails, and
stage gating.

Check:

- Does the PR preserve checkpoint status semantics?
- Does it avoid skipping required human approval?
- Does it preserve cost snapshots and review metadata where expected?
- Does it avoid writing incomplete canonical artifacts as completed stages?
- Does it align with `skills/meta/checkpoint-protocol.md`?
- Does it align with `skills/meta/reviewer.md`?

Review logic should remain instruction-driven unless the PR is adding a narrow
mechanical validator.

### Composition Runtimes

OpenMontage can compose with Remotion, HyperFrames, or FFmpeg. Runtime choices
are user-visible production decisions.

For render/composition PRs, check:

- Does `video_compose` preserve explicit `render_runtime` routing?
- Are Remotion, HyperFrames, and FFmpeg paths considered where relevant?
- Does the PR avoid silent runtime swaps?
- Are runtime availability errors surfaced as blockers?
- Are Node, FFmpeg, `npx`, and package requirements checked accurately?
- Do render reports contain enough evidence to debug failures?
- Are browser previews treated as QA/debug artifacts when the production render
  path is different?

Silent downgrades from motion-led production to still-led fallback are review
findings, not harmless implementation details.

### Cost, Budget, and Paid Providers

OpenMontage should not silently spend money or imply a paid provider is free.

Check:

- Does the tool estimate cost accurately enough for planning?
- Are first-time paid provider uses visible to the user?
- Does the provider doc mention pricing/free-tier caveats?
- Does fallback from paid to free, or free to paid, require user visibility?
- Are model downloads, hosted endpoints, or cloud GPU usage described honestly?

### Docs and User-Facing Claims

Docs are part of the product. Provider setup docs often drive agent behavior.

Check:

- Does the PR update `docs/PROVIDERS.md` when adding a provider?
- Does `docs/ARCHITECTURE.md` need an update for architectural changes?
- Are setup instructions accurate on macOS, Windows, and Linux where claimed?
- Do docs distinguish API keys, local installs, model downloads, and cached
  offline operation?
- Are package versions and model versions clearly separated?
- Are limitations stated plainly?

## Scenario-Specific Review Prompts

### New Provider or Tool

Ask:

- Is this provider useful for OpenMontage workflows?
- Does it add real coverage or just duplicate an existing provider?
- Is the provider internationally known, nationally or regionally important,
  or otherwise clearly valuable to OpenMontage users?
- Is the tool discoverable through the registry?
- Does the matching selector discover and route to it?
- Are provider inputs compatible with selector inputs?
- Does status checking reflect real availability?
- Are setup docs, dependencies, cost, network, and cache behavior accurate?
- Does it have focused tests?
- Does it avoid importing heavyweight dependencies at module import time?
- Are generated artifacts written to expected paths?

Minimum expected coverage:

- Tool metadata/contract test
- Registry discovery test
- Status behavior test with dependencies mocked when needed
- Selector/routing test if it joins a selector-backed capability
- Docs update for user-visible providers

Provider viability matters. OpenMontage should not become a grab bag of
unmaintained or one-off integrations. A provider does not need to be globally
dominant, but it should have a clear reason to belong here.

Consider:

- Is there evidence of an active user base, maintained API docs, SDK support,
  or community adoption?
- Is it widely used internationally, or meaningfully popular in a specific
  national, regional, language, or industry market?
- Does it unlock a capability, language, price point, region, quality tier,
  compliance posture, or local/offline workflow that existing providers do not
  cover well?
- Are pricing, quotas, API access, model availability, and terms clear enough
  for contributors to test and maintain the integration?
- Is the provider likely to remain usable over the next six months?
- Does the provider's value justify the maintenance burden it adds?

### Selector Change

Ask:

- Does it still auto-discover providers?
- Does it avoid hardcoded provider lists?
- Does it preserve explicit user preference?
- Does it handle unavailable providers cleanly?
- Does it explain the selected provider?
- Does it preserve alternatives considered?
- Does it map shared inputs to provider-specific inputs?

### Local GPU or Model Runtime Change

Ask:

- Is the hardware requirement accurate?
- Does CPU/MPS/CUDA behavior match the implementation?
- Are dtype choices safe for each device?
- Are model downloads and cache behavior documented?
- Does the resource profile reflect realistic RAM, VRAM, and disk needs?
- Does setup avoid pretending local GPU install is a one-minute API-key fix?

### Render Runtime Change

Ask:

- Does it preserve runtime choice in `edit_decisions.render_runtime`?
- Does it avoid fallback without user-visible approval?
- Are Remotion and HyperFrames contracts respected?
- Are smoke tests or render probes included?
- Does final output get validated with ffprobe/frame/audio checks where relevant?

### Pipeline or Skill Change

Ask:

- Does the manifest still validate?
- Do stage skills exist and match stage names?
- Are `review_focus` and `success_criteria` meaningful?
- Are canonical artifacts valid?
- Are human approval gates correct?
- Are tests updated?

### Schema Change

Ask:

- Which producers and consumers are affected?
- Is the field required or optional?
- Do existing checkpoints/artifacts still work?
- Are tests updated for both valid and invalid data?
- Does the change need a migration note?

### Dependency or Lockfile Change

Ask:

- Is the dependency necessary for the PR?
- Is the lockfile change proportional?
- Are install scripts or transitive packages risky?
- Is the package maintained and appropriately licensed?
- Does it work on the supported Python/Node versions?
- Are version bounds too loose or too strict?

### Docs-Only Change

Ask:

- Is the doc technically accurate?
- Does it match current code and registry behavior?
- Does it overpromise provider quality, cost, offline operation, or platform
  support?
- Does it point users to the right setup and troubleshooting path?

Docs-only PRs can still create regressions by teaching users or agents the
wrong behavior.

## Testing Expectations

Pick tests based on risk. Do not require expensive integration tests for every
small doc fix, but do require evidence for changed behavior.

Common checks:

```bash
python -m pytest tests/contracts -q
python -m pytest tests/tools -q
python -m pytest tests/qa -q
python -m py_compile path/to/changed_file.py
```

For provider PRs, focused mocked tests are often better than expensive live API
tests. Live-provider QA is useful when credentials and cost are acceptable, but
the contract should not depend on a maintainer having every provider configured.

If tests cannot be run, the review should say why and what risk remains.

## PR Comment Guidance

Good review comments are specific, evidence-based, and actionable.

Prefer:

- "This test fails with the current branch: `...`"
- "This provider will not be discovered because `capability` is set to `...`."
- "This setup claim is misleading because first run downloads model weights."
- "Please split the lockfile churn from this provider change."

Avoid:

- Vague comments like "clean this up"
- Personal comments about the contributor
- Public speculation about intent
- Overclaiming safety
- Long lists of nits when there is a clear blocker

When a PR has several issues, prefer one consolidated comment. It helps the
author fix everything in one pass. Use inline comments for exact line-level
bugs that need code context.

Suggested public language for security review:

- "I found an actionable security issue in this diff."
- "This area needs a security review before merge."
- "I did not find an actionable security issue in the reviewed diff."

Do not state or imply that a contributor has or lacks malicious intent. Review
the code and behavior.

## Maintainer and AI-Agent Workflow

This section is public so contributors understand how reviews are performed.
It is a workflow, not a limit on reviewer judgment.

For a full review:

1. Fetch latest `main`.
2. Check out the PR in a clean worktree.
3. Inspect PR metadata: title, linked issues, changed files, author notes, and
   prior comments.
4. Review the diff for scope, usefulness, and architecture fit.
5. Identify the PR scenario: provider, selector, pipeline, schema, runtime,
   docs, tests, dependency, or mixed.
6. Apply the relevant scenario prompts from this guide.
7. Run focused tests or explain why they were not run.
8. Check docs and user-facing claims against implementation.
9. Check security, dependency, and supply-chain risk.
10. Write findings ordered by severity.
11. Decide: approve, comment, request changes, or close/redirect.

For AI-assisted review, ask the agent to report evidence, not just conclusions:

- Commands run and their results
- Files inspected
- Architecture contracts touched
- Risks that remain unverified
- Exact merge blockers

Do not approve from a summary alone. The reviewer or agent should inspect the
diff and relevant project contracts.

## Merge-Readiness Rubric

Before approving, confirm:

- The PR is useful and aligned with project direction.
- The diff is focused and free of unrelated churn.
- Architecture contracts are preserved.
- Tests cover the behavior at the right level.
- Docs match user-visible behavior.
- Security and supply-chain risks have been considered.
- Performance, cost, and resource claims are realistic.
- The branch is current enough that review findings are still valid.
- Remaining risks are acceptable and stated.

Approving does not mean the PR is perfect. It means the change is useful,
understood, appropriately tested, and safe enough to land.
```

### docs/SPONSORS.md
```
# Sponsors

This document defines how sponsor logos are added to the OpenMontage README.

## Sponsor Asset Convention

- Store sponsor logos in `assets/sponsors/`.
- Use a lowercase kebab-case filename based on the sponsor name, for example `acme-video.svg`.
- Prefer SVG. Use PNG only when the sponsor cannot provide vector artwork.
- Keep logos transparent, tightly cropped, and readable at `44px` height.
- Use the sponsor's official website or product page as the link target.
- Use descriptive alt text: `Acme Video logo`, not just `logo`.

## README Snippet

Add each sponsor as a table row inside the `Sponsors` section near the top of `README.md`:

```html
<tr>
<td width="180" align="center"><a href="https://example.com"><img src="assets/sponsors/example-sponsor.svg" alt="Example Sponsor" width="150"></a></td>
<td><strong>Example Sponsor</strong> helps OpenMontage users do something concrete. Mention the useful product outcome, then close with a short <a href="https://example.com">CTA link</a>.</td>
</tr>
```

For a sponsor with separate light and dark logos, use a `picture` element:

```html
<tr>
<td width="180" align="center">
  <a href="https://example.com">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="assets/sponsors/example-sponsor-dark.svg">
      <img src="assets/sponsors/example-sponsor-light.svg" alt="Example Sponsor" width="150">
    </picture>
  </a>
</td>
<td><strong>Example Sponsor</strong> helps OpenMontage users do something concrete. Mention the useful product outcome, then close with a short <a href="https://example.com">CTA link</a>.</td>
</tr>
```

## Intake Checklist

Before adding a sponsor, collect:

- Sponsor display name
- Sponsor URL
- Logo file, preferably SVG
- Confirmation that OpenMontage has permission to display the logo in the README
- Any required trademark wording, if the sponsor has one

Do not add tracking URLs, affiliate redirects, or claims about endorsement unless they are explicitly approved by the project maintainer.
```

### docs/apple-silicon-mps.md
```
# Apple Silicon (MPS) Support

OpenMontage supports Apple Silicon Macs (M1/M2/M3/M4/M5) via PyTorch's
Metal Performance Shaders (MPS) backend. Local GPU tools — video generation,
upscaling, and face restoration — automatically detect and use MPS when
available.

## Requirements

- macOS 12.3 (Monterey) or later
- Apple Silicon Mac (M-series chip)
- Python 3.10+

## Quick Setup

```bash
# Enable local generation
export VIDEO_GEN_LOCAL_ENABLED=true

# Install dependencies — MPS support is included in the default torch wheel
uv pip install diffusers transformers accelerate torch pillow requests

# For upscaling and face restoration
uv pip install realesrgan gfpgan
```

No special CUDA build or separate MPS package is needed — `uv pip install torch`
on macOS automatically includes MPS support.

## How It Works

The `get_torch_device()` helper in `tools/video/_shared.py` detects the best
available device:

1. **CUDA** (NVIDIA GPU) — used when available; fastest for diffusion models
2. **MPS** (Apple Silicon Metal) — used on M-series Macs; good performance
3. **CPU** — fallback, always available but significantly slower

Device selection is automatic. All local GPU tools (`upscale`, `face_restore`,
`ltx_video_local`, `wan_video_local`, etc.) route through this helper.

## Known Limitations

- **VRAM**: Apple Silicon uses unified memory. Models that require >16 GB VRAM
  may not fit on 16 GB Macs. Check the tool's `resource_profile.vram_mb`.
- **bfloat16**: Not supported on MPS. The pipeline automatically uses float16
  on MPS and float32 on CPU.
- **CPU offloading**: `enable_model_cpu_offload()` is CUDA-only. On MPS, the
  pipeline falls back to direct device placement.
- **Half-precision in Real-ESRGAN**: fp16 can produce NaN artifacts on MPS, so
  upscaling automatically uses fp32 on non-CUDA devices.

## Verifying MPS Is Active

```python
from tools.video._shared import get_torch_device
print(get_torch_device())  # Should print "mps" on Apple Silicon
```

If this prints `"cpu"` on an Apple Silicon Mac, verify:
- macOS version is 12.3+
- PyTorch is installed (`uv pip install torch`)
- You're running native ARM Python (not Rosetta x86)
```



### CLAUDE.md
```
# OpenMontage

**MANDATORY: Read [`AGENT_GUIDE.md`](AGENT_GUIDE.md) before responding to ANY user message.**

Do not act on the user's request until you have read AGENT_GUIDE.md.
It contains routing rules that determine your first action based on what the user asked.
Skipping it WILL cause you to take the wrong action.

There are no instructions in this file. All instructions are in AGENT_GUIDE.md.
```

### AGENTS.md
```
# OpenMontage

**MANDATORY: Read `AGENT_GUIDE.md` before responding to ANY user message.**

Do not act on the user's request until you have read AGENT_GUIDE.md.
It contains routing rules that determine your first action based on what the user asked.
Skipping it WILL cause you to take the wrong action.

There are no instructions in this file. All instructions are in AGENT_GUIDE.md.
```

### CONTRIBUTING.md
```
# Contributing to OpenMontage

Thank you for improving OpenMontage. We do not require a Contributor License Agreement (CLA), Developer Certificate of Origin sign-off, or any separate contribution contract.

By submitting a pull request, you confirm that you have the right to contribute its contents. Contributions must be compatible with the repository's [AGPLv3 license](LICENSE), and accepted contributions remain available under that license.

Please keep pull requests focused and include tests when behavior changes.
```


## Top-level structure
```
dir	.agents	.agents
dir	.claude	.claude
dir	.codex	.codex
dir	.cursor	.cursor
file	.env.example	.env.example
file	.gitattributes	.gitattributes
dir	.github	.github
file	.gitignore	.gitignore
file	.python-version	.python-version
file	.windsurfrules	.windsurfrules
file	AGENTS.md	AGENTS.md
file	AGENT_GUIDE.md	AGENT_GUIDE.md
file	CLAUDE.md	CLAUDE.md
file	CODEX.md	CODEX.md
file	CONTRIBUTING.md	CONTRIBUTING.md
file	COPILOT.md	COPILOT.md
file	CURSOR.md	CURSOR.md
file	LICENSE	LICENSE
file	Makefile	Makefile
file	PROJECT_CONTEXT.md	PROJECT_CONTEXT.md
file	PROMPT_GALLERY.md	PROMPT_GALLERY.md
file	README.md	README.md
file	README_zh-CN.md	README_zh-CN.md
dir	assets	assets
dir	backlot	backlot
file	config.yaml	config.yaml
file	diagram.png	diagram.png
dir	docs	docs
dir	ink-theater	ink-theater
dir	lib	lib
dir	pipeline_defs	pipeline_defs
dir	remotion-composer	remotion-composer
file	render-demo.sh	render-demo.sh
file	render_demo.py	render_demo.py
file	requirements-dev.txt	requirements-dev.txt
file	requirements-gpu.txt	requirements-gpu.txt
file	requirements.txt	requirements.txt
dir	schemas	schemas
dir	scripts	scripts
file	setup.py	setup.py
dir	skills	skills
dir	styles	styles
dir	tests	tests
dir	tools	tools
```
