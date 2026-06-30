# raw/web/the-new-sdlc-with-vibe-coding.md

## Fetch log

- URL: https://drive.google.com/file/d/1IR7CddF_2FyQo_PdfBNTaEA50EGiVt2r/view
- Downloaded: 2026-06-30
- Type: PDF (Google Drive public share)
- File size: 9.97 MB
- Format: PDF 1.7
- Pages: 51
- Extraction tool: pdftotext (poppler)
- Mode: standalone-document
- Source: PDF authored by Addy Osmani, Shubham Saboo, and Sokratis Kartakis; published May 2026 under Google's "Agents Whitepaper Series"

---

## Document metadata

- Title: The New SDLC With Vibe Coding: From ad-hoc prompting to Agentic Engineering
- Authors: Addy Osmani, Shubham Saboo, Sokratis Kartakis
- Content contributors: Elia Secchi, Julia Wiesinger, Anant Nawalgaria
- Curators and editors: Anant Nawalgaria
- Designer: Michael Lanning
- Published: May 2026
- Series: Google Agents Whitepaper Series (Day 2 paper)
- Companion papers referenced:
  - Day 3: "Context Engineering: Sessions, Skills & Memory"
  - Day 5: "Spec-Driven Production Grade Development in the Age of Vibe Coding"
  - November 2025: "Introduction to Agents" whitepaper

---

## Full extracted text

The New SDLC
With Vibe Coding
From ad-hoc prompting to
Agentic Engineering

Authors: Addy Osmani, Shubham Saboo,
and Sokratis Kartakis

---

### Introduction

The most profound shift in software engineering isn't a new language, framework, or cloud service. It's the transition from writing code to expressing intent, and trusting intelligent systems to translate that intent into working software.

For most of computing history, programming has been an act of translation: understand the problem in human terms, design a solution in abstract terms, then render it in syntax a machine can execute. Each step introduces friction. That friction is now collapsing. Software engineering is undergoing its most significant transformation since the introduction of high-level programming languages. For decades, the developer's primary interface with the machine has been syntax: curly braces, semicolons, type annotations, and the precise grammar of programming languages. That era is ending.

A new paradigm has arrived in which developers express what they want to build rather than how to build it. The machine handles implementation. The human provides intent, architecture, and judgment. This isn't a distant future — it's the daily reality for a rapidly growing number of professional developers. As of early 2026, 85% of professional developers regularly use AI Coding Agents, 51% use them daily, and an estimated 41% of all new code is AI-generated.

This shift began with autocomplete — simple token prediction in the editor. Then came inline code suggestions that could complete entire functions. Next, chat-based interfaces allowed developers to describe features in natural language and receive working implementations. Now, fully autonomous agents can clone repositories, plan multi-file changes, execute them in sandboxed environments, run tests, and submit pull requests — all without a human typing a single line of code.

The implications for the software development life cycle (SDLC) are profound. Every phase — from requirements gathering to deployment to maintenance — is being reshaped by AI capabilities. But this transformation isn't uniform or simple. The spectrum ranges from casual "vibe coding," where a developer prompts an AI and accepts whatever comes back, to disciplined "agentic engineering," where AI acts as a powerful implementation engine within carefully designed systems of constraints, tests, and feedback loops, with humans retaining oversight over architecture, correctness, and quality.

The distinction matters. Telling a CTO that your team is vibe coding their payment processing system will, and should, raise alarm bells. Telling that same CTO that your team practices agentic engineering, with AI handling implementation under human-designed constraints while test coverage ensures correctness, is a fundamentally different conversation.

---

### Why this paper, why now

New tools, capabilities, and paradigms emerge weekly. Engineering teams need a framework for making sense of this landscape — not a snapshot that will be outdated in months, but a set of principles and mental models that will remain useful as the specific tools evolve.

### Who this paper is for

This paper is for software engineers, engineering managers, architects, and technical leaders who want to understand how AI is reshaping the SDLC and adopt these new capabilities without sacrificing the discipline that production software demands. We assume familiarity with modern software development practices but not with the specifics of AI or machine learning.

---

### The shift from syntax to intent

