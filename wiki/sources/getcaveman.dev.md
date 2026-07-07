---
type: source
source_url: https://getcaveman.dev/
companion_urls:
  - https://github.com/JuliusBrussee/caveman
raw_files:
  - ../../raw/web/getcaveman.dev.md
  - ../../raw/github/juliusbrussee-caveman.md
tags:
  - token-compression
  - claude-code-skill
  - agent-efficiency
  - byte-safe-proxy
  - mcp-memory
  - terminal-coding-agent
  - skills-ecosystem
  - eval-gated-rollout
related:
  - mattpocock-skills
  - skills.sh
  - aaif-goose-goose
  - warp.dev
  - voltagent-awesome-agent-skills
  - supermemory.ai
  - nadimtuhin-claude-token-optimizer
  - claudemarketplaces.com
product: caveman
detail_level: standard
created: 2026-07-01
updated: 2026-07-07
---

Caveman is an open token-efficiency stack for agent-native development — built around the viral 78k-star `JuliusBrussee/caveman` Claude Code skill that cuts ~65% of output tokens by compressing agent *speech* without sacrificing technical accuracy. The marketing site at getcaveman.dev positions a five-layer product family: a byte-safe LLM gateway (Cloud, waitlist), Cavemem persistent memory over MCP, Caveman Code terminal agent (`@juliusbrussee/caveman-code`), Cave Architect telemetry-to-plan tooling, and eval-gated rollout for verified savings. The open stack (compression engine, proxy, CLI, SDKs, browser extension) runs locally with BYOK keys and labels all local measurements `inferred` — never `verified` — until hosted Cloud metering is available.

_All claims below are sourced from ../../raw/web/getcaveman.dev.md unless otherwise noted._

## What it does

Caveman attacks token waste on two axes: **output compression** (how agents talk) and **input compression** (what agents send to models). The flagship skill teaches supported coding agents to drop filler and use terse, fragment-based language while preserving code, paths, and identifiers exactly — averaging ~65% output reduction across benchmark prompts. The deeper stack adds a Go compression engine that routes tool output, logs, code, diffs, and search results through safety-classed compressors (S0–S4), a local reverse proxy that meters spend via base-URL swap, and companion products (Cavemem, Cavekit, Shrink) for memory recall and tool-catalog compression.

For non-coders, a browser extension brings "Caveman Mode" to ChatGPT, Claude, and Gemini chat UIs.

## Key features

- **Five-layer product map** — Gateway (coming soon, Cloud), Cavemem (MCP memory with SQLite FTS5 + vector index), Caveman Code (terminal agent, ~2× fewer tokens than Codex on identical tasks), Cave Architect (ranked spend-reduction moves with $/day estimates), Eval-Gated Rollout (replay → shadow → canary → active with auto-rollback)
- **Skill install in one line** — `curl -fsSL …/install.sh | bash` auto-detects 30+ agents (Claude Code, Cursor, Codex, Gemini, OpenClaw, Windsurf, Cline, Copilot, and more)
- **Compression levels** — `/caveman [lite|full|ultra|wenyan]` for output style; `/caveman-compress` rewrites memory files (~46% input savings); `caveman-shrink` MCP middleware compresses tool descriptions (../../raw/github/juliusbrussee-caveman.md)
- **Local engine + proxy** — Build from source: `caveman-engine` and `caveman-proxy` binaries; proxy listens on `127.0.0.1:8787`; `record` mode is pass-through, `compress` mode is byte-safe with recovery handles
- **Honesty culture** — Three labels kept apart: `inferred` (local), `measured` (observed traffic), `verified` (hosted proof only); fail-closed defaults on unknown modes, routes, graders, and prices
- **Social proof** — 74k+ GitHub stars, #1 Hacker News, top 50 on [[skills.sh]]; starred by engineers at OpenAI, Microsoft, Vercel, Cloudflare, and others

## Architecture

The compression engine exposes a stable API (`Compress`, `Retrieve`, `Detect`, `Stats`). Public front ends wrap it without duplicating compressor logic: CLI (stdin/stdout + JSON report), proxy (provider traffic routing + SQLite spend rows), MCP server (three tools), SDKs (TypeScript + Python), Cavemem, and Shrink. (../../raw/github/juliusbrussee-caveman.md)

Proxy request path: agent base-URL swap → `caveman-proxy` → match route → authenticate (env key or inbound header) → optional byte-safe transform → SSRF-guarded upstream → meter to `~/.caveman/caveman.db`. Safety ladder S0–S4 governs transforms; S4 (lossy) requires content-addressed recovery storage before emitting compressed bytes.

