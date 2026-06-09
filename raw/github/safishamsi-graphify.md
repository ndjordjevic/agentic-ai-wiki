# safishamsi/graphify

## Metadata
- Stars: 63,681
- Primary language: Python
- Default branch: v8
- Latest release: v0.8.36 (2026-06-08)
- License: MIT License
- Homepage: https://graphifylabs.ai/
- Fetched: 2026-06-09
- Final URL: https://github.com/safishamsi/graphify

## Description
AI coding assistant skill (Claude Code, Codex, OpenCode, Cursor, Gemini CLI, and more). Turn any folder of code, SQL schemas, R scripts, shell scripts, docs, papers, images, or videos into a queryable knowledge graph. App code + database schema + infrastructure in one graph.

## README

Type `/graphify` in your AI coding assistant and it maps your entire project — code, docs, PDFs, images, videos — into a knowledge graph you can query instead of grepping through files.

Works in Claude Code, Codex, OpenCode, Kilo Code, Cursor, Gemini CLI, GitHub Copilot CLI, VS Code Copilot Chat, Aider, Amp, OpenClaw, Factory Droid, Trae, Hermes, Kimi Code, Kiro, Pi, Devin CLI, and Google Antigravity.

```
/graphify .
```

You get three files:
```
graphify-out/
├── graph.html       open in any browser — click nodes, filter, search
├── GRAPH_REPORT.md  the highlights: key concepts, surprising connections, suggested questions
└── graph.json       the full graph — query it anytime without re-reading your files
```

For a readable architecture page with Mermaid call-flow diagrams:
```bash
graphify export callflow-html
```

### Prerequisites
- Python 3.10+
- uv (recommended) or pipx

### Install
```bash
# Recommended:
uv tool install graphifyy

# Alternatives:
pipx install graphifyy
pip install graphifyy
```

Then register the skill:
```bash
graphify install
```

The PyPI package is `graphifyy` (double-y). The CLI is `graphify`.

### Platform support
Supports 24+ platforms: Claude Code, Codex, OpenCode, Kilo Code, Cursor, Gemini CLI, GitHub Copilot CLI, VS Code Copilot Chat, Aider, Amp, OpenClaw, Factory Droid, Trae, Trae CN, Hermes, Kimi Code, Kiro, Pi, Devin CLI, Google Antigravity, CodeBuddy.

Per-platform always-on install commands (e.g. `graphify claude install`, `graphify codex install`, `graphify cursor install`).

### Optional extras
| Extra | What it adds |
|---|---|
| `pdf` | PDF extraction |
| `office` | .docx and .xlsx support |
| `video` | Video/audio transcription (faster-whisper + yt-dlp) |
| `mcp` | MCP stdio server |
| `neo4j` | Neo4j push support |
| `leiden` | Leiden community detection (Python < 3.13 only) |
| `sql` | SQL schema extraction |
| `postgres` | Live PostgreSQL introspection |
| `terraform` | Terraform/HCL extraction |
| `ollama` | Ollama local inference |
| `openai` | OpenAI/OpenAI-compatible APIs |
| `gemini` | Google Gemini API |
| `anthropic` | Anthropic Claude API |
| `bedrock` | AWS Bedrock |
| `azure` | Azure OpenAI Service |
| `all` | Everything above |

### Supported file types
28 tree-sitter code grammars (.py, .ts, .js, .go, .rs, .java, .c, .cpp, .rb, .cs, .kt, .scala, .php, .swift, .lua, .zig, .ps1, .ex, .exs, .m, .mm, .jl, .vue, .svelte, .astro, .groovy, .dart, .f90, etc.), Salesforce Apex, Terraform/HCL, MCP configs, Markdown/MDX/HTML/YAML/TXT/RST, Office docs (.docx, .xlsx), PDFs, images (.png, .jpg, .webp, .gif), video/audio, YouTube/URLs.

### Key commands
```bash
/graphify .                        # build graph for current folder
/graphify ./docs --update          # re-extract only changed files
/graphify query "what connects auth to the database?"
/graphify path "UserService" "DatabasePool"
/graphify explain "RateLimiter"
/graphify add https://arxiv.org/abs/1706.03762   # fetch a paper
graphify hook install              # auto-rebuild on git commit
graphify prs                       # PR dashboard
graphify export callflow-html      # Mermaid architecture HTML
```

### Always-on integration
```bash
graphify claude install   # CLAUDE.md + PreToolUse hook
graphify codex install    # AGENTS.md + .codex/hooks.json
graphify cursor install   # .cursor/rules/graphify.mdc
graphify gemini install   # GEMINI.md + BeforeTool hook
```