#### AI Agents: A Quick Refresher

An AI agent is a software system that perceives a goal, plans steps to reach it, takes actions through tools, observes the results, and iterates until the goal is met or it hits a stopping condition. Where a chatbot produces a response and waits for the next prompt, an agent runs its own loop. You give it a goal at the top, then it decides what to do next at each step.

Every agent, however simple or sophisticated, is built from five parts:
- **The model** is the reasoning engine. It reads the current context, decides what should happen next, and produces the next thought, the next tool call, or the next message.
- **Tools** connect the model to the world. They include APIs the agent can call, code it can execute, databases it can query, and other agents it can delegate to.
- **Memory** is the state. It allows the agent to recall past interactions, retrieve project-specific rules, and retain context across sessions so it never starts from a blank slate.
- **Orchestration** is the code that runs the loop. It assembles the context for each model call, dispatches tool calls, captures their results, and decides whether to continue.
- **Deployment** is what turns the prototype into a service: hosting, identity, observability, and the production infrastructure the agent runs on.

#### What is vibe coding?

In February 2025, Andrej Karpathy posted a description of a new way of programming that resonated widely across the software engineering community. He described an approach where you "fully give in to the vibes, embrace exponentials, and forget that the code even exists." In this mode, a developer describes what they want in natural language, accepts the AI's output, and when something breaks, copies the error message back into the prompt and asks the AI to fix it.

The term went viral because it captured something real: many developers were already working this way but hadn't had language for it. Within months, "vibe coding" became a common descriptor for any AI-assisted development workflow, which created confusion. By early 2026, Karpathy himself acknowledged that the original framing was too narrow, introducing the term "agentic engineering" to describe the more disciplined end of the spectrum.

---

### The spectrum: vibe coding to agentic engineering

Rather than treating vibe coding and agentic engineering as a binary, the paper frames them as endpoints on a spectrum. The key differentiator is not whether you use AI. It's how much structure, verification, and human judgment surrounds the AI's output.

**Table 1: The Spectrum from Vibe Coding to Agentic Engineering**

| Dimension | Vibe Coding | Structured AI-Assisted | Agentic Engineering |
|---|---|---|---|
| Intent specification | Casual natural language prompts | Detailed prompts with examples and constraints | Formal specs, architecture docs, memory files |
| Verification | "Does it seem to work?" | Manual testing, spot-checking | Automated test suites, CI/CD gates, LM judges |
| Codebase understanding | Minimal; developer may not read the generated code | Selective review of critical paths | Comprehensive review of architecture; AI handles implementation details |
| Error handling | Copy-paste error messages back to the AI | Developer diagnoses root cause, AI implements fix | Agents self-diagnose within defined bounds; humans handle architectural issues |
| Appropriate scope | Prototypes, scripts, personal projects, hackathons | Features within established codebases | Production systems, team-scale development |
| Risk profile | High; acceptable for disposable code | Moderate; human judgment at key checkpoints | Low; systematic verification at every stage |

**Applied Tip:** The right position on this spectrum depends on the stakes. A weekend prototype can be pure vibe coding. A production API handling financial transactions demands agentic engineering. Most real work falls somewhere in between, and the skill is knowing where to draw the line for each task.

The single biggest differentiator between the two ends is how outputs get verified. In vibe coding, verification is optional; the developer runs the code and checks if it seems right. In agentic engineering, two mechanisms work together. Tests verify the deterministic parts of the system. Evaluations (evals) verify the non-deterministic parts: did the agent take the right trajectory of steps, choose the right tools, and produce a final response that meets the quality bar? Tests are checked by code; evals are checked by labelled datasets, scoring rubrics, and LM judges. Without both, the practice is always vibe coding, regardless of how sophisticated the prompts are.

---

### Context engineering: the real skill

As the field has matured, a key insight has emerged: the quality of AI-generated code depends less on the cleverness of your prompts and more on the quality of the context provided. This realization has given rise to **context engineering** — the practice of providing AI agents with rich, structured information about your codebase, architecture, conventions, and intent.

