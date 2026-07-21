---
type: source
category: "Knowledge, RAG, memory & context"
source_url: https://github.com/mksglu/context-mode
tags:
  - context-window-optimization
  - mcp-server
  - claude-code-hooks
  - session-continuity
  - context-sandboxing
  - multi-platform-hooks
  - sqlite-fts5
  - ai-coding-agent
related:
  - zilliztech-claude-context
  - obra-superpowers
  - anthropics-skills
  - chopratejas-headroom
  - rtk-ai-rtk
  - teamchong-pxpipe
product: context-mode
detail_level: standard
created: 2026-06-29
updated: 2026-07-21
---

Context Mode is an MCP server and hook layer that solves the context window problem for AI coding agents across 17 platforms. It addresses the fundamental issue that every MCP tool call dumps raw data into the context window — a Playwright snapshot costs 56 KB, 20 GitHub issues cost 59 KB, one access log 45 KB — by sandboxing tool output so only stdout enters context (98% reduction), tracking session events in SQLite FTS5 for compaction-resilient continuity, and enforcing the "Think in Code" paradigm that redirects the LLM from reading data directly into treating the LLM as a code generator that programs its own analysis. With 18,000+ stars and adoption at Microsoft, Google, Meta, and others, it is the de-facto standard for context optimization across the multi-agent coding ecosystem.

_All claims below are sourced from ../../raw/github/mksglu-context-mode.md unless otherwise noted._

## What it does

Context Mode solves four sides of the context window problem simultaneously. First, it sandboxes all large tool output through `ctx_execute`, `ctx_batch_execute`, and `ctx_execute_file` — raw data never enters the context window; only stdout does. Second, it persists session continuity by capturing every file edit, git operation, task, error, and user decision in a per-project SQLite database; when the conversation compacts, working state is reconstructed via BM25 search rather than a raw dump. Third, it enforces the "Think in Code" paradigm by blocking the model from reading 50 files into context when a single `ctx_execute` script can compute and surface only the result. Fourth, it avoids prescribing prose style — routing governs where data goes, not how the model talks.

## Key features

- **11 MCP tools**: `ctx_execute` (12-language sandbox), `ctx_batch_execute` (parallel execution with concurrency 1–8), `ctx_execute_file` (file processing sandbox), `ctx_index` / `ctx_search` / `ctx_fetch_and_index` (FTS5 knowledge base), `ctx_stats`, `ctx_doctor`, `ctx_upgrade`, `ctx_purge`, `ctx_insight`
- **Hook layer**: PreToolUse (intercept/block dangerous commands), PostToolUse (capture session events), SessionStart (inject routing + restore session), PreCompact (snapshot before compaction), UserPromptSubmit (capture decisions), Stop (turn-end state)
- **17-platform support**: Claude Code, Gemini CLI, VS Code Copilot, JetBrains Copilot, GitHub Copilot CLI, Cursor, OpenCode, KiloCode, OpenClaw, Codex CLI, Kimi Code, Qwen Code, Kiro, Zed, Pi, OMP, Antigravity IDE/CLI
- **Three hook paradigms**: JSON stdin/stdout (11 platforms), TypeScript Plugin in-process (OpenCode, KiloCode, OpenClaw), MCP-only (Zed, Antigravity IDE, Pi, OMP)
- **98% context savings** with hooks enabled vs ~60% with instruction files alone
- **Privacy-first**: no telemetry, no cloud sync, all data local in `~/.context-mode/`
- **Security**: `ctx_execute_file` confined to project root; credential redaction in session DB; network fetch hardening (blocks cloud metadata endpoints, configurable RFC1918 blocking)

## Architecture

The system is split into two portable layers: the **MCP server layer** (100% portable, provides all 11 `ctx_*` tools) and the **hook layer** (platform-specific adapters). Hooks intercept tool calls programmatically before execution (PreToolUse can block dangerous commands and redirect to sandbox), after execution (PostToolUse captures session events), and at lifecycle points (SessionStart restores session, PreCompact snapshots before compaction).

