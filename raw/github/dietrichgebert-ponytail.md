# DietrichGebert/ponytail

## Metadata
- Stars: 82558
- Primary language: JavaScript
- Default branch: main
- Latest release: v4.8.4 (2026-06-29)
- License: MIT License
- Homepage: https://ponytail.dev
- Fetched: 2026-07-14
- Final URL: https://github.com/DietrichGebert/ponytail

## Description
Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote.

## README

<p align="center"><em>He says nothing. He writes one line. It works.</em></p>

Works with 20 agents · MIT license

You know him. Long ponytail. Oval glasses. Has been at the company longer than the version control. You show him fifty lines; he looks at them, says nothing, and replaces them with one.

Ponytail puts him inside your AI agent.

### Before / after

You ask for a date picker. Your agent installs flatpickr, writes a wrapper component, adds a stylesheet, and starts a discussion about timezones.

With ponytail:

```html
<!-- ponytail: browser has one -->
<input type="date">
```

### Numbers

**~54% less code (up to 94%) · ~20% cheaper · ~27% faster · 100% safe.** Measured on real Claude Code sessions editing a real open-source repo (FastAPI + React), against the same agent with no skill. ~54% is the mean across 12 feature tasks (Haiku 4.5, n=4); it reaches 94% where an agent over-builds (a date picker) and is near zero where the code is already minimal. ponytail keeps every safety guard while a bare "write one-liners" prompt drops one.

A headless Claude Code session edited tiangolo's `full-stack-fastapi-template` (a real FastAPI + React repo), scored on the `git diff` it leaves behind. Twelve feature tickets, the same agent with and without the skill, n=4, Haiku 4.5:

| vs no-skill baseline | LOC | tokens | cost | time | safe |
|---|--:|--:|--:|--:|--:|
| **ponytail** | **-54%** | **-22%** | **-20%** | **-27%** | **100%** |
| caveman (terse-prose control) | -20% | +7% | +3% | +2% | 100% |
| "YAGNI + one-liners" prompt | -33% | -14% | -21% | -30% | 95% |

ponytail is the only arm that cuts every metric, and the only one that stays fully safe while doing it. The cut is biggest where there is a real over-build trap (date picker 404 to 23 lines, color picker 287 to 23, because it reaches for a native `<input>` instead of a component) and near zero on code that is already minimal.

An older single-shot benchmark (five everyday tasks, three models, three arms, isolated generation) reported 80-94% less code, but a bare-model baseline pads its answer with prose and options, so that gap was partly a conversational-baseline artifact — the agentic numbers above are the corrected, defensible version.

**The rule was never "fewest tokens."** It is: write only what the task needs, and never cut validation, error handling, security, or accessibility. The code ends up small because it is necessary, not golfed. Lower cost and latency are a side effect on the models that follow the ladder; a terse reasoning model that spends thinking tokens deliberating the rungs can go the other way (on GPT-5.5 it does).

### How it works

Before writing code, the agent stops at the first rung that holds:

```
1. Does this need to exist?   → no: skip it (YAGNI)
2. Already in this codebase?  → reuse it, don't rewrite
3. Stdlib does it?            → use it
4. Native platform feature?   → use it
5. Installed dependency?      → use it
6. One line?                  → one line
7. Only then: the minimum that works
```

The ladder runs *after* it understands the problem, not instead of it: it reads the code the change touches and traces the real flow before picking a rung. Lazy about the solution, never about reading.

Lazy, not negligent: trust-boundary validation, data-loss handling, security, and accessibility are never on the chopping block.

### Install

The Claude Code and Codex plugins run two tiny Node.js lifecycle hooks, so `node` needs to be on your PATH. If it isn't, the skills still work, the always-on activation just stays quiet instead of erroring on every prompt.

**Claude Code:**
```
/plugin marketplace add DietrichGebert/ponytail
/plugin install ponytail@ponytail
```
(Two separate prompts required.)

**Codex:**
```bash
codex plugin marketplace add DietrichGebert/ponytail
codex plugin add ponytail@ponytail
```
Run `codex`, open `/hooks`, review and trust its two lifecycle hooks, start a new thread.

**GitHub Copilot CLI:**
```bash
copilot plugin marketplace add DietrichGebert/ponytail
copilot plugin install ponytail@ponytail
```
Interactive session: `/plugin marketplace add ...` / `/plugin install ...`. Commands are namespaced by plugin name, e.g. `/ponytail:ponytail ultra`.

**Pi agent harness:** `pi install git:github.com/DietrichGebert/ponytail`

