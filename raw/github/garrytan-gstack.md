# garrytan/gstack

## Metadata
- Stars: 101,913
- Primary language: TypeScript
- Default branch: main
- Latest release: none (version tracked in VERSION file: 1.44.0.0)
- License: MIT License
- Homepage: (none)
- Fetched: 2026-05-25
- Final URL: https://github.com/garrytan/gstack

## Description
Use Garry Tan's exact Claude Code setup: 23 opinionated tools that serve as CEO, Designer, Eng Manager, Release Manager, Doc Engineer, and QA

## README

# gstack

> "I don't think I've typed like a line of code probably since December, basically, which is an extremely large change." — Andrej Karpathy, No Priors podcast, March 2026

When I heard Karpathy say this, I wanted to find out how. How does one person ship like a team of twenty? Peter Steinberger built OpenClaw — 247K GitHub stars — essentially solo with AI agents. The revolution is here. A single builder with the right tooling can move faster than a traditional team.

I'm Garry Tan, President & CEO of Y Combinator. I've worked with thousands of startups — Coinbase, Instacart, Rippling — when they were one or two people in a garage. Before YC, I was one of the first eng/PM/designers at Palantir, cofounded Posterous (sold to Twitter), and built Bookface, YC's internal social network.

**gstack is my answer.** I've been building products for twenty years, and right now I'm shipping more products than I ever have. In the last 60 days: 3 production services, 40+ shipped features, part-time, while running YC full-time. On logical code change — not raw LOC, which AI inflates — my 2026 run rate is **~810× my 2013 pace** (11,417 vs 14 logical lines/day). Year-to-date (through April 18), 2026 has already produced **240× the entire 2013 year**.

**gstack is how I do it.** It turns Claude Code into a virtual engineering team — a CEO who rethinks the product, an eng manager who locks architecture, a designer who catches AI slop, a reviewer who finds production bugs, a QA lead who opens a real browser, a security officer who runs OWASP + STRIDE audits, and a release engineer who ships the PR. Twenty-three specialists and eight power tools, all slash commands, all Markdown, all free, MIT license.

This is my open source software factory. I use it every day. I'm sharing it because these tools should be available to everyone.

**Who this is for:**
- **Founders and CEOs** — especially technical ones who still want to ship
- **First-time Claude Code users** — structured roles instead of a blank prompt
- **Tech leads and staff engineers** — rigorous review, QA, and release automation on every PR

## Quick start

1. Install gstack (30 seconds — see below)
2. Run `/office-hours` — describe what you're building
3. Run `/plan-ceo-review` on any feature idea
4. Run `/review` on any branch with changes
5. Run `/qa` on your staging URL
6. Stop there. You'll know if this is for you.

## Install — 30 seconds

**Requirements:** Claude Code, Git, Bun v1.0+, Node.js (Windows only)

### Step 1: Install on your machine

Open Claude Code and paste this. Claude does the rest.

> Install gstack: run **`git clone --single-branch --depth 1 https://github.com/garrytan/gstack.git ~/.claude/skills/gstack && cd ~/.claude/skills/gstack && ./setup`** then add a "gstack" section to CLAUDE.md that lists the available skills.

### Step 2: Team mode — auto-update for shared repos (recommended)

```bash
(cd ~/.claude/skills/gstack && ./setup --team) && ~/.claude/skills/gstack/bin/gstack-team-init required && git add .claude/ CLAUDE.md && git commit -m "require gstack for AI-assisted work"
```

No vendored files in your repo, no version drift, no manual upgrades. Every Claude Code session starts with a fast auto-update check (throttled to once/hour, network-failure-safe, completely silent).

### OpenClaw

OpenClaw spawns Claude Code sessions via ACP, so every gstack skill just works when Claude Code has gstack installed.

### Native OpenClaw Skills (via ClawHub)

Four methodology skills work directly in your OpenClaw agent, no Claude Code session needed:
- `gstack-openclaw-office-hours`
- `gstack-openclaw-ceo-review`
- `gstack-openclaw-investigate`
- `gstack-openclaw-retro`

