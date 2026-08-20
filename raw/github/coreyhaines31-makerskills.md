# coreyhaines31/makerskills

## Metadata
- Stars: 669
- Primary language: (none — SKILL.md docs)
- Default branch: main
- Latest release: v1.5.0 (2026-08-12)
- License: MIT License
- Homepage: https://maker-skills.com
- Fetched: 2026-08-20
- Final URL: https://github.com/coreyhaines31/makerskills

## Description
AI agent skills for the personal operator's craft — decisions, research, second-brain, content rotation, scenario modeling, and meta-skills to author more. Works with Claude Code, Codex, Cursor.

## README
# makerskills

**AI agent skills for the personal operator's craft.** Decisions, research, second-brain workflows, content rotation, scenario modeling, CFO cadence, domain hunts, and the meta-skills to author more.

Built for founders and indie operators. Works with Claude Code, Codex, Cursor, and other Agent Skills hosts.

**Site:** [maker-skills.com](https://maker-skills.com)

---

## Install

```bash
# In Claude Code
/plugin marketplace add coreyhaines31/makerskills
/plugin install makerskills@makerskills
```

Or symlink for local dev:

```bash
git clone https://github.com/coreyhaines31/makerskills ~/code/makerskills
ln -s ~/code/makerskills ~/.claude/plugins/makerskills
```

See INSTALL.md for env vars, personal-config setup, and runtime dependencies.

---

## Getting started — 5-minute path

1. Install the plugin; set `export MAKERSKILLS_CONFIG="$HOME/.config/makerskills"` in `~/.zshenv`.
2. Run `/decide` — no config required. Structured input → structured output → archived with revisit date.
3. Read one SKILL.md to understand the documentation-first pattern.
4. Try `/paste twitter` for a pure utility skill (no config needed).
5. Branch out by matching intent to the routing table below.

---

## Skill routing table

| Intent | Skill |
|---|---|
| Think through a decision with a real fork | `decide` |
| Break through a wall ("this seems impossible") | `unstuck` |
| Get a board of famous founders to weigh in | `maker-council` |
| Pressure-test a new business or product idea | `business-brainstorm` |
| Research a topic with citations | `deep-research` |
| Find an available `.com` for a new project | `domain` |
| Capture / query / lint personal knowledge base | `second-brain` |
| Same but for a team-shared knowledge base | `company-brain` |
| Extract notes / highlights from a book | `read-book` |
| Extract a transcript from a video | `watch-video` |
| Fetch any social post by URL as structured data | `social-fetch` |
| Plan / draft social content rotation | `jab-hook` |
| Draft, update, convert, or export a slide deck | `slide-deck` |
| Clean terminal output for Slack / LinkedIn / X | `paste` |
| Manage projects across businesses (kanban) | `pm` |
| Model personal financial scenarios | `personal-cfo` |
| Run monthly / weekly CFO for a company | `company-cfo` |
| Create, adapt, or update a skill | `skillify` |
| Wire up an integration / API / MCP | `toolify` |
| Set up an agent loop or scheduled task | `loopify` |

---

## The 20 skills

### Meta — extend Claude Code (the `-ify` trifecta)

| Skill | What |
|---|---|
| `skillify` | Create, adapt, or update a skill. Modes: CREATE (from-chat / from-video / from-dump / from-scratch), ADAPT (port external skill with license check + attribution), UPDATE (improve with cross-skill propagation + semver discipline). |
| `toolify` | Wire up an integration, API, MCP server, or third-party service into a Next.js or Rails project. |
| `loopify` | Set up an agent loop, cron-scheduled task, or recurring workflow. Judgment layer for picking pattern (dynamic / cron / one-shot), tunes delay for cache windows, enforces idempotency + bail-out conditions. |

### Decision & strategy

| Skill | What |
|---|---|
| `decide` | 37signals decision framework (38 questions + house additions). Archives with revisit dates. |
| `business-brainstorm` | Pressure-test a new business or product on 9 dimensions. Composes with `deep-research` + `domain`. |
| `domain` | 11-step .com domain hunt — Vercel CLI + whois + Domainr + Namecheap + rdap.org + agent-browser for USPTO screening + aftermarket click-throughs. |
| `deep-research` | Multi-source research with citations + archive. WebSearch, WebFetch, agent-browser, /last30days, memory. |
| `unstuck` | Classifies what kind of "no" you hit (assumption / framing / gatekeeper / tool / resource / physics), runs targeted lateral-thinking techniques from 10-technique inventory. |
| `maker-council` | Simulated personal board of advisors — Fried, Musk, Bezos, Jensen, Iger, Graham, Naval, Blakely. Seats 3–5 by question type with a designated dissenter. Custom members via config dir. |

### Knowledge & content consumption

| Skill | What |
|---|---|
| `second-brain` | Karpathy LLM Wiki workflow over any markdown vault. Capture / compile / query / lint / connect / search. Personal-scope. |
| `company-brain` | Team-scope sibling to second-brain. Structured raw dirs, multi-author attribution, sensitivity tagging, trust levels, `/cb review` culling pass, optional auto-sync from Fathom / Gong / Granola / CRM. |
| `read-book` | PDFs, EPUBs, MOBI, markdown — chapter-by-chapter notes, quotes, summaries, or spaced-rep study mode. |
| `watch-video` | YouTube, Loom, Vimeo, Riverside, Zoom, MP4. Transcript / visual / multimodal modes. |

### Output & creative

| Skill | What |
|---|---|
| `jab-hook` | Gary Vee's jab-jab-jab-right-hook rhythm applied to portfolio rotation on X + LinkedIn via Typefully. |
| `slide-deck` | Branded React decks (Next.js). "Show, don't tell" narrative pitching, density modes, PPT conversion, Playwright export. |

### Operations & utilities

| Skill | What |
|---|---|
| `pm` | Kanban (5-column) + Eisenhower across portfolio. Tool-agnostic adapters (Notion, GitHub, Plane, Linear, Obsidian). |
| `personal-cfo` | Personal financial scenarios — house purchase + rental forecasting, monthly cash flow, big-purchase decisions. |
| `company-cfo` | Company / agency CFO workflow — monthly snapshots, weekly cash pulse, scenario projector. |
| `paste` | Clean terminal output for 9 destinations (Slack, Notion, Twitter, LinkedIn, email, GitHub, plain, HTML). Secret-detection first. |
| `social-fetch` | Pull any social post by URL across 10 platforms (X, LinkedIn, IG, TikTok, Bluesky, Reddit, Mastodon, Threads, HN). |

---

## Skills compose

Skills call each other by name. Most-referenced skills in the plugin:

| Most referenced by siblings | Composes with... |
|---|---|
| `watch-video` (54 refs) | `second-brain`, `skillify from-video`, `social-fetch`, `pm`, `decide` |
| `skillify` (51 refs) | `watch-video`, `second-brain`, `compound-engineering:*` |
| `second-brain` (48 refs) | `deep-research`, `read-book`, `watch-video`, `paste` |
| `slide-deck` (38 refs) | `business-brainstorm`, `watch-video`, `second-brain` |
| `company-brain` (33 refs) | `toolify`, `loopify`, `deep-research`, `decide` |
| `domain` (32 refs) | `business-brainstorm`, `toolify`, `decide` |

---

## Architecture

Public + generic repo. Personal data (Typefully workspace IDs, portfolio properties, voice overlays, archives) lives in `~/.config/makerskills/` (gitignored, on disk only). Skills read from `${MAKERSKILLS_CONFIG:-$HOME/.config/makerskills}/<skill>/` paths.

```bash
export MAKERSKILLS_CONFIG="$HOME/.config/makerskills"
export SECOND_BRAIN_VAULT="$HOME/Documents/SecondBrain"
export COMPANY_BRAIN_VAULT="$HOME/Documents/CompanyBrain"
export COMPANY_CFO_ROOT="$HOME/code/company-cfo"
export SLIDE_DECK_REPO="$HOME/code/your-site-repo"
```

---

## Versioning

- **Plugin release tag** (e.g. `v1.5.0`) — overall repo version
- **Per-skill `metadata.version`** in SKILL.md frontmatter — each skill's individual version (evolves independently)

## SKILL.md format

```yaml
---
name: skill-name
description: When the user wants to [X]. Triggers on "[trigger phrase]"...
metadata:
  version: 0.1.0
---
```

## Cross-plugin refs

- Within plugin: mention by name (`see decide`)
- Cross-plugin: prefix with plugin name (`see marketingskills:cro`)

## Related skill packs

- `marketingskills` (https://github.com/coreyhaines31/marketingskills) — 46 marketing skills (CRO, copywriting, SEO, ads, etc.)

## Docs

- INSTALL.md — env vars, personal config setup, runtime dependencies
- EXAMPLES.md — one worked example per skill
- ARCHITECTURE.md — mental model, families, personal-config pattern, sibling-repo ecosystem
- CHANGELOG.md — release history
- CONTRIBUTING.md — how to add a skill, testing, PR conventions
- FAQ.md — common questions and gotchas
- BACKLOG.md — planned skills + brainstorm candidates

## Top-level structure

- `skills/` — 20 skill directories: `business-brainstorm/`, `company-brain/`, `company-cfo/`, `decide/`, `deep-research/`, `domain/`, `jab-hook/`, `loopify/`, `maker-council/`, `paste/`, `personal-cfo/`, `pm/`, `read-book/`, `second-brain/`, `skillify/`, `slide-deck/`, `social-fetch/`, `toolify/`, `unstuck/`, `watch-video/` — each with a `SKILL.md`
- `.claude-plugin/` — plugin manifest files (`marketplace.json`, `plugin.json`) for Claude Code plugin marketplace
- `ARCHITECTURE.md`, `BACKLOG.md`, `CHANGELOG.md`, `CONTRIBUTING.md`, `EXAMPLES.md`, `FAQ.md`, `INSTALL.md` — comprehensive documentation
- `LICENSE` — MIT License
- `README.md` — routing table, 5-minute path, architecture overview
