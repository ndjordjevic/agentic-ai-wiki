# how-to-master-dynamic-workflows-claude-code-6-patterns-14-steps

## Fetch log
- Inbox URL: https://x.com/0xCodez/status/2062127385923776831?s=20
- Final URL: https://x.com/i/article/2062116827220639744
- Fetched: 2026-07-08
- Pages: 1
- Mode: single-page
- Note: X article page requires login for direct fetch. Status page metadata captured via WebFetch and Jina Reader. Full article body captured from English mirror at https://glean.smartcoder.ai/en/a/how-to-master-dynamic-workflows-in-claude-code-6-patterns-an-vv9cep (faithful republish of the 0xCodez X Article, June 3 2026). No llms.txt, docs discovery, or companion fetch (single-page X article).

## Page — https://x.com/i/article/2062116827220639744

Title: How to master Dynamic Workflows in Claude Code: 6 patterns and 14 steps Anthropic engineers actually
Author: Codez (@0xCodez)
Published: 2026-06-03
Article ID: 2062116827220639744
Status URL: https://x.com/0xCodez/status/2062127385923776831

---

Most Claude Code users still write their workflows by hand. They chain prompts, copy outputs, paste them into the next prompt, fix what went wrong, repeat.

9 out of 10 builders haven't tried Dynamic Workflows even once, even though they shipped two weeks ago.

They write 50 prompts when one workflow would do. This is the 14-step roadmap and the 6 patterns Anthropic's own engineers actually use — for migrations, research, sorting, root-cause, triage, and evals.

## § 2 — What shipped

Dynamic Workflows shipped in Claude Code on May 28, 2026. The default Claude Code harness is built for coding — and that works well for most coding tasks. But there are classes of work where one context window starts to break down: long-running, massively parallel, highly structured, or adversarial.

For those, Anthropic used to build custom harnesses themselves (Research, Code Review, agent teams). With Dynamic Workflows, Claude writes that harness for you on the fly, custom-built for your task, in JavaScript.

## § 3 — Mental model

The default Claude Code harness has Claude plan and execute in the same context window. For most coding work, this is great. For long-running, parallel, or adversarial work, it breaks down.

A Dynamic Workflow is Claude writing its own custom harness for the task — a JavaScript file with a few special functions that spawn and coordinate subagents, plus standard JavaScript (Math, JSON, Array) to process the data flowing between them.

Three things this gives you that the default harness cannot:

- **Per-agent isolation.** Each subagent gets its own context window with one focused goal. No cross-contamination.
- **Per-agent model choice.** The workflow picks which model each subagent uses — Opus for hard reasoning, Haiku for cheap exploration, Sonnet for the middle.
- **Per-agent isolation level.** Worktree (isolated git checkout) or remote (no checkout). The workflow decides what each agent needs.

Start one by either asking Claude directly ("make a workflow that…") or with the trigger word `ultracode`. If a workflow is interrupted — user action, terminal quit — resuming the session picks up where it left off.

## § 4 — What workflows fix

To know when a workflow is the right tool, you have to know what it fixes. The longer Claude works on a complex task in a single context window, the more it becomes susceptible to three specific failure modes — named directly in the Anthropic launch writing:

- **Agentic laziness** — Claude stops before finishing a complex, multi-part task and declares done after partial progress. Addresses 20 of the 50 items in a security review and calls the rest "handled."
- **Self-preferential bias** — Claude prefers its own results when asked to verify or judge them against a rubric. A verifier with skin in the game can't be a fair verifier.
- **Goal drift** — the gradual loss of fidelity to the original objective across many turns, especially after compaction. Each summarization step is lossy. "Don't do X" constraints quietly disappear at turn 47.

A workflow solves all three structurally: separate Claudes with their own contexts, focused goals, and isolated state. If your task suffers from any of these patterns — that's the signal to reach for a workflow.

## § 5 — Static vs dynamic workflows

You may have already built static workflows using the Claude Agent SDK or `claude -p` — coordinating multiple Claude Code instances together.

- **Static workflows** are generic: written once to handle every edge case. They work, but they have to be conservative.
- **Dynamic Workflows** are different: Claude writes this workflow for this task. The harness is tailor-made.

The reason the dynamic version wins isn't the search step — both can search. It's that the workflow gets to shape itself around your context: read your billing code, check each feature against the actual new provider docs, price at your transaction volume, and run an adversarial "why not to migrate" pass against its own emerging answer. A static harness can't do this because it doesn't know your code exists.

## § 6 — Core primitives

