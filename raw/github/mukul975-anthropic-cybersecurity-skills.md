# mukul975/Anthropic-Cybersecurity-Skills

## Metadata
- Stars: 30,556
- Forks: 3,632
- Primary language: Python
- Default branch: main
- Latest release: v1.3.0 (2026-06-22)
- License: Apache License 2.0
- Homepage: https://mahipal.engineer/Anthropic-Cybersecurity-Skills/
- Fetched: 2026-08-22
- Final URL: https://github.com/mukul975/Anthropic-Cybersecurity-Skills

## Description

817 structured cybersecurity skills for AI agents · Mapped to 6 frameworks: MITRE ATT&CK, NIST CSF 2.0, MITRE ATLAS, D3FEND, NIST AI RMF & MITRE F3 (Fight Fraud) · agentskills.io standard · Works with Claude Code, GitHub Copilot, Codex CLI, Cursor, Gemini CLI & 20+ platforms · 29 security domains · Apache 2.0

## README

# Anthropic Cybersecurity Skills

### The largest open-source cybersecurity skills library for AI agents

**817 production-grade cybersecurity skills · 29 security domains · 6 framework mappings · 26+ AI platforms**

> ⚠️ **Community Project** — This is an independent, community-created project. Not affiliated with Anthropic PBC.
>
> 🔐 **Authorized & lawful use only.** This library includes offensive and dual-use techniques intended for authorized penetration testing, security research, defense, and education only. Use only against systems you own or have explicit written permission to test.

## Give any AI agent the security skills of a senior analyst

This repo contains **817 structured cybersecurity skills** spanning **29 security domains**, each following the agentskills.io open standard. The library maps across six industry frameworks — MITRE ATT&CK, NIST CSF 2.0, MITRE ATLAS, MITRE D3FEND, NIST AI RMF, and the MITRE Fight Fraud Framework (F3) — with each skill mapped only to the frameworks relevant to its type.

## Six frameworks, one skill library

Framework coverage across the 817 skills:
- MITRE ATT&CK v19.1: 805 skills
- NIST CSF 2.0: 804 skills
- MITRE D3FEND v1.4.0: 139 skills
- NIST AI RMF 1.0: 97 skills
- MITRE F3 v1.1: 94 skills
- MITRE ATLAS 2026.07: 93 skills

| Framework | Version | What it maps |
|---|---|---|
| MITRE ATT&CK | v19.1 | Adversary behaviors and TTPs |
| NIST CSF 2.0 | 2.0 | Organizational security posture |
| MITRE ATLAS | 2026.07 | AI/ML adversarial threats |
| MITRE D3FEND | v1.4.0 | Defensive countermeasures |
| NIST AI RMF | 1.0 | AI risk management |
| MITRE F3 (Fight Fraud Framework) | v1.1 (2026-04-09) | Cyber-enabled financial fraud TTPs |

### MITRE Fight Fraud Framework (F3) — 94 fraud-relevant skills

F3 was released April 9, 2026 by MITRE's Center for Threat-Informed Defense (CTID). It adds two tactics ATT&CK lacks:
- **Positioning** (FA0001) — after access, collect/manipulate data and prepare the fraud (synthetic-identity seeding, SIM-swap pre-positioning, banking-session hijack).
- **Monetization** (FA0002) — converting stolen assets into usable funds (money-mule layering, APP fraud, crypto off-ramping, card cash-out, refund/chargeback abuse).

Fraud-specific techniques use F1XXX IDs; reused ATT&CK techniques keep T1XXX IDs.

### MITRE ATT&CK v19.1 — 805/817 skills mapped

v19.1 splits Defense Evasion (TA0005) into Stealth and Defense Impairment (TA0112).

| Tactic | ID | Skills |
|---|---|---|
| Reconnaissance | TA0043 | 103 |
| Resource Development | TA0042 | 22 |
| Initial Access | TA0001 | 467 |
| Execution | TA0002 | 350 |
| Persistence | TA0003 | 444 |
| Privilege Escalation | TA0004 | 464 |
| Stealth | TA0005 | 442 |
| Defense Impairment | TA0112 | 92 |
| Credential Access | TA0006 | 202 |
| Discovery | TA0007 | 237 |
| Lateral Movement | TA0008 | 68 |
| Collection | TA0009 | 172 |
| Command and Control | TA0011 | 123 |
| Exfiltration | TA0010 | 82 |
| Impact | TA0040 | 50 |

## Quick start

```bash
# Option 1: npx (recommended)
npx skills add mukul975/Anthropic-Cybersecurity-Skills

# Option 2: Git clone
git clone https://github.com/mukul975/Anthropic-Cybersecurity-Skills.git
```

Works with Claude Code, GitHub Copilot, OpenAI Codex CLI, Cursor, Gemini CLI, and any agentskills.io-compatible platform.

## What's inside — 29 security domains

