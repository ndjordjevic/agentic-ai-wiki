---
type: source
source_url: https://github.com/chopratejas/headroom
tags:
  - context-compression
  - token-optimization
  - mcp-server
  - proxy
  - claude-code
  - reversible-compression
  - cross-agent-memory
  - local-first
related:
  - nadimtuhin-claude-token-optimizer
  - mksglu-context-mode
  - zilliztech-claude-context
  - aaif-goose-goose
  - langchain.com
product: headroom
detail_level: standard
created: 2026-07-08
updated: 2026-07-08
---

Headroom (57.6K+ stars, Apache 2.0, v0.30.0) is a local-first context compression layer for AI agents — it shrinks tool outputs, logs, RAG chunks, files, and conversation history before they reach the LLM, claiming 60–95% token reduction on JSON workloads and 15–20% on coding agents while preserving answer quality via reversible CCR caching. It ships as a Python/TypeScript library (`compress(messages)`), a drop-in OpenAI-compatible proxy (`headroom proxy`), one-command agent wrappers (`headroom wrap claude|codex|cursor|…`), an MCP server (`headroom_compress`, `headroom_retrieve`, `headroom_stats`), cross-agent memory, and `headroom learn` for mining failed sessions into `CLAUDE.md`/`AGENTS.md` corrections. The repo has moved to `headroomlabs-ai/headroom` but remains reachable via the original `chopratejas/headroom` URL.

_All claims below are sourced from ../../raw/github/chopratejas-headroom.md unless otherwise noted._

## What it does

Headroom intercepts everything an agent reads — tool outputs, logs, RAG results, files, and conversation history — and compresses it before the LLM sees it. Same answers, fraction of the tokens. It runs locally so data never leaves the machine.

Delivery modes cover the full agent stack:

- **Library** — `compress(messages)` in Python or TypeScript, inline in any app
- **Proxy** — `headroom proxy --port 8787`, zero code changes, any OpenAI-compatible client
- **Agent wrap** — `headroom wrap claude|codex|copilot|cursor|aider|opencode|cline|continue|goose|openhands|openclaw|vibe`; undo with `headroom unwrap <tool>`
- **MCP server** — `headroom_compress`, `headroom_retrieve`, `headroom_stats` for any MCP client
- **Cross-agent memory** — shared store across Claude, Codex, Gemini with auto-dedup
- **`headroom learn`** — mines failed sessions, writes corrections to `CLAUDE.local.md` (default, gitignored) or `CLAUDE.md` / `AGENTS.md` / `GEMINI.md`
- **Output token reduction** — trims what the model writes back (verbosity steering, effort routing) via `HEADROOM_OUTPUT_SHAPER=1`
- **Reversible (CCR)** — originals cached locally; LLM calls `headroom_retrieve` on demand

## Installation

```bash
# Python CLI (ships `headroom` command)
uv tool install "headroom-ai[all]"
pip install "headroom-ai[all]"

# TypeScript SDK only — library import, no CLI
npm install headroom-ai

# Docker
docker pull ghcr.io/chopratejas/headroom:latest
```

Granular extras: `[proxy]`, `[mcp]`, `[ml]`, `[code]`, `[memory]`, `[vector]`, `[relevance]`, `[image]`, `[agno]`, `[langchain]`, `[evals]`, `[pytorch-mps]`. Requires Python 3.10+. The `headroom` CLI ships only via PyPI; npm `headroom-ai` is the TypeScript SDK.

Quick start after install:

```bash
headroom wrap claude          # or: headroom proxy --port 8787
headroom doctor               # health check
headroom perf                 # savings report
headroom dashboard            # live dashboard (proxy must be running)
```

## Key features

