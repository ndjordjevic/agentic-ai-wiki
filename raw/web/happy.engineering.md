# happy.engineering

## Fetch log
- Inbox URL: https://happy.engineering/
- Final URL: https://happy.engineering/
- Fetched: 2026-07-03
- Pages: 10
- Mode: standard

## llms.txt — https://happy.engineering/llms.txt
# Happy Coder: Mobile Claude Code Client - Feature Specification

Happy Coder enables developers to access Claude Code and other AI coding agents from mobile devices (phones), providing seamless handoff between desktop and mobile environments. Mobile coding is not about matching desktop productivity - it's about using the right tool for the right task. Mobile excels at thinking, planning, exploration, and maintaining momentum when away from your desk. Desktop excels at precise editing, detailed review, and multi-monitor workflows. The power comes from seamlessly combining both in a single continuous session.

## Core Architecture Features

### 1. Real-Time CLI Synchronization

**Engineering Description**: Bidirectional real-time synchronization between the desktop CLI (`happy`) and mobile app through encrypted relay server. The CLI wraps Claude Code execution and streams terminal state, while mobile app provides input that flows back to the CLI seamlessly. Both devices can initiate conversations, send messages, and receive responses in the same shared session - there's no distinction between "primary" and "secondary" devices.

> **User Story 1**: As a developer, I want to start a Claude Code session on my laptop, see my typed message appear instantly on my phone, then pick up my phone and continue the same conversation while doing laundry, so I can maintain continuous progress without being tied to my desk.

> **User Story 2**: As a developer, I want to start planning a new feature on my phone during my commute, then seamlessly sit down at my laptop and review the generated code using my normal desktop tools (IDE, terminal, git) in the exact same Claude Code session, so I can transition from planning to implementation without any handoff friction.

> **User Story 3**: As a developer, I want to keep my coding momentum going even when I leave my desk, so I can use my phone to think through problems, describe changes to Claude Code, and explore possibilities, then return to my laptop to do the precise editing and review work without having to restart or re-explain my context.

> **User Story 4**: As a developer, I want to use my phone as a "playground" for experimenting with ideas and having Claude Code generate prototypes while I'm away from my computer, so when I sit back down at my laptop I have concrete code to review, test, and refine using my full desktop tooling (multiple monitors, IDE, hot reloading) in the same continuous session.

> **User Story 5**: As a developer, I want to request complex code changes from my phone that might affect multiple files, then review those changes on my laptop where I can see code side-by-side and navigate between files easily, and then continue making follow-up requests and refinements in the same Claude Code session with all my context preserved, rather than trying to do detailed code review and iterative development on a narrow mobile screen where I can't see enough context at once.


**Technical Implementation**:
- WebSocket connections for real-time bidirectional communication
- Terminal state serialization and synchronization
- Command history and context preservation
- Cross-device cursor position and selection state sync

### 2. Multi-Session Management
S

**Engineering Description**: Support for multiple concurrent Claude Code sessions with independent state management. Each session maintains its own project context, conversation history, and terminal state. Sessions can be paused, resumed, and switched between seamlessly.

> **User Story**: As a developer working on multiple projects, I want to maintain separate Claude Code sessions for each project simultaneously, so I can context-switch between different codebases without losing progress or mixing conversations.

**Technical Implementation**:
- Session isolation with unique identifiers
- Project-specific context management
- Session persistence across app restarts
- Background session state preservation

### 3. End-to-End Encryption with Zero-Trust Architecture

**Engineering Description**: All communication between CLI and mobile app encrypted using shared secrets (scan a QR code). Relay server handles only encrypted blobs without access to plaintext data. Public key authentication with challenge-response protocol.

> **User Story**: As a security-conscious developer, I want my code and conversations to remain private even from the service provider, so I can use the tool with proprietary or sensitive codebases without compromising confidentiality.

**Technical Implementation**:
- ChaCha20-Poly1305 encryption for all data in transit
- ECDH key exchange via QR code scanning
- Zero round-trip authentication protocol
- Public key hashing for channel identification
- Open-source relay server for self-hosting

### 4. Offline-First Architecture with Encrypted Pub/Sub

