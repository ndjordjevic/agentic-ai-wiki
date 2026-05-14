# anthropic.com

## Fetch log
- Inbox URL: https://www.anthropic.com/engineering/harness-design-long-running-apps
- Final URL: https://www.anthropic.com/engineering/harness-design-long-running-apps
- Fetched: 2026-05-14
- Pages: 6
- Mode: deep-multi-product
- Products discovered: 2
- Products: messages, managed-agents

## Discovery audit

Candidates from docs.anthropic.com/llms.txt section headings (### level):
- `Messages` → classified as **Product** (has `### Messages` heading in llms.txt; own docs subsection at `/docs/en/build-with-claude/`; appeared in comparison table in docs.anthropic.com as a distinct developer surface)
- `Managed Agents` → classified as **Product** (has `### Managed Agents` heading in llms.txt; own docs subsection at `/docs/en/managed-agents/`; described as "Pre-built, configurable agent harness that runs in managed infrastructure")
- `Admin` → classified as **Excluded section** (admin API, not a user-facing product)
- `API Reference` → classified as **Excluded section** (generic reference documentation section)

Candidates from docs.anthropic.com URL path analysis (depth 1/2/3):
- `build-with-claude` (depth 1) → classified as **Sub-section of Messages** (namespace container for the Messages API surface)
- `agents-and-tools/agent-skills` (depth 2) → classified as **Sub-section of Messages** (Agent Skills is a capability within the Messages API, not a standalone product)
- `managed-agents` (depth 1) → classified as **Product** (own path, own llms.txt heading, own overview page)
- `about-claude` (depth 1) → classified as **Excluded section** (generic documentation section about Claude models)
- `api` (depth 1) → classified as **Excluded section** (generic API reference container)

Candidates from landing page (anthropic.com):
- `claude.com` referenced → Claude.ai (separate consumer product; not a developer API product; excluded from this ingest)

Classified as products: messages, managed-agents
Classified as excluded: admin, api-reference, build-with-claude (container), about-claude (container), claude.ai (consumer product, separate ingest)

## Landing page — https://www.anthropic.com/engineering/harness-design-long-running-apps

_Written by Prithvi Rajasekaran, a member of the Anthropic Labs team._

Over the past several months I've been working on two interconnected problems: getting Claude to produce high-quality frontend designs, and getting it to build complete applications without human intervention. This work originated with earlier efforts on our frontend design skill and long-running coding agent harness, where my colleagues and I were able to improve Claude's performance well above baseline through prompt engineering and harness design—but both eventually hit ceilings.

To break through, I sought out novel AI engineering approaches that held across two quite different domains, one defined by subjective taste, the other by verifiable correctness and usability. Taking inspiration from Generative Adversarial Networks (GANs), I designed a multi-agent structure with a **generator** and **evaluator** agent. Building an evaluator that graded outputs reliably—and with taste—meant first developing a set of criteria that could turn subjective judgments like "is this design good?" into concrete, gradable terms.

I then applied these techniques to long-running autonomous coding, carrying over two lessons from our earlier harness work: decomposing the build into tractable chunks, and using structured artifacts to hand off context between sessions. The final result was a three-agent architecture—planner, generator, and evaluator—that produced rich full-stack applications over multi-hour autonomous coding sessions.

### Why naive implementations fall short

We've previously shown that harness design has a substantial impact on the effectiveness of long running agentic coding. In an earlier experiment, we used an initializer agent to decompose a product spec into a task list, and a coding agent that implemented the tasks one feature at a time before handing off artifacts to carry context across sessions. The broader developer community has converged on similar insights, with approaches like the "Ralph Wiggum" method using hooks or scripts to keep agents in continuous iteration cycles.

But some problems remained persistent. For more complex tasks, the agent still tends to go off the rails over time. While decomposing this issue, we observed two common failure modes with agents executing these sorts of tasks.

First is that models tend to lose coherence on lengthy tasks as the context window fills (see our post on context engineering). Some models also exhibit "context anxiety," in which they begin wrapping up work prematurely as they approach what they believe is their context limit. Context resets—clearing the context window entirely and starting a fresh agent, combined with a structured handoff that carries the previous agent's state and the next steps—addresses both these issues.

This differs from compaction, where earlier parts of the conversation are summarized in place so the same agent can keep going on a shortened history. While compaction preserves continuity, it doesn't give the agent a clean slate, which means context anxiety can still persist. A reset provides a clean slate, at the cost of the handoff artifact having enough state for the next agent to pick up the work cleanly. In our earlier testing, we found Claude Sonnet 4.5 exhibited context anxiety strongly enough that compaction alone wasn't sufficient to enable strong long task performance, so context resets became essential to the harness design. This solves the core issue, but adds orchestration complexity, token overhead, and latency to each harness run.

A second issue, which we haven't previously addressed, is self-evaluation. When asked to evaluate work they've produced, agents tend to respond by confidently praising the work—even when, to a human observer, the quality is obviously mediocre. This problem is particularly pronounced for subjective tasks like design, where there is no binary check equivalent to a verifiable software test. Whether a layout feels polished or generic is a judgment call, and agents reliably skew positive when grading their own work.

However, even on tasks that do have verifiable outcomes, agents still sometimes exhibit poor judgment that impedes their performance while completing the task. Separating the agent doing the work from the agent judging it proves to be a strong lever to address this issue. The separation doesn't immediately eliminate that leniency on its own; the evaluator is still an LLM that is inclined to be generous towards LLM-generated outputs. But tuning a standalone evaluator to be skeptical turns out to be far more tractable than making a generator critical of its own work, and once that external feedback exists, the generator has something concrete to iterate against.

### Frontend design: making subjective quality gradable

I started by experimenting on frontend design, where the self-evaluation issue was most visible. Absent any intervention, Claude normally gravitates toward safe, predictable layouts that are technically functional but visually unremarkable.

Two insights shaped the harness I built for frontend design. First, while aesthetics can't be fully reduced to a score—and individual tastes will always vary—they can be improved with grading criteria that encode design principles and preferences. "Is this design beautiful?" is hard to answer consistently, but "does this follow our principles for good design?" gives Claude something concrete to grade against. Second, by separating frontend generation from frontend grading, we can create a feedback loop that drives the generator toward stronger outputs.

With this in mind, I wrote four grading criteria that I gave to both the generator and evaluator agents in their prompts:

- **Design quality:** Does the design feel like a coherent whole rather than a collection of parts? Strong work here means the colors, typography, layout, imagery, and other details combine to create a distinct mood and identity.
- **Originality:** Is there evidence of custom decisions, or is this template layouts, library defaults, and AI-generated patterns? A human designer should recognize deliberate creative choices. Unmodified stock components—or telltale signs of AI generation like purple gradients over white cards—fail here.
- **Craft:** Technical execution: typography hierarchy, spacing consistency, color harmony, contrast ratios. This is a competence check rather than a creativity check. Most reasonable implementations do fine here by default; failing means broken fundamentals.
- **Functionality:** Usability independent of aesthetics. Can users understand what the interface does, find primary actions, and complete tasks without guessing?

I emphasized design quality and originality over craft and functionality. Claude already scored well on craft and functionality by default, as the required technical competence tended to come naturally to the model. But on design and originality, Claude often produced outputs that were bland at best. The criteria explicitly penalized highly generic "AI slop" patterns, and by weighting design and originality more heavily it pushed the model toward more aesthetic risk-taking.

I calibrated the evaluator using few-shot examples with detailed score breakdowns. This ensured the evaluator's judgment aligned with my preferences, and reduced score drift across iterations.

I built the loop on the Claude Agent SDK, which kept the orchestration straightforward. A generator agent first created an HTML/CSS/JS frontend based on a user prompt. I gave the evaluator the Playwright MCP, which let it interact with the live page directly before scoring each criterion and writing a detailed critique. In practice, the evaluator would navigate the page on its own, screenshotting and carefully studying the implementation before producing its assessment. That feedback flowed back to the generator as input for the next iteration. I ran 5 to 15 iterations per generation, with each iteration typically pushing the generator in a more distinctive direction as it responded to the evaluator's critique. Because the evaluator was actively navigating the page rather than scoring a static screenshot, each cycle took real wall-clock time. Full runs stretched up to four hours. I also instructed the generator to make a strategic decision after each evaluation: refine the current direction if scores were trending well, or pivot to an entirely different aesthetic if the approach wasn't working.

Across runs, the evaluator's assessments improved over iterations before plateauing, with headroom still remaining. Some generations refined incrementally. Others took sharp aesthetic turns between iterations.

The wording of the criteria steered the generator in ways I didn't fully anticipate. Including phrases like "the best designs are museum quality" pushed designs toward a particular visual convergence, suggesting that the prompting associated with the criteria directly shaped the character of the output.

While scores generally improved over iterations, the pattern was not always cleanly linear. Later implementations tended to be better as a whole, but I regularly saw cases where I preferred a middle iteration over the last one. Implementation complexity also tended to increase across rounds, with the generator reaching for more ambitious solutions in response to the evaluator's feedback. Even on the first iteration, outputs were noticeably better than a baseline with no prompting at all, suggesting the criteria and associated language themselves steered the model away from generic defaults before any evaluator feedback led to further refinement.

In one notable example, I prompted the model to create a website for a Dutch art museum. By the ninth iteration, it had produced a clean, dark-themed landing page for a fictional museum. The page was visually polished but largely in line with my expectations. Then, on the tenth cycle, it scrapped the approach entirely and reimagined the site as a spatial experience: a 3D room with a checkered floor rendered in CSS perspective, artwork hung on the walls in free-form positions, and doorway-based navigation between gallery rooms instead of scroll or click. It was the kind of creative leap that I hadn't seen before from a single-pass generation.

### Scaling to full-stack coding

With these findings in hand, I applied this GAN-inspired pattern to full-stack development. The generator-evaluator loop maps naturally onto the software development lifecycle, where code review and QA serve the same structural role as the design evaluator.

**The architecture**

In our earlier long-running harness, we had solved for coherent multi-session coding with an initializer agent, a coding agent that worked one feature at a time, and context resets between sessions. Context resets were a key unlock: the harness used Sonnet 4.5, which exhibited the "context anxiety" tendency mentioned earlier. Creating a harness that worked well across context resets was key to keeping the model on task. Opus 4.5 largely removed that behavior on its own, so I was able to drop context resets from this harness entirely. The agents were run as one continuous session across the whole build, with the Claude Agent SDK's automatic compaction handling context growth along the way.

For this work I built on the foundation from the original harness with a three-agent system, with each agent addressing a specific gap I'd observed in prior runs. The system contained the following agent personas:

**Planner:** Our previous long-running harness required the user to provide a detailed spec upfront. I wanted to automate that step, so I created a planner agent that took a simple 1-4 sentence prompt and expanded it into a full product spec. I prompted it to be ambitious about scope and to stay focused on product context and high level technical design rather than detailed technical implementation. This emphasis was due to the concern that if the planner tried to specify granular technical details upfront and got something wrong, the errors in the spec would cascade into the downstream implementation. It seemed smarter to constrain the agents on the deliverables to be produced and let them figure out the path as they worked. I also asked the planner to find opportunities to weave AI features into the product specs.

**Generator:** The one-feature-at-a-time approach from the earlier harness worked well for scope management. I applied a similar model here, instructing the generator to work in sprints, picking up one feature at a time from the spec. Each sprint implemented the app with a React, Vite, FastAPI, and SQLite (later PostgreSQL) stack, and the generator was instructed to self-evaluate its work at the end of each sprint before handing off to QA. It also had git for version control.

**Evaluator:** Applications from earlier harnesses often looked impressive but still had real bugs when you actually tried to use them. To catch these, the evaluator used the Playwright MCP to click through the running application the way a user would, testing UI features, API endpoints, and database states. It then graded each sprint against both the bugs it had found and a set of criteria modeled on the frontend experiment, adapted here to cover product depth, functionality, visual design, and code quality. Each criterion had a hard threshold, and if any one fell below it, the sprint failed and the generator got detailed feedback on what went wrong.

Before each sprint, the generator and evaluator negotiated a sprint contract: agreeing on what "done" looked like for that chunk of work before any code was written. This existed because the product spec was intentionally high-level, and I wanted a step to bridge the gap between user stories and testable implementation. The generator proposed what it would build and how success would be verified, and the evaluator reviewed that proposal to make sure the generator was building the right thing. The two iterated until they agreed.

Communication was handled via files: one agent would write a file, another agent would read it and respond either within that file or with a new file that the previous agent would read in turn. The generator then built against the agreed-upon contract before handing the work off to QA. This kept the work faithful to the spec without over-specifying implementation too early.

**Running the harness**

For the first version of this harness, I used Claude Opus 4.5, running user prompts against both the full harness and a single-agent system for comparison. I used Opus 4.5 since this was our best coding model when I began these experiments.

Prompt: "Create a 2D retro game maker with features including a level editor, sprite editor, entity behaviors, and a playable test mode."

| Harness | Duration | Cost |
|---|---|---|
| Solo | 20 min | $9 |
| Full harness | 6 hr | $200 |

The harness was over 20x more expensive, but the difference in output quality was immediately apparent. The solo run produced a non-functional game (broken entity-to-runtime wiring). The harness run expanded the spec to 16 features across ten sprints, and the resulting application was functional: entities appeared, responded to input, and the planner had woven in a Claude integration for AI-assisted game creation.

**Iterating on the harness**

The first set of harness results was encouraging, but it was also bulky, slow, and expensive. The logical next step was to find ways to simplify the harness without degrading its performance. This was partly common sense and partly a function of a more general principle: every component in a harness encodes an assumption about what the model can't do on its own, and those assumptions are worth stress testing, both because they may be incorrect, and because they can quickly go stale as models improve. Our blog post Building Effective Agents frames the underlying idea as "find the simplest solution possible, and only increase complexity when needed."

With Opus 4.6 released (improved long-context retrieval, better self-evaluation, less context anxiety), I removed the sprint construct entirely. The sprint structure had helped to decompose work into chunks for the model to work coherently. Given the improvements in Opus 4.6, there was good reason to believe that the model could natively handle the job without this sort of decomposition.

I kept both the planner and evaluator, as each continued to add obvious value. Without the planner, the generator under-scoped. With the sprint construct removed, I moved the evaluator to a single pass at the end of the run rather than grading per sprint. The evaluator's value depends on where the task sits relative to model capability: for tasks within the model's wheelhouse, the evaluator becomes unnecessary overhead; for tasks at the edge of the generator's capabilities, the evaluator gives real lift.

**Results from the updated harness**

Prompt: "Build a fully featured DAW in the browser using the Web Audio API."

| Agent & Phase | Duration | Cost |
|---|---|---|
| Planner | 4.7 min | $0.46 |
| Build (Round 1) | 2 hr 7 min | $71.08 |
| QA (Round 1) | 8.8 min | $3.24 |
| Build (Round 2) | 1 hr 2 min | $36.89 |
| QA (Round 2) | 6.8 min | $3.09 |
| Build (Round 3) | 10.9 min | $5.88 |
| QA (Round 3) | 9.6 min | $4.06 |
| **Total V2 Harness** | **3 hr 50 min** | **$124.70** |

The builder ran coherently for over two hours without sprint decomposition. The QA agent caught real gaps (display-only DAW features, stubbed audio recording, missing clip operations). The final app had all core pieces of a functional music production program including an AI-powered composition agent.

### What comes next

As models continue to improve, we can roughly expect them to be capable of working for longer, and on more complex tasks. In some cases, that will mean the scaffold surrounding the model matters less over time, and developers can wait for the next model and see certain problems solve themselves. On the other hand, the better the models get, the more space there is to develop harnesses that can achieve complex tasks beyond what the model can do at baseline.

Key lessons worth carrying forward: experiment with the model you're building against, read its traces on realistic problems, and tune its performance to achieve your desired outcomes. When working on more complex tasks, there is sometimes headroom from decomposing the task and applying specialized agents to each aspect of the problem. And when a new model lands, it is generally good practice to re-examine a harness, stripping away pieces that are no longer load-bearing to performance and adding new pieces to achieve greater capability that may not have been possible before.

From this work, the conviction is that the space of interesting harness combinations doesn't shrink as models improve. Instead, it moves, and the interesting work for AI engineers is to keep finding the next novel combination.

## Docs — https://docs.anthropic.com/en/docs/overview

Claude is a highly performant, trustworthy, and intelligent AI platform built by Anthropic. Claude excels at tasks involving language, reasoning, analysis, coding, and more.

The latest Claude models: Claude Opus 4.7, Claude Sonnet 4.6, Claude Haiku 4.5.

Anthropic offers two ways to build with Claude:

| | Messages API | Claude Managed Agents |
|---|---|---|
| What it is | Direct model prompting access | Pre-built, configurable agent harness that runs in managed infrastructure |
| Best for | Custom agent loops and fine-grained control | Long-running tasks and asynchronous work |

## Models — https://docs.anthropic.com/en/about-claude/models/overview

Claude is a family of state-of-the-art large language models. Key models:

| Model | API ID | Context | Max Output | Pricing |
|---|---|---|---|---|
| Claude Opus 4.7 | claude-opus-4-7 | 1M tokens | 128k tokens | $5/MTok in, $25/MTok out |
| Claude Sonnet 4.6 | claude-sonnet-4-6 | 1M tokens | 64k tokens | $3/MTok in, $15/MTok out |
| Claude Haiku 4.5 | claude-haiku-4-5-20251001 | 200k tokens | 64k tokens | $1/MTok in, $5/MTok out |

Available through Claude API, Claude Platform on AWS, Amazon Bedrock, Vertex AI, and Microsoft Foundry.

## Product: Messages API

- Slug: messages
- Deep link: n/a
- Docs URL: https://docs.anthropic.com/en/build-with-claude/overview
- Companion repo: n/a

### About

The Messages API provides direct model prompting access for custom agent loops and fine-grained control. Developers construct every turn, manage conversation state, and write their own tool loop. Best for custom integrations, bespoke agent architectures, and scenarios requiring precise control over the conversation flow.

Key capabilities: text and image input, multilingual support, tool use/function calling, extended thinking (Sonnet 4.6+), vision, batch processing, and the Agent Skills system for modular capability extension.

### Docs — https://docs.anthropic.com/en/agents-and-tools/agent-skills/overview

**Agent Skills** are modular capabilities that extend Claude's functionality. Each Skill packages instructions, metadata, and optional resources (scripts, templates) that Claude uses automatically when relevant.

Skills are reusable, filesystem-based resources that provide Claude with domain-specific expertise: workflows, context, and best practices that transform general-purpose agents into specialists. Unlike prompts (conversation-level instructions for one-off tasks), Skills load on-demand and eliminate the need to repeatedly provide the same guidance across multiple conversations.

Three tiers of loading:
- **Level 1 (Metadata):** YAML frontmatter with name and description; ~100 tokens per Skill; always loaded at startup
- **Level 2 (Instructions):** SKILL.md body with procedures and best practices; under 5k tokens; loaded when triggered
- **Level 3 (Resources):** Bundled scripts and reference files; effectively unlimited; loaded as needed via bash

This filesystem-based architecture enables **progressive disclosure**: Claude loads information in stages as needed, rather than consuming context upfront. When Claude runs a script, only the output (not the code) enters the context window, making scripts far more efficient than having Claude generate equivalent code on the fly.

Pre-built Agent Skills are available for PowerPoint, Excel, Word, and PDF. Custom Skills can be created in Claude Code, uploaded through the Claude API, or added in claude.ai settings.

## Product: Managed Agents

- Slug: managed-agents
- Deep link: https://docs.anthropic.com/en/managed-agents/overview
- Docs URL: https://docs.anthropic.com/en/managed-agents/overview
- Companion repo: n/a

### About

Claude Managed Agents provides the harness and infrastructure for running Claude as an autonomous agent. Instead of building your own agent loop, tool execution, and runtime, you get a fully managed environment where Claude can read files, run commands, browse the web, and execute code securely. The harness supports built-in prompt caching, compaction, and other performance optimizations for high-quality, efficient agent outputs. Currently in beta (requires `managed-agents-2026-04-01` header).

Core concepts:
- **Agent:** The model, system prompt, tools, MCP servers, and skills
- **Environment:** A configured container template (packages, network access)
- **Session:** A running agent instance within an environment, performing a specific task
- **Events:** Messages exchanged between your application and the agent (user turns, tool results, status updates)

### Docs — https://docs.anthropic.com/en/managed-agents/overview

How it works:
1. Create an agent (define model, system prompt, tools, MCP servers, skills)
2. Create an environment (configure cloud container with packages, network access)
3. Start a session (launch session referencing agent and environment)
4. Send events and stream responses (Claude autonomously executes tools, streams back results via SSE; event history persisted server-side)
5. Steer or interrupt (send additional user events mid-execution, or interrupt to change direction)

When to use: long-running execution (minutes to hours), cloud infrastructure (secure containers), minimal infrastructure overhead, stateful sessions (persistent filesystems and conversation history).

Built-in tools: Bash (shell commands), File operations (read/write/edit/glob/grep), Web search and fetch, MCP servers.

### Multi-Agent Orchestration — https://docs.anthropic.com/en/managed-agents/multi-agent

Multi-agent orchestration lets one agent coordinate with others to complete complex work. Agents can act in parallel with their own isolated context.

All agents share the same container and filesystem, but each runs in its own **session thread** — a context-isolated event stream with its own conversation history. The coordinator reports activity in the **primary thread**; additional threads are spawned at runtime when the coordinator delegates.

Threads are persistent: the coordinator can send follow-ups to previously called agents, which retain their prior context.

Patterns that work well:
- **Parallelization:** Fan out independent subtasks simultaneously; coordinator synthesizes results
- **Specialization:** Route to domain-focused agents (security, documentation) rather than loading one agent with every capability
- **Escalation:** Consult a more capable model for a subset of complex subtasks

Configuration: set `multiagent` on the coordinator agent definition with a roster of `agents`. Maximum 20 unique agents; maximum 25 concurrent threads per session. Coordinator can call multiple copies of the same agent.
