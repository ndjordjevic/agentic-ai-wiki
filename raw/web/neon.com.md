# neon.com

## Fetch log
- Inbox URL: https://neon.com/
- Final URL: https://neon.com/
- Fetched: 2026-07-08
- Pages: 11
- Mode: standard

## llms.txt — https://neon.com/llms.txt
# Neon Postgres

> Neon is the backend for apps and agents. Services include Neon Postgres, Neon Auth, Data API, Neon Functions, Object Storage, and AI Gateway. Every service is agent-ready: instant, branchable, and serverless. Neon Postgres includes autoscaling, instant restore, and scale-to-zero, and is fully compatible with any language, framework, or ORM that supports Postgres.

Neon docs are available as markdown. Append `.md` to any doc URL or set `Accept: text/markdown`. This is the primary index. Sections with many pages show key pages and link to full sub-indexes.

## Common Queries

- [Pricing and plans](https://neon.com/pricing.md)
- [Choose a connection method (drivers, pooling, serverless)](https://neon.com/docs/connect/choose-connection.md)
- [Troubleshoot connection errors and timeouts](https://neon.com/docs/connect/connection-errors.md)
- [pgvector extension for vector search and embeddings](https://neon.com/docs/extensions/pgvector.md)
- [Neon API reference (projects, branches, databases, endpoints)](https://neon.com/docs/reference/api-reference.md)

## Introduction

Architecture, features, autoscaling, branching concepts, billing, and plans.

- [All 34 Introduction pages](https://neon.com/docs/introduction/llms.txt) — key pages below

- [Neon's lakebase architecture](https://neon.com/docs/introduction/architecture-overview.md): Inside Neon Postgres: decoupled compute and durable storage
- [Plans and billing](https://neon.com/docs/introduction/about-billing.md): Learn about Neon's pricing plans and how to manage billing
- [Autoscaling](https://neon.com/docs/introduction/autoscaling.md): An introduction to Neon's autoscaling
- [Scale to Zero](https://neon.com/docs/introduction/scale-to-zero.md): Minimize costs by automatically scaling inactive databases to zero
- [Branching](https://neon.com/docs/introduction/branching.md): Branch your data the same way you branch your code
- [Neon Read Replicas](https://neon.com/docs/introduction/read-replicas.md): Scale your app, run ad-hoc queries, and provide read-only access without duplicating data

## Get Started

First-time setup: org/project creation, connection strings, driver installation, optional auth, and initial schema setup.

- [Build a full backend with Next.js and Neon](https://neon.com/docs/get-started/full-backend-quickstart.md): Connect Postgres with Drizzle, add managed authentication, and ship a typed server-side backend
- [Built to scale](https://neon.com/docs/get-started/built-to-scale.md): Neon supports you from prototype to scale-up
- [Built to scale](https://neon.com/docs/get-started/production-readiness.md): Neon supports you from prototype to scale-up
- [Connecting Neon to your stack](https://neon.com/docs/get-started/connect-neon.md): Learn how to integrate Neon into your application
- [Database branching workflow primer](https://neon.com/docs/get-started/workflow-primer.md): An introduction to integrating Postgres branching into your development workflow
- [Get started with your AI agent](https://neon.com/docs/get-started/with-an-agent.md): Connect your AI coding assistant to Neon
- [Getting ready for production](https://neon.com/docs/get-started/production-checklist.md): Guidelines to optimize price, performance, and reliability
- [Neon framework guides](https://neon.com/docs/get-started/frameworks.md): Find detailed instructions for connecting to Neon from various frameworks
- [Neon language guides](https://neon.com/docs/get-started/languages.md): Find detailed instructions for connecting to Neon from various languages
- [Neon ORM guides](https://neon.com/docs/get-started/orms.md): Find detailed instructions for connecting to Neon from various ORMs
- [Our DX Principles](https://neon.com/docs/get-started/dev-experience.md): Neon adapts to your workflow, not the other way around.
- [Query with Neon's SQL Editor](https://neon.com/docs/get-started/query-with-neon-sql-editor.md): Query your database from the Neon Console using the Neon SQL Editor
- [Tour the Neon Console](https://neon.com/docs/get-started/signing-up.md): Sign up and explore Neon's core features — the SQL Editor, branching, the Tables view, and Neon Auth
- [Why Neon?](https://neon.com/docs/get-started/why-neon.md): The backend for apps and agents, by Databricks

## Connect

Drivers, connection strings, pooling, local dev tooling, and troubleshooting.

- [Choosing your connection method](https://neon.com/docs/connect/choose-connection.md): Find the right driver and connection type for your deployment platform
- [Connect a GUI application](https://neon.com/docs/connect/connect-postgres-gui.md): Learn how to connect a GUI application to Neon
- [Connect from any application](https://neon.com/docs/connect/connect-from-any-app.md): Learn how to connect to Neon from any application
- [Connect Looker Studio to Neon](https://neon.com/docs/connect/connect-looker-studio.md): Learn how to connect your Neon Postgres database to Looker Studio
- [Connect to Neon](https://neon.com/docs/connect/connect-intro.md): Everything you need to know about connecting to Neon
- [Connect to Neon securely](https://neon.com/docs/connect/connect-securely.md): Learn how to connect to Neon securely when using a connection string
- [Connect with pgcli](https://neon.com/docs/connect/connect-pgcli.md): Learn how to connect to Neon using the interactive pgcli client
- [Connect with psql](https://neon.com/docs/connect/query-with-psql-editor.md): Learn how to connect to Neon using psql
- [Connection errors](https://neon.com/docs/connect/connection-errors.md): Learn how to resolve connection errors
- [Connection latency and timeouts](https://neon.com/docs/connect/connection-latency.md): Learn about strategies to manage connection latencies and timeouts
- [Connection pooling](https://neon.com/docs/connect/connection-pooling.md): Learn how connection pooling works in Neon
- [Neon Local](https://neon.com/docs/local/neon-local.md): Use Docker environments to connect to Neon and manage branches automatically
- [Neon serverless driver](https://neon.com/docs/serverless/serverless-driver.md): Connect to Neon from serverless environments over HTTP or WebSockets
- [Neon VS Code Extension](https://neon.com/docs/local/vscode-extension.md): Connect to Neon and manage your database directly in VS Code, Cursor, and other editors
- [neon.ts](https://neon.com/docs/reference/neon-ts.md): Infrastructure-as-code config for your Neon project.
- [Passwordless auth](https://neon.com/docs/connect/passwordless-connect.md): Learn how to connect to Neon without a password

## Neon CLI

Install: `npm i -g neonctl`. Use this for terminal-first workflows, scripts, and CI/CD automation with `neonctl`.

- [Neon CLI](https://neon.com/docs/cli.md): The Neon command-line interface: every command, with options and examples
- [Neon CLI command: api](https://neon.com/docs/cli/api.md): Call any Neon API route directly as an authenticated passthrough
- [Neon CLI command: auth](https://neon.com/docs/cli/auth.md): Authenticate to Neon via browser or API key and manage credentials
- [Neon CLI command: bootstrap](https://neon.com/docs/cli/bootstrap.md): Scaffold a new project from a Neon starter template
- [Neon CLI command: branches](https://neon.com/docs/cli/branches.md): List, create, rename, and delete branches; set default; run schema diff
- [Neon CLI command: buckets](https://neon.com/docs/cli/buckets.md): Manage branch object-storage buckets and their objects
- [Neon CLI command: checkout](https://neon.com/docs/cli/checkout.md): Pin a branch in your local .neon context file
- [Neon CLI command: completion](https://neon.com/docs/cli/completion.md): Generate shell completion scripts for neon commands and options
- [Neon CLI command: config](https://neon.com/docs/cli/config.md): Manage a branch with a neon.ts policy: init, status, plan, and apply
- [Neon CLI command: connection-string](https://neon.com/docs/cli/connection-string.md): Get Postgres connection strings for branches and databases
- [Neon CLI command: data-api](https://neon.com/docs/cli/data-api.md): Provision and manage the Neon Data API from the CLI
- [Neon CLI command: databases](https://neon.com/docs/cli/databases.md): List, create, and delete databases in a Neon project
- [Neon CLI command: deploy](https://neon.com/docs/cli/deploy.md): Apply a neon.ts policy to a branch
- [Neon CLI command: dev](https://neon.com/docs/cli/dev.md): Run Neon Functions locally with a dev server
- [Neon CLI command: env](https://neon.com/docs/cli/env.md): Manage a branch's Neon environment variables locally
- [Neon CLI command: functions](https://neon.com/docs/cli/functions.md): Deploy, list, inspect, and delete Neon Functions
- [Neon CLI command: init](https://neon.com/docs/cli/init.md): Initialize an app project with Neon, including auth, MCP server, extensions, and agent skills
- [Neon CLI command: ip-allow](https://neon.com/docs/cli/ip-allow.md): Manage the IP allowlist: list, add, remove, and reset allowed IPs
- [Neon CLI command: link](https://neon.com/docs/cli/link.md): Link a directory to a Neon project and write a `.neon` context file
- [Neon CLI command: me](https://neon.com/docs/cli/me.md): View current user info, login details, and project limits
- [Neon CLI command: neon-auth](https://neon.com/docs/cli/neon-auth.md): Manage Neon Auth from the CLI
- [Neon CLI command: operations](https://neon.com/docs/cli/operations.md): List and manage long-running operations for a Neon project
- [Neon CLI command: orgs](https://neon.com/docs/cli/orgs.md): List the Neon organizations you belong to
- [Neon CLI command: projects](https://neon.com/docs/cli/projects.md): List, create, update, delete, recover, and get Neon projects
- [Neon CLI command: psql](https://neon.com/docs/cli/psql.md): Connect to a Neon database via psql
- [Neon CLI command: roles](https://neon.com/docs/cli/roles.md): List, create, and delete database roles in a Neon project
- [Neon CLI command: set-context](https://neon.com/docs/cli/set-context.md): Set default project context for CLI sessions to avoid repeating project ID
- [Neon CLI command: status](https://neon.com/docs/cli/status.md): Show the branch's live Neon state
- [Neon CLI command: vpc](https://neon.com/docs/cli/vpc.md): Manage Private Networking VPC endpoints and project-level restrictions
- [Neon CLI quickstart](https://neon.com/docs/cli/quickstart.md): Get set up with the Neon CLI in just a few steps
- [Neon CLI: Install and connect](https://neon.com/docs/cli/install.md): Install the Neon CLI and connect with web auth or API key

## AI & Agents

Agent Skills, MCP integrations, vector search, and tools for building AI-powered applications with Neon.

- [Agent Skills](https://neon.com/docs/ai/agent-skills.md): Teach your AI coding assistant how to work with Neon
- [AI Concepts](https://neon.com/docs/ai/ai-concepts.md): Learn how embeddings are used to build AI applications
- [AI Starter Kit](https://neon.com/docs/ai/ai-intro.md): Resources for building AI applications with Neon Postgres
- [AI tools for Agents](https://neon.com/docs/ai/ai-agents-tools.md): AI-powered tools for development and database management
- [Azure Data Studio Notebooks](https://neon.com/docs/ai/ai-azure-notebooks.md): Use Azure Data Studio Notebooks with Neon for vector similarity search
- [Claude Code plugin for Neon](https://neon.com/docs/ai/ai-claude-code-plugin.md)
- [Codex plugin for Neon](https://neon.com/docs/ai/ai-codex-plugin.md)
- [Connect MCP clients to Neon](https://neon.com/docs/ai/connect-mcp-clients-to-neon.md): Learn how to connect MCP clients such as Cursor, Claude Code, VS Code, ChatGPT, and other tools to your Neon Postgres database.
- [Cursor plugin for Neon](https://neon.com/docs/ai/ai-cursor-plugin.md)
- [Database versioning with snapshots](https://neon.com/docs/ai/ai-database-versioning.md): How AI agents and codegen platforms implement database version control using snapshots and preview branches
- [Get started with Lakebase Search](https://neon.com/docs/ai/lakebase-search-get-started.md): Set up vector and full-text search on Neon in minutes
- [Google Colab](https://neon.com/docs/ai/ai-google-colab.md): Use Google Colab with Neon for vector similarity search
- [Inngest](https://neon.com/docs/ai/inngest.md): Quickly build AI RAG and Agentic workflows that scale with Inngest and Neon
- [Lakebase Search](https://neon.com/docs/ai/lakebase-search.md): Scalable vector and full-text search for Postgres
- [LangChain](https://neon.com/docs/ai/langchain.md): Build AI applications faster with LangChain and Postgres
- [LlamaIndex](https://neon.com/docs/ai/llamaindex.md): Build AI applications faster with LlamaIndex and Postgres
- [Neon agents for GitHub Copilot](https://neon.com/docs/ai/ai-github-copilot-agents.md): Custom agents for safe database migrations and query optimization in VS Code
- [Neon MCP Server overview](https://neon.com/docs/ai/neon-mcp-server.md): Connect your AI assistant to Neon to manage projects, run queries, and make schema changes
- [Optimize pgvector search](https://neon.com/docs/ai/ai-vector-search-optimization.md): Fine-tune parameters for efficient and accurate similarity searches in Postgres
- [Scale your AI application with Neon](https://neon.com/docs/ai/ai-scale-with-neon.md): Scale your AI application with Neon's Autoscaling and Read Replica features
- [Semantic Kernel](https://neon.com/docs/ai/semantic-kernel.md): Quickly build AI RAG and Agentic workflows with Semantic Kernel and Neon

## Auth

Managed authentication built on Better Auth that branches with your database.

- [Auth production checklist](https://neon.com/docs/auth/production-checklist.md): Required configuration before launching with Neon Auth
- [Auth troubleshooting](https://neon.com/docs/auth/troubleshooting.md): Common issues when implementing Neon Auth and how to fix them
- [Authentication flow](https://neon.com/docs/auth/authentication-flow.md): Understanding the complete sign-in and sign-up process
- [Branching authentication](https://neon.com/docs/auth/branching-authentication.md): How authentication works with Neon database branches
- [Neon Auth](https://neon.com/docs/auth/overview.md): Managed authentication that branches with your database
- [Neon Auth roadmap](https://neon.com/docs/auth/roadmap.md): What's supported today and what's coming next

### Quick Start

- [Use Neon Auth with Next.js (API methods)](https://neon.com/docs/auth/quick-start/nextjs-api-only.md): Build your own auth UI using SDK methods
- [Use Neon Auth with React (API methods)](https://neon.com/docs/auth/quick-start/react.md): Build your own auth UI
- [Use Neon Auth with TanStack Router](https://neon.com/docs/auth/quick-start/tanstack-router.md): Set up authentication using pre-built UI components

### Reference

- [Next.js Server SDK Reference](https://neon.com/docs/auth/reference/nextjs-server.md): Server-side authentication API for Next.js with Neon Auth
- [UI Components Reference](https://neon.com/docs/auth/reference/ui-components.md): Quick reference for Neon Auth UI components

### Guides

- [Admin](https://neon.com/docs/auth/guides/plugins/admin.md): Manage users, roles, bans, sessions, and impersonation
- [Configure trusted domains](https://neon.com/docs/auth/guides/configure-domains.md): Add your application domains to enable secure authentication redirects
- [Customize emails](https://neon.com/docs/auth/guides/customize-emails.md): Custom branding, content, and delivery for Neon Auth emails
- [Email OTP](https://neon.com/docs/auth/guides/plugins/email-otp.md): Sign in and verify email addresses with one-time passwords
- [Email verification](https://neon.com/docs/auth/guides/email-verification.md): Verify user email addresses during sign-up or account creation
- [JWT](https://neon.com/docs/auth/guides/plugins/jwt.md): Authenticate using JSON Web Tokens (JWT) for external services
- [Magic Link](https://neon.com/docs/auth/guides/plugins/magic-link.md): Passwordless sign-in via email magic links
- [Manage Neon Auth via the API](https://neon.com/docs/auth/guides/manage-auth-api.md): Enable, configure, and disable Neon Auth using the Neon API
- [Open API](https://neon.com/docs/auth/guides/plugins/openapi.md): Interactive API documentation and client generation
- [Organization](https://neon.com/docs/auth/guides/plugins/organization.md): Manage multi-tenant organizations, members, and invitations
- [Password reset](https://neon.com/docs/auth/guides/password-reset.md): Allow users to reset forgotten passwords
- [Phone Number](https://neon.com/docs/auth/guides/plugins/phone-number.md): Sign in existing users with phone OTP codes delivered via your SMS provider
- [Plugins](https://neon.com/docs/auth/guides/plugins.md): Supported Better Auth plugins in Neon Auth
- [Set up OAuth](https://neon.com/docs/auth/guides/setup-oauth.md): Add Google, GitHub, or Vercel sign-in to your application
- [User management](https://neon.com/docs/auth/guides/user-management.md): Update profiles, change passwords, and manage account settings
- [Webhooks](https://neon.com/docs/auth/guides/webhooks.md): Handle authentication events with custom server logic

### Migrate

- [Migrate from Supabase to Neon](https://neon.com/docs/auth/migrate/from-supabase.md): Switch from Supabase Auth and Database to Neon in a few steps
- [Migrate to Neon Auth with Better Auth](https://neon.com/docs/auth/migrate/from-legacy-auth.md): Update from the legacy Stack Auth-based implementation

## Neon Functions

Long-running serverless compute, close to your database.

- [AI agents on Neon Functions](https://neon.com/docs/compute/functions/agents.md): Run streaming, tool-calling agents on Neon Functions.
- [Deploy and manage Neon Functions](https://neon.com/docs/compute/functions/deploy.md): CLI and API reference for deploying and managing Neon Functions.
- [Get started with Neon Functions](https://neon.com/docs/compute/functions/get-started.md): Deploy your first Neon Function and call it over HTTP.
- [Neon Functions](https://neon.com/docs/compute/functions/overview.md): Deploy a backend onto your Neon branch, next to your data.
- [Neon Functions authentication](https://neon.com/docs/compute/functions/authentication.md): Verify callers before a Neon Function does any work.
- [Neon Functions environment variables](https://neon.com/docs/compute/functions/environment-variables.md): Neon-injected variables and how to set your own secrets.
- [Neon Functions preview access](https://neon.com/docs/compute/functions/preview-access.md): What's included in the Neon Functions private preview.
- [Neon Functions runtime limits](https://neon.com/docs/compute/functions/reference/runtime-limits.md): Hard constraints for Neon Functions.
- [WebSockets and SSE on Neon Functions](https://neon.com/docs/compute/functions/websockets.md): Hold long-lived connections open for real-time apps.

## Object Storage

S3-compatible object storage that branches with your projects.

- [Buckets](https://neon.com/docs/storage/buckets.md): Create and manage storage buckets
- [Get started with Neon Storage](https://neon.com/docs/storage/get-started.md): Upload your first file in minutes
- [Neon Storage](https://neon.com/docs/storage/overview.md): S3-compatible object storage that branches with your database
- [Objects](https://neon.com/docs/storage/objects.md): Upload, download, list, and delete files
- [S3 compatibility](https://neon.com/docs/storage/s3-compatibility.md): Which S3 operations Neon Storage supports
- [Storage authentication](https://neon.com/docs/storage/authentication.md): How Neon credentials map to S3 access keys
- [Storage troubleshooting](https://neon.com/docs/storage/troubleshooting.md): Common errors and how to fix them

## AI Gateway

Access frontier and open-source models through a single API.

- [AI Gateway authentication](https://neon.com/docs/ai-gateway/authentication.md): How Neon credentials work with AI Gateway
- [AI Gateway models](https://neon.com/docs/ai-gateway/models.md): Available models and how to specify them
- [AI Gateway troubleshooting](https://neon.com/docs/ai-gateway/troubleshooting.md): Common errors and how to fix them
- [Anthropic Messages API](https://neon.com/docs/ai-gateway/anthropic-messages.md): Use the Anthropic SDK with Neon AI Gateway
- [Chat completions](https://neon.com/docs/ai-gateway/chat-completions.md): The OpenAI-compatible unified endpoint
- [Gemini API](https://neon.com/docs/ai-gateway/gemini.md): Use the Google Gemini API with Neon AI Gateway
- [Get started with Neon AI Gateway](https://neon.com/docs/ai-gateway/get-started.md): Make your first inference request in minutes
- [Neon AI Gateway](https://neon.com/docs/ai-gateway/overview.md): One API for frontier and open-source models from Anthropic, OpenAI, Google, and more. Built into your Neon project.
- [OpenAI Responses API](https://neon.com/docs/ai-gateway/openai-responses.md): Use the OpenAI Responses API with Neon AI Gateway

## Data API

PostgREST-style REST interface for your Neon database.

- [Access control & security](https://neon.com/docs/data-api/access-control.md): Understand how the Data API authenticates requests and enforces database permissions.
- [Custom authentication providers](https://neon.com/docs/data-api/custom-authentication-providers.md): Configure custom authentication providers with the Data API
- [Data API Advisors](https://neon.com/docs/data-api/database-advisor.md): Identify security and performance issues in your API-exposed database
- [Data API troubleshooting](https://neon.com/docs/data-api/troubleshooting.md): Common issues and solutions when using the Neon Data API
- [Generate TypeScript types from your database schema](https://neon.com/docs/data-api/generate-types.md): Automatically generate TypeScript types from your database schema for type-safe Data API interactions.
- [Getting started with Neon Data API](https://neon.com/docs/data-api/get-started.md): Learn how to enable and use the Neon Data API
- [Manage Data API](https://neon.com/docs/data-api/manage.md): Configure schemas, manage authentication providers, and control API access.
- [Neon Data API](https://neon.com/docs/data-api/overview.md): A fully managed REST interface for your Neon database
- [Neon Data API tutorial](https://neon.com/docs/data-api/demo.md): Explore our demo note-taking app to learn about Data API queries with RLS
- [SQL to PostgREST Converter](https://neon.com/docs/data-api/sql-to-rest.md): Convert SQL queries to PostgREST API calls with real-time preview

## Branching

Instant copy-on-write database environments for dev, CI, previews, and recovery.

- [Blog posts, docs, guides, and more](https://neon.com/branching/tooling-and-automation.md): A collection of tools and resources to implement branching workflows, snapshot-based promotion, automation via APIs, and integrations with GitHub, Vercel, and agents
- [Branching with the Neon API](https://neon.com/docs/guides/branching-neon-api.md): Learn how to create and delete branches with the Neon API
- [Branching with the Neon CLI](https://neon.com/docs/guides/branching-neon-cli.md): Learn how to create and delete branches with the Neon CLI
- [Build versioning / checkpoints for your agent](https://neon.com/branching/branching-for-agents.md): Learn how to use branching in your agents or platforms. Manage databases per user or app and build versioning with snapshots that keep code and database state in sync
- [Create one branch per PR and per developer](https://neon.com/branching/branching-workflows-for-development.md): Build branching workflows for development: create one branch per developer, shared dev branches, or per-PR databases for safe, isolated, production-like testing
- [Create one branch per preview and per test run](https://neon.com/branching/ci-preview-workflows.md): Build branching workflows for CI and previews: spin up isolated branches per preview or test run, automate cleanup, and avoid shared test databases
- [Manage production and staging as branches](https://neon.com/branching/production-staging-workflows.md): Learn how to manage production and staging with database branching. Treat the production branch as the source, derive staging from it, and anonymize data for PII-safe workflows
- [Promote from dev to prod without conflict](https://neon.com/branching/advanced-branching-workflows.md): Build a snapshot-based promotion workflow for Postgres: replace production with a known-good dev version using database branches, snapshots, and instant restores
- [The building blocks](https://neon.com/branching/foundational-concepts.md): Learn how Neon projects, branches, and hierarchies work: fast copy-on-write branching, isolated compute per branch, and instant restore with snapshots
- [Use branches to restore instantly](https://neon.com/branching/recovery-workflows.md): Learn how to use branching for recovery: use database branches to go back in time, recover lost data, debug migrations, and audit historical states safely
- [Use database branches as environments](https://neon.com/branching/rethinking-the-database.md): Rethink the database developer experience: database branching replaces instance copying with fast, isolated environments built on copy-on-write storage

## Manage

Projects, branches, computes, roles, databases, and organization settings.

- [All 29 Manage pages](https://neon.com/docs/manage/llms.txt) — key pages below

- [Manage projects](https://neon.com/docs/manage/projects.md): Learn how to manage Neon projects from the Neon Console or the Neon API.
- [Manage branches](https://neon.com/docs/manage/branches.md)
- [Manage computes](https://neon.com/docs/manage/computes.md)
- [Organizations](https://neon.com/docs/manage/organizations.md): Manage your projects and collaborate with team members
- [Backups](https://neon.com/docs/manage/backups.md): An overview of backup strategies for Neon Postgres

## Guides

Step-by-step integration guides for frameworks, ORMs, auth providers, and deployment platforms.

- [All 169 Guides pages](https://neon.com/docs/guides/llms.txt) — key pages below

- [Connect a Next.js application to Neon](https://neon.com/docs/guides/nextjs.md): Set up a Neon project in seconds and connect from a Next.js application
- [Connect from Prisma to Neon](https://neon.com/docs/guides/prisma.md): Learn how to connect to Neon from Prisma
- [Connect from Drizzle to Neon](https://neon.com/docs/guides/drizzle.md): Learn how to connect to Neon from Drizzle
- [Neon integration guides](https://neon.com/docs/guides/integrations.md): Find detailed instructions for integration across various platforms and services.
- [Integrating Neon with Vercel](https://neon.com/docs/guides/vercel-overview.md): Choose the right connection path in seconds
- [Integrating with Neon](https://neon.com/docs/guides/platform-integration-overview.md): Choose the right integration path for your platform or application
- [Row-Level Security with Neon](https://neon.com/docs/guides/row-level-security.md): How Neon features use Postgres Row-Level Security

## Import

Migration guides by source, size, and downtime tolerance. Covers pg_dump, pgcopydb, logical replication, and provider-specific guides.

- [All 24 Import pages](https://neon.com/docs/import/llms.txt) — key pages below

- [Neon data migration guides](https://neon.com/docs/import/migrate-intro.md): Learn how to migrate data to Neon Postgres from different database providers and sources
- [Migrate data from Postgres with pg_dump and pg_restore](https://neon.com/docs/import/migrate-from-postgres.md)
- [Postgres sample data](https://neon.com/docs/import/import-sample-data.md): Import sample data for learning, testing, and exploring Neon
- [Import data from CSV](https://neon.com/docs/import/import-from-csv.md)
- [Import Data Assistant](https://neon.com/docs/import/import-data-assistant.md): Import a database under 10 GB to Neon using our automated import tool
- [Migrate from Supabase to Neon Postgres](https://neon.com/docs/import/migrate-from-supabase.md): Learn how to migrate your database from Supabase to Neon Postgres using pg_dump and pg_restore

## Workflows

Automate branching, data anonymization, and database provisioning in CI/CD pipelines and GitHub Actions.

- [Automate branching with GitHub Actions](https://neon.com/docs/guides/branching-github-actions.md): Create and delete branches with GitHub Actions
- [Claimable database integration guide](https://neon.com/docs/workflows/claimable-database-integration.md): Manage Neon projects for users with the project database claim API
- [Data anonymization](https://neon.com/docs/workflows/data-anonymization.md): Mask sensitive data in development branches using PostgreSQL Anonymizer
- [Data anonymization API reference](https://neon.com/docs/workflows/data-anonymization-api.md): API endpoints for managing anonymized branches and masking rules
- [Data anonymization with GitHub Actions](https://neon.com/docs/workflows/data-anonymization-github-actions.md): Automate anonymized branch creation in your CI/CD pipeline

## Reference

API reference, SDKs, Terraform provider, Postgres compatibility, and platform-level tooling.

- [Claimable Postgres by Neon](https://neon.com/docs/reference/claimable-postgres.md): Launch an instant Neon Postgres database with zero configuration
- [Manage Neon with Terraform](https://neon.com/docs/reference/terraform.md): Use Terraform to provision and manage your Neon projects, branches, endpoints, roles, databases, and other resources as code.
- [Metrics and logs reference](https://neon.com/docs/reference/metrics-logs.md): Complete reference for all metrics and log fields exported by Neon
- [Neon API](https://neon.com/docs/reference/api-reference.md)
- [Neon API TypeScript SDK](https://neon.com/docs/reference/typescript-sdk.md): Programmatically manage Neon projects, branches, databases, and other platform resources
- [Neon Auth and Data API SDK](https://neon.com/docs/reference/javascript-sdk.md): Reference documentation for @neondatabase/neon-js (authentication and Data API database queries)
- [Neon RSS feeds](https://neon.com/docs/reference/feeds.md): Stay updated with the latest news from Neon
- [Neon SDKs](https://neon.com/docs/reference/sdk.md)
- [Postgres compatibility](https://neon.com/docs/reference/compatibility.md): Learn about Neon as a managed Postgres service
- [Python SDK (Neon API)](https://neon.com/docs/reference/python-sdk.md): Programmatically manage Neon projects, branches, databases, and other platform resources
- [Neon API OpenAPI Spec](https://neon.com/api_spec/release/v2.json): Machine-readable OpenAPI 3.0 specification for the Neon API

## PostgreSQL

Postgres functions, data types, query optimization, indexing strategies, version upgrades, and general Postgres usage with Neon.

- [All 66 PostgreSQL pages](https://neon.com/docs/postgresql/llms.txt) — key pages below

- [Postgres query reference](https://neon.com/docs/postgresql/query-reference.md): Find examples of commonly-used Postgres queries for basic to advanced operations
- [Optimize Postgres query performance](https://neon.com/docs/postgresql/query-performance.md): Learn about strategies for optimizing Postgres query performance
- [Postgres indexes](https://neon.com/docs/postgresql/index-types.md): Optimize query performance with indexes in Postgres

## Security

Compliance certifications, acceptable use policies, HIPAA, and security reporting.

- [Acceptable Use Policy](https://neon.com/docs/security/acceptable-use-policy.md)
- [AI use in Neon](https://neon.com/docs/security/ai-use-in-neon.md): How Neon integrates AI into its platform
- [Compliance](https://neon.com/docs/security/compliance.md)
- [HIPAA Compliance](https://neon.com/docs/security/hipaa.md)
- [Security overview](https://neon.com/docs/security/security-overview.md)
- [Security reporting](https://neon.com/docs/security/security-reporting.md)

## Extensions

Postgres extensions supported by Neon, with install and usage instructions.

- [All 47 Extensions pages](https://neon.com/docs/extensions/llms.txt) — key pages below

- [Postgres extensions](https://neon.com/docs/extensions/pg-extensions.md)
- [The pg_stat_statements extension](https://neon.com/docs/extensions/pg_stat_statements.md): Track planning and execution statistics for all SQL statements
- [The pgvector extension](https://neon.com/docs/extensions/pgvector.md): Enable Postgres as a vector store with the pgvector extension
- [The pgcrypto extension](https://neon.com/docs/extensions/pgcrypto.md): Secure your data with cryptographic functions in Postgres

## Community

Contributor guides, component architecture, and documentation standards.

- [All 9 Community pages](https://neon.com/docs/community/llms.txt) — key pages below

- [Docs contribution guide](https://neon.com/docs/community/contribution-guide.md): Learn how to contribute to the Neon documentation
- [Getting Neon docs as Markdown](https://neon.com/docs/community/llms-markdown-guide.md): How to get our documentation as plain Markdown for LLMs, tools, and scripts

## Additional Resources

- [Changelog](https://neon.com/docs/changelog): Latest updates and releases
- [PostgreSQL Tutorial](https://neon.com/postgresql/tutorial): Comprehensive PostgreSQL tutorial and reference
- [Community Guides](https://neon.com/guides): Step-by-step tutorials for frameworks and tools
- [FAQs](https://neon.com/faqs): Frequently asked questions about Neon
- [Glossary](https://neon.com/docs/reference/glossary.md)
- [Blog](https://neon.com/blog.md): Engineering, product, and community posts from the Neon team

## Landing page — https://neon.com/
# Neon — Postgres backends for apps and agents

Autoscaling Report: Production databases on Neon use 2.4x less compute and 50% less cost than if they were running on a provisioned platform.

A DATABRICKS COMPANY

# Neon is the Postgres backend designed for apps and agents.

Get started | Read the docs

## Products (hero cards)
- Postgres Database — Serverless Postgres that scales and branches with your app.
- Authentication — Managed auth with users and sessions stored in Postgres.
- Compute (early access) — Functions without timeouts running close to your database.
- Storage (early access) — S3-compatible object storage that branches with your projects.
- AI Gateway (early access) — One API for all frontier & open-source models, powered by Databricks.

Tags: AI, Advanced Autoscaling, Instant Branching, Auth Included, Production-Grade Features

## Cloud primitives for the AI Engineering era
Integrate with a single command and the LLM does the hard work.
$ npx neonctl init
Connect MCP clients to Neon

## Advanced autoscaling
By separating compute and storage, Neon automatically scales CPU, memory and storage to fit your workload.
54,210 performance degradations prevented by Autoscaling every day

## Instant branching
- Copy-on-write — Create editable copies of databases instantly with git-like branching
- Anonymization — Mask sensitive data with realistic fake values
- Ephemerality — Obsolete branches delete themselves automatically after work is complete

## Authentication included, free
User authentication and management built in to the database.

## No platform fees
HIPAA and SOC2, Private networking (PrivateLink), Logs & metrics export (Datadog/OTel), Uptime SLAs (99.95% on Scale), Point-in-time recovery, Single sign-on

## Agent platform — Speed and scale for agents. And devs.
Codegen and agent platforms rely on Neon to run the backend for user-generated apps.

### Deploy thousands of databases that turn off when idle
Inactive databases pause on their own. Databases deployed: 41,092.

### Manage your fleet via API
Neon databases spin up in milliseconds.
curl -X POST https://api.neon.tech/v2/projects/:id/database — connection string in 120ms

### Database checkpoints
Copy-on-write storage makes it cheap and fast to save point-in-time versions.

## Trusted Postgres, Backed by Giants
Neon was founded by Postgres committers. In 2025, Neon became a Databricks company.
12,000,000 Postgres databases started daily.

$ npx neonctl init

## Docs — https://neon.com/docs
# Neon documentation

Neon is the backend for apps and agents.

## Getting started
- One-command setup: `npx neon@latest init` — AI-guided setup
- Build a full backend: Next.js + Postgres + Neon Auth + Drizzle

## Products
- Postgres: Serverless Postgres with branching, autoscaling, scale to zero, and instant restore.
- Neon Auth: Managed auth with sign-up, OAuth, and sessions. Users live in your Postgres and branch with it.
- Data API: HTTPS queries with no backend code. Drop-in compatible with Supabase.
- Storage: S3-compatible object storage that branches with your database.
- Functions: Long-running Node.js compute, deployed alongside your database.
- AI Gateway: One API for frontier and open-source models, built into your Neon project.

## Connect your framework
Next.js, Django, Drizzle, React Router, TanStack Start, Express, NestJS, Astro, SvelteKit, Nuxt, Laravel, Rails, Python, Go, Java, Rust, .NET, Elixir, Phoenix, Prisma, Kysely, Tortoise ORM, TypeORM, SQLAlchemy, Hono, SolidStart, Reflex, JavaScript, Symfony, Quarkus, Micronaut, Redwood

## AI tools and agents
Neon integrates with AI coding tools and agents through MCP.
- Cursor, Claude Code, Codex, GitHub Copilot

## Neon's lakebase architecture — https://neon.com/docs/introduction/architecture-overview.md
> This page location: Architecture > Architecture overview
> Full Neon documentation index: https://neon.com/docs/llms.txt

> Summary: Neon's lakebase architecture splits Postgres into an ephemeral compute layer and a durable storage layer connected by WAL, so compute nodes can scale, restart, or fail without data loss. The storage layer uses Paxos-based WAL quorum across safekeepers to define commit correctness, a pageserver to reconstruct page versions on demand, and object storage for immutable long-term history. None of those components sit on the hot query path. This design enables copy-on-write branching, instant point-in-time restores, and serverless autoscaling including scale-to-zero, all as metadata operations rather than data copies.

# Neon's lakebase architecture

Inside Neon Postgres: decoupled compute and durable storage

## Top level overview

Instead of running Postgres as a single stateful system tied to a VM and its filesystem, Neon is a serverless database that splits the system into two independent layers: compute and storage. These layers communicate over the network, with a stream of write-ahead log (WAL) records connecting them.

This separation is what puts Neon in the [lakebase category](https://www.databricks.com/blog/what-is-a-lakebase) of OLTP databases. Compute can scale up, scale down, go idle, and be restarted instantly without risking data loss or requiring data movement.

- **Ephemeral compute layer**: optimized for latency and execution. This layer runs Postgres, executing queries and transactions using RAM and local NVMe for performance. Compute nodes do not own durable state and can be replaced freely.
- **Durable storage layer**: optimized for correctness, history, and scale. This layer defines durability by replicating WAL via quorum, materializes Postgres pages on demand, and stores long-term, immutable history in object storage.

Neon's design intentionally keeps object storage off the critical path. Object storage provides durability and scale, but never sits in front of query execution. Latency-sensitive work stays close to compute, while durability and history are handled asynchronously and independently.

![Neon architecture overview](https://neon.com/docs/introduction/neon-architecture-overview.png)

**Note: What is the difference between Neon and Lakebase?**

Both products share the same architectural foundation but Lakebase comes with additional features integrating it with the rest of the Databricks Data and AI platform. For a full comparison, see [Neon and Lakebase](https://neon.com/docs/introduction/neon-and-lakebase).

## Resource hierarchy

While the sections below describe Neon's physical architecture, the platform organizes resources into a logical hierarchy:

| Concept          | Description                                                           | Relationship              |
| ---------------- | --------------------------------------------------------------------- | ------------------------- |
| Organization     | Highest-level container for billing, users, and projects              | Contains Projects         |
| Project          | Primary container for all database resources for an application       | Contains Branches         |
| Branch           | Lightweight, copy-on-write clone of database state                    | Contains Databases, Roles |
| Compute Endpoint | Running PostgreSQL instance (CPU/RAM for queries)                     | Attached to a Branch      |
| Database         | Logical container for data (tables, schemas, views)                   | Exists within a Branch    |
| Role             | PostgreSQL role for authentication and authorization                  | Belongs to a Branch       |
| Operation        | Async action by the control plane (creating branch, starting compute) | Associated with Project   |

For details on each concept, see the [glossary](https://neon.com/docs/reference/glossary).

## Compute layer

The compute layer is where Postgres actually runs. Each Neon compute node is a standard Postgres instance: it parses SQL, plans queries, executes transactions, enforces MVCC, and manages locks and indexes. From the perspective of the query engine, nothing about Postgres itself is rewritten or replaced.

What is different in Neon is what the compute node is responsible for. **It exists to execute work, not to preserve data.** A compute node can start, stop, scale, or fail at any time without putting durability at risk.

### Components

A Neon compute node has access to fast, local resources:

- RAM - used for shared_buffers, session state, and hot data
- Local NVMe - used as a performance cache for data pages

Pages cached in RAM or NVMe avoid network round-trips and keep most reads at memory or microsecond-level latencies.

### How compute fits into the system

When a query runs, the compute node behaves as you would expect:

- SQL is parsed and planned
- Pages are accessed through the buffer manager
- Changes are applied in memory

The Neon difference appears when the system crosses the boundary between execution and durability. **Instead of flushing WAL to a local filesystem, the compute node streams WAL to the storage layer.** A transaction is considered committed once that WAL has been acknowledged by a quorum of safekeepers (more on this later). The compute node does not wait for data pages to be written to disk or object storage.

For reads, **the compute node always prefers local access.** It first looks in memory, then in the local NVMe cache. Only when a page is missing locally does the compute node request it from the pageserver, which reconstructs the correct page version and returns it over the network. At no point does the compute node read directly from object storage.

## Storage layer

If the compute layer is responsible for execution, the storage layer is responsible for correctness, durability, and history. **This layer exists independently of any single compute node and continues to operate even when computes come and go.**

Rather than exposing a traditional filesystem, the Neon storage layer is built around three distinct components, each with a well-defined role:

- Safekeepers: define correctness by replicating WAL
- The pageserver: turns WAL into queryable data pages
- Object storage: holds long-term, immutable history

### Safekeepers: defining correctness via WAL quorum

Safekeepers are responsible for one thing: **durable replication of WAL**. When a compute node generates WAL records, it streams them to multiple safekeepers. A transaction is considered committed once a quorum of safekeepers has acknowledged the WAL record [via the Paxos protocol](https://neon.com/blog/paxos).

This is a fundamental difference from how traditional Postgres works:

- Correctness in Neon is enforced through replication and consensus
- Commit latency depends on network RTT, not disk fsync
- No single machine defines the durable state of the database

### Pageserver: WAL ⇄ pages

The pageserver sits between WAL and data [pages](https://neon.com/docs/reference/glossary#page). Its job is to **materialize page versions** by combining previously materialized base pages and committed WAL records. It is the system's translation layer between the logical history of the database and the physical representation needed to run queries.

When a compute node needs a page at a specific [LSN (Log Sequence Number)](https://neon.com/docs/reference/glossary#lsn), it asks the pageserver. The pageserver checks whether it already has that version available. If not, it reconstructs the page by replaying WAL up to the requested LSN and returns the result. Materialized pages are later persisted into object storage asynchronously, building up the long-term history of the database.

Importantly, page materialization is not on the transaction's critical path. Commits do not wait for pages to be written or uploaded.

### Object storage: long-term, immutable history

Object storage is where Neon keeps the **durable history** of the database. This layer stores materialized page versions, historical snapshots of data, and immutable representations of past states. It is not a query engine, and it is never accessed directly by the compute layer. It backs the pageserver, not Postgres.

This distinction is critical for performance. Object storage is optimal for durability, scale, and cost, not latency. Reads from object storage may take hundreds of milliseconds, but in Neon, those reads happen only inside the pageserver when reconstructing pages, and never on the hot query path.

## Write path: committing a transaction in Neon

![Write path in Neon](https://neon.com/docs/introduction/neon-write-path.png)

When a transaction executes on a compute node:

1. **Postgres applies changes in memory.** Rows are updated in shared buffers, indexes are modified, and WAL records are generated as usual.
2. **WAL is streamed to the safekeepers.** Instead of flushing WAL to a local filesystem, the compute node sends WAL records over the network to multiple safekeepers.
3. **Commit is defined by quorum.** A transaction is considered committed once a quorum of safekeepers has acknowledged the WAL record. At this point, the client receives success.
4. **Page materialization happens later.** Page reconstruction and persistence happen asynchronously in the storage layer.

## Read path: serving data without object-store latency

![Read path in Neon](https://neon.com/docs/introduction/neon-read-path.png)

The obvious concern with running a database on object storage is latency, but Neon's architecture is designed specifically to avoid this. The most important thing to understand about reads in Neon is this: **queries do not read from object storage.** Object storage backs the system, but it is never on the hot query path.

### The preferred path: local first

When Postgres running on a compute node needs to read a page, it follows a preference order:

1. **RAM (shared buffers).** This is the fastest path, just like in traditional Postgres.
2. **Local NVMe cache.** If the page is not in memory, the compute node checks its local NVMe cache. Access here is still fast.

Only if the page is missing locally does the system involve the storage layer (next section).

### Cache miss: requesting a page from the pageserver

On a cache miss, the compute node requests the required page from the pageserver, specifying the page identifier and the logical point in time (LSN). The pageserver then:

1. Checks whether it already has the requested page version materialized
2. If not, loads a base page from object storage, replays WAL records up to the requested LSN and returns the reconstructed page to the compute node

Once returned, the page can be cached in RAM and NVMe, making subsequent reads fast. This reconstruction only happens if needed, and only for the pages actually accessed.

## Durability

Durability in Neon is not a single mechanism but a composition of responsibilities. No single component is responsible for everything, and no single machine defines the state of the database.

This layering is what allows Neon to tolerate failures intrinsically:

- If a compute node dies → queries stop, but data is safe. A new compute attaches immediately and continues from the same history.
- If a pageserver dies → no durable state is lost. Another pageserver can be deployed and it can reconstruct pages using WAL and object storage.
- If a safekeeper dies → another can be deployed, and WAL replication continues as long as quorum remains.
- Object storage is the last line of defense → it holds immutable page history and survives failures across entire failure domains.

## What this architecture enables

**This design turns traditionally heavy-weight database operations (which usually require copying large amounts of data) into simple metadata operations.** These include creating a new branch, restoring from a snapshot, spinning up a read replica, or attaching a new compute node. In Neon, these operations are fast because they operate on references to existing history, not on the data itself.

- **Serverless compute provisioning.** Because durable state lives outside the compute layer, compute endpoints can [automatically scale up and down according to load](https://neon.com/docs/introduction/autoscaling), or [scale to zero](https://neon.com/docs/introduction/scale-to-zero) entirely. When compute starts, it simply attaches to existing database history rather than reconstructing local state.
- **Copy-on-write branching.** When you create a [branch](https://neon.com/docs/introduction/branching) in Neon, the engine does not duplicate files or pages. Instead, the new branch points to an existing point in history and begins diverging from there using copy-on-write semantics. Only new or modified data consumes additional storage.
- **Instant restores.** Because the database's history is preserved as immutable page versions in object storage, [restoring the database](https://neon.com/docs/introduction/branch-restore) does not involve copying data back into place. Compute can reattach to a past point in history, and execution can resume from the restored state. This process is fast and predictable, even for multi-terabyte databases.
- **A unified foundation for OLTP and OLAP.** Once transactional data lives in object storage, it is no longer isolated from analytical or AI workloads. The same underlying history that supports an OLTP engine (Neon) can also support OLAP engines and AI systems. This is the principle behind the [lakebase architecture](https://www.databricks.com/product/lakebase).

## In short

Neon Postgres, the database service in the Neon backend, is a serverless engine that treats:

- compute as ephemeral and replaceable;
- storage as durable, replicated, and shared;
- WAL as the source of truth;
- and object storage as the foundation.

The result is a database architecture that scales, recovers, and evolves without being constrained by a single machine or filesystem. For developers, this means faster iteration, safer workflows, and infrastructure that adapts automatically as applications grow from early prototypes to large-scale production systems. This design also enables advanced lakebase architectures that unify transactional and analytical data platforms.

---

## Related docs (Architecture)

- [Compute lifecycle](https://neon.com/docs/introduction/compute-lifecycle)
- [Serverless](https://neon.com/docs/introduction/serverless)

## Branching — https://neon.com/docs/introduction/branching.md
> This page location: Branching > About branching
> Full Neon documentation index: https://neon.com/docs/llms.txt

> Summary: Neon branching creates copy-on-write clones of your database instantly, with writes saved as deltas so parent branches see zero load or performance impact. Use branching to spin up isolated development or test environments pre-loaded with production data, or run parallel CI/CD pipelines. You can also recover from data loss by rolling back to any point within your history window.

# Branching

Branch your data the same way you branch your code

With Neon, you can quickly branch your data for development, testing, and various other purposes, enabling you to improve developer productivity and optimize continuous integration and delivery (CI/CD) pipelines.

You can also rewind your data or create branches from the past to recover from mistakes or analyze historical states.

[Watch on YouTube](https://youtube.com/watch?v=UuHnFlg66Io)

## What is a branch?

A branch is a copy-on-write clone of your data. You can create a branch from a current or past state. For example, you can create a branch that includes all data up to the current time or an earlier time.

**Tip: working with sensitive data?**

Neon also supports schema-only branching. [Learn more](https://neon.com/docs/guides/branching-schema-only).

A branch is isolated from its originating data, so you are free to play around with it, modify it, or delete it when it's no longer needed. Changes to a branch are independent. A branch and its parent can share the same data but diverge at the point of branch creation. Writes to a branch are saved as a delta.

Creating a branch does not increase load on the parent branch or affect it in any way, which means you can create a branch without impacting the performance of your production database.

Each Neon project is created with a [root branch](https://neon.com/docs/reference/glossary#root-branch) called `main`. The first branch that you create is branched from the project's root branch. Subsequent branches can be branched from the root branch or from a previously created branch.

**Tip: Using Neon Auth?**

Users, sessions, and auth configuration in the `neon_auth` schema branch with your data, so preview and test environments get isolated authentication state. See [Neon Auth](https://neon.com/docs/auth/overview) and [Branching authentication](https://neon.com/docs/auth/branching-authentication).

## Branching workflows

You can use Neon's branching feature in a variety of workflows.

### Development

You can create a branch of your production database that developers are free to play with and modify. By default, branches are created with all of the data that existed in the parent branch, eliminating the setup time required to deploy and maintain a development database.

![development environment branch](https://neon.com/docs/introduction/branching_dev_env.png)

The following video demonstrates creating a branch in the Neon Console. For step-by-step instructions, see [Create a branch](https://neon.com/docs/manage/branches#create-a-branch).

You can integrate branching into your development workflows and toolchains using the Neon CLI, API, or GitHub Actions. If you use Vercel, you can use the [Neon-managed Vercel integration](https://neon.com/docs/guides/neon-managed-vercel-integration) to create a branch for each preview deployment.

Refer to the following guides for instructions:

- [Branching with the Neon API](https://neon.com/docs/guides/branching-neon-api): Learn how to instantly create and manage branches with the Neon API
- [Branching with the Neon CLI](https://neon.com/docs/guides/branching-neon-cli): Learn how to instantly create and manage branches with the Neon CLI
- [Branching with GitHub Actions](https://neon.com/docs/guides/branching-github-actions): Automate branching with Neon's GitHub Actions for branching
- [The Neon-Managed Vercel Integration](https://neon.com/docs/guides/neon-managed-vercel-integration): Connect your Vercel project and create a branch for each preview deployment

### Testing

Testers can create branches for testing schema changes, validating new queries, or testing potentially destructive queries before deploying them to production. A branch is isolated from its parent branch but has all of the parent branch's data up to the point of branch creation, which eliminates the effort involved in hydrating a database. Tests can also run on separate branches in parallel, with each branch having dedicated compute resources.

![test environment branches](https://neon.com/docs/introduction/branching_test.png)

Refer to the following guide for instructions.

- [Branching: Testing queries](https://neon.com/docs/guides/branching-test-queries): Instantly create a branch to test queries before running them in production

### Temporary environments

Create branches with TTL by [setting an expiration date](https://neon.com/docs/guides/branch-expiration). Perfect for temporary development and testing environments that need automatic deletion.

Branches with expiration work well for:

- CI/CD pipeline testing environments
- Feature development with known lifespans
- Automated testing scenarios
- AI-driven development workflows

## Restore and recover data

If you lose data due to an unintended deletion or some other event, you can use **[instant restore](https://neon.com/docs/introduction/branch-restore)** to recover: roll the branch back to any point in time that still falls within your project's **history window** (the retention you configure under **Settings → Instant restore**). You can also create a new restore branch for historical analysis or any other reason.

![Recover from data loss using restore branching](https://neon.com/docs/introduction/branching_data_loss.png)

### History window

**Instant restore** (and Time Travel, branching from the past, and snapshots) need Neon to keep a log of data changes. The **history window** is the project-wide setting—on **Settings → Instant restore** in the Console—that controls how long that change history is retained, which sets how far back **instant restore** and the other features can reach.

Neon retains a history of changes for your branches, with defaults of 6 hours on Free plan and 1 day on paid plans. Increasing the history window expands recovery options but also increases storage costs, as more history is kept. You can configure it up to 7 days on Launch or 30 days on Scale plans.

For limits, billing, and how to change the setting, see [History window](https://neon.com/docs/introduction/history-window).

Learn how to use these data recovery features:

- [Instant restore](https://neon.com/docs/guides/branch-restore): Restore a branch to an earlier point in its history
- [Reset from parent](https://neon.com/docs/guides/reset-from-parent): Reset a branch to match its parent
- [Time Travel queries](https://neon.com/docs/guides/time-travel-assist): Run SQL queries against your database's past state

---

## Related docs (Branching)

- [Get started with branching](https://neon.com/docs/guides/branching-intro)
- [Branching workflow primer](https://neon.com/docs/get-started/workflow-primer)
- [Branching workflows](https://neon.com/docs/guides/branching-test-queries)
- [Branch archiving](https://neon.com/docs/guides/branch-archiving)
- [Branch expiration](https://neon.com/docs/guides/branch-expiration)
- [Schema-only branches](https://neon.com/docs/guides/branching-schema-only)
- [Reset from parent](https://neon.com/docs/guides/reset-from-parent)

## Autoscaling — https://neon.com/docs/introduction/autoscaling.md
> This page location: Autoscaling > Overview
> Full Neon documentation index: https://neon.com/docs/llms.txt

> Summary: Neon Autoscaling dynamically scales compute resources (measured in CUs) up and down in response to live database load, with no restarts or manual intervention required. Configure autoscaling by setting a min/max CU range on any primary compute or read replica; the maximum permitted autoscaling range is 8 CU. Use this page to understand how autoscaling works and to find the configuration steps before reading the full enablement guide.

# Autoscaling

An introduction to Neon's autoscaling

Neon's _Autoscaling_ feature dynamically adjusts the amount of compute resources allocated to a Neon compute in response to the current load, eliminating the need for manual intervention or restarts.

The following visualization shows how Neon's autoscaling works throughout a typical day. The compute resources scale up or down based on demand, ensuring that your database has the necessary compute resources when it needs them, while conserving resources during off-peak times.

![visualization for autoscaling](https://neon.com/docs/introduction/autoscaling_intro.png)

To dive deeper into how Neon's autoscaling algorithm operates, visit [Understanding Neon's autoscaling algorithm](https://neon.com/docs/guides/autoscaling-algorithm).

## Autoscaling benefits

Neon's Autoscaling feature offers the following benefits:

- **On-demand scaling:** Autoscaling helps with workloads that experience variations over time, such as applications with time-based changes in demand or occasional spikes.
- **Cost-effectiveness**: Autoscaling optimizes resource utilization, ensuring that you only use required resources, rather than over-provisioning to handle peak loads.
- **Resource and cost control**: Autoscaling operates within a user-defined range, ensuring that your compute resources and associated costs do not scale indefinitely.
- **No manual intervention or restarts**: After you enable autoscaling and set scaling limits, no manual intervention or restarts are required, allowing you to focus on your applications.

## Configuring autoscaling

You can enable autoscaling for any compute instance, whether it's a primary compute or a read replica. Simply open the **Edit compute** drawer ([learn how](https://neon.com/docs/guides/autoscaling-guide)) for your compute and set the autoscaling range. This range defines the minimum and maximum compute sizes within which your compute will automatically scale. For example, you might set the minimum to 2 CU (8 GB of RAM) and the maximum to 8 CU (32 GB of RAM). Your compute resources will dynamically adjust within these limits, never dropping below the minimum or exceeding the maximum, regardless of demand.

**Note:** The maximum permitted autoscaling range is 8 CU. This means the difference between your maximum and minimum compute size cannot exceed 8 CU.

We recommend regularly [monitoring](https://neon.com/docs/introduction/monitoring-page) your usage from the **Monitoring Dashboard** to determine if adjustments to this range are needed.

![autoscaling configuration](https://neon.com/docs/introduction/autoscaling_config.png)

For full details about enabling and configuring autoscaling, see [Enabling autoscaling](https://neon.com/docs/guides/autoscaling-guide).

---

## Related docs (Autoscaling)

- [Autoscaling architecture](https://neon.com/docs/introduction/autoscaling-architecture)
- [Autoscaling algorithm](https://neon.com/docs/guides/autoscaling-algorithm)
- [Configure autoscaling](https://neon.com/docs/guides/autoscaling-guide)

## Neon MCP Server overview — https://neon.com/docs/ai/neon-mcp-server.md
> This page location: AI > AI for Agents > MCP integration > Overview
> Full Neon documentation index: https://neon.com/docs/llms.txt

> Summary: The Neon MCP Server implements the Model Context Protocol (MCP), letting AI assistants interact with your Neon projects on your behalf. Set up with `npx neon@latest init` or use the config generator. Supports OAuth and API key auth.

# Neon MCP Server overview

Connect your AI assistant to Neon to manage projects, run queries, and make schema changes

The Neon MCP Server implements the Model Context Protocol (MCP), letting AI assistants interact with your Neon projects on your behalf. Your AI agent can interact with Neon via MCP tools or by running [Neon CLI](https://neon.com/docs/reference/neon-cli) commands directly.

**Important: Security**

The Neon MCP Server grants broad database management capabilities. **Always review and authorize actions requested by the LLM before execution.** Restrict access to trusted users only. See [MCP security guidance](https://neon.com/docs/ai/neon-mcp-server#mcp-security-guidance).

## Quick setup

```bash
npx neon@latest init
```

Runs `neon init` via npx to configure MCP and other integrations for your editor. If you only want the MCP server, use the config generator below.

## Config generator

Use the generator to build an MCP config for your editor, auth method, and transport, including the `Authorization` header for API key or remote agent setups.

## Access control

The Neon MCP Server supports URL parameters to restrict scope and permissions. Append them to the MCP URL (`https://mcp.neon.tech/mcp`).

### Read-only mode

Append `?readonly=true` to restrict the server to read operations:

```
https://mcp.neon.tech/mcp?readonly=true
```

`SELECT` queries and schema inspection remain available. Write operations (creating branches, running migrations, modifying auth config) are disabled.

With OAuth, you can also choose read-only scope during the authorization flow instead of using the URL parameter.

### Project-scoped mode

Scope all operations to a single project:

```
https://mcp.neon.tech/mcp?projectId=<your-project-id>
```

Cross-project search and navigation are disabled in this mode.

### Category filtering

Restrict active tools to specific categories using `?category=<name>` (repeatable):

```
https://mcp.neon.tech/mcp?category=querying&category=schema
```

See [Available tools](https://neon.com/docs/ai/neon-mcp-server#available-tools) for the full category list. To verify which tools are active for a given config without authenticating:

```bash
curl "https://mcp.neon.tech/api/list-tools?readonly=true&category=querying"
```

## MCP security guidance

We recommend MCP for **development and testing only**, not production environments.

- Use MCP only for local development or IDE-based workflows
- Never connect MCP agents to production databases
- Avoid exposing production or PII data; use anonymized data only
- Always review and authorize LLM-requested actions before execution
- Restrict MCP access to trusted users and regularly audit access

### Allowlist IP addresses

The hosted Neon MCP Server (`mcp.neon.tech`) connects to your Neon databases from the following static IP addresses:

- `34.192.103.46`
- `23.22.233.166`

If [IP Allow](https://neon.com/docs/introduction/ip-allow) is enabled on your project, add these addresses to your allowlist so the MCP server can connect.

## Available tools

Tools are grouped into categories. Use the `?category=` URL parameter to restrict which categories are active. You can pass it more than once to enable multiple categories.

| Category                        | What it enables                                                                     |
| ------------------------------- | ----------------------------------------------------------------------------------- |
| Project management (`projects`) | List, create, describe, and delete projects and organizations                       |
| Branch management (`branches`)  | Create branches, compare schemas, reset branches to parent state                    |
| Schema (`schema`)               | Inspect tables and columns; run schema changes via a safe temporary branch workflow |
| SQL (`querying`)                | Execute queries and transactions; inspect database structure                        |
| Neon Auth (`neon_auth`)         | Set up and configure app authentication for a branch                                |
| Neon Data API (`data_api`)      | Enable HTTP-based Data API access for a branch                                      |
| Documentation (`docs`)          | Look up Neon documentation from within your assistant (no OAuth required)           |

Search and navigation tools (search across projects, fetch resource details by ID) are available by default but disabled in [project-scoped mode](https://neon.com/docs/ai/neon-mcp-server#project-scoped-mode).

## Troubleshooting

If your client doesn't support JSON for MCP server configuration (such as older versions of Cursor), use this command when prompted:

```bash
npx -y @neondatabase/mcp-server-neon start <YOUR_NEON_API_KEY>
```

For per-client setup instructions, see [Connect MCP clients](https://neon.com/docs/ai/connect-mcp-clients-to-neon).

**Note:** For clients that don't support Streamable HTTP, you can use the deprecated SSE endpoint: `https://mcp.neon.tech/sse`. SSE is not supported with API key authentication.

## Resources

- [MCP Protocol](https://modelcontextprotocol.org)
- [Neon API Reference](https://api-docs.neon.tech/reference/getting-started-with-neon-api)
- [Neon API Keys](https://neon.com/docs/manage/api-keys#creating-api-keys)
- [Neon MCP server GitHub](https://github.com/neondatabase/mcp-server-neon)

---

## Related docs (MCP integration)

- [Connect MCP clients](https://neon.com/docs/ai/connect-mcp-clients-to-neon)

## Get started with your AI agent — https://neon.com/docs/get-started/with-an-agent.md
> This page location: Start with Neon > One-command setup
> Full Neon documentation index: https://neon.com/docs/llms.txt

> Summary: `npx neon@latest init` connects an AI coding assistant to Neon, installing agent skills and configuring the MCP server in one command.

# Get started with your AI agent

Connect your AI coding assistant to Neon

`npx neon@latest init` gives your agent two things: Neon-specific context from agent skills, and tools to act on your Neon account through the MCP server. The result is an agent that can connect your app to Neon and help you use Neon features as you build. For Cursor and VS Code, it also installs the Neon Local Connect extension for in-editor schema browsing.

For a full app walkthrough, see [Build a full backend](https://neon.com/docs/get-started/full-backend-quickstart).

## Before you start

You'll need:

- [Node.js 18+](https://nodejs.org/)
- A supported AI coding assistant, such as Cursor, VS Code with GitHub Copilot, Claude Code, Codex, Zed, Gemini CLI, Cline, OpenCode, or another [client supported by add-mcp](https://neon.com/docs/ai/connect-mcp-clients-to-neon#supported-agents-add-mcp)

## Run the init command

From your project root, run:

```bash
npx neon@latest init
```

The wizard asks which editor to configure, then:

- Signs you in to Neon (or signs you up for free)
- Creates a Neon API key
- Installs [agent skills](https://neon.com/docs/ai/agent-skills)
- Configures the [Neon MCP server](https://neon.com/docs/ai/neon-mcp-server)
- For Cursor and VS Code, installs the [Neon Local Connect extension](https://marketplace.visualstudio.com/items?itemName=databricks.neon-local-connect)

Run this from your project root so the skills are installed in the right place. For details and manual setup, see the [`neon init` reference](https://neon.com/docs/cli/init).

## Restart your editor

Reload your editor so it picks up the new MCP configuration and skills. For Cursor and VS Code, this also activates the Neon Local Connect extension.

## Tell your agent

In your editor's AI chat, send:

```text
Get started with Neon
```

Your agent reads the installed skill and uses the MCP server to walk you through setup. It can:

- Create a Neon project
- Configure your app
- Write your `DATABASE_URL` to `.env`
- Suggest a Postgres driver and starter query

The exact flow depends on your project. Your agent can scaffold a new connection or help with a migration.

## What's next

- [About branching](https://neon.com/docs/introduction/branching)
- [Neon Auth](https://neon.com/docs/auth/overview)
- [Data API](https://neon.com/docs/data-api/overview)
- [Browse your schema with Neon Local Connect](https://neon.com/docs/local/vscode-extension)
- [`neon init` reference](https://neon.com/docs/cli/init)

---

## Related docs (Start with Neon)

- [Build a full backend](https://neon.com/docs/get-started/full-backend-quickstart)
- [Tour the Neon Console](https://neon.com/docs/get-started/signing-up)

## Neon Auth — https://neon.com/docs/auth/overview.md
> This page location: Backend > Neon Auth > Introduction > Overview
> Full Neon documentation index: https://neon.com/docs/llms.txt

> Summary: Neon Auth is a managed authentication service built on Better Auth. It stores users, sessions, and OAuth configuration in your Neon Postgres database under the neon_auth schema, compatible with Row Level Security. Every database branch gets its own isolated auth environment, so you can test sign-up, login, and OAuth flows in preview or CI branches without touching production.

# Neon Auth

Managed authentication that branches with your database

**Note: Beta**

The **Neon Auth with Better Auth** is in Beta. Share your feedback on [Discord](https://discord.gg/92vNTzKDGp) or via the [Neon Console](https://console.neon.tech/app/projects?modal=feedback).

Neon Auth is the managed authentication service in the Neon backend for apps and agents. It stores users, sessions, and auth configuration directly in your Neon database. When you branch your database, your entire auth state branches with it, so you can test real authentication workflows in preview environments.

## Quick start guides

Choose your framework to get started:

- [Next.js](https://neon.com/docs/auth/quick-start/nextjs-api-only): Quick start with API methods
- [React](https://neon.com/docs/auth/quick-start/react): Quick start with API methods
- [TanStack Router](https://neon.com/docs/auth/quick-start/tanstack-router): With UI components

## Set up with your AI editor

The fastest way to connect your editor to Neon Auth is to run `npx neon@latest init` from your project root:

```bash
npx neon@latest init
```

This command configures the [Neon MCP server](https://neon.com/docs/ai/neon-mcp-server) and installs **[Agent Skills](https://neon.com/docs/ai/agent-skills)** (`neon-postgres`) in your project. Together they help you set up Neon Auth in two ways:

1. **Configure Neon Auth on your branch (MCP).** After `init`, ask your assistant to enable and configure auth in natural language. The MCP server exposes:

   - `provision_neon_auth`: Enable Neon Auth on a branch
   - `configure_neon_auth`: Set OAuth providers, email, sign-in methods, trusted domains, and more
   - `get_neon_auth_config`: Read the current configuration

   See [Neon MCP Server: Neon Auth tools](https://neon.com/docs/ai/neon-mcp-server#supported-actions-tools) for details.

2. **Add Neon Auth to your application (Agent Skills).** Skills teach your assistant how to install the SDK, environment variables, and routes for your framework. Use the quick start guides on this page, or ask your assistant directly.

**Example prompt:**

```text
Set up Neon Auth for my project. Enable Google OAuth and email/password sign-in,
and set the application name to "My App".
```

You can also enable Neon Auth in the [Neon Console](https://console.neon.tech) (Project → Branch → Auth) and configure settings manually.

## Why Neon Auth?

- **Identity lives in your database**  
  All authentication data is stored in the `neon_auth` schema. It's queryable with SQL and compatible with Row Level Security (RLS) policies.

- **Zero server management**  
  Neon Auth runs as a managed REST API service. Configure settings in the Console; use the [client SDK](https://neon.com/docs/reference/javascript-sdk) or [server SDK](https://neon.com/docs/auth/reference/nextjs-server) in your app. No infrastructure to maintain.

- **Auth that branches with your data**  
  Test sign-up, login, password reset, and OAuth flows in isolated branches without touching production data.

## Built on Better Auth

Neon Auth is powered by [Better Auth](https://www.better-auth.com/), which means you get familiar APIs. You can use Better Auth UI components or call auth methods directly to build your own UI.

Neon Auth currently supports Better Auth version **1.4.18**.

### When to use Neon Auth vs. self-hosting Better Auth

Neon Auth is a managed authentication service built into Neon's architecture:

- **Branch-aware authentication**: Every Neon branch gets its own isolated auth environment, so you can test authentication features without affecting your production branch.
- **Built-in Data API integration**: JWT token validation for the Data API has native support for Neon Auth.
- **No infrastructure to manage**: Neon Auth is deployed in the same region as your database, reducing latency without requiring you to run auth infrastructure.
- **Shared OAuth credentials for testing**: Get started quickly with out-of-the-box Google OAuth credentials, eliminating the setup complexity for testing and prototyping.

Self-hosting Better Auth makes sense if you need:

- Flexibility in auth configuration: custom plugins, hooks, and options not yet supported by Neon Auth.
- Full control over your auth code and the ability to run it inside your own infrastructure.

For more details on the SDK differences between `@neondatabase/auth` and `better-auth/client`, see [Why use @neondatabase/auth over better-auth/client](https://github.com/neondatabase/neon-js/blob/main/packages/auth/neon-auth_vs_better-auth.md).

As Neon Auth evolves, more Better Auth integrations and features will be added. Check the [roadmap](https://neon.com/docs/auth/roadmap) to see what's currently supported and what's coming next.

## Basic usage

Enable Auth in the Neon Console or [with your AI editor](https://neon.com/docs/auth/overview#set-up-with-your-ai-editor), then add authentication to your app.

**For Next.js (server-side):**

See the [Next.js Server SDK reference](https://neon.com/docs/auth/reference/nextjs-server) for complete API documentation.

```typescript filename="lib/auth/server.ts"
import { createNeonAuth } from '@neondatabase/auth/next/server';

export const auth = createNeonAuth({
  baseUrl: process.env.NEON_AUTH_BASE_URL!,
  cookies: { secret: process.env.NEON_AUTH_COOKIE_SECRET! },
});
```

```typescript filename="app/api/auth/[...path]/route.ts"
import { auth } from '@/lib/auth/server';

export const { GET, POST } = auth.handler();
```

**For React/Vite (client-side):**

See the [Client SDK reference](https://neon.com/docs/reference/javascript-sdk) for complete API documentation.

```typescript filename="src/auth.ts"
import { createAuthClient } from '@neondatabase/neon-js/auth';

export const authClient = createAuthClient(import.meta.env.VITE_NEON_AUTH_URL);
```

```tsx filename="src/App.tsx"
import { NeonAuthUIProvider, AuthView } from '@neondatabase/auth-ui';
import { authClient } from './auth';

export default function App() {
  return (
    <NeonAuthUIProvider authClient={authClient}>
      <AuthView pathname="sign-in" />
    </NeonAuthUIProvider>
  );
}
```

## Use cases

- **Production authentication**  
  Use Neon Auth as the identity system for your app. Store users, sessions, and OAuth configuration directly in Postgres, and pair with RLS for secure, database-centric access control.

- **Preview environments**  
  Test full authentication flows in Vercel previews with real users and sessions

- **Multi-tenant SaaS**  
  Test complex org and role hierarchies safely in isolated branches

- **CI/CD workflows**  
  Run end-to-end auth tests without touching production. The [Neon Create Branch GitHub Action](https://github.com/marketplace/actions/neon-create-branch-github-action) supports retrieving branch-specific auth URLs for testing authentication flows in GitHub Actions workflows.

- **Development workflows**  
  Spin up complete environments instantly with database and auth together

See [Branching authentication](https://neon.com/docs/auth/branching-authentication) for details on how auth branches with your database.

## Example applications

Beyond the quick starts on this site, the [neondatabase/neon-js](https://github.com/neondatabase/neon-js) monorepo ships **more runnable Neon Auth and `neon-js` samples** under [`examples/`](https://github.com/neondatabase/neon-js/tree/main/examples), including plugin demos (see [Plugins](https://neon.com/docs/auth/guides/plugins#example-applications)), Next.js and React apps, cross-subdomain setups, alternative UI stacks, and Data API patterns. Each folder includes its own README (many workflows use **bun** from the repository root). Browse there when you want a full project to clone next to the guides here.

## Availability

Neon Auth is currently available for AWS regions only. Azure support is not yet available.

Neon Auth does not currently support projects with [IP Allow](https://neon.com/docs/manage/projects#configure-ip-allow) or [Private Networking](https://neon.com/docs/guides/neon-private-networking) enabled.

## Pricing

Neon Auth is included in all Neon plans based on Monthly Active Users (MAU):

- **Free**: Up to 60,000 MAU
- **Launch**: Up to 1M MAU
- **Scale**: Up to 1M MAU

An MAU (Monthly Active User) is a unique user who authenticates at least once during a monthly billing period. If you need more than 1M MAU, request an increase in the [console feedback form](https://console.neon.tech/app/settings?modal=feedback\&modalparams=%22Neon%20auth%20limit%20increase%22).

See [Neon plans](https://neon.com/docs/introduction/plans#auth) for more details.

## Migration from Stack Auth

If you're using the previous Neon Auth implementation via Stack Auth, your version will continue to work. When you're ready to migrate to the new Better Auth implementation, see our [migration guide](https://neon.com/docs/auth/migrate/from-legacy-auth).

---

## Related docs (Introduction)

- [Authentication Flow](https://neon.com/docs/auth/authentication-flow)
- [Branching Authentication](https://neon.com/docs/auth/branching-authentication)
- [Roadmap](https://neon.com/docs/auth/roadmap)

## Neon API — https://neon.com/docs/reference/api-reference.md
> This page location: Tools & Workflows > API, CLI & SDKs
> Full Neon documentation index: https://neon.com/docs/llms.txt

> Summary: The Neon API (REST, base URL https://console.neon.tech/api/v2/) lets developers create and manage projects, branches, databases, roles, and compute endpoints programmatically, mirroring every action available in the Neon Console. Use this page to get an API key, authenticate with Bearer tokens, and understand constraints like rate limits, async operation polling, and branch deletion rules before building automation or CI/CD pipelines. Neon supports multiple API key scopes (personal, organization, and project-scoped), TypeScript and Python SDKs, an OpenAPI 3.0 spec, and an index of API examples covering branching, read replicas, snapshots, schema diff, and data anonymization.

# Neon API

Copy into your AI assistant to get an API key and make your first API call. [View prompt](https://neon.com/prompts/neon-api-prompt.md)

The Neon API allows you to manage your Neon projects programmatically. You can create and manage projects, branches, databases, roles, compute endpoints, and more. Everything you can do in the Neon Console, you can do with the API.

## Quick links

- [Neon API Reference](https://api-docs.neon.tech/reference/getting-started-with-neon-api): Interactive API documentation with "Try It" feature
- [OpenAPI Specification](https://neon.com/api_spec/release/v2.json): Machine-readable API spec (OpenAPI 3.0)
- [Neon SDKs](https://neon.com/docs/reference/sdk): TypeScript and Python SDKs for the Neon API

## Getting started

### Prerequisites

Before using the Neon API, you need:

1. **A Neon account**: [Sign up](https://console.neon.tech/signup) if you don't have one
2. **An API key**: Create one in the Neon Console (see below)
3. **curl or an HTTP client**: Or use our [TypeScript](https://neon.com/docs/reference/typescript-sdk) or [Python](https://neon.com/docs/reference/python-sdk) SDKs

### API key types

Neon supports three types of API keys, each with different scopes:

| Key Type                   | Scope                                  | Best For                      |
| -------------------------- | -------------------------------------- | ----------------------------- |
| **Personal API Key**       | All projects you own or have access to | Personal development, scripts |
| **Organization API Key**   | All projects within an organization    | Team automation, CI/CD        |
| **Project-scoped API Key** | Single project only                    | Limited access integrations   |

Create your first API key in the Neon Console under **Account settings** > **API keys**. For detailed instructions, see [Manage API keys](https://neon.com/docs/manage/api-keys).

**Important:** API key tokens are shown only once at creation. Store them securely; you cannot retrieve them later.

### Base URL

All API requests use this base URL:

```text
https://console.neon.tech/api/v2/
```

### Authentication

Include your API key in the `Authorization` header using Bearer authentication:

```bash
curl 'https://console.neon.tech/api/v2/projects' \
  -H 'Accept: application/json' \
  -H "Authorization: Bearer $NEON_API_KEY"
```

## Make your first API call

Set your API key as an environment variable, then list your projects:

**curl**

```bash
# Set your API key
export NEON_API_KEY="your-api-key-here"

# List all projects
curl 'https://console.neon.tech/api/v2/projects' \
  -H 'Accept: application/json' \
  -H "Authorization: Bearer $NEON_API_KEY" | jq
```

**TypeScript SDK**

```bash
npm install @neondatabase/api-client
```

```typescript
import { createApiClient } from '@neondatabase/api-client';

const apiClient = createApiClient({
  apiKey: process.env.NEON_API_KEY!,
});

async function listProjects() {
  const response = await apiClient.listProjects({});
  console.log(response.data.projects);
}

listProjects();
```

**Python SDK**

```bash
pip install neon-api
```

```python
import os
from neon_api import NeonAPI

neon = NeonAPI(api_key=os.environ["NEON_API_KEY"])

projects = neon.projects()
print(projects)
```

The response includes your projects with their IDs, regions, and other details:

```json
{
  "projects": [
    {
      "id": "spring-example-302709",
      "name": "my-project",
      "region_id": "aws-us-east-2",
      "pg_version": 17,
      "created_at": "2024-01-15T10:30:00Z"
    }
  ]
}
```

Use the `project_id` from the response to make subsequent requests, such as creating a branch:

**curl**

```bash
curl -X POST 'https://console.neon.tech/api/v2/projects/spring-example-302709/branches' \
  -H 'Accept: application/json' \
  -H "Authorization: Bearer $NEON_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"branch": {"name": "dev-branch"}}'
```

**TypeScript SDK**

```typescript
const response = await apiClient.createProjectBranch('spring-example-302709', {
  branch: { name: 'dev-branch' },
});
console.log(response.data.branch);
```

**Python SDK**

```python
branch = neon.branch_create(
    project_id="spring-example-302709",
    branch={"name": "dev-branch"}
)
print(branch)
```

## Key concepts

### Asynchronous operations

Many Neon API operations (creating branches, starting computes, etc.) are asynchronous. The API response includes an `operations` array with status information:

```json
"operations": [
  {
    "id": "22acbb37-209b-4b90-a39c-8460090e1329",
    "action": "create_branch",
    "status": "running"
  }
]
```

**Status values:** `scheduling`, `running`, `finished`, `failed`, `cancelling`, `cancelled`, `skipped`

When building automation, poll the operation status before proceeding with dependent requests:

```bash
curl 'https://console.neon.tech/api/v2/projects/{project_id}/operations/{operation_id}' \
  -H "Authorization: Bearer $NEON_API_KEY"
```

For details, see [Poll operation status](https://neon.com/docs/manage/operations#poll-operation-status).

### Rate limiting

- **700 requests per minute** (approximately 11 per second)
- **40 requests per second** burst limit per route
- **Organization API key creation** (`POST /organizations/{org_id}/api_keys`): 10 requests per second. Throttle requests or use retries with backoff when creating many keys. See [Manage organizations using the Neon API](https://neon.com/docs/manage/orgs-api) and [Manage API keys](https://neon.com/docs/manage/api-keys).

Exceeding these limits returns `HTTP 429 Too Many Requests`. Implement retry logic with exponential backoff in your applications.

### Pagination

Some endpoints that return lists support cursor-based pagination. Include `limit` and `cursor` parameters:

```bash
# First request with limit
curl 'https://console.neon.tech/api/v2/projects?limit=10' ...

# Subsequent request with cursor from previous response
curl 'https://console.neon.tech/api/v2/projects?limit=10&cursor=...' ...
```

### Important constraints

Keep these constraints in mind when building automation with the Neon API:

- You **cannot delete** a project's root or default branch.
- You **cannot delete** a branch that has child branches. Delete all children first.
- Creating a new role **may drop existing connections** to the active compute endpoint.
- A branch can have only one `read_write` endpoint but multiple `read_only` endpoints.
- Neon limits overlapping **operations** on a project. One response may still list several operations when they belong to the same request. Requests that try to schedule new work while conflicting operations are still running return `423 Locked`. Retry with exponential backoff, or poll for completion first. See [Handle concurrent operation errors](https://neon.com/docs/manage/operations#handle-concurrent-operation-errors).
- Operations older than 6 months may be removed from Neon's systems.

## SDKs and tools

Instead of using curl, you can use our official SDKs:

- **[TypeScript SDK](https://neon.com/docs/reference/typescript-sdk)**: Full-featured SDK for Node.js and browser
- **[Python SDK](https://neon.com/docs/reference/python-sdk)**: Pythonic wrapper for the Neon API
- **[Neon CLI](https://neon.com/docs/cli)**: Command-line interface for Neon

See [Neon SDKs](https://neon.com/docs/reference/sdk) for the full list, including community SDKs.

## API reference documentation

The interactive [Neon API reference](https://api-docs.neon.tech/reference/getting-started-with-neon-api) provides:

- Complete endpoint documentation
- Request/response examples
- "Try It" feature to execute requests directly
- Schema definitions for all objects

You can also access the [OpenAPI specification](https://neon.com/api_spec/release/v2.json) directly for code generation or API tooling.

## API examples index

The following sections link to API examples and guides throughout the Neon documentation, organized by resource type and use case.

### Core resources

Manage the fundamental building blocks of your Neon account.

- [Manage API keys](https://neon.com/docs/manage/api-keys#manage-api-keys-with-the-neon-api): Create, list, and revoke API keys for personal accounts and organizations
- [Manage projects](https://neon.com/docs/manage/projects#manage-projects-with-the-neon-api): Create, list, update, delete, and recover projects
- [Manage branches](https://neon.com/docs/manage/branches#branching-with-the-neon-api): Create, list, and delete branches
- [Manage computes](https://neon.com/docs/manage/computes#manage-computes-with-the-neon-api): Create, configure, restart, and delete compute endpoints
- [Manage roles](https://neon.com/docs/manage/roles#manage-roles-with-the-neon-api): Create roles, reset passwords, and manage database access
- [Manage databases](https://neon.com/docs/manage/databases#manage-databases-with-the-neon-api): Create, list, update, and delete databases
- [View operations](https://neon.com/docs/manage/operations#operations-and-the-neon-api): List operations, check status, and poll for completion
- [Maintenance windows](https://neon.com/docs/manage/updates#updates-on-paid-plans): Configure maintenance windows for compute updates via API
- [Organizations API](https://neon.com/docs/manage/orgs-api): Manage organization members and permissions
- [Project transfer](https://neon.com/docs/manage/orgs-project-transfer#transfer-projects-with-the-api): Transfer projects between accounts and organizations

### Usage and billing

Monitor resource consumption and configure usage limits.

- [Monitor billing and usage](https://neon.com/docs/introduction/monitor-usage): Where to see usage and costs in the Console; links to consumption API for programmatic access
- [Query consumption metrics](https://neon.com/docs/guides/consumption-metrics): Query project consumption metrics for usage-based plans. For legacy account and project endpoints, see [Query consumption metrics (legacy)](https://neon.com/docs/guides/consumption-metrics-legacy).
- [Organization consumption](https://neon.com/docs/manage/orgs-api-consumption#account-level-metrics): Query usage metrics for organizations
- [Configure consumption limits](https://neon.com/docs/guides/consumption-limits#configuring-quotas): Set and update quotas on compute, storage, and data transfer

### Branching workflows

Work with branches programmatically for development, testing, and CI/CD.

- [Branching with the Neon API](https://neon.com/docs/guides/branching-neon-api): Comprehensive guide to branch management via API
- [Branch restore](https://neon.com/docs/introduction/branch-restore#how-to-use-instant-restore): Restore branches to a previous state using Time Travel
- [Branch expiration](https://neon.com/docs/guides/branch-expiration#creating-a-branch-with-expiration): Automatically delete branches after a specified time
- [Schema-only branches](https://neon.com/docs/guides/branching-schema-only#creating-schema-only-branches): Create branches with schema but no data
- [Reset from parent](https://neon.com/docs/guides/reset-from-parent#how-to-reset-from-parent): Reset a branch to match its parent's current state
- [Protected branches](https://neon.com/docs/guides/protected-branches#define-an-ip-allowlist-for-your-project): Configure IP allowlist restrictions for protected branches
- [Branching for testing](https://neon.com/docs/guides/branching-test-queries#create-a-test-branch): Create isolated branches for running test queries
- [Branch archiving](https://neon.com/docs/guides/branch-archiving#monitoring-branch-archiving): Monitor branch archive status via API

### Snapshots and backup

Create and manage point-in-time snapshots for backup and versioning.

- [Backup and restore](https://neon.com/docs/guides/backup-restore#create-snapshots-manually): Create scheduled and on-demand snapshots
- [Database versioning](https://neon.com/docs/ai/ai-database-versioning#creating-snapshots): Create and manage snapshots via API for version control

### Data management

Transform and compare data across branches.

- [Data anonymization API](https://neon.com/docs/workflows/data-anonymization-api#create-anonymized-branch): Create anonymized copies of production data with masking rules
- [Data anonymization workflow](https://neon.com/docs/workflows/data-anonymization#create-a-branch-with-anonymized-data): End-to-end guide for setting up data anonymization
- [Schema comparison](https://neon.com/docs/guides/schema-diff#using-the-neon-api): Compare schemas between branches via API
- [Schema diff tutorial](https://neon.com/docs/guides/schema-diff-tutorial#view-the-schema-differences): Step-by-step schema comparison guide with API example

### Read replicas

Scale read operations with dedicated read-only compute endpoints.

- [Read replicas overview](https://neon.com/docs/introduction/read-replicas#manage-read-replicas-using-the-neon-api): List and manage read replica endpoints
- [Create read replicas](https://neon.com/docs/guides/read-replica-guide#create-a-read-replica-using-the-api): Create, configure, and delete read replica computes
- [Read replicas for data analysis](https://neon.com/docs/guides/read-replica-data-analysis#create-a-read-replica): Create read replicas for analytics workloads
- [Read replicas for ad-hoc queries](https://neon.com/docs/guides/read-replica-adhoc-queries#setting-up-a-read-replica-for-ad-hoc-queries): Create read replicas for exploratory queries

### Security and compliance

Configure security features and compliance settings.

- [HIPAA compliance](https://neon.com/docs/security/hipaa#step-2-enable-hipaa-for-your-projects): Create and configure HIPAA-compliant projects via API
- [API key management](https://neon.com/docs/manage/api-keys): Secure API key handling for personal and organization accounts

---

## Related docs (Tools & Workflows)

- [Local development](https://neon.com/docs/local/neon-local)
- [Integrations (3rd party)](https://neon.com/docs/guides/integrations)
- [Workflows & CI/CD](https://neon.com/docs/reference/claimable-postgres)
- [Templates](https://neon.com/docs/https://neon.com/templates)
- [Examples repo](https://neon.com/docs/https://github.com/neondatabase/examples)

## Scale to Zero — https://neon.com/docs/introduction/scale-to-zero.md
> This page location: Scale to zero
> Full Neon documentation index: https://neon.com/docs/llms.txt

> Summary: Scale to Zero suspends inactive Neon Postgres computes after 5 minutes and reactivates them in milliseconds on the next query, so you pay only for active compute time. Use this feature for development, test, or intermittently active production databases where always-on compute is unnecessary. Free plan users cannot disable it, but paid plan users can. Very large computes remain always active and are not eligible for scale to zero.

# Scale to Zero

Minimize costs by automatically scaling inactive databases to zero

Neon's _Scale to Zero_ feature suspends the Neon compute that runs your Postgres database after a period of inactivity, which minimizes costs for databases that aren't always active, such as development or test environment databases, and even production databases that aren't used 24/7.

- When your database is inactive, it automatically scales to zero after 5 minutes. This means you pay only for active time instead of 24/7 compute usage. No manual intervention is required.
- Once you query the database again, it reactivates automatically within a few hundred milliseconds.

The diagram below illustrates the _Scale to Zero_ behavior alongside Neon's _Autoscaling_ feature. The compute usage line highlights an _inactive_ period, followed by a period where the compute is automatically suspended until it's accessed again.

![Compute metrics graph](https://neon.com/docs/introduction/compute-usage-graph.jpg)

Neon compute scales to zero after an _inactive_ period of 5 minutes. For Neon Free plan users, this setting is fixed. Paid plan users can disable the scale-to-zero setting to maintain an always-active compute.

**Note:** Scale to zero is only available for computes up to 16 CU in size. Computes larger than 16 CU remain always active to ensure best performance.

You can enable or disable the scale-to-zero setting by editing your compute settings. For detailed instructions, see [Configuring scale to zero for Neon computes](https://neon.com/docs/guides/scale-to-zero-guide).

[Logical replication](https://neon.com/docs/guides/logical-replication-guide) **from** Neon keeps compute active while subscribers are connected, so the database does not scale to zero. See [Logical replication in Neon](https://neon.com/docs/guides/logical-replication-neon#important-notices) for details.

---

## Related docs (Scale to zero)

- [Scale to zero guide](https://neon.com/docs/guides/scale-to-zero-guide)

