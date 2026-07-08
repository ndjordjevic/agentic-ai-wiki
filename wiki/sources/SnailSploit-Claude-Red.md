---
type: source
source_url: https://github.com/SnailSploit/Claude-Red
tags:
  - agent-skills
  - offensive-security
  - red-team
  - claude-skills
  - pentest-methodology
  - skill-library
  - edr-evasion
  - ai-security
related:
  - anthropics-skills
  - skills.sh
  - davidondrej-skills
  - voltagent-awesome-agent-skills
  - claudemarketplaces.com
  - obra-superpowers
  - mattpocock-skills
  - forrestchang-andrej-karpathy-skills
  - pbakaus-impeccable
product: claude-red
detail_level: standard
created: 2026-07-08
updated: 2026-07-08
---

SnailSploit's `claude-red` (2,659+ stars, MIT, latest release Claude-Red-Skills V.2) is the largest domain-specific offensive-security skill library for the Claude Skills system — 58 `SKILL.md` files across 13 categories (web, wireless, AD, cloud, mobile, IoT, infrastructure/red team, exploit dev, fuzzing, recon, AI security, utility) that turn Claude into an on-demand specialist operator for authorized red team, bug bounty, CTF, and security research work.

_All claims below are sourced from ../../raw/github/SnailSploit-Claude-Red.md unless otherwise noted._

## What it does

Packages expert offensive-security methodology as drop-in `SKILL.md` modules under `Skills/<category>/<skill-name>/`. Each skill carries YAML frontmatter (`name:` matching the folder, dense `description:` trigger phrases) and a structured body (Quick Workflow, technique sections with language-tagged code blocks, optional defender view, engagement cheatsheet, references). Skills load on demand via conversational triggers — operators mention a surface (e.g. SQLi) and Claude loads only the matching specialist skill, avoiding context cost for unused domains.

## Installation

Clone into a Claude-scanned skills directory, use sparse checkout for single categories, or run the interactive `install.sh`:

```bash
git clone https://github.com/SnailSploit/claude-red ~/.claude/skills/claude-red
# sparse category install
git clone --filter=blob:none --sparse https://github.com/SnailSploit/claude-red
cd claude-red && git sparse-checkout set Skills/web Skills/active-directory
# install script
./install.sh --target ~/.claude/skills --category web
```

For Claude Code, pipe a skill or whole category via `--system-file`. For Claude.ai, paste `SKILL.md` contents into a Project system prompt.

## Key features

- **58 skills across 13 categories** — web (16: SQLi, XSS, SSRF, SSTI, XXE, IDOR, file upload, RCE, deserialization, race conditions, request smuggling, open redirect, HPP, GraphQL, WAF bypass, business logic); wireless (14: WPA2/3, EAP, WPS, evil twin, KRACK, BLE, Zigbee, Z-Wave, LoRa/sub-GHz); infrastructure/red team (7: initial access, kill chain, EDR evasion, shellcode, keylogger arch, Windows mitigations/boundaries); exploit dev (6); fuzzing/VR (4); auth (JWT, OAuth); recon (OSINT tools + methodology); AI security (prompt injection, jailbreaks, RAG poisoning); utility (fast triage, pro reporting); plus expanding AD, cloud, mobile, and IoT categories.
- **On-demand loading** — trigger-matched via `description:` frontmatter; no context paid for skills not in use.
- **Coverage cross-reference** — `MINDMAP.md` maps skills to MITRE ATT&CK, OWASP WSTG, HackTricks, and PayloadsAllTheThings for pre-engagement gap analysis.
- **Seven-phase expansion roadmap** — targeting ~107 skills (AD split into 16, cloud identity +10, wireless +12, IoT +10, web basics +8, web advanced +10).
- **Manifest tooling** — `claude-skills.json`, `convert_skills.py`, `tools/build_manifest.py` for skill inventory management.

## Architecture

Flat `Skills/<category>/<skill-folder>/SKILL.md` convention — no shared runtime, plugin manifest, or installer beyond `install.sh`. Each skill is self-contained instructions with required YAML frontmatter; folder name must match `name:`. CONTRIBUTING.md enforces "one skill, one surface" over monolithic overviews. Skills derive from Sahar Shlichov's offensive checklist collection, restructured for Claude's trigger-matching model. Primary language is Python (repo tooling); skill bodies are overwhelmingly Markdown with bash/python/powershell/sql code blocks.

## Example usage

```bash
# Claude Code — load a single skill
cat Skills/web/offensive-sqli/SKILL.md | claude --system-file -

# Load a whole category
cat Skills/active-directory/**/SKILL.md | claude --system-file -

# Category-only install
./install.sh --category web
```

Once installed in `~/.claude/skills/`, mentioning "SQL injection testing" or "Kerberoasting" in conversation auto-loads the matching skill.

## Maintenance status

2,659 stars, 443 forks, MIT license, default branch `main`, latest release Claude-Red-Skills V.2 (2026-03-08), last pushed 2026-05-08. Active expansion — Phase 7 (README, LICENSE, manifest, install polish) in progress; Phase 3 wireless split marked mandatory. Author: Kai Aizen (SnailSploit). Full writeup at [snailsploit.com/claude-red](https://snailsploit.com/claude-red).

## Ecosystem

Built for the Claude Skills system ([[anthropics-skills]] pattern) — same `SKILL.md` + frontmatter trigger model as [[obra-superpowers]], [[davidondrej-skills]], [[mattpocock-skills]], and [[forrestchang-andrej-karpathy-skills]], but specialized for offensive security rather than general agent workflows or document processing. Listed in skill marketplaces like [[skills.sh]] and [[claudemarketplaces.com]]. The `offensive-ai-security` skill directly addresses AI/agent attack surfaces (prompt injection, RAG poisoning) — adjacent to but distinct from agent-building skills in [[voltagent-awesome-agent-skills]]. No runtime dependency on other repos; operators combine with their own tooling (BloodHound, hashcat, Frida, etc.) as referenced inside each skill.
