---
type: source
category: "Business, career & learning"
source_url: https://planana.xyz
tags:
  - ai-tutor
  - personalized-learning
  - learning-plans
  - study-roadmap
  - goal-based-learning
  - self-paced-learning
related: [agiloop.ai]
  - producthunt.com
product: planana
detail_level: standard
created: 2026-05-13
updated: 2026-08-22
---

Planana AI is a free web application that converts an open-ended learning goal into a structured, personalized weekly study roadmap. The user describes what they want to learn and their current level; Planana's AI tutor generates a practical plan broken into weeks and daily sessions, with matched resources — eliminating the friction of figuring out what to study next.

_All claims below are sourced from ../../raw/web/planana.xyz.md unless otherwise noted._

## What it does

Planana takes a learning goal as free-text input (e.g. "learn Python for data science" or "understand linear algebra") and produces a week-by-week roadmap with clear next steps, study materials matched to the user's level, and a realistic daily pace designed to minimize overwhelm. Users sign in, describe their goal and current level, and the plan is generated immediately.

The `/learn/*` pages (covering Python, JavaScript, Rust, SQL, Algorithms, Statistics, Calculus, Linear Algebra, Computer Science, System Design, Philosophy, Economics, History, Japanese, Latin, and more) act as SEO entry points and illustrate the scope of subjects the tutor supports, showing the syllabus structure Planana generates for each domain.

## Key features

- **Personalized weekly roadmap** — goal broken into named weekly stages so the learner always knows what to study next
- **Matched resources** — study materials selected to fit the learner's stated level and goal, rather than generic recommendations
- **Realistic daily pacing** — short sessions and steady cadence over aggressive schedules, reducing dropout
- **AI plan generation** — no manual curriculum design required; the tutor handles sequencing and resource selection
- **Free to use** — SoftwareApplication offering at price 0 USD (per structured data)
- **Privacy** — account and learning data stored securely with per-user access controls

## Architecture and concepts

Planana is a Next.js web application deployed on Cloudflare Pages, served at `planana.xyz`. The core interaction model is a conversational or form-based goal entry → AI plan generation → structured roadmap display loop. No public API or SDK is exposed; the product is consumer-facing.

The `/learn/<subject>` URLs serve pre-rendered subject pages that demonstrate the typical curriculum Planana would generate for that subject, functioning as both marketing material and learning-entry points.

## When to use

Planana is suited for:
- **Self-directed learners** who have a broad goal (e.g. "learn Rust") but lack a concrete study plan
- **Beginners to experienced learners** who want consistent daily progress rather than ad hoc resource-hunting
- Anyone who has felt overwhelmed by the breadth of what there is to learn in a subject and wants an opinionated, actionable starting point

It is not a course platform or LMS — it generates a plan and points to external resources rather than hosting lessons directly.

## Ecosystem

Planana is a standalone product with no publicly documented integrations, companion GitHub repo, or plugin/API layer as of this ingest. It operates as a consumer web app. The broader context in this wiki's domain (agentic AI frameworks) is tangential: Planana uses AI internally to generate learning plans but does not expose those capabilities to agents or developers.
