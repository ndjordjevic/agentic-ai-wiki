# mksglu/context-mode

## Metadata
- Stars: 18301
- Primary language: TypeScript
- Default branch: main
- Latest release: v1.0.168 (2026-06-26)
- License: Elastic License v2 (ELv2)
- Homepage: https://context-mode.com
- Fetched: 2026-06-29
- Final URL: https://github.com/mksglu/context-mode

## Description
Context window optimization for AI coding agents. Sandboxes tool output (98% reduction), persists session memory, and enforces routing across 17 platforms via MCP + hooks.

## README

# Context Mode

**The other half of the context problem.**

Used across teams at Microsoft, Google, Meta, Amazon, IBM, NVIDIA, ByteDance, Stripe, Datadog, Salesforce, GitHub, Red Hat, Supabase, Canva, Notion, Hasura, Framer, Cursor.

## The Problem

Every MCP tool call dumps raw data into your context window. A Playwright snapshot costs 56 KB. Twenty GitHub issues cost 59 KB. One access log — 45 KB. After 30 minutes, 40% of your context is gone. And when the agent compacts the conversation to free space, it forgets which files it was editing, what tasks are in progress, and what you last asked for. On top of that, the agent wastes output tokens on filler, pleasantries, and verbose explanations — burning context from both sides.

### How Context Mode Solves It

Context Mode is an MCP server that solves all four sides of this problem:

1. **Context Saving** — Sandbox tools keep raw data out of the context window. 315 KB becomes 5.4 KB. 98% reduction.
2. **Session Continuity** — Every file edit, git operation, task, error, and user decision is tracked in SQLite. When the conversation compacts, context-mode doesn't dump this data back into context — it indexes events into FTS5 and retrieves only what's relevant via BM25 search. The model picks up exactly where you left off.
3. **Think in Code** — The LLM should program the analysis, not compute it. Instead of reading 50 files into context to count functions, the agent writes a script that does the counting and `console.log()`s only the result. One script replaces ten tool calls and saves 100x context. This is a mandatory paradigm enforced via hooks across all 17 supported clients.
4. **No prose-style enforcement** — context-mode keeps raw data out of context but never dictates how the model writes its final answer.

```js
// Before: 47 × Read() = 700 KB.  After: 1 × ctx_execute() = 3.6 KB.
ctx_execute("javascript", `
  const files = fs.readdirSync('src').filter(f => f.endsWith('.ts'));
  files.forEach(f => console.log(f + ': ' + fs.readFileSync('src/'+f,'utf8').split('\\n').length + ' lines'));
`);
```

## Install

### Claude Code (plugin marketplace — recommended)

```bash
/plugin marketplace add mksglu/context-mode
/plugin install context-mode@context-mode
```

Verify: `/context-mode:ctx-doctor` — all checks should show `[x]`.

### Global install (all other platforms)

```bash
npm install -g context-mode
```

Platform-specific hook configs exist for: Gemini CLI, VS Code Copilot, JetBrains Copilot, GitHub Copilot CLI, Cursor, OpenCode, KiloCode, OpenClaw, Codex CLI, Kimi Code, Qwen Code, Kiro, Zed, Pi, OMP, Antigravity IDE, Antigravity CLI (agy).

## Tools

| Tool | What it does | Context saved |
|---|---|---|
| `ctx_batch_execute` | Run multiple commands + search multiple queries in ONE call. Opt-in `concurrency: 1-8`. | 986 KB → 62 KB |
| `ctx_execute` | Run code in 12 languages. Only stdout enters context. | 56 KB → 299 B |
| `ctx_execute_file` | Process files in sandbox. Raw content never leaves. | 45 KB → 155 B |
| `ctx_index` | Chunk markdown into FTS5 with BM25 ranking. | 60 KB → 40 B |
| `ctx_search` | Query indexed content with multiple queries in one call. | On-demand retrieval |
| `ctx_fetch_and_index` | Fetch URL, chunk and index. Cache reuses content within TTL (default 24h). | 60 KB → 40 B |
| `ctx_stats` | Show context savings, call counts, and session statistics. | — |
| `ctx_doctor` | Diagnose installation: runtimes, hooks, FTS5, versions. | — |
| `ctx_upgrade` | Upgrade to latest version from GitHub, rebuild, reconfigure hooks. | — |
| `ctx_purge` | Permanently deletes all indexed content from the knowledge base. | — |
| `ctx_insight` | Opens the hosted Insight dashboard in your browser. | — |

## How the Sandbox Works

Each `ctx_execute` call spawns an isolated subprocess with its own process boundary. The subprocess runs your code, captures stdout, and only that stdout enters the conversation context. Twelve language runtimes: JavaScript, TypeScript, Python, Shell, Ruby, Go, Rust, PHP, Perl, R, Elixir, and C#. Bun is auto-detected for 3-5x faster JS/TS execution. Authenticated CLIs (gh, aws, gcloud, kubectl, docker) inherit environment variables without exposing them to the conversation.

## How the Knowledge Base Works

The `ctx_index` tool chunks markdown content by headings while keeping code blocks intact, then stores them in a **SQLite FTS5** virtual table. The SQLite backend is selected automatically at runtime: `bun:sqlite` on Bun, `node:sqlite` on Node.js ≥ 22.5, and `better-sqlite3` everywhere else. Search uses **BM25 ranking** with **Porter stemming**. Titles and headings are weighted **5x** in BM25 scoring.

Search runs two parallel strategies merged with **Reciprocal Rank Fusion (RRF)**:
- **Porter stemming** — FTS5 MATCH with porter tokenizer.
- **Trigram substring** — partial string matching.

