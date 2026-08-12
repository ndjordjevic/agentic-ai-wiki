---
type: source
category: "Agent Skills & plugins ecosystem"
source_url: https://github.com/UditAkhourii/neuroarxiv
tags: [arxiv, prior-art, research-grounding, evidence-driven, skill, architecture-decisions, source-skepticism]
related: [uditakhourii-adhd, aaravkashyap12-advise-project-approach, karpathy-autoresearch, anthropics-skills]
product: neuroarxiv
detail_level: standard
created: 2026-08-12
updated: 2026-08-12
---

`neuroarxiv` is an agent skill that forces Claude to consult real arXiv prior art before designing any non-trivial architecture, algorithm, or systems technique — producing one grounded recommendation with citations, a concrete first step, and documented failure modes pulled from the literature rather than invented from training data. Its defining discipline is isolate-then-converge: each paper is read by a parallel Agent call that sees only that one abstract, preventing any source from anchoring the reading of another, before a final convergence pass commits to a single recommended path and explains why the alternatives lost.

_All claims below are sourced from ../../raw/github/UditAkhourii-neuroarxiv.md unless otherwise noted._

## What it does

Before Claude designs something new, NeuroArxiv checks whether the hard part has already been solved and published — with the failure modes already known. The workflow is:

1. **Categorize** — maps the build problem onto 3–5 arXiv subject categories and 3–6 concrete search terms (the technical mechanism, not product jargon)
2. **Fetch** — makes real HTTP calls against `export.arxiv.org` API, category by category, never concurrently (courtesy rate-limiting); paper IDs, titles, and abstracts are real metadata, never invented
3. **Diverge** — spawns one isolated parallel Agent call per paper; each sees only ONE abstract, extracts approach, concrete implementable takeaway, limitation, and relevance note as JSON; isolation prevents cross-paper anchoring
4. **Score + cluster** — rates each reading 0–10 on relevance, practicality, and rigor; flags "traps" (limitations that imply failure modes a builder would rediscover the hard way); groups by underlying architectural angle
5. **Converge** — commits to ONE cluster as the recommended path; states why runner-ups lost; pulls pitfalls from every paper's limitations, not just the winner's

The explicit anti-patterns enforced by the skill: no invented arXiv IDs, no summarizing from memory, no letting isolation reads see each other, no open-ended "here are papers, you decide" output.

## Installation

```bash
npx github:UditAkhourii/neuroarxiv install
```

Installs to `~/.claude/skills/neuroarxiv`. Restart Claude Code (or start a new session) and `/neuroarxiv "<problem>"` is available. Manual install from a local clone:

```bash
git clone https://github.com/UditAkhourii/neuroarxiv.git
cd neuroarxiv && npm install && npm run build
node dist/cli.js install
```

## Architecture

The repository is a TypeScript Node.js project whose sole production output is the portable `skills/neuroarxiv/SKILL.md`. All TS/JS is installer scaffolding that copies the skill folder to `~/.claude/skills/`.

Key architectural decisions:

- **Real HTTP fetch, no LLM generation for paper discovery** — the categorize step uses LLM reasoning, but fetch is deterministic `export.arxiv.org` API calls
- **Parallel isolation in diverge** — each paper gets its own Agent context, preventing the anchoring failure where one abstract shapes the reading of the next
- **Forced single recommendation** — convergence is the deliberate departure from open-ended research: one path, one first step, one risk statement; runner-ups are explicitly eliminated with reasons
- **Source-skepticism as a first-class output** — in a 5-problem blind evaluation against cold and general web+arXiv search, NeuroArxiv produced 7 source-skepticism flags (catching a withdrawn proof, benchmark results validated only at one context length, etc.) vs. 0 for both alternatives

## Key features

- **Pre-flight gate:** explicit `/neuroarxiv` invocation bypasses self-check; implicit activation requires technical mechanism + real committed effort + open approach — skips for trivial CRUD, glue code, or already-converged decisions
- **Curated arXiv taxonomy** — `src/categories.ts` maps 20 arXiv categories (cs.AI, cs.LG, cs.CL, cs.DC, cs.IR, cs.CR, stat.ML, etc.) to problem domains
- **Trap flagging** — identifies and surfaces limitations in cited papers that represent failure modes, paired with a "strength" to avoid cherry-picking negatives
- **Evidence discipline** — every claim traces to a fetched abstract; abstract quotes are limited to a few consecutive words to prevent verbatim copying
- **Evaluated against baselines** — 5 cross-domain problems (physics, applied math, quantitative biology, ML, statistics) evaluated against cold and web+arXiv undisciplined conditions; NeuroArxiv beat web+arXiv by 1.1–1.3× on specificity and risk quality, lost on citation breadth in 2/5 problems (disclosed, not hidden)

## Example usage

```bash
neuroarxiv "cache LLM completions across requests without serving stale answers"
neuroarxiv "leader election for a queue with flaky nodes" --papers 6
```

Inside Claude Code:
```
/neuroarxiv "has anyone solved embedding-based deduplication at scale?"
/neuroarxiv "what's the state of the art for KV-cache compression?"
```

A typical output includes: TL;DR recommendation, recommended approach with cited arXiv papers (real IDs), concrete first step, why runner-up approaches were eliminated, and all prior-art pitfalls pulled from every paper's limitations section.

## When to use

- Before committing to a non-trivial architecture where prior art plausibly exists and the cost of guessing wrong is a rebuild
- When asking "has anyone solved this?" or "what's the state of the art?"
- When choosing between algorithms, protocols, retrieval strategies, or ML training approaches
- **Skip for:** trivial CRUD, glue code between two documented SDKs, already-converged decisions ("just implement it the simple way"), or when the user names a specific algorithm to use

## Maintenance status

- **Stars:** 308 (as of 2026-08-12)
- **Latest release:** no formal release tags
- **Default branch:** master
- **License:** MIT
- **Homepage:** https://www.divergent.sh/blog/neuroarxiv-never-build-from-scratch
- **Last push:** 2026-08-10

Actively developed by Udit Akhouri, the same author as [[uditakhourii-adhd]]. The Discord community coordinates arXiv category coverage, eval design, and integrations.

## Ecosystem

Sits in the same evidence-first, constraint-grounded skill cluster as [[aaravkashyap12-advise-project-approach]] (comparable-project research before committing to a stack), [[karpathy-autoresearch]] (autonomous research loops), and [[uditakhourii-adhd]] (parallel isolation for ideation). Where `advise-project-approach` researches comparable GitHub projects and operating costs, NeuroArxiv researches academic prior art from arXiv — the two skills are complementary for architectural decisions with both an engineering and a scientific prior-art angle.
