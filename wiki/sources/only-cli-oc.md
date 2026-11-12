---
type: source
category: "Browser & web automation"
source_url: https://github.com/only-cli/oc
tags:
  - agent-cli
  - token-efficient-browsing
  - site-shortcuts
  - html-distillation
  - chrome-impersonation
  - agent-skills
  - web-fetch
  - only-cli
related:
  - jackwener-opencli
  - browse.sh
  - vercel-labs-agent-browser
  - microsoft-playwright-mcp
  - firecrawl.dev
  - zenbu-labs-terminal-browser
  - Tencent-BrowserSkill
  - playwright.dev-agent-cli
  - skills.sh
  - x.com-ericzakariasson-building-clis-for-agents
product: oc
detail_level: standard
created: 2026-11-10
updated: 2026-11-10
studied: true

---

only-cli/oc (641★, MIT, JavaScript, npm `@only-cli/oc` v0.5.8) turns any mostly-static website into a compact CLI for AI agents: `oc open <url>` returns a distilled text view with numbered links and regions in roughly hundreds of tokens instead of raw HTML or browser snapshots. It ships per-site shortcuts (`clis/*.json`), an Agent Skill (`web-browsing-cli`), a Claude Code plugin, and benchmarks claiming ~118× fewer tokens than raw HTML versus tools like Jina Reader and Playwright MCP accessibility snapshots. Closest wiki peer is [[jackwener-opencli]] (website→CLI), with adjacent agent-browser tooling in [[browse.sh]], [[vercel-labs-agent-browser]], and [[microsoft-playwright-mcp]].

_All claims below are sourced from ../../raw/github/only-cli-oc.md unless otherwise noted._

## What it does

`oc` fetches pages (Chrome impersonation via optional `impers`, with Firefox then plain-fetch fallback), distills HTML/JSON/feeds into a budgeted terminal view, and lets the agent act with numbered commands: `do <n>` follows a link or reads a text region, `find`/`read`/`next` recover cut content without refetching, and `raw` dumps full markdown or cleaned HTML when needed. Session state and optional cookie jars live under `~/.only-cli`. Site shortcuts (`oc gh repo …`, `oc wiki article …`, `oc npm …`, etc.) resolve to URLs or public JSON/feed APIs so agents skip guessing URL shapes and login walls. Writing (`fill`/`submit`/`back`) and JavaScript rendering are explicitly not implemented yet.

## Installation

Node.js ≥20. Global install or zero-install:

```bash
npm install -g @only-cli/oc
# or
npx --yes @only-cli/oc@0.5.8 open https://example.com
```

Agent Skill: `npx skills add https://github.com/only-cli/oc --skill web-browsing-cli` (also listed on [[skills.sh]]). Claude Code can install the bundled `.claude-plugin` marketplace entry. Homepage marketing site: https://only-cli.com.

## Key features

- **Token budget** — default ~500 tokens per page (`--budget`); soft target with whole-page print when only slightly over; main content before nav/sidebar/footer.
- **Numbered actions** — `[n]` marks links, headings, and cut text blocks; `actions:` footer lists valid next commands; `--json` for machine-stable output.
- **Site shortcuts** — 40+ `clis/*.json` definitions (HN, Reddit Atom feeds, GitHub/GitLab/Codeberg APIs, Wikipedia, cloud docs, language docs with Sphinx/MkDocs/RDoc/Node index search, npm/PyPI/crates/RubyGems/Docker Hub JSON, OSV, caniuse, tldr, man pages, RFCs, Discourse forums, etc.).
- **Auth & SSRF** — `oc login --cookie - --domain …` seeds timeboxed https-only cookie jars from stdin; private/internal targets refused; `HTTP_PROXY`/`HTTPS_PROXY`/`NO_PROXY` honored.
- **Empty-page signal** — JS-only / consent / bot walls exit 2 with an `empty` JSON field so agents can escalate to a real browser.
- **Agent packaging** — `skills/web-browsing-cli/SKILL.md`, Claude plugin manifests, and repo-root `llms.txt`.

## Architecture

Plain ESM JavaScript, no build step. Runtime deps are `linkedom` + `turndown` (optional `impers` for TLS fingerprint impersonation). Core modules under `src/`: `cli.js` (command surface), `fetch.js` (HTTP + impersonation + proxy), `distill.js` / `render.js` (HTML→budgeted view), `sites.js` + search backends (`sphinx.js`, `mkdocs.js`, `rdoc.js`, `nodedocs.js`, `apisearch.js`), `session.js` / `cookies.js`, `act.js`. Site defs are data-only JSON under `clis/`; CONTRIBUTING ranks principles as token economy → slim install → stateless default → deterministic output → fail loud. Tests are fully offline against `tests/pages/` fixtures.

## Example usage

```bash
oc open https://news.ycombinator.com
oc do 3
oc find "Show HN"
oc next
oc raw https://example.com --html

oc hn top
oc gh repo only-cli oc
oc wiki article Eiffel Tower
oc py library json
oc npm pkg lodash

printf %s "session=…; auth=…" | oc login --cookie - --domain example.com --expires 2h --session work
oc open https://example.com/dashboard --session work
oc logout work
```

## Maintenance status

641 stars, 40 forks, default branch `main`, latest npm/GitHub release **v0.5.8** (2026-09-25), MIT. Actively pushed as of fetch (2026-11-10); CHANGELOG Unreleased already documents package-registry shortcuts, forge APIs, MkDocs search, and Discourse forums beyond the tagged release. Status section: reading path covered by offline tests; form fill/submit and headless JS fallback still on the roadmap. Security reports via GitHub advisories; `experiments/` out of scope.
