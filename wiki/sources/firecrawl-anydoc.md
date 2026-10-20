---
type: source
category: "Knowledge, RAG, memory & context"
source_url: https://github.com/firecrawl/anydoc
tags:
  - document-to-markdown
  - rust
  - llm-ingestion
  - pdf
  - office-docs
  - agent-skill
  - wasm
  - firecrawl
related:
  - firecrawl.dev
  - tavily.com
  - skills.sh
product: anydoc
detail_level: standard
created: 2026-10-20
updated: 2026-10-20
---

anydoc (~23k stars, MIT, v0.2.4) is Firecrawl's fast Rust library for converting Word, PowerPoint, Excel, OpenDocument, RTF, EPUB, CSV, and PDF into clean GitHub-Flavored Markdown — with Node.js, Python, and WebAssembly bindings plus an Agent Skill — so mixed office documents become consistent LLM-ready text in single-digit milliseconds.

_All claims below are sourced from ../../raw/github/firecrawl-anydoc.md unless otherwise noted._

## What it does

anydoc parses office/PDF bytes into a shared document model and renders one Markdown serializer for every format, so escaping, tables, heading anchors, and footnotes behave the same whether the input was a 2003 `.doc` or a fresh `.pptx`. It powers [Firecrawl Parse](https://firecrawl.dev/parse); the hosted API adds OCR for scanned pages that local conversion cannot read. A browser demo at https://firecrawl.github.io/anydoc/ runs the WASM build locally so files never leave the machine.

Supported formats: Word (`.doc`/`.docx`/`.docm`), PowerPoint (legacy + OOXML), Excel (`.xls`/`.xlsx`/`.xlsm`/`.xlsb`), OpenDocument (`.odt`/`.ods`/`.odp`), RTF, EPUB, CSV, PDF.

## Installation

```bash
# Agent Skill (Claude Code, Codex, Cursor, OpenCode, …)
npx skills add firecrawl/anydoc

# CLI (npx downloads a prebuilt binary; or npm install -g @firecrawl/anydoc)
npx @firecrawl/anydoc --help

# Language packages
npm install @firecrawl/anydoc          # Node
npm install @firecrawl/anydoc-wasm     # Browser WASM
pip install firecrawl-anydoc           # Python
cargo add anydoc                       # Rust
```

## Key features

- **One output for every format** — shared document model + single GFM serializer across 14 formats.
- **Full structure** — headings with anchors, emphasis, code, links/cross-refs, nested/task lists, tables (merged cells, header rows), block quotes, footnotes/endnotes, speaker notes.
- **Equations as LaTeX** — OMML (Word/PPT), MathML (ODF/EPUB), and RTF equations → `$...$` / `$$` GitHub math.
- **Embedded assets** — images/objects surface as alt text in Markdown; raw bytes stay on the document model with media types.
- **Content-based format detection** — PDF header, RTF open group, OLE streams, ZIP mimetype (CSV needs extension or explicit format).
- **Fast, local-first** — pure Rust, no ML models; median conversion under 5ms in their benchmark (4.4ms median, score 81 vs other converters).
- **Optional hosted OCR** — scanned/image-only PDFs fail with `NeedsOcr` locally; opt in (`--ocr hosted` / `ocr: 'hosted'`) to send the whole document to Firecrawl Parse. Rust crate never makes network calls.
- **Agent Skill** — `skills/convert-documents-to-markdown` teaches agents to use the anydoc CLI.

## Architecture

```
document bytes
  → format detection (content markers, not extension)
  → format parser (doc, docx, ppt, pptx, xls, xlsx, odt/ods/odp, rtf, epub, csv)
       → Document model (blocks, inlines, tables, footnotes, assets)
            → GFM serializer → Markdown
  PDF → pdf-inspector → Markdown directly
```

Node conversion runs on the libuv thread pool; Python releases the GIL. Errors are typed (`Unsupported`, `NeedsOcr`, `Malformed`, `Encrypted`, `ResourceLimit`, `MissingPart`, `Io`). Releases tag `v<version>` and publish crate + npm + PyPI from CI; version is kept in sync across `Cargo.toml`, `node/package.json`, and `python/Cargo.toml`.

## Example usage

```bash
npx @firecrawl/anydoc report.docx
npx @firecrawl/anydoc slides.pptx -o slides.md
npx @firecrawl/anydoc - --format csv < data.csv
npx @firecrawl/anydoc scan.pdf --ocr hosted   # needs Parse; FIRECRAWL_API_KEY for higher limits
```

```js
import { toMarkdown, toMarkdownBytes, toDocument } from '@firecrawl/anydoc';
const markdown = await toMarkdown('report.docx');
const withOcr = await toMarkdown('scan.pdf', { ocr: 'hosted' });
const fromBytes = await toMarkdownBytes(bytes, 'csv');
```

```python
import anydoc
markdown = anydoc.to_markdown("report.docx")
markdown = anydoc.to_markdown("scan.pdf", ocr="hosted")
document = anydoc.to_document(data)
```

```rust
let markdown = anydoc::to_markdown("report.docx")?;
let markdown = anydoc::to_markdown_bytes(&bytes, anydoc::Format::Csv)?;
let document = anydoc::to_document(&bytes, None)?;
```

## Maintenance status

- **Stars:** 22,980 (fetched 2026-10-20)
- **Latest release:** v0.2.4
- **Default branch:** `main` (pushed 2026-10-20)
- **License:** MIT
- **Language:** Rust (primary); Node, Python, WASM bindings
- **Homepage:** https://firecrawl.github.io/anydoc/
- Built by Firecrawl; CI publishes multi-language packages on version tags; fixture/robustness/fuzz tests under `tests/` and `fuzz/`
