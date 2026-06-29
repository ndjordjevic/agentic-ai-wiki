# tolaria.md

## Fetch log
- Inbox URL: https://tolaria.md/
- Final URL: https://tolaria.md/
- Fetched: 2026-06-29
- Pages: 7
- Mode: standard

## Landing page — https://tolaria.md/

## A second brain for the AI era. Free forever.

Organize your notes as Markdown files, with native relationships, Git, local agents, and direct AI model providers.

Open source, free forever, no account required

Architecture

### Just files on your disk

Every note is a Markdown file with a YAML frontmatter. No database, no proprietary format. Read them with any editor, grep them from the terminal, version them with Git.

Editor

### Writes richly, saves as Markdown

Block-based editing with slash commands, wikilinks, raw Markdown, whiteboards, media previews, table navigation, and note width controls. Everything durable stays in vault files.

Version control

### Fully integrated Git client

Commit, push, and browse history from within the app. Every change tracked. Sync across devices with the same tool you already trust for code.

AI

### Local agents and direct models

Use CLI coding agents such as Claude Code, Codex, OpenCode, Pi, and Gemini when you want tool-backed editing. Use local or API model providers for chat over note context without vault-write tools.

Documentation

### Learn the app the way it is built

The docs sit in the app repo so product behavior, architecture, and user-facing guidance can evolve together.

- Start with a vault: Install Tolaria, open the Getting Started vault, and understand the first-launch flow. https://tolaria.md/start/install
- Understand the model: Learn how notes, properties, types, relationships, custom views, Git, and AI fit together. https://tolaria.md/concepts/vaults
- Follow workflows: Capture notes, organize the inbox, use wikilinks, create types, push changes, configure AI, and navigate long notes. https://tolaria.md/guides/capture-a-note
- Keep docs current: Use the maintenance checklist when code changes affect commands, models, integrations, or platform behavior. https://tolaria.md/reference/docs-maintenance

Made with Love

### Built by Luca, for Luca

Tolaria is the product of the learnings from 5 years of full-time content creation. I published 300+ articles and organized my knowledge into 9000+ notes.

Tolaria is born from 5 years of full-time writing at Refactoring, during which I have written 300+ articles about software engineering and developer productivity. Along the way, I amassed 9000+ notes on my Notion workspace, learned a lot about knowledge management, productivity, and, more recently, on working well with AI on docs. None of the existing tools matched what I wanted, so I built one myself.

- 5 years full-time writing
- 300+ articles published
- 170,000+ newsletter subscribers

Subscribe to the Refactoring newsletter for updates on Tolaria: https://refactoring.fm/

GitHub repo referenced: https://github.com/refactoringhq/tolaria/releases (companion: github.com/refactoringhq/tolaria)

## Docs — https://tolaria.md/start/install

## Install Tolaria

Tolaria publishes desktop builds for macOS, Windows, and Linux. macOS is the primary day-to-day development target, with Windows and Linux builds supported through the release pipeline and fixed as platform issues are found.

### Download

Use the latest stable release unless you are intentionally testing pre-release builds:

- Download the latest stable build: https://tolaria.md/download/
- Browse all GitHub releases: https://github.com/refactoringhq/tolaria/releases
- Read the release notes: https://tolaria.md/releases/

### Homebrew

On macOS:

```bash
brew install --cask tolaria
```

### Platform Status

| Platform | Status | Notes |
| --- | --- | --- |
| macOS | Primary | Apple Silicon and Intel builds published. Homebrew available. |
| Windows | Supported, early | NSIS installers; Authenticode signing pending. |
| Linux | Supported, early | AppImage, deb, and RPM artifacts published. |

## Concepts — Vaults — https://tolaria.md/concepts/vaults

A vault is the folder Tolaria reads and writes. The filesystem is the source of truth; the app state and cache are derived from files.

Core rules:
- Notes are Markdown files.
- YAML frontmatter provides structure.
- Attachments are normal files inside the vault.
- Type definitions and saved views are also files.
- Git can track history and support remote sync.

Tolaria can load multiple registered vaults into one unified graph. Cross-vault wikilinks use the target vault's stable alias.

Vault state (type icons, saved views, pinned properties) travels with the vault. Machine-specific preferences stay with the app installation.

## Concepts — Notes — https://tolaria.md/concepts/notes

A note is a Markdown file with optional YAML frontmatter. Tolaria reads the first H1 as the primary title and keeps the file on disk as the durable representation.

Use `[[wikilinks]]` to connect notes from the body. Tolaria shows autocomplete suggestions while you type. Notes with `_display: sheet` open as spreadsheets.

## Concepts — Relationships — https://tolaria.md/concepts/relationships

Any frontmatter field containing wikilinks can become a relationship. Tolaria supports default relationship fields: `belongs_to`, `has`, and `related_to`. Default relationships have automatically computed inverses — if a note says it `belongs_to` a project, the project shows that note under its `has` relationship without reverse links.

Relationships appear in the Properties panel and in Neighborhood mode (graph view around the selected note).

## Concepts — Git — https://tolaria.md/concepts/git

Git is Tolaria's recommended history and sync layer. Tolaria acts as a lightweight Git client:

- Whole-vault commit history
- Per-note history and current diff
- Pull and push
- Conflict detection and resolution
- Remote connection for local-only vaults

Connect a compatible Git remote when you want sync or backup. Tolaria relies on system Git authentication (GitHub CLI, SSH keys, credential helpers).

## Concepts — AI — https://tolaria.md/concepts/ai

Tolaria has two AI paths:

**Coding Agents:** The AI panel streams supported local CLI agents through Tolaria's normalized event layer. Targets: Claude Code, Codex, OpenCode, Pi, and Antigravity CLI. Agents run in Vault Safe mode (file, search, edit tools) or Power User mode (local shell commands scoped to vault).

**Direct Models:** Chat mode. Active note, linked context, and conversation history — no vault-write tools or shell access. Supports Ollama, LM Studio, OpenAI, Anthropic, Gemini, OpenRouter, and custom OpenAI-compatible endpoints.

**External MCP Setup:** Tolaria exposes an MCP server. Setup flow writes Tolaria's MCP entry into Claude Code, Antigravity CLI, Cursor, or a generic MCP config path.

AI-generated changes are inspectable via Git diffs and history.
