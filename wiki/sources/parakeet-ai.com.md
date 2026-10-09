---
type: source
category: "Business, career & learning"
source_url: https://www.parakeet-ai.com/
tags:
  - real-time-ai-copilot
  - interview-assistant
  - screen-share-invisibility
  - live-speech-transcription
  - coding-call-support
  - credit-based-pricing
  - job-search-tooling
related:
  - santifer-career-ops
product: parakeet-ai
detail_level: standard
created: 2026-10-09
updated: 2026-10-09
---

ParakeetAI is a consumer SaaS "real-time AI interview assistant": a desktop/web/mobile app that listens to a live call (job interviews, sales calls, client meetings, or exams), transcribes speech, detects questions as they're asked, and surfaces AI-generated answers — including live code-reading and talk-through for technical/coding interviews — while the call is still happening. It markets itself as the "No. 1 Viral App" and "#1 AI Interview Assistant on SimilarWeb," claiming 1.5M+ users and a 4.86 rating from 340K+ reviews. For this wiki it's a notable example of an LLM-powered, latency-sensitive "live copilot" product built around undetectability rather than developer tooling or APIs.

_All claims below are sourced from ../../raw/web/parakeet-ai.com.md unless otherwise noted._

## What it does

ParakeetAI runs during a live call (via desktop app, browser, or mobile) and continuously transcribes the conversation with a stated "state-of-the-art" speech-recognition model, detects questions in real time, and generates an answer using a user-selected LLM. A session can be an "Interview" (uses an uploaded CV/resume) or a "Regular call" (meetings, sales calls, exams) and supports free-text instructions, uploaded documents (briefs, playbooks, past notes), and manual typed messages sent mid-call. It also auto-detects when a supported meeting platform (Zoom, Microsoft Teams, Google Meet, Webex, Lark/Feishu, Amazon Chime) starts and offers to join, and produces post-call AI Notes (summary, extracted questions, next steps) plus a saved transcript.

## Key features

- **Full coding support** — reads code shared on screen during technical interviews, suggests solutions, and explains the approach live, not just answers to spoken questions
- **Auto Answer + manual Answer/Chat controls** — a session view with live transcript, an "Auto Answer" toggle, a manual message box, and a screenshot action
- **Multi-model choice** — model dropdown spanning "several Gemini, GPT, and Claude models" with a fast default, user-selectable per session (renamed/retired models are auto-mapped to a current replacement, e.g. the FAQ notes Claude 4.5 Sonnet now runs as "Claude Sonnet 5")
- **50+ language support** — single-language-at-a-time live transcription, switchable mid-call via the session language setting
- **Cross-platform delivery** — native desktop app (Windows/macOS), browser (desktop Chrome required for live sessions; also the Linux path), and a mobile-optimized web app (no native iOS/Android app yet, per the FAQ)
- **Phone-call support** — works over Google Voice via a browser session
- **Bundled "Prepare" tools** — Question Bank (real interview questions by company, ranked by frequency), Mock Interviews (practice against an AI interviewer, first mock free), Resume Maker (role-tailored resumes), and Headshots (AI-generated studio-style headshots from one photo)

## Architecture and concepts

The product's defining technical claim is **screen-share and process-level invisibility**: the landing page lists five specific invisibility guarantees — invisible on screen share, invisible in the Dock, invisible in Activity Monitor (no visible process name/icon), invisible to tab-switch detection, and no cursor change on hover/click — and states these are "checked" against eight specific platforms (Zoom, Microsoft Teams, Google Meet, Webex, Lark/Feishu, Amazon Chime, CoderPad, HackerRank), each marked "Verified." Session state (transcript, notes, documents) persists across a dashboard-style "Workspace" with Call Sessions (Live/Ended/Ready-to-start), Resumes, and Documents areas, and sessions can be resumed or reviewed after the call ends.

## Main APIs

No public API, SDK, or developer integration surface was found in this capture — ParakeetAI is an end-user web/desktop/mobile application with a Sign-in-gated dashboard (`/auth/signin`), not a platform for third-party builders. There is no companion GitHub repository and no `llms.txt`/docs site was discovered (see Fetch log note in the raw capture) — the product is closed-source.

## When to use

ParakeetAI targets individuals preparing for or actively doing a live, high-stakes spoken conversation — job interviews (including live-coding rounds), sales calls, client meetings, or online exams — who want a real-time answer prompt without the other party noticing. It is explicitly not a static interview-prep content library like [[santifer-career-ops]] (which automates the *search and application* side of a job hunt via CLI agents); ParakeetAI instead automates *in-the-moment* performance during the call itself, with a bundled set of adjacent prep tools (question bank, mock interviews, resume, headshots) as a secondary offering.

## Ecosystem

ParakeetAI is built by "ParakeetAI d.o.o." and cross-links a sibling consumer product ("Kismo," at kismo.app) as "our other projects" in the footer. It uses credit- and subscription-based pricing (per-session credits, an "Unlimited" monthly/yearly plan, and an à la carte "Custom" tier for the Prepare tools only) rather than developer/API pricing. The landing page frames legitimate use explicitly around permitted contexts (sales calls, internal meetings, mock practice, language study) and states it honors employer-submitted blocklist requests — a notable self-imposed ethical/compliance stance for a tool whose core feature is call-time answer injection designed to evade detection.
