# n8n-io/n8n

## Metadata
- Stars: 192570
- Primary language: TypeScript
- Default branch: master
- Latest release: beta (pre-release, 2026-06-11)
- License: Sustainable Use License / n8n Enterprise License (fair-code)
- Homepage: https://n8n.io
- Fetched: 2026-06-15
- Final URL: https://github.com/n8n-io/n8n

## Description
Fair-code workflow automation platform with native AI capabilities. Combine visual building with custom code, self-host or cloud, 400+ integrations.

## README
![Banner image](https://user-images.githubusercontent.com/10284570/173569848-c624317f-42b1-45a6-ab09-f0ea3c247648.png)

# n8n - Secure Workflow Automation for Technical Teams

n8n is a workflow automation platform that gives technical teams the flexibility of code with the speed of no-code. With 400+ integrations, native AI capabilities, and a fair-code license, n8n lets you build powerful automations while maintaining full control over your data and deployments.

## Key Capabilities

- **Code When You Need It**: Write JavaScript/Python, add npm packages, or use the visual interface
- **AI-Native Platform**: Build AI agent workflows based on LangChain with your own data and models
- **Full Control**: Self-host with our fair-code license or use our cloud offering
- **Enterprise-Ready**: Advanced permissions, SSO, and air-gapped deployments
- **Active Community**: 400+ integrations and 900+ ready-to-use templates

## Quick Start

Try n8n instantly with npx (requires Node.js):

```
npx n8n
```

Or deploy with Docker:

```
docker volume create n8n_data
docker run -it --rm --name n8n -p 5678:5678 -v n8n_data:/home/node/.n8n docker.n8n.io/n8nio/n8n
```

Access the editor at http://localhost:5678

## Resources

- 📚 Documentation: https://docs.n8n.io
- 🔧 400+ Integrations: https://n8n.io/integrations
- 💡 Example Workflows: https://n8n.io/workflows
- 🤖 AI & LangChain Guide: https://docs.n8n.io/advanced-ai/
- 👥 Community Forum: https://community.n8n.io
- 📖 Community Tutorials: https://community.n8n.io/c/tutorials/28

## License

n8n is fair-code distributed under the Sustainable Use License and n8n Enterprise License.

- **Source Available**: Always visible source code
- **Self-Hostable**: Deploy anywhere
- **Extensible**: Add your own nodes and functionality

Enterprise Licenses available for additional features and support.

## What does n8n mean?

**Short answer:** It means "nodemation" and is pronounced as n-eight-n.

## Docs

### AGENTS.md

This file provides guidance on how to work with the n8n repository.

**Project Overview**

n8n is a workflow automation platform written in TypeScript, using a monorepo structure managed by pnpm workspaces. It consists of a Node.js backend, Vue.js frontend, and extensible node-based workflow engine.

**Architecture Overview**

Monorepo Structure: pnpm workspaces with Turbo build orchestration

Package Structure:
- `packages/@n8n/api-types` — Shared TypeScript interfaces between frontend and backend
- `packages/workflow` — Core workflow interfaces and types
- `packages/core` — Workflow execution engine
- `packages/cli` — Express server, REST API, and CLI commands
- `packages/editor-ui` — Vue 3 frontend application
- `packages/@n8n/i18n` — Internationalization for UI text
- `packages/nodes-base` — Built-in nodes for integrations
- `packages/@n8n/nodes-langchain` — AI/LangChain nodes
- `packages/@n8n/instance-ai` — AI Assistant backend in the UI
- `@n8n/design-system` — Vue component library for UI consistency
- `@n8n/config` — Centralized configuration management

**Technology Stack**

- Frontend: Vue 3 + TypeScript + Vite + Pinia + Storybook UI Library
- Backend: Node.js + TypeScript + Express + TypeORM
- Testing: Jest (unit) + Playwright (E2E)
- Database: TypeORM with SQLite/PostgreSQL support
- Code Quality: Biome (formatting) + ESLint + lefthook git hooks

**Key Architectural Patterns**

1. Dependency Injection: Uses `@n8n/di` for IoC container
2. Controller-Service-Repository: Backend follows MVC-like pattern
3. Event-Driven: Internal event bus for decoupled communication
4. Context-Based Execution: Different contexts for different node types
5. State Management: Frontend uses Pinia stores
6. Design System: Reusable components in `@n8n/design-system`

**Claude Code Plugin**

n8n-specific skills, commands, and agents live in `.claude/plugins/n8n/` namespaced under `n8n:`. Use `n8n:` prefix when invoking (e.g. `/n8n:create-pr`, `/n8n:plan`, `n8n:developer` agent).

**Essential Commands**

```bash
pnpm agent:setup          # install → build → test (full suite)
pnpm build > build.log 2>&1
pnpm test
pnpm test:affected
pnpm lint
pnpm typecheck
```

### docs/ directory

- `db.md` — Database schema documentation
- `generated/` — Auto-generated docs

## Top-level structure

```
.agents/          — agent configs
.claude/          — Claude Code plugin (n8n: namespace)
AGENTS.md         — monorepo contributing guide (fetched above)
CLAUDE.md         — Claude-specific project guidance
CONTRIBUTING.md   — Contributing guide
LICENSE.md        — Sustainable Use License
LICENSE_EE.md     — Enterprise License
README.md         — Main readme (fetched above)
SECURITY.md       — Security disclosure policy
assets/           — Static assets
docker/           — Docker configuration
docs/             — Internal docs (db.md, generated/)
packages/         — pnpm workspace packages (monorepo core)
scripts/          — Build and dev scripts
security/         — Security tooling
package.json      — Root package config (pnpm)
pnpm-workspace.yaml — Workspace definition
turbo.json        — Turbo build orchestration config
tsconfig.json     — Root TypeScript config
```
