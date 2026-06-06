---
type: source
source_url: https://www.canva.com/
tags:
  - mcp-server
  - visual-design
  - ai-assistant
  - connect-api
  - apps-sdk
  - brand-management
  - design-automation
  - canva-ai
related:
  - sequentialthinking-mcp
product: canva
detail_level: standard
created: 2026-05-02
updated: 2026-05-02
---

Canva is an AI-powered visual design platform used by 240 million+ people and teams worldwide to create social media posts, presentations, videos, print products, and more. It matters for this wiki because Canva has added a remote MCP server (`https://mcp.canva.com/mcp`) that exposes its design capabilities as MCP-compatible tools, making it directly usable by AI agents and assistants through the Model Context Protocol. The developer platform (`canva.dev`) also provides Connect APIs for embedding Canva into external platforms and an Apps SDK for building plugins that run inside the Canva editor.

_All claims below are sourced from ../../raw/web/canva.com.md unless otherwise noted._

## What it does

Canva is a browser-based creative suite that consolidates design, writing, video editing, print ordering, and team brand management into one platform. The Visual Suite includes Sheets (data + design), Docs, Whiteboards, Presentations, a Photo Editor, a Video Editor, a Website Builder, and a PDF Editor. Users design with drag-and-drop tools and a library of templates, then publish or export to any channel. Beyond consumer design, Canva provides a developer platform for extending the editor and integrating Canva into third-party products.

## Key features

- **Visual Suite** — Unified workspace covering docs, presentations, whiteboards, video, print, and websites in one product.
- **Canva AI 2.0** — Suite of AI tools embedded throughout: Magic Write (text generation), Magic Layers (image-to-editable layout), Magic Resize (multi-channel resizing), Magic Animate, Magic Eraser, AI Image Generator, AI Video Generator, AI Music Generator, Canva Code (code generation), Magic Insights (AI data analysis), Magic Formulas.
- **Brand Kit** — Stores brand colors, fonts, and logos so all team output stays on-brand; available from Pro plan upward.
- **Apps Marketplace** — 70+ third-party apps installable into the Canva editor; developers can publish via the Apps SDK.
- **MCP Server** — Remote MCP server at `https://mcp.canva.com/mcp` exposing design generation, editing, search, asset management, export, and commenting as MCP tools for AI assistants.
- **Connect APIs** — REST APIs for embedding Canva capabilities (autofill, bulk create, resize, export, comments) into external platforms.
- **SCIM API** — Automated user provisioning for enterprise identity sync.
- **Audit Logs** — Compliance-grade change tracking for enterprise teams.

## Architecture and concepts

Canva's developer surface has three layers. The **Apps SDK** lets developers build JavaScript plugins (running in an iframe inside the editor's object panel) that interact with the editor programmatically, add content to designs, and connect to external backends via the Fetch API. Apps are distributed via the public Apps Marketplace or shared privately within a team. The **Connect APIs** are REST APIs for external integrations — they cover design creation, autofill of brand templates with live data, bulk content generation, resizing, and export; they are appropriate for workflows that live outside the editor. The **MCP Server** is the newest layer: a remote MCP endpoint that wraps Canva's design capabilities in the Model Context Protocol, allowing AI assistants (Claude, ChatGPT, Codex, Gemini, Cursor, VS Code) to call Canva tools through natural language. Authentication uses Dynamic Client Registration (DCR); each user authenticates individually; permissions mirror that user's existing Canva access rights.

Product tiers gate features: all plans support design generation, editing, search, exports, comments, and asset uploads; Pro and above support design resizing; Enterprise adds autofill templates, brand kits, and brand templates.

## Main APIs

- **MCP Server** — `https://mcp.canva.com/mcp` (remote MCP). Supports stdio fallback via `mcp-remote` npm package. Integration requires waitlist approval to register redirect URIs. Tools cover: design generation, editing, discovery, asset management, export (PDF, PNG, JPG, PPTX, MP4), and comments.
- **Connect APIs** — REST. Entry: `https://www.canva.dev/docs/connect/`. Key capabilities: design CRUD, autofill (`/autofill`), bulk create, resizes (`/resizes`), exports, comments (`/comments`), brand templates (`/brand-templates`).
- **Apps SDK** — JavaScript SDK for browser-based editor plugins. Entry: `https://www.canva.dev/docs/apps/`. App UI Kit provides native Canva-style UI components. Starter kit: `github.com/canva-sdks/canva-apps-sdk-starter-kit`.
- **SCIM API** — For enterprise user provisioning. Entry: `https://www.canva.dev/docs/scim/`.
- **Canva CLI** — Command-line tool for creating and managing Canva apps. Entry: `https://www.canva.dev/docs/apps/canva-cli/`.

## When to use

- Teams or products that want to give their users AI-assisted design generation and editing via an existing AI assistant (Claude, ChatGPT, Gemini, Cursor, VS Code) — connect via the MCP server.
- Platforms needing to embed Canva capabilities (autofill branded templates, bulk personalization, export, resize) into their own product without requiring users to visit canva.com — use the Connect APIs.
- Developers building editor plugins that add new tools, data connectors, or content sources inside the Canva editor — use the Apps SDK.
- Enterprise IT teams automating user provisioning — use the SCIM API.
- AI agents in agentic workflows that need to produce design artifacts (social posts, presentations, exported PDFs/images) as part of a multi-step pipeline — the MCP server is the integration point.

## Ecosystem

Canva's developer community hub is at `community.canva.dev`. The Apps Marketplace hosts 70+ third-party integrations. The `canva-sdks` GitHub org publishes the Apps SDK starter kit. A dedicated Canva Dev MCP Server is also available to give AI assistants context about the developer docs themselves (`https://www.canva.dev/docs/apps/mcp-server/`). Enterprise deployments can use partner integrations via `partners.canva.com`. Related MCP tooling in this wiki: [[sequentialthinking-mcp]] documents the Sequential Thinking MCP Server pattern, showing how MCP-compatible tools can be packaged and consumed by the same AI assistants that Canva targets.
