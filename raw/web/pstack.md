# pstack

## Fetch log
- Inbox URL: https://github.com/cursor/plugins/tree/main/pstack
- Final URL: https://github.com/cursor/plugins/tree/main/pstack
- Fetched: 2026-10-02
- Pages: 1
- Mode: single-page

## Page — https://github.com/cursor/plugins/tree/main/pstack

i'm [poteto](https://x.com/poteto). i'm not a president or ceo, but i've worked with millions of lines of code at Meta, Netflix, and Cursor. i'm also on the react core team where i help build and maintain react compiler.

there's a growing sense that ai writes too much slop code. i agree. i don't want to ship like a team of twenty slop artists. throughput without quality is not a goal i aspire to. if you want to go fast, go deep first.

**pstack is my answer.** these are the same skills i use everyday to ship high quality code at Cursor. this turns cursor into a real engineering team. the goal is not to maximize loc, in fact it's the opposite. pstack helps you write less, but higher quality code.

**pstack gives you fearless parallelism.** when you can go deep on one agent and trust it to write good, verifiable code, you can truly parallelize with confidence. start multiple agents up with `poteto-mode` and trust that they'll apply rigorous engineering principles to their work.

**cursor gives you the best of all worlds.** every frontier model has its strengths and weaknesses. use any model with pstack. in fact, many of my skills use multi-model workflows to take advantage of each model's unique strengths.

fork it. improve it. make it yours. PRs are welcome!

two steps:

1. run `/setup-pstack` (pstack/skills/setup-pstack/SKILL.md), pick a reasoning budget, and choose which models you want.
2. use `/poteto-mode` (pstack/skills/poteto-mode/SKILL.md) whenever you're doing anything that requires rigor.

new here? the pstack guide (pstack/docs/guide/README.md) walks you through a first real task, from setup and prompting through verification and overnight runs.

that's it. the other skills are situational; the mode skill uses them for you as needed. out of the box the mode splits work by model strength: code delegates (feature, refactoring, bug fix, perf, hillclimb) go to grok, while the hardest changes, prose, and judgment go to opus 5.5. the default panel is opus 5.5 / sol / grok. `/setup-pstack` changes any of it.

use `/poteto-mode` at the start of a task. it reads your request, picks from a set of playbooks, and runs the other skills as the steps need them.

this skill is the main shortcut. i use it whenever i need the agent to do rigorous engineering work. it comes with twenty-three playbooks:

```
/poteto-mode this pr has a subtle bug where the scroll drifts every 750ms even when idle. repro
first, then fix and verify.
```

```
/poteto-mode i'm going to bed. land the stack even if ci flakes. i want everything merged by
morning.
```

### the twenty-three playbooks

| playbook | for |
|---|---|
| investigation | a read-only question. how does x work, why was y built this way, are we sure. |
| bug fix | reproduce a defect, root-cause it, and fix with runtime evidence. |
| perf | trace a measured slowness and improve it against a baseline. |
| hillclimb | sustained, scientific improvement of one metric against a target, looping hypotheses with before/after measurement and one commit per accepted win. |
| runtime forensics | diagnose a live symptom (leak, idle-cpu spin, glitch) from instrumentation. |
| trace forensics | diagnose a captured profiling artifact (cpuprofile, trace, spindump, heap snapshot). |
| feature | new or changed behavior, built from a named data shape. |
| refactoring | a behavior-preserving change to structure or shape. |
| prototype | a throwaway sketch to make a design or behavioral decision cheaply, or to settle an empirical fork by observing it. |
| visual parity | pixel-exact ui equivalence between two implementations. |
| authoring a skill | writing or editing a SKILL.md. |
| eval | test how a skill or prompt change affects agent behavior, blinded. |
| babysit | drive a pr or a stack to merge-ready: conflicts, review threads, ci. |
| shipping | independently verify a green stack, then land the contiguous verified run bottom-up through github by default or origin when available. |
| autonomous run | drive a long task to completion without stopping. |
| orchestrate | a standing project handed to one coordinator chat: multi-day, many stacked prs, fleets of subagents. |
| autopilot-full | run independent prs to merged with one owner per pr and a root swarm verdict on each round, from the code-ready head on. |
| autopilot-stack | build and verify one linear base-branch stack for the operator to review and land. |
| session pickup | resume or take over a prior agent's in-flight work. |
| pause safely | suspend in-flight work cleanly so it can be resumed later. |
| multi-phase plan | work that spans phases or stacked PRs. |
| worktree cleanup | reclaim disk by pruning merged or abandoned worktrees and stale ios simulators, safety-gated. |
| opening a pr | open a ready pr from small ordered commits with a conventional commits title and a briefing-style body. invoked at the end of every other playbook. |

when invoked it:

1. matches your task to a playbook and opens a todo list whose first items are its steps, copied in verbatim.
2. routes to the other skills as the steps fire.
3. writes unslopped replies framed for the consumer and the maintainer.

