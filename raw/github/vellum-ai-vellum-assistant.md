# vellum-ai/vellum-assistant

## Metadata
- Stars: 841
- Primary language: TypeScript
- Default branch: main
- Latest release: v0.10.6 (2026-07-06)
- License: MIT License
- Homepage: https://vellum.ai
- Fetched: 2026-07-07
- Final URL: https://github.com/vellum-ai/vellum-assistant

## Description
An AI Assistant that's easy to setup, does your work 24/7, knows your preferences and gets better over time.

## README
<p align="center">
  <img src="assets/banner.png" alt="Vellum Assistant" width="100%">
</p>

<p align="center">
  <a href="https://vellum.ai/docs"><img src="https://img.shields.io/badge/Docs-vellum.ai%2Fdocs-FFD700?style=for-the-badge" alt="Documentation"></a>
  <a href="https://vellum.ai/community"><img src="https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Discord"></a>
  <a href="https://github.com/vellum-ai/vellum-assistant/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License: MIT"></a>
  <a href="https://vellum.ai"><img src="https://img.shields.io/badge/Built%20by-Vellum-blueviolet?style=for-the-badge" alt="Built by Vellum"></a>
</p>

<p align="center"><b>A personal AI assistant that evolves with you.</b><br>
8 different types of memory (episodic, semantic, procedural, emotional, prospective, behavioral, narrative, shared) make it truly yours. It learns how you work, remembers what matters, and takes action across your apps.</p>

---

## What it does

If you've set up a Personal AI on OpenClaw, Hermes Agent, or Claude Code, you know how long it takes, and how many times you have to hatch a new one to get it right. Vellum gets you the result you're looking for out of the box, one download away.
| Area                          | Summary |
| ----------------------------- | --- |
| **Memory**                    | Eight types (episodic, semantic, procedural, emotional, prospective, behavioral, narrative, shared), each with its own staleness window, hybrid dense + sparse retrieval, and per-user and per-channel isolation. Structured items (identity, preferences, projects, events) extracted from conversations with source attribution and dedup. Embeddings run locally by default. Not a SQLite + markdown file you maintain yourself. |
| **Identity**                  | Behavior lives in SOUL.md. During onboarding the assistant observes how you communicate and writes its own personality files. It keeps a per-user journal of reflections and uses NOW.md as a scratchpad for current focus and active threads. |
| **Proactivity**               | Every hour the assistant re-reads its notes, looks for anything unfinished or due soon, and messages you if something needs attention. Notifications go to the right channel and won't interrupt an active conversation. |
| **Security**                  | Actor identity (guardian, trusted, unknown) is resolved once and enforced everywhere; unknown actors can't read memory, trigger tools, or escalate. Credentials live in a separate process and never reach the model. Every tool call runs in a sandbox. The default is to deny. |
| **Channels**           | macOS, iOS, Web, Voice, Email, Telegram, Slack, Twilio. One assistant, one memory, every channel. |
| **OAuth**             | Slack, Notion, Google, HubSpot, Linear, Discord, Twitter, Telegram, Twilio. No hand-rolled token refresh. |
| **Hosting**      | Managed runtime on Vellum Platform, or self-hosted. Same codebase, same data model. |

---

## Get started

**1. [Sign up](https://vellum.ai/signup) or [download the app](https://vellum.ai/download)**

**2. Pick your mode**

- **Managed**: sign in via Vellum Cloud, no local runtime required
- **Local**: everything runs on your machine

**3. Hatch your assistant**

- It's yours! Have fun with it.

<sub>Prefer the terminal? See <a href="#cli">CLI install</a> below.</sub>

---

## CLI

**Install**

```bash
bun install -g vellum
vellum hatch
```

**Install from source**

```bash
git clone https://github.com/vellum-ai/vellum-assistant.git
cd vellum-assistant
./setup.sh
source ~/.bashrc
vellum hatch
```

**Common commands**

```bash
vellum wake        # start services
vellum sleep       # stop services, keep data
vellum client      # interact through the terminal
vellum ps          # view running assistants
vellum terminal    # open a shell into a managed assistant container
vellum upgrade     # upgrade to latest version
```

---

## Infra and security

| Area                       | Summary |
| -------------------------- | ------- |
| **Computer use**           | Sandbox by default; with approval reaches your machine for files, commands, browser. Permission-gated (once / ten minutes / always). |
| **Skills**                 | SKILL.md + TOOLS.json plugins add tools at runtime, sandboxed. Catalog, bundle, or workspace drop-in. |
| **Channels**               | One assistant, one memory — macOS app, Telegram, Slack; cross-channel continuity. |
| **Multi-provider support** | Anthropic, OpenAI, Google Gemini, Fireworks, OpenRouter, MiniMax, Atlas Cloud, OpenAI-compatible endpoints, Ollama local. Embeddings: local ONNX default, cloud fallback. |

---

## Foundational documents

| Doc | What it is |
| --- | --- |
| [Constitution](CONSTITUTION.md) | Purpose, worldview, principles |
| [Glossary](GLOSSARY.md) | Shared vocabulary for personal intelligence |

---

## Documentation

| Section | What's covered |
| --- | --- |
| Architecture | Platform domains, repo structure, runtime · clients · gateway |
| Security & Permissions | Sandbox, credentials, trust rules |
| Features & Capabilities | Integrations, dynamic skills, browser, attachments |
| API & Communication | SSE event stream, remote access |
| Development Workflow | Claude Code commands, PRs, release pipeline |

Full docs: https://vellum.ai/docs

## Top-level structure

```
/
├── assistant/            # Bun-based assistant runtime (runtime, CLI, HTTP API)
├── clients/              # Native macOS client (menu bar app)
├── gateway/              # Gateway service (Telegram, Twilio, OAuth, reverse proxy)
├── credential-executor/  # Credential Execution Service (isolated RPC boundary)
├── packages/             # Shared private packages (CES contracts, credential storage)
├── cli/                  # Vellum CLI
├── skills/               # Bundled skill definitions
├── plugins/              # Plugin system
├── docs/                 # Documentation source
├── benchmarking/         # Load testing scripts
├── scripts/              # Utility scripts (publishing, tunneling, releases)
├── meta/                 # Meta configuration
├── .claude/              # Claude Code slash commands and workflow tools
└── .github/              # GitHub Actions workflows
```

Key files: `AGENTS.md`, `ARCHITECTURE.md`, `CONSTITUTION.md`, `GLOSSARY.md`, `CONTRIBUTING.md`, `SECURITY.md`, `setup.sh`
