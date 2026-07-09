# GoogleCloudPlatform/knowledge-catalog

## Metadata
- Stars: 6522
- Primary language: HTML
- Default branch: main
- Latest release: (none)
- License: Apache License 2.0
- Homepage: https://cloud.google.com/products/knowledge-catalog
- Fetched: 2026-07-09
- Final URL: https://github.com/GoogleCloudPlatform/knowledge-catalog

## Description
Google Cloud Knowledge Catalog Tools and Samples. Knowledge Catalog (formerly Dataplex) is an AI-powered data catalog and metadata management platform providing a dynamic knowledge graph of all data — structured and unstructured — to supply semantics and business context to AI agents.

## README
# Knowledge Catalog

[Knowledge Catalog](https://cloud.google.com/products/knowledge-catalog) (formerly Dataplex), is an AI-powered data catalog and metadata management platform. It provides a dynamic knowledge graph of all your data, structured and unstructured, to provide semantics and business context to AI agents.

This repository features tools, agents, and samples that demonstrate Knowledge Catalog features, and building context management, enrichment and retrieval solutions.

## Getting Started

[![Open in Cloud Shell](http://gstatic.com/cloudssh/images/open-btn.svg)](https://console.cloud.google.com/cloudshell/editor?cloudshell_git_repo=https%3A%2F%2Fgithub.com%2FGoogleCloudPlatform%2Fknowledge-catalog.git)

## Contributing

See the contributing [instructions](CONTRIBUTING.md) to get started contributed.

## License

All solutions within this repository are provided under the [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) license. Please see [LICENSE](LICENSE.md) for more detailed terms and conditions.

## Disclaimer

This repository and its contents are not an official Google product.

## Docs

### okf/README.md (Open Knowledge Format)

# Open Knowledge Format (OKF)

> **This repository is primarily about the Open Knowledge Format (OKF).**
>
> OKF is a **universal, vendor-neutral format** for representing knowledge as plain markdown files with YAML frontmatter. It is **not tied to any particular agent, framework, model provider, or serving system**.

Goals:
- **Anyone can produce** OKF — humans authoring by hand, agents built on any framework (Google ADK, LangChain, custom), export pipelines from existing catalogs (Dataplex, Unity Catalog, Collibra, …), or scripts walking a database.
- **Anyone can serve and consume** OKF — a static file server, a knowledge-management UI (Obsidian, Notion, MkDocs), an LLM loading files into context, a search index, or a graph viewer.

**Why OKF?** OKF represents catalog knowledge as plain markdown files with YAML frontmatter, organized in a directory hierarchy:
- **Human- and agent-readable** without tooling.
- **Version-controllable** — bundles live in git.
- **Portable and lock-in free** — a bundle is a directory.
- **Mixes structured and unstructured data** — frontmatter for query fields, markdown body for prose LLMs read.
- **Minimally opinionated, freely extensible** — small required-key set ensures interoperability.
- **Composes with existing tooling** — Notion, Obsidian, MkDocs, Hugo, Jekyll.
- **Progressive disclosure built in** — auto-generated `index.md` files for one-level-at-a-time navigation.
- **Graph-shaped, not just tree-shaped** — concepts link to each other via markdown links.

**Reference agent** (proof-of-concept OKF producer):
- Runs in two passes: **BQ pass** (writes one OKF doc per concept using BigQuery metadata) and **web pass** (LLM-as-crawler that fetches seed URLs and enriches existing concepts).
- Hard `--web-max-pages` cap and same-domain allowed-hosts filter prevent runaway crawling.
- Output: `visualize` subcommand renders any OKF bundle as a self-contained interactive HTML file (Cytoscape.js force-directed graph, no backend needed).

Install:
```
python3.13 -m venv .venv
.venv/bin/pip install --index-url https://pypi.org/simple/ -e .[dev]
```

Credentials:
- BigQuery: `gcloud auth application-default login`; set billing project via `gcloud config set project <id>`.
- Gemini: set `GEMINI_API_KEY` or use Vertex AI with `GOOGLE_GENAI_USE_VERTEXAI=true`.

Minimum run:
```
.venv/bin/python -m reference_agent enrich \
    --source bq \
    --dataset <project>.<dataset> \
    --web-seed-file <path/to/seeds.txt> \
    --out ./bundles/<name>
```

Sample bundles (checked in):
- `bundles/ga4/` — GA4 e-commerce dataset
- `bundles/stackoverflow/` — Stack Overflow public dataset
- `bundles/crypto_bitcoin/` — Bitcoin blocks/transactions

### okf/SPEC.md (OKF Specification v0.1 — Draft, excerpt)

OKF is an open, human- and agent-friendly format for representing knowledge — the metadata, context, and curated insight that surrounds data and systems.

**Bundle:** A self-contained, hierarchical collection of knowledge documents. The unit of distribution. Can be distributed as a git repo, tarball, or subdirectory.

**Concept:** A single unit of knowledge. One markdown file. Represented by a YAML frontmatter block + markdown body.

**Required frontmatter field:**
- `type` — short string identifying the kind of concept (e.g. `BigQuery Table`, `API Endpoint`, `Metric`, `Playbook`). Not centrally registered; consumers must tolerate unknown types.

**Recommended fields:** `title`, `description`, `resource` (canonical URI), `tags`, `timestamp`.

Reserved filenames at any hierarchy level: `index.md` (directory listing) and `log.md` (update history).

### toolbox/README.md

**Toolbox** contains:
- **Metadata as Code** (`mdcode/`) — manage metadata in the form of source code artifacts that can be sync'd with Knowledge Catalog.
- **Enrichment Agent** (`enrichment/`) — ready-to-use agent and customizable harness to produce, evolve/improve, and maintain metadata within Knowledge Catalog, making it ready for consumption by agents.

### toolbox/enrichment/README.md

The enrichment agent provides a customizable agentic workflow for extracting information from various sources to build metadata about data assets used as agent context.

CLI tools: `kcmd` (metadata-as-code tool), `kcagent enrich` (enrichment runner).

```bash
kcmd init --bigquery-dataset <projectId>.<datasetId>
kcmd pull
kcagent enrich --catalog-path . --tools-path tools --prompt-path prompt.md
```

MCP integration: supports `md-fileset` MCP server with `list_fileset_contents`, `read_fileset_file`, `search_fileset_content` tools. SKILL.md-based agent skill discovery pattern used for tooling configuration.

### samples/README.md

Samples demonstrate the use of Knowledge Catalog to manage metadata and context to power agents:
- **Discovery** — building a search and discovery agent using the catalog's Search APIs.
- **Enrichment** — an enrichment agent that generates and enriches documentation for assets managed in the catalog.

## Top-level structure

```
.gitignore              — standard gitignore
CODE_OF_CONDUCT.md      — Google OSS code of conduct
CONTRIBUTING.md         — contribution guide
LICENSE.md              — Apache 2.0
README.md               — project overview
okf/                    — Open Knowledge Format specification + reference agent (primary contribution)
  SPEC.md               — OKF v0.1 draft specification
  README.md             — OKF overview, install, run, visualize docs
  bundles/              — pre-built OKF bundles (GA4, StackOverflow, Bitcoin)
  samples/              — per-dataset recipe directories
  src/                  — reference agent source code
  tests/                — test suite
  pyproject.toml        — Python package config
toolbox/                — tools for working with Knowledge Catalog metadata
  enrichment/           — enrichment agent (Node/npm, kcagent CLI, MCP-backed)
  mdcode/               — metadata-as-code tool (kcmd CLI)
samples/                — demo samples for discovery and enrichment
```
