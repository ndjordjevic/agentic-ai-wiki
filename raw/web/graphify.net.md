# graphify.net

## Fetch log
- Inbox URL: https://graphify.net/
- Final URL: https://graphify.net/
- Fetched: 2026-06-09
- Pages: 7
- Mode: standard

## llms.txt — https://graphify.net/llms.txt
# Graphify

> Graphify is an open-source knowledge graph skill for AI coding assistants (Claude Code, Codex, OpenCode, OpenClaw, Factory Droid). It turns code, docs, papers and diagrams into a queryable graph built with Tree-sitter AST extraction, NetworkX, and Leiden community detection — no embeddings, no vector store, no server. Average query cost on a mixed 52-file corpus is ~1.7k tokens vs ~123k raw (71.5× reduction). MIT licensed.

## Core pages

- [Graphify homepage](https://graphify.net/): overview, features, install, architecture pipeline, worked examples, FAQ.
- [Knowledge Graphs for AI Coding Assistants](https://graphify.net/knowledge-graph-for-ai-coding-assistants.html): why structural graphs beat vector RAG for code understanding; god nodes, rationale nodes, hyperedges, provenance tagging.
- [Tree-sitter AST Extraction](https://graphify.net/tree-sitter-ast-extraction.html): deterministic local pass across 19 languages (Python, JS, TS, Go, Rust, Java, C, C++, Ruby, C#, Kotlin, Scala, PHP, Swift, Lua, Zig, PowerShell, Elixir, Objective-C); extracts classes, functions, call graphs, imports, docstrings and rationale comments.
- [Leiden Community Detection](https://graphify.net/leiden-community-detection.html): clustering over graph topology alone via graspologic; semantic similarity edges from the LLM pass feed into Leiden without a separate vector index.
- [Graphify + Claude Code Integration](https://graphify.net/graphify-claude-code-integration.html): `graphify claude install` writes a CLAUDE.md directive and a PreToolUse hook so Claude reads GRAPH_REPORT.md before every Glob/Grep; AGENTS.md equivalent for Codex, OpenCode, OpenClaw, Factory Droid.
- [CLI Command Reference](https://graphify.net/graphify-cli-commands.html): every `/graphify` and `graphify` command — build, update, watch, query, path, explain, add, wiki, svg, graphml, neo4j, mcp, hook install.
- [Graphify vs Alternatives](https://graphify.net/graphify-vs-alternatives.html): honest comparison to Sourcegraph, Code2Vec, and Neo4j.

## Install

```
pip install graphifyy && graphify install
/graphify .
```

Requires Python 3.10+ and one supported AI coding assistant. The PyPI package is named `graphifyy`; the CLI is `graphify`.

## Key facts

- License: MIT
- Author: Safi Shamsi
- Repo: https://github.com/safishamsi/graphify
- PyPI: https://pypi.org/project/graphifyy/
- Tech stack: NetworkX, graspologic (Leiden), Tree-sitter, vis.js. No Neo4j required, no server, runs entirely locally.
- Privacy: source code never leaves the machine (AST pass is local); only semantic descriptions of docs/papers/images are sent to the model API your assistant is already using. No telemetry.
- Outputs: `graphify-out/graph.html` (interactive), `GRAPH_REPORT.md` (audit), `graph.json` (persistent, queryable), `cache/` (SHA256 incremental cache).
- Provenance: every edge is tagged EXTRACTED (confidence 1.0), INFERRED (with confidence score), or AMBIGUOUS.

## Landing page — https://graphify.net/

Graphify is an open-source tool that transforms codebases into interactive knowledge graphs. It "turns an entire repository — including source code, documentation, research papers and diagrams — into an interactive graph."

Key Statistics:
- 3.7k+ GitHub Stars
- MIT License
- 71.5× Token Reduction
- Python 3.10+ Required

The tool provides multi-modal extraction from code, Markdown, PDFs and images. It generates NetworkX graphs using the Leiden algorithm for community detection and identifies high-degree "god nodes" representing critical system components.

Installation via PyPI under the name `graphifyy`:
```
pip install graphifyy && graphify install
graphify ./raw
```

Graphify integrates with Claude Code, OpenAI Codex, and OpenCode assistants. All core dependencies use permissive open-source licenses. On the httpx library: 144 nodes, 330 edges, 6 communities. On a mixed Karpathy corpus: 285 nodes, 340 edges with significant token savings compared to naive approaches.

## Knowledge Graphs for AI Coding Assistants — https://graphify.net/knowledge-graph-for-ai-coding-assistants.html

Graphify addresses a fundamental limitation in AI coding assistants: the context-window problem. "An AI coding assistant is only as good as the context it can fit in a prompt."

Key advantages over vector search:
1. **Structural preservation** — Relationships like function calls and module dependencies remain intact, unlike embedding-based retrieval that loses this information.
2. **Transparency** — Every connection is tagged with its source type (`EXTRACTED`, `INFERRED`, or `AMBIGUOUS`) and confidence scores.
3. **Multi-modal integration** — Diagrams, code, and documentation nodes coexist on a single graph.
4. **Efficiency** — On a 52-file corpus, the graph reduces token costs to approximately 1.7k compared to 123k for raw files — a "71.5× reduction."

Graphify operates as a slash command (e.g., `/graphify .` in Claude Code) and generates three outputs: an interactive HTML graph, an audit report, and persistent JSON data. For Claude Code specifically, a PreToolUse hook integrates graph consultation before file operations.

## Tree-sitter AST Extraction — https://graphify.net/tree-sitter-ast-extraction.html

Graphify's initial processing step uses Tree-sitter to analyze code files deterministically without network calls or ML models. The parser converts abstract syntax tree nodes into graph structures.

Key advantages:
1. **Privacy-focused** — "Source code never leaves the machine during the AST pass." Network requests occur only later for documentation retrieval, transmitting semantic summaries rather than raw code.
2. **Performance** — AST parsing operates at linear time complexity relative to file size.
3. **Language consistency** — Uniform node and edge structure across all supported languages.

Supported Languages (19): Python, JavaScript, TypeScript, Ruby, PHP, Lua, PowerShell (Scripting); Go, Rust, C, C++, Zig, Swift, Objective-C (Systems); Java, Kotlin, Scala, C# (JVM/.NET); Elixir (BEAM).

Extracted elements: structural definitions, function calls, module imports, and explanatory comments. "Rationale nodes — docstrings and rationale comments...are lifted out as separate nodes" to preserve development intent. All extracted data carries `EXTRACTED` tags with confidence 1.0.

## Leiden Community Detection — https://graphify.net/leiden-community-detection.html

Graphify applies the Leiden algorithm directly to graph topology to identify code communities, deliberately avoiding vector embeddings and external similarity indexes.

Three problems avoided vs embedding-based approaches:
1. **Structural Loss** — "Embedding similarity ignores call graphs and imports — the exact edges that tell you two files belong together."
2. **Opaque Results** — Clustering decisions lack clear justification; similarity scores provide no rationale.
3. **Infrastructure Overhead** — Vector databases introduce additional operational complexity and costs.

Semantic integration: `semantically_similar_to` edges marked with `INFERRED` confidence scores coexist with structural edges within the same graph, allowing Leiden to recognize both call-graph proximity and conceptual affinity.

Output includes: community reports with top-ranked "god nodes," surprising cross-community connections, and suggested analytical questions. The httpx example demonstrates communities centered on `Client`, `AsyncClient`, `Response`, and `Request`. Uses `graspologic` for Leiden, NetworkX for graph operations, runs entirely in Python locally.

## Graphify + Claude Code Integration — https://graphify.net/graphify-claude-code-integration.html

The deepest Graphify integration is with Claude Code. Installation:
```
pip install graphifyy
graphify install
graphify claude install   # from inside your project
```

The setup writes a `CLAUDE.md` directive and installs a `PreToolUse` hook in `settings.json`. This ensures Claude consults the knowledge graph "before every file-search tool call — not after," allowing navigation by structural elements like god nodes and communities rather than raw file searching.

Platform support: while Codex, OpenCode, OpenClaw, and Factory Droid lack PreToolUse support, Graphify accommodates them through `AGENTS.md` files in the project root.

Graph maintenance:
- Git hooks automatically rebuild after commits and branch switches
- Watch mode provides real-time updates during development

Query options: explicit CLI commands (`/graphify query`, `/graphify path`, `/graphify explain`) for detailed, edge-level graph traversals with relation types and confidence scores.

## CLI Command Reference — https://graphify.net/graphify-cli-commands.html

The Graphify CLI is organized into functional categories:

**Core Operations:**
- `/graphify ./raw --mode deep` for aggressive edge inference
- `--update` and `--watch` modes
- `add` command for papers, tweets, and external sources

**Query Capabilities:**
- Path tracing with `--dfs`
- Token budgeting via `--budget`
- Node-specific queries
- Both assistant-integrated slash commands and standalone terminal execution

**Export Formats:**
- Documentation: Wikipedia markdown, Obsidian vaults
- Visualization: SVG, GraphML (Gephi/yEd)
- Database: Neo4j Cypher, MCP servers

**Automation:**
Git hook integration enables automatic rebuilds; platform-specific installers cover Claude Code, Codex, OpenCode, OpenClaw, and Factory Droid.

"The AST pass always runs locally; the semantic pass uses your AI assistant's model API."

## Graphify vs Alternatives — https://graphify.net/graphify-vs-alternatives.html

| Project | Focus | Strength | Limitation vs Graphify |
|---|---|---|---|
| Sourcegraph | Cross-repo code search | Enterprise-grade navigation | Not a knowledge graph; limited design semantics; code-only |
| Code2Vec | Function-level embeddings | Vector retrieval and classification | No graph structure, no multi-modal input, no rationale |
| Neo4j | General graph database | Powerful Cypher queries | Doesn't generate graphs from code itself — you still need an extractor |

Key distinctions:
- **Sourcegraph** excels at "find every call site of this function across 400 repos" but lacks knowledge graph modeling of design reasoning and multi-modal input support.
- **Code2Vec** converts functions into vectors but "throw away call structure, imports and rationale" compared to Graphify's typed-edge approach.
- **Neo4j** requires external extraction tools; Graphify functions as the extractor itself, with optional Neo4j export via `/graphify ./raw --neo4j`.

Graphify's unique features: multi-modal integration (code, docs, papers, images), provenance tagging (EXTRACTED, INFERRED, AMBIGUOUS), rationale capture from docstrings and comments, local-only operation (no server/vector store required), assistant-native integration across multiple platforms.
