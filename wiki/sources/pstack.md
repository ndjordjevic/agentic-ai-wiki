---
type: source
category: "Coding-agent harnesses & methodologies"
source_url: https://github.com/cursor/plugins/tree/main/pstack
tags:
  - engineering-principles
  - playbooks
  - poteto-mode
  - subagent-routing
  - multi-model-workflows
  - cursor-plugin
related:
  - cursor-plugins
product: pstack
detail_level: standard
created: 2026-10-02
updated: 2026-10-02
---

pstack is Lauren "poteto" Tan's large third-party Cursor plugin for shipping high-quality, reviewable code with AI agents, built around the principle "if you want to go fast, go deep first." It packages a single sticky entry-point skill (`/poteto-mode`) that routes any task to one of 23 named playbooks, 23 standalone "principle" skills that auto-apply engineering discipline without explicit invocation, and a set of situational utility skills (`/how`, `/why`, `/architect`, `/arena`, `/swarm`, `/interrogate`, `/tdd`, `/unslop`, and more) that the playbooks call as needed. It is the deepest dive in this wiki into the [[cursor-plugins]] marketplace's `pstack` entry, extending that page's short summary into a full map of its routing model and principle catalog.

_All claims below are sourced from ../../raw/web/pstack.md unless otherwise noted._

## What it does
pstack turns Cursor into a structured "real engineering team" workflow rather than a single-shot code generator. The author types `/poteto-mode` at the start of nearly every task; the skill reads the request, matches it to one of 23 playbooks (investigation, bug fix, perf, hillclimb, runtime/trace forensics, feature, refactoring, prototype, visual parity, authoring-a-skill, eval, babysit, shipping, autonomous run, orchestrate, autopilot-full, autopilot-stack, session pickup, pause safely, multi-phase plan, worktree cleanup, and opening-a-pr), opens a todo list seeded with that playbook's steps verbatim, and then calls the other skills as those steps require them. `/poteto-mode` is a sticky mode: once entered it keeps applying itself across turns until the user opts out, and it is explicitly designed to pair with Cursor's `/loop` command for long unattended runs.

## Key features
- **Playbook-driven routing** — 23 playbooks cover read-only investigation, defect reproduction/fix, performance tracing against a baseline, sustained metric hillclimbing, forensic diagnosis from live instrumentation or captured profiling artifacts, net-new features, behavior-preserving refactors, throwaway prototypes for design comparison, pixel-exact visual parity, skill authoring, blinded prompt/skill evals, PR babysitting to merge-ready, verified stack shipping, long autonomous runs, multi-day multi-agent orchestration, and safe pause/resume of in-flight work.
- **Multi-model panel** — `/setup-pstack` lets the user pick a reasoning budget and assign specific models per role; out of the box, code-delegate work (feature, refactoring, bug fix, perf, hillclimb) routes to Grok while the hardest changes, prose, and judgment calls route to Opus 5.5, with a default panel of Opus 5.5 / Sol / Grok.
- **Named utility skills** — `/how` and `/why` answer "how does X work" and "why was Y built this way" (the latter querying available MCPs in parallel across source control, issue tracker, docs, chat, observability, error tracking, and analytics); `/architect` settles caller usage and module shape before a function-boundary change; `/arena` runs N parallel attempts at the same task to cherry-pick the best parts; `/swarm` runs N parallel workers across independent slices with one aggregated report; `/interrogate` has multiple models try to break a diff, including a strict code-quality lens; `/tdd` writes the failing test before the fix; `/no-comments` strips comments via a dedicated "Comment Sicko" reviewer subagent; `/unslop` removes AI writing tells; `/reflect` captures a completed task's recipe as a skill edit; `/show-me-your-work` logs a reviewable decision trail to a committable TSV.
- **Verification-skill generators** — `/create-verification-skill` and `/maintain-verification-skill` generate and keep in sync a project-local, language-agnostic "verify" skill with a feature map, so the agent always has a scripted way to prove app behavior rather than relying on self-report.
- **Subagents** — `subagent_type: "poteto-agent"` spawns a subagent that reads `poteto-mode` in full (including its inline principles index) before working, so its style matches the parent; substituting a generic subagent type skips that read and the style drifts. `subagent_type: "Comment Sicko"` is a read-only comment reviewer, normally invoked through `/no-comments` rather than directly.

## Architecture
The 23 principle skills are grouped into four categories, each auto-applying without explicit invocation: **core** (laziness-protocol, foundational-thinking, redesign-from-first-principles, attack-the-premise, subtract-before-you-add, minimize-reader-load, outcome-oriented-execution, experience-first, exhaust-the-design-space, build-the-lever), **architecture** (model-the-domain, boundary-discipline, type-system-discipline, make-operations-idempotent, migrate-callers-then-delete-legacy-apis, separate-before-serializing-shared-state), **verification** (prove-it-works, fix-root-causes, sequence-verifiable-units, test-behavior-not-implementation), and **delegation/meta** (guard-the-context-window, never-block-on-the-human, encode-lessons-in-structure). `poteto-mode` indexes all 23 inline and reads that index at task start; the standalone `principle-*/SKILL.md` files exist so other skills can reference a principle by name while pointing at its full rule.

## Example usage
```
/poteto-mode this pr has a subtle bug where the scroll drifts every 750ms even when idle. repro
first, then fix and verify.
```
```
/poteto-mode i'm going to bed. land the stack even if ci flakes. i want everything merged by
morning.
```
```
/swarm check every package under packages/ against its check.sh. one worker per package. one report.
```
Setup is two steps: run `/setup-pstack` to pick a reasoning budget and models, then invoke `/poteto-mode` on any task that needs rigor; a bundled "pstack guide" (`pstack/docs/guide/README.md`) walks a newcomer through a first real task end to end, from setup through overnight runs.

## When to use
Reach for pstack when adopting a dense, opinionated library of engineering-discipline skills on top of Cursor — particularly for teams that want a single sticky entry point (`/poteto-mode`) to route arbitrary tasks to the right playbook, want principle-level discipline (idempotency, boundary discipline, root-cause fixes) enforced automatically rather than requested per task, or want to multiplex work across several frontier models by role (code delegate vs. judgment/prose) without hand-picking a model per request.

## Ecosystem
pstack ships as one of the 13 plugins in [[cursor-plugins]], Cursor's official plugin marketplace repo, alongside `cursor-team-kit` (Cursor's own internal CI/PR workflows) and `thermos` (parallel security/code-quality audits); its playbook-and-principle structure is a dense, single-author counterpart to that marketplace's other skill bundles. Its multi-model routing (Grok for code delegates, Opus 5.5 for judgment) and parallel-worker skills (`/arena`, `/swarm`) echo the broader wiki pattern of agent harnesses that fan work across models or subagents rather than running a single model end to end.

## Further reading
- Flavio Copes, "pstack" walkthrough and review: https://flaviocopes.com/pstack/ (not yet ingested as a wiki source — bookmarked for later review)
