# openspec.dev

## Fetch log
- Inbox URL: https://openspec.dev/
- Final URL: https://openspec.dev/
- Fetched: 2026-05-19
- Pages: 1
- Mode: standard

## Landing page — https://openspec.dev/

# OpenSpec — A lightweight spec‑driven framework

A lightweight spec-driven framework

Universal | Open Source | No API Keys | No MCP

Install: `npm install -g @fission-ai/openspec@latest`

GitHub: https://github.com/Fission-AI/OpenSpec/
Discord: https://discord.gg/YctCnvvshC

## Supported Tools

### Native support — tools with native OpenSpec integration with custom slash commands built-in:
Claude Code, Cursor, Codex, GitHub Copilot, OpenCode, Windsurf, Gemini CLI, Antigravity, Cline, RooCode, Kilo Code, Amazon Q, Qoder, Auggie CLI, Qwen Code, CodeBuddy, CoStrict, Crush, Factory Droid, iFlow, and 16 more (25+ total)

## Features

### 1 — Review intent, not just code
Each OpenSpec change produces a spec delta that captures the change in requirements of the system. This makes it easy for developers to understand how they're modifying the system and what will need to change. It also allows reviewers to understand the change itself without having to dig through the code and quickly gain a high level understanding.

Example spec delta (openspec/specs/auth-session/spec.md):
```
### Requirement: Session expiration

- The system SHALL expire sessions after a configured duration.
+ The system SHALL support configurable session expiration periods.

#### Scenario: Default session timeout

 - GIVEN a user has authenticated
- - WHEN 24 hours pass without activity
+ - WHEN 24 hours pass without "Remember me"
 - THEN invalidate the session token

+ #### Scenario: Extended session with remember me
+ - GIVEN user checks "Remember me" at login
+ - WHEN 30 days have passed
+ - THEN invalidate the session token
+ - AND clear the persistent cookie
```

### 2 — Context that persists
Specs live in the repository alongside your code, organized by capability. When an agent needs context about how a feature should work, it reads the spec. When a new developer joins, they can browse the library to understand the system. Context doesn't disappear when a chat session ends or someone leaves the team.

Directory structure:
```
openspec/specs/
├── auth-login/
│   └── spec.md
├── auth-session/
│   └── spec.md
├── checkout-cart/
│   └── spec.md
└── checkout-payment/
    └── spec.md
```

### 3 — Something to review in seconds
When you describe a change you want to make, OpenSpec generates everything needed to review it: a proposal document, broken-down implementation tasks, technical design decisions, and the spec deltas showing how requirements will change. You review and refine the plan before any code is written, catching misalignment early.

Agent interaction example:
```
>/openspec:proposal Add remember me checkbox with 30-day sessions

Searching existing specs for authentication requirements...
Read(openspec/specs/auth-session/spec.md)
Searching existing codebase for session handling...
Read(src/auth/session.ts)
Creating proposal and breaking down implementation tasks...
Created change proposal with ID add-remember-me

openspec/changes/add-remember-me/
├── proposal.md    ← describe the change
├── design.md      ← technical decisions
├── tasks.md       ← implementation tasks
└── specs/         ← spec deltas
    └── auth-session/
        └── spec.md
This change affects 1 spec, with 3 phases and 8 tasks
```

## Coming Soon — Workspaces (In Development)
OpenSpec has become the go-to planning layer for many developers. Now building for teams:
- Large codebases
- Multi-repo planning
- Customization and integrations
- Better collaboration

## Frequently Asked Questions

**How is OpenSpec different from my agent's built-in plan mode?**
Plan mode is great for a single chat session. We focus on plans that extend over multiple sessions, or that you want to share with others. A workspace for feature planning lets you plan better and refine as you go. It's something you bring through the entire development lifecycle, not just one conversation.

**What makes OpenSpec different from other planning tools?**
1 — Lightweight. Minimal steps, minimal process. We want to get you building as quickly as possible.
2 — Brownfield-first. Most tools assume you're starting fresh. We focus on mature codebases where the real struggle is figuring out how the current system works.
3 — Specs live in your code. Other tools only use requirements during planning, then throw them away. We preserve the functional requirements behind your code as living documentation, so you always know what the code is supposed to do, not just what it currently does.

**Why use a spec instead of just writing a detailed prompt?**
Specs serve as alignment. A way to structure your thinking in a single space before a single line of code is written. Better clarity on what you're building, and better context for your agent when executing your plan.

**Can I use OpenSpec on an existing codebase?**
Yep! Specs get created as you build. Create specs as you need them and build your way through.

**What happens when I switch between coding agents?**
Our goal is to be a universal planning layer you can bring with you anywhere, no matter what coding agent you use. Your specs shouldn't care which agent you use.

**Where do specs live?**
In your codebase. Our view is they should be checked in — they provide visibility into how the system works and the intent it was built with.

**Wait isn't this just waterfall?**
Waterfall fails because of rigid plans and months of upfront planning. This is neither. We want you to get to a good enough plan and start coding — minimal effort, lightweight process.

© 2025 Fission
