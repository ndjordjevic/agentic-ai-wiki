# docusaurus.io

## Fetch log
- Inbox URL: https://docusaurus.io/
- Final URL: https://docusaurus.io/
- Fetched: 2026-07-08
- Pages: 8
- Mode: standard

## Landing page — https://docusaurus.io/

Build optimized websites quickly, focus on your content | Docusaurus

🎉 Docusaurus 3.10 is out!️ 🥳

# Build optimized websites quickly, focus on your content

Get Started | Try a Demo

### Powered by MDX
Save time and focus on text documents. Simply write docs and blog posts with MDX, and Docusaurus builds them into static HTML files ready to be served. You can even embed React components in your Markdown thanks to MDX.

### Built Using React
Extend and customize your project's layout by writing React components. Leverage the pluggable architecture, and design your own site while reusing the same data created by Docusaurus plugins.

### Ready for Translations
Localization comes out-of-the-box. Use git, Crowdin, or any other translation manager to translate your docs and deploy them individually.

### Document Versioning
Support users on all versions of your project. Document versioning helps you keep documentation in sync with project releases.

### Content Search
Make it easy for your community to find what they need in your documentation. We proudly support Algolia documentation search.

**Navigation:** Docs | API | Blog | Showcase | Community | GitHub (https://github.com/facebook/docusaurus)

**Version dropdown:** 3.10.1 (current), Canary, 3.9.2, 3.8.1, … archived versions back to 1.x.x

**Testimonials:** Redux, Supabase, Testing Library, Temporal, and others use Docusaurus for documentation sites.

## Docs — https://docusaurus.io/docs

Introduction | Docusaurus — Version 3.10.1

⚡️ Docusaurus will help you ship a beautiful documentation site in no time.
💸 Building a custom tech stack is expensive. Instead, focus on your content and just write Markdown files.
💥 Ready for more? Use advanced features like versioning, i18n, search and theme customizations.

🧐 Docusaurus is a static-site generator. It builds a single-page application with fast client-side navigation, leveraging the full power of React to make your site interactive. It provides out-of-the-box documentation features but can be used to create any kind of site (personal website, product, blog, marketing landing pages, etc).

### Fast Track
```bash
npx create-docusaurus@latest my-website classic
cd my-website
npx docusaurus start
```
Open http://localhost:3000 — or use docusaurus.new to test in browser.

### Features
- Built with React — extend with custom React components
- Pluggable — bootstrap with preset-classic, add plugins
- Developer experience — hot reloading, route-based code splitting, universal config entry point
- SEO friendly — static HTML per path, page-specific SEO
- Powered by MDX — interactive components in Markdown
- i18n, PRPL performance pattern, accessibility

### Design principles
- Little to learn (minimal API surface)
- Intuitive project structure
- Layered architecture (content/theming/styling separation)
- Sensible defaults
- No vendor lock-in

### Comparison with other tools
Gatsby, Next.js/Nextra, VitePress, MkDocs, Docsify, GitBook, Jekyll, Rspress — Docusaurus focuses specifically on documentation sites with out-of-the-box docs features.

## Installation — https://docusaurus.io/docs/installation

**Requirements:** Node.js 20.0+

```bash
npx create-docusaurus@latest my-website classic
# TypeScript variant:
npx create-docusaurus@latest my-website classic --typescript
```

**Classic template** includes `@docusaurus/preset-classic`: docs, blog, custom pages, CSS framework with dark mode.

**Project structure (classic):**
```
my-website/
├── blog/
├── docs/
├── src/pages/
├── static/
├── docusaurus.config.js
├── sidebars.js
└── package.json
```

**Dev server:** `npm run start` → http://localhost:3000
**Build:** `npm run build` → `/build` static output
**Monorepo:** run `npx create-docusaurus` inside monorepo root; set hosting `Base directory` to `./website` on Netlify/Vercel.

## Using Plugins — https://docusaurus.io/docs/using-plugins

Docusaurus core provides no features alone — all features come from plugins (docs, blog, pages) bundled in presets.

**@docusaurus/preset-classic** includes:
- @docusaurus/theme-classic
- @docusaurus/theme-search-algolia
- @docusaurus/plugin-content-docs
- @docusaurus/plugin-content-blog
- @docusaurus/plugin-content-pages
- @docusaurus/plugin-debug
- @docusaurus/plugin-google-gtag / google-tag-manager
- @docusaurus/plugin-sitemap
- @docusaurus/plugin-svgr

Plugins configured in `docusaurus.config.js` `plugins` or `presets` arrays. Multi-instance plugins need unique `id`. Themes loaded same way as plugins.

Module shorthands resolve `[name]` → `@docusaurus/plugin-[name]` etc.

## Deployment — https://docusaurus.io/docs/deployment

```bash
npm run build   # emits static files to build/
npm run serve   # test locally at localhost:3000
```

Required config: `url` and `baseUrl` in docusaurus.config.js.

Hosting options: Vercel, GitHub Pages, Netlify, Render, Surge, self-hosted Apache/Nginx.

`trailingSlash` config varies by host — use slorber/trailing-slash-guide.

Environment variables: only `docusaurus.config.js` has Node access; pass to client via `customFields`.

GitHub Pages, Netlify, Vercel each have dedicated deployment guides with `docusaurus deploy` CLI support.

## i18n - Introduction — https://docusaurus.io/docs/i18n/introduction

Goals: simple filesystem-based translations, flexible workflows (Git, Crowdin, FTP), modular per-plugin i18n, low-overhead runtime, scalable independent locale builds, RTL support, default theme label translations.

Translation file types:
1. **Markdown/MDX** — whole-document translation
2. **JSON** (Chrome i18n format) — React code labels, themeConfig navbar/footer, plugin option labels
3. **Data files** — e.g. `authors.yml` for blog

Location: `website/i18n/[locale]/[pluginName]/...`

CLI: `docusaurus write-translations` initializes JSON files.

## Versioning — https://docusaurus.io/docs/versioning

```bash
npm run docusaurus docs:version 1.1.0
```

Creates `versioned_docs/version-X/`, `versioned_sidebars/`, appends to `versions.json`.

**Warning:** versioning increases build time and complexity — only for high-traffic docs with rapid version changes.

Key concepts: **current version** (./docs folder), **latest version** (default /docs route via `lastVersion`).

Config options: `includeCurrentVersion`, `lastVersion`, `onlyIncludeVersions`, per-version `label`/`path`/`banner`/`badge`.

Navbar items: `doc`, `docSidebar`, `docsVersion`, `docsVersionDropdown`.

Best practices: don't version patch releases; keep <10 versions; use `@site` imports; link docs with `.md` extensions.

## Search — https://docusaurus.io/docs/search

Options:
- 🥇 Algolia DocSearch (official, free for OSS docs)
- Typesense DocSearch
- Local search plugins (community)
- Custom `SearchBar` via swizzle

Algolia: apply to DocSearch program; crawler runs weekly; preset-classic includes `@docusaurus/theme-search-algolia`.

`themeConfig.algolia`: `appId`, `apiKey`, `indexName`, `contextualSearch` (default true — filters by language/version), `askAi` for conversational search.

Contextual search creates facet filters on `docusaurus_tag`, `language`, `version`, `type`.

Swizzle: `npm run swizzle @docusaurus/theme-search-algolia SearchBar`