Developers must consider six primary types of context:
1. **Instructions:** The agent's core role, goals, and operational boundaries.
2. **Knowledge:** Retrieved documents, architectural diagrams, and domain-specific data.
3. **Memory:** Short-term session logs (what just happened) and long-term persistent state (what the project is).
4. **Examples:** Few-shot behavioral demonstrations and codebase reference patterns.
5. **Tools:** The precise definitions of the APIs, scripts, and external services the agent can invoke.
6. **Guardrails:** Hard constraints, formatting rules, and safety validations.

**Static vs. dynamic context:**
- **Static context** is always loaded: system instructions, rule files (AGENTS.md, CLAUDE.md, GEMINI.md), global memory, and persona definitions. It defines who the agent is and how it behaves. Static context is expensive because every token is present in every interaction.
- **Dynamic context** is loaded on demand: skill instructions triggered by task matching, tool results retrieved during execution, documents fetched from RAG pipelines, and windowed session history. Dynamic context is efficient because the agent pays the token cost only when the information is needed.

The design decision of what belongs in static context versus dynamic context is a genuine engineering trade-off. Too much static context wastes tokens and dilutes signals. Too little means the agent forgets critical rules. The best systems treat this boundary as a first-class architectural decision, reviewed and versioned like any other configuration.

**Agent Skills** are the primary pattern for managing dynamic context: structured, portable packages of procedural knowledge that the agent loads only when the task calls for it. Rather than embedding every piece of specialized knowledge into the agent's system prompt, skills allow the agent to remain a lightweight generalist that flexes into specialist roles on demand through progressive disclosure. The agent sees only lightweight metadata at startup, loads full instructions when a task matches, and pulls deep reference material only when explicitly needed.

Agent Skills solve four problems that have plagued AI agent development:
- Context rot from overloaded prompts
- Absence of procedural memory for LLMs
- Operational overhead of multi-agent architectures
- Need for portability across tools and vendors

Context engineering is the bridge between vibe coding and agentic engineering.

---

### The new software development life cycle

#### The traditional SDLC under pressure

The software development life cycle has already been through one major transformation. Over the past two decades, most enterprises moved from sequential waterfall processes to iterative models: Agile sprints, continuous integration, DevOps pipelines, and rapid release cycles.

AI compresses this cycle dramatically, but unevenly: implementation that once took weeks can now be done in hours, while requirements, architecture, and verification remain stubbornly human-paced. The result is not a faster version of the old SDLC. It is a different workflow, where the boundaries between phases blur, iteration cycles shorten from weeks to minutes, and the developer's role shifts from primary implementor to system designer and quality arbiter.

**Note on pace of change:** Early signs suggest that the compression will spread beyond implementation: teams are already experimenting with workflows where developers go directly from specs to review, with AI agents handling implementation, testing, and deployment in the background.

#### How AI transforms each phase

**Requirements and planning:** AI tools can participate directly in requirements refinement: generating user stories from product briefs, identifying edge cases that humans miss, producing API schemas from natural-language descriptions, and generating interactive prototypes from specification documents. Requirements stop being a document handed off between teams. They become a conversation between humans and AI that produces specification and initial implementation simultaneously.

**Design and architecture:** Architecture remains the most stubbornly human-centric phase. Architectural decisions are fundamentally about trade-offs: consistency vs. availability, complexity vs. flexibility, build vs. buy. AI excels at implementing architectural decisions once they are made. Given a clear architecture document, AI agents can scaffold entire applications, generate consistent patterns across modules, and ensure that new code conforms to established conventions.

**Implementation:** Modern coding agents can generate entire features from natural-language descriptions, implement complex algorithms, and produce multi-file changes that work together correctly. Industry surveys report 25–39% productivity improvements. However, a study by METR found that experienced developers using AI assistants actually took 19% longer on certain tasks, largely because of the time spent verifying, debugging, and correcting AI output. AI does not eliminate implementation work so much as transform it from writing to reviewing, guiding, and verifying.

**Testing and quality assurance:** Testing AI-generated code requires evaluating both what the agent produced AND how it got there. Output evaluation checks the final artifact. Trajectory evaluation checks the full sequence of tool calls and intermediate reasoning. Both are necessary because a fluent output that skipped its verification steps is a more dangerous failure than one with a visible error. AI also transforms test generation itself — agents can produce test cases, including edge cases and property-based tests, that humans might not think of.

