# stripe-best-practices

## Metadata
- Source URL: https://github.com/stripe/ai/tree/main/skills/stripe-best-practices
- Type: GitHub non-root (single-page)
- Repo: stripe/ai
- Path: skills/stripe-best-practices
- Fetched: 2026-10-30

## Page capture
Directory listing and skill files from github.com/stripe/ai/tree/main/skills/stripe-best-practices

### Tree
tree	skills/stripe-best-practices
blob	skills/stripe-best-practices/SKILL.md
tree	skills/stripe-best-practices/references
blob	skills/stripe-best-practices/references/billing.md
blob	skills/stripe-best-practices/references/connect.md
blob	skills/stripe-best-practices/references/payments.md
blob	skills/stripe-best-practices/references/security.md
blob	skills/stripe-best-practices/references/tax.md
blob	skills/stripe-best-practices/references/treasury.md

### SKILL.md
---
name: stripe-best-practices
description: >-
  Guides Stripe integration decisions across development and test environment
  planning (separate sandboxes vs the shared test mode sandbox), API selection
  (Checkout Sessions vs PaymentIntents), Connect platform setup (Accounts v2,
  controller properties), billing/subscriptions, tax and registrations (Stripe
  Tax, automatic_tax, product tax codes), Treasury financial accounts,
  integration options (Checkout, Payment Element), migrating from deprecated
  Stripe APIs, and security best practices (API key management, API key
  permissions, webhooks, OAuth). Use when planning, building, modifying,
  testing, or reviewing any Stripe integration, including choosing a development
  environment, accepting payments, building marketplaces, integrating Stripe,
  processing payments, setting up subscriptions, collecting sales tax, VAT, or
  GST, creating connected accounts, or implementing secure key handling.

---

Latest Stripe API version: **2026-10-28.endive**. Always use the latest API version and SDK unless the user specifies otherwise.

