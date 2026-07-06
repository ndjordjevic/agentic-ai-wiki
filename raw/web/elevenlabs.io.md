# elevenlabs.io
## Fetch log
- Inbox URL: https://elevenlabs.io/
- Final URL: https://elevenlabs.io/
- Fetched: 2026-07-06
- Pages: 9
- Mode: standard

## llms.txt — https://elevenlabs.io/llms.txt
# ElevenLabs

ElevenLabs is an AI research and product company transforming how we interact with technology. We launched in January 2023 with the first human-like AI voice model. Today, we serve millions of users and thousands of businesses across three main platforms. ElevenAgents enables businesses to deliver seamless and intelligent customer experiences, with the integrations, testing, monitoring, and reliability necessary to deploy voice and chat agents at scale. ElevenCreative empowers creators and marketers to generate and edit speech, music, image, and video across 70+ languages. ElevenAPI gives developers access to our leading AI audio foundational models.

## Fetching Markdown Content

Most ElevenLabs pages support a Markdown-optimized response format. When you request a page with the header `Accept: text/markdown`, the server returns a stripped-down Markdown version of the page — no navigation or boilerplate — containing only the essential content. This significantly reduces token usage and improves parsing accuracy.

**To request Markdown content, add this header to your HTTP requests:**

```
Accept: text/markdown
```

**Example (curl):**
```bash
curl -H "Accept: text/markdown" https://elevenlabs.io/text-to-speech
```