**Code review and deployment:** AI serves as a first-pass reviewer that can identify potential bugs, style violations, security vulnerabilities, and performance issues before a human reviewer sees the code. Deployment pipelines are becoming AI-aware as well. AI agents can monitor deployment health, automatically roll back problematic releases, and predict deployment risks based on the nature and scope of changes.

**Maintenance and evolution:** Legacy codebases that were once impenetrable to new team members can now be navigated, understood, and modified with AI assistance. Code that was considered "too risky to touch" can now be safely refactored, modernized, and extended. AI agents can systematically migrate codebases between frameworks, update deprecated APIs, and modernize test suites.

---

### The factory model: building the system that builds software

The developer's primary output is not code — it's the system that produces code. This system includes:
- Specifications and context that define what needs to be built
- Agents that translate specifications into implementation
- Tests and quality gates that verify correctness
- Feedback loops that route failures back to agents for correction
- Guardrails that constrain agents to safe, predictable behavior

A factory manager does not assemble every widget by hand. They design the assembly line and ensure quality control. The modern developer designs the development system and ensures that its output meets the required standard. Success comes from giving agents success criteria rather than step-by-step instructions, then letting them iterate.

---

### Harness Engineering: What surrounds the model

There is a temptation to treat the model as the system. That intuition is wrong. The model is one input into a running agent. Everything else — the prompts, the tools, the context policies, the hooks, the sandboxes, the sub-agents, the observability — is the **harness**: the scaffolding wrapped around the model that lets it actually finish something.

**A useful equation:** Agent = Model + Harness

A raw model is not an agent. It becomes one once a harness gives it state, tool execution, feedback loops, and enforceable constraints. The behavior developers experience when working with Claude Code, Cursor, Codex, Antigravity, Aider, or Cline is dominated by what the harness does, not just by which model is underneath.

**Concretely, a harness includes:**
- **Instructions and Rule Files:** The text that defines who the agent is, what it cares about, and what it is forbidden from doing. This includes AGENTS.md, CLAUDE.md, GEMINI.md, skill files, and sub-agent prompts.
- **Tools:** The functions, MCP servers, and APIs the agent can call, plus the prose around them that tells the model when and how to call them.
- **Sandboxes and execution environments:** Where the agent's code actually runs, what it has access to, what it cannot reach.
- **Orchestration logic:** Sub-agent spawning, model routing, hand-offs between specialists, and the rules that govern when each one fires.
- **Guardrails or Hooks:** Deterministic code that runs at specific lifecycle points: before a tool call, after a file edit, before a commit. Hooks are the place for things the agent should never forget but often does.
- **Observability:** Logs, traces, evaluations, cost and latency metering.

**Evidence for the harness effect:** On Terminal Bench 2.0, one team moved a coding agent from outside the Top 30 to the Top 5 by changing only the harness, with no model change at all. A separate study at LangChain raised a coding agent's score on the same benchmark by 13.7 points by tweaking only the system prompt, tools, and middleware around a fixed model.

The key insight: when an agent does something wrong, the first instinct is to blame the model. More often, the failure traces back to a missing tool, a vague rule, an absent guardrail, or a context window stuffed with noise. **Most agent failures, examined honestly, are configuration failures.**

**Harness across the SDLC:**
1. **Requirements, Planning, & Architecture (Configuring the Harness):** Developer sets up the agent's environment — instructions, rule files (AGENTS.md), architectural constraints, tools.
2. **Implementation (Running the Harness):** Sandboxes and execution environments keep the model focused and secure. Code executes in isolated sandbox.
3. **Testing & QA (The Feedback Loop):** Orchestration logic captures test failure output and routes it back to the model for self-correction.
4. **Code Review, Deployment, & Maintenance (Observing the Harness):** Hooks run deterministically (e.g., blocking hard-coded passwords). Observability tracks token costs, latency, and agent drift.

---

### The developer's evolving role: conductors and orchestrators