### Other AI Agents

gstack works on 10 AI coding agents, not just Claude. Supported agents:

| Agent | Flag |
|-------|------|
| OpenAI Codex CLI | `--host codex` |
| OpenCode | `--host opencode` |
| Cursor | `--host cursor` |
| Factory Droid | `--host factory` |
| Slate | `--host slate` |
| Kiro | `--host kiro` |
| Hermes | `--host hermes` |
| GBrain (mod) | `--host gbrain` |

## The sprint

gstack is a process, not a collection of tools. The skills run in the order a sprint runs:

**Think → Plan → Build → Review → Test → Ship → Reflect**

Each skill feeds into the next. `/office-hours` writes a design doc that `/plan-ceo-review` reads. `/plan-eng-review` writes a test plan that `/qa` picks up. `/review` catches bugs that `/ship` verifies are fixed. Nothing falls through the cracks because every step knows what came before it.

## Skills table

| Skill | Your specialist | What they do |
|-------|----------------|--------------|
| `/office-hours` | **YC Office Hours** | Start here. Six forcing questions that reframe your product before you write code. Pushes back on your framing, challenges premises, generates implementation alternatives. Design doc feeds into every downstream skill. |
| `/plan-ceo-review` | **CEO / Founder** | Rethink the problem. Find the 10-star product hiding inside the request. Four modes: Expansion, Selective Expansion, Hold Scope, Reduction. |
| `/plan-eng-review` | **Eng Manager** | Lock in architecture, data flow, diagrams, edge cases, and tests. Forces hidden assumptions into the open. |
| `/plan-design-review` | **Senior Designer** | Rates each design dimension 0-10, explains what a 10 looks like, then edits the plan to get there. AI Slop detection. |
| `/plan-devex-review` | **Developer Experience Lead** | Interactive DX review: explores developer personas, benchmarks against competitors' TTHW, designs your magical moment. Three modes: DX EXPANSION, DX POLISH, DX TRIAGE. |
| `/design-consultation` | **Design Partner** | Build a complete design system from scratch. Researches the landscape, proposes creative risks, generates realistic product mockups. |
| `/review` | **Staff Engineer** | Find the bugs that pass CI but blow up in production. Auto-fixes the obvious ones. Flags completeness gaps. |
| `/investigate` | **Debugger** | Systematic root-cause debugging. Iron Law: no fixes without investigation. Traces data flow, tests hypotheses, stops after 3 failed fixes. |
| `/design-review` | **Designer Who Codes** | Same audit as /plan-design-review, then fixes what it finds. Atomic commits, before/after screenshots. |
| `/devex-review` | **DX Tester** | Live developer experience audit. Actually tests your onboarding: navigates docs, tries the getting started flow, times TTHW. |
| `/design-shotgun` | **Design Explorer** | "Show me options." Generates 4-6 AI mockup variants, opens a comparison board in your browser, collects your feedback. |
| `/design-html` | **Design Engineer** | Turn a mockup into production HTML. Pretext computed layout: text reflows, heights adjust, layouts are dynamic. 30KB, zero deps. |
| `/qa` | **QA Lead** | Test your app, find bugs, fix them with atomic commits, re-verify. Auto-generates regression tests for every fix. |
| `/qa-only` | **QA Reporter** | Same methodology as /qa but report only. Pure bug report without code changes. |
| `/pair-agent` | **Multi-Agent Coordinator** | Share your browser with any AI agent. Scoped tokens, tab isolation, rate limiting, activity attribution. |
| `/cso` | **Chief Security Officer** | OWASP Top 10 + STRIDE threat model. Zero-noise: 17 false positive exclusions, 8/10+ confidence gate. |
| `/ship` | **Release Engineer** | Sync main, run tests, audit coverage, push, open PR. Bootstraps test frameworks if you don't have one. |
| `/land-and-deploy` | **Release Engineer** | Merge the PR, wait for CI and deploy, verify production health. |
| `/canary` | **SRE** | Post-deploy monitoring loop. Watches for console errors, performance regressions, page failures. |
| `/benchmark` | **Performance Engineer** | Baseline page load times, Core Web Vitals, and resource sizes. |
| `/document-release` | **Technical Writer** | Update all project docs to match what you just shipped. Catches stale READMEs. |
| `/document-generate` | **Documentation Author** | Generate missing docs from scratch using the Diataxis framework (tutorial / how-to / reference / explanation). |
| `/retro` | **Eng Manager** | Weekly retro with per-person breakdowns and shipping streaks. |
| `/browse` | **QA Engineer** | Give the agent eyes. Real Chromium browser, real clicks, ~100ms per command. |
| `/setup-browser-cookies` | **Session Manager** | Import cookies from your real browser (Chrome, Arc, Brave, Edge) into the headless session. |
| `/autoplan` | **Review Pipeline** | One command, fully reviewed plan. Runs CEO → design → eng → DX review automatically. |
| `/codex` | **Second Opinion** | Independent review from OpenAI Codex CLI. Three modes: code review (pass/fail gate), adversarial challenge, and open consultation. |
| `/context-save` | **Save State** | Save working context so any future session can resume. |
| `/context-restore` | **Restore State** | Resume from a saved context, even across Conductor workspace handoffs. |
| `/health` | **Code Quality Dashboard** | Wraps type checker, linter, tests, dead code detection. Computes a weighted 0-10 score. |
| `/benchmark-models` | **Model Benchmark** | Side-by-side cross-model benchmark (Claude vs GPT vs Gemini). |
| `/careful` | **Safety Guardrails** | Warns before destructive commands (rm -rf, DROP TABLE, force-push). |
| `/freeze` | **Edit Lock** | Restrict all file edits to a single directory. Hard block, not just a warning. |
| `/guard` | **Full Safety** | Combines /careful + /freeze in one command. |
| `/unfreeze` | **Unlock** | Remove the /freeze boundary. |
| `/scrape` | **Browser Data Extractor** | Pull data from a web page; first call prototypes, subsequent runs execute in ~200ms. |
| `/skillify` | **Skill Codifier** | Walks back through the conversation, finds the last /scrape prototype, synthesizes script + test + fixture. |
| `/learn` | **Memory** | Manage what gstack learned across sessions. Review, search, prune, and export. |
| `/gstack-upgrade` | **Self-Updater** | Upgrade gstack to the latest version. |
| `/landing-report` | **Ship Queue Dashboard** | Read-only snapshot of the workspace-aware ship queue. |
| `/setup-deploy` | **Deploy Configurator** | One-time setup for `/land-and-deploy`. Detects platform, production URL, and deploy commands. |
| `/setup-gbrain` | **Memory Sync** | Set up gbrain for cross-machine session memory sync. |
| `/sync-gbrain` | **Keep Brain Current** | Refresh gbrain against this repo's code. |
| `/open-gstack-browser` | **GStack Browser** | Launch GStack Browser with sidebar, anti-bot stealth, auto model routing, cookie import. |
| `/make-pdf` | **PDF Generator** | Turn any markdown file into a publication-quality PDF. |
| `/ios-qa` | **iOS QA Lead** | Live-device iOS QA via USB CoreDevice tunnel + embedded StateServer. |
| `/ios-fix` | **iOS Autonomous Fixer** | Closes the find→fix→verify loop on a real iPhone. |
| `/ios-design-review` | **iOS Designer's Eye** | 10-dimension Apple HIG audit on a real iPhone. |
| `/ios-clean` | **iOS Bridge Cleanup** | Strip DebugBridge SPM + `#if DEBUG` wiring before a Release build. |
| `/ios-sync` | **iOS Bridge Resync** | Regenerate accessors and Swift templates against the latest upstream gstack. |
| `/plan-tune` | **Question Tuner** | Self-tune AskUserQuestion sensitivity per question. |

