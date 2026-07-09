---
type: source
category: "Knowledge, RAG, memory & context"
source_url: https://tolaria.md/
companion_urls:
  - https://github.com/refactoringhq/tolaria
raw_files:
  - ../../raw/web/tolaria.md.md
  - ../../raw/github/refactoringhq-tolaria.md
tags:
  - personal-knowledge-management
  - second-brain
  - markdown-notes
  - local-first
  - git-first
  - ai-agents
  - offline-first
  - open-source
related:
  - supermemory.ai
  - runcabinet.com
product: tolaria
detail_level: standard
created: 2026-06-29
updated: 2026-06-29
---

Tolaria is a free, open-source, local-first desktop knowledge base for macOS, Windows, and Linux that stores all notes as plain Markdown files on disk, integrates Git as a first-class history and sync layer, and wires AI coding agents (Claude Code, Codex, OpenCode, Pi, Gemini) directly into the vault workflow. Built by Luca Rossi from five years of managing 10,000+ notes for the Refactoring newsletter, Tolaria fills the gap between plain Markdown editors and cloud-locked note apps, offering rich editing, typed relationships, spreadsheets, and AI chat — all without accounts, subscriptions, or proprietary formats.

_All claims below are sourced from ../../raw/web/tolaria.md.md unless otherwise noted._

## What it does

Tolaria treats a folder of Markdown files as a vault. Users write notes in a block-based editor that saves as Markdown; structured metadata lives in YAML frontmatter. The app provides typed relationships (a `belongs_to` field automatically generates an inverse `has` relationship), custom views and spreadsheets, and an inbox for capturing and organizing new material. Notes connect via `[[wikilinks]]` with autocomplete, and the Properties panel shows both outgoing and incoming relationships for any note.

Multiple vaults can run in one unified graph — each note retains a vault badge when disambiguation is needed, while Git status, commits, and sync stay scoped per vault.

## Key features

- **Plain Markdown on disk** — every note is a `.md` file with YAML frontmatter; no database, no proprietary format, readable by any tool
- **Block-based editor** — slash commands, wikilinks, whiteboards, media previews, table navigation, note width controls
- **Native relationships** — frontmatter fields containing wikilinks become typed relationships with auto-computed inverses; Neighborhood mode shows a graph view around any note
- **Spreadsheets** — notes with `_display: sheet` open as a spreadsheet editor while remaining plain files
- **Integrated Git client** — commit, pull, push, view whole-vault and per-note history and diffs from within the app (../../raw/github/refactoringhq-tolaria.md)
- **AI coding agents** — streams Claude Code, Codex, OpenCode, Pi, and Antigravity CLI through a normalized event layer; Vault Safe and Power User modes
- **Direct model providers** — chat mode against Ollama, LM Studio, OpenAI, Anthropic, Gemini, OpenRouter, or any OpenAI-compatible endpoint
- **MCP server** — Tolaria exposes an MCP server; setup flow writes the entry into Claude Code, Cursor, Antigravity CLI, or a generic config path
- **Multi-vault graph** — load multiple vaults into one unified search, note list, and navigation graph

## Architecture

Tolaria is built with Tauri (Rust shell + WebKit renderer), React, and TypeScript. The filesystem is the single source of truth; app cache and React state are always derived from disk and must be reconstructible by deleting them. Three representations coexist — filesystem (`.md` files), `~/.laputa/cache/` JSON index for fast startup, and `VaultEntry[]` in-memory React state — and the filesystem wins on any divergence. (../../raw/github/refactoringhq-tolaria.md)

Relationship fields are detected dynamically at runtime by scanning frontmatter for values containing `[[wikilinks]]` — no hardcoded field name lists. Standard conventions (`belongs_to`, `has`, `related_to`, `type:`, `status:`) trigger dedicated UI behavior out of the box, making vault structure legible to both humans and AI agents without bespoke configuration. (../../raw/github/refactoringhq-tolaria.md)

Vault-level state (type icons, saved views, pinned properties) travels with the vault folder. Machine-specific preferences (zoom, window size, API keys) stay in `~/.config/com.tolaria.app/`.

## Installation

**Homebrew (macOS):**
```bash
brew install --cask tolaria
```

**Download:** macOS, Windows, and Linux builds at https://tolaria.md/download/ (../../raw/github/refactoringhq-tolaria.md)

Platforms: macOS (primary, Apple Silicon + Intel), Windows (supported, early; Authenticode-signed), Linux (supported, early; AppImage, deb, RPM).

## Example usage

1. Open Tolaria and clone the Getting Started vault for a guided walkthrough.
2. Create a note by typing a title, add frontmatter fields like `type: Project` and `belongs_to: "[[workspace]]"`.
3. Connect notes with `[[wikilinks]]` in the body; inverse relationships appear automatically in the Properties panel.
4. Commit changes from the Git panel; push to a remote for cross-device sync.
5. Open the AI panel, select Claude Code in Vault Safe mode, and ask it to restructure notes — changes show up as a reviewable diff before commit. (../../raw/github/refactoringhq-tolaria.md)

## When to use

Tolaria is suited for individuals and teams who want a durable, portable knowledge base that works offline, scales to tens of thousands of notes, and integrates naturally with AI coding agents. It is a strong choice when:

- You want full data ownership (no cloud lock-in, AGPL-3.0 licensed open source)
- Your workflow already involves Git, terminal tools, and CLI AI agents
- You need structured, typed, relationship-aware notes rather than unstructured files
- You want AI agents to read and write vault notes with the same Git-inspectable history as code changes

Compare with [[supermemory.ai]] for a cloud-hosted memory layer focused on RAG retrieval for agents, and [[runcabinet.com]] for a structured knowledge base with automation and agent context management.

## Ecosystem

- **Getting Started vault** — sample vault at `github.com/refactoringhq/tolaria-getting-started`
- **Refactoring newsletter** — Luca Rossi's newsletter at `refactoring.fm`; 170,000+ subscribers; primary update channel for Tolaria
- **GitHub** — `github.com/refactoringhq/tolaria` (17,215+ stars, TypeScript, AGPL-3.0) (../../raw/github/refactoringhq-tolaria.md)
- **MCP integration** — built-in MCP server connects Tolaria vaults as tool-accessible context for any MCP-compatible agent
- **Agent instructions** — ships `AGENTS.md`, `CLAUDE.md`, and `GEMINI.md` in the repo for contributors using AI agents (../../raw/github/refactoringhq-tolaria.md)
- **Community** — GitHub Discussions at `github.com/refactoringhq/tolaria/discussions`; feature requests at `tolaria.canny.io`
