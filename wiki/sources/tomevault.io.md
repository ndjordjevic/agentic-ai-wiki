---
type: source
source_url: https://tomevault.io/
tags:
  - instruction-file-index
  - claude-md
  - agents-md
  - skill-md
  - cross-platform-conversion
  - security-scanning
  - tome-bundles
  - mcp-server
related:
  - skills.sh
product: tomevault
detail_level: standard
created: 2026-06-19
updated: 2026-06-19
---

TomeVault is a cross-platform index, converter, and trust layer for AI instruction files — indexing 117,590+ CLAUDE.md, AGENTS.md, SKILL.md, GEMINI.md, .cursorrules, Windsurf rules, and copilot-instructions.md files from public GitHub repos and converting them on-demand across six AI coding platforms. Its core insight: developers write one primary instruction file and TomeVault auto-translates it to every format variant, re-grading on each commit. It also introduces "Tomes" — installable packages that bundle a project config with related SKILL.md files — and applies deterministic security scoring (74 rules, 10 AST categories) to every file before indexing.

_All claims below are sourced from ../../raw/web/tomevault.io.md unless otherwise noted._

## What it does

TomeVault serves as a single source of truth for AI instruction files across Claude Code, Codex, GitHub Copilot, Cursor, Gemini CLI, and Windsurf. A developer maintains one canonical instruction file; on each repo commit TomeVault re-translates it into all six platform formats (CLAUDE.md, AGENTS.md, .cursorrules, GEMINI.md, copilot-instructions.md, .windsurfrules) and re-grades every variant. Beyond conversion it acts as a searchable public index: 48,172+ configs converted into 289,032+ format variants, 35,773+ developers indexed, and 1,208+ Tomes available for one-command install. Agents and MCP clients can reach the index directly via a remote MCP server at `mcp.tomevault.io`.

## Key features

- **Cross-platform conversion** — one instruction file in → six platform formats out. Supports Claude Code, Codex (AGENTS.md), GitHub Copilot, Cursor, Gemini CLI, and Windsurf; also works with Continue, Aider, and Zed.
- **Tomes** — portable bundles: a project config file (CLAUDE.md or AGENTS.md) plus related SKILL.md files from the same repo, packaged with provenance. Installable with a single CLI command.
- **Security scanning** — deterministic evaluation using 74 rules across 10 AST categories: hardcoded secrets, command execution risks, prompt injection, data exfiltration, unsafe file access, and obfuscation patterns. Files failing the gate are blocked from indexing. Mapped to the draft OWASP Agentic Skills Top 10.
- **Quality grading** — Bronze/Silver/Gold rubric based on clarity and loadability. Studio previews the clarity dimension live; composed tier computed at ingest.
- **Provenance tracking** — authorship classification and origin/ownership trace on every indexed file. "TomeVault Certified" requires quality + security + verified publisher identity.
- **Scan tool** — upload files to check loadability, clarity, and safety locally (no external server upload required).
- **MCP server** — `mcp.tomevault.io` (Streamable HTTP, no setup). Tools: `search_tomes`, `get_tome`, `get_provenance`, `scan_content`, `convert_content`, plus token-scoped vault reads. Anonymous public access.
- **CLI (`npx tomevault`)** — no install required. Commands: `search`, `install`, `init`, `convert`, `mcp` (local stdio MCP proxy).
- **GitHub App** — automatic re-sync and re-translation on each repo commit.

## Architecture and concepts

**Two instruction file types.** Config files (CLAUDE.md, AGENTS.md, .cursorrules, etc.) are always-on, project-wide; they tell an AI tool the constant truths about a project. Skill files (SKILL.md) are on-demand and task-specific — they load only when the relevant task arises (progressive disclosure pattern). Tomes bundle both.

**Conversion engine.** Each platform uses an incompatible format; TomeVault converts between all six. The conversion is style-aware, not just a format rewrite. Every output variant retains attribution to the original source repo.

**Standards layer (v1.2.0, updated 2026-06-12).** Six versioned, hand-curated standards govern the platform:
1. **Scope** — indexing/scanning only; TomeVault never executes code or hosts an LLM.
2. **Security Scanning** — 74 rules, pass/fail gate pre-index, OWASP Agentic Skills Top 10 mapping.
3. **Quality Scoring** — Bronze/Silver/Gold, weakest-link scoring.
4. **Provenance** — authorship classification, origin trace.
5. **Attestation** — signed token packaging security + quality + provenance findings.
6. **Ratification** — public RFC process (72h comment window for changes, 7 days for breaking changes). MIT-licensed rule catalog, public transparency logs.

**Key finding from 2026 annual report:** 78.7% of repositories using AI coding tools configure only one of them; 27.1% of instruction files exceed 50 instructions (creating recall gaps for buried rules).

## Main APIs

- **Remote MCP:** `https://mcp.tomevault.io` — tools: `search_tomes`, `get_tome`, `get_provenance`, `scan_content`, `convert_content`
- **CLI:** `npx tomevault search "<query>"`, `npx tomevault install <owner>/<repo>`, `npx tomevault init`, `npx tomevault convert`, `npx tomevault mcp`
- **Web UI endpoints:** `/tome/{owner}/{repo}`, `/profile/{owner}`, `/category/{category}`, `/tool/{tool}`, `/scan`, `/convert`, `/standards`, `/wtf-is`
- **Learn hub:** `/learn` (100+ articles), `/learn/compatibility`, `/learn/guides`, `/learn/trends`
- **Removal:** `/remove/{owner}` — self-serve content removal

## When to use

TomeVault is the right tool when: (1) you use multiple AI coding tools and don't want to maintain per-tool instruction files manually; (2) you're publishing a skills package and want one-command discoverability for others; (3) you need a security audit of instruction files before deploying them in an agent workflow; (4) you're an agent or MCP client that needs to search for, verify, or install instruction files programmatically. It is **not** an execution environment — it propagates and governs instruction files, it does not run them.

## Ecosystem

- **[[skills.sh]]** — complementary distribution layer for SKILL.md files; skills.sh handles install/discovery with the `npx skills` CLI while TomeVault handles index, conversion, and trust scoring across six platforms. The two are interoperable: a Tome from TomeVault can contain SKILL.md files that the skills.sh CLI can install.
- **AGENTS.md open standard** — TomeVault treats AGENTS.md as the primary cross-platform format and provides the `/wtf-is/agents-md` explainer; the platform actively promotes AGENTS.md adoption over platform-specific equivalents.
- **OWASP Agentic Skills Top 10** — TomeVault's security scanner is mapped against this draft standard; the security catalog lives at `/security` with live rule counts.
- **`.well-known/agent-skills`** — TomeVault maintains a publisher allowlist for this emerging distribution protocol at `/standards/publishers`.
