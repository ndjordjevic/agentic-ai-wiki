---
type: source
category: "Coding-agent harnesses & methodologies"
source_url: https://github.com/karpathy/autoresearch
tags:
  - autonomous-agent-loop
  - ml-research-automation
  - nanochat
  - single-file-editing
  - fixed-time-budget
  - program-md
  - unattended-agent
related:
  - snarktank-ralph
  - frankbria-ralph-claude-code
  - coleam00-agent-control-plane
  - openai-symphony
product: autoresearch
detail_level: standard
created: 2026-07-14
updated: 2026-07-22
---

`autoresearch` is Andrej Karpathy's minimal harness for letting a coding agent run unattended overnight ML research: it edits one file (`train.py`, a single-GPU simplified [nanochat](https://github.com/karpathy/nanochat) implementation), trains for a fixed 5-minute wall-clock budget, checks whether `val_bpb` improved, keeps or discards the change, and repeats — roughly 12 experiments/hour, ~100 overnight. It's a smaller, single-purpose sibling of the "Ralph"-style autonomous-loop pattern (see [[snarktank-ralph]], [[frankbria-ralph-claude-code]]): instead of a general coding loop, the loop target is a narrow, measurable ML metric.

_All claims below are sourced from ../../raw/github/karpathy-autoresearch.md unless otherwise noted._

## What it does

The repo has exactly three files that matter: `prepare.py` (fixed, one-time data prep and runtime utilities — never modified), `train.py` (the GPT model, Muon+AdamW optimizer, and training loop — the only file the agent edits), and `program.md` (human-written instructions that give the agent its research-org context, deliberately kept as a bare-bones baseline). A human points a coding agent (Claude Code, Codex, etc., with permissions disabled) at `program.md` and prompts it to kick off an experiment; the agent then iterates on `train.py` autonomously.

## Installation

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh   # install uv
uv sync                                             # install deps
uv run prepare.py                                   # one-time data + tokenizer prep (~2 min)
uv run train.py                                      # single manual experiment (~5 min)
```

## Key features

- **Single file, single metric** — the agent only ever touches `train.py`, scored purely on `val_bpb` (validation bits-per-byte, vocab-size-independent), keeping diffs small and reviewable and architectural changes fairly comparable.
- **Fixed 5-minute time budget** — every experiment gets exactly 5 minutes of wall clock regardless of the underlying hardware, making runs on the *same* machine directly comparable across agent-proposed architecture/hyperparameter changes (at the cost of cross-machine comparability).
- **`program.md` as the tunable "research org code"** — the actual iteration surface for the human is the agent's instructions, not the training code; the README explicitly frames finding a better `program.md` (more agents, different strategy) as the real optimization target.
- **Self-contained** — no distributed training, no complex config system, dependencies limited to PyTorch and a few small packages.

## Architecture

Standard from-scratch GPT training loop (nanochat-derived): BPE tokenizer trained once in `prepare.py`, model/optimizer/training defined in `train.py`. Key tunables documented for smaller-compute forks: `vocab_size`, `MAX_SEQ_LEN` (traded against `DEVICE_BATCH_SIZE`), `EVAL_TOKENS`, `DEPTH` (default 8), `WINDOW_PATTERN` (`"L"` vs. the alternating banded-attention `"SSSL"`), and `TOTAL_BATCH_SIZE` (kept as a power of 2).

## Example usage

```
Hi have a look at program.md and let's kick off a new experiment! let's do the setup first.
```

## Maintenance status

91,053 stars, 13,071 forks, MIT (per README; no LICENSE file detected by the GitHub API), no tagged release, last pushed 2026-03-26 — a from-Karpathy reference repo rather than an actively iterated package. Requires a single NVIDIA GPU (tested on H100); the maintainer has not personally taken on CPU/MPS/multi-platform support, instead pointing to community forks: miolini/autoresearch-macos, trevin-creator/autoresearch-mlx, jsegov/autoresearch-win-rtx (Windows), andyluo7/autoresearch (AMD).
