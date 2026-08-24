# x.ai

## Fetch log
- Inbox URL: https://x.ai/bot
- Final URL: https://x.ai/bot
- Fetched: 2026-08-24
- Pages: 7
- Mode: standard

## Landing page — https://x.ai/

NewMeet Grok 4.6 • Our new model

# Frontier AI models for everything you build.

Reasoning, code, voice, images, and video. Trained on the world's largest supercluster.

## Bot page — https://x.ai/bot

### Work with many Bots at once

Create a Bot, give it a task, and add another when the work grows—one on a project, one on outbound, one on systems. They work in parallel, collaborate where it makes sense, and keep working 24/7.

## API page — https://x.ai/api

How do I get an API key for Grok?

Create a free account at https://console.x.ai, open "API Keys", and create a key. It takes about a minute. Then point your existing SDK at `https://api.x.ai/v1` and make your first call.

Is Grok free to use through the API?

API usage is billed per token rather than free, but the Playground comes with every Console account, so you can test the latest Grok models before adding billing.

How much does Grok cost through the API?

xAI API pricing is usage-based: grok-4.6, the latest flagship, costs $2 per million input tokens and $6 per million output tokens. Full, always-current pricing for every Grok model is in the docs.

Can I use the OpenAI or Anthropic SDK with Grok?

Yes. Point your existing SDK at base URL `https://api.x.ai/v1` with your xAI API key. Most integrations need no other changes.

Which Grok models are available in the API?

The xAI API serves the latest Grok models: grok-4.6, grok-4.5 for text, reasoning, and coding, plus the Grok Imagine and Grok Voice model families. Every model runs on the same API key from the Console.

Where is the API documentation for Grok?

The full API reference, guides, and quickstart live at https://docs.x.ai.

Can I use Grok through my cloud provider?

Yes. Grok models are offered in the AI catalogs of the major clouds, including Microsoft, Oracle, Google, and Amazon platforms, alongside the native xAI API.

Can I use Grok to generate videos, ads, logos, or voiceovers?

Yes. The Grok Imagine API (/api/imagine) creates and edits images and video, from logos and product shots to animated campaign clips, and the Grok Voice API (/api/voice) handles voiceovers, dubbing, and realtime voice agents.

## Docs overview — https://docs.x.ai/overview

# Get started

Build with Grok — intelligent, fast, and cost-effective models across code, text, voice, image, and video.

### Code API (/build/overview)
Agentic coding with Grok Build (grok-build-0.1), our coding model, on the API and CLI.
- Agentic coding workflows
- Powers Grok Build
- Available on the API in early access

### Responses API (/developers/model-capabilities/text/generate-text)
Generate text, have conversations, use tools, and build AI-powered applications.
- Generate text
- Multi-turn chat
- Function calling

### Voice API (/developers/model-capabilities/audio/text-to-speech)
Convert text to natural speech or transcribe audio with our voice models.
- Text to speech
- Speech to text
- Real-time voice

### Imagine API (Images) (/developers/model-capabilities/images/generation)
Generate stunning images from text, edit existing images, and understand visual content.
- Generate images
- Edit images
- Precise control

### Imagine API (Video) (/developers/model-capabilities/video/generation)
Bring an image to life, start from a simple text prompt, or refine a complex cinematic sequence.
- Generate videos
- Edit videos
- Precise control

## Quick Start

```python
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_XAI_API_KEY",
    base_url="https://api.x.ai/v1",
)

response = client.responses.create(
    model="grok-4.6",
    input="Fix this function and explain the bug: function median(a){a.sort();return a[a.length/2]}",
)

print(response.output_text)
```

## Models — https://docs.x.ai/developers/models

### Text API Pricing

| Model | Context | Input / 1M tokens | Cached input / 1M tokens | Output / 1M tokens |
|---|---|---|---|---|
| grok-4.6 (< 200k prompt tokens) | 500k | $2.00 | $0.50 | $6.00 |
| grok-4.6 (≥ 200k prompt tokens) | 500k | $4.00 | $1.00 | $12.00 |
| grok-4.5 (< 200k prompt tokens) | 500k | $2.00 | $0.30 | $6.00 |
| grok-4.5 (≥ 200k prompt tokens) | 500k | $4.00 | $0.60 | $12.00 |
| grok-4.3 (< 200k prompt tokens) | 1M | $1.25 | $0.20 | $2.50 |
| grok-4.20-0309-reasoning (< 200k prompt tokens) | 1M | $1.25 | $0.20 | $2.50 |
| grok-build-0.1 (< 200k prompt tokens) | 256k | $1.00 | $0.20 | $2.00 |
| grok-4.20-multi-agent-0309 (< 200k prompt tokens) | 1M | $1.25 | $0.20 | $2.50 |

