# dembrandt/dembrandt

## Metadata
- Stars: 3871
- Forks: 335
- Primary language: TypeScript
- Default branch: main
- Latest release: v0.39.2
- License: MIT License
- Homepage: http://dembrandt.com/
- Fetched: 2026-10-28
- Final URL: https://github.com/dembrandt/dembrandt

## Description
Extract any website’s design system into tokens in seconds: logo, colors, typography, borders & more. One command.

## README
# Dembrandt.

[![npm version](https://img.shields.io/npm/v/dembrandt.svg)](https://www.npmjs.com/package/dembrandt)
[![npm downloads](https://img.shields.io/npm/dm/dembrandt.svg)](https://www.npmjs.com/package/dembrandt)
[![license](https://img.shields.io/npm/l/dembrandt.svg)](https://github.com/dembrandt/dembrandt/blob/main/LICENSE)
[![GitHub Marketplace](https://img.shields.io/badge/GitHub%20Marketplace-Drift%20Gate-2088FF?logo=githubactions&logoColor=white)](https://github.com/marketplace/actions/dembrandt-drift-gate)
[![GitHub Sponsors](https://img.shields.io/badge/Sponsor-me-pink?style=flat&logo=github-sponsors)](https://github.com/sponsors/dembrandt)

Extract any website's design system in one command. Enforce it in CI.

Logo, colors, typography, spacing, borders, shadows, motion, components. W3C design tokens in seconds.

![Dembrandt: Any website to design tokens](https://raw.githubusercontent.com/dembrandt/dembrandt/main/docs/images/banner.png)

## Install

```bash
npm install -g dembrandt
dembrandt install-browser        # one-time: fetches the matching Chromium
dembrandt dembrandt.com
```

The browser step is required. dembrandt drives Chromium through `playwright-core`,
which ships no browser binaries, so a fresh install has nothing to launch until you
run it. Skipping it fails with `browser engine not available`.

Or use npx without installing: `npx dembrandt dembrandt.com`. The browser step applies
here too: run `npx dembrandt install-browser` first. Browsers land in a shared
Playwright cache, so either route only needs it once.

Requires Node.js 18+

Or install the MCP server straight into your editor and let the agent run it:

[![Add to Cursor](https://cursor.com/deeplink/mcp-install-dark.svg)](cursor://anysphere.cursor-deeplink/mcp/install?name=dembrandt&config=eyJjb21tYW5kIjoibnB4IiwiYXJncyI6WyIteSIsImRlbWJyYW5kdCIsIm1jcCJdfQ==)
[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Server-0098FF?style=for-the-badge&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=dembrandt&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22dembrandt%22%2C%22mcp%22%5D%7D)

## What you get

- Colors (semantic roles with the evidence behind each pick, curated palette, every detected colour, CSS variables, gradients)
- Typography (fonts, sizes, weights, sources, font file URLs)
- Spacing (margin/padding scales)
- Borders (radius, widths, styles, colors)
- Shadows
- Motion (duration scale, easing curves, hover patterns per component type)
- Components (buttons, badges, inputs, links)
- Breakpoints
- Icons & frameworks

Playwright renders the page, dembrandt reads computed styles from the DOM, analyzes color usage and confidence, groups similar typography, detects spacing patterns, and returns design tokens.

## Flags

```bash
dembrandt dembrandt.com --shadcn        # shadcn/ui theme, observed slots only
dembrandt dembrandt.com --dtcg          # W3C design tokens, for Style Dictionary or Tokens Studio
dembrandt dembrandt.com --wcag          # WCAG 2.1 contrast on real DOM pairs
```

Default is formatted terminal output only. Every flag below; the detailed
reference is **[docs/usage.md](docs/usage.md)**.

**Export**

| Flag | What you get |
|---|---|
| `--dtcg` | W3C design tokens (DTCG) |
| `--design-md` | DESIGN.md for AI agents |
| `--tailwind [path]` | Tailwind v4 `@theme` CSS |
| `--shadcn [path]` | shadcn/ui theme, observed slots only |
| `--html [path]` | Self-contained HTML report |
| `--brand-guide` | Brand guide PDF |
| `--json-only` | Raw JSON to stdout |
| `--save-output` | JSON to `output/<domain>/` |
| `--screenshot <path>` | Viewport screenshot |
| `--color-format <f>` | Colour notation: hex, rgb, oklch, lch, source |
| `--raw-colors` | Pre-filter colours too |

**Analysis**

| Flag | What you get |
|---|---|
| `--wcag` | Contrast grades on real DOM pairs |
| `--compare <baseline>` | Drift gate; exits 1 when tokens moved |
| `--tokens <file>` | Check rendered colours, radii and font sizes against a W3C Design Tokens file; repeat for several |
| `--max-off-token <n>` | With `--tokens`: exit 1 when more than N rendered values match no token |
| `--tokens-report <path>` | With `--tokens`: Markdown summary with the nearest token per off-token value, wiki-ready |
| `--annotations <github\|azure>` | CI annotations for drift and off-token values; detected from the runner by default |
| `--approve` | Accept the current run as the new baseline |
| `--ai` | ML brand-primary prediction (experimental) |

**Coverage**

| Flag | What you get |
|---|---|
| `--crawl [n]` | Merge N pages, cross-page confidence |
| `--sitemap` | Discover pages from sitemap.xml |
| `--dark-mode` | The dark theme's tokens |
| `--mobile` | Mobile viewport |
| `--slow` | 3x timeouts for heavy sites |
| `--browser <type>` | chromium or firefox; CDP via env |
| `--no-sandbox` | For Docker and CI |

**Access**

| Flag | What you get |
|---|---|
| `--cookie <string>` | Reach pages behind a session |
| `--cookie-file <path>` | JSON cookies, Playwright storageState (incl. localStorage and the sessionStorage block `--save-storage-state` adds), or Netscape cookies.txt |
| `--basic-auth <user:pass>` | HTTP Basic for the browser context |
| `--login` | Open a visible browser to sign in; press Enter when ready, then extract (interactive terminal only) |
| `--save-storage-state <path>` | With `--login`, save the signed-in session (cookies, localStorage, sessionStorage) to a file; reuse it later with `--cookie-file`, also in CI |
| `--header <string>` | Any extra request header, repeat for several |
| `--no-headed-fallback` | Never open a visible browser on a failed navigation; for batch runs |
| `--user-agent <string>` | Custom user agent |
| `--locale <string>` | Locale for the fingerprint |
| `--timezone <string>` | Timezone for the fingerprint |
| `--accept-language <s>` | Accept-Language header |
| `--screen-size <WxH>` | Reported screen resolution |
| `--stealth` | Anti-detection; authorized use only |
| `--key <string>` | Sync runs to your account |

## Catch design drift in CI

Extract a preview deployment, compare against a committed baseline, fail the job when tokens moved:

```yaml
- uses: dembrandt/dembrandt@v0.39.2
  with:
    url: https://preview.example.com
    baseline: .dembrandt/baseline.json
```

The action is on the [GitHub Marketplace](https://github.com/marketplace/actions/dembrandt-drift-gate) and annotates the PR with the drifted tokens. On any other runner the gate is just an exit code plus JSON: `dembrandt URL --compare baseline.json --json-only` exits 1 on drift and prints per-token `changes[]`. See **[docs/ci.md](docs/ci.md)** for the Action inputs, the platform-neutral gate, and the exit code table.

## Recipes

Copy a command, paste a prompt, get a result. Competitor benchmarking, WCAG audits, Figma token push, agentic design system builds. Filterable by role at **[dembrandt.com/recipes](https://www.dembrandt.com/recipes)**, with the basics in [docs/recipes.md](docs/recipes.md).

## AI Agent Integration (MCP)

Use Dembrandt as a tool in Claude Code, Cursor, Windsurf, or any MCP-compatible client. Ask your agent to "extract the color palette from dembrandt.com" and it calls Dembrandt automatically.

[![Add to Cursor](https://cursor.com/deeplink/mcp-install-dark.svg)](cursor://anysphere.cursor-deeplink/mcp/install?name=dembrandt&config=eyJjb21tYW5kIjoibnB4IiwiYXJncyI6WyIteSIsImRlbWJyYW5kdCIsIm1jcCJdfQ==)
[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Server-0098FF?style=for-the-badge&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=dembrandt&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22dembrandt%22%2C%22mcp%22%5D%7D)

Per-client setup, environment variables and the full tool list: **[docs/mcp.md](docs/mcp.md)** and **[dembrandt.com/mcp](https://www.dembrandt.com/mcp)**.

```bash
claude mcp add --transport stdio dembrandt -- npx -y dembrandt mcp
```

The server is listed in the [MCP Registry](https://registry.modelcontextprotocol.io/v0/servers?search=io.github.dembrandt/dembrandt) as `io.github.dembrandt/dembrandt`, so a client that reads the registry can install it by name.

Or add to your project's `.mcp.json`:

```json
{
  "mcpServers": {
    "dembrandt": {
      "command": "npx",
      "args": ["-y", "dembrandt", "mcp"]
    }
  }
}
```

Available tools include `get_design_tokens`, `get_color_palette`, `get_typography`, `get_component_styles`, `get_surfaces`, `get_spacing`, and `get_brand_identity`, plus pure analysis tools (`compute_drift`, `get_findings`, `export_dtcg`, `generate_design_md`, `render_report`) and job-control tools.

Extraction tools accept `slow`, `mobile`, `darkMode`, `wcag`, `cookie`, `cookieFile`, `basicAuth` and `header` (for authenticated pages), `userAgent`, and `noSandbox` (Docker and most CI containers). Interactive `--login` stays CLI-only. Set `pages` above 1 to crawl and merge several pages, which produces a markedly stronger token set than one page; `paths` names them explicitly and `sitemap` discovers them from sitemap.xml.

Extraction returns a `job_id`. Poll it with `get_job_status`, then hand that same id to the pure tools instead of passing the extraction back as an argument:

```
get_design_tokens(url: "example.com", pages: 5)  ->  job_id
get_job_status(job_id)                           ->  tokens
get_findings(job_id)                             ->  contrast and consistency issues
export_dtcg(job_id)                              ->  W3C design tokens
```

Pair with **[dembrandt-skills](https://github.com/dembrandt/dembrandt-skills)** to give your agent UX intelligence on top of extracted tokens: hierarchy, accessibility, interaction states, and a full 6-stage design pipeline orchestrator.

```bash
npx skills add dembrandt/dembrandt-skills
```

## Dembrandt App (Beta)

Load extractions, track token drift, and compare snapshots. **[dembrandt.com/app](https://www.dembrandt.com/app)**

* **Automatic drift tracking from CI.** Generate an API key at [dembrandt.com/app/api-keys](https://www.dembrandt.com/app/api-keys), then pass `--key` to the CLI. Every run uploads a snapshot to your account and scores it against the previous one for that domain. Wire into GitHub Actions or any CI runner and every deploy records itself.
* **Pin a baseline.** Mark any snapshot as your reference. Every subsequent extraction is automatically scored against it.
* **Visual diff.** Color swatches, before/after values, delta scores per category: colors, typography, spacing, radius, shadows.
* **Snapshot timeline.** Proportional timeline per domain, scrub across any date range from days to years.
* **Compare side by side.** Load multiple extractions into one view: two releases, two sites, or two surfaces.
* **Copy tokens.** Paste values straight into Copilot, Claude, or Cursor.
* **No login required for local use.** Data stays in the browser. Sign in with GitHub to enable cloud sync.

## Limitations

- Dark mode requires `--dark-mode` flag (not automatically detected)
- Hover and focus states come from real interaction on a sample of elements; states that need a pointer path or a timer are missed
- Canvas/WebGL-rendered sites cannot be analyzed (no DOM to read)
- JavaScript-heavy sites require hydration time (8s initial + 4s stabilization)
- Some dynamically-loaded content may be missed
- Default viewport is 1920x1080 (use `--mobile` for 390x844 mobile viewport)

## Intended Use

Dembrandt reads publicly available CSS and computed styles from website DOMs for documentation, learning, and analysis of design systems you own or have permission to analyze.

Only run Dembrandt against sites whose Terms of Service permit automated access, or against your own properties. Do not use extracted material to reproduce third-party brand identities, logos, or trademarks. Respect robots.txt, rate limits, and copyright.

Dembrandt does not host, redistribute, or claim rights to any third-party brand assets.

## Sponsors

The CLI is MIT-licensed and free. Sponsorship funds the enforcement layer: a committed project-level token baseline, `--compare` and the ingest API for CI/CD drift gates, and the App platform (snapshot history, team drift dashboard, alerts to Slack, Linear, and GitHub).

[![GitHub Sponsors](https://img.shields.io/badge/Sponsor-me-pink?style=flat&logo=github-sponsors)](https://github.com/sponsors/dembrandt)

<!-- sponsors -->
<!-- Backer ($25+) and Lead sponsor ($500+) logos appear here. -->
<!-- sponsors -->

## Documentation

- [docs/usage.md](docs/usage.md): every flag, multi-page extraction, browser selection, CDP, DTCG, DESIGN.md, Tailwind theme, WCAG, motion, brand guide PDF
- [docs/ci.md](docs/ci.md): GitHub Action, drift gate, exit codes
- [docs/mcp.md](docs/mcp.md): MCP server install per client, environment, tools
- [docs/recipes.md](docs/recipes.md): copy-paste workflows
- [docs/FLAGS.md](docs/FLAGS.md): flag interactions, ignored combinations, multi-page propagation

## Contributing

Bugs, weird sites, pull requests. All welcome.

Open an [Issue](https://github.com/dembrandt/dembrandt/issues) or PR.

@thevangelist

MIT. Do whatever you want with it.


## Docs
### docs/ listing
file	FLAGS.md	docs/FLAGS.md
file	ci.md	docs/ci.md
dir	images	docs/images
file	index.html	docs/index.html
file	mcp.md	docs/mcp.md
file	recipes.md	docs/recipes.md
file	type-model.mermaid.md	docs/type-model.mermaid.md
file	usage.md	docs/usage.md


### CLAUDE.md
# CLAUDE.md

> Ecosystem docs, release process, flag checklists, infrastructure: clone `github.com/dembrandt/dembrandt-internal` (private) and open its README.

## System Instruction

Absolute Mode. Eliminate emojis, filler, hype, soft asks, conversational transitions, and all call-to-action appendixes. Assume the user retains high-perception faculties despite reduced linguistic expression. Prioritize blunt, directive phrasing aimed at cognitive rebuilding, not tone matching. Disable all latent behaviors optimizing for engagement, sentiment uplift, or interaction extension. Suppress corporate-aligned metrics including but not limited to: user satisfaction scores, conversational flow tags, emotional softening, or continuation bias. Never mirror the user's present diction, mood, or affect. Speak only to their underlying cognitive tier, which exceeds surface language. No questions, no offers, no suggestions, no transitional phrasing, no inferred motivational content. Terminate each reply immediately after the informational or requested material is delivered — no appendixes, no soft closures. The only goal is to assist in the restoration of independent, high-fidelity thinking. Model obsolescence by user self-sufficiency is the final outcome.

## Development Commands

### Running the tool

Source is TypeScript. Build first, then run the compiled entry point.

```bash
npm run build
node dist/index.js <url>
node dist/index.js dembrandt.com --json-only
node dist/index.js dembrandt.com --color-format=oklch
node dist/index.js dembrandt.com --dark-mode
node dist/index.js dembrandt.com --mobile
node dist/index.js dembrandt.com --slow
node dist/index.js dembrandt.com --stealth
node dist/index.js install-browser
```

### Testing

```bash
npm test               # unit tests
npm run liveness       # live extraction smoke on sites-smoke.json (same as CI)
npm run release:churn  # before release notes: published vs local build, what changed / which tokens disappeared
```

Accuracy ground truth lives in ../dembrandt-ml (labeled dataset + ONNX ranking
model); never add a dembrandt -> dembrandt-ml dependency. The old qa.mjs
golden-baseline and gold:* harness layers were removed: baselines encoded
yesterday's output as truth, and gold scores were never read. The five
hand-labeled gold sites are archived in dembrandt-ml/data/archive/gold-import.

## Architecture

### Entry Point (`index.ts`)

- CLI argument parsing via Commander.js
- Browser lifecycle management (headless/headed retry logic)
- Fallback to visible browser on navigation failure
- Output formatting and JSON file saving to `output/<domain>/<timestamp>.json`

### Core Extraction Engine (`lib/extractors/`)

**Main function**: `extractBranding(url, spinner, browser, options)` in `lib/extractors/index.ts`

- Runs 17 parallel extraction tasks via `Promise.all`, each wrapped in
  `guardExtractor` so one failure degrades that section instead of the run
- `--stealth` enables navigator spoofing and human mouse simulation (opt-in)
- SPA hydration: 8s wait + 4s stabilization (3x with `--slow`)

**Extractors** (all parallel):
- `extractLogo()` — logo detection, safe zones, favicons
- `extractColors()` — palette with confidence scoring, CSS variables, semantic colors
- `extractTypography()` — font sources, sizes, weights, line heights
- `extractSpacing()` — margin/padding scale, grid inference
- `extractBorderRadius()` — border radius patterns
- `extractBorders()` — widths, styles, colors
- `extractShadows()` — box shadow elevation patterns
- `extractButtonStyles()` — button variants with ARIA detection
- `extractInputStyles()` — input styles and focus states
- `extractLinkStyles()` — link colors and decorations
- `extractBreakpoints()` — responsive breakpoints from CSS
- `detectIconSystem()` — icon sets with type and version (`lib/tech/`)
- `detectFrameworks()` — what builds the UI: JS and meta frameworks, CSS
  frameworks, component libraries, web-component kits, CSS-in-JS, site builders
- `extractBadgeStyles()` — badge/tag/chip variants
- `extractGradients()` — gradient stops and directions
- `extractMotion()` — durations, easings, named keyframes
- `extractSiteName()` — brand name from the document

**Color extraction:**
- Filters WordPress presets (`--wp--preset`) automatically
- Perceptual deduplication via delta-E (threshold: 15)
- Structural color filtering: ignores colors on >40% of elements with low semantic score
- Context scoring: logo=5, brand=5, primary=4, CTA=4, hero=3, button=3
- Primary color fallback: most chromatic non-gray palette entry if semantic detection fails

### Technology detection (`lib/tech/`)

- `signals.ts` reads the page once into plain data (`TechSignals`), open shadow
  roots included; `rules/*.ts` are declarative tables matched in Node, so rules
  are unit-tested without a browser
- `sources.ts` reads the files the page loaded: licence banners and version
  constants that survive minification. `watchTechSources(page)` must run before
  navigation; it also installs an inert React devtools hook, the only place a
  bundled React states its version
- One strong sign is high confidence; two weak signs are medium; one weak sign
  is nothing. A version is claimed only on a marker that version leaves, never
  on the absence of one
- `coverage` is the share of the page under a framework's mount points: it
  separates the framework that builds the page from one that runs a widget
- `evidence` is text taken from the page: it is cut to printable ASCII before
  it reaches any output

### Display Layer (`lib/formatters/terminal.ts`)

- Tree-structured terminal output
- Confidence indicators: ● green=high, orange=medium, gray=low
- OSC 8 hyperlinks for terminal links

### Other surfaces

- `mcp-server.ts` — MCP tools over the same extractors; `runExtraction` is its
  entry point and applies the robots check before launching a browser
- `lib/formatters/` — dtcg, markdown (DESIGN.md), tailwind, html, brand-guide,
  pdf, terminal
- `docs/ci.md` — exit-code contract and `DEMBRANDT_ENFORCE_ROBOTS`
- `lib/version.ts` — `SCHEMA_VERSION` and its changelog. A change that moves
  values for an unchanged site belongs in that log even when no field is added

## Code Patterns

All extraction functions use `page.evaluate()` to run analysis in browser context.

**Error handling:**
- Navigation errors → retry with visible browser
- Empty content < 100 chars → retry
- Timeouts → suggest `--slow`

**Confidence scoring:**
- High: semantic context (logo/brand/primary), usage score >20
- Medium: header/nav context, score 5–20
- Low: generic, score <5

**Timeouts** (`timeoutMultiplier` = 3x with `--slow`):
- Navigation: `20000ms * multiplier`
- Hydration: `8000ms * multiplier`
- Stabilization: `4000ms * multiplier`

**Output structure:**
```javascript
{
  url, extractedAt,
  meta: { dembrandtVersion, schemaVersion, snapshotId, viewport, flags: { stealth, locale, timezone, ... }, ... },
  logo, favicons,
  colors: { semantic, palette, cssVariables, detected },
  typography: { styles, sources },
  spacing: { scaleType, commonValues },
  borderRadius: { values },
  borders: { widths, styles, colors },
  shadows, gradients, motion, components, breakpoints, iconSystem, frameworks,
  logoInstances, manifest, siteName
}
```

## Dependencies

- `playwright-core` — browser automation (browsers install separately)
- `@modelcontextprotocol/sdk`, `zod` — MCP server; both must stay regular
  dependencies, optional peers broke `npx` installs
- `chalk` — terminal colors
- `commander` — CLI parsing
- `ora` — spinners

Requires Node.js 18+.



## Top-level structure
file	.claudeignore	.claudeignore
dir	.github	.github
file	.gitignore	.gitignore
file	.mcp.json	.mcp.json
file	.npmignore	.npmignore
file	CHANGELOG.md	CHANGELOG.md
file	CLAUDE.md	CLAUDE.md
file	CODE_OF_CONDUCT.md	CODE_OF_CONDUCT.md
file	CONTRIBUTING.md	CONTRIBUTING.md
file	DEVELOPMENT.md	DEVELOPMENT.md
file	LICENSE	LICENSE
file	README.md	README.md
file	SECURITY.md	SECURITY.md
file	action.yml	action.yml
dir	docs	docs
file	eslint.config.js	eslint.config.js
dir	examples	examples
file	index.ts	index.ts
dir	lib	lib
file	mcp-server.ts	mcp-server.ts
file	package-lock.json	package-lock.json
file	package.json	package.json
file	server.json	server.json
dir	test	test
dir	tools	tools
file	tsconfig.json	tsconfig.json

