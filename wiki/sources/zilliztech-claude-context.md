---
type: source
source_url: https://github.com/zilliztech/claude-context
tags:
  - mcp-server
  - semantic-code-search
  - vector-database
  - milvus
  - claude-code
  - typescript
  - code-indexing
  - embedding-search
related:
  - modelcontextprotocol-servers-tree-main-src-sequentialthinking
product: claude-context
detail_level: standard
created: 2026-05-19
updated: 2026-05-19
---

Claude Context is an MCP plugin for AI coding agents (11,432 stars, MIT, TypeScript) that adds semantic code search over an entire codebase by indexing it into a Milvus/Zilliz Cloud vector database and exposing four MCP tools — `index_codebase`, `search_code`, `get_indexing_status`, and `clear_index` — that Claude Code and other AI assistants call to retrieve semantically relevant code without loading entire directories into the context window. It is published on npm as `@zilliz/claude-context-mcp` and can be added to Claude Code in a single `claude mcp add` command, making it a drop-in context-precision upgrade for large codebases.

_All claims below are sourced from ../../raw/github/zilliztech-claude-context.md unless otherwise noted._

## What it does

Claude Context solves the context cost problem for large codebases: loading full directories into Claude per request is expensive and often exceeds context limits. Instead, Claude Context indexes the codebase once into a vector database, then uses semantic search to pull only the relevant code snippets into the agent's context window on demand. The result is more accurate, lower-cost interactions — the agent can search millions of lines without seeing all of them at once.

## Key features

- **Semantic code search** over the full codebase via Milvus/Zilliz Cloud vector storage and configurable embedding providers (OpenAI `text-embedding-3-small` by default; also VoyageAI `voyage-code-3`, Gemini, and Ollama for fully local deployment).
- **Asynchronous indexing**: `index_codebase` returns immediately; background indexing runs independently so users can search partial results while the codebase is still being indexed.
- **Progress tracking**: `get_indexing_status` reports phase-based percentage (0% setup → ~5% scan → 10–100% embedding/write) persisted to `~/.context/mcp-codebase-snapshot.json`.
- **Configurable file inclusion**: additive extension sets (defaults + `customExtensions` MCP param + `CUSTOM_EXTENSIONS` env var) minus additive ignore patterns (defaults + `ignorePatterns` MCP param + `CUSTOM_IGNORE_PATTERNS` env var + `.gitignore` + `.xxxignore` files + global `~/.context/.contextignore`).
- **Multi-client support**: one `npx @zilliz/claude-context-mcp@latest` server works with Claude Code, Cursor, VS Code, Windsurf, Cline, Augment, Roo Code, Gemini CLI, Codex CLI, Qwen Code, and any stdio-based MCP client.
- **VS Code extension**: "Semantic Code Search" (`zilliz.semanticcodesearch`) on the VS Code Marketplace provides an IDE-native interface.

## Architecture

The monorepo (`pnpm` workspaces) has three main packages:

- **`packages/core` (`@zilliz/claude-context-core`)**: the indexing and semantic search library. Exports `Context`, `MilvusVectorDatabase`, `OpenAIEmbedding`, and provider interfaces. Houses `DEFAULT_SUPPORTED_EXTENSIONS` and `DEFAULT_IGNORE_PATTERNS`. The `Context.indexCodebase()` method walks the filtered file tree, chunks code, generates embeddings, and writes batches to Milvus; `Context.semanticSearch()` queries by vector similarity and returns `{relativePath, startLine, endLine, score, content}` result objects.
- **`packages/mcp` (`@zilliz/claude-context-mcp`)**: the MCP server layer. Wraps the core library and exposes the four MCP tools over stdio transport. Published to npm; consumed via `npx @zilliz/claude-context-mcp@latest`.
- **`packages/vscode-extension`**: VS Code Marketplace extension wrapping the core library with an IDE UI.

Codebase identity is tracked by the resolved **absolute path**: two clones of the same repo at different paths are treated as separate codebases. Collection names in Milvus are derived from the normalized absolute path, so consistent paths matter for status checks, searches, and clear operations.

## Installation

```bash
# Claude Code (single command)
claude mcp add claude-context \
  -e OPENAI_API_KEY=sk-your-openai-api-key \
  -e MILVUS_ADDRESS=your-zilliz-cloud-public-endpoint \
  -e MILVUS_TOKEN=your-zilliz-cloud-api-key \
  -- npx @zilliz/claude-context-mcp@latest
```

Prerequisites: Node.js ≥ 20.0.0, a free Zilliz Cloud account (for MILVUS_ADDRESS and MILVUS_TOKEN), and an OpenAI API key (or alternative embedding provider key). For local/air-gapped setups, Ollama (`nomic-embed-text`) replaces OpenAI.

## Example usage

After configuration, interact through natural language in Claude Code:

```
Index this codebase
Check the indexing status
Find functions that handle user authentication
```

Programmatic usage via the core package:

```typescript
import { Context, MilvusVectorDatabase, OpenAIEmbedding } from '@zilliz/claude-context-core';

const context = new Context({
  embedding: new OpenAIEmbedding({ apiKey: process.env.OPENAI_API_KEY, model: 'text-embedding-3-small' }),
  vectorDatabase: new MilvusVectorDatabase({ address: process.env.MILVUS_ADDRESS, token: process.env.MILVUS_TOKEN })
});

const stats = await context.indexCodebase('./your-project', p => console.log(`${p.phase} - ${p.percentage}%`));
const results = await context.semanticSearch('./your-project', 'vector database operations', 5);
```

## When to use

Use Claude Context when working with codebases too large to fit in the Claude context window, when per-request directory loading is cost-prohibitive, or when an AI coding agent repeatedly fails to find relevant code via multi-round discovery. It pairs naturally with any MCP-compatible agent harness and removes the need to craft manual file-inclusion prompts for large repos.

## Maintenance status

11,432 stars, MIT License, TypeScript, last pushed 2026-05-06. No versioned releases — distributed directly via `npx` from npm. Maintained by Zilliz (the commercial company behind Milvus). Roadmap includes an agent-based interactive search mode, search result ranking optimization, and a Chrome Extension. The related `memsearch` plugin (mentioned in the README) extends the same infrastructure with persistent markdown-first memory for cross-session agent memory.
