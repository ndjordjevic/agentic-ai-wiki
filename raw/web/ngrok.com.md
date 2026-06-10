# ngrok.com

## Fetch log
- Inbox URL: https://ngrok.com/
- Final URL: https://ngrok.com/
- Fetched: 2026-06-10
- Pages: 8
- Mode: standard

## llms.txt — https://ngrok.com/llms.txt
# ngrok

> Canonical entrypoint for AI assistants and automated agents using ngrok.com.

## Priority resources

- [Docs](https://ngrok.com/docs): Product documentation and reference.
- [Docs llms.txt](https://ngrok.com/docs/llms.txt): AI-oriented index for documentation content.
- [Docs sitemap](https://ngrok.com/docs/sitemap.xml): Complete index of docs URLs.
- [Pricing (markdown)](https://ngrok.com/pricing.md): Machine-readable pricing, plans, limits, and overage rates. Dollar amounts are served live from the billing service.
- [Blog](https://ngrok.com/blog): Product updates, guides, and engineering posts.
- [Blog sitemap](https://ngrok.com/blog/sitemap.xml): Complete index of blog URLs.
- [Blog RSS](https://ngrok.com/blog/rss.xml): Blog feed for recent posts.

## Site index

- [Sitemap index](https://ngrok.com/sitemap.xml): Main sitemap that includes site, docs, and blog indexes.

## Landing page — https://ngrok.com/

ngrok is an all-in-one cloud networking platform that "secures, transforms, and routes your traffic to services running anywhere."

**Main Products:**
- Universal Gateway
- Secure Tunnels
- AI Gateway
- Traffic Observability
- Traffic Policy
- Kubernetes Operator

**Key Use Cases:**

*Delivery:* API gateway, AI Gateway, webhook gateway, ephemeral workloads

*Development:* Share localhost, connect MCPs to AI providers, test webhooks, access remote Kubernetes clusters

*Connectivity:* Site-to-site connectivity, device gateway, remote access (SSH/RDP)

**Core Features:**

Traffic Policy operates as a CEL-based rules system allowing teams to "Route by any request property," enforce OAuth, block by IP reputation and geography, and apply rate limits and WAF protections.

Secure Tunnels enable services to connect through encrypted channels without opening inbound ports, providing "Zero Open Ports" and "Least Privileged Access."

Developer Experience includes Traffic Inspector for real-time request inspection, log export to platforms like Datadog and CloudWatch, and Kubernetes Operator support.

**Adoption:**
The platform serves "millions of developers routing billions of requests every day" and is trusted by companies including GitHub, Microsoft, OpenAI, Databricks, and Zoom.

## Docs — https://ngrok.com/docs

ngrok is described as "an all-in-one cloud networking platform that secures, transforms, and routes your traffic to services running anywhere."

**Core Solutions:**
1. Share localhost — Deploy local applications to public URLs via CLI
2. API Gateway — Manage production APIs with Traffic Policy security
3. AI Gateway — Route and secure traffic to AI models
4. Device Gateway — Enable remote IoT device access
5. Site-to-Site Connectivity — Access APIs and databases across networks
6. Kubernetes Ingress — Use ngrok Operator for K8s cluster ingress

**Additional Capabilities:**
Webhook handling, preview URL security, SSH/RDP access, remote Kubernetes connectivity, MCP server integration, and HTTP request replay functionality.

**Resources for Implementation:**
- Universal Gateway Examples for API, database, and webhook gateway patterns
- Traffic Policy Examples for routing, authentication, and request modification
- Guides covering site-to-site connectivity, gaming servers, and IoT management

**Developer Integration:**
ngrok supports programmatic access through SDKs (Python, Go, Node, Rust) and integrates with services like Okta SSO, Microsoft Entra ID, and Datadog.

## What Is ngrok — https://ngrok.com/docs/what-is-ngrok

ngrok functions as "a globally distributed reverse proxy that secures, protects, and accelerates your applications and network services." The platform operates independently of environment constraints, routing traffic from services running anywhere—whether on AWS, Azure, Kubernetes clusters, or local machines—without requiring network configuration changes.

**Key Capabilities:**

The platform consolidates reverse proxy, load balancer, API gateway, firewall, and DDoS protection functions into one unified system. Primary use cases include:

- Production infrastructure: API gateway functionality via Traffic Policy, Kubernetes ingress support through the ngrok Operator, identity-aware proxy capabilities using OAuth/JWT/OpenID Connect, and load balancing through Endpoint Pools.
- External network access: Lightweight agents enable secure API connections within customer environments and on devices, while library imports support enhanced local development experiences.
- Development workflows: Webhook testing with request inspection, local website previews, and mobile backend testing against locally-running services.
- Remote connectivity: TCP endpoints facilitate SSH and RDP access to remote machines.

The platform's environment-independent architecture and consolidated feature set position it as an accessible ingress solution across diverse deployment scenarios.

## AI Gateway — https://ngrok.com/docs/ai-gateway

The ngrok AI Gateway enables routing of requests to AI providers like OpenAI and Anthropic with "automatic failover, load balancing, and observability."

**Key Features:**
- No Provider Account Requirements: Access OpenAI and Anthropic without individual provider signups
- Automatic Failover: "If one provider fails, the gateway automatically tries the next model, provider, or key"
- SDK Compatibility: Works with official and third-party SDKs by changing the base URL
- Self-Hosted Models: Routes to local inference servers like Ollama or vLLM

**How It Works:**
On each request, the gateway:
1. Receives your request with your AI Gateway API Key
2. Validates your key
3. Selects which model and provider to use
4. Forwards the request with ngrok's managed provider API keys
5. Retries with failover options if needed
6. Returns the response

**Supported Use Cases:**
Automatic model selection, multi-provider failover, cost-based routing, access control, content modification (PII redaction, response sanitization), and custom selection strategies using CEL expressions.

**Requirements:**
AI Gateway requires the Pay-as-you-go plan with pricing details available in the Credits section.

**Supported Providers:**
OpenAI, Anthropic, Google (Gemini), DeepSeek, Groq, Hyperbolic, InceptionLabs, Inference.net, OpenRouter, Azure OpenAI, LM Studio, Ollama, vLLM.

## Secure Tunnels (Agent Overview) — https://ngrok.com/docs/agent/overview

The ngrok agent functions as a lightweight CLI tool that "creates secure tunnels from ngrok's global network to your local services, devices, and applications." This enables exposure of firewalled services and facilitates remote device connections across multiple protocols.

**Core Technical Capabilities:**
- Multi-protocol support: HTTP, HTTPS, TCP, and TLS endpoints for diverse applications
- Zero dependencies: Runs as a standalone executable across major operating systems
- Concurrent operations: Multiple simultaneous endpoints managed via configuration files or CLI
- Service installation: Native OS integration with automatic startup and crash recovery

**Essential Concepts:**
1. Agent CLI — Command-line interface for endpoint management and API interaction
2. Configuration File — YAML-based setup for complex multi-tunnel deployments
3. Authtokens — Account-scoped authentication credentials
4. TLS Termination — End-to-end encryption at the agent level
5. SSH Reverse Tunnel — Public key authentication for secure connections

**Practical Applications:**
Agent-assisted gateways for AI development, secure developer environments with individual public URLs, webhook validation gateways, and centralized API gateway infrastructure.

## Traffic Policy — https://ngrok.com/docs/traffic-policy

ngrok's Traffic Policy is "a configuration language that offers you the flexibility to filter, match, manage, and orchestrate traffic to your endpoints."

**Core Capabilities:**
1. Actions — Tools like `add-headers`, `rate-limit`, and `jwt-validation` for traffic transformation and management
2. Variables — Predefined values such as IP addresses and endpoint URLs for dynamic traffic handling
3. Macros — Mechanisms to refine traffic segmentation through rule conditions

**Primary Use Cases:**
- Blocking unwanted traffic (malicious actors, bots, specific IPs)
- Implementing authentication (JWT, OAuth, OIDC, basic auth)
- Rate limiting by endpoint, IP, or API key
- URL rewriting for backend routing

## API — https://ngrok.com/docs/api

The ngrok API provides programmatic access to ngrok resources via REST at `https://api.ngrok.com` on port 443 only.

**Authentication:**
API key passed as a bearer token in the `Authorization` header; requests also need an `ngrok-version: 2` header.

**Access Methods:**
curl, HTTP libraries, native client libraries, ngrok Agent CLI, or Terraform Provider.

**Client Libraries:**
Go, .NET, Ruby, Python, Java, and Scala (across the ngrok GitHub organization).

**Key Details:**
- All requests use `application/json` content type
- API guarantees no breaking changes unless version upgrades are explicit
- Pagination via `limit` and `before_id` query parameters (max 100 results)
- Rate Limits: 120 requests per 60-second rolling window; exceeding returns HTTP 429 with error code `ERR_NGROK_226`
- Error responses include globally unique error codes (e.g., `ERR_NGROK_218`)
- IP Restrictions: Configurable via dashboard or API (type: `api`) to limit CIDR block access
- CORS Support: Enabled for browser-based requests with 10-minute preflight caching
- Pricing: Available at no additional charge to all users; costs apply only to provisioned resources
