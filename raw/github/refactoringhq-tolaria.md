# refactoringhq/tolaria

## Metadata
- Stars: 17,215
- Primary language: TypeScript
- Default branch: main
- Latest release: alpha-v2026.6.29-alpha.0003 (2026-06-29)
- License: GNU Affero General Public License v3.0 (AGPL-3.0)
- Homepage: https://tolaria.md
- Fetched: 2026-06-29
- Final URL: https://github.com/refactoringhq/tolaria

## Description
Desktop app to manage markdown knowledge bases

## README

![Latest stable](https://img.shields.io/github/v/release/refactoringhq/tolaria?display_name=tag) [![CI](https://github.com/refactoringhq/tolaria/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/refactoringhq/tolaria/actions/workflows/ci.yml)

# 💧 Tolaria

Tolaria is a desktop app for macOS, Windows, and Linux for managing **markdown knowledge bases**. People use it for a variety of use cases:

* Operate second brains and personal knowledge
* Organize company docs as context for AI
* Store OpenClaw/assistants memory and procedures

Personally, I use it to **run my life** (hey 👋 [Luca here](http://x.com/lucaronin)). I have a massive workspace of 10,000+ notes, which are the result of my [Refactoring](https://refactoring.fm/) work + a ton of personal journaling and *second braining*.

## Walkthroughs

- How I Organize My Own Tolaria Workspace: https://www.loom.com/share/bb3aaffa238b4be0bd62e4464bca2528
- My Inbox Workflow: https://www.loom.com/share/dffda263317b4fa8b47b59cdf9330571
- How I Save Web Resources to Tolaria: https://www.loom.com/share/8a3c1776f801402ebbf4d7b0f31e9882

## Principles

- 📑 **Files-first** — Your notes are plain markdown files. Portable, work with any editor, require no export step.
- 🔌 **Git-first** — Every vault is a git repository. Full version history, any git remote, zero dependency on Tolaria servers.
- 🛜 **Offline-first, zero lock-in** — No accounts, no subscriptions, no cloud dependencies. Your vault works completely offline.
- 🔬 **Open source** — Tolaria is free and open source.
- 📋 **Standards-based** — Notes are markdown files with YAML frontmatter. No proprietary formats.
- 🔍 **Types as lenses, not schemas** — Types in Tolaria are navigation aids, not enforcement mechanisms. No required fields, no validation.
- 🪄 **AI-first but not AI-only** — A vault of files works very well with AI agents. Supports Claude Code, Codex CLI, and Gemini CLI setup paths. Provides an AGENTS file for agents.
- ⌨️ **Keyboard-first** — Designed for power-users who want to use keyboard as much as possible.
- 💪 **Built from real use** — Created to manage a personal vault of 10,000+ notes, used every day.

## Installation

### Homebrew

```bash
brew install --cask tolaria
```

### Download from releases

Download the latest release: https://refactoringhq.github.io/tolaria/download/ for macOS, Windows, or Linux.

## Getting started

When you open Tolaria for the first time you get the chance of cloning the getting started vault (https://github.com/refactoringhq/tolaria-getting-started).

The public user docs live in `site/` and are published to GitHub Pages. Start with [Install Tolaria](site/start/install.md), then [First Launch](site/start/first-launch.md).

## Open source and local setup

Built with Tauri, React, and TypeScript.

### Prerequisites

- Node.js 20+
- pnpm 8+
- Rust stable
- macOS or Linux for development

### Quick start

```bash
pnpm install
pnpm dev
```

Run the native desktop app:

```bash
pnpm tauri dev
```

## Tech Docs

- 📐 [ARCHITECTURE.md](docs/ARCHITECTURE.md) — System design, tech stack, data flow
- 🧩 [ABSTRACTIONS.md](docs/ABSTRACTIONS.md) — Core abstractions and models
- 🚀 [GETTING-STARTED.md](docs/GETTING-STARTED.md) — How to navigate the codebase
- 📚 [ADRs](docs/adr) — Architecture Decision Records

## License

Tolaria is licensed under AGPL-3.0-or-later.

## Docs — ARCHITECTURE.md

Tolaria is a personal knowledge and life management desktop app. It reads a vault of markdown files with YAML frontmatter and presents them in a four-panel UI inspired by Bear Notes.

### Design Principles

**Filesystem as the single source of truth:** The vault is a folder of plain markdown files. The app never owns the data — it only reads and writes files. When in doubt, the file on disk wins.

**Convention over configuration:** Standard field names (`type:`, `status:`, `url:`, `belongs_to:`, `related_to:`, `has:`) have well-defined meanings and trigger specific UI behavior without setup. Relationship defaults are detected dynamically by checking whether values contain `[[wikilinks]]`. This serves AI-readability: the more structure comes from shared conventions, the easier for an AI agent to navigate correctly.

**Three representations, one authority:** Vault data exists as (1) filesystem — `.md` files on disk (source of truth), (2) cache — `~/.laputa/cache/<hash>.json` for fast startup, (3) React state — `VaultEntry[]` in-memory session. These must never diverge permanently. If they do, the filesystem wins and cache/state are rebuilt.

**AI-first knowledge graph:** Notes are nodes in a structured graph of people, projects, events, responsibilities, and ideas. Every design decision asks: "Does this make the knowledge graph easier for a human *and* an AI to navigate?"

**No hardcoded exceptions:** No field names, folder paths, or vault-specific values should be hardcoded in application source code. Relationship fields are detected dynamically.

### Tech Stack

Built with Tauri (Rust shell + WebKit renderer), React, and TypeScript frontend. The `src-tauri/` directory contains the Rust shell; `src/` contains the React/TypeScript frontend.

## Top-level structure

```
AGENTS.md         — AI agent instructions (references ARCHITECTURE.md, ABSTRACTIONS.md)
CLAUDE.md         — Claude-specific agent instructions
GEMINI.md         — Gemini-specific agent instructions
CONTRIBUTING.md   — Contribution guide
docs/             — Architecture docs: ARCHITECTURE.md, ABSTRACTIONS.md, GETTING-STARTED.md, adr/
e2e/              — End-to-end tests (Playwright)
mcp-server/       — Bundled MCP server for external tool integration
site/             — User docs (published to GitHub Pages / tolaria.md)
src/              — React/TypeScript frontend source
src-tauri/        — Tauri/Rust native shell
tests/            — Unit and integration tests
```
