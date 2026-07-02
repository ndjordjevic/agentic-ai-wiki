---
type: source
source_url: https://lovable.dev/
tags:
  - vibe-coding
  - full-stack-app-builder
  - github-sync
  - lovable-cloud
  - workspace-skills
  - subagents
  - browser-testing
  - enterprise-governance
related:
  - retool.com
  - open-design.ai
  - the-new-sdlc-with-vibe-coding
  - bolt.new
  - producthunt.com
  - voltagent-awesome-design-md
product: lovable
detail_level: standard
created: 2026-07-01
updated: 2026-07-02
---

Lovable is a hosted full-stack AI app builder that turns natural-language prompts into editable web applications, then keeps the whole delivery loop inside one product: planning, autonomous implementation, manual code inspection, GitHub sync, testing, publishing, and a managed backend runtime. It matters for this wiki because it productizes several agentic-engineering patterns in a mainstream SaaS surface — Build mode as an execution agent, Plan mode as a pre-implementation reasoning mode, reusable skills, read-only subagents, and a Supabase-backed cloud layer that lets the agent provision database/auth/storage infrastructure without leaving the workspace.

_All claims below are sourced from ../../raw/web/lovable.dev.md unless otherwise noted._

## What it does

Lovable lets users describe an app, site, or internal tool in chat and receive a working codebase with frontend, backend, database, authentication, and integrations already wired in. The product is organized around shared workspaces containing one or more projects; each project is a single application that can stay inside Lovable, sync to GitHub, or ship to a live lovable.app or custom-domain deployment. The official docs position it for founders, product and design teams, agencies, developers, and enterprises building anything from MVPs and marketing sites to multi-user SaaS products and operational dashboards.

## Key features

- **Build mode** — Lovable's autonomous execution mode implements changes directly in the project, explores the codebase, resolves issues during development, and exposes visible task progress with file diffs and tool traces.
- **Plan mode** — a separate reasoning mode for investigation, comparison, and structured planning before code is changed.
- **Code editor** — paid plans can inspect and edit files directly, search the project tree, preview Markdown, and reference exact files or line ranges back into chat.
- **GitHub round-trip sync** — projects can sync to GitHub with branch-aware two-way updates so teams can keep using pull requests, local IDEs, and external deployments.
- **Lovable Cloud** — managed database, auth, storage, edge functions, jobs, AI features, secrets, logs, and usage analytics built on Supabase's open-source foundation.
- **Skills** — workspace-level markdown playbooks that load on demand, can be slash-invoked, and can be imported from GitHub or ZIP bundles.
- **Subagents** — temporary read-only investigators that parallelize research, code exploration, and review without modifying the project themselves.
- **Verification + security** — browser testing, frontend tests, edge-function verification, basic/deep security scans, optional pentest/security integrations, and publish-time security checks.

## Architecture and concepts

Lovable's core unit is the **workspace/project** model: a workspace holds members, settings, and reusable assets such as skills, while a project is the actual app being built. Around that sits a clear division of labor between **Plan mode** (decide) and **Build mode** (execute). Build mode is not described as a pure code generator; it is a task-oriented agent that can inspect files, apply coordinated edits, queue work, and use verification tools when asked.

The runtime side is **Lovable Cloud**, which gives the agent a managed backend surface instead of leaving infrastructure as an exercise for the user. It bundles database, auth, storage, edge functions, jobs, secrets, and logs behind permission controls and regional hosting options, while the docs explicitly say it rides on Supabase's open-source foundation. That makes Lovable closer to an opinionated full-stack app platform than to a narrow frontend generator.

On the collaboration side, GitHub integration is modeled as a **workspace connection** plus a **project repository connection**, which is how Lovable shares one GitHub installation across many projects while still tracking branch-level sync per app. On the agent-behavior side, Lovable splits persistent instruction layers into **knowledge** (always on) and **skills** (loaded on demand), then adds **subagents** as read-only parallel researchers. That combination gives it a recognizable agentic stack: static context, dynamic procedural context, autonomous execution, delegated investigation, and post-change verification.

## Main APIs

- **Build with URL** — the docs index exposes a Lovable API beta entry for building and sharing apps from simple URLs.
- **Lovable Cloud edge functions** — the main server-side API surface for app developers; Lovable can generate and operate these from chat for custom backend logic.
- **GitHub integration** — not a public REST API for Lovable itself, but a key programmable surface for exporting code, branching, syncing, and collaborating outside the product.
- **Connectors and integrations** — the documentation emphasizes connectors, MCP servers, and third-party APIs as the way Lovable apps gain external capabilities and real data.

Lovable is fundamentally a workspace product rather than an API-first developer platform, so most of its important interfaces are operational surfaces inside the product rather than a single canonical public SDK.

## When to use

- You want to move from prompt to working full-stack web app quickly without separately assembling frontend, backend, auth, storage, deployment, and verification tooling.
- You need a hosted path from prototype to governed production app, with GitHub sync and security controls available when the work matures.
- Your team benefits from shared procedural context such as reusable skills and from built-in exploratory helpers such as subagents.
- You want a concrete product embodiment of the transition from ad hoc vibe coding to more disciplined agentic engineering described in [[the-new-sdlc-with-vibe-coding]].
- **Compared with [[retool.com]]**, Lovable is broader and more end-user-app oriented, while Retool is more explicitly optimized for governed internal software, workflows, and agents on top of existing enterprise data.
- **Compared with [[open-design.ai]]**, Lovable is a hosted full-stack app platform, while Open Design is a local-first agent-native design system focused on artifact generation rather than end-to-end application hosting and delivery.

## Ecosystem

Lovable sits on top of several adjacent ecosystems rather than trying to replace them. GitHub is the escape hatch and collaboration substrate; Supabase provides the open-source backend foundation behind Lovable Cloud; external connectors and MCP-style tools expand what Lovable-built apps can do; and workspace skills give teams a portable way to encode procedures across projects. The product also fits naturally beside other agentic-development references in this wiki: [[retool.com]] covers the enterprise internal-tooling side of AI app builders, [[open-design.ai]] covers agent-native design generation, and [[the-new-sdlc-with-vibe-coding]] supplies the conceptual frame for why tools like Lovable are becoming central to modern AI-assisted software delivery.
