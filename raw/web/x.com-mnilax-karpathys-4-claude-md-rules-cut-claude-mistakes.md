# x.com-mnilax-karpathys-4-claude-md-rules-cut-claude

## Fetch log
- Inbox URL: https://x.com/mnilax/status/2053116311132155938?s=43&t=5l2OHSF10JbahgpENs1smw
- Final URL: https://x.com/mnilax/status/2053116311132155938?s=43&t=5l2OHSF10JbahgpENs1smw
- Fetched: 2026-05-11
- Pages: 1
- Mode: standard
- Note: x.com/llms.txt returned HTML (not a plain-text catalog — treated as absent). Page fetched via Jina Reader (r.jina.ai) fallback; direct WebFetch returned blocked response. No docs discovery relevant for a specific status/post URL.

## Landing page — https://x.com/mnilax/status/2053116311132155938

Title: Mnimiy on X: "Karpathy's 4 CLAUDE.md rules cut Claude mistakes from 41% to 11%. After 30 codebases, I added 8 more" / X

URL Source: https://x.com/mnilax/status/2053116311132155938?s=43&t=5l2OHSF10JbahgpENs1smw

In late January 2026, Andrej Karpathy posted a thread complaining about how Claude writes code. Three failure modes: silent wrong assumptions, over-complication, orthogonal damage to code it shouldn't have touched.

Forrest Chang read the thread, packaged the complaints into 4 behavioral rules in a single CLAUDE.md file, and dropped it on GitHub. It hit 5,828 stars in the first day. 60,000 bookmarks in two weeks. 120,000 stars today. The fastest-growing single-file repo of 2026.

Then I tested it on 30 codebases over 6 weeks.

The 4 rules work. Mistakes that used to happen ~40% of the time dropped to under 3% on tasks that played to their strengths. But the template was built to fix code-writing mistakes from January.

The Claude Code ecosystem in May 2026 has different problems — agent fights, hook cascades, skill loading conflicts, multi-step workflows that break across sessions.

So I added 8 more rules. Below: the full 12-rule CLAUDE.md, why each one earned its place, and the 4 places where the original Karpathy template silently breaks.

If you want to skip the explanations and just paste, the full file is at the end.

Claude Code's CLAUDE.md is the most under-leveraged file in the entire AI coding stack. Most developers either:

- Treat it as a dump for every preference they've ever had, bloated to 4,000+ tokens, compliance drops to 30%
- Skip it entirely and prompt every time — 5x token waste, no consistency between sessions
- Copy a template once and forget. Works for two weeks, then breaks silently as their codebase shifts

The official Anthropic docs are explicit: CLAUDE.md is advisory. Claude follows it about 80% of the time. Past 200 lines, compliance drops sharply because important rules get buried in the noise.

Karpathy's template solved this in one file, 65 lines, 4 rules. That's the floor.

The ceiling is higher. With 8 more rules, the ones I'll go through below, you cover not just the January 2026 code-writing problems Karpathy complained about, but the May 2026 agent-orchestration problems that didn't exist yet when the template was written.

If you haven't read Forrest Chang's repo, the floor:

Rule 1 — Think Before Coding. No silent assumptions. State what you're assuming. Surface tradeoffs. Ask before guessing. Push back when a simpler approach exists.

Rule 2 — Simplicity First. Minimum code that solves the problem. No speculative features. No abstractions for single-use code. If a senior engineer would call it overcomplicated — simplify.

Rule 3 — Surgical Changes. Touch only what you must. Don't "improve" adjacent code, comments, or formatting. Don't refactor what isn't broken. Match existing style.

Rule 4 — Goal-Driven Execution. Define success criteria. Loop until verified. Don't tell Claude what steps to follow, tell it what success looks like and let it iterate.

These four close ~40% of the failure modes I see in unsupervised Claude Code sessions. The remaining ~60% live in the gaps below.

Each of these came from a real moment where Karpathy's 4 weren't enough. I'll show the moment, then the rule.

Karpathy's rules are silent on this. The model decides things that should be deterministic code, whether to retry an API call, how to route a message, when to escalate. Different decisions every week. Flaky if-else at $0.003 per token.