the full rules and playbooks live in `skills/poteto-mode/SKILL.md`.

`/poteto-mode` is also a sticky mode: once entered it stays on across turns, applying itself when a playbook matches or the task needs rigor and staying out of the way otherwise. opt out any time by saying so.

`/poteto-mode` works extremely well with cursor's `/loop` command. you can make cursor work for many hours without sacrificing rigor.

`/poteto-mode` runs most of these for you when a step needs them (`how`, `why`, `architect`, `arena`, `swarm`, `interrogate`, `unslop`, `no-comments`, `technical-writing`, `tdd`, and the principles). the table below is for when you want one directly:

```
/how do we cancel runs? do we have an n+1 when we look up every run to cancel?
```

```
/interrogate review this pr.
```

### all skills

| skill | use it when |
|---|---|
| `/poteto-mode` | default entry point for any non-trivial task. |
| `/how` | you want a walkthrough of how a subsystem works. |
| `/why` | you want to know why something was built this way. discovers available MCPs at run time and queries each evidence category in parallel (source control, issue tracker, long-form docs, real-time chat, infra observability, error tracking, analytics warehouse). |
| `/recall` | you're starting or resuming work and want your recent context on a topic rebuilt from your own chat history and the shared record, handed back as a tight current-state brief. |
| `/blast-radius` | you have a small-looking change and want to know what else it could break, with the one fact it's safe because of proven by running code, not asserted. |
| `/architect` | you're about to write code that crosses a function boundary and want the caller's usage, types, and module shape settled first. |
| `/arena` | you want N parallel attempts at the same thing, then to grab the best parts of each. |
| `/swarm` | you want N parallel workers across different slices or races, then one aggregated report. |
| `/interrogate` | you have a diff and want several different models to try to break it, including a strict code-quality lens. |
| `/automate-me` | you want your own `-mode` skill, drafted from how you've actually worked. |
| `/make-bot-ui` | you want a page or dashboard whose buttons wake a Grok Bot over a webhook, including the sender-key handoff and Tailscale. |
| `/setup-pstack` | you want to pick which models pstack uses per role. detects your models and writes a config rule. |
| `/reflect` | a long task landed and you want the recipe captured as a skill edit. |
| `/teach` | you want to actually understand a change or subsystem, not just have it summarized. runs how + why and weaves one plain explanation, built up diagram by diagram. |
| `/tdd` | you're fixing a bug and there's a cheap local test path. write the failing test first, then the fix. |
| `/no-comments` | strip comments before review; spawns Comment Sicko, fixes accepted findings, offers encodings for claimed constraints. |
| `/typescript-best-practices` | you're reading or editing typescript. grounds the type-system-discipline principle in syntax. |
| `/figure-it-out` | no bundled playbook fits. designs a rigorous, auditable playbook for the task. |
| `/show-me-your-work` | you want a reviewable decision trail. logs decisions to a tsv you can commit. |
| `/create-verification-skill` | your project has no scripted way to prove app behavior. generates a project-local verify skill with a feature map, for any language or platform. |
| `/maintain-verification-skill` | your verify skill's feature map has drifted from the app. source wave + one live pass, at most one PR of proven corrections. |
| `/unslop` | you're cleaning up writing. removes AI tells. |
| `/bro` | you want the last message restated in plain human language, no jargon. |
| `/technical-writing` | layered doc standard (Diátaxis + Google developer style + STE + Global English) for docs, RFCs, readmes, PR descriptions, commit messages. |

mostly i type `/poteto-mode` at the start of a task and let it route to a playbook. the other skills fire as the steps need them. a few i reach for directly.

### all the examples

```
bug fix:           /poteto-mode this pr has a subtle bug where the scroll drifts every 750ms even
                   when idle. repro first, then fix and verify.
perf:              /poteto-mode a big list takes a second or two to load even though we virtualize.
                   run a cpu trace and tell me why.
feature:           /poteto-mode build a small feature behind a feature flag. verify it really works.
prototype:         /poteto-mode build two prototypes of the markdown renderer so we can compare.
                   spawn an agent for each.
multi-phase:       /poteto-mode open source these skills as a plugin. nothing internal leaks, work
                   in a temp dir, show me the dependency graph first.
overnight run:     /poteto-mode i'm going to bed. land the stack even if ci flakes. i want
                   everything merged by morning.
babysit:           /poteto-mode check on pr 123. anything outstanding?
visual parity:     /poteto-mode the row spacing is too tall when this flag is on. the second image
                   is correct. repro and fix until it matches.
figure it out:     /poteto-mode i'm stepping away. migrate every caller from the synchronous store
                   to the new async one, keeping behavior identical. i want to trust it was done
                   right when i'm back.
how:               /how do we cancel runs? do we have an n+1 when we look up every run to cancel?
why:               /why is this feature flag not on yet?
architect:         design this instrumentation to be high signal with no false positives. /architect
                   this first.
arena:             /arena take my prompt to the arena verbatim. i want to compare their proposals
                   with yours.
swarm:             /swarm check every package under packages/ against its check.sh. one worker per
                   package. one report.
interrogate:       /interrogate review this pr.
tdd:               /tdd implement
unslop:            can we unslop and tighten the new changes?
reflect:           /reflect that took too long. capture what we learned so the next run doesn't
                   repeat it.
show-me-your-work: /show-me-your-work keep a decision trail i can review when i'm back.
automate-me:       /automate-me
```

