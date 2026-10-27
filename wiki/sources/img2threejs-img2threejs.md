---
type: source
category: "Design & UI generation"
source_url: https://github.com/img2threejs/img2threejs
tags:
  - image-to-3d
  - three-js
  - procedural-3d
  - agent-skills
  - landing-page
  - quality-gated
  - apache-2
  - token-efficient
related:
  - oso95-scroll-world
  - calesthio-OpenMontage
  - leonxlnx-taste-skill
  - emilkowalski-skills
  - skills.sh
  - higgsfield.ai
product: img2threejs
detail_level: standard
created: 2026-10-27
updated: 2026-10-27
---

img2threejs/img2threejs (19,511 stars, Apache-2.0) is an agent skill that rebuilds the object in one reference image as a code-only, procedural, quality-gated, animation-ready Three.js model. It is "reconstruction-by-code, not photogrammetry, mesh extraction, or downloaded art packs", and deliberately token-efficient: deterministic Python scripts do validation and gating so model tokens go only to visual judgment and code. It runs under Hermes, Claude Code, Codex, or OpenCode. The README does not target landing pages specifically; the wiki groups it with design skill packs like [[emilkowalski-skills]] and [[leonxlnx-taste-skill]] because its output is a browser-rendered Three.js asset.

_All claims below are sourced from ../../raw/github/img2threejs-img2threejs.md unless otherwise noted._

## What it does

You give it one reference image; it produces a TypeScript `THREE.Group` factory that recreates the object from primitives, procedural shaders, and generated geometry, with a runtime hierarchy (pivots, sockets, colliders) so the result is ready to animate. Each subject is classified `object`, `character`, or `hybrid`: objects follow a hard-surface pipeline, characters an anatomy-aware track (head-unit proportions, facial landmarks, pose).

Before codegen, a detail-first analysis enumerates a `detailInventory` of identity-defining small details (gloss, bevels, screws, linework, wear), and a strict-quality gate blocks generation until it is complete. Opt-in paths cover maximum likeness (projection-first, with per-region confidence), multi-view silhouette carving (`geometryDescriptor.visualHull`), a material reference pipeline with a per-region comparison gate, and CS2 weapon review gates. The README's "Honesty about limits" section says a single image cannot reveal hidden sides, so output may be approximate, stylized, or low-poly, and "cannot reach the requested fidelity" is a valid result.

## Installation

Needs Node.js ≥ 18, Git, Python ≥ 3.10, and one of Claude Code, Codex, OpenCode, or Hermes.

```bash
npx --yes img2threejs@latest install   # links the skill into every agent it finds
npx --yes img2threejs@latest doctor    # one line per agent: "managed" means installed
```

Hermes users must also symlink the skill into their profile. Plugins use a separate harness: `npx --yes @img2threejs/img2@latest install --yes`, then `img2 add <id> --yes`. The base skill is not a plugin, so `img2 add` must not be used to install the repository. Restart the agent after installing.

## Key features

- **Staged sculpting pipeline** — `blockout → structural → form → material → surface → lighting → interaction → optimization`, one build pass at a time, self-correcting until each identity-defining feature clears its threshold.
- **Scripts enforce, the model judges** — scripts handle validation, gating, spec authoring, PBR extraction, and state; they never score visuals. The model reviews one reference-vs-render comparison sheet per pass.
- **Zero dependencies** — all scripts are pure Python 3.10+ standard library (PNG I/O via `struct` and `zlib`); no pip, PIL, numpy, or Playwright.
- **Fail-closed codegen** — `generate_threejs_factory.py` repeats the `--strict-quality` gate and returns `BLOCKED` rather than writing a shallow factory; it emits only the currently unlocked pass.
- **Plugin catalog (v2.0)** — `character`, `cs2`, `hello-cube`, `img2glb` (hosted TRELLIS), and a private `environment` plugin; plugins contribute checklist steps, raise-only quality floors, and blocking review gates.
- **Resumable workflow** — `forge/state.py` and `forge/next.py --state` resume from an evidence-backed checklist.

## Architecture

Top-level layout: `SKILL.md`, `forge/` (about ninety Python modules in stage folders: intake, spec, build, review, rig, `_shared`), `grimoire/` (rubrics for each gate), `integrations/` (optional GLB-baseline character pipeline with its own `pyproject.toml`), `docs/`, `scripts/`, `skills/`, `bin/`. Outputs are an `ObjectSculptSpec` JSON, a `createObjectNameModel(spec, options)` factory returning a `THREE.Group` with `userData.sculptRuntime` (and `userData.rig` for characters), and per-pass comparison sheets. Optional reference-fidelity tools (SAM2, Depth Anything V2, MediaPipe, Chrome DevTools, Playwright) never approve a pass or silently supply geometry. Full design: `docs/ARCHITECTURE.md`; token breakdown: `docs/TOKEN_COST.md`.

## Example usage

In Claude Code, attach an image and invoke:

```text
/img2threejs Rebuild the object in ./reference.png as a procedural Three.js model.
Keep its proportions, silhouette and colours. Follow the quality gates.
Report the output files, render-review evidence and any inferred regions.
```

For multi-session work, run `python3 forge/state.py init --reference <image> --profile character --spec object-sculpt-spec.json`, then `python3 forge/next.py --state .img2threejs/state.json`. Live demos (tropical island, robot, guitar, Starship, CS2 knives) are in the gallery at img2threejs.io.

## Maintenance status

19,511 stars, 1,635 forks, Apache License 2.0, primary language Python, default branch `main`, latest release 2.0.0 "The Plugin Update" (2026-09-06), most recent push 2026-10-27. Roadmap lists v2.1 (character split) through v3.0 (procedural worlds). Sponsored by MiniMax, Atlas Cloud, Tripo, and Hyper3D; the README states sponsorship pays for compute, not coverage.
