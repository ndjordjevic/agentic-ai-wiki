---
type: source
category: "Security"
source_url: https://github.com/mukul975/Anthropic-Cybersecurity-Skills
tags: [cybersecurity-skills, mitre-attack, agentskills-io, agent-skills, threat-hunting, penetration-testing, mitre-atlas, nist-csf, ai-security, red-teaming]
related: [voltagent-awesome-agent-skills, anthropics-skills, obra-superpowers, skills.sh]
product: anthropic-cybersecurity-skills
detail_level: standard
created: 2026-08-22
updated: 2026-08-22
---

Anthropic Cybersecurity Skills is the largest open-source cybersecurity skills library for AI agents — 817 production-grade skills across 29 security domains, each following the agentskills.io standard with YAML frontmatter for agent discovery and structured Markdown workflows for step-by-step execution. The library's defining feature is its six-framework mapping: every skill is tagged to whichever subset of MITRE ATT&CK v19.1, NIST CSF 2.0, MITRE ATLAS 2026.07, MITRE D3FEND v1.4.0, NIST AI RMF 1.0, and the MITRE Fight Fraud Framework (F3 v1.1) applies to it. With 30,556 stars and an Apache 2.0 license, it is a community project (not affiliated with Anthropic PBC) and installs with a single `npx skills add` command on any agentskills.io-compatible platform.

_All claims below are sourced from ../../raw/github/mukul975-anthropic-cybersecurity-skills.md unless otherwise noted._

## What it does

Each of the 817 skills gives an AI agent the structured decision-making workflow a senior security analyst follows: when to use the technique, what prerequisites to check, how to execute step-by-step, and how to verify results. The library is designed for **progressive disclosure**: frontmatter costs ~30 tokens to scan so agents can search all 817 skills in a single context pass, then load the 500–2,000-token full workflow only for the top matches. Skills are organized in individual directories under `skills/`, each with sections:

- **Description** — one-paragraph what/when summary
- **When to Use** — trigger conditions for agent activation
- **Prerequisites** — required tools, access levels, environment setup
- **Workflow** — step-by-step execution with specific commands and decision points
- **Verification** — how to confirm successful execution

## Key features

- 817 skills across 29 security domains (Cloud Security 66, Threat Hunting 58, Threat Intelligence 52, Network Security 43, Web App Security 42, Digital Forensics 41, Malware Analysis 39, IAM 37, SOC Operations 35, Red Teaming 33, Container Security 33, AI Security 14, and more)
- Six-framework mapping: MITRE ATT&CK 805 skills, NIST CSF 2.0 804, D3FEND 139, NIST AI RMF 97, MITRE F3 94, MITRE ATLAS 93
- Progressive disclosure architecture: ~30 tokens to scan a skill frontmatter, 500–2,000 tokens for full workflow
- One-line install: `npx skills add mukul975/Anthropic-Cybersecurity-Skills`
- `index.json` — machine-readable catalog of all 817 frontmatters for agent indexing
- `.claude-plugin` manifest for direct Claude Code integration
- ATT&CK Navigator layer included in v1.0.0 release assets

## Architecture and concepts

Skills live as individual directories under `skills/` with a `SKILL.md` following the agentskills.io standard. YAML frontmatter declares `name`, `description`, `domain`, `subdomain`, `tags`, `mitre_attack`, `atlas_techniques`, `d3fend_techniques`, `nist_ai_rmf`, `nist_csf`, and `mitre_f3` fields. The `mitre_f3` block is kept separate from `mitre_attack` because F3 redefines several ATT&CK tactics for the fraud context — `mitre_attack` answers "how did the adversary operate technically" and `mitre_f3` answers "how did that turn into money."

Framework highlights:
- **MITRE ATLAS 2026.07**: 101 techniques covering AI/ML adversarial threats including agentic AI attack vectors added in late 2025 (agent context poisoning, tool invocation abuse, MCP server compromises, malicious agent deployment)
- **MITRE F3 v1.1**: adds Positioning (FA0001) and Monetization (FA0002) tactics absent from ATT&CK; fraud-specific IDs use F1XXX notation alongside reused T1XXX ATT&CK IDs
- **MITRE ATT&CK v19.1**: reflects the April 2026 restructuring that split Defense Evasion (TA0005) into Stealth (TA0005) and Defense Impairment (TA0112)

## Installation

```bash
# Recommended
npx skills add mukul975/Anthropic-Cybersecurity-Skills

# Manual
git clone https://github.com/mukul975/Anthropic-Cybersecurity-Skills.git
```

Compatible platforms: Claude Code, GitHub Copilot, Cursor, Windsurf, Cline, Aider, Continue, Roo Code, Amazon Q Developer, OpenAI Codex CLI, Gemini CLI, Devin, Replit Agent, SWE-agent, OpenHands, LangChain, CrewAI, AutoGen, Semantic Kernel, Haystack, Vercel AI SDK, and any MCP-compatible agent.

## Example usage

```
User: "Analyze this memory dump for signs of credential theft"

Agent:
  1. Scans 817 skill frontmatters (~30 tokens each)
     → identifies 12 relevant skills by tags, description, domain
  2. Loads top 3:
     • performing-memory-forensics-with-volatility3
     • hunting-for-credential-dumping-lsass
     • analyzing-windows-event-logs-for-credential-access
  3. Executes the Workflow section step-by-step
```

## Maintenance status

- 30,556 stars · 3,632 forks (as of 2026-08-22)
- Latest release: v1.3.0 (2026-06-22); main branch at 817 skills (2026-08-20)
- License: Apache 2.0
- Community project by @mukul975 (Mahipal Jangra), not affiliated with Anthropic PBC
- PRs reviewed for technical accuracy and agentskills.io standard compliance within 48 hours
- Cited in: VoltAgent/awesome-agent-skills, ottosulin/awesome-ai-security, SkillsLLM

## Ecosystem

The repo is indexed in [[voltagent-awesome-agent-skills]] as part of the broader agent-skills ecosystem. It sits alongside [[anthropics-skills]] (Anthropic's official skill collection) and [[obra-superpowers]] (the superpowers plugin framework) as examples of structured, portable skill libraries for AI coding agents — distinguished from those by its exclusive focus on offensive and defensive cybersecurity workflows and its six-framework compliance mapping. [[skills.sh]] provides the registry infrastructure (`npx skills add`) that makes the one-line install possible.