## Docs

### AGENTS.md (agent instruction file)

gstack is a collection of SKILL.md files that give AI agents structured roles for software development. Each skill is a specialist: CEO reviewer, eng manager, designer, QA lead, release engineer, debugger, and more.

Skills live in `.agents/skills/` (or `~/.claude/skills/gstack/` on Claude Code). Invoke them by name (e.g., `/office-hours`).

Build commands:
```bash
bun install              # install dependencies
bun test                 # run free tests (no API spend)
bun run build            # generate docs + compile binaries
bun run gen:skill-docs   # regenerate SKILL.md files from templates
bun run skill:check      # health dashboard for all skills
```

Key conventions:
- SKILL.md files are **generated** from `.tmpl` templates. Edit the template, not the output.
- The browse binary provides headless browser access. Use `$B <command>` in skills.
- Safety skills (careful, freeze, guard) use inline advisory prose.
- State paths resolve via `bin/gstack-paths`.

### ARCHITECTURE.md (excerpts)

The core idea: gstack gives Claude Code a persistent browser and a set of opinionated workflow skills. The browser is the hard part — everything else is Markdown.

The key insight: an AI agent interacting with a browser needs **sub-second latency** and **persistent state**. gstack runs a long-lived Chromium daemon that the CLI talks to over localhost HTTP.

