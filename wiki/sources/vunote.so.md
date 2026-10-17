---
type: source
category: "Media, voice & content"
source_url: https://www.vunote.so/
tags:
  - youtube-to-notes
  - timestamped-notes
  - video-transcription
  - cross-video-synthesis
  - study-tools
  - chrome-extension
  - ai-credits
related:
  - meetclaras.com
  - notebooklm.google
  - supadata.ai
product: vunote
detail_level: standard
created: 2026-10-17
updated: 2026-10-17
---

Vunote is a YouTube-to-notes product for students, researchers, and professionals: import videos, playlists, or audio into project workspaces, capture timestamped notes and transcripts while watching, then turn that material into mindmaps, recall cards, quizzes, AI research reports, and project-scoped chat. It sits in the same end-user video-knowledge niche as [[meetclaras.com]], with stronger multi-video project synthesis and study tooling, versus [[supadata.ai]]'s developer transcript API and [[notebooklm.google]]'s broader multi-source research notebooks.

_All claims below are sourced from ../../raw/web/vunote.so.md unless otherwise noted._

## What it does

Vunote turns YouTube (and uploaded video/audio) into organized learning workspaces. The core loop is three steps: add videos and audio (URLs, playlists, or file drops), get smart timestamped notes and transcripts as you watch, then search, mindmap, generate recall cards or reports, and chat against the same notes. A Chrome extension adds a YouTube side panel for timestamped notes, chapter thumbnails, and one-click sync into a Vunote project. Help docs frame a **project** as the container for a course, campaign, or research thread — holding videos, structured notes, AI chat context, and generated documents.

## Key features

- **YouTube & playlists** — paste a video or playlist into a learning workspace; playlist import supports progress with pause/resume (up to 100 videos in recent changelog).
- **Smart timestamped notes** — every note locks to the playhead; jump back in the player or workspace.
- **Transcripts & search** — searchable notes and transcripts so you do not rewatch hours for one idea; downloads as TXT, SRT, or PDF.
- **Multi-video / cross-video work** — Board insights, project-scoped AI Chat, and Document Studio summaries/study guides across sources in one project.
- **Mindmaps, quizzes, flashcards, Visual tab** — study modes beside Notes, best after AI notes/transcript exist.
- **AI research reports** — select notes and generate a structured report to refine and export (Word, PDF, Markdown, JSON depending on plan).
- **AI chat with notes** — questions grounded in notes and transcripts.
- **Chrome extension** — YouTube-only side panel: timestamped notes, chapters, sync to Vunote; free to install.
- **AI credit system** — credits for transcription, AI-structured notes, chat, Document Studio, and advanced insights; watching and manual notes are free. Plans: Free (~500 credits), Pro $9/mo (3,000), Plus $29/mo (12,000), Ultra $49/mo (60,000); credit packs available.

## Architecture and concepts

**Transcript pipeline (product write-up):** import YouTube URL → extract/chunk audio → Whisper transcribes chunks in parallel → stitch with overlap detection → optional AssemblyAI speaker diarisation → store with per-segment timestamps. Status in Workspace shows queued / running / completed / needs attention (e.g. missing captions).

**Summarisation pipeline:** transcript → semantic section chunks → per-section summaries → merge → final coherence pass, aimed at long videos.

**Model stack (as published):** Whisper / AssemblyAI for transcription; GPT-4 Turbo for summaries and project reports (128k context); GPT-4 + RAG for AI Chat; GPT-4 Vision for frame analysis; GPT-4 + custom prompts for insight extraction. Ultra plan marketing mentions advanced models (GPT-5, Claude Opus).

**Credits vs free surface:** transcription, AI notes/study generation, chat, Document Studio, and advanced insights consume credits; watching, hand-edited notes, browsing, and exporting already-generated content do not. Failed transcription jobs refund reserved credits (changelog v1.1.1).

## Main APIs

No public developer API is documented on the marketing/help surface captured here. Ultra plan lists **API access** as a plan feature. Product entry points are the web app (`app.vunote.so` / get-started), the Chrome extension page, and help at `/help` (Getting started, Workspace & notes, AI Chat & documents, Plans & billing). Exports include Word, PDF, Markdown, and on higher plans JSON; transcript download formats include TXT, SRT, PDF.

## When to use

Use Vunote when the primary input is YouTube lectures, interviews, or playlists and you want a **project workspace** with timestamped notes, transcripts, cross-video synthesis, and study artifacts (mindmap/quiz/flashcards/reports) — not just a one-shot summary. Prefer [[meetclaras.com]] for lighter instant transcript + Q&A on a single video; [[notebooklm.google]] when sources mix PDFs, Docs, and video into Gemini-grounded notebooks; [[supadata.ai]] when you need a transcript/metadata API or MCP tools inside agent pipelines rather than a student/researcher UI.

## Ecosystem

- Competes in the YouTube-to-notes market with NoteGPT, ScreenApp, Eightify, Mindgrasp, and others (covered in Vunote's own comparison blog posts).
- Transcription providers referenced: OpenAI Whisper and AssemblyAI.
- Planned/mentioned integrations: Notion and Google Docs export (blog "upcoming").
- Chrome Web Store extension for YouTube-only capture; llms.txt at `https://vunote.so/llms.txt` for agent/crawler discovery.