Three functions do most of the work in a workflow. Knowing them is enough to read any workflow Claude writes for you and to nudge Claude when you want a specific shape.

- `agent(prompt, opts?)` — spawns a single subagent. Add a `schema` option when you need structured JSON output you'll parse downstream.
- `parallel(thunks)` — fans out concurrent tasks and waits for all of them before continuing. This is a synchronization barrier.
- `pipeline(items, …stages)` — streams items through stages without waiting. Item A can be in stage three while item B is still in stage one.

`parallel()` is a barrier: it fans out, then waits for everything before returning. `pipeline()` is streaming: each item flows through every stage independently.

Pick by the question: do I need all results before I can do anything next? Yes → `parallel`. No → `pipeline` (cheaper, faster overall).

## § 7 — Pattern 1: Classify-and-act

A classifier agent decides on the type of task, then the workflow routes to different agents or behaviors based on the answer. Or a classifier runs at the end, sorting raw outputs into buckets for whatever comes next.

When this pattern earns its keep:

- The task is heterogeneous — different sub-types need different treatment.
- You want to spend the expensive model only where complexity demands it (classifier on cheap, then route to Opus only when needed).
- The decomposition of work is itself non-trivial and benefits from a model deciding the shape.

Example: "Explain how the auth module works." A classifier subagent reads the codebase first, estimates complexity, then routes the actual explanation task to Sonnet for a 10-file module or Opus for a 100-file one.

## § 8 — Pattern 2: Fan-out-and-synthesize

Split a task into many smaller steps. Run an agent on each step in parallel. Synthesize the results into one answer.

The synthesize step is a barrier — it waits for every fan-out agent, then merges their structured outputs.

Why this pattern dominates in practice: it solves the "too many things at once" failure of single-context work. Each subagent sees only its piece. The orchestrator never gets distracted by 50 unrelated details.

Use this when:

- You have a clearly enumerable list of work items (50 files, 200 endpoints, 100 reviews).
- Each item is independent — no item needs another's output to begin.
- You want a single consolidated answer at the end, not a pile of partial reports.

```javascript
// Fan out: one agent per file. Barrier: wait for all.
const reviews = await parallel(
  files.map(file => () => agent(
    `Review ${file} for security issues`,
    { model: "haiku", schema: IssueList }
  ))
)

// Synthesize: one Opus agent merges everything.
const report = await agent(
  `Merge these reviews into one prioritized report:\n${JSON.stringify(reviews)}`,
  { model: "opus" }
)
```

## § 9 — Pattern 3: Adversarial verification

This is the structural fix for self-preferential bias. For each spawned agent, run a separate spawned agent that adversarially verifies its output against a rubric. The verifier has never seen the original work; it can't favor it.

The pattern matters most for:

- **Claim-checking** — every factual statement in a report gets its own verifier subagent, checking against the original source.
- **Code review** — the author agent writes the fix, the reviewer agent (separate context) reviews it. Never the same Claude judging itself.
- **Quality gates** — before any artifact ships, an adversary tries to find the weakest case against it.

The pairing rule: the verifier should know only the rubric and the artifact, not who produced it.

## § 10 — Pattern 4: Generate-and-filter

Generate a number of ideas on a topic, then filter them by a rubric or by verification. Dedupe duplicates. Return only the highest quality, tested ideas.

Where this pattern shines:

- Brainstorming — 30 product names, then a verifier kills clichés, trademark conflicts, and weak phonetics.
- Hypothesis generation — 5 different approaches to a problem, then each gets scored against your constraints.
- Solution design — same shape as hypothesis generation.

The opposite of asking Claude for "the best answer." Generate-and-filter makes Claude commit late, after every option has been challenged.

## § 11 — Pattern 5: Tournament

Instead of dividing the work, have agents compete on it. Spawn N agents that each attempt the same task using different approaches, then judge the results in pairwise fashion until one wins.

Comparative judgment is more reliable than absolute scoring — especially for taste-based work.

Why this beats sort-by-score: trying to sort 1,000 items in one prompt fails on two fronts — quality degrades, and it won't fit in context. A tournament splits the bracket across fresh agents, each comparing just two items. The bracket itself lives in deterministic loop code, not in context.

## § 12 — Pattern 6: Loop until done

For tasks with an unknown amount of work, loop spawning agents until a stop condition is met — no new findings, no more errors in the logs, theory verified — instead of running a fixed number of passes.

This pattern is the answer to "keep going until it's actually done":

- Flaky test debugging — reproduce, form theories, test them, until one theory holds.
- Bug hunting — keep finding bugs until a full pass returns zero.
- Mining for patterns — cluster, identify rules, until no new clusters appear.

