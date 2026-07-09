---
type: source
category: "Infra, hosting, DB & observability"
source_url: https://docusaurus.io/
companion_urls:
  - https://github.com/facebook/docusaurus
raw_files:
  - ../../raw/web/docusaurus.io.md
  - ../../raw/github/facebook-docusaurus.md
tags:
  - static-site-generator
  - documentation-sites
  - mdx
  - react
  - jamstack
  - i18n
  - algolia-docsearch
  - open-source
related:
  - vercel.com
  - render.com
  - aaif-goose-goose
  - skills.sh
  - streamlit.io
product: docusaurus
detail_level: standard
created: 2026-07-08
updated: 2026-07-08
---

Docusaurus is Meta's open-source React static-site generator purpose-built for documentation websites — and usable for blogs, marketing pages, and product sites. Version 3.10.1 pairs a marketing site at docusaurus.io with the `facebook/docusaurus` monorepo (65K+ stars, MIT), delivering MDX authoring, plugin/preset architecture, document versioning, i18n, and first-class Algolia DocSearch integration out of the box. For this wiki's domain, Docusaurus is the canonical choice many agent frameworks and OSS projects use to publish human- and agent-readable docs (including [[aaif-goose-goose]] and references in [[skills.sh]] deployment guides).

_All claims below are sourced from ../../raw/web/docusaurus.io.md unless otherwise noted._

## What it does

Docusaurus builds optimized static websites from Markdown/MDX content with fast client-side navigation as a React single-page application. It targets documentation-first use cases: ship a docs section, blog, and custom pages from the `classic` preset with minimal configuration, then extend via plugins, themes, and React components. The `npx create-docusaurus@latest my-website classic` scaffold and `docusaurus.new` playground lower the barrier to a working docs site in minutes.

The core deliberately delegates all features to plugins — docs, blog, pages, search, sitemap, analytics — typically bundled through `@docusaurus/preset-classic`. Sites compile to static HTML in `build/` for deployment to any Jamstack host.

## Key features

- **MDX-powered content** — write docs and blog posts in Markdown with embedded React components; static HTML output for SEO.
- **Pluggable architecture** — install/configure plugins and themes in `docusaurus.config.js`; multi-instance plugins via unique `id`; module shorthands (`content-docs` → `@docusaurus/plugin-content-docs`).
- **Preset-classic bundle** — docs + blog + pages + classic theme + Algolia search theme + sitemap + SVGR + optional Google analytics tags.
- **Versioning** — `docusaurus docs:version` snapshots docs into `versioned_docs/` with per-version sidebars and navbar dropdown.
- **i18n** — filesystem-based locale folders under `i18n/[locale]/[plugin]/`; Chrome i18n JSON for UI strings; Crowdin-friendly; RTL support.
- **Search** — official Algolia DocSearch integration with contextual search (language/version facets) and optional Ask AI; community Typesense and local-search alternatives.
- **Developer experience** — hot reload, route-based code splitting, universal config entry point, TypeScript template flag.

The companion repo confirms the project scope: "building, deploying, and maintaining open source project websites easily," with localization via Crowdin, customizable pages/styling, and active community channels (Discord, X, GitHub Issues). (../../raw/github/facebook-docusaurus.md)

## Architecture

Docusaurus v2+ is a total rewrite: React SPA with client-side routing, static HTML pre-rendering per route, and a layered separation between content (MDX in `docs/`, `blog/`, `src/pages/`), theming (`@docusaurus/theme-classic`), and styling (Infima CSS + `custom.css`). Design principles emphasize minimal API surface, intuitive directory layout, sensible performance defaults (PRPL pattern), and no vendor lock-in for Markdown engine or CSS choices.

The `facebook/docusaurus` repo is a Lerna + pnpm monorepo: `packages/` holds core and plugins, `examples/` starter templates, `website/` the project's own docs site, with Argos visual regression testing and `AGENTS.md` for agent contributors. (../../raw/github/facebook-docusaurus.md)

Configuration flows through a single `docusaurus.config.js` (the only file with Node.js environment access); client-side code accesses env via `customFields`. `sidebars.js` controls docs navigation; presets relay options to constituent plugins.

## Installation

```bash
npx create-docusaurus@latest my-website classic
cd my-website
npm run start    # dev server at http://localhost:3000
npm run build    # static output in build/
```

Requires Node.js 20+. TypeScript: add `--typescript`. For monorepo doc sites, scaffold inside the monorepo and point the host's base directory at the website folder (e.g. `./website` on Netlify/Vercel). (../../raw/github/facebook-docusaurus.md)

## Example usage

**Plugin configuration** in `docusaurus.config.js`:

```js
export default {
  presets: [
    ['@docusaurus/preset-classic', {
      docs: {},
      blog: {},
      theme: { customCss: ['./src/css/custom.css'] },
    }],
  ],
  themeConfig: {
    algolia: {
      appId: 'YOUR_APP_ID',
      apiKey: 'YOUR_SEARCH_API_KEY',
      indexName: 'YOUR_INDEX_NAME',
      contextualSearch: true,
    },
  },
};
```

**Version a release:** `npm run docusaurus docs:version 1.1.0`

**Deploy:** `npm run build` then push `build/` to Vercel, Netlify, Render, GitHub Pages, or `npm run serve` to preview locally. Set `url` and `baseUrl` correctly for subdirectory deployments.

**Customize search UI:** `npm run swizzle @docusaurus/theme-search-algolia SearchBar`

## When to use

Choose Docusaurus when you want a modern Jamstack documentation site with SPA navigation, MDX, versioning, i18n, and integrated search — without building those features from scratch in Next.js or Gatsby. It fits OSS projects, technical blogs, and product docs that deploy as static files. Prefer alternatives when you need Vue (VitePress), Python-only tooling (MkDocs), non-SPA static sites, or a general-purpose app framework rather than a docs-centric generator.

Many agent-framework projects in this wiki ecosystem publish docs with Docusaurus and deploy to hosts covered by [[vercel.com]] and [[render.com]].

## Maintenance status

`facebook/docusaurus`: **65,531 stars**, **9,959 forks**, TypeScript, **MIT License**, default branch `main`, latest release **3.10.1** (2026-04-30), last push 2026-07-03. Actively maintained by Meta Open Source with Discord, Open Collective backers/sponsors, and CI via GitHub Actions + Argos visual testing. Docusaurus v1 is deprecated; v2+ is the supported line. (../../raw/github/facebook-docusaurus.md)

## Ecosystem

- **Algolia DocSearch** — free hosted search for qualifying OSS docs; weekly crawl; contextual facets by locale/version.
- **Crowdin** — recommended translation workflow; `docusaurus write-translations` CLI for JSON catalogs.
- **Deployment** — first-class guides for GitHub Pages, Netlify, Vercel, Render; `docusaurus deploy` CLI.
- **Showcase** — docusaurus.io/showcase lists production sites (Redux, Supabase, React Native docs, Temporal, Testing Library, etc.).
- **Community plugins** — unofficial plugin list; swizzle pattern for theme overrides.

Docs content is Creative Commons licensed separately from the MIT-licensed code. (../../raw/github/facebook-docusaurus.md)

## Documentation

Official docs at https://docusaurus.io/docs (v3.10.1) cover introduction, installation, plugins/presets/themes, deployment, i18n, versioning, search, blog, markdown features, and CLI API reference at `/docs/cli`. Versioned docs back to 2.x plus archived 1.x on separate hosts.