**The conductor: hands-on, real-time direction**
In conductor mode, a developer works in real-time with an AI pair-programmer. They're in the IDE, watching code appear, guiding the AI with prompts and corrections, maintaining fine-grained control over what gets written. Typical for complex logic, debugging tricky issues, or working in unfamiliar codebases. Tools: GitHub Copilot, Google Gemini Code Assist, Cursor, Windsurf.

**The orchestrator: async, multi-agent delegation**
In orchestrator mode, the developer operates at a higher level of abstraction. They define goals, assign them to agents, and review results — not watching code appear line by line. Agents may be working in the background, in parallel, on different parts of a codebase. Typical for well-defined tasks: bug fixes, feature implementations, codebase migrations, test generation. Tools: Google Jules, GitHub Copilot agent mode, Cursor's background agents, Claude Code.

The orchestrator mode requires different skills:
- **Specification:** Defining tasks precisely enough that an agent can execute them without ambiguity
- **Decomposition:** Breaking large tasks into appropriately sized units for agent execution
- **Evaluation:** Quickly assessing whether agent output meets quality standards
- **System design:** Designing the constraints, tests, and feedback loops that keep agents productive

---

### The 80% problem

A persistent challenge in AI-assisted development: AI agents can rapidly generate approximately 80% of the code for a feature, but the remaining 20% — edge cases, error handling, integration points, and subtle correctness requirements — demands deep contextual knowledge that current models often lack.

The nature of AI errors has evolved from simple syntax mistakes to more insidious conceptual failures: wrong assumptions about business logic, failure to seek clarification on ambiguous requirements, missing edge cases, and architectural decisions that create subtle long-term maintenance burdens. These errors are harder to detect precisely because the code "looks right" and may even pass basic tests.

The developers who navigate this challenge most effectively adopt a specific posture: they use AI for what it's good at (rapid implementation of well-specified tasks) while reserving their own attention for what AI struggles with (ambiguous requirements, architectural trade-offs, and correctness verification).

---

### Coding agents in practice

Coding agents show up in three places in everyday work:

**In the editor:** Inline completion, chat panels, whole-codebase awareness inside the IDE. Examples: GitHub Copilot, Cursor, Windsurf, JetBrains AI Assistant.

**In the terminal:** Coding agents launched from the command line, given a goal in plain language, working across the codebase with full file system access, multi-file edits, ability to run tools and tests. Examples: Antigravity CLI, Claude Code, Codex CLI, OpenCode, Cline.

**In the background:** Agents that take a task and run autonomously in cloud-hosted sandboxes, often producing a pull request as output. Examples: Google Jules, GitHub Copilot agent mode, Cursor's background agents, Google's AlphaEvolve.

---

### Vibe Coding Production-ready Agents

The same terminal-based workflow that produces prototype scripts now reaches production agents. Building, evaluating, and deploying a real agent that runs at scale — with persistent memory, governance, and observability — has moved from a framework and cloud console task into something that happens in the same terminal.

**Google's Agents CLI** is built around this idea. It bundles a set of skills for building agents on Google Cloud and works with whichever coding agent the developer prefers. After a one-time install, the coding agent gains seven new skills covering the full ADK lifecycle: scaffolding a project, writing the agent code, evaluating it, deploying it to Agent Runtime, and wiring up observability.

```
# One-time setup
uvx google-agents-cli setup
# Then in your coding agent:
> Build a support agent that answers questions from our docs.
> evaluate it on the FAQ dataset
> Deploy it to Agent Engine
```

Coordination across agents happens through:
- Shared session state for simple cases
- Model Context Protocol (MCP) for tool access
- Agent2Agent (A2A) protocol for cross-agent delegation

Anthropic's engineering team published an experiment in early 2026 in which agent teams built a working C compiler in Rust over two weeks, with humans setting direction and reviewing output but not writing the implementation.

---

### The Economics of AI Development

**Total Cost of Ownership (TCO) framing:**

The paper reframes AI development economics around CapEx (upfront investment to build) vs. OpEx (ongoing cost to run, fix, maintain), where OpEx is heavily dictated by the token economy.

