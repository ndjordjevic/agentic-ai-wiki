# santifer/career-ops

## Metadata
- Stars: 52587
- Primary language: JavaScript
- Default branch: main
- Latest release: v1.10.0 (2026-06-11)
- License: MIT License
- Homepage: https://career-ops.org
- Fetched: 2026-06-11
- Final URL: https://github.com/santifer/career-ops

## Description
AI-powered job search system built on Claude Code. 14 skill modes, Go dashboard, PDF generation, batch processing.

## README
# Career-Ops

Career-Ops (career-ops.org, also known as **careerops**) turns any AI coding CLI into a full job search command center. Instead of manually tracking applications in a spreadsheet, you get an AI-powered pipeline that:

- **Evaluates offers** with a structured A-F scoring system (10 weighted dimensions)
- **Generates tailored PDFs** — ATS-optimized CVs customized per job description
- **Scans portals** automatically (Greenhouse, Ashby, Lever, company pages)
- **Processes in batch** — evaluate 10+ offers in parallel with sub-agents
- **Tracks everything** in a single source of truth with integrity checks

> **Important: This is NOT a spray-and-pray tool.** Career-ops is a filter — it helps you find the few offers worth your time out of hundreds. The system strongly recommends against applying to anything scoring below 4.0/5. Your time is valuable, and so is the recruiter's. Always review before submitting.

Career-ops is agentic: Claude Code navigates career pages with Playwright, evaluates fit by reasoning about your CV vs the job description (not keyword matching), and adapts your resume per listing.

Built by someone who used it to evaluate 740+ job offers, generate 100+ tailored CVs, and land a Head of Applied AI role.

### Features

| Feature | Description |
|---|---|
| **Auto-Pipeline** | Paste a URL, get a full evaluation + PDF + tracker entry |
| **6-Block Evaluation** | Role summary, CV match, level strategy, comp research, personalization, interview prep (STAR+R) — plus a Block G posting-legitimacy check that flags scams and ghost jobs |
| **Interview Story Bank** | Accumulates STAR+Reflection stories across evaluations — 5-10 master stories that answer any behavioral question |
| **Negotiation Scripts** | Salary negotiation frameworks, geographic discount pushback, competing offer leverage |
| **ATS PDF Generation** | Keyword-injected CVs with Space Grotesk + DM Sans design |
| **Cover Letter Generator** | Research-backed cover letters with keyword mirroring, four interactive angle prompts, draft-in-chat approval gate, and A4 PDF via ReportLab |
| **Portal Scanner** | 45+ companies pre-configured (Anthropic, OpenAI, ElevenLabs, Retool, n8n...) + custom queries across Ashby, Greenhouse, Lever, Wellfound |
| **Batch Processing** | Parallel evaluation with `claude -p` workers |
| **Dashboard TUI** | Terminal UI to browse, filter, and sort your pipeline |
| **Human-in-the-Loop** | AI evaluates and recommends, you decide and act. The system never submits an application |
| **Pipeline Integrity** | Automated merge, dedup, status normalization, health checks |

### Quick Start

```bash
npx @santifer/career-ops init
cd career-ops
claude   # or gemini / codex / qwen / opencode
```

On first launch, career-ops walks you through setup — your CV, profile, and target roles — just by chatting.

### Usage

```
/career-ops                → Show all available commands
/career-ops {paste a JD}   → Full auto-pipeline (evaluate + PDF + tracker)
/career-ops scan           → Scan portals for new offers
/career-ops pdf            → Generate ATS-optimized CV
/career-ops cover          → Cover letter generator
/career-ops batch          → Batch evaluate multiple offers
/career-ops tracker        → View application status
/career-ops apply          → Fill application forms with AI
/career-ops pipeline       → Process pending URLs
/career-ops contacto       → LinkedIn outreach message
/career-ops deep           → Deep company research
/career-ops training       → Evaluate a course/cert
/career-ops project        → Evaluate a portfolio project
```

### Pre-configured Portals (45+ companies)

**AI Labs:** Anthropic, OpenAI, Mistral, Cohere, LangChain, Pinecone
**Voice AI:** ElevenLabs, PolyAI, Parloa, Hume AI, Deepgram, Vapi, Bland AI
**AI Platforms:** Retool, Airtable, Vercel, Temporal, Glean, Arize AI
**Automation:** n8n, Zapier, Make.com
**Job boards:** Ashby, Greenhouse, Lever, Wellfound, Workable, RemoteFront

### Dashboard TUI

```bash
cd dashboard
go build -o career-dashboard .
./career-dashboard --path ..
```

Features: 6 filter tabs, 4 sort modes, grouped/flat view, lazy-loaded previews, inline status changes.

## Docs

### ARCHITECTURE.md (summary)

The system uses AI coding CLI agents (Claude Code, Gemini CLI, Codex, etc.) reading `AGENTS.md` + `modes/*.md` as the primary orchestrator. Three main pipelines:

