# stackblitz/bolt.new

## Metadata
- Stars: 16430
- Primary language: TypeScript
- Default branch: main
- Latest release: none
- License: MIT License
- Homepage: https://bolt.new
- Fetched: 2026-07-01
- Final URL: https://github.com/stackblitz/bolt.new

## Description
Prompt, run, edit, and deploy full-stack web applications. -- bolt.new -- Help Center: https://support.bolt.new/ -- Community Support: https://discord.com/invite/stackblitz

## README
[![Bolt.new: AI-Powered Full-Stack Web Development in the Browser](./public/social_preview_index.jpg)](https://bolt.new)

# Bolt.new: AI-Powered Full-Stack Web Development in the Browser

Bolt.new is an AI-powered web development agent that allows you to prompt, run, edit, and deploy full-stack applications directly from your browser—no local setup required. If you're here to build your own AI-powered web dev agent using the Bolt open source codebase, [click here to get started!](./CONTRIBUTING.md)

## What Makes Bolt.new Different

Claude, v0, etc are incredible- but you can't install packages, run backends or edit code. That’s where Bolt.new stands out:

- **Full-Stack in the Browser**: Bolt.new integrates cutting-edge AI models with an in-browser development environment powered by **StackBlitz’s WebContainers**. This allows you to:
  - Install and run npm tools and libraries (like Vite, Next.js, and more)
  - Run Node.js servers
  - Interact with third-party APIs
  - Deploy to production from chat
  - Share your work via a URL

- **AI with Environment Control**: Unlike traditional dev environments where the AI can only assist in code generation, Bolt.new gives AI models **complete control** over the entire  environment including the filesystem, node server, package manager, terminal, and browser console. This empowers AI agents to handle the entire app lifecycle—from creation to deployment.

Whether you’re an experienced developer, a PM or designer, Bolt.new allows you to build production-grade full-stack applications with ease.

For developers interested in building their own AI-powered development tools with WebContainers, check out the open-source Bolt codebase in this repo!

## Tips and Tricks

Here are some tips to get the most out of Bolt.new:

- **Be specific about your stack**: If you want to use specific frameworks or libraries (like Astro, Tailwind, ShadCN, or any other popular JavaScript framework), mention them in your initial prompt to ensure Bolt scaffolds the project accordingly.

- **Use the enhance prompt icon**: Before sending your prompt, try clicking the 'enhance' icon to have the AI model help you refine your prompt, then edit the results before submitting.

- **Scaffold the basics first, then add features**: Make sure the basic structure of your application is in place before diving into more advanced functionality. This helps Bolt understand the foundation of your project and ensure everything is wired up right before building out more advanced functionality.

- **Batch simple instructions**: Save time by combining simple instructions into one message. For example, you can ask Bolt to change the color scheme, add mobile responsiveness, and restart the dev server, all in one go saving you time and reducing API credit consumption significantly.

## FAQs

**Where do I sign up for a paid plan?**  
Bolt.new is free to get started. If you need more AI tokens or want private projects, you can purchase a paid subscription in your [Bolt.new](https://bolt.new) settings, in the lower-left hand corner of the application. 

**What happens if I hit the free usage limit?**  
Once your free daily token limit is reached, AI interactions are paused until the next day or until you upgrade your plan.

**Is Bolt in beta?**  
Yes, Bolt.new is in beta, and we are actively improving it based on feedback.

**How can I report Bolt.new issues?**  
Check out the [Issues section](https://github.com/stackblitz/bolt.new/issues) to report an issue or request a new feature. Please use the search feature to check if someone else has already submitted the same issue/request.

**What frameworks/libraries currently work on Bolt?**  
Bolt.new supports most popular JavaScript frameworks and libraries. If it runs on StackBlitz, it will run on Bolt.new as well.

**How can I add make sure my framework/project works well in bolt?**  
We are excited to work with the JavaScript ecosystem to improve functionality in Bolt. Reach out to us via [hello@stackblitz.com](mailto:hello@stackblitz.com) to discuss how we can partner!

## Docs
### CONTRIBUTING.md
[![Bolt Open Source Codebase](./public/social_preview_index.jpg)](https://bolt.new)

> Welcome to the **Bolt** open-source codebase! This repo contains a simple example app using the core components from bolt.new to help you get started building **AI-powered software development tools** powered by StackBlitz’s **WebContainer API**.

### Why Build with Bolt + WebContainer API

By building with the Bolt + WebContainer API you can create browser-based applications that let users **prompt, run, edit, and deploy** full-stack web apps directly in the browser, without the need for virtual machines. With WebContainer API, you can build apps that give AI direct access and full control over a **Node.js server**, **filesystem**, **package manager** and **dev terminal** inside your users browser tab. This powerful combination allows you to create a new class of development tools that support all major JavaScript libraries and Node packages right out of the box, all without remote environments or local installs.

### What’s the Difference Between Bolt (This Repo) and [Bolt.new](https://bolt.new)?

- **Bolt.new**: This is the **commercial product** from StackBlitz—a hosted, browser-based AI development tool that enables users to prompt, run, edit, and deploy full-stack web applications directly in the browser. Built on top of the [Bolt open-source repo](https://github.com/stackblitz/bolt.new) and powered by the StackBlitz **WebContainer API**.

- **Bolt (This Repo)**: This open-source repository provides the core components used to make **Bolt.new**. This repo contains the UI interface for Bolt as well as the server components, built using [Remix Run](https://remix.run/). By leveraging this repo and StackBlitz’s **WebContainer API**, you can create your own AI-powered development tools and full-stack applications that run entirely in the browser.

# Get Started Building with Bolt

Bolt combines the capabilities of AI with sandboxed development environments to create a collaborative experience where code can be developed by the assistant and the programmer together. Bolt combines [WebContainer API](https://webcontainers.io/api) with [Claude Sonnet 3.5](https://www.anthropic.com/news/claude-3-5-sonnet) using [Remix](https://remix.run/) and the [AI SDK](https://sdk.vercel.ai/).

### WebContainer API

Bolt uses [WebContainers](https://webcontainers.io/) to run generated code in the browser. WebContainers provide Bolt with a full-stack sandbox environment using [WebContainer API](https://webcontainers.io/api). WebContainers run full-stack applications directly in the browser without the cost and security concerns of cloud hosted AI agents. WebContainers are interactive and editable, and enables Bolt's AI to run code and understand any changes from the user.

The [WebContainer API](https://webcontainers.io) is free for personal and open source usage. If you're building an application for commercial usage, you can learn more about our [WebContainer API commercial usage pricing here](https://stackblitz.com/pricing#webcontainer-api).

### Remix App

Bolt is built with [Remix](https://remix.run/) and
deployed using [CloudFlare Pages](https://pages.cloudflare.com/) and
[CloudFlare Workers](https://workers.cloudflare.com/).

### AI SDK Integration

Bolt uses the [AI SDK](https://github.com/vercel/ai) to integrate with AI
models. At this time, Bolt supports using Anthropic's Claude Sonnet 3.5.
You can get an API key from the [Anthropic API Console](https://console.anthropic.com/) to use with Bolt.
Take a look at how [Bolt uses the AI SDK](https://github.com/stackblitz/bolt.new/tree/main/app/lib/.server/llm)

## Prerequisites

Before you begin, ensure you have the following installed:

- Node.js (v20.15.1)
- pnpm (v9.4.0)

## Setup

1. Clone the repository (if you haven't already):

```bash
git clone https://github.com/stackblitz/bolt.new.git
```

2. Install dependencies:

```bash
pnpm install
```

3. Create a `.env.local` file in the root directory and add your Anthropic API key:

```
ANTHROPIC_API_KEY=XXX
```

Optionally, you can set the debug level:

```
VITE_LOG_LEVEL=debug
```

**Important**: Never commit your `.env.local` file to version control. It's already included in .gitignore.

## Available Scripts

- `pnpm run dev`: Starts the development server.
- `pnpm run build`: Builds the project.
- `pnpm run start`: Runs the built application locally using Wrangler Pages. This script uses `bindings.sh` to set up necessary bindings so you don't have to duplicate environment variables.
- `pnpm run preview`: Builds the project and then starts it locally, useful for testing the production build. Note, HTTP streaming currently doesn't work as expected with `wrangler pages dev`.
- `pnpm test`: Runs the test suite using Vitest.
- `pnpm run typecheck`: Runs TypeScript type checking.
- `pnpm run typegen`: Generates TypeScript types using Wrangler.
- `pnpm run deploy`: Builds the project and deploys it to Cloudflare Pages.

## Development

To start the development server:

```bash
pnpm run dev
```

This will start the Remix Vite development server.

## Testing

Run the test suite with:

```bash
pnpm test
```

## Deployment

To deploy the application to Cloudflare Pages:

```bash
pnpm run deploy
```

Make sure you have the necessary permissions and Wrangler is correctly configured for your Cloudflare account.

### package.json
```json
{
  "name": "bolt",
  "description": "StackBlitz AI Agent",
  "private": true,
  "license": "MIT",
  "packageManager": "pnpm@9.4.0",
  "sideEffects": false,
  "type": "module",
  "scripts": {
    "deploy": "npm run build && wrangler pages deploy",
    "build": "remix vite:build",
    "dev": "remix vite:dev",
    "test": "vitest --run",
    "test:watch": "vitest",
    "lint": "eslint --cache --cache-location ./node_modules/.cache/eslint .",
    "lint:fix": "npm run lint -- --fix",
    "start": "bindings=$(./bindings.sh) && wrangler pages dev ./build/client $bindings",
    "typecheck": "tsc",
    "typegen": "wrangler types",
    "preview": "pnpm run build && pnpm run start"
  },
  "engines": {
    "node": ">=18.18.0"
  },
  "dependencies": {
    "@ai-sdk/anthropic": "^0.0.39",
    "@codemirror/autocomplete": "^6.17.0",
    "@codemirror/commands": "^6.6.0",
    "@codemirror/lang-cpp": "^6.0.2",
    "@codemirror/lang-css": "^6.2.1",
    "@codemirror/lang-html": "^6.4.9",
    "@codemirror/lang-javascript": "^6.2.2",
    "@codemirror/lang-json": "^6.0.1",
    "@codemirror/lang-markdown": "^6.2.5",
    "@codemirror/lang-python": "^6.1.6",
    "@codemirror/lang-sass": "^6.0.2",
    "@codemirror/lang-wast": "^6.0.2",
    "@codemirror/language": "^6.10.2",
    "@codemirror/search": "^6.5.6",
    "@codemirror/state": "^6.4.1",
    "@codemirror/view": "^6.28.4",
    "@iconify-json/ph": "^1.1.13",
    "@iconify-json/svg-spinners": "^1.1.2",
    "@lezer/highlight": "^1.2.0",
    "@nanostores/react": "^0.7.2",
    "@radix-ui/react-dialog": "^1.1.1",
    "@radix-ui/react-dropdown-menu": "^2.1.1",
    "@remix-run/cloudflare": "^2.10.2",
    "@remix-run/cloudflare-pages": "^2.10.2",
    "@remix-run/react": "^2.10.2",
    "@uiw/codemirror-theme-vscode": "^4.23.0",
    "@unocss/reset": "^0.61.0",
    "@webcontainer/api": "1.3.0-internal.10",
    "@xterm/addon-fit": "^0.10.0",
    "@xterm/addon-web-links": "^0.11.0",
    "@xterm/xterm": "^5.5.0",
    "ai": "^3.3.4",
    "date-fns": "^3.6.0",
    "diff": "^5.2.0",
    "framer-motion": "^11.2.12",
    "isbot": "^4.1.0",
    "istextorbinary": "^9.5.0",
    "jose": "^5.6.3",
    "nanostores": "^0.10.3",
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-hotkeys-hook": "^4.5.0",
    "react-markdown": "^9.0.1",
    "react-resizable-panels": "^2.0.20",
    "react-toastify": "^10.0.5",
    "rehype-raw": "^7.0.0",
    "rehype-sanitize": "^6.0.0",
    "remark-gfm": "^4.0.0",
    "remix-island": "^0.2.0",
    "remix-utils": "^7.6.0",
    "shiki": "^1.9.1",
    "unist-util-visit": "^5.0.0"
  },
  "devDependencies": {
    "@blitz/eslint-plugin": "0.1.0",
    "@cloudflare/workers-types": "^4.20240620.0",
    "@remix-run/dev": "^2.10.0",
    "@types/diff": "^5.2.1",
    "@types/react": "^18.2.20",
    "@types/react-dom": "^18.2.7",
    "fast-glob": "^3.3.2",
    "is-ci": "^3.0.1",
    "node-fetch": "^3.3.2",
    "prettier": "^3.3.2",
    "typescript": "^5.5.2",
    "unified": "^11.0.5",
    "unocss": "^0.61.3",
    "vite": "^5.3.1",
    "vite-plugin-node-polyfills": "^0.22.0",
    "vite-plugin-optimize-css-modules": "^1.1.0",
    "vite-tsconfig-paths": "^4.3.2",
    "vitest": "^2.0.1",
    "wrangler": "^3.63.2",
    "zod": "^3.23.8"
  },
  "resolutions": {
    "@typescript-eslint/utils": "^8.0.0-alpha.30"
  }
}
```

### load-context.ts
```ts
import { type PlatformProxy } from 'wrangler';

type Cloudflare = Omit<PlatformProxy<Env>, 'dispose'>;

declare module '@remix-run/cloudflare' {
  interface AppLoadContext {
    cloudflare: Cloudflare;
  }
}
```

## Top-level structure
- `app/` — Remix application code with `components/`, `lib/`, `routes/`, `styles/`, `types/`, and `utils/`, plus `entry.client.tsx`, `entry.server.tsx`, and `root.tsx` as the app entrypoints.
- `functions/` — Cloudflare Pages Function entrypoint at `functions/[[path]].ts`.
- `public/` — static assets including logos and social preview images.
- `types/` — ambient TypeScript declarations such as `istextorbinary.d.ts`.
- `package.json` — project scripts for `dev`, `build`, `start`, `preview`, `test`, `typecheck`, `typegen`, and `deploy`, plus Remix/Vite/Cloudflare/WebContainer dependencies.
- `load-context.ts` — extends Remix `AppLoadContext` with a typed Cloudflare `PlatformProxy`.
- `bindings.sh`, `wrangler.toml`, `vite.config.ts`, `uno.config.ts`, and `eslint.config.mjs` — local runtime, deployment, styling, and lint configuration.
- `CONTRIBUTING.md` — setup, API-key configuration, scripts, testing, and deployment guide for building your own Bolt-like tool on WebContainers.
- `README.md` — commercial-product positioning, differentiators, and operator tips for using or reusing the open-source codebase.
