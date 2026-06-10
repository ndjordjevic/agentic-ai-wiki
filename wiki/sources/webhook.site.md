---
type: source
source_url: https://webhook.site/
companion_urls:
  - https://github.com/webhooksite/webhook.site
raw_files:
  - ../../raw/web/webhook.site.md
  - ../../raw/github/webhooksite-webhook.site.md
tags:
  - webhook-testing
  - http-inspection
  - workflow-automation
  - custom-actions
  - local-tunneling
  - email-hooks
  - dns-hooks
  - api-mocking
related:
  - resend.com
  - ngrok.com
product: webhook.site
detail_level: standard
created: 2026-06-10
updated: 2026-06-10

---

Webhook.site is a webhook testing and workflow-automation service: every visitor instantly gets a free, unique URL, e-mail address, and DNS name (DNSHook), and everything sent to those addresses is displayed in real time — headers, query strings, form values, files, and request metadata. On top of the inspection tool, paid tiers add Custom Actions (a visual/scripted workflow builder with 50+ action types that run in the cloud on each incoming request), Schedules (cron jobs), a PostgreSQL-compatible Database, and a CLI (`whcli`) that tunnels requests to localhost in the style of ngrok. For agentic stacks it serves as zero-infrastructure plumbing: a place to receive, inspect, transform, mock, and forward HTTP, email, and DNS traffic without running a server. The platform positions itself explicitly as an alternative to Zapier, Ngrok, Localtunnel, and Pipedream, and the core request-inspection app is open source.

_All claims below are sourced from ../../raw/web/webhook.site.md unless otherwise noted._

## What it does

Webhook.site generates a unique random URL (`https://webhook.site/<uuid>`, also reachable as a subdomain), an e-mail address (`<uuid>@emailhook.site`), and a wildcard DNS name (`*.<uuid>.dnshook.site`) per session. Anything sent there appears instantly in the web UI. Free URLs are anonymous, expire after 7 days, and accept a maximum of ~50–100 requests; paid URLs never expire, are protected by login, and keep the latest 10,000 requests (data purged after at most 365 days, configurable down to zero stored requests for strict data-protection requirements). A "Token" is the API name for one such URL/address container. Each URL's default response (status, content type, body, timeout, CORS headers) is fully configurable, which makes it usable as an instant API or mock endpoint — including a Mock action that turns an uploaded OpenAPI/Swagger spec into an automatic mock server. Common uses include receiving webhooks without an internet-facing server, sending webhooks to machines behind firewalls, transforming webhooks between formats, connecting incompatible APIs, building contact forms that send email, and acting as a logging proxy/gateway.

## Key features

- **Request inspection** — live view of every HTTP request, email, or DNS query with headers, body, files, IP, and timestamps; CSV export, search queries, and Share Links (whitelabel read-only access)
- **Custom Actions** — chained workflow steps executed in the cloud per request: text extraction (Extract JSON/JSONPath/Regex/XPath), HTTP Request (forward mode), Send Email/SMTP, SSH/SFTP/FTP, Database Query, Conditions, variables, JavaScript and WebhookScript scripting, image resize, PDF generation, plus native integrations for Google Sheets, Excel, OneDrive, S3, CloudFront, Discord, Slack, Dropbox, HubSpot, X/Twitter, push notifications (Pushed, ntfy.sh), and RabbitMQ; an "Action AI" generator builds action chains from a prompt
- **Workflow control flow** — Conditions, repeating actions (loop over up to 100 items), queued/asynchronous actions (up to 120 s, 300 s on Enterprise), Templates with predefined variables, Replay over historical requests, and an Error Log with failure notifications
- **Schedules** — cron-style or preset intervals (1 min to monthly, UTC) that hit any URL with custom method/headers; usable for uptime/SSL monitoring with response-body and status-code requirements
- **Databases** — built-in PostgreSQL-compatible database (CockroachDB under the hood) queried from Custom Actions or the API; a free `DB-S` instance ships with Pro/Enterprise plans
- **DNSHook** — logs all DNS lookups to a unique name and its subdomains; data can be smuggled via base64-encoded subdomains, used as a canary token, and dynamic A/CNAME/TXT responses can be returned via JSON
- **CLI (`whcli`)** — forwards Webhook.site traffic to localhost over an auto-reconnecting WebSocket; bidirectional proxying, URL merging, `exec` mode that runs shell commands per request with variable substitution (../../raw/github/webhooksite-webhook.site.md)
- **REST API** — full token/request management (create/update/delete tokens with `default_status`, `expiry`, `request_limit`, `alias`, `clone_from`, etc.), search-query request retrieval and bulk deletion, API-key auth; rate limits 10/min free, 60/min paid
- **Enterprise** — multi-user with roles and SSO (Google Workspace, Microsoft Entra), custom domains, white-label sharing

