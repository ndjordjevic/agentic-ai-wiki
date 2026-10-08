# cloudflare.com

## Fetch log
- Inbox URL: https://www.cloudflare.com/
- Final URL: https://www.cloudflare.com/
- Fetched: 2026-10-08
- Pages: 7
- Mode: standard

## llms.txt — https://www.cloudflare.com/llms.txt
# Cloudflare

> Cloudflare is a global cloud connectivity company operating in 335+ cities worldwide. It provides a unified platform spanning developer infrastructure (serverless compute, databases, AI inference, and storage), application security (WAF, DDoS mitigation, bot management, and API Shield), Zero Trust / SASE (Access, Gateway, Browser Isolation, DLP, and Email Security), and network services (CDN, DNS, load balancing, and Magic Transit). Cloudflare powers approximately 20% of Internet traffic and protects millions of websites, applications, APIs, and enterprise networks.

This is the main Cloudflare website at cloudflare.com. For technical documentation, see developers.cloudflare.com.

## About Cloudflare

Cloudflare launched in 2010 and went public in 2019 (NYSE: NET). It operates one of the world's largest and most interconnected networks, spanning 335+ cities and 125+ countries, with interconnections to 13,000+ networks. The network operates within 50 ms of 95% of the Internet-connected world.

Cloudflare serves three primary audiences:
- **Developers** building applications on its global compute, storage, and AI platform
- **Security teams** protecting web applications, APIs, networks, and users from attacks and data loss
- **Enterprise IT** replacing legacy VPN and network appliances with its Zero Trust / SASE platform (Cloudflare One)

Key facts:
- 335+ cities, 125+ countries
- 500 Tbps total network capacity
- Interconnected with 13,000+ networks
- More than 220 cities running GPUs for AI inference worldwide
- <50 ms from 95% of Internet-connected users
- Processes ~8.4 trillion DNS queries/day across 1.1.1.1 and authoritative DNS
- ~20% of web traffic flows through Cloudflare
- 42% of the Fortune 500 are paying Cloudflare customers
- Blocks an average of 234 billion cyber threats per day (Q1 2026)
- Serves over 102 million HTTP requests per second on average, 145 million at peak
- Named a Leader in Forrester Wave™ for Web Application Firewalls (2025)
- Largest DDoS attack ever mitigated: 31.4 Tbps (November 2025)
- All pages on this site are available in markdown format by appending .md to the URL

---

## Developer Platform - Compute

Workers run on V8 isolates for zero cold starts; Containers support heavier workloads. Both deploy globally across Cloudflare's network, not to specific regions. Durable Objects and supporting primitives complete the platform.

