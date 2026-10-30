---
type: source
category: "Agent Skills & plugins ecosystem"
source_url: https://github.com/expo/skills
tags:
  - expo
  - agent-skills
  - eas
  - expo-router
  - react-native
  - skills-cli
  - claude-code-plugin
  - official-skills
related:
  - addyosmani-agent-skills
  - anthropics-skills
  - googleworkspace-cli
  - voltagent-awesome-agent-skills
product: expo-skills
detail_level: standard
created: 2026-10-30
updated: 2026-10-30
---

expo/skills is the official Expo team collection of AI agent skills for building, deploying, upgrading, and debugging Expo apps and Expo Application Services (EAS). Skills give agents focused Expo knowledge—when to use APIs, how to structure workflows, and which Expo, EAS, React Native, iOS, and Android constraints matter—while Expo docs, Expo CLI, and EAS CLI remain the source of truth.

_All claims below are sourced from ../../raw/github/expo-skills.md unless otherwise noted._

## What it does

The pack routes agents through an `expo-overview` entry skill into framework (open-source SDK/RN) skills and services/paid-distribution (EAS) skills, with free vs paid labeled in each skill description and every services skill opening with a costs/plan-limits note. Agents pick skills from task context and descriptions. A separate experimental track (`expo-migrate-module` and peers) ships in the `expo-experiments` plugin or via per-skill CLI install. The Expo MCP server (docs on demand, `npx expo install`, EAS builds/workflows, TestFlight crashes, simulator screenshots) is bundled with the Claude Code / Codex `expo` plugin; other agents follow the Expo MCP setup guide.

## Installation

| Path | Best for |
| --- | --- |
| Plugin install | Claude Code or Codex — updates via official plugin marketplaces |
| Skills CLI | Cursor, OpenCode, GitHub Copilot, Windsurf, Gemini, Cline, AMP, Factory Droid, Antigravity, Kiro CLI, and similar |

**Skills CLI** (all Expo skills; CLI still asks where to install; add `--agent <agent>` to target one):

```text
npx skills@latest add expo/skills --skill '*'
```

Run from the project root, then restart or refresh the agent session.

**Claude Code plugin:**

```text
claude plugin install expo@claude-plugins-official
```

Or `/plugin install expo@claude-plugins-official` inside Claude Code.

**Codex plugin:**

```text
codex plugin add expo@openai-curated
```

Or open `/plugins` and install `expo` from the OpenAI-curated marketplace.

**Updates:** marketplace for plugins; `npx skills@latest update` (or `npx skills@latest update expo-router` for one skill) for CLI installs.

## Key features

- **`expo-overview`** — router and shared setup; load first when the request is vague or no specific Expo tool is named.
- **Framework (open source)** — `expo-project-structure`, `expo-router`, `expo-animation`, `expo-native-ui`, `expo-design-system`, `expo-ui`, `expo-data-fetching`, `expo-dom`, `expo-web-to-native`, `expo-module`, `expo-brownfield`, `expo-dev-client`, `expo-examples`, `expo-app-clip`, `expo-upgrade`.
- **Services & paid distribution** — `eas-app-stores`, `eas-hosting`, `eas-workflows`, `eas-observe`, `eas-update`, `eas-update-insights`, `eas-simulator`.
- **Experimental** — `expo-migrate-module` (Modules API 1.0 DSL → 2.0 macro); may change or retire; separate `expo-experiments` plugin.
- **Feedback loop** — every skill instructs submitting feedback via `npx --yes @expo/agent-cli@latest feedback`.
- Official Expo badge; listed on [skills.sh/expo/skills](https://skills.sh/expo/skills).

## Architecture

Skills are Agent Skills-style packages consumed via plugins or the skills CLI. Repo layout includes `plugins/expo` and `plugins/expo-experiments`, `.claude-plugin/` marketplace metadata, `.agents/`, `.claude/`, `.eas/`, `scripts/`, `tests/`, `eval-harness`, `skills.sh.json`, `AGENTS.md`, and `CLAUDE.md`. Primary language Shell; MIT license. Docs site entry: https://docs.expo.dev/skills/. MCP configuration is part of the `expo` plugin for Claude Code/Codex; standalone MCP setup is documented at Expo's EAS AI MCP guide.

## Example usage

After install, ask Expo-specific questions such as:

- "Build a native-feeling Expo Router screen with tabs, modals, and animations."
- "Create an EAS workflow that builds previews on pull requests."
- "Help me upgrade this app to the latest Expo SDK."
- "Check whether this EAS Update rollout is healthy."

```text
npx skills@latest add expo/skills --skill '*'
npx skills@latest update
npx skills@latest update expo-router
```

## Maintenance status

3,767 stars, 241 forks, Shell primary language, default branch `main`, last pushed 2026-10-29. No tagged releases (n/a). MIT License. Maintained as official Expo skills.

## When to use

Use when coding agents work on Expo / React Native apps or EAS (Router screens, SDK upgrades, EAS Update health, store submit, workflows) and need vendor-authored guidance that respects free vs paid EAS boundaries. Prefer the Claude Code / Codex plugin when you want marketplace updates; use the skills CLI for Cursor and other agents. Do not treat skills as replacing Expo docs or CLI—they teach agents how to apply those sources.

## Ecosystem

Peers among official / curated skill packs in this wiki: [[addyosmani-agent-skills]] (full-SDLC engineering skills), [[anthropics-skills]] (Anthropic reference skills), [[googleworkspace-cli]] (Workspace agent tooling), and the catalog [[voltagent-awesome-agent-skills]]. Expo skills are product-vendor skills (Expo/EAS) rather than general SDLC methodology. Complements the Expo MCP server for live docs, installs, builds, and simulator access alongside static skill instructions.