## Architecture

The cloud platform is a Laravel (PHP) API with an Angular.js single-page frontend; live request updates are pushed via laravel-echo-server WebSockets. The repository ships a Dockerfile, docker-compose setup, nginx config, and a Helm chart for Kubernetes self-hosting. (../../raw/github/webhooksite-webhook.site.md)

WebhookScript, the platform's built-in scripting language for Custom Actions, is based on the Primi scripting language, with JSONPath extraction provided by the FlowCommunications JSONPath library. (../../raw/github/webhooksite-webhook.site.md)

Custom Actions execute in a chain per incoming request, exchanging variables (`$request.query.x$`, with modifiers like `.json` for escaping) between steps; queued actions branch into an asynchronous background queue that inherits the execution scope up to that point. The CLI listens over a persistent WebSocket rather than polling, and Schedules run from the cloud against any URL. Two open-source versions exist: the MIT-licensed self-hostable core (request inspection only, no Custom Actions) and the full cloud product at webhook.site.

## Installation

The hosted service needs no installation — visiting webhook.site issues a URL immediately. The CLI installs via Docker (`docker run -ti webhooksite/cli -- whcli help`) or npm (`npm install -g @webhooksite/cli`, Node 14+). Self-hosting the open-source core uses the repo's Docker/docker-compose or Helm artifacts. (../../raw/github/webhooksite-webhook.site.md)

## Example usage

```bash
# Tunnel incoming webhooks to a local dev server (ngrok-style)
whcli forward \
  --token=1e25c1cb-e4d4-4399-a267-cd2cf1a6c864 \
  --api-key=ef6ef2f8-3e48-4f77-a54c-3891dc11c05c \
  --target=https://localhost:8080

# Run a shell command for every incoming request
whcli exec --token=<uuid> --command='ping $request.ip$'

# Create a URL/token via the API
curl -X POST https://webhook.site/token \
  -d '{"default_content": "Hello world!", "alias": "my-webhook", "actions": true}'
```
(../../raw/github/webhooksite-webhook.site.md)

## When to use

Reach for Webhook.site when you need to see exactly what an external system sends — debugging webhook integrations, capturing callbacks from third-party APIs, or testing email/DNS delivery — without standing up infrastructure. It also covers lightweight production automation: the operator-facing pitch is building workflows (receive → extract → transform → forward/store/notify) "without needing to hire a programmer or pay for and set up servers," with auto-deletion controls for data-protection compliance. The docs position it directly as an alternative to Zapier (workflow automation), Ngrok/Localtunnel (local tunnels via the CLI), and Pipedream. For agent development specifically, it is a quick way to give an agent an inspectable HTTP/email endpoint, mock an API from an OpenAPI spec, or bridge incompatible services.

## Maintenance status

The open-source repository (`webhooksite/webhook.site`) has 6,602 stars, 521 forks, JavaScript/PHP codebase, last pushed 2026-05-07; the latest tagged release is 1.3 LTS (2023-06-21) — cloud development continues ahead of the open-source LTS core. The cloud service reports 400,000 monthly users, 3,000 subscribed customers, 700 million HTTP requests/day, and 150,000 Custom Actions automations (November 2025), operated by Webhook ApS, a Danish corporation, since 2020. Paid plans start at $7.5/month. (../../raw/github/webhooksite-webhook.site.md)

## Ecosystem

The platform spans several companion properties: docs.webhook.site (documentation, built from the open `webhooksite/docs` repo), the MIT-licensed `webhooksite/cli` repo, support.webhook.site, and the emailhook.site / dnshook.site capture domains. Custom Actions integrate natively with Google Sheets, Microsoft Excel/OneDrive, AWS S3/CloudFront, Discord, Slack, Dropbox, HubSpot, X/Twitter, Pushed, ntfy.sh, and RabbitMQ. In this wiki it complements [[resend.com]]: Resend covers the outbound transactional-email path (and suggests tunnel tools for local webhook testing), while Webhook.site covers the inbound side — receiving, inspecting, and forwarding webhooks and email during development.