Where Markdown responses are available, the server will reply with `Content-Type: text/markdown`. If a page does not support this format, it will fall back to the standard HTML response. The [LLM-optimized full documentation](https://elevenlabs.io/docs/llms-full.txt) is always available as a single flat Markdown file without requiring any special headers.

## Products

### ElevenCreative
- [ElevenCreative overview](https://elevenlabs.io/creative): A single studio for creators to combine voice, music, image, and video. Built for creators, brands, and media companies elevating storytelling and production workflows.
- [Text to Speech](https://elevenlabs.io/text-to-speech): Controllable, expressive speech across 70+ languages. Our models dynamically predict voice characteristics and adapt to content context.
- [Speech to Text](https://elevenlabs.io/speech-to-text): Scribe, our most accurate Speech to Text model, with speaker diarization and character-level timestamps.
- [Voice Library](https://elevenlabs.io/voice-library): Thousands of pre-built voices, plus tools to clone your own voice or design one from a prompt.
- [Voice Cloning](https://elevenlabs.io/voice-cloning): Create a high-fidelity replica of a voice from audio samples. Requires consent verification for cloning public figures.
- [Music](https://elevenlabs.io/music): Studio-quality music from natural language prompts in any genre or style, trained on licensed data and cleared for commercial use.
- [Sound Effects](https://elevenlabs.io/sound-effects): Custom sound effects and ambient audio from text prompts.
- [Productions](https://elevenlabs.io/productions): Translate and re-voice video and audio content across languages while preserving original speaker characteristics.
- [Projects / Studio](https://elevenlabs.io/studio): Create and edit audiobooks, podcasts, and voiceovers in an editor built on all of ElevenLabs' audio research.
- [Video](https://elevenlabs.io/video): Turn ideas into videos using leading models including Veo, Sora, Wan, Kling, and Seedance.
- [Image](https://elevenlabs.io/image): Generate and edit images with leading AI image models.

### ElevenAgents
- [ElevenAgents overview](https://elevenlabs.io/agents): Enterprise platform for AI agents that can talk, type, and take action. Elevate customer experience, empower revenue teams, and streamline internal operations.
- [Conversational AI](https://elevenlabs.io/conversational-ai): Build agents powered by V3, our most expressive text to speech model, with improved turn-taking, natural dialogue, and emotion understanding.
- [Agents Platform](https://elevenlabs.io/docs/eleven-agents/overview): Configure multimodal agents via dashboard, developer toolkit, or visual workflow builder. Deploy across telephony, web, and mobile.
- [LLM Integration](https://elevenlabs.io/docs/eleven-agents/customization/llm): Agents support natively integrated LLMs (OpenAI, Claude, Gemini, and others) plus custom LLM endpoints. Backup LLM cascading is configurable to maintain conversation continuity if a primary model fails.
- [Analytics and Evals](https://elevenlabs.io/docs/eleven-agents/overview): Built-in testing, evaluations, and performance analytics at scale.
- [HIPAA and Data Residency](https://elevenlabs.io/docs/eleven-agents/customization/llm/llm-cascading): HIPAA-compliant mode and EU/US/IN data residency options available.

### ElevenAPI
- [ElevenAPI overview](https://elevenlabs.io/api): Direct API access to ElevenLabs' audio intelligence for developers. HTTP and WebSocket support, official Python and Node.js SDKs. For full API details, see the [LLM-optimized docs](https://elevenlabs.io/docs/llms-full.txt).
- [Text to Speech](https://elevenlabs.io/docs/api-reference/text-to-speech): Convert text to audio using any voice. Supports streaming, multiple output formats, and expressive control.
- [Speech to Text](https://elevenlabs.io/docs/api-reference/speech-to-text): High-accuracy transcription with speaker diarization and character-level timestamps.
- [Voice Cloning](https://elevenlabs.io/docs/api-reference/voices/pvc/create): Programmatically clone voices from audio samples.
- [Voice Design](https://elevenlabs.io/docs/api-reference/voices): Generate novel voices from text prompts or browse the voice library.
- [Voice Changer](https://elevenlabs.io/docs/api-reference/speech-to-speech/convert): Transform audio from one voice to another in real time.
- [Music](https://elevenlabs.io/docs/api-reference/music): Generate studio-quality music from natural language prompts.
- [Sound Effects](https://elevenlabs.io/docs/api-reference/text-to-sound-effects/convert): Generate custom sound effects and ambient audio from text.
- [Audio Isolation](https://elevenlabs.io/docs/api-reference/audio-isolation): Separate voice from background noise.
- [Dubbing](https://elevenlabs.io/docs/api-reference/dubbing): Translate and re-voice audio and video content across languages.
- [Webhooks](https://elevenlabs.io/docs/api-reference/webhooks): Event-driven integration for platform events.
- [API servers](https://api.elevenlabs.io): Global (`api.elevenlabs.io`), US residency (`api.us.elevenlabs.io`), EU residency (`api.eu.residency.elevenlabs.io`), India residency (`api.in.residency.elevenlabs.io`).

## Documentation

- [Full documentation](https://elevenlabs.io/docs/overview/intro): Product guides, API reference, best practices, and integration tutorials.
- [Full documentation (LLM-optimized)](https://elevenlabs.io/docs/llms-full.txt): Complete documentation in a single flat Markdown file — no headers required, always available.
- [Getting started](https://elevenlabs.io/docs/eleven-creative/overview): Quickstart for new users and developers.
- [Python SDK](https://elevenlabs.io/docs/api-reference/introduction): `pip install elevenlabs`
- [Node.js SDK](https://elevenlabs.io/docs/api-reference/introduction): `npm install @elevenlabs/elevenlabs-js`

## Pricing and Plans

- [Pricing](https://elevenlabs.io/pricing): Free tier available. Paid plans (Starter, Creator, Pro, Scale, Business) scale by credit volume and feature access. Creator and above support pay-as-you-go usage-based billing for credits beyond the monthly quota. Enterprise pricing available with custom terms.
- [Enterprise](https://elevenlabs.io/enterprise): Custom contracts, SLAs, data residency, HIPAA compliance, and dedicated support.
- [Data Processing Agreement](https://elevenlabs.io/dpa): GDPR-compliant DPA available for enterprise customers.

## Safety and Trust

ElevenLabs is committed to building the most trusted voice and agents AI platform. Our safety program focuses on preventing, detecting, and responding to abusive use of our models - particularly misuse that could lead to serious harm through deception or exploitation.

- [Prohibited Use Policy](https://elevenlabs.io/use-policy): Our external-facing policy governing acceptable use of ElevenLabs products. Violations may result in feature restrictions or account removal.
- [Safety overview](https://elevenlabs.io/safety): How ElevenLabs approaches responsible AI, including red-teaming, KYC/KYB verification, product safeguards, and monitoring.
- [Compliance portal](https://compliance.elevenlabs.io/): GDPR, EU AI Act, DORA, HIPAA, SOC 2 certifications and compliance documentation.
- [C2PA and watermarking](https://elevenlabs.io/safety): ElevenLabs supports open standards for AI content provenance, including C2PA metadata and watermarking. A public classifier is available to detect content created with ElevenLabs.

## Contact and Support

- [Press inquiries](mailto:press@elevenlabs.io): Media and press contact.
- [Brand assets](https://elevenlabs.io/brand): Official logos, fonts, and brand guidelines.

## Legal

- [Terms of Service](https://elevenlabs.io/terms-of-use): Governs use of ElevenLabs products and services.
- [Privacy Policy](https://elevenlabs.io/privacy-policy): How ElevenLabs handles user data.
- [Data Processing Agreement](https://elevenlabs.io/dpa): For GDPR-compliant enterprise data handling.
- [Service Level Agreement](https://elevenlabs.io/enterprise): Available for enterprise customers upon request, appended to Order Forms.
## Landing page — https://elevenlabs.io/
# Bringing technology to life

## Powering the best enterprises, creators, and developers

From ElevenAgents for customer experience, ElevenCreative for content creation, to the leading AI voice generator.

### Three platforms
- **ElevenCreative** — Generate ultra-realistic speech, videos, music, and sound effects. All-in-one AI editor for podcasts, audiobooks, voiceovers. Ultra-realistic speech across 70+ languages. Music, SFX, Voices (clone/design/10,000+ library), Image & Video (Veo, Wan, Kling, Seedance).
- **ElevenAgents** — Configure, deploy and monitor conversational agents in 70+ languages. Omnichannel (phone, chat, email, WhatsApp). Analytics, Testing, Guardrails, Workflows. Customers: Deliveroo, Meesho, Cars24.
- **ElevenAPI** — Text to Speech API (Eleven Flash ~75ms, Eleven Multilingual, Eleven v3). Speech to Text API (Eleven Scribe 98% accuracy). Music API. Official Python (`elevenlabs`) and Node.js (`@elevenlabs/elevenlabs-js`) SDKs.

### Trusted by
Twilio, Walt Disney Studios, KPN, TVS, Telus Digital, Cisco, Epic Games, Nvidia, Revolut, Meta, Bertelsmann, deliveroo, Chess.com, Deutsche Telekom, meesho, Harvey, Salesforce

### Research timeline
- Eleven Multilingual v2 (Aug 2023) — consistent lifelike TTS
- Eleven Turbo v2 (Nov 2023) — high-quality low-latency TTS
- Eleven Flash v2.5 (Dec 2024) — ultra-low latency TTS
- Scribe (Feb 2025) — original STT, later surpassed by Scribe v2
- Eleven v3 (Jun 2025) — most expressive TTS
- Eleven Music (Aug 2025) — AI music on licensed data
- Scribe v2 Realtime (Nov 2025) — real-time transcription
- Scribe v2 (Jan 2026) — most accurate transcription
- Expressive Mode for Agents (Feb 2026)
- Music v2 (May 2026)
- Dubbing v2 (May 2026)

### Safety
Moderation, Accountability, Provenance (C2PA/watermarking)

### Latest updates (Mar 2026)
- Introducing Flows in ElevenCreative (Mar 11, 2026)
- Introducing ElevenLabs for Government (Feb 11, 2026)
- Introducing Expressive Mode for ElevenAgents (Feb 10, 2026)

## Docs — https://elevenlabs.io/docs/overview/intro
> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# ElevenLabs Documentation

## How ElevenLabs works

ElevenLabs provides AI voice infrastructure: text-to-speech, speech-to-text, voice cloning, conversational agents, and generative audio. You can use it in four ways, suited to different audiences.

**[ElevenCreative](/docs/eleven-creative)** is a no-code web application where creators, producers, and editors generate voiceovers, music, dubs, and studio projects directly in the browser.

**[ElevenAgents](/docs/eleven-agents)** is the platform for designing and operating conversational voice agents, with a visual builder for non-technical users and full programmatic control for developers.

**[ElevenAPI](/docs/eleven-api)** exposes every capability as a REST interface with official Python and TypeScript SDKs, so developers can embed voice into their own applications and workflows.

**[Reception AI](/docs/reception-ai)** is a ready-to-deploy AI phone receptionist for small and medium businesses that answers calls, books appointments, and manages day-to-day operations from a single dashboard.

### Concepts

**Voices** are the speech persona used in audio generation. Each voice has a unique ID — for example, `JBFqnCBsd6RMkjVDRZzb` — that you select in the dashboard or pass in API requests. ElevenLabs maintains a [library of 10,000+ voices](https://elevenlabs.io/app/voice-library). You can also clone a voice from an audio recording or generate one from a text description.

**Models** control the quality, latency, and language coverage of generated audio. [`eleven_v3`](/docs/overview/models) produces the most expressive output across 70+ languages. [`eleven_flash_v2_5`](/docs/overview/models) targets real-time use at \~75ms latency. Each capability — speech-to-text, music, sound effects — has its own dedicated model.

**Credits** are the unit of consumption shared across every product. Text-to-speech costs one credit per character of input text. Other operations are charged per second of audio processed. Credits reset monthly and unused credits roll over for up to two months. See [pricing](https://elevenlabs.io/pricing/api) for a full breakdown.

## Choose your path

<a href="/docs/eleven-creative/overview">
  <img src="https://files.buildwithfern.com/elevenlabs.docs.buildwithfern.com/12097a437e55f60c199946cf59c9528eb8349d110142394833d67fe93b50e68d/assets/images/overview/voice-library-bg.webp" alt="" />

  <h3>
    ElevenCreative
  </h3>

  <p>
    Learn how to use the ElevenCreative platform with step-by-step guides
  </p>
</a>

<a href="/docs/eleven-agents/overview">
  <img src="https://files.buildwithfern.com/elevenlabs.docs.buildwithfern.com/17a81505a62493491ead763b307b1e854825a0da67ab1a1d86b41b57ad87bc73/assets/images/agents/agents-overview-integrate.png" alt="" />

  <h3>
    ElevenAgents
  </h3>

  <p>
    Learn how to build, launch, and scale agents with ElevenLabs
  </p>
</a>

<a href="/docs/eleven-api/quickstart">
  <img src="https://files.buildwithfern.com/elevenlabs.docs.buildwithfern.com/002b2432fa6ab18befc9f1a6e7fadf348f46506a5a5a72a2358ba1e7f92d8ded/assets/images/overview/scribe-code-bg.webp" alt="" />

  <h3>
    ElevenAPI
  </h3>

  <p>
    Learn how to integrate with the ElevenLabs API with examples and tutorials
  </p>
</a>

## Meet the models

Our most emotionally rich, expressive speech synthesis model

Dramatic delivery and performance

70+ languages supported

5,000 character limit

Support for natural multi-speaker dialogue

Lifelike, consistent quality speech synthesis model

Natural-sounding output

29 languages supported

10,000 character limit

Most stable on long-form generations

Our fast, affordable speech synthesis model

Ultra-low latency (\~75ms†)

32 languages supported

40,000 character limit

Faster model, 50% lower price per character for API generations

State-of-the-art speech recognition model

Accurate transcription in 90+ languages

Keyterm prompting, up to 1000 terms

Entity detection, up to 56

Precise word-level timestamps

Speaker diarization, up to 32 speakers

Dynamic audio tagging

Smart language detection

Real-time speech recognition model

Accurate transcription in 90+ languages

Real-time transcription

Low latency (\~150ms†)

Precise word-level timestamps

<a href="/docs/overview/models">
  Explore all
</a>

<small>
  † Excluding application & network latency
</small>

## Browse by capability

Text to Speech

<p>
  Convert text into lifelike speech
</p>

Speech to Text

<p>
  Transcribe spoken audio into text
</p>

Music

<p>
  Generate music from text
</p>

Text to Dialogue

<p>
  Create natural-sounding dialogue from text
</p>

Image & Video

<p>
  Generate images and videos from text
</p>

Voice changer

<p>
  Modify and transform voices
</p>

Voice isolator

<p>
  Isolate voices from background noise
</p>

Dubbing

<p>
  Dub audio and videos seamlessly
</p>

Sound effects

<p>
  Create cinematic sound effects
</p>

Voices

<p>
  Clone and design custom voices
</p>

Voice Remixing

<p>
  Transform and enhance existing voices
</p>

Forced Alignment

<p>
  Align text to audio
</p>

Speech Engine

<p>
  Add voice to anything
</p>

ElevenAgents

<p>
  Deploy intelligent voice agents
</p>
## ElevenAgents overview — https://elevenlabs.io/docs/eleven-agents/overview
> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# ElevenAgents

Agents accomplish tasks through natural dialogue - from quick requests to complex, open-ended workflows. ElevenLabs provides voice-rich, expressive models, developer tools for building multimodal agents, and tools to monitor and evaluate agent performance at scale.

<a href="/docs/eleven-agents/build/overview">
  <img src="https://files.buildwithfern.com/elevenlabs.docs.buildwithfern.com/b01da89ad7994300673d0932d321cd0f53fe727b6210e6c1f00e765e498f8722/assets/images/agents/agents-overview-build.png" alt="" />

  <h3>
    Configure
  </h3>

  <p>
    Configure multimodal agents with our developer toolkit, dashboard, or visual workflow
    builder
  </p>
</a>

<a href="/docs/eleven-agents/integrate/overview">
  <img src="https://files.buildwithfern.com/elevenlabs.docs.buildwithfern.com/17a81505a62493491ead763b307b1e854825a0da67ab1a1d86b41b57ad87bc73/assets/images/agents/agents-overview-integrate.png" alt="" />

  <h3>
    Deploy
  </h3>

  <p>
    Integrate multimodal agents across telephony systems, web, and mobile
  </p>
</a>

<a href="/docs/eleven-agents/operate/overview">
  <img src="https://files.buildwithfern.com/elevenlabs.docs.buildwithfern.com/3790a000d203429c852cd4be74f2635ea41222f31b0edb53ae760c61e4a0f07d/assets/images/agents/agents-overview-operate.png" alt="" />

  <h3>
    Monitor
  </h3>

  <p>
    Evaluate agent performance with built-in testing, evals, and analytics
  </p>
</a>

## Platform capabilities

From design to deployment to optimization, ElevenLabs provides everything you need to build agents at scale.

### Design and configure

| Goal                          | Guide                                                                    | Description                                                            |
| ----------------------------- | ------------------------------------------------------------------------ | ---------------------------------------------------------------------- |
| Create conversation workflows | [Workflows](/docs/eleven-agents/customization/agent-workflows)           | Build multi-step workflows with visual workflow builder                |
| Write system prompts          | [System prompt](/docs/eleven-agents/best-practices/prompting-guide)      | Learn best practices for crafting effective agent prompts              |
| Select language model         | [Models](/docs/eleven-agents/customization/llm)                          | Choose from supported LLMs or bring your own custom model              |
| Control conversation flow     | [Conversation flow](/docs/eleven-agents/customization/conversation-flow) | Configure turn-taking, interruptions, and timeout settings             |
| Configure voice & language    | [Voice & language](/docs/eleven-agents/customization/voice)              | Select from 5k+ voices across 31 languages with customization options  |
| Add knowledge to agent        | [Knowledge base](/docs/eleven-agents/customization/knowledge-base)       | Upload documents and enable RAG for grounded responses                 |
| Connect tools                 | [Tools](/docs/eleven-agents/customization/tools)                         | Enable agents to call clients & APIs to perform actions                |
| Personalize each conversation | [Personalization](/docs/eleven-agents/customization/personalization)     | Use dynamic variables and overrides for per-conversation customization |
| Secure agent access           | [Authentication](/docs/eleven-agents/customization/authentication)       | Implement custom authentication for protected agent access             |

### Connect and deploy

| Goal                        | Guide                                                                             | Description                                                        |
| --------------------------- | --------------------------------------------------------------------------------- | ------------------------------------------------------------------ |
| Build with React components | [ElevenLabs UI](https://ui.elevenlabs.io)                                         | Pre-built components library for audio & agent apps (shadcn-based) |
| Embed widget in website     | [Widget](/docs/eleven-agents/customization/widget)                                | Add a customizable web widget to any website                       |
| Build React web apps        | [React SDK](/docs/eleven-agents/libraries/react)                                  | Voice-enabled React hooks and components                           |
| Build iOS apps              | [Swift SDK](/docs/eleven-agents/libraries/swift)                                  | Native iOS SDK for voice agents                                    |
| Build Android apps          | [Kotlin SDK](/docs/eleven-agents/libraries/kotlin)                                | Native Android SDK for voice agents                                |
| Build React Native apps     | [React Native SDK](/docs/eleven-agents/libraries/react-native)                    | Cross-platform iOS and Android with React Native                   |
| Connect via SIP trunk       | [SIP trunk](/docs/eleven-agents/phone-numbers/sip-trunking)                       | Integrate with existing telephony infrastructure                   |
| Make batch outbound calls   | [Batch calls](/docs/eleven-agents/phone-numbers/batch-calls)                      | Trigger multiple calls programmatically                            |
| Use Twilio integration      | [Twilio](/docs/eleven-agents/phone-numbers/twilio-integration/native-integration) | Native Twilio integration for phone calls                          |
| Build custom integrations   | [WebSocket API](/docs/eleven-agents/libraries/web-sockets)                        | Low-level WebSocket protocol for custom implementations            |
| Receive real-time events    | [Events](/docs/eleven-agents/customization/events)                                | Subscribe to conversation events and updates                       |

### Monitor and optimize

| Goal                         | Guide                                                                                    | Description                                          |
| ---------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------- |
| List users by external ID    | [Users](/docs/eleven-agents/operate/users)                                               | See end users and open their conversations           |
| Search transcripts           | [Searching conversations](/docs/eleven-agents/customization/agent-analysis/smart-search) | Keyword and semantic search in Conversation history  |
| Run A/B tests                | [Experiments](/docs/eleven-agents/operate/experiments)                                   | Test agent configuration changes with live traffic   |
| Test agent behavior          | [Testing](/docs/eleven-agents/customization/agent-testing)                               | Create and run automated tests for your agents       |
| Analyze conversation quality | [Conversation analysis](/docs/eleven-agents/customization/agent-analysis)                | Extract insights and evaluate conversation outcomes  |
| Track metrics & analytics    | [Analytics](/docs/eleven-agents/dashboard)                                               | Monitor performance metrics and conversation history |
| Configure data retention     | [Privacy](/docs/eleven-agents/customization/privacy)                                     | Set retention policies for conversations and audio   |
| Reduce LLM costs             | [Cost optimization](/docs/eleven-agents/customization/llm/optimizing-costs)              | Monitor and optimize language model expenses         |

## Architecture

ElevenAgents coordinates 4 core components:

1. A fine-tuned Speech to Text (ASR) model for speech recognition
2. Your choice of language model or [custom](/docs/eleven-agents/customization/llm/custom-llm) LLM
3. A low-latency Text to Speech (TTS) model across 5k+ voices and 70+ languages
4. A proprietary turn-taking model that handles conversation timing

Build your first agent in 5 minutes
## ElevenCreative overview — https://elevenlabs.io/docs/eleven-creative/overview
> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# ElevenCreative

The ElevenCreative platform transforms text into lifelike audio across 50+ languages with the most advanced voice AI models available. From audiobooks to ads, podcasts to games, create professional voice content at scale with intuitive tools for creators, producers, and developers.

<a href="/docs/eleven-creative/playground/text-to-speech">
  <h3>
    Playground
  </h3>

  <p>
    Test and experiment with text-to-speech, voice changing, and sound effects in real-time
  </p>
</a>

<a href="/docs/eleven-creative/products/studio">
  <h3>
    Products
  </h3>

  <p>
    Purpose-built tools that integrate multiple capabilities into streamlined workflows for
    specific use cases like long-form content, video localization, and music production
  </p>
</a>

<a href="/docs/eleven-creative/voices/voice-library">
  <h3>
    Voices
  </h3>

  <p>
    Access 10,000+ pre-made voices or clone your own with instant or professional voice cloning
  </p>
</a>

## Platform capabilities

ElevenLabs capabilities span synthesis, dubbing, music, sound design, voices, and analytics. Review
the [capabilities overview](/docs/overview/intro#capabilities) for detailed breakdowns, parameters, and
best-fit guidance across every use case.

## Use cases

The ElevenCreative platform powers audio production across industries:

* **Audiobooks & Publishing** - Produce full-length audiobooks with consistent character voices
* **Content Creation** - Generate voiceovers for YouTube, podcasts, and social media
* **Gaming** - Create dynamic character voices and sound effects
* **Film & TV** - Localize content with AI dubbing in 30+ languages
* **Advertising** - Scale ad campaigns globally with multilingual voice AI
* **Education** - Produce engaging e-learning content with natural narration
## API Introduction — https://elevenlabs.io/docs/api-reference/introduction
> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Introduction

## Installation

You can interact with the API through HTTP or Websocket requests from any language, via our official Python bindings or our official Node.js libraries.

To install the official Python bindings, run the following command:

```bash
pip install elevenlabs
```

To install the official Node.js library, run the following command in your Node.js project directory:

```bash
npm install @elevenlabs/elevenlabs-js
```

## Tracking generation costs

Access response headers to retrieve generation metadata including character costs.

```python
from elevenlabs.client import ElevenLabs

client = ElevenLabs(api_key="your_api_key")

# Get raw response with headers
response = client.text_to_speech.with_raw_response.convert(
    text="Hello, world!",
    voice_id="voice_id"
)

# Access character cost from headers
char_cost = response.headers.get("character-cost")

# Optionally store these for debugging
request_id = response.headers.get("request-id")
trace_id = response.headers.get("x-trace-id")

audio_data = response.data
```

```typescript
import { ElevenLabsClient } from '@elevenlabs/elevenlabs-js';

const client = new ElevenLabsClient({ apiKey: 'your_api_key' });

// Get raw response with headers
const { data, rawResponse } = await client.textToSpeech
  .convert('voice_id', {
    text: 'Hello, world!',
    modelId: 'eleven_v3',
  })
  .withRawResponse();

// Access character cost from headers
const charCost = rawResponse.headers.get('character-cost');

// Optionally store these for debugging
const requestId = rawResponse.headers.get('request-id');
const traceId = rawResponse.headers.get('x-trace-id');

const audioData = data;
```

The raw response provides access to:

* Response data - The actual API response content
* HTTP headers - Metadata including character costs and request IDs
## Text to Speech API — https://elevenlabs.io/docs/api-reference/text-to-speech
> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# WebSocket

GET /v1/text-to-speech/{voice_id}/stream-input

The Text-to-Speech WebSockets API is designed to generate audio from partial text input
while ensuring consistency throughout the generated audio. Although highly flexible,
the WebSockets API isn't a one-size-fits-all solution. It's well-suited for scenarios where:
  * The input text is being streamed or generated in chunks.
  * Word-to-audio alignment information is required.

However, it may not be the best choice when:
  * The entire input text is available upfront. Given that the generations are partial,
    some buffering is involved, which could potentially result in slightly higher latency compared
    to a standard HTTP request.
  * You want to quickly experiment or prototype. Working with WebSockets can be harder and more
    complex than using a standard HTTP API, which might slow down rapid development and testing.


Reference: https://elevenlabs.io/docs/api-reference/text-to-speech/v-1-text-to-speech-voice-id-stream-input

## AsyncAPI Specification

```yaml
asyncapi: 2.6.0
info:
  title: V 1 Text To Speech Voice Id Stream Input
  version: subpackage_v1TextToSpeechVoiceIdStreamInput.v1TextToSpeechVoiceIdStreamInput
  description: >
    The Text-to-Speech WebSockets API is designed to generate audio from partial
    text input

    while ensuring consistency throughout the generated audio. Although highly
    flexible,

    the WebSockets API isn't a one-size-fits-all solution. It's well-suited for
    scenarios where:
      * The input text is being streamed or generated in chunks.
      * Word-to-audio alignment information is required.

    However, it may not be the best choice when:
      * The entire input text is available upfront. Given that the generations are partial,
        some buffering is involved, which could potentially result in slightly higher latency compared
        to a standard HTTP request.
      * You want to quickly experiment or prototype. Working with WebSockets can be harder and more
        complex than using a standard HTTP API, which might slow down rapid development and testing.
channels:
  /v1/text-to-speech/{voice_id}/stream-input:
    description: >
      The Text-to-Speech WebSockets API is designed to generate audio from
      partial text input

      while ensuring consistency throughout the generated audio. Although highly
      flexible,

      the WebSockets API isn't a one-size-fits-all solution. It's well-suited
      for scenarios where:
        * The input text is being streamed or generated in chunks.
        * Word-to-audio alignment information is required.

      However, it may not be the best choice when:
        * The entire input text is available upfront. Given that the generations are partial,
          some buffering is involved, which could potentially result in slightly higher latency compared
          to a standard HTTP request.
        * You want to quickly experiment or prototype. Working with WebSockets can be harder and more
          complex than using a standard HTTP API, which might slow down rapid development and testing.
    parameters:
      voice_id:
        description: The unique identifier for the voice to use in the TTS process.
        schema:
          type: string
    bindings:
      ws:
        query:
          type: object
          properties:
            authorization:
              type: string
            single_use_token:
              type: string
            model_id:
              type: string
            language_code:
              type: string
            enable_logging:
              type: boolean
              default: true
            enable_ssml_parsing:
              type: boolean
              default: false
            output_format:
              $ref: >-
                #/components/schemas//v1/text-to-speech/{voice_id}/stream-input_output_format
              default: mp3_44100
            inactivity_timeout:
              type: integer
              default: 20
            sync_alignment:
              type: boolean
              default: false
            auto_mode:
              type: boolean
              default: false
            apply_text_normalization:
              $ref: >-
                #/components/schemas//v1/text-to-speech/{voice_id}/stream-input_apply_text_normalization
              default: auto
            seed:
              type: integer
        headers:
          type: object
          properties:
            xi-api-key:
              type: string
    publish:
      operationId: >-
        subpackage_v1TextToSpeechVoiceIdStreamInput.v1TextToSpeechVoiceIdStreamInput-publish
      summary: subscribe
      description: Receive messages from the WebSocket
      message:
        name: subscribe
        title: subscribe
        description: Receive messages from the WebSocket
        payload:
          $ref: '#/components/schemas/V1TextToSpeechVoiceIdStreamInputSubscribe'
    subscribe:
      operationId: >-
        subpackage_v1TextToSpeechVoiceIdStreamInput.v1TextToSpeechVoiceIdStreamInput-subscribe
      summary: publish
      description: Send messages to the WebSocket
      message:
        name: publish
        title: publish
        description: Send messages to the WebSocket
        payload:
          $ref: '#/components/schemas/V1TextToSpeechVoiceIdStreamInputPublish'
servers:
  Production:
    url: wss://api.elevenlabs.io/
    protocol: wss
    x-default: true
  Production US:
    url: wss://api.us.elevenlabs.io/
    protocol: wss
  Production EU:
    url: wss://api.eu.residency.elevenlabs.io/
    protocol: wss
  Production India:
    url: wss://api.in.residency.elevenlabs.io/
    protocol: wss
  Production Singapore:
    url: wss://api.sg.residency.elevenlabs.io/
    protocol: wss
components:
  schemas:
    /v1/text-to-speech/{voice_id}/stream-input_output_format:
      type: string
      enum:
        - mp3_22050_32
        - mp3_44100_32
        - mp3_44100_64
        - mp3_44100_96
        - mp3_44100_128
        - mp3_44100_192
        - pcm_8000
        - pcm_16000
        - pcm_22050
        - pcm_24000
        - pcm_44100
        - ulaw_8000
        - alaw_8000
        - opus_48000_32
        - opus_48000_64
        - opus_48000_96
        - opus_48000_128
        - opus_48000_192
      description: The output audio format
      title: /v1/text-to-speech/{voice_id}/stream-input_output_format
    /v1/text-to-speech/{voice_id}/stream-input_apply_text_normalization:
      type: string
      enum:
        - auto
        - 'on'
        - 'off'
      default: auto
      description: >-
        This parameter controls text normalization with three modes - 'auto',
        'on', and 'off'. When set to 'auto', the system will automatically
        decide whether to apply text normalization (e.g., spelling out numbers).
        With 'on', text normalization will always be applied, while with 'off',
        it will be skipped. For the 'eleven_flash_v2_5' model, text
        normalization can only be enabled with Enterprise plans. Defaults to
        'auto'.
      title: /v1/text-to-speech/{voice_id}/stream-input_apply_text_normalization
    NormalizedAlignment:
      type: object
      properties:
        charStartTimesMs:
          type: array
          items:
            type: integer
          description: >
            A list of starting times (in milliseconds) for each character in the
            normalized text as it

            corresponds to the audio. For instance, the character 'H' starts at
            time 0 ms in the audio.

            Note these times are relative to the returned chunk from the model,
            and not the

            full audio response.
        charDurationsMs:
          type: array
          items:
            type: integer
          description: >
            A list of durations (in milliseconds) for each character in the
            normalized text as it

            corresponds to the audio. For instance, the character 'H' lasts for
            3 ms in the audio.

            Note these times are relative to the returned chunk from the model,
            and not the

            full audio response.
        chars:
          type: array
          items:
            type: string
          description: >
            A list of characters in the normalized text sequence. For instance,
            the first character is 'H'.

            Note that this list may contain spaces, punctuation, and other
            special characters.

            The length of this list should be the same as the lengths of
            `charStartTimesMs` and `charDurationsMs`.
      description: >
        Alignment information for the generated audio given the input normalized
        text sequence.
      title: NormalizedAlignment
    Alignment:
      type: object
      properties:
        charStartTimesMs:
          type: array
          items:
            type: integer
          description: >
            A list of starting times (in milliseconds) for each character in the
            text as it

            corresponds to the audio. For instance, the character 'H' starts at
            time 0 ms in the audio.

            Note these times are relative to the returned chunk from the model,
            and not the

            full audio response.
        charDurationsMs:
          type: array
          items:
            type: integer
          description: >
            A list of durations (in milliseconds) for each character in the text
            as it

            corresponds to the audio. For instance, the character 'H' lasts for
            3 ms in the audio.

            Note these times are relative to the returned chunk from the model,
            and not the

            full audio response.
        chars:
          type: array
          items:
            type: string
          description: >
            A list of characters in the text sequence. For instance, the first
            character is 'H'.

            Note that this list may contain spaces, punctuation, and other
            special characters.

            The length of this list should be the same as the lengths of
            `charStartTimesMs` and `charDurationsMs`.
      description: >
        Alignment information for the generated audio given the input text
        sequence.
      title: Alignment
    AudioOutput:
      type: object
      properties:
        audio:
          type: string
          description: >
            A generated partial audio chunk, encoded using the selected
            output_format, by default this

            is MP3 encoded as a base64 string.
        normalizedAlignment:
          $ref: '#/components/schemas/NormalizedAlignment'
        alignment:
          $ref: '#/components/schemas/Alignment'
      required:
        - audio
      title: AudioOutput
    FinalOutput:
      type: object
      properties:
        isFinal:
          type: boolean
          enum:
            - true
          description: >
            Indicates if the generation is complete. If set to `True`, `audio`
            will be null.
      title: FinalOutput
    V1TextToSpeechVoiceIdStreamInputSubscribe:
      oneOf:
        - $ref: '#/components/schemas/AudioOutput'
        - $ref: '#/components/schemas/FinalOutput'
      title: V1TextToSpeechVoiceIdStreamInputSubscribe
    RealtimeVoiceSettings:
      type: object
      properties:
        stability:
          type: number
          format: double
          default: 0.5
          description: Defines the stability for voice settings.
        similarity_boost:
          type: number
          format: double
          default: 0.75
          description: Defines the similarity boost for voice settings.
        style:
          type: number
          format: double
          default: 0
          description: >-
            Defines the style for voice settings. This parameter is available on
            V2+ models.
        use_speaker_boost:
          type: boolean
          default: true
          description: >-
            Defines the use speaker boost for voice settings. This parameter is
            available on V2+ models.
        speed:
          type: number
          format: double
          default: 1
          description: >-
            Controls the speed of the generated speech. Values range from 0.7 to
            1.2, with 1.0 being the default speed.
      title: RealtimeVoiceSettings
    GenerationConfig:
      type: object
      properties:
        chunk_length_schedule:
          type: array
          items:
            type: number
            format: double
          description: >
            This is an advanced setting that most users shouldn't need to use.
            It relates to our

            generation schedule.


            Our WebSocket service incorporates a buffer system designed to
            optimize the Time To First Byte (TTFB) while maintaining
            high-quality streaming.


            All text sent to the WebSocket endpoint is added to this buffer and
            only when that buffer reaches a certain size is an audio generation
            attempted. This is because our model provides higher quality audio
            when the model has longer inputs, and can deduce more context about
            how the text should be delivered.


            The buffer ensures smooth audio data delivery and is automatically
            emptied with a final audio generation either when the stream is
            closed, or upon sending a `flush` command. We have advanced settings
            for changing the chunk schedule, which can improve latency at the
            cost of quality by generating audio more frequently with smaller
            text inputs.


            The `chunk_length_schedule` determines the minimum amount of text
            that needs to be sent and present in our

            buffer before audio starts being generated. This is to maximise the
            amount of context available to

            the model to improve audio quality, whilst balancing latency of the
            returned audio chunks.


            The default value for `chunk_length_schedule` is: [120, 160, 250,
            290].


            This means that the first chunk of audio will not be generated until
            you send text that

            totals at least 120 characters long. The next chunk of audio will
            only be generated once a

            further 160 characters have been sent. The third audio chunk will be
            generated after the

            next 250 characters. Then the fourth, and beyond, will be generated
            in sets of at least 290 characters.


            Customize this array to suit your needs. If you want to generate
            audio more frequently

            to optimise latency, you can reduce the values in the array. Note
            that setting the values

            too low may result in lower quality audio. Please test and adjust as
            needed.


            Each item should be in the range 50-500.
      title: GenerationConfig
    PronunciationDictionaryLocator:
      type: object
      properties:
        pronunciation_dictionary_id:
          type: string
          description: The unique identifier of the pronunciation dictionary
        version_id:
          type: string
          description: The version identifier of the pronunciation dictionary
      required:
        - pronunciation_dictionary_id
        - version_id
      description: Identifies a specific pronunciation dictionary to use
      title: PronunciationDictionaryLocator
    InitializeConnection:
      type: object
      properties:
        text:
          type: string
          enum:
            - ' '
          description: The initial text that must be sent is a blank space.
        voice_settings:
          $ref: '#/components/schemas/RealtimeVoiceSettings'
        generation_config:
          $ref: '#/components/schemas/GenerationConfig'
        pronunciation_dictionary_locators:
          type: array
          items:
            $ref: '#/components/schemas/PronunciationDictionaryLocator'
          description: >
            Optional list of pronunciation dictionary locators. If provided,
            these dictionaries will be used to

            modify pronunciation of matching text. Must only be provided in the
            first message.


            Note: Pronunciation dictionary matches will only be respected within
            a provided chunk.
        xi-api-key:
          type: string
          description: >
            Your ElevenLabs API key. This can only be included in the first
            message and is not needed if present in the header.
        authorization:
          type: string
          description: >
            Your authorization bearer token. This can only be included in the
            first message and is not needed if present in the header.
      required:
        - text
      title: InitializeConnection
    SendText:
      type: object
      properties:
        text:
          type: string
          description: >-
            The text to be sent to the API for audio generation. Should always
            end with a single space string.
        try_trigger_generation:
          type: boolean
          default: false
          description: >
            This is an advanced setting that most users shouldn't need to use.
            It relates to our generation schedule.


            Use this to attempt to immediately trigger the generation of audio,
            overriding the `chunk_length_schedule`.

            Unlike flush, `try_trigger_generation` will only generate audio if
            our

            buffer contains more than a minimum

            threshold of characters, this is to ensure a higher quality response
            from our model.


            Note that overriding the chunk schedule to generate small amounts of

            text may result in lower quality audio, therefore, only use this
            parameter if you

            really need text to be processed immediately. We generally recommend
            keeping the default value of

            `false` and adjusting the `chunk_length_schedule` in the
            `generation_config` instead.
        voice_settings:
          $ref: '#/components/schemas/RealtimeVoiceSettings'
          description: >-
            The voice settings field can be provided in the first
            `InitializeConnection` message and then must either be not provided
            or not changed.
        generator_config:
          $ref: '#/components/schemas/GenerationConfig'
          description: >-
            The generator config field can be provided in the first
            `InitializeConnection` message and then must either be not provided
            or not changed.
        flush:
          type: boolean
          default: false
          description: >
            Flush forces the generation of audio. Set this value to true when
            you have finished sending text, but want to keep the websocket
            connection open.


            This is useful when you want to ensure that the last chunk of audio
            is generated even when the length of text sent is smaller than the
            value set in chunk_length_schedule (e.g. 120 or 50).
      required:
        - text
      title: SendText
    CloseConnection:
      type: object
      properties:
        text:
          type: string
          enum:
            - ''
          description: End the stream with an empty string
      required:
        - text
      title: CloseConnection
    V1TextToSpeechVoiceIdStreamInputPublish:
      oneOf:
        - $ref: '#/components/schemas/InitializeConnection'
        - $ref: '#/components/schemas/SendText'
        - $ref: '#/components/schemas/CloseConnection'
      title: V1TextToSpeechVoiceIdStreamInputPublish

```
## Speech to Text API — https://elevenlabs.io/docs/api-reference/speech-to-text
> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Realtime

GET /v1/speech-to-text/realtime

Realtime speech-to-text transcription service. This WebSocket API enables streaming audio input and receiving transcription results.

## Event Flow
- Audio chunks are sent as `input_audio_chunk` messages
- Transcription results are streamed back in various formats (partial, committed, with timestamps)
- Supports manual commit or VAD-based automatic commit strategies

Authentication is done either by providing a valid API key in the `xi-api-key` header or by providing a valid token in the `token` query parameter. Tokens can be generated from the [single use token endpoint](/docs/api-reference/tokens/create). Use tokens if you want to transcribe audio from the client side.


Reference: https://elevenlabs.io/docs/api-reference/speech-to-text/v-1-speech-to-text-realtime

## AsyncAPI Specification

```yaml
asyncapi: 2.6.0
info:
  title: V 1 Speech To Text Realtime
  version: subpackage_v1SpeechToTextRealtime.v1SpeechToTextRealtime
  description: >
    Realtime speech-to-text transcription service. This WebSocket API enables
    streaming audio input and receiving transcription results.


    ## Event Flow

    - Audio chunks are sent as `input_audio_chunk` messages

    - Transcription results are streamed back in various formats (partial,
    committed, with timestamps)

    - Supports manual commit or VAD-based automatic commit strategies


    Authentication is done either by providing a valid API key in the
    `xi-api-key` header or by providing a valid token in the `token` query
    parameter. Tokens can be generated from the [single use token
    endpoint](/docs/api-reference/tokens/create). Use tokens if you want to
    transcribe audio from the client side.
channels:
  /v1/speech-to-text/realtime:
    description: >
      Realtime speech-to-text transcription service. This WebSocket API enables
      streaming audio input and receiving transcription results.


      ## Event Flow

      - Audio chunks are sent as `input_audio_chunk` messages

      - Transcription results are streamed back in various formats (partial,
      committed, with timestamps)

      - Supports manual commit or VAD-based automatic commit strategies


      Authentication is done either by providing a valid API key in the
      `xi-api-key` header or by providing a valid token in the `token` query
      parameter. Tokens can be generated from the [single use token
      endpoint](/docs/api-reference/tokens/create). Use tokens if you want to
      transcribe audio from the client side.
    bindings:
      ws:
        query:
          type: object
          properties:
            model_id:
              type: string
            token:
              type: string
            include_timestamps:
              type: boolean
              default: false
            include_language_detection:
              type: boolean
              default: false
            audio_format:
              $ref: '#/components/schemas//v1/speech-to-text/realtime_audio_format'
              default: pcm_16000
            language_code:
              type: string
            commit_strategy:
              $ref: '#/components/schemas//v1/speech-to-text/realtime_commit_strategy'
              default: manual
            keyterms:
              type: array
              items:
                type: string
            no_verbatim:
              type: boolean
              default: false
            vad_silence_threshold_secs:
              type: number
              format: double
              default: 1.5
            vad_threshold:
              type: number
              format: double
              default: 0.4
            min_speech_duration_ms:
              type: integer
              default: 100
            min_silence_duration_ms:
              type: integer
              default: 100
            enable_logging:
              type: boolean
              default: true
        headers:
          type: object
          properties:
            xi-api-key:
              type: string
    publish:
      operationId: subpackage_v1SpeechToTextRealtime.v1SpeechToTextRealtime-publish
      summary: subscribe
      description: Receive transcription results from the WebSocket
      message:
        name: subscribe
        title: subscribe
        description: Receive transcription results from the WebSocket
        payload:
          $ref: '#/components/schemas/V1SpeechToTextRealtimeSubscribe'
    subscribe:
      operationId: subpackage_v1SpeechToTextRealtime.v1SpeechToTextRealtime-subscribe
      summary: publish
      description: Send audio data to the WebSocket
      message:
        name: publish
        title: publish
        description: Send audio data to the WebSocket
        payload:
          $ref: '#/components/schemas/V1SpeechToTextRealtimePublish'
servers:
  Production:
    url: wss://api.elevenlabs.io/
    protocol: wss
    x-default: true
  Production US:
    url: wss://api.us.elevenlabs.io/
    protocol: wss
  Production EU:
    url: wss://api.eu.residency.elevenlabs.io/
    protocol: wss
  Production India:
    url: wss://api.in.residency.elevenlabs.io/
    protocol: wss
  Production Singapore:
    url: wss://api.sg.residency.elevenlabs.io/
    protocol: wss
components:
  schemas:
    /v1/speech-to-text/realtime_audio_format:
      type: string
      enum:
        - pcm_8000
        - pcm_16000
        - pcm_22050
        - pcm_24000
        - pcm_44100
        - pcm_48000
        - ulaw_8000
      default: pcm_16000
      description: Audio encoding format for speech-to-text.
      title: /v1/speech-to-text/realtime_audio_format
    /v1/speech-to-text/realtime_commit_strategy:
      type: string
      enum:
        - manual
        - vad
      default: manual
      description: Strategy for committing transcriptions.
      title: /v1/speech-to-text/realtime_commit_strategy
    AudioFormatEnum:
      type: string
      enum:
        - pcm_8000
        - pcm_16000
        - pcm_22050
        - pcm_24000
        - pcm_44100
        - pcm_48000
        - ulaw_8000
      default: pcm_16000
      description: Audio encoding format for speech-to-text.
      title: AudioFormatEnum
    MessagesSessionStartedConfigCommitStrategy:
      type: string
      enum:
        - manual
        - vad
      description: Strategy for committing transcriptions.
      title: MessagesSessionStartedConfigCommitStrategy
    MessagesSessionStartedConfig:
      type: object
      properties:
        sample_rate:
          type: integer
          description: Sample rate of the audio in Hz.
        audio_format:
          $ref: '#/components/schemas/AudioFormatEnum'
          default: pcm_16000
        language_code:
          type: string
          description: Language code in ISO 639-1 or ISO 639-3 format.
        commit_strategy:
          $ref: '#/components/schemas/MessagesSessionStartedConfigCommitStrategy'
          description: Strategy for committing transcriptions.
        vad_silence_threshold_secs:
          type: number
          format: double
          description: Silence threshold in seconds.
        vad_threshold:
          type: number
          format: double
          description: Threshold for voice activity detection.
        min_speech_duration_ms:
          type: integer
          description: Minimum speech duration in milliseconds.
        min_silence_duration_ms:
          type: integer
          description: Minimum silence duration in milliseconds.
        model_id:
          type: string
          description: ID of the model to use for transcription.
        enable_logging:
          type: boolean
          description: >-
            When enable_logging is set to false zero retention mode will be used
            for the request. This will mean history features are unavailable for
            this request. Zero retention mode may only be used by enterprise
            customers.
        include_timestamps:
          type: boolean
          description: >-
            Whether the session will include word-level timestamps in the
            committed transcript.
        include_language_detection:
          type: boolean
          description: >-
            Whether the session will include language detection in the committed
            transcript.
        keyterms:
          type: array
          items:
            type: string
          description: List of keyterms the model is biased towards.
        no_verbatim:
          type: boolean
          description: >-
            Whether filler words and disfluencies are removed from the
            transcript.
      description: Configuration for the transcription session.
      title: MessagesSessionStartedConfig
    SessionStarted:
      type: object
      properties:
        message_type:
          type: string
          enum:
            - session_started
          description: The message type identifier.
        session_id:
          type: string
          description: Unique identifier for the session.
        config:
          $ref: '#/components/schemas/MessagesSessionStartedConfig'
          description: Configuration for the transcription session.
      required:
        - message_type
        - session_id
        - config
      description: Payload sent when the transcription session is successfully started.
      title: SessionStarted
    PartialTranscript:
      type: object
      properties:
        message_type:
          type: string
          enum:
            - partial_transcript
          description: The message type identifier.
        text:
          type: string
          description: Partial transcription text.
      required:
        - message_type
        - text
      description: Payload for partial transcription results that may change.
      title: PartialTranscript
    CommittedTranscript:
      type: object
      properties:
        message_type:
          type: string
          enum:
            - committed_transcript
          description: The message type identifier.
        text:
          type: string
          description: Committed transcription text.
      required:
        - message_type
        - text
      description: Payload for committed transcription results.
      title: CommittedTranscript
    TranscriptionWordType:
      type: string
      enum:
        - word
        - spacing
      description: The type of word.
      title: TranscriptionWordType
    TranscriptionWord:
      type: object
      properties:
        text:
          type: string
          description: The transcribed word.
        start:
          type: number
          format: double
          description: Start time in seconds.
        end:
          type: number
          format: double
          description: End time in seconds.
        type:
          $ref: '#/components/schemas/TranscriptionWordType'
          description: The type of word.
        speaker_id:
          type: string
          description: The ID of the speaker if available.
        logprob:
          type: number
          format: double
          description: Confidence score for this word.
        characters:
          type: array
          items:
            type: string
          description: The characters in the word.
      description: Word-level transcription data with timing information.
      title: TranscriptionWord
    CommittedTranscriptWithTimestamps:
      type: object
      properties:
        message_type:
          type: string
          enum:
            - committed_transcript_with_timestamps
          description: The message type identifier.
        text:
          type: string
          description: Committed transcription text.
        language_code:
          type:
            - string
            - 'null'
          description: Detected or specified language code.
        words:
          type:
            - array
            - 'null'
          items:
            $ref: '#/components/schemas/TranscriptionWord'
          description: Word-level information with timestamps.
      required:
        - message_type
        - text
      description: Payload for committed transcription results with word-level timestamps.
      title: CommittedTranscriptWithTimestamps
    ScribeError:
      type: object
      properties:
        message_type:
          type: string
          enum:
            - error
          description: The message type identifier.
        error:
          type: string
          description: Error message describing what went wrong.
      required:
        - message_type
        - error
      description: Payload for error events during transcription.
      title: ScribeError
    ScribeAuthError:
      type: object
      properties:
        message_type:
          type: string
          enum:
            - auth_error
          description: The message type identifier.
        error:
          type: string
          description: Authentication error details.
      required:
        - message_type
        - error
      description: Payload for authentication errors.
      title: ScribeAuthError
    ScribeQuotaExceededError:
      type: object
      properties:
        message_type:
          type: string
          enum:
            - quota_exceeded
          description: The message type identifier.
        error:
          type: string
          description: Quota exceeded error details.
      required:
        - message_type
        - error
      description: Payload for quota exceeded errors.
      title: ScribeQuotaExceededError
    ScribeThrottledError:
      type: object
      properties:
        message_type:
          type: string
          enum:
            - commit_throttled
          description: The message type identifier.
        error:
          type: string
          description: Throttled error details.
      required:
        - message_type
        - error
      description: Payload for throttled errors.
      title: ScribeThrottledError
    ScribeUnacceptedTermsError:
      type: object
      properties:
        message_type:
          type: string
          enum:
            - unaccepted_terms
          description: The message type identifier.
        error:
          type: string
          description: Unaccepted terms error details.
      required:
        - message_type
        - error
      description: Payload for unaccepted terms errors.
      title: ScribeUnacceptedTermsError
    ScribeRateLimitedError:
      type: object
      properties:
        message_type:
          type: string
          enum:
            - rate_limited
          description: The message type identifier.
        error:
          type: string
          description: Rate limited error details.
      required:
        - message_type
        - error
      description: Payload for rate limited errors.
      title: ScribeRateLimitedError
    ScribeQueueOverflowError:
      type: object
      properties:
        message_type:
          type: string
          enum:
            - queue_overflow
          description: The message type identifier.
        error:
          type: string
          description: Queue overflow error details.
      required:
        - message_type
        - error
      description: Payload for queue overflow errors.
      title: ScribeQueueOverflowError
    ScribeResourceExhaustedError:
      type: object
      properties:
        message_type:
          type: string
          enum:
            - resource_exhausted
          description: The message type identifier.
        error:
          type: string
          description: Resource exhausted error details.
      required:
        - message_type
        - error
      description: Payload for resource exhausted errors.
      title: ScribeResourceExhaustedError
    ScribeSessionTimeLimitExceededError:
      type: object
      properties:
        message_type:
          type: string
          enum:
            - session_time_limit_exceeded
          description: The message type identifier.
        error:
          type: string
          description: Session time limit exceeded error details.
      required:
        - message_type
        - error
      description: Payload for session time limit exceeded errors.
      title: ScribeSessionTimeLimitExceededError
    ScribeInputError:
      type: object
      properties:
        message_type:
          type: string
          enum:
            - input_error
          description: The message type identifier.
        error:
          type: string
          description: Input error details.
      required:
        - message_type
        - error
      description: Payload for input errors.
      title: ScribeInputError
    ScribeChunkSizeExceededError:
      type: object
      properties:
        message_type:
          type: string
          enum:
            - chunk_size_exceeded
          description: The message type identifier.
        error:
          type: string
          description: Chunk size exceeded error details.
      required:
        - message_type
        - error
      description: Payload for chunk size exceeded errors.
      title: ScribeChunkSizeExceededError
    ScribeInsufficientAudioActivityError:
      type: object
      properties:
        message_type:
          type: string
          enum:
            - insufficient_audio_activity
          description: The message type identifier.
        error:
          type: string
          description: Insufficient audio activity error details.
      required:
        - message_type
        - error
      description: Payload for insufficient audio activity errors.
      title: ScribeInsufficientAudioActivityError
    ScribeTranscriberError:
      type: object
      properties:
        message_type:
          type: string
          enum:
            - transcriber_error
          description: The message type identifier.
        error:
          type: string
          description: Transcriber error details.
      required:
        - message_type
        - error
      description: Payload for transcriber errors.
      title: ScribeTranscriberError
    V1SpeechToTextRealtimeSubscribe:
      oneOf:
        - $ref: '#/components/schemas/SessionStarted'
        - $ref: '#/components/schemas/PartialTranscript'
        - $ref: '#/components/schemas/CommittedTranscript'
        - $ref: '#/components/schemas/CommittedTranscriptWithTimestamps'
        - $ref: '#/components/schemas/ScribeError'
        - $ref: '#/components/schemas/ScribeAuthError'
        - $ref: '#/components/schemas/ScribeQuotaExceededError'
        - $ref: '#/components/schemas/ScribeThrottledError'
        - $ref: '#/components/schemas/ScribeUnacceptedTermsError'
        - $ref: '#/components/schemas/ScribeRateLimitedError'
        - $ref: '#/components/schemas/ScribeQueueOverflowError'
        - $ref: '#/components/schemas/ScribeResourceExhaustedError'
        - $ref: '#/components/schemas/ScribeSessionTimeLimitExceededError'
        - $ref: '#/components/schemas/ScribeInputError'
        - $ref: '#/components/schemas/ScribeChunkSizeExceededError'
        - $ref: '#/components/schemas/ScribeInsufficientAudioActivityError'
        - $ref: '#/components/schemas/ScribeTranscriberError'
      title: V1SpeechToTextRealtimeSubscribe
    InputAudioChunk:
      type: object
      properties:
        message_type:
          type: string
          enum:
            - input_audio_chunk
          description: The message type identifier.
        audio_base_64:
          type: string
          format: base64
          description: Base64-encoded audio data.
        commit:
          type: boolean
          description: Whether to commit the transcription after this chunk.
        sample_rate:
          type: integer
          description: Sample rate of the audio in Hz.
        previous_text:
          type: string
          description: >-
            Send text context to the model. Can only be sent alongside the first
            audio chunk. If sent in a subsequent chunk, an error will be
            returned.
      required:
        - message_type
        - audio_base_64
        - commit
        - sample_rate
      description: Payload for sending audio chunks from client to server.
      title: InputAudioChunk
    V1SpeechToTextRealtimePublish:
      oneOf:
        - $ref: '#/components/schemas/InputAudioChunk'
      title: V1SpeechToTextRealtimePublish

```
## ElevenAgents LLM models — https://elevenlabs.io/docs/eleven-agents/customization/llm
> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Models

ElevenAgents provides a unified interface to connect your agent to multiple models and providers, offering flexibility, reliability, and cost optimization.

## Key features

* **Unified access**: Switch between providers and models with minimal code changes
* **High reliability**: Automatically cascade from one provider to another if one fails
* **Spend monitoring**: Monitor your spending across different models

## Supported models

Currently, the following models are natively supported and can be configured via the agent settings:

| Provider       | Model                         |
| -------------- | ----------------------------- |
| **ElevenLabs** | Qwen3.6-35B-A3B               |
|                | Qwen3.5-397B-A17B             |
| **Google**     | Gemini 3.5 Flash              |
|                | Gemini 3.1 Pro Preview        |
|                | Gemini 3.1 Flash Lite         |
|                | Gemini 3.1 Flash Lite Preview |
|                | Gemini 3 Pro Preview          |
|                | Gemini 3 Flash Preview        |
|                | Gemini 2.5 Flash              |
|                | Gemini 2.5 Flash Lite         |
| **OpenAI**     | GPT-5.5                       |
|                | GPT-5.4                       |
|                | GPT-5.4 Mini                  |
|                | GPT-5.4 Nano                  |
|                | GPT-5.2                       |
|                | GPT-5.2 Chat Latest           |
|                | GPT-5.1                       |
|                | GPT-5                         |
|                | GPT-5 Mini                    |
|                | GPT-5 Nano                    |
|                | GPT-4.1                       |
|                | GPT-4.1 Mini                  |
|                | GPT-4.1 Nano                  |
|                | GPT-4o                        |
|                | GPT-4o Mini                   |
| **Anthropic**  | Claude Opus 4.7               |
|                | Claude Sonnet 4.6             |
|                | Claude Sonnet 4.5             |
|                | Claude Sonnet 4               |
|                | Claude Haiku 4.5              |

Pricing is typically denoted in USD per 1 million tokens unless specified otherwise. A token is a
fundamental unit of text data for LLMs, roughly equivalent to 4 characters on average.

### Custom LLM

Using your own custom LLM is supported by specifying the endpoint we should make requests to and providing credentials through our secure secret storage. Learn more about [custom LLM integration](/docs/eleven-agents/customization/llm/custom-llm).

With EU data residency enabled, a small number of older Gemini and Claude LLMs are not available
in ElevenLabs Agents to maintain compliance with EU data residency. Custom LLMs and OpenAI LLMs
remain fully available. For more information please see [GDPR and data
residency](/docs/overview/administration/data-residency).

## Choosing a model

Selecting the most suitable LLM for your application involves considering several factors:

* **Task complexity**: More demanding or nuanced tasks generally benefit from more powerful models (e.g., OpenAI's GPT-4 series, Anthropic's Claude Sonnet 4, Google's Gemini 2.5 models)
* **Latency requirements**: For applications requiring real-time or near real-time responses, such as live voice conversations, models optimized for speed are preferable (e.g., Google's Gemini Flash series, Anthropic's Claude Haiku, OpenAI's GPT-4o-mini)
* **Context window size**: If your application needs to process, understand, or recall information from long conversations or extensive documents, select models with larger context windows
* **Cost-effectiveness**: Balance the desired performance and features against your budget. LLM prices can vary significantly, so analyze the pricing structure (input, output, and cache tokens) in relation to your expected usage patterns
* **HIPAA compliance**: If your application involves Protected Health Information (PHI), it is crucial to use an LLM that is designated as HIPAA compliant and ensure your entire data handling process meets regulatory standards

The maximum system prompt size is 2MB, which includes your agent's instructions, knowledge base
content, and other system-level context.

## Model configuration

### Temperature

Temperature controls the randomness of model responses. Lower values produce more consistent, focused outputs while higher values increase creativity and variation.

* **Low (0.0-0.3)**: Deterministic, consistent responses for structured interactions
* **Medium (0.4-0.7)**: Balanced creativity and consistency
* **High (0.8-1.0)**: Creative, varied responses for dynamic conversations

### Backup LLM configuration

Configure backup LLMs to ensure conversation continuity when the primary LLM fails or becomes unavailable.

**Configuration options:**

* **Default**: Uses ElevenLabs' recommended fallback sequence
* **Custom**: Define your own cascading sequence of backup models
* **Disabled**: No fallback (strongly discouraged for production)

Disabling backup LLMs means conversations will end abruptly if your primary LLM fails or becomes
unavailable. This is strongly discouraged for production use.

Learn more about [LLM cascading](/docs/eleven-agents/customization/llm/llm-cascading).

### Thinking budget

Control how many internal reasoning tokens the model can use before responding. More tokens improve answer quality but slow down response time.

**Options:**

* **Disabled**: Fastest replies with no internal reasoning overhead
* **Low**: Minimal reasoning for quick responses
* **Medium**: Balanced reasoning and speed
* **High**: Maximum reasoning for complex queries

### Reasoning effort

Some models support configurable reasoning effort levels (None, Low, Medium, High).

**For conversational use-cases:**

Keep reasoning effort set to **None** to avoid the agent thinking too long, which can disrupt natural conversation flow.

**For workflow steps:**

Reasoning effort is perfect for workflow steps that require complex thought or decision-making where response time is less critical.

## Understanding pricing

* **Tokens**: LLM usage is typically billed based on the number of tokens processed. As a general guideline for English text, 100 tokens is approximately equivalent to 75 words
* **Input vs. output pricing**: Providers often differentiate pricing for input tokens (the data you send to the model) and output tokens (the data the model generates in response)
* **Cache pricing**:
  * `input_cache_read`: This refers to the cost associated with retrieving previously processed input data from a cache. Utilizing cached data can lead to cost savings if identical inputs are processed multiple times
  * `input_cache_write`: This is the cost associated with storing input data into a cache. Some LLM providers may charge for this operation
* The prices listed in this document are per 1 million tokens and are based on the information available at the time of writing. These prices are subject to change by the LLM providers

For the most accurate and current information on model capabilities, pricing, and terms of service, always consult the official documentation from the respective LLM providers (OpenAI, Google, Anthropic).

## HIPAA compliance

Certain LLMs available on our platform may be suitable for use in environments requiring HIPAA compliance, please see the [HIPAA compliance docs](/docs/eleven-agents/legal/hipaa) for more details.

## Related resources

* [Custom LLM integration](/docs/eleven-agents/customization/llm/custom-llm)
* [LLM cascading](/docs/eleven-agents/customization/llm/llm-cascading)
* [Optimizing costs](/docs/eleven-agents/customization/llm/optimizing-costs)
