# openrouter.ai

## Fetch log
- Inbox URL: https://openrouter.ai/
- Final URL: https://openrouter.ai/
- Fetched: 2026-05-18
- Pages: 6
- Mode: standard

## Landing page — https://openrouter.ai/

# OpenRouter

Navigation: Models | Fusion | Chat | Rankings | Apps | Enterprise | Pricing | Docs

# The Unified Interface For LLMs

Better prices, better uptime, no subscriptions.

**Stats:**
- 80T Monthly Tokens
- 8M+ Global Users
- 60+ Providers
- 400+ Models

**Providers supported:** Microsoft, NVIDIA, Meta (Llama), Google Gemini, Amazon, DeepSeek, Qwen, MoonshotAI, MiniMax, Z-AI, MistralAI, Anthropic, OpenAI, Google AI Studio, X-AI, Cohere, HuggingFace, Perplexity, NousResearch, Together, Morph, Inflection, Liquid, Inception, Arcee-AI, and more.

### One API for Any Model
Access all major models through a single, unified interface. OpenAI SDK works out of the box.

### Higher Availability
Reliable AI models via our distributed infrastructure. Fall back to other providers when one goes down.

### Price and Performance
Keep costs in check without sacrificing speed. OpenRouter runs at the edge for minimal latency between your users and their inference.

### Custom Data Policies
Protect your organization with fine grained data policies. Ensure prompts only go to the models and providers you trust.

## Featured Models (400+ active models on 60+ providers)
- Claude Opus 4.7 by anthropic — 1.6T tokens weekly, +11% trend
- GPT-5.5 by openai — 493.5B tokens weekly, +8% trend
- Gemini 3.1 Pro Preview by google — 441.1B tokens weekly, +38% trend

## Featured Agents (250k+ apps using OpenRouter with 4.2M+ users globally)
- Replit — The easiest way to go from idea to app
- Hermes Agent — An autonomous agent that grows with you
- Kilo Code — Everything you need for agentic development

## How to Get Started
1. Signup — Create an account to get started.
2. Buy credits — Credits can be used with any model or provider.
3. Get your API key — Create an API key and start making requests. Fully OpenAI compatible.

## Recent Announcements
- Human-in-the-Loop Tools for the Agent SDK (May 8, 2026)
- Consistent Web Search and Fetch Across Every Model (May 7, 2026)
- GPT-5.5 Price Increase: What It Actually Costs (May 4, 2026)

## Product Nav (Footer)
- Product: Chat, Rankings, Apps, Models, Providers, Pricing, Enterprise, Labs
- Company: About, Announcements, Careers, Privacy, Terms, Support, State of AI, Works With OR, Data
- Developer: Documentation, API Reference, SDK, Status
- GitHub: https://github.com/OpenRouterTeam

## Docs — https://openrouter.ai/docs/quickstart

OpenRouter provides a unified API that gives you access to hundreds of AI models through a single endpoint, while automatically handling fallbacks and selecting the most cost-effective options.

Three integration approaches:

| Approach | Best for |
|---|---|
| API | Full control, any language, no dependencies |
| Client SDKs | Type-safe model calls with minimal overhead |
| Agent SDK | Building agents with tool use, loops, and state |

### Using the OpenRouter API
Send standard HTTP requests to `/api/v1/chat/completions` — compatible with any language or framework. The endpoint is OpenAI-compatible.

Example (Python):
```python
import requests
import json

response = requests.post(
  url="https://openrouter.ai/api/v1/chat/completions",
  headers={
    "Authorization": "Bearer <OPENROUTER_API_KEY>",
    "HTTP-Referer": "<YOUR_SITE_URL>",
    "X-OpenRouter-Title": "<YOUR_SITE_NAME>",
  },
  data=json.dumps({
    "model": "~openai/gpt-latest",
    "messages": [{"role": "user", "content": "What is the meaning of life?"}]
  })
)
```

### Using the Client SDKs
The Client SDKs wrap the OpenRouter API with full type safety, auto-generated types from the OpenAPI spec, and zero boilerplate.

```bash
npm install @openrouter/sdk
```

```typescript
import OpenRouter from '@openrouter/sdk';

const client = new OpenRouter({ apiKey: '<OPENROUTER_API_KEY>' });
const completion = await client.chat.send({
  model: '~openai/gpt-latest',
  messages: [{ role: 'user', content: 'What is the meaning of life?' }],
});
```

### Using the Agent SDK
The Agent SDK (`@openrouter/agent`) provides higher-level primitives for building AI agents. It handles multi-turn conversation loops, tool execution, and state management automatically via the `callModel` function.

```bash
npm install @openrouter/agent
```

