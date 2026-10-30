---
type: source
category: "Agent Skills & plugins ecosystem"
source_url: https://github.com/stripe/ai/tree/main/skills/stripe-best-practices
tags:
  - stripe-integration
  - agent-skills
  - checkout-sessions
  - stripe-connect
  - restricted-api-keys
  - stripe-tax
  - webhooks
  - metronome
related:
  - supabase.com
  - addyosmani-agent-skills
  - anthropics-skills
  - supabase-agent-skills
product: stripe-best-practices
detail_level: standard
created: 2026-10-30
updated: 2026-10-30
---

stripe-best-practices is Stripe’s official Agent Skill (`SKILL.md` plus domain reference files) that steers coding agents through current Stripe integration decisions—sandboxes, API and SDK versions, Checkout vs PaymentIntents, Connect Accounts v2, Billing/Metronome, Tax, Treasury, and security—so agents recommend modern patterns instead of deprecated APIs.

_All claims below are sourced from ../../raw/web/stripe-best-practices.md unless otherwise noted._

## What it does

The skill activates when planning, building, modifying, testing, or reviewing any Stripe integration: choosing a development environment, accepting payments, building marketplaces, subscriptions, sales tax/VAT/GST, connected accounts, Treasury financial accounts, or secure key handling. It pins the latest Stripe API version (**2026-10-28.endive**), tables current SDK versions (Ruby, Python, Node.js, PHP, Java, Go, .NET), and routes each product area to a dedicated reference under `references/` that the agent must read before answering or writing code.

## Key features

- **Integration routing table** — maps one-time payments, embedded Payment Element, Setup Intents, Connect platforms, usage-based billing (Metronome), subscriptions, Stripe Tax, v2 Financial Accounts, and security topics to the matching reference file.
- **Critical rules** — prefer separate sandboxes over shared test mode for new work; recommend restricted API keys (`rk_`) over secret keys (`sk_`); never pass `payment_method_types` except Terminal (`card_present`); treat webhooks as required (not optional); always use `StripeClient` instance APIs, not deprecated global key patterns; confirm active Tax registrations before enabling `automatic_tax`.
- **Domain references** — `payments.md`, `billing.md`, `connect.md`, `tax.md`, `treasury.md`, and `security.md` encode traps, migration paths from Charges/Sources/Tokens/Card Element, and Connect v2 capability checks.
- **CLI sandbox path** — `npm i -g @stripe/cli` then `stripe sandbox create` for test keys without registration; do not use MCP after sandbox create until `stripe sandbox claim`; prefer `stripe whoami --format json` over `stripe config --list`.

## Architecture and concepts

The package is a single skill directory: root `SKILL.md` (YAML `name` / `description` plus routing and critical rules) and `references/` for deep guidance. Agents are told to load the relevant reference before answering. Billing steers new usage-based work to Metronome (not Billing Meters by default) and pairs subscriptions with Checkout `mode: 'subscription'` plus Customer Portal. Connect mandates Accounts v2 (`/v2/core/accounts`) with dashboard / fees_collector / losses_collector dimensions instead of legacy `type: express|custom|standard`. Payments prefer Checkout Sessions (or Payment Element backed by Checkout `ui_mode: 'custom'`) over raw PaymentIntents when possible, and fulfill from webhook handlers (`checkout.session.completed` and `checkout.session.async_payment_succeeded`, gated on `payment_status`), not success pages.

## Main APIs

Primary surfaces the skill steers agents toward: Checkout Sessions (`checkout.sessions.create`, including `integration_identifier` on API `2026-03-25.dahlia`+), PaymentIntents / SetupIntents, Billing APIs and Metronome for usage-based billing, Accounts v2 (`POST /v2/core/accounts`) with merchant vs recipient capability paths, Stripe Tax settings/registrations and `automatic_tax`, Tax Calculations for verification, and v2 Financial Accounts (`POST /v2/core/vault/financial_accounts`) for new Treasury work. Explicitly avoid Charges, Sources, Tokens, Card Element, v1 account `type` fields, and v1 Treasury for new integrations.

## When to use

Use when an agent is writing or reviewing Stripe-backed payment, marketplace, subscription, tax, or embedded-finance code and needs up-to-date defaults (sandboxes, RAKs, dynamic payment methods, Connect v2, Metronome, Tax registration checks) rather than training-data patterns that still suggest deprecated APIs.

## Ecosystem

Lives under `stripe/ai` at `skills/stripe-best-practices`. Points agents at Stripe docs (Integration Options, API Tour, Go Live Checklist, sandboxes, keys, webhooks) and, for Metronome implementation questions, the separate `metronome` skill (or `https://docs.stripe.com/.well-known/skills/metronome/SKILL.md` if not installed). Fits the same Agent Skills packaging pattern as other vendor and community skill packs in this wiki.
