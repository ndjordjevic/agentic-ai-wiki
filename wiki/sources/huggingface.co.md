---
type: source
source_url: https://huggingface.co/
tags:
  - machine-learning-hub
  - open-source-models
  - transformers
  - smolagents
  - model-hosting
  - inference-api
  - fine-tuning
  - diffusers
related:
  - langchain.com
  - pytorch.org
  - litellm.ai
product: huggingface
detail_level: standard
created: 2026-05-18
updated: 2026-05-18
---

Hugging Face is the open-source AI platform where the machine learning community collaborates on models, datasets, and applications. It hosts over 2 million models, 1.5 million datasets, and 1.5 million AI apps (Spaces), serving as both the primary distribution hub for state-of-the-art ML research and a production deployment platform. For agentic AI practitioners, Hugging Face is significant on two levels: as the ecosystem through which most open-weight foundation models (Llama, Mistral, Qwen, and thousands more) are accessed, fine-tuned, and served, and as the home of smolagents — a lightweight Python library for building code-first agents that rivals LangChain in simplicity while staying model- and tool-agnostic.

_All claims below are sourced from ../../raw/web/huggingface.co.md unless otherwise noted._

## What it does

Hugging Face operates as a multi-layer platform:

- **Model Hub:** the canonical repository for 2M+ open-weight models across text, vision, audio, video, and multimodal tasks. Every model ships with a Model Card, inference widget, evaluation metadata, and a serverless Inference Providers API for immediate testing.
- **Dataset Hub:** 500k+ public datasets in 8,000+ languages across NLP, Computer Vision, and Audio; each with a Data Studio browser, Dataset Card, and streaming access via the `datasets` library.
- **Spaces:** hosted ML demo apps supporting Gradio, Streamlit, static HTML/CSS/JS, and Docker containers. ZeroGPU provides dynamic NVIDIA RTX Pro 6000 Blackwell GPU allocation at zero cost for demo workloads.
- **Storage Buckets:** S3-compatible object storage powered by the Xet backend for large-scale artifacts (checkpoints, logs, embeddings) without version-control overhead.
- **Inference Providers:** a unified API gateway to 200,000+ models across 10+ inference partners (Fireworks, Together, Nebius, and others), with no service fees added by Hugging Face.
- **Inference Endpoints:** fully managed, dedicated GPU infrastructure for deploying any Hub model at production scale.

## Key features

- **smolagents:** a ~1,000-line Python library for code-first agentic workflows. `CodeAgent` writes tool invocations as executable Python (loops, conditionals, nested calls) rather than JSON schemas; `ToolCallingAgent` covers JSON-based tool calling. Both support sandboxed execution via Modal, E2B, Blaxel, or Docker. Tools can be pulled from any MCP server, LangChain, or a Hub Gradio Space. CLI utilities `smolagent` and `webagent` enable one-command agent runs.
- **Transformers:** the canonical model-definition framework for 1M+ Hub checkpoints. Backed by `Pipeline` (zero-shot inference for 50+ tasks), `Trainer` (mixed precision, FlashAttention, distributed training), and `generate` (streaming, beam search, speculative decoding). Acts as the pivot point across training frameworks (Axolotl, Unsloth, DeepSpeed, FSDP) and inference engines (vLLM, SGLang, TGI, llama.cpp, mlx).
- **TRL (Transformers Reinforcement Learning):** full-stack post-training library supporting SFT, GRPO (with vLLM co-location ⚡️), DPO, PPO, and reward modeling. TRL v1 (March 2026) is a major redesign. Integrates with PEFT, DeepSpeed, and Liger Kernel.
- **PEFT:** parameter-efficient fine-tuning methods (LoRA, QLoRA, IA³, prefix tuning) that make large-model fine-tuning feasible on consumer hardware.
- **Diffusers:** reference implementation of diffusion models (Stable Diffusion, SDXL, Flux) in PyTorch.
- **Datasets library:** streaming-capable, Arrow-backed dataset access with one-line Hub downloads.
- **Accelerate:** hardware-agnostic training launcher for multi-GPU, multi-node, TPU, and mixed-precision setups with minimal code changes.
- **Text Generation Inference (TGI):** production-grade LLM serving toolkit with continuous batching, tensor parallelism, quantization, and structured output.
- **Gradio:** Python library for building ML demo apps and web UIs in minutes; powers the Spaces ecosystem.
- **AutoTrain:** no-code / low-code model fine-tuning UI and API for classification, NER, summarization, and LLM fine-tuning.

