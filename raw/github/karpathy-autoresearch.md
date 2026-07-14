# karpathy/autoresearch

## Metadata
- Stars: 91053
- Primary language: Python
- Default branch: master
- Latest release: (none)
- License: MIT (per README; no LICENSE file detected by GitHub API)
- Homepage: (none)
- Fetched: 2026-07-14
- Final URL: https://github.com/karpathy/autoresearch

## Description
AI agents running research on single-GPU nanochat training automatically.

## README
# autoresearch

*One day, frontier AI research used to be done by meat computers in between eating, sleeping, having other fun, and synchronizing once in a while using sound wave interconnect in the ritual of "group meeting". That era is long gone. Research is now entirely the domain of autonomous swarms of AI agents running across compute cluster megastructures in the skies. The agents claim that we are now in the 10,205th generation of the code base, in any case no one could tell if that's right or wrong as the "code" is now a self-modifying binary that has grown beyond human comprehension. This repo is the story of how it all began. -@karpathy, March 2026*.

The idea: give an AI agent a small but real LLM training setup and let it experiment autonomously overnight. It modifies the code, trains for 5 minutes, checks if the result improved, keeps or discards, and repeats. You wake up in the morning to a log of experiments and (hopefully) a better model. The training code here is a simplified single-GPU implementation of [nanochat](https://github.com/karpathy/nanochat). The core idea is that you're not touching any of the Python files like you normally would as a researcher. Instead, you are programming the `program.md` Markdown files that provide context to the AI agents and set up your autonomous research org. The default `program.md` in this repo is intentionally kept as a bare bones baseline, though it's obvious how one would iterate on it over time to find the "research org code" that achieves the fastest research progress, how you'd add more agents to the mix, etc.

## How it works

The repo is deliberately kept small and only really has three files that matter:

- **`prepare.py`** — fixed constants, one-time data prep (downloads training data, trains a BPE tokenizer), and runtime utilities (dataloader, evaluation). Not modified.
- **`train.py`** — the single file the agent edits. Contains the full GPT model, optimizer (Muon + AdamW), and training loop. Everything is fair game: architecture, hyperparameters, optimizer, batch size, etc. **This file is edited and iterated on by the agent**.
- **`program.md`** — baseline instructions for one agent. Point your agent here and let it go. **This file is edited and iterated on by the human**.

By design, training runs for a **fixed 5-minute time budget** (wall clock, excluding startup/compilation), regardless of the details of your compute. The metric is **val_bpb** (validation bits per byte) — lower is better, and vocab-size-independent so architectural changes are fairly compared.

## Quick start

**Requirements:** A single NVIDIA GPU (tested on H100), Python 3.10+, uv.

```bash
# 1. Install uv project manager (if you don't already have it)
curl -LsSf https://astral.sh/uv/install.sh | sh

# 2. Install dependencies
uv sync

# 3. Download data and train tokenizer (one-time, ~2 min)
uv run prepare.py

# 4. Manually run a single training experiment (~5 min)
uv run train.py
```

## Running the agent

Simply spin up your Claude/Codex or whatever you want in this repo (and disable all permissions), then you can prompt something like:

```
Hi have a look at program.md and let's kick off a new experiment! let's do the setup first.
```

The `program.md` file is essentially a super lightweight "skill".

## Project structure

```
prepare.py      — constants, data prep + runtime utilities (do not modify)
train.py        — model, optimizer, training loop (agent modifies this)
program.md      — agent instructions
pyproject.toml  — dependencies
```

## Design choices

- **Single file to modify.** The agent only touches `train.py`. This keeps the scope manageable and diffs reviewable.
- **Fixed time budget.** Training always runs for exactly 5 minutes, regardless of your specific platform — approx 12 experiments/hour and approx 100 experiments while you sleep. This makes experiments directly comparable regardless of what the agent changes, and means autoresearch will find the most optimal model for your platform within that time budget. The downside: runs (and results) are not comparable to other people's other compute platforms.
- **Self-contained.** No external dependencies beyond PyTorch and a few small packages. No distributed training, no complex configs. One GPU, one file, one metric.

## Platform support

Currently requires a single NVIDIA GPU. CPU/MPS support is possible but not planned by the maintainer personally; forks are welcome. Tuning guidance for smaller compute (e.g. MacBooks): use a lower-entropy dataset such as the TinyStories GPT-4-generated short-story dataset, decrease `vocab_size` (down to a byte-level 256-vocab tokenizer if needed), lower `MAX_SEQ_LEN` in `prepare.py` (compensating with a slightly higher `DEVICE_BATCH_SIZE`), decrease `EVAL_TOKENS`, lower `DEPTH` (default 8) in `train.py`, use `WINDOW_PATTERN="L"` instead of the alternating banded-attention `"SSSL"` pattern, and lower `TOTAL_BATCH_SIZE` (keeping it a power of 2, e.g. down to ~16K).

## Notable forks

- miolini/autoresearch-macos (MacOS)
- trevin-creator/autoresearch-mlx (MacOS)
- jsegov/autoresearch-win-rtx (Windows)
- andyluo7/autoresearch (AMD)

## License

MIT

## Top-level structure
- `prepare.py` — fixed data-prep/tokenizer/runtime utilities (not modified by the agent)
- `train.py` — GPT model, optimizer, training loop (the single file the agent edits)
- `program.md` — agent-facing instructions ("research org" skill, human-edited)
- `analysis.ipynb` — notebook for inspecting experiment results
- `progress.png` — teaser/progress image used in the README
- `pyproject.toml`/`uv.lock` — Python dependencies (uv-managed)
- `.python-version` — pinned Python version
