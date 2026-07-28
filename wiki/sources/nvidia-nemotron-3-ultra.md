---
type: source
category: "Model infra, ML & providers"
source_url: https://decrypt.co/369689/nvidia-open-ai-model-nemotron-3-ultra
tags:
  - nemotron
  - open-weight-models
  - mixture-of-experts
  - nvidia
  - agentic-performance
  - inference-speed
  - long-context
  - open-source-ai
related:
  - litellm.ai
  - openrouter.ai
  - huggingface.co
  - nvidia.com
product: nvidia-nemotron-3-ultra
detail_level: standard
created: 2026-06-03
updated: 2026-07-28
---

Decrypt news coverage of Nvidia's Computex 2026 launch of Nemotron 3 Ultra — a 550B-parameter (55B active) open-weight mixture-of-experts model positioned as the top U.S. open model for agentic workloads, with public weights, released training recipes, 1M-token context, and 300+ tokens/sec inference on DeepInfra — while still trailing Moonshot AI's Kimi K2.6 on Artificial Analysis's Intelligence Index.

_All claims below are sourced from ../../raw/web/nvidia-nemotron-3-ultra.md unless otherwise noted._

## What it does

Reports Jensen Huang's June 1, 2026 Computex keynote unveiling of Nemotron 3 Ultra as Nvidia's largest open AI model to date. The article frames it as the smartest open-weight model built in America at launch, benchmarked by Artificial Analysis at 48 on a composite Intelligence Index (reasoning, coding, general knowledge, and agentic performance), ahead of other U.S. open options (Gemma 4 31B at 39, Nemotron 3 Super at 36, OpenAI gpt-oss-120b at 33) but behind China's Kimi K2.6 at 54.

## Key features

- **Mixture-of-experts scale:** ~550B total parameters with ~55B active per forward pass; Nvidia claims ~5× faster inference and ~30% lower cost versus comparable open-weight alternatives.
- **Hybrid architecture:** Mamba-2 layers plus standard Transformer attention plus MoE routing across the Nemotron 3 family (Nano, Super, Ultra).
- **Long context:** 1M-token context window — positioned for agents holding full codebases or large document sets in one pass.
- **Multi-token prediction (MTP):** predicts multiple future tokens per step to accelerate generation.
- **Agent-oriented post-training:** reinforcement learning across interactive environments to teach multi-step planning and execution, not only Q&A.
- **Open release:** public weights and training recipes; datacenter-scale self-hosting expected, with access via Nvidia API and cloud providers.
- **Inference speed:** 300+ output tokens/sec on a pre-release DeepInfra endpoint vs. 50–100 tok/s cited for DeepSeek V4 Pro and Kimi K2.6 commercial APIs.
- **Roadmap:** Nemotron 4 in development via the Nemotron Coalition (eight labs including Mistral AI and Perplexity) on DGX Cloud; Ultra shipping June 4, 2026.

## Architecture and concepts

The Nemotron line dates to November 2023 (first Nemotron-branded model); generation 3 was announced December 2025. Three tiers — Nano (lightweight), Super (mid-range enterprise), Ultra (complex reasoning) — share the same hybrid Mamba-2 + attention + MoE stack. Mamba-2 is described as a lower-cost alternative to standard attention for long sequences, supporting the 1M context claim. MoE is explained as activating only relevant "expert" subnetworks per token, decoupling serving cost from headline parameter count.

Artificial Analysis partnered with Nvidia on pre-release evaluation; the article treats its Intelligence Index as the primary cross-model intelligence comparison, with a separate emphasis on throughput for agent loops where step latency compounds.

## Main APIs

Not a product docs page — access paths mentioned in coverage:

- **Nvidia API** and **cloud providers** for hosted use without owning datacenter hardware.
- **DeepInfra** pre-release endpoint used for the 300+ tok/s measurement cited in the article.

For unified routing to many providers (including NVIDIA NIM), see [[litellm.ai]] and [[openrouter.ai]] in this wiki.

## When to use

Relevant when choosing an open-weight backbone for autonomous agents that need long context, competitive U.S.-origin open licensing, and high inference throughput — with the caveat that intelligence benchmarks in the article still favor Kimi K2.6 and proprietary frontier models (Anthropic, Google, OpenAI tied at 57). Nemotron 3 Super (March 2026, 120B) is noted as already viable for autonomous agents; Ultra adds a large index jump (+12 vs Super). Fits stacks that route open models through gateways ([[litellm.ai]], [[openrouter.ai]]) or host weights from hubs ([[huggingface.co]]).

## Ecosystem

Nvidia's $26B five-year open-weight AI bet is positioned against rising Chinese open-model share (~1.2% → ~30% of global open-model usage, late 2024–end 2025 per Decrypt's prior reporting). Nemotron Coalition partners include Mistral AI and Perplexity. Competitors cited: Kimi K2.6 (Moonshot AI), DeepSeek V4 Pro, U.S. open models from Google and OpenAI. No companion GitHub repo was ingested with this article-only source.
