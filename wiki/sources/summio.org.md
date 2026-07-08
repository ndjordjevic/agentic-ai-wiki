---
type: source
source_url: https://summio.org/
tags:
  - ai-reading-companion
  - source-grounded-rag
  - book-summaries
  - spaced-repetition
  - document-chat
  - pdf-ocr
  - youtube-summarization
  - consumer-ios-app
related:
  - teng-lin-notebooklm-py
  - reseek.net
  - firecrawl.dev
  - deepwiki.com
  - supermemory.ai
product: summio
detail_level: standard
created: 2026-07-08
updated: 2026-07-08
---

Summio is an AI reading companion for iPhone (iOS 18+) that turns books, YouTube videos, long articles, and PDFs into structured editorial summaries at four depth levels — then lets users chat with the full source text, listen to audio editions, and retain ideas via spaced-repetition flashcards. Unlike catalogue-locked apps like Blinkist, it accepts any source the user points at (100,000+ book catalogue plus arbitrary URLs and uploads), grounds every claim in cited passages using RAG, and ships in 27 interface languages with Premium ($39.99/year) and Max ($79.99/year) tiers billed through Apple's App Store.

_All claims below are sourced from ../../raw/web/summio.org.md unless otherwise noted._

## What it does

Summio compresses long-form content into chaptered editorial editions — quotes, key ideas, glossary, takeaways, and source citations — at user-selected depth (short, medium, long, or detailed). It supports four source types: books (title/author/ISBN search), YouTube (any video, lecture, podcast, or playlist URL with timestamps preserved), articles (any long-form web link), and PDFs (upload with automatic OCR for scanned documents). The app is iPhone/iPad only at launch; Sign in with Apple is the sole authentication method.

Beyond one-shot summaries, Summio offers four "instruments": structured **Summary** editions, **Dialogue** chat grounded in the full source (not just the summary), **Listen** audio narration chapter-by-chapter, and **Companion** spaced-recall drills and nudges from saved material. Saved editions sync to a searchable personal library with offline re-read support (generation requires cloud connectivity).

## Key features

- **Four depth levels** — short (triage), medium (comprehension), long, and detailed (study-grade with chapters, quotes, glossary, takeaways)
- **Source-grounded RAG chat** — ask any saved book, video, article, or PDF questions; answers cite specific passages; claims without grounding are refused
- **Multi-source ingestion** — books via 100,000+ catalogue or PDF upload; YouTube via URL; articles via link; PDFs with automatic OCR
- **Audio summaries** — natural narration per chapter for commute listening; YouTube MP3 export on Premium
- **Spaced repetition** — flashcards and recall prompts generated from saved key ideas, glossary terms, and pull quotes
- **27 interface languages** — summaries can be generated in the user's preferred language regardless of source language (Max tier unlocks all languages and five tones of voice: professional, friendly, succinct, story-driven, scholarly)
- **Personal library** — searchable, offline-readable saved editions; export collections as PDF or EPUB; public and private collections (Premium: 20 public + 5 private)
- **No dark patterns** — no trial traps or hidden renewals; one-tap cancel via App Store Settings

## Architecture and concepts

Summio's core technical pattern is **retrieval-augmented generation (RAG)** for both summary generation and chat: the system retrieves relevant passages from the source document, passes them as context to the LLM, and enforces a source-grounding policy — if a claim cannot be tied to a passage, it is not printed. Chat operates on the **full source text**, not only the generated summary layer, keeping follow-up questions anchored to the original material.

The backend stack (from privacy disclosures) uses **Supabase** for database/storage, **Cloudflare** for hosting/edge, **Firebase** for authentication and analytics, **OpenAI** and **Google Gemini** for AI summary and chat processing, **OneSignal** for push notifications, and **AppsFlyer** (with Apple SKAdNetwork, Meta, TikTok) for marketing attribution behind App Tracking Transparency consent. User content is not used to train AI models. Subscriptions run through Apple StoreKit 2.

Content processing pipelines differ by source: books resolve via catalogue/ISBN lookup; YouTube fetches transcripts; articles condense from fetched web content; PDFs run OCR when needed before summarization. Each output is a structured editorial object (chapters, pull quotes, glossary, takeaways) rather than a flat abstract.

## Main APIs

Summio is a closed consumer iOS app with no public developer API, MCP server, or CLI. Integration surfaces are limited to the mobile app and marketing/support web pages (`summio.org`). Programmatic access to similar grounded-document workflows in this wiki is available via [[teng-lin-notebooklm-py]] (NotebookLM automation) or custom RAG stacks using ingestion tools like [[firecrawl.dev]].

## When to use

Summio fits readers who want to triage many books, lectures, articles, or PDFs quickly on iPhone — decide what deserves full attention, retain key ideas via spaced repetition, and chat with sources using cited answers. It is strongest for personal knowledge consumption on iOS, not for building agent pipelines or team workflows. Operators building agentic document-analysis systems should compare [[teng-lin-notebooklm-py]], [[reseek.net]], or self-hosted RAG instead; Summio is the end-user reading product, not infrastructure.

Choose Premium for regular reading (20 summaries/month, depth up to "long"); Max for power readers (45 summaries/month, "detailed" depth, all languages and tones). Free tier covers limited monthly summaries across all four source types.

## Ecosystem

Summio positions against **Blinkist**, **Headway**, **Shortform**, and one-shot **ChatGPT/Claude PDF uploads** — emphasizing source-agnostic input, deeper structure, persistent library, and citation-grounded chat versus catalogue-only or ephemeral assistant sessions. Adjacent agentic-wiki sources: [[teng-lin-notebooklm-py]] (programmatic grounded research notebooks), [[reseek.net]] (multi-format personal knowledge capture with MCP), [[firecrawl.dev]] (web-to-markdown for agent ingestion), [[deepwiki.com]] (AI-generated repo wikis), and [[supermemory.ai]] (persistent memory for agents). Summio publishes SEO glossary content on RAG, spaced repetition, and PDF OCR that explicitly describes its grounding architecture.