```typescript
import { callModel, tool } from '@openrouter/agent';
import { z } from 'zod';

const weatherTool = tool({
  name: 'get_weather',
  description: 'Get the current weather for a location',
  inputSchema: z.object({ location: z.string().describe('City name') }),
  execute: async ({ location }) => ({ temperature: 72, condition: 'sunny', location }),
});

const result = await callModel({
  model: '~anthropic/claude-sonnet-latest',
  messages: [{ role: 'user', content: 'What is the weather in San Francisco?' }],
  tools: [weatherTool],
});
console.log(await result.getText());
```

### Using the OpenAI SDK (drop-in)
```typescript
import OpenAI from 'openai';

const openai = new OpenAI({
  baseURL: 'https://openrouter.ai/api/v1',
  apiKey: '<OPENROUTER_API_KEY>',
});
```

## API Reference — https://openrouter.ai/docs/api/reference

OpenRouter normalizes the schema across models and providers. Request format is nearly identical to OpenAI's Chat Completions API.

### Endpoint
`POST https://openrouter.ai/api/v1/chat/completions`

### Key request parameters:
- `model` — model slug (e.g. `anthropic/claude-sonnet-4`, `~openai/gpt-latest`)
- `messages` — array of {role, content} objects
- `stream` — boolean for SSE streaming
- `response_format` — `{type: 'json_object'}` or `{type: 'json_schema', json_schema: {...}}`
- `tools` / `tool_choice` — tool calling
- `models` — array of fallback models (OpenRouter-specific)
- `route` — `'fallback'` for manual fallback routing
- `provider` — ProviderPreferences object for routing control
- OpenAI-compatible: `temperature`, `max_tokens`, `top_p`, `frequency_penalty`, `presence_penalty`, `stop`, `seed`

### Plugins
- `web` — web search
- `file-parser` — PDF/document parsing
- `response-healing` — auto-repair malformed outputs
- `context-compression` — compress large contexts

### Structured Outputs
Supports `json_object` and `json_schema` response formats.

OpenAPI spec available at: https://openrouter.ai/docs/api/openapi.json

## Agent SDK Overview — https://openrouter.ai/docs/agent-sdk/overview

The Agent SDK (`@openrouter/agent`) provides primitives for building agentic applications. It handles multi-turn conversation loops, tool dispatch, and state tracking.

### Core features:
- **Multi-turn agent loops** — `callModel` loops until a stop condition is met
- **Tool definitions** — define tools with the `tool()` helper; SDK executes them automatically
- **Stop conditions** — `stepCountIs`, `hasToolCall`, `maxCost`, and more
- **Conversation state** — tracks messages, tool results, and context across turns
- **Streaming** — real-time token output within each agent step
- **Dynamic parameters** — change model, temperature, or tools between turns

### Comparison: Agent SDK vs Client SDKs
| | Agent SDK | Client SDKs |
|---|---|---|
| Focus | Agentic primitives — multi-turn, tools, stop conditions | Lean API client — mirrors REST API |
| Languages | TypeScript | TypeScript, Python, Go |
| Tool execution | Automatic | Manual |
| Conversation state | Managed by SDK | Managed by developer |

### Stop conditions example:
```typescript
const result = await callModel({
  model: 'anthropic/claude-sonnet-4',
  messages: [{ role: 'user', content: 'Research this topic thoroughly' }],
  tools: [searchTool],
  stopWhen: [stepCountIs(10), maxCost(0.50)],
});
```

## Provider Routing — https://openrouter.ai/docs/guides/routing/provider-selection

OpenRouter routes requests to the best available provider using intelligent load balancing.

### Default strategy: Price-Based Load Balancing
1. Prioritize providers with no significant outages in last 30 seconds
2. Among stable providers, select weighted by inverse square of price
3. Use remaining providers as fallbacks

Example: Provider A at $1/M tokens is 9x more likely to be selected than Provider C at $3/M (inverse square: 1/1² vs 1/3²).

### `provider` object parameters:
| Field | Type | Default | Description |
|---|---|---|---|
| `order` | string[] | - | Ordered list of provider slugs to try |
| `allow_fallbacks` | boolean | true | Allow backup providers on failure |
| `require_parameters` | boolean | false | Only use providers supporting all request params |
| `data_collection` | "allow"/"deny" | "allow" | Control data storage by providers |
| `zdr` | boolean | - | Zero Data Retention endpoints only |
| `only` | string[] | - | Whitelist specific providers |
| `ignore` | string[] | - | Blacklist specific providers |
| `quantizations` | string[] | - | Filter by quantization level (int4, int8) |
| `sort` | string/object | - | Sort by price, throughput, or latency |
| `preferred_min_throughput` | number/object | - | Minimum tokens/sec threshold |
| `preferred_max_latency` | number/object | - | Maximum latency threshold |
| `max_price` | object | - | Maximum price per request |

EU in-region routing available for Enterprise customers.

## Uptime Optimization — https://openrouter.ai/docs/guides/best-practices/uptime-optimization

OpenRouter continuously monitors provider health in real-time: response times, error rates, and availability. Smart routing automatically avoids degraded providers and falls back to alternatives. Developers can also customize provider selection via the `provider` object.
