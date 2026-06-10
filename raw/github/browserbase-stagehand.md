# browserbase/stagehand

## Metadata
- Stars: 23055
- Primary language: TypeScript
- Default branch: main
- Latest release: stagehand-server-v3/v3.7.2 (2026-06-09)
- License: MIT License
- Homepage: https://stagehand.dev
- Fetched: 2026-06-10
- Final URL: https://github.com/browserbase/stagehand

## Description
The SDK For Browser Agents

## README
The AI Browser Automation Framework. Read the Docs at https://docs.stagehand.dev

If you're looking for the Python implementation, you can find it at https://github.com/browserbase/stagehand-python

### What is Stagehand?

Stagehand is a browser automation framework used to control web browsers with natural language and code. By combining the power of AI with the precision of code, Stagehand makes web automation flexible, maintainable, and actually reliable.

### Why Stagehand?

Most existing browser automation tools either require you to write low-level code in a framework like Selenium, Playwright, or Puppeteer, or use high-level agents that can be unpredictable in production. By letting developers choose what to write in code vs. natural language (and bridging the gap between the two) Stagehand is the natural choice for browser automations in production.

1. **Choose when to write code vs. natural language**: use AI when you want to navigate unfamiliar pages, and use code when you know exactly what you want to do.
2. **Go from AI-driven to repeatable workflows**: Stagehand lets you preview AI actions before running them, and also helps you easily cache repeatable actions to save time and tokens.
3. **Write once, run forever**: Stagehand's auto-caching combined with self-healing remembers previous actions, runs without LLM inference, and knows when to involve AI whenever the website changes and your automation breaks.

### Getting Started

Start with Stagehand with one line of code, or check out the Quickstart Guide for more information:

```bash
npx create-browser-app
```

### Example

```typescript
// Stagehand's CDP engine provides an optimized, low level interface to the browser built for automation
const page = stagehand.context.pages()[0];
await page.goto("https://github.com/browserbase");

// Use act() to execute individual actions
await stagehand.act("click on the stagehand repo");

// Use agent() for multi-step tasks
const agent = stagehand.agent();
await agent.execute("Get to the latest PR");

// Use extract() to get structured data from the page
const { author, title } = await stagehand.extract(
  "extract the author and title of the PR",
  z.object({
    author: z.string().describe("The username of the PR author"),
    title: z.string().describe("The title of the PR"),
  }),
);
```

### Documentation

Visit https://docs.stagehand.dev to view the full documentation.

### Build and Run from Source

```bash
git clone https://github.com/browserbase/stagehand.git
cd stagehand
pnpm install
pnpm run build
pnpm run example
```

### Contributing

Focused on improving reliability, extensibility, speed, and cost in that order of priority. Bug fixes and small improvements are the best way to get started.

### License

Licensed under the MIT License. Copyright 2025 Browserbase, Inc.

## Top-level structure
```
packages/         — monorepo workspace (cli, core, docs, evals, server-v3)
README.md         — main readme
claude.md         — Claude agent instructions for the repo
CHANGELOG.md      — version history
.env.example      — environment variable template (API keys for LLM providers and Browserbase)
package.json      — root package config
pnpm-workspace.yaml — workspace definition
turbo.json        — Turborepo build pipeline
```

### Key packages
- `packages/core` — The main Stagehand SDK (TypeScript)
- `packages/cli` — `@browserbasehq/cli` CLI tool
- `packages/server-v3` — Stagehand server (latest: v3.7.2)
- `packages/evals` — evaluation suite
- `packages/docs` — documentation source
