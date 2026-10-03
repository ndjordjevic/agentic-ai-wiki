# tamaratran/fast-jev-compaction

## Metadata
- Stars: 7341
- Primary language: TypeScript
- Default branch: main
- Latest release: none found
- License: MIT License
- Homepage: (none)
- Fetched: 2026-10-03
- Final URL: https://github.com/tamaratran/fast-jev-compaction

## Description
Claude Code plugin that replaces the compaction summary with Jev decisions: every tool call and result is scored in one fast request, stale ones are dropped or truncated, everything kept stays verbatim.

## README
# fast-jev-compaction

Claude Code plugin that replaces the compaction summary with Jev decisions:
every tool call and result is scored in one fast request, stale ones are
dropped or truncated, everything kept stays verbatim. Also usable as an npm
library.

## What and why

Most context compaction asks an LLM to summarize old turns. A summary is
lossy: a file path, exact error, constraint, or command can disappear even when
it matters later. This library never rewrites anything. It only deletes tool
calls and tool results Jev says are no longer needed, and it asks Jev while
showing it the whole conversation. User and assistant text stays verbatim and
in order.

The repository is both an npm package (`src/`) and a Claude Code plugin
(`hooks/`, `.claude-plugin/`) that uses the package to replace Claude Code's
built-in compaction summary with the original messages.

## How it works

1. Every `tool_use` is paired with its `tool_result` by `tool_use_id`. Calls in
   the first message or in the newest `preserveRecentMessages` messages are
   pinned and never touched.
2. The **state** sent to Jev is the whole conversation so far, oldest first,
   with every tool result replaced by a short note (`ok, 4213 chars (omitted)`).
   Tool inputs are included, texts are included, nothing is summarized.
3. The state is fitted into `maxStateTokens` (25k by default) in stages, each
   applied only if the previous one was not enough: tool inputs truncated to
   1000, then 200, then 60 characters; long texts abridged to head + tail,
   oldest non-pinned messages first; old non-pinned messages collapsed to a
   `[… N chars omitted …]` note; old tool calls reduced to one line each
   (`t12 Read file_path=src/a.ts → ok 480ch`); old call-less messages left
   out; runs of old call-only messages folded into one entry. If it still
   does not fit, compaction throws. Tokens are estimated without a tokenizer (a
   word per six letters, half a token per digit, ~one per other symbol),
   calibrated to land a little above the counts Jev reports.
4. For every non-pinned call Jev gets two `noul` questions: should the **call**
   stay (knowing it was made, with its input, still matters), and should the
   **result** stay verbatim (its contents are still needed and re-running the
   tool would not do).
5. Questions are split into as many requests as needed so state plus questions
   stays under `maxRequestTokens` (30k by default, under Jev's 32k request
   limit). The same full state is resent with every request; requests run
   concurrently and their answers are merged.
6. Decisions per call, against `keepThreshold`:
   - `keepResult ≥ threshold` → keep call and result;
   - else `keepCall ≥ threshold` → keep the call, truncate the result to its
     first `truncateHeadChars` characters plus a one-line note;
   - else → remove the call together with its result.
7. The message list is rebuilt: a message that loses all its content is
   removed, untouched messages are returned as the same objects, and no result
   is ever left without its call.

Jev failures, malformed answers, a missing key, or a history that cannot be
fitted throw; the caller (or the Claude Code hook) decides what to fall back to.

## Install and usage

```sh
npm install fast-jev-compaction
export TYPESAFE_API_KEY=...
```

```ts
import { compactMessages, reductionRatio, type Message } from 'fast-jev-compaction';

const transcript: Message[] = [
  { role: 'user', text: 'Fix the failing test. Never edit src/generated.', toolUses: [] },
  {
    role: 'assistant',
    text: '',
    toolUses: [{ tool_use_id: 'toolu_1', tool: 'Read', input: { file_path: 'src/a.ts' } }],
  },
  { role: 'user', text: '', toolUses: [], toolResults: [{ tool_use_id: 'toolu_1', text: '…file…' }] },
  // …
];

const result = await compactMessages(transcript, { preserveRecentMessages: 4 });
console.log(result.messages, result.decisions, result.stats);
if (reductionRatio(result) < 0.25) {
  // not worth it: keep the original transcript, or summarize instead
}
```

`Message` is a subset of Claude Code's `SessionMessage`, so a session transcript
can be passed in as is.

To bring your own transport, implement `JevAsker` (one `ask(state, questions)`
method) and call `compact(messages, asker, options)`; `buildJevRequest` and
`parseJevResponse` give you the HTTP request body and response validation.
The building blocks (`collectToolCalls`, `fitState`, `batchCalls`,
`decideCall`, `applyDecisions`) are exported too.

