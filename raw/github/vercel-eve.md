# vercel/eve

## Metadata
- Stars: 3916
- Primary language: TypeScript
- Default branch: main
- Latest release: eve@0.26.1 (2026-07-20T22:46:23Z)
- License: Apache License 2.0
- Homepage: https://eve.dev
- Fetched: 2026-07-21
- Final URL: https://github.com/vercel/eve

## Description
The Framework for Building Agents

## README
<div align="center">
  <a href="https://github.com/vercel/eve">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset=".github/assets/eve.svg">
      <img alt="eve logo" src=".github/assets/eve.svg" height="128">
    </picture>
  </a>
  <h1>eve</h1>
</div>

eve is a filesystem-first framework for durable AI agents. Core agent capabilities live in conventional locations, so projects are easier to inspect, extend, and operate.

### Quick start
```bash
npx eve@latest init my-agent
```

### Minimal structure
```text
my-agent/
└── agent/
    ├── agent.ts            # Optional: model and runtime config
    ├── instructions.md     # Required: the always-on system prompt
    ├── tools/              # Optional: typed functions the model can call
    ├── skills/             # Optional: procedures loaded on demand
    ├── channels/           # Optional: message channels
    └── schedules/          # Optional: recurring cron jobs
```

### Minimal model config
```ts
import { defineAgent } from "eve";

export default defineAgent({
  model: "anthropic/claude-sonnet-5",
});
```

## Docs
### AGENTS.md
- Canonical project guidance uses lowercase `eve` in user-facing text.
- Repo layout centers `packages/eve`, docs, fixtures, and integration apps.
- Developer workflow emphasizes lint/typecheck/unit-first validation.

### docs/introduction.mdx
- Defines the filesystem-first authoring model and durable session execution.
- Documents how folders map to capabilities (`tools`, `skills`, `channels`, `connections`, `sandbox`, `subagents`, `schedules`).

### docs/getting-started.mdx
- Covers scaffold path (`npx eve@latest init`) and manual install (`npm install eve ai zod`).
- Documents HTTP session API and stream/continuation flow.

### docs/connections/mcp.mdx
- Specifies MCP connection authoring (`defineMcpClientConnection`) and auth models (Connect OAuth vs static token).
- Covers allow/block tool filters and approval gating for high-risk actions.

### docs/evals/overview.mdx
- Defines `defineEval` and `defineEvalConfig` testing flow.
- Explains deterministic fixtures, assertion surfaces, and `eve eval` CLI.

### docs/channels/overview.mdx
- Describes channel contract and default HTTP channel behavior.
- Lists built-in platform channels and custom `defineChannel` path.

## Top-level structure
- `.changeset/` — release/versioning metadata
- `.github/` — CI and repository automation
- `apps/` — framework integrations, templates, docs app, and fixtures
- `docs/` — published framework documentation source
- `e2e/` — end-to-end eval/test assets
- `packages/` — core framework packages (`eve`, catalog)
- `research/` — issue-backed research/planning docs
- `scripts/` — repo utility and guard scripts
- `skills/` — official skills collection for eve ecosystem
- `package.json` / `pnpm-workspace.yaml` / `turbo.json` — monorepo orchestration
