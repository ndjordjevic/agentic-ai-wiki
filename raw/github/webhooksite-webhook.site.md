# webhooksite/webhook.site

## Metadata
- Stars: 6602
- Primary language: JavaScript
- Default branch: master
- Latest release: 1.3 — "Version 1.3 – LTS" (2023-06-21)
- License: Other (repo LICENSE file; README states the self-hosted version is MIT-licensed)
- Homepage: https://webhook.site
- Fetched: 2026-06-10
- Final URL: https://github.com/webhooksite/webhook.site

## Description
⚓️ Easily test HTTP webhooks with this handy tool that displays requests instantly.

## README
# [Webhook.site](https://webhook.site)

![Docker Pulls](https://img.shields.io/docker/pulls/webhooksite/webhook.site)
[![GitHub last commit](https://img.shields.io/github/last-commit/fredsted/webhook.site.svg)](https://github.com/fredsted/webhook.site/commits/master)

With [Webhook.site](https://webhook.site), you instantly get a unique, random URL that you can use to test and debug Webhooks and HTTP requests, as well as to create your own workflows using the Custom Actions graphical editor or WebhookScript, a simple scripting language, to transform, validate and process HTTP requests.

## What are people using it for?

* Receive Webhooks without needing an internet-facing Web server
* Send Webhooks to a server that’s behind a firewall or private subnet
* Transforming Webhooks into other formats, and re-sending them to different systems
* Connect different APIs that aren’t compatible
* Building contact forms that send emails
* Instantly build APIs without needing infrastructure

Built by Simon Fredsted ([@fredsted](https://x.com/fredsted).

## Open Source

There are two versions of Webhook.site:

* The completely open-source, MIT-licensed version is available on Github, which can be self-hosted using e.g. Docker, is great for testing Webhooks, but doesn’t include features like Custom Actions.

* The cloud version at [https://webhook.site](https://webhook.site) which has more features, some of them requiring a paid subscription.

## Acknowledgements

* The app was built with [Laravel](https://laravel.com) for the API and Angular.js for the frontend SPA.
* WebhookScript based on [Primi](https://github.com/smuuf/Primi) Copyright (c) Přemysl Karbula.
* The WebhookScript editor is using the [Ace](https://ace.c9.io/).
* JSONPath extraction provided by [FlowCommunications](https://github.com/FlowCommunications/JSONPath).
* This documentation site uses [Just the Docs](https://github.com/pmarsceill/just-the-docs), a documentation theme for Jekyll.

**[Full Documentation at docs.webhook.site](https://docs.webhook.site)**

## Top-level structure
- `app/` — Laravel application code (API backend)
- `bootstrap/`, `config/`, `database/`, `storage/` — standard Laravel framework directories
- `resources/` — frontend resources (Angular.js SPA)
- `public/` — web root
- `tests/`, `phpunit.xml` — PHP test suite
- `helm/` — Helm chart for Kubernetes deployment
- `Dockerfile`, `docker-compose.yml`, `.dockerignore`, `nginx.conf` — Docker/self-hosting setup
- `laravel-echo-server.json.example` — websocket server config example (live request updates)
- `composer.json` / `composer.lock` — PHP dependencies
- `package.json` / `package-lock.json`, `gulpfile.js` — JS dependencies and build
- `artisan`, `server.php` — Laravel entry points
- `LICENSE`, `SECURITY.md`, `readme.md` — project meta
- `webhook-paw.paw` — Paw (HTTP client) project file
- No `docs/` or `examples/` directories — documentation lives in the separate `webhooksite/docs` repo, published at docs.webhook.site
