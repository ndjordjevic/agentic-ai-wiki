# mastra-ai/mastra

## Metadata
- Stars: 26626
- Primary language: TypeScript
- Default branch: main
- Latest release: @mastra/core@1.52.0 (2026-07-27)
- License: Other (dual-licensed — see below)
- Homepage: https://mastra.ai
- Fetched: 2026-07-28
- Final URL: https://github.com/mastra-ai/mastra

## Description
Mastra is the modern TypeScript framework for AI-powered applications and agents.

## README
# Mastra

Mastra is a framework for building AI-powered applications and agents with a modern TypeScript stack.

It includes everything you need to go from early prototypes to production-ready applications. Mastra integrates with frontend and backend frameworks like React, Next.js, and Node, or you can deploy it anywhere as a standalone server. It's the easiest way to build, tune, and scale reliable AI products.

## Why Mastra?

Purpose-built for TypeScript and designed around established AI patterns, Mastra gives you everything you need to build great AI applications out-of-the-box.

Some highlights include:

- **Model routing** - Connect to 40+ providers through one standard interface. Use models from OpenAI, Anthropic, Gemini, and more.
- **Agents** - Build autonomous agents that use LLMs and tools to solve open-ended tasks. Agents reason about goals, decide which tools to use, and iterate internally until the model emits a final answer or an optional stopping condition is met.
- **Workflows** - When you need explicit control over execution, use Mastra's graph-based workflow engine to orchestrate complex multi-step processes. Mastra workflows use an intuitive syntax for control flow (`.then()`, `.branch()`, `.parallel()`).
- **Human-in-the-loop** - Suspend an agent or workflow and await user input or approval before resuming. Mastra uses storage to remember execution state, so you can pause indefinitely and resume where you left off.
- **Context management** - Give your agents the right context at the right time. Provide conversation history, retrieve data from your sources (APIs, databases, files), and add human-like memory with Observational Memory so your agents behave coherently.
- **Integrations** - Bundle agents and workflows into existing React, Next.js, or Node.js apps, or ship them as standalone endpoints. When building UIs, integrate with agentic libraries like Vercel's AI SDK UI and CopilotKit to bring your AI assistant to life on the web.
- **MCP servers** - Author Model Context Protocol servers, exposing agents, tools, and other structured resources via the MCP interface. These can then be accessed by any system or agent that supports the protocol.
- **Production essentials** - Shipping reliable agents takes ongoing insight, evaluation, and iteration. With built-in evals and observability, Mastra gives you the tools to observe, measure, and refine continuously.

## Get started

The **recommended** way to get started with Mastra is by running the command below:

```shell
npm create mastra@latest
```

Follow the Installation guide (https://mastra.ai/guides/getting-started/quickstart) for step-by-step setup with the CLI or a manual install.

If you're new to AI agents, check out the templates, course, and YouTube videos to start building with Mastra today.

**Alternative — pre-built prompt to get started:**

```md
Create a new Mastra project. Mastra is a framework for AI applications and agents on a modern TypeScript stack. Before running the command, ask these questions one at a time and wait for each answer unless it was already provided:

Project name? (default: "my-mastra-app")
Provider? (required; options: "openai", "anthropic", "google", "xai")

If the provider isn't supported, ask again and list the supported values.

Run: npm create mastra@latest <project-name> -- --llm <provider>

The command creates a default Mastra project, installs Mastra skills for detected coding assistants, and initializes Git when appropriate.

After creation, enter the project directory and start the dev server: npx bgproc start -n <project-name> -w -- npm run dev

Open Mastra Studio at http://localhost:4111. Studio is the interface for building, testing, and managing agents, workflows, and tools.

Also mention that the Mastra model router provides access to thousands of models: https://mastra.ai/models
```

## Documentation

Visit the official documentation at https://mastra.ai/docs.

## Build with AI

Learn how to make your agent a Mastra expert by following the Build with AI guide (https://mastra.ai/docs/getting-started/build-with-ai).

## Contributing

Looking to contribute? All types of help are appreciated, from coding to testing and feature specification. Read `CONTRIBUTING.md` for more details on how to get involved.

If you are a developer and would like to contribute with code, please open an issue to discuss before opening a Pull Request.

Information about the project setup can be found in the development documentation (`DEVELOPMENT.md`).

## Support

There is an open community Discord (https://discord.gg/BTYqqHKUrf). Come and say hello and let us know if you have any questions or need any help getting things running.

## Licensing

This repository uses a dual-license model:

- **Apache License 2.0** — The core framework and the vast majority of this codebase is open source under Apache-2.0.
- **Mastra Enterprise License** — Code in any directory named `ee/` (e.g., `packages/core/src/auth/ee/`) is source-available under the Mastra Enterprise License. These features require a valid enterprise license for production use but can be freely used for development and testing.

See `LICENSE.md` for the full license mapping and `ee/LICENSE` for the enterprise license terms.

## Security

The maintainers ask that security findings be responsibly disclosed to security@mastra.ai.

## Top-level structure

Not fetched in detail at `standard` companion-fetch depth — README and metadata are the primary source for this ingest. Per the README, the codebase is a monorepo built around `packages/core` (the `@mastra/core` npm package), with enterprise-only code isolated in `ee/` subdirectories throughout the tree (dual Apache-2.0 / Mastra Enterprise License split).
