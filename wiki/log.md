---
type: log
domain: "Agentic AI"
created: 2026-04-25
---

# Agentic AI wiki — log

Append-only record of all ingests, refreshes, and significant changes. Newest entries at top.

---

## 2026-04-25 | update | agent instructions | Git — never auto-commit

- Updated: `AGENTS.md`, `.cursor/rules/wiki-instructions.mdc`, `.github/copilot-instructions.md`, `.pin-llm-wiki.yml` — all agents must not run `git commit` / `git push` after ingests, refresh, lint, remove, or scaffold unless the human explicitly asks.

---

## 2026-04-25 | update | config | removed `auto_commit` from `.pin-llm-wiki.yml`

- Updated: `.pin-llm-wiki.yml`, `AGENTS.md`, `.cursor/rules/wiki-instructions.mdc`, `.github/copilot-instructions.md` — align with pin-llm-wiki: no `auto_commit` key; **Git — never auto-commit** remains the rule for agents.

---

## 2026-04-25 | ingest | gsd-build-get-shit-done | GET SHIT DONE — meta-prompting + spec-driven development system for AI coding assistants (57k stars)

- Created: wiki/sources/gsd-build-get-shit-done.md
- Updated: wiki/index.md, wiki/overview.md, wiki/log.md, raw/github/README.md, inbox.md

---

## 2026-04-25 | update | agent instructions | Cursor skill parity in Phase 1 note

- Updated: `AGENTS.md`, `.cursor/rules/wiki-instructions.mdc`, `.github/copilot-instructions.md` — document `/pin-llm-wiki` via installed Cursor skill; Copilot and other tools without the skill still use manual workflow steps (aligned with pin-llm-wiki `AGENTS.md.tmpl`).

---

## 2026-04-25 | lint | auto-fix — 6 topic stubs created

- Created: wiki/topics/ai-agent-orchestration.md, wiki/topics/embedded-html-apps.md, wiki/topics/web-terminal.md, wiki/topics/scheduled-jobs.md, wiki/topics/full-text-search.md, wiki/topics/wysiwyg-editor.md
- Updated: wiki/index.md

---

## 2026-04-25 | ingest | hilash-cabinet | Cabinet GitHub repo — TypeScript agentic knowledge base OS with provider adapter layer

- Created: wiki/sources/hilash-cabinet.md
- Updated: wiki/index.md, wiki/overview.md, wiki/log.md, raw/github/README.md, inbox.md

---

## 2026-04-25 | ingest | runcabinet.com | Cabinet — AI-first self-hosted knowledge base OS with agent orchestration

- Created: wiki/sources/runcabinet.com.md
- Updated: wiki/index.md, wiki/overview.md, wiki/log.md, raw/web/README.md, inbox.md

---

## 2026-04-25 | ingest | coleam00-claude-memory-compiler | Claude Code session memory compiler using hooks + Claude Agent SDK

- Created: wiki/sources/coleam00-claude-memory-compiler.md
- Updated: wiki/index.md, wiki/overview.md, wiki/log.md, raw/github/README.md, inbox.md

---

## 2026-04-25 | init | wiki scaffolded

- Created `.pin-llm-wiki.yml`
- Created `inbox.md`, `CLAUDE.md`, `raw/`, `wiki/`
