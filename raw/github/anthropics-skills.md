# anthropics/skills

## Metadata
- Stars: 132032
- Primary language: Python
- Default branch: main
- Latest release: none
- License: none (source-available for document skills; Apache 2.0 for example skills)
- Homepage: (none)
- Fetched: 2026-05-11
- Final URL: https://github.com/anthropics/skills

## Description
Public repository for Agent Skills. Contains Anthropic's official skill implementations for Claude, ranging from document processing (xlsx, docx, pptx, pdf) to creative and technical skills, plus the Agent Skills specification and a skill template.

## README
> **Note:** This repository contains Anthropic's implementation of skills for Claude. For information about the Agent Skills standard, see [agentskills.io](http://agentskills.io).

# Skills
Skills are folders of instructions, scripts, and resources that Claude loads dynamically to improve performance on specialized tasks. Skills teach Claude how to complete specific tasks in a repeatable way, whether that's creating documents with your company's brand guidelines, analyzing data using your organization's specific workflows, or automating personal tasks.

For more information, check out:
- [What are skills?](https://support.claude.com/en/articles/12512176-what-are-skills)
- [Using skills in Claude](https://support.claude.com/en/articles/12512180-using-skills-in-claude)
- [How to create custom skills](https://support.claude.com/en/articles/12512198-creating-custom-skills)
- [Equipping agents for the real world with Agent Skills](https://anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)

# About This Repository

This repository contains skills that demonstrate what's possible with Claude's skills system. These skills range from creative applications (art, music, design) to technical tasks (testing web apps, MCP server generation) to enterprise workflows (communications, branding, etc.).

Each skill is self-contained in its own folder with a `SKILL.md` file containing the instructions and metadata that Claude uses. Browse through these skills to get inspiration for your own skills or to understand different patterns and approaches.

Many skills in this repo are open source (Apache 2.0). We've also included the document creation & editing skills that power Claude's document capabilities under the hood in the `skills/docx`, `skills/pdf`, `skills/pptx`, and `skills/xlsx` subfolders. These are source-available, not open source, but we wanted to share these with developers as a reference for more complex skills that are actively used in a production AI application.

## Disclaimer

**These skills are provided for demonstration and educational purposes only.** While some of these capabilities may be available in Claude, the implementations and behaviors you receive from Claude may differ from what is shown in these skills. These skills are meant to illustrate patterns and possibilities. Always test skills thoroughly in your own environment before relying on them for critical tasks.

# Skill Sets
- `./skills`: Skill examples for Creative & Design, Development & Technical, Enterprise & Communication, and Document Skills
- `./spec`: The Agent Skills specification
- `./template`: Skill template

# Try in Claude Code, Claude.ai, and the API

## Claude Code
You can register this repository as a Claude Code Plugin marketplace by running:
```
/plugin marketplace add anthropics/skills
```

Then install specific sets:
```
/plugin install document-skills@anthropic-agent-skills
/plugin install example-skills@anthropic-agent-skills
```

## Claude.ai
These example skills are all already available to paid plans in Claude.ai.

## Claude API
You can use Anthropic's pre-built skills, and upload custom skills, via the Claude API. See the Skills API Quickstart for more.

# Creating a Basic Skill
```markdown
---
name: my-skill-name
description: A clear description of what this skill does and when to use it
---

# My Skill Name

[Add your instructions here that Claude will follow when this skill is active]
```

The frontmatter requires only two fields: `name` and `description`.

# Partner Skills
- **Notion** - Notion Skills for Claude

## Docs

### .claude-plugin/marketplace.json — Plugin registry
```json
{
  "name": "anthropic-agent-skills",
  "plugins": [
    {
      "name": "document-skills",
      "description": "Collection of document processing suite including Excel, Word, PowerPoint, and PDF capabilities",
      "skills": ["./skills/xlsx", "./skills/docx", "./skills/pptx", "./skills/pdf"]
    },
    {
      "name": "example-skills",
      "description": "Collection of example skills demonstrating various capabilities including skill creation, MCP building, visual design, algorithmic art, internal communications, web testing, artifact building, Slack GIFs, and theme styling",
      "skills": [
        "./skills/algorithmic-art", "./skills/brand-guidelines", "./skills/canvas-design",
        "./skills/doc-coauthoring", "./skills/frontend-design", "./skills/internal-comms",
        "./skills/mcp-builder", "./skills/skill-creator", "./skills/slack-gif-creator",
        "./skills/theme-factory", "./skills/web-artifacts-builder", "./skills/webapp-testing"
      ]
    },
    {
      "name": "claude-api",
      "description": "Claude API and SDK documentation skill for building LLM-powered applications",
      "skills": ["./skills/claude-api"]
    }
  ]
}
```

### skills/skill-creator/SKILL.md — excerpt
```yaml
---
name: skill-creator
description: Create new skills, modify and improve existing skills, and measure skill performance. Use when users want to create a skill from scratch, edit, or optimize an existing skill, run evals to test a skill, benchmark skill performance with variance analysis, or optimize a skill's description for better triggering accuracy.
---
```
The skill-creator skill itself has an `agents/` subdir, `eval-viewer/` with `generate_review.py`, `references/`, `assets/`, and `scripts/` — a multi-file skill with supporting tools.

### template/SKILL.md
```markdown
---
name: template-skill
description: Replace with description of the skill and when Claude should use it.
---

# Insert instructions below
```

### spec/agent-skills-spec.md
The spec has moved to https://agentskills.io/specification

## Top-level structure
```
.claude-plugin/          — marketplace.json (Claude Code plugin registry config; maps plugin bundles to skill subdirs)
.gitignore
README.md                — top-level overview and usage guide
THIRD_PARTY_NOTICES.md   — third-party license notices (Apache 2.0, MIT, etc.)
skills/                  — 17 individual skill folders, each containing SKILL.md + supporting files
  algorithmic-art/       — generative art creation using code
  brand-guidelines/      — apply org brand rules to content
  canvas-design/         — canvas/design-system workflows
  claude-api/            — Claude API and SDK documentation skill
  doc-coauthoring/       — collaborative document editing
  docx/                  — Word document creation & editing (source-available)
  frontend-design/       — frontend/UI design patterns
  internal-comms/        — internal communications drafting
  mcp-builder/           — MCP server generation
  pdf/                   — PDF creation & processing (source-available)
  pptx/                  — PowerPoint creation & editing (source-available)
  skill-creator/         — meta-skill: create, eval, and iterate on skills (has agents/, eval-viewer/, scripts/)
  slack-gif-creator/     — Slack GIF generation
  theme-factory/         — visual theme creation
  web-artifacts-builder/ — web artifact (HTML/JS) generation
  webapp-testing/        — web application testing
  xlsx/                  — Excel creation & editing (source-available)
spec/                    — Agent Skills specification (now at agentskills.io/specification)
template/                — minimal SKILL.md starter template
```
