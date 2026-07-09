# redis.io

## Fetch log
- Inbox URL: https://redis.io/iris/
- Final URL: https://redis.io/iris/
- Fetched: 2026-07-09
- Pages: 4
- Mode: standard

## llms.txt — https://redis.io/llms.txt
(See on-disk capture at ingest time; catalog entries relevant to this page — RDI, LangCache, Redis for AI, Agent Memory tutorials — cross-referenced below. Full llms.txt is large and general-purpose across the entire redis.io site, not Iris-specific; only Iris-relevant excerpt retained here to keep the raw file focused.)

- [Redis Data Integration (docs)](https://redis.io/docs/latest/integrate/redis-data-integration/index.html.md): CDC-style sync from relational and operational databases into Redis with declarative pipelines.
- [Redis Data Integration (product)](https://redis.io/data-integration/): Near-real-time sync from Oracle, PostgreSQL, MySQL, MongoDB, SQL Server, and cloud SQL into Redis with CDC and declarative transforms.
- [LangCache](https://redis.io/langcache/): Managed semantic caching REST API to cut LLM token cost and latency via embedding-backed similarity matching.
- [Redis for AI](https://redis.io/redis-for-ai/): Positioning for RAG, vector retrieval, semantic cache, agent memory, and hybrid search on Redis as a unified low-latency context layer. Note: as of fetch date, this URL redirects to the Iris landing page content below — the standalone "Redis for AI" page appears to have been superseded/merged into Iris positioning.
- [How to build a car dealership AI agent with Google ADK and Redis Agent Memory Server](https://redis.io/tutorials/build-a-car-dealership-agent-with-google-adk-and-redis-agent-memory.md)
- [How to build a document agent with Redis, RAG, and agent memory](https://redis.io/tutorials/build-a-document-agent-with-redis-rag-and-agent-memory.md)
- [How to build semantic caching with Redis LangCache](https://redis.io/tutorials/semantic-caching-with-redis-langcache.md)
- [What is Agent Memory? Example using LangGraph and Redis](https://redis.io/tutorials/what-is-agent-memory-example-using-langgraph-and-redis.md)

## Landing page — https://redis.io/iris/
(Fetched via Jina Reader fallback — WebFetch's summarizer initially fabricated an inaccurate description, misattributing Redis Iris to "Anthropic"; verified and replaced with a verbatim capture below.)

REDIS IRIS

## Your agents should be getting smarter

Build them on fresh data & context that improves over time.

Unreliable agents fail in production. Redis Iris is a unified, real-time context engine that delivers fresh, relevant context so agents perform at scale.

Nav: Redis Iris | Context Retriever | RDI | Agent Memory | LangCache | Maturity Assessment | Get Started

## Context saves under-informed agents

Agents fail because data spread across countless systems is fragmented, stale, slow, and difficult to navigate. The results are inaccurate answers, slow performance, and frustrated users. Agents are missing the key context layer that makes data AI-ready.

Context delivers navigable systems, not data silos — Agents rely on connections to deliver the best performance. Data has to work as a connected system agents can explore, not just query.

Instant retrieval makes everything tick — Latency has a snowball effect. The more time it takes an agent to complete a step, the bigger the risk it will fall apart under real-world workloads.

Real-time data is always fresh — Data never sits still. Apps change state, CRMs update, and events don't stop. Agents have to trust that the context they have is accurate up to the instant.

Context must compound — Context should get more relevant, personalized, and informed by past interactions. That means agents must have memory, learning, and durable state built in.

## Introducing Redis Iris

Keeps operational state fresh in Redis, so agents act on current business context instead of stale exports, cron jobs, or brittle data pulls.

Gives agents a navigable path through business entities like customers, orders, and tickets, so they can reason over context instead of guessing across tools.

Lets context compound across sessions, channels, and agents, so every interaction can build on what happened before.

Keeps repeated and semantically similar LLM work fast by serving trusted responses from Redis inside the agent's latency budget.

## Address any data with Context Retriever

Give agents clean, schema-first paths through all business data, including customers, orders, tickets, and more. Agents spend less time guessing and more time reliably getting the right answers.

## Redis Data Integration feeds agents fresh data

Ground agents in what's actually happening. Pull fresh operational data from your systems of record straight into Redis, at the speed of Redis, so agents act on up-to-the instant business state in one runtime path.

## Agentic AI gets smarter with Agent Memory

Deliver working memory and long-term recall in one place. Keep current agent conversations tight with active context, while persisting vital long-term pieces like user preferences, past decisions, and more across sessions.

## Get answers before your window closes

Redis Search pulls and filters live operational context at Redis speed. LangCache cuts the waste, caching semantically similar prompts and responses so agents don't ask the same questions twice.

## See if your business is context-ready

Our context engineering maturity model gives a clear picture of where you stand today, what's blocking you from the next stage, and where to invest to close the gaps before your competitors do.

## Take the context maturity self assessment

8 questions. 2 minutes. Recommendations for your team.

NAVIGABLE — How do your AI agents access business data?

<250ms P95 query latency across all production workloads

### Customer testimonials

> Memory is core to how agents improve over time, and teams we work with are realizing they need scalable infrastructure behind it. Together, Redis Iris and LangSmith's Context Hub give customers a structured way to manage agent context across environments, connecting live operational data and retrieval into the same system that versions and evolves agent memory over time.
> — Harrison Chase, Cofounder and CEO, LangChain

> At Character.ai, every millisecond matters. Before Redis, we spent too much time fighting latency and managing complex pipelines. Redis lets us deliver fast, intelligent search that feels instantaneous to our users.
> — Yi Duan, Member of Technical Staff, Character.ai

> Redis Agent Memory helps us store and reuse context across our coding agents in real time. We use it to capture critical engineering decisions, bug details, and development context as our agents work, so that information is available across the team instead of getting lost between sessions or tools. We also have a service reading from and writing to the same memory while monitoring our API, which lets us detect issues and report bugs into our ticketing system in real time. We're excited to see what we can build next with Redis Iris.
> — Nick Thompson, Senior Software Developer, Safe in Home

## Ready to build with Redis Iris?

See how Redis Iris keeps your agents grounded in fresh, relevant context.

CTAs: Try for free (/try-free/?rcplan=iris) | Book a meeting with sales (/meeting/) | View the Context Engine Maturity Model report (/resources/the-context-engine-maturity-model/) | Take a context maturity self-assessment

## Redis Data Integration (docs) — https://redis.io/docs/latest/integrate/redis-data-integration/index.html.md

Redis Data Integration (RDI) keeps your Redis cache in sync with a primary system-of-record database in near real time.

RDI's purpose is to help Redis customers sync Redis Enterprise with live data from their slow disk based databases in order to:
- Meet the required speed and scale of read queries and provide an excellent and predictable user experience.
- Save resources and time when building pipelines and coding data transformations.
- Reduce the total cost of ownership by saving money on expensive database read replicas.

RDI keeps a Redis cache up to date with changes in the primary database, using a Change Data Capture (CDC) mechanism. It also lets you transform the data from relational tables into convenient and fast data structures that match your app's requirements. You specify the transformations using a configuration system, so no coding is necessary. RDI supports both standard Redis databases and Active-Active (CRDB) replication targets.

### RDI in Redis Cloud

RDI is also available as a fully managed service on Redis Cloud, removing the need to install or maintain the underlying infrastructure. Redis manages the compute, scaling, and upgrades for you. You define the source connection and pipeline configuration using the Redis Cloud console.

The Cloud service currently supports AWS-hosted source databases (Amazon RDS, Amazon Aurora, and Amazon EC2), as well as MongoDB Atlas and Snowflake, writing to a Redis Cloud Pro target database.

### Features

RDI provides enterprise-grade streaming data pipelines with the following features:
- **Near realtime pipeline** — CDC captures changes in short intervals, ships/processes them in micro-batches.
- **At least once guarantee** — RDI delivers any change to the selected data set at least once to the target Redis database.
- **Data integrity** — RDI keeps the data change order per source table or unique key.
- **High availability** — All stateless components have hot failover or quick automatic recovery; RDI state is highly available via Redis Enterprise replication.
- **Easy to install and operate** — self-documenting CLI for installation and day-two operations.
- **No coding needed** — create/test pipelines using Redis Insight.
- **Data-in-transit encryption** — RDI never persists data to disk; all in-flight data is protected via TLS/mTLS.
- **Observability — Metrics** — data processing counters at source table granularity plus performance metrics, available via GUI, CLI, and Prometheus endpoints.
- **Observability — logs** — rotating JSON logs in a single folder.
- **Backpressure mechanism** — RDI backs off writing data when the cache is disconnected, preventing cascading failure; catches up quickly once reconnected.
- **Recovering from full failure** — RDI can reconstruct cache data in Redis from a full snapshot of the defined dataset.
- **High throughput** — with a single processor core and ~1KB records, RDI processes ~10,000 records/second; auto-scales processing units during initial full snapshot.

### Supported source databases

Oracle (19c, 21c, 23ai LogMiner-only), MariaDB, MongoDB, MySQL, PostgreSQL, Supabase (PostgreSQL-based), SQL Server, Spanner, AlloyDB for PostgreSQL, AWS Aurora/PostgreSQL, Neon, Snowflake (preview) — with per-database version tables for direct, AWS RDS, and GCP SQL variants.

## Redis LangCache — https://redis.io/langcache/

Tagline: "Save 90% on API costs and shorten response times with intelligent, Redis-based semantic caching for AI."

### Platform section (site nav, for context on Iris's sibling products)
- Redis Iris — Real-time context for agents
- Redis LangCache — Save on tokens for common questions
- Redis Context Retriever — Leverage context from anywhere
- Redis Agent Memory — Agentic memory for consistent experiences
- Redis Data Integration — CDC across your structured data
- Redis Flex — More data, more speed, less cost

### How it works
1. **Simple deployment** — store and reuse previous LLM responses for repeated queries via a fully managed semantic caching REST API. (`/docs/latest/develop/ai/langcache/`)
2. **Fewer costly LLM calls** — chatbots get asked the same questions repeatedly; agents use 4x more tokens than chat; skip extra calls with LangCache. (`/calculator/langcache/`)
3. **More accurate results** — advanced cache management controls data access/privacy; eviction protocols and fine-tuning for embedding models. (`/demo-center/#langcache`)

LangCache checks if a similar response has already been made and returns it instantly from cache instead of calling the LLM for every request, saving time and money.

### Customer testimonial — Mangoes.ai
> Our voice app for patient care gets a lot of specific treatment questions, so it has to be absolutely accurate, and that's what LangCache does. I was worried about LLM costs for high usage, but with LangCache, we're getting a 70% cache hit rate, which saves 70% of our LLM spend. On top of that, it's 4X faster, which makes a huge difference for real-time patient interactions.
> — Amit Lamba, Founder & CEO, Mangoes.ai

### Key features
1. **The fastest response times** — benchmark-leading vector database for accurate, timely responses.
2. **A fully managed service** — REST API compatible with any language; no database management required.
3. **Embedding model selection** — use default models or bring your own vector tool.
4. **Adaptive controls** — auto-optimize settings for precision and recall with improved results over time.

Available in: CLI, Python, JavaScript.

CTAs: Try it for free (/try-free/?rcplan=langcache) | Try Redis (/try-free/?rcplan=langcache) | Talk to sales (/meeting/) | Learn how - Visit our dev hub (/dev/) | Book a meeting (/meeting/)
