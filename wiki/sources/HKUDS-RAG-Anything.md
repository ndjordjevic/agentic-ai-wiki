---
type: source
source_url: https://github.com/HKUDS/RAG-Anything
tags:
  - multimodal-rag
  - lightrag
  - knowledge-graph
  - document-parsing
  - mineru
  - python
  - vision-language-model
  - pdf-processing
related:
  - supermemory.ai
  - zilliztech-claude-context
  - reseek.net
  - graphify.net
  - cocoindex-io-cocoindex
product: rag-anything
detail_level: standard
created: 2026-07-01
updated: 2026-07-06
---

RAG-Anything is an open-source Python framework (21,717 stars, MIT, v1.3.1) from HKUDS that extends [LightRAG](https://github.com/HKUDS/LightRAG) into an all-in-one multimodal RAG pipeline: ingest PDFs, Office files, and images; parse them with MinerU/Docling/PaddleOCR; analyze images, tables, and equations with dedicated modal processors; build a multimodal knowledge graph; and query across text and non-text content through hybrid/local/global retrieval modes plus VLM-enhanced answers. It targets academic papers, technical docs, and enterprise knowledge bases where traditional text-only RAG loses tables, figures, and formulas.

_All claims below are sourced from ../../raw/github/HKUDS-RAG-Anything.md unless otherwise noted._

## What it does

RAG-Anything solves the gap between text-centric RAG and real-world documents that mix paragraphs, figures, tables, equations, and charts. The `RAGAnything` class orchestrates a multi-stage pipeline: high-fidelity document parsing (MinerU by default), concurrent multimodal content routing, specialized analyzers per modality, entity extraction into a LightRAG-backed knowledge graph, and hybrid retrieval that can attach images or equations to queries. Users can also bypass parsing entirely by inserting pre-parsed content lists from external parsers, or run batch folder ingestion with parallel workers.

## Installation

```bash
# PyPI (recommended)
pip install raganything
pip install 'raganything[all]'   # optional: image + text format extras

# From source with uv
git clone https://github.com/HKUDS/RAG-Anything.git
cd RAG-Anything
uv sync
uv run python examples/raganything_example.py --help
```

Prerequisites: Python 3.10+, an LLM API key (OpenAI-compatible), embedding model access, and MinerU for document parsing (`mineru --version`). Office formats (.doc/.docx/.ppt/.pptx/.xls/.xlsx) require LibreOffice installed on the host. Offline deployments must pre-cache `tiktoken` models via `TIKTOKEN_CACHE_DIR` because LightRAG pulls encodings on first use.

## Key features

- **End-to-end multimodal pipeline** — parse → analyze → graph → query in one `RAGAnything` API, eliminating separate tools for OCR, table extraction, and retrieval.
- **Universal document support** — PDFs, Office documents, images (with optional Pillow extras for BMP/TIFF/GIF/WebP), TXT/MD; parser selectable via `RAGAnythingConfig(parser="mineru"|"docling"|"paddleocr")`.
- **Modal processors** — `ImageModalProcessor`, `TableModalProcessor`, equation handling, and extensible `GenericModalProcessor` subclasses for custom modalities.
- **Context-aware processing** — surrounding text from the document is injected when analyzing images/tables/equations (`context_config.py`, configurable via `RAGAnythingConfig` and env vars) for semantically coherent captions.
- **Multimodal knowledge graph** — entity extraction and cross-modal relationships via LightRAG storage (`working_dir`); query modes `hybrid`, `local`, `global`, `naive`.
- **VLM-enhanced queries** — when `vision_model_func` is provided, retrieved image paths are base64-encoded and sent to a vision LLM for direct figure analysis during `aquery()`.
- **Direct content-list insertion** — skip MinerU parsing by inserting pre-parsed `content_list` JSON from external pipelines.
- **Batch processing** — `process_folder_complete()` with `max_workers`, tqdm progress, dry-run preview, and per-file error reporting.
- **Local model backends** — examples for LM Studio and vLLM integration; `env.example` documents full configuration surface.

## Architecture

The repo centers on the `raganything/` Python package built on LightRAG:

- **`raganything.py`** — `RAGAnything` facade: `process_document_complete()`, `process_folder_complete()`, `aquery()`, `aquery_with_multimodal()`, sync `query()`.
- **`parser.py`** — large parser integration layer (~105k LOC) bridging MinerU, Docling, and PaddleOCR; produces structured content lists and markdown.
- **`processor.py`** — document-level orchestration: routes parsed blocks through modal processors and into LightRAG indexing.
- **`modalprocessors.py`** — modality-specific LLM analysis (images via vision models, tables as structured markdown, equations as LaTeX) with entity/chunk creation.
- **`query.py`** — retrieval orchestration including multimodal query attachments and VLM enhancement flags.
- **`enhanced_markdown.py`** — richer markdown output from parsed multimodal documents.
- **`context_config.py` / `config.py`** — `RAGAnythingConfig` with parser selection, feature toggles (`enable_image_processing`, `enable_table_processing`, `enable_equation_processing`), and context-extraction modes.

Processing stages (from README architecture): **Document Parsing** (MinerU adaptive decomposition) → **Multi-Modal Content Understanding** (concurrent text + modal pipelines) → **Multimodal Analysis Engine** (visual/table/equation analyzers) → **Knowledge Graph Construction** (LightRAG entities/relations) → **Hybrid Intelligent Retrieval** (text + optional VLM over retrieved images). LightRAG now natively integrates RAG-Anything for multimodal RAG (per project news, June 2026).

## Example usage

```python
import asyncio
from functools import partial
from raganything import RAGAnything, RAGAnythingConfig
from lightrag.llm.openai import openai_complete_if_cache, openai_embed
from lightrag.utils import EmbeddingFunc

async def main():
    config = RAGAnythingConfig(
        working_dir="./rag_storage",
        parser="mineru",
        parse_method="auto",
        enable_image_processing=True,
        enable_table_processing=True,
        enable_equation_processing=True,
    )
    rag = RAGAnything(
        config=config,
        llm_model_func=lambda prompt, **kw: openai_complete_if_cache("gpt-4o-mini", prompt, api_key="...", **kw),
        vision_model_func=...,  # optional VLM for images
        embedding_func=EmbeddingFunc(embedding_dim=3072, max_token_size=8192, func=...),
    )
    await rag.process_document_complete("paper.pdf", output_dir="./output", parse_method="auto")
    result = await rag.aquery("What do the figures show?", mode="hybrid")
    mm_result = await rag.aquery_with_multimodal(
        "Explain this formula",
        multimodal_content=[{"type": "equation", "latex": r"E=mc^2"}],
        mode="hybrid",
    )

asyncio.run(main())
```

Batch folder ingestion: `await rag.process_folder_complete("./documents", output_dir="./output", file_extensions=[".pdf", ".docx"], max_workers=4)`.

## Maintenance status

Actively maintained by HKUDS (University of Hong Kong Data Science lab): last push 2026-06-15, latest release v1.3.1 (2026-05-21), 21,717 GitHub stars, 2,537 forks, MIT license. Technical report on arXiv ([2510.12323](http://arxiv.org/abs/2510.12323)). Published on PyPI as `raganything`. Community on Discord and WeChat. Troubleshooting guide in `docs/multimodal_rag_failure_modes.md` covers common OCR/table/layout issues before filing bugs.