Open-core boundary: public packages are MIT or BSL 1.1, single-tenant, local, BYOK. Commercial Cloud/Enterprise layers add multi-tenant verified billing and eval-gated rollout — not documented in the public local stack.

## Installation

One-line skill install (macOS/Linux/WSL/Git Bash): (../../raw/github/juliusbrussee-caveman.md)

```bash
curl -fsSL https://raw.githubusercontent.com/JuliusBrussee/caveman/main/install.sh | bash
```

Windows PowerShell: `irm …/install.ps1 | iex`. Needs Node ≥18. Trigger with `/caveman` or "talk like caveman"; stop with "normal mode".

Per-agent matrix includes Claude Code (plugin + auto-activate hooks), Gemini CLI (extension), OpenClaw (`--only openclaw` drops skill + SOUL.md nudge), Cursor/Windsurf/Cline (`npx skills add` with optional `--with-init` for always-on rules), and 25+ more. Full matrix in `bin/install.js` `PROVIDERS` array.

Engine/proxy build from repo (Go toolchain from `.tool-versions`):

```bash
go build -o ./bin/caveman-engine ./public/engine/cmd/caveman-engine
go build -o ./bin/caveman-proxy ./public/proxy/cmd/caveman-proxy
```

Caveman Code: `npm install -g @juliusbrussee/caveman-code`. Cavemem: `npm install -g cavemem`.

## Example usage

Compress tool-output JSON through the engine: (../../raw/web/getcaveman.dev.md)

```bash
echo '{"items":[{"id":1,"status":"ok"},…]}' | ./bin/caveman-engine compress
```

Wrap an agent behind the local proxy:

```bash
ANTHROPIC_API_KEY=sk-ant-… ./bin/caveman-proxy
export ANTHROPIC_BASE_URL=http://127.0.0.1:8787
claude   # or codex, gemini, opencode, aider…
```

Skill commands: `/caveman-commit` (≤50-char conventional commits), `/caveman-review` (one-line PR comments), `/caveman-stats` (session token usage + lifetime savings), `/caveman-compress <file>` (rewrite CLAUDE.md-style memory files). Statusline badge shows `[CAVEMAN] ⛏ 12.4k` lifetime tokens saved in Claude Code.

## When to use

Use the **skill alone** when you want shorter agent replies across existing tools with zero infrastructure — ideal for Claude Code, Cursor, Codex, or chat UIs via the browser extension. Build the **engine + proxy** when you need input-side compression of tool output, logs, and diffs, plus local `inferred` spend metering. Add **Caveman Code** when you want a dedicated terminal agent optimized for token budget across 20+ providers. Consider **Cavemem** when agents repeatedly re-send the same context instead of pulling from persistent MCP recall.

Caveman complements workflow skills like those in [[mattpocock-skills]] (which ships its own `/caveman` ultra-compressed mode) and distribution via [[skills.sh]] — it optimizes token economics rather than prescribing planning or TDD process. OpenClaw gateway users can scope install with `--only openclaw` per the README's "Lobster, Meet Rock" section ([[aaif-goose-goose]] ecosystem).

## Maintenance status

GitHub: 78,406 stars, 4,435 forks, JavaScript primary language, MIT license, latest release v1.9.0 (2026-06-12), default branch `main`, homepage caveman.so. Active development with benchmark tables, eval harness, and CI-synced skill files. Managed Cloud gateway is waitlist-only (getcaveman.dev). Contact: contact@caveman.so. (../../raw/github/juliusbrussee-caveman.md)

## Ecosystem

Related products on the same site: **CaveGemma** (compression baked into Gemma weights), **Cavekit** (compressed spec-driven development), **Caveman Proxy/Cloud** (byte-safe LLM gateway with verified savings). Caveman Code is a separate repo (`JuliusBrussee/caveman-code`). The skill references OpenClaw integration, `caveman-shrink` on npm, and cavecrew subagents (~60% fewer tokens than vanilla subagents). Overlaps with terminal/agent platforms like [[warp.dev]] (listed in the install matrix) and memory layers like [[supermemory.ai]] (Cavemem competes as local MCP recall).

## Documentation

Public docs at getcaveman.dev/docs cover Quickstart, Architecture, Honesty rules, Licensing, Compression engine, Proxy, CLI, SDKs, MCP server, and recoverable compression. Only the skill one-liner is published to npm/PyPI today; engine, proxy, CLI, and SDKs build from source. Docs distinguish `inferred` local measurements from future `verified` Cloud receipts.