- **Content-aware compressors** — SmartCrusher (JSON), CodeCompressor (AST for Python/JS/TS/Go/Rust/Java/C/C++/Perl), Kompress-v2-base (HuggingFace text model trained on agentic traces), image compression via ML router
- **CacheAligner** — stabilizes prompt prefixes so Anthropic/OpenAI KV caches actually hit
- **CCR (reversible compression)** — stores originals locally within configurable TTL; model retrieves via `headroom_retrieve` when needed
- **Live-zone compression** — compresses fresh tool output while keeping frozen prefix byte-stable
- **Output token reduction** — `HEADROOM_OUTPUT_SHAPER=1` adds verbosity steering and effort routing; `headroom learn --verbosity` auto-tunes terseness from past sessions
- **Agent compatibility matrix** — native `headroom wrap` for Claude Code, Codex, Aider, Copilot CLI, OpenCode, Cline, Continue, Goose, OpenHands, OpenClaw, Mistral Vibe; manual setup for Cursor; library-only for Cortex Code
- **GitHub Copilot CLI subscription mode** — `headroom copilot-auth login` + `headroom wrap copilot --subscription`
- **Framework integrations** — Anthropic/OpenAI SDK wrappers, Vercel AI SDK middleware, LiteLLM callbacks, LangChain `HeadroomChatModel`, Agno `HeadroomAgnoModel`, Strands, ASGI `CompressionMiddleware`, SharedContext for multi-agent
- **Benchmarks** — 92% savings on code search and SRE debugging workloads; accuracy preserved on GSM8K (±0.000), TruthfulQA (+0.030), SQuAD v2 (97% at 19% compression), BFCL (97% at 32% compression)
- **RTK integration** — ships RTK binary for shell-output rewriting; can also use lean-ctx via `HEADROOM_CONTEXT_TOOL=lean-ctx`

## Architecture

The pipeline exposes one stable request lifecycle across `compress()`, the SDK, and the proxy:

`Setup` → `Pre-Start` → `Post-Start` → `Input Received` → `Input Cached` → `Input Routed` → `Input Compressed` → `Input Remembered` → `Pre-Send` → `Post-Send` → `Response Received`

Core flow:

```
Agent/app → Headroom (local) → LLM provider
              CacheAligner → ContentRouter → CCR
                ├─ SmartCrusher (JSON)
                ├─ CodeCompressor (AST)
                └─ Kompress-v2-base (text)
              Cross-agent memory · headroom learn · MCP
```

- **Transforms** do the compression work: CacheAligner, ContentRouter, SmartCrusher, CodeCompressor, Kompress-v2-base
- **Pipeline extensions** observe lifecycle stages via `on_pipeline_event(...)`
- **Compression hooks** sit alongside the canonical lifecycle as an additional extension seam
- **Proxy extensions** are the server/app integration seam for ASGI middleware, routes, and startup policy
- **Provider slices** under `headroom/providers/` — Claude, Copilot, Codex, Gemini, OpenClaw — keep core orchestration (`wrap.py`, `client.py`, `cli/proxy.py`, `proxy/server.py`) provider-agnostic

The codebase is Python 80.4% + Rust 15.1% + TypeScript 2.5%, with Rust crates for performance-critical paths and a TypeScript SDK under `sdk/typescript/`.

## Example usage

```bash
# Wrap a coding agent (starts proxy + MCP + configured session)
headroom wrap claude

# Drop-in proxy for any OpenAI-compatible client
headroom proxy --port 8787

# Inline library
from headroom import compress
compressed = compress(messages, model="claude-sonnet-4-20250514")

# MCP install for native clients
headroom mcp install

# Output token reduction
export HEADROOM_OUTPUT_SHAPER=1
headroom proxy --port 8787

# Learn verbosity from past sessions
headroom learn --verbosity --apply

# Update in place
headroom update
```

For Codex or MCP clients that cannot inherit shell `PATH`, install as a persistent uv tool and point MCP config at the absolute binary path:

```toml
[mcp_servers.headroom]
command = "/absolute/path/from/command-v/headroom"
args = ["mcp", "serve"]
```

## Maintenance status

- **Stars:** 57,639 | **Forks:** 4,252 | **Primary language:** Python
- **Latest release:** v0.30.0 (2026-07-03) | **License:** Apache 2.0
- **Homepage/docs:** https://headroom-docs.vercel.app/docs
- **Final repo URL:** https://github.com/headroomlabs-ai/headroom (redirects from `chopratejas/headroom`)
- **Active development** — 1,906 commits, CI via GitHub Actions, codecov, release-please, devcontainers (default + `memory-stack` with Qdrant & Neo4j)
- **Team offering** — Headroom OSS is individual-developer focused; managed/org deployment via hello@headroomlabs.ai
- **Compared to:** RTK (CLI outputs only, not reversible), lean-ctx (similar scope, reversible), Compresr/Token Co. (hosted API, not local), OpenAI Compaction (provider-native conversation only)
