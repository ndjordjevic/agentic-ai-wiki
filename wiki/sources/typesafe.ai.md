---
type: source
category: "Model infra, ML & providers"
source_url: https://typesafe.ai/
tags:
  - system-one-models
  - typed-decisions
  - calibrated-confidence
  - rlcd
  - smart-if-statements
  - structured-classification-api
  - jev-model
related:
  - tamaratran-fast-jev-compaction
  - dzhng-jevgrep
  - reticlehq-reticle
product: typesafe
detail_level: standard
created: 2026-10-15
updated: 2026-10-27
---

TypeSafe AI is a San Francisco model lab founded by Diogo Almeida, who previously worked at OpenAI on the instruction-following research behind ChatGPT. After two years in stealth it launched a new class of models it calls **System One Models**, which are built to be called by software rather than chatted with. Its first public model, **Jev** (early access since September 15, 2026), does not generate text. Each call takes a *state* (text or JSON) plus a set of typed *questions* (Choice, Score, Noul, and the experimental Box). Jev evaluates every question in parallel and returns typed answers with calibrated probabilities and, for some types, a confidence value. It is trained with a method TypeSafe calls Reinforcement Learning for Calibrated Decisions (RLCD) and uses a parallel sampler instead of token-by-token generation. TypeSafe claims 70–500 ms responses, $42 per billion input tokens with free output, and no type errors or hallucinated outputs, because the answer schema is fixed in advance. For this wiki, Jev is a cheap, fast decision primitive ("smart if-statements") for routing, scoring, guardrails, and relevance checks inside agents and pipelines. It does not replace the LLM that drives an agent. Two sources already in the wiki use it: [[tamaratran-fast-jev-compaction]] and [[dzhng-jevgrep]].

_All claims below are sourced from ../../raw/web/typesafe.ai.md unless otherwise noted._

## What it does

- **Typed decisions instead of strings.** Jev is described as "a frontier-intelligence function call: unstructured state in, typed probabilistic decisions out." You define the possible answers up front, so the output always matches the schema and needs no parsing or validation.
- **Calibrated probabilities and confidence.** Every Choice and Score answer includes a probability per option or level plus a `confidence` value derived from those probabilities. Noul answers are a single probability. Code can then act automatically when confidence is high and escalate to a human or a reasoning LLM when it is low.
- **Many questions per call.** Any mix of question types goes into one request. Each question is evaluated independently against the same state, so adding questions barely changes latency and doesn't cause context rot. The *Parallel questions* cookbook reports that batching 13 questions into one call was 12.2x cheaper and 10.0x faster than separate calls, with the same answers.
- **Enterprise offering.** SOC 2 Type II, zero data retention for enterprise customers, no training on customer inputs or outputs, and higher rate limits on request. TypeSafe cites case studies with 88% lower candidate-screening cost (Jack & Jill) and 98.7% lower classification cost.

## Key features

- **Primitives (question types):**
  - **Choice** picks one option from a labeled set and returns `choice`, `probabilities`, and `confidence`.
  - **Score** rates the state against ordered, descriptive levels and returns a probability-weighted `score`, `probabilities`, `confidence`, and a `legend`.
  - **Noul** asks whether a statement is true and returns `noul`, a probability between 0 and 1.
  - **Box** (experimental, `jev-1.14.0` only) returns one bounding box in an image, given as edge fractions.
  - Instructions, options, levels, and criteria all accept JSON structure.
- **Pricing and speed.** Input costs $0.042 per million tokens ($42 per billion), and output tokens are free. The launch post compares this with LLMs at $0.20–$10 per million input tokens and response times of 3–329 seconds. The home page claims 193.6x faster and 444.6x cheaper on TypeSafe's own workflow evals, and also "238x lower input price than Claude Fable 5.1". TypeSafe itself says the workflow-eval numbers are "on the higher end of real world gains".
- **"Danger zone" header flags** (added in Jev 1.14, October 14, 2026) turn on features TypeSafe doesn't yet consider production-ready:
  - `TypeSafe-Danger-Zone-Images: true` enables composable images through an `assets` find-and-replace, usable in the state, instructions, or criteria.
  - `TypeSafe-Danger-Zone-Long-Context: true` raises both context limits from 64k per request and 32k per question to 262k tokens.
- **Model aliases and versions.** `jev-latest` points to the stable release (`jev-1.13.0`, moving to 1.14 a week after its release). `jev-preview` points to the newest build (`jev-1.14.0`). TypeSafe promises 60 days' notice before deprecating 1.13 and 30 days for 1.14. Each response's `model` field reports the exact version that answered, so you can pin a version for tuned thresholds.
- **Agent skill for coding agents.** Install it with `claude plugin marketplace add typesafe-ai/skills` and `claude plugin install typesafe@typesafe-ai`, or with `npx skills add typesafe-ai/skills --skill typesafe-ai` for other agents. It gives Claude Code, Codex, and similar agents the API, primitives, and patterns so they can write correct Jev integrations.
- **Playground and console.** `console.typesafe.ai` provides API keys, per-organization rate limits, and a browser playground.

## Architecture and concepts

**System One vs. LLMs.** The name comes from Kahneman's *Thinking, Fast and Slow*, where System 1 is fast, intuitive judgment. Jev is named after William Stanley Jevons and the Jevons paradox: TypeSafe expects each drop in the cost of intelligence to unlock far more uses. TypeSafe contrasts its training objective with the usual ones. RLHF optimizes for human preference, and RLVR optimizes for programmatically verifiable outputs. RLCD instead optimizes for calibrated decisions, meaning probabilities that are honest about uncertainty. The model has a new architecture and a parallel, hardware-aware sampler that produces every output in a single pass. It gives up string generation entirely and cannot write replies, code, or explanations. Calibration holds across groups of predictions and does not guarantee that any single answer is right.