```
## Rule 5 — Use the model only for judgment calls
Use Claude for: classification, drafting, summarization, extraction from unstructured text.
Do NOT use Claude for: routing, retries, status-code handling, deterministic transforms.
If a status code already answers the question, plain code answers the question.
```

The moment: Code that called Claude to "decide if we should retry on 503" worked beautifully for two weeks, then started flaking because the model started reading the request body as context for the decision. The retry policy was random because the prompt was random.

CLAUDE.md without budgets is a blank check. Every loop has a chance to spiral into a 50,000-token context dump. The model won't stop on its own.

```
## Rule 6 — Token budgets are not advisory
Per-task budget: 4,000 tokens.
Per-session budget: 30,000 tokens.
If a task is approaching budget, summarize and start fresh. Do not push through.
Surfacing the breach > silently overrunning.
```

The moment: A debugging session ran for 90 minutes. The model was perfectly happy iterating on the same 8KB error message, gradually losing track of which fix it had already tried. By the end, it was suggesting fixes I'd rejected 40 messages earlier. Token budget would have killed it at minute 12.

When two parts of the codebase disagree, Claude tries to please both. The result is incoherent.

```
## Rule 7 — Surface conflicts, don't average them
If two existing patterns in the codebase contradict, don't blend them.
Pick one (the more recent / more tested), explain why, and flag the other for cleanup.
"Average" code that satisfies both rules is the worst code.
```

The moment: A codebase had two error-handling patterns — one async/await with explicit try/catch, one with a global error boundary. Claude wrote new code that did both. Doubled error handlers. Took me 30 minutes to figure out why errors were swallowed twice.

Karpathy's "Surgical Changes" tells Claude not to touch adjacent code. It doesn't tell Claude to understand adjacent code first. Without this, Claude writes new code that conflicts with existing code 30 lines away.

```
## Rule 8 — Read before you write
Before adding code in a file, read the file's exports, the immediate caller, and any obvious shared utilities.
If you don't understand why existing code is structured the way it is, ask before adding to it.
"Looks orthogonal to me" is the most dangerous phrase in this codebase.
```

The moment: Claude added a function next to an existing identical function it hadn't read. Both functions did the same thing. The new one took precedence because of import order. The old one had been the source of truth for 6 months.

Karpathy's Goal-Driven Execution implies tests as success criteria. In practice, Claude treats "tests pass" as the only goal, and writes code that passes shallow tests while breaking everything else.

```
## Rule 9 — Tests verify intent, not just behavior
Every test must encode WHY the behavior matters, not just WHAT it does.
A test like `expect(getUserName()).toBe('John')` is worthless if the function takes a hardcoded ID.
If you can't write a test that would fail when business logic changes, the function is wrong.
```

The moment: Claude wrote 12 tests for an auth function. All passed. Auth was broken in production. The tests were testing the function returned something, not whether it returned the right thing. The function passed because it was returning a constant.

Karpathy's template assumes one-shot interactions. Real Claude Code work is multi-step — refactoring across 20 files, building features over a session, debugging across multiple commits. Without checkpoints, one wrong turn loses all progress.

```
## Rule 10 — Checkpoint after every significant step
After completing each step in a multi-step task: summarize what was done, what's verified, what's left.
Don't continue from a state you can't describe back to me.
If you lose track, stop and restate.
```

The moment: A 6-step refactor went wrong on step 4. By the time I noticed, Claude had also done step 5 and 6 on top of the broken state. Untangling took longer than redoing the whole thing. Checkpoints would have caught it at step 4.

In a codebase with established patterns, Claude likes to introduce its own. Even when its way is "better," the introduction of two patterns is worse than either pattern alone.

```
## Rule 11 — Match the codebase's conventions, even if you disagree
If the codebase uses snake_case and you'd prefer camelCase: snake_case.
If the codebase uses class-based components and you'd prefer hooks: class-based.
Disagreement is a separate conversation. Inside the codebase, conformance > taste.
If you genuinely think the convention is harmful, surface it. Don't fork it silently.
```

