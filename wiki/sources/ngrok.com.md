---
type: source
category: "MCP servers & integrations"
source_url: https://ngrok.com/
tags:
  - tunnel
  - api-gateway
  - ai-gateway
  - secure-tunnels
  - traffic-policy
  - mcp-server
  - webhook-gateway
  - developer-tools
related:
  - webhook.site
  - garrytan-gstack
product: ngrok
detail_level: standard
created: 2026-06-10
updated: 2026-06-10
---

ngrok is a globally distributed cloud networking platform that secures, transforms, and routes traffic to services running anywhere — local machines, Kubernetes clusters, IoT devices, or cloud instances — without firewall changes or open inbound ports. Originally known for developer tunnels ("share localhost with a public URL"), ngrok has evolved into an enterprise-grade unified ingress platform consolidating reverse proxy, API gateway, AI gateway, firewall, DDoS protection, and Kubernetes operator capabilities into a single system trusted by millions of developers at GitHub, Microsoft, OpenAI, Databricks, and Zoom.

_All claims below are sourced from ../../raw/web/ngrok.com.md unless otherwise noted._

## What it does

ngrok operates as a globally distributed reverse proxy that accepts traffic from its edge network and forwards it to user-managed services, regardless of where those services run. Traffic enters at ngrok's edge (with TLS termination, authentication, and policy enforcement), then travels through an encrypted tunnel to the ngrok agent running alongside the user's service. Key delivery patterns include API gateway for production services, AI gateway for LLM provider routing, webhook gateway for receiving and routing webhooks, and device/IoT gateway for remote access. Development patterns include localhost sharing, MCP server connectivity for AI providers, webhook testing, and Kubernetes ingress via the ngrok Operator.

## Key features

- **Secure Tunnels** — lightweight agent (standalone executable, no dependencies) that creates encrypted TCP/HTTP/TLS tunnels; zero open ports required; supports multi-protocol (HTTP, HTTPS, TCP, TLS), concurrent endpoints via YAML config, and native OS service installation
- **AI Gateway** — routes AI requests to OpenAI, Anthropic, Google Gemini, DeepSeek, Groq, Ollama, vLLM, and 10+ other providers with automatic failover, multi-key load balancing, cost-based routing, PII redaction, and SDK compatibility (change base URL only); Pay-as-you-go plan required
- **Traffic Policy** — CEL-based rules language for filtering, routing, and transforming traffic by any request property; built-in actions include `add-headers`, `rate-limit`, `jwt-validation`, OAuth/OIDC enforcement, IP reputation blocks, geographic blocks, and WAF protections
- **Traffic Observability** — real-time Traffic Inspector for request replay and debugging; log export to Datadog, CloudWatch, and other platforms
- **Kubernetes Operator** — native Kubernetes ingress controller; manages ngrok endpoints from cluster-native resources
- **Agent SDKs** — programmatic tunnel management in Python, Go, Node.js, and Rust; embed ngrok directly into applications without the CLI agent
- **REST API** — full resource management at `api.ngrok.com` (port 443); client libraries for Go, .NET, Ruby, Python, Java, Scala; 120 req/60s rate limit; globally unique error codes (`ERR_NGROK_*`)

## Architecture and concepts

The ngrok architecture has three layers: the ngrok edge (globally distributed PoPs that terminate TLS and enforce Traffic Policy), the ngrok agent (a standalone CLI or embedded SDK on the user's machine), and the ngrok cloud service (control plane, dashboard, APIs). The agent authenticates via an authtoken, opens a persistent connection to the edge, and receives forwarded traffic. Endpoints (HTTP, TCP, TLS, labeled) represent addressable network entities. Traffic Policy rules apply at the edge before forwarding.

The AI Gateway layer sits between AI SDK clients and upstream LLM providers. Clients point their SDK's `base_url` at the ngrok AI Gateway endpoint and authenticate with an AI Gateway API Key; the gateway validates, selects a provider+model, injects managed provider keys, handles failover, and returns the response — fully compatible with the OpenAI SDK wire format.

## Main APIs

- `ngrok.com/docs/agent/cli` — CLI reference for `ngrok http`, `ngrok tcp`, `ngrok tls`, `ngrok start`
- `ngrok.com/docs/agent/config` — YAML configuration (v2 and v3) for multi-tunnel setups
- `api.ngrok.com` — REST API; `Authorization: Bearer <api-key>`, `ngrok-version: 2` header required
- `ngrok.com/docs/traffic-policy` — Traffic Policy configuration reference; CEL expressions, actions, variables, macros
- `ngrok.com/docs/ai-gateway` — AI Gateway config schema, provider list, CEL model selection functions, SDK integration guides
- Agent SDKs: Python (`pip install ngrok`), Go (`go get golang.ngrok.com/ngrok`), Node (`npm install @ngrok/ngrok`), Rust (`cargo add ngrok`)

## When to use

Reach for ngrok when a service running anywhere (local dev, private network, edge device) needs a public, policy-enforced, observable ingress point without infrastructure changes. It is the standard choice for webhook development and testing (inspect and replay every request), for exposing local MCP servers to AI providers, for device and IoT remote access (SSH/RDP over TCP tunnels), and for Kubernetes clusters that need a managed ingress controller. The AI Gateway tier is appropriate for teams that want multi-provider LLM routing, automatic failover, and observability without managing separate gateway infrastructure. Compare with [[webhook.site]] for the inbound inspection-only use case (webhook.site does not require an agent); use ngrok when you need live bidirectional tunneling to a running service.

## Ecosystem

ngrok integrates with the MCP ecosystem (exposing local MCP servers to Claude and other AI providers), Kubernetes (ngrok Operator), Okta/Microsoft Entra ID (SSO via Traffic Policy OAuth module), Datadog/CloudWatch (log export), and major CI/CD platforms. The AI Gateway supports OpenAI SDK, Anthropic SDK, LangChain, Vercel AI SDK, and TanStack AI with no client-code changes beyond the base URL. [[garrytan-gstack]] uses ngrok's tunnel mode to expose a localhost Chromium daemon to remote coding agents via a scoped endpoint. [[webhook.site]] positions itself as an alternative to ngrok for the pure inspection use case (receiving and forwarding webhooks without running a local service).
