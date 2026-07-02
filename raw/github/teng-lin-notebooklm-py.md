# teng-lin/notebooklm-py

## Metadata
- Stars: 17077
- Primary language: Python
- Default branch: main
- Latest release: v0.7.3
- License: MIT License
- Homepage: https://github.com/teng-lin/notebooklm-py
- Fetched: 2026-07-02
- Final URL: https://github.com/teng-lin/notebooklm-py

## Description
Unofficial Python API and agentic skill for Google NotebookLM. Full programmatic access to NotebookLM's features—including capabilities the web UI doesn't expose—via Python, CLI, and AI agents like Claude Code, Codex, and OpenClaw.

## README

# notebooklm-py
<p align="left">
  <img src="https://raw.githubusercontent.com/teng-lin/notebooklm-py/main/notebooklm-py.png" alt="notebooklm-py logo" width="128">
</p>

**A Comprehensive NotebookLM Skill & Unofficial Python API.** Full programmatic access to NotebookLM's features—including capabilities the web UI doesn't expose—via Python, CLI, and AI agents like Claude Code, Codex, and OpenClaw.

[![PyPI version](https://img.shields.io/pypi/v/notebooklm-py.svg)](https://pypi.org/project/notebooklm-py/)
[![Python Version](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12%20%7C%203.13%20%7C%203.14-blue)](https://pypi.org/project/notebooklm-py/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Tests](https://github.com/teng-lin/notebooklm-py/actions/workflows/test.yml/badge.svg)](https://github.com/teng-lin/notebooklm-py/actions/workflows/test.yml)
<p>
  <a href="https://trendshift.io/repositories/19116" target="_blank"><img src="https://trendshift.io/api/badge/repositories/19116" alt="teng-lin%2Fnotebooklm-py | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>
</p>

**Source & Development**: <https://github.com/teng-lin/notebooklm-py>

> **⚠️ Unofficial Library - Use at Your Own Risk**
>
> This library uses **undocumented Google APIs** that can change without notice.
>
> - **Not affiliated with Google** - This is a community project
> - **APIs may break** - Google can change internal endpoints anytime
> - **Rate limits apply** - Heavy usage may be throttled
>
> Best for prototypes, research, and personal projects. See [Troubleshooting](docs/troubleshooting.md) for debugging tips.

## What You Can Build

🤖 **AI Agent Tools** - Integrate NotebookLM into Claude Code, Codex, and other LLM agents. Ships with a root [NotebookLM skill](SKILL.md) for GitHub and `npx skills add` discovery, local `notebooklm skill install` support for Claude Code and `.agents` skill directories, and repo-level Codex guidance in [`AGENTS.md`](AGENTS.md).

📚 **Research Automation** - Bulk-import sources (URLs, PDFs, YouTube, Google Drive), run web/Drive research queries with auto-import, and extract insights programmatically. Build repeatable research pipelines.

🎙️ **Content Generation** - Generate Audio Overviews (podcasts), videos, slide decks, quizzes, flashcards, infographics, data tables, mind maps, and study guides. Full control over formats, styles, and output.

📥 **Downloads & Export** - Download all generated artifacts locally (MP3, MP4, PDF, PNG, CSV, JSON, Markdown). Export to Google Docs/Sheets. **Features the web UI doesn't offer**: batch downloads, quiz/flashcard export in multiple formats, mind map JSON extraction.

## Use Cases & Recipes

NotebookLM is a **grounded** engine: Gemini does the heavy reading and answers from *your* sources with citations. The winning pattern is to let it do the expensive analysis while your agent (Claude Code, Codex, …) orchestrates and handles the final mile. Recipes people build on top of this library:

- **🪙 Zero-token research offload** — Throw 30 documents into a notebook, let Gemini do the heavy analysis, and have your agent spend tokens only on the final polish. The agent just orchestrates (`create` → `source add` → `ask`); the reasoning happens server-side.
- **🧠 Web research → expert agent** — Run [Deep Research](docs/cli-reference.md#source-add-research) (`source add-research`) to scan the web into a sourced report, then distill that report into a reusable Claude skill — a packaged domain expert without hand-curating sources.
- **💾 Persistent cross-session memory** — Keep a "Master Brain" notebook; a wrap-up step appends each session's decisions and fixes as notes (`note create` / `ask --save-as-note`), and a line in your `CLAUDE.md` queries it (`ask`) at the start of the next session. Storage and recall live on Google's infrastructure.
- **🕸️ Obsidian / knowledge-graph sync** — Run the CLI from your vault root so downloaded artifacts (reports, mind-map JSON, transcripts) land as files in your knowledge graph; community skills built on this library even resolve NotebookLM's citation markers into Obsidian `[[wikilinks]]`. Pair with a podcast overview for an audio digest of your notes.
- **🔁 Multi-format content repurposing** — One source set, every format: `generate audio` (podcast), `generate video`, `generate slide-deck`, plus a `generate report` blog draft, `generate quiz`, and `generate flashcards` — fan a single notebook out across channels.
- **📞 Grounded knowledge base (RAG)** — Load product docs, FAQs, RFCs, and past tickets, then `ask --json` for **source-grounded, cited** answers for support, on-call, or internal Q&A.
- **🧩 Grounded memory for coding agents** — Expose a notebook of your internal docs/RFCs/architecture over the [MCP server](docs/mcp-guide.md) (or plain `ask`) so an agent answers from *your* code with citations rather than plausible-sounding guesses — a zero-infra alternative to standing up your own vector DB and embedding pipeline.
- **🚨 Incident runbook generator** — On an alert, spin up a notebook of the relevant docs, ask targeted diagnostic questions, and emit a briefing-doc report (`generate report --format briefing-doc`) as an automated runbook.
- **📚 Curriculum / study-set builder** — Scrape a syllabus or developer roadmap, create one notebook per topic (with deliberate pacing to dodge rate limits), and bulk-generate podcasts, quizzes, and flashcards for each.
- **📰 Scheduled audio briefings** — Pair `auth refresh --quiet` (cron/launchd/systemd) with `generate audio` to publish a fresh personalized briefing to a podcast feed on a schedule.

These combine ordinary library primitives — see the [CLI Reference](docs/cli-reference.md) and [Python API](docs/python-api.md). The agent-side glue (skills, scheduling, vault layout) lives in your own setup, not this package.

**Seen in the wild:** ["Claude Code + NotebookLM = CHEAT CODE"](https://www.youtube.com/watch?v=usTeU4Uh0iM) · ["…+ Obsidian = GOD MODE"](https://www.youtube.com/watch?v=kU3qYQ7ACMA) · [a browser-free YouTube→notebook→cited-answers pipeline driven entirely from the terminal](https://artemxtech.substack.com/p/notebooklm-has-a-knowledge-graph) · [a four-workflow guide to offloading heavy document analysis onto NotebookLM so Claude Code stops burning tokens (zero-token research, web-research agents, cross-session memory, an Obsidian "second brain")](https://x.com/hooeem/status/2042293751805329445) · [turning a notebook into the source-grounded "project brain" a coding agent consults before it writes code](https://medium.com/@pradeep00271/every-software-project-needs-a-project-brain-5cbc33917160).

## Ways to Use

| Method | Best For |
|--------|----------|
| **Python API** | Application integration, async workflows, custom pipelines |
| **CLI** | Shell scripts, quick tasks, CI/CD automation |
| **MCP Server** | Exposing NotebookLM tools to Claude Desktop/Code, Cursor, Windsurf, and other MCP clients |
| **REST Server** | Local automation over guarded HTTP routes without spawning a CLI process per call |
| **Agent Integration** | Claude Code, Codex, LLM agents, natural language automation |

## Features

### Complete NotebookLM Coverage

| Category | Capabilities |
|----------|--------------|
| **Notebooks** | Create, list, rename, delete |
| **Sources** | URLs, YouTube, files (PDF, text, Markdown, Word, EPUB, audio, video, images), Google Drive, pasted text; refresh, get guide/fulltext |
| **Chat** | Questions, conversation history, custom personas |
| **Notes** | Create, list, rename, delete, save chat answers, save conversation history |
| **Source Labels** | AI-generated or manual topic labels; add/remove source membership; filter sources by label |
| **Research** | Web and Drive research agents (fast/deep modes) with auto-import |
| **Sharing** | Public/private links, user permissions (viewer/editor), view level control |

### Content Generation (All Artifact Types)

| Type | Options | Download Format |
|------|---------|-----------------|
| **Audio Overview** | 4 formats (deep-dive, brief, critique, debate), 3 lengths, 50+ languages | MP3/MP4 |
| **Video Overview** | 3 formats (explainer, brief, cinematic), 9 visual styles, plus a dedicated `cinematic-video` CLI alias | MP4 |
| **Slide Deck** | Detailed or presenter format, adjustable length; individual slide revision | PDF, PPTX |
| **Infographic** | 3 orientations, 3 detail levels | PNG |
| **Quiz** | Configurable quantity and difficulty | JSON, Markdown, HTML |
| **Flashcards** | Configurable quantity and difficulty | JSON, Markdown, HTML |
| **Report** | Briefing doc, study guide, blog post, or custom prompt | Markdown |
| **Data Table** | Custom structure via natural language | CSV |
| **Mind Map** | Hierarchical node tree — **two kinds**: note-backed JSON or the newer interactive studio map (`--kind` / `MindMapKind`) | JSON |

### Beyond the Web UI

These features are available via API/CLI but not exposed in NotebookLM's web interface:

- **Batch downloads** - Download all artifacts of a type at once
- **Quiz/Flashcard export** - Get structured JSON, Markdown, or HTML (web UI only shows interactive view)
- **Mind map data extraction** - Export hierarchical JSON for visualization tools
- **Data table CSV export** - Download structured tables as spreadsheets
- **Slide deck as PPTX** - Download editable PowerPoint files (web UI only offers PDF)
- **Slide revision** - Modify individual slides with natural-language prompts
- **Report template customization** - Append extra instructions to built-in format templates
- **Save chat to notes** - Save Q&A answers or conversation history as notebook notes
- **Source fulltext access** - Retrieve the indexed text content of any source
- **Programmatic sharing** - Manage permissions without the UI
- **Multi-account profiles** - Switch between Google accounts without re-authenticating
- **Browser cookie import** - Reuse cookies from your existing browser session instead of driving Playwright

## Installation

The full install guide — six personas (agent, end-user, library, headless, contributor, power-user), optional extras matrix, platform notes — lives in **[docs/installation.md](docs/installation.md)**.

**Quickest start** (CLI users and AI agents) — install the CLI with `uv tool` (recommended) or `pipx`:

```bash
uv tool install "notebooklm-py[browser]"   # or: pipx install "notebooklm-py[browser]"
notebooklm login                           # first run auto-downloads Chromium (~170 MB), then Google sign-in
notebooklm auth check --test --json        # verify: expect "status": "ok"
```

**Why `uv tool` / `pipx`?** They install the CLI into its own isolated environment and put `notebooklm` on your `PATH` — no dependency clashes with other tools, a one-line upgrade (`uv tool upgrade notebooklm-py`) or uninstall, and, crucially, they work on modern macOS (Homebrew Python) and Debian/Ubuntu where a system-wide `pip install` is blocked with `error: externally-managed-environment` ([PEP 668](https://peps.python.org/pep-0668/)). No `uv` yet? `curl -LsSf https://astral.sh/uv/install.sh | sh` (or `brew install uv` / `winget install astral-sh.uv`).

**Prefer plain `pip`?** It works the same **inside a virtualenv** (and directly on Windows, where Python isn't externally-managed):

```bash
python3 -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install "notebooklm-py[browser]"
```

**As a library** (embedded in your app — no Playwright, no Chromium):

```bash
uv add notebooklm-py                    # or, inside a virtualenv: pip install notebooklm-py
```

If `playwright install chromium` fails on Linux with `TypeError: onExit is not a function`, see the [Linux workaround](docs/troubleshooting.md#linux). **Contributors:** see [CONTRIBUTING.md](CONTRIBUTING.md).

## Quick Start

<p align="center">
  <a href="https://asciinema.org/a/767284" target="_blank"><img src="https://asciinema.org/a/767284.svg" width="600" /></a>
  <br>
  <em>16-minute session compressed to 30 seconds</em>
</p>

### CLI

```bash
# 1. Authenticate (opens browser)
notebooklm login
# Or use Microsoft Edge (for orgs that require Edge for SSO)
# notebooklm login --browser msedge
# Or reuse cookies from an already-logged-in browser session
# notebooklm login --browser-cookies chrome
# notebooklm login --browser-cookies 'chrome::Profile 1'  # one Chromium profile
# (combine with --profile to populate a specific profile;
#  use --account / --all-accounts after auth inspect when several
#  Google accounts are signed in)

# 2. Create a notebook and add sources
notebooklm create "My Research"
notebooklm use <notebook_id>
notebooklm source add "https://en.wikipedia.org/wiki/Artificial_intelligence"
notebooklm source add "./paper.pdf"

# 3. Chat with your sources
notebooklm ask "What are the key themes?"
notebooklm ask --prompt-file ./long_question.txt  # Read question from file

# 4. Generate content (use --prompt-file for long prompts)
notebooklm generate audio "make it engaging" --wait
notebooklm generate video --style whiteboard --wait
notebooklm generate cinematic-video "documentary-style summary" --wait
notebooklm generate quiz --difficulty hard
notebooklm generate flashcards --quantity more
notebooklm generate slide-deck
notebooklm generate infographic --orientation portrait
notebooklm generate mind-map                       # interactive studio map (default); --kind note-backed for the JSON tree
notebooklm generate data-table "compare key concepts"

# 5. Download artifacts
notebooklm download audio ./podcast.mp3
notebooklm download video ./overview.mp4
notebooklm download cinematic-video ./documentary.mp4
notebooklm download quiz --format markdown ./quiz.md
notebooklm download flashcards --format json ./cards.json
notebooklm download slide-deck ./slides.pdf
notebooklm download infographic ./infographic.png
notebooklm download mind-map ./mindmap.json
notebooklm download data-table ./data.csv
```

Other useful CLI commands:

```bash
notebooklm auth check --test         # Diagnose auth/cookie issues
notebooklm auth refresh --quiet      # One-shot cookie keepalive (for cron / launchd / systemd)
notebooklm auth refresh --browser-cookies chrome  # Re-extract and repair account routing
notebooklm auth inspect --browser 'chrome::Profile 1'  # Preview one Chromium profile
notebooklm agent show codex          # Print bundled Codex instructions
notebooklm agent show claude         # Print bundled Claude Code skill template
notebooklm language list             # List supported output languages
notebooklm metadata --json           # Export notebook metadata and sources
notebooklm share status              # Inspect sharing state
notebooklm source add-research "AI"  # Start web research and import sources
notebooklm skill status              # Check local agent skill installation
notebooklm profile list              # List all Google account profiles
notebooklm profile switch work       # Switch active account profile
```

Use `--prompt-file PATH` with `ask`, prompt-based `generate` commands, and `source add-research` when the text is too long for the shell command line. This reads prompt/query text from a file and is separate from `source add ./file.pdf`, which still uploads that file as a NotebookLM source.

### Python API

```python
import asyncio
from notebooklm import NotebookLMClient, MindMapKind

async def main():
    async with NotebookLMClient.from_storage() as client:
        # Create notebook and add sources
        nb = await client.notebooks.create("Research")
        await client.sources.add_url(nb.id, "https://example.com", wait=True)

        # Chat with your sources
        result = await client.chat.ask(nb.id, "Summarize this")
        print(result.answer)

        # Generate content (podcast, video, quiz, etc.)
        status = await client.artifacts.generate_audio(nb.id, instructions="make it fun")
        await client.artifacts.wait_for_completion(nb.id, status.task_id)
        await client.artifacts.download_audio(nb.id, "podcast.mp3")

        # Generate quiz and download as JSON
        status = await client.artifacts.generate_quiz(nb.id)
        await client.artifacts.wait_for_completion(nb.id, status.task_id)
        await client.artifacts.download_quiz(nb.id, "quiz.json", output_format="json")

        # Generate a mind map via the unified client.mind_maps API (issue #1256) —
        # two kinds: the newer MindMapKind.INTERACTIVE studio map (shown; polled to
        # completion by default) or MindMapKind.NOTE_BACKED JSON. Both export via:
        await client.mind_maps.generate(nb.id, kind=MindMapKind.INTERACTIVE)
        await client.artifacts.download_mind_map(nb.id, "mindmap.json")

asyncio.run(main())
```

### Agent Setup

**Option 1 — CLI install**:

```bash
notebooklm skill install
```

Installs the skill into `~/.claude/skills/notebooklm` and `~/.agents/skills/notebooklm`.

**Option 2 — `npx` install** (via the open skills ecosystem):

```bash
npx skills add teng-lin/notebooklm-py
```

Fetches the canonical [SKILL.md](SKILL.md) directly from GitHub.


## Documentation

- **[CLI Reference](docs/cli-reference.md)** - Complete command documentation
- **[Python API](docs/python-api.md)** - Full API reference
- **[MCP Guide](docs/mcp-guide.md)** - MCP server setup, transports, and tool reference
- **[REST API Server](docs/installation.md#rest-api-server)** - Experimental localhost FastAPI server
- **[Configuration](docs/configuration.md)** - Storage and settings
- **[Release Guide](docs/releasing.md)** - Release checklist and packaging verification
- **[Troubleshooting](docs/troubleshooting.md)** - Common issues and solutions
- **[API Stability](docs/stability.md)** - Versioning policy and stability guarantees
- **[Upgrading to v0.8.0](docs/upgrading-to-0.8.0.md)** - Breaking-change migration guide for the v0.8.0 error-and-return contract

### For Contributors

- **[Architecture](docs/architecture.md)** - Architectural overview and design principles
- **[Development Guide](docs/development.md)** - Architecture, testing, and releasing
- **[RPC Development](docs/rpc-development.md)** - Protocol capture and debugging
- **[RPC Reference](docs/rpc-reference.md)** - Payload structures
- **[Changelog](CHANGELOG.md)** - Version history and release notes
- **[Security](SECURITY.md)** - Security policy and credential handling

## Platform Support

| Platform | Status | Notes |
|----------|--------|-------|
| **macOS** | ✅ Tested | Primary development platform |
| **Linux** | ✅ Tested | Fully supported |
| **Windows** | ✅ Tested | Tested in CI |

## Star History

[![Star History Chart](https://api.star-history.com/image?repos=teng-lin/notebooklm-py&type=timeline&legend=top-left)](https://www.star-history.com/?repos=teng-lin%2Fnotebooklm-py&type=timeline&legend=top-left)

## License

MIT License. See [LICENSE](LICENSE) for details.


## Docs

### docs/architecture.md (excerpt)

# Architecture

This document is the canonical map of `notebooklm-py`'s current runtime shape.
The historical refactor narrative (including the program that first established
this layering) lives in [`docs/refactor-history.md`](./refactor-history.md).

## Layered overview

```text
            three thin, transport-specific adapters
+----------------+  +----------------+  +----------------+
| CLI    (cli/)  |  | MCP    (mcp/)  |  | REST (server/) |
| Click commands |  | FastMCP tools  |  | FastAPI routes |
+----------------+  +----------------+  +----------------+
         \                  |                  /
          \                 |                 /
           +----------------+----------------+
                            ▼
+----------------------------------------------------------+
| Application Layer  (src/notebooklm/_app/*)               |
|   Transport-neutral business logic shared by all three   |
|   adapters: id validation/resolution, plan-building,     |
|   status projection, retry/wait orchestration,           |
|   errors.classify (the single failure-category source),  |
|   diagnostics. Imports no click / rich / fastmcp /       |
|   fastapi (boundary lint-enforced; ADR-0021).            |
+----------------------------------------------------------+
                            ▼
+----------------------------------------------------------+
| Client Layer (client.py + feature APIs)                  |
|   NotebookLMClient + namespaced sub-clients:             |
|     .notebooks  .sources  .artifacts  .chat              |
|     .notes      .mind_maps .research   .settings         |
|     .sharing    .labels                                  |
+----------------------------------------------------------+
                            ▼
+----------------------------------------------------------+
| Runtime Layer (client-owned collaborators)               |
|   ClientComposed + RpcExecutor, RuntimeTransport,        |
|   ClientLifecycle, Kernel.                               |
+----------------------------------------------------------+
                            ▼
+----------------------------------------------------------+
| RPC Layer (src/notebooklm/rpc/*)                         |
|   types.py    method IDs + enums (source of truth)       |
|   encoder.py  request encoding                           |
|   decoder.py  response parsing                           |
+----------------------------------------------------------+
```

Three thin **transport adapters** fan into that one shared core; everything below
`_app/` is then identical regardless of which adapter drove the call — there is
exactly one client runtime and one RPC stack:

| Adapter | Package | Transport | Console script | Install | Failures render as |
| --- | --- | --- | --- | --- | --- |
| **CLI** | `cli/` | terminal (Click) | `notebooklm` | base | exit codes + the byte-stable `--json` error envelope (ADR-0015) |
| **MCP** | `mcp/` | Model Context Protocol (FastMCP) | `notebooklm-mcp` | `mcp` extra · experimental | MCP tool error content (`CODE: message`) |
| **REST** | `server/` | HTTP (FastAPI) | `notebooklm-server` | `server` extra · experimental | HTTP status + `{"error": {"category": "...", "message": "..."}}` |

### Transport-neutral application layer (`_app/`)

The CLI, the MCP server (`mcp/`), and the REST server (`server/`) are each thin
adapters over `src/notebooklm/_app/` — transport-neutral business logic (id
validation/resolution, plan-building, status projection, retry/wait
orchestration, error classification, diagnostics) shared by all three
front-ends. Each adapter parses its transport's inputs into typed
`Request`/`Plan`/`Result` dataclasses, calls the neutral core (which receives the
live client), and renders the typed result into its own envelope vocabulary;
simple reads/mutations call the `client.*` namespaces directly, while multi-step
flows go through the `_app/` cores. The package imports no transport framework —
`click` / `rich` / `fastmcp` / `fastapi`, nor the `cli` / `server` / `rpc`
sibling packages — with the boundary lint-enforced
(`tests/_guardrails/test_app_boundary.py`). It raises only the public
`notebooklm.exceptions` hierarchy, with `_app.errors.classify` as the single
neutral source of the failure-category decision each adapter projects onto its
own codes (CLI exit codes, MCP error shapes, REST HTTP statuses). See ADR-0021.
The per-module index and the full tree are in [File map](#file-map) below.

## Library call flows

`NotebookLMClient` is the composition root. It constructs the shared runtime
collaborator graph, wires feature APIs to narrow runtime Protocols, and
injects stateful services such as `SourceUploadPipeline`, `NoteService`,
`NoteBackedMindMapService`, and `ArtifactDownloadService`. Feature modules
build NotebookLM params and parse domain rows; client-owned collaborators own
dispatch, transport, auth refresh, metrics, and lifecycle.

### Typed batchexecute RPCs

Most public methods (`client.notebooks.list()`, `client.sources.rename()`,
`client.settings.get()`, artifact generation, note CRUD, etc.) follow this path:

```text
+----------------------------------------------------------------+
| CLI command / MCP tool / REST route / library call             |
+----------------------------------------------------------------+
                                 |
                                 v
+----------------------------------------------------------------+
| NotebookLMClient.<feature>.<method>()                          |
|   feature API / service builds params and chooses RPCMethod   |
+----------------------------------------------------------------+
                                 |
                                 v
+----------------------------------------------------------------+
| RpcExecutor.rpc_call(...)                 satisfies RpcCaller  |
|   - pre-open guard via Kernel.get_http_client()                |
|   - logical-RPC request id + rpc_calls_started metric          |
+----------------------------------------------------------------+
                                 |
                                 v
+----------------------------------------------------------------+
| RpcExecutor._execute_once(...)                                 |
|   - idempotency policy resolution                              |
|   - method-id resolution, request encoding, URL/body builder   |
+----------------------------------------------------------------+
                                 |
                                 v
+----------------------------------------------------------------+
| RuntimeTransport.perform_authed_post(...)                      |
|   - loop-affinity guard, auth snapshot                         |
|   - RpcRequest materialization                                 |
+----------------------------------------------------------------+
                                 |
                                 v
+----------------------------------------------------------------+
| ADR-0009 middleware chain                                       |
|   Drain -> Metrics -> Sema -> Retry -> AuthRefresh             |
|   -> ErrInj -> Tracing                                         |
+----------------------------------------------------------------+
                                 |
                                 v
+----------------------------------------------------------------+
| MiddlewareChainHost._authed_post_chain_terminal(...)           |
|   chain leaf — ADR-0014 Rule 4                                  |
+----------------------------------------------------------------+
                                 |
                                 v
+----------------------------------------------------------------+
| RuntimeTransport.terminal(...)                                 |
|   - final auth-freshness rebuild immediately before POST       |
+----------------------------------------------------------------+
                                 |
                                 v
+----------------------------------------------------------------+
| Kernel.post(...) -> _streaming_post -> httpx.AsyncClient       |
+----------------------------------------------------------------+
                                 |
                                 v  response unwinds back up
+----------------------------------------------------------------+
| RpcExecutor decodes via rpc.decode_response(...)               |
| Feature API maps decoded payload -> typed/domain result        |
+----------------------------------------------------------------+
```

Production wires `RpcExecutor` directly into each feature as its
`RpcCaller` per ADR-0014 Rule 1; `NotebookLMClient.rpc_call` dispatches
through the same `RpcExecutor` stored as `NotebookLMClient._rpc_executor`
for the public raw-RPC escape hatch.

`NotebookLMClient.rpc_call(method, params)` is the public raw-RPC escape hatch.
It skips feature-specific param builders and result parsers, but still enters
the same `RpcExecutor.rpc_call → RuntimeTransport → Kernel`
pipeline.

### Chat ask path

`ChatAPI.ask()` is the major transport-sharing exception to the pure
`RpcExecutor` shape. Streaming chat has a custom request body and chat-flavored
error mapping, so the first ask POST goes through:

```text
+----------------------------------------------------------------+
| ChatAPI.ask(...)                                               |
|   - loop_guard.assert_bound_loop()                             |
|   - source-id lookup                                           |
|   - conversation lock / cache                                  |
|   - reqid.next_reqid()                                         |
+----------------------------------------------------------------+
                                 |
                                 v
+----------------------------------------------------------------+
| chat_aware_authed_post(transport, ...)                         |
+----------------------------------------------------------------+
                                 |
                                 v
+----------------------------------------------------------------+
| RuntimeTransport.perform_authed_post(...)                      |
+----------------------------------------------------------------+
                                 |
                                 v
+----------------------------------------------------------------+
| ADR-0009 middleware chain                                       |
+----------------------------------------------------------------+
                                 |
                                 v
+----------------------------------------------------------------+
| RuntimeTransport.terminal(...) -> Kernel.post                  |
+----------------------------------------------------------------+
                                 |
                                 v  streaming response
+----------------------------------------------------------------+
| streaming chat parser + citation/reference parser              |
+----------------------------------------------------------------+
```

`ChatAPI` holds the four collaborators it needs (`rpc`, `transport`,
`reqid`, `loop_guard`) directly — there is no `ChatRuntime` composite
or broad runtime transport indirection.

For a new conversation, `ChatAPI.ask()` then calls `GET_LAST_CONVERSATION_ID`
through the normal `RpcExecutor` path. Other chat methods such as
`get_conversation_turns()` and `delete_conversation()` also use normal
`rpc_call`.

### Uploads, downloads, and polling

Some feature workflows intentionally combine RPC with non-RPC HTTP work:

| Flow | Runtime shape |
|------|---------------|
| Source file upload | `SourcesAPI.add_file()` delegates to `SourceUploadPipeline.add_file()`. The pipeline opens an `operation_scope`, takes its own upload semaphore, registers the file source through `runtime.rpc_call(ADD_SOURCE_FILE)`, then uses a de

...(truncated for standard detail capture)...

### docs/development.md (excerpt)

# Contributing Guide

**Status:** Active
**Last Updated:** 2026-06-11

This guide covers everything you need to contribute to `notebooklm-py`: architecture overview, testing, and releasing.

> **New contributor?** Start with [CONTRIBUTING.md](../CONTRIBUTING.md) at the
> repo root for the install/lint/test workflow and PR conventions, then come
> back here for architectural context once you're ready to write code.

---

## Architecture

> **Canonical post-refactor map:** see [`docs/architecture.md`](./architecture.md)
> for the current adapter/app/client/runtime/RPC graph and
> capability-protocol model. This section
> remains as the contributor on-ramp (package layout + adding-features
> guidance) and links out to the architecture doc rather than duplicating it.

### Package Structure

```
src/notebooklm/
├── __init__.py          # Public exports
├── client.py            # NotebookLMClient main class
├── auth.py              # Public auth facade
├── types.py             # Dataclasses and type definitions
├── _app/                # Transport-neutral business logic shared by adapters
├── _client_composed.py  # Client-owned composition holder
├── _runtime/            # Runtime contracts, config, lifecycle, auth, transport
├── _notebooks.py        # NotebooksAPI implementation
├── _notebook_metadata.py # Private notebook metadata composition service
├── _sources.py          # SourcesAPI implementation
├── _source/             # Private source services
├── _artifacts.py        # ArtifactsAPI implementation
├── _artifact/           # Private artifact services
├── _chat/               # ChatAPI implementation (facade + chat helpers)
├── _research.py         # ResearchAPI implementation
├── _notes.py            # NotesAPI implementation
├── _mind_map.py         # Private note-backed mind-map service
├── _mind_maps_api.py    # MindMapsAPI implementation
├── _labels.py           # LabelsAPI implementation
├── _settings.py         # SettingsAPI implementation
├── _sharing.py          # SharingAPI implementation
├── _sharing_manager.py  # Private legacy notebook share-link service
├── rpc/                 # RPC protocol layer
│   ├── __init__.py
│   ├── types.py         # RPCMethod enum and constants
│   ├── encoder.py       # Request encoding
│   └── decoder.py       # Response parsing
├── cli/                 # Click adapter (`*_cmd.py`) plus `cli/services/`
├── mcp/                 # FastMCP adapter (optional `mcp` extra)
└── server/              # FastAPI REST adapter (optional `server` extra)
```

### Layered Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                      Adapter Layer                          │
│        cli/ (Click), mcp/ (FastMCP), server/ (FastAPI)       │
└───────────────────────────┬─────────────────────────────────┘
                            │
┌───────────────────────────▼─────────────────────────────────┐
│                  App Core Layer (`_app/`)                    │
│        transport-neutral request/plan/result workflows       │
└───────────────────────────┬─────────────────────────────────┘
                            │
┌───────────────────────────▼─────────────────────────────────┐
│                      Client Layer                           │
│  NotebookLMClient → NotebooksAPI, SourcesAPI, ArtifactsAPI  │
│       private services compose cross-facade behavior         │
└───────────────────────────┬─────────────────────────────────┘
                            │
┌───────────────────────────▼─────────────────────────────────┐
│                      Runtime Layer                          │
│          RpcExecutor, RuntimeTransport, Kernel, lifecycle    │
└───────────────────────────┬─────────────────────────────────┘
                            │
┌───────────────────────────▼─────────────────────────────────┐
│                        RPC Layer                            │
│        encoder.py, decoder.py, types.py (RPCMethod)         │
└─────────────────────────────────────────────────────────────┘
```

### Layer Responsibilities

| Layer | Files | Responsibility |
|-------|-------|----------------|
| **Adapters** | `cli/`, `mcp/`, `server/` | User commands/tools/routes, transport-specific input/output, auth envelopes |
| **App core** | `_app/*.py` | Transport-neutral workflows reused by adapters |
| **Client** | `client.py`, `_*.py` | High-level Python API, returns typed dataclasses |
| **Runtime** | `client.py`, `_client_composed.py`, `_runtime/init.py`, `_kernel.py`, runtime collaborators | `NotebookLMClient` composition root plus seam-module helpers (HTTP client lifecycle, RPC dispatch, metrics, drain bookkeeping, request-id counter, auth refresh, conversation cache, polling registry, cookie persistence) |
| **RPC** | `rpc/*.py` | Protocol encoding/decoding, method IDs |

#### Runtime seam modules

The client runtime is split across `NotebookLMClient` (composition root),
`ClientComposed` (holder), `_runtime/init.py` (construction helpers),
`_kernel.py` (HTTP client owner), and single-responsibility collaborator
modules. (The legacy `_core.py` compatibility shim was deleted in v0.5.0;
callers import directly from the canonical modules.) Each helper exposes
a narrow Protocol surface so it can be unit-tested against a stub:

| Module | Class | Responsibility |
|---|---|---|
| `_client_composed.py` | `ClientComposed` | Client-owned holder for transport, executor, chain host, middleware metadata, and session collaborator bundle. |
| `_runtime/init.py` | `RuntimeCollaborators` helpers | Validates constructor args, builds collaborators, wires middleware, and binds `ClientComposed`. |
| `_client_metrics.py` | `ClientMetrics` | `ClientMetricsSnapshot` counters, queue-wait recorders, `on_rpc_event` async callback. |
| `_transport_drain.py` | `TransportDrainTracker` | In-flight transport counters, `_TransportOperationToken`, lazy `asyncio.Condition` powering `client.drain(...)`. |
| `_reqid_counter.py` | `ReqidCounter` | Monotonic `_reqid` counter for chat backend (baseline 100000, step 100000). |
| `_runtime/auth.py` | `AuthRefreshCoordinator` | Refresh-task lifecycle, refresh lock, `AuthSnapshot` rotation. |
| `_runtime/contracts.py` | Runtime Protocols | Shared capability Protocols: `Kernel`, `RpcCaller`, and `LoopGuard`. Single-consumer capabilities stay local to their owner modules. |
| `_runtime/lifecycle.py` | `ClientLifecycle` | Loop-affinity guard, `aclose` plumbing, keepalive task wiring. |
| `_runtime/transport.py` | `RuntimeTransport` | Authenticated transport leg used by `RpcExecutor` and the middleware chain terminal. |
| `_rpc_executor.py` | `RpcExecutor` | RPC dispatch executor with direct collaborator dependencies. |
| `_request_types.py` | `AuthSnapshot`, `BuildRequest`, request materialization | Shared request construction Interface. |
| `_transport_errors.py` | transport exceptions, `parse_retry_after`, `raise_mapped_post_error` | Terminal `Kernel.post` error mapping for middleware retry/auth behavior. |
| `_streaming_post.py` | `stream_post_with_size_cap` | Low-level POST streaming and response-size guard. |
| `_conversation_cache.py` | `ConversationCache` | Per-instance true-LRU conversation cache for `ChatAPI` continuity. Caps the conversation count (`MAX_CONVERSATION_CACHE_SIZE`) and the turns retained per conversation (`MAX_TURNS_PER_CONVERSATION`). |
| `_polling_registry.py` | `PollRegistry` | Pending-poll registry shared by long-running artifact generations. |
| `_cookie_persistence.py` | `CookiePersistence` | Cookie-jar → storage-state serialization, `__Secure-1PSIDTS` rotation. |

The feature-facing surface is the set of **capability Protocols** in
`notebooklm._runtime.contracts` — `Kernel`, `RpcCaller`, and
`LoopGuard`. Single-consumer capability shapes stay in the owning
feature module (`AuthMetadata` in `_source/upload.py`,
`OperationScopeProvider` in `_artifact/polling.py`), and the unused
`AsyncWorkRuntime` composite was deleted. The broad `Session` Protocol


...(truncated for standard detail capture)...

### docs/mcp-guide.md (excerpt)

# MCP server guide

> **Experimental / preview.** The MCP server ships behind the optional `mcp` extra. Its
> tool surface (names, parameters, output shapes) is **not** covered by the library's semver
> guarantees and may change between releases. `pip install notebooklm-py` is unaffected — the
> server and its dependencies only arrive with the `mcp` extra.

The MCP server exposes NotebookLM to any [Model Context Protocol](https://modelcontextprotocol.io)
client (Claude Desktop, Claude Code, Cursor, Windsurf, …) as a set of **32 tools** — manage
notebooks and sources, chat over a notebook's sources, generate and download studio artifacts,
and run deep research. It is a thin adapter over the same business logic the CLI uses, so it
behaves identically to `notebooklm <command>`.

## Install

The server is behind the `mcp` extra (pulls in `fastmcp`):

```bash
pip install "notebooklm-py[mcp]"
# or run with no install, straight from PyPI:
uvx --from "notebooklm-py[mcp]" notebooklm-mcp --help
```

## Authenticate (once)

The server reuses the CLI's stored credentials — it does **not** log in on its own. Authenticate
once before starting it:

```bash
notebooklm login
# or, if you didn't install the package:
uvx --from "notebooklm-py[mcp]" notebooklm login
```

Credentials are stored per profile under `~/.notebooklm/`. The server binds the **active profile**
at startup (override with `--profile`, below). See [configuration.md](configuration.md) for profiles
and multi-account setup.

## Connect a client

The fastest path is the auto-config command, which writes the server block into a client's MCP
config (idempotent, never clobbers other servers):

```bash
notebooklm mcp install claude-desktop   # or: claude-code | cursor | windsurf
```

| Client | Config written |
|--------|----------------|
| `claude-desktop` | `claude_desktop_config.json` (per-OS location) |
| `claude-code` | `~/.claude.json` (user scope) |
| `cursor` | `~/.cursor/mcp.json` |
| `windsurf` | `~/.codeium/windsurf/mcp_config.json` |

It writes a block that launches the server via `uvx` (so only `uv` needs to be on the host):

```jsonc
{
  "mcpServers": {
    "notebooklm": {
      "command": "uvx",
      "args": ["--from", "notebooklm-py[mcp]", "notebooklm-mcp"]
    }
  }
}
```

Restart the client after installing. For a one-click Claude Desktop bundle, see
[`desktop-extension/README.md`](../desktop-extension/README.md).

## Run it directly

The console script is `notebooklm-mcp`:

```bash
notebooklm-mcp                         # stdio transport (default — for desktop hosts)
notebooklm-mcp --profile work          # bind a specific auth profile
notebooklm-mcp --transport http        # loopback streamable-HTTP on 127.0.0.1:9420
notebooklm-mcp --transport http --port 9000
```

| Flag | Default | Notes |
|------|---------|-------|
| `--profile` | active profile | which stored auth profile the process binds |
| `--transport` | `stdio` | `stdio` (subprocess hosts) or `http` (loopback) |
| `--host` | `127.0.0.1` | http only; non-loopback is **refused** unless `NOTEBOOKLM_MCP_ALLOW_EXTERNAL_BIND=1` |
| `--port` | `9420` | http only |
| `--log-level` | `INFO` | logs go to **stderr**; stdout stays pure JSON-RPC |

There is no `--token` flag — the HTTP bearer token is **env-only**
(`NOTEBOOKLM_MCP_TOKEN`) so it cannot leak via `ps aux`.

`stdio` is right for Claude Desktop/Code, Cursor, and Windsurf (they launch the server as a
subprocess). Use `http` for a local web client or to share one running server across clients on
the same machine. The HTTP transport is loopback-only by default; binding to a non-loopback
address requires **both** the explicit `NOTEBOOKLM_MCP_ALLOW_EXTERNAL_BIND=1` override **and** a
`NOTEBOOKLM_MCP_TOKEN` — the server fails closed (refuses to start) on a network bind without a
token, since it fronts a full Google account.

## Remote deployment (Docker + a tunnel)

Because master-token auth keeps the session alive unattended (no browser), the HTTP transport can
run as a **remote connector** reachable from Claude Code, Claude Desktop, claude.ai, and mobile.
The [`deploy/`](../deploy/) directory ships a turn-key Docker + Compose stack with a **tunnel
sidecar** — pick one via a Compose profile — so you get HTTPS with **no public IP, no open ports,
and no TLS certificate to manage** (the tunnel terminates TLS at its edge).

**Common setup (both tunnels):**
```bash
# 1. bootstrap the master token once (a machine with a browser):
notebooklm login --master-token --account you@example.com      # writes ~/.notebooklm/profiles/default
# 2. secrets:
cp deploy/.env.example deploy/.env                              # edit per the steps below
#    NOTEBOOKLM_PROFILE_DIR defaults to ~/.notebooklm/profiles/default (override for a throwaway profile)
```

**Two auth methods coexist on one `/mcp`** (FastMCP `MultiAuth`):
- **Claude Code / Desktop** → the static `NOTEBOOKLM_MCP_TOKEN` bearer (an `Authorization` header).
- **claude.ai (web/mobile)** → optional **self-hosted OAuth** (one password, no external IdP):
  set `NOTEBOOKLM_MCP_OAUTH_PASSWORD` (≥16 random chars) + `NOTEBOOKLM_MCP_OAUTH_BASE_URL`
  (the **bare public origin**, no `/mcp`). Unset → bearer-only.

### Tunnel A — Cloudflare (needs a domain in your Cloudflare account)
1. Cloudflare **Zero Trust → Networks → Tunnels**: create a tunnel; copy its token to
   `CF_TUNNEL_TOKEN` in `.env`.
2. Add a **Public Hostname** (e.g. `notebooklm.yourdomain.com`) → **Service**
   `http://notebooklm-mcp:9420` — the **docker service name**, not `localhost`; route the **whole
   host** (`/`), not a `/mcp`-scoped ingress (the OAuth routes live at the root). Cloudflare
   auto-creates the proxied DNS record and serves a valid cert.
3. `.env`: `NOTEBOOKLM_MCP_OAUTH_BASE_URL=https://notebooklm.yourdomain.com` (bare origin).
4. Run: `cd deploy && make dev` (Cloudflare is the default profile).

### Tunnel B — Tailscale Funnel (no domain — free, stable `*.ts.net` HTTPS)
Best when you don't own a doma

...(truncated for standard detail capture)...

## Top-level structure

- `file` **.dockerignore**
- `file` **.env.example**
- `dir` **.github** — CI workflows
- `file` **.gitignore**
- `file` **.pre-commit-config.yaml**
- `file` **AGENTS.md** — agent instruction / skill files
- `file` **CHANGELOG.md**
- `file` **CLAUDE.md** — agent instruction / skill files
- `file` **CONTRIBUTING.md**
- `file` **LICENSE**
- `file` **README.md**
- `file` **SECURITY.md**
- `file` **SKILL.md** — agent instruction / skill files
- `dir` **deploy** — primary package / docs / examples / CI
- `dir` **desktop-extension** — primary package / docs / examples / CI
- `dir` **docs** — primary package / docs / examples / CI
- `dir` **examples** — primary package / docs / examples / CI
- `file` **notebooklm-py.png**
- `file` **pyproject.toml** — package metadata and optional extras (browser, mcp, server, cookies)
- `dir` **scripts** — primary package / docs / examples / CI
- `dir` **src** — primary package / docs / examples / CI
- `dir` **tests** — primary package / docs / examples / CI
- `file` **uv.lock**