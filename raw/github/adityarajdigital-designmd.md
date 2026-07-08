# adityarajdigital/designmd

## Metadata
- Stars: 49
- Primary language: null
- Default branch: main
- Latest release: v0.1.2 — version alignment (2026-05-20)
- License: MIT License
- Homepage: https://designmd.cc
- Fetched: 2026-07-08
- Final URL: https://github.com/adityarajdigital/designmd

## Description
Production-grade design context for AI coding workflows. Extract a real design system from any URL — colors, typography, spacing, breakpoints — as a portable DESIGN.md.

## README

<div align="center">

<img src="./assets/logo.png" alt="DesignMD" width="120" />

# DesignMD

### Production-grade design context for AI coding workflows.

Extract a real design system from any production URL — colors, typography, spacing, breakpoints, motion, interaction states — and stream it as a portable `DESIGN.md` your coding agent can actually read.

[![npm](https://img.shields.io/npm/v/@designmdcc/cli?style=flat-square&color=2A2620&label=%40designmdcc%2Fcli)](https://www.npmjs.com/package/@designmdcc/cli)
[![Demo](https://img.shields.io/badge/demo-designmd.cc-D14E2F?style=flat-square)](https://designmd.cc)
[![Benchmarks](https://img.shields.io/badge/benchmarks-56_sites-2A2620?style=flat-square)](https://designmd.cc/benchmarks)
[![License](https://img.shields.io/badge/license-MIT-2A2620?style=flat-square)](./LICENSE)

[**Web**](https://designmd.cc) · [**Benchmarks**](https://designmd.cc/benchmarks) · [**CLI on npm**](https://www.npmjs.com/package/@designmdcc/cli) · [**Examples**](./examples)

</div>

<br />

---

## Quick start

```bash
npx @designmdcc/cli stripe.com > DESIGN.md
```

That's the whole flow. No account, no config, no API key. The command streams a measured `DESIGN.md` spec for `stripe.com` to stdout; redirect it into a file and hand it to your AI coding agent.

For repeat use, install globally:

```bash
npm install -g @designmdcc/cli
dmd stripe.com > DESIGN.md
```

Requires **Node 18+**.

<br />

---

## What it does

```
URL  →  Live browser measurement  →  Structured tokens  →  DESIGN.md  →  Your AI agent
```

DesignMD opens the URL in a headless browser, measures the real visual system — colors from computed styles, typography from the cascade, breakpoints from live `@media` rules, hover/focus states from the CSSOM — and synthesizes a portable specification.

The output is the kind of file a senior engineer would actually use to rebuild the brand. Drop it into Cursor, Claude Code, Windsurf, Aider, Copilot, or paste it into any LLM chat. The model gets ground truth instead of guesses.

<br />

---

## Terminal usage

```bash
dmd <url>                  # stream DESIGN.md to stdout
dmd <url> --out=PATH       # write to a file
dmd <url> --json           # extract tokens only (no LLM call — instant, no quota)
dmd <url> --force          # bypass cache, re-extract from live page
dmd <url> --quiet          # suppress progress messages on stderr
dmd --help
dmd --version
```

### Common patterns

```bash
# Pipe into a project file
dmd stripe.com > ./design/stripe.md

# Send to clipboard
dmd https://linear.app | pbcopy

# Token-only extraction (machine-readable, free, instant)
dmd vercel.com --json | jq '.colors'

# Self-hosting / regional endpoint
DESIGNMD_API=https://my-designmd.internal dmd notion.so
```

`stdout` always carries the markdown (or JSON). Progress lines go to `stderr`, so pipes stay clean.

<br />

---

## AI workflow integration

The generated `DESIGN.md` is purpose-built for LLM context windows. Drop it in once; reference it from your agent's rules file.

### Claude Code

Add to your project's `CLAUDE.md`:

```markdown
When building any UI in this project, read @DESIGN.md before generating code.
Use the colors, typography, and spacing from that file exactly — do not invent
brand values.
```

### Cursor

Add to `.cursor/rules` (or `.cursorrules`):

```
Read DESIGN.md before writing UI code. Use its color palette, type scale,
and spacing values exactly. Every brand value should trace back to the file.
```

### Windsurf · Aider · Cline · Continue

Same pattern — every modern coding agent supports a project-root rules file. Reference `DESIGN.md` from it.

Full integration guide: [`docs/ai-workflows.md`](./docs/ai-workflows.md).

<br />

---

## Sample output

A snippet from [`examples/DESIGN-stripe.md`](./examples/DESIGN-stripe.md):

```markdown
## Color Palette & Roles

### Primary
- **Brand Indigo (#0a2540)** — Hero typography, primary footer surface
- **Stripe Purple (#635bff)** — Primary buttons, focus rings, link accents

### Surface
- **Pure White (#ffffff)** — Page background, card surface
- **Cool Mist (#f6f9fc)** — Secondary surface, alternating sections

### Typography
| Role    | Font      | Size | Weight | Line Height |
|---------|-----------|------|--------|-------------|
| Display | Sohne Var | 64px | 600    | 1.05        |
| H1      | Sohne Var | 40px | 600    | 1.15        |
| Body    | Sohne Var | 18px | 400    | 1.6         |
| Code    | Sohne Mono| 14px | 400    | 1.5         |

### Breakpoints (measured live)
- 480px · 600px · 768px · 880px · 1024px · 1200px · 1440px
```

Full file: [DESIGN-stripe.md](./examples/DESIGN-stripe.md) · [Live page](https://designmd.cc/benchmarks/stripe)

<br />

---

## More examples

Eight production sites, each measured live. Click a card for the full `DESIGN.md`.

Cards: Stripe ([DESIGN-stripe.md](./examples/DESIGN-stripe.md)), Linear ([DESIGN-linear.md](./examples/DESIGN-linear.md)), Vercel ([DESIGN-vercel.md](./examples/DESIGN-vercel.md)), Notion ([DESIGN-notion.md](./examples/DESIGN-notion.md)), Anthropic ([DESIGN-anthropic.md](./examples/DESIGN-anthropic.md)), Mercury ([DESIGN-mercury.md](./examples/DESIGN-mercury.md)), Figma ([DESIGN-figma.md](./examples/DESIGN-figma.md)), Airbnb ([DESIGN-airbnb.md](./examples/DESIGN-airbnb.md)).

A larger reference catalog — 56 measured sites across 13 categories — is live at [**designmd.cc/benchmarks**](https://designmd.cc/benchmarks).

<br />

---

## Why DESIGN.md

| Approach | Failure mode |
|---|---|
| Agent guesses from prompt | Hallucinates plausible-looking but wrong colors, fonts, spacing |
| Designer hand-documents tokens | Stale within weeks; doesn't scale |
| Screenshot → vision model | Loses structural information; treats decorative pixels as design intent |
| Static design-system catalog | Hand-curated, biased to designer aesthetics, doesn't match a real brand |

DesignMD measures live, then formalizes the measurement as a markdown spec that survives the round-trip into an LLM context window. The file is portable, diff-able, and re-generable when the source site evolves.

<br />

---

## Exit codes

The CLI uses distinct exit codes so scripts and agents can react correctly:

| Code | Meaning                                        |
| ---- | ---------------------------------------------- |
| `0`  | Success                                        |
| `1`  | User error (bad URL, unsupported flag, refused extraction) |
| `2`  | Transient — try again (rate limit, server busy, timeout)   |
| `3`  | Network error                                  |

<br />

---

## Rate limits

Anonymous use: **5 generations per day** per IP-bucket. The `--json` flag does not count against this — it skips the LLM step entirely and returns the raw token extraction.

Per-user API keys with higher quotas will arrive alongside account auth.

<br />

---

## Proprietary boundary

This repository is the **public developer surface**. It contains:

- Sample `DESIGN.md` outputs from the live catalog (`examples/`)
- FAQ and AI-coding-agent integration guide (`docs/`)
- UI screenshots (`screenshots/`)
- The CLI's published documentation (this README)

It does **not** contain:

- The extraction pipeline or browser instrumentation
- LLM prompts and synthesis logic
- Server source, rate-limiting, caching, or auth internals
- Schema definitions or operator tooling

For commercial licensing or production-access inquiries, reach out — [adityaraj.info](https://adityaraj.info).

<br />

---

## Environment

| Variable        | Default                  | Purpose                                    |
| --------------- | ------------------------ | ------------------------------------------ |
| `DESIGNMD_API`  | `https://designmd.cc`    | Override the API base URL (self-hosting)   |

<br />

---

## Contributing

This is a curated developer surface, not a fully open-source project. We welcome:

- Bug reports on [designmd.cc](https://designmd.cc) — open an issue here
- Benchmark suggestions — open an issue with a URL you want measured
- Documentation improvements in `docs/`
- Better sample examples — PRs against `examples/` welcome

For larger changes, open an issue first to discuss. See [CONTRIBUTING.md](./CONTRIBUTING.md).

<br />

---

## License

[MIT](./LICENSE) — covers the materials in this repository: the CLI source, sample `DESIGN.md` outputs, documentation, screenshots, and example thumbnails.

The MIT license does **not** extend to:

- The DesignMD production source code, automation, or infrastructure
- The token-extraction pipeline and prompts
- The DesignMD name, logo, and brand identity

<br />

---

## Acknowledgments

Built by [Aditya Raj](https://adityaraj.info). Thanks to the designers and engineers behind the modern web whose publicly accessible visual systems make benchmarking and design research possible.

<br />

<div align="center">

**[Try the live demo →](https://designmd.cc)** · **[Install the CLI →](https://www.npmjs.com/package/@designmdcc/cli)**

</div>

## Docs

### docs/ai-workflows.md — Using DesignMD output with AI coding tools

The `DESIGN.md` files produced by DesignMD are purpose-built for LLM context windows. Drop one into your project, reference it from your coding agent's rules file, and the assistant will build UI that matches the real design system of the source brand — colors, typography, spacing, all measured live.

#### Step 0 — generate the file

The fastest path is the CLI:

```bash
npx @designmdcc/cli stripe.com > DESIGN.md
```

Or, installed globally:

```bash
npm install -g @designmdcc/cli
dmd stripe.com > DESIGN.md
```

You can also paste a URL into [designmd.cc](https://designmd.cc) and download the result. Same output either way.

#### Claude Code

Project-level reference — add to your project's `CLAUDE.md`:

```markdown
# Design context

When building any UI in this project, reference the design specification at
@DESIGN.md.

That file contains the exact colors, typography, spacing scale, breakpoints,
and component patterns extracted from the source URL. Do not invent brand
values — read them from the file.
```

Per-task usage:

```
@DESIGN.md — build me a pricing card that matches the primary button style
and uses the body typography from §3.
```

#### Cursor

Add to `.cursor/rules` at project root:

```
Before writing any UI code:

1. Read DESIGN.md (in the project root).
2. Use its color palette, typography scale, and spacing values exactly.
3. Match the component patterns described in §4.
4. Do NOT infer brand styles — every value should trace back to the file.
```

Cursor loads this rule into every chat session in the project.

#### GitHub Copilot

Copilot reads open files. The pattern:

1. Keep `DESIGN.md` open in a sidebar tab.
2. Reference the spec in code comments — Copilot will suggest styles matching the spec.

#### Windsurf, Aider, Cline, Continue

Same pattern as Cursor — every modern AI coding tool supports a project-root rules file:

| Tool             | Config file                                      |
| ---------------- | ------------------------------------------------ |
| Cursor           | `.cursor/rules` or `.cursorrules`                |
| Windsurf         | `.windsurfrules`                                 |
| Aider            | `CONVENTIONS.md` or `.aider.conf.yml`            |
| Cline (VS Code)  | `.clinerules`                                    |
| Continue         | `~/.continue/config.json` → `customCommands`     |

#### Plain ChatGPT / Claude.ai web

If you're not in a coding tool:

1. Open the generated `.md` file in a text editor
2. Copy the entire contents
3. Paste as the first message in a new conversation, prefaced with instructions to use it as the design spec for all generated UI code
4. Then ask for components, screens, layouts, etc.

#### Best practices

- **Keep the file in the repo** — paste `DESIGN.md` content into the repository as a file rather than referencing a URL; AI tools work better with local file context.
- **Regenerate when the brand changes** — `dmd stripe.com --force > DESIGN.md` bypasses the cache and re-extracts from the live page.
- **Cite the source in PRs** — reference the extraction date/source in PR descriptions for auditability.
- **Mix and match** — multiple `DESIGN.md` files can be used in the same project (e.g. Stripe's button styling + Linear's typography).

#### Examples in this repository

See `/examples` for 8 production `DESIGN.md` outputs covering: Fintech (Stripe, Mercury), AI (Anthropic), Productivity (Linear, Notion), Hosting (Vercel), Design tools (Figma), Consumer (Airbnb).

### docs/faq.md — FAQ

**What is DesignMD?** A platform that measures the design systems of production websites and turns them into structured, AI-ready specifications. Paste any URL, get back a `DESIGN.md` file with the real color palette, typography, spacing, and component patterns extracted from the live page.

**How do I use it?** Three ways: CLI (`npx @designmdcc/cli stripe.com > DESIGN.md` or `npm install -g @designmdcc/cli` then `dmd <url>`), Web (paste a URL into designmd.cc), or Catalog (browse pre-generated benchmarks for 56 well-known sites).

**Is this an open-source project?** The CLI source and showcase materials in this repository (sample outputs, documentation, screenshots) are MIT-licensed. The production source code — extraction pipeline, prompts, server, automation — is proprietary and not published here.

**How accurate are the extractions?** Every signal is sourced from the live DOM and CSSOM at extraction time. Colors from computed-style sampling, typography from the cascade, breakpoints from `@media` rule enumeration, hover states from CSSOM pseudo-class traversal. The LLM stage is a formatter, not a value inventor. Some extractions are imperfect (WebGL-heavy pages may time out, obscure CSS-in-JS frameworks may obscure variable names); the extracted JSON is ground truth, the rendered markdown a presentation layer.

**Why these 56 sites?** Curated for category coverage, design quality, recognizability, and comparison value (direct competitors in the same category).

**Can I get a DESIGN.md for my own site?** Yes — `dmd yourdomain.com` or paste at designmd.cc. Free tier rate-limited to 5 generations/day per IP-bucket.

**How does this differ from existing design-system catalogs?** Most catalogs (Awwwards, Land-book) are inspiration galleries — hand-curated screenshots with editorial commentary. DesignMD is a measurement layer — every page is parsed by an actual browser, every value measured, every export structured for machine consumption. Intended for AI coding agents seeking ground truth, not designers seeking inspiration.

**Will sites change over time?** Yes — each benchmark is stored in a version-tagged directory. Re-running the extractor produces a new version. Roadmap includes token-diff visualization.

**What about privacy?** Reads only public-web pages — no login, no cookie-jar, no scraping of authenticated content. URLs resolving to private IPs are blocked at the URL-guard layer.

**Cost / commercial use?** Live site and CLI free within the per-day rate limit. Commercial use of generated `DESIGN.md` outputs permitted under the MIT license attached to repo materials. The platform itself (production code, automation, hosting) is not commercially licensed.

## Top-level structure
- `.gitignore` — standard ignore file
- `CONTRIBUTING.md` — contribution guidelines
- `LICENSE` — MIT license
- `README.md` — project README (captured above)
- `assets/` — logo image
- `docs/` — `ai-workflows.md`, `faq.md` (captured above)
- `examples/` — 8 sample `DESIGN-<site>.md` outputs (Stripe, Linear, Vercel, Notion, Anthropic, Mercury, Figma, Airbnb) plus matching screenshot thumbnails and a README
- `screenshots/` — UI screenshots (not fetched)
