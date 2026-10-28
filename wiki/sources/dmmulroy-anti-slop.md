---
type: source
category: "Coding-agent harnesses & methodologies"
source_url: https://github.com/dmmulroy/anti-slop
tags:
  - oxlint
  - typescript
  - javascript
  - lint-rules
  - anti-slop
  - code-quality
  - agent-guardrails
  - low-evidence-patterns
related:
  - leonxlnx-taste-skill
  - Nutlope-hallmark
  - openqodex-openqodex
  - sonarsource.com
  - coderabbit.ai
  - skills.sh
  - usehallmark.com
product: anti-slop
detail_level: standard
created: 2026-10-27
updated: 2026-10-28
---

dmmulroy/anti-slop (5,709 stars, MIT) is a set of opinionated Oxlint rules that reject low-evidence and low-signal TypeScript and JavaScript patterns, plus an agent skill that vendors them into your repo. It is a code-pattern linter, not a visual or aesthetic "anti-slop" pack like [[leonxlnx-taste-skill]]. The author calls it "first and foremost the ruleset I use with my work, projects, and team", reflecting taste rather than a universal standard.

_All claims below are sourced from ../../raw/github/dmmulroy-anti-slop.md unless otherwise noted._

## What it does

The rules target patterns that fabricate or discard type evidence: nested `as` assertions, widening known values to `unknown` or `object` and asserting back, `unknown` parameters and returns, `Record<string, unknown>` dictionaries, runtime `typeof` narrowing instead of boundary parsing, `Reflect.apply`/`Reflect.get`, module mocking, eager `filter().map()` chains, and reducers that copy their accumulator. A separate opt-in Effect group covers manual `_tag` comparison and construction. The README does not mention coding agents beyond the install skill and ignore patterns for agent directories, so the agent-guardrail framing in this wiki is an interpretation: the rules would flag such patterns in agent-written code.

## Installation

The project is meant to be vendored, not used as an npm dependency; there is no official npm package. The bundled skill does the copy and config:

```bash
npx skills add dmmulroy/anti-slop --skill install-anti-slop
```

Then ask the agent to install or configure anti-slop. It copies the plugin, installs Oxlint dependencies (matching an existing version), merges the plugin into the lint config, enables every generic rule, validates the result, and enables the Effect group if the repo depends on Effect. Updates are done by asking the agent to update "while preserving local customizations" (three-way merge when possible). Manual install: copy `src/` to e.g. `tools/oxlint/anti-slop/`, pin `oxlint` and `@oxlint/plugins` to the same exact version, and register `jsPlugins` in `oxlint.config.ts`.

## Key features

- **18 generic rules** — e.g. `no-array-filter-map`, `no-chained-type-assertions`, `no-known-value-widening`, `no-module-mocking`, `no-runtime-typeof`, `no-unknown-parameters`, `no-unsafe-dictionary-type`, `no-widen-then-assert`, `require-readable-spacing` (autofix), `require-safety-comment-for-type-assertion`.
- **5 Effect rules** — `no-manual-effect-error-tag`, `no-manual-tag-comparison`, `no-manual-tagged-construction`, `no-service-constructor-imports`, `prefer-effect-match`.
- **Safety-comment convention** — non-const assertions need a nearby `// SAFETY: ...` justification; markers are configurable.
- **Pairs with native Oxlint** — enable `oxc/no-accumulating-spread` alongside `no-reduce-accumulator-copy`.
- **Documented limits** — rules use Oxlint's ESTree and lexical-scope APIs, not a type checker, and do not infer imported types or cross-file signatures.

## Architecture

`src/` is canonical (an Oxlint JS plugin with `index.ts` and an `effect/index.ts` entry); `skills/` holds the install skill with a bundled copy, kept identical by `pnpm sync:skill-assets` and a CI drift check. A comment-aware spacing engine is vendored from ESLint Stylistic under MIT (`src/vendor/eslint-stylistic/UPSTREAM.md`). Also `scripts/`, `.oxlintrc.json`, `AGENTS.md`, `package.json`, and pnpm lockfile. `pnpm check` runs Oxlint, RuleTester suites, typechecking, and the drift check.

## Example usage

```ts
export default defineConfig({
  jsPlugins: [{ name: "anti-slop", specifier: "./tools/oxlint/anti-slop/index.ts" }],
  rules: { "anti-slop/no-chained-type-assertions": "error" }
});
```

Rejected: `const user = input as object as User;`. Accepted with justification: `// SAFETY: parseUserId validated the identifier before branding it.` followed by `const userId = value as UserId;`. Run `oxlint --fix` (or `vp lint --fix`), then your formatter.

## Maintenance status

5,709 stars, 155 forks, MIT License, primary language TypeScript, default branch `main`, most recent push 2026-10-14, no tagged releases. Because the project is vendored, upgrades are your responsibility; community forks and packages are welcome but have their own lifecycles. Has a [[skills.sh]] badge.