### the `poteto-agent` and Comment Sicko subagents

pstack also ships a subagent that runs my style end to end. spawn it from a parent agent via `subagent_type: "poteto-agent"` (pstack/agents/poteto-agent.md). it reads `poteto-mode` in full, including its inline principles index, before doing any work. substituting `generalPurpose` skips that read and drifts.

`/poteto-mode` and `subagent_type: "poteto-agent"` route through the same wrapper.

pstack also ships Comment Sicko (pstack/agents/comment-sicko.md), a read-only comment reviewer available as `subagent_type: "Comment Sicko"`. usually invoke it through `/no-comments`, not directly.

twenty-three short skills, one principle each. `poteto-mode` indexes them inline and reads that index at task start. the standalone files are there so other skills can reference a principle by name, and so the index can point at the full rule for each.

### all twenty-three principles

| principle | group | rule |
|---|---|---|
| laziness-protocol | core | Bias toward deletion and the smallest change that solves the problem. |
| foundational-thinking | core | Apply before writing logic: choosing core types and data structures, sequencing scaffold-vs-feature work, asking what concurrent actors share. Get the data structures right so downstream code becomes obvious. |
| redesign-from-first-principles | core | Redesign as if the requirement had been a foundational assumption from day one, instead of bolting it on. |
| attack-the-premise | core | Apply when two or more fixes that share one premise have failed the same gate. Take a census of which actors hold the imbalance before the next fix, then question the premise instead of writing another fix that assumes it. |
| subtract-before-you-add | core | Remove dead weight, redundant validators, and stub references first, then build on the simpler base. |
| minimize-reader-load | core | Count layers between question and answer, and hidden state in the reader's head; collapse one-caller wrappers and shrink mutable scope. |
| outcome-oriented-execution | core | Apply during planned rewrites and migrations with explicit phase boundaries. Converge on the target architecture; don't preserve smooth intermediate states with throwaway compatibility code. |
| experience-first | core | Choose user delight over implementation convenience; ship fewer polished features over more rough ones. |
| exhaust-the-design-space | core | Build 2-3 competing prototypes and compare side by side before committing. |
| build-the-lever | core | Apply to any non-trivial work, not just bulk work: edits, migrations, analyses, checks. Build the tool that does it or proves it (codemod, script, generator, or a skill your subagents follow) instead of working by hand. The tool is the artifact a reviewer can rerun. |
| model-the-domain | architecture | Encode the domain in a structure instead of scattered conditionals. |
| boundary-discipline | architecture | Concentrate guards at system boundaries (CLI, config, network, external APIs); trust internal types and keep business logic in pure functions. |
| type-system-discipline | architecture | Make illegal states unrepresentable, brand semantic primitives, parse external data at boundaries, refuse to lie to the compiler, exhaust variants, derive from authoritative schemas. |
| make-operations-idempotent | architecture | Converge to the same end state regardless of partial prior runs. |
| migrate-callers-then-delete-legacy-apis | architecture | Migrate callers and delete the old API in the same wave instead of preserving compatibility layers. |
| separate-before-serializing-shared-state | architecture | Eliminate the sharing first; serialize structurally only when one shared writer is a real invariant. |
| prove-it-works | verification | Apply after completing a task, before declaring done. Verify against the real artifact (run the feature, read the actual value, inspect the diff), not a proxy, self-report, or 'it compiles.'. |
| fix-root-causes | verification | Trace each symptom to its root cause and fix it there; reproduce first, ask why until you reach it, resist nil-check guards that silence crashes. |
| sequence-verifiable-units | verification | Apply to multi-step work (sweeps, migrations, runs of similar edits) and to how you stack commits and PRs. Break work into small units that each end in a verifiable state, check each before the next, and order delivery so the sequence proves itself to a reviewer. |
| test-behavior-not-implementation | verification | Apply when you write, change, or keep a test. Call the code the way its users do and assert the result they observe against a literal expected value. If the test would still pass when every imported function returns undefined, rewrite the assertion or delete the test. |
| guard-the-context-window | delegation | Route bulk to subagents; keep summaries in the main thread, not raw payloads. |
| never-block-on-the-human | delegation | Proceed, present the result, let the human course-correct after the fact; reserve confirmation for irreversible actions. |
| encode-lessons-in-structure | meta | Encode the rule as a lint, metadata flag, runtime check, or script instead of more text. |

Note: capture truncated after the principles table (remaining content beyond this point was not fetched in this ingest — primarily closing boilerplate).
