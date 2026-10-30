# microsoft/TokenEconomizer

## Metadata
- Stars: 954
- Forks: 75
- Primary language: Python
- Default branch: main
- Latest release: v0.1.0 (2026-10-26)
- License: Apache-2.0
- Homepage: https://tokeneconomizer.github.io
- Pushed: 2026-10-30T06:00:40Z
- Fetched: 2026-10-30
- Final URL: https://github.com/microsoft/TokenEconomizer
- arXiv: https://arxiv.org/abs/2610.22732

## Description
Experience-Driven Black-Box Cost Control for Coding Agents

## README
# TokenEconomizer: Experience-Driven Black-Box Cost Control for Coding Agents

<p align="center">
  Aaron J. Li<sup>1</sup>,
  Weijia Xu<sup>2</sup>,
  Chandan Singh<sup>2</sup>,
  Zixiao Chen<sup>3</sup>,
  Jeevana Priya Inala<sup>2</sup>,
  Charlotte Siska<sup>3</sup>,
  <br>
  Acar Tamersoy<sup>3</sup>,
  Bin Yu<sup>1</sup>,
  Ion Stoica<sup>1</sup>,
  Michel Galley<sup>2</sup>,
  Jianfeng Gao<sup>2</sup>
</p>
<p align="center">
  <sup>1</sup>UC Berkeley &nbsp; <sup>2</sup>Microsoft Research &nbsp; <sup>3</sup>Microsoft Security
</p>

<p align="center">
  <a href="https://arxiv.org/abs/2610.22732"><img src="https://img.shields.io/badge/arXiv-2610.22732-b31b1b.svg" alt="arXiv"></a>
  <a href="https://tokeneconomizer.github.io"><img src="https://img.shields.io/badge/project-page-2f6fb0.svg" alt="Project page"></a>
  <a href="https://x.com/aaron_jli/status/2114797313613053952"><img src="https://img.shields.io/badge/X-post-000000.svg?logo=x&logoColor=white" alt="X post"></a>
  <img src="https://img.shields.io/badge/python-3.10%2B-3776ab.svg" alt="Python 3.10+">
  <img src="https://img.shields.io/badge/license-Apache%202.0-blue.svg" alt="Apache 2.0 license">
</p>

<p align="center">
  Our measurement on SWE-Bench tasks: <b>18.4–30.9% lower mean cost</b> across five agent–model
  combinations, cheaper in <b>all 30</b> repository × combination cells, and Pass@1 up in
  <b>4 of 5</b>. <a href="#results">Results</a>
</p>

<p align="center">
  <picture>
    <source media="(prefers-reduced-motion: reduce)" srcset="docs/assets/teaser.png">
    <img src="docs/assets/teaser.gif" width="100%" alt="An animation that opens on a title card: TokenEconomizer, experience-driven black-box cost control for coding agents, with its three mechanisms (micro-skills, tool pruning, failure-loop intervention), the agents it works with (Claude Code, Codex, GitHub Copilot CLI, Pi) and the UC Berkeley and Microsoft logos. Then a schematic of six sessions in one repository, each a bar of what it cost: the work itself plus three kinds of waste, namely re-learning the repo, tools never used, and getting stuck in loops. Each of the first three sessions teaches TokenEconomizer one thing, in order: 1 micro-skills remember how the repo works (run tests with python -m pytest), 2 tool pruning skips tools never used here (Read and Edit kept, Notebook and Browser left out), and 3 failure-loop intervention spots loops and steps in (the same error three times meets a nudge to try another way). In the session after each lesson that waste shrinks, so the bars step down below a dashed line marking the cost without TokenEconomizer. It ends on results measured on SWE-Bench tasks: 18.4–30.9% lower mean cost across five agent–model combinations, cheaper than default in 30 of 30 repository × combination cells, and Pass@1 up in 4 of 5; per combination, cost 23.6% lower and Pass@1 +1.3 for Claude Code with Sonnet 5, 30.9% and −1.0 with Opus 4.8, 24.7% and +0.9 for Codex with GPT-5.6 Terra, 26.1% and +1.6 with GPT-5.6 Sol, and 18.4% and +2.6 for Copilot CLI with Sonnet 5.">
  </picture>
</p>

TokenEconomizer makes coding agents cheaper to run in the repositories you work in often,
without changing the agent itself. It learns from the sessions an agent has already run in a
repository, and uses that experience to cut waste in the sessions that follow. It has three
mechanisms:

- **Micro-skills: remember how the repository works.** Sessions keep rediscovering the same
  facts: a build step that must run first, the spelling of a command that works here
  (`python -m pytest` where `pytest` is missing, `npx tsc` where `tsc` is), an environment
  variable a command needs, where generated files live. Micro-skills learns such facts, in any
  language, from two sources: failures that repeat across sessions, and a model that reviews the
  recent sessions every *k* sessions (*k* = 3) and proposes facts. A fact is stated at the start
  of each session once three sessions have confirmed it, and dropped when later sessions
  contradict it.
- **Tool pruning: stop loading tools that go unused.** Every loaded tool's definition is sent with
  every request. A tool that goes unused over *p* prompts spread across at least *m* sessions, or
  over *s* sessions of any length (*p* = 10, *m* = 2, *s* = 5), is left out of the next sessions
  through the agent's own settings. One command brings it back.
