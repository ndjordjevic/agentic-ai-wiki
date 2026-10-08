---
type: source
category: "Media, voice & content"
source_url: https://github.com/storytold
tags:
  - ai-image-generation
  - ai-video-generation
  - creative-ide
  - rust
  - open-source-adobe-clones
  - 3d-compositing
  - model-orchestration
product: storytold
detail_level: standard
related:
  - higgsfield.ai
  - kie.ai
  - open-design.ai
created: 2026-10-08
updated: 2026-10-08
---

Storytold is the GitHub organization behind **ArtCraft**, an open-source "IDE for interactive AI image and video creation," plus a growing family of standalone open-source "Crafting Apps" — clean-room Rust reimplementations of well-known Adobe and Microsoft creative/productivity tools (Photoshop, Premiere, Lightroom, Acrobat, Illustrator, Word, PowerPoint, Excel, AutoCAD, Pro Tools), several tagged `ai` on GitHub. The org has 41 public repos, 9,466 followers, and two breakout projects by stars: **photocraft** (19.5k★, Photoshop clone) and **artcraft** itself (5.3k★). For this wiki, it's notable as a model-orchestration IDE for creatives — letting users choose and combine AI image/video models inside a visual, scene-based workflow — rather than a single-purpose generation API.

_All claims below are sourced from ../../raw/web/storytold.md unless otherwise noted._

## What it does

ArtCraft positions itself as "the IDE for artists": a desktop app for composing AI-generated image and video content in 2D and 3D, where users stage scenes, place virtual actors/props, and then choose which generation model to apply, rather than iterating purely through text prompts. The broader Storytold org packages this flagship app alongside a dozen-plus separately open-sourced "Crafting Apps" — each a clean-room Rust reimplementation of a specific proprietary creative or office tool (Photoshop → photocraft, Premiere → filmcraft, Lightroom → lightcraft, Acrobat → pdfcraft, Illustrator → vectorcraft, Word → wordcraft, PowerPoint → deckcraft, Excel → gridcraft, AutoCAD → cadcraft, Pro Tools → soundcraft), plus supporting repos (`artcraft-services`, `artcraftx`, `craft-fonts`).

## Key features

- **Model orchestration, not a single model** — Text to Image and Prompted Image Editing let users pick from a range of image models (the README names Nano Banana Pro and GPT Image as examples) rather than locking into one provider
- **Scene-based composition** — Image to Location (consistent environments across shots), 3D Image Compositing (layered backdrops/foregrounds/props with depth), 2D Image Compositing (layers, background removal, drawing tools), and Image to 3D Mesh (turn a 2D image into a positionable 3D object)
- **Character control** — Character Posing and Character Identity Transfer (a posed mannequin guides a character's placement and pose before generation), aimed at precise, repeatable results rather than one-off prompt luck
- **Scene Blocking with Kitbashing** — combine 3D asset kits to control camera angles, object placement, and depth
- **Mixed Asset Crafting** — combine image cutouts, 3D worlds, and meshes in one scene
- **A parallel suite of open-source "Crafting Apps"** — full clean-room reimplementations of major Adobe/Microsoft tools in pure Rust, independently popular (photocraft alone has nearly 4x ArtCraft's own star count)

## Architecture and concepts

ArtCraft is written in Rust and built around a visual canvas/scene model: 2D layers and 3D scene elements (actors, props, meshes, cameras) are staged before a generation model is invoked, so the model receives a precisely composed input rather than a bare text prompt. This "build the scene before you generate it" philosophy is the project's stated differentiator from prompt-only AI image/video tools. The Crafting Apps are architecturally separate repositories (not plugins within ArtCraft) sharing the "clean-room reimplementation in pure Rust" design pattern and, per their GitHub topics, several (photocraft in particular) carry their own AI-assisted features (e.g. `adobe-photoshop-2026-ai`) independent of ArtCraft's model orchestration.

## Main APIs

No public API or SDK surface was found in these captures beyond the desktop app itself and its companion Crafting Apps; distribution is via downloadable builds from getartcraft.com and GitHub releases, with build-from-source instructions in each repo's `_docs/dev_setup.md`. `artcraft-services` (191★) is listed as backend/web-frontend infrastructure supporting the apps, suggesting a hosted component exists, but no documented external API was captured.

## When to use

ArtCraft fits creatives (filmmakers, designers, illustrators) who want fine-grained compositional control over AI-generated image/video output — camera placement, character identity, multi-shot environment consistency — without being limited to a single model vendor's prompt box. It's less relevant for developers wanting a programmatic generation API (compare [[kie.ai]] for a unified multimodal gateway, or [[higgsfield.ai]] for agent/MCP-oriented video generation) or no-code web-based design tools (compare [[open-design.ai]]). The sibling Crafting Apps are independently useful as open-source, offline-capable replacements for specific proprietary creative/office software, with or without any AI component.

## Ecosystem

Storytold publishes its work entirely on GitHub under permissive-looking but custom ("Other"/NOASSERTION) licensing, with community presence on Discord, YouTube, X, and LinkedIn under the ArtCraft brand. The Crafting Apps ecosystem (photocraft, filmcraft, lightcraft, pdfcraft, vectorcraft, wordcraft, cadcraft, gridcraft, soundcraft, deckcraft, effectcraft, designcraft) gives the org an unusually broad footprint across creative and productivity software categories, all sharing the Rust/clean-room-reimplementation pattern. Related patterns in this wiki: AI image/video generation platforms [[higgsfield.ai]] and [[kie.ai]]; AI-assisted design tooling [[open-design.ai]].
