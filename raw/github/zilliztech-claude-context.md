# zilliztech/claude-context

## Metadata
- Stars: 11432
- Primary language: TypeScript
- Default branch: master
- Latest release: none
- License: MIT License
- Homepage: https://github.com/zilliztech/claude-context/tree/master/docs
- Fetched: 2026-05-19
- Final URL: https://github.com/zilliztech/claude-context

## Description
Code search MCP for Claude Code. Make entire codebase the context for any coding agent.

## README
![](assets/claude-context.png)

> 🆕 **Looking for persistent memory for Claude Code?** Check out [memsearch Claude Code plugin](https://github.com/zilliztech/memsearch#for-claude-code-users) — a markdown-first memory system that gives your AI agent long-term memory across sessions.

### Your entire codebase as Claude's context

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Node.js](https://img.shields.io/badge/Node.js-20%2B-green.svg)](https://nodejs.org/)
[![Documentation](https://img.shields.io/badge/Documentation-📚-orange.svg)](docs/)
[![VS Code Marketplace](https://img.shields.io/visual-studio-marketplace/v/zilliz.semanticcodesearch?label=VS%20Code%20Extension&logo=visual-studio-code)](https://marketplace.visualstudio.com/items?itemName=zilliz.semanticcodesearch)
[![npm - core](https://img.shields.io/npm/v/@zilliz/claude-context-core?label=%40zilliz%2Fclaude-context-core&logo=npm)](https://www.npmjs.com/package/@zilliz/claude-context-core)
[![npm - mcp](https://img.shields.io/npm/v/@zilliz/claude-context-mcp?label=%40zilliz%2Fclaude-context-mcp&logo=npm)](https://www.npmjs.com/package/@zilliz/claude-context-mcp)

**Claude Context** is an MCP plugin that adds semantic code search to Claude Code and other AI coding agents, giving them deep context from your entire codebase.

🧠 **Your Entire Codebase as Context**: Claude Context uses semantic search to find all relevant code from millions of lines. No multi-round discovery needed. It brings results straight into the Claude's context.

💰 **Cost-Effective for Large Codebases**: Instead of loading entire directories into Claude for every request, which can be very expensive, Claude Context efficiently stores your codebase in a vector database and only uses related code in context to keep your costs manageable.

---

## Quick Start

### Prerequisites

- Node.js >= 20.0.0
- A free Zilliz Cloud vector database (sign up at https://cloud.zilliz.com/signup)
- An OpenAI API key for the embedding model

### Configure MCP for Claude Code

```bash
claude mcp add claude-context \
  -e OPENAI_API_KEY=sk-your-openai-api-key \
  -e MILVUS_ADDRESS=your-zilliz-cloud-public-endpoint \
  -e MILVUS_TOKEN=your-zilliz-cloud-api-key \
  -- npx @zilliz/claude-context-mcp@latest
```

Other supported clients: OpenAI Codex CLI, Gemini CLI, Qwen Code, Cursor (with OpenAI, VoyageAI, Gemini, or Ollama embedding providers), VS Code, Windsurf, Void, Claude Desktop, Cherry Studio, Cline, Augment, Roo Code, Zencoder, and any MCP-compatible client via stdio transport.

### Usage

1. Open Claude Code in your project directory
2. Index your codebase: `Index this codebase`
3. Check indexing status: `Check the indexing status`
4. Search: `Find functions that handle user authentication`

---

## Core Package Usage

```typescript
import { Context, MilvusVectorDatabase, OpenAIEmbedding } from '@zilliz/claude-context-core';

const embedding = new OpenAIEmbedding({
    apiKey: process.env.OPENAI_API_KEY || 'your-openai-api-key',
    model: 'text-embedding-3-small'
});

const vectorDatabase = new MilvusVectorDatabase({
    address: process.env.MILVUS_ADDRESS || 'your-zilliz-cloud-public-endpoint',
    token: process.env.MILVUS_TOKEN || 'your-zilliz-cloud-api-key'
});

const context = new Context({ embedding, vectorDatabase });

// Index codebase with progress tracking
const stats = await context.indexCodebase('./your-project', (progress) => {
    console.log(`${progress.phase} - ${progress.percentage}%`);
});

// Semantic search
const results = await context.semanticSearch('./your-project', 'vector database operations', 5);
results.forEach(result => {
    console.log(`File: ${result.relativePath}:${result.startLine}-${result.endLine}`);
    console.log(`Score: ${(result.score * 100).toFixed(2)}%`);
});
```

---

## Docs

### docs/getting-started/quick-start.md

# Quick Start Guide

Get Claude Context running with AI assistants in under 5 minutes! This guide covers the most common setup using MCP (Model Context Protocol) with Claude Code.

## 🚀 1-Minute Setup for Claude Code

### Step 1: Get API Keys

1. **OpenAI API Key**: Get from https://platform.openai.com/api-keys
2. **Zilliz Cloud API Key**: Sign up on Zilliz Cloud to get an API key.

### Step 2: Configure Claude Code

```bash
claude mcp add claude-context \
  -e OPENAI_API_KEY=sk-your-openai-api-key \
  -e MILVUS_ADDRESS=your-zilliz-cloud-public-endpoint \
  -e MILVUS_TOKEN=your-zilliz-cloud-api-key \
  -- npx @zilliz/claude-context-mcp@latest
```

### Step 3: Start Using Claude Context

1. Open Claude Code in your project directory
2. Index your codebase: `Index this codebase`
3. Check indexing status: `Check the indexing status`
4. Start searching: `Find functions that handle user authentication`

Cursor also supports multiple embedding providers: OpenAI (default), VoyageAI (`voyage-code-3`), Gemini, and Ollama (local, e.g. `nomic-embed-text`).

---

### docs/dive-deep/asynchronous-indexing-workflow.md

# Asynchronous Indexing Workflow

Claude Context MCP handles codebase indexing asynchronously in the background. Users can start indexing and get an immediate response, while the actual indexing happens in the background. Users can search and monitor progress at any time.

## MCP Tools

- **`index_codebase`** — Starts background indexing, returns immediately
- **`search_code`** — Searches codebase (works during indexing with partial results)
- **`get_indexing_status`** — Shows current progress and status
- **`clear_index`** — Removes indexed data

## Status States

- **`indexed`** — ✅ Ready for search
- **`indexing`** — 🔄 Background process running
- **`indexfailed`** — ❌ Error occurred, can retry
- **`not_found`** — ❌ Not indexed yet

## Progress Calculation

`get_indexing_status` reports a coarse, phase-based percentage:

- **0%** — Preparing collection and validating prerequisites
- **~5%** — Scanning codebase and building file list
- **10% → 100%** — Processing files, chunking code, generating embeddings, writing to vector database
- **100%** — Indexing finished

Progress is persisted to `~/.context/mcp-codebase-snapshot.json`.

## Codebase Identity

Codebases are tracked by resolved **absolute path**. The same repo at two different absolute paths (symlink, different clone) is treated as two separate codebases.

---

### docs/dive-deep/file-inclusion-rules.md

# File Inclusion & Exclusion Rules

```
Final Files = (All Supported Extensions) - (All Ignore Patterns)
```

## Extension Sources (Additive)

1. **Default extensions**: `.ts`, `.tsx`, `.js`, `.jsx`, `.py`, `.java`, `.cpp`, `.c`, `.h`, `.hpp`, `.cs`, `.go`, `.rs`, `.php`, `.rb`, `.swift`, `.kt`, `.scala`, `.m`, `.mm`, `.dart`, `.sol`, `.md`, `.markdown`, `.ipynb`
2. **MCP custom extensions**: passed via `customExtensions` parameter dynamically
3. **Environment variable**: `CUSTOM_EXTENSIONS=".vue,.svelte,.astro"`

## Ignore Pattern Sources (Additive)

1. **Default patterns**: `node_modules/**`, `dist/**`, `build/**`, `.git/**`, `.env`, `*.min.js`, `*.log`, cache dirs, IDE dirs, etc.
2. **MCP custom patterns**: passed via `ignorePatterns` parameter dynamically
3. **Environment variable**: `CUSTOM_IGNORE_PATTERNS="temp/**,*.backup"`
4. **`.gitignore`** files in codebase root
5. **`.xxxignore`** files (`.cursorignore`, `.codeiumignore`, `.contextignore`, etc.)
6. **Global `~/.context/.contextignore`**

---

## Top-level structure

```
.env.example          — environment variable template
.eslintrc.js          — ESLint config
.github/              — CI/CD workflows
.gitignore
.npmrc
.vscode/              — editor settings
CONTRIBUTING.md       — contributing guide
LICENSE               — MIT
README.md             — main documentation
assets/               — images and diagrams used in docs
build-benchmark.json  — performance benchmarking results
docs/                 — documentation (getting-started/, dive-deep/, troubleshooting/)
evaluation/           — retrieval evaluation scripts and benchmarks
examples/             — basic-usage example
package.json
packages/             — monorepo packages:
    chrome-extension/     — Chrome extension (in development)
    core/                 — @zilliz/claude-context-core — indexing + search library
    mcp/                  — @zilliz/claude-context-mcp — MCP server
    vscode-extension/     — VS Code "Semantic Code Search" extension
python/               — Python bindings / evaluation scripts
scripts/              — build/utility scripts
tsconfig.json
pnpm-workspace.yaml   — pnpm monorepo config
```

**Key packages:**
- `packages/core` — `@zilliz/claude-context-core`: the indexing and semantic search library. Exports `Context`, `MilvusVectorDatabase`, `OpenAIEmbedding` and more. Contains `DEFAULT_SUPPORTED_EXTENSIONS` and `DEFAULT_IGNORE_PATTERNS`.
- `packages/mcp` — `@zilliz/claude-context-mcp`: the MCP server, published to npm; runs via `npx`.
- `packages/vscode-extension` — VS Code Marketplace extension "Semantic Code Search" (zilliz.semanticcodesearch).

**Agent instruction files:** None (`CLAUDE.md`, `AGENTS.md`, `GEMINI.md` not present in top-level).
