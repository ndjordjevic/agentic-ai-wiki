---
type: source
category: "Model infra, ML & providers"
source_url: https://magazine.sebastianraschka.com/p/coding-llms-from-the-ground-up
companion_urls:
  - https://github.com/rasbt/LLMs-from-scratch
raw_files:
  - ../../raw/web/coding-llms-from-the-ground-up.md
  - ../../raw/github/rasbt-LLMs-from-scratch.md
tags:
  - llms-from-scratch
  - attention
  - pretraining
  - instruction-tuning
  - pytorch
  - gpt
  - tokenization
  - bpe
related:
  - building-reasoning-models
  - pytorch.org
  - fastai-fastbook
  - rohitg00-ai-engineering-from-scratch
product: coding-llms-from-the-ground-up
detail_level: standard
created: 2026-11-04
updated: 2026-11-04
---

Sebastian Raschka's *Coding LLMs from the Ground Up* is a ~15-hour PyTorch video course that implements a ChatGPT-like LLM from scratch — tokenization and BPE, attention, GPT architecture, pretraining, classification finetuning, and instruction finetuning — as the companion track to *Build a Large Language Model (From Scratch)* and the widely used `rasbt/LLMs-from-scratch` repo (~108k★). For this wiki it is the foundational "how the engine is built" course that [[building-reasoning-models]] then extends into reasoning post-training and test-time compute.

_All claims below are sourced from ../../raw/web/coding-llms-from-the-ground-up.md unless otherwise noted._

## What it does

The Substack post collects seven main coding lectures (~15h total; ~5× longer than Raschka's earlier 3-hour workshop) that walk through building an LLM in Python/PyTorch without relying on external LLM libraries for the core path. Videos were recorded as book supplements but work as standalone content. A paid-subscriber bonus (~2.5h) surveys the LLM landscape from GPT-2-era 2018 through early 2025 (post–Llama 4). The pedagogical pitch: build a go-kart before a Formula 1 car — implement the mechanisms so you understand what production stacks abstract away.

## Key features

- **~15 hours of coding lectures** from environment setup through instruction finetuning.
- **From-scratch stack** — text prep (tokenization, BPE, dataloaders), self/causal/multi-head attention, GPT-style architecture, unlabeled pretraining, classification finetune, instruction finetune.
- **Official code repo** `rasbt/LLMs-from-scratch` with chapter notebooks, exercise solutions, appendices (PyTorch intro, LoRA PEFT, training-loop extras), and extensive chapter-5 bonus material (Llama/Qwen/Gemma/Olmo from-scratch ports, MoE, KV-cache variants, etc.). (../../raw/github/rasbt-LLMs-from-scratch.md)
- **Setup via uv** — `uv pip` / optional `uv add`; Windows note to skip TensorFlow when loading original GPT-2 weights, with Hugging Face PyTorch weights at `rasbt/gpt2-from-scratch-pytorch` as alternative.
- **Manning live video** — separate ~17h 15m "Master and Build Large Language Models" course mirroring book chapters. (../../raw/github/rasbt-LLMs-from-scratch.md)
- **Sequel path** — points forward to *Build a Reasoning Model (From Scratch)* / [[building-reasoning-models]].

## Architecture

Course arc matches the book mental model: data → attention → GPT module stack → pretrain on unlabeled text → specialize (classification, then instruction following). The repo's main chapters are `ch01`–`ch07` with appendices A–E; bonus trees under later chapters re-implement modern architecture pieces (GQA, MLA, MoE, sliding-window attention, etc.) once the baseline GPT is solid. Hardware target is conventional laptops; GPUs used automatically when present. (../../raw/github/rasbt-LLMs-from-scratch.md)

## Installation

```bash
git clone https://github.com/rasbt/LLMs-from-scratch.git
cd LLMs-from-scratch
# setup/ covers Python, uv, and optional Docker; see troubleshooting.md
```

Article tip: on Windows, remove the TensorFlow line from requirements if GPT-2 TF weight loading fails, and use the Hugging Face PyTorch weight mirror for video 5. (../../raw/github/rasbt-LLMs-from-scratch.md)

## Example usage

Main lecture list from the article (durations as published):

1. Set up your code environment (0:21:01) — uv; GPT-2 weight caveats
2. Working with text data (1:28:01) — tokenization, BPE, dataloaders
3. Coding attention mechanisms (2:15:40) — self-, causal, multi-head attention
4. Coding an LLM architecture — GPT model from scratch
5. Pretraining on Unlabeled Data (2:36:44)
6. Finetuning for Classification (2:15:29) — spam classifier intro
7. Instruction Finetuning (1:46:04)

Work chapter notebooks under `ch02`–`ch07` alongside each video; exercise solutions live in the same chapter folders. (../../raw/github/rasbt-LLMs-from-scratch.md)

## When to use

Use when you want a durable, code-first mental model of how base LLMs are built and finetuned in PyTorch — especially before (or alongside) agent/harness work that treats the model as a black box. Pairs with [[pytorch.org]] literacy and curricula like [[fastai-fastbook]] / [[rohitg00-ai-engineering-from-scratch]]. Continue to [[building-reasoning-models]] for RLVR, inference scaling, and distillation. Some Substack video embeds may require a paid subscription; the GitHub notebooks remain openly available.

## Maintenance status

Companion repo `rasbt/LLMs-from-scratch`: ~107,796★, 16,654 forks, Apache-2.0 (`LICENSE.txt`), default branch `main`, no GitHub Release tag at fetch time, primary language Jupyter Notebook, homepage Amazon book link; actively maintained with large bonus-material surface. Article published 2025-05-10 on Ahead of AI. (../../raw/github/rasbt-LLMs-from-scratch.md)

## Ecosystem

Canonical book *Build a Large Language Model (From Scratch)* (Manning/Amazon); sequel [[building-reasoning-models]] / `rasbt/reasoning-from-scratch`. Adjacent wiki education sources: [[pytorch.org]], [[fastai-fastbook]], [[rohitg00-ai-engineering-from-scratch]]. Hugging Face weight mirror for GPT-2-from-scratch PyTorch tensors supports the pretraining chapter without TensorFlow.
