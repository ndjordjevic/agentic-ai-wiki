---
type: source
source_url: https://github.com/GoogleCloudPlatform/knowledge-catalog
tags:
  - knowledge-catalog
  - data-catalog
  - metadata-management
  - open-knowledge-format
  - okf
  - agent-context
  - enrichment-agent
  - google-cloud
  - bigquery
  - dataplex
related:
  - adk.dev
  - cocoindex-io-cocoindex
  - HKUDS-RAG-Anything
  - coleam00-cole-medin-ai-coding
product: knowledge-catalog
detail_level: standard
created: 2026-07-09
updated: 2026-07-09
---

`GoogleCloudPlatform/knowledge-catalog` is the official Google Cloud sample and tooling repository for **Knowledge Catalog** (formerly Dataplex) — an AI-powered data catalog and metadata management platform. Its primary contribution is the **Open Knowledge Format (OKF)**, a vendor-neutral specification for representing any knowledge as plain markdown files with YAML frontmatter that any agent, human, or tool can read and produce without bespoke SDKs. The repo also ships a reference enrichment agent, a metadata-as-code toolbox, and discovery/enrichment samples that show how to build agent context management pipelines on top of the catalog.

_All claims below are sourced from ../../raw/github/GoogleCloudPlatform-knowledge-catalog.md unless otherwise noted._

## What it does

Knowledge Catalog provides a dynamic knowledge graph over all data — structured (BigQuery tables, datasets) and unstructured (docs, references) — supplying the semantics and business context AI agents need at inference time. The repository demonstrates three interrelated use-cases: (1) producing OKF knowledge bundles via agentic pipelines, (2) managing catalog metadata as version-controlled code, and (3) enriching existing catalog entries with agent-generated documentation.

## Key features

- **Open Knowledge Format (OKF) v0.1 specification** — a universal markdown+YAML frontmatter directory format for knowledge bundles; not tied to any framework, model provider, or storage system. Concepts are single `.md` files; a bundle is a directory tree. Required frontmatter field is `type`; all other fields are recommended or producer-defined.
- **Reference OKF agent** — two-pass pipeline: a BigQuery pass writes one OKF concept doc per dataset entity, then a web pass runs the LLM as a crawler against seed URLs to enrich those docs. Includes a hard `--web-max-pages` cap and same-domain allowed-hosts filter to prevent runaway crawling.
- **Visualizer** — `reference_agent visualize` renders any OKF bundle as a self-contained interactive HTML file (Cytoscape.js force-directed graph) with no backend required; supports search, type filters, and backlink panels.
- **Metadata-as-code toolbox** (`kcmd`) — CLI that initialises, pulls, and syncs catalog snapshots to/from local YAML/markdown files; underpins the enrichment agent.
- **Enrichment agent** (`kcagent enrich`) — customizable agentic harness that reads a catalog snapshot and produces/evolves metadata by calling MCP-backed tools including an `md-fileset` server for navigating local markdown knowledge bases.
- **Pre-built sample bundles** — GA4 e-commerce, Stack Overflow, and Bitcoin public BigQuery datasets converted to browsable OKF bundles checked into the repo.

## Architecture

The repo is organized into three top-level modules:

- **`okf/`** — the OKF specification (`SPEC.md`) and the reference agent (`src/`). The agent is a Python package installable via `pip -e .[dev]`. Credentials: BigQuery via ADC, Gemini via `GEMINI_API_KEY` or Vertex AI env vars. Sample bundles live in `bundles/`; per-dataset recipes in `samples/`.
- **`toolbox/`** — two Node/npm tools: `mdcode/` (the `kcmd` metadata-as-code CLI) and `enrichment/` (the `kcagent` enrichment runner, MCP-integrated). The enrichment agent discovers agent skills from `SKILL.md` files in a `tools/skills/` directory — the same SKILL.md pattern used by superpowers and other agent skill systems.
- **`samples/`** — lightweight sample projects for catalog discovery (search-and-discovery agent on top of Knowledge Catalog Search APIs) and catalog enrichment (enrichment agent demo).

## Installation

**OKF reference agent (Python):**
```bash
python3.13 -m venv .venv
.venv/bin/pip install --index-url https://pypi.org/simple/ -e .[dev]
# BigQuery creds
gcloud auth application-default login && gcloud config set project <id>
# Gemini creds
export GEMINI_API_KEY=<key>   # or use Vertex AI env vars
```

**Toolbox (Node):**
```bash
cd toolbox/enrichment && npm install && npm run build
```

## Example usage

Run the reference enrichment agent against a BigQuery dataset:
```bash
.venv/bin/python -m reference_agent enrich \
    --source bq \
    --dataset <project>.<dataset> \
    --web-seed-file seeds.txt \
    --out ./bundles/<name>
```

Iterate on a single concept:
```bash
.venv/bin/python -m reference_agent enrich \
    --source bq --dataset <project>.<dataset> \
    --concept tables/events_ --out ./bundles/<name>
```

Visualize a bundle:
```bash
.venv/bin/python -m reference_agent visualize --bundle ./bundles/<name>
```

Metadata-as-code + enrichment toolbox:
```bash
kcmd init --bigquery-dataset <projectId>.<datasetId>
kcmd pull
kcagent enrich --catalog-path . --tools-path tools --prompt-path prompt.md
```

## When to use

- Building agent context pipelines on top of BigQuery or Dataplex/Knowledge Catalog data assets.
- Adopting a vendor-neutral, git-native format for sharing knowledge corpora across teams, tools, or organizations.
- Enriching catalog metadata automatically with an LLM agent rather than manually.
- Prototyping an OKF consumer (viewer, search index, downstream agent) — the pre-built bundles and visualizer provide a ready environment.
- Running a metadata-as-code workflow where catalog snapshots are treated like source code with PRs and diffs.

## Maintenance status

6,522 stars · Apache 2.0 · Primary language: HTML · No formal release tags · Last pushed June 2026. Not an official Google product. Actively maintained by Google Cloud engineers. Contributions follow the standard Google OSS CONTRIBUTING.md guide.

## Ecosystem

OKF is designed to compose with any knowledge toolchain: Obsidian, Notion, MkDocs, Hugo, and Jekyll can all render OKF bundles natively since they already consume markdown+YAML frontmatter. The reference agent supports Google ADK (see [[adk.dev]]) as an agent runtime and Gemini / Vertex AI as the model layer. The enrichment agent uses the MCP `md-fileset` server pattern. For incremental data pipeline alternatives that also target agent context, see [[cocoindex-io-cocoindex]]; for graph-based RAG over knowledge corpora, see [[HKUDS-RAG-Anything]].
