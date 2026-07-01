# getcaveman.dev

## Fetch log
- Inbox URL: https://getcaveman.dev/
- Final URL: https://getcaveman.dev/
- Fetched: 2026-07-01
- Pages: 6
- Mode: standard

## Landing page — https://getcaveman.dev/

Caveman — the token-efficient stack for agent-native development

# Cut 65% of your tokens.

Install Caveman (4 ways):
- Claude Code skill: `curl -fsSL https://raw.githubusercontent.com/JuliusBrussee/caveman/main/install.sh | bash`
- Caveman Code: `npm install -g @juliusbrussee/caveman-code`
- Cavemem: `npm install -g cavemem`
- Browser extension: ChatGPT · Claude · Gemini

Join the Cloud waitlist — byte-safe gateway · verified savings

74k on GitHub · #1 on Hacker News

≈35% kept · 65% cut

Starred by engineers at: OpenAI, Microsoft, Vercel, Cloudflare, IBM, Netflix, Siemens, Huawei, Instacart, Bluesky, Google, LinkedIn, Uber, Shopify, ByteDance, Booking.com

Why use many token when few token do trick.

## Five layers. Every token earns its place.

01 coming soon — **Caveman Gateway** — Compress any LLM traffic.
- Swap one base URL — your agents never change
- Truthful spend, metered token-for-token
- Byte-safe: record mode never touches what the model sees
- Example: prompt tokens 4,210; cached prefix reused 2,890; billed to you 1,320; model-visible bytes unchanged; −69% billed

02 — **Cavemem** — Agents that stop forgetting.
- One persistent recall layer, served over MCP
- Local SQLite with FTS5 and a vector index
- Pull back what matters instead of re-sending it
- `npm install -g cavemem`

03 — **Caveman Code** — A terminal agent on a token budget.
- Four compression layers across 20+ providers
- Plan first, then ship — one autonomous loop
- Same models, roughly half the tokens
- `npm install -g @juliusbrussee/caveman-code` (v0.19.1)

04 — **Cave Architect** — Telemetry becomes a ranked plan.
- Measured spend turns into ordered moves
- Each move carries its own dollars-per-day
- Split by how much app change it costs you (S0 zero app change, S1 SDK cooperation, S2 eval-gated routing)

05 — **Eval-Gated Rollout** — Savings you actually earned.
- Clears replay, shadow and canary before live
- Gated on evals — nothing counts until it passes
- Auto-reverts the moment quality slips

Truthful spend, down to the byte. See exactly where every token goes, priced to the cent.

## Don't code? Caveman help anyway.

Lives in your chat box: ChatGPT, Claude, Gemini (browser extension).

## The proof is public.

Every number here is live and cited — held to the same honesty we hold our own metering to.
- 74k GitHub stars, live
- #1 Hacker News & GitHub Trending
- Top 220 of every public repo on GitHub
- Top 50 of every skill on skills.sh
- As seen on: Hacker News, Trendshift, BNR Nieuwsradio, Leiden University, HyperAI, daily.dev

## Fewer words. Same work.

The open stack is public today — read the source, send a patch. The managed Cloud is in private development; leave your email and we'll reach out the moment a spot opens.

Products nav:
- Compression: Caveman, CaveGemma
- Agent toolkit: Caveman Code, Cavemem, Cavekit
- Cloud: Caveman Proxy (soon), Caveman Cloud waitlist

Contact: contact@caveman.so · MIT · 2026

## Docs — https://getcaveman.dev/docs

Overview · Caveman Cloud

# Public Caveman docs

These pages cover the public, local Caveman stack: the compression engine, standalone proxy, CLI, SDKs, MCP tools, browser extension, memory, kit, and shrink tools. Everything here builds from the public source in this repo, runs on your machine, and labels local numbers as `inferred`.

The caveman skill changes how an agent answers. The stack documented here changes what an agent sends: tool output, logs, code, diffs, search results, memory recall, and tool catalogs can be compressed before they reach a model.

The public rule is simple: local, single-operator, BYOK tools report `inferred` results. They do not certify savings, do not claim hosted rollout proof, and do not need an account.

## Start here

- Quickstart — Install the skill, compress a payload, and wrap an agent in five minutes.
- Architecture — How engine, proxy, CLI, SDKs, and MCP tools fit together.
- Honesty rules — Why local output stays inferred, recoverable, and conservative.
- Licensing — MIT packages, BSL packages, and the hosted-service restriction.

## What's in the box

| Component | What it does | License |
| --- | --- | --- |
| Compression engine | Detects content type and routes it to a safety-classed compressor | BSL 1.1 |
| Proxy | Base-URL-swap reverse proxy that meters truthful spend | BSL 1.1 |
| cave CLI | Builds local binaries, wraps agents, delegates to the proxy and engine | MIT |
| TypeScript SDK · Python SDK | The same gateway contract, in two languages | MIT |
| MCP server | Compression and retrieval as Model Context Protocol tools | BSL 1.1 |
| Cavemem · Cavekit · Shrink | Local memory, provenance UI, and tool-catalog compression | mixed |
| Browser extension | Caveman Mode in the chat box of ChatGPT, Claude, and Gemini | MIT |

## The number

A committed tool-output JSON fixture currently compresses like this: 16,098 → 1,091 tok (−93% inferred). Sixteen thousand inferred tokens down to about eleven hundred. Dropped detail is recoverable through a content-addressed handle. This is a local engine measurement, not a billing claim.

Install names aren't live yet — public binaries and packages build from source here. The live one-line install is the skill: `curl -fsSL …/install.sh | bash`.

