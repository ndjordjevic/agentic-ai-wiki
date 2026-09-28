# coleam00/skills

## Metadata
- Stars: 635
- Forks: 176
- Primary language: Python
- Default branch: main
- Latest release: none
- License: MIT License
- Homepage: (none)
- Fetched: 2026-09-28
- Final URL: https://github.com/coleam00/skills

## Description
The agent skills I actually use to build software with coding agents. The PIV loop, planning, worktrees, and the meta-skills for building your own AI Layer.

## README
# Cole's AI Skills

The skills I actually use to build software with coding agents. Straight out of my `.claude/skills/` folder.

## What this is

A skill is a folder with a `SKILL.md` in it: a name, a description of when to use it, and the procedure the agent
should follow. Your agent loads the description at startup and pulls in the full skill only when the work matches.
That's the whole idea, and it's why skills scale where a 2,000-line `CLAUDE.md` doesn't.

These 34 skills are the AI Layer from my [Agentic Coding course](https://dynamous.ai). They're built around one
loop I run on nearly every ticket:

**prime → plan → implement → validate → review → commit → PR**

Around that loop sit the pieces that feed it (PRD, architecture, epic slicing), the pieces that run it in parallel
(worktrees), and the meta-skills that let you build more of your own AI Layer (rules, hooks, skills, opportunity
scans).

Nothing here is a framework. Each skill is a plain markdown file you can read in two minutes, disagree with, and
edit. That's the point: read them, take the ones that fit how you work, rewrite the rest.

## Bring them in

### As a Claude Code plugin (easiest, stays updated)

Run these two commands inside Claude Code:

```
/plugin marketplace add coleam00/skills
/plugin install skills@cole-medin
```

That's it. All 34 skills, managed and read-only, and `/plugin marketplace update` pulls new ones as I add them.
Plugin skills are namespaced, so you invoke them as `/skills:piv-implement`.

The whole set costs roughly 4,400 tokens of always-on context (just the descriptions; the bodies load only when a
skill fires). Run `claude plugin details skills` to see the per-skill breakdown, and disable the plugin any
time with `/plugin`.

> **If that first command fails with `Permission denied (publickey)`:** the `owner/repo` shorthand prefers SSH,
> and your SSH key isn't authenticating to GitHub. Recent Claude Code versions detect that and fall back to HTTPS
> on their own. If yours doesn't, pass the HTTPS URL directly, which needs no key:
>
> ```
> /plugin marketplace add https://github.com/coleam00/skills.git
> ```
>
> Setting `CLAUDE_CODE_PLUGIN_PREFER_HTTPS=1` in your environment makes the shorthand use HTTPS permanently.

### As editable files, in any agent

```bash
npx skills add coleam00/skills                             # everything
npx skills add coleam00/skills --list                      # see what's here first
npx skills add coleam00/skills --skill piv-plan-implementation piv-implement piv-validate
```

Add `-g` to install globally (`~/.claude/skills/`) instead of into the current project. This route writes real
files into your repo, so you can edit them, which is what I'd actually recommend once you know which ones you keep
reaching for.

### Or just clone and copy

They're only markdown files:

```bash
git clone https://github.com/coleam00/skills.git
cp -r skills/.claude/skills/piv-implement your-project/.claude/skills/
```

### Or ask your agent

This works fine too:

> Clone https://github.com/coleam00/skills, look at the skills in `.claude/skills/`, and copy the ones
> that fit this project into my `.claude/skills/` folder. Tell me which ones you picked and why.

For the last two, restart your session (or run `/skills`) and they'll show up.

## The skills

**Prime: load the right context, and only that**

| Skill | What it does |
|---|---|
| `prime-codebase` | Orients the agent in a codebase before planning or implementing |
| `prime-backend` | Same, scoped to API routes, services, and the data layer |
| `prime-frontend` | Same, scoped to components, routing, state, and styling |

**Plan: intent before implementation**

| Skill | What it does |
|---|---|
| `plan-create-prd` | Interviews you into a problem-first PRD. Intent, never engineering decisions |
| `plan-architecture` | A working session on *how* to build it: stack, data shape, trade-offs, risks |
| `piv-slice-epic` | Slices an epic plus its architecture into PIV-sized tickets with a dependency graph |
| `plan-create-stories` | Turns a PRD into a real backlog in Jira or GitHub |

**The PIV loop: plan, implement, validate**

| Skill | What it does |
|---|---|
| `piv-plan-implementation` | Deep codebase analysis plus research into a one-pass-ready implementation plan |
| `piv-implement` | Executes that plan task-by-task, validating at every step |
| `piv-validate` | Runs the project's full suite and returns one PASS/FAIL verdict |
| `piv-review-changes` | Pre-commit technical review of what changed |
| `piv-fix-review-findings` | Triages review findings. You decide what gets fixed now vs deferred |
| `piv-commit` | One atomic, conventionally-tagged commit |
| `piv-create-pr` | Pushes the branch and opens the PR with a real body |
| `piv-review-pr` | The agentic gate on an open PR: fresh eyes, severity-ranked, posted to GitHub |
| `piv-run-full-loop` | Chains the core loop end-to-end from a single feature description |

**Issues: diagnose before you fix**

| Skill | What it does |
|---|---|
| `piv-investigate-issue` | Parallel investigation of a GitHub issue into an evidence-backed RCA |
| `piv-implement-issue` | Implements the fix from that RCA, with regression tests |

**Parallel work**

| Skill | What it does |
|---|---|
| `worktree-create` | Spins up N git worktrees, each configured, installed, and health-checked |
| `worktree-merge` | Integrates those branches through one safe integration branch |

**Build your own AI Layer: the meta-skills**

| Skill | What it does |
|---|---|
| `rules-create-global` | Derives a lean root `CLAUDE.md` from your codebase or your specs. The customizable `/init` |
| `rules-check-drift` | Checks whether your rules file is still *true* after recent changes |
| `ablate-ai-layer` | Tests whether your rules still earn their place: strips them, reruns the same task, diffs the two |
| `skills-create` | Authors a new skill, or refactors a fat one into `SKILL.md` plus `references/` |
| `hooks-create` | Turns "never let the agent touch my migrations" into a working hook, wired into settings |
| `opportunity-scan` | Reads how you actually work and recommends what to encode next |
| `system-execution-report` | Reflects on a just-finished implementation: what diverged from the plan |
| `system-evolution-review` | Finds the bugs in your *process*, not your code |
| `second-brain-audit` | Finds facts in your notes that quietly stopped being true, and restructures so they stop |

**Autonomy: hand the whole loop over**

| Skill | What it does |
|---|---|
| `build-dark-factory` | Takes a PRD and builds a repo around it that ships validated code with nobody at the keyboard. All five components, in construction order, plus a deterministic audit of what you built. It encodes the AI coding process you already run rather than replacing it, and it deliberately does not write the PRD: bring one, or make one with `plan-create-prd` first |

**Tools**

| Skill | What it does |
|---|---|
| `agent-browser` | Browser automation for the agent: navigate, fill, click, screenshot, extract |
| `ast-grep` | Structural code search by AST pattern instead of text |
| `drive-screen` | Real desktop control: focus a window, type, paste, click, screenshot. Windows, macOS, Linux |
| `setup-ai-tutor` | Stands up the course's sample project. Sample-specific, so adapt it or delete it |

## Using these with other agents

Skills are just markdown. There is no Claude-specific runtime here, so most of this works anywhere a coding agent
can read files.

The `npx skills` CLI installs to 75+ agents (Codex, Cursor, Copilot, Cline, Windsurf, OpenCode, Continue and the
rest) into whatever directory each one expects:

```bash
npx skills add coleam00/skills -a codex
npx skills add coleam00/skills -a cursor -a claude-code
```

If your agent has no skills mechanism at all, the fallback is boring and effective: keep the folder in your repo
and point at it from `AGENTS.md` (or the equivalent), telling the agent to read the matching `SKILL.md` before
starting that kind of work.

Two things to adjust when you port them:

- **Slash-command syntax.** Skills that reference each other by name (`/piv-validate`) assume Claude Code's
  invocation. Elsewhere, say "use the piv-validate skill" instead.
- **`allowed-tools` frontmatter.** A few skills declare it. Other agents ignore the field harmlessly.

## Hooks

Skills are the *procedural* half of an AI Layer, the things the agent reaches for. `hooks/` is the other half:
deterministic code that fires on a lifecycle event whether the model remembers or not.

> A rule *asks* the agent to behave. A hook **guarantees** it.

Six copy-in hooks live in [`hooks/`](hooks/) with their own README: block every route to your secrets, refuse
`rm -rf`, enforce declared file coupling, log every tool call, inject today's git state at session start, refuse
to let the agent finish while the tests are red, and ping you when it does finish.

```bash
mkdir -p .claude/hooks
cp hooks/*.py .claude/hooks/
cp hooks/settings.json.example .claude/settings.json   # or merge the "hooks" block
```

Unlike a skill, **a hook does something the moment it exists** - so read them before you wire them, set
`TEST_COMMAND` in the stop hook, and check both directions (exit 0 on green, exit 2 on red) before you trust it.
[`hooks/README.md`](hooks/README.md) covers the five failure modes that waste an afternoon, the venv trap chief
among them.

To build one of your own without writing Python, describe it to the `hooks-create` skill.

## Make them yours

Two things deliberately ship as templates and expect an edit before first use:

- **`piv-validate`** has a placeholder command list. Put your project's real test, type-check, and lint commands
  in it.
- **`piv-commit`** and **`piv-create-pr`** read `.claude/references/conventions.md` if it exists, the first its
  `## commit` section and the second its `## pr` section. Create one and they'll follow your conventions instead
  of guessing.

`piv-review-pr` will hand its deep pass to a `code-reviewer` subagent if you have one in `.claude/agents/`. Without
it, the skill still works, it just does the review inline.

Everything else runs as-is. But read them anyway. A skill you haven't read is just a longer prompt you don't
control.

## License

MIT, see [LICENSE](LICENSE). Take them, fork them, rewrite them.

## Docs

### hooks/README.md
# Hooks

Six hooks I actually run, as copy-in files.

A rule *asks* the agent to behave. A hook **guarantees** it. Your rules file is guidance the model reads,
weighs against everything else in context, and follows most of the time. A hook is code the harness runs on a
lifecycle event, whether the model remembers it or not. The agent never chooses to invoke a hook, which is
precisely why a hook can guarantee anything at all.

The decision is one line:

> **If the consequence of the agent ignoring it is a minor annoyance, write a rule.
> If the consequence is a production incident, a leaked secret, or a broken deploy, write a hook.**

Most people's AI Layer is 90% rules and 0% hooks. That is backwards for the handful of things that must be
true every single time.

## Why this matters more than it sounds

There is a measurement behind this, not just a preference. In [Agentic Harness
Engineering](https://arxiv.org/abs/2604.25850) a research team let an agent rewrite its own harness for ten
rounds and measured which layer earned the gain. The system prompt it wrote for itself was genuinely good, 9 KB
of well-reasoned rules. Swapped into the baseline **on its own it scored below doing nothing** (67.4% against a
69.7% seed). Every point of the improvement came from the other layers: memory, tools, and middleware, which is
to say, from enforcement rather than instruction.

The arc inside that repo is the whole argument. The prompt already said "do not destroy verified state." The
agent ignored it. So at iteration 5 the loop wrote a guard into the shell tool that intercepted the destructive
command. It gave itself an override token. Three rounds later it took the override away from itself.

Rules got ignored. Guards did not.

## What ships here

| File | Event | What it does | Blocks? |
|---|---|---|---|
| `pre_tool_use_secrets.py` | **PreToolUse** | Refuses any route to a credential (env file, ssh keys, `.pem`, `.aws`, `.netrc`, or dumping the process environment) and refuses `rm -rf`. Committed `.env.example` is allowed. | **Yes** |
| `pre_tool_use_dependencies.py` | **PreToolUse** | Declared file coupling, enforced. The agent cannot edit a file until it has read that file's dependencies this session. | **Yes** (or injects) |
| `post_tool_use_log.py` | **PostToolUse** | Appends one JSONL line per tool call to `logs/agent-actions.jsonl`. A greppable audit trail of everything the agent did. | No |
| `session_start_context.py` | **SessionStart** | Injects what is true *today*: branch, uncommitted files, recent commits, plus any working-notes file. | No |
| `stop_tests_must_pass.py` | **Stop** | Runs your test command when the agent tries to finish. Red, and it blocks the stop and hands back the failures. | **Yes** |
| `stop_notify.py` | **Stop** | Native desktop notification when the turn ends, so you can walk away. | No |

That split is the mental model: **pre = gate, post = log.** Pre-hooks fire before the action, so they can stop
it. Post-hooks fire after, so all they can do is observe and react.

## Install

```bash
# from your project root
mkdir -p .claude/hooks
cp path/to/skills/hooks/*.py .claude/hooks/
cp path/to/skills/hooks/settings.json.example .claude/settings.json   # or merge the "hooks" block
```

If you already have a `.claude/settings.json`, **merge** the `hooks` block rather than replacing the file.
Hooks from different settings files merge; they do not overwrite each other.

Then pick your two edits:

- `stop_tests_must_pass.py` → set `TEST_COMMAND` to your actual test command.
- `pre_tool_use_dependencies.py` → copy `dependencies.example.json` to `.claude/hooks/dependencies.json` and
  declare your own couplings. **Until that file exists this hook allows everything**, so it is safe to install
  before you have configured it.

Commit `.claude/settings.json`. That is how the whole team inherits the same guarantees.

## Prove they work

Never trust a hook you have only read. A hook that always blocks and a hook that never blocks look identical
until the moment one of them fires wrong. Feed each one a payload and check the exit code:

```bash
# should BLOCK (exit 2)
echo '{"session_id":"t","cwd":".","tool_name":"Read","tool_input":{"file_path":".env"}}' \
  | uv run .claude/hooks/pre_tool_use_secrets.py; echo "exit=$?"

# should ALLOW (exit 0)
echo '{"session_id":"t","cwd":".","tool_name":"Read","tool_input":{"file_path":"README.md"}}' \
  | uv run .claude/hooks/pre_tool_use_secrets.py; echo "exit=$?"
```

For `stop_tests_must_pass.py` you must check **both** directions: exit 0 while the suite is green, exit 2 once
you deliberately break a test. If it exits 2 in both states your test command is not resolving - see the venv
note below, which is the cause roughly every time.

## The six things that will bite you

**1. The venv trap.** This is the one that wastes an afternoon. A hook runs under `uv run` in a throwaway
environment that has none of your project's packages, and it is not your shell, so your project's `.venv` was
never on `PATH` either. Strip uv's venv and `python` falls through to some global interpreter with the wrong
packages. Either way the hook exits 2 on a green suite and blames an unrelated module - it looks like a real
failure. `stop_tests_must_pass.py` handles both halves in `_project_env()`; steal it.

**2. `@file` mentions bypass PreToolUse entirely.** When you type `@config/secrets.yml` in your prompt, the file
is attached without a tool call, so no PreToolUse hook fires. Your guard covers what the *agent* reaches for,
not what *you* hand it.

**3. `additionalContext` must be nested.** It goes inside `hookSpecificOutput`, never at the top level. Put it
at the top level and Claude Code silently ignores it. No error, no warning, it just does not arrive.

**4. Exit code 1 does not block. Exit code 2 does.** This is backwards from every other CLI you use, where 1
means failure. In a hook, 1 is a non-blocking error: it is logged and the agent carries straight on. Only 2
blocks, and only on events that can block at all. Get it the wrong way round and you believe you are protected
when you are not, with nothing on screen to tell you otherwise.

**5. A `Stop` hook without a loop guard will spin.** It blocks the stop, the agent works, tries to stop, gets
blocked again. Claude Code caps this at **eight consecutive blocks** and then overrides the hook and ends the
turn with a warning, so it is a bounded spin rather than a true infinite loop, but you have still burned eight
turns going nowhere. Read `stop_hook_active` from the payload and stand down when it is true. Both `Stop` hooks
here do.

**6. Hooks run in a non-interactive shell.** No `~/.zshrc`, no `~/.bashrc`. A tool that is only on `PATH`
because of your shell profile works when you test by hand and fails when the hook runs it. And if your profile
prints anything at startup, that text mixes into the hook's stdout and breaks JSON parsing.

Debugging: `claude --debug` shows hook execution, and `CLAUDE_CODE_DEBUG_LOG_LEVEL=verbose` shows matcher
counts, which answers "did my matcher actually match."

## Exit codes

| Code | Meaning |
|---|---|
| `0` | Allow. stdout is parsed for JSON on the events that accept it. |
| `2` | **Block.** stderr goes back to the agent as the reason, so it adapts. |
| anything else | Non-blocking error. Shown to you, execution continues. |

Exit `1` is the trap: it means "error," and Claude Code logs it and carries on. If you meant to block and you
exit 1, nothing is blocked and you will not be told.

Only some events honor a block: `PreToolUse`, `UserPromptSubmit`, `Stop`, `SubagentStop`, `PreCompact`,
`PostToolBatch`, and a few others. `PostToolUse` cannot block, because the tool already ran.

## Beyond command hooks

Every hook here is a `command` hook, a script that gets JSON on stdin. There are four other handler types worth
knowing about, configured the same way in `settings.json`:

- **`prompt`** - send the event to a fast model and get an allow/deny back. For judgments a regex cannot make
  ("does this commit message describe what actually changed?").
- **`agent`** - spawn a subagent with real tools that can read the codebase before deciding. Expensive and
  slow; reserve it for gates worth a minute.
- **`http`** - POST the event to a server. This is how you enforce one policy across a whole org from one place.
- **`mcp_tool`** - call a tool on an MCP server you already have connected.

Command hooks are still the right default: they are instant, free, and you can read them.

## Two things to know

**Hooks run real code, automatically, with your credentials, with no sandbox.** Review a hook the way you
review a CI script. Only run hooks you have read and trust. Same caution as an MCP server.

**Coverage is yours.** The hook is guaranteed to *run*. What it *catches* is only as good as the check you
wrote. `pre_tool_use_secrets.py` covers three routes to a secret: the env file, the other credential files, and
the process environment. That third one matters more than it looks, because a guard that blocks the env *file*
but not the *environment* is mostly theatre when the same values are sitting right there in the shell.

What it deliberately does not cover is the two-step route: nothing stops the agent writing a script that reads
the environment and then running it, because the run looks innocent. Closing that means inspecting the
*content* of `Write` and `Edit` calls, not just the path, which roughly triples the size of the file. If you
are guarding something that matters, that is the next thing to add.

## Write your own without writing Python

Use the [`hooks-create`](../.claude/skills/hooks-create/SKILL.md) skill. Describe the guarantee in plain
English and it picks the event, writes the script, wires `settings.json`, and tests it:

```
/hooks-create "never let the agent edit anything under db/migrations/"
/hooks-create "run ruff on every python file the moment it's edited"
/hooks-create "ping me on Slack when the agent needs my input"
```

## Portability

Not a Claude Code party trick. Codex and Cursor use the same shape (a script, JSON on stdin, exit 2 to block);
Gemini CLI does the same job by reading a structured JSON decision instead of the exit code; Pi and opencode
run hooks in-process as plugins. Learn it once and it transfers, the same way `AGENTS.md` became the shared
rules file.

### .claude-plugin/plugin.json
```json
{
  "$schema": "https://json.schemastore.org/claude-code-plugin-manifest.json",
  "name": "skills",
  "displayName": "Cole's AI Skills",
  "version": "1.3.1",
  "description": "The PIV loop (plan, implement, validate, review, commit, PR) plus priming, planning, worktrees, and the meta-skills for building your own AI Layer.",
  "author": { "name": "Cole Medin", "url": "https://github.com/coleam00" },
  "homepage": "https://github.com/coleam00/skills",
  "repository": "https://github.com/coleam00/skills",
  "license": "MIT",
  "keywords": ["piv-loop", "planning", "code-review", "worktrees", "ai-layer", "agentic-coding"],
  "skills": ["./.claude/skills"]
}
```

### .claude-plugin/marketplace.json (excerpt)
```json
{
  "name": "cole-medin",
  "description": "Cole Medin's agent skills for building software with coding agents",
  "owner": { "name": "Cole Medin", "url": "https://github.com/coleam00" },
  "plugins": [
    {
      "name": "skills",
      "version": "1.3.1",
      "displayName": "Cole's AI Skills",
      "category": "productivity"
    }
  ]
}
```

## Top-level structure
- `.claude-plugin/` — `marketplace.json`, `plugin.json` — Claude Code plugin manifest, publishes this repo as the `skills` plugin under marketplace `cole-medin`.
- `.claude/skills/` — 35 skill folders (each a `SKILL.md`), organized in the README under: Prime (`prime-codebase`, `prime-backend`, `prime-frontend`), Plan (`plan-create-prd`, `plan-architecture`, `piv-slice-epic`, `plan-create-stories`), the PIV loop (`piv-plan-implementation`, `piv-implement`, `piv-validate`, `piv-review-changes`, `piv-fix-review-findings`, `piv-commit`, `piv-create-pr`, `piv-review-pr`, `piv-run-full-loop`), Issues (`piv-investigate-issue`, `piv-implement-issue`), Parallel work (`worktree-create`, `worktree-merge`), meta-skills (`rules-create-global`, `rules-check-drift`, `ablate-ai-layer`, `skills-create`, `hooks-create`, `opportunity-scan`, `system-execution-report`, `system-evolution-review`, `second-brain-audit`), Autonomy (`build-dark-factory`), and Tools (`agent-browser`, `ast-grep`, `drive-screen`, `setup-ai-tutor`). One additional folder present in the tree but not tabulated in the README: `second-brain-fix`.
- `hooks/` — six copy-in Python hook scripts (`pre_tool_use_secrets.py`, `pre_tool_use_dependencies.py`, `post_tool_use_log.py`, `session_start_context.py`, `stop_tests_must_pass.py`, `stop_notify.py`) plus `README.md`, `dependencies.example.json`, `settings.json.example`.
- `LICENSE` — MIT.
- `.gitattributes`, `.gitignore` — standard repo boilerplate.
