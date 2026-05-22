# wasp-lang/open-vibe

## Metadata
- Stars: 36
- Primary language: Astro
- Default branch: main
- Latest release: none
- License: none listed
- Homepage: https://OpenVibe.sh
- Fetched: 2026-05-22
- Final URL: https://github.com/wasp-lang/open-vibe

## Description
Open Vibe turns Claude Code, or your agent of choice, into the ultimate SaaS-building assistant, helping you understand the systems behind a production-ready SaaS while building your own app idea.

## README

# Open Vibe

Open Vibe turns Claude Code, or your agent of choice, into the ultimate SaaS-building assistant, helping you understand the systems behind a production-ready SaaS while building your own app idea on top of the free, open-source SaaS boilerplate template [Open SaaS](https://opensaas.sh), powered by [Wasp](https://wasp.sh).

## Start the course

Paste this prompt into your agent:

> I want to ship my app with Open Vibe. Run `curl -fsSL https://openvibe.sh/llms.txt` and follow the file's instructions.

**Works with:** Claude Code, Codex, Copilot, Open Code, and any agent that can read files and run terminal commands.

## How it works

1. The learner runs a setup script that installs Node.js, Wasp CLI, and verifies their environment
2. They create a new Wasp app and open their AI coding agent in the project folder
3. The agent fetches module instructions and acts as a tutor and pair programmer
4. The learner directs what to build in plain language; the agent handles the code
5. Progress is tracked via JSON files the agent writes to the project

## Links

- [Course landing page for humans](https://openvibe.sh/)
- [Wasp](https://wasp.sh)
- [Wasp Discord](https://discord.gg/rzdnErX)

## Top-level structure
```
.gitignore
.nojekyll
README.md
astro.config.mjs
package.json / package-lock.json
planning/          — internal planning docs
public/            — static assets served at openvibe.sh
  assets/
  llms.txt         — agent entry-point (course instructions)
  modules/         — course module markdown files
    setup.md
    module-0.md
    phase-2-module-1.md
    phase-2-module-2.md
    phase-3-module-1.md
    phase-3-module-2.md
  robots.txt
  setup.sh         — environment setup script
scripts/           — build/utility scripts
src/               — Astro site source
  assets/
  layouts/
  pages/
```
