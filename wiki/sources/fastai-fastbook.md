---
type: source
category: "Model infra, ML & providers"
source_url: https://github.com/fastai/fastbook
tags:
  - deep-learning
  - fastai
  - pytorch
  - jupyter-notebooks
  - ml-education
  - computer-vision
  - nlp
  - nbdev
related:
  - pytorch.org
  - huggingface.co
product: fastbook
detail_level: standard
created: 2026-07-02
updated: 2026-07-02
---

The fastai book (*Deep Learning for Coders with Fastai and PyTorch*) is the canonical open-source companion to Jeremy Howard and Sylvain Gugger's practical deep-learning course — 25k+ GitHub stars, published as 20 Jupyter notebooks plus appendices, backed by a free MOOC at course.fast.ai and an O'Reilly print edition. It teaches deep learning top-down through the fastai layered API on PyTorch, covering computer vision, tabular data, collaborative filtering, and NLP before diving into implementation details, convolutions, ResNets, optimizers, and the Learner/callback architecture. For agentic-AI practitioners, fastbook is foundational ML literacy: the same PyTorch and transformer/NLP building blocks that underpin modern LLM tooling, with a pedagogy optimized for coders who want working models before theory.

_All claims below are sourced from ../../raw/github/fastai-fastbook.md unless otherwise noted._

## What it does

fastbook is a notebook-first textbook and course artifact. Each chapter is a runnable Jupyter notebook (or Google Colab link) that walks through a complete deep-learning workflow — from training a pet-breed classifier in chapter 5 to building NLP models in chapters 10–12 and reconstructing fastai's `Learner` API in chapter 19. The repo is built with **nbdev** (`settings.ini` configures `nbs_path = .`, `doc_path = docs`, published to `https://fastai.github.io/fastbook/`). A `tools/clean.py` script exports "clean" notebook copies (stripping hidden cells and questionnaire sections) into the `clean/` directory for readers who want simplified versions.

## Installation

**Recommended for beginners — Google Colab:** open any chapter directly via Colab links in the README (no local Python setup required).

**Local conda environment:**

```bash
git clone https://github.com/fastai/fastbook.git
cd fastbook
conda env create -f environment.yml
conda activate fastbook
jupyter notebook
```

The `environment.yml` pulls from `fastai` and `pytorch` conda channels with `python>=3.6`, `pytorch>=1.6`, `torchvision`, and pip-installs `requirements.txt` (`fastai>=2.0.0`, `nbdev>=0.2.12`, `scikit_learn`, `sentencepiece`, etc.).

## Key features

- **20 progressive chapters** — intro and Jupyter basics → production deployment → AI ethics → MNIST → image classification (single- and multi-category) → sizing/TTA → collaborative filtering → tabular → NLP → mid-level data API → NLP deep dive → convolutions → ResNet → architecture details → optimizers/callbacks → mathematical foundations → GradCAM interpretability → Learner API internals → conclusion.
- **fastai 2.x layered API** — teaches through `fastai.vision.all`, tabular, collab, and text modules before peeling back to PyTorch primitives and fastai source.
- **Multiple access modes** — full notebooks in repo root, cleaned copies in `clean/`, free online subset at `fastai.github.io/fastbook2e/`, Colab one-click launch per chapter, and purchasable O'Reilly book.
- **Shared utilities (`utils.py`)** — common imports, plotting helpers, graphviz diagram generation, Bing/DuckDuckGo image search for dataset construction.
- **Internationalization** — localized README files (Spanish, Korean, Chinese, Bengali, Indonesian, Italian, Portuguese, Vietnamese, Japanese, Arabic, Turkish) and a `translations/` directory.
- **MOOC integration** — notebooks are the live course material for [course.fast.ai](https://course.fast.ai).

## Architecture

The repo follows the **nbdev notebook-as-library** pattern:

- **Source of truth = notebooks** — chapter `.ipynb` files in the repo root are both readable content and exportable code; `settings.ini` points nbdev at `nbs_path = .` with docs generated to `doc_path = docs` and hosted at `fastai.github.io/fastbook/`.
- **`utils.py`** — cross-chapter Python helpers imported by notebooks (fastai/torch/pandas setup, `plot_function`, image search APIs, graphviz `gv()` helper).
- **`tools/clean.py`** — post-processes notebooks for the `clean/` export: strips cell metadata tags (`# hide_input`, `# clean`, etc.), removes cells before the "Questionnaire" section, and writes simplified copies for readers.
- **`clean/`** — parallel directory of cleaned chapter notebooks with a symlinked `images/` folder.
- **Dependency stack** — fastai 2.x (high-level API) → PyTorch (tensor/autograd backend) → domain libraries (torchvision, sentencepiece for NLP tokenization).

Pedagogically, the book uses a **top-down then bottom-up** arc: early chapters train state-of-the-art models with few lines of fastai code; later chapters rebuild the training loop, data pipeline, and callback system from scratch so readers understand what the abstractions hide.

## Example usage

Open chapter 1 in Colab (no install):

```
https://colab.research.google.com/github/fastai/fastbook/blob/master/01_intro.ipynb
```

Or locally after conda setup:

```bash
conda activate fastbook
jupyter notebook 01_intro.ipynb
```

Generate cleaned notebook copies:

```bash
python tools/clean.py
# writes stripped notebooks to clean/
```

## Maintenance status

25,078 GitHub stars, 9,484 forks. Default branch `master`. Latest release **v0.0.19** (April 2022). Last push August 2024. Primary language: Jupyter Notebook. License: code (notebooks and `.py` files) under **GPL v3**; prose/markdown cells under custom copyright — redistribution and format changes restricted beyond private fork use; no commercial or broadcast use. Authors: Jeremy Howard and Sylvain Gugger (fast.ai). Companion O'Reilly book ISBN 9781492045526. Online chapters at `fastai.github.io/fastbook2e/`. Community contributions require copyright assignment to the authors.