## Architecture and concepts

The Hub is built on Git-based repositories backed by Xet storage — an intelligent chunking layer that deduplicates and accelerates large-file uploads/downloads across models, datasets, and Spaces. Every repository supports versioning, commit history, branches, and diffs.

smolagents follows a minimal design philosophy: the full agent loop fits in ~1,000 lines of Python. The `CodeAgent` paradigm treats tool invocations as first-class Python code executed in a sandboxed interpreter, enabling natural composability (functions calling functions, loops, error handling) without a custom DSL. Multi-agent pipelines are formed by composing `CodeAgent` instances as managed agents. Integration with the Hub means agents and tools can be published as Gradio Spaces and loaded with a single call.

Transformers centralizes model definitions so a single checkpoint is compatible with the full ecosystem: training frameworks load it, inference engines serve it, and neighboring libraries (PEFT, TRL, Accelerate) modify it in place. This "model-definition as pivot" architecture keeps the open-source stack interoperable at scale.

Inference Providers expose the same Hub model identifiers through partner inference APIs, so swapping from a local Transformers run to production cloud serving requires only changing the `InferenceClientModel` call target — the same interface smolagents uses.

## Main APIs

**smolagents quickstart:**
```python
from smolagents import CodeAgent, InferenceClientModel, DuckDuckGoSearchTool

model = InferenceClientModel()  # defaults to HF Inference API
agent = CodeAgent(tools=[DuckDuckGoSearchTool()], model=model)
result = agent.run("What is the current weather in Paris?")
```

**Switching models:**
```python
from smolagents import LiteLLMModel, TransformersModel
# OpenAI-compatible
model = LiteLLMModel(model_id="gpt-4")
# Local
model = TransformersModel(model_id="meta-llama/Llama-2-7b-chat-hf")
```

**Hub Python Library — push/pull:**
```python
from huggingface_hub import HfApi
api = HfApi()
api.upload_file(path_or_fileobj="model.bin", path_in_repo="model.bin", repo_id="my-org/my-model")
```

**Transformers Pipeline:**
```python
from transformers import pipeline
pipe = pipeline("text-generation", model="meta-llama/Llama-3.1-8B-Instruct")
result = pipe("Explain reinforcement learning in one sentence.")
```

## When to use

- Use **smolagents** when you need a lightweight, code-first agent framework without the abstraction overhead of LangChain or Anthropic's Managed Agents. Best fit for Python-native teams who want full control over the agent loop with minimal framework surface area.
- Use **Hub models + Inference Providers** when you want to swap between open-weight and proprietary models through a single API, or prototype rapidly before committing to a deployment target.
- Use **TRL + PEFT + Accelerate** when you need to fine-tune or post-train an open-weight model with RL methods (GRPO, DPO) on limited hardware.
- Use **Transformers + TGI** when self-hosting LLM inference at production scale with quantization, continuous batching, and structured output.
- Use **Spaces + Gradio** when you need to ship an ML demo quickly, integrate it into a multi-agent tool chain (Spaces can be used as smolagents tools), or share results with non-technical stakeholders.

## Ecosystem

Hugging Face integrates with most of the tools documented in this wiki:
- **smolagents ↔ LangChain:** smolagents can load LangChain tools directly via `Tool.from_langchain()`; both frameworks target the same open-weight model ecosystem.
- **Inference Providers ↔ agent frameworks:** any framework using an OpenAI-compatible endpoint (LangChain, smolagents, AutoGen) can point at an Inference Provider URL.
- **Transformers ↔ TGI / vLLM / SGLang:** Transformers defines the model; TGI and vLLM serve it at scale.
- **Hub ↔ Anthropic Models API:** Anthropic's Claude models are available through Hub-proxied Inference Providers, letting agent code use a single client regardless of backend.

Enterprise offering includes SSO, audit logs, resource groups, dedicated inference endpoints, and a managed private Hub deployment option.
