# cursor/plugins

## Metadata
- Stars: 2428
- Primary language: TypeScript
- Default branch: main
- Latest release: none published
- License: none declared in repo metadata (README states MIT)
- Homepage: (none)
- Fetched: 2026-07-24
- Final URL: https://github.com/cursor/plugins

## Description
Cursor plugin specification and official plugins.

## README
# Cursor plugins

Official Cursor plugins for popular developer tools, frameworks, and SaaS products. Each plugin is a standalone directory at the repository root with its own `.cursor-plugin/plugin.json` manifest.

## Plugins

| `name` | Plugin | Author | Category | `description` (from marketplace) |
|:-------|:-------|:-------|:---------|:-------------------------------------|
| `continual-learning` | [Continual Learning](continual-learning/) | Cursor | Developer Tools | Incremental transcript-driven memory updates for AGENTS.md using high-signal bullet points only. |
| `cursor-team-kit` | [Cursor Team Kit](cursor-team-kit/) | Cursor | Developer Tools | Internal team workflows used by Cursor developers for CI, code review, shipping, local automation, and verification. |
| `thermos` | [Thermos](thermos/) | Cursor | Developer Tools | Thermo-nuclear branch review: deep security/correctness audits, harsh code-quality rubrics, parallel subagents, thermos orchestration, and optional merge-ready PR flows. |
| `create-plugin` | [Create Plugin](create-plugin/) | Cursor | Developer Tools | Scaffold and validate new Cursor plugins. |
| `agent-compatibility` | [Agent Compatibility](agent-compatibility/) | Cursor | Developer Tools | CLI-backed repo compatibility scans plus Cursor agents that audit startup, validation, and docs against reality. |
| `cli-for-agent` | [CLI for Agents](cli-for-agent/) | Cursor | Developer Tools | Patterns for designing CLIs that coding agents can run reliably: flags, help with examples, pipelines, errors, idempotency, dry-run. |
| `pr-review-canvas` | [PR Review Canvas](pr-review-canvas/) | Cursor | Developer Tools | Render PR diffs as interactive Cursor Canvases organized for reviewer comprehension — groups changes by importance, separates boilerplate from core logic, and highlights tricky or unexpected code. |
| `docs-canvas` | [Docs Canvas](docs-canvas/) | Cursor | Developer Tools | Render documentation — architecture notes, API references, runbooks, and codebase walkthroughs — as a navigable Cursor Canvas with sections, table of contents, diagrams, and cross-references. |
| `cursor-sdk` | [Cursor SDK](cursor-sdk/) | Cursor | Developer Tools | Build apps, scripts, CI pipelines, and automations on top of the Cursor TypeScript SDK (@cursor/sdk) — runtime selection, auth, streaming, MCP, error handling, and ready-to-extend integration patterns. |
| `orchestrate` | [Orchestrate](orchestrate/) | Cursor | Developer Tools | Fan large tasks out across parallel Cursor cloud agents with planners, workers, verifiers, and structured handoffs. |
| `pstack` | [pstack](pstack/) | Lauren Tan | Developer Tools | if you want to go fast, go deep first. pstack helps you write less, but higher quality code. rigorous agent workflows you can parallelize with confidence. |

Author values match each plugin's `plugin.json` `author.name` (Cursor lists `plugins@cursor.com` in the manifest).

Two additional plugins exist in the repo tree but are not yet listed in the README table (present as top-level directories with valid `.cursor-plugin/plugin.json` manifests, discovered via the contents API on 2026-07-24):
- `ralph-loop` — Ralph Loop: continuous self-referential AI loops for iterative development (the "Ralph Wiggum technique" — run the agent in a while-true loop with the same prompt until task completion).
- `teaching` — Teaching: skill mapping, practice plans, and learning retrospectives; builds personalized roadmaps with milestones and practice checkpoints, and runs periodic reviews to adjust based on progress.

## Repository structure

This is a multi-plugin marketplace repository. The root `.cursor-plugin/marketplace.json` lists all plugins, and each plugin has its own manifest:

