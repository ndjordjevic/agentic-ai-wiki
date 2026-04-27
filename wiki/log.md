---
type: log
domain: "Agentic AI"
created: 2026-04-25
---

# Agentic AI wiki — log

Append-only record of all ingests, refreshes, and significant changes. Newest entries at top.

---

## 2026-04-27 | cleanup | source pages — added source_url + populated product on all sources

- Updated: all 5 wiki/sources/*.md — added `source_url:` frontmatter field with canonical URL (GitHub repo, website); replaced `product: null` with meaningful product slug on independent sources (`claude-memory-compiler`, `gsd`, `superpowers`); `cabinet` sources unchanged.
- Updated: AGENTS.md (frontmatter schema, Step 2 rules, Step 2b derivation rules, Frontmatter rules block); re-synced .cursor/rules/wiki-instructions.mdc and .github/copilot-instructions.md.
- Updated: pin-llm-wiki/skill/ingest.md (same schema and Step 2b changes), pin-llm-wiki/skill/templates/AGENTS.md.tmpl (mirrored).
- Reason: `product: null` appeared empty/meaningless to users; independent sources now carry their own product identifier. `source_url` gives each page a direct clickable link to the original source (GitHub repo, website, YouTube video).

---

## 2026-04-27 | ingest | microsoft-playwright-mcp | Playwright MCP — official Microsoft MCP server for browser automation via accessibility snapshots (31k stars)

- Created: wiki/sources/microsoft-playwright-mcp.md
- Created: raw/github/microsoft-playwright-mcp.md
- Updated: wiki/index.md, wiki/overview.md, wiki/log.md, raw/github/README.md, inbox.md

---

## 2026-04-27 | ingest | paperclipai-paperclip | Paperclip GitHub — open-source agent company orchestrator with org chart, budgets, governance (59k stars)

- Created: wiki/sources/paperclipai-paperclip.md
- Created: raw/github/paperclipai-paperclip.md
- Updated: wiki/index.md, wiki/overview.md, wiki/log.md, raw/github/README.md, inbox.md
- Updated: wiki/sources/hilash-cabinet.md, wiki/sources/gsd-build-get-shit-done.md (bidirectional `related` links added)
- Product grouping: paperclipai-paperclip.homepageUrl = https://paperclip.ing → matches web source slug `paperclip.ing` → both set to `product: paperclip.ing`

---

## 2026-04-27 | ingest | paperclip.ing | Paperclip website — human control plane for AI labor, autonomous company platform

- Created: wiki/sources/paperclip.ing.md
- Created: raw/web/paperclip.ing.md
- Updated: wiki/index.md, wiki/overview.md, wiki/log.md, raw/web/README.md, inbox.md

---



- Created: wiki/sources/obra-superpowers.md
- Created: raw/github/obra-superpowers.md
- Updated: wiki/index.md, wiki/overview.md, wiki/log.md, raw/github/README.md, inbox.md
- Updated: wiki/sources/gsd-build-get-shit-done.md (bidirectional `related` link added)

---

## 2026-04-27 | cleanup | populate tags + related on all source pages

- Updated: all 4 wiki/sources/*.md — populated `tags` (4–11 specific kebab-case terms each: persistent-memory, claude-code-hooks, knowledge-base, agent-orchestration, provider-adapter, meta-prompting, etc.) and `related` (bidirectional wikilinks between conceptually overlapping sources). `product:` field unchanged (cabinet sources stay grouped; the other two stay null). `updated:` bumped to 2026-04-27 on all four.
- Bidirectional `related` verified — every cross-link is reciprocal (coleam00↔hilash, coleam00↔runcabinet, coleam00↔gsd, hilash↔runcabinet, hilash↔gsd; runcabinet and gsd don't link to each other by mutual omission, since the marketing-site/workflow-tool overlap is weak).
- Updated: AGENTS.md (rule reversed: `tags` and `related` are now populated at ingest time with explicit guidance, and a bidirectional-update step is required so older pages gain forward links to newer ones). Cursor and Copilot adapters re-synced.
- Skill updated upstream: pin-llm-wiki/skill/ingest.md Step 2 — same rule reversal and bidirectional-update guidance for future ingests.
- Reason: leaving frontmatter empty produced a sparse, unnavigable wiki — Obsidian graph view and lint Check #5 both rely on populated `related` to surface connections. Populating at ingest gives immediate value rather than deferring to a separate editorial pass.

---

## 2026-04-27 | cleanup | adapter sync — Cursor + Copilot mirrors of AGENTS.md

- Updated: .cursor/rules/wiki-instructions.mdc (full body re-synced from AGENTS.md, Cursor frontmatter preserved), .github/copilot-instructions.md (verbatim copy of AGENTS.md), AGENTS.md (added Check #11 to lint table + Auto-fix bullet).
- Reason: manual edits to AGENTS.md (product field, Step 2b, topic_creation, no-H1 rule, paragraph-count invariant, etc.) had not propagated to the Cursor/Copilot adapters. Cursor and Copilot were therefore reading older instructions than Claude Code, producing inconsistent agent behavior across the three tools that share this wiki.
- Skill updated upstream: pin-llm-wiki/skill/lint.md adds Check #11 (adapter sync) with Auto-fix 3 (re-sync drifted adapters from AGENTS.md), so this drift will be caught and fixed automatically by future `/pin-llm-wiki lint` runs.
- Home-folder skill installs verified: ~/.claude/skills/pin-llm-wiki, ~/.cursor/skills/pin-llm-wiki, and ~/.copilot/skills/pin-llm-wiki are all symlinks to /home/ndjordjevic/Projects/LLM/pin-llm-wiki/skill — single source of truth for all three tools.

---

## 2026-04-27 | cleanup | source-page consistency + overview gap

- Updated: wiki/sources/gsd-build-get-shit-done.md — removed H1 heading, removed `---` horizontal rules between sections, reset `tags` and `related` to `[]`, added `product: null`, folded the standalone "Configuration" section into "Key Features", added a missing "Example Usage" section.
- Updated: wiki/sources/coleam00-claude-memory-compiler.md — added `product: null` for schema consistency.
- Updated: wiki/overview.md — added the missing dedicated paragraph for [[hilash-cabinet]] (overview previously had 3 paragraphs for 4 sources); refreshed `updated:` to 2026-04-27.
- Reason: source pages were inconsistent in headings, frontmatter, and section structure; `wiki/overview.md` violated the one-paragraph-per-source invariant. Skill updated upstream — see pin-llm-wiki/skill/ingest.md Step 2 (no H1, no `---`, leave `tags`/`related` empty at ingest, canonical sections) and Step 5 (paragraph-count invariant before writing).

---

## 2026-04-27 | cleanup | topics directory | removed 6 same-product stubs

- Archived: wiki/topics/{ai-agent-orchestration,embedded-html-apps,web-terminal,scheduled-jobs,full-text-search,wysiwyg-editor}.md → wiki/.archive/wiki/topics/
- Updated: wiki/index.md (Topics section reverted to placeholder), wiki/sources/runcabinet.com.md and wiki/sources/hilash-cabinet.md (added `product: cabinet` frontmatter)
- Reason: stubs were generated by lint Auto-fix 2 from two sources that describe the same product (Cabinet's marketing site + Cabinet's own GitHub repo). Skill updated upstream — see pin-llm-wiki/skill/lint.md and pin-llm-wiki/skill/ingest.md: Check #4 now counts distinct products via the `product:` frontmatter field, threshold raised to 3, and topic creation defaults to report-only.

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