**Engineering Description**: Asynchronous communication through encrypted relay server that acts as a message queue between desktop CLI and mobile app. Desktop CLI logs Claude Code activity, encrypts it, and uploads encrypted blobs to object storage. Mobile app fetches and decrypts these blobs to display progress. Commands flow in reverse - mobile encrypts instructions, uploads to relay, desktop downloads and decrypts to execute.

> **User Story 1**: As a developer, I want to queue up tasks for Claude Code and then go on a hike or ride through train tunnels, knowing that Claude will continue working and I can catch up on progress later without the session dying due to connectivity issues.

> **User Story 2**: As a developer using SSH apps on mobile, I'm frustrated when I type out a long, carefully formatted command but my connection drops before it's sent, and when I reconnect to tmux/screen the terminal clears or breaks formatting, forcing me to retype or paste mangled text that gives poor results. I want a solution where my messages are reliably delivered even if my connection drops during transmission.

**Technical Implementation**:
- Encrypted blob storage on relay server (server cannot read contents)
- Desktop CLI writes encrypted activity logs to object storage
- Mobile app polls for encrypted updates and decrypts locally
- Bidirectional encrypted pub/sub messaging system
- Session persistence independent of network connectivity
- Simple relay server with no access to plaintext data

### 5. Permission Prompts for MCP Tools and Edit Operations

**Engineering Description**: Real-time permission system that intercepts MCP tool calls and file edit operations initiated by Claude Code, presenting mobile developers with contextual Allow/Deny prompts before execution. When Claude Code attempts to use MCP tools (Model Context Protocol integrations like JIRA, Linear, GitHub APIs) or perform sensitive file operations, the mobile app displays the exact operation details and waits for explicit user approval before proceeding.

> **User Story 1**: As a developer using Claude Code with JIRA integration while commuting, I want to see exactly what tickets Claude Code wants to create or modify before it makes those API calls, so I can approve legitimate automation while preventing accidental changes to production systems.

> **User Story 2**: As a developer, I want to review and approve file modifications that Claude Code proposes to make while I'm away from my desk, so I can maintain control over my codebase even when using AI agents remotely through my phone.

> **User Story 3**: As a security-conscious developer, I want to explicitly authorize each MCP tool operation (database queries, API calls, external integrations) that Claude Code attempts, so I can ensure no unauthorized actions occur in my development environment even when I'm not actively monitoring the desktop session.

**Technical Implementation**:
- Interceptor middleware in CLI that pauses execution for permission-required operations
- Real-time permission request serialization and transmission to mobile app
- Mobile UI components for displaying operation context with Allow/Deny buttons
- Encrypted request/response flow through relay server maintaining zero-trust architecture
- Operation queuing system that preserves Claude Code session state during permission waits
- Granular permission categories (file operations, API calls, system commands, external integrations)
- Per-session permission memory with option to "Remember for this session"

## Mobile-Optimized User Experience Features

### 6. Push Notification System

**Engineering Description**: Push notifications triggered by Claude Code state changes. Notifications 
include session status updates, completion alerts, error notifications, and input requests. Unlike social media apps where notification fatigue is a concern, work-focused notifications prioritize immediate awareness over filtering - when you're actively developing, you need to know when each async operation completes to make the next work mode decision.

> **User Story**: As a developer, I want to be notified when Claude Code finishes a task or needs my input, so I can provide guidance without constantly checking my phone or wondering if progress has stalled.

**Technical Implementation**:
- Comprehensive state change notifications (completion, error, input needed)
- Immediate delivery without smart filtering or bundling delays
- Deep linking to specific sessions and exact completion points
- Rich notification content with operation details

### 7. Voice Agent Integration

**Engineering Description**: AI-powered voice interface that acts as an intermediary between the user and Claude Code. The voice agent processes natural language input, maintains conversational context, and generates structured prompts for Claude Code execution.

> **User Story**: As a developer, I want to brainstorm and iterate on coding ideas through voice conversation before committing to a Claude Code execution, so I can think through problems conversationally without immediately locking in a time-consuming code generation process.

**Technical Implementation**:
- Speech-to-text with Eleven Labs
- Conversation state management with its own context independent of claude code session.
- Text-to-speech
- Agentic assistant that can send messages to claude code and has some special prompts to get better results in turning rubber duck style stream of conciousness planning into a concrete request for claude code to execute.