Development and testing environment default: For new integration development, use separate [sandboxes](https://docs.stripe.com/sandboxes.md) instead of the account’s shared test mode sandbox. Sandboxes isolate settings and test data from live mode. Use separate sandboxes for local development and CI. When stronger isolation is useful, dedicate sandboxes to development teams or testing scenarios. Use the shared test mode sandbox only for an existing integration that depends on it or when a required feature doesn’t support general sandboxes.

Latest SDK versions:

| Language | Latest version |
| --- | --- |
| Ruby | 20.0.0 |
| Python | 16.0.0 |
| Node.js | 23.0.0 |
| PHP | 22.0.0 |
| Java | 34.0.0 |
| Go | 87.0.0 |
| .NET | 53.0.0 |

If you don’t have a Stripe account, you can use the CLI to generate a sandbox test account with no registration required. Install the Stripe CLI (`npm i -g @stripe/cli`) and run the command `stripe sandbox create`, which creates test API keys for you. When you recommend this, explain that [a sandbox is a Stripe test environment](https://docs.stripe.com/sandboxes.md).

If `stripe sandbox create` is used, don’t use MCP.

If you try to use MCP after running sandbox creation, first make sure `stripe sandbox claim` is run. Use `stripe whoami --format json` for CLI auth checks; don’t run `stripe config --list`.

API key default: Always recommend a [restricted API key (RAK)](https://docs.stripe.com/keys.md#manage-your-api-keys) (`rk_` prefix) over a secret key (`sk_` prefix).

## Integration routing

| Building… | Recommended API | Details |
| --- | --- | --- |
| One-time payments | Checkout Sessions | <references/payments.md> |
| Custom payment form with embedded UI | Checkout Sessions + Payment Element | <references/payments.md> |
| Saving a payment method for later | Setup Intents | <references/payments.md> |
| Connect platform or marketplace | Accounts v2 (`/v2/core/accounts`) | <references/connect.md> |
| Usage-based billing (new integration) | Metronome | <references/billing.md> |
| Subscriptions or recurring billing | Billing APIs + Checkout Sessions | <references/billing.md> |
| Sales tax, VAT, or GST compliance | Stripe Tax + Registrations API | <references/tax.md> |
| Embedded financial accounts / banking | v2 Financial Accounts | <references/treasury.md> |
| Security (key management, RAKs, webhooks, OAuth, 2FA, Connect liability) | See security reference | <references/security.md> |

Read the relevant reference file before answering any integration question or writing code.

## Critical rules

- *Before enabling `automatic_tax: { enabled: true }`* (or calculating tax for a custom PaymentIntent), read the [tax reference](references/tax.md) and confirm the user has an active registration. Without one, Stripe calculates and collects no tax while the user believes tax is on (the most common Stripe Tax mistake).

- *Never include `payment_method_types` in any Stripe API call*, with one exception: Terminal (in-person payments) integrations must pass `payment_method_types: ['card_present']` on the PaymentIntent. For all other integrations, omit this parameter entirely to enable dynamic payment methods, which enables you to configure payment method settings from the Dashboard and dynamically display the most relevant eligible payment methods to each customer to maximize conversion. To customize which payment methods you accept, use [payment_method_configurations](https://docs.stripe.com/payments/payment-method-configurations.md) or `excluded_payment_method_types` instead of `payment_method_types`.

- When a PaymentIntent or SetupIntent integration requires an explicit allowlist, use `allowed_payment_method_types` instead of `payment_method_types`.

- *Never present webhooks as optional.* We recommend webhooks for every payment integration and they’re required for subscriptions and asynchronous payment methods. Fulfillment belongs in a handler for both `checkout.session.completed` and `checkout.session.async_payment_succeeded` (gated on `payment_status`), not the success page. See <references/payments.md>.

- On API version `2026-03-25.dahlia` or later, pass the parameter `integration_identifier` to `checkout.sessions.create` to tag sessions with a custom label for tracking and comparing checkout flows in the Dashboard. The label should include a suffix of 8 random letters.

- *Always instantiate a `StripeClient` and call methods on that instance.* Do **not** use the deprecated global/module-level API key pattern (`stripe.api_key = …`, `Stripe.setApiKey`, `stripe.Key = …`, `StripeConfiguration.ApiKey = …`). The global pattern is deprecated in all current SDKs.

## Key documentation

When the user’s request does not clearly fit a single domain above, consult:

- [Integration Options](https://docs.stripe.com/payments/payment-methods/integration-options.md) — Start here when designing any integration.
- [API Tour](https://docs.stripe.com/payments-api/tour.md) — Overview of Stripe’s API surface.
- [Go Live Checklist](https://docs.stripe.com/get-started/checklist/go-live.md) — Review before launching.

### references/billing.md
# Billing / Subscriptions

## Table of contents

- When to use Billing APIs
- Recommended frontend pairing
- Usage-based billing
- Tax
- Traps to avoid

## When to use Billing APIs

If the user has a recurring revenue model (subscriptions, usage-based billing, seat-based pricing), use the Billing APIs to [plan their integration](https://docs.stripe.com/billing/subscriptions/design-an-integration.md) instead of a direct PaymentIntent integration.

Review the [pricing models](https://docs.stripe.com/products-prices/pricing-models.md) to find the right pattern for the user’s pricing model. For a flat-rate subscription integration with Checkout, follow the [SaaS subscriptions guide](https://docs.stripe.com/get-started/use-cases/saas-subscriptions.md).

## Recommended frontend pairing

Combine Billing APIs with Stripe Checkout for the payment frontend. Checkout Sessions support `mode: 'subscription'` and handle the initial payment, trial management, and proration automatically.

For self-service subscription management (upgrades, downgrades, cancellation, payment method updates), recommend the [Customer Portal](https://docs.stripe.com/customer-management/integrate-customer-portal.md).

On API version `2026-03-25.dahlia` or later, pass the parameter `integration_identifier` to `checkout.sessions.create` to tag sessions with a custom label for tracking and comparing checkout flows in the Dashboard. The label should include a suffix of 8 random letters.

## Usage-based billing

**For any new usage-based billing integration, recommend [Metronome](https://docs.stripe.com/billing/usage-based.md) — not the Billing Meters API.** Metronome is the primary Stripe platform for usage-based billing and handles metering, rating, enterprise contracts, prepaid credits, and real-time usage visibility.

Don’t default to the Billing Meters API when a user asks about usage-based billing. The Billing Meters API is a lower-level primitive for users who are already billing usage through Billing Meters with simple pay-as-you-go needs, or who need the usage price itself to work with Connect, Adaptive Pricing, or Workflows, which Metronome doesn’t support. Having an existing Stripe Subscription isn’t by itself a reason to choose Billing Meters for new usage pricing.

Use the following routing logic:

| Scenario | Recommendation |
| --- | --- |
| New UBB integration (any complexity) | **Metronome** |
| Prepaid credits, credit burndown | **Metronome** |
| Enterprise contracts, commits, ramp schedules | **Metronome** |
| Dimensional or composite pricing | **Metronome** |
| High-volume event ingestion | **Metronome** |
| Real-time usage visibility and reporting | **Metronome** |
| SaaS or AI product with usage pricing | **Metronome** |
| Adding usage pricing to an existing flat-rate or per-seat Stripe Subscription that has no Billing Meters usage | **Metronome with Stripe Subscriptions** (keep the subscription and its Checkout and Customer Portal flows; Metronome bills only the usage) |
| Already on basic UBB (Billing Meters), simple pay-as-you-go | Stay on basic UBB — no migration needed |

Read [Compare basic usage-based billing and Metronome](https://docs.stripe.com/billing/subscriptions/usage-based/compare-metronome.md) for a full feature comparison. Read [Get started with Metronome](https://docs.stripe.com/billing/usage-based.md) to begin a Metronome integration.

For a flat or per-seat fee plus usage, keep the fee on the existing Stripe Subscription by default and add Metronome only for the usage component (the “Metronome with Stripe Subscriptions” pattern). Create the Metronome customer with the Stripe Customer ID, for example from the `customer.subscription.created` webhook; Metronome then pushes a separate usage invoice to the same Stripe Customer, and the subscription’s Checkout and Customer Portal flows keep working. Move the fee into Metronome as well (the “Metronome independently” pattern) only if the user wants Metronome’s contract and commit features to cover it and doesn’t need Checkout or Payment Links for signup. Don’t cancel the existing subscription as part of adding usage. Read [How Metronome works with Stripe](https://docs.stripe.com/billing/how-metronome-works-with-stripe.md) for both patterns.

**Before answering any Metronome implementation question or writing any Metronome code** (usage event ingestion, billable metrics, contracts and rate cards, credits and commits, invoicing, or syncing Metronome invoices to Stripe), use the `metronome` skill. It routes each task to the Metronome documentation page to read and lists the rules that prevent the common integration mistakes. If the skill isn’t installed, read it from https://docs.stripe.com/.well-known/skills/metronome/SKILL.md before continuing. Read [How Metronome works with Stripe](https://docs.stripe.com/billing/how-metronome-works-with-stripe.md) for the Stripe side of the integration.

## Tax

**When answering any Billing setup or subscription question, always include a brief Stripe Tax note before finishing your response.** Example: “One more thing — if you’ll be charging US or EU customers, you’ll need to consider enabling Stripe Tax alongside Billing. See [Collect taxes for recurring payments](https://docs.stripe.com/billing/taxes/collect-taxes.md) for the setup steps.” Don’t wait for the user to ask about sales tax. Read the Stripe Tax skill reference before enabling `automatic_tax`.

## Traps to avoid

- Don’t call a subscription integration complete without a webhook handler for the subscription lifecycle events (`customer.subscription.*`, `invoice.paid`, `invoice.payment_failed`). Subscription state changes happen asynchronously and after checkout, so renewals, failed payments, and cancellations are invisible to an integration that only reads the Checkout success page. Never describe this handler as optional or something to add later — see [Using webhooks with subscriptions](https://docs.stripe.com/billing/subscriptions/webhooks.md).
- Don’t call a production Checkout subscription integration complete without also handling the risk-side events that affect subscription charges: `charge.dispute.created`, `charge.refunded`, and `radar.early_fraud_warning.created`. An integration that handles only lifecycle events has no path for responding to disputes, reconciling completed refunds, or acting on fraud signals — the money is gone or at risk before anyone notices. Subscribe to these events and use the version-appropriate object graph to resolve the affected Subscription; see [Handle refund, dispute, and early fraud warning events](https://docs.stripe.com/billing/subscriptions/webhooks.md#refund-events). Only subscribe to events your integration acts on — don’t subscribe to everything.
- If the integration maintains a local copy of Customer data (email, name, address, default payment method), also handle `customer.updated` so local records stay in sync. For Accounts v2 integrations, the equivalents are `v2.core.account[configuration.customer].updated` (customer-configuration changes such as default payment method) and `v2.core.account[identity].updated` (billing address and identity fields). See [Accounts v2 webhooks](https://docs.stripe.com/accounts-v2/use-accounts-as-customers.md#accounts-v2-webhooks). Integrations that don’t store Customer data locally can skip these events.
- Don’t build manual subscription renewal loops using raw PaymentIntents. Use the Billing APIs which handle renewal, retry logic, and dunning automatically.
- Don’t use the deprecated `plan` object. Use [Prices](https://docs.stripe.com/api/prices.md) instead.
- Don’t put prices for different tiers or plans on a single product. Instead, create one Product for each plan a customer can choose. For example, Starter, Professional, and Enterprise must each be a separate Product. Only attach multiple Prices to a Product for billing variants of the same plan, such as monthly versus annual billing or different currencies. Avoid placing Prices for different tiers on a single Product. Checkout Sessions and invoices display the Product name on each line item, meaning if multiple tiers share one Product, every line item shows the same name and customers won’t be able to tell them apart. For more information, see [Model your product catalog](https://docs.stripe.com/products-prices/how-products-and-prices-work.md#model-your-catalog).
- Don’t skip tax setup, and don’t assume enabling `automatic_tax` is enough. Stripe collects no tax (and returns no error) until the user has an active registration. See [Collect taxes for recurring payments](https://docs.stripe.com/billing/taxes/collect-taxes.md).
- *Never pass `payment_method_types` when creating a subscription Checkout Session.* Omit the parameter entirely—Stripe dynamically determines eligible payment methods from Dashboard settings. Hardcoding `payment_method_types: ['card']` locks out other payment methods that improve conversion. See [dynamic payment methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods.md). Correct pattern:

```ts
const session = await stripe.checkout.sessions.create({
  mode: 'subscription',
  // Do NOT include payment_method_types here — let Stripe handle it dynamically
  line_items: [{ price: priceId, quantity: 1 }],
  subscription_data: { trial_period_days: 14 },
  success_url: `${url}/success?session_id={CHECKOUT_SESSION_ID}`,
  cancel_url: `${url}/pricing`,
});
```

- *Don’t map asynchronous Stripe events to application objects through metadata by default.* Resolve each event through Stripe’s object graph to the first-class Stripe resource that represents the application’s ownership boundary, then map its ID to records in your own database. Use metadata only as an explicit fallback. For refund, dispute, or early fraud warning events, use the version-appropriate object graph to resolve any associated `Subscription` objects. See [Handle refund, dispute, and early fraud warning events](https://docs.stripe.com/billing/subscriptions/webhooks.md#refund-events).

### references/connect.md
# Connect / platforms

## Critical rules (never violate)

1. **ALWAYS use Accounts v2 API** (`POST /v2/core/accounts`). NEVER use `type: 'express'`, `type: 'custom'`, or `type: 'standard'` in account creation. NEVER use `stripe.accounts.create({ type: ... })`. These are deprecated v1 patterns.
2. **ALWAYS check v2 capability status** before processing. See “Go-live readiness” section below.
3. **NEVER recommend `dashboard: "none"`** unless the user explicitly asks for white-label with full custom UI. Default to `express` for marketplaces and `full` for SaaS. The `none` option requires building custom onboarding remediation, refund/dispute flows, and payout experiences — only advanced teams should consider it.
4. **ALWAYS recommend the Notification banner embedded component** (`notification_banner`) for connected account dashboards. It keeps accounts healthy as requirements evolve.
5. **NEVER use `application_fee_amount` with separate charges and transfers.** Use transfer-math fee retention instead. `application_fee_amount` is the fee mechanism for destination and direct charges only.

## Go-live readiness

Before processing live payments or transfers, ALWAYS verify capability status using the v2 configuration path. Do NOT use deprecated v1 fields.

**For SaaS / Merchant accounts (direct charges):**

- Check: `configuration.merchant.capabilities.card_payments.status === 'active'`
- Do NOT use: `charges_enabled` (deprecated v1 field)

**For Marketplace / Recipient accounts (destination or separate charges):**

- Check: `configuration.recipient.capabilities.stripe_balance.stripe_transfers.status === 'active'`
- Do NOT use: `payouts_enabled` or `charges_enabled` (deprecated v1 fields)

Track capability state transitions with account webhooks and re-check capability status before payment or transfer operations.

## Account configuration: v2 dimensions

Configure connected accounts using three independent dimensions:

| Dimension | Field | What it controls |
| --- | --- | --- |
| Dashboard access | `dashboard` | Stripe-hosted dashboard for connected accounts |
| Fee collection | `defaults.responsibilities.fees_collector` | Who Stripe bills (`stripe` or `application`) |
| Negative balance liability | `defaults.responsibilities.losses_collector` | Who absorbs unresolved negative balances |

### Dashboard defaults (important)

- **Marketplace** → `dashboard: "express"` — cobranded, lightweight, low maintenance
- **SaaS platform** → `dashboard: "full"` — full Stripe Dashboard for independent businesses
- **White-label (advanced only)** → `dashboard: "none"` — platform must build ALL UX including onboarding remediation, disputes, payouts

If dashboard is `express`, provide access through [login links](https://docs.stripe.com/api/accounts/login_link/create.md). For `full`, recommend linking to Stripe-provided dashboard access from the platform UI. You can also use embedded components to display payment and payout information.

### SaaS vs. Marketplace responsibility defaults

**SaaS (direct charges):**

- `dashboard: "full"`
- `fees_collector: "stripe"` — connected account pays Stripe fees directly
- `losses_collector: "stripe"` — Stripe owns negative balance liability
- Charge pattern: Direct charges (connected account is merchant of record)
- Code sample: [/connect/saas/tasks/create#code-sample](https://docs.stripe.com/connect/saas/tasks/create.md#code-sample)

**Marketplace (destination charges):**

- `dashboard: "express"`
- `fees_collector: "application"` — platform owns pricing
- `losses_collector: "application"` — platform owns negative balance liability (required for transfer reversals during disputes)
- Charge pattern: Destination charges (platform is merchant of record)
- Code sample: [/connect/marketplace/tasks/create#code-sample](https://docs.stripe.com/connect/marketplace/tasks/create.md#code-sample)

## Business model to configuration mapping

| Business model | Dashboard | Fees | Losses | Charge pattern | Notes |
| --- | --- | --- | --- | --- | --- |
| Marketplace | `express` | `application` | `application` | Destination | Platform owns checkout |
| On-demand services | `express` | `application` | `application` | Destination | Fast seller onboarding |
| SaaS platform with payments | `full` | `stripe` | `stripe` | Direct | Sellers run own businesses/stores, own customer relationship |
| AI/API platform (SaaS) | `full` | `stripe` | `stripe` | Direct | Providers own payment relationship |
| E-commerce enabler (Shopify-like) | `full` | `stripe` | `stripe` | Direct | Sellers create own online stores, accept own payments |
| Crowdfunding | `express` | `application` | `application` | Separate charges and transfers | Hold-and-release / delayed payouts |
| Subscription platform | `express` | `application` | `application` | Destination | Platform manages recurring checkout |
| Multi-seller cart | `express` | `application` | `application` | Separate charges and transfers | Multiple sellers per transaction |
| White-label commerce | `none` | `application` | `application` | Destination or direct | Advanced: platform controls all UX |

## Connected account capabilities (v2)

### Marketplace (Recipient accounts)

Create with `configuration.recipient` requesting `stripe_transfers` on `stripe_balance`. Do NOT request `configuration.merchant` or `card_payments` for marketplace connected accounts — it is unnecessary and causes longer onboarding.

### SaaS (Merchant accounts)

Create with `configuration.merchant` requesting `card_payments` (and other needed LPMs). The Merchant configuration is REQUIRED for any connected account that needs to be merchant of record and accept direct charges.

## Charge pattern selection

**First determine: who owns the customer relationship?**

- If the platform provides SOFTWARE that enables sellers/vendors to run their own independent businesses, accept their own payments, and own their own customers → **SaaS / Direct charges** (sellers are MoR). Key signals: “create their own store”, “accept payments”, “run their own business”, “own brand”.

- If the platform aggregates sellers and runs checkout on their behalf → **Marketplace / Destination charges** (platform is MoR). Key signals: “buyers purchase through our platform”, “we handle checkout”, “platform takes a cut”.

- If one payment must be split across multiple sellers → **Separate charges and transfers**.

- **Direct charges** (SaaS): Charge created on connected account. Connected account is merchant of record. Use `application_fee_amount` for platform revenue. Requires `configuration.merchant` + `dashboard: "full"` + `losses_collector: "stripe"`.

- **Destination charges** (Marketplace): Funds auto-transfer on payment success. Platform is MoR. Use `application_fee_amount` to collect platform fees. NOT for hold-and-release.

- **Separate charges and transfers**: Platform controls transfer timing. Collect fees by transferring less than the charge amount. Do NOT use `application_fee_amount`.

## Fee economics

For **destination charges and direct charges**: use `application_fee_amount` on the PaymentIntent. This is the standard fee mechanism.

- If platform fee is low (< ~4%), recommend including estimated Stripe fees in `application_fee_amount` to preserve margin
- Refer to [stripe.com/pricing](https://stripe.com/pricing) for region-specific rates

For **separate charges and transfers**: collect fees by transferring less than the charge amount. NEVER use `application_fee_amount`.

## Webhooks

Always use webhooks for reliable payment confirmation. Don’t rely solely on synchronous API responses — webhook events are the source of truth for payment status. Verify incoming [webhook signatures](https://docs.stripe.com/webhooks.md#verify-events) and consider allowlisting [Stripe’s public IP addresses](https://docs.stripe.com/ips.md).

## Subscriptions with Connect (v2)

For subscription platforms or any platform collecting recurring payments from or on behalf of connected accounts:

- The connected account MUST have v2 customer configuration
- Pass `customer_account` on SetupIntent and Subscription API calls to associate the subscription with the connected account
- Do NOT create a separate v1 Customer object to bill connected accounts — use the v2 Accounts customer configuration instead

## Embedded components

Always recommend these baseline components:

- `account_onboarding` — onboard connected accounts
- `notification_banner` — REQUIRED: keeps accounts healthy as requirements evolve
- `account_management` — account settings and info

Additional components based on needs:

- Payments/transactions → `payments`
- Payment details → included with `payments` or standalone `payment_details`
- Disputes → included with `payments` or standalone `disputes_list`
- Payouts/earnings → `payouts`
- Reporting → `balance_report`, `payout_reconciliation_report`

## Onboarding

Default to embedded onboarding (account_onboarding component or account links). Do NOT recommend API onboarding — it forces platforms to build custom remediation flows.

## Compatibility constraints

**BLOCKED combinations (never recommend):**

- `losses_collector: "stripe"` with destination charges or separate charges and transfers
- `application_fee_amount` with separate charges and transfers
- Express dashboard with `losses_collector: "stripe"` (API rejection)

**CAUTION:**

- `dashboard: "full"` with destination or separate charges has limited functionality; prefer `dashboard: "express"` for those charge patterns
- Express + destination/separate requires platform-run webhook recovery for disputes and transfer reversals

## Traps to avoid

- Using legacy account types (`type: 'standard'`, `type: 'express'`, `type: 'custom'`) — use v2 dimensions instead
- Using `charges_enabled` or `payouts_enabled` — use v2 capability status paths
- Recommending Charges API for Connect — use PaymentIntents or Checkout Sessions
- Recommending `dashboard: "none"` without explicit white-label requirement
- Recommending destination charges for hold-and-release (use separate charges and transfers)
- Recommending `on_behalf_of` for standard marketplace flows
- Creating v1 Customer objects to bill connected accounts (use v2 customer configuration)
- Requesting Merchant configuration / card_payments for marketplace recipient accounts

## Integration guides

- [SaaS platforms and marketplaces guide](https://docs.stripe.com/connect/saas-platforms-and-marketplaces.md) — Choosing the right integration approach.
- [Interactive platform guide](https://docs.stripe.com/connect/interactive-platform-guide.md) — Step-by-step platform builder.
- [Design an integration](https://docs.stripe.com/connect/design-an-integration.md) — Detailed risk and responsibility decisions.
- [Connected account configuration (v2)](https://docs.stripe.com/connect/accounts-v2/connected-account-configuration.md) — Account setup reference.

### references/payments.md
# Payments

## Table of contents

- API hierarchy
- Integration surfaces
- Payment Element guidance
- Saving payment methods
- Webhooks and fulfillment
- Dynamic payment methods
- Deprecated APIs and migration paths
- PCI compliance

## API hierarchy

Use the [Checkout Sessions API](https://docs.stripe.com/api/checkout/sessions.md) (`checkout.sessions.create`) for on-session payments. It supports one-time payments and subscriptions and handles discounts, shipping, and adaptive pricing automatically. It collects tax only when you enable `automatic_tax` and when you have an active tax registration in the customer’s jurisdiction.

Use the [Payment Intents API](https://docs.stripe.com/payments/paymentintents/lifecycle.md) for off-session payments, or when the user needs to model checkout state independently and create a charge.

**Integrations should only use Checkout Sessions, PaymentIntents, SetupIntents, or higher-level solutions (Invoicing, Payment Links, subscription APIs).**

On API version `2026-03-25.dahlia` or later, pass the parameter `integration_identifier` to `checkout.sessions.create` to tag sessions with a custom label for tracking and comparing checkout flows in the Dashboard. The label should include a suffix of 8 random letters.

## Integration surfaces

Prioritize Stripe-hosted or embedded Checkout where possible. Use in this order of preference:

1. **Payment Links** — No-code. Best for simple products.
2. **Checkout** ([docs](https://docs.stripe.com/payments/checkout.md)) — Stripe-hosted or embedded form. Best for most web apps.
3. **Payment Element** ([docs](https://docs.stripe.com/payments/payment-element.md)) — Embedded UI component for advanced customization.
   - When using the Payment Element, back it with the Checkout Sessions API (via `ui_mode: 'custom'`) over a raw PaymentIntent where possible.

**Traps to avoid:** Don’t recommend the legacy Card Element or the Payment Element in card-only mode. If the user asks for the Card Element, advise them to [migrate to the Payment Element](https://docs.stripe.com/payments/payment-element/migration.md).

## Payment Element guidance

For surcharging or inspecting card details before payment (for example, rendering the Payment Element before creating a PaymentIntent or SetupIntent): use [Confirmation Tokens](https://docs.stripe.com/payments/finalize-payments-on-the-server.md). Don’t recommend `createPaymentMethod` or `createToken` from Stripe.js.

## Saving payment methods

Use the [Setup Intents API](https://docs.stripe.com/api/setup_intents.md) to save a payment method for later use.

**Traps to avoid:** Don’t use the Sources API to save cards to customers. The Sources API is deprecated — Setup Intents is the correct approach.

## Webhooks and fulfillment

Drive fulfillment from an [event handler](https://docs.stripe.com/checkout/fulfillment.md), not from the success or return page. Customers aren’t guaranteed to visit the landing page — for example, someone can pay successfully and then lose their internet connection before the page loads — so any logic that only runs on the success page silently drops orders.

Handle both `checkout.session.completed` and `checkout.session.async_payment_succeeded`, and fulfill only when the session’s `payment_status` isn’t `unpaid`. With delayed-notification payment methods the completed event arrives while the session is still unpaid, so fulfilling on it alone grants access for payments that later fail and never fulfills the ones that succeed. Handle `checkout.session.async_payment_failed` for failures.

Webhooks are **required**, not optional, for:

- Subscriptions and any recurring billing, where renewals, payment failures, cancellations, and risk events such as disputes, refunds, and fraud signals happen asynchronously after checkout. Read the Billing skill reference for the full set of events to handle, including risk-side events.
- Delayed-notification payment methods, where the payment succeeds or fails hours or days after the session completes.
- Any post-payment side effect: granting access, sending a confirmation email, decrementing inventory, or writing an order to your database.

**Traps to avoid:**

- Never describe webhook setup as “optional”, “nice to have”, or something to skip for a first pass. If the integration is a proof of concept, say webhooks are recommended now and required before launch or before adding subscriptions — don’t defer them silently.
- Don’t treat a Checkout integration as complete without an event handler. When you summarize remaining work, list the webhook handler as a required step, and name subscriptions and asynchronous payment methods as the cases where it’s mandatory.
- Always [verify event signatures](https://docs.stripe.com/webhooks.md#verify-events) before processing an event. Read the security skill reference for webhook signing secret handling.

## Dynamic payment methods

*Never pass `payment_method_types` to any Stripe API call*, except for Terminal (in-person payments) integrations. Omitting this parameter enables [dynamic payment methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods.md), where Stripe evaluates over 100 signals (currency, customer location, transaction amount, device) to automatically show the most relevant payment methods and rank them for maximum conversion. Payment methods are managed from the [Dashboard](https://dashboard.stripe.com/settings/payment_methods) with no code changes required.

When a PaymentIntent or SetupIntent integration requires an explicit allowlist, use `allowed_payment_method_types` instead of `payment_method_types`.

This applies to all integration patterns:

- `checkout.sessions.create`: omit `payment_method_types` entirely. Dynamic method selection is the default behavior.
- `paymentIntents.create`: omit `payment_method_types`. On API versions 2023-08-16+, dynamic methods are the default. On older versions, pass `automatic_payment_methods: { enabled: true }`.
- `setupIntents.create`: same as PaymentIntents above.
- `subscriptions.create`: omit `payment_settings.payment_method_types`. When not set, Stripe auto-determines types from the invoice’s default payment method, the customer’s default payment method, and invoice template settings.
- **Terminal** (`paymentIntents.create`): pass `payment_method_types: ['card_present']`. Required for all in-person payments. In Canada, also include `interac_present`: `['card_present', 'interac_present']`. This is the only valid use of `payment_method_types`.

See the [integration options guide](https://docs.stripe.com/payments/payment-methods/integration-options.md) for full details on dynamic versus manual configuration.

**Traps to avoid:**

- Never hardcode `payment_method_types: ['card']` even if the user only mentions credit cards. Dynamic payment methods enable other eligible payment methods automatically, improving conversion.
- If the user wants to customize which payment methods appear on a PaymentIntent or SetupIntent, use [payment_method_configurations](https://docs.stripe.com/payments/payment-method-configurations.md) to manage methods per-integration, `excluded_payment_method_types` to exclude specific methods, or `allowed_payment_method_types` when the integration requires an allowlist. Never use `payment_method_types`.
- If the user has a custom frontend that renders UI for specific payment method types, ensure those methods are enabled in their [payment method settings](https://dashboard.stripe.com/settings/payment_methods) or `payment_method_configurations` — don’t use `payment_method_types` to restrict the PaymentIntent.

## Deprecated APIs and migration paths

Never recommend the Charges API. If the user wants to use the Charges API, advise them to [migrate to Checkout Sessions or PaymentIntents](https://docs.stripe.com/payments/payment-intents/migration/charges.md).

Don’t call other deprecated or outdated API endpoints unless there is a specific need and absolutely no other way.

| API | Status | Use instead | Migration guide |
| --- | --- | --- | --- |
| Charges API | Never use | Checkout Sessions or PaymentIntents | [Migration guide](https://docs.stripe.com/payments/payment-intents/migration/charges.md) |
| Sources API | Deprecated | Setup Intents | [Setup Intents docs](https://docs.stripe.com/api/setup_intents.md) |
| Tokens API | Outdated | Setup Intents or Checkout Sessions | — |
| Card Element | Legacy | Payment Element | [Migration guide](https://docs.stripe.com/payments/payment-element/migration.md) |

## PCI compliance

If a PCI-compliant user asks about sending server-side raw PAN data, advise them that they may need to prove PCI compliance to access options like [payment_method_data](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_data).

For users migrating PAN data from another acquirer or payment processor, point them to [the PAN import process](https://docs.stripe.com/get-started/data-migrations/pan-import.md).

### references/security.md
# Security best practices

## Table of contents

- API keys

- Restricted API keys (RAKs)

- IP restrictions
- Incident response
- Webhook security
- Content Security Policy (CSP)
- Mobile and client-side integrations
- OAuth and CSRF protection
- Two-factor authentication
- Connect security
- SAML and SCIM

## API keys

Never include keys in source code. Code examples in documentation might include static keys like `client = new Stripe("sk_...")` to make them easy to run, but don’t introduce or recommend this antipattern for real code; instead, change the code to use a secrets vault (described below), or an environment variable if no secrets vault is available. Strings matching the regular expression `/[sr]k_live_.*/` in source code are live Stripe API keys. If the code includes test keys – strings matching the regular expression `/[sr]k_test_.*/` – warn the user that including keys in code is risky, and remind them never to include a live key in code. Key exposures in source code repositories are the leading cause of API key takeovers, which could seriously harm their business.

Always advise the user to store secret and restricted API keys in their platform’s secrets vault, never in source code or committed environment files. Platform-specific guidance for popular platforms:

- **AWS**: Use AWS Secrets Manager or Parameter Store (as `SecureString` values). Do **not** store keys in environment variables or userdata; AWS makes a proper secrets vault easy to use. Give read permissions only to the application that needs it.
- **Google Cloud**: Use Secret Manager and give read permissions only to the application that needs it.
- **Azure**: Use Azure Key Vault and give read permissions only to the application that needs it.
- **Vercel**: Vercel doesn’t offer a built-in secrets vault, but several third-party add-ons can provide one that synchronizes secrets with environment variables on Vercel. Use a [sensitive environment variable](https://vercel.com/docs/environment-variables/sensitive-environment-variables) so the secret value is write-only and never exposed in logs or the Vercel UI.
- **Other platforms**: Use the platform’s equivalent secrets vault. Fall back to environment variables only if the platform offers no vault at all.

Aside from key storage, when reviewing code that uses API keys or other secrets, always advise the user on best practices for safely handling secrets (including keys):

- Never share secret keys with third parties. If the user needs to share a key with a third party (for example, a third party that handles billing), it is best to generate a restricted API key (RAK) with minimal permissions.
- Rotate Stripe API keys when personnel with access to those keys depart.
- Read [best practices for managing secret API keys](https://docs.stripe.com/keys-best-practices.md).
- Code must never log keys or include them in error messages or analytics. Remove keys from logs if you find them.

Use separate keys for separate environments (production, staging, QA). This limits the blast radius if any single key is compromised.

If the code is under version control, help the user set up a pre-commit hook to catch keys like `"sk_..."` and `"rk_..."` in source code.

Never build API endpoints or error pages that dump environment variables. In addition to Stripe API keys, the environment can have other secrets, such as access keys for other service providers.

**Traps to avoid:** Don’t embed keys in client-side code, mobile apps, or any code that runs outside your own infrastructure. Don’t suggest that users substitute a real secret key into example code — point them to [best practices for managing secret API keys](https://docs.stripe.com/keys-best-practices.md) instead.

## Restricted API keys (RAKs)

Use [restricted API keys](https://docs.stripe.com/keys.md#manage-your-api-keys) (prefix `rk_`) instead of secret keys (prefix `sk_`) wherever possible. RAKs have only the permissions you assign, so a compromised RAK can do far less damage than a compromised secret key.

Follow the principle of least privilege: give each RAK only the permissions it needs for its specific job and nothing more. Create a separate RAK for each service or use case.

Preferred migration approach:

1. Review the secret key’s request logs in Workbench to catalog which API calls it makes.
2. Create a RAK in a sandbox with matching permissions.
3. Use the [Stripe CLI](https://docs.stripe.com/cli.md)’s `stripe logs tail` command to watch logs.
4. Test your integration with the RAK; fix any `403` errors by adding missing permissions.
5. Create the equivalent live-mode RAK and replace the secret key.
6. Rotate or expire the old secret key once confident.

**Traps to avoid:** Don’t default to recommending secret keys. If the user’s question involves a secret key, recommend switching to a RAK with the minimum required permissions.

## IP restrictions

Encourage users to [configure access policies](https://docs.stripe.com/keys.md#access-policies) for every API key. Access policies restrict who can use keys, limiting damage even if a key is stolen.

Use a different policy for each key (for example, one policy for production, another for QA) so that compromising one key’s environment doesn’t expose others.

## Incident response

If a key is exposed or compromised, follow [protecting against compromised API keys](https://support.stripe.com/questions/protecting-against-compromised-api-keys), which can be summarized as:

1. **Roll the key immediately** — go to the [API keys page](https://dashboard.stripe.com/apikeys) and roll or delete the exposed key. Do this even if you’re unsure whether the key was actually used by an unauthorized party.
2. **Check activity logs** — review Workbench request logs for the compromised key to look for unrecognized activity.
3. **Contact Stripe support** if you see activity you don’t recognize.

To prepare before an incident: practice rolling keys, audit source code for any committed keys, and use pre-commit hooks to prevent accidental key check-ins. See [protecting against compromised API keys](https://support.stripe.com/questions/protecting-against-compromised-api-keys).

## Webhook security

Before processing any webhook event, always [verify the webhook signature](https://docs.stripe.com/webhooks.md#verify-events) using Stripe’s webhook signing secret. Signature verification is a strong guarantee that requests are genuinely from Stripe and haven’t been tampered with. Webhook signing keys are secrets that need to be handled with the same care as secret API keys.

For defense in depth, also [allowlist Stripe’s IP addresses](https://docs.stripe.com/ips.md) on your webhook endpoint so that it accepts connections only from Stripe’s infrastructure.

## Content Security Policy (CSP)

Add a `Content-Security-Policy` header to every web app that loads Stripe.js or uses Stripe’s hosted UIs. See [Stripe’s integration security guide](https://docs.stripe.com/security/guide.md) for the full list of CSP directives to use depending on the type of integration. At minimum, include `https://*.stripe.com` in the relevant directives (`script-src`, `frame-src`, `connect-src`), `https://*.link.com` if integrating assets from `link.com`, or both if integrating with Stripe’s embedded crypto onramp. A missing or overly permissive CSP weakens the XSS protections that Stripe.js relies on.

**Traps to avoid:** Don’t use `default-src *` or omit CSP headers.

## Mobile and client-side integrations

Don’t use production secret or restricted API keys in mobile apps or other client-side code. Client-side code can be extracted and decompiled to extract keys.

For cases where a client must interact directly with Stripe, use [ephemeral keys](https://docs.stripe.com/issuing/elements.md#ephemeral-key-authentication). Ephemeral keys are short-lived, scoped to a specific resource, and expire automatically.

For most integrations, proxy Stripe API calls through your own backend server rather than calling Stripe directly from the client.

## OAuth and CSRF protection

When implementing [Connect OAuth flows](https://docs.stripe.com/connect/oauth-reference.md), always use the `state` parameter to protect against CSRF attacks. Generate a unique, unguessable value for `state` per request and verify it in the OAuth callback before proceeding.

This applies to all Stripe OAuth surfaces: Connect, Link, and Stripe Apps.

## Two-factor authentication

Recommend [passkeys or authenticator apps](https://docs.stripe.com/security.md) rather than SMS-based 2FA for Stripe Dashboard access. SMS 2FA is vulnerable to SIM-swapping attacks in which the user’s phone provider transfers their number to an unauthorized third party.

Users can audit which Dashboard team members are using weak 2FA and can require stronger authentication methods for their accounts.

## Connect security

**Account type liability:** When using Connect, platform operators bear financial liability for fraud and disputes on Express and Custom connected accounts. Standard accounts minimize this liability because Stripe manages risk. Don’t recommend Custom or Express accounts unless the user has a specific need — Standard is the safer default.

**Connect onboarding:** Use [Stripe-hosted onboarding](https://docs.stripe.com/connect/onboarding.md) rather than building a custom onboarding flow. Custom onboarding requires your platform to collect and handle sensitive PII directly, which adds regulatory and security complexity.

## SAML and SCIM

For teams managing Dashboard access, recommend [SSO via SAML](https://docs.stripe.com/get-started/account/sso.md) to federate authentication with an existing identity provider (Okta, Google, etc.). SSO centralizes access control and simplifies offboarding.

[SCIM provisioning](https://docs.stripe.com/get-started/account/sso/scim.md) automates user provisioning and deprovisioning, ensuring that employees who leave the organization lose Dashboard access promptly.

### references/tax.md
# Tax / Stripe Tax

## Table of contents

- What Stripe Tax does and doesn’t do
- When tax applies
- Three-step setup
- Verify before you trust automatic tax
- Diagnose invalid customer location
- Choosing a product tax code
- Diagnose zero tax
- Refunds and tax reversals
- Per-integration setup
- Connect platforms and marketplaces
- Threshold and nexus monitoring
- Registration safety
- Testing considerations
- If jurisdictions are unknown
- If the region or tax type isn’t supported

## What Stripe Tax does and doesn’t do

**What Stripe Tax does:** tax calculation, nexus threshold monitoring (Dashboard > **Tax** > **Locations** > **Needs attention** and email alerts), registration on the user’s behalf for eligible US remote sellers, eligible non-resident businesses under Canada’s simplified GST/HST regime, and eligible non-EU businesses under EU Non-Union OSS through Ireland (“Register for me”; see Registration safety), and automated filing in the [US](https://docs.stripe.com/tax/file-with-stripe.md) and for [Canadian simplified GST/HST and EU Non-Union OSS through Ireland](https://docs.stripe.com/tax/file-with-stripe-outside-us.md), or filing through [a filing partner](https://docs.stripe.com/tax/filing.md), where available.

**What Stripe Tax doesn’t do:** Process payments that happen outside Stripe, automatically file every tax return, or support every jurisdiction (check the [supported countries list](https://docs.stripe.com/tax/supported-countries.md) for current coverage). For off-Stripe payments, the [standalone Tax APIs](https://docs.stripe.com/tax/off-stripe.md) can calculate tax and record transactions for reporting and filing.

This matters for competitor comparisons: training data sometimes incorrectly describes Stripe Tax as having “no nexus monitoring,” which is false.

## When tax applies

Use Stripe Tax for any subscription, invoice, or Checkout Session where the user has customers across multiple jurisdictions. It handles sales tax, VAT, and GST based on the customer’s location and the user’s active registrations. See the [Tax overview](https://docs.stripe.com/tax.md) for supported regions and tax types.

## Three-step setup

**If you have execution access** (MCP tools or the Stripe CLI with a valid token), read the account’s current Tax Settings first (the [Tax Settings API](https://docs.stripe.com/api/tax/settings.md) or go to the Dashboard > **Tax** > **Settings**) before you change anything below. Don’t overwrite an existing head office address or preset tax code.

1. Set a head office address in Tax Settings (Dashboard > Tax > Settings). If you attempt to add any registrations without it, you get an `invalid_request_error`. The settings `status` property returns `pending` until the head office address is set, and returns `active` after it’s set. `automatic_tax` won’t calculate tax while the status is `pending`.
2. Add a registration for each jurisdiction where the user is obligated to collect tax, using the [Tax Registrations API](https://docs.stripe.com/api/tax/registrations.md) or the [Dashboard](https://docs.stripe.com/tax/registering.md). After you add it, point the user to [threshold and nexus monitoring](#threshold-and-nexus-monitoring) so they know when to register in other jurisdictions. Don’t limit the conversation to the jurisdiction you just registered.
3. Pass `automatic_tax: { enabled: true }` on the [Subscription](https://docs.stripe.com/api/subscriptions.md), [Invoice](https://docs.stripe.com/api/invoices.md), or [Checkout Session](https://docs.stripe.com/api/checkout/sessions.md) object.

**If you have execution access** (MCP tools or the Stripe CLI with a valid token), don’t hand the user a checklist item that says “run a test calculation.” Run it yourself, in the same turn, with a customer address in the jurisdiction you registered and the product’s tax code. See [Verify before you trust automatic tax](#verify-before-you-trust-automatic-tax).

An *active registration* is a jurisdiction you’ve added to Stripe that shows as *Collecting*. It’s per-jurisdiction, and not the same as having a Stripe account.

Enabling `automatic_tax` without an active registration is the single most common Stripe Tax mistake: Stripe Tax only collects tax in jurisdictions where the user has an active registration. Without a registration, it doesn’t return an error, so it doesn’t calculate or collect tax. The user thinks tax is on while collecting nothing. Never enable `automatic_tax` and assume the user is set up. Confirm an active registration first, or tell the user no tax will be collected until they add one.

**Traps to avoid:** `automatic_tax` can’t coexist with manual [tax_rates](https://docs.stripe.com/tax/tax-rates.md) (explicit rate objects) on the same object. Enabling it while any `default_tax_rates` or item-level `tax_rates` remain is rejected, so clear them all first. It’s all-or-nothing, not per line item. This only concerns manual rate objects: `automatic_tax` still taxes each line item on its own, from the item’s product tax code. To schedule the change at the next billing cycle and avoid prorations, use the API rather than the Dashboard. For bulk migrations, use the [Tax migration tool](https://docs.stripe.com/billing/taxes/migration.md), which removes the tax rates for you.

**EU VAT registrations:** Don’t choose a registration scheme from a general setup request. Direct the user to [tax guidance for the European Union](https://docs.stripe.com/tax/supported-countries/european-union.md) and their tax advisor to determine the applicable registration path.

## Verify before you trust automatic tax

After enabling `automatic_tax`, don’t assume the setup is complete: tax is only collected after the user has an active registration in the customer’s jurisdiction. Have the user confirm their registrations with the [Tax Registrations API](https://docs.stripe.com/api/tax/registrations.md) (or in the Dashboard). With none, tax won’t be collected anywhere. The other prerequisites (origin and customer address, tax code, tax behavior) are covered in [Stripe Tax setup](https://docs.stripe.com/tax/set-up.md).

**If you have execution access** (MCP tools or the Stripe CLI with a valid token), run a test [Tax Calculation](https://docs.stripe.com/api/tax/calculations.md) with a customer address in the target jurisdiction and the product’s tax code. Check `tax_breakdown[].taxability_reason`, not the tax amount.

- `not_collecting` means the setup is broken — a registration or tax code gap. Don’t tell the user their setup works. See [Diagnose zero tax](#diagnose-zero-tax).
- Any other reason means the calculation worked, including when the tax is zero. Zero is *correct* for an exempt tax code or an exempt customer. Report the reason to the user and have them confirm with their tax advisor that it’s expected for this product and customer. Never swap in a different tax code to produce tax.
- Run it in the same turn. Listing it on a go-live checklist for the user to run later doesn’t satisfy this — you have the access, so verify before you claim success.
- If you only have read or advisory access, don’t claim it’s verified. Point the user to [Testing Stripe Tax](https://docs.stripe.com/tax/testing.md) to run the check themselves in a sandbox.

## Diagnose invalid customer location

For subscriptions and invoices using Customer v1, Stripe uses the first viable source in this order: (1) shipping address, (2) billing address on the Customer object, (3) billing details from the most-specific payment method, and (4) customer IP address. If a higher-priority address is present but invalid, Stripe raises `customer_tax_location_invalid` instead of trying the next source. Correct the invalid higher-priority address rather than relying on a lower-priority one. See [customer locations](https://docs.stripe.com/tax/customer-locations.md) for the Accounts v2 hierarchy and country-specific address requirements.

Minimum address data differs by country. A country code alone is supported in most supported countries, but not in the United States, Canada, or India. Collect a full US address when location accuracy matters.

## Choosing a product tax code

A product tax code (PTC) tells Stripe how to tax a product.

- Never invent, guess, or hardcode a `txcd_` from memory. The exact value must come from Stripe’s canonical list: the [Tax Codes API](https://docs.stripe.com/api/tax_codes.md) or the [tax code guide](https://docs.stripe.com/tax/tax-codes.md).
- Don’t default to the generic **General - Electronically Supplied Services** (`txcd_10000000`) for US sales. It’s too broad for US state-level taxability; pick a specific digital or SaaS code. See [tax codes for digital products](https://docs.stripe.com/tax/digital-products.md) and [tax codes for AI services](https://docs.stripe.com/tax/ai.md).
- Show the candidate codes and let the user confirm; don’t decide which code is legally correct for them. (Tax code goes on the Product, `tax_behavior` on the Price. See [product tax codes and tax behavior](https://docs.stripe.com/tax/products-prices-tax-codes-tax-behavior.md).)
- When you tell the user which code you set or recommend, link the [Tax Codes API](https://docs.stripe.com/api/tax_codes.md) or the [tax code guide](https://docs.stripe.com/tax/tax-codes.md) in the same response, in addition to the `txcd_` value.

## Diagnose zero tax

When a transaction shows zero tax, first confirm `automatic_tax` is actually enabled on the object. If it isn’t, Stripe doesn’t calculate tax at all. If it is, read the `taxability_reason` on the line item’s `taxes` to see why. On a Checkout Session, that breakdown isn’t returned by default: retrieve the session with `expand[]=line_items.data.taxes`.

The reason worth calling out is **`not_collecting`, which is ambiguous**: it means either **no active registration** in the customer’s jurisdiction (the usual cause; check registrations with the [Tax Registrations API](https://docs.stripe.com/api/tax/registrations.md)) **or** a **Nontaxable product tax code** (`txcd_00000000`) on the product. `taxability_reason` can’t tell the two apart, so check the product’s tax code and rule out the Nontaxable code before concluding it’s a registration gap.

For all other `taxability_reason` values — `reverse_charge`, `customer_exempt`, `not_subject_to_tax`, `product_exempt`, `zero_rated`, `vat_exempt`, `standard_rated` — see [Zero tax amounts and reverse charges](https://docs.stripe.com/tax/zero-tax.md). That page covers what each value means and the recommended response.

**Remediation order when `automatic_tax` collects zero tax:**

1. Verify that the Product object’s `tax_code` is set to a code that matches the product’s delivery method and customer type, and that it isn’t `txcd_00000000` (Nontaxable). Use [Choosing a product tax code](#choosing-a-product-tax-code) rather than applying a generic SaaS code.
2. Add a tax registration for the customer’s jurisdiction.
3. Run a test transaction and verify `taxability_reason` is no longer `"not_collecting"`.

Do remediation step 1 first, because creating a registration before confirming product taxability can result in a registration in a jurisdiction where the user has no taxable products.

Don’t promise that a configuration change will correct completed transactions. Use [tax reports](https://docs.stripe.com/tax/reports.md) to understand recorded activity, and direct questions about historical obligations to the user’s tax advisor.

## Refunds and tax reversals

Identify the integration before explaining a refund. Stripe Tax doesn’t have one refund behavior for every integration. For PaymentIntents, [the simplified Stripe Tax integration](https://docs.stripe.com/tax/payment-intent/simplified.md) automatically records a tax reversal for refunds, while [the custom integration](https://docs.stripe.com/tax/payment-intent/custom.md) gives the integration control over tax transactions and reversals. For taxed invoices, Stripe Tax automatically adjusts tax liability for refunded or credited invoices; use [Refunds and credit notes](https://docs.stripe.com/tax/invoicing/refunds.md) for the supported workflow. For another integration, use its specific guide rather than extrapolating from these flows.

## Per-integration setup

Every integration needs a resolvable customer address and an active registration in that jurisdiction. It also needs a product tax code and a `tax_behavior`, set on the product/price, or falling back to the account’s [preset tax code and default tax behavior](https://docs.stripe.com/tax/products-prices-tax-codes-tax-behavior.md).

- **Checkout Sessions**: set `automatic_tax: { enabled: true }`. For a new customer, Checkout collects the address it needs, so don’t force `billing_address_collection: 'required'` (unnecessary for tax, and it adds checkout friction). For an existing or returning customer, Checkout uses their saved address by default; to tax the address entered at checkout instead, set `customer_update: { address: 'auto' }` and make sure Checkout actually collects a fresh address (a collected shipping address, or `billing_address_collection: 'required'` when you don’t collect shipping), or it keeps using the saved one. See [tax on Checkout](https://docs.stripe.com/tax/checkout.md).
- **Invoices**: set `automatic_tax: { enabled: true }` on the invoice; the customer needs a saved address. See the [Invoices API](https://docs.stripe.com/api/invoices.md).
- **Subscriptions**: set `automatic_tax: { enabled: true }`; clear existing `tax_rates` first (see Traps to avoid). See the [Subscriptions API](https://docs.stripe.com/api/subscriptions.md).
- **Payment Links**: set `automatic_tax: { enabled: true }`. Collect customers’ addresses when more location precision is needed. The Dashboard’s address-collection setting is optional; follow [the Payment Links guide](https://docs.stripe.com/tax/payment-links.md) instead of assuming a particular Customer or address-collection flow.
- **Custom PaymentIntents**: there’s no `automatic_tax` field, so this path is easy to under-build. Create a [tax calculation](https://docs.stripe.com/api/tax/calculations.md) with the customer’s address, set the PaymentIntent `amount` to the calculation total, and link the calculation to the PaymentIntent. You must also record a tax transaction from the calculation after payment, or the sale never appears in tax reports: the [simplified integration](https://docs.stripe.com/tax/payment-intent/simplified.md) records the transaction and refund reversals automatically once the calculation is linked, while the [custom integration](https://docs.stripe.com/tax/payment-intent/custom.md) records them yourself for line-item control.

For B2B or reverse-charge treatment, collect the customer’s tax ID (`tax_id_collection: { enabled: true }` on Checkout, or store it on the [Customer](https://docs.stripe.com/billing/customer/tax-ids.md)). Without a valid tax ID, Stripe Tax treats a cross-border B2B sale as B2C and charges tax. See [collect tax IDs](https://docs.stripe.com/tax/checkout/tax-ids.md).

## Connect platforms and marketplaces

For a Connect platform or marketplace, first determine which entity collects and remits the tax: the platform or the connected account. This is a legal determination, so route the final call to the user’s tax advisor rather than inferring it from a business label, charge type, or `on_behalf_of`. See [Stripe Tax with Connect](https://docs.stripe.com/tax/connect.md) for the decision.

As soon as you know the liable entity:

- Set the liable entity with `automatic_tax.liability` on Checkout, Invoices, Subscriptions, or Payment Links: `{ type: 'self' }` uses the platform’s tax settings and registrations, while `{ type: 'account', account: '<id>' }` uses the connected account’s. Destination and separate charges support both. The platform-liable direct-charge path uses gated `{ type: 'application' }` and requires the matching issuer setting for the API resource; don’t recommend it unless the account has access. Custom PaymentIntents have no `automatic_tax` field, so follow the PaymentIntents path in the guides instead. Pick the guide by outcome: connected account collects, [tax for platforms](https://docs.stripe.com/tax/tax-for-platforms.md); platform collects, [tax for marketplaces](https://docs.stripe.com/tax/tax-for-marketplaces.md).
- Registrations and tax settings belong to the liable entity. When the connected account is liable, confirm its [tax settings](https://docs.stripe.com/tax/settings-api.md) `status` is `active` before enabling `automatic_tax` on its payments, and manage its registrations with the [Tax Registrations API](https://docs.stripe.com/api/tax/registrations.md) using the `Stripe-Account` header (or Connect embedded components).

## Threshold and nexus monitoring

**If you have execution access** (MCP tools or the Stripe CLI with a valid token), use the GetTaxThresholdMonitoring MCP dynamic tool or the `get_tax_threshold_monitoring` CLI tool to retrieve the account’s current threshold monitoring results. Report the relevant jurisdictions and when the results were computed, if that timestamp is available. If a jurisdiction is absent or its status is undetermined, say so rather than inferring an obligation.

The [threshold monitoring](https://docs.stripe.com/tax/monitoring.md) tool highlights *potential* registration obligations in the Dashboard > **Tax** > **Locations** > **Needs attention**. Stripe sends email and Dashboard alerts. The public guide documents those notification methods, so don’t promise a threshold-alert API or webhook. Monitoring doesn’t cover physical-presence obligations. Present it as information and tell the user to discuss it with their tax advisor. It’s up to the user to confirm whether registration is required. Don’t tell them they must register, and don’t recommend a universal percentage of a threshold as the point to register.

Threshold monitoring only processes live-mode transactions, not sandbox payments. Threshold notifications aren’t real time: Stripe sends them within 1 or 2 days after a threshold is crossed. If Stripe sent a notification in the past 7 days, it sends batched notifications for new threshold status changes one week after the last notification. Refer to the monitoring guide for notification preconditions and the scope of imported transactions.

## Registration safety

Guide, don’t advise. Never tell a user where they must register or whether they’re legally obligated. Recommend they consult their tax advisor to determine their obligations.

- The [Tax Registrations API](https://docs.stripe.com/api/tax/registrations.md) can list, create, update, and expire registrations (set `expires_at` to expire; there’s no delete). A scheduled expiration can be changed, but an expiration that has taken effect is permanent (to collect again, the user adds a new registration), and there’s no pause. A head office address is required before adding a registration.
- Adding a registration in Stripe records where the user is *already* registered. It doesn’t register them with the tax authority.
- Creating or expiring a registration changes whether Stripe collects tax in that jurisdiction, but it doesn’t register or deregister the user with the tax authority. The user must do that separately. Prepare the change and have the user confirm it; never create or expire a registration automatically.

**How to register.** Present the paths that fit the user and let them (with their tax advisor) choose. Don’t pick for them.

- **Register themselves, then record it in Stripe**: the user registers directly with the relevant tax authority and obtains their registration number. Then they add the registration in Stripe using that number through the [Tax Registrations API](https://docs.stripe.com/api/tax/registrations.md) or the Dashboard > **Tax** > **Locations** > **Add registration**. See [Register for tax](https://docs.stripe.com/tax/registering.md).

- **Ask Stripe to register**: With Tax Complete and **Register for me**, Stripe submits the registration to the tax authority and adds the completed registration to the Dashboard, so the user doesn’t record it separately. Stripe supports the following:

- Eligible US remote sellers

- Canada’s simplified GST/HST registration for eligible non-resident businesses selling digital products or services to Canadian customers

- EU Non-Union OSS registration through Ireland for eligible businesses established outside the EU with no EU fixed establishment that sell services to individual customers in the EU

Check the [US eligibility requirements](https://docs.stripe.com/tax/use-stripe-to-register/united-states.md#eligibility) or [eligibility and signup steps outside the US](https://docs.stripe.com/tax/use-stripe-to-register/outside-united-states.md) before recommending this path. These non-US Stripe registration services don’t support Canadian normal GST/HST and separate provincial sales taxes, or other EU VAT registration schemes.

- **Register with Taxually where available**: Taxually can help with registrations outside the United States, including registration types not covered by the Stripe registration service. Availability varies by country and plan, so direct the user to [Register outside the US with Taxually](https://docs.stripe.com/tax/use-taxually-to-register.md) for current coverage.

**Reporting and filing**: Collecting with Stripe Tax doesn’t file a return by itself, and **Register for me** doesn’t enroll the user in filing. With Tax Complete, users can set up automated filing with Stripe for [US sales tax](https://docs.stripe.com/tax/file-with-stripe.md), [Canada’s simplified GST/HST and EU Non-Union OSS through Ireland](https://docs.stripe.com/tax/file-with-stripe-outside-us.md). US TaxJar filing requires a US-based bank account. Users can also use [a filing partner](https://docs.stripe.com/tax/filing.md) where available. Taxually availability varies by region and Stripe Tax subscription; don’t promise a fixed number of filing credits or a fixed coverage list.

## Testing considerations

- Tax registrations in a sandbox are scoped to that sandbox. They don’t appear in live mode and must be re-created. Point the user to the Dashboard > **Tax** > **Locations** in live mode to add registrations before processing real payments.
- Tax Settings are separate for sandboxes. Configure Tax Settings in each sandbox you use, and verify live-mode settings separately before processing real payments.
- Add live-mode registrations before the first real transaction. If a transaction occurs with no active tax registration, `automatic_tax` silently collects 0 tax, with no error or warning.
- Sandbox transactions have no effect on threshold monitoring. Don’t infer live-mode threshold activity from sandbox activity.

## If jurisdictions are unknown

Don’t guess which jurisdictions apply or add a registration without confirmation that the business is registered with the tax authority. Ask where the business sells, direct the user to their tax advisor when needed, then help them record confirmed registrations with the [Tax Registrations API](https://docs.stripe.com/api/tax/registrations.md) or the Dashboard.

## If the region or tax type isn’t supported

Check the [supported countries list](https://docs.stripe.com/tax/supported-countries.md). If the jurisdiction isn’t listed, tell the user:

- Stripe Tax doesn’t support that region yet
- They can collect tax manually using `tax_rates` on the subscription or invoice instead (not alongside `automatic_tax`; you can’t use both)
- For unsupported tax types (customs duties, excise taxes), Stripe Tax doesn’t apply, so those are out of scope

Don’t attempt to approximate using a supported region as a proxy.

### references/treasury.md
# Treasury / Financial Accounts

## Table of contents

- v2 Financial Accounts API
- Legacy v1 Treasury

## v2 Financial Accounts API

For embedded financial accounts (bank accounts, account and routing numbers, money movement), use the [v2 Financial Accounts API](https://docs.stripe.com/api/v2/core/vault/financial-accounts.md) (`POST /v2/core/vault/financial_accounts`). This is required for new integrations.

For Treasury for platforms concepts and guides, see the [Treasury for platforms overview](https://docs.stripe.com/treasury/connect.md).

## Legacy v1 Treasury

Don’t use the [v1 Treasury Financial Accounts API](https://docs.stripe.com/api/treasury/financial_accounts.md) (`POST /v1/treasury/financial_accounts`) for new integrations. Existing v1 integrations continue to work.