**The Hidden Debt of Vibe Coding (Low CapEx, High OpEx):**
- **Token Burn Rate:** Dumping massive, unstructured files into context windows and repeatedly asking the model to fix its own unverified mistakes creates expensive "prompting loops" with low first-pass success rates.
- **Maintenance Tax:** Code written through ad-hoc prompting often lacks structural consistency. Debugging unstructured, AI-generated "spaghetti" code is expensive.
- **Security Remediation:** Without an automated evaluation harness, rapid code generation leads to rapid vulnerability generation. Fixing security flaws in production costs exponentially more than catching them during design.

**The Investment of Agentic Engineering (High CapEx, Low OpEx):**
- Deliberate upfront investment: designing API schemas, building deterministic test suites, structuring the agent's context.
- The AI operates within a strictly governed "factory," meaning its output is structurally sound, pre-tested, and aligned with company standards.
- The marginal cost of shipping and maintaining a feature drops dramatically.

**Context Engineering as a Financial Lever:**
- LLMs charge for every piece of information you send them. Passing a 100,000-token repository into every prompt is financially unviable at scale.
- Effective context engineering ensures the model receives a dense, high-signal payload rather than a sprawling, noisy one.
- Dramatically increases the agent's first-pass success rate, avoiding costly trial-and-error loops.

**Intelligent Model Routing:**
- Vibe coding: relies on a single frontier model for every interaction — paying premium token prices just to fix a typo.
- Agentic engineering: routes large models to complex tasks (Requirements, Architecture, initial Implementation), smaller faster cheaper models to deterministic tasks (Test Generation, Code Review, CI/CD monitoring).

---

### Where to start

**For individual developers:**
1. Set up an AGENTS.md (or equivalent) for the project. Start with ten lines: stack, conventions, hard rules, workflow. Add a rule every time the agent does something it should not do again.
2. Install a set of skills for your coding agents (like Agents CLI) to build, evaluate, deploy, and optimize agents.
3. Pick one repetitive workflow and make it the first agent.
4. Write the tests and evals before generating the code. Together they are the contract with the AI.
5. Review every line the agent produces that is going to ship. Be skeptical of anything that looks clever.
6. Maintain your developer skills. Treat AI as a way to apply expertise at a greater scale, not as a substitute for it.

**For engineering leaders:**
1. Make context engineering a first-class engineering practice. Treat AGENTS.md, system prompts, eval suites, and skill libraries as code: reviewed in pull requests, versioned with the project, owned by named engineers.
2. Set the bar at the eval, not the demo. A working demo proves an agent can succeed once. A passing eval suite proves it succeeds reliably.
3. Re-shape code review for AI-generated code. Extra attention to hallucinated dependencies, inadequate error handling, and subtle correctness gaps.
4. Distinguish prototyping work from production work in team norms. Make the boundary explicit.
5. Invest in the harness components as a shared team asset.

**For organizations:**
1. Treat AI-assisted development as an engineering investment, not a productivity feature.
2. Invest in the production substrate before scale: trajectory and final-response evals in CI, traces of every agent run, scoped permissions per agent, security review tuned to AI failure modes.
3. Adopt open standards for tools and inter-agent communication: MCP for tool access, A2A for cross-agent delegation.
4. Plan for hybrid teams of humans and agents, not human-only or agent-only workflows.
5. Reframe hiring and skill development around judgment, not just implementation. The most valuable engineers will be the ones who can direct agents well, not the ones who can write the most code.

---

### Conclusion: Intent as the new Interface

The transition from syntax to intent is not a future prediction — it's a present reality.

Three principles stand out as durable:

1. **Structure scales, vibes don't.** Vibe coding is valid for exploration, prototyping, and personal projects. But for software that organizations depend on, the discipline of agentic engineering — specifications, tests, guardrails, and human oversight of architecture — is not optional.

2. **AI amplifies your engineering culture.** Organizations with strong testing practices, clear architectural standards, and healthy code review processes get dramatically more value from AI-assisted development than those without.

3. **The human role is evolving, not diminishing.** The builders who understand architecture, can define precise specifications, evaluate output critically, and design effective systems of constraints and feedback loops are more valuable than ever.

