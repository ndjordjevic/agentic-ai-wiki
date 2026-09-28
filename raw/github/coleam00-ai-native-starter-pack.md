# coleam00/ai-native-starter-pack

## Metadata
- Stars: 76
- Forks: 28
- Primary language: Python
- Default branch: main
- Latest release: none
- License: none declared
- Homepage: (none)
- Fetched: 2026-09-28
- Final URL: https://github.com/coleam00/ai-native-starter-pack

## Description
(no repo description set)

## README
# AI Layer Starter Pack

The reusable **AI Layer** for agentic engineering - the skills, agents, and reference
docs you install **once** into any codebase. This is the generic foundation used in the
free *"AI-Native Engineering Org"* workshop: you install this, then **derive the rest from
your own code** and wire it into your team's process.

> **Install once → customize from your codebase.** The pack is intentionally generic.
> The codebase-specific part of the AI Layer - your `CLAUDE.md` rules and on-demand
> `.claude/context/` modules - you generate with the **`/create-rules`** skill below,
> reading *your* actual code. That's the whole idea: the AI Layer is your team's own
> knowledge and process, encoded.

## Install

```bash
# 1. Clone this pack
git clone https://github.com/coleam00/ai-native-starter-pack
# 2. Copy the AI Layer into your project (skills/agents/references + the Atlassian .mcp.json)
cp -r ai-native-starter-pack/.claude <your-repo>/.claude
cp ai-native-starter-pack/.mcp.json <your-repo>/.mcp.json
# 2a. Optional: turn on the two baseline hooks (env-file / rm -rf guardrail + an
#     audit-log trail). Commit the resulting settings.json so your whole team
#     inherits the guarantee.
cp ai-native-starter-pack/.claude/settings.json.example <your-repo>/.claude/settings.json
# 2b. Optional: the PR review workflow (needs a CLAUDE_CODE_OAUTH_TOKEN repo secret)
cp -r ai-native-starter-pack/.github <your-repo>/.github
# 3. In your repo, derive your rules from your real code:
#    run  /create-rules   → writes CLAUDE.md + .claude/context/ (cited to your code)
# 4. Wire external context: the pack ships a .mcp.json for the Atlassian MCP (Jira +
#    Confluence) - edit/replace it for your stack - then
#    run  /prime <jira-keys> <confluence-page-ids>
```

(Git submodule also works if you want to track upstream updates.)

## What's in here

**Context & priming**
- `prime` - load codebase context; optionally pull Jira issues + Confluence pages first (`prime [jira-keys] [confluence-page-ids]`, via the Atlassian MCP)
- `prime-backend` / `prime-frontend` - focused priming for one side of a full-stack repo

**Build the layer (codebase-specific, derived)**
- `create-rules` - **derive `CLAUDE.md` + `.claude/context/` from your real codebase** (Brownfield Type A). The one you run first per project.
- `create-prd` - greenfield: turn an idea into a PRD

**The PIV loop** (Plan → Implement → Validate - the core methodology)
- `plan-feature` - **P**lan: a context-rich, one-pass implementation plan
- `execute` - **I**mplement: build strictly from the approved plan
- `validate` - **V**alidate: run the project's tests / type-check / lint / build before a PR
- `commit` - structured commit at the end of a loop

**Review**
- `code-review` (+ the `code-reviewer` agent) - first-pass review on a diff/PR
- `code-review-fix` - apply review findings

**System evolution** (improve the AI Layer over time)
- `rca` - root-cause a bug *and* propose a rule + regression test so the class can't recur
- `system-review` - diff intent vs outcome; surface rules/context to tighten
- `execution-report` - capture what a loop actually did vs the plan

**Slicing & parallelism**
- `spec` - slice an epic / PRD into PIV-sized tickets with a dependency graph
- `new-worktrees` / `merge-worktrees` - run independent tickets in parallel git worktrees

**Examples / extras**
- `end-to-end-feature`, `implement-fix`, `ast-grep`, `init-project` - additional reusable skills

**Agents:** `code-reviewer`, `system-reviewer`, `research-agent`
**References (universal best-practice):** `architecture-patterns`, `backend-api-best-practices`, `frontend-component-best-practices`, `vertical-slice-architecture`
**MCP wiring:** `.mcp.json` - ships pointing at the **Atlassian MCP** (Jira + Confluence) so `prime` can pull tickets + linked spec pages out of the box; edit it to point at your own stack.
**Hooks:** `.claude/hooks/` - two generic, always-on guardrails (block reads of real secrets + `rm -rf`; log every tool call) plus `settings.json.example` to turn them on. See `.claude/hooks/README.md` for anything specific to your own workflow (a completion gate, an artifact hand-off between skills) - those have to be described to your agent, not copied from a generic pack.