```
plugins/
├── .cursor-plugin/
│   └── marketplace.json       # Marketplace manifest (lists all plugins)
├── plugin-name/
│   ├── .cursor-plugin/
│   │   └── plugin.json        # Per-plugin manifest
│   ├── skills/                # Agent skills (SKILL.md with frontmatter)
│   ├── rules/                 # Cursor rules (.mdc files)
│   ├── mcp.json               # MCP server definitions
│   ├── README.md
│   ├── CHANGELOG.md
│   └── LICENSE
└── ...
```

## License
MIT

## Docs

### All plugins and skills (fetched from each plugin's `skills/*/SKILL.md` frontmatter, 2026-07-24)

13 plugins, 75 skills total. Each skill entry is `name — description` from its `SKILL.md` frontmatter.

### agent-compatibility

- **check-agent-compatibility** — Run the full repository compatibility pass: scanner score, startup path, validation loop, and docs reliability.

### cli-for-agent

- **cli-for-agents** — Designs or reviews CLIs so coding agents can run them reliably: non-interactive flags, layered --help with examples, stdin/pipelines, fast actionable errors, idempotency, dry-run, and predictable structure. Use when building a CLI, adding commands, writing --help, or when the user mentions agents, terminals, or automation-friendly CLIs.

### continual-learning

- **continual-learning** — Orchestrate continual learning by delegating transcript mining and AGENTS.md updates to `agents-memory-updater`.

### create-plugin

- **create-plugin-scaffold** — Create a new Cursor plugin scaffold with a valid manifest, component directories, and marketplace wiring. Use when starting a new plugin or adding a plugin to a multi-plugin repository.
- **review-plugin-submission** — Audit a Cursor plugin for marketplace readiness. Use when validating manifests, component metadata, discovery paths, and submission quality before publishing.

### cursor-sdk

- **cursor-sdk** — Guide users building apps, scripts, CI pipelines, or automations on top of the Cursor TypeScript SDK (`@cursor/sdk`). Triggers on `Agent.create`, `Agent.prompt`, `Agent.resume`, `agent.send`, `run.stream`, `CursorAgentError`, or `@cursor/sdk` mentions; running Cursor agents programmatically from a script, CI/CD pipeline, GitHub Action, or backend service; choosing local vs. cloud runtime; configuring MCP servers for an SDK agent; or handling streaming, cancellation, or errors. Also covers porting REST `/v1/agents` calls to the SDK. Used eagerly rather than answered from memory since the SDK surface evolves.

### cursor-team-kit

- **check-compiler-errors** — Run compile and type-check commands and report failures.
- **control-cli** — Build or adapt a local harness to drive, inspect, and profile an interactive CLI or TUI without external services. Use for CLI UX checks, startup regressions, memory leaks, hangs, prompt flows, or terminal demos.
- **control-ui** — Build or adapt a local browser/CDP harness to drive and inspect a web, IDE, or Electron UI. Use for local UI verification, screenshots, accessibility snapshots, perf profiles, visual diffs, or reproducing UI bugs.
- **deslop** — Remove AI-generated code slop and clean up code style.
- **fix-ci** — Find failing PR checks, inspect logs or external check links, and apply focused fixes.
- **fix-merge-conflicts** — Resolve merge conflicts non-interactively, validate build and tests, and finalize conflict resolution.
- **get-pr-comments** — Fetch and summarize review comments from the active pull request.
- **loop-on-ci** — Monitor PR checks and fix failures until green, using `gh pr checks` as the source of truth for PR-attached checks.
- **make-pr-easy-to-review** — Prepare PRs for review by cleaning noisy history, improving PR descriptions, and adding reviewer guidance without changing code behavior.
- **new-branch-and-pr** — Create a fresh branch, complete work, and open a pull request.
- **pr-review-canvas** — Generate an interactive PR review walkthrough as an HTML page: fetches PR data via `gh` API, categorizes files into core vs. mechanical changes, adds reviewer annotations, and renders diffs with moved-code detection.
- **review-and-ship** — Review the current branch for bugs, intent fit, and test coverage; run or write tests; commit focused work; open or update a PR.
- **run-smoke-tests** — Run Playwright smoke tests, debug failures, and verify fixes.
- **thermo-nuclear-code-quality-review** — Run an extremely strict maintainability review for abstraction quality, giant files, and spaghetti-condition growth.
- **verify-this** — Verify a claim with fresh local evidence: restate it falsifiably, capture baseline and treatment, compare artifacts, and return VERIFIED, NOT VERIFIED, or INCONCLUSIVE.
- **weekly-review** — Produce a weekly synthesis of authored commits with highlights by bugfix, tech debt, and net-new work.
- **what-did-i-get-done** — Summarize authored commits over a user-specified time period into a concise update.
- **workflow-from-chats** — Extract durable working preferences from recent Cursor chats and convert them into skills, rules, or workflow docs.

