# davila7/claude-code-templates

## Metadata
- Stars: 29431
- Primary language: Python
- Default branch: main
- Latest release: v1.28.3 (2025-11-15)
- License: MIT License
- Homepage: https://aitmpl.com
- Fetched: 2026-07-14
- Final URL: https://github.com/davila7/claude-code-templates

## Description
CLI tool for configuring and monitoring Claude Code

## README
[![npm version](https://img.shields.io/npm/v/claude-code-templates.svg)](https://www.npmjs.com/package/claude-code-templates)
[![npm downloads](https://img.shields.io/npm/dt/claude-code-templates.svg)](https://www.npmjs.com/package/claude-code-templates)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

<p align="center">
  <a href="https://trendshift.io/repositories/15113" target="_blank">
    <img src="https://trendshift.io/api/badge/repositories/15113" alt="davila7%2Fclaude-code-templates | Trendshift" style="width: 200px; height: 40px;" width="125" height="40"/>
  </a>
</p>

---

# Claude Code Templates ([aitmpl.com](https://aitmpl.com))

**Ready-to-use configurations for Anthropic's Claude Code.** A comprehensive collection of AI agents, custom commands, settings, hooks, external integrations (MCPs), and project templates to enhance your development workflow.

## Browse & Install Components and Templates

**[Browse All Templates](https://aitmpl.com)** - Interactive web interface to explore and install 100+ agents, commands, settings, hooks, and MCPs.

## 🚀 Quick Installation

```bash
# Install a complete development stack
npx claude-code-templates@latest --agent development-team/frontend-developer --command testing/generate-tests --mcp development/github-integration --yes

# Browse and install interactively
npx claude-code-templates@latest

# Install specific components
npx claude-code-templates@latest --agent development-tools/code-reviewer --yes
npx claude-code-templates@latest --command performance/optimize-bundle --yes
npx claude-code-templates@latest --setting performance/mcp-timeouts --yes
npx claude-code-templates@latest --hook git/pre-commit-validation --yes
npx claude-code-templates@latest --mcp database/postgresql-integration --yes
```

## What You Get

| Component | Description | Examples |
|-----------|-------------|----------|
| **🤖 Agents** | AI specialists for specific domains | Security auditor, React performance optimizer, database architect |
| **⚡ Commands** | Custom slash commands | `/generate-tests`, `/optimize-bundle`, `/check-security` |
| **🔌 MCPs** | External service integrations | GitHub, PostgreSQL, Stripe, AWS, OpenAI |
| **⚙️ Settings** | Claude Code configurations | Timeouts, memory settings, output styles |
| **🪝 Hooks** | Automation triggers | Pre-commit validation, post-completion actions |
| **🎨 Skills** | Reusable capabilities with progressive disclosure | PDF processing, Excel automation, custom workflows |

## 🛠️ Additional Tools

Beyond the template catalog, Claude Code Templates includes powerful development tools:

### 📊 Claude Code Analytics
Monitor your AI-powered development sessions in real-time with live state detection and performance metrics.

```bash
npx claude-code-templates@latest --analytics
```

### 💬 Conversation Monitor
Mobile-optimized interface to view Claude responses in real-time with secure remote access.

```bash
# Local access
npx claude-code-templates@latest --chats

# Secure remote access via Cloudflare Tunnel
npx claude-code-templates@latest --chats --tunnel
```

### 🔍 Health Check
Comprehensive diagnostics to ensure your Claude Code installation is optimized.

```bash
npx claude-code-templates@latest --health-check
```

### 🔌 Plugin Dashboard
View marketplaces, installed plugins, and manage permissions from a unified interface.

```bash
npx claude-code-templates@latest --plugins
```

## 📖 Documentation

**[📚 docs.aitmpl.com](https://docs.aitmpl.com/)** - Complete guides, examples, and API reference for all components and tools.

## Attribution

This collection includes components from multiple sources, each retaining its original license and attribution:

**Scientific Skills:** K-Dense-AI/claude-scientific-skills (MIT, 139 skills)

**Official Anthropic:** anthropics/skills (21 skills), anthropics/claude-code (10 skills)

**Community Skills & Agents:** obra/superpowers (MIT, 14 skills), alirezarezvani/claude-skills (MIT, 36 skills), wshobson/agents (MIT, 48 agents), NerdyChefsAI Skills

**Commands & Tools:** awesome-claude-code (CC0), awesome-claude-skills (Apache 2.0), move-code-quality-skill (MIT), cocoindex-claude (Apache 2.0)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Links

- **🌐 Browse Templates**: [aitmpl.com](https://aitmpl.com)
- **📚 Documentation**: [docs.aitmpl.com](https://docs.aitmpl.com)
- **💬 Community**: [GitHub Discussions](https://github.com/davila7/claude-code-templates/discussions)
- **🐛 Issues**: [GitHub Issues](https://github.com/davila7/claude-code-templates/issues)

## Docs

### CLAUDE.md (repo root — contributor/agent instructions, excerpted)

**Project Overview:** Node.js CLI tool for managing Claude Code components (agents, commands, MCPs, hooks, settings) with a static website for browsing and installing components. The dashboard and its API routes are deployed on Cloudflare Pages, with supporting cron and monitoring tasks running as Cloudflare Workers.

**Essential Commands:**
```bash
npm install                    # Install dependencies
npm test                       # Run tests
npm version patch|minor|major  # Bump version
npm publish                    # Publish to npm
python scripts/generate_components_json.py  # Update docs/components.json
cd dashboard && npm run build  # Build dashboard (Astro on Cloudflare Pages)
npm run deploy                 # Deploy www + app.aitmpl.com via wrangler
```
Deploys to production happen automatically via GitHub Actions on push to `main` (changes in `dashboard/**`). Manual deploy uses `wrangler pages deploy`, not Vercel.

**Component System — types tracked in the catalog:**
- Agents (600+) — AI specialists for development tasks
- Commands (200+) — custom slash commands for workflows
- MCPs (55+) — external service integrations
- Settings (60+) — Claude Code configuration files
- Hooks (39+) — automation triggers
- Loops (18+) — autonomous agentic workflows (goal + interval + stop condition) that reference other components
- Templates (14+) — complete project configurations

**Component development workflow:** components live at `cli-tool/components/{type}/{category}/{name}.md`, kebab-case named. All new/changed components must be validated with the `component-reviewer` subagent (checks YAML frontmatter, naming, no hardcoded secrets, relative paths, supporting files present, description clarity, category placement, security), then the catalog is regenerated via `python scripts/generate_components_json.py`.

**Skill security scanning (SkillSpector):** skills under `cli-tool/components/skills/**` are statically scanned by SkillSpector (NVIDIA, Apache-2.0; 64 vulnerability patterns — prompt injection, data exfiltration, supply chain, dangerous code/AST, taint tracking, YARA) in `--no-llm` static-only mode via `scripts/skillspector_scan.py`. A PR workflow scans only changed skills and blocks merges on HIGH/CRITICAL risk (score > 50); a weekly/manual workflow scans all skills without blocking. Risk bands: 0-20 LOW, 21-50 MEDIUM, 51-80 HIGH, 81-100 CRITICAL.

**Publishing workflow:** bump `package.json` version above the current npm registry version → `npm test` → commit/push → `npm publish` (granular access token with "Bypass 2FA", removed from config after use) → tag `vX.Y.Z` → dashboard deploys automatically via GitHub Actions on push to `main`.

**API architecture:** dashboard API routes are Astro routes under `dashboard/src/pages/api/`. Key endpoints: `/api/track-download-supabase` (tracks every CLI install, Supabase-backed), `/api/discord/interactions` (Discord bot: /search, /info, /install, /popular), `/api/claude-code-check` (polls Claude Code releases every 30 min via a Cloudflare Worker cron; stores to Neon). Shared libs: `dashboard/src/lib/api/cors.ts`, `neon.ts` (Neon client), `auth.ts` (Clerk JWT), `changelog-parser.ts`.

**Cloudflare Workers:** `cloudflare-workers/` holds independent Worker projects (e.g. `crons`, replacing former Vercel cron jobs) that call dashboard API endpoints on a schedule using a shared `TRIGGER_SECRET`.

### cli-tool/README.md (npm package overview, excerpted)

**CLI tool for configuring and monitoring Claude Code** — quick setup for any project with framework-specific commands and a real-time monitoring dashboard.

```bash
npx claude-code-templates@latest                 # Interactive setup
npx claude-code-templates@latest --analytics      # Real-time analytics dashboard
npx claude-code-templates@latest --health-check   # System health check
```

Core features: smart project setup (auto-detect + framework-specific config), real-time analytics (live session state detection, performance metrics), health check (system validation with recommendations), individually installable agents/commands/MCPs, and "Global Agents" (agents runnable from anywhere via the Claude Code SDK, e.g. `npx claude-code-templates@latest --create-agent customer-support`).

Supported technologies: JavaScript/TypeScript (React, Vue, Angular, Node.js), Python (Django, Flask, FastAPI), Common/universal configs — all "Ready"; Go and Rust listed "Coming Soon".

## Top-level structure

- `.claude-plugin/`, `.claude/` — plugin manifest / Claude Code project config for this repo itself
- `.github/` — CI workflows, including the SkillSpector security-scan actions
- `CLAUDE.md` / `CLAUDE_BACKUP.md` — agent instructions for contributors (see Docs above)
- `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md`, `LICENSE` — project governance
- `api/` — API-related code (top-level, distinct from `dashboard/src/pages/api/`)
- `cli-rust/` — Rust implementation/port of CLI functionality
- `cli-tool/` — the main Node.js CLI package (`components/`, `src/`, `bin/`, `templates/`, `analytics-ui/`, `docs_to_claude/`, tests) — published to npm as `claude-code-templates`
- `cloudflare-workers/` — independent Worker projects (e.g. `crons`) supporting the dashboard
- `dashboard/` — Astro app deployed to Cloudflare Pages (`app.aitmpl.com`), includes API routes
- `database/` — database schema/migration assets (Supabase/Neon)
- `docs/` — static website source for aitmpl.com component browser (GitHub Pages/Jekyll-adjacent: `index.html`, `components.json`, `guides/`, `blog/`, `claude-prs/`, `featured/`)
- `scripts/` — maintenance scripts (`generate_components_json.py`, `skillspector_scan.py`)
- `package.json`, `vercel.json` — root package/deploy config