- **Failure-loop intervention (the loop guard): step in when a turn is stuck.** When a turn (the
  agent's work on one prompt) keeps hitting the same failures, a judge model checks whether it is
  stuck. If the judge is at least *c* sure (*c* = 0.7), the agent gets a redirect (a short note,
  added to its context, to try another approach), at most *r* times per turn (*r* = 1). If the
  turn is still stuck after that, TokenEconomizer tells you how to stop it; it never stops a turn
  itself.

TokenEconomizer is a plugin for **Claude Code**, **Codex**, the **GitHub Copilot CLI** and **Pi**,
with experimental support for **opencode**. Each italic letter above is a setting, shown with its
default ([Settings](#settings)), and each mechanism can be turned on or off. The plugin announces
each action in one line, and if any part of it fails, your session carries on as if it were not
installed. Its model calls (the fact proposer, and the judge with the redirect it writes) run
through your own agent, on the same plan or login, and their cost is included in its reports.
What it learns stays on your machine, in `~/.tokeneconomizer`.

## Results

The paper ran five agent–model combinations on the same 277 SWE-Bench tasks from six repositories.
Each task ran as its own session, and each repository's tasks ran in order, starting with nothing
learned. Costs include every model call TokenEconomizer made. Within each repository and
combination, cost fell by 5–40%. The savings held on Web-Bench (16–21% lower) and on two
security-auditing benchmarks where every task is in a new repository (6–20% lower). The
[project page](https://tokeneconomizer.github.io) has interactive charts, per-repository numbers
and nine annotated runs, and [`experiments/`](experiments/README.md) reruns the SWE-Bench and
Web-Bench experiments.

## How it works

<p align="center"><img src="docs/assets/framework_overview.png" width="100%" alt="TokenEconomizer: the plugin keeps what it knows about a repository and applies micro-skills, tool pruning and failure-loop intervention to your unchanged coding agent; each finished session's log updates all three"></p>

Coding agents are built to finish tasks, not to keep them cheap. Every turn pays again for the
agent's instructions, every loaded tool, and the conversation so far. Developers use the same
agent on the same repository again and again, so much of that cost repeats: the same facts
rediscovered, the same unused tools sent, the same kinds of failing loops. TokenEconomizer leaves
the agent's model, weights and code alone and learns across a repository's sessions instead of
treating each one on its own, so whatever the plugin spends is paid back over the sessions that
follow. Four principles guide the mechanisms:

- **Work through what the agent already reads.** Facts enter the context at session start, and
  tools are removed through the agent's own settings, so nothing depends on the agent learning a
  new tool.
- **Count cost as it is billed.** Most tokens in a session are cached re-reads, so cost is
  computed with cache pricing, and it includes the plugin's own model calls.
- **Protect task success.** Facts form only from repeated evidence, tools are removed only after
  going unused, and the loop guard leaves alone a turn that is still making progress.
- **Keep every action reversible.** A fact that later sessions contradict is dropped, removed
  tools can be given back, and the loop guard only redirects and tells you: stopping a turn is
  your call.

## Quick start

You need one of these agents, signed in any way it supports, and Python 3.10 or newer on
`PATH`. The plugin needs no API key of its own and never handles credentials, so any plan or
login works.

### Install

Run these commands in the folder where you want to keep the clone. Claude Code, Codex, the
Copilot CLI and opencode run the plugin from the clone, so leave it in place. Then start the agent
in one of your repositories.

**Claude Code**

```sh
git clone https://github.com/microsoft/TokenEconomizer.git
claude plugin marketplace add "$PWD/TokenEconomizer"
claude plugin install tokeneconomizer@tokeneconomizer
```

Start `claude`, trust the folder (**Yes, I trust this folder**), and run
`/tokeneconomizer:status`, allowing its script if asked. Once per machine, and again after Claude
Code updates, run `/tokeneconomizer:toolprune refresh-catalog`.

**Codex**

```sh
git clone https://github.com/microsoft/TokenEconomizer.git
codex plugin marketplace add "$PWD/TokenEconomizer"
codex plugin add tokeneconomizer@tokeneconomizer
```

Start `codex`, choose **Trust and continue** for the folder, then at **Hooks need review**
choose **Trust all and continue**. The hooks take effect from your next Codex session, so quit
(`/exit`), start `codex` again, and check with `$tokeneconomizer:status`.

**Copilot CLI**

```sh
git clone https://github.com/microsoft/TokenEconomizer.git
copilot plugin marketplace add "$PWD/TokenEconomizer"
copilot plugin install tokeneconomizer@tokeneconomizer
```

Start `copilot`, choose **Yes, and remember this folder for future sessions**, and run
`/tokeneconomizer:status`, choosing **Yes** to run its script. Once per machine, and again after
Copilot updates, run `/tokeneconomizer:toolprune refresh-catalog`.

**Pi**

```sh
pi install git:github.com/microsoft/TokenEconomizer
```

Start `pi` and run `/te status`.

**opencode** (experimental)

```sh
git clone https://github.com/microsoft/TokenEconomizer.git
mkdir -p ~/.config/opencode/plugins
ln -s "$PWD/TokenEconomizer/plugin/opencode/tokeneconomizer.ts" ~/.config/opencode/plugins/
```

Start `opencode` and send a prompt, then check in the repository with
`~/.tokeneconomizer/bin/te --host opencode status`. opencode has no plugin commands, so the
plugin's commands run from a terminal.

If the install worked, the status command prints a short status block. `refresh-catalog`
records every tool a session loads (without a model call), so that tool pruning can consider all
of them. Keep the marketplace path absolute, as above: the Copilot CLI reads a relative path such
as `./TokenEconomizer` as the name of a GitHub repository.

To update:

| Agent | Update |
|---|---|
| Claude Code, Copilot CLI, opencode | `git pull` in the clone |
| Codex | `git pull` in the clone, then the `codex plugin add` line again |
| Pi | `pi update --extensions` |

**[`plugin/README.md`](plugin/README.md)** walks through each agent in more detail, including
uninstalling, using Copilot with your own model key, and troubleshooting.

### Supported versions

| Agent | Supported | Older versions |
|---|---|---|
| Claude Code | 2.1.300 to 2.1.310 | not supported |
| Codex | 0.153.1 to 0.164.0 | not supported |
| Copilot CLI | 1.0.83 to 1.0.102 | not supported |
| Pi | 1.2.0 to 1.3.0 | 0.99.x: load the extension by path (below) |
| opencode (experimental) | 1.19.5 and 2.2.0 | not tested |

The commands above were tested on the oldest and newest version in each range; newer versions
have not been tested yet.

- **Codex before 0.141.0** does not run plugin hooks at all.
- **Pi 0.99.x**: instead of `pi install`, clone the repository and start each session with
  `pi --extension /path/to/TokenEconomizer/plugin/pi/tokeneconomizer.ts`, using your clone's
  full path; `git pull` in the clone updates it.
- **opencode** support is experimental: it was tested on 1.19.5 and 2.2.0 only, and not in the
  2.x terminal UI.

### Everyday commands

Work as usual; the plugin needs nothing from you. To see or change what it does, use its
commands. They have the same names on every agent; only the way you type them differs:

| Agent | Type a command as |
|---|---|
| Claude Code, Copilot CLI | `/tokeneconomizer:<command>` |
| Codex | `$tokeneconomizer:<command>` |
| Pi | `/te <command>` |
| opencode | from a terminal: `~/.tokeneconomizer/bin/te --host opencode <command>` |
| a terminal, in the repository | `~/.tokeneconomizer/bin/te <command>` |

| Command | What it does |
|---|---|
| `status` | what it learned and did here, and what your sessions cost |
| `microskills` | the facts it injects, and those still forming |
| `toolprune` | the tools it left out, and the evidence (not on Pi or opencode) |
| `toolprune restore` | give them back; they will not be removed again |
| `config` | every setting in effect |
| `config set microskills=on` | turn a mechanism on (or `=off`) in this repository; add `--global` for every repository |

Inside an agent, a command costs one model turn; from a terminal it is free. The other commands
(`repos`, `doctor`, `config unset`, ...) and each agent's permission prompts are listed under
[Commands](plugin/README.md#commands).

## Settings

Tool pruning and the loop guard are on by default; with these defaults, the plugin calls a model
only when a turn shows signs of looping: the judge, and the redirect it writes if it finds the
turn stuck. Micro-skills is off by default, because its proposer adds model calls and how much it
saves depends on the repository and the work you do there. Each mechanism has its own switch
(`microskills`, `toolprune`, `loopguard`) that takes `on` or `off`, and the italic letters above
are these settings:

| | Setting | Default | What it sets |
|---|---|---|---|
| *k* | `microskills_propose_every` | 3 | sessions between runs of micro-skills' fact proposer |
| *p* | `toolprune_evidence` | 10 | prompts a tool must go unused before it is left out |
| *m* | `toolprune_min_sessions` | 2 | sessions those prompts must span |
| *s* | `toolprune_sessions` | 5 | or this many sessions, of any length |
| *q* | `toolprune_quiet_minutes` | 60 | minutes your sessions here must be idle before a deny list is written |
| *e* | `loopguard.envelope_min_samples` | 5 | turns here that ended well (no failing check after the last edit) before the loop guard acts |
| *c* | `loopguard.judge_confidence` | 0.7 | how sure the judge must be that a turn is stuck |
| *r* | `loopguard_nudges` | 1 | redirects per turn before the guard only tells you |
| *b* | `loopguard.backstop_mult` | 2.5 | how many times its usual length a churning turn may run before it is redirected without the judge |

Change them with `config set`, shown here in Claude Code's form (other agents type it as in
[Everyday commands](#everyday-commands)):

```text
/tokeneconomizer:config set microskills=on                 # turn micro-skills on
/tokeneconomizer:config set microskills_propose_every=5    # k = 5: propose facts less often
/tokeneconomizer:config set toolprune_evidence=20          # p = 20: wait for twenty unused prompts
/tokeneconomizer:config set loopguard_nudges=2             # r = 2: redirect twice before telling you
```

Tool pruning counts prompts so that long sessions weigh more, and requires *m* sessions so that a
single session never decides alone. It writes the deny list only once your sessions in the
repository have been idle for *q* minutes (or, at the latest, a day after the list formed): a
conversation resumed after its tools change must write its whole history to the prompt cache again
instead of reading it, and after an idle hour that cache has expired anyway.

Besides `on` and `off`, two modes are useful: `toolprune=propose` only proposes the deny list, and
nothing changes until you run `toolprune apply`; `microskills=envfacts` learns facts only from
repeated failures, with no model calls.

To change a single session, set an environment variable when you start the agent:
`TE_DISABLE=1 claude` turns the whole plugin off, and `TE_LOOPGUARD=off codex` turns off one
mechanism (likewise `TE_MICROSKILLS` and `TE_TOOLPRUNE`). Every setting and its default are
listed under [Settings](plugin/README.md#settings); each one's environment variable is `TE_` plus
its name in capitals.

## What it does on each agent

Micro-skills and the loop guard work the same way on every agent. Each agent learns on its own:
facts, tool evidence and the loop guard's sense of a usual turn are kept per agent and
repository, while settings are shared. Tool pruning acts through each agent's own settings, so
what it can leave out differs:

| Agent | Tool pruning leaves out | Written to |
|---|---|---|
| Claude Code | single tools | `.claude/settings.local.json` |
| Codex | capability packages | `.codex/config.toml` |
| Copilot CLI | whole MCP servers | `.github/copilot/settings.local.json` |
| Pi | nothing (Pi loads only four tools) | — |
| opencode | nothing yet | — |

Tool pruning adds only its own entries and never touches deny rules you wrote; a settings file it
creates is kept out of git (`.git/info/exclude`). On Claude Code, the session-start line that says
what it left out shows only in the detailed transcript (**Ctrl+O**), so check with
`/tokeneconomizer:toolprune`. `toolprune restore` removes the plugin's entries and nothing else,
and tools you give back are not removed again. If the plugin cannot edit a file safely (a
`.codex/config.toml` your repository commits, a settings file that is not valid JSON, a symlink
that leads out of the repository), the list stays a proposal and the session start says why;
`toolprune apply` tries again. **[`docs/PLUGIN.md`](docs/PLUGIN.md)** records how each agent's
hooks and settings were verified to behave, and **[`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md)**
how the package fits together.

### When a turn gets stuck

The loop guard first learns how long a turn in this repository usually runs: it waits until *e*
turns here have ended well, on their own and with no failing check after the last edit. After
that, a turn that shows signs of looping (the same failures repeating, or errors piling up) goes
to the judge. One case is redirected without the judge: a turn that runs past *b* times the usual
length while churning the same edits through the same failures. If a turn is still stuck after its
redirects, you see one line that ends with how to stop it:

> TokenEconomizer: this turn still looks stuck after a redirect (judge-stuck@0.82, 46 tool
> calls). Press Esc to interrupt it.

Where that line appears, and how to stop the turn, in the terminal UI and in a headless run
(`claude -p`, `codex exec`, `copilot -p`, `pi -p`, `opencode run`):

| Agent | Interactive: where it shows | How to stop | Headless: where it shows | How to stop |
|---|---|---|---|---|
| Claude Code | in Claude's reply | Esc | in the final reply | Ctrl+C |
| Codex | in the conversation | Esc, then `/stop` | not shown | Ctrl+C |
| Copilot CLI | in the conversation | Esc twice | on stdout | Ctrl+C |
| Pi | as a notification | Esc | on stderr | Ctrl+C |
| opencode | as a notification | Esc | on stderr | Ctrl+C |

- **Claude Code** shows a plugin's own lines only in its detailed transcript (Ctrl+O), so the
  plugin asks Claude to repeat this one in its reply; the model may word it differently or leave
  it out.
- **Codex**: Esc interrupts the turn, but a command it started keeps running until `/stop`.
  `codex exec` prints no hook messages.
- **Pi**: Ctrl+C ends a headless run, but a command it started runs on until it finishes.
- **opencode** 2.x prints the line to the opencode server's error output, not in its terminal UI.

In a headless run nobody may be watching, so a flagged turn runs until it ends or reaches the
agent's own limits; afterwards, `te status` counts the redirects and "still stuck" notices.

## Repository

| | |
|---|---|
| [`tokeneconomizer/microskills`](tokeneconomizer/microskills/) | Micro-skill synthesis and injection: facts learned from finished sessions |
| [`tokeneconomizer/toolprune`](tokeneconomizer/toolprune/) | Tool pruning: unused tools and Codex capability packages |
| [`tokeneconomizer/loopguard`](tokeneconomizer/loopguard/) | Failure-loop intervention: the per-call guard and its per-repository envelope |
| [`tokeneconomizer/trace`](tokeneconomizer/trace/) | Each agent's session log, read into one shape |
| [`tokeneconomizer/plugin`](tokeneconomizer/plugin/) | The runtime the hooks and the `te` command run |
| [`plugin`](plugin/) | The installable plugin: manifests, hook files, launchers, slash commands, the Pi extension, the opencode plugin |
| [`experiments`](experiments/) | The harness, launchers and task sets behind the paper's results |
| [`docs`](docs/) | `PLUGIN.md` (design, verified agent behavior) and `ARCHITECTURE.md` (how the package fits together) |
| [`tests`](tests/) | Offline tests for the package and the plugin |

The package is standard-library only. Run the tests with `python -m pytest tests` (add
`experiments/tests` for the benchmark side), and build a self-contained plugin bundle with
`python3 scripts/build_plugin.py --out dist/marketplace`.

## Reproducing the experiments

The code behind the paper's results -- a harness that runs Claude Code, Codex and the Copilot CLI
on SWE-Bench and Web-Bench, the launchers, and the evaluated task sets -- is in
**[`experiments/`](experiments/README.md)**, whose README gives the setup and one command per
result. It is not part of the installed plugin; the two share only `tokeneconomizer/`.

## Citation

```bibtex
@misc{li2026tokeneconomizer,
  title         = {{TokenEconomizer}: Experience-Driven Black-Box Cost Control for Coding Agents},
  author        = {Li, Aaron J. and Xu, Weijia and Singh, Chandan and Chen, Zixiao and
                   Inala, Jeevana Priya and Siska, Charlotte and Tamersoy, Acar and Yu, Bin and
                   Stoica, Ion and Galley, Michel and Gao, Jianfeng},
  year          = {2026},
  eprint        = {2610.22732},
  archivePrefix = {arXiv},
  primaryClass  = {cs.CL},
  url           = {https://arxiv.org/abs/2610.22732}
}
```

## License

Apache 2.0; see [`LICENSE`](LICENSE).

## Docs
### docs/ARCHITECTURE.md
# Architecture

The three mechanisms (see the [main README](../README.md)) know neither the agent, the harness
nor the task domain. Everything specific to those enters through a few small interfaces in the
standard-library-only package `tokeneconomizer`:

- `tokeneconomizer.trace` is the one place a saved session log is read (`load_trajectory`,
  `call_cwds`, `tool_usage`, `parse_catalog`), with one module per agent's format. A new agent
  needs a reader here and nothing else.
- `tokeneconomizer.ledger` and `tokeneconomizer.pricing` are the one definition of cost.
  Mechanisms record their per-task overhead (in the plugin, a session counts as one task); the
  plugin's session ledger and the experiments' aggregation read it back through the same modules,
  so recorded and reported cost cannot drift.
- `tokeneconomizer.domain.DomainAdapter` is the interface to the task domain: reading a session,
  the tools pruning protects or excludes, a trajectory's loop signals, the task text for the
  optional judge, and the micro-skill vocabulary. A new domain is a new adapter, with no change
  to a mechanism. The plugin's adapter is `tokeneconomizer.plugin.adapter.LiveAdapter`; the
  benchmark adapters (SWE-Bench, Web-Bench, CredData, ReposVul) are in
  `experiments/te_bench/adapters/`.
- `tokeneconomizer.stage.Stage` is the set of hooks a mechanism offers whoever runs it:
  `before_task`, `build_tools`, `run_kwargs` and `after_task`.

Two callers run the stages, and the mechanisms import neither:

- **The plugin** (`tokeneconomizer.plugin`) runs them inside a person's sessions through each
  agent's hooks: `PrefixStage` and `ToolingStage` over each finished session, and the loop guard
  (`loopguard.TurnGuard`) one tool call at a time. What happens at each hook, and what was
  verified on each agent, is in [`PLUGIN.md`](PLUGIN.md).
- **The experiments** (`experiments/te_bench`) run them over benchmark task streams: the
  `Economizer` facade wires the three stages around one adapter, and
  `te_bench.runner.AgentRunner` is the interface to a task-execution harness (Docker, an agent
  CLI, a grader), with `experiments/te_harness` as the implementation the paper used. The
  benchmark-only controllers -- `SpiralStage`, the streamed `NudgeGuard` and the Codex finalize
  policy -- live there too. See [`experiments/README.md`](../experiments/README.md).

`tests/test_plugin_package.py` pins both boundaries: the mechanisms never import
`tokeneconomizer.plugin`, and nothing under `tokeneconomizer/` imports `experiments/`.

### docs/PLUGIN.md (excerpt — first ~400 lines; full file 51KB)
# The plugin: design and verified agent behaviour

How the plugin runs the three mechanisms inside your own Claude Code, Codex, Copilot CLI and Pi
sessions, through the hooks (on Pi, the extension events) each agent exposes: what it does at
each hook, what differs from the experiments and why, the agent behaviour each choice rests on,
where its state lives, and its known limitations. The code is `tokeneconomizer/plugin/` (what
the hooks run) and `plugin/` (the packaging for each agent). To install and use it, see
[`plugin/README.md`](../plugin/README.md).

---

## 1. What it does, hook by hook

| Hook | What the plugin does | Mechanism it drives |
|---|---|---|
| `SessionStart` | Injects the repository's micro-skills (a cached render) as `additionalContext`, at a new start, and on a Copilot resume the text that session started with (§3); announces changed facts, tools the deny list newly left out, or, under `toolprune=propose` (or when `auto` could not write the file), a proposal still waiting, each in one `systemMessage` line; folds any earlier session whose end was never seen | microskills |
| `UserPromptSubmit` | Opens a prompt-turn for the loop guard | loopguard |
| `PostToolUse` | Folds the call into the turn's guard; delivers a redirect as `additionalContext`, then, if the turn is still stuck, a one-line notice to the person (on Claude Code, also as context asking the model to repeat it); never stops the turn | loopguard |
| `PostToolUseFailure` | The same, for a call that failed (Claude Code and Copilot report a failed call only here); the answer names this event, as Claude Code requires | loopguard |
| `Stop` | Closes the turn; a turn that *ended green* feeds the per-repository envelope | loopguard |
| `SessionEnd` | Hands the session to a detached `te fold` and returns at once | microskills, toolprune, ledger |

`te fold` runs the **same classes the experiments ran** over the finished session's log:
`PrefixStage` (with micro-skills on, the free envfacts layer under the proposer) and
`ToolingStage` (evidence pruning). The loop guard (`loopguard.TurnGuard`) is the benchmark
harness's `NudgeGuard` control flow — `SpiralState.update`, `assess_abort`, `is_stuck`,
`nudge_text`, the cumulative backstop — one tool call at a time. None of the thresholds were
re-tuned. Three things it adds:

* It counts **edits made through the shell**: `sed -i`, `perl -pi`, a redirect or `tee` into a
  source file, an inline Python script that writes a file back, `patch`/`git apply`, Codex's
  `apply_patch <<'PATCH'`. The loop
  state counts only edit tools, and agents that edit through Bash then looked as if they had
  edited nothing.
* **The redirect always comes before the still-stuck notice.** The benchmark ladder checks a
  hard backstop (a multiple of the learned envelope: 2.5 × at the default level, 1.8 × at
  `aggressive`) before anything else. With the large envelopes of the benchmark streams, the
  backstop lay well past the stuck rule's own floor (20 calls at the default level, 14 at
  `aggressive`), and the redirect came first. An interactive repository learns a small envelope.
  Its backstop then falls inside that floor, so the first call that counts as stuck has also
  tripped the backstop, and the turn would get the notice without ever being redirected. Now an
  unspent redirect goes first, and the notice needs a second stuck segment after it.
* The **stuck judge and nudge writer run in a detached `te judge` job**, not in
  the hook. The hook starts the job and returns; a later PostToolUse picks up the verdict, with
  the redirect already written. Each job's spend is charged to the ledger when it is spent.

Every hook fails open: any error becomes an empty output (no change) and a traceback in
`~/.tokeneconomizer/errors.log`. The hooks are stdlib only, and none waits on a model call.

## 2. What changes relative to the experimental setting

| | Experiments | Plugin | Why |
|---|---|---|---|
| Unit of work | one benchmark task | a **session** for micro-skills and tool pruning; a **prompt-turn** for the loop guard | In interactive use a person already splits work into short turns. A whole session folded as one trajectory would look stuck merely by being long |
| Learning signal | the official grader's `resolved` | the envelope learns from turns that **ended green**: the agent stopped on its own, was not stopped by the guard, and no verification after its last edit failed | There is no grader. Micro-skills and evidence pruning never needed one |
| Injection channel | a prefix on the task prompt | `SessionStart` `additionalContext` | Verified to reach the model (§3) |
| Tool removal | `--disallowed-tools` / Codex config at launch | a **deny list**, applied by default once the evidence forms it and the repository's sessions have been idle longer than a prompt cache lives (§3), and announced at the next session start (`toolprune=propose` waits for approval instead), written to the repository's own settings file — tools in `.claude/settings.local.json`, Codex capability packages in `.codex/config.toml`, Copilot MCP servers in `.github/copilot/settings.local.json` — effective from the **next** session | The plugin launches nothing. A session keeps the tools it started with, but a conversation resumed after a change sends the new ones, re-writing its cached prefix, hence the idle wait. Each agent's file can express a different unit (§3) |
| Pruning candidates | `toolprune.tools.INAPPLICABLE_TOOLS` — orchestration, Q&A, plan mode, web — "inapplicable by construction" for a sealed headless task | nothing is inapplicable by construction; only **evidence** (never used, and unused over `toolprune_evidence` prompts (10) across at least `toolprune_min_sessions` sessions (2), or over `toolprune_sessions` sessions (5)) proposes a tool, and a person's tools — AskUserQuestion, plan mode, sub-agents, the web — are protected | A person asks questions, plans and browses in a real session. A deny rule the plugin wrote for a tool that has since become protected is given back at the next fold |
| Network | every arm, baseline included, carries an answer-key guard — a `PreToolUse` hook and an `/etc/hosts` block refuse the benchmarks' upstream sources — and drops the web tools | **no guard**: no `PreToolUse` hook (on Pi, no `tool_call` handler), no blocked command or host; the web tools stay | A benchmark's answer is a fetch away. A real session has no answer key, and the web is part of the work |
| Who decides a turn is stuck | in the guard's arms, the trace judge, woken by the rule gate or by a turn past the envelope (the agents ran under a turn cap); without a judge, the strict rule | **always the judge** when the guard is on, woken only by a sign of trouble (a repeated failure, or dense errors) after `min_turns` calls, and never before the repository has an envelope; a `productive` or ambiguous verdict spares the turn (at the `aggressive` preset an ambiguous one past the envelope gets the redirect). The hard backstop (far past the envelope AND the strict stall rule) still acts without it. While the agent's model calls are paused, the judge gives no verdict and only the backstop acts | The rule alone redirected turns that had found their cause and were working around it (§5); interactive turns outrun a small envelope all the time, so the envelope alone wakes nothing |
| Redirect | kill the agent, resume it with a continuation prompt | a mid-turn reminder attached to the tool result | Different intervention, so its effect is not inherited from the experiments |
| Still stuck after the redirect | terminal abort, in autonomous runs | a one-line **notice** to the person, ending with how to stop the turn on that agent and in that mode (§3); the plugin never stops a turn, and `loopguard: stop` is read as `nudge` | Not every agent's hooks can stop a turn (Codex and Copilot ignore `continue: false`), and the person decides: the benchmark guard's own design note says "interactive callers should map it to a hand-off" |
| Micro-skills' reading | a domain vocabulary per benchmark (Python/git, Node/web); the proposer's digest counts edited Python files, lists test invocations and flags Python import errors, and its prompt leads with the test command | **generic**, whatever the repository: every ecosystem's interpreters, package tools and test runners at once, builds and checks (`make`, `tsc`, `npm run build`, `cargo check`, ...) as their own intent, every edited file, and a language-neutral digest (failing commands with a normalized error line, paths relative to the repository) and prompt, with tests one topic among several. `vocabulary=python-git` or `node-web` selects an experiment's | A person's repository may be in any language, or several; the experiments keep the paper's reading (its prompt is pinned by a test) |
| Micro-skills | on in the arms that measured it: the proposer every 5 tasks (on Codex, every 10, over the free layer) | **off by default**; `on` runs the free layer under the proposer, every `microskills_propose_every` sessions (3 by default: after the 2nd, 5th, 8th, ...), since a real session usually carries more work than one benchmark task | The proposer calls a model on the person's plan, and what it injects is derived from command output a repository controls: turning it on is the person's call. In the experiments the free layer alone formed almost nothing once the harness set each environment up properly, so `on` keeps the proposer |
| Optimizer model | the agent's own model, so overhead could not look cheaper than its arm | the cheapest capable model on the user's own agent CLI (`paid_model`; when empty, `haiku` on Claude Code, the agent's default model on Codex and Pi, and on Copilot a concrete `COPILOT_MODEL` or a BYOK provider's Haiku): the proposer when micro-skills is on, the loop guard's judge and redirect writer whenever the guard is on | Every call is still charged to the session ledger |

## 3. Verified agent behaviour

What the code relies on about each agent, and how it was checked. Each block names the version
and date it was verified on; §5 says what has not been exercised.

**Claude Code 2.1.286 — verified with a local plugin (`--plugin-dir`) on Haiku, 2026-09-30:**

* `SessionStart` `additionalContext` reaches the model. End to end through this plugin: four
  synthetic sessions taught it that bare `pytest` is missing; a real `claude -p` session in that
  checkout then answered "Tests should be run with `python -m pytest` since `pytest` command is
  not found in this environment", and the detached fold priced that session from its transcript.
* `PostToolUse` `additionalContext` is followed **in the same turn** — no restart needed.
* `PostToolUse` `{"continue": false}` halts the loop after the current tool (one of three
  requested commands ran) and the session ends cleanly. (The plugin no longer uses it: it stops
  no turn on any agent.)
* A bare-name `permissions.deny` rule **removes the tool from the session's tool list**, the same
  list `--disallowed-tools` produces, whether the rule comes from `--settings` or from a
  project's `.claude/settings.local.json`. A plugin's own `settings.json` cannot carry deny rules
  (only `agent` and `subagentStatusLine` take effect), which is why the deny-list writer edits the
  project-local file (by itself under `toolprune=auto`, on `toolprune apply` under `propose`).
* An interactive transcript does not record the tool list a session loaded. Without a recorded
  catalog, evidence pruning sees only the tools Claude Code defers (one listing line each) and
  those a session used; `te toolprune refresh-catalog` records the always-loaded set, with no model
  call.
* **A call that fails fires `PostToolUseFailure`, not `PostToolUse`** (verified on 2.1.299,
  2026-10-14): `{tool_name, tool_input, tool_use_id, error, is_interrupt, duration_ms}`, where
  `error` is the text the model saw (`"Exit code 2\nls: cannot access ..."`). Until the hook
  file registered it, the guard never saw a failing call: live sessions counted 39 of 47
  calls, and a failing test run after the last edit could not make a turn end red.
* Bash `tool_response` is `{stdout, stderr, interrupted, isImage, noOutputExpected}` — **no exit
  code**, so on Claude Code failure is read from the output text, as the loop state's detectors do.
* Interactive transcripts parse with the existing `trace.load_trajectory`, but write **one entry
  per content block, each repeating its message's usage**, so an assistant message id can repeat
  many times; the ledger de-duplicates by message id. Subagents log to
  `<session>/subagents/`, and their calls and tokens are counted with their session.
* A `claude -p` session's hooks see `CLAUDE_CODE_SESSION_ATTENDED=0` and
  `CLAUDE_CODE_ENTRYPOINT=sdk-cli`; `mode: auto` uses them to tell headless from interactive.

**Codex 0.153.1 — verified live with `codex exec`** (`gpt-5.6-sol`, direct OpenAI API key, an
isolated `CODEX_HOME`, `--dangerously-bypass-hook-trust`; 2026-09-30):

* All five hooks fire — `SessionStart`, `UserPromptSubmit`, `PostToolUse`, `Stop`, `SessionEnd` —
  and both `SessionStart` and `PostToolUse` `additionalContext` reach the model (a probe's
  codeword and its mid-turn instruction both came back in the answer).
* `PostToolUse` fires for shell commands as `tool_name: "Bash"`, `tool_input: {"command": "..."}`,
  with `tool_response` a plain string and no exit code. Issue #38850 (PostToolUse not firing in
  Code Mode) did not reproduce on this build and model.
* The plugin installs through Codex's own commands: `codex plugin marketplace add <dir>` reads
  `.claude-plugin/marketplace.json`, and `codex plugin add tokeneconomizer@tokeneconomizer`
  **copies** the plugin into `$CODEX_HOME/plugins/cache/…` and enables it, dropping the `lib`
  symlink to the package; the bootstrap then finds the package in the checkout `config.toml`
  records as the marketplace's `source` (verified 2026-10-14). `"${PLUGIN_ROOT:-…}"` in the hook
  command resolves to that copy.
* End to end: four synthetic rollouts taught it that bare `pytest` is missing; a real Codex
  session then answered "Run tests with `python -m pytest …` because the `pytest` command is
  unavailable here", the guard folded the turn's tool call, and SessionEnd's detached fold priced
  the session from its rollout: fresh, cached, written and output tokens matched the stream's own
  usage block, converted as `te_harness.codex.row_usage` converts it.
* Hooks inherit the agent's environment, including a parent Claude Code session's `CLAUDE_*`
  variables, which is why the host is detected from the payload (`turn_id`), never the env.
* `CODEX_HOME` under `/tmp` makes Codex refuse to install its helper binaries, and its sandbox then
  fails every command (`codex-linux-sandbox: No such file`); keep it out of temporary dirs.
* Codex also turns a plugin's `commands/` folder into skills of its own (`source-command-status`,
  …), which listed every command twice in its skill picker beside `codex-skills/`. The slash
  commands therefore live in `slash-commands/`, which the Claude Code and Copilot manifests name
  and Codex does not read (verified 2026-10-17).
* Codex lists a plugin's skills under the plugin's name, `tokeneconomizer:<skill>` (every release
  from 0.131.0, the first with `codex plugin add`, to 0.163.0), and in `codex exec` a `$` mention
  matches only that full name: `$tokeneconomizer-status`, the name these guides once gave, reached
  no skill. The skills are therefore named after the commands, so `$tokeneconomizer:status` reads
  as `/tokeneconomizer:status` does on the other agents (verified 2026-10-21, with arguments:
  `$tokeneconomizer:config set loopguard=off --global`). Releases before 0.141.0 install the
  plugin but never run its hooks (tried: 0.131.0, 0.135.0, 0.140.0).
  A question in plain words is a weaker route: on `gpt-5.4-mini`, *"what has TokenEconomizer
  learned here?"* ran the skill's command in none of six `codex exec` runs, under either naming
  (the model read the plugin's state files instead), so the guides name the skill.

Hooks are **trust-gated**: skipped until approved in `/hooks` (stored as
`[hooks.state.<key>].trusted_hash`), unless the run passes `--dangerously-bypass-hook-trust`.
That gate, kebab-case event names and an argv-list handler are why `te_harness` once recorded
that Codex "honours no PreToolUse hook"; with PascalCase events, a command string and trust,
every hook fires. Not exercised, from the binary's schemas and the docs: `PostToolUse`
`continue: false` does **not** stop a Codex turn mid-flight, one reason the guard's last rung is
a notice on every agent, matching the Codex-native finalize policies, which never abort. Code
Mode presents one `exec` tool with nested descriptions and defers MCP tools, so Codex pruning
works on capability packages (below), not on single tool schemas.

**Codex pruning — verified on 0.153.1, 2026-10-07** (`codex debug prompt-input` renders a
session's prompt input locally, with no model call; `codex features list` prints the effective
feature flags):

* A project's `.codex/config.toml` is read **only in a trusted project**. The same toggles
  changed the rendered prompt input under a `CODEX_HOME` that trusted the checkout, and changed
  nothing in an untrusted one, including a subdirectory of a trusted path. `te --host codex
  toolprune apply` checks trust and runs `codex features list` to confirm.
* The project-local toggles for `collaboration` (`[agents] enabled`, `[features] multi_agent`,
  `include_collaboration_mode_instructions`), `goals` and `image_media` take effect. `goals` and
  `view_image` remove declarations inside the code-mode tool description, which the render does
  not show, so `toolprune measure` understates them, and its output says so.
* `[[skills.config]] enabled = false` hides the bundled skills listing from the user-level
  config only. A per-repository decision does not belong there, so `skills` is not offered.
* The plugin writes each toggle as a line marked `# tokeneconomizer:<capability>` into the
  file. It never overrides a key you already set, and `restore` removes exactly its own lines.
* Code mode routes every call through one `exec` tool (`tools.view_image(…)`,
  `tools.web__run(…)`), recorded as `response_item` `custom_tool_call` records, not as rollout
  items. The fold therefore reads a capability trace that includes them.
* In a live session (gpt-5.6-sol on a Codex login), after `te --host codex toolprune apply
  collaboration goals image_media` the model reported no sub-agents, image viewer or goals, and
  could no longer view an image in the repository; `toolprune restore` returned the folder to its
  earlier state. Codex loaded those runs' hooks from the repository's `.codex/hooks.json`. A run
  trusts a project with `-c 'projects={"<path>"={trust_level="trusted"}}'`; the dotted `-c` form
  does not take.

**Copilot with a real model — 2026-10-07, over BYOK.** These checks ran on Copilot's BYOK mode
(`COPILOT_PROVIDER_TYPE=anthropic`, `_BASE_URL`, `_API_KEY`) with `claude-haiku-4-5`, through
`te --host copilot probe` (`plugin/probe.py`, which any user can run on their own setup):

* **Settings apply only in a trusted folder.** Copilot ignores a repository's `.github/copilot`
  settings outside its `trustedFolders`: a deny list applied in an untrusted directory under
  `/tmp` changed nothing, and a local capture showed the same file taking effect under a trusted
  folder. `toolprune apply` therefore warns about an untrusted folder and confirms the effect with a
  local capture, `doctor` reports trust, and the probe builds its repository inside a trusted
  folder.
* Copilot's `session.shutdown` records the request's tool-definition size as
  `toolDefinitionsTokens`; the probe reports it before and after the deny list.
* **Usage under BYOK** keeps the grand-total form: with an Anthropic provider, `inputTokens`
  includes the `cacheWriteTokens`, which the ledger splits out.
* **The plugin's own model calls under BYOK.** With `COPILOT_MODEL=auto` (the subscription's router) in the
  environment, `copilot -p` without a model answered nothing. The side call now names a model:
  `paid_model`, else a concrete `COPILOT_MODEL`, else `claude-haiku-4-5` on an Anthropic
  provider. It answered, and was priced from its own session log. The local capture behind
  `refresh-catalog` and `measure` mimics the person's model family, so it records the same
  built-in tools (`edit`/`create` for Claude models, not `apply_patch`). Copilot 1.0.83 does not
  pass its `COPILOT_PROVIDER_*` variables to the hooks, so with BYOK set through them the side
  calls run signed out; they answer nothing and say so in `errors.log`.

**GitHub Copilot CLI 1.0.83 — verified live, 2026-10-07**, against a scripted OpenAI-compatible
endpoint on localhost (Copilot's BYOK mode, `COPILOT_PROVIDER_BASE_URL`). Every request the CLI
built was recorded, so whether a hook's output reached the model was read off the request
itself, with no model and no quota:

* Copilot loads a Claude-format plugin, and prefers `.github/plugin/plugin.json` to
  `.claude-plugin/plugin.json`: with both present, only the hook file the first one names
  ran. That is how the plugin gives Copilot its own `hooks/copilot-hooks.json` (`--host
  copilot`) while Claude Code keeps `hooks/hooks.json`.
  `copilot plugin marketplace add <checkout>` and `copilot plugin install` load the plugin
  live from the checkout ("nothing was copied"), and the installed copy's hooks all fired.
* PascalCase events receive Claude-shaped snake_case payloads: `session_id`, `cwd`,
  `hook_event_name`. `SessionStart` has `source: "new"`, and there is no turn id. Only `Stop`
  carries `transcript_path` (`~/.copilot/session-state/<id>/events.jsonl`). Tool names are
  Claude's (`Bash`, `Read`). A shell result is `tool_result.text_result_for_llm`, ending in
  `<shellId: N completed with exit code X>`. A failed tool fires `PostToolUseFailure` with an
  `error` string.
* Context reaches the model only as a **top-level `additionalContext`**, on `SessionStart`,
  `UserPromptSubmit` and `PostToolUse` (the last as "Additional guidance from postToolUse
  hooks"). `hookSpecificOutput.additionalContext` is ignored.
* `continue: false` from `PostToolUse` did **not** stop a turn: all three scripted calls ran.
  As on Codex, the guard's last rung is a notice.
* The session log is the `tool.execution_*` stream the trace seam already reads. Usage arrives
  in `session.shutdown` (`modelMetrics[].usage`), written just after the `SessionEnd` hook
  returns, so the detached fold waits for it. `inputTokens` is the grand input total: a scripted
  4 × (1,000 prompt, 600 cached) became `inputTokens` 4,000 and `cacheReadTokens` 2,400.
* End to end, through the installed plugin: four sessions that hit "bare `pytest` is missing"
  taught it the fact, and in the sessions after them the fact was in the request the model
  received. Every session was folded and priced from its own `session.shutdown`.
* **The interactive TUI** (driven in a pseudo-terminal, same local endpoint). `SessionStart`
  fires lazily, at the first prompt; `SessionEnd` fires **once per session**, at `/exit`, not per
  prompt. `systemMessage` is **never shown**, so a notice was invisible until the plugin printed
  it as a `{"type": "progress", "message": …}` line ahead of its JSON. Copilot displays that as a
  status line (verified on SessionStart, UserPromptSubmit and PostToolUse), and the final object
  still applies. Plugin slash commands **do** run in the TUI, as skills. `-p` does not expand
  them. Copilot substitutes only `$ARGUMENTS` in a command's text: `${CLAUDE_PLUGIN_ROOT}`,
  `${PLUGIN_ROOT}`, `${COPILOT_PLUGIN_ROOT}` and `{{plugin_root}}` arrive literally, and its shell
  exports none of them. So every session start now keeps a launcher at
  `~/.tokeneconomizer/bin/te`, and the commands fall back to it when the substituted path is not
  there. Through it, `/tokeneconomizer:status` printed Copilot's status in Copilot, and Claude
  Code's still printed Claude's.
* A side effect to know when scripting Copilot's TUI: under an editor's terminal (`TERM_PROGRAM`
  set), its first run offers to add a shift+enter binding and writes that editor's
  `keybindings.json` if accepted.
* Tool pruning. Copilot has no persistent per-tool filter: `--excluded-tools` is a launch flag,
  and `permissions.deny` refuses a call but leaves the schema in the request. What does work,
  from the repository's `.github/copilot/settings.local.json`, is `disabledMcpServers`: listing
  the built-in `github-mcp-server` removes all of that server's tools from the request.
  `githubMcpTools`, `disabledSkills` and `builtInAgents` changed nothing. The plugin therefore
  proposes a server only when none of its tools was used. With the catalog recorded
  (`refresh-catalog`, captured the same way, with no model call), five sessions that never used
  the GitHub tools produced that proposal, and the next session's request no longer carried the
  server's tools.

**Pi 0.99.2 — verified live with `pi --print`** (`@earendil-works/pi-coding-agent`, the
extension loaded with `--extension`, gpt-5.6-sol through an `openai-responses` provider in an
isolated `PI_CODING_AGENT_DIR`):

* Pi has no hook protocol; `plugin/pi/tokeneconomizer.ts` speaks the dispatcher's on Pi's
  behalf — `session_start`, `before_agent_start`, `tool_result`, `agent_end` and
  `session_shutdown` each become one `te-hook --host pi` call — and applies the answers with
  Pi's own levers: a system-prompt section, a steering message, a UI notice.
* End to end: four synthetic Pi session files taught it that bare `pytest` is missing; in a real
  session the `<tokeneconomizer>` section appeared in the session's recorded system prompt, the
  model answered "Tests should be run with `python -m pytest …` because the `pytest` command is
  unavailable here", the guard folded its `bash` call, and the detached fold priced the session
  from Pi's own session file.
* The section is re-applied on every prompt: Pi diffs prompt sections between runs and records
  the change, so one left out would be recorded as removed. Unchanged, it adds nothing after
  the first prompt.
* Pi's bash result carries a real exit code (`structuredContent.exit_code`), which the
  ended-green proxy uses (unless another command's status replaced it: 2026-10-26, below); its
  session file is a tree, and only the active branch is read.
* Not exercised live here: a nudge (`sendMessage` with `deliverAs: "steer"`, since exercised:
  2026-10-21 and 2026-10-26, below) and a stop (`ctx.abort()`, since removed: the plugin no
  longer stops a turn). Tool pruning does not apply: Pi declares four tools by default.

**Pi 1.2.0 — verified live, 2026-10-14** (Haiku 4.5 through Pi's built-in OpenRouter provider,
set as the default provider and model in an isolated `PI_CODING_AGENT_DIR`, as a Pi user's own
settings would be):

* `pi install` of the repository root — the manifest a `git:` source reads after cloning —
  listed the package and loaded the extension. In a `--print` session its events reached the
  dispatcher, the turn closed green, the session folded and was priced from Pi's own session
  file, and `errors.log` stayed empty.
* `/te status` answered as a `notify` over RPC (the terminal UI's notice), and on stderr in
  print mode, leaving stdout to the reply.
* One of the plugin's own model calls — `pi --print --mode json` with no tools, extensions, skills, prompt
  templates, context files, MCP servers or saved session, and no `--model` — ran on the default
  model and returned its text and usage; the plugin's own extension did not load inside it. Pi
  0.99.2 rejects `--no-mcp`, so the call retries without it.
* Not yet exercised: `pi install git:github.com/…` against GitHub itself, which needs the
  root manifest pushed.

**End to end, as a new user, 2026-10-14** — on each agent a fresh home followed `README.md` and
this plugin's guide step by step (Claude Code 2.1.300, Codex 0.153.1, Copilot CLI 1.0.83, Pi
1.2.0; every model through OpenRouter; a small Python repository where `pytest` is missing and
`python -m pytest` works):

* Every agent: native install, hooks firing in new sessions, every session folded and priced,
  facts injected and changing the first test command, every command and its earlier name,
  settings under old and new names, uninstall leaving no hook running.
* The deny list end to end on Claude Code (20 → 10 tools), Codex (`codex debug prompt-input`
  7,021 vs 10,397 characters) and Copilot (a user MCP server gone from the next session);
  `restore` gave each back and kept the person's own entries.
* The loop guard's redirect reached the model mid-turn on all four; on Pi a `steer` message, and
  with `loopguard=stop` a headless turn ended at the next stuck verdict (nudged at call 17,
  stopped at 35) — the first live check of both on Pi. On Codex and Copilot the second fire is
  a notice. (Since 2026-10-21 the second fire is a notice on every agent; see below.)
* The plugin's own model calls ran through each agent's own CLI (Copilot's only off BYOK, above) and were
  charged to the ledger, without recursing into the plugin.
* Pi's real git install (a local git daemon standing in for GitHub): cloned, `npm install`ed,
  listed, loaded; `pi update --extensions` fast-forwarded it; `pi remove` removed it.

**Again as a new user, interactively, 2026-10-21** -- one fresh home for all four agents (Claude
Code 2.1.306, Codex 0.163.0, Copilot CLI 1.0.101, Pi 1.3.0; every model through OpenRouter),
the main README's Quick start typed as written. `git clone https://github.com/microsoft/…` and
`pi install git:github.com/microsoft/…` ran unchanged, a `url.insteadOf` in the new user's
`~/.gitconfig` pointing them at a local repository of the tree. Each agent then ran in its own
terminal UI: the first-run prompts, every Everyday command, the Update row, and a session that
ended and was folded and priced. What the run showed:

* Claude Code asks a new user to trust the folder (**Yes, I trust this folder**); its default
  auto mode then ran the plugin's script with no prompt.
* Codex asks for the folder (**Trust and continue**), then **Hooks need review**: **Review
  hooks**, **Trust all and continue**, or continue without them. Its default sandbox keeps
  `~/.tokeneconomizer` read-only, and `$tokeneconomizer:config set …` failed with a traceback
  until the skills that change state asked to leave the sandbox (`sandbox_permissions:
  require_escalated`); Codex now asks the user, and `te` refuses a change it could only half
  make. `/exit` keeps a session open to `codex resume` and sends no `SessionEnd`, so such a
  session is folded at a later session start once quiet; `codex debug prompt-input` sends a
  `SessionEnd` for a thread that never started, which the plugin now ignores.
* Copilot offers **Yes, and remember this folder for future sessions**, which a deny list in
  `.github/copilot` needs. It substituted a slash command's arguments into `$ARGUMENTS`, yet the
  model ran `config show` for `config set loopguard=off` three times: the command's text said
  "use `show` when no arguments were given" and "do not run `set` … unless those words appear in
  the arguments above". Rewritten to name the typed arguments plainly, it ran what was typed.
* Pi announced `pi update --extensions` itself when the repository moved on, and `/te` answered
  in its terminal UI with no model call.

**The loop guard on every agent and mode, 2026-10-21** (Claude Code 2.1.306, Codex 0.163.0,
Copilot CLI 1.0.101, Pi 1.3.0; every model through OpenRouter): each agent ran a provoked loop
(an exercise of twelve failing edit-and-test cycles, with a small seeded envelope and pinned
thresholds), in its terminal UI and headless.

* All four got the redirect and then, once, the still-stuck notice; none was stopped.
* Where the notice appears: Claude Code, only in the detailed transcript (Ctrl+O), as
  "PostToolUse:Bash says: …", and in `claude -p` only as a `hook_response` event of
  `--output-format stream-json --verbose`; Codex, in the conversation ("↳ Hook · …"), and nowhere
  under `codex exec`; Copilot, in the conversation and on stdout under `-p`; Pi, as a notification
  and on stderr under `-p`. The redirect's own announcement showed only in Claude Code's detailed
  transcript, on `copilot -p`'s stdout and on `pi -p`'s stderr.
* How a person stops a turn, each checked on a running `sleep`: Claude Code, **Esc** (the command
  is killed too); Codex, **Esc** interrupts the turn but its command runs on as a background
  terminal until `/stop`; Copilot, **Esc** twice; Pi, **Esc**. Headless, Ctrl+C ends `claude -p`,
  `codex exec` and `copilot -p` with their commands, and `pi -p` while its command, started
  detached, runs on until it finishes. The notice ends with the agent's way (`hosts.stop_hint`).
* Then, since Claude Code hid its own line, the plugin there also asks the model to repeat the
  notice word for word (`hosts.relay`). Claude Haiku 5.5 opened its next message and its final
  reply with it, in the terminal UI and under `claude -p`, whose text output then began with it.
  Claude Code drops an answer to a failed call that names `PostToolUse` ("Hook returned
  incorrect event name: expected 'PostToolUseFailure' but got 'PostToolUse'"), so an answer
  names the event it answers. Answering a failed call, the hook's own line also showed under the
  call without Ctrl+O.
* Telling headless from interactive: Claude Code's environment says so, and Pi's extension; Codex
  only in its rollout's first record (`source: "exec"`); Copilot only in its own command line
  (`copilot -p`), its payloads, environment and session log being the same in both modes.
* Codex 0.163.0 edits with `apply_patch <<'PATCH'` and runs the tests in the same command; the
  guard counts those edits (`loopguard.shell_edits`).

**Prompt caching, 2026-10-21.** A prompt cache matches a request's prefix: the tools, the
system prompt, then the conversation in order. What the plugin changes must leave a cached
prefix alone. Checked on Claude Code 2.1.307 against a local fake Messages API (no model calls),
and on Codex 0.163.0, Copilot CLI 1.0.102 and Pi 1.3.0 through a logging proxy in front of
OpenRouter (cache breakpoints, which move every turn, left out of the comparison).

* A deny list present at session start takes its tools out of the request: Claude Code 12 tools
  to 11, Codex 9 to 4 (goals, multi-agent, view_image), Copilot 21 to 19 (an MCP server's two).
* A running session keeps its tools, on all three. A deny list written mid-turn (while the
  model's `sleep` ran) or between interactive turns by another process, as another session's
  fold would, left every later request's tools byte-identical and its history extending the
  last. Claude Code even reloaded the rule (`/permissions` listed it) and kept the tool; nor
  does a rule a `SessionStart` hook writes reach that session's first request.
* A resumed conversation does not keep them, on all three: `claude --continue`, `codex exec
  resume --last` and `copilot --continue` sent the old history with exactly the new tool list,
  so a conversation resumed while its cache is warm writes its whole history to the cache again
  instead of reading it. The fold runs just after a session ends, when its cache is warmest and
  resuming it likeliest, so `auto` holds a new list as pending, and a detached
  `te toolprune apply-pending` writes it once every session of the repository has been idle for
  `toolprune_quiet_minutes` (60; a hook call or a write to the session's own log counts as
  activity), or once it has waited a day. End to end on Claude Code, the window set to one
  minute: the list waited through a second session, was written one idle minute after it, and
  the next session sent 8 tools instead of 12.
* Within a session the facts and the guard keep the prefix on every agent: the facts block is
  rendered at fold time and given once (on Pi, the same system-prompt section on every prompt),
  and a redirect or notice comes after a tool result. Facts changed on disk mid-session leave a
  running session alone.
* A resumed conversation must carry the facts it started with, byte for byte. Claude Code and

### plugin/README.md
# TokenEconomizer plugin

How to install and use TokenEconomizer in Claude Code, Codex, the GitHub Copilot CLI, Pi and
(experimental) opencode. What the plugin does and why is in the [main README](../README.md); its
design and the verified behaviour of each agent are in [`docs/PLUGIN.md`](../docs/PLUGIN.md).

- [Before you start](#before-you-start)
- Install and use it on [Claude Code](#claude-code) · [Codex](#codex) ·
  [Copilot CLI](#copilot-cli) · [Pi](#pi)
- [What to expect](#what-to-expect) · [Commands](#commands) · [Settings](#settings)
- [Repository map](#repository-map) · [Using with rtk](#using-with-rtk) ·
  [Model calls and API keys](#model-calls-and-api-keys) · [Troubleshooting](#troubleshooting)

## Before you start

- [ ] Your agent installed and signed in, any way it supports (a subscription or an API key), at a
  supported version ([Supported versions](../README.md#supported-versions))
- [ ] Python 3.10 or newer on `PATH` (or set `TE_PYTHON=/path/to/python3.10+`)
- [ ] Copilot CLI only: the repository's folder trusted by Copilot (it asks the first time you
  start it there: choose **Yes, and remember this folder for future sessions**); Copilot ignores a
  folder's `.github/copilot` settings otherwise

No extra API key is needed. Plugins load when a session starts, so start a new session after
installing. Claude Code, Codex and the Copilot CLI install from a clone of this repository:

```bash
git clone https://github.com/microsoft/TokenEconomizer.git
```

Keep the clone where it is: the installed plugin runs from it.

> **Where commands go.** Lines starting with `/` or `$` (`/plugin …`, `/tokeneconomizer:…`,
> `$tokeneconomizer:…`, `/te …`) are typed into **the agent's prompt**, not your shell. Shell
> commands are in `bash` blocks.

## Claude Code

**1. Install.**

```bash
claude plugin marketplace add /path/to/TokenEconomizer
claude plugin install tokeneconomizer@tokeneconomizer
claude plugin list        # should show tokeneconomizer@tokeneconomizer ... enabled
```

(Inside Claude Code the same thing is `/plugin marketplace add …` and `/plugin install …`.)

On Windows, the hooks run under Git for Windows' `sh`, which Claude Code uses for its shell.
Give the marketplace as an absolute path with forward slashes (`C:/path/to/TokenEconomizer`)
and keep the clone in place: a checkout without symlinks has no package in the install copy,
which finds it in that clone. Python is taken as `python3`, `python`, then `py -3`; the
Microsoft Store alias is skipped when it runs nothing.

**2. Check it.** Start Claude Code in any project (`cd my-project && claude`) and type
`/tokeneconomizer:status`. It should print a short status block, not an error. Claude Code may ask
permission to run the plugin's script; allow it always.

**3. Record the tool list, once.**

```text
/tokeneconomizer:toolprune refresh-catalog
```

This records which tools a Claude Code session loads, with no model call. Do it once on this
machine, and again after Claude Code updates. **Don't skip it:** without it the deny list sees
only the few tools Claude Code defers, not the ones every session loads.

**4. Work normally.** When the plugin leaves tools out ([What to expect](#what-to-expect) says
when), the next session start says so once. To see or undo it:

```text
/tokeneconomizer:toolprune            # the tools it left out, and the evidence
/tokeneconomizer:toolprune restore    # give them back, from your next session; they stay back
```

The deny rules go into this repository's `.claude/settings.local.json`, which the plugin keeps
out of git; deny rules you wrote are never touched. To approve each deny list yourself instead:
`/tokeneconomizer:config set toolprune=propose`, then `/tokeneconomizer:toolprune apply`.

**Where its messages appear.** Claude Code shows the plugin's one-line messages (facts added,
tools left out) only in its detailed transcript: press **Ctrl+O**, where they read
`<event> says: TokenEconomizer: …`. The exception is a turn that still looks stuck: the plugin
also asks Claude to repeat that line word for word, so it shows in Claude's reply (under
`claude -p`, in the final reply). Claude may word it differently or leave it out; the detailed
transcript always has it. Press **Esc** to stop the turn; under `claude -p`, Ctrl+C ends the
run. With `--output-format stream-json --verbose`, every message also arrives as a
`hook_response` event.

Each slash command costs one model turn; the same commands are free from a terminal, as
`~/.tokeneconomizer/bin/te --host claude <command>` run inside the repository
([Commands](#commands)). To try the plugin for one session without installing it:
`claude --plugin-dir /path/to/TokenEconomizer/plugin`.

**Update.** `git pull` in the clone, then start a new session (or `/reload-plugins`): Claude Code
runs the plugin straight from the clone. If `/tokeneconomizer:status` still shows the old
behaviour, run `claude plugin update tokeneconomizer@tokeneconomizer`.

**Uninstall.**

1. In each repository where the plugin left tools out: `/tokeneconomizer:toolprune restore`.
2. `claude plugin uninstall tokeneconomizer@tokeneconomizer`, then
   `claude plugin marketplace remove tokeneconomizer`.
3. Optional: `rm -rf ~/.tokeneconomizer` to delete what it learned. (A line the plugin added to a
   repository's `.git/info/exclude` stays; it is harmless.)

## Codex

**1. Install.**

```bash
codex plugin marketplace add /path/to/TokenEconomizer
codex plugin add tokeneconomizer@tokeneconomizer
```

**2. Approve its hooks.** Start `codex` in a repository. Codex asks whether to trust the folder
(**Trust and continue**), then shows **Hooks need review**: choose **Trust all and continue**.
Hooks run from the next session on (the session in which you approve gets no session-start
injection), so quit with `/exit` and start `codex` again. To approve later: `/hooks`.

**3. Check it.** Type `$tokeneconomizer:status`. Codex has no plugin slash commands, so the
plugin's commands are Codex skills with the same names as on the other agents:
`$tokeneconomizer:status`, `:microskills`, `:toolprune`, `:config` and `:repos`, each followed by
its arguments (`$tokeneconomizer:config set loopguard=off`); type `$tokeneconomizer` to pick one.
Name the skill rather than asking in plain words: a question such as *"what has TokenEconomizer
learned here?"* may be answered from the plugin's files without running its command. Commands
that change something (`config set` or `unset`, `toolprune apply` or `restore`, `repos migrate`
or `merge`) write to `~/.tokeneconomizer`, which Codex's sandbox keeps read-only, so Codex asks
first: choose **Yes, proceed**. From a terminal, inside the repository:
`~/.tokeneconomizer/bin/te --host codex <command>` (the launcher appears after the first
session).

**4. Work normally.** See [What to expect](#what-to-expect). On Codex the deny list can turn off
the sub-agent (`collaboration`), `goals` and image (`image_media`) packages, each only after it
has been loaded and gone unused long enough; a package you used even once is kept. Web access,
asking you questions and the bundled skills are never turned off. The list is written to the
project's `.codex/config.toml`, which Codex reads **only in a trusted project** (otherwise the
session start that announces it says so), and never into a `config.toml` your repository
commits: that stays a proposal, and the session start says why.
`$tokeneconomizer:toolprune restore` gives the packages back, and `toolprune measure` shows the
difference with no model call.

**Messages.** Under `codex exec`, Codex prints no hook messages, so the plugin's notices are not
shown, though a loop guard redirect still reaches the model. In the terminal UI, a turn still
stuck after its redirect shows "↳ Hook · TokenEconomizer: … Press Esc to interrupt it, then /stop
to end a command it left running": Esc interrupts the turn, but a command it started keeps
running in the background until `/stop`. Under `codex exec`, Ctrl+C ends the run and its command.

**When a session is learned from.** Quitting interactive Codex (`/exit`) keeps the session open
for `codex resume` and sends no session end, so the plugin learns from it at a later session
start, once it has been quiet for ten minutes. `codex exec` sessions are learned from as they
end.

**Update.** `git pull` in the clone, then `codex plugin add tokeneconomizer@tokeneconomizer`
again to refresh Codex's installed copy. Your hook approval is kept unless the update changed the
hooks themselves; then Codex asks again (**Hooks need review**, or `/hooks`).

**On Windows,** Codex runs each hook's `commandWindows` in its native shell rather than `sh`; it
starts the hook with the `python` on PATH (3.10 or later), which `TE_PYTHON` does not change.

**Uninstall.**

1. In each repository where the plugin turned packages off:
   `~/.tokeneconomizer/bin/te --host codex toolprune restore` (it leaves an empty `.codex/`).
2. `codex plugin remove tokeneconomizer@tokeneconomizer`, then
   `codex plugin marketplace remove tokeneconomizer`.
3. Optional: `rm -rf ~/.tokeneconomizer`.

**A self-contained install.** Codex copies an installed plugin, and the copy uses the package in
your clone. To install a copy that carries the package itself, so the clone can move or go:

```bash
python3 /path/to/TokenEconomizer/scripts/build_plugin.py --out ~/te-marketplace
codex plugin marketplace add ~/te-marketplace
codex plugin add tokeneconomizer@tokeneconomizer
```

To update it, rebuild the bundle and run `codex plugin add tokeneconomizer@tokeneconomizer` again.

## Copilot CLI

**1. Install.**

```bash
copilot plugin marketplace add /path/to/TokenEconomizer
copilot plugin install tokeneconomizer@tokeneconomizer
copilot plugin list       # tokeneconomizer@tokeneconomizer ... (enabled)
```

Copilot loads the plugin from the clone directly, without copying it.

**2. Check it.** In Copilot's interactive mode, type `/tokeneconomizer:status`. Each slash command
is a model turn, and Copilot asks before running the plugin's script; choose **Yes**. Slash
commands work only in interactive mode; the plugin's notices also appear under `copilot -p`.

**3. Record the tool list, once.**

```text
/tokeneconomizer:toolprune refresh-catalog
```

With no model call. Do it once on this machine, and again after Copilot updates.

**4. Work normally.** See [What to expect](#what-to-expect). Copilot cannot remove a single
built-in tool, only turn off a whole MCP server, so the deny list turns off a server only when
**all** of its tools have gone unused long enough: one of yours from
`~/.copilot/mcp-config.json`, or the built-in `github-mcp-server`, which loads only when you are
signed in to GitHub. It is written to `.github/copilot/settings.local.json`, and the next session
start says so. `/tokeneconomizer:toolprune restore` turns the server back on, and
`toolprune measure` shows the difference with no model call.

From a terminal, inside the repository: `~/.tokeneconomizer/bin/te --host copilot <command>` (the
launcher appears after the first session). A turn that is still stuck after the loop guard's
redirect shows "● TokenEconomizer: …" in the conversation (and on stdout under `copilot -p`); press
**Esc** twice to interrupt it, or Ctrl+C to end a `copilot -p` run.

**Update.** `git pull` in the clone; Copilot loads the plugin from it, so nothing else is needed.

**Uninstall.**

1. In each repository where the plugin turned a server off: `/tokeneconomizer:toolprune restore`.
2. `copilot plugin uninstall tokeneconomizer@tokeneconomizer`, then
   `copilot plugin marketplace remove tokeneconomizer`.
3. Optional: `rm -rf ~/.tokeneconomizer`.

**With your own model key (BYOK).** If Copilot answers *"Access denied by policy settings"*, your
organization's policy refuses its models, and Copilot can use your own provider instead. The
plugin works the same way there, except for its model calls (below). In your shell profile:

```bash
export COPILOT_PROVIDER_TYPE=anthropic                  # or openai, azure
export COPILOT_PROVIDER_BASE_URL=https://api.anthropic.com
export COPILOT_PROVIDER_API_KEY=...                     # your provider's key
```

Then start Copilot with a model id your provider knows, for example `copilot --model
claude-sonnet-5` (an Anthropic provider wants its own ids, such as `claude-haiku-4-5`, not the
subscription's `claude-haiku-4.5`). Through **OpenRouter**, keep Copilot on the Anthropic wire, so
prompt caching works, and give it both ids:

```bash
export COPILOT_PROVIDER_TYPE=anthropic
export COPILOT_PROVIDER_BASE_URL=https://openrouter.ai/api
export COPILOT_PROVIDER_BEARER_TOKEN=...                 # your OpenRouter key
export COPILOT_PROVIDER_MODEL_ID=claude-haiku-4.5        # the id Copilot configures itself for
export COPILOT_PROVIDER_WIRE_MODEL=anthropic/claude-haiku-4.5   # the id OpenRouter bills
```

Copilot does not pass these variables to the plugin's hooks, so under BYOK its model calls
(micro-skills' proposer, the loop guard's judge) cannot reach your
provider: `copilot -p` asks to sign in instead. The first such answer leaves a line in
`~/.tokeneconomizer/errors.log` and pauses those calls, and the next session start says so once;
the facts that need no model call are still learned (`microskills=envfacts` keeps only those).
Everything else, including `refresh-catalog` and `measure`, needs no provider.
`~/.tokeneconomizer/bin/te --host copilot doctor` shows the route it sees, and a pause.

To check the whole plugin on your own setup:

```bash
~/.tokeneconomizer/bin/te --host copilot probe      # 7 short real sessions, in a temp repo
```

It builds a throwaway repository that is set up for pytest, without pytest installed, and whose
tests pass under `python -m unittest`. It runs the same prompt in real Copilot sessions with the
plugin, under a state directory of its own, and reports for each session whether the fact the
plugin learned was in the context and which test command the model ran first. Then it applies the
deny list it proposed, shows the tool-definition tokens of one more session, and restores the
list. It makes real model calls on your key or quota, and leaves those sessions in Copilot's
history.

## Pi

**1. Install.** The repository is a Pi package, so Pi installs it like any other:

```bash
pi install git:github.com/microsoft/TokenEconomizer
```

(Over SSH: `pi install git:git@github.com:microsoft/TokenEconomizer`. From a clone:
`pi install /path/to/TokenEconomizer`.) On Pi 0.99.x, install nothing: clone the repository and
start each session with `pi --extension /path/to/TokenEconomizer/plugin/pi/tokeneconomizer.ts`,
using your clone's full path; `git pull` in the clone updates it.

**2. Check it.** Start a new Pi session and type `/te status`. The commands are `/te status`,
`/te microskills`, `/te config …` and `/te repos`; from a terminal, inside the repository,
`~/.tokeneconomizer/bin/te --host pi <command>`. Tool pruning does not apply: Pi loads four
tools. In print and JSON modes the plugin's notices go to stderr. A turn that is still stuck
after the loop guard's redirect gets a notice: press **Esc** to abort it, or Ctrl+C to end a
`pi -p` run (a command Pi started then runs on until it finishes).

**3. Work normally.** See [What to expect](#what-to-expect).

**Update.** `pi update --extensions` (plain `pi update` does not update extensions).

**Uninstall.** `pi remove git:github.com/microsoft/TokenEconomizer` (the source you installed
from); `pi config` turns it off without removing it. Optional: `rm -rf ~/.tokeneconomizer`.

## opencode

**1. Install.** One plugin file serves opencode 1.x (the `server` entry) and 2.x (the `setup`
entry). Link it where opencode looks for plugins, keeping it next to `scripts/` and `lib/`:

```bash
mkdir -p ~/.config/opencode/plugins
ln -s /path/to/TokenEconomizer/plugin/opencode/tokeneconomizer.ts ~/.config/opencode/plugins/tokeneconomizer.ts
```

(Per repository: `.opencode/plugins/`.) Python 3.10+ must be on `PATH`, or named by `TE_PYTHON`.

**2. Check it.** Run a session, then `~/.tokeneconomizer/bin/te --host opencode status` in the
repository. opencode has no plugin slash commands, so every command runs from a terminal. Tool
pruning does not apply. Micro-skills is off by default: `te --host opencode config set
microskills=on` (or `envfacts`, without model calls).

**How it hands a session over.** On 1.x the plugin exports the session with `opencode export` at
the end of every turn and sends the path; on 2.x, which has no export command, it records the
session from its events and writes the same JSON. A headless `opencode run` is folded when its
turn ends and a deleted session when it is deleted. Quitting the TUI gives a plugin no chance to
say so: that session is folded by the next session's start, once its export has been quiet for
10 minutes.

**Model calls.** The proposer and the loop guard's judge run through `opencode run` on your
default opencode model (`paid_model` names another): tools that change anything are denied,
the session is deleted afterwards, and no other plugin runs (`--pure` on 1.x; `--standalone` on
2.x). On 2.x a reply that used no tool carries no usage, so its cost is estimated.

**Verified live,** on opencode 1.19.5 and 2.2.0 (Python 3.12), with a scripted local model
endpoint and, on 1.19.5, the free `opencode/big-pickle` model:
the plugin loads; sessions are folded with real usage and model; facts learned over five sessions
reach the next session through the system prompt; the loop guard's judge ran, nudged a
failing edit-and-test loop, and the redirect arrived in the model's next tool results; the
still-stuck notice was printed (`opencode run`) and the first notice shown as a TUI toast
(1.19.5); a session quit with Ctrl+D in the TUI was folded by the next start.

**Not covered:** the 2.x TUI, and notices on 2.x, which go to the server's stderr rather than a
toast. A `read`, `task` or `*` permission denial stalls opencode 1.19.5 at start-up, which is why
the side call denies only `bash`, `edit`, `webfetch` and `websearch`.

## What to expect

The plugin works session by session: what it learns from a repository's earlier sessions is
applied to the ones that follow. Facts and the deny list take effect when a session starts; the
loop guard acts during a turn. Each agent learns on its own (what Claude Code learned in a
repository is not used by Codex there), while settings are shared by every agent.

- **Facts** (once you turn micro-skills on; it is off by default). Two sources propose them, in
  any language or toolchain. The first needs no model call: the same environment failure in a few
  sessions (a tool, interpreter, build or test command that fails as typed and works spelled
  another way). The second runs every `microskills_propose_every` sessions (3 by default): a model
  reads digests of the recent sessions (the commands run, including build, test and lint commands,
  the files edited, and each failing command with its error line, with paths relative to the
  repository) and writes facts about the repository, each with patterns that test it against later
  sessions. A fact becomes active once three sessions confirm it (for a proposed fact about the
  code, sessions that edited different files), and is injected at every session start while the
  failure it prevents keeps showing up, or keeps being avoided, in at least 40% of the sessions
  where it applies (over at least four). It is retired when a session contradicts it (for a
  command-spelling fact, two in a row). How much this helps depends on the repository's state and
  the tasks you run in it. A session start that adds facts says so once, in one line. A resumed
  session keeps the facts it started with, word for word, so its cached prompt still matches.
  `microskills` shows the facts injected and those still forming.
- **Deny list.** A tool, package or server that is loaded but never used here is left out without
  asking you, once it has gone unused over `toolprune_evidence` prompts (10 by default) across at
  least `toolprune_min_sessions` sessions (2), or over `toolprune_sessions` sessions of any length
  (5); Claude Code's `NotebookEdit` and Codex's `image_media` package need three times as long. A
  session that ran no prompt does not count. The list is written once the repository's sessions
  have been idle for `toolprune_quiet_minutes` (60 by default), so that no conversation you resume
  loses its prompt cache (a list that has waited a day is written anyway), and it applies from the
  next session, whose start says so once. `toolprune` shows a list still waiting.
  `toolprune restore` gives back what the plugin removed, and only that; what you give back is
  never removed again (`toolprune apply NAME` removes one again). With `toolprune=propose`, the
  list is only proposed, the session start says so, and nothing changes until you run
  `toolprune apply`. `toolprune=off` stops new lists but leaves an applied one in place;
  `toolprune restore` gives the tools back. A settings file the plugin creates is added to
  `.git/info/exclude`. Each checkout keeps its own settings file: a repository's clones share what
  was learned, and each gets the list when one of its own sessions ends.
- **Loop guard.** Quiet on normal turns, and idle until `loopguard.envelope_min_samples` turns in
  a repository (5 by default) have ended well: on their own, with no failing check after the last
  edit. After that, a turn that keeps hitting the same failures, or piles up errors, after
  `loopguard.min_turns` tool calls is put to a judge model. Only a "stuck" verdict with confidence
  `loopguard.judge_confidence` (0.7) or more attaches a redirect (written by that model) to a tool
  result (at the `aggressive` preset, an ambiguous verdict past the envelope also does), at most
  `loopguard_nudges` (1) per turn; if the turn is still stuck after that, a one-line notice tells
  you how to stop it. A long turn with no sign of looping is never judged. A turn past
  `loopguard.backstop_mult` (2.5) times the repository's usual length that also keeps churning
  edits through the same failures is redirected even if the judge disagrees. The plugin never
  stops a turn itself. Where the notice appears, and how to stop the turn, on each agent and in
  each mode: [When a turn gets stuck](../README.md#when-a-turn-gets-stuck).
- **Cost.** `status` shows each session's tokens, priced after it ends, and the plugin's own
  overhead: the loop guard's judge, and micro-skills' proposer when it is on.

## Commands

| Command | What it does |
|---|---|
| `status` | what it has learned in this repository, what it did, and what your sessions cost |
| `microskills` | the facts it injects at session start, and those still forming |
| `toolprune` | the deny list: what it left out, what it would leave out next, and the evidence |
| `toolprune apply [ITEM …]` | apply a waiting proposal (with `toolprune=propose`), or the named items; from the next session |
| `toolprune restore [ITEM …]` | give back the plugin's entries (all, or the named ones); they are not removed again |
| `toolprune refresh-catalog` | record the tools a session loads (Claude Code, Copilot) |
| `toolprune measure` | the request with and without the proposal |
| `config` | the settings: what is on, and every value in effect |
| `config set KEY=VALUE … [--global]` | change settings for this repository (or every one); see [Settings](#settings) |
| `config unset KEY … [--global]` | remove the setting at this level, so the global value (or the default) applies |
| `repomap` / `repomap refresh` | the cached repository map / make it now (see [Repository map](#repository-map)) |
| `repos` | every repository it keeps state for: how it was identified, its sessions per agent, the checkouts seen |
| `repos migrate` | file state an earlier version recorded under the repository it belongs to (runs by itself, once, after an upgrade) |
| `repos merge KEY [INTO]` | merge one repository's state into another's (default: this one), for state whose checkouts are gone |
| `doctor` | check Python, the state directory, the agents found, how this directory was identified, and the error log |

How to run them:

| Agent | Inside the agent | From a terminal, in the repository |
|---|---|---|
| Claude Code | `/tokeneconomizer:<command>` | `~/.tokeneconomizer/bin/te --host claude <command>` |
| Codex | `$tokeneconomizer:<command>` (`status`, `microskills`, `toolprune`, `config`, `repos`) | `~/.tokeneconomizer/bin/te --host codex <command>` |
| Copilot CLI | `/tokeneconomizer:<command>` (interactive mode) | `~/.tokeneconomizer/bin/te --host copilot <command>` |
| Pi | `/te <command>` | `~/.tokeneconomizer/bin/te --host pi <command>` |
| opencode | none (run from a terminal) | `~/.tokeneconomizer/bin/te --host opencode <command>` |

`doctor` and `repomap` run from a terminal (or as `/te …` on Pi); there is no slash command or
Codex skill for them.

Inside an agent, each command is one model turn; from a terminal it costs nothing. Codex asks
before a command that changes something (`config set`, `toolprune restore`, ...), since it
writes outside Codex's sandbox: choose **Yes, proceed**. The Copilot CLI runs these commands in
its interactive mode only and asks before each: choose **Yes**.

The launcher in `~/.tokeneconomizer/bin` is written by the first session; before that, use
`/path/to/TokenEconomizer/plugin/scripts/te`. From a plain terminal, `--host` defaults to the
agent that last worked in the repository.

## Settings

Each of the three mechanisms can be turned on or off on its own, and each has numbers you can
set by hand. Settings apply to the current repository, or to every repository with `--global`,
and are shared by every agent working in it. The examples use Claude Code's form; the same
`config` command on each agent is:

| Agent | Set one value in this repository |
|---|---|
| Claude Code | `/tokeneconomizer:config set loopguard=off` |
| Codex | `$tokeneconomizer:config set loopguard=off` |
| Copilot CLI | `/tokeneconomizer:config set loopguard=off` (interactive mode) |
| Pi | `/te config set loopguard=off` |
| any agent, from a terminal | `~/.tokeneconomizer/bin/te config set loopguard=off` |

**Turn a mechanism on or off:**

```text
/tokeneconomizer:config set microskills=on               # micro-skills, in this repository
/tokeneconomizer:config set toolprune=off loopguard=off
/tokeneconomizer:config set microskills=on --global       # in every repository
/tokeneconomizer:config                                # what is on, and every value in effect
```

| Mechanism | Key | `on` means | Other values |
|---|---|---|---|
| Micro-skills (off by default) | `microskills` | `envfacts+distiller`: facts found without model calls, plus a model proposing facts every `microskills_propose_every` sessions | `off`; `envfacts`: only the facts found without model calls; `distiller`: only the proposer |
| Tool pruning | `toolprune` | `auto`: applied without asking once your sessions have been idle for `toolprune_quiet_minutes` (or a day after it formed), from the next session, which announces it | `off`; `propose`: only proposed, applied when you run `toolprune apply` |
| Loop guard | `loopguard` | `nudge`: a judge model decides whether a looping turn is stuck; if so, up to `loopguard_nudges` mid-turn redirects, then a notice to you if the turn is still stuck | `off` (no judge either); `stop` is read as `nudge`, with a warning |

**Tune a mechanism:**

```text
/tokeneconomizer:config set microskills_max_facts=2            # inject at most two facts
/tokeneconomizer:config set toolprune_evidence=20              # wait for twenty unused prompts
/tokeneconomizer:config set loopguard_nudges=2 loopguard.min_turns=30
/tokeneconomizer:config unset loopguard.min_turns              # back to the default
```

| Key | Default | What it sets |
|---|---|---|
| `microskills_max_facts` | `4` | the most facts from repeated failures injected at session start (the proposer's facts are not capped) |
| `microskills_max_tokens` | `150` | the size of those facts' block, in tokens (about 4 characters each) |
| `microskills_propose_every` | `3` | sessions between runs of the fact proposer (the first run comes one session early: after the second, by default) |
| `toolprune_evidence` | `10` | prompts a never-used tool must go unused, over at least `toolprune_min_sessions` sessions, before it is left out (three times as many for `NotebookEdit` and Codex's `image_media`; the web is never proposed) |
| `toolprune_min_sessions` | `2` | sessions those prompts must span; `1` lets a single session's prompts decide |
| `toolprune_sessions` | `5` | or this many sessions, however few prompts they ran |
| `toolprune_quiet_minutes` | `60` | how long the repository's sessions must have been idle before `auto` writes a deny list, so that no conversation resumed while its prompt cache is warm loses it (a list is written at the latest a day after it formed); `0` writes at once |
| `toolprune_protect` | none | tools never left out however long they go unused, by name or pattern (`mcp__headroom__*`), separated by commas; a deny rule the plugin added for one is removed at the next fold, and rules you wrote are never touched |
| `loopguard_aggr` | `default` | the guard's threshold preset: `conservative`, `default` or `aggressive` |
| `loopguard_nudges` | `1` | redirects per turn before the guard only tells you |
| `loopguard.<name>` | from the preset | one guard threshold, set by hand (below) |

The guard looks for a turn that keeps editing the same files and hitting the same failures. It
also learns how long this repository's turns usually run when they end well (on their own, with
no failing check after the last edit): the *envelope*. Until `envelope_min_samples` such turns
exist the guard does nothing; after that, some thresholds are learned from those turns, on top
of the preset. A value you set with `loopguard.<name>` wins over both. Defaults at each preset:

| `loopguard.<name>` | `conservative` | `default` | `aggressive` | What it sets |
|---|---|---|---|---|
| `min_turns` | 28 | 20 | 14 | tool calls in a turn before it can count as stuck |
| `edit_churn` | 5 | 4 | 3 | edits to one file that count as churn |
| `distinct_edit_files` | 3 | 3 | 3 | files edited that count as scattered |
| `error_outputs` | 8 | 6 | 4 | failing tool results that count as sustained errors |
| `stagnation` | 0.30 | 0.20 | 0.12 | share of failures that repeat an earlier one |
| `envelope_pct` | 90 | 90 | 90 | percentile of the repository's well-ended turns the envelope starts from |
| `envelope_margin` | 1.5 | 1.25 | 1.0 | multiplier on that percentile |
| `envelope_min_samples` | 7 | 5 | 3 | well-ended turns needed before the guard acts |
| `backstop_mult` | 3.5 | 2.5 | 1.8 | past this multiple of the envelope, a turn the rule calls stuck is redirected even if the judge disagrees, then flagged to you |
| `judge_confidence` | 0.85 | 0.7 | 0.55 | how sure the judge must be that a turn is stuck |
| `gate_min_turns` | 24 | 18 | 12 | tool calls before the judge is asked (never fewer than `min_turns`) |
| `gate_error_outputs` | 8 | 8 | 8 | failing results that ask the judge without a repeated failure |

**Repository map** (off by default; see [Repository map](#repository-map)):

| Key | Default | What it sets |
|---|---|---|
| `repomap` | `off` | `on`: a map ranked toward the session's first prompt; `start`: the cached map at session start |
| `repomap_tokens` | `2048` | the map's size, in tokens |
| `repomap_python` | auto | the Python that has aider installed |
| `repomap_timeout` | `8` | seconds the first prompt may wait for a ranked map before the cached one is used |

**Other settings:**

| Key | Default | Values |
|---|---|---|
| `paid_model` | `""` | model for the plugin's own calls; empty: `haiku` on Claude Code, the agent's own default model on Codex and Pi, on Copilot `COPILOT_PROVIDER_MODEL_ID` or `COPILOT_MODEL` (unless it is `auto`), else a BYOK provider's Haiku, else Copilot's own default |
| `shadow` | `false` | decide and log everything, act on nothing |
| `mode` | `auto` | `interactive` or `headless` to override what the plugin detects |

**Where settings live, and when they apply.** For one session, an environment variable wins:
`TE_` plus the setting's name in capitals (`TE_MICROSKILLS`, `TE_TOOLPRUNE_EVIDENCE`,
`TE_LOOPGUARD_NUDGES`, ...), and `TE_LOOPGUARD_THRESHOLDS='{"min_turns": 30}'` for the guard's
thresholds; `TE_DISABLE=1` turns the whole plugin off. Otherwise the repository's
settings win over the global ones, and those over the defaults; `unset` goes back one level. A
change applies from the agent's next hook call: the guard at the next tool call, facts and the
deny list at the next session start. A new fact-size cap shows once the next session has ended.

**Earlier names.** Before the mechanisms were renamed they were `inject`, `untool` and `spiral`,
with settings such as `inject_max_facts`, `untool_evidence`, `spiral_nudges`, `spiral.<name>` and
variables `TE_INJECT`, `TE_UNTOOL`, `TE_SPIRAL`, ...; all of them are still read (`spiral=guard`
as `loopguard=stop`, which works as `nudge`), and a new name set alongside its old one wins.
`config set` writes the new name. The earlier commands `te facts` and `te untool`, and
`/tokeneconomizer:facts` and `/tokeneconomizer:untool`, still work.

## Repository map

An opt-in fourth mechanism: aider's map of the repository's key files and symbols (signatures
only, ranked by how much of the code refers to them), added to the session's context so the
agent knows where things are before it starts reading files. Turn it on per repository:

```bash
pip install aider-chat                      # or: pipx install aider-chat / uv tool install aider-chat
~/.tokeneconomizer/bin/te config set repomap=on      # settings are shared by every agent
```

- **What goes in.** At most `repomap_tokens` tokens (default 2048), once per session. On Claude
  Code, the Copilot CLI and Pi it is ranked toward the identifiers in your first prompt; if that
  takes longer than `repomap_timeout` seconds (about 5 s on a repository of Django's size, well
  under a second on a small one), the cached map is used instead. Codex gets the cached map at
  session start. `repomap=start` does that on every agent and never delays a prompt.
- **What it reads.** The files `git ls-files` lists, in every language aider understands,
  without vendored code, minified files or files over 256 KB.
- **Where it runs.** In whichever Python has aider: `repomap_python` if you set it, else the one
  behind an installed `aider` command, else the plugin's own. `te doctor` says which it found.
  The plugin never imports aider itself.
- **What it writes.** Nothing in the repository. The map and aider's tag cache live in the
  plugin's state directory. The map is cached per commit and remade in the background when
  `HEAD` moves.
- **What it costs.** No model calls. The map is part of every request of the session, so it
  costs on sessions that already knew where to look and saves on those that would have searched.
  `te status` shows its size.

## Using with rtk

[rtk](https://github.com/rtk-ai/rtk) compresses shell output. Install it on its own (`rtk init
-g`); it does not need to be part of this plugin, and the two do not get in each other's way:
rtk rewrites shell commands before they run, and this plugin reads sessions, injects context and
watches tool results. The plugin reads `rtk`-prefixed commands as the commands they wrap, and
rtk adds no tools for the deny list to see. `te doctor` reports an installed rtk.

One interaction to know: with rtk 0.45.0, `rtk pytest` prints nothing when pytest is missing (it
exits with code 1). The agent sees no error and the plugin cannot learn the "`pytest` fails here;
`X` works" fact from it. Commands that name their interpreter (`.venv/bin/python -m pytest`) are
not rewritten, so the commands that fact recommends keep working.

## Model calls and API keys

**With the defaults, the plugin's only model calls are the loop guard's**: the judge, asked about
a turn that shows signs of looping, and, when the judge finds the turn stuck, the redirect it
writes. Tool pruning never calls a model. Turning micro-skills on adds its fact proposer, once
every `microskills_propose_every` sessions (`microskills=envfacts` keeps only the facts found
without a model call); `loopguard=off` turns the judge off along with the guard.

These calls run through **your own agent's CLI**: `claude -p`; `codex exec`; `copilot -p`, with
every tool removed; and `pi -p`, with nothing loaded but the model. So they use whatever your
sessions already use (a Claude subscription or Anthropic API key, your Codex login or OpenAI key,
Copilot's subscription, or the provider and login Pi is set up with), are billed there, and are
shown in `status`. Copilot with BYOK is the exception; see [Copilot CLI](#copilot-cli).

A call that gets no reply leaves a line in `~/.tokeneconomizer/errors.log`. If the CLI answers
that it is not signed in, that agent's calls are also paused (the loop guard then redirects only
at its backstop), the next session start says so once, and `config set microskills=on` (or
`loopguard=on`) tries again. `toolprune measure` on Claude Code makes its two calls the same way,
and only when you run it.

## Troubleshooting

| Symptom | Fix |
|---|---|
| a command prints an import error, or the hooks seem to do nothing | run `~/.tokeneconomizer/bin/te doctor` (or `plugin/scripts/te doctor` in the clone) and read its errors.log lines |
| errors.log says the package "was not found for the plugin" | the clone the plugin was installed from moved or is gone: add it again, or use the [self-contained install](#codex) |
| `TokenEconomizer needs Python >= 3.10 (this is 3.x)` | install Python 3.10+ or set `TE_PYTHON` to one |
| the deny list leaves nothing out after many sessions | run `toolprune refresh-catalog` (Claude Code, Copilot) |
| a Codex deny list was applied but nothing changed | trust the project in Codex; `~/.tokeneconomizer/bin/te --host codex doctor` says whether it is trusted |
| errors.log has `sidecall copilot: no reply`, and a session start says the plugin's model calls are paused | they cannot use a Copilot BYOK provider ([Copilot CLI](#copilot-cli)): micro-skills keeps its facts that need no model call (`microskills=envfacts` stops trying the proposer), and the loop guard redirects only at its backstop. Once Copilot is signed in, `config set microskills=on` (or `loopguard=on`) tries again |
| `te` shows another agent's state | add `--host claude`, `codex`, `copilot` or `pi` |

### CLAUDE.md
# TokenEconomizer

A plugin for Claude Code, Codex, the Copilot CLI and Pi that reads finished sessions and changes
what later sessions in the same repository pay for: micro-skills, tool pruning, and a loop guard.
See `README.md` for the overview and the method, `docs/PLUGIN.md` for the design and the verified
agent behavior, and `docs/ARCHITECTURE.md` for how the package fits together.

## Layout
- `tokeneconomizer/` — the one Python package, standard library only
  - `microskills/` — learn repository facts from finished sessions; render the injected block
  - `toolprune/` — unused-tool evidence and the deny-list proposal; Codex capability packages
  - `loopguard/` — the per-call failure-loop guard and its per-repository envelope
  - `trace/` — each agent's session-log format (Claude Code, Codex, Copilot CLI, Pi, opencode)
  - `plugin/` — the runtime: hook dispatch, per-repository state, settings, the `te` CLI
  - `config.py`, `ledger.py`, `pricing.py`, `domain.py`, `stage.py` — shared by all three
- `plugin/` — the installable plugin directory: manifests per agent, hook files, launchers
  (`scripts/te`, `scripts/te-hook`), slash commands (`slash-commands/`, named in the Claude Code
  and Copilot manifests, since Codex would turn a `commands/` folder into duplicate skills), Codex
  skills (`codex-skills/`, Codex having no plugin slash commands), the Pi extension; `lib/` links
  the package
- `experiments/` — benchmark-only: `te_bench/` (adapters, arms, facade, benchmark-only
  controllers), `te_harness/` (Docker runners), `scripts/`, `workloads/`, its own `tests/`;
  its `README.md` is the run book
- `package.json` — the repository as a Pi package (`pi install git:github.com/…`); it names
  the same extension as `plugin/package.json`, which a test pins
- `scripts/build_plugin.py` — a self-contained plugin bundle for marketplace installs
- `tests/` — offline tests for the package and the plugin

## Conventions
- The mechanisms (`microskills`, `toolprune`, `loopguard`, `trace`) never import
  `tokeneconomizer.plugin`, and nothing under `tokeneconomizer/` imports `experiments/`; both
  are pinned by `tests/test_plugin_package.py`.
- Standard library only, Python >= 3.10. A hook must start fast and fail open: any exception in
  a hook becomes `{}` and a line in `~/.tokeneconomizer/errors.log`.
- On-disk state names (`injection.json`, `untool.json`, `envelope.json`, event kinds) are a
  compatibility surface; renaming them strands what users have learned.
- Settings keep their earlier names as aliases (`inject`, `untool`, `spiral`, ...; see
  `plugin/config.py`); write new code against the current names.
- No run outputs in the repository: transcripts, rows, streams, figures rendered from runs and
  tables derived from them stay out of git (`.gitignore`). The one exception is the paper's
  headline results in `README.md` (the line under the badges, the Results section, and the
  teaser's closing results, which read `docs/assets/results_overview.py`'s `ROWS`; that script
  also draws `results_overview.*`, which the README no longer shows): quoted from the paper's
  Table 1 and attributed to it. Change them only with the paper, and redraw both figures with
  `python docs/assets/results_overview.py` and `python docs/assets/teaser.py --plex FONTS`
  (its docstring says where to get IBM Plex). The teaser's middle act is a schematic with
  made-up sessions and no numbers.
- The plugin's own text (`plugin/`, its manifests, slash commands and skills, and what the
  hooks print) makes no claims of effect.
- Tests: `python -m pytest tests experiments/tests`. A change to what the plugin learns or
  decides should be checked against recorded sessions, not only the unit tests.
- Every model-backed test goes through the agent's own CLI on a provider you control
  (OpenRouter in development); never hard-code a key.

### pyproject.toml
[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[project]
name = "tokeneconomizer"
version = "0.1.0"
description = "Experience-driven black-box cost control for coding agents (Claude Code, Codex, Copilot CLI, Pi), as a plugin."
readme = "README.md"
requires-python = ">=3.10"
license = { text = "Apache-2.0" }
authors = [{ name = "TokenEconomizer authors" }]
keywords = ["llm-agents", "cost-optimization", "swe-bench", "token-economy"]

# The package is STDLIB-ONLY: the three mechanisms, the trace reader, the ledger and the plugin
# runtime import nothing outside the standard library, so it runs on any Python >=3.10 with zero
# install-time dependencies.
dependencies = []

[project.scripts]
# The plugin's command line (status, microskills, toolprune, config, ...). The plugin ships its
# own launcher (plugin/scripts/te) and does not need the package installed.
te = "tokeneconomizer.plugin.cli:main"

[project.optional-dependencies]
# Test suite is offline (no Docker / no datasets).
test = ["pytest>=7.0"]
# The reference task-execution harness under experiments/te_harness/ (see
# experiments/README.md). It adds no
# PyPI dependency -- it is stdlib-only at import time and the official SWE-bench grader is
# imported lazily from a checkout named by TE_SWEBENCH_REPO -- so this extra installs
# nothing. It exists to give "I intend to run the harness" a name, since what the harness
# actually needs cannot come from pip: Docker, an agent CLI on PATH, an API key, the
# benchmark images, and for Web-Bench a built Rush monorepo.
harness = []
# The repo-map external baseline (experiments/te_bench/baselines/repomap.py) generates aider's
# token-budgeted map on the HOST -- the task container's Python is pinned to the issue's
# era and cannot run a modern tree-sitter stack. This is the ONLY baseline with a host
# dependency: rtk ships a static binary and Serena installs itself in-container.
#
# It stays an EXTRA: aider is imported inside `preflight()`, and the generator both the
# baseline and the plugin's opt-in map run (tokeneconomizer/plugin/repomap_gen.py) is a subprocess
# that nothing imports, so `import tokeneconomizer` keeps its zero-dependency guarantee. A
# machine that will never make a repo map never needs aider installed.
baselines = ["aider-chat>=0.60"]

[tool.setuptools.packages.find]
# The package ONLY. The reproduction code (experiments/, including te_harness and te_bench) is
# deliberately not distributed: `import tokeneconomizer` must not be able to reach Docker or a
# benchmark harness, and excluding it here is what makes that structural.
include = ["tokeneconomizer*"]
exclude = ["experiments*", "te_harness*", "tests*", "scripts*"]

[tool.pytest.ini_options]
testpaths = ["tests", "experiments/tests"]
addopts = "-q"

[tool.setuptools.package-data]
# The Claude Code tool-description snapshot the catalog reader joins against.
tokeneconomizer = ["trace/*.json"]

## Top-level structure
dir	.claude-plugin
dir	.github
file	CLAUDE.md
file	LICENSE
file	README.md
file	SECURITY.md
dir	docs
dir	experiments
file	package.json
dir	plugin
file	pyproject.toml
dir	scripts
dir	tests
dir	tokeneconomizer

## Notable directories
### tokeneconomizer/
config.py domain.py ledger.py loopguard/ microskills/ plugin/ pricing.py stage.py toolprune/ trace/
### plugin/
.claude-plugin .codex-plugin hooks lib opencode pi slash-commands scripts (multi-agent packaging)
