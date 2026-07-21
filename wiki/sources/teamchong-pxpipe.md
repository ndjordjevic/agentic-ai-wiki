---
type: source
category: "Knowledge, RAG, memory & context"
source_url: https://github.com/teamchong/pxpipe
tags:
  - token-optimization
  - context-compression
  - claude-code
  - vision-channel
  - proxy
  - prompt-caching
  - model-profiling
related:
  - nadimtuhin-claude-token-optimizer
  - mksglu-context-mode
  - chopratejas-headroom
  - rtk-ai-rtk
product: pxpipe
detail_level: standard
created: 2026-07-21
updated: 2026-07-21
---

pxpipe is a TypeScript local proxy for AI coding workflows that converts bulky request context (system/tool docs, older history, large tool results) into dense PNG pages before forwarding to model APIs, aiming to reduce input-token cost while keeping the same operational flow for agent clients. The project is unusually explicit about tradeoffs: it treats dense image context as lossy for exact-string recall, keeps precision-critical identifiers in adjacent text/factsheet channels, and positions savings claims around measured request-level baselines rather than headline-only percentages.

_All claims below are sourced from ../../raw/github/teamchong-pxpipe.md unless otherwise noted._

## What it does

pxpipe sits between an agent client and the upstream model endpoint, intercepting request payloads and rewriting selected high-token text blocks into image content whose cost depends on pixel area rather than source character length. It targets token-dense payloads (tool output, long static prefixes, older conversation chunks), preserves recent/live state in text, and logs per-request measurements so teams can compare transformed requests against text counterfactuals.

## Installation

Quick-start usage is `npx pxpipe-proxy`, then pointing the client (for example Claude Code) at the local proxy URL via `ANTHROPIC_BASE_URL=http://127.0.0.1:47821`. The repository also documents offline export mode (`pxpipe export`) for generating PNG context pages without running an active proxy.

## Key features

- Request-side context imaging with model-specific render profiles.
- Dashboard for live savings/transform inspection and runtime controls.
- Profitability gate intended to avoid imaging when sparse prose would cost more.
- Per-request baseline math (`count_tokens` counterfactual) and event logging in `~/.pxpipe/events.jsonl`.
- Multi-model opt-in policy (defaulting to `claude-fable-5`, with Sol/Grok/Opus variants explicitly gated).
- Library APIs for embedding transformations without running the CLI proxy.

## Architecture

The repo structure points to a modular pipeline: `src/core/` houses transform/measurement/baseline logic, while runtime entrypoints (`node.ts`, `worker.ts`) and dashboard/session/stats modules compose operational interfaces around that core. Documentation (`docs/CACHING_AND_SAVINGS.md`, `docs/NOT-OCR.md`, `docs/MODEL_RENDER_PROFILES.md`) ties implementation details to explicit mathematical accounting and model-readability constraints, reflecting a design where compression behavior, billing math, and quality risk are treated as first-class system boundaries.

## Example usage

```bash
npx pxpipe-proxy
ANTHROPIC_BASE_URL=http://127.0.0.1:47821 claude
```

For offline context rendering:

```bash
pxpipe export src/
cat prompt.txt | pxpipe export --stdin
pxpipe export --git
```

## Maintenance status

As of this ingest, the repository is active (`pushedAt: 2026-07-21`), uses an MIT license, and has a tagged latest release `v0.7.1` (2026-07-03). The project exposes an extensive test surface (`tests/` includes cache alignment, transform behavior, provider routing, API bridges, and E2E checks), and accompanying docs/eval folders show ongoing benchmarking and methodology updates.
