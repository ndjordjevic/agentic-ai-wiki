# tomevault.io

## Fetch log
- Inbox URL: https://tomevault.io/
- Final URL: https://tomevault.io/
- Fetched: 2026-06-19
- Pages: 6
- Mode: standard

## llms.txt — https://tomevault.io/llms.txt
# TomeVault
> Cross-platform index for AI instruction files. Better inputs, better outputs.

TomeVault indexes AI instruction files (CLAUDE.md, AGENTS.md, SKILL.md, GEMINI.md, .cursorrules, Windsurf rules, copilot-instructions.md) from public GitHub repos. It converts config files across 6 major AI coding platforms and bundles configs with related skills into Tomes — installable cross-platform packages.

## Key facts
- 117,590+ indexed instruction files
- 48,172+ configs converted to 289,032+ format variants across 6 platforms
- 1,208+ Tomes (config + skills bundles)
- 35,773+ developers indexed
- 6 platforms: Claude Code, Codex (AGENTS.md), GitHub Copilot, Cursor, Gemini CLI, Windsurf

## What is a Tome?
A Tome bundles a project config file (e.g. CLAUDE.md) with related skill files (SKILL.md) from the same repo into one cross-platform package. The config tells an AI tool how your project works. The skills give it specific capabilities. Together they are more useful than either alone.

## What is a config file?
An always-on, project-wide instruction file that tells an AI coding tool how to work with a project. Different platforms use different formats (CLAUDE.md, GEMINI.md, .cursorrules, AGENTS.md, copilot-instructions.md, Windsurf rules). TomeVault converts between all of them so project instructions work everywhere.

## What is a skill file?
An on-demand, task-specific instruction file (SKILL.md) that gives an AI tool a particular capability. SKILL.md follows the Agent Skills open standard and works natively on all 6 platforms without conversion.

## Pages

### Search and discovery
- / — Search and browse all instruction files with filters for type, category, author, and platform

### Tome and config detail pages
- /tome/{owner}/{repo} — Individual config or Tome with full content preview, all format variants, platform compatibility, and quality grade

### Creator profiles
- /profile/{owner} — Public profile showing all of a developer's configs, skills, and Tomes indexed by TomeVault

### Category browsing
- /category/{category} — Browse instruction files by topic (e.g. react, python, testing, docker)

### Platform browsing
- /tool/{tool} — Browse by AI platform (claude-code, codex, copilot, cursor, gemini-cli, windsurf)

### Learning hub
- /learn — Data-driven guides on AI instruction files, grouped by pillar
- /learn/platforms — Platform guides: how each AI tool's instruction format works
- /learn/categories — Category index across the catalog
- /learn/guides — Long-form how-to guides
- /learn/bundles — Curated Tome bundles by category
- /learn/trends — Ecosystem trends and growth signals
- /learn/gaps — Coverage gaps the index is filling
- /learn/compatibility — Cross-platform compatibility matrix
- /learn/relay-app — The TomeVault GitHub app overview

### Beginner explainers (WTF is...)
- /wtf-is — Plain-English entry point for new readers
- /wtf-is/skill — What a Skill is and when to use one
- /wtf-is/tome — What a Tome bundles and why
- /wtf-is/agents-md — The AGENTS.md format
- /wtf-is/agents-md-vs-skill-md — AGENTS.md compared to SKILL.md
- /wtf-is/claude-md — The CLAUDE.md format
- /wtf-is/cursor-rules — The .cursorrules format
- /wtf-is/cursor-rules-not-working — Common reasons .cursorrules fails to apply
- /wtf-is/skill-vs-mcp — When to use a Skill vs an MCP server
- /wtf-is/skill-vs-tome — Skill vs Tome decision guide
- /wtf-is/skill-vs-subagent — Skill vs subagent decision guide
- /wtf-is/progressive-disclosure — The progressive-disclosure pattern in instruction files
- /wtf-is/instruction-file — Umbrella definition for instruction files
- /wtf-is/well-known — The .well-known/agent-skills publisher protocol
- /wtf-is/cross-format-conventions — Conventions shared across formats

### Per-role landing pages
- /for — Role hub
- /for/product-managers
- /for/backend-engineers
- /for/frontend-engineers
- /for/devops
- /for/data-scientists
- /for/ml-engineers