### 8. Smart Planning Mode

**Engineering Description**: Conversation-first interface for developing and refining development plans before execution. Includes conversation history analysis, plan validation, and seamless transition from planning to execution mode.

> **User Story**: As a developer, I want to work through my ideas in a low-pressure conversational format where I can think out loud and refine my approach before sending Claude Code off to make actual changes, so I can avoid costly mistakes and poorly-defined requirements.

**Technical Implementation**:
- Conversation threading with plan extraction
- Requirement validation and conflict detection
- Plan export to structured Claude Code prompts
- Conversation-to-execution handoff protocol
- Historical plan analysis and template suggestion

## Productivity Enhancement Features

### 9. Pre-Sleep Task Seeding

> **User Story**: As a developer, I've always heard about the productivity hack of leaving something unfinished to start the next morning, but it never worked for me because setting up a meaningful task took 10-20 minutes - too long to be spontaneous, especially when I'd already overstayed at the office to finish something and didn't want to spend another 20 minutes setting myself up for tomorrow. 
>
> With Claude Code and MCP tools for JIRA or Linear, I can now sit in bed and instead of scrolling Reddit or Instagram, I run a custom bedtime agent slash command where I've already set up my `~/.claude/agents/bedtime.md` to describe the process of finding something simple that I can start tonight and finish tomorrow. I describe a feature I want or a problem I'm thinking about, then work back and forth with Claude in planning mode for about 5 minutes to develop an implementation plan I like. When I approve the plan, Claude gets to work while I put my phone on the charger. 
>
> When I wake up, I have a notification from Claude Code "4 files to review, 237 lines of code added" - something nice and small to start my day. Having Claude Code on my phone is key because previously, to leave something unfinished for the next day, I had to be in programmer brain and actually make code changes myself. Now I can do this setup at any point in the evening - the task shrunk from 20 minutes of focused programming work down to a 5-minute conversational planning session. Having Claude Code accessible from my phone dramatically increased the surface area of opportunities when this routine could actually happen, making it way more likely to become a consistent habit.


## Landing page — https://happy.engineering/
# Claude Code Anywhere

Spawn and control multiple Claude Codes in parallel. Happy Coder runs on your hardware, works from your phone and desktop, and costs nothing. Open source.

`npm i -g happy && happy`

Launch Web App | Star on GitHub

Hands-free control with voice agent—not just dictation
Multiple active sessions across multiple machines
Works seamlessly with your existing tools and workflow
Secure with end-to-end encryption
Open source (MIT licensed)

### Why Happy?

Zero workflow disruption — Keep using your favorite tools, editors, and development environments exactly as before.

Multiple Active Sessions — Run several Claude Code instances simultaneously across different projects.

Everything from the terminal, on your phone — Access all Claude Code features on mobile. From plan mode to custom agents, if it works in the terminal, it works in Happy.

Open source and free — Well organized codebase makes it easy to contribute.

Secure — Happy uses End to End Encryption. No one can read your messages or code.

Smart Push Notifications — Get alerted when your input is needed, when code is ready to review, or when something went wrong.

Real-Time Voice Execution — Speak commands and watch them execute instantly. Not just transcription - true voice-to-action.

### How does it work?

Happy has three parts that work together:

CLI Program (happy) — runs on your computer, starts Claude Code, encrypts state, sends to server.

Mobile App — gets encrypted data from server, displays what Claude Code is doing.

Relay Server — passes encrypted messages between computer and phone; server can't read data.

GitHub: github.com/slopus/happy


## Docs — https://happy.engineering/docs
# Welcome

Happy lets you control AI coding agents from anywhere - your phone, tablet, or web browser. Happy those AI coding agents runs on computers YOU own.

With Happy Coder you get:
- Zero workflow disruption
- Work from anywhere
- Multiple sessions
- End-to-end encryption
- No cloud costs — free and open source

Unlike cloud services that run code on rented machines, Happy Coder works with computers you already have.

Getting Started: Quick Start, Managing Sessions, Voice Commands, Enable Push Notifications


## Quick Start Guide — https://happy.engineering/docs/quick-start
# Quick Start Guide