### Imagine Pricing

| Model | Cost |
|---|---|
| grok-imagine-image-2.0 | $0.04 / image |
| grok-imagine-image | $0.02 / image |
| grok-imagine-image-quality | $0.05 / image |
| grok-imagine-video-1.5 | $0.080 / sec |
| grok-imagine-video | $0.050 / sec |

### Voice Pricing

| Mode | Cost |
|---|---|
| Speech to Speech (grok-voice-think-fast-2.0) | $0.08 / min ($4.80 / hr) audio; $0.004 / text input |
| Speech to Text | $0.10 / hr (REST), $0.20 / hr (Streaming) |
| Text to Speech | $15.00 / 1M chars |

Which model should I choose?

- Code: Grok 4.6
- Chat: Grok 4.6
- Images: Grok Imagine Image 2.0
- Videos: Grok Imagine Video 1.5
- Voice: Grok Voice API

Model aliases: `<modelname>` is aliased to latest stable version; `<modelname>-latest` to the absolute latest.

## Grok Bot — https://docs.x.ai/grok-bot/overview

Bots are AI teammates you can give real work to. Bots can sign and use apps and websites just like you do on a persistent cloud computer. They can collaborate independently, passing context between each other and handing off tasks, and understand the nuances of how you like work done over time. They finish jobs end to end, and only come back when something needs your approval.

You work with a Bot by messaging it like a teammate. Give it a task or function, relevant context, and access to any tools or files needed to do the work. Bots take on ambitious projects, work across multiple tools and systems, and keep you updated of their actions in the conversation.

### What makes Grok Bot different

- **It has a computer of its own.** Each Bot runs on a persistent cloud VM with a browser, filesystem, and terminal. It can use connectors/MCP where available, and computer use for apps and websites without a clean API, so work finishes in the real tools rather than as chat drafts.
- **It is very easy to get started.** Create a Bot, message it, and grant access as needed. No workflow builder or prior Bot setup required. The same Bot is reachable from the desktop app and iOS.
- **It coordinates independently with other Bots.** Multiple Bots share one user-scoped computer and can run in parallel. They can message each other, share context in threads or group chats, and pass ownership so you are not the router between tools.
- **It can learn workflows from live demonstration.** Ask a Bot to follow along once through a multi-step or multi-system path. It persists that path as a routine and can re-run it on a schedule or on demand.
- **It is a persistent, named teammate with a durable state.** Named Bots keep memory, files, browser sessions, and preferences across turns. Context compounds instead of resetting to a fresh environment on every task.

### Bots share one computer

All of your Bots use the same persistent cloud computer. They share files, browser sessions, and app logins, which makes handoffs possible without repeating setup.

### A good first handoff example

> Pull this week's Strategic Prospects PG List from Salesforce. Skip anyone already in a sequence. Research the top 5 accounts across the web, Slack, Databricks, and Sumble, pull contacts, and draft LinkedIn and email in my voice, and leave me drafts to approve by tomorrow morning.

## Grok Build — https://docs.x.ai/build/overview

Grok Build is a powerful and extensible coding agent. Use it via an interactive TUI, headlessly in scripts or bots, or through the Agent Client Protocol (ACP) in other apps.

### Install
```bash
curl -fsSL https://x.ai/cli/install.sh | bash
```

### Start an interactive session
```bash
cd your-project
grok
```

### Run headlessly
```bash
grok -p "Explain this codebase"
grok -p "Explain the architecture" --output-format streaming-json
```

### Custom models
Grok supports any custom model. Add it to `~/.grok/config.toml`:
```toml
[model.my-model]
model = "model-id"
base_url = "https://api.example.com/v1"
name = "Display Name"
env_key = "API_KEY"

[models]
default = "my-model"
```

Use `grok inspect` to see config sources, instructions, skills, plugins, hooks, and MCP servers.

### Features
- Skills, Plugins & Marketplaces
- Modes and Commands
- Headless & Scripting
- Enterprise Deployments

## Voice API — https://x.ai/api/voice

# Grok Voice API: voice agents that feel human.

Deploy intelligent speech-to-speech voice agents for customer support, sales, and more. Enterprise-grade text-to-speech and speech-to-text APIs.

- #1 Tau Voice Leaderboard
- Sub-second latency
- 25+ languages
- $0.05 / min