Architecture diagram:
```
Claude Code                     gstack
─────────                      ──────
                               ┌──────────────────────┐
  Tool call: $B snapshot -i    │  CLI (compiled binary)│
  ─────────────────────────→   │  • reads state file   │
                               │  • POST /command      │
                               └──────────┬───────────┘
                                          │ HTTP
                               ┌──────────▼───────────┐
                               │  Server (Bun.serve)   │
                               │  • dispatches command  │
                               └──────────┬───────────┘
                                          │ CDP
                               ┌──────────▼───────────┐
                               │  Chromium (headless)   │
                               │  • persistent tabs     │
                               │  • 30min idle timeout  │
                               └───────────────────────┘
```

First call starts everything (~3s). Every call after: ~100-200ms.

Why Bun: compiled binaries (single ~58MB executable), native SQLite for cookie decryption, native TypeScript, built-in HTTP server.

**Daemon model:** The server writes `.gstack/browse.json` (atomic, mode 0o600) with `{pid, port, token, startedAt, binaryVersion}`. The CLI reads this to find the server. Random port between 10000-60000. Version auto-restart when binary hash changes.

**Security model:** HTTP server binds to `127.0.0.1` only. Dual-listener architecture for pair-agent tunnel mode: local listener (full surface) vs tunnel listener (locked allowlist: /connect, /command with scoped tokens, /sidebar-chat). ngrok only forwards the tunnel port; socket separation enforces security boundaries.

### ETHOS.md (gstack builder principles)

These principles are injected into every workflow skill's preamble automatically.

**The Golden Age:** A single person with AI can now build what used to take a team of twenty. Compression ratios by task type:
- Boilerplate / scaffolding: ~100x
- Test writing: ~50x
- Feature implementation: ~30x
- Bug fix + regression test: ~20x
- Architecture / design: ~5x
- Research / exploration: ~3x

**1. Boil the Lake:** AI-assisted coding makes marginal cost of completeness near-zero. When the complete implementation costs minutes more than the shortcut — do the complete thing. A "lake" is boilable — 100% test coverage for a module, full feature implementation. An "ocean" is not — rewriting an entire system.

**2. Search Before Building:** The 1000x engineer's first instinct is "has someone already solved this?" Three Layers of Knowledge: (1) tried and true, (2) new and popular, (3) novel work.

## Top-level structure

