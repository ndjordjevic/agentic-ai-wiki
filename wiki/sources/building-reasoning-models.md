---
type: source
category: "Model infra, ML & providers"
source_url: https://magazine.sebastianraschka.com/p/building-reasoning-models
companion_urls:
  - https://github.com/rasbt/reasoning-from-scratch
raw_files:
  - ../../raw/web/building-reasoning-models.md
  - ../../raw/github/rasbt-reasoning-from-scratch.md
tags:
  - reasoning-models
  - inference-time-scaling
  - rlvr
  - grpo
  - distillation
  - pytorch
  - math-500
  - qwen3
related:
  - coding-llms-from-the-ground-up
  - pytorch.org
  - fastai-fastbook
  - rohitg00-ai-engineering-from-scratch
product: building-reasoning-models
detail_level: standard
created: 2026-11-04
updated: 2026-11-04
studied: true

---

Sebastian Raschka's *Building Reasoning Models from the Ground Up* is an eight-video (~11h) PyTorch coding course that starts from a pre-trained Qwen3 base model and implements evaluation, inference-time scaling, reinforcement learning with verifiable rewards (RLVR / GRPO), and distillation — the companion video track to his book *Build a Reasoning Model (From Scratch)* and the official `rasbt/reasoning-from-scratch` repo (~5.8k★). For this wiki it is the clearest hands-on map of how a conventional LLM becomes the *engine* inside an agent harness: reasoning post-training and test-time compute sit under the harness's context/tool layer rather than replacing it.

_All claims below are sourced from ../../raw/web/building-reasoning-models.md unless otherwise noted._

## What it does

The Substack post packages eight lecture videos that walk through coding reasoning methods on a small Qwen3 0.6B model: environment setup, text generation with KV cache / `torch.compile`, a MATH-500 answer verifier, sampling and self-consistency, scoring and self-refinement, a simplified GRPO training loop for RLVR, GRPO extras (clipping, KL, format rewards), and distillation from a stronger teacher (DeepSeek R1 traces). It also spells out the engine analogy: conventional LLM → reasoning model (RLVR + optional inference scaling) → agent harness (context management + tools). Optional preview: a ~90-minute LinkedIn Learning conceptual course on the same themes.

## Key features

- **Eight coding lectures (~11 hours)** covering motivation/setup through distillation, each paired with chapter code under `rasbt/reasoning-from-scratch`.
- **Starts from pre-trained weights** (Qwen3) so the course focuses on evaluation, test-time compute, RL, and distillation rather than pretraining a base model.
- **MATH-500 verifier** used both for evaluation and as the RLVR reward signal.
- **Inference-time scaling** — temperature / multinomial / top-p sampling, self-consistency (majority vote), log-prob scoring, and self-refinement critique/revise loops.
- **RLVR via simplified GRPO** — group sampling, relative advantages, clipped policy ratios, KL terms, format rewards, checkpoint eval.
- **Distillation path** — hard/soft and on-/off-policy variants; teacher-generated MATH answers; supervised answer-token training.
- **Book + repo companion** — Manning/Amazon *Build a Reasoning Model (From Scratch)*; Apache-2.0 GitHub with chapter notebooks, appendices (Qwen3 source, larger LLMs, batching, evaluation, chat UI), and CI across Linux/macOS/Windows. (../../raw/github/rasbt-reasoning-from-scratch.md)

## Architecture

The pedagogical stack is layered: (1) load a small open base LLM and make generation efficient (KV cache, compile); (2) build a math verifier that extracts, normalizes, and equivalence-checks answers; (3) spend extra inference compute without weight updates (sampling diversity → aggregation / refinement); (4) update weights with RLVR using verifier rewards and GRPO-style relative advantages; (5) optionally distill a stronger teacher's reasoning traces into the small student. The article's engine analogy places this stack under agent harnesses: the harness owns tools and context; the reasoning model is the improved engine. Repo layout mirrors book chapters `ch02`–`ch08` plus appendices `chC`–`chG`, with an installable `reasoning_from_scratch` package. (../../raw/github/rasbt-reasoning-from-scratch.md)

## Installation

```bash
git clone --depth 1 https://github.com/rasbt/reasoning-from-scratch.git
cd reasoning-from-scratch
# Chapter 2 / setup tips cover uv, CUDA vs Apple Silicon, and remote GPU + VS Code
```

Early text-generation and evaluation work on CPU; later training chapters recommend a GPU. See `ch02/02_setup-tips/` and `troubleshooting.md` in the repo. (../../raw/github/rasbt-reasoning-from-scratch.md)

## Example usage

Lecture ↔ chapter mapping (YouTube + repo paths from the article):

1. Motivation and code setup — [video](https://www.youtube.com/watch?v=Kh9mqTzjuEQ) · `ch02/02_setup-tips`
2. Loading base model, generation, KV caching — [video](https://www.youtube.com/watch?v=BJua0yjO5dk) · `ch02`
3. Verifier for evaluation / RLVR — [video](https://www.youtube.com/watch?v=JQJ_8_jSAoY) · `ch03`
4. Inference scaling: sampling & self-consistency — [video](https://www.youtube.com/watch?v=t5y-kS9nNxU) · `ch04`
5. Inference scaling: scoring & self-refinement — [video](https://www.youtube.com/watch?v=TVMyOJ_3Gxo) · `ch05`
6. RL: simplified GRPO for RLVR — [video](https://www.youtube.com/watch?v=237Hf7Q3lgg) · `ch06`
7. RL: clipping, KL, format rewards — [video](https://www.youtube.com/watch?v=VxfUrUrrczs) · `ch07`
8. Distilling a reasoning model — [video](https://www.youtube.com/watch?v=msp69FR5NZs) · `ch08`

Suggested study loop from the article: read the matching book chapter, code along with the video, then try the exercises. (../../raw/github/rasbt-reasoning-from-scratch.md)

## When to use

Use when you need a concrete, code-first understanding of modern reasoning-model techniques (test-time compute, RLVR/GRPO, distillation) and how they relate to agent harnesses — especially if you already know Python/PyTorch and want implementations rather than survey slides. Prior [[coding-llms-from-the-ground-up]] / *Build an LLM from Scratch* content is recommended but not required. Not a drop-in agent framework; it trains the model that frameworks wrap.

## Maintenance status

Companion repo `rasbt/reasoning-from-scratch`: ~5,775★, 925 forks, Apache-2.0, default branch `main`, latest release **v1.0** (2026-05-18), primary language Jupyter Notebook, homepage Manning book link; CI test badges for Linux/macOS/Windows. Article published 2026-10-24 on Ahead of AI. (../../raw/github/rasbt-reasoning-from-scratch.md)

## Ecosystem

Sequel to [[coding-llms-from-the-ground-up]] and `rasbt/LLMs-from-scratch`. Cross-links Raschka's *Components of a Coding Agent* Substack article for the harness side of the engine analogy. Adjacent education sources in this wiki: [[pytorch.org]], [[fastai-fastbook]], [[rohitg00-ai-engineering-from-scratch]]. Book: Manning / Amazon *Build a Reasoning Model (From Scratch)* (ISBN 9781633434677).