**Atomic questions, composed in code.** The core design rule is that each question should be a "gut-check" judgment an expert could make in a few seconds. Larger judgments get split into atomic questions whose answers your code combines with its own weights. For example, a startup pitch would be scored separately on market size, feasibility, and differentiation, and the weights live in code. The documented patterns are:
- **Speculative fan-out:** ask many questions, including speculative ones, and let code decide which answers matter.
- **Confidence-gated routing:** the answer says what to do, and confidence says whether to act on it.
- **Composite scoring:** combine several atomic scores into one.
- **Intent routing:** send each request to deterministic logic, a specialist LLM, or a human.

**Confidence.** Confidence is computed from the probability distribution. For a Choice it depends on the probability of the top option. For a Score it also accounts for distance between levels, so probability spread across two adjacent levels lowers confidence less than probability split between opposite ends. Noul has no separate confidence because a value near 0.5 already means "unsure." The docs recommend dividing confidence into three ranges with different system behavior, and setting stricter thresholds for actions with worse consequences.

**Limits and customization.** By default Jev reads text only: strings, JSON objects, and arrays of text. Each request is limited to 64k tokens and each question to 32k. English is the primary language, and other languages, CJK included, work less well. Every account uses the same weights, with no fine-tuning or LoRA. You adapt Jev to your domain through the state, the instructions and criteria, and how you decompose questions, or by training a downstream classical model on Jev's probabilities, as the AutoResearch cookbook does with CatBoost. A Choice supports up to 255 options; larger sets use a two-stage process that scores options first and then chooses. A published "jaggedness" page lists the known weak spots in 1.13.

## Main APIs

- **HTTP:** `POST https://api.typesafe.ai/v1/systemone` with `Authorization: Bearer <API_KEY>` and a JSON body containing `state`, `model` (for example `jev-latest`), and `questions`. `questions` maps your own IDs to `{type: choice|score|noul, instructions, criteria}`. The response contains `model`, `answers` keyed by your question IDs, and `usage` (`input_tokens`, `output_tokens`). `GET /v1/models` lists the available aliases. Rate limits are measured in tokens per second and requests per second, and exceeding them returns `429` with `retry-after`.
- **Python SDK** (`typesafe-sdk`, Python 3.10+): `TypeSafeClient` and `AsyncTypeSafeClient` with `.system_one(state=..., questions={...})`, question classes `Choice`, `Score`, and `Noul`, and typed accessors `response.choices[...]`, `.scores[...]`, and `.nouls[...]`. It retries automatically using `RetryPolicy`.
- **JavaScript/TypeScript SDK** (`@typesafe-ai/sdk`, Node 20+): `new TypeSafeClient({ defaultModel })` with `client.systemOne({ state, questions })` and helper functions `choice()`, `score()`, `noul()`, `box()`, and `image()`. The TypeScript types infer answer unions from your questions, so a Choice over billing, technical, and sales options is typed as `"billing" | "technical" | "sales"`.

## When to use

- Use Jev when code needs a fast, cheap, structured judgment on natural-language input, such as ticket routing, moderation and guardrail screening of LLM inputs and outputs, re-ranking or filtering RAG passages, citation checking, entity matching, hierarchical classification, picking a skill or tool, or deciding what to keep in memory or context. The docs include cookbooks for each of these, including skill suggestion over Nous Research's Hermes catalog, LLM guardrails, and an SDE (structured data extraction) cascade.
- Use it as a cheaper first stage in front of an expensive reasoning LLM, escalating only the cases where confidence is low. Several cookbooks show this mini-model, then verification, then reasoning-model cascade.
- Use it for real-time or high-volume work where LLM latency or per-call cost is too high: map-reduce over large datasets, interactive UX, or game bots like the Doom demo, which costs about $7 per hour at 10 queries per second.
- **Not** a model for powering a coding agent. The docs say plainly that Jev cannot be dropped in behind Claude Code, Cursor, Copilot, and similar tools, because it doesn't stream text, call tools, or edit files.
- Things to weigh: the service is in early access and served from the US West Coast. TypeSafe acknowledges it cannot yet prove its pricing isn't subsidized. Images, Box, and long context are explicitly not production-ready, and the benchmark claims come from TypeSafe's own evaluations.

## Ecosystem

- **Built on Jev in this wiki:** [[tamaratran-fast-jev-compaction]] uses Jev to decide which tool calls and results to prune during Claude Code context compaction. [[dzhng-jevgrep]] uses Jev to judge relevance during hierarchical semantic code search for coding agents.
- **Agent skill:** `github.com/typesafe-ai/skills` provides a Claude Code plugin and a [[skills.sh]] install that follows the agentskills.io conventions.
- **Docs:** Mintlify docs at `docs.typesafe.ai` with an `llms.txt` index. They cover concepts, primitives, patterns, about 25 cookbooks, demos, the API reference, and SDK references.
- **Company:** the manifesto, "Composable AI: Build Prod, Not God," argues that the bottleneck for AI is composability rather than raw intelligence. TypeSafe compares today's AI to "databases before SQL" and wants intelligence to be a dependable primitive that can be layered into software. The blog (per the sitemap) also includes posts such as "antibenchmaxxing" and "bitterest-lesson", in line with TypeSafe's stated dislike of public benchmarks.