## The diagrams from the workshop

The maps from the live session, free to reuse.

### The AI Layer at a glance

What actually goes in the layer: global rules and on-demand context, skills and agents, then the
wiring (MCP, hooks, LSP) that connects the agent to the tools you already use.

![The AI Layer at a glance](diagrams/ai-layer-at-a-glance.png)

### The same epic, two systems

The whole workshop in one frame. Same Confluence epic down two paths: one where the team burns
its time cleaning up slop, one where it ships. The only difference is the AI Layer.

![Two-lane SDLC map](diagrams/two-lane-sdlc.png)

### The AI-Native SDLC, in detail

The same flow with the tool zones (Confluence, Jira, your IDE, GitHub), the artifact produced at
each step, and the bug-to-rule loop that feeds the layer back into the next ticket.

![The AI-Native SDLC in detail](diagrams/ai-native-sdlc-detailed.png)

## Relationship to the Dynamous Agentic Coding course

This is a **focused subset** for the 2-hour workshop - enough to build the AI Layer and run
the PIV loop + system evolution end-to-end. The full **Dynamous Agentic Coding course** goes
much deeper across many more modules, commands, subagents, and the complete validation,
remote-coding, MCP, and Archon workflows. This pack is the on-ramp.

## License / use

Free to use. Built for attendees of the *"AI-Native Engineering Org Transformation"* workshop, but
you don't need to have been there. Clone it, install it, make it yours.

## Docs

### .claude/hooks/README.md
# Hooks — the deterministic layer of the AI Layer

Hooks are the fifth primitive. Rules, subagents, tools, and skills are all things the agent *reaches for*.
A hook is the one the agent never chooses: it fires automatically on a lifecycle event.

> **A rule asks the agent to behave. A hook guarantees it.**
>
> Reach for a rule when "usually" is fine. Reach for a hook when it **must** happen every single time.

## What ships here

| File | Event | What it does | Can it block? |
|---|---|---|---|
| `pre_tool_use.py` | **PreToolUse** | Blocks reading/writing/searching a real env file (committed `.env.example` templates are allowed) and blocks `rm -rf`. Prints the reason to stderr and `exit(2)` → the tool is stopped and the agent is told why, so it adapts. | **Yes** — this is the guarantee |
| `post_tool_use.py` | **PostToolUse** | Appends every tool call to `logs/post_tool_use.json` — a full audit trail of what the agent did. | No — the tool already ran; observe only |

That split *is* the mental model: **pre = gate, post = log.** This is deliberately the whole hooks layer this
pack ships — always-on safety, generic to any codebase. Anything more specific to *your* workflow (a checker
that gates completion, an artifact hand-off between two skills) is a conversation with your agent away, not a
file to copy — see below.

### Exit codes — the one thing to get right

**Only `exit 2` blocks.** Not exit 1, which is what every linter, type checker and test runner returns on
failure. Converting one into the other is most of what a gate-style hook does.

| Exit | Meaning |
|---|---|
| `0` | success. stdout goes to the debug log (except on `UserPromptSubmit` / `SessionStart`, where it becomes context) |
| **`2`** | **blocking error.** stderr is handed to the agent as the reason |
| anything else | non-blocking error: noise, no effect |

What `exit 2` blocks depends on the event:

| Event | Does `exit 2` block? |
|---|---|
| `PreToolUse` | **yes** — the tool call is stopped (`pre_tool_use.py` relies on this) |
| `Stop` | **yes** — the session is prevented from finishing |
| `PostToolUse` | **no** — the tool already ran; stderr is merely shown, so `post_tool_use.py` always exits 0 |

## Turning them on

Hooks are the one primitive that does something the moment it exists, so the pack ships the wiring as a
**template** rather than a live file:

```bash
cp .claude/settings.json.example .claude/settings.json
```

`.claude/settings.json` is gitignored here in the pack so the hooks don't fire while you're reading the
material. **In your own project, commit it** — that's how the whole team inherits the same guarantees. If you
already have a `settings.json`, merge the `hooks` block in rather than overwriting it.

