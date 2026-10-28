# Ying-Kai-Liao/jev-browser

## Metadata
- Stars: 126
- Primary language: JavaScript
- Default branch: main
- Latest release: v0.2.1
- License: MIT License
- Homepage: (none)
- Fetched: 2026-10-28
- Final URL: https://github.com/Ying-Kai-Liao/jev-browser

## Description
Browser automation where an LLM plans and Jev (Typesafe System One) decides. Library, CLI and MCP server.

## README
# jev-browser

Browser automation where an LLM plans and **Jev** decides.

> Unofficial project, not affiliated with TypeSafe. It calls the TypeSafe System One API
> with your own API key.

The calling LLM (Claude, via MCP) says what outcome it wants, one step at a time, and hands
over any text to type. For each round of a step, code describes the page. Then one ~300 ms
[Typesafe System One](https://docs.typesafe.ai) request asks Jev several questions at once:
which element, which action, which value, and is the step done / blocked / showing an error /
about to do something irreversible. Playwright performs the action. The LLM never reads page
snapshots unless it chooses to take over.

```
Claude ── browser_do("Log in", {email, password}) ──▶ jev-browser
                                                       │  loop until done / stuck / needs confirmation
                                                       │   1. settle   (network + DOM quiet)
                                                       │   2. describe (elements, labels, state, visible text, diff, counts)
                                                       │   3. Jev      (done? error? irreversible? tool? target? value?)
                                                       │   4. act      (Playwright)
Claude ◀── { status: "done", url, actions[], done_score } ─┘
```

https://github.com/user-attachments/assets/2e688df9-4985-4854-8ebe-ba97c9d13d68

With [WebMCP](#webmcp-when-the-page-offers-its-own-tools), a page offers its own tools. Jev
chooses between those and the page's buttons, and fills each argument by picking one of the
caller's `values` (`text: values.g1 → "milk"`), never by writing text:

https://github.com/user-attachments/assets/fe309fb8-aada-4187-a91e-f18493a39526

Jev only answers with probability distributions: yes/no (`noul`), pick one option (`choice`)
or a rating (`score`). It never writes text. So everything free-form comes from the caller as
candidates, and code turns disagreement or low confidence into a status the LLM can act on.

## Results

42 tasks in 16 categories on live sites (see [RESULTS.md](RESULTS.md)):

- **40/42 correct in the latest run, 0 false "done" claims** (38/41 twice before the latest
  fixes). Remaining misses: counting ("add until 3", flagged `likely_done`) and verifying a sort.
- **~300 ms per Jev call**, 2–4 calls for most steps; a 5-step checkout takes ~14 s end to end.
- **Pause before irreversible actions**: across ~200 rounds it flagged only saucedemo's
  "Finish" (place order) button.
- **Less page content for the LLM** than a Playwright-MCP-style loop on the same tasks
  (estimate): median 5× per task, ≈8k vs ≈557k tokens in total. Big pages dominate the total:
  a Wikipedia article is ~149k snapshot tokens. On tiny pages there is no saving. The page
  reading moves to Jev.

Works on: forms, native and custom dropdowns, checkboxes and radios (including styled
replacements), dynamic loading, modals, JS dialogs, hover, right-click, drag and drop, key
presses, file upload, iframes, shadow DOM, new tabs, pages with 2,000+ elements (two-stage
selection), and non-English UIs.

Known limits, so write steps around them:
- **Ordered sub-goals in one step** ("add two todos, complete one, clear completed") → split
  into one outcome per step.
- **Open-ended goals** ("scroll to load more") → make them measurable or check yourself.
- **Judgements that compare many values** (is this table sorted, did exactly one thing change)
  → verify with `browser_check` or `browser_snapshot`.

## Quick start (Claude Code plugin)

```
/plugin install jev-browser --marketplace Ying-Kai-Liao/jev-browser
```

On older Claude Code versions, add the marketplace first:

```
/plugin marketplace add Ying-Kai-Liao/jev-browser
/plugin install jev-browser@jev-browser
```

Claude Code then asks for your TypeSafe API key (or an OpenRouter key), which goes to its secure credential store. It
also offers two optional settings: show the browser window, and a persistent profile directory
so that logins survive restarts. The plugin runs the MCP server below, pinned to the same
version, and adds a skill that teaches Claude how to write steps and handle each status. The
first browser call downloads Chromium for Playwright if it is missing (one time, about 30 s).

Data: see [Privacy](#privacy). Page content goes to the TypeSafe API (or OpenRouter); passwords and other
secrets you pass in `values` don't.

## Quick start (MCP, from npm)

```bash
npx playwright install chromium          # once (the server also does this on first use)
claude mcp add jev-browser -e TYPESAFE_API_KEY=your-key -- npx -y -p jev-browser jev-browser-mcp
```

Any MCP client works the same way: command `npx`, args `-y -p jev-browser jev-browser-mcp`,
env `TYPESAFE_API_KEY`. Add `JEV_BROWSER_HEADED=1` to watch it work.

No TypeSafe account? Jev is also on [OpenRouter](https://openrouter.ai/typesafe/jev-1.13): pass
`-e OPENROUTER_API_KEY=your-key` instead, and calls are billed to your OpenRouter account. When both
keys are set, `TYPESAFE_API_KEY` wins, whether each comes from the environment or `.env`. `JEV_API_URL` and
`JEV_MODEL` override the TypeSafe endpoint and model; they are ignored when the OpenRouter key is used.

## Setup (from source)

```bash
git clone https://github.com/Ying-Kai-Liao/jev-browser && cd jev-browser
npm install
npm run setup                    # downloads Chromium for Playwright
cp .env.example .env             # add TYPESAFE_API_KEY or OPENROUTER_API_KEY
npm test                         # offline tests (no network, no key)
npm run test:e2e                 # MCP server end to end (network + key)
```

### Use from Claude Code (MCP, from source)

```bash
claude mcp add jev-browser -- node /absolute/path/to/jev-browser/bin/jev-browser-mcp.mjs
```

From a source checkout the server reads `TYPESAFE_API_KEY` (or `OPENROUTER_API_KEY`) from the repo's `.env`.

| tool | purpose |
|---|---|
| `browser_open(url, viewport?)` | navigate and wait for the page to settle; `viewport: "390x844"` resizes the window (e.g. to check a phone layout) and the size sticks for later calls |
| `browser_do(goal, values?, max_actions?, allow_irreversible?, explain?)` | work toward one outcome; returns a status |
| `browser_check(question)` | yes/no about the page → `p_yes` |
| `browser_choose(question, options)` | pick among given options → distribution |
| `browser_snapshot(diff?, interactive?, filter?, urls?, max_chars?)` | compact numbered element list, for taking over; the options below narrow it |
| `browser_act(action, element, value?, key?, destination?, accept_dialog?)` | act on an element directly, no model; confirm/prompt dialogs are dismissed unless `accept_dialog`. `scroll` moves the page's main scrollable area (or the box around `element`) by most of a screen, `value: "up"` goes back, and the reply says how far it `scrolled` |
| `browser_read(question, max_chars?)` | the page text that helps answer a question; Jev drops the rest |
| `browser_screenshot(full_page?)` | PNG image |
| `browser_close()` | end the session |
| `browser_webmcp_tools()` | list the [WebMCP](https://github.com/webmachinelearning/webmcp) tools the page registered |
| `browser_webmcp_call(name, arguments?)` | run one of the page's WebMCP tools; no clicking, no Jev call |

### WebMCP: when the page offers its own tools

A page that supports [WebMCP](https://github.com/webmachinelearning/webmcp) registers tools for
agents with `document.modelContext.registerTool(...)` (or `navigator.modelContext.provideContext`
in earlier drafts). An init script records them before the page's scripts run, in every browser —
where Chromium has no native `modelContext`, a minimal one is installed so feature-detecting pages
still register. `browser_open` lists their names as `webmcp_tools`.

**In `browser_do`, Jev uses them.** Each round, the page's tools are offered next to click, type
and the rest, with a yes/no "can one of the page's tools do the next step?" that decides between
them. The same request fills every tool's arguments: each is one of your `values` or, for an
`enum`, one of its options (a list, a priority), because Jev never writes text. The page's own
`execute` runs, its result goes into the step's history for the "done?" judgement, and the action
shows as `webmcp tool add_todo {"text":"values.todo"} => "…"`. A tool the site does not mark
`readOnlyHint` is guarded like a click: if it looks irreversible the step stops with
`needs_confirmation`.

To call a tool yourself instead, `browser_webmcp_tools` gives each schema and
`browser_webmcp_call` runs it directly, with no Jev call. Main frame only. Tool descriptions and results come from the site:
untrusted, and results are capped at 20k chars. A tool not marked `readOnlyHint` may have side
effects, so the caller should treat it like `allow_irreversible`.

### Reading a page: `browser_read`

`browser_snapshot` is the take-over-and-act surface: numbered elements, plus the text **in the
viewport**. That is the right trade for acting, and it is already small (99–6,900 tokens on
every page measured, because elements are capped at 400 and the text at 2,500 chars). It is a
poor way to *read*, though — a Wikipedia article is ~179k chars of text, so a snapshot shows
about 1.4% of it and the rest costs a scroll-and-snapshot loop.

`browser_read(question)` is the understand-the-content surface. Code extracts the whole
document's text and cuts it at headings and sections; Jev rates every block against the
question in batches of 40; code returns the blocks that help, in document order, inside a
character budget. Jev ranks, it never writes — the text you get back is the page's own.

| | `browser_snapshot` | `browser_read` |
|---|---|---|
| gives you | numbered elements + viewport text | document text relevant to a question |
| use it to | act (with `browser_act`) | read, quote, answer |
| model calls | none | 1 per ~50k chars, ~1 s each |
| lossless | yes | no — drops blocks, and says which |

**When it pays.** Long articles, documentation and reference pages. On the WW2 article,
"When and why did Japan surrender?" returned 11.8k of 178.5k chars — 15× less — in 3.4 s over
5 Jev calls, keeping the atomic-bomb and surrender paragraphs.

**When it doesn't.** Short pages, apps and forms. Below a 8,000-char floor (and below your own
`max_chars`) it returns the page whole and never calls Jev at all, because paying ~1 s to prune
a 2k-token page is a loss. Hacker News, a BBC front page and saucedemo all land under the floor.

It is **biased to keep**: a block Jev cannot rate — or a whole batch whose request failed — is
kept, and whatever is left out is counted and marked in place with `[… N blocks dropped …]`.
Nothing is ever silently cut. Use `browser_snapshot` if you need the page as the caller
normally sees it.

```bash
node examples/read-demo.mjs                                   # WW2 article, default question
node examples/read-demo.mjs "https://…" "what do you want?"   # needs a key
```

`browser_do` statuses:

| status | meaning / what the caller should do |
|---|---|
| `done` | goal reached |
| `likely_done` | the page looks done but Jev is unsure: verify before moving on |
| `needs_login` | a sign-in wall and no credentials in `values`; log in yourself (headed + `JEV_BROWSER_PROFILE`) or pass credentials |
| `needs_confirmation` | next action, or a confirm dialog it opened (then dismissed), looks irreversible (order, pay, send, delete); see `pending`, re-call with `allow_irreversible: true` only if the user wants it |
| `error` | the page shows an error after the last action (e.g. wrong password); see `page_text` |
| `stuck` / `max_actions` | no progress; see `info`, `page_text`, `candidates` |
| `ambiguous` | low confidence in the target; pick from `candidates` with `browser_act` |
| `blocked` | captcha, access denied, error page |

`browser_snapshot` options. A snapshot is the one page the calling LLM reads in full, so every
option narrows what gets rendered. All of them are pure formatting: nothing is collected
differently and none of them costs a Jev call.

| option | default | effect |
|---|---|---|
| `diff` | `false` | only what changed since the previous snapshot, using the same diff the `browser_do` loop feeds Jev. With no previous snapshot you get a full one and a note saying so. A diff carries no element numbers: take a full snapshot to act. |
| `interactive` | `false` | drop the `visible text:` block; element lines and dialog/status text stay. The element list is interactive-only already, so this narrows the prose, not the elements. |
| `filter` | — | keep only elements whose label, text, placeholder, name or href contains the substring, case-insensitive; the header says how many were hidden |
| `urls` | `false` | print `href=` on element lines. **Off by default** — on a link-heavy page link targets are the largest single share of the output, and `browser_act` takes element numbers, not URLs. A link with nothing else to identify it keeps its href. |
| `max_chars` | `10000` | size of the rendered snapshot, hard cap 20000. When it truncates, the last line says how many element lines and characters were dropped and which option would narrow it. |

A typed password is never printed: `input:password` values render as `[redacted]`, in a snapshot
and in a diff. Measured on a Wikipedia article (1,840 elements), a default snapshot went from
26,919 to 9,926 characters (~6,700 → ~2,500 estimated tokens); `filter` brings it to ~800 and
`diff` after a scroll to ~50.

Env: `JEV_BROWSER_HEADED=1` shows the browser, `JEV_BROWSER=chrome` runs your own browser
instead of Playwright's Chromium (`chrome`, `chrome-beta`, `msedge`, or the path to any
Chromium-based browser's executable, such as Brave), `JEV_BROWSER_PROFILE=/dir` keeps a persistent
profile (logins survive restarts; use a dedicated directory, since Chrome won't be automated with
your everyday profile), `JEV_BROWSER_LOG=1` prints per-round decisions to stderr,
and `JEV_BROWSER_NO_INSTALL=1` turns off the Chromium download on first use. The MCP server
reads `TYPESAFE_API_KEY` or `OPENROUTER_API_KEY` from its environment, or from the `.env` of a source checkout, but
never from the `.env` of the directory it was started in.

### Library

```js
// npm install jev-browser && npx playwright install chromium
import { JevBrowser } from "jev-browser";

const b = await JevBrowser.launch({ headed: true });
await b.open("https://www.saucedemo.com/");
await b.do("Log in", { values: { username: "standard_user", password: "secret_sauce" } });
await b.do("Add the Sauce Labs Backpack to the cart");
const p = await b.check("Does the cart badge show 1 item?");   // 0..1
await b.close();
```

### Watch it

```bash
node examples/webmcp-demo.mjs        # headed: 9 plain goals on a planner; Jev picks page tools or clicks, ~25 s
STEP_MS=800 RECORD=demo.mp4 node examples/webmcp-demo.mjs   # same, paced, recorded at 2x (needs ffmpeg)
node examples/x-profile-demo.mjs     # headed, read-only x.com walkthrough with decision highlights
```

Each action is outlined in red with Jev's choice and scores before it happens (`highlight: true`,
on by default in the MCP server when `JEV_BROWSER_HEADED=1`). Some sites, x.com included, serve a
blank page to headless Chromium: use headed mode there.

### CLI

```bash
node bin/jev-browser.mjs do https://the-internet.herokuapp.com/login "Log in" username=tomsmith 'password=SuperSecretPassword!'
node bin/jev-browser.mjs run examples/flows/todomvc.json --headed
```

## Writing good steps

- One observable outcome per step: "Log in", "Open the Pull requests tab", "Mark 'buy milk' completed".
- Every string goes in `values` with a meaningful key (`email`, `postal_code`, `file`).
- Treat `likely_done`, `needs_confirmation`, `ambiguous` and `stuck` as your turn: check,
  snapshot or ask the user, don't just retry.
- After steps with side effects, `browser_check` what must *not* have changed.

## Cost: what the caller pays and what Jev spends

`bin/jev-cost.mjs` measures both sides of the trade this project claims to make, on a page you
name. Every snapshot, every tool result and every Jev call is measured as it happens — nothing
is measured once and multiplied.

```bash
npm run cost                                              # the built-in saucedemo + wikipedia cases
npm run cost -- --url https://example.com/ --goal "Log in" --value user=ada --value pw=secret
npm run cost -- --json > run.json                         # machine-readable
npm run cost -- --report run.json                         # re-print the table from a saved run
node bin/jev-cost.mjs --help                              # every flag
```

Per scenario it reports **caller tokens** (the text crossing the MCP boundary: every tool result
plus the arguments the caller had to write, at chars ÷ 4 — an approximation, and the report says
so), **Jev tokens and calls** (the API's own `usage.input_tokens`, exact), and wall-clock
seconds. The scenarios are run on the same page toward the same goal so they compare: a
Playwright-MCP-style baseline that takes a fresh `page.ariaSnapshot({ mode: "ai" })` after every
action, `browser_do`, each `browser_snapshot` option against the default, and `browser_read`
against dumping the whole document.

The `net` column is caller tokens saved minus Jev tokens spent, one for one, and it goes negative
when a scenario loses — on a small page Jev's spend and latency can outweigh the saving, and the
tool prints that as a loss. Measured numbers and what they say about the older estimate are in
[RESULTS.md](RESULTS.md).

A run needs network and `TYPESAFE_API_KEY`, and costs API credits. `npm test` stays offline: the
ledger arithmetic is pure and tested in `test/cost.test.mjs`.

## Benchmark

```bash
node bench/run.mjs --set all            # base, hard, guard (+ bench/tasks.local.mjs if present)
node bench/run.mjs --only ti-login,drag
node bench/context-cost.mjs bench/results/<run>.json   # older one-sided estimate; see npm run cost
```

Private sites and credentials go in `bench/tasks.local.mjs` (git-ignored), exporting `LOCAL`.

## Layout

```
src/session.mjs      JevBrowser: settle, snapshot, decide (1 or 2 stages), resolve, act, do, check, choose
src/page-script.mjs  runs in each frame: elements, labels, state, visible text, metrics, dialogs
src/page-model.mjs   pure helpers: diff between pages, counts, compact rendering
src/webmcp.mjs       init script recording the page's WebMCP tools; result formatting
src/prune.mjs        pure helpers: split page text into blocks, batch, rank, reassemble
src/jev.mjs          System One API client
src/flow.mjs         JSON flow runner
bin/                 CLI and MCP server
.claude-plugin/      Claude Code plugin manifest and the repo's own marketplace
.mcp.json            the plugin's MCP server: npx jev-browser@<version>, key from plugin settings
skills/jev-browser/  skill the plugin adds: how to write steps and handle each status
scripts/             keeps plugin.json and .mcp.json on package.json's version
bin/jev-cost.mjs     two-sided token ledger: caller tokens vs Jev tokens, measured per scenario
bench/               tasks with ground-truth checks, runner, context-cost estimate
test/                offline fixture tests, MCP end-to-end test
NOTES.md             design notes: what works with Jev, what doesn't, and why
```

## Releasing

CI runs the offline tests on every push and pull request. To publish, bump the version and push
the tag; `.github/workflows/release.yml` tests, publishes to npm with provenance and creates a
GitHub release:

```bash
npm version patch            # or minor / major: commits and tags vX.Y.Z
git push --follow-tags
```

`npm version` also sets the version in `.claude-plugin/plugin.json` and the pinned
`jev-browser@X.Y.Z` in `.mcp.json`, so the plugin always launches the release it ships with.
CI checks that the three agree and runs `claude plugin validate . --strict` (`npm run validate`
does both locally). Plugin users get the new version when the marketplace repo updates; the
directory listing picks it up from the tracked branch.

Publishing uses npm trusted publishing, set up once with
`npx npm@latest trust github jev-browser --file release.yml --repo Ying-Kai-Liao/jev-browser --allow-publish`.

## Privacy

jev-browser runs locally. It has no server of its own and collects no telemetry. To decide
each action it sends the following to the TypeSafe System One API (`api.typesafe.ai`), or to
OpenRouter (`openrouter.ai`) when you use an OpenRouter key, using your key:

- the current page's URL, title, visible text and interactive elements, as well as the text
  blocks `browser_read` ranks;
- the step's `goal`, recent action history, and your `browser_check` and `browser_choose`
  questions;
- the `values` you pass, **except** those whose key names a secret (`password`, `pw`, `token`,
  `secret`, `otp`, `card`, `cvv`, `cvc`, `ssn`, `api_key`, `pin`). Those are shown by key only.
  Values typed into password fields are also redacted, and so is a secret value the page
  shows back (in its text or a WebMCP tool's result).

Playwright types the real values locally. TypeSafe's (and OpenRouter's) handling of this data
is covered by their own terms. Screenshots and snapshots go only to your MCP client. See [PRIVACY.md](PRIVACY.md).

## License

MIT


## Docs
### RESULTS.md

# Results (2026-09-17)

Model `jev-latest` (resolved to jev-1.13.0). Headless Chromium 1280×800, 3 tasks in parallel.
Commands: `node bench/run.mjs --set all`, `node bench/context-cost.mjs <run.json>`.
A task is **correct** when every step returns its expected status (`done`/`likely_done`, or
`needs_confirmation` for the guard test) and its ground-truth check passes. Tasks built to
fail are correct when no step claims done. **False done** = a step said `done` while its
ground-truth check failed.

## Latest: r10 (after the add-item, overlay and login fixes)

42 tasks (a `login-wall` task was added): **40/42 correct, 0 false done**, 202 Jev calls, 286 ms
average. Misses: `ti-add-remove` stopped at 2 of 3 buttons but returned `likely_done`, not
`done`; `ti-sort-table` is still `stuck`. `todomvc-coarse` and `infinite-scroll` now pass. The
tables below are from the earlier r6/r7 pair (41 tasks) and are kept for comparison.

## Two full runs, same code (r6, r7)

| run | correct | false done | likely_done | Jev calls | avg ms/call | input tokens/call | wall time (41 tasks, 3 parallel) |
|-----|---------|------------|-------------|-----------|-------------|-------------------|------------------|
| r6  | 38/41   | 0          | 0           | 211       | 290         | 2,890             | 251 s            |
| r7  | 38/41   | 0          | 0           | 208       | 299         | 2,801             | 248 s            |

Both runs failed the same 3 tasks, and each of those failures is a known model limit, not a flake:

| task | status | what happened |
|---|---|---|
| todomvc-coarse | stuck | one step with ordered sub-goals (add 2, complete 1, clear); the same actions pass as 5 steps |
| ti-sort-table | stuck | the table was sorted, but nothing marks sort state; Jev can't judge order from rows (0.21) |
| infinite-scroll | stuck | "scroll to load more" has no end point; content did load, `done` swung 0.2↔0.84 |

In r6, 190 rounds: median target confidence 0.97; 7 rounds needed two-stage selection (largest
page 2,273 elements). Actions performed: click 61, type 41, scroll 9, wait 6, select 4,
press_enter 4, and one each of hover, drag, right_click, press_key, upload.

## By category (r6 + r7)

| category | correct | calls/task | s/task |
|---|---|---|---|
| form (login, number, 5-field form as one goal and as 7 steps) | 8/8 | 7.0 | 5.1 |
| widget (select, checkboxes) | 4/4 | 3.0 | 5.4 |
| dynamic (delayed load, enable-then-type, add until 3) | 6/6 | 5.0 | 7.6 |
| spa (TodoMVC by steps / one goal) | 2/4 | 9.5 | 5.2 |
| interaction (hover, JS confirm, delayed modal, sort) | 6/8 | 2.3 | 5.2 |
| navigation (HN, books) | 4/4 | 3.5 | 4.8 |
| large-page (Wikipedia search/link, GitHub tabs/search) | 8/8 | 4.3 | 8.2 |
| e2e (saucedemo checkout by steps / one goal, a private staging login run from tasks.local.mjs) | 6/6 | 12.3 | 13.1 |
| negative (bad password, missing page, disabled field, missing option) | 8/8 | 2.8 | 4.4 |
| iframe (form, jQuery date picker) | 4/4 | 3.3 | 2.8 |
| shadow-dom | 2/2 | 2.0 | 1.1 |
| custom-widget (react-select) | 2/2 | 3.0 | 5.3 |
| tabs (new window) | 2/2 | 2.0 | 4.7 |
| lazy (infinite scroll) | 0/2 | 11.0 | 9.4 |
| actions (drag, right-click, key press, upload) | 8/8 | 2.8 | 4.4 |
| guard (login and form not paused; checkout paused at Finish) | 6/6 | 8.3 | 7.1 |

## Irreversible-action pause

Every round asks `irreversible` (would the next action have a hard-to-undo effect outside the
browser?). In tasks run *without* the pause, the rounds where it would have fired (≥0.6 on a
click/Enter/key) were only:

- r6: saucedemo-fine `Finish` (0.66, 0.77), saucedemo-coarse `Finish` (0.70)
- r7: saucedemo-fine `Finish` (0.77), saucedemo-coarse `Finish` (0.72)

Logins, form submits, "Add to cart", "Checkout", "Continue", upload and drag never reached it.

## Page content the calling LLM reads (estimate)

Playwright-MCP style = one AI aria snapshot (`page.ariaSnapshot({mode: "ai"})`) of the task's
start page per action, plus the initial one. jev-browser = the `browser_do` results. Tokens ≈ characters / 4.

| | total over 40 tasks (r6) | median task |
|---|---|---|
| Playwright-MCP style, to the LLM | ≈557k tokens | — |
| jev-browser, to the LLM | ≈8.3k tokens | 5.4× less |
| read by Jev instead | ≈602k tokens | |

The gap comes from big pages: Wikipedia link (≈149k-token snapshot, ~2,300×), GitHub (~270×),
HN and books (~115–180×). Small test pages save 2–8×. The iframe and shadow-DOM pages
cost *more* (0.3–0.4×), because their snapshots are tiny. This does not measure how many
actions an LLM would take on its own.

## Measured two-sided ledger (2026-09-19)

The section above is an estimate: `bench/context-cost.mjs` measures one aria snapshot on each
task's start page and reuses its size for every action, and it reports Jev's own spend as a
trailing column that is never subtracted from the saving. `bin/jev-cost.mjs` measures every
snapshot, every tool result and every Jev call as it happens, and puts both sides in one table:

```
npm run cost                                    # the two cases below
npm run cost -- --url <url> --goal "<goal>"     # any page
npm run cost -- --json > run.json && npm run cost -- --report run.json
```

Model `jev-latest`, headless Chromium 1280×800, one run, 2026-09-19. **Caller tokens** are the
text crossing the MCP boundary — every tool result plus the arguments the caller had to write —
at chars ÷ 4, an approximation. **Jev tokens** are the API's own `usage.input_tokens`, exact.
`net` = caller tokens saved against the row's baseline − Jev tokens spent, counted one for one;
it is the pessimistic reading, since a Jev token is much cheaper than a caller token.

```
══ saucedemo ══ https://www.saucedemo.com/
   goal: "Log in"   question: "Which usernames can be used to log in, and what is the password?"

group   scenario                                 caller tok  jev tok calls      s   vs base        net
------------------------------------------------------------------------------------------------------
act     playwright-mcp (baseline)                     1,928        —     —   0.05     1.00×          0
open    browser_open                                     86        0     0   1.75         —          —
observe browser_snapshot (baseline)                     110        0     0   0.00     1.00×          0
observe browser_snapshot --interactive                   70        0     0   0.00     1.57×         40
observe browser_snapshot --filter                        95        0     0   0.00     1.16×         15
observe browser_snapshot --urls                         112        0     0   0.00     0.98×         -2
observe browser_snapshot --max-chars 2000               114        0     0   0.00     0.96×         -4
read    browser_read (whole doc) (baseline)             157        0     0   0.00     1.00×          0
read    browser_read (ranked)                           152        0     0   0.00     1.03×          5
act     browser_do                                      110    7,383     4   2.89     17.5×     -5,565
observe browser_snapshot (after action) (baseli…        607        0     0   0.21     1.00×          0
observe browser_act scroll                               45        0     0   0.00         —          —
observe browser_snapshot --diff                          62        0     0   0.01     9.79×        545
------------------------------------------------------------------------------------------------------
TOTAL                                                 3,648    7,383     4   4.93     17.5×     -5,565

  LOSS on this page: browser_do (-5,565 tokens), browser_snapshot --max-chars 2000 (-4),
                     browser_snapshot --urls (-2)

══ wikipedia ══ https://en.wikipedia.org/wiki/Alan_Turing
   goal: "Open the linked article about Bletchley Park"
   question: "What did Alan Turing do at Bletchley Park during the Second World War?"

group   scenario                                 caller tok  jev tok calls      s   vs base        net
------------------------------------------------------------------------------------------------------
act     playwright-mcp (baseline)                   267,662        —     —   0.41     1.00×          0
open    browser_open                                    158        0     0   2.45         —          —
observe browser_snapshot (baseline)                   2,491        0     0   1.21     1.00×          0
observe browser_snapshot --interactive                2,497        0     0   0.12     1.00×         -6
observe browser_snapshot --filter                       805        0     0   0.12     3.09×      1,686
observe browser_snapshot --urls                       2,484        0     0   0.11     1.00×          7
observe browser_snapshot --max-chars 2000               699        0     0   0.11     3.56×      1,792
read    browser_read (whole doc) (baseline)          28,042        0     0   0.05     1.00×          0
read    browser_read (ranked)                         3,270   41,334     4   2.77     8.58×    -16,562
act     browser_do                                       81   44,259     4   8.57     3,304×    223,322
observe browser_snapshot (after action) (baseli…      2,489        0     0   0.10     1.00×          0
observe browser_act scroll                               50        0     0   0.00         —          —
observe browser_snapshot --diff                          67        0     0   0.07     37.1×      2,422
------------------------------------------------------------------------------------------------------
TOTAL                                               310,795   85,593     8  16.11     3,304×    223,322

  LOSS on this page: browser_read (ranked) (-16,562 tokens), browser_snapshot --interactive (-6)
```

The `playwright-mcp` row is one real `page.ariaSnapshot({ mode: "ai" })` per navigation and per
action, taken on the page as it then was. Its Jev columns are `—`: a Playwright-MCP run has no
cheap model, and the Jev calls used here only walked the page into each state (saucedemo 6 calls
/ 9,847 tokens, wikipedia 4 / 44,569) — they are excluded. Its seconds are the measured
snapshot time only; a real run also pays the caller model's own latency, which this cannot
measure, so the number is a floor and not a comparison.

### How this compares to the estimate above

**The caller-side ratio holds up; the conclusion drawn from it does not.** The estimate put the
Wikipedia-link task at ~2,300×; measured, it is 3,304×. That is the same order of magnitude, so
the headline was not inflated by the reuse assumption. What the estimate never did was subtract
Jev's own spend, and once it is subtracted the small-page case is a **loss**: logging in to
saucedemo costs the caller 110 tokens instead of 1,928 — a 17.5× win on the expensive model —
while spending 7,383 tokens on the cheap one, for a net of **−5,565**. On the same page the trade
also costs 2.89 s of `browser_do` against 0.05 s of aria snapshotting.

**Reusing one snapshot size is wrong in both directions, and badly wrong when the page changes.**
The four aria snapshots of the saucedemo walk measured 140, 146, 150 and **1,400** tokens: the
page after login is ten times the login form. The estimate's method (4 × the start page) gives
560 tokens against the measured 1,928 — **3.4× low**. On Wikipedia the same method gives 2 ×
149,370 = 298,740 against the measured 267,662 — **12% high**, because the second page is smaller
than the first.

**`browser_read` is a loss on a long article at today's settings.** Answering from the Alan
Turing page costs the caller 3,270 tokens ranked against 28,042 for the whole document — 8.6×
less — but the ranking spends 41,334 Jev tokens across 4 requests, for a net of **−16,562**. It
is still the right tool when the caller's context is the binding constraint; it is not a saving
in total tokens.

**The new `browser_snapshot` options are free, and only pay on large pages.** On Wikipedia
`--max-chars 2000` is 3.6× cheaper, `--filter` 3.1×, and `--diff` after one scroll 37×; on
saucedemo they move 70–114 tokens and `--urls` and `--max-chars` are a couple of tokens *worse*
than the default. `--interactive` is 1.57× on saucedemo but 1.00× on Wikipedia, where the
element list, not the prose, is what fills the budget. None of them calls Jev.

Two pages is not a benchmark. These numbers say what these two pages cost, not what a median
task costs; run `npm run cost -- --url …` on the page you care about.


## Top-level structure
```
.claude-plugin/, .mcp.json, .env.example
bin/, bench/, examples/, scripts/, skills/jev-browser/, src/, test/
NOTES.md, PRIVACY.md, RESULTS.md, LICENSE, package.json
```
- `src/`: flow, jev, page-model, page-script, prune, session, webmcp — library core
- `skills/jev-browser`: agent skill
- `examples/`: demos (webmcp, x-profile, flows)
- `bench/`: context-cost and task benchmarks
- Dual surface: library + CLI + MCP server