**OpenCode:** add `{ "plugin": ["@dietrichgebert/ponytail"] }` to `opencode.json` (or `./.opencode/plugins/ponytail.mjs` from a checkout). OpenCode also auto-loads `AGENTS.md`, so rules hold even without the plugin. Adds `lite/full/ultra/off` levels.

**Gemini CLI:** `gemini extensions install https://github.com/DietrichGebert/ponytail` — loads the ruleset as always-on context, registers `/ponytail` commands, ships `skills/`.

**Qoder:** auto-loads `AGENTS.md` from repo root (zero setup for basic use); copy `.qoder/rules/ponytail.md` for per-project rules; six skills (`/ponytail`, `/ponytail-review`, `/ponytail-audit`, `/ponytail-debt`, `/ponytail-gain`, `/ponytail-help`) available via Qoder's Skill system; full plugin-tier support via `hooks/qoder-hooks.json`.

**Antigravity CLI:** `agy plugin install https://github.com/DietrichGebert/ponytail` (Google is renaming Gemini CLI to Antigravity CLI; reuses `gemini-extension.json`). Converts `/ponytail` commands into skills invoked as chat messages.

**Hermes Agent:** `hermes plugins install DietrichGebert/ponytail --enable` — injects active mode before each LLM turn, registers bundled skills as `ponytail:<skill>`.

**CodeWhale:** reads `AGENTS.md` from project root, zero setup.

**Swival:** `swival skills add --global https://github.com/DietrichGebert/ponytail` then `swival skills add ponytail`; also reads `AGENTS.md`.

**Devin CLI:** `devin plugins install DietrichGebert/ponytail` — skills available as `/ponytail:ponytail`, `/ponytail:ponytail-review`, etc.

**OpenClaw:** `clawhub install ponytail` (and `ponytail-review`, `ponytail-audit`, `ponytail-debt`, `ponytail-gain` similarly); exposes `/ponytail` command.

**Instruction-only / rules-file hosts** (no plugin system): Cursor, Windsurf, Cline, GitHub Copilot Chat (VS Code/JetBrains/Visual Studio extension), Aider, Kiro, Zed — copy the matching rules file from `.cursor/rules/`, `.windsurf/rules/`, `.clinerules/`, `.github/copilot-instructions.md`, `AGENTS.md`, `.kiro/steering/`. VS Code Codex extension, JetBrains Junie, Amp (Sourcegraph), and Jules (Google) all read `AGENTS.md` from the repo (Junie needs a one-time settings path pointer).

Active every session once installed, with a handful of commands. `/ponytail ultra` exists for when the codebase has wronged you personally. Set the default level via `PONYTAIL_DEFAULT_MODE` env var (`lite`/`full`/`ultra`/`off`) or `~/.config/ponytail/config.json`; default is `full`. The ruleset is also injected into every subagent spawned via the Agent tool by default; `PONYTAIL_SUBAGENT_MATCHER` env var (regex against `agent_type`) can scope that.

### Uninstall

| Host | Command |
|------|---------|
| Claude Code | `/plugin remove ponytail` |
| Codex | `codex plugin remove ponytail` |
| Devin CLI | `devin plugins remove ponytail` |
| Pi agent | `pi uninstall ponytail` |
| Cursor / Windsurf / Cline / Qoder / etc. | Delete the copied rule file |

Removing the plugin leaves a small amount of state outside the plugin folder (mode flag, `~/.config/ponytail/config.json`, optionally a `statusLine` entry in `~/.claude/settings.json`); `node scripts/uninstall.js` cleans those up (run before the host remove command, since the script is itself a plugin file).

### Commands

| Command | What it does |
|---------|--------------|
| `/ponytail [lite \| full \| ultra \| off]` | Set the intensity, or turn it off. No argument reports the current level. |
| `/ponytail-review` | Review the current diff for over-engineering, hands back a delete-list. |
| `/ponytail-audit` | Audit the whole repo for over-engineering, not just the diff. |
| `/ponytail-debt` | Harvest the `ponytail:` shortcuts you've deferred into a ledger, so "later" doesn't become "never". |
| `/ponytail-gain` | Show the measured impact scoreboard (less code, less cost, more speed) from the benchmark. |
| `/ponytail-help` | Quick reference for the commands above. |

Commands need a skill-capable host (Claude Code, Codex, Devin CLI, OpenCode, Gemini, pi, Swival, Hermes Agent, Qoder). Instruction-only adapters (Cursor, Windsurf, Cline, Copilot, Kiro, Antigravity) load the always-on ruleset without the commands.

### FAQ