The moment: Claude introduced React hooks into a class-component codebase. They worked. They also broke the codebase's testing patterns, which assumed componentDidMount. Half a day to remove and rewrite.

The most expensive Claude failures are the ones that look like success. A function "works" but returns wrong data. A migration "completes" but skipped 30 records. A test "passes" but only because the assertion was wrong.

```
## Rule 12 — Fail loud
If you can't be sure something worked, say so explicitly.
"Migration completed" is wrong if 30 records were skipped silently.
"Tests pass" is wrong if you skipped any.
"Feature works" is wrong if you didn't verify the edge case I asked about.
Default to surfacing uncertainty, not hiding it.
```

The moment: Claude said a database migration "completed successfully." It had silently skipped 14% of records that hit a constraint violation. The skip was logged but not surfaced. Discovered the problem 11 days later when reports started looking wrong.

I tracked the same set of 50 representative tasks across 30 codebases for 6 weeks. Three configurations:

Mistake rate = task required correction or rewrite to match intent. Counts: silent wrong assumption, over-engineering, orthogonal damage, silent failure, convention violation, conflict averaging, missed checkpoint.

Compliance = how often Claude visibly applied the relevant rule when it was applicable.

The interesting result isn't the headline drop from 41% to 3%. It's that going from 4 rules to 12 added almost no compliance overhead (78% -> 76%) but cut the mistake rate by another 8 points. The new rules cover failure modes the original 4 didn't address — they don't compete for the same attention budget.

Four places where the original 4-rule template is not enough, even before adding new rules:

1. Long-running agent tasks. Karpathy's rules target the moment Claude is writing code. They're silent on what happens when Claude is running a multi-step pipeline. No budget rule. No checkpoint rule. No "fail loud" rule. Pipelines drift.

2. Multi-codebase consistency. "Match existing style" assumes one style. In a monorepo with 12 services, Claude has to pick which style. The original rules don't tell it how. It picks randomly or averages.

3. Test quality. Goal-Driven Execution treats "tests pass" as success. Doesn't say tests have to be meaningful. The result is tests that test nothing useful but make Claude confident.

4. Production vs prototype. The same 4 rules that protect production code from over-engineering also slow down prototypes that legitimately need 100 lines of speculative scaffolding to figure out a direction. Karpathy's "Simplicity First" overfires on early-stage code.

The 8 added rules don't replace Karpathy's 4. They patch the gaps where his model, January 2026, autocomplete-style coding, doesn't match May 2026's agent-driven, multi-step, multi-codebase work.

Things I tried before settling on the 12 rules:

- Adding rules I'd seen on Reddit / X. Most were either restatements of Karpathy's 4 with different words, or domain-specific rules ("always use Tailwind classes") that don't generalize. Cut them.
- More than 12 rules. I tested up to 18. Compliance dropped from 76% to 52% past 14 rules. The 200-line ceiling is real. Past it, Claude starts pattern-matching to "rules exist" without actually reading them.
- Rules that depend on tooling that might not exist. "Always use eslint" breaks when eslint isn't installed. Rule fails silently. Replaced with capability-agnostic phrasings: "match the codebase's enforced style" instead of "use eslint."
- Examples in CLAUDE.md instead of rules. Examples are heavier than rules. Three examples cost as much context as ~10 rules and Claude over-fits to them. Rules are abstract, examples are specific. Use rules.
- "Be careful" / "think hard" / "really focus." Pure noise. Compliance with these dropped to ~30% because they're not testable. Replaced with concrete imperatives ("state assumptions explicitly").
- Telling Claude to be "senior." Doesn't work. Claude already thinks it's senior. The compliance gap is between thinking and doing. Imperative rules close the gap; identity prompts don't.

