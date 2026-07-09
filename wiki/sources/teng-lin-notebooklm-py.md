---
type: source
category: "Knowledge, RAG, memory & context"
source_url: https://github.com/teng-lin/notebooklm-py
tags:
  - notebooklm
  - unofficial-api
  - python-cli
  - mcp-server
  - agent-skills
  - source-grounded
  - grounded-rag
  - research-automation
related:
  - notebooklm.google
  - voltagent-awesome-agent-skills
  - anthropics-skills
  - microsoft-playwright-mcp
  - agents-cli
  - 6eanut-llm-wiki
  - obra-superpowers
  - supermemory.ai
  - kepano-obsidian-skills
  - summio.org
product: notebooklm-py
detail_level: standard
created: 2026-07-02
updated: 2026-07-09
---

notebooklm-py is an unofficial Python library, CLI, and agent skill that exposes Google NotebookLM's full feature surface — including capabilities the web UI does not offer — to programmatic callers and MCP-aware coding agents. With 17,000+ stars (v0.7.3, MIT), it wraps undocumented Google APIs behind a layered architecture (CLI, MCP, and REST adapters over shared transport-neutral business logic), ships a root `SKILL.md` for `npx skills add` discovery, and targets the agentic pattern of offloading heavy document analysis to NotebookLM's grounded Gemini backend while the agent orchestrates and spends tokens only on the final mile.

_All claims below are sourced from ../../raw/github/teng-lin-notebooklm-py.md unless otherwise noted._

## What it does

notebooklm-py gives developers and agents complete programmatic control over NotebookLM notebooks: create and manage notebooks, bulk-import heterogeneous sources (URLs, PDFs, YouTube, Google Drive, pasted text), chat with source-grounded answers, run web/Drive deep-research queries with auto-import, generate every artifact type (audio overviews, video overviews, slide decks, quizzes, flashcards, infographics, data tables, mind maps, reports), and download results in formats the web UI cannot export (batch downloads, quiz/flashcard JSON/Markdown/HTML, mind-map JSON, PPTX slide decks, CSV data tables). It exposes four consumption surfaces — async Python API (`NotebookLMClient`), a `notebooklm` Click CLI, an experimental FastMCP server (`notebooklm-mcp`, 32 tools), and an experimental FastAPI REST server — all sharing the same `_app/` business-logic core.

The library is explicitly unofficial: it reverse-engineers Google's internal batchexecute RPC protocol, carries no Google affiliation, and may break when upstream endpoints change. It is positioned for prototypes, research pipelines, personal automation, and agent workflows rather than production SaaS backends.

## Installation

Recommended install for CLI users and agents is an isolated tool environment:

```bash
uv tool install "notebooklm-py[browser]"   # or: pipx install "notebooklm-py[browser]"
notebooklm login                           # first run downloads Chromium (~170 MB)
notebooklm auth check --test --json
```

Library-only use (no Playwright/Chromium) installs the base package inside a virtualenv: `pip install notebooklm-py` or `uv add notebooklm-py`. Optional extras add `browser` (Playwright login), `mcp` (FastMCP server), `server` (FastAPI REST), and `cookies` (browser-cookie import). Agent skill install: `notebooklm skill install` (writes to `~/.claude/skills/notebooklm` and `~/.agents/skills/notebooklm`) or `npx skills add teng-lin/notebooklm-py`.

## Key features

- **Full NotebookLM coverage** — notebooks, sources (URLs/YouTube/files/Drive/pasted text), chat with custom personas, notes, source labels, web/Drive research agents, and sharing/permissions.
- **All artifact types** — audio (4 formats, 50+ languages), video (9 visual styles), slide decks (PDF/PPTX with per-slide revision), infographics, quizzes, flashcards, reports, data tables, and mind maps (interactive studio or note-backed JSON).
- **Beyond-web-UI exports** — batch artifact downloads, structured quiz/flashcard export, mind-map JSON extraction, CSV data tables, PPTX slides, report template customization, source fulltext access, programmatic sharing, multi-account profiles, and browser-cookie auth import.
- **MCP server (experimental)** — 32 tools over stdio or loopback HTTP; auto-config for Claude Desktop, Claude Code, Cursor, and Windsurf via `notebooklm mcp install <client>`; Docker + Cloudflare/Tailscale tunnel deployment for remote connectors.
- **Agent recipes** — documented patterns for zero-token research offload, web-research-to-expert-skill pipelines, cross-session persistent memory via notebook notes, Obsidian vault sync, multi-format content repurposing, grounded RAG Q&A, incident runbook generation, curriculum builders, and scheduled audio briefings.
- **Bundled agent files** — root `SKILL.md`, `AGENTS.md` (Codex guidance), and `CLAUDE.md` for harness-aware development.

## Architecture

The codebase follows a strict layered design: three thin transport adapters (CLI/`click`, MCP/`fastmcp`, REST/`fastapi`) fan into a transport-neutral `_app/` layer (id validation, plan-building, error classification, retry orchestration — boundary lint-enforced, no framework imports), then into namespaced client APIs (`NotebookLMClient` with `.notebooks`, `.sources`, `.artifacts`, `.chat`, `.notes`, `.mind_maps`, `.research`, `.settings`, `.sharing`, `.labels`), a runtime collaborator graph (`RpcExecutor`, `RuntimeTransport`, `ClientLifecycle`, auth refresh, conversation cache, polling registry), and an RPC encoding layer (`rpc/types.py` method IDs, encoder/decoder). Feature modules depend on narrow capability Protocols rather than a monolithic session facade.

Most calls flow: adapter → feature API → `RpcExecutor.rpc_call` → HTTP batchexecute POST → decoder → typed dataclass. Long-running artifact generation uses a shared poll registry. Guardrail tests in `tests/_guardrails/` enforce CLI boundary rules (no `_private` imports), app-layer purity, and facade reach-in constraints. Python 3.10+ async throughout; 90%+ test coverage with unit, integration (VCR cassettes), server, and authenticated e2e suites.

## Example usage

CLI quick path:

```bash
notebooklm login
notebooklm create "My Research"
notebooklm use <notebook_id>
notebooklm source add "https://example.com/paper"
notebooklm ask "What are the key themes?"
notebooklm generate audio "make it engaging" --wait
notebooklm download audio ./podcast.mp3
```

Python API:

```python
import asyncio
from notebooklm import NotebookLMClient

async def main():
    async with NotebookLMClient.from_storage() as client:
        nb = await client.notebooks.create("Research")
        await client.sources.add_url(nb.id, "https://example.com", wait=True)
        result = await client.chat.ask(nb.id, "Summarize this")
        print(result.answer)

asyncio.run(main())
```

MCP clients connect via `notebooklm mcp install cursor` or manual `uvx --from "notebooklm-py[mcp]" notebooklm-mcp` stdio config.

## Maintenance status

Actively maintained community project: 17,077 stars, 2,324 forks, default branch `main`, latest release v0.7.3 (2026-06-30), last push 2026-07-02. MIT license. Primary development on macOS with CI coverage on Linux and Windows. Uses `uv`, Ruff, mypy, pre-commit, and Playwright for quality gates. APIs are undocumented upstream — the project documents stability policy in `docs/stability.md` and ships a v0.8.0 migration guide for an upcoming error-contract change. Not affiliated with Google; rate limits and endpoint breakage are operational risks called out prominently in the README.