## Quickstart — https://getcaveman.dev/docs/quickstart

# Quickstart

Start with the skill if you only want shorter replies. Build the engine and proxy if you want local input-side compression and spend metering. Both paths are local; provider keys stay with you.

## 1 — The skill (works now)

```bash
curl -fsSL https://raw.githubusercontent.com/JuliusBrussee/caveman/main/install.sh | bash
```

## 2 — Build the engine and proxy

```bash
go build -o ./bin/caveman-engine ./public/engine/cmd/caveman-engine
go build -o ./bin/caveman-proxy ./public/proxy/cmd/caveman-proxy
```

Full code compression needs cgo for tree-sitter (Python, JS/TS). JSON, logs, diffs, search results, and text use the same compressors either way.

## 3 — Compress something

```bash
echo '{"items":[{"id":1,"status":"ok"},{"id":2,"status":"ok"},{"id":3,"status":"ok"}]}' \
  | ./bin/caveman-engine compress
```

On a real tool-output sample the engine turns sixteen thousand tokens into about eleven hundred: 16,098 → 1,091 tok (−93% inferred). If compression emits a recovery handle, `caveman-engine retrieve <handle>` returns it byte-for-byte.

## 4 — Put an agent behind the proxy

```bash
ANTHROPIC_API_KEY=sk-ant-… ./bin/caveman-proxy
export ANTHROPIC_BASE_URL=http://127.0.0.1:8787
```

The cave CLI automates this: `caveman start` launches the proxy; `caveman wrap claude` starts a wrapped agent with the right base URL.

Honesty rule: Default `record` mode is pass-through. `compress` mode only runs when explicitly enabled and falls back to the original bytes on any problem. Local spend and compression output are `inferred`, never `verified`.

## Architecture — https://getcaveman.dev/docs/architecture

# Architecture

One engine does detection, compression, token counting, and recovery. Public front ends call that engine instead of carrying their own compressor. The proxy adds routing and local spend rows around provider traffic.

## One core, many front doors

| Front door | What it adds over the engine |
| --- | --- |
| caveman-engine CLI | stdin/stdout + a JSON report |
| Proxy | routes provider traffic and writes local `inferred` spend rows |
| MCP server | the engine as three Model Context Protocol tools |
| Cavemem · Shrink | memory and tool-catalog compression on top |
| SDKs | gateway client methods; `compress()` delegates instead of reimplementing |

## The request path

When the proxy is in the loop, provider traffic runs through five steps: Agent base-URL swap → caveman-proxy (127.0.0.1:8787) → match/auth/transform (byte-safe)/meter → Provider BYOK upstream → response bytes intact → ~/.caveman/caveman.db inferred spend SQLite.

In `record` mode it never transforms. On transform failure it forwards the original bytes.

## The safety ladder

Each transform declares a safety class, S0 through S4.
- S0-S3: metadata, additive hints, reorder, structural changes guarded by policy
- S4: lossy; engine compressors sit here; S4 `RequiresCCR` — lossy result emitted only after original stored for byte-exact recovery

## Public boundary

Public local tools are single-operator and BYOK. They report `inferred` measurements. Hosted proof, billing, and tenant governance are outside these public docs.

Commercial side: Cloud, Enterprise, OEM — verified savings, eval-gated rollout.

## Fail-closed by construction

Unknown inputs take the conservative path: unknown mode → `record`; low-confidence content → `text`; unknown grader → `passed: false`; unknown proxy route → 404; unknown model price → zero + `unpriced:` tag.

## Honesty rules — https://getcaveman.dev/docs/honesty

# Honesty rules

Compression docs get useless fast when estimates are sold as proof. Public Caveman tools avoid that: local counts stay `inferred`, pass-through beats risky transforms, and lossy output is recoverable.

## Three words, kept apart

- `inferred` — local estimate from bytes, token counters, and local records. Public offline tools emit this.
- `measured` — observed traffic, not proof of a saved dollar.
- `verified` — proof label reserved for hosted rollout systems, not emitted by local public tools.

## The four rules

1. **No fake savings** — Headline figures stay labeled `inferred`; not multiplied into monthly savings.
2. **Byte-safe** — `record` mode is pass-through. On parse problems, unsupported inputs, missing recovery store, or not-smaller output, keep original bytes.
3. **No placeholders, fail closed** — Unknown cases fail toward conservative answers.
4. **Recoverable, so lossy stays honest** — Lossy result emitted only after original stored under content-addressed handle. `Retrieve(handle)` returns original byte-for-byte.

## The proxy — https://getcaveman.dev/docs/proxy

# The proxy

Point an agent at `http://127.0.0.1:8787` and provider traffic runs through the standalone Caveman proxy. Single-operator, BYOK, and local. Default mode records traffic without changing request bodies.

## Base-URL swap, nothing else

```bash
go build -o ./bin/caveman-proxy ./public/proxy/cmd/caveman-proxy
ANTHROPIC_API_KEY=sk-ant-… ./bin/caveman-proxy
export ANTHROPIC_BASE_URL=http://127.0.0.1:8787
```

The cave CLI wraps both halves: `caveman start` launches the binary and `caveman wrap <agent>` starts a supported agent with the right environment.

## The request lifecycle

Every request runs five steps: Match (route → provider adapter; unknown → 404) → Authenticate (env key first, else pass-through inbound auth header) → Inspect & transform (byte-safe; `record` = no transform; `compress` falls back on any problem) → Upstream (SSRF-guarded client) → Meter (local SQLite, `inferred` basis).

Provider adapters live under `public/proxy/providers`. Standalone records `Basis: "inferred"` on every spend row; never writes `verified`.
