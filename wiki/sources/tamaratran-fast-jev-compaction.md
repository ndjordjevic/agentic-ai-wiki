---
type: source
category: "Knowledge, RAG, memory & context"
source_url: https://github.com/tamaratran/fast-jev-compaction
tags:
  - context-compaction
  - claude-code-plugin
  - function-hooks
  - tool-call-pruning
  - verbatim-preservation
  - claude-code-hooks
related:
  - chopratejas-headroom
  - mksglu-context-mode
  - nadimtuhin-claude-token-optimizer
product: fast-jev-compaction
detail_level: standard
created: 2026-10-03
updated: 2026-10-03
---

fast-jev-compaction is a Claude Code plugin and npm library that replaces LLM-summarized context compaction with a scoring-and-pruning approach: an auxiliary model ("Jev", served by TypeSafe's System One API) judges, per tool call, whether the call and its result still matter, and the library deletes what it says is no longer needed rather than rewriting anything. User and assistant text is always kept verbatim and in order — only tool calls and tool results are candidates for removal or truncation. It ships both as a reusable TypeScript library (`src/`) and as an early-access Claude Code function-hook plugin (`hooks/`, `.claude-plugin/`) that intercepts `session.compact` and falls back to Claude Code's built-in summary when Jev fails or the estimated reduction is too small.

_All claims below are sourced from ../../raw/github/tamaratran-fast-jev-compaction.md unless otherwise noted._

## What it does

Standard context compaction asks an LLM to summarize old turns, which is lossy — a file path, exact error, constraint, or command can silently disappear. fast-jev-compaction instead pairs every `tool_use` with its `tool_result` by `tool_use_id`, pins the first message and the newest `preserveRecentMessages` messages, and sends the rest of the conversation ("state", with tool outputs replaced by short notes) to the Jev model. For every non-pinned call, Jev answers two yes/no-style questions — should the call stay, and should its result stay verbatim — and decisions are made against a `keepThreshold`: keep both, keep the call but truncate the result, or drop the call and result together.

## Installation

```sh
npm install fast-jev-compaction
export TYPESAFE_API_KEY=...
```

As a Claude Code plugin (function hooks are early-access, 2.1.274+):

```sh
export CLAUDE_CODE_ENABLE_FUNCTION_HOOKS=1
claude plugin marketplace add tamaratran/fast-jev-compaction
claude plugin install fast-jev-compaction@fast-jev-compaction
```

## Key features

- **Never rewrites text** — only tool calls/results are removed or truncated; user and assistant prose is untouched.
- **Token-budgeted state fitting** — the conversation state is fit into `maxStateTokens` (25k default) through staged degradation: truncate tool inputs (1000 → 200 → 60 chars), abridge long texts to head+tail, collapse old messages to omission notes, shrink old tool calls to one-liners, drop old call-less messages, and fold runs of call-only messages — each stage applied only if the previous one wasn't enough.
- **Concurrent batched requests** — questions are split across as many requests as needed to stay under `maxRequestTokens` (30k default, under Jev's 32k limit), with the full state resent each time and answers merged.
- **Estimated tokenization without a tokenizer** — a calibrated heuristic (characters per word/digit/symbol) that's tuned to land a bit above what Jev itself reports.
- **Exported building blocks** — `collectToolCalls`, `fitState`, `batchCalls`, `decideCall`, `applyDecisions`, plus a pluggable `JevAsker` transport interface so callers can bring their own HTTP client.

## Architecture

The `src/` package (`client.ts`, `compact.ts`, `request.ts`, `state.ts`, `messages.ts`, `types.ts`) implements the core algorithm independent of Claude Code: `compactMessages(transcript, options)` takes a `Message[]` (a subset of Claude Code's `SessionMessage`, so a raw session transcript can be passed in directly) and returns `{ messages, decisions, stats }`, with a `reductionRatio()` helper to decide whether compaction was worth applying versus falling back to summarization. (../../raw/github/tamaratran-fast-jev-compaction.md)

## Example usage

```ts
import { compactMessages, reductionRatio, type Message } from 'fast-jev-compaction';

const result = await compactMessages(transcript, { preserveRecentMessages: 4 });
console.log(result.messages, result.decisions, result.stats);
if (reductionRatio(result) < 0.25) {
  // not worth it: keep the original transcript, or summarize instead
}
```
(../../raw/github/tamaratran-fast-jev-compaction.md)

## When to use

Useful for long-running Claude Code (or similar) agent sessions where repeated auto-compaction via LLM summarization risks dropping exact file paths, error text, or constraints that matter later — teams wanting compaction that is reversible-in-spirit (verbatim survivors, not paraphrases) at the cost of extra model calls to an external scoring service (TypeSafe/Jev) and an API key dependency.

## Maintenance status

MIT licensed; default branch `main`; no tagged GitHub releases found at time of ingest. The README frames the Claude Code integration as using "early-access" function hooks (available from Claude Code 2.1.274+) that "may change between Claude Code releases," with a generated `types/claude-code.d.ts` type reference that needs regenerating after Claude Code upgrades. (../../raw/github/tamaratran-fast-jev-compaction.md)

## Ecosystem

The repository root doubles as both the npm package and the Claude Code plugin marketplace entry (`.claude-plugin/marketplace.json`); `hooks/fast-jev.ts` is the thin Claude Code adapter that imports `src/` directly and maps results back onto session messages, falling back to Claude Code's built-in compaction summary on error or insufficient reduction. A separate `demo/JevDemo` SwiftUI macOS app plays a scripted, non-networked animation of the compaction flow for screen recordings. For related approaches to managing Claude Code's context budget, see [[chopratejas-headroom]] (reversible context compression as an MCP proxy), [[mksglu-context-mode]] (context-window optimization via hooks and session sandboxing), and [[nadimtuhin-claude-token-optimizer]] (CLAUDE.md/.claudeignore-based token budgeting). (../../raw/github/tamaratran-fast-jev-compaction.md)
