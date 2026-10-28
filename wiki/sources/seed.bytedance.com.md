---
type: source
category: "Media, voice & content"
source_url: https://seed.bytedance.com/en/seedance2_5
tags:
  - seedance
  - video-generation
  - multimodal-reference
  - audio-video-joint
  - bytedance-seed
  - modelark-api
  - clay-render-control
  - long-form-storytelling
related:
  - higgsfield.ai
  - kie.ai
  - elevenlabs.io
  - storytold
product: seedance
detail_level: standard
created: 2026-10-20
updated: 2026-10-28
---

ByteDance Seed's Seedance 2.5 product page covers a next-generation audio-video joint generation model aimed at 30-second storytelling with multimodal reference control and professional editing. For this wiki it matters as the primary vendor surface for a model already appearing in aggregator catalogs ([[higgsfield.ai]], [[kie.ai]]): Jimeng / Doubao product access plus BytePlus ModelArk API (`dreamina-seedance-2-5-260628`) for agent and app builders who need controllable long-form video generation.

_All claims below are sourced from ../../raw/web/seed.bytedance.com.md unless otherwise noted._

## What it does

Seedance 2.5 generates synchronized audio-video clips from text and multimodal references. Building on Seedance 2.0's unified multimodal joint-generation architecture, 2.5 focuses on foundational generation plus reference-based generation: single-pass clips up to 30 seconds (up from 15), multi-round extension for multi-minute narratives, up to 50 reference assets per request (30 images, 10 videos, 10 audio), and timestamp-level editing (green screen, camera perspective, reference-based edits). The Seed site positions it under GenMedia alongside Seedream (image), SeedRealtime (full-duplex AV interaction), and Seed Audio.

## Key features

- **30-second single-pass generation with multi-round extension** — longer coherent stories with improved shot transitions, subject stability, and audiovisual sync; extension preserves characters, environment, and pacing.
- **Omni multimodal reference** — up to 30 images, 10 videos, and 10 audio clips in one pass; clay-render (white-model) control for blocking, camera paths, and physically grounded lighting; motion and creative referencing beyond simple motion transfer.
- **Timestamp and professional editing** — prompt-time and post-generation edits at timestamp granularity; green-screen background replacement with environment-aware subject response; camera-perspective and reference-based editing for film/ads workflows.
- **Native multilingual output** — ModelArk docs list 11 languages (Chinese, English, Spanish, Indonesian, Malay, Thai, Arabic, Portuguese, Vietnamese, Japanese, Korean).
- **Draft mode and MOV output** — draft mode on 2.5; MOV with H.264 / yuv444p / PCM for higher color fidelity in edit/extend pipelines.
- **Task types** — text-to-video; first-frame / first-last-frame; omni reference-to-video with subtasks `auto` / `edit` / `extend` via `omni_reference_task_type`.

## Architecture and concepts

Seedance sits in ByteDance Seed's GenMedia line on `seed.bytedance.com`, with consumer surfaces (Jimeng AI, Doubao Pro) and a developer path through **BytePlus ModelArk**. The model classifies tasks from assets + prompt intent; edit/extend impose hard constraints (`ratio=adaptive`, `duration=-1`, reference video 4–30s) and can fail asynchronously with `InvalidParameter.TaskTypeConstraint` or `InvalidParameter.TaskTypeMismatch` if parameters and prompt intent disagree. Output resolutions include 480p/720p (8-bit) and 1080p (10-bit on 2.5). Sibling Seed models on the same site (Seed2.1 agents, Seedream 5.0 Pro, SeedRealtime, Seed Audio 1.0, Seed GR-RL/GR-3 robotics, Protenix) share branding but are separate product pages.

## Main APIs

- **Model ID** — `dreamina-seedance-2-5-260628` on BytePlus ModelArk; family also includes `dreamina-seedance-2-0-*` and older `seedance-1-*` IDs (1.5 Pro retiring).
- **Create video generation task** — asynchronous ModelArk API; Python SDK sample flow uses `ARK_API_KEY`, polls status (~30s), returns video URL. Docs: `docs.byteplus.com/en/docs/ModelArk/seedance-2-5` (+ prompt guide).
- **Playground** — `ai.byteplus.com/en/playground/model/gen_video?model=dreamina-seedance-2-5-260628`.
- **Resource packs** — activation tied to purchased Dreamina Seedance 2.5 series quota on BytePlus.

## When to use

- Agent or app pipelines that need **long-form, reference-controlled video** (ads, education explainers, synthetic data) rather than short clip generators.
- Workflows requiring **edit/extend with timestamp control**, green screen, or clay-render blocking instead of one-shot text-to-video only.
- Teams already on **BytePlus ModelArk** or Chinese product surfaces (Jimeng, Doubao) who want the first-party Seedance stack rather than only third-party resellers.
- Prefer aggregators like [[higgsfield.ai]] / [[kie.ai]] when you need multi-vendor model switching; use this source when you need Seedance-specific capabilities and ModelArk IDs.

## Ecosystem

Distributed via Jimeng AI, Doubao Pro, Dreamina creative workspace, CapCut-adjacent Seed products, and BytePlus ModelArk / AI Playground. Third-party platforms (e.g. Higgsfield model IDs like `bytedance/seedance/v1/pro/image-to-video`, [[kie.ai|Kie.ai]] Seedance listings) already expose earlier Seedance versions to agent builders. No public companion GitHub repo was linked from the Seedance 2.5 pages at ingest. Contact: `seed.feedback@bytedance.com`.