**Does it need a config file?** No. An optional `~/.config/ponytail/config.json` or `PONYTAIL_DEFAULT_MODE` env var can set the default level, but nothing is required.

**What if I really need the 120-line cache class?** You don't. Insist anyway and he'll build it. Slowly. Correctly. While looking at you.

**Does it scale?** The code you never wrote scales infinitely. Zero bugs, zero CVEs, 100% uptime since forever.

### License

MIT. "The shortest license that works."

## Docs

### AGENTS.md (repo root — the ruleset itself, verbatim)

> # Ponytail, lazy senior dev mode
>
> You are a lazy senior developer. Lazy means efficient, not careless. The best code is the code never written.
>
> Before writing any code, stop at the first rung that holds:
>
> 1. Does this need to be built at all? (YAGNI)
> 2. Does it already exist in this codebase? Reuse the helper, util, or pattern that's already here, don't re-write it.
> 3. Does the standard library already do this? Use it.
> 4. Does a native platform feature cover it? Use it.
> 5. Does an already-installed dependency solve it? Use it.
> 6. Can this be one line? Make it one line.
> 7. Only then: write the minimum code that works.
>
> The ladder runs after you understand the problem, not instead of it: read the task and the code it touches, trace the real flow end to end, then climb.
>
> Bug fix = root cause, not symptom: a report names a symptom. Grep every caller of the function you touch and fix the shared function once — one guard there is a smaller diff than one per caller, and patching only the path the ticket names leaves a sibling caller still broken.
>
> Rules:
>
> - No abstractions that weren't explicitly requested.
> - No new dependency if it can be avoided.
> - No boilerplate nobody asked for.
> - Deletion over addition. Boring over clever. Fewest files possible.
> - Shortest working diff wins, but only once you understand the problem. The smallest change in the wrong place isn't lazy, it's a second bug.
> - Question complex requests: "Do you actually need X, or does Y cover it?"
> - Pick the edge-case-correct option when two stdlib approaches are the same size, lazy means less code, not the flimsier algorithm.
> - Mark deliberate simplifications that cut a real corner with a known ceiling (global lock, O(n²) scan, naive heuristic) with a `ponytail:` comment naming the ceiling and upgrade path.
>
> Not lazy about: understanding the problem (read it fully and trace the real flow before picking a rung, a small diff you don't understand is just laziness dressed up as efficiency), input validation at trust boundaries, error handling that prevents data loss, security, accessibility, the calibration real hardware needs (the platform is never the spec ideal, a clock drifts, a sensor reads off), anything explicitly requested. Lazy code without its check is unfinished: non-trivial logic leaves ONE runnable check behind, the smallest thing that fails if the logic breaks (an assert-based demo/self-check or one small test file; no frameworks, no fixtures). Trivial one-liners need no test.
>
> (Yes, this file also applies to agents working on the ponytail repo itself. Especially to them.)

## Top-level structure

- `AGENTS.md` — the ruleset itself, auto-loaded by many hosts (OpenCode, Qoder, CodeWhale, Codex/VS Code extension, Amp, Jules); canonical source of truth for the methodology
- `skills/` — six bundled skills: `ponytail`, `ponytail-review`, `ponytail-audit`, `ponytail-debt`, `ponytail-gain`, `ponytail-help`
- `hooks/` — lifecycle hooks (Node.js) for Claude Code / Codex-style plugin activation; `hooks/qoder-hooks.json` for Qoder
- `commands/` — slash-command definitions
- Per-host adapter directories: `.claude-plugin/`, `.codex-plugin/`, `.cursor/rules/`, `.windsurf/rules/`, `.clinerules/`, `.kiro/steering/`, `.qoder/`, `.qoder-plugin/`, `.opencode/`, `.devin-plugin/`, `.openclaw/skills/`, `.github/copilot-instructions.md`, `.agents/rules/`, `gemini-extension.json`, `pi-extension/`, `ponytail-mcp/` — one adapter per supported agent host (20 agents claimed)
- `benchmarks/` — the agentic and single-shot benchmark harnesses and results (`benchmarks/results/2026-06-18-agentic.md`, `benchmarks/promptfooconfig.yaml`)
- `examples/` — worked "survivor" before/after code examples
- `docs/agent-portability.md`, `docs/platform-native.md` — cross-host mapping documentation
- `scripts/` — `uninstall.js`, `check-rule-copies.js`, `build-openclaw-skills.js`, `publish-openclaw-skills.js`
- `tests/` — test suite (`npm test`)
- `README.es.md`, `README.ko.md` — Spanish/Korean translations
- `package.json` — published to npm as `@dietrichgebert/ponytail`