### MCP server
```bash
python -m graphify.serve graphify-out/graph.json
# or HTTP:
python -m graphify.serve graphify-out/graph.json --transport http --port 8080
```
MCP tools: `query_graph`, `get_node`, `get_neighbors`, `shortest_path`, `list_prs`, `get_pr_impact`, `triage_prs`.

### Privacy
- Code files: processed locally via tree-sitter. Nothing leaves your machine.
- Video/audio: transcribed locally with faster-whisper.
- Docs, PDFs, images: sent to your AI assistant's model API. No raw source code sent.
- No telemetry, no usage tracking, no analytics.

### Penpax
Built on Graphify — [Penpax](https://graphifylabs.ai) is the always-on layer that applies the same graph approach to your entire working life: meetings, browser history, emails, files, and code, updating continuously in the background. Fully on-device. Free trial launching soon.

## Docs

### ARCHITECTURE.md

graphify is a Claude Code skill backed by a Python library. The skill orchestrates the library; the library can be used standalone.

**Pipeline:**
```
detect()  →  extract()  →  build_graph()  →  cluster()  →  analyze()  →  report()  →  export()
```

Each stage is a single function in its own module. They communicate through plain Python dicts and NetworkX graphs — no shared state, no side effects outside `graphify-out/`.

**Module responsibilities:**

| Module | Function | Input → Output |
|--------|----------|----------------|
| `detect.py` | `collect_files(root)` | directory → `[Path]` filtered list |
| `extract.py` | `extract(path)` | file path → `{nodes, edges}` dict |
| `build.py` | `build_graph(extractions)` | list of extraction dicts → `nx.Graph` |
| `cluster.py` | `cluster(G)` | graph → graph with `community` attr on each node |
| `analyze.py` | `analyze(G)` | graph → analysis dict (god nodes, surprises, questions) |
| `report.py` | `render_report(G, analysis)` | graph + analysis → GRAPH_REPORT.md string |
| `export.py` | `export(G, out_dir, ...)` | graph → Obsidian vault, graph.json, graph.html, graph.svg |
| `callflow_html.py` | `write_callflow_html(...)` | graphify-out files → Mermaid architecture/call-flow HTML |
| `ingest.py` | `ingest(url, ...)` | URL → file saved to corpus dir |
| `cache.py` | `check_semantic_cache / save_semantic_cache` | files → (cached, uncached) split |
| `security.py` | validation helpers | URL / path / label → validated or raises |
| `validate.py` | `validate_extraction(data)` | extraction dict → raises on schema errors |
| `serve.py` | `start_server(graph_path)` | graph file path → MCP stdio server |
| `watch.py` | `watch(root, flag_path)` | directory → writes flag file on change |
| `benchmark.py` | `run_benchmark(graph_path)` | graph file → corpus vs subgraph token comparison |

**Extraction output schema:**
```json
{
  "nodes": [
    {"id": "unique_string", "label": "human name", "source_file": "path", "source_location": "L42"}
  ],
  "edges": [
    {"source": "id_a", "target": "id_b", "relation": "calls|imports|uses|...", "confidence": "EXTRACTED|INFERRED|AMBIGUOUS"}
  ]
}
```

**Confidence labels:**
| Label | Meaning |
|-------|---------|
| `EXTRACTED` | Relationship is explicitly stated in the source (e.g., an import statement, a direct call) |
| `INFERRED` | Relationship is a reasonable deduction (e.g., call-graph second pass, co-occurrence in context) |
| `AMBIGUOUS` | Relationship is uncertain; flagged for human review in GRAPH_REPORT.md |

**Adding a new language extractor:**
1. Add `extract_<lang>(path: Path) -> dict` in `extract.py` following the existing pattern.
2. Register the file suffix in `extract()` dispatch and `collect_files()`.
3. Add the suffix to `CODE_EXTENSIONS` in `detect.py` and `_WATCHED_EXTENSIONS` in `watch.py`.
4. Add the tree-sitter package to `pyproject.toml` dependencies.
5. Add a fixture file to `tests/fixtures/` and tests to `tests/test_languages.py`.

## Top-level structure
```
.dockerignore
.gitattributes
.github/              — CI workflows
.gitignore
.pre-commit-config.yaml
AGENTS.md             — always-on instructions for Codex, OpenCode and other AGENTS.md-based assistants
ARCHITECTURE.md       — module breakdown, pipeline, extraction schema
CHANGELOG.md
Dockerfile
LICENSE               — MIT
README.md             — full installation and command reference
SECURITY.md           — threat model
docs/                 — how-it-works.md, docker-mcp-sqlite.md, translations/, superpowers/
graphify/             — Python library (detect, extract, build, cluster, analyze, report, export, serve, ...)
pyproject.toml
tests/                — unit tests (one file per module, no network calls)
tools/
uv.lock
worked/               — worked examples corpus outputs
```
