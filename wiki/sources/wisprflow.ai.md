---
type: source
category: "Media, voice & content"
source_url: https://wisprflow.ai/
tags:
  - voice-to-text
  - ai-dictation
  - productivity
  - cross-platform
  - developer-tools
  - enterprise-security
related:
  - pi.dev
  - elevenlabs.io
  - Starmel-OpenSuperWhisper
product: wisprflow
detail_level: standard
created: 2026-06-08
updated: 2026-07-08
---

Wispr Flow is an AI-powered voice-to-text dictation application that converts natural speech into polished, edited text inside any app on macOS, Windows, iOS, and Android — without requiring per-app integrations. It is notable for its context-aware transcription, AI auto-editing that removes filler words and corrects grammar, and developer-focused features like syntax-smart dictation and file tagging in Cursor and Windsurf IDEs. Wispr recently raised $81M to develop a broader "Voice OS" platform.

_All claims below are sourced from ../../raw/web/wisprflow.ai.md unless otherwise noted._

## What it does

Wispr Flow captures voice input system-wide and transcribes it into any text field the user is currently focused on. Transcription uses advanced AI models trained for context-awareness, understanding the user's writing style over time. A claimed throughput of 220 words per minute (vs. 45 wpm typing) is the core value proposition. The app supports 100+ languages with automatic detection and runs on Mac, Windows, iPhone, and Android with settings synced across devices.

## Key features

- **AI Auto-Edits**: Automatically removes filler words ("um," "uh"), corrects grammar, applies punctuation from pauses and tone
- **Backtrack**: Understands mid-speech corrections without re-dictating the full sentence
- **Personal Dictionary**: Learns industry terms, names, and jargon for accurate transcription
- **Voice Snippets**: Reusable text templates triggered by voice commands (scheduling links, FAQs, code templates)
- **Tone Styling**: Adjusts output style per context — formal, casual, concise, enthusiastic
- **Whisper Mode**: Dictates quietly without triggering noise complaints
- **Privacy Mode**: Zero data retention option for sensitive dictation sessions
- **Contextual Spelling**: Smart capitalization and formatting based on surrounding context
- **Developer Mode**: Syntax-aware dictation for code; file tagging in Cursor and Windsurf; recognizes camelCase, snake_case, and acronyms

## Architecture and concepts

Wispr Flow operates as a system-level overlay rather than an in-app plugin, which is what enables it to work in any application. The AI pipeline takes raw audio, applies speaker-adapted transcription models, then runs a post-processing pass for auto-edits and tone styling before committing text to the focused field.

For teams, shared resources (dictionary, snippets) are synced centrally while usage dashboards expose aggregated metrics only — individual audio and transcripts are not exposed to admins, preserving user privacy.

## Main APIs

Wispr Flow does not expose a public API. Integration happens via IDE extensions (Cursor, Windsurf) and at the OS/keyboard level rather than programmatic API contracts.

## When to use

- **Developers** who write code, documentation, or PR descriptions and want to reduce keyboard burden — file tagging and syntax-aware dictation make it viable for technical content
- **Knowledge workers** in healthcare, legal, or enterprise contexts where HIPAA and SOC 2 compliance are required
- **Accessibility users** who need hands-free operation
- **Teams** needing consistent terminology across voice workflows (shared dictionary, shared snippets)
- **Students** at a discounted rate ($6/month with .edu email, 3 months free)

## Ecosystem

Wispr Flow integrates with 40+ apps including Gmail, Slack, VS Code, Notion, ChatGPT, Figma, Cursor, and Windsurf. Notable enterprise users include Lovable, Mercury, Vercel, Replit, Warp, Rivian, Notion, Amazon, Strava, and Nvidia.

Security certifications: SOC 2 Type II, HIPAA, and ISO 27001.

**Pricing**:
- Flow Basic (free): 2,000 words/week on Mac/Windows; 1,000 words/week on iPhone
- Flow Pro: $12/user/month (annual) or $15/user/month (monthly); unlimited words, command mode, team collaboration
- Flow Enterprise: custom pricing; SSO/SAML, enforced HIPAA, advanced dashboards

Docs are hosted at `docs.wisprflow.ai` and cover Getting Started, Features, Platforms, Developer integrations, Teams, Security, Accessibility, Troubleshooting, and Billing.