Pair this pattern with `/goal` to set a hard completion requirement and with `/loop` if you want the entire workflow itself to run on a recurring schedule.

## § 13 — Composing patterns (use-case matrix)

The 6 patterns rarely appear alone. A real workflow composes 2–4 of them:

| Use case | Typical pattern composition |
|---|---|
| Migrations and refactors | Fan-out → adversarial verification → loop until done |
| Deep research (`/deep-research`) | Fan-out → adversarial verification → synthesize |
| Deep verification of a draft | Identify claims → fan-out verifiers → meta-verifier |
| Sorting 1,000+ items | Tournament (pairwise comparison, never absolute scoring) |
| Memory and rule adherence | Fan-out verifiers per rule → skeptic reviews rules |
| Root-cause investigation | Generate theories → panel of verifiers/refuters → loop until one survives |
| Triage at scale | Classify-and-act → dedupe → fix or escalate; pair with `/loop` |
| Exploration and taste | Generate-and-filter → tournament with rubric |
| Lightweight evals | Run candidate in worktree → comparison agents grade → refine and re-grade |

The right way to internalize these: identify which failure mode your current task is failing under, then pick the pattern that structurally prevents it.

- Drift → fan-out
- Self-preference → adversarial verification
- Open-ended → loop until done
- Hard-to-score → tournament

## § 14 — Cost controls

Workflows can be expensive. Three controls turn them from "cool but costly" into "a tool I run unattended":

- **`/goal`** sets a hard completion requirement. Pair it with the loop pattern: "don't stop until one theory works." Without `/goal`, a workflow stops at a soft completion point.
- **`/loop`** runs the entire workflow on a recurring schedule. Use it for workflows you want running continuously — triage, weekly research updates, recurring verification.
- **Explicit token budgets.** Tell Claude in the prompt: "use 10k tokens." Without a cap, an ambitious workflow can balloon to 5–10× the tokens you expected.

Example prompt:

```
> ultracode quick adversarial review of this assumption:
  "moving to Postgres eliminates our shard rebalancing."
  Use 5k tokens. /goal don't stop until you have either
  a counterexample or three independent confirmations.
```

Quoting the Claude Code team: "Best practices are still developing. Dynamic workflows often use more tokens, so think carefully about when and how to use them." Most traditional coding tasks do not need a panel of 5 reviewers.

Ask yourself: does this task really need more compute? If a regular Claude Code session would finish it in five minutes, you don't need a workflow.

## § 15 — Quarantine pattern (untrusted inputs)

Any workflow that reads untrusted public content — support tickets, bug reports, user feedback, scraped data — needs to assume that content might contain prompt injection.

The fix: **quarantine**. Bar the agents that read the untrusted content from taking any high-privilege actions. Separate agents, with no exposure to the raw content, do the acting.

If the input wasn't written by you or a trusted teammate, quarantine it. A 30-line read-only reader agent costs almost nothing and removes an entire class of prompt injection risk.

## § 16 — Saving and shipping workflows

Once a workflow works, save it: press `s` in the workflow menu. Saved workflows go to `~/.claude/workflows`. From there:

- **Keep it local** — reuse it across your own projects.
- **Ship it as a Skill** — bundle the JavaScript file inside a Skill folder, reference it in `SKILL.md`, and anyone who installs the Skill runs the same workflow.

When packaging a workflow into a Skill, prompt Claude to treat the workflow as a template, not a script to run verbatim — leaving room to adapt the shape to the specific task while keeping the overall structure intact.

## § 17 — Common mistakes

- Reaching for a workflow when a regular Claude Code session would do.
- No token budget — ambitious workflows balloon to 5–10× what you expected.
- One agent doing both the work and the verification (self-preferential bias).
- Treating `parallel()` and `pipeline()` as interchangeable.
- Skipping `/goal` on loop patterns — workflow stops early at first soft completion.
- Letting untrusted content reach the actor without quarantine.
- Sorting with absolute scores instead of tournament-style comparative judgment.
- Never saving working workflows — re-prompting the same shape every week.

## Activation methods

- Ask for a workflow in your prompt, or include the keyword `ultracode`.
- Set `/effort ultracode` and Claude plans a workflow for every substantive task in the session.
- Run `/deep-research` to experience dynamic workflows before touching your codebase.
- Monitor runs via `/workflows` dashboard.
- Requirements: Claude Code CLI v2.1.154+, paid plan (Pro/Max/Team/Enterprise); Pro users enable dynamic workflows from `/config`.
