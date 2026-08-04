# impeccable.style

## Fetch log
- Inbox URL: https://impeccable.style/
- Final URL: https://impeccable.style/
- Fetched: 2026-08-04
- Pages: 8
- Mode: standard

## llms.txt — https://impeccable.style/llms.txt
# Impeccable

> Impeccable is an open-source design skill, CLI, browser extension, and website for improving AI-generated frontend design with 23 commands, live browser iteration, and deterministic anti-pattern detection.

Use the website pages below as the current public documentation. Use the GitHub repository when you need source code, implementation details, tests, or release history. The fastest install path is `npx impeccable install` from a project root.

## Start Here

- [Home](https://impeccable.style/): Product overview, install options, supported AI coding harnesses, and download entry points.
- [Designing with Impeccable](https://impeccable.style/designing): The end-to-end workflow from setup and brief to iteration, polish, and maintenance.
- [Documentation](https://impeccable.style/docs): Command reference index for `/impeccable` and its commands.
- [Getting started](https://impeccable.style/tutorials/getting-started): Install Impeccable, run `/impeccable init`, create design context, and start with a polish pass.
- [Live Mode](https://impeccable.style/live-mode): Browser-based UI iteration with element picking, annotations, generated variants, and source writeback.
- [Slop](https://impeccable.style/slop): Catalog of AI-generated UI anti-patterns and the detection overlay behind the CLI, extension, and critique workflow.

## Tutorials

- [Tutorials index](https://impeccable.style/tutorials): Step-by-step guides for installation, live iteration, and visual critique.
- [Iterate on UI with Live Mode](https://impeccable.style/tutorials/iterate-live): Use `/impeccable live` against a running dev server to generate and accept UI variants.
- [Critique with the visual overlay](https://impeccable.style/tutorials/critique-with-overlay): Combine `/impeccable critique`, deterministic detection, and the browser overlay.

## Concepts and Reference

- [Design Context](https://impeccable.style/docs/context): PRODUCT.md, DESIGN.md, surface briefs, the four visitor modes, the platform axis, and the design sidecar.
- [New work](https://impeccable.style/docs/new-work): How a direction is resolved for a new page, a redesign, or an addition to an existing one.
- [Config and ignores](https://impeccable.style/docs/config): `.impeccable/config.json`, detector exceptions, inline ignore comments, and project roots.
- [Detector CLI](https://impeccable.style/docs/detector): `npx impeccable detect` over files, directories, and rendered URLs.
- [Design hooks](https://impeccable.style/docs/hooks): Provider-native hooks that run the detector as the agent edits UI files.
- [Doctor](https://impeccable.style/docs/doctor): Find and repair drift between a project's Impeccable files and the installed version.

## Command Reference

- [impeccable](https://impeccable.style/docs/impeccable): Main command for recommendations, freeform design work, and loading the full design guide.
- [init](https://impeccable.style/docs/init): Set up design context with `PRODUCT.md`, optional `DESIGN.md`, Live Mode configuration, and next-command recommendations.
- [shape](https://impeccable.style/docs/shape): Run a discovery interview and produce a design brief before code.
- [live](https://impeccable.style/docs/live): Select browser elements, generate UI variants, and write accepted changes back to source.
- [document](https://impeccable.style/docs/document): Generate a `DESIGN.md` file from the current visual system.
- [extract](https://impeccable.style/docs/extract): Consolidate repeated patterns, components, and design tokens.
- [critique](https://impeccable.style/docs/critique): Evaluate UX, hierarchy, cognitive load, brand fit, and anti-patterns.
- [audit](https://impeccable.style/docs/audit): Run technical checks for accessibility, performance, theming, responsiveness, and anti-patterns.
- [polish](https://impeccable.style/docs/polish): Perform a final quality pass for alignment, spacing, consistency, and micro-details.
- [harden](https://impeccable.style/docs/harden): Add production resilience for errors, edge cases, i18n, and text overflow.
- [optimize](https://impeccable.style/docs/optimize): Improve UI performance, rendering, images, animations, and bundle cost.
- [adapt](https://impeccable.style/docs/adapt): Adapt designs across screens, devices, contexts, and platforms.
- [clarify](https://impeccable.style/docs/clarify): Improve UX copy, labels, errors, empty states, and instructions.
- [onboard](https://impeccable.style/docs/onboard): Design onboarding, first-run experiences, empty states, and activation paths.
- [typeset](https://impeccable.style/docs/typeset): Improve typography, font choices, hierarchy, sizing, weight, and readability.
- [layout](https://impeccable.style/docs/layout): Improve composition, spacing, rhythm, alignment, and visual hierarchy.
- [colorize](https://impeccable.style/docs/colorize): Add strategic color without falling into generic AI palettes.
- [animate](https://impeccable.style/docs/animate): Add purposeful motion, transitions, feedback, and reduced-motion support.
- [delight](https://impeccable.style/docs/delight): Add memorable details and moments of joy without compromising usability.
- [bolder](https://impeccable.style/docs/bolder): Push safe designs toward stronger impact.
- [quieter](https://impeccable.style/docs/quieter): Reduce visual intensity while preserving quality.
- [distill](https://impeccable.style/docs/distill): Strip unnecessary complexity and focus the interface.
- [overdrive](https://impeccable.style/docs/overdrive): Build ambitious effects such as shaders, spring physics, and scroll-driven reveals.

## Developer Resources

- [GitHub repository](https://github.com/pbakaus/impeccable): Source code, tests, issues, pull requests, and release workflow.
- [Repository README](https://github.com/pbakaus/impeccable#readme): Package overview, command list, install methods, and supported harnesses.
- [Changelog](https://impeccable.style/changelog): Release notes for the skill, CLI, extension, and detector.
- [FAQ](https://impeccable.style/faq): Installation paths, update commands, pinning, troubleshooting, and harness-specific setup.

## Optional

- [Neo Mirai case study](https://impeccable.style/cases/neo-mirai): Example of Impeccable turning generated references into a shipped website.
- [Design system](https://impeccable.style/design-system): Public style system reference for the Impeccable website itself.
- [Detector lab](https://impeccable.style/detector): Fixture-backed detector examples for anti-pattern rules and visual checks.
- [Privacy](https://impeccable.style/privacy): Website analytics, download logging, and browser extension privacy notes.

## Landing page — https://impeccable.style/
# Impeccable: Design Vocabulary for AI Agents

**What it is:**
Impeccable is a design tool that eliminates common AI-generated interface problems ("slop") by providing precise commands to steer AI agents and iterate visual variants. According to the homepage, it "strips the slop from AI-generated interfaces, gives you precise commands to steer, and iterates visual variants live in your product."

**Key Features:**

- **58 automatic slop detections** that catch default patterns before they ship
- **23 commands** offering shared design vocabulary (like `/typeset`, `/distill`, `/audit`)
- **Live mode** for real-time in-app refinement with element picking
- **Design system integration** that respects existing tokens, components, and conventions
- **DESIGN.md portability** using Google Stitch format for system documentation
- **Context awareness** via PRODUCT.md to understand mode (Persuade, Operate, Read, Experience)

**Available Across Platforms:**
Works with Claude Code, Cursor, GitHub Copilot, Gemini CLI, Codex CLI, Grok Build, and others. Each build is tuned to specific model tendencies.

**Installation:**
Recommended via Claude Code marketplace, or through `npx impeccable install` (requires Node 22.12+).

**Additional Tools:**
Chrome extension for detector overlay, CLI for CI/CD integration, and regular design-thinking newsletter updates.

## Docs — https://impeccable.style/docs
# Impeccable Documentation Page Content

This page serves as the main documentation hub for Impeccable, a CLI tool for design automation. The navigation structure includes:

**Main Sections:**
- Home, Designing, Docs, Slop, Live Mode
- Learning resources (Tutorials and Reference guides)

**Key Command Categories:**
- Create (impeccable, shape)
- Evaluate (audit, critique)
- Refine (8 commands including animate, bolder, colorize, layout, typeset)
- Simplify (adapt, clarify, distill)
- Harden (harden, onboard, optimize, polish)
- System (document, extract, init, live)

**Core Workflow:**
The page emphasizes a structured design process: "Install, add context, then run one command." It outlines three initial steps using `npx impeccable install`, `/impeccable init`, and testing commands on real pages.

**Session Path:**
The documentation describes a complete workflow: Plan → Review → Refine → Iterate, with corresponding commands (shape → critique → polish → live).

**Featured Pairs:**
The page highlights complementary command combinations like bolder/quieter (voice control) and critique/polish (review then refine).

Footer credits Paul Bakaus as creator, with links to changelog, FAQ, privacy policy, and GitHub repository (48k stars).

## Design Context — https://impeccable.style/docs/context
# Design Context | Impeccable

Impeccable is a CLI tool that helps designers and developers make specific, consistent design decisions by maintaining project memory through documentation files.

## Core Files Structure

The system uses four main files:

**PRODUCT.md** - Strategy documentation covering "Platform, users, purpose, positioning, evidence, brand commitments."

**DESIGN.md** - Visual system file detailing "Colors, type, components, radii, design rules."

**.impeccable/surfaces/*.md** - Per-page documentation tracking mode, job, proof sequence, and chosen direction.

**.impeccable/design.json** - Generated structured metadata for automation (user should not hand-edit).

## Four Design Modes

Impeccable categorizes surfaces into four types based on visitor intent:

- **Persuade**: Landing pages and marketing where design earns attention
- **Operate**: Task-completion interfaces like dashboards and admin panels
- **Read**: Documentation and guides prioritizing comprehension
- **Experience**: Portfolios and galleries where the artifact leads

## Platform Support

The tool supports multiple platforms with `PRODUCT.md` configuration:
- `web` (default)
- `ios`
- `android`
- `adaptive` (Flutter, React Native, KMP)

Native platforms receive specialized auditing for accessibility and platform conformance.

## Keeping Context Fresh

Updates are triggered by specific changes:
- Strategic changes → `/impeccable init`
- Visual system changes → `/impeccable document`
- Stale context concerns → `/impeccable doctor`

## impeccable command — https://impeccable.style/docs/impeccable
# Impeccable Documentation - Main Command Reference

## Overview
Impeccable is a design-focused CLI tool that helps generate and refine UI components. The `/impeccable` command serves as the primary entry point for design work.

## Primary Uses

The documentation identifies two main ways to use this command:

1. **Standalone inspection**: Running `/impeccable` alone triggers project analysis and recommendations for next steps.

2. **Natural language requests**: Users can describe desired design outcomes in plain English, allowing the tool to select appropriate methods.

## Key Scenarios

According to the docs, reach for this command when:
- "You are not sure where to start" - the tool inspects setup files and suggests next steps
- Command selection is unclear - describe goals naturally and let the tool choose
- Work spans multiple design disciplines (e.g., layout, typography, color, motion)
- Freeform design assistance is needed

## How It Works

The tool relies on two configuration files at the project root:

- **PRODUCT.md**: Describes the project's platform, audience, purpose, and brand positioning
- **DESIGN.md**: Specifies visual standards including colors, typography, components, and design rules

## Related Features

The documentation mentions a "live mode" variant (`/impeccable live`) for browser-based visual iteration using hot module replacement to preview design variants.

## Designing with Impeccable — https://impeccable.style/designing
# Impeccable: Design System CLI Tool

Impeccable is a command-line interface for Claude that operates through four design phases: setting context, iterating refinements, pre-ship validation, and maintaining design systems.

## Core Workflow

The platform structures design work into distinct stages:

**Start**: Initialize projects with `/impeccable init` to establish foundational context about the platform, users, and product positioning. This generates `PRODUCT.md` and scans codebases for existing design documentation.

**Iterate**: Refine designs through either specific commands targeting named disciplines (typography, layout, color, motion) or Live Mode for visual exploration. The tool generates three production-quality variants for user selection.

**Polish**: Pre-ship validation uses three commands—audit, clarify, and harden—to identify accessibility issues, refine copy for target audiences, and stress-test with realistic data scenarios.

**Maintain**: Combat design drift through pattern consolidation and system documentation, capturing tokens and components into updated design specifications.

## Key Features

The tool operates within AI coding environments including Cursor, Claude Code, GitHub Copilot, and Gemini CLI. It includes a Chrome extension for analyzing live pages and a CI integration for detecting anti-patterns during deployment.

Four design modes adapt to different contexts: Persuade (landing pages), Operate (app interfaces), Read (documentation), and Experience (portfolios).

## Warnings Against Common Mistakes

Users should avoid running Impeccable alongside Anthropic's frontend-design skill, over-pinning commands, skipping the initialization phase, and treating the tool as a validator rather than a collaborative design partner.

## Live Mode — https://impeccable.style/live-mode
# Impeccable Live Mode Beta

Impeccable is a design tool that integrates with your development environment. According to the page, it allows developers to "Pick any element in the browser. Drop a comment or a stroke. Three production-quality variants swap in via your framework's HMR."

## How It Works

The tool operates in three steps:

1. **Pick** - Users click elements on their running dev server and can add comments, draw strokes, or describe desired changes like "more playful"

2. **Generate** - The system produces three distinct design variants that "anchor to different archetypes" exploring different axes such as hierarchy, typography, density, layout, or palette strategy

3. **Accept** - The chosen variant "replaces the picked element in your source file. CSS consolidates into your real stylesheet, not inline"

## Key Features

The page indicates the tool works with major frameworks including Vite, Next.js, SvelteKit, Astro, Nuxt, Bun, and plain HTML. The current status is described as beta—"works end-to-end across the common frameworks and is ready for daily use" though "uncommon setups may still hit rough edges."

The interface includes a command `/impeccable live` to activate the functionality, and the project is maintained by Paul Bakaus with documentation available for tutorials and command references.

## Slop — https://impeccable.style/slop
# Slop | Impeccable

Impeccable is a design quality detector that identifies 64 patterns exposing AI-generated UI defaults and production defects across 59 rules.

## Overview

The tool catches recognizable aesthetics from AI-generated interfaces, including "purple gradients, glassmorphism, neon glow" and other recurring signatures. It provides overlay detection on synthetic test pages and offers broader design assessments through critique functionality.

## Key Features

**Detection Methods:**
- CLI-based deterministic detection via `npx impeccable detect`
- Browser extension for one-click activation
- LLM-powered design review through critique command
- Personalized detection using DESIGN.md for design system alignment

## Pattern Categories (64 Total)

The catalog covers:

- **Your Design System** (4 rules) – fonts, colors, radii, sizing outside documented systems
- **Visual Details** (8 rules) – decorative grids, glassmorphism, side-tab borders, extreme border-radius
- **Typography** (11 rules) – kickers, flat hierarchies, icon tiles, italic serifs, oversized heroes
- **Color & Contrast** (7 rules) – radial glows, AI palettes, gradient text, gray-on-color contrast
- **Layout & Space** (12 rules) – numbered labels, card nesting, monotonous spacing, line length
- **Motion** (6 rules) – pulsing dots, decorative cursors, marquees, bounce easing, layout animations
- **Copy** (5 rules) – em-dash overuse, buzzwords, aphoristic cadence, theater framing
- **Imagery** (2 rules) – shape-assembled illustrations, broken images
- **General Quality** (10 rules) – script errors, invisible content, contrast, heading hierarchy, line height

## Usage Options

Users can access Impeccable through the Chrome Web Store, CLI, or critique command for design assessments.

## Getting started — https://impeccable.style/tutorials/getting-started
# Impeccable Getting Started Guide

Impeccable is a design automation tool that works as a skill within AI coding harnesses like Claude Code, Cursor, and GitHub Copilot.

## Core Workflow

The tool operates through the command structure `/impeccable <command> <target>`. Users install it via `npx impeccable install`, which auto-detects their coding environment and deploys appropriate skill files.

## Three-Step Setup

**Installation**: Running the npm command configures Impeccable for the user's specific AI coding tool.

**Project Context**: The `/impeccable init` command conducts a brief interview to establish design strategy, capturing details about the product's target audience, positioning, and constraints in a `PRODUCT.md` file.

**Visual System**: The `/impeccable document` command catalogs existing design elements and generates a `DESIGN.md` file following Google Stitch's format.

## Key Capabilities

The platform organizes 23 commands across categories:

- **Create**: Commands like `impeccable` and `shape` for generating new work
- **Evaluate**: `audit` and `critique` for review and scoring
- **Refine**: Tools including `polish`, `colorize`, `typeset`, and `animate`
- **Simplify**: Commands like `adapt`, `clarify`, and `distill`
- **Harden**: Including `optimize`, `polish`, and accessibility-focused operations

## Getting Value

A typical polish pass makes "targeted fixes" addressing alignment, spacing, typography, color consistency, interaction states, and motion. The guide emphasizes that changes remain reviewable and reversible.