### docs-canvas

- **docs-canvas** — Render a documentation-style Cursor Canvas that organizes architecture notes, API references, walkthroughs, and how-tos into a navigable layout with sections, tables of contents, and cross-references.

### orchestrate

- **orchestrate** — Used only when the user explicitly types `/orchestrate <goal>`: decomposes a large task, spawns a tree of parallel cloud-agent workers/subplanners/verifiers via the Cursor SDK, and collects structured handoffs; does not invoke autonomously.

### pr-review-canvas

- **pr-review-canvas** — Render a PR diff review as a Cursor Canvas that groups changes by reviewer importance, separates boilerplate from core logic, and highlights tricky or unexpected code.

### pstack

pstack ships one general-purpose skill per named workflow plus a large library of standalone "principle" skills (each auto-applies to matching situations rather than being explicitly invoked):

- **architect** — Sketch types, signatures, and module structure before code, then stay in the loop while implementation fills in. Use for non-trivial work where jumping to code would lock in the wrong shape.
- **arena** — Spawn N parallel candidates at the same task, pick a base, graft the strongest parts of the losers into it.
- **automate-me** — Draft or revise a personal "-mode" skill capturing the user's preferences or working style, via create-skill + unslop.
- **blast-radius** — Find what a change could break elsewhere before it ships, and prove the one fact it's safe because of by running real code rather than writing it up.
- **create-verification-skill** — Generate a project-local verification skill that drives an app the way a user does, for any language/framework/platform.
- **figure-it-out** — Design an auditable playbook when no narrower one fits (a large migration or ambitious multi-part change); scales rigor to the task and logs decisions via show-me-your-work.
- **how** — Explain subsystem architecture, runtime flow, and onboarding mental models; answers placement/ownership/layering questions and can critique architecture.
- **interrogate** — Multiple LLM reviewers challenge changes from independent angles (adversarial/multi-model review).
- **maintain-verification-skill** — Periodic pass that keeps a project's verification skill and feature map honest via parallel source readers and one live driving session.
- **Poteto Mode** — An agent working-style mode: concise detailed responses, deliberate subagents, unslopped prose, simple code, verified work.
- **principle-boundary-discipline** — Concentrate validation/error-handling guards at system boundaries; trust internal types and keep business logic in pure functions.
- **principle-build-the-lever** — Build the tool that does or proves non-trivial work (codemod, script, generator, skill) instead of doing it by hand.
- **principle-encode-lessons-in-structure** — Encode a recurring correction as a lint, metadata flag, runtime check, or script instead of restating it in prose.
- **principle-exhaust-the-design-space** — Build 2–3 competing prototypes and compare side by side before committing, for novel UI or architectural decisions.
- **principle-experience-first** — Choose user delight over implementation convenience; ship fewer polished features over more rough ones.
- **principle-fix-root-causes** — Trace each debugging symptom to its root cause and fix it there rather than adding guard clauses that silence crashes.
- **principle-foundational-thinking** — Get core types and data structures right before writing logic so downstream code becomes obvious.
- **principle-guard-the-context-window** — Route bulk output to subagents; keep summaries, not raw payloads, in the main thread.
- **principle-laziness-protocol** — Bias toward deletion and the smallest change that solves the problem when refactoring.
- **principle-make-operations-idempotent** — Design commands and lifecycle steps to converge to the same end state regardless of partial prior runs.
- **principle-migrate-callers-then-delete-legacy-apis** — Migrate callers and delete the old API in the same wave instead of preserving compatibility layers.
- **principle-minimize-reader-load** — Collapse one-caller wrappers and shrink mutable scope to reduce what a reader must hold in their head.
- **principle-model-the-domain** — Encode the real domain in a data structure instead of scattering it across conditionals.
- **principle-never-block-on-the-human** — Proceed on reversible work and let the human course-correct after the fact; reserve confirmation for irreversible actions.
- **principle-outcome-oriented-execution** — Converge directly on the target architecture during planned rewrites instead of preserving throwaway compatibility states.
- **principle-prove-it-works** — Verify task output against the real artifact (run the feature, inspect the diff) rather than a proxy or self-report.
- **principle-redesign-from-first-principles** — Redesign as if a new requirement had been a foundational assumption from day one, instead of bolting it on.
- **principle-separate-before-serializing-shared-state** — Eliminate sharing between concurrent writers first; serialize structurally only when one shared writer is a real invariant.
- **principle-sequence-verifiable-units** — Break multi-step work into small units that each end in a verifiable state, checked in order.
- **principle-subtract-before-you-add** — Remove dead weight and redundant validators first, then build on the simpler base.
- **principle-type-system-discipline** — Make illegal states unrepresentable; brand semantic primitives; parse external data at boundaries; exhaust variants.
- **recall** — Reconstruct recent working context from chat history, live state, and the shared record, then hand back a tight current-state brief.
- **reflect** — Spawn three parallel review subagents over the active transcript, surface learnings, and route each to a concrete skill edit.
- **setup-pstack** — Configure which models pstack uses per role; writes an always-applied rule overriding skill defaults.
- **show-me-your-work** — Keep a reviewable TSV decision-trail log (what, why, evidence, result) for long-running or unattended work.
- **tdd** — Used only when the user explicitly asks for TDD, a failing test, or a regression test, or the bug has an obvious cheap local test target.
- **teach** — Explain a body of work plainly by running the `how` and `why` skills and weaving their findings into one clear explanation.
- **typescript-best-practices** — TypeScript best practices; used when reading or editing any `.ts`/`.tsx` file.
- **unslop** — Cut AI tells from any writing; must always apply.
- **why** — Discover available MCPs and query each evidence category (source control, issue tracker, docs, chat, observability, error tracking, analytics) in parallel, then return a cited read on decisions and tradeoffs.

