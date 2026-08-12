# UditAkhourii/neuroarxiv

## Metadata
- Stars: 308
- Primary language: TypeScript
- Default branch: master
- Latest release: none
- License: MIT License
- Homepage: https://www.divergent.sh/blog/neuroarxiv-never-build-from-scratch
- Fetched: 2026-08-12
- Final URL: https://github.com/UditAkhourii/neuroarxiv

## Description
A skill to kill from-scratch coding — Claude checks real arXiv prior art before it designs a new architecture.

## README

# NeuroArxiv — a skill to kill from-scratch coding

> **Before Claude designs something new, it checks arXiv first.**

Real papers, fetched over real HTTP, read in isolation so no source anchors
another, converged into ONE recommendation — cited, with a first step and
the known ways this has already gone wrong for somebody else. Not a search
wrapper: search finds you sources, NeuroArxiv forces a decision grounded in
them.

Reach for it before committing to non-trivial architecture, algorithms, or
systems techniques — anywhere real prior art plausibly exists and the cost
of guessing wrong is a rebuild, not a typo.

### Fair fight: cold vs. general web search vs. NeuroArxiv

Not "research vs. no research" — the real question is whether NeuroArxiv's
isolate-then-converge discipline beats a plain capable agent with normal web
+ arXiv access and no special process.

| | Cold | Web + arXiv (undisciplined) | **NeuroArxiv** |
| --- | :---: | :---: | :---: |
| Problems with a source-skepticism flag | 0/5 | 0/5 | **5/5** |
| Total flags | 0 | 0 | **7** |

Zero vs. zero vs. seven, out of five problems each. NeuroArxiv caught a
withdrawn proof it had cited and declined to rely on it.

### Install

```bash
npx github:UditAkhourii/neuroarxiv install
```

Installs to `~/.claude/skills/neuroarxiv`. Restart Claude Code (or start a
new session) and `/neuroarxiv "<problem>"` is live.

### How it works

```
PROBLEM
  │
  ▼
0. CATEGORIZE  — map the problem onto 3-5 arXiv categories + search terms
  │
  ▼
1. FETCH       — real HTTP against export.arxiv.org, category by category
  │               (no LLM call — deterministic, courtesy-rate-limited)
  ▼
2. DIVERGE     — one isolated LLM read per paper, in parallel
  │               (each sees ONE abstract, never the others)
  ▼
3. SCORE       — relevance / practicality / rigor, per paper
   + CLUSTER   — group by underlying architectural angle
  │
  ▼
4. CONVERGE    — pick ONE cluster as the recommended path, synthesize,
                 cite, name the first step, name the risk, list pitfalls
                 pulled from EVERY paper's limitation — not just the winner's
```

Convergence is the deliberate departure from open-ended research tools:
NeuroArxiv doesn't hand back "here are 4 papers, you decide." It commits
to one recommendation, states why the runner-ups lost, and names what to
watch for even in the paths not taken.

Every claim traces to a fetched abstract — papers, ids, and links are real
arXiv metadata, never invented.

## Docs / SKILL.md (skill source)

The SKILL.md describes a four-phase process:

**Pre-flight gate:** Explicit invocation check (/neuroarxiv or "check arXiv");
self-judge (technical mechanism? real effort committed? approach still open?).
Abort if any fails.

**Phase 0 — Categorize:** Map problem onto 3-5 arXiv subject categories
(cs.AI, cs.LG, cs.CL, cs.DC, cs.DB, etc.) and 3-6 concrete search terms.

**Phase 1 — Fetch:** Real HTTP against export.arxiv.org API, category by
category. Never concurrently (arXiv courtesy rate limiting). Retry with
broad query if < 2 results per category.

**Phase 2 — Diverge:** Parallel Agent call per paper, each seeing only
ONE abstract in isolation. Extracts approach, borrow (concrete imperative
takeaway), limitation, relevanceNote as JSON. Critical invariant: calls
must be isolated so no paper anchors the reading of another.

**Phase 3 — Converge:** Score each reading 0-10 on relevance, practicality,
rigor. Flag "traps" (limitations that imply failure modes). Cluster by
architectural angle. Pick ONE cluster as recommended path. Output: TL;DR,
recommended approach, first concrete step, why runner-ups lost, ALL
prior-art pitfalls from every paper (not just the winner).

Anti-patterns enforced: no invented arXiv IDs, no summarizing from memory,
no mixing isolation reads, no open-ended "here are papers" output.

## Top-level structure

```
├── .claude-plugin/           # Claude plugin manifest
├── .github/                  # CI workflow (validate.yml)
├── Assets/                   # Banner image
├── EVALS.md                  # Evaluation methodology and results
├── LICENSE                   # MIT
├── README.md
├── bench/                    # Raw eval transcripts
│   └── deep-tech-eval-transcripts.md
├── package.json              # Node.js build tooling
├── skills/
│   └── neuroarxiv/
│       └── SKILL.md          # Portable skill runtime specification
├── src/
│   ├── categories.ts         # Curated arXiv category taxonomy
│   └── ...                   # CLI installer logic
├── tests/                    # Test suite
└── tsconfig.json
```

Key: this is a TypeScript project with a Node.js CLI installer. The
portable runtime is `skills/neuroarxiv/SKILL.md`; all TS/JS is for the
npm-based installer that copies the skill folder to `~/.claude/skills/`.

## Fetch log
- Mode: standard
- Date: 2026-08-12
- Sections: Metadata, README, SKILL.md (excerpt), EVALS.md (excerpt), top-level structure