1. **Single Eval (auto-pipe):** User pastes JD → archetype detection → 6-block A-F evaluation → report.md + PDF + tracker TSV
2. **Portal Scan (scan.md):** Zero-token ATS API calls (Greenhouse/Ashby/Lever) → pipeline.md inbox → optional `--verify` Playwright liveness check
3. **Batch Process (batch-runner.sh):** N headless CLI workers via `claude -p` → parallel evaluation → merge into applications.md

Data flow: `cv.md` + `article-digest.md` + `config/profile.yml` + `portals.yml` → evaluation context.

File naming: Reports `{###}-{company}-{YYYY-MM-DD}.md`, PDFs `cv-candidate-{company}-{YYYY-MM-DD}.pdf`.

Pipeline integrity scripts: `merge-tracker.mjs`, `verify-pipeline.mjs`, `dedup-tracker.mjs`, `normalize-statuses.mjs`, `cv-sync-check.mjs`.

### AGENTS.md (key extracts)

**Data Contract (two layers):**
- **User Layer** (never auto-updated): `cv.md`, `config/profile.yml`, `modes/_profile.md`, `article-digest.md`, `portals.yml`, `data/*`, `reports/*`, `output/*`, `interview-prep/*`
- **System Layer** (auto-updatable): `modes/_shared.md`, all other modes, `AGENTS.md`, `*.mjs` scripts, `dashboard/*`, `templates/*`, `batch/*`

**THE RULE:** All user customizations go to `modes/_profile.md` or `config/profile.yml`. Never edit `modes/_shared.md` for user-specific content.

Multi-CLI support: Claude Code, Gemini CLI, Codex, OpenCode, Qwen, GitHub Copilot, Kimi — all CLIs read `AGENTS.md`. CLI-specific wrappers: `CLAUDE.md`, `GEMINI.md`, `.claude-plugin/`, `.agents/`, `.qwen/`.

Auto-update system: session start runs `node update-system.mjs check` silently; only announces when an update is available.

## Top-level structure

```
career-ops/
├── AGENTS.md               — canonical agent instructions (all CLIs load this)
├── CLAUDE.md               — Claude Code wrapper (imports AGENTS.md)
├── GEMINI.md               — Gemini CLI wrapper
├── .claude/                — Claude Code settings + hooks
├── .claude-plugin/         — Claude Code plugin manifest
├── .agents/                — agent config for other CLIs
├── .qwen/                  — Qwen CLI config
├── cv.md                   — user's CV (created during onboarding)
├── article-digest.md       — proof points (optional)
├── config/
│   └── profile.example.yml — user profile template
├── modes/                  — 15+ skill mode files (_shared.md, oferta.md, pdf.md, cover.md, scan.md, batch.md, apply.md, contacto.md, deep.md, training.md, project.md, pipeline.md, tracker.md, interview.md, interview-prep.md, update.md, patterns.md, followup.md, auto-pipeline.md, ofertas.md, latex.md, + localized variants)
├── templates/
│   ├── cv-template.html    — ATS-optimized CV HTML template
│   ├── cv-template.tex     — LaTeX/Overleaf template
│   ├── portals.example.yml — scanner config template
│   └── states.yml          — canonical status values
├── batch/
│   ├── batch-prompt.md     — self-contained headless worker prompt
│   └── batch-runner.sh     — orchestrator script
├── dashboard/              — Go TUI (Bubble Tea + Lipgloss, Catppuccin theme)
├── data/                   — tracking data (gitignored): applications.md, pipeline.md, scan-history.tsv
├── reports/                — evaluation reports (gitignored)
├── output/                 — generated PDFs (gitignored)
├── fonts/                  — Space Grotesk + DM Sans
├── docs/                   — SETUP.md, ARCHITECTURE.md, CUSTOMIZATION.md, SCRIPTS.md
├── examples/               — sample CV, report, proof points, dual-track examples
├── providers/              — provider-specific configs
├── interview-prep/         — story-bank.md + per-company interview intel
├── jds/                    — job description inbox
├── writing-samples/        — cover letter writing samples
├── scaffolder/             — project scaffolding tools
├── scan.mjs                — zero-token portal scanner (Greenhouse/Ashby/Lever API)
├── generate-pdf.mjs        — Playwright HTML→PDF pipeline
├── generate-latex.mjs      — LaTeX CV validator + pdflatex compiler
├── generate-cover-letter.mjs — cover letter generator
├── merge-tracker.mjs       — merge batch TSV additions into applications.md
├── verify-pipeline.mjs     — pipeline health check
├── dedup-tracker.mjs       — deduplication by company+role
├── normalize-statuses.mjs  — status alias normalization
├── doctor.mjs              — onboarding prerequisite checker
├── update-system.mjs       — self-update CLI
├── analyze-patterns.mjs    — application pattern analyzer (JSON output)
├── followup-cadence.mjs    — follow-up cadence calculator
├── Dockerfile / docker-compose.yml — container support
└── package.json            — Node.js dependencies
```