## Installation
- iPhone/iPad: App Store
- Android: Google Play
- Web App: app.happy.engineering

```
npm install -g happy
```
Requires Node.js 18+.

```
happy --auth # Shows QR code
```

Scan QR with mobile app, then start coding with Claude.


## How It Works — https://happy.engineering/docs/how-it-works
# How It Works

Three parts: CLI (`happy`), Mobile App, Relay Server.

Relay solves firewalls — both devices connect outbound to server.

Security: QR-shared secret key; server only sees encrypted blobs. Zero round-trip authentication with challenge-response. Public key hash stored, not raw key. Server is ~900 lines, self-hostable.

Data flow: CLI starts Claude Code → watches activity → encrypts → relay → mobile decrypts and displays.

Encrypted blobs persisted for history and intermittent connectivity (train/hiking scenarios).

Contributor guidance: keep server dumb; logic belongs in mobile app; CLI stays simple generic command runner.

Packages: happy-app (Expo), happy-cli, happy-agent, happy-server.


## Real-Time Sync — https://happy.engineering/docs/features/real-time-sync
# Why Happy Coder Has Real-Time Synchronization

Lightweight extension of reach — not a cloud sandbox "background agent" workflow.

Real-time bidirectional sync via WebSockets between CLI and mobile. Same Claude Code session on laptop and phone with zero handoff friction.

Mobile excels at: describing changes, reviewing approach, maintaining momentum, planning.
Desktop essential for: multi-file review, debugging, complex git, precise editing.

CLI is source of truth; mobile is synchronized interface. No primary/secondary device relationship.


## Security & Encryption — https://happy.engineering/docs/security
# Security & Encryption

End-to-end encryption — code stays private even from operators.

Short version:
1. Code encrypted before leaving device
2. Only you have keys — master secret never leaves phone
3. Relay server can't read anything
4. Open source — auditable

Key hierarchy:
- MASTER SECRET (mobile only, once per account, base32 backup)
- CONTENT KEY PAIR derived via HKDF
- Per-session and per-machine keys for CLI auth

Encryption: ChaCha20-Poly1305 for data in transit; ECDH via QR for pairing.

Authentication: zero round-trip challenge-response; server stores public key hash only.

Self-host relay for complete infrastructure control.


## Self-Host Your Own Happy Server — https://happy.engineering/docs/guides/self-hosting
# Self-Host Your Own Happy Server

Relay server ~1,293 lines TypeScript. Docker build from github.com/slopus/happy-server.

Configure mobile Settings → Relay Server URL; CLI via HAPPY_SERVER_URL.

Production: Caddy reverse proxy for HTTPS. Docker Compose with PostgreSQL + Redis.

Requirements: 512MB RAM / 1 CPU for 1-10 developers.

Compared to Omnara ($9/mo), Cursor Mobile (VM), commercial alternatives — self-host is free with full control.


## Voice Coding — https://happy.engineering/docs/features/voice-coding-with-claude-code
# Why Voice Coding Makes Sense (Even Though It Sucks)

Architecture: You talking → Voice agent (on phone) → Claude Code (on computer) → Your code

Voice agent translates rambling into structured Claude Code requests — not a conversational partner.

Uses Eleven Labs speech-to-text; separate context from Claude Code session; customizable prompts in-app.

50% effectiveness during "dead hours" beats 0%. Bridges hammock/commute thinking to desk continuation via real-time sync.


## Happy Coder vs Alternatives — https://happy.engineering/docs/comparisons/alternatives
# Happy Coder vs Alternatives

Key distinction: Happy runs agents on YOUR machine (like Omnara, ClaudeCodeUI) vs cloud VMs (Terragon, Cursor Mobile).

Mobile comparison highlights:
- Happy: Free, iOS/Android/Web, MIT open source, E2E encryption, self-hostable, voice coding
- Omnara: $9/mo, no E2E encryption on hosted
- Cursor Mobile: $20/mo, runs on their infrastructure
- CodeRemote: $49/mo
- SSH+tmux: free but poor mobile UX, no push notifications

Happy advantages: privacy (encrypted blobs on relay), no subscription, full MCP/custom agents on local machine, native mobile UX.

Migration: `npm install -g happy` — no code migration needed from cloud providers.
