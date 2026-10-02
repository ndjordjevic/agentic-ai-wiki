---
type: source
category: "Coding-agent harnesses & methodologies"
source_url: https://github.com/michael-denyer/pstack-claude
tags:
  - poteto-mode
  - subagent-routing
  - multi-runtime
  - claude-code-plugin
  - codex-plugin
  - engineering-principles
related:
  - pstack
  - cursor-plugins
product: pstack-claude
detail_level: standard
created: 2026-10-02
updated: 2026-10-02
---

pstack-claude is Michael Denyer's community port of Lauren "poteto" Tan's Cursor plugin [[pstack]] to Claude Code, Codex, OpenCode, Gemini CLI, and Prime Agent. It carries the same `/poteto-mode` entry point, playbook routing, and principle-skill catalog across harnesses other than Cursor, tracking pstack's upstream revisions plus its own named policy forks declared in `tools/forks.json`.

_All claims below are sourced from ../../raw/github/michael-denyer-pstack-claude.md unless otherwise noted._

## What it does
pstack-claude re-implements [[pstack]]'s skill tree — `poteto-mode` plus its playbooks, principle skills, and utility skills (`how`, `why`, `architect`, `arena`, `swarm`, `interrogate`, `tdd`, `unslop`, and more) — for runtimes that are not Cursor. All runtimes share one skills tree (`plugins/pstack/skills/`); Claude Code and Codex additionally get native plugin packaging and an automatic SessionStart routing hook that invokes `poteto-mode` when a task touches multiple files, involves a design/architecture decision, or concerns a bug with an unknown cause or a performance issue. A companion plugin, `agent-formal-verify`, adds TLA+ model checking and Lean proofs for concurrency bugs that tests cannot reach.

## Installation
- **Claude Code**: `/plugin marketplace add michael-denyer/pstack-claude` then `/plugin install pstack@pstack-claude`.
- **Codex**: `codex plugin marketplace add michael-denyer/pstack-claude` then `codex plugin add pstack@pstack-claude`; Codex requires trusting the installed hook via `/hooks`.
- **Prime Agent, OpenCode, Gemini CLI, or skills-only installs**: clone the repo and symlink each directory under `plugins/pstack/skills/` into `~/.agents/skills/`, or install via the `skills` CLI (`npx skills add .../plugins/pstack/skills --skill "*" --agent "*" --yes`).
- `setup-pstack` (`/pstack:setup-pstack` on Claude Code) configures per-role model defaults, per-role reasoning effort, and can turn the automatic routing hook off.

## Key features
- **Runtime support matrix** — Claude Code and Codex are fully tested (native plugins with automatic routing hooks); Prime Agent and Gemini CLI rely on documented shared-directory discovery but are untested in a live session; opencode's skill discovery was verified on v1.18.25. A Claude-to-other-runtime tool/model mapping (`poteto-mode/references/codex-tools.md`) translates tool names and model defaults for Codex.
- **Upstream tracking plus named forks** — the skill tree is synced against a pinned upstream pstack revision (`12d587d`, v0.15.5); `tools/sync.mjs`, `tools/upstream.json`, and `tools/substitutions.json` manage the sync and Cursor→Claude rewrite rules, while `tools/forks.json` declares deliberate policy deviations from upstream.
- **Port scope** — includes 7 ported `cursor-team-kit` skills plus an independently authored `babysit` skill (PR monitoring/CI-fix/merge-readiness); explicitly excludes Cursor-specific automations, sticky-mode metadata, the Grok Bot UI workflow, and the Cursor UI tutorial.
- **Generated artifacts and CI checks** — `tools/generate.mjs` regenerates versions, model defaults, Codex prompt stubs, and reference files from a single slash-command table; `tests/readme-facts.test.mjs` checks skill counts and the upstream pin stay in sync; CI also validates shell scripts, workflows, Markdown, relative links, and the installed skills CLI output.
- **Same slash-command surface as pstack** — 54 skill directories (31 public skills, 23 `principle-*` references) expose the same command set documented on the [[pstack]] page (`/poteto-mode`, `/how`, `/why`, `/architect`, `/arena`, `/swarm`, `/interrogate`, `/tdd`, `/unslop`, `/no-comments`, `/babysit`, `/fix-ci`, `/fix-merge-conflicts`, and more).

## Architecture
Repository layout separates the Claude Code (`.claude-plugin/`) and Codex (`.codex-plugin/`) marketplace/plugin manifests from the shared `plugins/pstack/skills/` tree used by every runtime; `plugins/pstack/agents/` holds Claude Code subagent definitions and `plugins/pstack/hooks/` the SessionStart routing hook shared by Claude Code and Codex. `tools/` carries the generator, validator, and upstream-sync scripts that keep the port's generated files (prompt stubs, reference docs, version/model defaults) consistent with the canonical slash-command table.

## Example usage
```
Use poteto-mode to fix the search filter resetting when I change pages.
```
As with upstream pstack, this reproduces the failure, investigates with `how`/`why`, delegates the fix (bringing in `architect` first if it crosses a function boundary), and reruns the failing case before reporting back with failing-then-passing evidence.

## Maintenance status
Actively maintained: 747 stars, 95 forks, MIT-licensed, latest release `v0.9.57` (2026-10-01), last pushed 2026-10-02. Maintenance follows a documented sync boundary in `CONTRIBUTING.md` — skill-tree changes track upstream pstack, while runtime adaptations and workflow changes (declared as named forks) land directly in this repo. No telemetry or server component; local scripts use the user's GitHub CLI login for PR-related workflows.

## Ecosystem
pstack-claude is the multi-runtime counterpart to [[pstack]] (itself part of the [[cursor-plugins]] marketplace), carrying the same playbook/principle-skill structure to Claude Code, Codex, OpenCode, Gemini CLI, and Prime Agent rather than Cursor alone. It is a concrete example of the broader wiki pattern of community ports that track an upstream agent-skill bundle while adapting tool names, model defaults, and packaging per harness.

## Further reading
- Flavio Copes, "pstack" walkthrough and review: https://flaviocopes.com/pstack/ (not yet ingested as a wiki source — bookmarked for later review)
