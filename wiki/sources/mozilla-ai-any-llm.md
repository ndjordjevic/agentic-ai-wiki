---
type: source
category: "Model infra, ML & providers"
source_url: https://github.com/mozilla-ai/any-llm
tags:
  - provider-adapter
  - unified-llm-api
  - official-sdks
  - openai-compatible
  - litellm-alternative
  - responses-api
  - python-sdk
related:
  - litellm.ai
  - openrouter.ai
  - pydantic-pydantic-ai
  - router-for-me-CLIProxyAPI
product: any-llm
detail_level: standard
created: 2026-07-22
updated: 2026-07-28
---

any-llm is a Mozilla.ai open-source Python SDK that provides a single, unified interface for calling any LLM provider — OpenAI, Anthropic, Azure/Microsoft Foundry, Mistral, Ollama, and 45+ others — without changing application code between providers. Unlike LiteLLM ([[litellm.ai]]), which reimplements each provider's request/response format itself, any-llm deliberately wraps each provider's **official SDK**, trading breadth of custom translation logic for compatibility guarantees and lower maintenance risk. It positions itself as a drop-in migration target for existing LiteLLM users and powers Mozilla.ai's own agent framework, any-agent.

_All claims below are sourced from ../../raw/github/mozilla-ai-any-llm.md unless otherwise noted._

## What it does

any-llm exposes a `completion()` function (and `AnyLLM` class) that accepts a `provider` and `model` string pair and returns a normalized, OpenAI-compatible response regardless of which backend actually served the request. Both synchronous and async (`acompletion`) calling styles are supported, along with an OpenAI-style `responses`/`aresponses` API for providers that implement the Responses API. Switching providers is a one-line change: swap the `provider` string and set the corresponding API key environment variable.

## Installation

```bash
pip install 'any-llm-sdk[openai]'           # single provider
pip install 'any-llm-sdk[mistral,ollama]'   # multiple providers
pip install 'any-llm-sdk[all]'              # every supported provider
```

Requires Python 3.11+. Library authors can install the bare `any-llm-sdk` package and let downstream users add provider extras themselves. API keys are set as environment variables (e.g. `MISTRAL_API_KEY`, `OPENAI_API_KEY`) or passed directly via the `api_key` parameter.

## Key features

- **50+ provider integrations** under `src/any_llm/providers/` — OpenAI, Anthropic, Azure, AzureAnthropic, AzureOpenAI, Bedrock, Cerebras, Cohere, Databricks, DeepSeek, Fireworks, Gemini, Groq, HuggingFace, Llama, LlamaCpp, LlamaFile, LMStudio, Mistral, Moonshot, Nebius, Ollama, OpenRouter, Perplexity, Portkey, SageMaker, SambaNova, Together, VertexAI, VertexAIAnthropic, vLLM, Voyage, Watsonx, xAI, and more.
- **Two calling styles:** direct API functions (`completion`/`acompletion`) for scripts and one-off requests (stateless, new client per call), and an `AnyLLM` class (`AnyLLM.create(provider)`) for production apps that reuse a client across multiple requests (connection pooling).
- **`provider:model` combined syntax** as an alternative to separate `provider`/`model` parameters, e.g. `model="mistral:mistral-small-latest"`.
- **Responses API support** (`responses`/`aresponses`) mirroring OpenAI's Responses API for providers that implement it.
- **Provider metadata introspection** via `llm.get_provider_metadata()` — reports per-provider capability flags such as streaming and tool-calling support.
- **Otari Gateway** (separate project, [mozilla-ai/otari](https://github.com/mozilla-ai/otari)) adds budget management, API key management, usage analytics, and multi-tenant support on top of any-llm.

## Architecture

The package lives under `src/any_llm/`, with `providers/` containing one subpackage per provider — each wraps that provider's official SDK rather than reimplementing the wire protocol. Shared logic lives in `api.py` (module-level `completion`/`responses` functions) and `any_llm.py` (the `AnyLLM` class), with `types/`, `utils/`, `constants.py`, `exceptions.py`, `logging.py`, and `tools.py` providing cross-provider normalization (response shapes, error mapping, tool-call formatting). Leveraging official SDKs per provider is the project's core architectural bet: it trades a larger dependency surface for closer parity with each provider's actual behavior and faster support for new provider features.

## Example usage

```python
from any_llm import completion
import os

assert os.environ.get('MISTRAL_API_KEY')

response = completion(
    model="mistral-small-latest",
    provider="mistral",
    messages=[{"role": "user", "content": "Hello!"}]
)
print(response.choices[0].message.content)
```

```python
from any_llm import AnyLLM

llm = AnyLLM.create("mistral", api_key="your-mistral-api-key")
response = llm.completion(
    model="mistral-small-latest",
    messages=[{"role": "user", "content": "Hello!"}]
)
```

Migrating from LiteLLM requires only an import and model-string change (`openai/gpt-4o` → `openai:gpt-4o`); environment variables and API keys carry over unchanged.

## When to use

any-llm fits teams that want provider breadth similar to LiteLLM but prefer relying on each provider's official SDK for compatibility guarantees rather than a reimplemented request/response layer. It is framework-agnostic (no proxy server required) and is used in production inside Mozilla.ai's own agent framework, [any-agent](https://github.com/mozilla-ai/any-agent). It is a good fit for libraries and applications that need a thin, in-process abstraction over multiple LLM providers without standing up a gateway service.

## Ecosystem

any-llm distinguishes itself from three categories of alternatives (per its own README): **LiteLLM** (reimplements provider interfaces instead of using official SDKs), **AISuite** (clean but no longer actively maintained), and **proxy-only solutions** like OpenRouter ([[openrouter.ai]]) and Portkey (require a hosted proxy between application code and the provider). Companion project **Otari** provides gateway-style features (budgeting, key management, multi-tenancy) for teams that do want a hosted layer. Full docs, provider list, and cookbook examples are at https://docs.mozilla.ai/any-llm/.

## Maintenance status

2,134 stars, 196 forks, Apache 2.0 license, actively released (latest tag 1.21.0, 2026-07-16; pushed 2026-07-17). Python 3.11+. Published to PyPI as `any-llm-sdk`. CI covers linting, unit tests, and integration tests across providers.