### Per-tool upgrade paths
- /upgrade — Hub for migrating instruction files between tools
- /upgrade/claude-code
- /upgrade/cursor
- /upgrade/windsurf
- /upgrade/copilot
- /upgrade/gemini
- /upgrade/aider

### Facet-led discovery
- /solutions — Browse Tomes by role, stack, or use case
- /solutions/by-role — Role-shaped facets
- /solutions/by-stack — Stack-shaped facets
- /solutions/by-use-case — Use-case-shaped facets

### Insights and reports
- /insights/cross-platform — Programmatic cross-platform feature and coverage comparison

### Self-service
- /convert — Submit a GitHub repo for conversion to all platforms, or build a Tome
- /feedback — Share what's working, what's broken, and what's missing

### Standards (trust + quality cornerstone)
- /standards — Versioned, hand-curated reference for how TomeVault scans, scores, classifies, and governs instruction files
- /standards/scope — What TomeVault does, what it explicitly never does
- /standards/security-scanning — Rules, severities, the pre-index gate, and the mapping to the draft OWASP Agentic Skills Top 10
- /standards/quality-scoring — Deterministic Bronze/Silver/Gold rubric (clarity + loadability, weakest-link) used on /scan and behind every Tome card; Studio previews the clarity dimension live, with the composed tier computed at ingest
- /standards/provenance — Authorship classification standard and the origin/ownership trace every indexed file carries
- /standards/state-reports/2026 — State of AI instructions 2026: annual report on governance, marketplaces, scanners, and corpus data
- /standards/ratification — Public RFC + 72h comment window + chair ratification process
- /standards/publishers — .well-known/agent-skills publisher protocol: publishers TomeVault has allowlisted, with live adoption numbers
- /security — Live catalog of all 74 patterns the security scanner runs against, mapped to the draft OWASP Agentic Skills Top 10
- /transparency — Live aggregates, incident log, rule-set version in force

### Other pages
- /faq — How TomeVault works, answered for skeptical developers
- /claim/{owner} — Claim page for developers to manage their distributed content
- /claim — Search for your GitHub username to find your content

## CLI
Install via npx (no install required):
- npx tomevault search "query" — Search the index
- npx tomevault install owner/repo — Install skills and configs locally
- npx tomevault init — Scan your repo, pull missing platform formats
- npx tomevault convert — Submit your repo for conversion
- npx tomevault mcp — Run a local stdio MCP server that proxies to TomeVault, for MCP clients that prefer stdio

## MCP (Model Context Protocol)
Agents can connect to TomeVault directly over MCP:
- https://mcp.tomevault.io — remote MCP server (Streamable HTTP, no setup). Tools: search_tomes, get_tome (provenance verdict attached), get_provenance, scan_content, convert_content, plus token-scoped vault reads. Anonymous public access; full reference at /docs/mcp.

## Content licensing
All indexed content originates from public GitHub repositories. Converted format variants include attribution back to the original repo. Developers can remove their content at any time via /remove/{owner}.

## Landing page — https://tomevault.io/

TomeVault is "one source of truth for your AI instructions," enabling users to maintain a single primary file that automatically translates across multiple AI tool formats.

### Multi-Tool Translation
The platform supports Claude, Cursor, GitHub Copilot, Gemini, Windsurf, Codex, Continue, Aider, and Zed, converting instructions into each tool's preferred format and style.

### Real-Time Synchronization
Upon each repository commit, TomeVault re-translates and re-grades all instruction file formats, keeping versions current across CLAUDE.md, AGENTS.md, .cursorrules, GEMINI.md, copilot-instructions.md, and .windsurfrules.

### Security Grading
Files undergo deterministic evaluation using 74 rules across 10 AST categories, checking for hardcoded secrets, command execution risks, prompt injection, data exfiltration, unsafe file access, and obfiltration patterns.

### Scan Tool
Users can upload files to check loadability, clarity, and safety without uploading content to external servers.

### Pricing
14-day Pro trial (no card required). Private Vault: £9/month. Team Vault: £19 per seat/month. Free plan available indefinitely.