`apiKey` defaults to `process.env.TYPESAFE_API_KEY`. Never commit the key or
put it in a source file.

## Options

| Option | Default | Description |
| --- | --- | --- |
| `apiKey` | `TYPESAFE_API_KEY` | TypeSafe API key (`compactMessages`/`JevClient`) |
| `model` | `jev-latest` | Jev model name |
| `baseUrl` | `https://api.typesafe.ai/v1/systemone` | System One endpoint |
| `fetch` | native `fetch` | Injectable fetch implementation for tests |
| `goal` | last 3 user prompts | Ongoing task description included in the state |
| `keepThreshold` | `0.5` | Minimum keep probability for a call or result to stay |
| `preserveRecentMessages` | `6` | Newest messages never touched (the first is always kept) |
| `maxStateTokens` | `25000` | Estimated token ceiling for the state |
| `maxRequestTokens` | `30000` | Estimated ceiling for state plus one batch of questions |
| `truncateHeadChars` | `300` | Characters of a dropped tool result retained before its note |

`result.stats` reports message and character counts before and after, the
per-reason decision counts, the state size in estimated tokens, which fitting
stage was needed, and the number of requests.

## Limitations

- Only tool calls and results are candidates; text messages are never removed
  or shortened in the output (they are only abridged in the state Jev sees).
- Token sizes are estimates from character counts, not a tokenizer.
- Calibration is at the request level; a probability is not a proof that a
  result is safe to delete. The assistant can always re-run the tool.
- The full state is repeated with every request, so a history near the state
  ceiling costs one request per handful of questions.

## Claude Code plugin

The repository root is a Claude Code function-hook plugin: `hooks/fast-jev.ts`
is a thin adapter that feeds `session.compact` transcripts through `src/` and
falls back to Claude Code's built-in summary on errors or insufficient
reduction. See [`hooks/README.md`](hooks/README.md) for configuration and the
Claude Code 2.1.274 type reference.

### Install in Claude Code

Function hooks are an early-access Claude Code feature (2.1.274+), so the
opt-in flag must be set wherever Claude Code runs, e.g. in `~/.claude/settings.json`:

```json
{ "env": { "CLAUDE_CODE_ENABLE_FUNCTION_HOOKS": "1", "TYPESAFE_API_KEY": "<your key>" } }
```

Then add this repository as a plugin marketplace and install the plugin,
either from the shell or as slash commands inside a session:

```sh
claude plugin marketplace add tamaratran/fast-jev-compaction
claude plugin install fast-jev-compaction@fast-jev-compaction
```

The install prompts for the plugin options (API key, thresholds, `truncateHeadChars`,
…); leave them at their defaults to use `TYPESAFE_API_KEY` from the environment.
Restart Claude Code or run `/reload-plugins`. From then on `/compact` (and
auto-compaction) goes through Jev: the toast reads
`fast-jev-compaction: kept N/M messages, no summary (…)` when the pruned history
replaced the built-in summary, or `fallback to built-in summary (…)` when Jev
could not remove enough (short sessions, or when it fails).

To run from a checkout without installing: `CLAUDE_CODE_ENABLE_FUNCTION_HOOKS=1 claude --plugin-dir .`
from the repository root. No publishing step is required; the marketplace is
just the repo's `.claude-plugin/marketplace.json`.

## Development

```sh
npm install
npm run typecheck        # library + hook
npm test
npm run build
npm run validate:plugin  # claude plugin validate
TYPESAFE_API_KEY="$(cat ~/.typesafe_key)" npm run demo
```

The unit tests use a fake Jev and never contact TypeSafe. The demo is the live
network check.

## Animated demo (macOS)

`demo/JevDemo` is a small native SwiftUI app that plays a scripted, dramatized
version of the compaction flow inside a Claude Code-style terminal: the tool
calls of a canned transcript are scored, results and calls Jev lets go turn red
and collapse away, and the rest stays verbatim. It never calls the API; it
exists to be screen recorded.

```sh
demo/JevDemo/build.sh   # builds demo/JevDemo/build/JevDemo.app and launches it
```

Press space in the app to replay from the start.

## Docs

### hooks/README.md

# fast-jev-compaction Claude Code mod

