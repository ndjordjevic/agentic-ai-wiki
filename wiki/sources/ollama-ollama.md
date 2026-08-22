---
type: source
category: "Model infra, ML & providers"
source_url: https://github.com/ollama/ollama
tags:
  - local-llm
  - model-runtime
  - llama-cpp
  - open-source-models
  - rest-api
  - agent-backend
  - mlx-engine
  - coding-agent-integration
related: [router.com]
  - litellm.ai
  - strandsagents.com
  - pydantic.dev
  - gitlawb-openclaude
  - adk.dev
  - microsoft-agent-framework
  - crewai.com
  - langchain.com
  - huggingface.co
  - zilliztech-claude-context
  - vercel.com
  - nvidia.com
product: ollama
detail_level: standard
created: 2026-07-07
updated: 2026-08-22
---

**Ollama** (`ollama/ollama`, 175k+ stars, MIT, Go) is the dominant local LLM runtime for running open-weight models on macOS, Windows, and Linux. It packages model pull/run, a localhost REST API on port 11434, official Python/JS SDKs, OpenAI- and Anthropic-compatible endpoints, and first-party `ollama launch` integrations for coding agents (Claude Code, Codex, Copilot CLI, OpenCode, OpenClaw). Inference backends include llama.cpp (GGUF) and MLX (safetensors); GPU acceleration spans Metal, CUDA, ROCm, and Vulkan.

_All claims below are sourced from ../../raw/github/ollama-ollama.md unless otherwise noted._

## What it does

Ollama is a self-contained runtime that downloads, quantizes, caches, and serves open models locally. Users install via curl/Homebrew/Docker, run `ollama run <model>` for interactive chat, or call the REST API from agents and apps. The `ollama` CLI also wires local models into existing agent tooling — `ollama launch claude` for Claude Code, `ollama launch openclaw` for omnichannel personal assistants — without rewriting agent code. Model library and registry live at ollama.com/library.

## Installation

**macOS / Linux:**
```shell
curl -fsSL https://ollama.com/install.sh | sh
```

**Windows:**
```powershell
irm https://ollama.com/install.ps1 | iex
```

**Docker:** official image `ollama/ollama` on Docker Hub.

**From source** (requires Go, CMake 3.24+, C/C++ compiler):
```shell
cmake -B build .
cmake --build build --parallel 8
./ollama serve
```

Quick Go-only iteration: `go run . serve` (requires existing native payload under `build/lib/ollama`).

## Key features

- **Model library** — pull/run models by name (`gemma4`, `llama3.2`, `deepseek-r1`, etc.) with `model:tag` versioning; defaults to `latest`.
- **REST API** — chat (`POST /api/chat`), completion (`POST /api/generate`), embeddings (`POST /api/embed`), pull/push/copy/delete, model listing (`GET /api/tags`), running-model status (`GET /api/ps`); default `http://localhost:11434`.
- **SDKs** — official [ollama-python](https://github.com/ollama/ollama-python) and [ollama-js](https://github.com/ollama/ollama-js) packages.
- **Compatibility layers** — OpenAI-compatible and Anthropic-compatible API surfaces (`openai/`, `anthropic/` packages) so existing agent SDKs can point at localhost.
- **Agent launch integrations** — `ollama launch <integration>` for Claude Code, Codex, Copilot CLI, Droid, OpenCode, OpenClaw (docs at docs.ollama.com/integrations).
- **Multimodal & structured output** — image inputs for vision models; JSON schema / JSON mode via `format` parameter; `think` levels for reasoning models.
- **Modelfile** — declarative model customization (system prompt, parameters, adapters).
- **GPU backends** — llama.cpp with CUDA (`cuda_v12`/`cuda_v13`), ROCm (`rocm_v7_1`/`rocm_v7_2`), Vulkan; MLX engine on Apple Silicon (default) and optional CUDA MLX; Metal on macOS arm64.

## Architecture

Ollama is a Go application with CGO-linked native inference payloads. The HTTP `server/` exposes REST routes; `cmd/` builds the `ollama` CLI. Core inference flows through `llm/` and `runner/` against `llama/` (llama.cpp bindings) or `ml/` (MLX engine for safetensors). `model/` handles manifests, pull/push lifecycle, and local storage. `convert/` transforms external formats; `discover/` finds available models. `integration/` and `agent/` house coding-agent launch wiring. `tools/` implements tool-calling for agent use. `template/` manages prompt templates; `thinking/` supports reasoning models.

Native builds use CMake: on macOS arm64, Metal inference is default; elsewhere CPU-only unless GPU backends are explicitly selected (`-DOLLAMA_LLAMA_BACKENDS="cuda_v13;vulkan"`). MLX backends are selected via `OLLAMA_MLX_BACKENDS`. Runtime libraries resolve from `build/lib/ollama` (dev), `../lib/ollama` (install), or platform-specific layouts documented in `docs/development.md`.

## Example usage

**Interactive chat:**
```shell
ollama run gemma4
```

**REST chat:**
```shell
curl http://localhost:11434/api/chat -d '{
  "model": "gemma4",
  "messages": [{"role": "user", "content": "Why is the sky blue?"}],
  "stream": false
}'
```

**Python SDK:**
```python
from ollama import chat
response = chat(model='gemma4', messages=[{'role': 'user', 'content': 'Why is the sky blue?'}])
print(response.message.content)
```

**Launch Claude Code against a local model:**
```shell
ollama launch claude
```

## Maintenance status

- **175,624 stars**, 16,864 forks (fetched 2026-07-07)
- **Latest release:** v0.31.2-rc1 (2026-07-06, pre-release)
- **License:** MIT
- **Default branch:** `main`
- **Homepage:** https://ollama.com
- **Docs:** https://docs.ollama.com (CLI, API, modelfile, integrations, GPU)
- **Community:** Discord, Reddit r/ollama, extensive third-party integration list in README