```
# CLAUDE.md — 12-rule template

These rules apply to every task in this project unless explicitly overridden.
Bias: caution over speed on non-trivial work. Use judgment on trivial tasks.

## Rule 1 — Think Before Coding
State assumptions explicitly. If uncertain, ask rather than guess.
Present multiple interpretations when ambiguity exists.
Push back when a simpler approach exists.
Stop when confused. Name what's unclear.

## Rule 2 — Simplicity First
Minimum code that solves the problem. Nothing speculative.
No features beyond what was asked. No abstractions for single-use code.
Test: would a senior engineer say this is overcomplicated? If yes, simplify.

## Rule 3 — Surgical Changes
Touch only what you must. Clean up only your own mess.
Don't "improve" adjacent code, comments, or formatting.
Don't refactor what isn't broken. Match existing style.

## Rule 4 — Goal-Driven Execution
Define success criteria. Loop until verified.
Don't follow steps. Define success and iterate.
Strong success criteria let you loop independently.

## Rule 5 — Use the model only for judgment calls
Use me for: classification, drafting, summarization, extraction.
Do NOT use me for: routing, retries, deterministic transforms.
If code can answer, code answers.

## Rule 6 — Token budgets are not advisory
Per-task: 4,000 tokens. Per-session: 30,000 tokens.
If approaching budget, summarize and start fresh.
Surface the breach. Do not silently overrun.

## Rule 7 — Surface conflicts, don't average them
If two patterns contradict, pick one (more recent / more tested).
Explain why. Flag the other for cleanup.
Don't blend conflicting patterns.

## Rule 8 — Read before you write
Before adding code, read exports, immediate callers, shared utilities.
"Looks orthogonal" is dangerous. If unsure why code is structured a way, ask.

## Rule 9 — Tests verify intent, not just behavior
Tests must encode WHY behavior matters, not just WHAT it does.
A test that can't fail when business logic changes is wrong.

## Rule 10 — Checkpoint after every significant step
Summarize what was done, what's verified, what's left.
Don't continue from a state you can't describe back.
If you lose track, stop and restate.

## Rule 11 — Match the codebase's conventions, even if you disagree
Conformance > taste inside the codebase.
If you genuinely think a convention is harmful, surface it. Don't fork silently.

## Rule 12 — Fail loud
"Completed" is wrong if anything was skipped silently.
"Tests pass" is wrong if any were skipped.
Default to surfacing uncertainty, not hiding it.
```

Save as CLAUDE.md at your repo root. Add project-specific rules below the 12 (stack, test commands, error patterns). Don't go past 200 lines combined, past that, compliance falls off.

Two steps:

```
# 1. Append Karpathy's 4-rule baseline to your CLAUDE.md
curl https://raw.githubusercontent.com/forrestchang/andrej-karpathy-skills/main/CLAUDE.md >> CLAUDE.md

# 2. Paste rules 5-12 from this article below
```

Save at your repo root. The >> matters, it appends to your existing CLAUDE.md instead of overwriting any project-specific rules you already have.

CLAUDE.md is not a wishlist. It's a behavioral contract that closes specific failure modes you've observed. Every rule should answer: what mistake does this prevent?

Karpathy's 4 prevent the failure modes he saw in January 2026: silent assumptions, over-engineering, orthogonal damage, weak success criteria. They're foundational. Don't skip them.

The 8 I added prevent failure modes that emerged in May 2026: agent loops without budgets, multi-step tasks without checkpoints, tests that don't test, silent successes hiding silent failures. They're additive.

Your mileage will vary. If you don't run multi-step pipelines, Rule 10 doesn't matter. If your codebase has one consistent style enforced by linting, Rule 11 is redundant. Read the 12, keep the ones that map to mistakes you've actually made, drop the rest.

A 6-rule CLAUDE.md tuned to your real failure modes beats a 12-rule one with 6 rules you'll never need.

Karpathy's January 2026 thread was a complaint. Forrest Chang turned it into 4 rules. 120,000 developers starred the result. Most of them are still running 4 rules today.

The model has improved. The ecosystem has changed. Multi-step agents, hook cascades, skill loading, multi-codebase work — none of these existed when Karpathy wrote his thread. The 4 rules don't address them. They're not wrong; they're incomplete.

8 more rules. 6 weeks of testing across 30 codebases. Mistake rate from 41% to 3%.