| Domain | Skills | Key capabilities |
|---|---|---|
| Cloud Security | 66 | AWS, Azure, GCP hardening · CSPM · cloud attack emulation · cloud forensics |
| Threat Hunting | 58 | Hypothesis-driven hunts · LOTL detection · EVTX hunting · fleet hunting |
| Threat Intelligence | 52 | STIX/TAXII · MISP · OpenCTI · feed integration · actor profiling |
| Network Security | 43 | IDS/IPS · firewall rules · VLAN segmentation · traffic analysis |
| Web Application Security | 42 | OWASP Top 10 · SQLi · XSS · SSRF · deserialization |
| Digital Forensics | 41 | Disk imaging · memory forensics · Hayabusa/KAPE/Plaso timelines |
| Malware Analysis | 39 | Static/dynamic analysis · reverse engineering · sandboxing |
| Identity & Access Management | 37 | Entra ID/ROADtools · device-code phishing · PAM · zero trust identity |
| SOC Operations | 35 | Playbooks · escalation workflows · Graph-log detection · tabletop exercises |
| Red Teaming | 33 | ADCS/Certipy · BloodHound CE · Sliver/Havoc C2 · NTLM relay |
| Container Security | 33 | K8s RBAC · image scanning · Falco · container escape |
| Security Operations | 28 | SIEM correlation · log analysis · alert triage |
| OT/ICS Security | 28 | Modbus · DNP3 · IEC 62443 · historian defense · SCADA |
| API Security | 28 | GraphQL · REST · OWASP API Top 10 · WAF bypass |
| Incident Response | 26 | Breach containment · ransomware response · IR playbooks |
| Vulnerability Management | 25 | Nessus · scanning workflows · patch prioritization · CVSS |
| Penetration Testing | 21 | Network · web · cloud · mobile · NetExec lateral movement |
| DevSecOps | 18 | CI/CD security · Trivy IaC/image scanning · code signing |
| Zero Trust Architecture | 17 | BeyondCorp · CISA maturity model · microsegmentation |
| Endpoint Security | 17 | EDR · LOTL detection · fileless malware · persistence hunting |
| Cryptography | 16 | TLS · Ed25519 · post-quantum migration · key management |
| Phishing Defense | 15 | Email authentication · BEC detection · phishing IR |
| AI Security | 14 | LLM red-teaming (garak/PyRIT) · prompt injection · MCP/agentic security · guardrails |
| Mobile Security | 13 | Android/iOS analysis · mobile pentesting · MDM forensics |
| Ransomware Defense | 13 | Precursor detection · response · recovery · encryption analysis |
| Compliance & Governance | 9 | NIST 800-30/RMF · CMMC · HIPAA · TPRM · CIS benchmarks |
| Supply Chain Security | 8 | SBOMs · dependency confusion · malicious-package triage · SLSA/Sigstore |
| Deception Technology | 6 | Honeytokens · canarytokens · breach detection |
| Hardware & Firmware Security | 4 | CHIPSEC/UEFI audit · Secure Boot bypass · TPM attestation · bootkit hunting |

## How AI agents use these skills

Each skill costs ~30 tokens to scan (frontmatter only) and 500–2,000 tokens to fully load (complete workflow). Progressive disclosure: agents search all 817 frontmatters in a single pass, then load top matches in full.

Skill structure:
- `## Description` — one-paragraph what/when summary
- `## When to Use` — trigger conditions for agent activation
- `## Prerequisites` — required tools, access levels, environment setup
- `## Workflow` — step-by-step execution guide with specific commands and decision points
- `## Verification` — how to confirm successful execution

Frontmatter fields: `name`, `description`, `domain`, `subdomain`, `tags`, `atlas_techniques`, `d3fend_techniques`, `nist_ai_rmf`, `nist_csf`, `mitre_attack`, `mitre_f3`.

## Skill architecture

```
skills/
  abusing-dpapi-for-credential-access/
  abusing-shadow-credentials-for-privesc/
  achieving-cmmc-level-2-compliance/
  ... (817 total)
docs/
  mitre-f3-mapping.md
mappings/
tools/
index.json
```

## Compatible platforms

Claude Code · GitHub Copilot · Cursor · Windsurf · Cline · Aider · Continue · Roo Code · Amazon Q Developer · OpenAI Codex CLI · Gemini CLI · Devin · Replit Agent · SWE-agent · OpenHands · LangChain · CrewAI · AutoGen · Semantic Kernel · Haystack · Vercel AI SDK · Any MCP-compatible agent

## Releases

| Version | Date | Highlights |
|---|---|---|
| v1.0.0 | 2026-03-11 | 734 skills · 26 domains · MITRE ATT&CK + NIST CSF 2.0 · ATT&CK Navigator layer |
| v1.3.0 | 2026-06-22 | Latest tagged release |
| main (current) | 2026-08-20 | 817 skills · 29 domains · 6 frameworks (ATLAS, D3FEND, AI RMF, F3 added) |

## Top-level structure

```
.claude-plugin        — agent skill manifest for Claude Code
.github/              — CI/CD configuration
ATTACK_COVERAGE.md    — ATT&CK tactic/technique coverage detail
CITATION.cff          — citation metadata
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE               — Apache 2.0
README.md
README.fr.md          — French translation
SECURITY.md           — responsible disclosure policy
assets/               — banner and images
docs/                 — mitre-f3-mapping.md
index.json            — machine-readable skills catalog (all frontmatters)
mappings/             — framework mapping files
skills/               — 817 individual skill directories
tools/                — Python tooling for validation and maintenance
```
