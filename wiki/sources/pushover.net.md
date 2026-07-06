---
type: source
source_url: https://pushover.net/
tags: [push-notifications, rest-api, mobile-alerts, ios-notifications, android-notifications, priority-alerts, webhook-integration]
related: [happy.engineering, marketstack.com]
product: pushover
detail_level: standard
created: 2026-07-06
updated: 2026-07-06
---

Pushover is a hosted push-notification service: any script, server, or third-party integration sends a simple HTTP request and Pushover fans it out to a user's registered Android, iOS, and desktop clients. For agentic workflows it is a lightweight way to alert a human when a long-running agent needs input, hits an error, or finishes a task — the same "ping me on my phone" pattern seen in [[happy.engineering]], but as a standalone, single-purpose notification backend rather than a full mobile Claude Code client.

_All claims below are sourced from ../../raw/web/pushover.net.md unless otherwise noted._

## What it does

Pushover accepts a POST request containing an application token, a user key, and a message, then delivers it as a push notification to every device the user has registered. Responses are available in JSON or XML. No OAuth or session handling is required — plain HTTP requests work directly from shell scripts, cron jobs, or backend services.

## Key features

- **Simple three-parameter API** — `token`, `user`, `message` are the only required fields to send a notification to `https://api.pushover.net/1/messages.json`.
- **Message formatting** — HTML tags (bold, italics, underline, colored text, links) via `html=1`, or monospace via `monospace=1`.
- **Priority levels** — range from -2 (lowest, silent) to 2 (emergency); emergency priority requires `retry` and `expire` parameters and keeps re-notifying until the user acknowledges it.
- **Attachments** — a single image per message, up to 5MB, sent via `multipart/form-data` or Base64 encoding.
- **Rate limits** — 10,000 messages/month on free individual accounts, 25,000/month for Pushover for Teams; exceeding the limit returns HTTP 429.

## Architecture and concepts

Delivery uses native push channels under the hood — Google's push service on Android, Apple's APNs on iOS — rather than polling, so the client apps avoid battery drain. The desktop client runs in Chrome, Firefox, or Safari and, on macOS, can deliver notifications without a browser open. A device can also expose Watch-face style live values via the separate Glances API.

## Main APIs

- `POST https://api.pushover.net/1/messages.json` — send a message; minimum parameters `token`, `user`, `message`.
- Success returns HTTP 200 with `{"status":1}`; failures return a 4xx status with an `errors` array describing what was invalid.

## When to use

Pushover fits any workflow — agentic or otherwise — that needs a dead-simple, cross-platform "notify a human" primitive without building push infrastructure: CI/CD alerts, monitoring/alerting pipelines, or an agent signaling that it needs a decision or has finished a job. It is not a two-way messaging or chat platform — delivery is one-directional from the integration to the user's devices, with only basic acknowledgment support for emergency-priority messages.

## Ecosystem

Client apps exist for Android, iOS/iPadOS (including Apple Watch and Watch face complications), and desktop browsers, all bundled behind one API token/user-key pair. "Pushover for Teams" adds per-organization billing and user management for shared alerting across a team. Support and FAQ content is hosted separately at support.pushover.net, organized into categories covering common problems, API/integration, licensing, platform-specific clients, and an email-to-notification gateway.