### ralph-loop

- **cancel-ralph** — Cancel an active Ralph Loop.
- **ralph-loop-help** — Explain the Ralph Loop plugin, how it works, and available skills.
- **ralph-loop** — Start a Ralph Loop: an iterative development loop that reruns the same prompt until task completion (the "Ralph Wiggum technique").

### teaching

- **create-learning-path** — Build a personalized learning roadmap with milestones and practice checkpoints.
- **run-learning-retrospective** — Evaluate learning progress, identify blockers, and adjust the learning plan.

### thermos

- **thermo-nuclear-code-quality-review** — Run an extremely strict maintainability review for abstraction quality, giant files, and spaghetti-condition growth.
- **thermo-nuclear-review** — Comprehensive security and correctness audit of a branch's changes: bugs, breaking changes, security issues, devex regressions, feature-gate leaks.
- **thermos** — Launch both thermo-nuclear review subagents in parallel, then synthesize their findings.

## Top-level structure

- `.cursor-plugin/` — root marketplace manifest (`marketplace.json`) listing all plugins.
- `.github/` — repo CI/community config (skipped, boilerplate).
- `README.md` — plugin marketplace table (see above).
- `schemas/` — `marketplace.schema.json` and `plugin.schema.json`, the JSON Schemas that validate the marketplace manifest and each plugin's `plugin.json`.
- `scripts/` — `validate-plugins.mjs`, a validation script for plugin manifests (likely run in CI to check submissions against the schemas).
- 13 plugin directories at repo root (`agent-compatibility/`, `cli-for-agent/`, `continual-learning/`, `create-plugin/`, `cursor-sdk/`, `cursor-team-kit/`, `docs-canvas/`, `orchestrate/`, `pr-review-canvas/`, `pstack/`, `ralph-loop/`, `teaching/`, `thermos/`) — each with its own `.cursor-plugin/plugin.json` manifest and a `skills/` subdirectory of `SKILL.md`-based agent skills (see Docs above for full skill listing). Several also carry `rules/` (`.mdc` Cursor rules), `mcp.json` (MCP server definitions), `hooks/` (e.g. `ralph-loop`), or `assets/` (logos/avatars).
