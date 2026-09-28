---
type: source
category: "Agent Skills & plugins ecosystem"
source_url: https://github.com/coleam00/ai-native-starter-pack
tags:
  - ai-layer
  - piv-loop
  - claude-code-hooks
  - workshop-material
  - atlassian-mcp
  - codebase-derived-rules
related:
  - coleam00-skills
  - anthropics-skills
  - obra-superpowers
  - gsd-build-get-shit-done
  - coleam00-agent-control-plane
product: ai-native-starter-pack
detail_level: standard
created: 2026-09-28
updated: 2026-09-28
---

Cole Medin's copy-in "AI Layer" starter pack: a `.claude/` folder of skills, agents, reference docs, an MCP wiring, and two baseline hooks meant to be dropped once into any codebase and then customized from that codebase's own code. It is the free, workshop-scoped companion to [[coleam00-skills]] — a smaller, generic 22-skill subset (vs. that repo's 35) built for a 2-hour "AI-Native Engineering Org Transformation" session and explicitly framed as an on-ramp to the fuller paid Dynamous Agentic Coding course.

_All claims below are sourced from ../../raw/github/coleam00-ai-native-starter-pack.md unless otherwise noted._

## What it does

The pack installs by literally copying its `.claude/` directory and `.mcp.json` into a target repo, then running one skill (`/create-rules`) to derive that repo's own `CLAUDE.md` and `.claude/context/` modules from its actual code — the pack itself stays generic; the codebase-specific layer is generated, not shipped. The core methodology is the same PIV loop (Plan → Implement → Validate) as [[coleam00-skills]], here named `plan-feature` → `execute` → `validate` → `commit`, wrapped by priming (`prime`, `prime-backend`, `prime-frontend` — `prime` can pull Jira issues and Confluence pages via the bundled Atlassian MCP before loading context), review (`code-review` plus a `code-reviewer` agent, and `code-review-fix`), system evolution (`rca`, `system-review`, `execution-report`), and slicing/parallelism (`spec`, `new-worktrees`, `merge-worktrees`). `create-prd` covers the greenfield case where `create-rules` (brownfield, derived-from-code) doesn't apply.

## Key features

- **Derive, don't copy, the codebase-specific layer**: `create-rules` reads the consumer's real code to write `CLAUDE.md` + `.claude/context/`, rather than shipping generic rules that would go stale.
- **Atlassian MCP wired in by default**: `.mcp.json` points at Jira + Confluence out of the box so `prime <jira-keys> <confluence-page-ids>` can pull ticket and spec context before planning; meant to be edited or replaced for a different stack.
- **Two generic, always-on hooks only**: `pre_tool_use.py` (blocks reads/writes/searches of real env files and blocks `rm -rf`, committed `.env.example` templates excepted) and `post_tool_use.py` (append-only audit log to `logs/post_tool_use.json`). The pack deliberately ships no more than this — anything workflow-specific (a completion gate, an artifact hand-off between skills) is meant to be described to the agent rather than copied as a file, since it has to encode the consumer's own commands and paths. (../../raw/github/coleam00-ai-native-starter-pack.md)
- **Hooks wiring ships inert**: `.claude/settings.json` is gitignored in the pack itself so the hooks don't fire while reading the material — a consumer opts in with `cp .claude/settings.json.example .claude/settings.json` and is told to commit the result so the whole team inherits the guarantee. (../../raw/github/coleam00-ai-native-starter-pack.md)
- **Optional PR-review workflow**: `.github/workflows/claude-review.yml`, copyable alongside `.claude/`, needs a `CLAUDE_CODE_OAUTH_TOKEN` repo secret to run.
- **Three named hook shapes for building more**: the hooks README teaches "react" (`PostToolUse` — e.g. auto-format on edit), "gate" (`Stop` — block finishing until checks pass, with a self-bounded retry counter since a hook has no memory), and "baton" (one skill's output triggers the next skill in a fresh context, guarded on file state rather than memory so it's safe to fire repeatedly and act exactly once). (../../raw/github/coleam00-ai-native-starter-pack.md)

## Architecture

The repo is a plain file tree, not a Claude Code plugin (no `.claude-plugin/` manifest) — it is designed to be `git clone`d or added as a git submodule and then partially `cp -r`'d into a consumer repo: `.claude/` wholesale, `.mcp.json`, optionally `.claude/settings.json.example` → `settings.json`, and optionally `.github/workflows`. (../../raw/github/coleam00-ai-native-starter-pack.md) `.claude/` breaks into `skills/` (22 folders), `agents/` (`code-reviewer.md`, `system-reviewer.md`, `research-agent.md`), `references/` (four universal best-practice docs: `architecture-patterns.md`, `backend-api-best-practices.md`, `frontend-component-best-practices.md`, `vertical-slice-architecture.md`), and `hooks/`. (../../raw/github/coleam00-ai-native-starter-pack.md) The hooks README frames hooks as "the fifth primitive" alongside rules, subagents, tools, and skills — the one the agent never chooses to invoke, because it fires automatically on a lifecycle event — with the same rule-vs-hook split documented in [[coleam00-skills]]'s hook set: only `exit 2` blocks (not the more familiar `exit 1`), and which events honor a block differs (`PreToolUse` and `Stop` do; `PostToolUse` cannot, since the tool already ran). (../../raw/github/coleam00-ai-native-starter-pack.md) The README also notes hook portability: Codex and Cursor share the same script/stdin-JSON/exit-2 shape, Gemini CLI reads a structured JSON decision instead of the exit code, and Pi/opencode run hooks in-process as plugins. (../../raw/github/coleam00-ai-native-starter-pack.md)

## Installation

```bash
# 1. Clone this pack
git clone https://github.com/coleam00/ai-native-starter-pack
# 2. Copy the AI Layer into your project (skills/agents/references + the Atlassian .mcp.json)
cp -r ai-native-starter-pack/.claude <your-repo>/.claude
cp ai-native-starter-pack/.mcp.json <your-repo>/.mcp.json
# 2a. Optional: turn on the two baseline hooks
cp ai-native-starter-pack/.claude/settings.json.example <your-repo>/.claude/settings.json
# 2b. Optional: the PR review workflow (needs a CLAUDE_CODE_OAUTH_TOKEN repo secret)
cp -r ai-native-starter-pack/.github <your-repo>/.github
# 3. In your repo, derive your rules from your real code:
#    run  /create-rules   → writes CLAUDE.md + .claude/context/ (cited to your code)
# 4. Wire external context: edit/replace .mcp.json for your stack, then
#    run  /prime <jira-keys> <confluence-page-ids>
```
A git submodule also works if the consumer wants to track upstream updates. (../../raw/github/coleam00-ai-native-starter-pack.md)

## Example usage

Testing the secrets/`rm -rf` guard directly, without the agent: `echo '{"tool_name":"Read","tool_input":{"file_path":".env"}}' | uv run .claude/hooks/pre_tool_use.py; echo "exit=$?"` — `exit=2` means the guard fired. (../../raw/github/coleam00-ai-native-starter-pack.md) To ask for a workflow-specific hook beyond the two generic ones, the README's suggested phrasing is plain English to the agent, e.g. "Don't let me finish until my tests pass — run my test command when I try to stop, and if it fails, block the stop and tell me why." (../../raw/github/coleam00-ai-native-starter-pack.md)

## When to use

Best fit for a team running (or evaluating) a first pass at a Claude Code "AI Layer" without committing to the larger, more idiosyncratic [[coleam00-skills]] set — a smaller, generic 22-skill surface plus an explicit codebase-derivation step (`create-rules`) that produces the team's own rules rather than shipping someone else's. It particularly suits teams already using Jira/Confluence, given the pack's default Atlassian MCP wiring. Because it ships only two hooks (both safety-only, no gate/react/baton examples included), teams wanting a fuller hooks catalog out of the box should look at [[coleam00-skills]]'s six-hook set instead and treat this pack's hooks README as a how-to-build-your-own guide rather than a ready library.

## Maintenance status

76 stars, 28 forks, no declared license, primary language Python (the hook scripts), default branch `main`, no tagged GitHub releases. Most recently pushed 2026-08-24. Built and maintained by Cole Medin (coleam00) as the companion material for a specific "AI-Native Engineering Org Transformation" workshop; framed in its own README as a deliberately narrower on-ramp to the paid Dynamous Agentic Coding course rather than a standalone, continuously expanding project. (../../raw/github/coleam00-ai-native-starter-pack.md)