Multi-term queries get **proximity reranking**. **Fuzzy correction** via Levenshtein distance corrects typos before re-searching. **Smart snippets** return windows around matching query terms rather than first-N characters. **Progressive throttling**: calls 1–3 return 2 results/query; calls 4–8 return 1; calls 9+ are blocked (redirects to `ctx_batch_execute`).

**TTL Cache:** `ctx_fetch_and_index` defaults to 24h TTL. Cache hits return ~0.3 KB instead of re-fetching 48 KB+. 14-day content cleanup on startup.

## Session Continuity

Context Mode captures every meaningful event during a session and persists them in a per-project SQLite database (`~/.context-mode/`). On context compaction or `--continue`/`--resume`, working state is rebuilt automatically: files edited, tasks in progress, errors resolved, decisions made.

Events captured: file edits, git operations, task completions, user decisions/corrections, errors. Events are indexed into FTS5 and retrieved via BM25 on resume — only relevant context is injected, not a full log dump.

`/resume <picker>`: the SessionStart hook detects the empty live-event table for the freshly issued session id and falls back to the most recent unconsumed snapshot for the project.

## Platform Compatibility (17 platforms)

| Paradigm | Platforms |
|---|---|
| **JSON stdin/stdout hooks** | Claude Code, Gemini CLI, VS Code Copilot, JetBrains Copilot, GitHub Copilot CLI, Cursor, Codex CLI, Qwen Code, Kimi Code, Antigravity CLI (`agy`), Kiro |
| **TS Plugin** | OpenCode, KiloCode, OpenClaw |
| **MCP-only** | Antigravity IDE, Zed, Pi, OMP (Oh My Pi) |

The MCP server layer is 100% portable. Only the hook layer requires platform-specific adapters.

### Routing Enforcement

| Platform | With Hooks | Without Hooks |
|---|---|---|
| Claude Code, Gemini CLI, VS Code Copilot, JetBrains Copilot, GitHub Copilot CLI, Cursor, OpenCode, OpenClaw, Codex CLI, Kiro, Pi, OMP | **~98% saved** | ~60% saved |
| Antigravity IDE, Zed | — | ~60% saved |

Hooks intercept tool calls programmatically (block dangerous commands, redirect to sandbox). Instruction files guide via prompts but cannot block. **Always enable hooks where supported.**

## Benchmarks

| Scenario | Raw | Context | Saved |
|---|---|---|---|
| Playwright snapshot | 56.2 KB | 299 B | 99% |
| GitHub Issues (20) | 58.9 KB | 1.1 KB | 98% |
| Access log (500 requests) | 45.1 KB | 155 B | 100% |
| Context7 React docs | 5.9 KB | 261 B | 96% |
| Analytics CSV (500 rows) | 85.5 KB | 222 B | 100% |
| Git log (153 commits) | 11.6 KB | 107 B | 99% |
| Test output (30 suites) | 6.0 KB | 337 B | 95% |
| Repo research (subagent) | 986 KB | 62 KB | 94% |

Over a full session: 315 KB of raw output becomes 5.4 KB. Session time extends from ~30 minutes to ~3 hours.

## Privacy & Architecture

Nothing leaves your machine. No telemetry, no cloud sync, no usage tracking, no account required. Code, prompts, session data — all local. SQLite databases live in your home directory. Context optimization happens at the source (MCP protocol layer), not in a cloud dashboard.

## Security

Context Mode enforces the same permission rules as the host (Claude Code `permissions.deny`/`allow` format). `ctx_execute_file` is confined to the project root by default — path traversal and symlink escapes are blocked. `ctx_fetch_and_index` blocks dangerous URL targets: `file://`, `gopher://`, cloud metadata endpoints (`169.254.169.254`), multicast, reserved ranges. `CTX_FETCH_STRICT=1` additionally blocks RFC1918/loopback. Tool inputs for MCP calls are redacted of credentials (tokens, secrets, api_keys, passwords) before persistence in the session DB.

## License

Licensed under **Elastic License v2 (ELv2)**. Source-available; free to use, fork, modify, distribute. Cannot offer as a hosted/managed service or remove licensing notices.

## Docs

### Top-level structure
```
.agents/              agent instruction files
.claude-plugin/       Claude Code plugin manifest + hooks + routing configs
.codex-plugin/        Codex CLI plugin manifest
.cursor-plugin/       Cursor plugin configs
.openclaw-plugin/     OpenClaw plugin configs
.pi/                  Pi agent extension
bin/                  compiled binaries
configs/              per-platform configs (claude-code, gemini-cli, cursor, opencode, codex, etc.)
docs/                 adapters/, adr/, platform-support.md, jetbrains-copilot.md
hooks/                PreToolUse, PostToolUse, PreCompact, SessionStart, Stop hook scripts
scripts/              build/diagnostic scripts
skills/               bundled skills for Copilot CLI, Codex, etc.
src/                  TypeScript source
tests/                vitest test suite
web/                  Insight dashboard frontend
BENCHMARK.md          full benchmark data (21 scenarios)
CLAUDE.md             Claude Code routing instructions (auto-injected by SessionStart hook)
CONTRIBUTING.md       development workflow and TDD guidelines
```

### Key ADR decisions
- 0001: sessiondb-multi-writer
- 0002: tool-description-style
- 0003: routing-deny-reasons
- 0004: stats-strict-compression-formula

### Platform support
Supports 17 client platforms via three hook paradigms (JSON stdin/stdout, TS Plugin, MCP-only). Full capability comparison in docs/platform-support.md. Hook events used: PreToolUse (route/block), PostToolUse (capture events), SessionStart (inject routing + restore session), PreCompact (snapshot before compaction), UserPromptSubmit (capture decisions), Stop (record turn-end state).
