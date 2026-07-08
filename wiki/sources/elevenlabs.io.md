---
type: source
source_url: https://elevenlabs.io/
tags:
  - text-to-speech
  - speech-to-text
  - voice-agents
  - conversational-ai
  - voice-cloning
  - multimodal-audio
  - llm-integration
  - api-platform
related:
  - developers.openai.com
  - browser-use.com
  - wisprflow.ai
  - hermes-agent.nousresearch.com
  - strandsagents.com
  - crafterq.ai
product: elevenlabs
detail_level: standard
created: 2026-07-06
updated: 2026-07-08
---

ElevenLabs is an AI research and product company (launched January 2023) building foundational audio models and three integrated platforms: **ElevenCreative** for no-code speech, music, image, and video production; **ElevenAgents** for deploying omnichannel voice and chat agents with testing, guardrails, and analytics; and **ElevenAPI** exposing TTS, STT, voice cloning, music, dubbing, and sound effects via HTTP/WebSocket with official Python and Node.js SDKs. It matters for agentic AI because ElevenAgents wires natively to OpenAI, Anthropic, Google, and custom LLMs with backup cascading, tool calling, knowledge-base RAG, and telephony integrations — a full voice layer for autonomous customer-facing agents.

_All claims below are sourced from ../../raw/web/elevenlabs.io.md unless otherwise noted._

## What it does

ElevenLabs provides AI voice infrastructure spanning generation (text-to-speech, music, sound effects, dubbing), recognition (speech-to-text with diarization and timestamps), voice design/cloning, and conversational agents. Users can work through a browser studio (ElevenCreative), an agent builder with visual workflows (ElevenAgents), or direct API/SDK integration (ElevenAPI). A fourth offering, **Reception AI**, is a ready-to-deploy AI phone receptionist for SMB appointment booking. Credits are the shared consumption unit across products (TTS charged per character; other operations per second of audio).

## Key features

- **ElevenCreative**: Studio editor for audiobooks/podcasts/voiceovers; 10,000+ voice library; instant and professional voice cloning; music generation on licensed data; SFX; image and video generation (Veo, Sora, Wan, Kling, Seedance); Productions for multilingual dubbing; Flows workflow builder (Mar 2026)
- **ElevenAgents**: Multimodal agents across phone, chat, email, WhatsApp; visual workflow builder; knowledge-base RAG; tool/API integrations; guardrails and compliance rules; simulated testing and A/B experiments; resolution-rate analytics; Expressive Mode for customer conversations (Feb 2026); HIPAA mode and EU/US/IN data residency
- **ElevenAPI**: REST + WebSocket APIs for TTS, STT, voice changer, music, dubbing, audio isolation, webhooks; regional API servers (`api.elevenlabs.io`, US/EU/IN residency endpoints); character-cost tracking via response headers
- **Models**: `eleven_v3` (most expressive, 70+ languages); `eleven_multilingual_v2` (consistent long-form); `eleven_flash_v2_5` (~75ms latency); Scribe v2 (batch STT, 90+ languages, speaker diarization); Scribe v2 Realtime (~150ms); Eleven Music / Music v2; Dubbing v2 (emotion-preserving cross-language dubbing)
- **LLM integration (agents)**: Native support for OpenAI GPT-5.x/4.x, Anthropic Claude 4.x/Opus 4.7, Google Gemini 2.5/3.x, ElevenLabs Qwen models; custom LLM endpoints; configurable backup LLM cascading; temperature, thinking budget, and reasoning effort controls
- **Developer tooling**: `pip install elevenlabs`, `npm install @elevenlabs/elevenlabs-js`; ElevenLabs UI component library (shadcn-based); React, Swift, Kotlin, React Native SDKs for agents; SIP trunk, Twilio, and batch-call telephony integrations
- **Safety**: Prohibited Use Policy, KYC/KYB verification, content moderation, C2PA provenance/watermarking, public AI-audio classifier, SOC 2 / GDPR / HIPAA compliance portal

## Architecture and concepts

ElevenAgents coordinates four core components: a fine-tuned ASR model for speech recognition, the operator's chosen LLM (or custom endpoint), a low-latency TTS model across 5,000+ voices and 70+ languages, and a proprietary turn-taking model for conversation timing. Agents are configured via dashboard, developer toolkit, or visual workflow builder, then deployed across telephony (SIP, Twilio), web widgets, and mobile SDKs. WebSocket APIs support streaming TTS (partial text input with alignment) and realtime STT (chunked audio with VAD-based commit). Pages support `Accept: text/markdown` for LLM-friendly fetches; full docs also ship as flat `llms-full.txt`.

## Main APIs

| API | Endpoint pattern | Notes |
|---|---|---|
| Text to Speech | `POST /v1/text-to-speech/{voice_id}` | Streaming HTTP + WebSocket `stream-input`; models: `eleven_v3`, `eleven_multilingual_v2`, `eleven_flash_v2_5` |
| Speech to Text | `POST /v1/speech-to-text` | Scribe v2 batch; WebSocket `/v1/speech-to-text/realtime` for streaming |
| Voices | `/v1/voices/*` | Clone (PVC), design from prompt, library browse |
| Music | `/v1/music/*` | Composition plans from natural-language prompts |
| Sound Effects | `/v1/text-to-sound-effects/convert` | Text-to-SFX generation |
| Dubbing | `/v1/dubbing/*` | Cross-language re-voicing |
| Agents | ElevenAgents platform + WebSocket | Configure LLM, tools, knowledge base, telephony |
| Webhooks | `/v1/webhooks` | Event-driven platform integration |

SDK example (Node.js TTS):

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";
const client = new ElevenLabsClient({ apiKey: "YOUR_API_KEY" });
await client.textToSpeech.convert("JBFqnCBsd6RMkjVDRZzb", {
  outputFormat: "mp3_44100_128",
  text: "The first move is what sets everything in motion.",
  modelId: "eleven_multilingual_v2",
});
```

## When to use

- **Voice-enabled customer agents** needing phone/chat/WhatsApp deployment with testing, analytics, guardrails, and multi-LLM failover — ElevenAgents is purpose-built vs. bolting TTS onto a text agent framework
- **Content production at scale** — audiobooks, ads, localization/dubbing, podcast voiceovers, game character voices via ElevenCreative studio or API
- **Low-latency conversational TTS** — Flash v2.5 (~75ms) or realtime Scribe for live agent pipelines where latency dominates UX
- **Multilingual voice** — 70+ TTS languages, 90+ STT languages, dubbing with emotion preservation (Dubbing v2)
- **Developer embedding** — when you need production voice APIs with regional residency, HIPAA options, and official SDKs rather than wrapping open models yourself

## Ecosystem

Enterprise customers include Twilio, Disney, Nvidia, Meta, Salesforce, Deliveroo, Meesho, and Deutsche Telekom. ElevenAgents integrates with major LLM providers (OpenAI, Anthropic, Google) and telephony (Twilio native, SIP trunking). The ElevenLabs UI library (`ui.elevenlabs.io`) provides shadcn-based React components for audio and agent apps. Pricing tiers from Free through Business with pay-as-you-go credits; Enterprise adds custom SLAs, data residency, and HIPAA. Docs at `elevenlabs.io/docs` with `llms.txt` and `llms-full.txt` for agent consumption. Compare voice-input productivity tools like [[wisprflow.ai]], general agent frameworks ([[strandsagents.com]], [[crewai.com]]), OpenAI's Realtime/Agents path in [[developers.openai.com]], and browser-automation agents like [[browser-use.com]] — ElevenLabs is the specialized voice/audio + voice-agent layer rather than a general coding harness.