This plugin uses Claude Code function hooks to replace a compaction with the
original messages, minus the tool calls and tool results Jev judged no longer
needed. `hooks/fast-jev.ts` is a thin adapter: it reads the plugin options,
finds the TypeSafe key, hands `session.compact` transcripts to the
`fast-jev-compaction` library in `src/` (the plugin folder is the repository
root, so the hook imports it directly) and maps the result back onto session
messages. User and assistant text is never touched. Jev is sent the whole
conversation as `state` (tool outputs replaced by a one-line note) and, for
every tool call outside the pinned first and newest messages, two questions:
whether the call should stay and whether its full output should stay. An
item is kept when Jev's probability reaches `keepThreshold`; a dropped result
is truncated to its first `truncateHeadChars` characters plus a one-line note,
and a dropped call disappears with its result.

The state is fitted into `maxStateTokens` in stages: tool inputs are
truncated, then long texts are abridged (oldest first, pinned messages last),
then old messages collapse to a `[… N chars omitted …]` note, then old tool
calls shrink to one line each, then old call-less messages are left out and
runs of old call-only messages fold together. Questions are split into as many requests as
needed so each request (state plus questions) stays under `maxRequestTokens`;
the full state is resent with every request. Token counts are estimated
without a tokenizer, calibrated to land a little above what Jev reports.

The mod is an early-access Claude Code function-hook module. The checked-in
type reference was generated by Claude Code **2.1.274**. Enable the function
hooks surface before installing or loading it:

```sh
export CLAUDE_CODE_ENABLE_FUNCTION_HOOKS=1
export TYPESAFE_API_KEY="<your TypeSafe key>"

claude plugin marketplace add tamaratran/fast-jev-compaction
claude plugin install fast-jev-compaction@fast-jev-compaction
```

For local development:

```sh
CLAUDE_CODE_ENABLE_FUNCTION_HOOKS=1 claude --plugin-dir .
```

#### Configuration

The plugin declares these `userConfig` values in
`.claude-plugin/plugin.json`:

| Option | Default |
| --- | ---: |
| `keepThreshold` | `0.5` |
| `preserveRecentMessages` | `6` |
| `compactAtPercent` | `60` |
| `minReductionRatio` | `0.25` |
| `maxStateTokens` | `25000` |
| `maxRequestTokens` | `30000` |
| `truncateHeadChars` | `300` |
| `model` | `jev-latest` |

The TypeSafe key can be supplied as the sensitive `apiKey` plugin option or
through `TYPESAFE_API_KEY`. The environment variable is the recommended
development setup.

Every option except `apiKey`, `compactAtPercent`, `minReductionRatio` and
`model` is passed straight to the library; see the root README for what they
do. The `session.compact` hook runs the Jev requests concurrently. If Jev fails,
the response is malformed, the key is unavailable, the history cannot be
fitted into the state budget, or the estimated reduction is below
`minReductionRatio`, the hook logs a fallback and delegates to Claude Code's
built-in compaction. The outcome is shown as a toast and logged with the
reduction, per-reason counts, state size and request count; a per-call
`decisions:` line with both probabilities is logged for diagnosis. The
`turn.complete` hook requests
compaction when `context.percent` reaches `compactAtPercent`, with an
in-flight guard.

#### Scope and caveat

Function hooks are early access and may change between Claude Code releases.
This mod uses the generated declarations from 2.1.274 in
`types/claude-code.d.ts`; regenerate and review that file after a
Claude Code upgrade.

References:

- [Claude Code plugins](https://code.claude.com/docs/en/plugins)
- [Claude Code plugins reference](https://code.claude.com/docs/en/plugins-reference)
- [Claude Code hooks](https://code.claude.com/docs/en/hooks)

## Top-level structure
- `.claude-plugin/` — Claude Code plugin manifest: `marketplace.json` (marketplace entry) and `plugin.json` (plugin metadata, `userConfig` declarations).
- `demo/JevDemo/` — native SwiftUI macOS app that plays a scripted, non-networked animation of the compaction flow for screen recording.
- `examples/demo.ts` — example/demo script for the library.
- `hooks/` — Claude Code function-hook adapter: `fast-jev.ts` (the hook implementation), `hooks.json` (hook registration), `README.md` (plugin-specific docs).
- `src/` — the npm library implementation: `client.ts` (Jev/TypeSafe HTTP client), `compact.ts` (core compaction algorithm — fitting, batching, decisions), `index.ts` (public exports), `messages.ts` (message/transcript helpers), `request.ts` (Jev request building), `state.ts` (state construction/fitting), `types.ts` (shared types).
- `tests/` — unit tests using a fake Jev implementation (no network calls).
- `types/claude-code.d.ts` — generated Claude Code 2.1.274 type declarations for the function-hooks API.
- `tsconfig.json`, `tsconfig.hooks.json` — TypeScript configs for the library and the hooks build respectively.
- `package.json`, `package-lock.json` — npm package manifest (published as `fast-jev-compaction`).
- `LICENSE` — MIT License.
- `.gitignore` — standard ignores.
