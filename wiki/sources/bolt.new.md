---
type: source
source_url: https://bolt.new/
companion_urls:
  - https://github.com/stackblitz/bolt.new
raw_files:
  - ../../raw/web/bolt.new.md
  - ../../raw/github/stackblitz-bolt.new.md
tags:
  - vibe-coding
  - full-stack-app-builder
  - webcontainers
  - bolt-cloud
  - github-sync
  - mcp-connectors
  - design-systems
  - browser-dev-environment
related:
  - lovable.dev
  - retool.com
  - the-new-sdlc-with-vibe-coding
  - producthunt.com
product: bolt
detail_level: standard
created: 2026-07-01
updated: 2026-07-01
---

Bolt is StackBlitz's hosted AI-powered full-stack app builder and browser-native development environment. It turns natural-language prompts into websites, web apps, and mobile-oriented projects, then keeps planning, coding, infrastructure setup, GitHub backup, collaboration, and publishing inside one surface. For this wiki it matters as a concrete commercial implementation of agentic app building that also exposes its underlying WebContainers-based open-source harness through a companion GitHub repo.

_All claims below are sourced from ../../raw/web/bolt.new.md unless otherwise noted._

## What it does

Bolt is positioned as an AI builder for websites, web apps, and mobile apps. Users can start from a natural-language prompt or import work from Figma, Google Stitch, GitHub, or Lovable, then continue iterating inside the same project. The product is aimed at both non-coders and experienced developers, with docs that frame it as useful for product managers, entrepreneurs, marketers, agencies, and students as well as full-stack engineers.

The hosted experience is broader than a one-shot code generator. The help-center docs describe a lifecycle that starts with planning, moves through iterative prompting and code edits, then ends in publishing via Bolt hosting or external deployment paths. Collaboration, project sharing, team templates, and branch-aware GitHub workflows are treated as first-class product features rather than afterthoughts.

## Key features

- **Selectable agents + planning mode** — users can switch between Standard and Max agents, and use Plan Mode before code changes to reason about architecture, debugging, APIs, and feature ideas.
- **Prompt scaffolding** — Bolt can enhance a first prompt, encourage app planning up front, and guide the user toward smaller iterative follow-up prompts.
- **Bolt Cloud** — built-in databases, hosting, domains, authentication, file storage, server functions, analytics, and Stripe-connected payments keep the common full-stack runtime inside the product.
- **Design-system-guided UI generation** — Bolt can build from pre-loaded or team-specific design systems so generated interfaces reflect real components and brand rules instead of generic placeholders.
- **GitHub + MCP connectivity** — GitHub provides backup, branching, import/export, and collaboration, while MCP connectors let Bolt pull context and actions from external tools such as Notion, Linear, and GitHub itself.
- **Open-source companion codebase** — the public repo shows the browser-resident harness that gives the agent direct control over the filesystem, package manager, terminal, server, and browser console. (../../raw/github/stackblitz-bolt.new.md)

## Architecture

The companion repo frames Bolt as a browser-native AI development agent built on StackBlitz WebContainers. Instead of sending code execution to a remote VM, the harness runs Node.js, package installs, dev servers, and file edits directly inside the browser tab while still exposing those capabilities to the model. The repo explicitly positions this environment control as the core differentiator versus assistants that only emit code suggestions. (../../raw/github/stackblitz-bolt.new.md)

At the implementation level, the open-source codebase is a Remix application with Vite-based build/dev flows and Cloudflare Pages/Workers deployment hooks. The fetched `package.json` exposes `dev`, `build`, `start`, `preview`, `test`, `typecheck`, `typegen`, and `deploy` scripts, while `load-context.ts` extends Remix's app context with typed Cloudflare platform bindings. The top-level tree is organized around `app/` for the UI/runtime, `functions/` for the Cloudflare Pages Function entrypoint, `public/` for static assets, and supporting config files such as `wrangler.toml`, `vite.config.ts`, and `uno.config.ts`. (../../raw/github/stackblitz-bolt.new.md)

