# teamchong/pxpipe

## Metadata
- Stars: 6552
- Primary language: TypeScript
- Default branch: main
- Latest release: v0.7.1 (2026-07-03)
- License: MIT License
- Homepage: (none)
- Fetched: 2026-07-21
- Final URL: https://github.com/teamchong/pxpipe

## Description
cut Fable 5 token usage by rendering text context as images

## README
# pxpipe

**Cut Claude Code's input tokens by rendering bulky context as images — the same system prompt, tool docs, and history, in a fraction of the tokens.**

An image's token cost is fixed by its pixel dimensions, not by how much text
is inside it. Dense content (code, JSON, tool output) packs ~3.1 chars per
image-token vs ~1 char per text-token on real Claude Code traffic. The
reader is the same vision channel that Anthropic's computer use already
relies on for screenshots. pxpipe is a local proxy that uses that channel
for context: it rewrites the bulky parts of each request into compact PNGs
before it leaves your machine. At current Fable
list prices that lands as a **~59–70% lower end-to-end bill** — but prices
move and workloads differ, so the durable number is the token cut itself,
measured per-request against a free `count_tokens` counterfactual in
`~/.pxpipe/events.jsonl`.

This is what the model sees instead of text:

![example: a real `transformRequest` output: system prompt + tool docs reflowed into one dense page, instruction banner on top, ↵ marking original newlines](https://raw.githubusercontent.com/teamchong/pxpipe/main/docs/assets/example-render.png)

*~48k chars of system prompt + tool docs: ≈25k tokens as text, ≈2.7k image
tokens as this page. Real pipeline output; the model reads renders like this
at 100/100 (see benchmarks).*

![chart: characters a frontier context window holds, 2018–2026 — vendor text series including Grok 4.5; orange measured overlay is Fable 5 [1m] + pxpipe ~18M (4.6×)](docs/assets/context-window-chars.png)

*Eight years of context growth, in characters. Every text line tops out near
~4M chars (a 1M-token window at ~4 chars/token); **Grok 4.5** is shown as a
text-window point only (500K). The orange overlay is the **same Fable 5 1M
window** read through pxpipe images — ~18M chars at the measured Anthropic
density (**4.6×** the text ceiling). Density is measured from a live render at
generation time, not hand-typed: regenerate with
`npx tsx scripts/gen-context-chart.ts`
([source](scripts/gen-context-chart.ts)).*

## Demo

**Fable 5 (the default, 100/100 reader) — plain left, pxpipe right:**

https://github.com/user-attachments/assets/1c8ee63a-fcd7-4958-917b-da788d718349

pxpipe counts an exact token **10/10** across 39 imaged filler files
(matches `grep` line-for-line), gets the multi-step ledger arithmetic right,
and ends the session at **$6.06** with context to spare (73.5k/1M) vs
**$42.21** at 96% full. One caveat visible in the clip: the pxpipe arm
needed a nudge to match the requested one-line output format.

**Opus 4.8 (disabled by default) — same layout:**

https://github.com/user-attachments/assets/f4e50137-31b5-426f-a6ed-b83f829b4a2c

Text needles read fine on both arms; the imaged phrase-count doesn't read on
Opus — and pxpipe **says so instead of fabricating a number**. That misread
rate is why Opus is opt-in.

## Try it (30 seconds)

```bash
npx pxpipe-proxy                                  # proxy on 127.0.0.1:47821
ANTHROPIC_BASE_URL=http://127.0.0.1:47821 claude  # point Claude Code at it
```

Dashboard at <http://127.0.0.1:47821/>: tokens saved, every text→image
conversion side by side, kill switch, live model chips. Responses stream
normally — pxpipe compresses the *request* only, never the model's output.
Recent turns stay text; the system prompt, tool docs, and older bulk history
are imaged.

## Offline export (no proxy)

You can render text, files, or diffs to PNG pages without running the proxy or
connecting Claude Code:

```bash
pxpipe export src/
cat prompt.txt | pxpipe export --stdin
pxpipe export --git
```

Each run writes a fresh `pxpipe-export-XXXXXX/` output folder (the exact path
is printed when the command finishes) containing `page-*.png`, `factsheet.txt`,
`manifest.json`, and `prompt.txt`. Upload the PNG pages and paste the prompt
into image-upload clients such as Cursor when you want dense visual context
without running the proxy.

## The honest part

- **It is lossy.** Exact 12-char hex strings in dense imaged content:
  **13/15** on Fable 5, **0/15** on Opus, and **0/15** on Sol — misses are *silent
  confabulations*, not errors. Byte-exact values (IDs, hashes, secrets)
  must stay text; recent turns do. A dedicated verbatim-risk guard is not
  built yet.
- **Escape hatch:** subagents on non-allowlisted models pass through as
  text — route byte-exact work there
  (`CLAUDE_CODE_SUBAGENT_MODEL=claude-sonnet-4-6`, or `model: sonnet` in
  agent frontmatter).
- **Real work:** SWE-bench Lite pilot **10/10 both arms** at −65% request
  size; SWE-bench Pro **14/19 ON vs 15/19 OFF** at −60%, verdicts agree
  18/19, and the single split re-resolved 3/3 on replication — run-to-run
  variance, not compression. Small n; receipts in `eval/`.
- **Workload-dependent.** Wins on token-dense content (~1 char/token),
  loses money on sparse prose (~3.5 chars/token); a profitability gate
  (calibrated on N=391 production rows) images only where the math wins.
- **Client-dependent.** Savings track uncached bulk the client still
  re-sends as text. Claude Code re-sends system + tools + history on
  `/anthropic/messages` and typically lands ~60–70%. Details and measured
  splits: [docs/CACHING_AND_SAVINGS.md](docs/CACHING_AND_SAVINGS.md).
- **Model scope:** default `PXPIPE_MODELS=claude-fable-5`. Sol, Opus
  4.7/4.8, GPT 5.5, and **Grok** are opt-in only (dashboard chips or
  `PXPIPE_MODELS`) — not good enough as silent defaults for imaged context.
- **Per-model rendering:** opt-in `gpt-5.6-sol` uses a 152-column,
  5×8 Spleen profile; Claude keeps its 312-column 5×8 Spleen profile.

## Benchmarks (reproducible)

The README reports benchmark suites for novel arithmetic, gist recall, state tracking, confabulation checks, and verbatim hex recall across Claude Fable, GPT-5.6 Sol, Grok 4.5, Opus 4.8, and Kimi K3, with links into `eval/` for receipts and methodology.

## How it works

```
model id ──► render profile ──► wrap/reflow bulk context ──► PNG[] + exact-token factsheet
```

The proxy intercepts `/v1/messages`, rewrites eligible bulk into image
blocks, splices them back cache-friendly (static prefix preserved, prompt
caching keeps working), and forwards. Every enabled model gets the same
production stack: 5×8 Spleen pages, in-image IDS block, and adjacent text
factsheet. Events log to `~/.pxpipe/events.jsonl`.

## Library use (no proxy)

```ts
import { renderTextToImages, transformAnthropicMessages } from "pxpipe-proxy";

const { pages } = await renderTextToImages(toolResultText);
const { body, applied, info } = await transformAnthropicMessages({
  body: requestBytes,
  model: "claude-fable-5",
});
```

## Development

```bash
pnpm install && pnpm test
pnpm run build
```

## Limitations

- Lossy for exact-string recall from dense image blocks.
- PNG encoding adds latency before upstream request forwarding.
- ASCII/Latin-1 are best-tested; CJK is handled conservatively.

## Roadmap

Rendering optimization is intentionally constrained by measured vision-readability limits; the repo emphasizes model-by-model reevaluation and practical guardrails rather than claiming lossless OCR-equivalent behavior.

## Community projects

- [pxpipe-windows](https://github.com/DivyeshPatro/pxpipe-windows)
- [OmniGlyph](https://github.com/diegosouzapw/OmniGlyph)

## License

MIT.

## Docs

### docs/CACHING_AND_SAVINGS.md
# Prompt-Caching Alignment And Honest Savings Math

This document details two core implementation guarantees: (1) cache-aligned rewrite behavior against Anthropic prompt caching semantics; (2) "honest savings" accounting that avoids counting provider prompt-cache discounts as pxpipe-generated savings. It identifies `src/core/transform.ts` and `src/core/baseline.ts` as implementation sources of truth and documents formulas for warm/cold baseline comparisons and effective token-cost calculations.

### docs/NOT-OCR.md
# Not OCR: how models read renders, and why that changed with Fable 5

This document explains pxpipe's key model-behavior claim: VLM image reading is not OCR (patch embeddings + language-prior decoding), so dense exact-string recall can fail silently while semantic gist can still be high. It includes evaluation comparisons (e.g., Opus 4.8 vs Fable 5) and argues that practical viability shifted with newer model generations rather than with rendering trick changes alone.

### docs/MODEL_RENDER_PROFILES.md
# Model render profiles

This document maps rendering profiles by model-id family (`claude-fable-5*`, `gpt-5.6-sol*`, `grok-*`, other GPT/o-series), including cell/font geometry and max-height settings, and describes profile override mechanics via `PXPIPE_GPT_PROFILES`.

## Top-level structure
- `.github/` — repository automation/config files.
- `assets/` — static media and generated visual assets.
- `bench/` — benchmark harnesses and scripts.
- `bin/` — executable entrypoints and command wrappers.
- `demo/` — demo assets and scripts.
- `docs/` — technical design notes (caching math, render profiles, legibility, routing).
- `eval/` — evaluation receipts, datasets, and quality/savings result artifacts.
- `scripts/` — utility and chart-generation scripts.
- `src/` — implementation code:
  - `core/` — transformation, measurement, baseline accounting, proxy primitives.
  - `dashboard/` and `dashboard.ts` — local dashboard server/UI glue.
  - `worker.ts` / `node.ts` — runtime-specific entry paths.
  - `export-collect.ts`, `sessions.ts`, `stats.ts` — export/session/statistics support.
- `tests/` — comprehensive automated test suite (cache alignment, transforms, model routing, history handling, API bridges, dashboard APIs, regression/e2e).
- `README.md`, `CHANGELOG.md`, `FINDINGS.md`, `LICENSE`, `package.json`, `pnpm-lock.yaml`, `pnpm-workspace.yaml`, `tsconfig.json`, `vitest.config.ts`, `wrangler.toml` — repo metadata and build configuration.
