# blog.n8n.io

## Fetch log
- Inbox URL: https://blog.n8n.io/meet-nod/
- Final URL: https://blog.n8n.io/meet-nod/
- Fetched: 2026-11-16
- Pages: 11
- Mode: standard
- Note: https://blog.n8n.io/llms.txt returned HTML blog homepage (not a catalog); treated as absent. Docs discovery on blog.n8n.io found only blog sitemap; product docs captured from linked nod.n8n.io/docs/. Companion discovered: https://github.com/n8n-io/nod


## Landing page — https://blog.n8n.io/meet-nod/
Title: Meet Nod: a standalone personal agent from n8n Labs that runs on your computer

URL Source: https://blog.n8n.io/meet-nod/

Published Time: 2026-11-10T12:52:49.000Z

Markdown Content:
Today we're releasing Nod as a research preview from n8n Labs, a new team within n8n that experiments with ideas outside our core product. Nod is a standalone app, separate from n8n, that runs on your computer. It's a personal agent with its own computer and browser: you tell it what you need, and it works in your apps and on websites until the job is finished. It's open source, and it uses the AI provider you choose.

You can download Nod for Mac and Windows. The code is on GitHub under an open-source licence.

[Video 3](https://www.youtube.com/watch?v=cjEK7V9GucQ)

See Nod in Action

## Why we built it

n8n has always been about helping people automate work. That was true before AI and it's true now. AI lets software take on more kinds of work, but the goal is the same.

A lot of what people build in n8n is multiplayer: processes that a team or a business shares and runs on a shared n8n instance. Nod is for a single player. It's built for one person, connects to that person's accounts, and gets their jobs done, whether the job is for their business or their household.

Nod also lives outside n8n. It's a separate app from n8n and from the agents you can build inside n8n, and you don't need an n8n account to use it. You install it on your computer, connect your accounts and ask for something. There's no server or cloud service to set up first.

When we sat down with early testers, many of them placed Nod in the same spot on their own: their chat assistant is where they think and write, n8n runs their shared processes, and Nod takes the ongoing jobs that are theirs alone.

Nod is a n8n Labs experiment, and it doesn't change the direction of n8n. Work on n8n and the n8n agent continues as planned. Building and using Nod has taught us a lot about how AI can take on more of the work people do, and we're releasing it as a research preview so more people can use it and show us where it should go next.

## What Nod does

Because Nod has its own computer (a sandbox that runs locally) and browser, it can finish jobs that a chat tool would hand back to you as a to-do list. It works in the apps you connect, such as Gmail, Calendar, Drive and Slack, and on websites that have no integration at all.

Some of the jobs people hand it:

*   Cancel a subscription, turn down the retention offers and ask for your refund
*   Watch a price and tell you when it drops
*   Find a hotel that fits your trip and book it once you say go
*   Sign in to your supplier portals each month, download the invoices, and file them for your accountant
*   Pull last week's numbers from a dashboard that has no way to export the data and put them in your weekly report

Nod also works ahead of you: it reads your connected apps and offers the jobs it could take off your plate. You talk to it in one conversation, in the app or on Telegram or WhatsApp, while it runs several jobs in parallel in the background. Jobs that repeat, like a morning brief or a price check, can run on a schedule.

## It gets to know you

Nod remembers months of conversation, so you don't have to keep reminding it what you want. On [LongMemEval](https://xiaowu0162.github.io/long-mem-eval/), a public benchmark for long-term memory, it scored 93.2%, among the best published memory systems.

It learns your preferences as you go, and when you connect Gmail it checks how you write so its drafts sound like you. It also writes down how it got a task done, uses those notes the next time, and fixes them when a site changes. You can see, edit or delete anything Nod keeps about you.

## Who it's for

Nod is for anyone who wants to hand the mundane parts of their week to AI: the forms, the follow-ups, the logins and the reminders. Solo operators and freelancers use it for their business, and plenty of people use it for errands at home.

For now you connect your own AI provider, with an API key or your ChatGPT plan, so Nod suits people who are comfortable with that kind of setup. If you use n8n, you can connect your instance so Nod can work with your workflows.

## Built to be trustworthy

An agent that can send email and pay with your card has to earn your trust. We designed Nod so you can check how it behaves.

**It's yours**  
Nod is open source under Apache 2.0, and every rule it follows is in the code. It runs on your Mac, your Windows PC or your own server, with the model provider you choose.

**It works in its own sandbox**  
Nod works inside a private virtual machine on your computer, with its own browser. Its data, memory and saved logins stay on the machine running it; your AI provider gets what each task needs.

**Only you give it permission**  
Before Nod sends, pays, posts or deletes anything you didn't ask for, a separate check confirms you asked for it. A web page or an email can't give Nod orders.

**The AI never sees your passwords**  
Your saved logins and cards are encrypted on your machine, and Nod enters them through private forms the model can't read.

**Everything is on record**  
Nod logs every sign-in, card use and action in your apps, along with what each task cost.

The permission check is itself a model and can make mistakes, which is why Nod asks when your words don't cover an action.

## What it costs

Nod is open source and free. You pay your model provider for the AI you use, or you can connect an open-source model running on your own computer. Some early testers found tasks cost more than they expected, so cost has been a focus of our recent releases, and the latest one brought it down substantially.

Nod also has guardrails so costs don't run away:

*   Every task shows what it cost, and a finished task ends with a receipt
*   You can set a monthly spending limit
*   Nod checks in with you once a task passes $5, and you can change that amount
*   Each schedule shows its estimated monthly cost

## What it doesn't do, yet

*   When Nod is running on your laptop, it stops when the laptop sleeps. Some testers keep it on an always-on Mac mini or run it on their own server, and a hosted version is on our roadmap.
*   Each installation has one owner.
*   It can't make phone calls.

## Try it

Download Nod for Mac or Windows, or read the code on GitHub. Then hand it one job from your list. Tell us how it went on the [community forum post](https://community.n8n.io/t/nod-an-open-source-personal-agent-with-its-own-computer-research-preview-from-n8n-labs/328026), or with Send feedback in the app.

More info:  
[https://github.com/n8n-io/nod](https://github.com/n8n-io/nod) - Github repo  
[https://nod.n8n.io/docs/](https://nod.n8n.io/docs/) - Nod Docs

**Download and install Nod:**  
[**https://nod.n8n.io**](https://nod.n8n.io/)



## Product home — https://nod.n8n.io/
Title: Nod · Your personal agent

URL Source: https://nod.n8n.io/

Markdown Content:
Research preview

## Meet Nod

Open source personal agent with its own computer. It chases invoices, preps your calls and cancels trials. On your machine, with your approval.

Free · Apache 2.0 · [All install options](https://nod.n8n.io/docs/get-started/install-desktop/)

![Image 1](https://nod.n8n.io/docs/_astro/hero-collage.D0GYu5h7_Z1P4D19.jpg)

### 98%of jobs finished

226 errands, each run three times.

### 0 of 678 runs acted without permission

The same runs, checked for any action beyond what the user allowed.

### 93%of facts recalled

500 questions about earlier chats, asked in new sessions.

### 0 of 216 false memories planted

108 published attack emails, each tried two ways.

## On your machine, on your word

It gets on with the work, and asks before it speaks for you.

### Walk into every call prepared

Every morning, Nod reads your threads, your calendar and the client's latest news, and writes a one-page brief for each call.

Nod stores the brief on the computer or server that runs it. Your model service receives the information needed for the task.

![Image 2](https://nod.n8n.io/docs/_astro/brief-collage.CXp10RLz_ZKa5Un.jpg)

Your brief for Brightline is ready.

Brightline Studio – call brief.pdf PDF · 1 page · 40 KB

Call brief

Brightline Studio

Tuesday, 27 October 2026 · 11:00–11:30 · Sara Kim, producer

Where things stand

Sara wants 3 short videos for the Brightline launch. She asked about pricing in Slack last week and is waiting on an answer.

From your last emails

*   Launch date moved to 20 November.
*   They liked the cut-down format of the September reel.
*   Brand assets folder still to be shared.

Their latest news

*   New pricing page: 3 plans from $1,200.
*   Opened a second studio in Lisbon.

Ask on the call

*   Deadline for the first cut?
*   Who signs off on scripts?
*   Budget range for 3 videos?

### Catch the question you missed

Nod finds the question you never answered, like a client's pricing ask from last week, and drafts the reply from your own pricing sheet.

You decide what it may send. Nod checks each action against your request and rules, and asks when they don't cover it.

![Image 3](https://nod.n8n.io/docs/_astro/reply-collage.DNZvTat0_1Oy2Kg.jpg)

Also: Sara asked in Slack last week, **“What would pricing look like for 3 videos?”** and it was never answered. I pulled your pricing sheet from Notion and drafted a reply:

> Hi Sara! For three launch videos it’s **$3,600** ($1,200 each), first cuts in 10 working days. Happy to walk you through it on a call.

Reply to Sara in Slack?

Yes, reply

Replied in Slack ✅

### Hear about it when it matters

Tell Nod to keep an eye on a client's pricing page. It checks every few hours and only speaks up when something changes.

Each check uses the model service you choose. Nod shows estimated model costs in Usage.

![Image 4](https://nod.n8n.io/docs/_astro/watch-collage.DpjSUkUz_Z1lx8OE.jpg)

**Nod**now

Brightline pricing changed: 3 plans from $1,500, was $1,200.

Brightline pricing page

Recurring

Every 6 hours Next 27 Oct, 12:00

Check brightline.studio/pricing and tell me when their plans or prices change

Baseline: 3 plans from $1,200 · 26 Oct, 18:00

## A memory like an elephant

See how we test [recall](https://nod.n8n.io/docs/how-it-works/benchmarks/#longmemeval-s-recall).

1.   ### ![Image 5](blob:http://localhost/83ce1c4e260b652dd5af0b95d8d79c85)Tell it once

Say Anna handles invoices now, and it remembers from then on.

2.   ### ![Image 6](blob:http://localhost/20f19fc33d89087e03c0ebd484f4845c)Every note, visible

See, edit or forget each one, with the message it came from.

3.   ### ![Image 7](blob:http://localhost/d7e7e9083888c2c8f575c1eb498b02b7)Drafts that sound like you

Learns your style from sent emails, no names or numbers.

4.   ### ![Image 8](blob:http://localhost/c66b3d600b7dae3c466c66323d172e6f)It learns how to do a task

Reuses the steps and fixes them when a site changes.

## Hand it the hard ones

Jobs that take an afternoon of tabs, logins and forms. Nod finishes them start to end.

Finance

Chase it until it's paid

Friendly reminders, and it asks before a second nudge

Life Admin

Get your money back

Cancels, turns down the offers to stay, asks for a refund

Work

Client requests into tasks

From email and Slack into Linear, skipping duplicates

Admin

File your month-end paperwork

Bank and tax statements, downloaded and filed by name

Travel

Book the team offsite

Compares three spaces, books the best once you say go

## Coming next

1.   **Managed hosting.** An always-on Nod, hosted for you.

2.   **Make phone calls.** For the errands that still need a voice.

3.   **Nod for your team.** Share one Nod, with its apps and memory.

4.   **Make it your own.** Add your own skills and tools without touching the core.

## Straight answers

How do I set it up?
[Install the app](https://nod.n8n.io/docs/get-started/install-desktop/) on your machine and add your [AI provider](https://nod.n8n.io/docs/connect/models/): OpenAI, Anthropic, OpenRouter, or your ChatGPT Plus or Pro plan. [Connect your apps](https://nod.n8n.io/docs/connect/apps/) (Gmail, Slack, Notion, Drive, Calendar) with one sign-in, and save the logins Nod may use on websites. Then ask for something, in the app or on [Telegram](https://nod.n8n.io/docs/use/channels/). About ten minutes.

Which models can I use?
Any of [30+ providers](https://nod.n8n.io/docs/connect/models/), including OpenAI, Anthropic, Google and OpenRouter, or your ChatGPT Plus or Pro plan. You can also run a [local model](https://nod.n8n.io/docs/connect/local-models/) through Ollama, LM Studio, vLLM or llama.cpp. A local model needs tool calling and a 64,000-token context, and small models are less reliable at the safety check.

Is it for work or personal stuff?
Built for people who run their own work: client calls, follow-ups, invoices, supplier portals. It handles life admin too, like a refund or a booking.

What does it cost?
Nod is free to download. Connect an AI service or a supported plan. Provider fees apply, and Nod [shows estimated model costs in Usage](https://nod.n8n.io/docs/use/spending/).

Do I need n8n?
No, Nod is its own app, made by the team behind [n8n](https://n8n.io/). It is not the n8n AI Assistant.

Which computers?
Mac with macOS 14 or later, Windows 11 in preview, [Linux x64 as a Flatpak preview](https://nod.n8n.io/docs/get-started/install-desktop/#linux), or [your own server](https://nod.n8n.io/docs/deploy/self-host/) for one person.

Can I use it in Europe?
Yes. Nod runs on your own computer, so it works wherever your computer does, including the EU, the UK and Switzerland. Your AI provider's own terms still apply.

Where does my data go?
Nod [stores your database, files, memory, and saved logins](https://nod.n8n.io/docs/trust/privacy/) on the computer or server that runs it. Model services, apps, and websites receive the data they need for your tasks. App connections use n8n and Composio by default. Beyond update checks, n8n receives usage data to improve Nod, which you can turn off anytime in Settings, and whatever you choose to share, such as feedback, traces or your email.

Does it work when my laptop is closed?
Nod needs the computer running it to stay on and awake. To keep [schedules](https://nod.n8n.io/docs/use/schedules/) running while your laptop is closed, run Nod on [your own server](https://nod.n8n.io/docs/deploy/self-host/) or a [Mac mini](https://nod.n8n.io/docs/deploy/mac-mini/) that stays on.

Can I run it in the cloud?
Yes. You can [host Nod on your own server](https://nod.n8n.io/docs/deploy/self-host/) for one person. A managed hosted version is on the roadmap.

Can it make mistakes?
Yes. Its [safety check](https://nod.n8n.io/docs/trust/) is a model's judgement, and Nod is an experiment. That is why it asks before actions your request does not cover. [Usage](https://nod.n8n.io/docs/use/spending/) shows recorded app actions, sign-ins, and model costs.

Where can I get help?
Start with the [docs](https://nod.n8n.io/docs/), which cover setup and the [common problems](https://nod.n8n.io/docs/deploy/troubleshooting/). If something goes wrong, choose [Send feedback](https://nod.n8n.io/docs/use/chat/#send-feedback) in the chat. It goes to the Nod team at n8n. You can review the diagnostic report before you send it. For questions and tips from other people using Nod, ask in the[n8n community forum](https://community.n8n.io/c/n8n-labs/48).



## Docs — https://nod.n8n.io/docs/
Title: Nod docs

URL Source: https://nod.n8n.io/docs/

Markdown Content:
[Skip to content](https://nod.n8n.io/docs/#_top)

[![Image 1](https://nod.n8n.io/docs/_astro/nod-dark.Cbk1dc7D.svg)![Image 2](https://nod.n8n.io/docs/_astro/nod-light.DOMfonca.svg)Nod](https://nod.n8n.io/docs/)

Search Ctrl K

Cancel

Clear

[GitHub](https://github.com/n8n-io/nod)

Select theme 

# Nod docs

A personal assistant with its own computer. You give it the task. You keep control of your accounts and actions.

[Install Nod](https://nod.n8n.io/docs/get-started/install-desktop/)[What is Nod?](https://nod.n8n.io/docs/get-started/what-is-nod/)

![Image 3: Nod comparing three venues in a table and drafting a booking request it hasn't sent.](https://nod.n8n.io/docs/_astro/card-chat-light.BVi8rUvJ_129vQa.webp)![Image 4: Nod comparing three venues in a table and drafting a booking request it hasn't sent.](https://nod.n8n.io/docs/_astro/card-chat-dark.DynKyDKG_2vJ4bt.webp)

Give it the whole task

![Image 5: The Tasks page with a weekday calendar check and a Friday recap scheduled.](https://nod.n8n.io/docs/_astro/card-tasks-light.GIa5r41n_Zk8Nl2.webp)![Image 6: The Tasks page with a weekday calendar check and a Friday recap scheduled.](https://nod.n8n.io/docs/_astro/card-tasks-dark.DDtExn4Z_Z1vcYp3.webp)

Keep watch on a schedule

![Image 7: Usage with this month's spending and every recorded app action, sign-in and card use.](https://nod.n8n.io/docs/_astro/card-usage-light.DBq3p-vn_1OSLlo.webp)![Image 8: Usage with this month's spending and every recorded app action, sign-in and card use.](https://nod.n8n.io/docs/_astro/card-usage-dark.ilZX22Bs_ZSoq2A.webp)

See everything it did and spent

## Start here

[Section titled “Start here”](https://nod.n8n.io/docs/#start-here)

Get set up

*   [Install the desktop app](https://nod.n8n.io/docs/get-started/install-desktop/) on Mac or Windows, or use the Linux x64 Flatpak preview
*   [Install from source](https://nod.n8n.io/docs/get-started/install-from-source/) on macOS or Linux
*   [Host your own server](https://nod.n8n.io/docs/deploy/self-host/) and connect from the web or desktop app
*   [Connect a supported model service](https://nod.n8n.io/docs/connect/models/), or [run a model locally](https://nod.n8n.io/docs/connect/local-models/)

Try your first task

*   [Your first conversation](https://nod.n8n.io/docs/get-started/first-conversation/)
*   [Chat with Nod](https://nod.n8n.io/docs/use/chat/) from the app, Telegram or WhatsApp
*   [Run work on a schedule](https://nod.n8n.io/docs/use/schedules/)

Stay in control

*   [Why you can trust Nod](https://nod.n8n.io/docs/trust/principles/)
*   [When Nod asks before acting](https://nod.n8n.io/docs/trust/approvals/)
*   [How Nod compares](https://nod.n8n.io/docs/trust/compare/)

Understand Nod

*   [What is Nod](https://nod.n8n.io/docs/get-started/what-is-nod/)
*   [Key concepts](https://nod.n8n.io/docs/get-started/glossary/)
*   [How Nod works](https://nod.n8n.io/docs/how-it-works/architecture/)

## Nod in one picture

[Section titled “Nod in one picture”](https://nod.n8n.io/docs/#nod-in-one-picture)

You talk to one Nod. It plans the work, then uses its own computer, the web and the apps you connect. Trust checks what it does. Vault keeps your secrets out of the model.

## What Nod can do

[Section titled “What Nod can do”](https://nod.n8n.io/docs/#what-nod-can-do)

Research

Search the web, read pages and PDFs, and compare sources.

Work on files

Write documents, sheets and code in its own Linux workspace.

Use your apps

Read and draft in Gmail, Calendar, Slack, Notion, Linear and more.

Browse and sign in

Fill forms, sign in with saved logins and download what you need.

Keep watch

Run on a schedule and, when you ask, notice new email that needs you.

Reply anywhere

Pick up the same conversation on Telegram or WhatsApp.

## Explore the docs

[Section titled “Explore the docs”](https://nod.n8n.io/docs/#explore-the-docs)

[Use Nod](https://nod.n8n.io/docs/use/chat/)Chat, tasks, schedules, files, the browser and memory.

[Trust and Vault](https://nod.n8n.io/docs/trust/)Approvals, saved logins, payments and your data.

[Connect](https://nod.n8n.io/docs/connect/models/)Models, Composio apps, MCP servers, APIs and CLIs.

[How Nod works](https://nod.n8n.io/docs/how-it-works/architecture/)Threads, turns, the sandbox and memory.

[Deploy and operate](https://nod.n8n.io/docs/deploy/configuration/)Settings, the desktop app and analytics.

[Contribute](https://nod.n8n.io/docs/contribute/)Set up development, run checks and write docs.

This website uses cookies

We use cookies to personalise content, ads and to analyse our traffic. We also share information about your use of our site with our advertising and analytics partners who may combine it with other information that you’ve provided to them or that they’ve collected from your use of their services.

[Read more](https://n8n.io/legal/#privacy)

Essential

- [x] 

 

Functional

- [x] 

 

Marketing

- [x] 

 

Accept all Decline all Show details



## What is Nod — https://nod.n8n.io/docs/get-started/what-is-nod/
Title: What is Nod

URL Source: https://nod.n8n.io/docs/get-started/what-is-nod/

Markdown Content:
Nod is a personal assistant you talk to in one chat. It has its own Linux workspace and browser, so it can do real work for you, not only answer questions.

Early preview Expect rough edges and breaking changes.

![Image 1: Nod chat comparing three suppliers in a table, then drafting a reply that it hasn't sent.](https://nod.n8n.io/docs/_astro/chat-light.D9FxgDyO_ZTeYje.webp)

## How Nod fits together

[Section titled “How Nod fits together”](https://nod.n8n.io/docs/get-started/what-is-nod/#how-nod-fits-together)

You have one ongoing conversation with Nod. The app, your web browser, Telegram and WhatsApp all show the same conversation, so you can start a task on your laptop and check on it from your phone.

*   **Its own computer.** Nod runs commands and keeps files in a private Linux workspace. It browses the web in its own browser, which you can take over when a site needs you.
*   **Your apps.** Connect Gmail, Calendar, Slack, Notion, Linear and others, and Nod can read and act in them.
*   **Work that runs on its own.** Nod can run tasks on a schedule. When you ask, it also notices new email and app activity that needs you.
*   **Your hosting, your model.** Nod runs on your computer or a [server you host](https://nod.n8n.io/docs/deploy/self-host/). Its model requests go to the [provider you choose](https://nod.n8n.io/docs/connect/models/) or an [OpenAI-compatible model server](https://nod.n8n.io/docs/connect/local-models/) such as Ollama that you run yourself.

| Area | Try asking |
| --- | --- |
| Research | "Compare three project tools for a team of five. Put the prices in a table." |
| Files | "Turn the attached CSV into a chart and a one-page PDF summary." |
| Email and apps | "Find client emails from this week that still need a reply and draft answers." |
| Websites | "Download last month's invoice from billing.example.com with my saved login." |
| Schedules | "Every Friday at 5 pm, send me a recap of what we finished this week." |
| On the go | Message Nod on Telegram: "Did the supplier reply yet?" |

Nod is designed to check with you before it sends, posts or deletes anything you didn't ask for. The Nod server runs that check before every such action, but an AI model makes the call, so it can be wrong. Background work that Nod starts on its own only reads and drafts, unless you've told it what to do on its own. See [Trust and Vault](https://nod.n8n.io/docs/trust/) for how that works.

|  | Local desktop assistant | Local source install | Self-hosted server |
| --- | --- | --- | --- |
| Best for | Using Nod on your own computer | Running from source, or changing Nod's code | Reaching one assistant from several devices |
| Runs on | Mac (Apple silicon or Intel), Windows 11, Linux x64 preview | macOS or Linux with Docker | A machine with Docker Compose |
| You need | Mac: macOS 14 or later. Windows local: WSL 2 and virtualization. Linux: Flatpak and a secret store; KVM for local use. | Node.js, pnpm, Docker and Git | [Server setup](https://nod.n8n.io/docs/deploy/self-host/) and HTTPS for network access |
| Updates | Automatic on Mac and Windows; install the next bundle on Linux | `git pull` and restart | [Update the server](https://nod.n8n.io/docs/deploy/server-operations/) |

The desktop app can also connect to a server. Its chat, files, model connections and connected apps then come from that server. Closing the client doesn't stop the assistant.

Each assistant needs a [model connection](https://nod.n8n.io/docs/connect/models/): a supported service's credentials, a ChatGPT plan that supports sign-in, or a model server. [Connect apps](https://nod.n8n.io/docs/connect/apps/) by signing in to each app and reviewing its permissions.

*   **It doesn't run models itself.** It connects to a model provider, which bills you for use, or to a [local model](https://nod.n8n.io/docs/connect/local-models/) server you run.
*   **It needs a running host.** A local assistant runs only while Nod is open and your computer is awake. A server keeps working while its clients are closed.
*   **It belongs to one person.** Several devices can reach the same server and assistant. Separate installations don't sync their data.
*   **Network access needs setup.** Local source installs listen on loopback by default. A [self-hosted server](https://nod.n8n.io/docs/deploy/self-host/) uses an access token and HTTPS.
*   **It isn't finished.** Nod is an early preview, so features and data formats can change.

*   [Your first conversation](https://nod.n8n.io/docs/get-started/first-conversation/)
*   [Connect a model](https://nod.n8n.io/docs/connect/models/)
*   [How Nod works](https://nod.n8n.io/docs/how-it-works/architecture/)



## Install the desktop app — https://nod.n8n.io/docs/get-started/install-desktop/
Title: Install the desktop app

URL Source: https://nod.n8n.io/docs/get-started/install-desktop/

Markdown Content:
The desktop app is the quickest way to run Nod. You don't need Node.js, Docker or developer tools.

Already have a [Nod server](https://nod.n8n.io/docs/deploy/self-host/)? Choose **Connect to a server** on first launch. After setup, choose **Replay onboarding…** in the Nod menu (on Windows, from the tray icon), then **Connect to a server**. Enter its address and access token to use that assistant.

For a local assistant, have a [supported model service](https://nod.n8n.io/docs/connect/models/) ready with its required credentials, a ChatGPT plan that supports sign-in, or a [local model](https://nod.n8n.io/docs/connect/local-models/) server such as Ollama. Paid providers bill you for use. A local model costs nothing per request. A remote assistant uses the models configured on its server.

*   [Mac](https://nod.n8n.io/docs/get-started/install-desktop/#tab-panel-0-0)
*   [Windows](https://nod.n8n.io/docs/get-started/install-desktop/#tab-panel-0-1)

You need macOS 14 or later, on Apple silicon or Intel. For a local assistant, the app and its runtime are about 1.8 GB to download.

1.   In **Apple menu → About This Mac**, check whether your Mac has a **Chip** (Apple silicon) or **Processor** (Intel). Download the latest [Apple silicon DMG](https://github.com/n8n-io/nod/releases/latest/download/nod-arm64.dmg) or [Intel DMG](https://github.com/n8n-io/nod/releases/latest/download/nod-x64.dmg) from GitHub.

2.   Open the DMG, drag **Nod** to **Applications** and open it from there.

3.   The first time, macOS asks whether to open an app downloaded from the internet. Select **Open**.

4.   At Welcome, choose **Connect to a server** to use an existing assistant, or **Get started** to start a local one. Local setup offers an optional email connection, a few optional questions about you, a model if none works yet, a choice about conversation traces, which also says basic usage data is shared by default for new owners and can be turned off in **Settings → Privacy & data**, and an optional email address for updates about Nod and other n8n products, with its own consent checkbox. Discord and forum links are also in **Settings → General**. Other apps can be connected later from the first chat or **Apps**. Nod tries to turn on **Open at login** when local setup finishes. If the operating system blocks this setting, setup still finishes. After the first chat introduction, choose **Enable notifications** if you want Nod to alert you while you’re away. macOS may ask for permission. If macOS asks for your keychain password, approve it so Nod can protect your saved keys.

5.   For local setup, Nod downloads its runtime to this computer and shows progress. Keep your internet connection on. When setup is ready, Nod opens your chat with your saved connections. See [Your first conversation](https://nod.n8n.io/docs/get-started/first-conversation/).

Install from Terminal instead
You can install the latest release on Apple silicon or Intel with one command. Quit Nod first, then paste this into Terminal:

`(  installer="$(mktemp)" || exit  trap 'rm -f "$installer"' EXIT  curl -q --proto '=https' --tlsv1.2 -fsSL https://raw.githubusercontent.com/n8n-io/nod/main/deployment/n8n/install.sh -o "$installer" && /bin/sh "$installer")`

Run it as your normal user, without `sudo`. It finds the latest published GitHub release, verifies the downloaded app, installs it to `/Applications/Nod.app`, and opens Nod. An existing installation keeps its current path. Your existing data stays in place. You don't need a GitHub account.

Before it replaces Nod, the installer stops any old ShipIt update job and removes its cache. If it cannot stop the job, it keeps your app. If the new app cannot open, it keeps the previous copy and shows its location.

The Linux x64 app is a Flatpak preview. It needs a 64-bit Intel or AMD computer, Flatpak, and a desktop secret store. A local assistant also needs hardware virtualization and access to `/dev/kvm`. GNOME Keyring and KWallet are supported secret stores. Nod refuses to save keys without secure storage.

1.   Install Flatpak with your Linux distribution's package manager. Add Flathub for the desktop runtime:

`flatpak remote-add --user --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo` 
2.   Open [Nod releases](https://github.com/n8n-io/nod/releases). Select a release with Linux files. Download **every**`nod-linux-x64.flatpak.partNN` file and `SHA256SUMS-linux-x64` from that release into one empty folder. GitHub limits each release file to 2 GiB, so Nod divides the bundle into numbered parts.

3.   In that folder, join the parts, check their contents, and install the bundle. The install command runs only if every checksum passes:

`cat nod-linux-x64.flatpak.part[0-9][0-9] > nod-linux-x64.flatpak &&  sha256sum --check SHA256SUMS-linux-x64 &&  flatpak install --user ./nod-linux-x64.flatpak` 
4.   Open **Nod** from your application menu, or run `flatpak run io.n8n.Nod`. Choose **Get started** for a local assistant or **Connect to a server** for an existing one. The bundle includes Nod's private computer runtime. Flatpak can also download its desktop runtime during installation.

5.   Keep your secret store unlocked during setup. After setup, choose **Enable notifications** if you want alerts. **Open at login** uses your desktop's autostart folder. See [Your first conversation](https://nod.n8n.io/docs/get-started/first-conversation/).

Linux ARM builds are not published. Developers can [build the Flatpak from source](https://nod.n8n.io/docs/contribute/desktop-releases/#build-a-linux-flatpak).

For a local assistant, closing the window keeps Nod running in the menu bar on a Mac, or the tray on Windows and Linux. Linux tray support depends on your desktop. **Quit Nod** stops Nod and its private computer. On Windows, running the installer or uninstaller while Nod is open offers to quit it first.

| Nod is | What runs |
| --- | --- |
| Open, or closed to the menu bar or tray | Chat, channels, schedules and background checks |
| Quit, or your computer is asleep | Nothing, until Nod is open and awake again |
| Your computer restarted or lost power | Nothing, until you sign in and Nod opens |

Nod tries to turn on **Open at login** when setup finishes. If the operating system blocks this setting, setup still finishes. If you rely on scheduled tasks, keep it on in **Settings → General**.

When connected to a server, the server keeps your assistant, channels and schedules running after you quit the app or put your computer to sleep. The server must stay running and connected.

## Change the app font size

[Section titled “Change the app font size”](https://nod.n8n.io/docs/get-started/install-desktop/#change-the-app-font-size)

Open **Settings → General → Appearance** and use the **Font size** controls to make the desktop app smaller or larger. Use the reset button to return to 100%.

These controls change the same app zoom as **View → Zoom Out** and **View → Zoom In**. You can also use `Cmd-` and `Cmd+` on a Mac, or `Ctrl-` and `Ctrl+` on Windows and Linux.

On Linux, quit Nod, then download, check, and install the next bundle with the [Linux procedure](https://nod.n8n.io/docs/get-started/install-desktop/#linux). Your profile and private computer stay in place. These bundles have no update repository. `flatpak update` can update shared desktop runtimes, but it does not fetch a new Nod bundle. Nod's own update checks are off on Linux. The rest of this section applies to Mac and Windows.

Nod checks for updates after it starts, every six hours while it's open, and after your computer wakes if a check is due. Checks continue when an update is already downloaded, so a newer release can replace it before you restart.

To check now, select **Check for Updates…** in the **Nod** menu on a Mac, or from the menu bar or tray icon. This stays available alongside **Restart to update** when an update is ready. While a check or download runs, its menu item shows progress and restart waits until it finishes.

Newer Nod builds show an in-app notice when an update finishes downloading. It names the new version and offers **Restart to update** or **Later**. Select **Release notes** in the notice to open that version's GitHub release page in your browser. **Later** hides the notice for that version during the current app session; **Restart to update** stays in the menu. Older builds may show only the menu action, so use **Check for Updates…** there to check immediately. If Nod is in the middle of a task, it asks before restarting, and you can ask it to continue afterwards. While it shuts down to install, Nod shows **Updating Nod…**, then opens again where you left it, with any unsent message still in the box. Nod keeps your profile, keys and data. A completed installation does not repeat onboarding after an update.

On Windows, the restart runs the new installer in the background and opens Nod again when it's done.

Updating a connected desktop client does not update its server. Follow [Server operations](https://nod.n8n.io/docs/deploy/server-operations/) to update the server separately.

## Where your data lives

[Section titled “Where your data lives”](https://nod.n8n.io/docs/get-started/install-desktop/#where-your-data-lives)

For a local assistant, Nod's database, workspace and browser stay on your computer. When connected to a server, the server stores them along with model credentials and the Composio identity. Every client using the same server reaches the same assistant and connected accounts. Your device keeps its server address, encrypted access token, preferences and client data, such as unsent drafts and downloaded files.

Requests go to the model provider and apps you choose. Managed app requests and results pass through the configured connection service and Composio; n8n hosts the default service. Usage analytics are on by default for a new owner. Turning off **Share usage data** in **Settings → Privacy & data** stops new sends, though a submission already in flight may still complete. If you enter an email address and agree to updates about Nod and other n8n products, Nod links it to this installation's usage in PostHog and sends an unverified signup request to n8n's Customer.io Labs workspace only if **Share usage data** is on when you submit. Fixed About you choices accompany it only if you shared them successfully. Nod records the request on a new or existing profile and sends no email. Conversation traces leave only if you turn on **Share conversation traces** in **Settings → Privacy & data**. See [Your data and privacy](https://nod.n8n.io/docs/trust/privacy/).

Nod starts with a fresh profile and doesn't import data from a source install.

|  | Mac | Windows |
| --- | --- | --- |
| App data and settings | `~/Library/Application Support/nod/profiles/local` | `%APPDATA%\nod\profiles\local` |
| Private computer | `~/.nod-desktop/<profile id>` | A WSL distribution named `nod-<profile id>` |
| Saved keys | Encrypted with the macOS key store | Encrypted with Windows DPAPI |

On Linux, app data and settings are in `~/.var/app/io.n8n.Nod/config/nod/profiles/local`. The private computer is in `~/.nod-desktop/<profile id>`. Your desktop's Secret Service protects saved keys. The Flatpak contains Nod's runtime pack.

Moving Nod to the Trash or uninstalling it keeps your data, so a later install opens where you left off. Uninstalling a connected client does not delete server data. To return to a local assistant first, choose **Replay onboarding… → Change server → Use this computer**, then:

1.   Select **Remove all data** in **Settings → Privacy & data**. If Nod can't finish setup, select **Remove all data…** in the **Nod** menu instead.
2.   Review the warning, then confirm. It lists what Nod will delete and explains that you must complete setup again. Nod deletes your profile and private computer, then restarts and opens setup. The app stays installed.
3.   To remove the app too, quit Nod. Move it to the Trash on a Mac, uninstall it in **Settings → Apps** on Windows, or run `flatpak uninstall --delete-data io.n8n.Nod` on Linux.

On Linux, uninstalling the Flatpak alone leaves the private computer in `~/.nod-desktop`. Use **Remove all data** first to delete it safely.

On a Mac, Nod keeps the runtime it downloaded, so a new install doesn't download it again, and its entry in the key store. Neither holds your data. Apps you connected may still list Nod until you remove it there.

If you deleted Nod's folders by hand, Nod removes the private computer they leave behind the next time it opens.

| Problem | Try this |
| --- | --- |
| macOS blocks the first launch | Install the newest release. On a managed Mac, ask your IT team to allow Nod. |
| Setup stops with an error | Select **Try again**. If it fails again, send the error with **Send feedback…** from the menu bar or tray icon. |
| Nod asks for a runtime file | Select **Choose runtime file** and pick the `nod-Runtime-…` file from the same release. |
| Windows can't download the runtime | Put `nod-Runtime-win32-x64.tar.gz` from the same release next to `nod-Setup-x64.exe` and run the installer again. |
| Windows downloads the same update again after a restart | Nod 0.6.2 and earlier can't install updates on Windows. Quit Nod from the tray icon, then download and run the [newest Windows installer](https://github.com/n8n-io/nod/releases/latest/download/nod-Setup-x64.exe) once. Your data stays in place. |
| A scheduled task didn't run | Check that the machine running your assistant was awake and Nod was running. For a remote assistant, check the server. |

### A failed Mac update blocks a new install

[Section titled “A failed Mac update blocks a new install”](https://nod.n8n.io/docs/get-started/install-desktop/#a-failed-mac-update-blocks-a-new-install)

After a failed update, the ShipIt update job can stay loaded. A new copy of Nod can then fail to open. If macOS shows **“Nod” is damaged and can't be opened** after an update failed, remove the old update job before you install Nod again.

1.   Quit Nod. If it stays open, use **Activity Monitor** to stop it.

2.   Open **Terminal** and run these commands as your normal user:

`launchctl bootout "gui/$(id -u)/dev.nod.desktop.ShipIt"rm -rf "$HOME/Library/Caches/dev.nod.desktop.ShipIt"` 
If no ShipIt job is loaded, the first command can report an error. Continue with the second command.

3.   Download the newest DMG from the [releases page](https://github.com/n8n-io/nod/releases). Replace the copy in **Applications**, then open it.

These commands remove only the update job and its cache. They keep your profile, conversations, saved keys and private computer. If Nod still does not open, [send feedback](https://nod.n8n.io/docs/deploy/troubleshooting/#send-feedback-with-a-diagnostic-report).

*   [What is Nod](https://nod.n8n.io/docs/get-started/what-is-nod/)
*   [Your first conversation](https://nod.n8n.io/docs/get-started/first-conversation/)
*   [Install from source](https://nod.n8n.io/docs/get-started/install-from-source/)
*   [The desktop app in depth](https://nod.n8n.io/docs/deploy/desktop-app/)
*   [Troubleshooting](https://nod.n8n.io/docs/deploy/troubleshooting/)



## Your first conversation — https://nod.n8n.io/docs/get-started/first-conversation/
Title: Your first conversation

URL Source: https://nod.n8n.io/docs/get-started/first-conversation/

Markdown Content:
This page walks you through Nod's onboarding, your first tasks and what to do when Nod needs you.

## Onboarding at a glance

[Section titled “Onboarding at a glance”](https://nod.n8n.io/docs/get-started/first-conversation/#onboarding-at-a-glance)

Nod opens onboarding the first time you set up an assistant. After the welcome screen, Nod starts preparing its private computer in the background while you optionally connect email, tell it a bit about yourself, choose an AI provider if none is set up yet, decide whether to share conversation traces, and optionally leave an email address for updates. If you connected email, Nod reads a small sample of it in the meantime to suggest first ideas in chat.

For a local desktop assistant, you connect accounts while Nod prepares its computer. When you connect to a server, setup and saved connections belong to that server. A server that already completed onboarding opens your existing chat.

## Go through onboarding

[Section titled “Go through onboarding”](https://nod.n8n.io/docs/get-started/first-conversation/#go-through-onboarding)

1.   **Choose your assistant.** The welcome screen shows what sets Nod apart, including that Nod checks your connected apps in the background with your model, so those checks count as model usage. When **Share usage data** is on, it also asks you to keep usage data on; select **How Nod uses your data** to see what it includes. Select **Get started**. In the desktop app, select **Connect to a server** instead to use an existing assistant. The desktop app starts preparing its private computer as soon as the welcome screen opens, and the web app as soon as you continue. If the desktop app isn't ready to save your choices yet, it shows a loading screen with the current setup stage. Onboarding opens as soon as it can save them, while the workspace and browser continue preparing in the background.

2.   **Connect email (optional).** Select **Connect via Composio** next to **Gmail** or **Outlook**, then sign in and review the permissions, or select **Continue without email** to move to the next setup step. You can connect email later from **Apps**. Google or Microsoft asks you to allow [Composio](https://nod.n8n.io/docs/connect/apps/), the service Nod uses to connect apps, as the note under the buttons says. Setup continues after the connection is confirmed. Once you've also answered or skipped the About you questions, Nod starts reading a small sample of recent email in the background to learn what you work on and suggest first ideas. From that sample it keeps only the names of apps that send you notifications, never the email itself. Failed sign-in does not erase your earlier progress. If you go **Back**, **Manage** opens the same account manager as Apps.

3.   **Tell Nod about yourself (optional).** Nod asks where you'd like its help, what you do, how big your company is, and what you'd like to take off your plate. You can choose more than one role and more than one task, or choose **Something else** to type your own. Outside **Mostly personal life**, if you run a business, freelance, or work at an agency, Nod also asks whether the help is for you, your clients, or both. **Mostly personal life** still asks what you do but skips that question and the company-size question. **Not now** skips a question, and the pen next to an answer lets you change it. If memory is on, Nod saves your answers as one note in [Memory](https://nod.n8n.io/docs/use/memory/) and uses them for your first ideas in chat. Anything you type that looks like a password, key, or card number is left out. When **Share usage data** is on, Nod says before the first question that your answers reach the Nod team as usage data. It saves the fixed choices on the analytics ID's profile and never includes what you type in **Something else**; see [Analytics](https://nod.n8n.io/docs/deploy/analytics/). If Nod cannot confirm analytics received the choices, select **Continue without retrying** to move on, or **Retry sharing** to try again. The first attempt may already have reached analytics.

4.   **Connect a model (only if none is set up).** Choose a provider, or select **More providers** to search all supported services. The **OpenAI** row notes that you can sign in with a ChatGPT Plus or Pro plan at no extra cost. See [Connect a model](https://nod.n8n.io/docs/connect/models/) for required credentials and cloud settings. Nod skips this step when a model connection already works, including one configured through server environment variables.

To use an [OpenAI-compatible model server](https://nod.n8n.io/docs/connect/local-models/), choose **Your own server** and enter an address reachable from Nod's server. Choose a model if prompted, then select **Continue**.

While setting up a provider, **Back** returns to the provider list. From that list, **Back** returns to About you.

5.   **Help improve Nod.** Nod asks whether you'll share conversation traces, and says that it shares basic usage data, which is on by default. Select **Share traces** or **Not now**; either one saves your choice and continues, and traces stay off unless you share them. To see what each one includes and what's never shared, select **How Nod uses your data**. You can change both later in **Settings → Privacy & data**; see [What Nod shares with n8n](https://nod.n8n.io/docs/trust/privacy/#what-nod-shares-with-n8n). Traces appear only where they're available.

6.   **Email updates (optional).** Where the email option is available, enter an address and tick the consent box if you want n8n GmbH to email you about Nod and other n8n products. The box also says that n8n links your email to your Nod usage data. A line below it explains how to unsubscribe and unlink your email. **Start chatting**, or **Continue** in the desktop app, submits the address and finishes setup. Leave the address blank to finish without submitting it. If submission fails, choose **Try again** or **Continue to chat** without retrying. While **Share usage data** is on, Nod stores the submitted address and consent record on a PostHog person profile linked to this installation's usage. It also sends them to n8n's Customer.io Labs workspace, with fixed About you choices only if you shared those successfully. Submitting the form creates or updates an unverified Customer.io profile and sends no email. A submission already in flight may finish after **Share usage data** is turned off. Updates require a later email confirmation flow. To stop future emails, use the unsubscribe link in each email. To unlink your email from your usage data, write to [privacy@n8n.io](mailto:privacy@n8n.io). Discord and the n8n Labs forum are secondary links here and are also in **Settings → General**.

Setup finishes after the last step in the web app or a desktop client connected to a server. For a local assistant, Nod also turns on **Open at login** so it's ready when you sign in to your computer. You can turn it off in **Settings → General**. If its computer is still preparing, Nod shows a loading screen and opens chat when ready. Finishing setup always opens chat, even while first ideas are still being prepared. A startup failure offers **Try again** without clearing your connections. If setup needs a model connection, Nod sends you back to that step.

You can add more later from **Apps** and **Channels** in the sidebar. See [Connect apps](https://nod.n8n.io/docs/connect/apps/) and [Channels](https://nod.n8n.io/docs/use/channels/).

To revisit setup in your browser, open `/onboarding?replay=1` on your Nod address. This returns to Welcome while keeping saved connections and settings.

In the desktop app, **Replay onboarding** opens setup again without deleting saved connections or preferences. While first setup is still running, it returns to your current step. Finishing setup opens chat rather than following links received during setup, including the Apps return link from sign-in. For a separate empty test install on a Mac, use the [Mac test installer](https://nod.n8n.io/docs/contribute/desktop-releases/#test-a-local-mac-build); it creates a new isolated profile.

## Start your first task

[Section titled “Start your first task”](https://nod.n8n.io/docs/get-started/first-conversation/#start-your-first-task)

Nod opens the conversation with a short hello. Ask for a task directly, choose an idea, or say hello in your language. There is no required interview. What you share follows the normal chat memory settings.

When you greet Nod, test the chat, or ask what it can do, it offers one small task you can start now. It uses your stated goals, current work, and available tools. It explains the result and why it helps, then asks one easy question. When it needs no more information, reply choices let you start or get another idea. For example, it can check recent email and return links to messages that need your reply. A clear yes to that offer starts the work. Nod checks the result and delivers it before it offers recurring work, unless you asked for a schedule.

If you upload a file without text, Nod uses the instructions you already gave. It asks one specific question when your intent is unclear. Say **continue** to resume unfinished work. Nod checks the context or history before it asks which task you mean.

After the first chat introduction, choose **Enable notifications** to hear from Nod while you’re away, or **Not now** to dismiss the offer. Nod does not enable notifications just because you open chat. In the web app, your browser asks for permission after you select Enable. Your browser and system settings control delivery. You can change the choice in **Settings → Notifications**. Enabling alerts does not authorize app monitoring or scheduled work.

Nod then shows idea cards. The first three are one to do once and two that repeat. When your connected tools, such as email, have useful recent activity, they're based on a small sample of it; otherwise they're general suggestions. Nod's message above them says where it looked. The cards after them add common ideas, such as a morning brief on your day or a Friday recap. A picked idea might be an upcoming meeting to prepare for, a conversation waiting on you, or a recurring report. Meeting suggestions use the current time and, when known, your time zone to avoid preparation for events that have already started, ended, or been cancelled. It uses only available read operations and respects your rules. Preparing suggestions never sends messages, changes your accounts, or starts ongoing work.

If a tool can't be read or has nothing useful to surface, Nod suggests work without claiming it found something. You can ignore the cards and type any request.

Under the cards, Nod says you can ask it for more ideas. If you get notification email from apps you haven't connected, such as Slack, GitHub or Linear, it names up to three of them. Connecting those apps helps it find more. You can ask for ideas without connecting another app. Nod uses your stated goals, work already in the conversation, or a small recent sample from a relevant connected app. It recommends a task and names the result you would get. You can also ask for more choices or a detailed overview.

New connections are optional. If an app is empty or cannot be read, Nod says what it could not check and suggests work with text, files or public sources instead. It names any input it needs. Asking for ideas does not start a task, save drafts, create a schedule or connect an app. Choose a specific offer to start it. Nod then does the work and delivers the result through the normal approval and private sign-in checks.

The whole card is the button. A card that works in one of your tools shows that tool's logo under its title, and a card that repeats shows **Repeats**. Select a card to send its title to Nod as your message. The card shows **On it…** while its turn or saved task works. It shows **Waiting for you** when that work needs your attention. **Waiting** means a saved task waits for someone or something else. **Done** or **Set up** means its saved tasks are complete. **Request sent** means the chat turn ended without a saved task. Read the delivered result to check what Nod completed.

Nod keeps the saved tasks started from these cards available with recent tasks, so a card can still show completion when you return to the first conversation later.

You can get useful work without connected apps. For example, paste three supplier quotes and ask Nod to compare their prices and delivery times. Include your deadline and ask for a recommendation. Check the delivered comparison in chat. A starting card or an acknowledgement is not the result.

Use **Send feedback** in chat when you want to report a problem or suggest a change. New setup does not open a feedback hint over your first result.

## Write a good first request

[Section titled “Write a good first request”](https://nod.n8n.io/docs/get-started/first-conversation/#write-a-good-first-request)

*   **Say what done looks like:** "Compare these three suppliers and put the price and delivery time in a table."
*   **Name the account or site:** "Download last month's invoice from billing.example.com with my saved login."
*   **Say whether to send or draft:** "Draft a reply to the Northstar quote. Don't send it."
*   **Ask for a schedule in plain words:** "Every Monday at 9 am, send me a summary of new client email."

You can keep writing while Nod works. Nod reads new messages before its next step.

## When Nod needs you

[Section titled “When Nod needs you”](https://nod.n8n.io/docs/get-started/first-conversation/#when-nod-needs-you)

| Nod needs | What you see | What you do |
| --- | --- | --- |
| A choice or a missing detail | A question in the chat | Reply in the chat |
| Your OK for an action | "Reply yes to go ahead, no to skip it, or tell me what to change." | Reply **yes** or **no** |
| A password, code or card | A private form, such as **Sign in** or **Approve payment** | Enter it in the form, not the chat |
| You to use a website | A live browser view in chat | Take over, then select **Return to Nod** |

What you type in a private form goes to the website, not to the model. Nod never asks for a password, code, card number or API key in the chat. See [Approvals and the trust check](https://nod.n8n.io/docs/trust/approvals/) and [Vault](https://nod.n8n.io/docs/trust/vault/).

To stop Nod, select **Stop**, the square button next to the send button. It shows while Nod is working. Nod stops the current work and cancels anything still queued. Stopping can't undo an action that already started, such as an email that's already on its way.

*   [What is Nod](https://nod.n8n.io/docs/get-started/what-is-nod/)
*   [Key concepts](https://nod.n8n.io/docs/get-started/glossary/)
*   [Chat with Nod](https://nod.n8n.io/docs/use/chat/)
*   [Connect a model](https://nod.n8n.io/docs/connect/models/)
*   [Trust and Vault](https://nod.n8n.io/docs/trust/)



## Architecture — https://nod.n8n.io/docs/how-it-works/architecture/
Title: Architecture

URL Source: https://nod.n8n.io/docs/how-it-works/architecture/

Markdown Content:
This page shows how Nod's parts fit together and where each one lives in the code. Start here before you change Nod or evaluate how it works.

The short version: Nod is one Node process plus Docker containers on the computer running your assistant. That can be your desktop's private runtime or a self-hosted server reached by web and desktop clients.

## One conversation, independent tasks

[Section titled “One conversation, independent tasks”](https://nod.n8n.io/docs/how-it-works/architecture/#one-conversation-independent-tasks)

The main chat session coordinates work. It answers short requests and starts a saved session for each independent task. Task questions, progress and results return to the same conversation. Task results do not need a second model call in the coordinator.

The `tasks` table is the task ledger. All sessions share the owner's workspace and memory, with separate saved histories and task folders. The server routes replies and delivers addressed owner updates to the correct session.

See [Task sessions](https://nod.n8n.io/docs/how-it-works/task-sessions/) for the architecture diagram, records, context sharing and lifecycle.

## One process and a few containers

[Section titled “One process and a few containers”](https://nod.n8n.io/docs/how-it-works/architecture/#one-process-and-a-few-containers)

One Node process serves the React client and runs the Fastify API, the agent runtime, the thread-drain worker and the schedulers. Docker containers run PostgreSQL, the workspace and the browser. While you pick a login from 1Password, a separate helper process talks to the 1Password app, so the server never loads 1Password's code.

Messages and schedule fires become turns in PostgreSQL with a `thread-drain` job. App events and source checks feed one observer through a saved source queue. The worker picks up the job and asks the runtime to run a turn. The runtime opens a Pi agent session, and Pi calls tools that act in the workspace, the browser and your connected apps.

One thread per owner

One conversation shared by web, Telegram and WhatsApp. Its ID keys the workspace and chat session. Background sessions have their own browsers and saved Pi transcripts.

Everything is a turn

Messages, schedule fires, event wakes and resumes each run as a turn. Turns are never retried.

Policy lives on the server

The server checks app actions, Vault use and payments. The model's instructions sit on top of those checks, not in place of them.

A sandboxed computer

Commands run in a locked-down container. Provider keys never enter it or the browser.

One observer reads connected apps and saves private work. It starts separate tasks for outside actions, questions, and approvals. Those tasks use normal tools and Trust. See [Proactivity engine](https://nod.n8n.io/docs/how-it-works/proactivity/). Ordinary tasks and schedules keep their normal tools.

Guides tell Pi to list the full requested scope and time range before keyword filters in a broad review. A narrow search cannot establish full coverage.

Structured results from apps, connected MCP tools, `read_source` and `proactive_issue` can include timestamps with UTC or numeric offsets. Before Pi reads a result, the runtime adds up to 32 local time equivalents in the owner's time zone. The source values stay unchanged. Posted local hours keep their original zone unless the owner asks for a conversion. Converted times name their zone. Nested script calls keep raw data; their JSON output can receive the same display annotation. Date-only values, times without an offset and direct browser observations are not converted. Personal tools such as `prepared_list` do not get this annotation. The annotation stays inside the same untrusted data block.

For calendar plans, Pi uses availability tools when available and code for durations, gaps and proposed moves. Time ranges that only share an endpoint do not overlap. Required travel or preparation buffers are checked separately. Each proposed alternative is checked against the relevant calendar window.

## Where the code lives

[Section titled “Where the code lives”](https://nod.n8n.io/docs/how-it-works/architecture/#where-the-code-lives)

*   
Directory src/ 
    *   
Directory ports/
        *   …

    *   
Directory providers/
        *   …

    *   
Directory runtime/
        *   …

    *   
Directory server/
        *   composition.ts

    *   
Directory shared/
        *   …

    *   
Directory web/
        *   …

*   
Directory scripts/ 
    *   check-architecture.mjs

[`scripts/check-architecture.mjs`](https://github.com/n8n-io/nod/blob/main/scripts/check-architecture.mjs) runs as part of `pnpm run check`. It fails when an import crosses a boundary:

| Folder | Can import from |
| --- | --- |
| `web` | `web`, `shared` |
| `shared` | `shared` |
| `ports` | `ports`, `shared` |
| `runtime` | `runtime`, `ports`, `shared` |
| `providers` | `providers`, `ports`, `shared` |
| `server` | `server`, `ports`, `shared`. Only `composition.ts` also imports `runtime` and `providers`. |

The same check keeps vendor packages (Pi, Composio, chat adapters and agent-browser) inside `providers`. It also stops `runtime`, `ports`, `shared` and `web` from reading `process.env`. Configuration belongs in [`src/server/composition.ts`](https://github.com/n8n-io/nod/blob/main/src/server/composition.ts).

*   [Threads and turns](https://nod.n8n.io/docs/how-it-works/threads-and-turns/): how messages, schedules and events become turns, and how they share one thread.
*   [The agent runtime](https://nod.n8n.io/docs/how-it-works/agent-runtime/): Pi sessions, tools, codemode, the turn guard and the system prompt.
*   [Sandbox and browser isolation](https://nod.n8n.io/docs/how-it-works/sandbox-and-browser/): what the workspace and browser containers can and can't reach.
*   [Memory](https://nod.n8n.io/docs/how-it-works/memory/): how Nod learns and keeps what it knows about you.
*   [Skills](https://nod.n8n.io/docs/how-it-works/skills/): the trusted task guides Nod reads before it works.



## Models — https://nod.n8n.io/docs/connect/models/
Title: Models

URL Source: https://nod.n8n.io/docs/connect/models/

Markdown Content:
Nod needs a model connection to think and reply. Connect one or more services in **Settings > Models**, then choose the model Nod uses.

Your requests go to the service you connect. Paid providers bill you for use. To run a model on your own computer instead, see [Local models](https://nod.n8n.io/docs/connect/local-models/).

## Supported connections

[Section titled “Supported connections”](https://nod.n8n.io/docs/connect/models/#supported-connections)

Select **Add connection** (or **Add** when you already have a connection), then search for a service. Regional and token-plan entries use the key issued for that particular service.

| Connection | Setup | Initial choice |
| --- | --- | --- |
| Google Gemini | [AI Studio API key](https://aistudio.google.com/api-keys) | Gemini 3.8 Flash, medium effort |
| OpenAI / ChatGPT | API key or existing ChatGPT sign-in | GPT-6.1 Sol / GPT-6 Sol, high effort |
| Anthropic | API key | Claude Opus 5.5, high effort |
| OpenRouter | API key or browser sign-in | GPT-6.1 Sol, high effort |
| Google Vertex AI | Vertex API key | Gemini 4 Argon, medium effort |
| Amazon Bedrock | API key and Region | You choose the model and routing profile |
| Azure OpenAI | Endpoint, deployment, model, and API key | The deployment's model |
| Cloudflare Workers AI / AI Gateway | Token, account ID, and gateway ID for AI Gateway | Kimi K2.7 Code / GPT-6.1 Sol |
| Other named providers | Service-specific API key | A capable model from that connection |
| OpenAI-compatible | Server address and optional key | A model offered by the server |

Other providers include Ant Ling, Baseten, Cerebras, DeepSeek, Fireworks AI, Groq, Hugging Face, Kimi Coding China, Meta, MiniMax, Mistral, Moonshot AI, NVIDIA, OpenCode Zen and Go, Qwen Token Plan, Radius, Together AI, Vercel AI Gateway, xAI, Xiaomi MiMo and token plans, and Z.AI. The picker includes their supported regional variants.

When an account model list is available, Nod loads it. For services with only a bundled catalog, Nod saves the key and checks access on first use. Neither a catalog nor a saved key proves that your account has credit or permission to run every listed model.

You can change the initial choice. Nod preserves a working choice when you add another connection. It uses the recommended model when available, otherwise the first supported model in that connection's catalog. For Google Gemini, you must choose a model if Gemini 3.8 Flash is unavailable. When Bedrock offers several models or profiles, you must also choose because profiles can change where requests are processed.

Google does not permit third-party assistants to reuse [Gemini CLI OAuth](https://geminicli.com/docs/resources/faq/). A Gemini app subscription is not a Nod sign-in option. Anthropic's [authentication conditions](https://code.claude.com/docs/en/legal-and-compliance) also require an API connection for Claude in Nod.

## Connect a service

[Section titled “Connect a service”](https://nod.n8n.io/docs/connect/models/#connect-a-service)

Select **Settings** at the bottom of the sidebar, then **Models**. Select **Add connection** or **Add**, then choose a provider. Onboarding shows the same options before your first chat.

If a key has a recognizable format for a different provider, Nod shows the mismatch beside the key field before sending or saving it. Choose the matching provider or paste that provider's key. Unfamiliar formats still use the provider's normal connection checks; a matching format alone does not prove a key works.

In **Settings > Models**, select the model in **When you talk to Nod, it uses …** to open **Choose a model**. Search by model, provider or account, or filter by provider. Models are grouped by connection, with recommended choices first in each group. A check marks both your current model and its connection. Image, audio and thinking icons identify each model’s capabilities; hover over an icon for its label. You can use the arrow keys, Home and End to move through models, then Enter to choose one. During onboarding, **More providers** opens the full list to browse or search.

Select **Manage** beside a provider to see its accounts, add another connection or remove one. If a connection stops working, **Reconnect** restores a sign-in. For a key or server, add the details again; remove the old connection if you no longer need it. When it's the connection you selected, chat links to that screen.

Select **Reload models** beside a connected account to load its current model list and controls. If the saved effort is no longer supported, Nod uses a supported effort for the same model. This also applies when you save the connection again. Reload an existing Ollama connection after an update to use its current thinking controls.

NVIDIA reloads its hosted model list. A listed model can still require account access or an available route. A failed reload keeps the saved list and selection. If a successful reload removes your selected model, choose another model yourself.

If a model request stops your task, the failure message links to **Settings > Models**. Use that link to check the connection or choose another model. The message keeps the provider's reason, including key, credit, quota, model access, and service errors. Nod shows the provider's reason directly instead of asking the model that failed to rewrite it. When another connection is set up, the message says you can switch to it. A daily quota error asks you to check the limit or choose another model and shows the provider's retry delay when supplied. A zero quota error asks you to check access or choose another model.

Nod checks your selected model with a tiny request when you choose it, including choosing it again, and when you start Nod. While a model's last request failed, **Settings > Models** shows the provider's reason beside its connection and chat shows it above the message box, before you send anything.

After a model fails a request, automatic work stops using that model on that connection. This includes background checks, background helpers and cache warming, and recurring schedules skip their runs. A one-time schedule still runs and reports the failure. Errors Nod retries on its own, such as an overload, and a conversation too long for the model's context don't count. Nod tries automatic work again after 2 minutes, and each further failure waits longer: 6, 18, 54 and 162 minutes, then 6 hours at most. A request that succeeds clears that model's failure. When a failing model works again, the connection's other paused models try again too. Requests you start always go through, and so does work that continues after you approve, sign in, pay, hand back the browser or connect an app. The failure survives a restart, and other connections stay available.

To change to an available model, you can also tell Nod which model and service to use. This works in Nod, Telegram, and WhatsApp. Nod changes the saved selection for the next turn. Connecting a new service or signing in again still needs the private flow in the app.

*   [OpenAI](https://nod.n8n.io/docs/connect/models/#tab-panel-0-0)
*   [ChatGPT](https://nod.n8n.io/docs/connect/models/#tab-panel-0-1)
*   [Anthropic](https://nod.n8n.io/docs/connect/models/#tab-panel-0-2)
*   [OpenRouter](https://nod.n8n.io/docs/connect/models/#tab-panel-0-3)
*   [Google Gemini](https://nod.n8n.io/docs/connect/models/#tab-panel-0-4)
*   [Other services](https://nod.n8n.io/docs/connect/models/#tab-panel-0-5)
*   [Amazon Bedrock](https://nod.n8n.io/docs/connect/models/#tab-panel-0-6)
*   [Google Vertex AI](https://nod.n8n.io/docs/connect/models/#tab-panel-0-7)
*   [Azure OpenAI](https://nod.n8n.io/docs/connect/models/#tab-panel-0-8)
*   [OpenAI-compatible](https://nod.n8n.io/docs/connect/models/#tab-panel-0-9)

1.   Choose **OpenAI**, then **Use an API key**.
2.   Set **API region** to the region of your OpenAI API project. Leave **Global** for a project without a regional restriction.
3.   Paste your key into **API key**, then select **Connect**.

For a project with EU data residency, choose **Europe (EEA + Switzerland)**. Nod uses `eu.api.openai.com` for that connection's model requests, speech, and OpenAI decision checks. It keeps the native OpenAI models and their settings.

Each connection keeps its own region. Nod does not switch regions after a failed request. Regional model and feature availability depends on your OpenAI project. See [OpenAI data residency](https://developers.openai.com/api/docs/guides/your-data#data-residency-controls).

## Switch and manage connections

[Section titled “Switch and manage connections”](https://nod.n8n.io/docs/connect/models/#switch-and-manage-connections)

All the models from your connections appear in one searchable list, grouped by connection. Choosing a model also chooses the connection that pays for it.

OpenRouter models show input and output token prices beside each model name, in USD per million tokens. Prices can wrap to the next line on small screens. The list identifies free tokens and prices that vary by model. These are the rates from the last model list update. Actual charges can vary with routing, caching, context length, and extra services. See [OpenRouter's model pricing](https://openrouter.ai/docs/guides/overview/models#pricing-object).

You can connect several accounts of one service, such as two ChatGPT accounts or a personal and a work API key. A ChatGPT connection shows the account's email. A key connection, including one an OpenRouter sign-in created, shows only the last four characters of a key longer than four characters. Shorter keys stay hidden. The model never sees this display value. Signing in again with an account you already connected, or adding the same key or server address to the same service again, updates that connection instead of adding another.

If your selected connection is removed or needs reconnecting, the next connection you add or reconnect in **Models** becomes your model. If only your model disappears from a working connection, Nod keeps your choice and asks you to choose another. Nod doesn't switch by itself after a failed request.

| To | Do this |
| --- | --- |
| Switch model | Open **Settings → Models**, then pick a model for chat, schedules or work Nod starts on its own. |
| Load a missing model list | Select **Manage** beside the provider, then **Load models** or **Try again**. |
| Fix a broken connection | Open **Manage** and **Reconnect** a sign-in, or add the key or server details again. |
| Remove a connection | Open **Manage** and select **Remove connection** beside the account. If it was selected, choose a new model. |

## Models for each kind of work

[Section titled “Models for each kind of work”](https://nod.n8n.io/docs/connect/models/#models-for-each-kind-of-work)

Nod uses your model when you talk to it, in the app, Telegram and WhatsApp, and for tasks you start unless you give one its own model. Schedules, and work Nod starts on its own, such as checking your apps and the tasks it starts from them, can each use another model. In **Settings > Models**, select the model after **Schedules use** or **Work Nod starts on its own uses**:

*   **The same model** uses your model.
*   **The light model** uses the smaller model on your model's connection, such as Claude Haiku 5.5 or GPT-6 Luna, when it costs no more than your model. Without one, Nod uses your model.
*   Any connected text model.

A lighter model costs much less, but in Nod's evals it read less and flagged fewer time-sensitive things for you than your main model.

A schedule or task can have its own model too: in **Scheduled**, open it and select **Change** beside **Model**. **Settings > Models** lists the ones that differ from their default. When that work has priced usage in the last 30 days, each list shows what it cost, repriced on each model; otherwise it shows each model's token prices. Different models use different numbers of tokens for the same work, so the price is an estimate.

You can also tell Nod, for example "Run my schedules on the light model" or "Use Opus for the weekly report", in Nod, Telegram or WhatsApp. Nod replies with the cost change.

A change applies from the next turn; work that's already running keeps its model until then. Checking what Nod may do, writing the questions it asks you and reading your answers always use your model. If a model you chose for some work is no longer available, that work fails with the reason instead of switching models, and **Settings > Models** shows it as unavailable so you can choose another. Removing a connection returns the work that used it to its default: the model for its kind of work, else your model. An audio model's **Text support** label names its companion from the same connection. Requests without recordings use that companion; follow-ups that still include recordings use the audio model. Both use the smaller context and output limits of the pair. Your saved model choice stays unchanged.

If a model request fails, Nod doesn't switch to another connection on its own; the notice above the chat box offers one when you have it. Nod retries a temporary provider error up to three times, waiting 4, 8 and 16 seconds. Temporary errors include an overload, a rate limit, and, for hosted providers, a request that gets no response within 90 seconds of being sent, cache warming included. Requests to a model server you run have no such limit, because local models can take minutes to start answering.

Background work, such as memory upkeep, uses a smaller model from the same connection when it has one, such as `gpt-6-luna` or `claude-haiku-5-5`. Otherwise it uses your model or, for an audio model, its text companion. Background work and checks use the lightest reasoning their model offers: off, minimal, low or medium in that order, or the model's first effort level if it offers none of these.

## Models with a small context window

[Section titled “Models with a small context window”](https://nod.n8n.io/docs/connect/models/#models-with-a-small-context-window)

For a context window below 65,536 tokens, Nod uses short instructions and loads one detailed tool at a time. It reads guides, saved memory and older messages when needed. Large tool results stay in workspace files, with a short preview in the conversation.

Nod limits reply size and asks Pi to start history compaction earlier. Pi handles context limits from the provider and can summarize older work before continuing. Large images, tool schemas or a request that cannot be summarized can still need a larger window. A failure keeps the provider's or compaction's specific reason.

Pi also manages saved context when you switch models. The full chat stays saved, and Nod can search earlier details. If the request or its summary cannot fit the new model, choose a model with more context or shorten the request.

The same server checks still decide app actions, sign-ins and payments. A smaller context window does not change those checks. Model ability still affects whether Nod can complete a task.

To compare what each model declares with how it scores on computer use, tool selection and coding, see [Measure model capabilities](https://nod.n8n.io/docs/contribute/evals/#measure-model-capabilities).

Nod can use a decision model to check action permission, read confirmation replies, and check emails that give account access. Your selected text model writes most confirmation questions and button labels in your conversation language. The same model checks its wording against the saved action and arguments in a separate request. For permanent Gmail deletion, Nod writes a fixed question and button label from verified target details in English, regardless of your conversation language, without a wording-model request. You can answer in any language. Nod selects each checker before its request. A failed check never switches models.

### Select the action checker

[Section titled “Select the action checker”](https://nod.n8n.io/docs/connect/models/#select-the-action-checker)

Set `NOD_TRUST_MODEL` in the server configuration, then [apply the change](https://nod.n8n.io/docs/deploy/configuration/#how-settings-work).

| Value | Action permission, strict app reads, and confirmation replies |
| --- | --- |
| `selected` | Your selected model at its lowest reasoning setting. This is the default. |
| `llm` | A small LLM. |
| `decision` | The first available decision model, or a small LLM. |

For an audio model, `selected` uses the same-connection text companion shown under **Text support**. The small LLM comes from your selected connection when it offers a known small model. Otherwise, Nod chooses a known small model from another connected service. It chooses before making a request. If no small model is available, the check cannot authorize an action. It never replaces the small checker with your larger chat model.

The small checker can have API costs. A free OpenRouter selection does not start a paid small checker. If no checker is available, Nod cannot approve an action. Check model charges in Usage.

Decision mode selects the first available option in this order:

1.   Direct TypeSafe Jev 1.14 with `TYPESAFE_API_KEY`.
2.   Jev 1.14 through OpenRouter.
3.   Perplexity Decider 1.2 through OpenRouter.
4.   OpenAI Decisions with an OpenAI API key, or through OpenRouter.
5.   The same small LLM as `llm` mode, when none of these decision models is available.

These keys can come from a connection other than your chat model. ChatGPT subscription credentials never go to a decision service. Nod uses OpenRouter's decision-model list for your key, which applies your provider, privacy and access settings. This list is cached for five minutes. A failed lookup blocks the check. Nod keeps one provider for all steps of each check. A failed or uncertain decision never switches the checker to an LLM.

`NOD_TRUST_MODEL=decision`

There is no separate decision-model setting. Nod selects the model. The confirmation writer and wording check receive the proposed action and arguments, available target details and task or schedule context, and page-visible text for browser confirmations. Nod redacts known secrets and private links first. The action and reply classifiers still use the selected trust mode.

The gate receives the complete action, owner messages and rules. It receives no tool results or page text. It must preserve exact targets and terms. The server obtains a permission quote from the selected owner source and checks it against the original words. Choosing a source cannot authorize an action by itself.

Jev classifies the full action, then checks the selected owner words in a separate request without action data. A fixed local classifier combines those probabilities. This uses no LLM in decision mode. Reads and private work get a separate effect check, including each declared nested operation.

The server adds calendar facts for month ends, leap days, time zones, and local scheduled-run times. Jev selects the relevant time fields and owner constraints. It also reads calendar dates inside scheduled messages. Code compares explicit clocks, weekdays and elapsed event lengths. These facts grant no permission. The original input stays unchanged. An action that changes Nod settings, signs in, opens a saved session, or uploads a file cannot use the private-preparation path.

A time zone in your words controls conversion. Otherwise, Nod uses your configured time zone, or UTC when none is set. An unresolved relative date requires confirmation.

Before code corrects a time comparison, Jev checks all your instructions for other time conditions. A deadline warning still blocks the action.

A decision request must return every requested answer in a valid form. Missing answers, invalid probabilities and failures cannot authorize an action. A request that exceeds the provider limit fails the check. Nod never cuts your instructions to fit.

Strict app reads and confirmation replies use their own checks. A Jev strict read needs both its read-only check and a separate effect check. Both must reach the Jev threshold of 0.8. The effect check rejects private drafts and each nested write. Other decision models use a read threshold of 0.99. These thresholds are model settings, not measured error rates. An uncertain strict read is skipped. An uncertain reply stays undecided. The reply check sees only your reply, never the action, question or conversation.

### Account-access email checks

[Section titled “Account-access email checks”](https://nod.n8n.io/docs/connect/models/#account-access-email-checks)

Account-access email checks have separate connection rules in every mode. Without a decision service, email checks use the connection's smaller background model.

Pick a capable checker if Nod acts for you. See the [trust check](https://nod.n8n.io/docs/trust/approvals/) and [decision evals](https://nod.n8n.io/docs/contribute/evals/#compare-decision-checks).

| Current connection | Account-access email checks |
| --- | --- |
| OpenAI API key | GPT Decisions (`gpt-6-luna`) with the same key |
| OpenRouter | Jev (`typesafe/jev-1.13`) with the same OpenRouter key |
| Every other connection | Your connection's smaller background model |

These calls are billed through the connection that runs them. GPT Decisions is paid API use, separate from a ChatGPT subscription. OpenRouter sends the checks to TypeSafe, even when you selected a chat model from another provider. See [OpenAI Decisions](https://developers.openai.com/api/docs/guides/decisions) and [Jev on OpenRouter](https://openrouter.ai/blog/insights/what-is-jev/).

In a source install or self-hosted server, set `TYPESAFE_API_KEY` in `.env` to use Jev directly (`jev-1.13.0`) for these checks. The key selects TypeSafe regardless of your chat connection. Remove it to use the connection rules above, then [apply the configuration change](https://nod.n8n.io/docs/deploy/configuration/#how-settings-work). The key stays on the server and is not added to **Models**.

A failed decision request does not switch providers or approve anything: a failed account-access email check hides that email's content. See [Approvals and the trust check](https://nod.n8n.io/docs/trust/approvals/).

## Set connections in server settings

[Section titled “Set connections in server settings”](https://nod.n8n.io/docs/connect/models/#set-connections-in-server-settings)

In a source install or self-hosted server, you can add connections in `.env`. They show **Server settings** in **Models**. Update their values in `.env`, then [apply the configuration change](https://nod.n8n.io/docs/deploy/configuration/#how-settings-work).

Removing an API key removes its server-managed connection. For an OpenAI-compatible server, remove `OPENAI_COMPATIBLE_BASE_URL` instead. Connections saved through the app stay intact. If you removed the selected connection, choose another model in **Models**.

Every service below supports environment setup. You can add several provider keys at once. Set `LLM_PROVIDER` to the provider ID for your initial model choice. Leave `LLM_MODEL` empty for the [provider's default](https://nod.n8n.io/docs/connect/models/#supported-connections), or set an exact model ID from its list. A model you choose in the app takes priority. ChatGPT subscriptions still need browser sign-in in **Models**.

| Provider ID | Service | Key variable |
| --- | --- | --- |
| `openai` | OpenAI | `OPENAI_API_KEY` |
| `anthropic` | Anthropic | `ANTHROPIC_API_KEY` |
| `google` | Google Gemini | `GEMINI_API_KEY` |
| `openrouter` | OpenRouter | `OPENROUTER_API_KEY` |
| `amazon-bedrock` | Amazon Bedrock | `AWS_BEARER_TOKEN_BEDROCK` |
| `google-vertex` | Google Vertex AI | `GOOGLE_CLOUD_API_KEY` |
| `azure` | Azure OpenAI | `AZURE_OPENAI_API_KEY` |
| `ant-ling` | Ant Ling | `ANT_LING_API_KEY` |
| `baseten` | Baseten | `BASETEN_API_KEY` |
| `cerebras` | Cerebras | `CEREBRAS_API_KEY` |
| `cloudflare-workers-ai` | Cloudflare Workers AI | `CLOUDFLARE_WORKERS_AI_API_KEY` |
| `cloudflare-ai-gateway` | Cloudflare AI Gateway | `CLOUDFLARE_AI_GATEWAY_API_KEY` |
| `deepseek` | DeepSeek | `DEEPSEEK_API_KEY` |
| `fireworks` | Fireworks AI | `FIREWORKS_API_KEY` |
| `groq` | Groq | `GROQ_API_KEY` |
| `huggingface` | Hugging Face | `HF_TOKEN` |
| `kimi-coding` | Kimi Coding China | `KIMI_API_KEY` |
| `meta` | Meta | `META_API_KEY` |
| `minimax` | MiniMax | `MINIMAX_API_KEY` |
| `minimax-cn` | MiniMax China | `MINIMAX_CN_API_KEY` |
| `mistral` | Mistral | `MISTRAL_API_KEY` |
| `moonshotai` | Moonshot AI | `MOONSHOT_API_KEY` |
| `moonshotai-cn` | Moonshot AI China | `MOONSHOT_CN_API_KEY` |
| `nvidia` | NVIDIA | `NVIDIA_API_KEY` |
| `opencode` | OpenCode Zen | `OPENCODE_API_KEY` |
| `opencode-go` | OpenCode Go | `OPENCODE_GO_API_KEY` |
| `qwen-token-plan` | Qwen Token Plan | `QWEN_TOKEN_PLAN_API_KEY` |
| `qwen-token-plan-cn` | Qwen Token Plan China | `QWEN_TOKEN_PLAN_CN_API_KEY` |
| `qwen-token-plan-individual` | Qwen Token Plan Individual | `QWEN_TOKEN_PLAN_INDIVIDUAL_API_KEY` |
| `radius` | Radius | `RADIUS_API_KEY` |
| `together` | Together AI | `TOGETHER_API_KEY` |
| `vercel-ai-gateway` | Vercel AI Gateway | `AI_GATEWAY_API_KEY` |
| `xai` | xAI | `XAI_API_KEY` |
| `xiaomi` | Xiaomi MiMo | `XIAOMI_API_KEY` |
| `xiaomi-token-plan-ams` | Xiaomi Token Plan Amsterdam | `XIAOMI_TOKEN_PLAN_AMS_API_KEY` |
| `xiaomi-token-plan-cn` | Xiaomi Token Plan China | `XIAOMI_TOKEN_PLAN_CN_API_KEY` |
| `xiaomi-token-plan-sgp` | Xiaomi Token Plan Singapore | `XIAOMI_TOKEN_PLAN_SGP_API_KEY` |
| `zai` | Z.AI | `ZAI_API_KEY` |
| `zai-coding-cn` | Z.AI Coding China | `ZAI_CODING_CN_API_KEY` |

Additional settings:

| Service | Settings |
| --- | --- |
| OpenAI | `OPENAI_API_REGION`: `global` by default. Use `eu` for Europe or `us` for the United States. Other regions: `au`, `ca`, `in`, `jp`, `sg`, `kr`, `ae`, and `gb`. |
| Anthropic | `ANTHROPIC_WORKSPACE_ID`, required for organization keys that aren't limited to one workspace. Leave empty for keys limited to one workspace. |
| Amazon Bedrock | `AWS_REGION`, such as `us-east-1`. Set `LLM_MODEL` to select a model or inference profile when several are available. |
| Azure OpenAI | `AZURE_OPENAI_ENDPOINT` and `AZURE_OPENAI_MODEL`, the model ID your deployment runs. Set `AZURE_OPENAI_DEPLOYMENT` if the deployment has a different name. |
| Cloudflare | `CLOUDFLARE_ACCOUNT_ID`, the 32-character hexadecimal account ID. AI Gateway also requires `CLOUDFLARE_GATEWAY_ID`. |
| OpenAI-compatible | `OPENAI_COMPATIBLE_BASE_URL` and optional `OPENAI_COMPATIBLE_API_KEY`. Use `LLM_PROVIDER=compatible` for the initial choice. |

Set the cloud provider's required fields before starting Nod. A Cloudflare gateway ID has one to 64 lowercase letters, digits, or hyphens, starting with a letter or digit. Both Cloudflare connections use the same account ID from `.env`; connections saved in **Models** can use separate accounts and gateways.

For Azure, leave `LLM_MODEL` empty to use the deployment's model, or set it to the same model ID as `AZURE_OPENAI_MODEL`. The deployment name defaults to that ID. The [Azure setup rules](https://nod.n8n.io/docs/connect/models/#connect-a-service) for endpoints also apply to `.env`.

`LLM_PROVIDER=googleGEMINI_API_KEY=<your-key>`

Regional providers use separate key variables so one region's key isn't automatically sent to another region. These connections don't inherit host-wide AWS profiles or Google service account files.

## Where your keys go

[Section titled “Where your keys go”](https://nod.n8n.io/docs/connect/models/#where-your-keys-go)

The Nod server adds your key to each model request. The key never enters the workspace, Nod's browser or the model's context.

*   Nod encrypts saved keys and sign-ins with the Vault key. macOS uses Keychain, the Windows app uses Windows DPAPI, and the Linux Flatpak uses Secret Service. Linux source installs use a private file. The self-hosting stack generates `NOD_VAULT_KEY` in its private `.env`. See [Vault configuration](https://nod.n8n.io/docs/deploy/configuration/#vault).
*   Nod checks credential storage before starting a connection. If storage is unavailable, check the Vault configuration, permissions and database connection, then try again.
*   Keys from `.env` stay in server memory and aren't copied into the database.
*   Each key goes only to its own service: Amazon Bedrock in the Region you entered, Google Vertex AI, or the Azure OpenAI endpoint you entered.
*   Your browser doesn't store the key, and Nod removes it from provider errors.

*   [Local models](https://nod.n8n.io/docs/connect/local-models/)
*   [Apps with Composio](https://nod.n8n.io/docs/connect/apps/)
*   [MCP servers, APIs and CLIs](https://nod.n8n.io/docs/connect/mcp-api-cli/)
*   [Configuration](https://nod.n8n.io/docs/deploy/configuration/)
*   [Spending](https://nod.n8n.io/docs/use/spending/)
*   [Your data and privacy](https://nod.n8n.io/docs/trust/privacy/)

## Images with a text model

[Section titled “Images with a text model”](https://nod.n8n.io/docs/connect/models/#images-with-a-text-model)

If your selected model cannot read images, Nod looks for an image model in your connected services. It checks your selected connection first, then your other connected services. When one is available, it receives your current request and the images. Your selected chat model receives its description and stays selected. This image request uses that service's credentials and counts toward your spending limits. If no image model is available, the files stay in the workspace. See [Files and voice messages](https://nod.n8n.io/docs/use/channels/#files-and-voice-messages).



## Schedules and background work — https://nod.n8n.io/docs/use/schedules/
Title: Schedules and background work

URL Source: https://nod.n8n.io/docs/use/schedules/

Markdown Content:
Ask Nod to do something later or regularly, and it saves a schedule and does the work in the background.

When you ask, Nod also notices new email and activity in your connected apps and prepares useful work on its own. This page covers both.

## Create a schedule

[Section titled “Create a schedule”](https://nod.n8n.io/docs/use/schedules/#create-a-schedule)

Ask in chat. For example:

*   "Every weekday at 8:00, summarize my calendar and anything urgent in my inbox."
*   "Tomorrow at 15:00, remind me to call the landlord."

A schedule runs **One time** or is **Recurring**. Nod tells you when it's saved and when it runs next. If you ask for a schedule that's already active with the same name or instruction, time and chat, Nod keeps the one you have instead of adding a copy, and uses the model you named for it, if any. When you hand Nod work that needs follow-up, it can also plan its own check-in, such as "I'll look for a reply on Friday". Check-ins are schedules too.

Nod uses your time zone, saved from your browser the first time you use Nod. Change it in **Settings → General**. If Nod doesn't know your time zone, it asks.

## Change, pause or delete a schedule

[Section titled “Change, pause or delete a schedule”](https://nod.n8n.io/docs/use/schedules/#change-pause-or-delete-a-schedule)

Open **Scheduled**. Select **New schedule** to start a conversation with Nod, which asks one question at a time about what to do and when. Existing schedules show their timing and next run.

*   Use the switch to pause or resume it.
*   Select **Run now** to start one run and open its history.
*   Select **See details** to read the instruction, any saved baseline, and that schedule's runs.
*   Select **Edit schedule** to change its name, instructions or timing.
*   Select **Ask Nod** to change it in your own words.
*   Select **Delete schedule**. Future runs stop, and past activity stays in [Usage](https://nod.n8n.io/docs/use/spending/).

Pausing or deleting a schedule here removes any unanswered request to change or cancel it from Nod's chat. A request already sent to Telegram or WhatsApp remains there, but replying to it cannot change the schedule.

In chat, "stop the morning summary" asks Nod to pause the schedule. If Nod asks for confirmation, it stays active until you approve. Once paused, you can resume it in **Scheduled**; use **Delete schedule** to remove it.

## Run a schedule now

[Section titled “Run a schedule now”](https://nod.n8n.io/docs/use/schedules/#run-a-schedule-now)

Open **Scheduled** and select **Run now** on a schedule. Nod opens its details so you can follow the run. The new result opens when it is available.

The extra run uses the saved instruction and delivery channel. The usual approval checks still apply. It does not change the next scheduled time or resume a paused schedule. You can also run a completed one-time schedule again.

The button shows **Queued**, **Working**, or **Needs your input** while a run is active. You cannot start another run until that run ends. A recurring schedule skips timed runs that fall due during an active run. A one-time schedule waits for the active run to end.

**Run now** runs a watch even when its connected accounts have no changes. If the connection drops, **Try again** checks or starts the same run. It cannot start a second copy.

## What happens when a schedule runs

[Section titled “What happens when a schedule runs”](https://nod.n8n.io/docs/use/schedules/#what-happens-when-a-schedule-runs)

flowchart TD
  due[Schedule is due]:::accent --> run[Nod runs it<br/>in the background]
  run --> check[Trust check<br/>against your instruction]
  check --> useful{{Something you asked to get,<br/>a useful result or a question?}}
  useful -- yes --> send[Message in the chat<br/>where you set it up]:::go
  useful -- no --> quiet[Stays quiet]:::muted
*   **It runs next to your chat.** A schedule doesn't wait for the conversation, and the conversation doesn't wait for it.
*   **What you asked to get arrives every time.** A summary, brief or reminder comes on every run. A watch or check-in messages you only when something needs you, such as a real price drop, a problem or a question. Routine checks stay quiet.
*   **A failed run tells you.** If a run stops on an error, Nod sends a short message that names the schedule and says what stopped it, so a missing summary never goes unnoticed.
*   **It replies where you asked.** A schedule you set up on Telegram sends its messages to Telegram.
*   **Corrections keep the rest.** Nod keeps the owner request and later changes used to set up the schedule. “Every hour instead” changes timing. “Send it to Lena instead” changes the recipient. Other limits stay in effect, and a later “only summarize” removes an earlier send request. Timing changes keep their owner request even when the work instruction stays the same. There is no ten-change reset.
*   **Approvals still apply.** Each outside action passes the same [trust check](https://nod.n8n.io/docs/trust/approvals/). The checker gets the saved owner inputs in order, the exact proposal a reply answered, and the run time. Earlier eligible owner messages can explain “it” or “that folder”; they cannot grant another action. Chat, tasks and schedules use the same source-selection rules. LLM and decision-model checks receive the same evidence. If your instructions do not cover an action, Nod asks first. If the check cannot decide, the action does not run and Nod does not ask.
*   **A complete instruction approval has a clear scope.** When you approve a new complete schedule instruction, Nod shows its future work, targets, timing and limits. That approval can cover the recurring work it describes. Approving a name or timing change changes only those fields. Approving one email never grants recurring sends.
*   **Saved instructions stay traceable.** Each run keeps its execution request, run time and owner inputs. Required messages that become withdrawn or unavailable cannot return as permission. Nod then refuses work that needs them. You can save a complete replacement in **Schedules**, or approve a complete replacement Nod proposes. A check that cannot process the complete request refuses it; it never drops older limits to fit. Existing schedules keep their known instruction without guessed earlier context. Some schedules changed through an older Nod version have incomplete permission history. To use them again, edit their complete instruction in **Schedules**, or approve a complete replacement that Nod proposes.
*   **One run at a time.** While a run is still queued, working or waiting for your answer, a recurring schedule skips its next runs. A one-time schedule waits for the active run to end. A run does its work itself and can't set up more schedules.
*   **Watches skip unchanged runs.** When a recurring check can only find something new after a change in your connected accounts, such as waiting for a reply, Nod saves which accounts it watches. Before each run, Nod checks those accounts for new mail, changed events or app activity without a model call, and skips the run when nothing changed since the last finished run. The first run, and the run after a failed one, always run. Reminders, digests, websites and checks tied to a time don't skip.

Open a schedule's **See details** to read its runs, newest first. Select **Load earlier runs** for older results. Completed one-time schedules remain under **Inactive**, with their runs available to review.

Each run shows its status. When a saved web reply is available, select **See details** on the result to read it within the schedule. Runs with complete API pricing also show their recorded cost. Subscription usage and runs with unavailable pricing show no cost amount. Review recorded app actions and activity from deleted schedules in [Usage](https://nod.n8n.io/docs/use/spending/).

## Work Nod starts on its own

[Section titled “Work Nod starts on its own”](https://nod.n8n.io/docs/use/schedules/#work-nod-starts-on-its-own)

Nod reads every app you connect on its own, prepares useful work privately and messages you only when it's worth it. See [Nudges](https://nod.n8n.io/docs/use/nudges/). There's nothing to turn on. At any time, you can say what's worth interrupting you for, such as "tell me when a client emails", and Nod uses it to choose what to flag.

How Nod checks:

*   **Gmail.** Nod checks for new inbox mail every 15 minutes. If a check is temporarily unavailable, it keeps the messages already found and schedules another check one to five minutes later. Each new message starts a quiet private run that decides whether there's useful work, such as preparing a reply.
*   **Google Calendar.** Nod checks for changed events every 30 minutes without a model call.
*   **Other connected apps.** Every 30 minutes, one quiet private run reads them through their own read tools.

Work Nod starts on its own reads and drafts. It sends, deletes or changes something only when you've told it to do that on its own, such as "whenever Ana sends an invoice, forward it to [accounting@acme.com](mailto:accounting@acme.com)". Anything else waits for your yes. [Your rules](https://nod.n8n.io/docs/trust/approvals/#your-rules) can change both: a rule to go ahead lets an action run without asking, and a rule to ask first makes Nod ask even when your standing instruction covers the action. See [Standing instructions](https://nod.n8n.io/docs/trust/approvals/#standing-instructions). To change or stop it, tell Nod, for example "stop flagging Slack messages".

The private preparation behind nudges can only read, prepare private work and nudge you. It can't send, delete, submit, book, buy or change connected apps. To stop it, tell Nod "Pause preparation".

The first time Nod messages you about something on its own, such as a calendar change, it sends a short second message to say it will keep doing this. When that first message asks you something, the line goes in it, before the question, so a short reply still answers the question. Tell it to stop or to do less at any time. After a one-off job that will come up again, such as this week's top posts or a reply to a client, Nod offers once, in its own message, to keep doing it, unless a schedule already covers it. It sets nothing up until you say yes. When you act on something background work brought you, such as asking Nod to reply, and it will come up again, Nod offers once to do it without asking next time.

## Edit schedule details

[Section titled “Edit schedule details”](https://nod.n8n.io/docs/use/schedules/#edit-schedule-details)

Select **Edit schedule** to review its name, instructions and timing together. Timing changes preview the next run without changing the saved schedule. **Save changes** applies only the fields you changed, so renaming a schedule keeps its next run. Editing the complete work instruction supplies a new complete instruction. A name or timing edit keeps the existing work and its permission limits. **Cancel** closes the editor without saving.

A schedule uses the model for schedules from **Settings > Models**. To give one schedule its own model, open **See details** and select **Change** beside **Model**. When a recurring schedule shows a projected monthly cost, it prices the schedule's recent runs on that model. See [Models for each kind of work](https://nod.n8n.io/docs/connect/models/#models-for-each-kind-of-work).

**Undo** restores the previous values only if no newer change has replaced them. The Undo notice stays available while you hover over it, focus it, or switch away from Nod. If the schedule changes while you edit, your draft stays open so you can review it.

Quiet hours are on by default, from 22:00 to 08:00. Change them in **Settings → Notifications → Quiet hours**.

During quiet hours, Nod keeps checking new mail and app activity, but prepares only what may need you before quiet hours end; everything else waits until they end. Its nudges wait until they end, except a high-impact one with strong evidence whose deadline comes first. Any task it starts on its own waits too, with its questions and approvals. Schedules you created still run and deliver on time.

For a local assistant, closing the window keeps Nod running in the menu bar or tray. **Quit Nod** stops it. **Open at login** is on after setup; keep it on in **Settings → General** if you rely on schedules. It starts Nod when you sign in to your computer, not when the computer turns on, so after a restart or power cut nothing runs until you sign in. On a Mac with FileVault turned on, automatic login is off, so someone has to enter your password after every restart.

If a run comes due while the assistant is stopped, it runs once when Nod is running again. If a run starts more than 10 minutes late, its instructions include the due time and start time. If later runs of a recurring schedule were skipped, the instructions also include that count. Counts of 100 or more are shown as "100 or more".

*   [Track tasks](https://nod.n8n.io/docs/use/tasks/)
*   [Chat with Nod](https://nod.n8n.io/docs/use/chat/)
*   [Telegram and WhatsApp](https://nod.n8n.io/docs/use/channels/)
*   [Approvals and the trust check](https://nod.n8n.io/docs/trust/approvals/)
*   [Connect apps](https://nod.n8n.io/docs/connect/apps/)



## Trust and Vault — https://nod.n8n.io/docs/trust/
Title: Trust and Vault

URL Source: https://nod.n8n.io/docs/trust/

Markdown Content:
Trust decides what Nod can do in your apps and on websites. Vault decides how Nod uses your saved logins and cards, and it never shows them to the model.

Nod can sign in to a website, read a report, prepare a reply and complete a checkout. The model plans that work. A separate check decides which app actions, browser steps and sign-ins can run. It sees your words and the action, never the pages or emails Nod read: for a browser step, that's the website, the control's label and what Nod typed. It asks you when your words don't cover the action. Every payment waits for your approval.

[Video 3](https://nod.n8n.io/docs/_astro/trust-layer.CwBCO0RM.mp4)
Watch a narrated overview with synthetic data. The scenes show example states from the app. The model check can make mistakes.

## Two jobs, two paths

[Section titled “Two jobs, two paths”](https://nod.n8n.io/docs/trust/#two-jobs-two-paths)

|  | Trust | Vault |
| --- | --- | --- |
| Protects | Actions in your connected apps | Saved logins, verification codes and cards |
| Checks | The action and its arguments as Nod sends them | The task, the saved account and the exact website |
| Asks you when | Your words don't cover an action beyond a read or draft | Nod wants an account you haven't allowed for this task |
| The model sees | The action and its result | Account names and status, never the secret |
| You review it in | The confirmation in chat and **Usage** | **Usage** |

## Three rules behind everything

[Section titled “Three rules behind everything”](https://nod.n8n.io/docs/trust/#three-rules-behind-everything)

Authority comes from you

Nod is designed so that only you give it permission, through your messages, approvals and the instructions you set, never a web page, email or file.

Secrets have their own path

The server enters saved values into the website. The model never receives them.

One use, one result

An approved action runs once. If the outcome is unclear, Nod says so. You check the result, or ask Nod to, before any new attempt.

## What Nod does in common cases

[Section titled “What Nod does in common cases”](https://nod.n8n.io/docs/trust/#what-nod-does-in-common-cases)

| You ask Nod to | What happens |
| --- | --- |
| Read your calendar or inbox | It runs. |
| Draft a reply | It runs. |
| Add an event, send an email or delete files | A review checks it matches your request, then it runs. If it doesn't match, Nod asks. |
| Email a recipient you didn't ask it to contact | The review finds no permission for that recipient, so Nod asks. |
| Sign in to a site with a saved login | Vault checks the account and website, then fills in the password privately. |
| Pay at a checkout | You approve that one payment with your card's security code, which Nod never saves. |
| Do something while it reacts to a new email on its own | It does what you told it to do on its own, such as forwarding Ana's invoices to [accounting@acme.com](mailto:accounting@acme.com), unless a rule says to ask first. Anything else waits for you unless a rule allows it. Separately, it reads your apps and can nudge you about work it prepared, without acting. |

## Where you see and change things

[Section titled “Where you see and change things”](https://nod.n8n.io/docs/trust/#where-you-see-and-change-things)

*   **Usage** in the sidebar (⌘5 in the Mac app, Ctrl+5 in the Windows or Linux app) shows what Nod did and spent: app actions, sign-ins, card uses, questions and held attempts, with costs when pricing is available. For API models, the summary shows this month's spending and monthly limit; select a value to inspect or change it. With a subscription such as ChatGPT, it shows plan usage without costs or limit controls. Activities with an available chat message open that message; sign-ins and card uses open their saved Vault item when it is still available.
*   **Chat** is where you ask Nod to show or change [standing instructions](https://nod.n8n.io/docs/trust/approvals/#standing-instructions), [rules](https://nod.n8n.io/docs/trust/approvals/#your-rules) and [task check-ins](https://nod.n8n.io/docs/use/spending/#task-check-ins).
*   **Vault** (⌘6 or Ctrl+6) lists your logins, cards and saved browser sessions. Edit or remove logins and cards, and sign out of sessions.
*   **Settings → Memory** shows what Nod remembers about you and where it learned it.

*   [Our trust principles](https://nod.n8n.io/docs/trust/principles/): the seven commitments behind Nod's design.
*   [How Nod compares](https://nod.n8n.io/docs/trust/compare/): Nod next to other assistants that act for you.
*   [Security review guide](https://nod.n8n.io/docs/trust/security-review/): what a security team needs to assess Nod.
*   [Approvals and the trust check](https://nod.n8n.io/docs/trust/approvals/): which app actions run directly and which wait for you.
*   [Untrusted content](https://nod.n8n.io/docs/trust/untrusted-content/): how Nod treats pages, emails and files that try to give it instructions.
*   [Vault and saved logins](https://nod.n8n.io/docs/trust/vault/): add logins, sign in privately and review activity.
*   [Saved browser sessions](https://nod.n8n.io/docs/trust/browser-sessions/): reuse a signed-in browser on the websites you allow.
*   [Payments](https://nod.n8n.io/docs/trust/payments/): approve one checkout with a saved card.
*   [One use, one result](https://nod.n8n.io/docs/trust/outcomes/): why approved work never runs twice.
*   [Your data and privacy](https://nod.n8n.io/docs/trust/privacy/): where your assistant stores data and what it sends to other services.
*   [Conversation traces](https://nod.n8n.io/docs/trust/conversation-traces/): what the optional traces contain, what Nod removes first and how they avoid identifying you.
*   [Security model and limits](https://nod.n8n.io/docs/trust/security-model/): the exact boundaries, and what they don't cover.



## How Nod compares — https://nod.n8n.io/docs/trust/compare/
Title: How Nod compares

URL Source: https://nod.n8n.io/docs/trust/compare/

Markdown Content:
This page compares Nod with other personal assistants that act for you, on the questions a security team asks first.

The short version: most assistants run on their vendor's servers and ask you to trust that vendor. Nod runs where you choose, enforces its rules outside the model, and lets you read the code that makes each decision.

|  | Nod | Instinct | Meta Muse | OpenAI dots |
| --- | --- | --- | --- | --- |
| Where it runs | ✅ Your computer, or your own hosting | ❌ Vendor service, connected to your apps and devices [1](https://nod.n8n.io/docs/trust/compare/#user-content-fn-1) | ❌ A dedicated VM on Meta's service [2](https://nod.n8n.io/docs/trust/compare/#user-content-fn-3) | ⚠️ Not documented |
| Who can access your data | You and the hosting operator. n8n processes default managed app traffic, plus optional feedback, analytics and traces | ❌ Terms grant a "perpetual and irrevocable" licence, including for training [1](https://nod.n8n.io/docs/trust/compare/#user-content-fn-1) | ⚠️ Meta, "to support, secure or operate the service" [3](https://nod.n8n.io/docs/trust/compare/#user-content-fn-2) | ⚠️ Not documented |
| Model | ✅ Your choice of provider | ⚠️ Not documented | ❌ Meta's own model [2](https://nod.n8n.io/docs/trust/compare/#user-content-fn-3) | ❌ OpenAI's own models |
| Rules enforced outside the model | ✅ Server trust check | ❌ Reported sending an email without asking [1](https://nod.n8n.io/docs/trust/compare/#user-content-fn-1) | ✅ A separate permission process [3](https://nod.n8n.io/docs/trust/compare/#user-content-fn-2) | ⚠️ Rules exist; enforcement not documented [4](https://nod.n8n.io/docs/trust/compare/#user-content-fn-4) |
| Secrets kept out of the model | ✅ Private entry and masking | ⚠️ Not documented | ✅ Placeholder tokens swapped at the network edge [3](https://nod.n8n.io/docs/trust/compare/#user-content-fn-2) | ⚠️ Not documented |
| A record of what it did | ✅ Usage page: every app change, send, sign-in and card use | ⚠️ Not documented | ✅ "Complete audit trail" [2](https://nod.n8n.io/docs/trust/compare/#user-content-fn-3) | ✅ Activity view [4](https://nod.n8n.io/docs/trust/compare/#user-content-fn-4) |
| Hard spending limit | ✅ Monthly limit | ⚠️ Not documented | ⚠️ Not documented | ⚠️ Not documented |
| Open source | ✅ Apache 2.0 | ❌ | ❌ | ❌ |

✅ yes · ⚠️ partly, or not documented · ❌ no

## Why these questions matter

[Section titled “Why these questions matter”](https://nod.n8n.io/docs/trust/compare/#why-these-questions-matter)

### Where it runs decides who can read your life

[Section titled “Where it runs decides who can read your life”](https://nod.n8n.io/docs/trust/compare/#where-it-runs-decides-who-can-read-your-life)

An assistant that reads your email, calendar and documents holds a copy of your life. If it runs on a vendor's servers, that vendor's access policy is your privacy policy. A local Nod assistant keeps its server, database, workspace and browser on your computer. A self-hosted assistant keeps them on your server. Model requests go to the provider you picked. Managed app requests and results pass through the configured connection service and Composio; n8n hosts the default service. See [Your data and privacy](https://nod.n8n.io/docs/trust/privacy/).

### A check the agent can't skip

[Section titled “A check the agent can't skip”](https://nod.n8n.io/docs/trust/compare/#a-check-the-agent-cant-skip)

Models can be persuaded. A web page or an email can carry instructions written for an AI. Nod's trust check runs in the server, on the action as it will be sent. A separate review compares it with your own words. It doesn't read the page or email itself, only what Nod puts into the action. The review is a model too, so it can be wrong, but injected text has to get past it rather than simply tell Nod what to do. [See how approvals work](https://nod.n8n.io/docs/trust/approvals/).

### Checkable, not just promised

[Section titled “Checkable, not just promised”](https://nod.n8n.io/docs/trust/compare/#checkable-not-just-promised)

Every Nod user gets the full record: each use of a saved login, each held action, each app action and its cost. And because the code is open, a security team can read the exact rule behind every decision. [Read the principles](https://nod.n8n.io/docs/trust/principles/).

## Where others are ahead

[Section titled “Where others are ahead”](https://nod.n8n.io/docs/trust/compare/#where-others-are-ahead)

Being honest about gaps is part of the deal.

*   **Single-use cards.** Muse pays with single-use card numbers tied to one merchant and amount [3](https://nod.n8n.io/docs/trust/compare/#user-content-fn-2). Nod stores a card in its Vault and can't enforce the amount at the card issuer. [See payment limits](https://nod.n8n.io/docs/trust/payments/).
*   **Bug bounty.** Meta offers rewards of up to $300,000 for Muse reports [3](https://nod.n8n.io/docs/trust/compare/#user-content-fn-2). Nod takes private reports through its [security policy](https://github.com/n8n-io/nod/blob/main/SECURITY.md), without a published bounty.
*   **Key isolation.** Muse swaps placeholder tokens at the network edge [3](https://nod.n8n.io/docs/trust/compare/#user-content-fn-2). Nod's server can read a saved value while it uses it. [See the limits](https://nod.n8n.io/docs/trust/security-model/).

*   [Trust and Vault overview](https://nod.n8n.io/docs/trust/)
*   [Our trust principles](https://nod.n8n.io/docs/trust/principles/)
*   [Security review guide](https://nod.n8n.io/docs/trust/security-review/)

1.   TechCrunch, [Instinct's powerful AI assistant is raising privacy and security concerns](https://techcrunch.com/2026/08/24/instincts-powerful-ai-assistant-is-raising-privacy-and-security-concerns/), 24 August 2026. [↩](https://nod.n8n.io/docs/trust/compare/#user-content-fnref-1)[↩2](https://nod.n8n.io/docs/trust/compare/#user-content-fnref-1-2)[↩3](https://nod.n8n.io/docs/trust/compare/#user-content-fnref-1-3)

2.   Meta, [Introducing Muse](https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/), September 2026. [↩](https://nod.n8n.io/docs/trust/compare/#user-content-fnref-3)[↩2](https://nod.n8n.io/docs/trust/compare/#user-content-fnref-3-2)[↩3](https://nod.n8n.io/docs/trust/compare/#user-content-fnref-3-3)

3.   Meta, [Security and safety for AI agents: our approach with Muse](https://research.meta.ai/blog/security-and-safety-for-ai-agents-our-approach-with-muse), September 2026. [↩](https://nod.n8n.io/docs/trust/compare/#user-content-fnref-2)[↩2](https://nod.n8n.io/docs/trust/compare/#user-content-fnref-2-2)[↩3](https://nod.n8n.io/docs/trust/compare/#user-content-fnref-2-3)[↩4](https://nod.n8n.io/docs/trust/compare/#user-content-fnref-2-4)[↩5](https://nod.n8n.io/docs/trust/compare/#user-content-fnref-2-5)[↩6](https://nod.n8n.io/docs/trust/compare/#user-content-fnref-2-6)

4.   OpenAI, [dots controls](https://learn.chatgpt.com/docs/dots/controls.md), October 2026. [↩](https://nod.n8n.io/docs/trust/compare/#user-content-fnref-4)[↩2](https://nod.n8n.io/docs/trust/compare/#user-content-fnref-4-2)

