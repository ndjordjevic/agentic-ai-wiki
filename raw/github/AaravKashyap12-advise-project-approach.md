# AaravKashyap12/advise-project-approach

## Metadata
- Stars: 160
- Primary language: Python
- Default branch: main
- Latest release: v0.6.0 - Cross-harness portability (2026-08-11T17:00:46Z)
- License: MIT License
- Homepage: 
- Fetched: 2026-08-12
- Final URL: https://github.com/AaravKashyap12/advise-project-approach

## Description
A Claude/Codex skill that makes AI agents research comparable projects, tradeoffs, costs, and failure conditions before giving build advice.

## README
<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="./assets/brand/lockup-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="./assets/brand/lockup-light.svg">
    <img alt="advise-project-approach" src="./assets/brand/lockup-light.svg" width="680">
  </picture>
</p>

<p align="center"><strong>AI agents should not give project advice from vibes.</strong></p>

<p align="center">
  <strong>
    <a href="#one-line-install">Install</a> |
    <a href="./skills/advise-project-approach/SKILL.md">Skill source</a> |
    <a href="#whats-new-in-v060">What's new in v0.6</a> |
    <a href="#demo">Examples</a> |
    <a href="#evaluation">Tests &amp; evidence</a> |
    <a href="./CHANGELOG.md">Changelog</a> |
    <a href="./CONTRIBUTING.md">Contributing</a>
  </strong>
</p>

`advise-project-approach` is an agent skill for project planning, course correction, and review. Its portable `SKILL.md` can be loaded by Claude, Codex, pi, and other Agent Skills-compatible harnesses.

Before recommending a stack, architecture, vendor, refactor, or shipping plan, it checks:

- your actual constraints
- comparable real-world projects
- tradeoffs and failure conditions
- cost and lock-in realities
- when the recommendation becomes wrong

### Use It When

- you have a rough project idea and need a build plan
- your repo is getting messy and you need course correction
- you are choosing between stacks or vendors
- you want a review before shipping
- you want the agent to explain what not to build yet

### One-Line Install

```bash
npx skills@latest add AaravKashyap12/advise-project-approach --skill advise-project-approach
```

This uses the open `skills` installer to fetch the repo from GitHub and install only this skill. It requires Node.js/npm. Review installed skills before use; skills run with your agent's normal permissions.

### Source of Truth

The runtime skill spec lives in [skills/advise-project-approach/SKILL.md](./skills/advise-project-approach/SKILL.md). That file is the source of truth for the workflow agents actually run.

Everything else in this repo exists to package, explain, test, or distribute that skill.

### What's New in v0.6.0

v0.6 makes the skill portable across agent harnesses without removing the compatibility layers existing users rely on.

- Adds `AGENTS.md` as the shared repository guidance source, with a small `CLAUDE.md` import bridge for Claude Code.
- Documents installation for pi, Claude Code, Codex, and generic Agent Skills-compatible harnesses.
- Keeps the packaged `.skill`, Claude plugin manifest, and Codex `agents/openai.yaml` as additive compatibility layers.
- Adds a portability evidence matrix that separates structural compatibility from runtime claims.
- Adds release-version validation so `VERSION`, plugin metadata, and the README cannot silently drift apart.

See the [full changelog](./CHANGELOG.md) for earlier versions.

## AGENTS.md - Repository Guidance

# Repository Guidance

This repository packages one public skill: `advise-project-approach`.

## Source of Truth

- Edit the runtime skill at `skills/advise-project-approach/SKILL.md`.
- Do not edit `dist/advise-project-approach.skill` by hand. Rebuild it with `python scripts/package_skill.py`.
- Keep `.claude-plugin/plugin.json`, `skills/advise-project-approach/agents/openai.yaml`, `CHANGELOG.md`, and release notes in sync when changing their public metadata.

## Release Discipline