- [Workers](https://www.cloudflare.com/products/workers.md): Serverless functions with zero cold starts - deploy JS, TS, Python, or Rust to 335+ cities globally
- [Containers](https://www.cloudflare.com/products/containers.md): Run any language or Docker image globally; no Kubernetes, no regions, scales to zero
- [Durable Objects](https://www.cloudflare.com/products/durable-objects.md): Stateful serverless with built-in WebSockets and embedded SQLite; ideal for real-time and multiplayer apps
- [Sandboxes](https://www.cloudflare.com/products/sandboxes.md): Isolated secure environments for running untrusted or AI-generated code
- [Workflows](https://www.cloudflare.com/products/workflows.md): Durable multi-step execution engine with automatic retries and state persistence
- [Cloudflare Pages](https://www.cloudflare.com/products/pages.md): Build and deploy frontend sites globally
- [Workers for Platforms](https://www.cloudflare.com/products/workers-for-platforms.md): Multi-tenant compute - let your customers run sandboxed code on your platform
- [Workers Observability](https://www.cloudflare.com/products/workers-observability.md): First-party logs, traces, and metrics for Workers applications
- [Browser Run](https://www.cloudflare.com/products/browser-rendering.md): Headless browser automation for screenshots, scraping, PDF generation, and AI agent web access
- [Email Service](https://www.cloudflare.com/products/email-service.md): Send and receive email directly from Workers
- [Artifacts](https://www.cloudflare.com/products/artifacts.md): Git-native versioned storage - create millions of repos, fork from GitHub, give every agent its own branch

---

## Developer Platform - Storage

- [R2](https://www.cloudflare.com/products/r2.md): S3-compatible object storage with zero egress fees; ideal for training data, media, and backups
- [D1](https://www.cloudflare.com/products/d1.md): Serverless SQLite database with global read replication, time-travel backups, and Prisma/Drizzle support
- [KV](https://www.cloudflare.com/products/kv.md): Globally distributed key-value store with <5 ms hot read latency; ideal for config, feature flags, and auth tokens
- [Queues](https://www.cloudflare.com/products/queues.md): Message queue for reliable async processing between Workers
- [Hyperdrive](https://www.cloudflare.com/products/hyperdrive.md): Accelerates queries to existing PostgreSQL/MySQL databases from the edge by pooling and caching connections globally
- [Basin](https://www.cloudflare.com/products/data-platform.md): Serverless analytics platform on R2 using Apache Iceberg; ingest via Basin Pipelines and query with Basin SQL, Snowflake, or DuckDB
- [Cache Reserve](https://www.cloudflare.com/products/cache-reserve.md): Persistent CDN caching backed by R2 to reduce origin load for long-tail content

---

## Developer Platform - AI

Cloudflare's AI platform lets developers run inference, build agents, store vectors, and observe model calls - all on the same global network.

- [Workers AI](https://www.cloudflare.com/products/workers-ai.md): Run 100+ AI models (Llama 3, Gemma, Whisper, FLUX, BGE) serverlessly across 220+ cities; OpenAI-compatible API
- [Agents](https://www.cloudflare.com/products/agents.md): SDK for building stateful AI agents with built-in memory, scheduling, WebSockets, and tool calling
- [AI Gateway](https://www.cloudflare.com/products/ai-gateway.md): Observability, caching, rate limiting, and model fallback for any AI provider (OpenAI, Anthropic, etc.)
- [Vectorize](https://www.cloudflare.com/products/vectorize.md): Globally replicated vector database for RAG; pairs natively with Workers AI
- [AI Search](https://www.cloudflare.com/products/ai-search.md): Managed RAG with automatic indexing for AI-powered search and chat
- [AI Security for Apps](https://www.cloudflare.com/products/ai-security-for-apps.md): Protect AI-powered applications and model endpoints from prompt injection and abuse

---

## Developer Platform - Media

- [Images](https://www.cloudflare.com/products/images.md): Resize, optimize, and deliver images globally from a single upload
- [Stream](https://www.cloudflare.com/products/stream.md): End-to-end video streaming - upload, encode, store, and deliver
- [RealtimeKit](https://www.cloudflare.com/products/realtime.md): WebRTC-based live communications platform
- [TURN / SFU](https://www.cloudflare.com/products/turn-sfu.md): Real-time media relay infrastructure (TURN server and Selective Forwarding Unit)

---

## Application Security

Cloudflare's application security products protect websites, APIs, and applications from attacks. Named a Leader in the Forrester Wave™ for Web Application Firewalls (2025). All protections are deployed at Cloudflare's edge - no appliances, no latency penalty.

- [WAF](https://www.cloudflare.com/products/waf.md): Web Application Firewall with OWASP Top 10 protection, zero-day CVE rules, and low false-positive managed rulesets
- [DDoS Protection](https://www.cloudflare.com/products/ddos.md): Always-on, unmetered L3/L4/L7 DDoS mitigation; mitigates most attacks in under 3 seconds; largest attack mitigated was 31.4 Tbps
- [Bot Management](https://www.cloudflare.com/products/bot-management.md): ML-based bot detection and mitigation; scores every request in <1 ms and blocks credential stuffing, scraping, and inventory hoarding
- [Turnstile](https://www.cloudflare.com/products/turnstile.md): Privacy-preserving, user-friendly CAPTCHA replacement - free for all Cloudflare customers
- [API Shield](https://www.cloudflare.com/products/api-shield.md): API security with schema validation, mTLS, and endpoint discovery; protects REST and GraphQL traffic
- [Rate Limiting](https://www.cloudflare.com/products/rate-limiting.md): Granular per-path, per-IP, per-header request throttling; blocks brute force and API abuse at the edge
- [Page Shield](https://www.cloudflare.com/products/page-shield.md): Client-side protection against Magecart-style supply chain attacks and malicious JavaScript
- [SSL](https://www.cloudflare.com/products/ssl.md): Free, auto-renewed SSL/TLS certificates with support for custom certificates and Keyless SSL
- [Advanced Certificate Manager](https://www.cloudflare.com/products/advanced-certificate-manager.md): Automated certificate lifecycle management for custom and wildcard certificates
- [Keyless SSL](https://www.cloudflare.com/products/keyless-ssl.md): TLS termination at Cloudflare's edge without ever exposing your private key
- [Spectrum](https://www.cloudflare.com/products/spectrum.md): DDoS protection and proxying for any TCP/UDP application (not just HTTP)
- [Spectrum for Minecraft](https://www.cloudflare.com/products/spectrum-for-minecraft.md): DDoS protection specifically for Minecraft game servers
- [Waiting Room](https://www.cloudflare.com/products/waiting-room.md): Virtual queue to protect origins during traffic spikes - users see a branded waiting page
- [Zaraz](https://www.cloudflare.com/products/zaraz.md): Server-side third-party tag and script manager; loads analytics and marketing tools without client-side risk

---

## Zero Trust / SASE (Cloudflare One)

Cloudflare One is Cloudflare's Zero Trust network access and SASE platform, replacing legacy VPN with identity-aware, device-aware security controls for users, applications, networks, and data. It unifies ZTNA, SWG, CASB, RBI, DLP, email security, and network firewall into a single control plane.

- [Access](https://www.cloudflare.com/products/access.md): Zero Trust Network Access (ZTNA) - replace VPN with identity + device posture checks for every application
- [Gateway](https://www.cloudflare.com/products/gateway.md): Secure Web Gateway (SWG) with DNS filtering, HTTP inspection, and policy-based internet access controls
- [Browser Isolation](https://www.cloudflare.com/products/browser-isolation.md): Remote Browser Isolation (RBI) - execute web pages in Cloudflare's cloud, not on the user's device
- [Data Loss Prevention](https://www.cloudflare.com/products/dlp.md): Inspect traffic for sensitive data patterns (PII, credentials, secrets) and block exfiltration
- [CASB](https://www.cloudflare.com/sase/products/casb.md): Cloud Access Security Broker - API-driven scanning of SaaS apps for misconfigurations, unauthorized user activity, shadow IT, and data security issues
- [Email Security](https://www.cloudflare.com/products/email-security.md): AI-driven inbound email protection against phishing, BEC, and malware; integrates with M365 and Google Workspace
- [Magic Transit](https://www.cloudflare.com/products/magic-transit.md): Network-layer DDoS protection and traffic acceleration for enterprise IP prefixes via BGP anycast
- [Magic WAN](https://www.cloudflare.com/products/wan.md): Replace MPLS and SD-WAN with Cloudflare's global network as the enterprise WAN backbone
- [Network Firewall](https://www.cloudflare.com/products/network-firewall.md): Cloud-native stateful firewall for enterprise WAN traffic; replaces hardware firewall appliances
- [Mesh](https://www.cloudflare.com/products/mesh.md): Private, encrypted networking between AI agents and services
- [RDP](https://www.cloudflare.com/products/rdp.md): Secure browser-based Remote Desktop access without exposing RDP ports to the internet

---

## Network & Performance

- [CDN](https://www.cloudflare.com/products/cdn.md): Global content delivery network caching static and dynamic content across 335+ cities; zero-configuration setup
- [DNS](https://www.cloudflare.com/products/dns.md): World's fastest authoritative DNS, consistently ranked #1 by DNSPerf; free, fully API-managed, DNSSEC supported
- [Load Balancing](https://www.cloudflare.com/products/load-balancing.md): Global load balancing with sub-second health checks and automatic failover across origins
- [Argo Smart Routing](https://www.cloudflare.com/products/argo-smart-routing.md): Congestion-aware routing that reduces median latency by ~30% over standard BGP paths
- [Network Interconnect](https://www.cloudflare.com/products/network-interconnect.md): Direct physical or partner-delivered private interconnections into Cloudflare's network
- [Network Flow](https://www.cloudflare.com/products/network-flow.md): NetFlow/sFlow analytics for enterprise network traffic visibility
- [Log Explorer](https://www.cloudflare.com/products/log-explorer.md): Query and explore Cloudflare logs directly in the dashboard for security forensics and observability
- [Analytics](https://www.cloudflare.com/products/analytics.md): Web performance and security analytics across all Cloudflare products
- [China Network](https://www.cloudflare.com/products/china-network.md): Cloudflare's data center presence inside mainland China via a licensed partner network
- [Email Routing](https://www.cloudflare.com/products/email-routing.md): Route custom domain email addresses to any destination inbox - free
- [Automatic Platform Optimization](https://www.cloudflare.com/products/automatic-platform-optimization.md): WordPress-specific performance optimization using edge caching and smart routing
- [Website Optimization](https://www.cloudflare.com/products/website-optimization.md): Application delivery optimizations including minification, image compression, and HTTP/3
- [Custom Domain Protection](https://www.cloudflare.com/products/custom-domain-protection.md): Registrar-level domain security to prevent hijacking and unauthorized transfers
- [Web3](https://www.cloudflare.com/products/web3.md): IPFS and Ethereum gateway infrastructure for decentralized application delivery

---

## Solutions

- [AI](https://www.cloudflare.com/solutions/ai.md): Build and deploy AI agents and applications - inference, RAG, agents, MCP servers, and AI security on one platform
- [Security](https://www.cloudflare.com/solutions/security.md): Unified WAF, DDoS, bot management, Zero Trust, and API security - ship fearlessly on the open Internet
- [Network](https://www.cloudflare.com/solutions/network.md): Global anycast network delivering <50 ms latency to 95% of users with Argo smart routing and built-in resilience
- [Platforms](https://www.cloudflare.com/solutions/platforms.md): Build secure multi-tenant SaaS platforms - give customers isolated compute, storage, and custom domains
- [Frontends](https://www.cloudflare.com/solutions/frontends.md): Deploy React, Vue, Next.js and other frontend frameworks globally with CI/CD and edge functions built in
- [Workflows](https://www.cloudflare.com/solutions/workflows.md): Orchestrate multi-step, long-running processes with durable execution and automatic retries
- [Financial Services](https://www.cloudflare.com/solutions/financial-services.md): Security, performance, and compliance for financial institutions
- [Healthcare](https://www.cloudflare.com/solutions/healthcare.md): Protect patient data and ensure compliance for healthcare organizations
- [Public Sector](https://www.cloudflare.com/solutions/public-sector.md): Secure and accelerate government and public sector applications
- [Retail](https://www.cloudflare.com/solutions/retail.md): Protect and accelerate retail and e-commerce applications

---

## Pricing

- [Pricing hub and Compute & Storage](https://www.cloudflare.com/plans.md): Usage-based pricing for Workers, storage, AI, media, observability, and other developer platform services
- [Network & CDN pricing](https://www.cloudflare.com/plans/network-cdn.md): Free, Pro, Business, and Contract domain plans, feature comparisons, and paid add-ons
- [SASE / Zero Trust pricing](https://www.cloudflare.com/plans/sase-zero-trust.md): Free, pay-as-you-go, and Contract seat-based plans and feature comparisons

---

## Other Pages

- [Privacy Policy](https://www.cloudflare.com/policies/privacy.md): Privacy policy
- [Terms of Service](https://www.cloudflare.com/policies/terms.md): Terms of service

---

## External Resources

- [Developer Documentation](https://developers.cloudflare.com/): Full technical documentation for all products
- [Cloudflare Dashboard](https://dash.cloudflare.com): Manage your Cloudflare account
- [Cloudflare Status](https://www.cloudflarestatus.com): Real-time network and product status
- [Community Discord](https://discord.cloudflare.com): Developer community support
- [GitHub](https://github.com/cloudflare): Open source projects including workerd, wrangler, and workers-sdk
- [Cloudflare Blog](https://blog.cloudflare.com): Product announcements, technical deep-dives, and Internet trend reports
- [Cloudflare Radar](https://radar.cloudflare.com): Real-time Internet traffic insights and threat intelligence

## Optional

- [Full Context Version](https://www.cloudflare.com/llms-full.txt): Expanded version with all product content inline for larger context windows

## Landing page — https://www.cloudflare.com/

---
title: "Cloudflare - Global Serverless Platform"
description: "Deploy serverless code instantly across the globe with zero cold starts, infinite scalability, and integrated storage, AI, and network services."
url: "https://www.cloudflare.com"
---

# Cloudflare

> Deploy serverless code instantly across the globe with zero cold starts, infinite scalability, and integrated storage, AI, and network services.

## What is Cloudflare Workers?

Cloudflare Workers is a serverless platform that runs your code on Cloudflare's global network of 330+ data centers. Unlike traditional serverless platforms that use containers, Workers uses V8 isolates for instant startup times with no cold starts.

## Key Features

- **Zero Cold Starts**: Code starts executing immediately using V8 isolates
- **Global by Default**: Deploy once, run in 330+ cities worldwide
- **Multiple Languages**: JavaScript, TypeScript, Python, Rust, and WASM
- **Integrated Platform**: Storage (R2, D1, KV), AI (Workers AI), and network services built-in
- **Pay for What You Use**: CPU-time based billing, not wall-clock time

## Products

### Compute
- [Workers](/products/workers.md): Global serverless functions
- [Containers](/products/containers.md): Any language, anywhere
- [Durable Objects](/products/durable-objects.md): Stateful compute
- [Browser Rendering](/products/browser-rendering.md): Automated browsers
- [Workflows](/products/workflows.md): Process orchestration

### Storage
- [R2](/products/r2.md): Egress-free object storage
- [Hyperdrive](/products/hyperdrive.md): Global database acceleration
- [D1](/products/d1.md): Serverless SQL
- [KV](/products/kv.md): Key-value storage
- [Queues](/products/queues.md): Message processing

### AI
- [Workers AI](/products/workers-ai.md): Edge AI models
- [AI Gateway](/products/ai-gateway.md): AI observability
- [Vectorize](/products/vectorize.md): Vector database
- [AI Search](/products/ai-search.md): Instant retrieval

### Media
- [Images](/products/images.md): Image optimization
- [Stream](/products/stream.md): Video streaming
- [RealtimeKit](/products/realtime.md): Live communications

### Network
- [DNS](/products/dns.md): Fast DNS
- [CDN](/products/cdn.md): Content delivery
- [WAF](/products/waf.md): Application protection
- [Load Balancing](/products/load-balancing.md): Zero downtime
- [Rate Limiting](/products/rate-limiting.md): Abuse prevention
- [Bot Mitigation](/products/bot-mitigation.md): Block bots

## Getting Started

1. Sign up at [dash.cloudflare.com](https://dash.cloudflare.com/sign-up)
2. Install the CLI: `npm install -g wrangler`
3. Create a project: `wrangler init my-worker`
4. Deploy: `wrangler deploy`

## Resources

- [Documentation](https://developers.cloudflare.com/workers/): Full technical docs
- [Pricing](/plans.md): See what it costs
- [Discord](https://discord.cloudflare.com): Community support

---

*This is a markdown version of [https://www.cloudflare.com](https://www.cloudflare.com) for AI/LLM consumption.*

## Docs — https://developers.cloudflare.com/

---
description: Connect, protect, and build everywhere.
title: Cloudflare Developer Docs
image: https://developers.cloudflare.com/og-docs.png
---

# Cloudflare Developer Docs

Explore guides and tutorials to start building on Cloudflare's platform.

## Powerful primitives, seamlessly integrated

### Deploy with one command
Build and deploy serverless functions and full-stack apps on Cloudflare's global network. No servers to manage. No cold starts or region complexity.
`npm create cloudflare@latest my-app`
[Create your first Worker](https://developers.cloudflare.com/workers/get-started/guide/)
[Workers](https://developers.cloudflare.com/workers/)· [Containers](https://developers.cloudflare.com/containers/)· [Durable Objects](https://developers.cloudflare.com/durable-objects/)· [Queues](https://developers.cloudflare.com/queues/)· [Flagship](https://developers.cloudflare.com/flagship/)

### The AI inference platform
Run AI inference globally with one API call, build agents, and search across your data — no GPUs to manage, no capacity planning.
`npx wrangler ai models` / `cf ai run @cf/meta/llama-3.1-8b-instruct --help`
[Browse available models](https://developers.cloudflare.com/workers-ai/models/)
[Workers AI](https://developers.cloudflare.com/workers-ai/)· [AI Gateway](https://developers.cloudflare.com/ai-gateway/)· [AI Search](https://developers.cloudflare.com/ai-search/)· [Agents](https://developers.cloudflare.com/agents/)· [Vectorize](https://developers.cloudflare.com/vectorize/)· [Browser Run](https://developers.cloudflare.com/browser-run/)

### Make your database feel instant, everywhere
Serverless SQL, globally distributed key-value, and global database acceleration — query directly from Workers with no connection management.
`npx wrangler d1 create my-database` / `cf d1 --help`
[Get started with D1](https://developers.cloudflare.com/d1/get-started/)
[R2](https://developers.cloudflare.com/r2/)· [Basin](https://developers.cloudflare.com/basin/)· [K2](https://developers.cloudflare.com/k2/)· [D1](https://developers.cloudflare.com/d1/)· [KV](https://developers.cloudflare.com/kv/)· [Hyperdrive](https://developers.cloudflare.com/hyperdrive/)

### Build media pipelines without infrastructure headaches
Cloudflare Images helps teams build scalable, reliable media pipelines to store, optimize, and deliver images.
`curl --request POST https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/images/v1`
[Get started with Images](https://developers.cloudflare.com/images/get-started/introduction/)
[Images](https://developers.cloudflare.com/images/)· [Stream](https://developers.cloudflare.com/stream/)· [Realtime](https://developers.cloudflare.com/realtime/)

## Build with your favorite AI agent
Paste into any AI coding agent to install Cloudflare agent tooling. [All agents](https://developers.cloudflare.com/agent-setup/)

## Fundamentals — https://developers.cloudflare.com/fundamentals/

---
description: Understand core Cloudflare concepts, set up your account, manage domains, and configure essential platform settings.
title: Cloudflare Fundamentals
---

# Cloudflare Fundamentals

Cloudflare is one of the world's largest connectivity cloud networks. Today, anyone with an Internet presence can have faster and more secure websites and applications thanks to Cloudflare. This includes bloggers, businesses, and even non-profits.

Millions of Internet properties are on Cloudflare, and our network is growing by tens of thousands each day. Cloudflare powers Internet requests for millions of websites and serves 55 million HTTP requests per second on average.

Before you get started, we recommend reviewing [Concepts](https://developers.cloudflare.com/fundamentals/concepts/) to learn about key concepts related to using different Cloudflare products.

## Additional resources
- [Cloudflare blog](https://blog.cloudflare.com)
- [Cloudflare's Go library](https://github.com/cloudflare/cloudflare-go)
- [Cloudflare system status](https://www.cloudflarestatus.com/)
- [Cloudflare Radar](https://radar.cloudflare.com)
- [Cloudflare TV](https://cloudflare.tv/schedule)
- [Terraform](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs)

## Workers AI — https://developers.cloudflare.com/workers-ai/

---
description: Run machine learning models, powered by serverless GPUs, on Cloudflare's global network.
title: Cloudflare Workers AI
---

# Cloudflare Workers AI

Run machine learning models, powered by serverless GPUs, on Cloudflare's global network. Available on Free and Paid plans.

Workers AI allows you to run AI models in a serverless way, without having to worry about scaling, maintaining, or paying for unused infrastructure. You can invoke models running on GPUs on Cloudflare's network from your own code — from Workers, Pages, or anywhere via the Cloudflare API.

Workers AI gives you access to:
- 50+ open-source models, available as a part of our model catalog
- Serverless, pay-for-what-you-use pricing model
- All as part of a fully-featured developer platform, including AI Gateway, Vectorize, Workers and more

Workers AI is now Generally Available.

## Related products
- [AI Gateway](https://developers.cloudflare.com/ai-gateway/): Observe and control your AI applications with caching, rate limiting, request retries, model fallback, and more.
- [Vectorize](https://developers.cloudflare.com/vectorize/): Cloudflare's vector database for semantic search, recommendations, anomaly detection, or providing context/memory to an LLM.
- [Workers](https://developers.cloudflare.com/workers/): Build serverless applications and deploy instantly across the globe.
- [Pages](https://developers.cloudflare.com/pages/): Create full-stack applications instantly deployed to the Cloudflare global network.
- [R2](https://developers.cloudflare.com/r2/): Unstructured data storage without egress bandwidth fees.
- [D1](https://developers.cloudflare.com/d1/): Serverless SQL databases to query from Workers and Pages.
- [Durable Objects](https://developers.cloudflare.com/durable-objects/): Globally distributed coordination API with strongly consistent storage.
- [KV](https://developers.cloudflare.com/kv/): Global, low-latency, key-value data storage.

## More resources
- [Get started](https://developers.cloudflare.com/workers-ai/get-started/workers-wrangler/): Build and deploy your first Workers AI application.
- [Plans](https://developers.cloudflare.com/workers-ai/platform/pricing/): Free and Paid plans.
- [Limits](https://developers.cloudflare.com/workers-ai/platform/limits/)
- [Use cases](https://developers.cloudflare.com/use-cases/ai/)

## WAF — https://developers.cloudflare.com/waf/

---
description: The Cloudflare Web Application Firewall (WAF) provides automatic protection from vulnerabilities and the flexibility to create custom rules.
title: Cloudflare Web Application Firewall
---

# Cloudflare Web Application Firewall

Get automatic protection from vulnerabilities and the flexibility to create custom rules. Available on all plans.

The Cloudflare Web Application Firewall (Cloudflare WAF) checks incoming web and API requests and filters undesired traffic based on sets of rules called rulesets. The WAF uses the Rules language, a flexible expression syntax that lets you filter traffic by request properties such as IP address, URL path, headers, and body content.

## Features
- Application Profiles — compare requests with an application-specific expected structure
- Custom rules — protect websites/APIs from malicious traffic, including WAF attack score and malicious uploads detection
- Rate limiting rules — define rate limits and actions when reached
- Managed rules — pre-configured, regularly updated rulesets for zero-day vulnerability protection
- Account-level configuration (Enterprise only) — deploy rulesets to multiple Enterprise zones
- Security Events — review mitigated requests using sampled logs
- Security Analytics — information about all incoming HTTP requests, including unaffected ones

## Availability (summary)
Attack score, Leaked credentials detection, Malicious uploads detection, and AI Security for Apps scale from Free (limited/none) up through Enterprise (full/paid add-on). Custom rules, rate limiting rules (one rule on Free), WAF Managed Rules (Free Managed Ruleset only on Free), custom lists, Email Address Obfuscation, Hotlink Protection, IP Access rules, User Agent Blocking, and Zone Lockdown are available on all plans. Security Analytics (account-level) and Security Events alerts require Business/Enterprise.

## Related products
- [DDoS Protection](https://developers.cloudflare.com/ddos-protection/): Secures websites, applications, and networks while preserving legitimate traffic performance.
- [Client-side security](https://developers.cloudflare.com/client-side-security/): Formerly Page Shield — protects website visitors' browser environment.
- [Bots](https://developers.cloudflare.com/bots/): Identify and mitigate automated traffic to protect domains from bad bots.