The product docs add the hosted runtime picture around that harness. Bolt Cloud consolidates database provisioning, hosting, domains, auth, file storage, edge-style server functions, analytics, and payments so the AI can build against a managed backend surface without the user separately wiring infrastructure vendors together.

## Installation

The public repo is intended for builders who want to create their own Bolt-like tool rather than for end users of bolt.new itself. The setup path is: clone `stackblitz/bolt.new`, install dependencies with `pnpm install`, add an `ANTHROPIC_API_KEY` to `.env.local`, then run the Remix dev server. The contributing guide lists Node.js 20.15.1 and pnpm 9.4.0 as the recommended prerequisites. (../../raw/github/stackblitz-bolt.new.md)

```bash
git clone https://github.com/stackblitz/bolt.new.git
cd bolt.new
pnpm install
printf 'ANTHROPIC_API_KEY=XXX\\n' > .env.local
pnpm run dev
```
(../../raw/github/stackblitz-bolt.new.md)

## Example usage

For hosted-product users, the canonical flow is: describe the app, optionally refine the plan in Plan Mode, let Bolt scaffold and iterate on the code, then publish to a `bolt.host` site or connect GitHub / Netlify / Expo depending on the deployment target.

For builders reusing the open-source repo, the README and contributing guide position Bolt as a template for creating browser-based AI development tools powered by WebContainers, Remix, Cloudflare, and the AI SDK. In that model the repo itself is the example: prompt-driven full-stack app development where the agent can install packages, run servers, inspect the filesystem, and deploy from chat. (../../raw/github/stackblitz-bolt.new.md)

## When to use

Bolt fits when the goal is to move quickly from prompt to working full-stack product without leaving a hosted browser environment. It is especially strong when you want one product to cover planning, implementation, database setup, hosting, domains, GitHub backup, and external-tool context.

Compared with [[lovable.dev]], Bolt leans harder into the browser-native dev-environment story and the openly published WebContainers-based harness, while Lovable adds more explicit workspace-level skills, subagents, and Supabase-centric cloud framing. Compared with [[retool.com]], Bolt is aimed more at prompt-first product building across websites and apps, whereas Retool is more explicitly optimized for governed internal software, workflows, and enterprise data operations. It also serves as a product-side example of the shift from casual vibe coding toward more structured AI-assisted delivery described in [[the-new-sdlc-with-vibe-coding]].

## Maintenance status

The companion GitHub repo shows 16,430 stars, 14,675 forks, a `main` default branch, MIT license, and no tagged release returned by `gh release list` at ingest time. The most recent `pushedAt` value in repo metadata is 2024-12-17T06:29:27Z. The repo describes itself as a simple example app for building AI-powered software-development tools on WebContainers, so its maintenance signal should be read as the status of the public reference codebase rather than the full commercial hosted product documented on bolt.new and support.bolt.new. (../../raw/github/stackblitz-bolt.new.md)

## Ecosystem

Bolt sits in a dense integration ecosystem. The docs explicitly connect it to Expo for mobile-app packaging, Figma and Google Stitch for design import, GitHub for version control and collaboration, Netlify as an alternative deployment path, Stripe for payments, Supabase as an alternative database backend, and MCP servers for pulling context and actions from external tools.

The design-system support also gives Bolt an interesting overlap with other sources in this wiki: it shares the high-level prompt-to-product territory with [[lovable.dev]], overlaps with [[retool.com]] where governed app delivery meets AI generation, and intersects conceptually with design-oriented systems such as [[open-design.ai]] even though Bolt is primarily a hosted application builder rather than a local-first design runtime.

## Documentation

Bolt's Help Center is unusually comprehensive for a consumer-facing app builder. The docs index is organized around getting started, working in Bolt, design systems, Bolt Cloud, best practices, integrations, settings, troubleshooting, and reference material. The most relevant operator-facing guides captured at `standard` detail cover intro / first-project setup, Plan Mode, agent selection, MCP connectors, GitHub workflows, Bolt Cloud, databases, publishing, and design-system usage.