> "Generation is solved. Verification, judgment, and direction are the new craft."

---

## Endnotes

1. GetPanto, "AI Coding Assistant Statistics 2025-2026," https://www.getpanto.ai/blog/ai-coding-assistant-statistics; Index.dev, "Developer Productivity Statistics with AI Tools"
2. Karpathy, A., "Vibe Coding," X/Twitter post, February 2025.
3. Osmani, A., "Agentic Engineering," https://addyosmani.com/blog/agentic-engineering/
4. Karpathy, A., "From Vibe Coding to Agentic Engineering," 2026
5. Glide Blog, "What is Agentic Engineering?" https://www.glideapps.com/blog/what-is-agentic-engineering
6. CircleCI, "AI-Native SDLC," https://circleci.com/blog/ai-sdlc/
7. GroovyWeb, "SDLC in the AI Era: Software Development 2026"
8. Osmani, A., "The Factory Model," https://addyosmani.com/blog/factory-model/
9. Deloitte, "AI in Software Engineering: Productivity Gains 2025-2026"
10. METR, "Uplift Update: Measuring the Impact of AI Coding Tools," February 2026
11. Google, "Introduction to Agents," Agents Whitepaper Series, November 2025
12. Osmani, A., "From Conductors to Orchestrators: The Future of Agentic Coding," https://addyosmani.com/blog/future-agentic-coding/
13. Google, "Jules: AI-Powered Coding Agent"
14. Osmani, A., "The 80% Problem in Agentic Coding," https://addyo.substack.com/p/the-80-problem-in-agentic-coding
15. Dave Patten, "The State of AI Coding Agents 2026: From Pair Programming to Autonomous AI Teams"
16. Lawfare, "When the Vibes Are Off: The Security Risks of AI-Generated Code"
17. Google, "Introduction to Agents," Multi-Agent Systems and Design Patterns section
18. Google, "Agent Development Kit (ADK)," https://google.github.io/adk-docs/
19. Google, "Agent-to-Agent (A2A) Protocol," https://google.github.io/a2a-protocol/
20. TLDL, "AI Coding Tools 2026," https://www.tldl.io/resources/ai-coding-tools-2026; Kanerika, "GitHub Copilot vs Claude Code vs Cursor vs Windsurf," https://kanerika.com/blogs/github-copilot-vs-claude-code-vs-cursor-vs-windsurf/
21. Google, "Gemini Code Assist," https://cloud.google.com/gemini/docs/codeassist/overview
22. Dark Reading, "Coders Adopt AI Agents, but Security Pitfalls Lurk in 2026," https://www.darkreading.com/application-security/coders-adopt-ai-agents-security-pitfalls-lurk-2026
23. Google, "Gemini CLI," https://github.com/google-gemini/gemini-cli
24. Google, "Agent Tools: Interoperability with Model Context Protocol (MCP)," Agents Whitepaper Series, November 2025
25. Google, "Agent Quality" and "Prototype to Production," Agents Whitepaper Series, November 2025
26. Lawfare, "When the Vibes Are Off: The Security Risks of AI-Generated Code," https://www.lawfaremedia.org/article/when-the-vibe-are-off--the-security-risks-of-ai-generated-code
27. DevOps.com, "AI-Generated Code Packages Can Lead to Slopsquatting Threat," https://devops.com/ai-generated-code-packages-can-lead-to-slopsquatting-threat/
28. Osmani, A., "Beyond Vibe Coding," O'Reilly Media, 2025-2026, https://www.oreilly.com/library/view/beyond-vibe-coding/9798341634749/
29. "Awesome LLM Apps," https://github.com/Shubhamsaboo/awesome-llm-apps
30. Osmani, A., "My LLM Coding Workflow Going Into 2026," https://addyosmani.com/blog/ai-coding-workflow/
31. Questera, "7 AI Coding Trends to Watch in 2026," https://www.questera.ai/blogs/7-ai-coding-trends-to-watch-in-2026
32. DEV Community, "Programming in the Age of AI: From Code to Intent," https://dev.to/robertobutti/programming-in-the-age-of-ai-from-code-to-intent-46eo