```
.env.example            — environment variable template (Anthropic API key, etc.)
AGENTS.md               — agent instruction file: skill listing for all supported agents
ARCHITECTURE.md         — system design and architectural decisions
BROWSER.md              — browser integration documentation
CHANGELOG.md            — version history (very large, 742KB)
CLAUDE.md               — Claude Code agent instructions (main entry point for Claude)
CONTRIBUTING.md         — contribution guide
DESIGN.md               — design principles
ETHOS.md                — builder philosophy principles injected into all skills
LICENSE                 — MIT License
README.md               — primary documentation (43.9KB)
SKILL.md                — combined skill instructions (generated from .tmpl)
SKILL.md.tmpl           — skill template source
TODOS.md                — project roadmap and open items
USING_GBRAIN_WITH_GSTACK.md — gbrain cross-machine memory sync integration
VERSION                 — version string: 1.44.0.0
agents/                 — OpenClaw/multi-agent configurations
autoplan/               — /autoplan skill (runs CEO→design→eng→DX pipeline)
benchmark/              — /benchmark skill
benchmark-models/       — /benchmark-models cross-model benchmark skill
bin/                    — CLI binaries and helper scripts (gstack-paths, gstack-team-init)
browse/                 — browser automation daemon (Bun/TypeScript, CDP-based)
browser-skills/         — web-specific scraping skills
canary/                 — /canary SRE post-deploy monitoring skill
careful/                — /careful safety guardrails skill
claude/                 — Claude-specific configurations
codex/                  — /codex OpenAI Codex integration skill
conductor.json          — Conductor workspace config
context-restore/        — /context-restore skill
context-save/           — /context-save skill
contrib/                — community contributions
cso/                    — /cso OWASP+STRIDE security audit skill
design/                 — design resources
design-consultation/    — /design-consultation skill
design-html/            — /design-html production HTML generation skill
design-review/          — /design-review live visual audit skill
design-shotgun/         — /design-shotgun multi-variant exploration skill
devex-review/           — /devex-review live DX audit skill
docs/                   — documentation (skills.md, ARCHITECTURE docs, OPENCLAW.md, etc.)
document-generate/      — /document-generate skill (Diataxis docs generation)
document-release/       — /document-release skill (docs sync after shipping)
extension/              — browser extension
freeze/                 — /freeze edit-lock safety skill
gstack/                 — core gstack setup utilities
gstack-upgrade/         — /gstack-upgrade self-update skill
guard/                  — /guard combined safety skill
health/                 — /health code quality dashboard skill
hosts/                  — multi-host (10 agents) configuration files
investigate/            — /investigate systematic debug skill
ios-clean/              — /ios-clean iOS bridge cleanup skill
ios-design-review/      — /ios-design-review iOS visual audit skill
ios-fix/                — /ios-fix iOS autonomous bug fixer skill
ios-qa/                 — /ios-qa live iPhone QA skill
ios-sync/               — /ios-sync iOS bridge resync skill
land-and-deploy/        — /land-and-deploy post-merge deploy verification skill
landing-report/         — /landing-report ship queue dashboard skill
learn/                  — /learn session memory management skill
lib/                    — shared utility library
make-pdf/               — /make-pdf markdown→PDF skill
model-overlays/         — model configuration overlays
office-hours/           — /office-hours YC office hours reframing skill
open-gstack-browser/    — /open-gstack-browser headed browser launcher skill
openclaw/               — OpenClaw agent integration
package.json            — Bun project config (TypeScript, test runner, build scripts)
pair-agent/             — /pair-agent multi-agent browser coordination skill
plan-ceo-review/        — /plan-ceo-review CEO strategic review skill
plan-design-review/     — /plan-design-review design audit skill
plan-devex-review/      — /plan-devex-review DX review skill
plan-eng-review/        — /plan-eng-review architecture review skill
plan-tune/              — /plan-tune question sensitivity tuning skill
qa/                     — /qa automated browser QA skill
qa-only/                — /qa-only report-only QA skill
retro/                  — /retro weekly retrospective skill
review/                 — /review pre-landing PR review skill
scrape/                 — /scrape web data extraction skill
scripts/                — build and generation scripts
setup                   — install script (bash, 46KB)
setup-browser-cookies/  — /setup-browser-cookies skill
setup-deploy/           — /setup-deploy deploy config skill
setup-gbrain/           — /setup-gbrain memory sync setup skill
ship/                   — /ship release and PR creation skill
skillify/               — /skillify scrape→permanent-skill codifier
supabase/               — Supabase integration utilities
sync-gbrain/            — /sync-gbrain gbrain update skill
test/                   — test suite
test-setup.ts           — test configuration
unfreeze/               — /unfreeze edit-unlock skill
```
