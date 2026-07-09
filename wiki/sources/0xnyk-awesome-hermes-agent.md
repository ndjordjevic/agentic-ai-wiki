---
type: source
category: "Agent Skills & plugins ecosystem"
source_url: https://github.com/0xNyk/awesome-hermes-agent
tags:
  - hermes-agent
  - awesome-list
  - skill-directory
  - agentskills-io
  - ecosystem-catalog
  - community-skills
  - plugins
  - memory-providers
related:
  - hermes-agent.nousresearch.com
  - voltagent-awesome-agent-skills
  - skills.sh
  - obra-superpowers
  - felix-forever-hermes-agent-desktop
  - garrytan-gbrain
  - supermemory.ai
  - paperclipai-paperclip
  - Chachamaru127-claude-code-harness
product: hermes-agent
detail_level: standard
created: 2026-07-07
updated: 2026-07-08
---

Awesome Hermes Agent is the community-maintained discovery layer for the Hermes Agent ecosystem (4,524 stars, CC BY 4.0), cataloging skills, plugins, memory providers, GUIs, deployment templates, integrations, and domain applications built around [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent). Unlike generic agent-skill lists, every entry is Hermes-specific or agentskills.io-compatible, tagged with maturity levels (production / beta / experimental), and organized into operational playbooks and level-up blueprints for teams assembling a production stack.

_All claims below are sourced from ../../raw/github/0xnyk-awesome-hermes-agent.md unless otherwise noted._

## What it does

Awesome Hermes Agent is a curated Awesome-list (`README.md`, ~76KB) that serves as the definitive index for the Hermes ecosystem. It tracks the core Hermes Agent project (v0.18.0 "The Judgment Release"), official Nous Research satellites (autonovel, hermes-paperclip-adapter, hermes-agent-self-evolution, tinker-atropos), and hundreds of community contributions across skills, plugins, memory backends, operator dashboards, deployment tooling, bridges, multi-agent frameworks, and domain-specific applications. A three-step onboarding path (official docs → first skills → GUI) and maturity tags help newcomers navigate without installing everything at once.

## Key features

- **Ecosystem-wide coverage:** 15 top-level sections — Official Resources, Skills & Plugins (community skills, plugins, agentskills.io ecosystem, skill registries), Memory Providers, Tools & Utilities (including deployment), Integrations & Bridges, Detection & Media Forensics, Multi-Agent & Swarms, Domain Applications, Forks & Derivatives, Guides & Documentation, Operational Playbooks, and Level-Up Blueprints.
- **Maturity tagging:** Every entry carries `production`, `beta`, or `experimental` so operators know what is safe to build on versus what is proof-of-concept.
- **agentskills.io focus:** Dedicated subsection for cross-platform skills compatible with Hermes, Claude Code, Cursor, Codex, and other agentskills.io hosts — including wondelai/skills, youtube-skills, Anthropic-Cybersecurity-Skills (753+ skills), chainlink-agent-skills, drawio-skill, open-design, and dozens more.
- **Memory provider catalog:** 15+ persistent memory backends (hindsight, mem0, supermemory, Mnemosyne, gbrain, honcho, hexus, yantrikdb, and others) with install notes and trade-offs.
- **Operator tooling index:** GUIs and dashboards (hermes-workspace, mission-control, hermes-web-ui, hermes-desktop), cost profilers (agentburn, cronalytics), token compressors (rtk-hermes, llmtrim), and migration tools (openclaw-to-hermes).
- **Opinionated blueprints:** Six "level-up" bundles — memory stack, self-improvement without self-delusion, operator cockpit, multi-agent execution, migration + deployment hardening, and Paperclip-managed autonomous ops.

## Architecture

The repository is a single-file Awesome-list with no runtime code. Content is organized as markdown sections with bullet entries in the form `**[tag]** [name](url) by [author] — description`. Official Nous Research resources sit at the top; community contributions are grouped by function. Operational Playbooks document recurring production patterns (nightly self-evolution, memory pressure handling, OpenClaw migration, USER.md/MEMORY.md curation). Level-Up Blueprints combine multiple list entries into recommended stacks. The list is maintained by 0xNyk (Builderz) with community PRs via CONTRIBUTING.md; ecosystem status is reviewed against Hermes releases (last reviewed 2026-07-04, Hermes v0.18.0).

## Example usage

To discover and install Hermes ecosystem resources referenced in this list:

```bash
# Start with official docs
open https://hermes-agent.nousresearch.com/docs/

# Install a cross-platform skill pack
hermes skills install wondelai/skills

# Add a community skill tap
hermes skills tap add Moshe-ship/hurmoz

# Set up the recommended GUI
git clone https://github.com/outsourc-e/hermes-workspace
```

Browse the README sections for memory providers (`hermes plugins`), deployment templates (Docker/Nix/Portainer), and integration bridges (MCP servers, messaging platforms, device control).

## Maintenance status

4,524 stars, 323 forks, CC BY 4.0 license, actively maintained (last pushed 2026-07-04). No versioned releases — the list updates continuously via community contributions. Ecosystem status block tracks Hermes Agent version (v0.18.0 / v2026.7.1) and core repo star count. Contribution policy: resources must be directly related to Hermes or agentskills.io, have a clear README, and not duplicate existing entries.

## Ecosystem

This list is the Hermes-specific counterpart to general agent-skill directories like [[voltagent-awesome-agent-skills]] and [[skills.sh]]. It complements [[hermes-agent.nousresearch.com]] (official docs + core agent) by indexing the community layer — skills, plugins, memory, GUIs, and integrations that extend the core runtime. Notable cross-references include [[garrytan-gbrain]] (gbrain memory provider), [[supermemory.ai]] (supermemory memory provider), [[felix-forever-hermes-agent-desktop]] (desktop GUI), and [[paperclipai-paperclip]] (Paperclip-managed ops via hermes-paperclip-adapter). For methodology skills that work across agents, see [[obra-superpowers]].