- Treat `VERSION` as the canonical release version.
- Every public push must bump `VERSION` using semantic versioning, update `.claude-plugin/plugin.json`, replace the README's single current `What's New` section and release-asset link, and add a dated entry to `CHANGELOG.md`.
- Rebuild `dist/advise-project-approach.skill` before committing.
- After pushing, create or update the matching `vX.Y.Z` GitHub release and attach the rebuilt `.skill` artifact.
- Do not accumulate old release summaries in the README; keep full history in `CHANGELOG.md`.

## Maintainer Agent Roles

- For each PR or issue task, create a fresh read-only communication sub-agent with the complete discussion, review, check, and linked-issue context. Use it to recommend or draft communication, then close it when the task is complete.
- Keep communication review separate from code review. Use an independent code-review sub-agent to inspect correctness, regressions, compatibility, security, and missing tests.
- Communication agents must not post, close, merge, label, or otherwise mutate GitHub without explicit maintainer authorization.
- Read the full conversation before replying, distinguish a useful idea from implementation quality, and credit ideas incorporated through a different implementation.
- A green check is necessary but not sufficient for merging. Accepted changes must also satisfy scope, behavior, compatibility, documentation, and release requirements.

## Validation

Before committing changes, run:

```bash
python scripts/validate_skill.py
python scripts/package_skill.py
python scripts/validate_skill.py
```

## Cross-Harness Compatibility

- `SKILL.md` is the portable runtime contract and must remain usable without optional metadata or adapters.
- Host-specific files are additive compatibility layers. Do not remove one harness's metadata merely to support another harness.
- Pi can discover the skill from `~/.agents/skills/` or `~/.pi/agent/skills/`.
- Claude Code can discover it from `~/.claude/skills/` and can use the optional plugin manifest.
- Codex can discover it from `~/.codex/skills/`; `agents/openai.yaml` supplies recommended UI metadata.
- Other Agent Skills-compatible harnesses can load the skill folder or point directly to `SKILL.md`.

## Top-level structure

```
├── .claude-plugin/           # Claude plugin manifest for plugin-aware installers
├── .github/                  # GitHub Actions workflows (validation)
├── .gitignore
├── .gitattributes
├── AGENTS.md                 # Repository guidance for agents (source of truth for cross-harness)
├── CLAUDE.md                 # Claude Code-specific guidance (import bridge)
├── CHANGELOG.md              # Full release history
├── CONTRIBUTING.md           # Contribution guidelines
├── LICENSE                   # MIT
├── README.md                 # This file
├── ROADMAP.md                # Future direction
├── SECURITY.md               # Security policy
├── VERSION                   # Canonical release version (0.6.0)
├── assets/                   # Brand assets (logo, SVG)
├── dist/                     # Packaged .skill archive (generated)
│   └── advise-project-approach.skill
├── evals/                    # Evaluation cases, test matrix, results
│   ├── README.md
│   ├── cases.json
│   ├── portability.md
│   └── results/
├── examples/                 # Demo outputs and scenario walkthroughs
│   ├── ab-comparisons.md
│   ├── pricing-operating-cost.md
│   ├── prebuild-bookmark-manager.md
│   ├── midbuild-express-api.md
│   └── postbuild-fastapi-template.md
├── scripts/                  # Build and validation tools
│   ├── package_skill.py
│   └── validate_skill.py
└── skills/
    └── advise-project-approach/   # Runtime skill folder
        ├── SKILL.md               # Portable skill source (runtime contract)
        └── agents/
            └── openai.yaml        # Codex UI metadata

Key observation: This is a skill distribution repo with a single production skill (SKILL.md) plus documentation, examples, evaluation, and cross-harness compatibility layers. The skill is evidence-driven project-approach advice, portable across Claude Code, Codex, pi, and generic Agent Skills-compatible runners.
```

## Changelog (Recent)

v0.6.0 - 2026-08-11
- Replaced the oversized README preview with a compact, theme-aware horizontal logo lockup.
- Added additive pi and generic Agent Skills installation guidance without removing Claude or Codex compatibility layers.
- Added `AGENTS.md` as cross-harness repository guidance while retaining `CLAUDE.md` as an import bridge.
- Added a portability evidence matrix that distinguishes structural compatibility from executed smoke tests.
- Added a canonical `VERSION` file and validation that keeps release metadata and the README current-version aligned.

v0.5.0 - 2026-08-11
- Added a turn-ending intake gate so vague project ideas cannot receive invented product or stack recommendations before constraints are known.
- Added required evidence status, constraint fit, comparable evidence, alternatives, failure conditions, and next actions to every completed recommendation.
- Added an explicit permission boundary before running repository tests, builds, linters, audits, benchmarks, or dependency installation.
- Added bounded first-pass repository inspection and external-research stopping rules.
- Added a reusable behavioral evaluation matrix, rubric, and the first recorded six-case forward-test report.

v0.4.0 - 2026-08-09
- Added a lightweight intake interview for vague pre-build requests while skipping unnecessary questions when constraints are already clear.
- Added user permission before researching current community signals from X, Reddit, and YouTube.
- Added capability routing, source fallback, and evidence-coverage disclosure for external research.
- Added optional Agent-Reach adapter guidance without bundling its dependencies or requiring installation.
- Added external-content prompt-injection and secret-handling guardrails.

## Fetch log

- Mode: standard
- Date: 2026-08-12
- Sections: Metadata, README, AGENTS.md, CHANGELOG, top-level structure
