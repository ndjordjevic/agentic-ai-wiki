# cognition.ai

## Fetch log
- Inbox URL: https://cognition.ai/
- Final URL: https://cognition.ai/
- Fetched: 2026-06-10
- Pages: 5
- Mode: standard

## Landing page — https://cognition.ai/

Title: Cognition
Description: Cognition builds autonomous software engineering agents

Navigation: Home | Careers | Research | Blog | Contact | Devin

### Hero
Cognition operates Devin, described as "the first autonomous software engineer." The company's philosophy emphasizes technology expanding human capacity through collaboration rather than replacement. Devin handles planning, writing, testing, and shipping production code within existing codebases and team tools.

### Customers
Mercedes-Benz, Goldman Sachs, Ramp, RV Tech, Anduril, Infosys, Itaú, Cognizant, Nubank, DeNA, Athena Health

### Recent Blog Articles
- Introducing FrontierCode (2026-06-08)
- Estimating the Productivity of an Autonomous AI Software Engineer (2026-06-04)
- AI should earn its keep: Introducing the AI Productivity Guarantee (2026-06-04)
- Introducing Devin Desktop (2026-06-02)
- More Devins in More Places (2026-05-27)
- Devin in Windsurf (2026-04-15)
- An Early Preview of SWE-1.6 and Research Update (2026-03-01)
- How Cognition Uses Devin to Build Devin (2026-02-27)
- Introducing Cognition for Government (2026-02-25)
- Introducing Devin 2.2 (2026-02-24)

### Footer
Social: LinkedIn, X
Legal: website-terms, terms-of-service, privacy-policy, acceptable-use-policy, data-processing-addendum, security

## Research — https://cognition.ai/research

Cognition trains models optimized for software engineering, focusing on systems that perform well in actual workflows rather than isolated benchmarks.

### Key Research Areas

**SWE-Check** — A specialized bug detection model that matches larger frontier models while operating approximately 10× faster.

**SWE-1.6** — Their latest model emphasizing both capability and user experience improvements.

**SWE-1.6 Preview** — Early preview shared March 2026 of ongoing training efforts.

### Open Positions (Research, San Francisco)
- Research Engineer, Infrastructure
- Research, Mid-Training
- Research, Post-Training

## Blog — Introducing Devin — https://cognition.ai/blog/introducing-devin

Cognition introduced Devin as "the first AI software engineer," functioning as an autonomous teammate capable of completing engineering tasks independently or collaboratively.

### Key Capabilities
- Long-term reasoning and planning for complex tasks
- Access to developer tools (shell, code editor, browser) in a sandboxed environment
- Real-time progress reporting and collaboration with human engineers
- Learning from unfamiliar technologies
- End-to-end app building and deployment
- Autonomous bug identification and fixes
- AI model training and fine-tuning
- Open source repository contributions

### Performance
On SWE-bench, Devin resolved 13.86% of real-world GitHub issues end-to-end, vs. the previous state-of-the-art of 1.96%. Evaluated using a random 25% dataset subset, operating unassisted while competing models received assistance.

### Funding
Series A of $21 million led by Founders Fund. Cognition is described as an applied AI lab focused on reasoning.

## Blog — Estimating the Productivity of an Autonomous AI Software Engineer — https://cognition.ai/blog/ai-productivity

Cognition developed an automated system to measure how many productive engineering hours each Devin session delivers.

### Methodology
Unit chosen: "productive engineering hours" — because "Hours are already how organizations value engineering work — salaries and contractor rates are denominated in time."

The system classifies whether sessions produced useful output, then estimates how long a human engineer would have taken to complete the same work.

### Dataset and Results
- 258 sessions across 126 users at enterprise customers
- Estimator achieved r_log of 0.74 on held-out evaluation sessions
- ~50% of estimates fall within a factor of 2 of true values

### Design Principles
1. Reason about the human's path rather than the agent's actual trajectory
2. Credit only work the user didn't specify beforehand
3. Account for codebase familiarity variations
4. Assume relevant expertise to avoid inflating cross-disciplinary work

### Limitations
Ground-truth bias from self-reporting, potential sampling skew toward engaged users, and engineering hours don't directly measure business value or account for quality issues such as post-merge bugs. System is deployed with Devin customers in production.

## Blog — Introducing Devin 2.2 — https://cognition.ai/blog/introducing-devin-2-2

Devin 2.2 introduced three major capability upgrades.

### End-to-End Testing with Computer Use
Devin can access its own Linux desktop to launch and test desktop applications, in addition to existing browser testing. Users can approve testing suggestions and receive screen recordings of the agent's work.

### Devin Review Autofix
The agent completes the full development cycle independently: "it plans, codes, reviews its own output, catches issues, and fixes them — all before you ever open the PR."

### Performance and Interface Improvements
- Startup time reduced by 3×
- Interface redesigned to unify the entire development lifecycle from planning through code review
- New users can access Devin with $10 in credits
- Desktop support enabled by default for sessions after 2026-02-24