## Try it

```
ask the agent to read your env file          -> blocked (exit 2, reason handed back)
ask it to read a committed .env.example       -> allowed
ask it to run `rm -rf ...`                    -> blocked
any normal command                            -> allowed, and logged to logs/post_tool_use.json
```

You can also test a hook directly, without the agent:

```bash
echo '{"tool_name":"Read","tool_input":{"file_path":".env"}}' | uv run .claude/hooks/pre_tool_use.py; echo "exit=$?"
```

`exit=2` means the guard fired.

## Building your own — you don't have to write Python by hand, and this pack doesn't ship examples on purpose

The two hooks above are deliberately generic — safe defaults for any codebase. The moment you want something
specific to *your* workflow (gate completion on your own checks, hand an artifact from one skill to the next,
auto-format on edit), that's not something a generic starter pack can hand you as a ready file — it has to
know your commands, your paths, your checks. Describe it to your agent instead, in plain English, e.g.:

> "Don't let me finish until my tests pass — run my test command when I try to stop, and if it fails, block the
> stop and tell me why."

Claude Code (and most current coding agents) can pick the right lifecycle event, write the script, and wire it
into `settings.json` for you from a description like that — no need to hand-write hook JSON. Common shapes
worth knowing by name before you ask for one:

- **react** (`PostToolUse`) — something fires because a file changed. Auto-format on edit is the classic case.
- **gate** (`Stop`) — the agent can't declare done while your checks are red. **Bound it yourself** — a
  hook has no memory, so if it can retry, give it its own attempt counter on disk. Don't trust an
  undocumented flag to bound a loop for you; verify what actually happens before you rely on it.
- **baton** — one skill's artifact lands, and the hook starts the next skill in a **fresh** context. Guard it
  on file state (input present, output absent), never on memory — the guard is what makes it safe to fire a
  hundred times and act exactly once.

## Two things to know

- **Hooks run real code, automatically, with your credentials, with no sandbox.** Review a hook the way you'd
  review a CI script. Only run hooks you have read and trust. This is the same caution as MCP servers.
- **Coverage is yours.** The hook is guaranteed to *run*; what it *catches* is only as good as the check you
  wrote. It is the enforcement point, not omniscience.

## Portability

This is not a Claude Code party trick. Codex and Cursor use the same shape (a script, JSON on stdin,
`exit 2` to block); Gemini CLI does the same job by reading a structured JSON decision instead of the exit
code; Pi and opencode run hooks in-process as plugins. Learn it once, it transfers — the same way `AGENTS.md`
became the shared rules file.

## Top-level structure
- `.claude/` — the AI Layer payload meant to be copied wholesale into a target repo:
  - `skills/` — 22 skill folders: `prime`, `prime-backend`, `prime-frontend` (context/priming); `create-rules`, `create-prd` (build the layer, codebase-specific); `plan-feature`, `execute`, `validate`, `commit` (the PIV loop); `code-review`, `code-review-fix` (review); `rca`, `system-review`, `execution-report` (system evolution); `spec`, `new-worktrees`, `merge-worktrees` (slicing & parallelism); `end-to-end-feature`, `implement-fix`, `ast-grep`, `init-project` (examples/extras); `agent-browser`.
  - `agents/` — `code-reviewer.md`, `system-reviewer.md`, `research-agent.md`.
  - `references/` — `architecture-patterns.md`, `backend-api-best-practices.md`, `frontend-component-best-practices.md`, `vertical-slice-architecture.md`.
  - `hooks/` — `pre_tool_use.py`, `post_tool_use.py`, `README.md`.
  - `settings.json.example` — the hooks wiring template; `.claude/settings.json` itself is gitignored in the pack so hooks stay inert until a consumer opts in.
- `.github/workflows/claude-review.yml` — the optional PR-review workflow (needs a `CLAUDE_CODE_OAUTH_TOKEN` repo secret), copyable alongside `.claude/`.
- `.mcp.json` — ships pre-wired to the Atlassian MCP (Jira + Confluence) so `prime` can pull tickets and linked spec pages; meant to be edited/replaced per consumer's stack.
- `diagrams/` — three PNG diagrams from the live workshop (`ai-layer-at-a-glance.png`, `two-lane-sdlc.png`, `ai-native-sdlc-detailed.png`).
- `.gitignore` — standard.