### Navigation
Main sections: Home, Vault, Scan, Search, Docs, Standards, and "Wtf is…" educational content.

## Learn — https://tomevault.io/learn

TomeVault's learning hub: "AI skill & instruction files — by the data." Data-driven guides covering 100+ articles across 6 platforms.

### Content pillars
- **Compatibility Matrix** — Canonical reference for which file format works with which AI tool, where each one goes, and what TomeVault converts between
- **Platform Guides** (2 articles) — How instruction formats function across different AI tools
- **Category Guides** (23 articles) — Landscape analysis and top-rated configurations by topic
- **Writing Guides** (24 articles) — Quality differentiation in instruction file creation
- **Gap Analysis** (24 articles) — Missing configurations and common file failures
- **Best Bundles** (24 articles) — Top-rated Tomes (config + skills packages) installable with one command
- **Weekly Trends** (3 articles) — Ecosystem shifts within the instruction file landscape

## WTF Is — https://tomevault.io/wtf-is

Plain-English explainers for AI instruction file concepts. Covers 14 topics:

- **Skill** — A Markdown file that tells an AI how to do one specific thing; loads only when relevant tasks arise
- **Tome** — A portable bundle: an AGENTS.md (or CLAUDE.md) plus one or more Skills, packaged with provenance
- **AGENTS.md** — A single Markdown file in the repo root that tells almost every AI coding tool what's true about this project; supports Codex, Copilot, Gemini, Cursor, and Claude Code
- **CLAUDE.md** — Claude-specific predecessor to the cross-platform AGENTS.md standard
- **Skills vs Tomes** — Skills are single-purpose files; Tomes are packaged bundles with config + multiple skills
- **AGENTS.md loads continuously** (project-wide truths); SKILL.md activates only when task descriptions match (progressive disclosure)
- **Skill vs MCP** — When to use a Skill file vs an MCP server
- **Skill vs subagent** — Skill vs subagent decision guide
- **Progressive disclosure** — The underlying pattern: load only necessary context when needed
- **.well-known/agent-skills** — Emerging standard for distributing Skills across platforms

## Standards — https://tomevault.io/standards

TomeVault calls itself "the trust layer for AI instruction files." Standards are versioned (v1.2.0, published 2026-05-06, updated 2026-06-12) and governed by a public ratification process.

### Six core standards
1. **Scope** — Boundaries between indexing/scanning and specification-setting or execution
2. **Security Scanning** — What gets scanned, pass/fail gates, mapping to OWASP Agentic Skills Top 10; 74 rules across 10 AST categories
3. **Quality Scoring** — Bronze/Silver/Gold rubric based on clarity and loadability
4. **Provenance** — Authorship classification and file ownership tracing
5. **Attestation** — Packages security, quality, and provenance findings into one signed token
6. **Ratification** — RFC process: 72-hour comment window for standard changes, 7 days for breaking changes

### Key data points from 2026 annual report
- 78.7% of repositories using AI coding tools configure only one of them
- 27.1% of files exceed 50 instructions (recall gaps between buried and prominent rules)

### Governance cycle
RFC submission → 72-hour review → ratification → publication. Public rule catalog (MIT-licensed), transparency logs, and incident tracking maintained.

## FAQ — https://tomevault.io/faq

Core function: converting AI instruction files across six platforms (Claude Code, Codex, Copilot, Cursor, Gemini CLI, Windsurf).

### Problem and solution
"Six major AI coding platforms use six incompatible config formats." TomeVault converts a single instruction file into formats for all platforms simultaneously.

### What TomeVault offers
- File conversion across platforms
- Security scanning (credentials, injection patterns, exfiltration)
- Quality grading (Bronze/Silver/Gold)
- Provenance verification
- Free indexing and distribution

### Trust and safety ("TomeVault Certified")
Three gates: quality rating + clean security scan + verified publisher identity. Files failing security checks are blocked from indexing entirely.

### Practical features
- Studio for creating/publishing files
- CLI tools (init, convert, search, install)
- GitHub App for automatic re-syncing
- Self-serve removal at tomevault.io/remove

### Cost
Entirely free for indexing and distribution (no paid tiers for core features).

TomeVault acts as a "propagation layer" — it does not execute code or host LLM interfaces.