The **sandbox** spawns isolated subprocesses per `ctx_execute` call. Twelve language runtimes are available (JS, TS, Python, Shell, Ruby, Go, Rust, PHP, Perl, R, Elixir, C#). Bun is auto-detected for 3–5× faster JS/TS execution. Authenticated CLIs inherit env vars without exposing them to conversation context.

The **knowledge base** uses SQLite FTS5 (backend auto-selected: `bun:sqlite`, `node:sqlite`, or `better-sqlite3`). Indexing chunks markdown by headings. Search uses BM25 with Porter stemming, Reciprocal Rank Fusion across two parallel strategies (porter + trigram), proximity reranking for multi-term queries, Levenshtein fuzzy correction, and smart snippet extraction. Titles/headings weighted 5× in BM25. Progressive throttling enforces escalation to `ctx_batch_execute` after 8 search calls. TTL cache (default 24h) avoids re-fetching previously indexed URLs.

**Session continuity**: per-project SQLite at `~/.context-mode/` stores all events with FTS5 indexing. On `--continue`/`--resume` or post-compaction SessionStart, the hook queries the event DB and injects only relevant context (BM25-ranked snippets) into the new session's system prompt — no full log dump.

## Installation

**Claude Code** (recommended — plugin marketplace):

```bash
/plugin marketplace add mksglu/context-mode
/plugin install context-mode@context-mode
```

**All other platforms** — global install + platform config:

```bash
npm install -g context-mode
```

Then follow the platform-specific config in the repo's `configs/` directory (one subdirectory per platform: `gemini-cli/`, `vscode-copilot/`, `jetbrains-copilot/`, `copilot-cli/`, `cursor/`, `opencode/`, `codex/`, etc.).

**Verify** (any platform): type `ctx stats` in the agent chat; or run `context-mode doctor` in the terminal.

## Example usage

```bash
# Deep repo research — 5 calls, 62 KB context (raw: 986 KB, 94% saved)
ctx_batch_execute([
  { type: "shell", code: "find src -name '*.ts' | head -50" },
  { type: "shell", code: "cat package.json" },
  ...
])

# Process a large file without loading it into context
ctx_execute_file({ path: "logs/access.log", type: "javascript", code: `
  const lines = content.split('\\n');
  const errors = lines.filter(l => l.includes('ERROR'));
  console.log('Error count:', errors.length);
  console.log('Sample:', errors.slice(0,3).join('\\n'));
` })

# Fetch and index documentation for later querying
ctx_fetch_and_index({ url: "https://docs.example.com/api", source: "example-api" })
ctx_search({ queries: ["authentication middleware", "rate limiting"] })
```

Benchmarks: Playwright snapshot 56 KB → 299 B (99% saved); GitHub Issues ×20: 59 KB → 1.1 KB (98%); access log 500 lines: 45 KB → 155 B (100%); full session: 315 KB → 5.4 KB, session length ~30 min → ~3 hr.

## When to use

Use Context Mode when working with AI coding agents on any of the 17 supported platforms and dealing with large tool outputs (Playwright snapshots, GitHub API responses, log files, test output, CSV data) that would otherwise fill the context window. It is especially valuable for long sessions with frequent compaction, multi-step research tasks, or projects that require reading many files. The Claude Code plugin install is the lowest-friction path; all other platforms require a one-time manual config but provide the same 98% context savings with hooks enabled.

## Maintenance status

18,301 stars, 1,285 forks, released 2026-06-26 (v1.0.168). Actively maintained with frequent releases (v1.0.168 in 14 days from prior date). License: Elastic License v2 (source-available; free to use/fork/modify; cannot offer as hosted SaaS). Discord community at discord.gg/DCN9jUgN5v. Reached #1 on Hacker News with 570+ points.

## Ecosystem

Context Mode integrates directly with the Claude Code plugin marketplace, the Codex CLI plugin system (`codex plugin marketplace add mksglu/context-mode`), and Antigravity CLI (`agy plugin install`). It ships routing instruction files for every platform (`CLAUDE.md`, `AGENTS.md`, `GEMINI.md`, `KIRO.md`, etc.) and a skills bundle for Copilot CLI, Codex, and Antigravity CLI. The companion Insight dashboard (`context-mode.com/insight`) provides org-level analytics for AI-assisted engineering teams. Related: [[zilliztech-claude-context]] (semantic code search MCP for Claude Code), [[obra-superpowers]] (agent skills/hooks paradigm), [[anthropics-skills]] (Claude Code skill methodology).
