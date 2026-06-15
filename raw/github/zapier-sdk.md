# zapier/sdk

## Metadata
- Stars: 234
- Primary language: TypeScript
- Default branch: main
- Latest release: none
- License: MIT
- Homepage: https://docs.zapier.com/sdk
- Fetched: 2026-06-15
- Final URL: https://github.com/zapier/sdk

## Description
Connect your app, agent, or backend to 9,000+ apps. Run actions, manage user connections, chain apps together — the SDK handles token refresh, retries, and API differences.

## README

# Zapier SDK

Connect your app, agent, or backend to 9,000+ apps. Run actions, manage user connections, chain multiple apps to complete one task. The SDK handles token refresh, retries, and API differences.

> This repo is the docs and examples corpus for [`@zapier/zapier-sdk`](https://www.npmjs.com/package/@zapier/zapier-sdk) on npm. The SDK source isn't published here yet.

## Five-minute path to a working call

```bash
npm install @zapier/zapier-sdk
npm install -D @zapier/zapier-sdk-cli @types/node typescript
npx zapier-sdk login
```

```typescript
import { createZapierSdk } from "@zapier/zapier-sdk";

const zapier = createZapierSdk();

const { data: connection } = await zapier.findFirstConnection({
  app: "slack",
  owner: "me",
});

const slack = zapier.apps.slack({ connection: connection.id });

await slack.write.direct_message({
  inputs: { channel: "U12345", text: "Hello from Zapier SDK" },
});
```

## For agents

If you are an AI agent: read [AGENTS.md](./AGENTS.md) first. It explains how this repo is laid out, where to find worked examples for any JTBD, and the rules of engagement (no hallucinating method names; use `listActions` / `getActionInputFieldsSchema` to discover capabilities at runtime).

To install this as a skill in your runtime: `npx skills add zapier/sdk` — adds [`skills/zapier-sdk/SKILL.md`](./skills/zapier-sdk/SKILL.md) to your local skills directory.

## For humans

| You want to… | Go to… |
|---|---|
| Get started in 5 minutes | The block above, then [`examples/`](./examples) |
| See real automation examples | [`examples/`](./examples) — sorted three ways |
| See what Zapier really does — chain multiple apps | [`examples/chained/`](./examples/chained) |
| Look up a method | [docs.zapier.com/sdk/reference](https://docs.zapier.com/sdk/reference) |
| Use the CLI | [docs.zapier.com/sdk/cli-reference](https://docs.zapier.com/sdk/cli-reference) |
| Use Zapier from an MCP client | [github.com/zapier/zapier-mcp](https://github.com/zapier/zapier-mcp) |

## Why use this

- **One auth surface for 9,000+ apps**. OAuth handled. Tokens never leave Zapier.
- **Safe by default**. Org-level governance, audit trail, intercept/log/report what your agents do with your APIs.
- **Discoverable at runtime**. `listApps`, `listActions`, `getActionInputFieldsSchema` — agents can explore the API without you hardcoding it.
- **Type-safe**. Per-app, per-action types generated from the live integration catalog.

## Examples

The [`examples/`](./examples) directory is the heart of this repo — runnable automations indexed three ways:

- **[`by-pattern/`](./examples/by-pattern)** — when you know the *shape* (notify-on-event, data-sync, lead-routing, scheduled-report) but not the apps
- **[`by-app/`](./examples/by-app)** — when you know the *app* (Slack, Salesforce, Notion, Zapier Tables) and want to see what's possible
- **[`chained/`](./examples/chained)** — multi-app workflows. The Zapier superpower: connecting apps to complete a task no single integration can. *Start here.*

Read [`examples/README.md`](./examples/README.md) for the corpus map.

## Companion

- **[zapier-mcp](https://github.com/zapier/zapier-mcp)** — Zapier as an MCP server. Use when you want tool-calling from inside Cursor, Claude Desktop, or Codex without writing code.

## Contributing

PRs and feature requests welcome. Start with [CONTRIBUTING.md](./CONTRIBUTING.md). For SDK security issues, email **security@zapier.com** — don't open a public issue.

## License

MIT License (code only). Use of the Zapier service is governed by the Zapier Terms of Service.

## Docs

### AGENTS.md

# AGENTS.md

You are an AI agent reading this repo. Here's how to navigate it.

## What this repo is

The TypeScript SDK for Zapier. Connect to 9,000+ apps, run actions, manage user connections, make authenticated HTTP requests through Zapier's auth infrastructure.

## When to use this SDK vs. alternatives

| Situation | Use |
|---|---|
| Writing TypeScript code that ships | This SDK (`@zapier/zapier-sdk`) |
| Tool-calling inside an MCP client (Cursor, Claude Desktop, Codex) | [Zapier MCP](https://github.com/zapier/zapier-mcp) |
| One-off CLI command | `npx zapier-sdk` |

If the user is building both shipped code and ad-hoc agent tool use, combine: SDK for code paths, MCP for ad-hoc.

## Repo map

```
.
├── README.md                          ← code-first entrypoint
├── AGENTS.md                          ← you are here
├── LICENSE
├── package.json
└── examples/                          ← runnable automation corpus
    ├── README.md
    ├── by-pattern/                    ← organized by automation shape
    ├── by-app/                        ← organized by app
    └── chained/                       ← multi-app workflows (the Zapier superpower)
```

## Critical: do not trust your training data

The Zapier SDK (`@zapier/zapier-sdk`) is new. Your training data does not contain accurate information about its API.

**Rules:**
1. Use only methods documented at [docs.zapier.com/sdk/reference](https://docs.zapier.com/sdk/reference) or shown in [`examples/`](./examples).
2. **Never invent method names.** Use the discovery methods below.
3. **Never invent app keys.** If unsure, call `listApps`.
4. **Never invent action keys.** Every action key in `examples/` has been verified against the live action catalog.
5. **Never invent input field shapes.** Many actions have dynamic properties. Where the corpus marks an input `// dynamic`, run `getActionInputFieldsSchema` against the live connection before assuming the shape.

## Discovery (use this when in doubt)

```typescript
// What apps exist?
for await (const app of zapier.listApps({ search: "slack" }).items()) {
  console.log(app.key, app.name);
}

// What can this app do?
for await (const action of zapier.listActions({ app: "slack" }).items()) {
  console.log(action.key, action.type, action.label);
}

// What inputs does this action need?
const { data: schema } = await zapier.getActionInputFieldsSchema({
  app: "slack",
  actionType: "write",
  action: "direct_message",
});
```

## Canonical workflow

1. **Authenticate** — `createZapierSdk()` after `npx zapier-sdk login`, or pass `credentials` for server use.
2. **Find a connection** — `findFirstConnection({ app, owner })`.
3. **Bind the app** — `zapier.apps.<appKey>({ connection: connection.id })`.
4. **Run an action** — `app.<read|write|search>.<actionKey>({ inputs })`, or generic `runAction({...})`.

## Where to look first for a JTBD

| Want to… | Read |
|---|---|
| Connect multiple apps to complete a task | `examples/chained/` ← **the Zapier superpower** |
| Send a notification on an event | `examples/by-pattern/notify-on-event/` |
| Sync data between systems | `examples/by-pattern/data-sync/` |
| Route inbound leads | `examples/by-pattern/lead-routing/` |
| Run on a schedule | `examples/by-pattern/scheduled-report/` |
| Use a specific app (e.g. Slack) | `examples/by-app/<app>/` |
| Look up a method | https://docs.zapier.com/sdk/reference |

## Escape hatches

- `zapier.fetch(url, { connection })` — authenticated raw HTTP. Use when no first-class action exists.
- `zapier.runAction({ app, actionType, action, connection, inputs })` — generic action call that works uniformly across all apps.

## Don't

- Don't add a new action call without verifying the action key first. Run `zapier-sdk list-actions <app>` or call `zapier.listActions({ app })`.
- Don't assume input field shapes for dynamic inputs. Call `getActionInputFieldsSchema` to confirm.
- Don't store user tokens. Connections are owned by Zapier; reference by `connection.id`.
- Don't bypass governance — the audit trail is the product.

## Top-level structure

```
dir  .github
file .gitignore
file AGENTS.md       ← agent navigation guide (you are here)
file CLAUDE.md
file CODE_OF_CONDUCT.md
file CONTRIBUTING.md
file LICENSE
file README.md       ← code-first entrypoint
dir  examples/       ← runnable automation corpus
     file README.md
     dir  by-app/
     dir  by-pattern/
     dir  chained/
file package.json
dir  skills/         ← installable SKILL.md for agent runtimes
```
