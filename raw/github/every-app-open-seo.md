# every-app/open-seo

## Metadata
- Stars: 25694
- Forks: 3511
- Primary language: TypeScript
- Default branch: main
- Latest release: v0.1.21 (2026-10-30T08:24:42Z)
- License: MIT License
- Homepage: https://openseo.so
- Pushed: 2026-10-30T08:24:41Z
- Fetched: 2026-10-30
- Final URL: https://github.com/every-app/open-seo

## Description
Open source alternative to Semrush and Ahrefs

## README
# OpenSEO

> Open source alternative to Semrush and Ahrefs

OpenSEO is an SEO tool for _the people_. If tools like Semrush or Ahrefs are too expensive or bloated, OpenSEO is a pay-as-you-go alternative that you actually control.

> All-in-one SEO tool for you and your AI agent.

Connect with any agent like Claude Code, OpenClaw or Hermes. We have pre-built skills, but you can build your own to tailor OpenSEO to your needs.

<img width="100%" alt="openseo-keyword-research" src="https://github.com/user-attachments/assets/8ebdc439-3e72-41ab-8bde-8cda771ef2e8" />

## Hosted Version

Try OpenSEO for free on our website. If you want to support the project, a hosted subscription is $10/month.

[openseo.so](https://openseo.so)

### EveryApp

Host OpenSEO and other open source apps on our platform EveryApp.

[Self-host on EveryApp and give it a star →](https://github.com/every-app/every-app)

## Why use OpenSEO?

- Best in class MCP and AI Skills.
- Modern, simple UI.
  - Focused workflows instead of a bloated, complex SEO suite.
- No subscriptions.
  - Bring your own DataForSEO API key and pay only for what you use.
- Fork and vibe code your own custom tool.

## Main SEO Workflows

- Keyword research
- Rank tracking
- Competitor Insights
- Backlinks
- Site Audits
- AI Visibility

## OpenSEO MCP & Agent Skills

OpenSEO exposes an MCP server so AI agents like Claude Code, OpenClaw, and Hermes can use your SEO data directly. Agent Skills are reusable workflows that guide your agent through SEO tasks using the MCP.

- [Set up ChatGPT web or desktop](https://openseo.so/docs/chatgpt) (works on Free and paid ChatGPT plans)
- [Set up Codex](https://openseo.so/docs/codex-plugin)
- [Set up OpenSEO MCP](https://openseo.so/docs/mcp)
- [Set up OpenSEO Agent Skills](https://openseo.so/docs/skills/setup)

## Self-Hosting

OpenSEO supports two self-hosting paths. Both use email and password accounts: the first visitor creates the admin account, teammates join from invitation links, and MCP clients (Claude, ChatGPT, Codex, Cursor) sign in with the same accounts.

- **Docker** - On your own server or computer, with a prebuilt image that is ready in seconds. Works with Compose-based platforms such as Coolify, Portainer and Dokploy. See [`docs/SELF_HOSTING_DOCKER.md`](./docs/SELF_HOSTING_DOCKER.md).
  - Running the older single-container image? It keeps getting updates; [move to the new setup](./docs/SELF_HOSTING_DOCKER.md#move-from-the-old-docker-image) when you are ready, data included.
- **Cloudflare** - No server to run: one deploy command puts OpenSEO on your own Cloudflare account (works on the free plan). See [`docs/SELF_HOSTING_CLOUDFLARE.md`](./docs/SELF_HOSTING_CLOUDFLARE.md).

For security-conscious setups, two advanced options replace the accounts with your own network controls:

- **Cloudflare Access** in front of the Cloudflare deploy, so Cloudflare checks every request before it reaches OpenSEO. See [`docs/SELF_HOSTING_CLOUDFLARE.md`](./docs/SELF_HOSTING_CLOUDFLARE.md).
- **No sign-in on Docker**, behind Tailscale, a private network or your own authenticating proxy. See [Without sign-in](./docs/SELF_HOSTING_DOCKER.md#without-sign-in-advanced).

Either way, you need a DataForSEO API key to get SEO data. See [`docs/DATAFORSEO_API_KEY.md`](./docs/DATAFORSEO_API_KEY.md).

## Costs

OpenSEO needs a [DataForSEO](https://dataforseo.com/?aff=255379) API key so that you can get SEO data. You pay them directly when self hosting.

See [openseo.so/pricing](https://openseo.so/pricing)

When you self host, your costs will be slightly lower than the estimates on our website. The way the hosted service makes money is by charging 28% extra for every request we make to DataForSEO.

## Local Development

See [`docs/LOCAL_DEVELOPMENT.md`](./docs/LOCAL_DEVELOPMENT.md).

## Contributing

Creating clear issues is the best way to contribute.

Read more here: [`docs/CONTRIBUTING.md`](./docs/CONTRIBUTING.md)

We have this skill: `/simple-issue-description` which helps.

```sh
npx skills add every-app/open-seo --skill simple-issue-description
```

## Community

Join Discord to chat: [Discord](https://discord.gg/c9uGs3cFXr)

Follow along for updates:

- Follow on X: https://x.com/bensenescu
- Sign up for the mailing list on our website: [openseo.so](https://openseo.so)

## Docs
file	CONTRIBUTING.md	docs/CONTRIBUTING.md
file	DATAFORSEO_API_KEY.md	docs/DATAFORSEO_API_KEY.md
file	GOOGLE_MAPS_SETUP.md	docs/GOOGLE_MAPS_SETUP.md
file	LOCAL_DEVELOPMENT.md	docs/LOCAL_DEVELOPMENT.md
file	LOCAL_POSTGRES.md	docs/LOCAL_POSTGRES.md
file	SELF_HOSTING_CLOUDFLARE.md	docs/SELF_HOSTING_CLOUDFLARE.md
file	SELF_HOSTING_CLOUDFLARE_LEGACY.md	docs/SELF_HOSTING_CLOUDFLARE_LEGACY.md
file	SELF_HOSTING_CLOUDFLARE_OPERATIONS.md	docs/SELF_HOSTING_CLOUDFLARE_OPERATIONS.md
file	SELF_HOSTING_DOCKER.md	docs/SELF_HOSTING_DOCKER.md
file	SELF_HOSTING_DOCKER_LEGACY.md	docs/SELF_HOSTING_DOCKER_LEGACY.md
file	SELF_HOSTING_GOOGLE_ANALYTICS.md	docs/SELF_HOSTING_GOOGLE_ANALYTICS.md
file	SELF_HOSTING_GOOGLE_SEARCH_CONSOLE.md	docs/SELF_HOSTING_GOOGLE_SEARCH_CONSOLE.md
dir	maintainers	docs/maintainers
dir	release-notes	docs/release-notes

## Top-level structure
dir	.agents	.agents
dir	.claude-plugin	.claude-plugin
dir	.claude	.claude
dir	.cursor-plugin	.cursor-plugin
file	.env.example	.env.example
dir	.github	.github
file	.gitignore	.gitignore
file	.npmrc	.npmrc
dir	.oss-scanner	.oss-scanner
file	.oxlintrc.json	.oxlintrc.json
file	.prettierignore	.prettierignore
file	AGENTS.md	AGENTS.md
file	LICENSE	LICENSE
file	README.md	README.md
file	SECURITY.md	SECURITY.md
file	cloudflare.config.ts	cloudflare.config.ts
file	components.json	components.json
file	compose.yaml	compose.yaml
dir	deploy	deploy
dir	docs	docs
dir	drizzle	drizzle
file	everyapp.config.ts	everyapp.config.ts
file	knip.jsonc	knip.jsonc
file	package.json	package.json
dir	patches	patches
dir	plugins	plugins
file	pnpm-lock.yaml	pnpm-lock.yaml
file	pnpm-workspace.yaml	pnpm-workspace.yaml
dir	scripts	scripts
dir	specs	specs
dir	src	src
dir	tests	tests
file	tsconfig.json	tsconfig.json
file	tsconfig.report-widgets.json	tsconfig.report-widgets.json
file	vite-plugin-every-app.ts	vite-plugin-every-app.ts
file	vite-plugin-lean-worker-bundle.ts	vite-plugin-lean-worker-bundle.ts
file	vite-plugin-mcp-widgets.ts	vite-plugin-mcp-widgets.ts
file	vite.config.ts	vite.config.ts
file	vite.report-widgets.config.ts	vite.report-widgets.config.ts
dir	web	web
file	wrangler.audit.jsonc	wrangler.audit.jsonc
file	wrangler.jsonc	wrangler.jsonc
file	wrangler.standalone.json	wrangler.standalone.json

## Notable directories

### .claude-plugin/
file	marketplace.json	.claude-plugin/marketplace.json

### plugins/
dir	openseo	plugins/openseo
