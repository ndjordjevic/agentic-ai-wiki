# superdesigndev/treg

## Metadata
- Stars: 6825
- Primary language: Python
- Default branch: main
- Latest release: (none listed)
- License: Apache 2.0 with additional terms (hosted-service restriction)
- Homepage: https://treg.to
- Version (pyproject): 0.28.0
- Package name: tools-registry
- Forks: 592
- Pushed at: 2026-10-31T16:40:49Z
- Fetched: 2026-10-31
- Final URL: https://github.com/superdesigndev/treg

## Description
OpenRouter for agent tools. Join community here: https://discord.gg/6mQYYfFMAn

## README
# Treg (OpenRouter for Tools)

![treg — the tool catalog for your agent](docs/assets/treg-hero.png)

**OpenRouter, but for agent tools instead of models.** Point an agent at one base URL with one token
and it can do the job: **a curated catalog of thousands of endpoints across many providers** — SEO and backlinks,
social and trends, people and company enrichment, ads, scraping, image and video generation —
**priced per call, from a cent**,
with no provider signup. Plus your own team's keys, skills and CLIs, callable by every teammate's
agent without the credential ever leaving the server.

**Ask for the task, not the tool.** You do not need to know which vendor sells backlink data, or to
hold an account with them. Search for what you want to do, read the price, call it.

Built for the Superdesign team, live at [treg.to](https://treg.to) — anyone can self-host.

## Why it exists

The tools an agent needs for real work sit behind subscriptions nobody buys for a single run —
Semrush $139/mo, Moz $99/mo, Crunchbase $99/mo, Apollo $59/seat — behind signup walls, or behind no
public API at all (invite-only, partner-only, app-review-only). treg carries those accounts and
bills fractions of a cent per call.

## Two kinds of tool, one token

- **The catalog** — external endpoints treg can serve with its own key or through a verified public
  route that needs no provider key. Own-key calls use the team's prepaid balance; anonymous calls
  are free. No account with the provider is needed. New verified accounts receive **$1.00 free**
  once, when they create an eligible team.
- **Your own tools** — anything a teammate registered: a paid API account, an OAuth connection, a
  vendor CLI, a `SKILL.md`. **Your own key always wins over treg's, and those calls are never
  metered.**

The vocabulary for the second half:

- **tool** = something the registry calls for you with the org's credential. Two kinds:
  - **endpoint** — an upstream `base_url` + credential **bindings** (each binding injects one
  secret into the request; a request can carry several, e.g. an OAuth bearer *and* a
  `developer-token` header).
  - **CLI** — a vendor binary (`stripe`, `gh`, `vercel`, ...) run with the credential injected.
- **skill / bundle** = a recipe (`SKILL.md`) + its secrets + its tool(s), registered together.

**The one rule:** the proxy **relays, never models** the upstream, and **injects auth server-side**
— so it survives upstream API changes and callers never hold keys.

---

# Part 1 · Using the registry

Visit [**treg.to**](https://treg.to) (hosted on Render) — the dashboard,
sign-in, and every URL below live there.

## Quickstart

Same flow as the dashboard's **Getting started** guide:

```bash
# 1. install the CLI — also points it at the registry
curl -fsSL https://treg.to/install.sh | sh

# 2. sign in (GitHub default · --email for a one-time code · --token for agents/CI)
treg login

# 3. do something useful immediately — no key, nothing registered
treg catalog search "backlinks for a domain"     # find a tool by what it DOES
treg call tikhub.tiktok.user.profile --query uniqueId=tiktok
treg balance                                     # exactly what that cost

# (or `treg onboard` for the guided walkthrough)
```

Fish Audio provides S2.1 Pro speech, public-voice discovery, and private voice cloning.
Speech is binary stdout, so redirect it to a file. A discovered voice's `_id` or a team voice id is
the TTS `reference_id`; voices created on treg's Fish account are durable team resources:

```bash
treg call fishaudio.tts.s2-1-pro --method POST --header model=s2.1-pro \
  --data '{"text":"Hello from treg","format":"mp3"}' > speech.mp3
treg call fishaudio.voices.discover --query self=false --query licensed=false --query language=en
treg resources list --provider fishaudio --kind voice
```

With your own Fish key, requests remain an unrestricted, unmetered upstream relay and Fish owns the
account boundary.

Catalog tool inputs are described by `treg catalog get <id>`. Tools marked `strict_query` reject undeclared or repeated query parameters, unsupported values and request bodies.

Your token identifies you on every call (`X-Treg-Token` header) and is the same for all tools.
Discover what your team has shared: `treg tool ls` · check credential health: `treg health`.

### Or install it as a Claude Code plugin

```
/plugin marketplace add superdesigndev/treg
/plugin install treg@treg
```

Installs the treg skill and treg's tools with no token and no configuration. Run `/mcp`, pick
treg and sign in; the tools appear after it. Other agents: `npx skills add superdesigndev/treg -s treg`
(or see [Workflow skills](#workflow-skills) for the rest).
See [docs/CLAUDE-PLUGIN.md](docs/CLAUDE-PLUGIN.md). MiniMax Code / MiniMax Agent users: the same
skill ships via the MiniMax Plugin Marketplace ([docs/MINIMAX-PLUGIN.md](docs/MINIMAX-PLUGIN.md)).

### Workflow skills

Ready-made recipes your agent runs end to end, every call through treg:

| Skill | What your agent can do |
|---|---|
| [`treg`](skills/treg/SKILL.md) | Find and call any tool in the catalog, plus your own tools |
| [`web-access`](skills/web-access/SKILL.md) | Read the live web without local scrapers: free search and page reads first, then the right platform job for social, stores, reviews, maps and papers, with treg falling back to the next vendor when one fails |
| [`lead-signals`](skills/lead-signals/SKILL.md) | Find in-market buyers from public signals (complaints, job changes, hiring, funding, tool adoption) and monitor a topic, competitor or account list for them ([treg.to/leads-signals](https://treg.to/leads-signals)) |
| [`recruit`](skills/recruit/SKILL.md) | Turn a LinkedIn job post into a ranked shortlist: criteria from the post, people search, filters with reasons, one line on why each fits, cited evidence (posts, GitHub, talks, tenure, job change) under a per-candidate spend cap, then a checked personal email and phone, with a run file of counts, evidence and the vendor trail per candidate |
| [`make-ugc`](skills/make-ugc/SKILL.md) | Make AI UGC videos: trending hooks, a presenter, talking-head clips, captions ([treg.to/ugc](https://treg.to/ugc)) |
| [`jev-memory`](skills/jev-memory/SKILL.md) | Give Claude Code a memory: a Claude Code mod where Jev judges each prompt after the turn and keeps your lasting preferences, installed ready-made or built from one prompt ([the mod](examples/claude-code-mods/jev-memory)) |

`install.sh` installs all of them for you except `jev-memory`, which is opt-in. In Claude Code each one is
also its own plugin in treg's marketplace: `/plugin install recruit@treg`, or pick them from `/plugin`. To add
them to an existing agent instead ([skills.sh](https://skills.sh) CLI):

```bash
npx skills add superdesigndev/treg                        # every public skill
npx skills add superdesigndev/treg --skill lead-signals   # just one
treg skill bootstrap                                      # same set, with the treg CLI you already have
```

The workflow skills run on treg, so set it up first (the Quickstart above, or point your agent at
[treg.to/llms.txt](https://treg.to/llms.txt)).

### Claude.ai connector

The Claude Connectors Directory surface is `https://treg.to/mcp/v2/`. It exposes only curated
catalog endpoints, without image, video or audio generation, and separates read calls from write
calls so Claude receives accurate safety signals. The existing `/mcp/` surface remains available for catalog endpoints, team-owned tools,
and imported skills. See the [MCP and OAuth architecture](docs/context/architecture/mcp-oauth.md)
for the boundary and implementation, and the
[submission runbook](https://github.com/superdesigndev/treg-internal/blob/main/docs/distribution/CLAUDE-CONNECTOR-SUBMISSION.md) for release gates.

## Call a tool you don't have a key for

The catalog is grouped by what endpoints **do**: keyword and rank tracking, backlinks and authority,
AI visibility, trending and discovery, publishing to socials, people and company enrichment, ads
management and creative, measurement.

```bash
treg catalog                                    # every platform, busiest first
treg catalog search "find a work email"         # by the job, not the vendor
treg catalog search --new                       # tools added in the last 30 days, newest first
treg catalog get hunter.people.email.find       # params, PRICE, example response
treg call hunter.people.email.find --query domain=reddit.com --query full_name="Alexis Ohanian"
```

**How a catalogued call is served** — the credential ladder, in order:

1. your team registered its own tool for that provider → that tool, that key;
2. your team stored a secret for the provider → injected through a virtual tool;
3. neither, and the endpoint has a verified public route → **no provider key**, free;
4. otherwise → **treg's own key**, billed to the team's prepaid balance.

The anonymous price assumes the caller does not send a provider credential header. The faithful
relay preserves caller headers, so a caller-supplied provider key can use that key's credits.
Your own credential always beats treg's, so connecting a key you already pay for makes those calls
free of the balance rather than duplicating them. An endpoint treg has no published price for is
**refused**, not served free — you are told to connect your own key instead. Where several providers
serve one capability, `treg catalog search` shows them side by side with prices; **choosing is
yours** — treg does not silently pick or fail over between providers for you. (When treg's own
account for a provider is out it may serve the *same* endpoint through a treg-owned relay account,
disclosed on the response; a team can opt out.) The exception you opt into: `treg.<capability>` routed endpoints, where treg picks the provider for you and names it. For common jobs (scraping a page, web search, Google results, finding an email) start with the routed endpoint, such as `treg.web.extract` or `treg.web.search`, rather than a provider you remember by name. On `treg.people.email.find` and `treg.people.phone.find`, `X-Treg-Route-Verify: true` also checks the found address or number in the same call, as its own charge, and says what the check found.

```bash
treg balance          # credit left, calls in flight, recent spend
treg topup            # add funds, or set up automatic top-ups
```

Out of balance is an HTTP **402** `error: insufficient_balance` carrying `balance_micro`, `estimated_cost_micro` and a `topup_url`,
so an agent can act on it without reading prose.

**Enrich Arena** lives at `/enrich-arena`, outside the dashboard. Compare enrichment answers with each vendor’s cost and speed,
vote for the best answer in one click, or watch a sequential waterfall. Capability-compatible
async providers participate too; Arena handles submit and polling internally. Browsing is
public; submitting requires login, and billable attempts use your team's credits. See the
[Arena guide](docs/context/interface/enrich-arena.md).

**Web Arena** compares Web Search, Web Fetch, and Sitemap providers at `/web-arena`.
Battle calls selected providers for the same input; Waterfall tries them in order. The
live leaderboard combines direct provider-call hit rates and response times with checked
Web Arena quality results over a rolling 30-day window. The pages open when the feature
is enabled. See the
[Web Arena guide](docs/context/interface/web-arena.md).

## Share & use your own tools

The zero-thought path — point treg at a project and it figures out what's shareable:

```bash
treg scan     # read-only preview: the keys, skills & CLIs upload would register
treg upload   # register them (encrypted server-side); idempotent, --replace to update
```

`treg upload` scans the `.env` (matching keys against ~80 known providers), every skill
subdirectory, and installed catalog CLIs. Three kinds of things go into the registry — here's how
to share and use each:

### 1. Endpoints (HTTP APIs)

**Share** — one upstream URL callable with a stored key, or bulk from a `.env`:

```bash
treg secret add STRIPE_KEY --value sk_live_123
treg add stripe --base-url https://api.stripe.com --secret STRIPE_KEY

treg upload env --select openai,stripe,resend     # or straight from the .env
```

**Use** — the agent-native way: build the **real** upstream request and prefix it with the proxy.
treg resolves the tool by host, injects the credential, and relays everything else faithfully
(your `X-Treg-Token` is stripped before the upstream sees it):

```
Real request:   GET https://api.intercom.io/conversations?per_page=5
Through treg:   GET https://treg.to/call/https://api.intercom.io/conversations?per_page=5
                    header:  X-Treg-Token: <your token>
```

Or the CLI shorthand — and `treg calls` for the audit log:

```bash
treg call intercom conversations --query per_page=5
treg call stripe v1/balance
```

### 2. CLIs

**Share** — automatic: `treg upload` detects installed catalog CLIs (`stripe`, `gh`, `vercel`, …)
and registers them; a recipe-only catalog CLI skill (e.g. `stripe-cli`) auto-becomes runnable too.

**Use** — `treg run` executes the vendor CLI **with the org's credential injected**, so you never
hold the key or log in:

```bash
treg run stripe -- get /v1/balance
treg run gh -- pr list
```

`--local` (default) runs on your machine. Server-side CLI execution (`--server`) is disabled globally.
For a whole session, `treg shell start` opens a subshell where every registered CLI injects
automatically — just use `stripe`, `gh`, … normally; `exit` reverts. `treg runs` is the audit log.

### 3. Skills

**Share** — a skill is a whole capability (`SKILL.md` recipe + its secrets + its tool(s)),
registered together so the whole team runs the same skill, maintained in one place:

```bash
treg upload skills --dir ~/.claude/skills --all   # register a folder of skills in one pass
```

**Use** — pull any shared skill into your agent; its API calls go through treg with your token,
so the key stays on the server, never in the skill:

```bash
treg skill install seo-blog-writer      # writes into ./.claude/skills/  (--all for the library)
```

### Manual registration — when the heuristics can't figure a tool out

```bash
# multi-credential tool (e.g. google-ads: OAuth bearer + a developer-token header)
treg tool add google-ads --base-url https://googleads.googleapis.com \
  --bind "secret=<oauth-id>,injector=oauth" \
  --bind "secret=<dev-id>,name=developer-token,format={secret}"

# one skill, step by step
treg skill init --dir ./my-skill          # drafts treg.json (guesses base_url, finds secrets)
treg skill add  --dir ./my-skill          # registers recipe + secrets + tool, atomically

# OAuth via the browser (mints the first token, treg holds it and auto-refreshes)
treg oauth connect gsc --client-secret client_secret.json \
  --scopes https://www.googleapis.com/auth/webmasters.readonly
```

Full options for every command: [`USAGE.md`](USAGE.md).

The CLI sends anonymous command usage to PostHog when using treg.to (no arguments or credentials).
Disable with `TREG_TELEMETRY=0` or `DO_NOT_TRACK=1`.
See [analytics details](USAGE.md#anonymous-usage-analytics).

## Teams

An account can own up to 10 teams. Joining other teams as a member does not count toward this limit.

Everything is scoped to an **org**: a token = a `(user, org)` membership, and every secret, tool,
and skill belongs to the active org. Roles: **owner / admin / member / viewer**.

```bash
treg org create "Acme"                        # make a team, become owner
treg org invite teammate@acme.com             # invite by email (pick role + tool access)
treg org join <code> --email you@acme.com     # accept an invite (creates you if new)
treg org ls | use <slug> | members            # switch orgs, see the roster
treg org access <member> --tools a,b          # per-member tool access (admin+)
```

Team owners can enable enterprise SSO from the dashboard's **Team → SSO** tab. WorkOS connects the
company's identity provider; owners can invite their IT admin to finish setup. Employees can enter
their work email in any sign-in dialog or use the team's direct sign-in link. treg keeps its team roles and API keys. The
Directory Sync plan removes a deactivated employee's team access. See
[enterprise SSO setup](docs/enterprise-sso.md).

## Going deeper

- **Feedback:** `treg feedback submit friction "The pagination example is unclear."`
  Share problems or suggestions without private information. See [feedback instructions](https://treg.to/feedback.md).
- **Review:** `treg review CALL_ID useful`
  Rate an invited catalog call after using its result; `not_sure` is fine. Omit private data and continue the task.

- [`USAGE.md`](USAGE.md) — the full `treg` CLI reference.
- [`/llms.txt`](https://treg.to/llms.txt): the agent entry point, in the [llms.txt](https://llmstxt.org)
format: what treg is, setup for each kind of agent, the search-read-call loop and the rules, with
links to [`/skill.md`](https://treg.to/skill.md), the operating guide, for everything else.
- **The dashboard** at [treg.to](https://treg.to) — full CRUD, a guided
tutorial (Help → Tutorial), and copyable setup instructions for your agents.
- **The API** — everything the CLI does is plain HTTP; interactive OpenAPI docs live at `/docs`.
The proxy endpoint is `/call/{...}`; all endpoints take the `X-Treg-Token` header.

---

# Part 2 · Self-hosting & development

## Run it locally

One command (needs `tmux` + [`uv`](https://docs.astral.sh/uv/); it syncs the venv itself):

```bash
scripts/dev-local.sh up        # server on http://localhost:18790, dev-safe settings
```

That runs the server in tmux with hot-reload, its own sqlite DB (`treg-dev.db`), and email OTP dev
mode (sign-in codes shown on the page — no mail sender needed). Day-to-day:

```bash
scripts/dev-local.sh cli login   # sandboxed CLI: never touches your real ~/.treg/config.json
scripts/dev-local.sh logs        # server output          · status / restart / down
scripts/dev-local.sh reset       # wipe the dev DB + CLI sandbox for a fresh start
```

Or run the server directly, without tmux:

```bash
bash scripts/build-dashboard.sh # Node 22.12+ and npm; build the Dashboard
uv sync                        # create the venv from uv.lock (pulls the server deps for dev)
uv run python -m treg upgrade  # prepare schema + run idempotent release tasks without serving
uv run python -m treg          # serve on 0.0.0.0:18790 (add --reload for dev)
uv run python -m treg keygen   # print a fresh Fernet key for TREG_SECRET_KEY
```

> **Installing to run a server (not from source):** the base package is the **CLI only**. To run a
> registry, install the server extra — `pip install "tools-registry[server]"` — which adds FastAPI, the
> database drivers, and encryption. `pip install tools-registry` alone gives just the `treg` command for
> talking to an existing registry.

The official hosted service is available at `treg.to`. Its production topology and live settings are
maintained in the private [operator runbook](https://github.com/superdesigndev/treg-internal/blob/main/docs/production/deploy.md).

## Configuration

Environment variables (prefix `TREG_`, read from `.env`):


| Var                                       | Default                         | Purpose                                                                                                                                                                    |
| ----------------------------------------- | ------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `TREG_DATABASE_URL`                       | `sqlite+aiosqlite:///./treg.db` | DB URL (SQLite for dev, Postgres in prod)                                                                                                                                  |
| `TREG_READ_DATABASE_URL`                  | *(empty)*                       | Optional SQLite / PostgreSQL read datasource; empty reuses the primary. Requires callers to opt in; existing queries are unchanged. See [read datasource setup](docs/context/ops/deploy.md#optional-read-replica). |
| `TREG_SECRET_KEY`                         | *(empty)*                       | Fernet key for secrets-at-rest; empty → an ephemeral key is minted (secrets won't survive a restart)                                                                       |
| `TREG_PUBLIC_URL`                         | `https://treg.to`  | treg's public base, used to build the OAuth callback URI                                                                                                                   |
| `TREG_SESSION_SECRET`                     | *(empty)*                       | signs the dashboard session cookie; falls back to `TREG_SECRET_KEY`. Set a real value in prod                                                                              |
| `TREG_GITHUB_CLIENT_ID` / `_SECRET`       | *(empty)*                       | GitHub OAuth sign-in (callback `<public_url>/auth/github/callback`); empty hides the button                                                                                |
| `TREG_GOOGLE_CLIENT_ID` / `_SECRET`       | *(empty)*                       | Google OAuth sign-in (redirect `<public_url>/auth/google/callback`); empty hides the button                                                                                |
| `TREG_WORKOS_API_KEY` / `_CLIENT_ID` / `_WEBHOOK_SECRET` | *(empty)* | WorkOS enterprise SSO; configure callback and signed directory webhook as described in [enterprise SSO setup](docs/enterprise-sso.md) |
| `TREG_ENTERPRISE_SSO_BUNDLE_ONLY` | `true` | Show only the SSO + Directory Sync plan by default; set to `false` to offer both monthly plans. |
| `TREG_ENTERPRISE_SSO_BUNDLE_PRICE_ID` / `TREG_ENTERPRISE_SSO_ONLY_PRICE_ID` | *(empty)* | Reusable monthly Stripe Price IDs in the same account as `TREG_STRIPE_SECRET_KEY`; an unset or unusable Price hides its plan. Stripe's Price supplies the displayed amount and Checkout charge. |
| `TREG_ENTERPRISE_SSO_BUNDLE_MIN_PRICE_USD` / `TREG_ENTERPRISE_SSO_ONLY_MIN_PRICE_USD` | `0` | Optional whole-dollar minimum for each monthly Stripe Price; lower prices are hidden and rejected at Checkout. |
| `TREG_INSTAGRAM_CLIENT_ID` / `_SECRET`    | *(empty)*                       | Instagram App ID and secret for direct Instagram Login (redirect `<public_url>/oauth/callback`)                                                                           |
| `TREG_META_CLIENT_ID` / `_SECRET`         | *(empty)*                       | Meta app credentials for Facebook Pages, Meta Ads, and optional Instagram `page-tools`                                                                                     |
| `TREG_OAUTH_REVIEW_PENDING`               | `instagram-login,page-messages` | Comma-separated registry review keys whose capabilities must remain gated; hosted review state is maintained privately.                                                   |
| `TREG_RESEND_API_KEY` / `TREG_EMAIL_FROM` | *(empty)*                       | transactional email via Resend (OTP codes + invites); From must be a Resend-verified sender                                                                                |
| `TREG_BLOCKED_EMAIL_DOMAINS`              | *(empty)*                       | comma-separated email domains refused at every sign-up/sign-in door and at team creation (subdomains included, case-insensitive). Empty blocks nothing — no list ships in the code |
| `TREG_CLIENT_IP_HEADER`                   | *(empty)*                       | a header only your edge can set, used as the client address for every per-IP limit (`cf-connecting-ip` behind Cloudflare) |
| `TREG_TRUSTED_PROXY_HOPS`                 | `1`                             | without that header: the `X-Forwarded-For` entry this many hops from the RIGHT (the one your nearest proxy appended); `0` when clients connect directly. The first entry is client-written and never trusted |
| `TREG_REQUIRED_EXTENSIONS`                | *(empty)*                       | comma-separated policy extensions (`treg.extensions` entry points) that must be installed, else startup fails. treg.to runs a private abuse-policy extension this way; it can only restrict ([policy extensions](docs/context/architecture/policy-extensions.md)) |
| `TREG_TURNSTILE_SITE_KEY` / `_SECRET`     | *(empty)*                       | Cloudflare Turnstile on every email sign-in form; either empty = off. The site key is served in `/captcha.js`, the secret only reaches siteverify |
| `TREG_TURNSTILE_MODE`                     | `observe`                       | `observe` logs each outcome and changes nothing; `enforce` refuses a code to a missing or invalid token, and gives no signup credit when Cloudflare cannot answer |
| `TREG_TURNSTILE_HOSTNAMES`                | *(empty)*                       | comma-separated hosts a token must be solved on; empty = the `TREG_PUBLIC_URL` host (and its known aliases) |
| `TREG_ADMIN_TOKEN`                        | *(empty)*                       | cross-tenant **super-admin** bearer; authorizes every `/admin/*` endpoint. Empty disables the env path (only `is_superadmin` users reach `/admin`). Keep it long + secret. |
| `TREG_EMAIL_DEV_MODE`                     | `false`                         | when true, `/auth/email/start` returns the OTP in its response (no mail sender needed) — **dev/local only**, never in prod.                                                |
| `TREG_KV_URL`                             | *(empty)*                       | shared key-value store (Redis protocol) for counters every worker must agree on, today the per-team review-invitation budget. Empty = an in-process fallback, fine for one worker |


No `.env` is needed for local dev — every setting has a working default (ephemeral key, sqlite).

> **⚠️ Back these up before moving or redeploying:** the Fernet key (`TREG_SECRET_KEY`) and the
> database (Postgres in prod; `treg.db` for a local sqlite run). Lose the Fernet key and every
> stored secret becomes unrecoverable.

## Architecture

**Request flow for `/call`:** resolve tool (by URL host + longest `base_url` prefix, or by name) →
decrypt its secret(s) → apply each binding's injector → stream to the upstream → fire-and-forget
audit record. The infra relay streams bytes without business logic. The call application buffers
responses needing settlement or ownership evidence up to 8 MiB; larger responses return a 502
without charging instead of a truncated success. Endpoints that inline media (Gemini images)
declare `spooled_response`: their metered answer is read to a temp file instead, settled from its
reported usage, and relayed whole. Authorized free final downloads needing no body
evidence stream in full, as do own-key and own-tool responses.

**Module map** (`src/treg/`):


| Module                                     | Role                                                                                                             |
| ------------------------------------------ | ---------------------------------------------------------------------------------------------------------------- |
| `proxy.py`                                 | `relay()` — the whole product in one function: a faithful streaming proxy                                        |
| `injectors.py`                             | the auth-shape seam: `env`, `cli_auth`, `secret_file`, `oauth` place a secret into a header/query                |
| `oauth.py`                                 | token freshness (single-flight refresh) + the connect flow (consent URL, code exchange)                          |
| `health.py`                                | credential health: refresh oauth, probe tools, webhook the owner of anything broken                              |
| `convert.py`                               | scaffold a skill directory into a registerable bundle manifest                                                   |
| `api.py`                                   | the API — the only brain; CLI + skill are thin clients over it                                                   |
| `cli.py`                                   | the `treg` CLI                                                                                                   |
| `models.py`                                | SQLModel tables: `Org`, `User`, `Membership`, `Invite`, `Secret`, `Tool`, `Bundle`, `PendingOAuth`, `CallRecord` |
| `crypto.py` `config.py` `db.py` `audit.py` | Fernet encryption + tokens · settings · async DB · deferred audit writer                                         |


**The 4 auth shapes** (per binding `injector`): `env` (plain string / API key) · `secret_file` (a
JSON token file, pull a field) · `oauth` (a JSON OAuth token, auto-refreshed if refreshable) ·
`cli_auth` (material lifted from a CLI's keychain).

**Faithful-relay contract:** the proxy alters **only** three things, everything else is verbatim:

1. hop-by-hop transport headers (re-derived per hop),
2. treg's own control + edge-forwarding headers (`x-treg-token`, `x-treg-org`,
`ngrok-skip-browser-warning`, `x-forwarded-*`, `via`, …) and treg's session cookie — all stripped,
never leak upstream,
3. the injected credential(s).

**OAuth, three ways to get the first token:** *manual upload* (drop in a `token.json`) ·
*auto-refresh* (if the token carries `refresh_token` + client creds, treg keeps it fresh, you never
re-upload) · *hosted connect flow* (`treg oauth connect` → browser consent → treg captures the
token itself).

**Health checks:** give a tool an optional probe (`{method, path, expect_status}`); a periodic run
(on demand or via cron) validates every credential, refreshes OAuth, and webhooks the owner of any
that break.

Deep design lives in [`docs/context/`](docs/context/README.md) (per-subsystem fragments).

## Tests

```bash
uv run --with pytest-xdist pytest -n auto -q   # daily local default (same shape as CI)
uv run --frozen python -m pytest -q            # serial: debugging one test, or order
```

Coverage: proxy walking-skeleton, all injector shapes, per-user auth + CRUD + audit, skill composer,
URL-passthrough + faithful relay, OAuth refresh + connect flow, health checks, `treg run`/shell,
upload/scan, orgs + invites, the dashboard API, CLI.

## Contributing & docs

```
treg/
├── src/treg/            # the package (api, cli, proxy, injectors, oauth, health, convert, models, …)
│   └── web/             # dashboard, landing, tutorial, llms.txt, skill.md, install.sh
├── tests/               # pytest suite (CI + local default: pytest-xdist -n auto)
├── docs/
│   ├── context/         # design fragments (codemap system) + generated index
│   └── ONBOARDING.md    # first-time bootstrap
├── USAGE.md             # full treg CLI reference
└── pyproject.toml
```

Per-subsystem design docs are **fragments** in `docs/context/`, each citing its `src/treg/*`
sources. Working in this repo with an AI agent? The `/tools-registry-context` skill loads the
right fragment for what you're touching and keeps the docs in sync — run
`/tools-registry-context sync` before pushing.

**Roadmap:** MCP support · finer permission tiers · at-rest key-management hardening · possible
Loopni merge.

## License

Apache 2.0 with additional terms ([`LICENSE`](LICENSE)): use it freely — including commercially,
inside your own organization (self-hosting your own registry is encouraged). The restriction: don't
redistribute the code to third parties as a competing hosted/managed registry service without written
permission (`jason@superdesign.dev`). **Using the hosted treg.to API** inside your own product —
with pass-through billing via `X-Treg-Meta` and `usage/by-tag` — is allowed without permission;
that's calling our API, not redistributing our software.

### Pinned customer read scopes

For a restricted customer agent, `treg org agent-new bot --pin customer=cust_A` enforces attribution
and scopes call/run history, archived results and shared-provider async ownership to that pin.
Foreign or unattributed ids return 404; an unpinned operator keeps the org-wide view and shared
balance. BYOK account access and public media URLs retain their existing permissions. See the
[multi-tenancy contract](docs/context/architecture/multi-tenancy.md#caller-tags-and-pinned-read-scopes)
for multiple pins, migration and replay behavior.

## Docs

### docs/ listing
- file: CAPABILITY-CHOICE-PLAN.md
- file: CLAUDE-PLUGIN.md
- file: CUSTOMER-BILLING-PLAN.md
- file: DASHBOARD-TOUR.md
- file: DSH-PLUGIN.md
- file: HUB-DECISIONS.md
- file: IDEMPOTENT-CALLS-PLAN.md
- file: LOCAL-PROXY-PLAN.md
- file: MARKET-DATA-CATEGORY-RESEARCH.md
- file: MCP-OAUTH-PLAN.md
- file: MCP-PLUGIN-PLAN.md
- file: MINIMAX-PLUGIN.md
- file: ONBOARDING.md
- file: RECIPES-DECISIONS.md
- file: SHARED-PLAN-PRICING-PLAN.md
- file: TUTORIAL.md
- file: VENDORS.md
- dir: archive
- dir: assets
- dir: context
- file: enterprise-sso.md
- file: hub-listing-decisions.md
- file: hub-pricing-decisions.md
- dir: hub-recipes
- dir: ideas
- file: image.png
- file: tutorial.html

### docs/ONBOARDING.md
# tools-registry — onboarding

The bootstrap an agent (or human) follows to start calling shared tools and to share its own.
The CLI is a thin client over the API at `https://treg.to`; the API is the only brain.

## 1. Install the CLI

```bash
curl -fsSL https://treg.to/install.sh | sh   # installs `treg`, points it at the registry
```

(Working from a clone instead? `uv sync && uv run treg --help`.)

## 2. Sign in

Three doors, one identity (your email):

```bash
treg login                                  # GitHub OAuth (opens the browser)
treg login --email you@example.com          # email one-time code
treg login --token <TOKEN>                  # agents/CI: a per-org token from a team owner
```

Your token identifies you on every call (`X-Treg-Token`). New here? `treg onboard` walks you
through everything with a disposable demo team.

## 3a. Use a tool someone already shared (consumer)

```bash
treg tool ls                                 # what's available
treg call posthog query/events --query limit=5
treg run gh -- pr list                       # vendor CLIs work too
```

You hold **no upstream key** — the registry injects it server-side.

## 3b. Share your own (creator)

Point treg at a project — it finds the provider keys in the `.env`, the skill folders, and the
installed catalog CLIs, and registers what you pick:

```bash
treg scan          # read-only preview; nothing leaves the machine
treg upload        # register (encrypted server-side); idempotent, --replace to update
```

For one skill or a tricky tool (multi-credential, OAuth), see the manual flow in
[`USAGE.md`](../USAGE.md) — `treg skill init` / `skill add`, `treg tool add --bind`,
`treg oauth connect`.

## 4. Verify + observe

```bash
treg call <tool> <upstream-path>     # smoke-test
treg calls                           # audit: who called which tool, when, status
treg health                          # credential health across the org
```

## Notes

- Secrets are write-only; the API never returns a stored value.
- A tool can reference a secret another member uploaded (use-without-hold).
- Everything is org-scoped: `treg org ls` / `treg org use <slug>` picks the active team.

### docs/CLAUDE-PLUGIN.md
# The Claude Code plugin, and where it gets listed

treg ships as a Claude Code plugin served from this repo as its own marketplace: live the moment it
merges, with no reviewer in the loop. It installs the treg skill and treg's remote MCP server.

## Install

```
/plugin marketplace add superdesigndev/treg
/plugin install treg@treg
```

Then `/mcp`, pick `plugin:treg:treg`, and Authenticate. The server is declared URL-only with
`type: "http"`; Claude Code runs OAuth itself, so the install needs **no token and no
configuration**. Until sign-in the server is listed as "needs authentication" and contributes no
tools, so nothing 401s in the meantime.

The skill checks for the tools first and sends the human to `/mcp` when they are missing. The CLI
(`curl … install.sh | sh`, `treg login`) stays optional: the plugin path never asks an agent to run
a downloaded script, which Claude Code's auto mode blocks by default.

## What is where

```
.claude-plugin/marketplace.json           makes this repo its own marketplace: treg plus the workflow plugins
plugins/treg/.claude-plugin/plugin.json   the manifest Claude Code reads, MCP server inline
plugins/treg/.cursor-plugin/plugin.json   the manifest Cursor (and Grok Bot) read
plugins/treg/mcp.json                     Cursor's URL-only MCP config
plugins/treg/skills/treg/SKILL.md         GENERATED - the plugin's skill
plugins/workflows/<name>/                 GENERATED - one optional plugin per workflow skill
skills/treg/SKILL.md                      GENERATED - the bare skill for `npx skills add` and ClawHub
skills.sh.json                            category grouping for skills.sh / Hermes' Skills Hub
```

Claude Code and Cursor install **the same folder**, `plugins/treg/`, through their own manifests.
The marketplace `source` must stay `./plugins/treg`: a source of `./` makes the repo root the plugin,
which ships the whole repository and every workflow skill under `skills/`.

The workflow skills (`lead-signals`, `recruit`, `make-ugc`, `web-access`, `jev-memory`) are separate
plugins in the same marketplace, generated with their manifests and marketplace entries by
`scripts/build_plugin.py`, so `/plugin` offers them one by one instead of installing them with
treg. The plugin's skill tells the agent to offer one when the task matches it.

The MCP server is inline in the Claude manifest rather than pointing at `mcp.json` because Claude
Code rejects a server with a `url` and no `type` (it logs "Invalid MCP server config" and registers
nothing), while `mcp.json` stays URL-only for the hosts that read it.

The served page's first section branches on what the agent has: treg's MCP tools, the `treg` CLI,
or neither. Only the last installs anything, and only when the human asked for setup. So the bare
skill at the repo root is the served page unchanged, and the plugin's prepended note says only that
its tools are waiting for `/mcp` sign-in.

**Never edit `skills/treg/SKILL.md`.** Change `src/treg/web/skill.md` and regenerate:

```bash
uv run python scripts/build_plugin.py            # regenerate every plugin
uv run python scripts/build_plugin.py --check    # fail if any is stale (also a test)
```

## Listing runbook

Ordered so that everything self-serve ships before anything with a queue.

### 1. Own marketplace — live on merge

Nothing to submit. Merging to `main` publishes it; the install lines above start working.

Bump `version` in `pyproject.toml` and every manifest together: `test_plugin_version_tracks_the_package`
pins all of them to one value.

### 2. ClawHub (clawhub.ai) — ✅ LIVE, self-serve, CLI-based

**Published 2026-08-14: [clawhub.ai/superdesigndev](https://clawhub.ai/superdesigndev) · `treg@0.11.0`
· owner `@superdesigndev` · MIT-0.** Verified by installing it back out of the registry into a scratch
dir — the delivered `SKILL.md` is byte-identical to `skills/treg/SKILL.md` in this repo.

The publisher org was created with
`clawhub publisher create superdesigndev --display-name "Superdesign dev, Inc."`. Publishing under a
personal handle would also have worked — `--owner <handle> --migrate-owner` moves a skill later — but
a company handle reads as a product listing rather than a side project.


`https://clawhub.ai/submit` **404s** (Hermes' CLI still points there; its `--to clawhub` is a stub).
The live path is the npm CLI:

```bash
npm i -g clawhub
clawhub login                     # device flow; opens a browser (--no-browser prints a URL + code)
clawhub whoami                    # confirm before publishing

clawhub skill publish "$PWD/skills/treg" \
  --slug treg --name "treg" --version 0.11.0 \
  --changelog "..." \
  --topics "api,seo,serp,backlinks,enrichment,scraping,agent-tools,web-search" \
  --source-repo superdesigndev/treg \
  --source-commit "$(git rev-parse HEAD)" \
  --source-ref main --source-path skills/treg \
  --dry-run                       # drop --dry-run to publish for real

# Publishing is TWO PHASES. The command above only SUBMITS — the version sits at
# `pending.publication`, invisible on every public surface, until a scan is attached to it:
clawhub scan --slug treg --version 0.11.0 --update    # took ~37 minutes; let it run
```

**Do not skip that second command, and do not conclude the publish failed while it runs.** This is
the single least obvious thing about ClawHub and it is not in their docs. `clawhub skill publish`
reports `"status": "pending-publication"` and exits; nothing else happens on its own. `scan --update`
("write published scan results back to the selected version") is not a convenience — it is the step
that completes publication. Watch the moderation record flip:

```bash
curl -s -H "Authorization: Bearer $(clawhub token)" \
  https://clawhub.ai/api/v1/skills/treg/moderation
```

| | before `scan --update` | after |
|---|---|---|
| `legacyReason` | `pending.publication` | `scanner.llm.review` |
| `reasonCodes` | `[]` | `["review.llm_review"]` |
| public `GET /api/v1/skills/treg` | 403, hidden | returns the skill |

Note `package publish` has a `--wait` flag that polls to a definitive state; **`skill publish` does
not**, and `/api/v1/publish/attempts/<attemptId>` 404s for skill attempts. So for skills there is no
progress indicator at all — run `scan --update` and wait it out.

Verified against clawhub CLI **v0.23.3** — the published docs are thinner than the real `--help`,
so read the CLI:

- **Pass an ABSOLUTE path.** A relative `./skills/treg` fails with `Path must be a folder`, because
  paths resolve against `--workdir` + `--dir` (which defaults to `skills`), so it looks for
  `skills/skills/treg`. `"$PWD/skills/treg"` is the reliable form.
- **The `--source-*` flags are worth filling in.** They link the listing back to a GitHub repo,
  commit and path. That is the one provenance signal available on a registry whose own vetting
  history is the reason Hermes marks every ClawHub skill `community` trust.
- **`--categories` takes slugs the public API does not enumerate** (`/api/v1/categories` 404s and
  listings come back with empty `categories`). Do not invent one — use `--topics`, which is
  free-form, until a real category slug can be read off a live listing.
- `--dry-run --json` prints the resolved slug, version, file count and fingerprint without
  publishing. `latestVersion: null` means the slug is unclaimed.
- Publishing is not irreversible: `clawhub delete` soft-deletes a skill or withdraws one version,
  and `clawhub hide` / `undelete` exist too. Ownership can move later with
  `--owner <handle> --migrate-owner`, so publishing under a personal handle now does not lock the
  skill out of a `superdesigndev` org later.

Requirements the generated skill already satisfies: frontmatter `name` + `description` + semver
`version`, with `name` matching the parent directory (`treg`). A security scan runs post-publish;
flagged releases are hidden from the public catalog but stay in your dashboard.

⚠️ **ClawHub forces MIT-0 on every skill, with no per-skill override.** This repo is Apache-2.0 plus
a hosted-service restriction. `SKILL.md` is prose — it documents a hosted service rather than
implementing one — so licensing that one file permissively is consistent with wanting it copied
everywhere. It is a deliberate choice, not an oversight; do not let it drift into a claim about the
server code.

Listing here also feeds Hermes' Skills Hub automatically. Note Hermes hard-codes every ClawHub skill
to `community` trust after the Feb 2026 "ClawHavoc" incident (341 malicious skills), so this is a
discovery channel, not a trust signal.

#### Two verdicts, and only one of them gates visibility

Do not confuse these — one costs a day if you do:

- **Moderation** (`/api/v1/skills/treg/moderation`) is what hides or shows a skill. Ours is
  `verdict: "clean"`, `isSuspicious: false`, `isMalwareBlocked: false`, empty `reasonCodes`. Reading
  the CLI source: `isSuspicious` only prints an install-time warning that `--force` bypasses; only
  `isMalwareBlocked` hard-blocks.
- **`clawscan`** (`clawhub scan`) is an LLM review published as an **advisory on the listing**. It
  rated treg `suspicious` — and that changed nothing about visibility.

The v0.11.0 advisory raised four findings against `SKILL.md`. Three restate deliberate product
decisions; **one is worth weighing on its own merits, independent of ClawHub**:

| id | sev | what it says |
|---|---|---|
| `PE3` | **HIGH** | `cli_auth` consumes material from a CLI's keychain and relays it — "expands the agent's credential-access surface … without a strong, explicit consent boundary". Remediation suggested: per-tool opt-in before using keychain-derived credentials, and prefer scoped service tokens. |
| `SQP-1` | MEDIUM | the frontmatter `description` is broad enough to get the skill selected for loosely-related tasks |
| `SQP-2` | MEDIUM | `curl … \| sh` executes remote code with no checksum or signature |
| `EA2` | MEDIUM | the "ask once, not per command" guidance discourages per-command approval |

`EA2` and `SQP-2` are the trade-offs treg made knowingly. **`PE3` is a real description of a real
feature** and deserves a decision rather than a dismissal — see `docs/context/architecture/` for how
`cli_auth` binds. Static analysis and VirusTotal both came back clean.

### 3. Skill Store (aiskillstore/marketplace) + skills.sh

**Do NOT open a pull request against `aiskillstore/marketplace`.** Its README is explicit — *"PRs
adding skills will be closed"*; the repo is written to by the platform's own review pipeline, not by
contributors. Submit through the form instead:

> <https://skillstore.io/submit> — one required field, and it accepts a **directory**, so give it:
> `https://github.com/superdesigndev/treg/tree/main/skills/treg`

GitHub auth is optional (it only adds review notifications); anonymous submissions are allowed. The
audit there is **report-only** — a risk finding does not block publication. This is still worth doing
because `aiskillstore/marketplace` is one of only two repos in Hermes' `KNOWN_MARKETPLACES`, so it is
the cheapest route into Hermes' `claude-marketplace` source. Note `npx skillstore` is install-only —
there is no CLI submit path.

**skills.sh / `npx skills` — pass `-s treg`, always:**

```bash
npx skills add superdesigndev/treg -s treg     # ✅ just the treg skill
npx skills add superdesigndev/treg             # ❌ installs NINE skills
```

Verified on a scratch machine: the bare form scans the whole repo, finds `.agents/skills/*` as well
as `skills/treg/`, and installs this repo's **internal development skills** (`dev-local`,
`tools-registry-context`, `write-provider-skill`, `add-oauth-provider`, `vendor-listing`, the three
Google-provider skills) into the user's agent alongside treg. That is our layout leaking into a
product install. `skills.sh.json` does not prevent it — it only supplies category labels.

`-s treg` scopes it to one skill and is what every install line we publish must carry. With it, that
one command still covers 70+ coding agents beyond Claude Code.

### 4. anthropics/claude-plugins-official — the queue

Submit at <https://claude.ai/settings/plugins/submit>. Highest-trust placement, and it also feeds
Hermes. It is a review queue — the same "takes too long" risk as the MCP track — which is exactly why
it is last: everything above is already shipping by the time it is filed.

Entries in that directory use `git-subdir` with a pinned `ref` **and** `sha`, so being inside this
monorepo is not a blocker. **Tag a release and give them the tag.**

## The fourth door: treg.to itself

`GET /.well-known/skills/index.json` + `/.well-known/skills/treg/SKILL.md` (in `src/treg/api.py`)
make this host a first-class skill source under the agentskills.io convention — no registry, no
review, no third party. Hermes reads it directly. Because it goes through the same `_serve_md` as
`/skill.md`, `{BASE}` is templated to the **serving** host, so a self-hosted registry advertises
itself rather than treg.to.

## Before you submit anywhere

- `uv run --frozen python -m pytest tests/test_plugin.py tests/test_skill_md.py -q`
- `claude plugin validate .` — validates the marketplace manifest the way Claude Code itself parses
  it, which catches shape errors the JSON schema does not.
- Install it for real from a scratch clone, because markup that reads correctly still breaks:

  ```bash
  git clone --depth 1 https://github.com/superdesigndev/treg /tmp/treg-check
  claude plugin marketplace add /tmp/treg-check
  claude plugin install treg@treg
  claude plugin details treg@treg     # then: uninstall + marketplace remove
  ```

  `details` must report **Skills (1) treg** and **MCP servers (1) treg**, but it counts a server
  Claude Code later rejects. `claude mcp list` is the real check: it must list
  `plugin:treg:treg: https://treg.to/mcp/ (HTTP) - ! Needs authentication`.
- `claude plugin tag` creates the `treg--v{version}` release tag and validates that `plugin.json`
  and the enclosing marketplace entry agree — worth running before handing a tag to Anthropic.
- Confirm the copy still says treg **compares** providers and the caller chooses. treg does not route
  and does not fail over; the landing page had to be corrected for that claim once already, and a
  store listing is much harder to correct. `test_the_listing_does_not_promise_routing` guards it.
- Confirm the one-line positioning is identical in all three places (`test_one_product_one_sentence`).

### docs/MINIMAX-PLUGIN.md (excerpt)
# The MiniMax plugin, and how to submit it

treg's fifth shop window: the **MiniMax Plugin Marketplace**, which serves both **MiniMax Code**
(desktop) and **MiniMax Agent** (cloud). Like the Claude Code and Cursor plugins it is
**skills-only**, and for a harder reason than convenience: MiniMax rejects any package holding a
credential, and treg's MCP is bearer-authed per user. An authenticated MCP would have to go through
their **App/Connector** program (OAuth MCP server, PKCE, MiniMax-registered client) — see
"Later: an App" below.

Source of the rules: MiniMax's *Plugin Development and Submission Guide* (Feishu wiki
`QlTLwbAGNiACwLkWI85cFxHzn4L`, last updated 2026-08-17). It is a JS-rendered page behind a Feishu
login; the rules that matter are encoded in `scripts/minimax_plugin.py`.

## What is where

```
plugins/minimax/
├── .minimax-plugin/plugin.json   the manifest (schemaVersion 1)
├── icon.png                      512×512, the ▚ mark — same file as plugin/assets/icon.png
└── skills/treg/SKILL.md          GENERATED — never edit by hand
scripts/minimax_plugin.py         validator (--check) and ZIP builder (--zip OUT)
```

`plugins/minimax/` is the **plugin root** (a sibling of the Cursor root `plugins/treg/`; each store needs its own root because the manifests and generated bootstraps differ): `.minimax-plugin/plugin.json` sits directly inside it, which is
what MiniMax requires of a ZIP root or a GitHub subdirectory. Manifest `name` is `treg`; the skill is
exposed at runtime as `treg:treg`.

**Never edit `plugins/minimax/skills/treg/SKILL.md`.** Change `src/treg/web/skill.md` and regenerate:

```bash
uv run python scripts/build_plugin.py            # regenerate ALL plugins
uv run python scripts/build_plugin.py --check    # fail if any is stale (also a test)
python3 scripts/minimax_plugin.py --check  # MiniMax package rules (also a test)
```

### No bootstrap

The skill is the served page unchanged. Its first section already covers an agent with neither
treg's MCP tools nor the CLI, and nothing in it sends the agent to `treg mcp install`, which has no
MiniMax target.

### What their validator enforces (and ours pre-checks)

- `.minimax-plugin/plugin.json` at the root, **no wrapper directory** in the ZIP.
- `name`: lowercase, starts with a letter, ≤80 chars of `[a-z0-9._-]`. `version`: SemVer, **must
  bump whenever package content changes** (region/target-only changes may keep it). Ours tracks
  `pyproject.toml` — `test_plugin_version_tracks_the_package` pins it.
- `category` from a fixed list (Office, Studio, Design & Sites, Code, Business, Sales,
  Productivity, Science & Healthcare, Education, Other). We use **Productivity**.
- `exampleQueries`: 0–3, non-empty, ≤4,096 chars, *production* content.
- `apps` / `mcpServers` / `skills`: relative paths; **unused ones stay as empty arrays**.
- `icon`: relative path, lowercase `.png/.jpg/.jpeg/.webp`, square.
- Skill: `skills/<name>/SKILL.md`, YAML frontmatter with `name` == directory and non-empty
  `description`; body must be executable instructions, not marketing.
- Paths ASCII-only, `/` separators. No symlinks, hardlinks, LFS pointers, submodules, install
  scripts, native binaries, executable bits. UTF-8 without BOM. JSON = object, no duplicate keys.
- Limits: ZIP ≤64 MiB, ≤2,048 entries, ≤1,024 files, ≤16 MiB per file, path ≤512 B / segment
  ≤128 B / depth ≤16.
- **No token, key, secret or personal data anywhere.**

The manifest carries no `license` key — their schema does not define one and unknown keys are a
validator risk. The licence is stated here instead: `SKILL.md` is prose about a hosted service and
ships under the repo's Apache-2.0 (see `LICENSE`).

## Submission runbook

Two sources are accepted and go through the same pipeline. **Prefer GitHub** — no artefact to
manage, and updates are a new `Ref`.

**Submit** (form linked from the guide: "Open the Plugin submission form"; needs a Feishu account —
use one the team keeps, the *same* account must query status later):

| field | value |
|---|---|
| Action | Submit a new Plugin |
| Region | **US** (and CN if wanted — separate dimension; treg.to is reachable from CN but billing is Stripe) |
| Delivery target | **Desktop (MiniMax Code) + Cloud (MiniMax Agent)** — the skill is CLI-driven, so cloud only helps if the Agent sandbox can run `install.sh`; pick both, they can disable one |
| Source | GitHub |
| Repo | `https://github.com/superdesigndev/treg` |
| Ref | `main` (or the release tag, e.g. `v0.12.1`) |

### docs/context/README.md
# tools-registry — design fragments

<!-- GENERATED by scripts/build-map.py — do not edit by hand; edit fragment frontmatter instead -->

Small, focused fragments that mirror the codebase. Each declares the source files it
covers (frontmatter `sources:`). Regenerate this index with
`python3 .claude/skills/tools-registry-context/scripts/build-map.py`.

## Foundation

| Fragment | Status | Covers |
|---|---|---|
| [Tools Registry — charter (what it is, why, the proxy model)](foundation/charter.md) | foundational | 2026-06-30-jason-tools-registry.md, README.md |

## Architecture (proxy, auth, data model)

| Fragment | Status | Covers |
|---|---|---|
| [Google Ads conversion tracking — capture, outbox, upload](architecture/ads-conversions.md) | shipped | adsconv.py, signup.py, adtrack.js, gtag.js, … |
| [Archive - versioned history and cache admission](architecture/archive.md) | building | archive.py, hunter.yaml, results.py, 0031_archive_result_admission.py, … |
| [Auth & secrets — injectors, encryption, OAuth freshness, health](architecture/auth-secrets.md) | shipped | injectors.py, ssrf.py, crypto.py, oauth.py, … |
| [Call events — one pseudonymous event per call, to an Iceberg table outside Postgres](architecture/call-events.md) | building | call_events.py, call_events.py, contracts.yaml, test_call_events.py |
| [Endpoint catalog — what you can DO with a connected key, and which provider should do it](architecture/catalog.md) | shipped | rankings.py, rankings.py, test_rankings.py, catalog_added.py, … |
| [Application composition and deployment roles](architecture/composition.md) | shipped | bootstrap.py, bootstrap_handlers.py, bootstrap_http.py, worker.py, … |
| [Data model — the registry tables, async DB, audit writer](architecture/data-model.md) | shipped | 0042_pinned_read_scope.py, alembic.ini, env.py, 0001_baseline_current_schema.py, … |
| [Feedback - private intake for problems and suggestions](architecture/feedback.md) | shipped | feedback_contract.py, __init__.py, reports.py, reviews.py, … |
| [Find tools for a job - /catalog/find, recall by job and one judge request](architecture/find.md) | building | catalog_find.py, find_recall.py, find_index.py, embed.py, … |
| [The tool hub — tools a maker publishes, made of other tools](architecture/hub.md) | built (phases 1–10, 2026-09-09/14; pricing flexibility 9.1–9.5 (`docs/hub-pricing-decisions.md`), listing + public run log 10.1–10.5 (`docs/hub-listing-decisions.md`)); behind `hub_enabled` (TREG_HUB_ENABLED), off in production until the final merge | __init__.py, manifest.py, refs.py, graph.py, … |
| [Enforced import boundaries](architecture/import-boundaries.md) | shipped | pyproject.toml, ci.yml, __init__.py, __init__.py, … |
| [Instagram OAuth — direct Login and optional Facebook Page tools](architecture/instagram-oauth.md) | built; Meta configuration and live verification pending | catalog_ingest.py, access.py, resolve.py, service.py, … |
| [Local proxy — catch a program's own outgoing calls (`treg <command>`)](architecture/local-proxy.md) | shipped | localproxy.py, server.js |
| [Local CLI runs — run a vendor CLI as a dedicated user with a server-held credential (`treg run`)](architecture/local-run.md) | shipped | localrun.py, egress.py, fsjail.py |
| [MCP — the front door for assistants, and treg as an OAuth authorization server](architecture/mcp-oauth.md) | shipped | auth.py, mcp.py, health.py, mcp_oauth.py, … |
| [Media hosting - reference files a vendor can fetch (`treg host`)](architecture/media.md) | shipped | media.py, media.py, models.py, object_store.py, … |
| [Money — prepaid balance, the ledger, Stripe, and the reports that check it](architecture/money.md) | shipped | policy.py, tavily.yaml, tinyfish.yaml, test_tinyfish.py, … |
| [Multi-tenancy — orgs, memberships, invites, per-org scoping](architecture/multi-tenancy.md) | shipped | access.py, 0042_pinned_read_scope.py, test_pinned_read_scope.py, models.py, … |
| [Published organization concurrent-request admission](architecture/org-concurrency.md) | shipped | org_concurrency.py, kv.py, config.py, call.py, … |
| [Exact organization and endpoint call allowances](architecture/org-endpoint-quota.md) | shipped | org_endpoint_quota.py, service.py, types.py, route.py, … |
| [Published organization pause, rate and concurrency admission](architecture/org-flow-control.md) | shipped | org_flow_control.py, structured_logging.py, kv.py, config.py, … |
| [Process-local organization traffic logs](architecture/org-traffic.md) | shipped | org_traffic.py, structured_logging.py, bootstrap.py, call.py, … |
| [Policy extensions — decision points a private abuse policy can plug into](architecture/policy-extensions.md) | shipped | policy.py, bootstrap.py, signup.py, promotions.py, … |
| [The proxy — faithful credential-injecting relay + tool resolution](architecture/proxy-model.md) | shipped | relay.py, jsontext.py, ssrf.py, api.py, … |
| [Replay - recorded exchanges re-run through one checkout's billing, outcome and routing code](architecture/replay.md) | building | __init__.py, __main__.py, records.py, engine.py, … |
| [Discovery experiment — a relevance judge behind catalog search, measured on what the caller does next; the job-first answer served to agents](architecture/search-experiment.md) | building | catalog_search.py, search_experiment.py, interleave.py, judge.py, … |
| [Shadow provider — a candidate asked the same question as served calls, after the fact, and compared](architecture/shadow.md) | building | shadow.py, shadow.py, 0086_shadow_pairs.py, test_shadow.py |
| [Showcase leaderboard and pictures - applications, review, votes, avatars](architecture/showcase.md) | shipped | __init__.py, showcase.py, showcase.py, __init__.py, … |
| [Super-admin — cross-tenant read + control](architecture/super-admin.md) | shipped | api.py, admin.py, evidence_retention.py, access.py, … |
| [The table layer — one call, answered as rows and columns (`/table/`)](architecture/table.md) | built, behind `table_enabled` (TREG_TABLE_ENABLED), off by default | __init__.py, table.py, table.py, call.py, … |
| [Workbench table storage](architecture/workbench-storage.md) | foundational | models.py, 0077_workbench_table_metadata.py, teams.py, test_workbench_table_schema.py, … |

## Interfaces (API · CLI · skill)

| Fragment | Status | Covers |
|---|---|---|
| [The API — the only brain (FastAPI)](interface/api.md) | shipped | key_spend.py, media.py, sitetrack.js, api.py, … |
| [Catalog browse taxonomy — open placement and naming decisions](interface/catalog-review-proposal.md) | backlog | — |
| [The CLI (treg) + skill scaffolding](interface/cli.md) | shipped | cli.py, cli_view.py, home.py, test_released_cli_compat.py, … |
| [The web dashboard (served from FastAPI)](interface/dashboard.md) | shipped | App.vue, TeamShowcase.vue, TeamAvatar.vue, UserAvatarDialog.vue, … |
| [Enrich Arena — paid comparisons, one-click feedback, and visible waterfalls](interface/enrich-arena.md) | shipped | arena.py, arena.py, arena.py, models.py, … |
| [Import — scan a .env AND/OR a skills dir, auto-register as tools + bundles](interface/env-import.md) | in-progress | providers.py, skills.py |
| [Landing sandbox backend - closed](interface/landing-sandbox.md) | closed | sandbox.py, sandbox_identity.py, sandbox.py, __init__.py, … |
| [Onboarding — the first-run demo team (dashboard + CLI)](interface/onboarding.md) | shipped | auth.py, __init__.py, demo.py, first_run.py, … |
| [Search surfaces — robots, sitemap, the crawlable catalog, and the social card](interface/seo.md) | shipped | api.py, web.py, agent_pages.py, robots.txt, … |
| [Shell mode (treg shell) — transparent CLI interception](interface/shell.md) | shipped | shell.py, cli.py |
| [Test cases for the ChatGPT plugin submission](interface/skill-openai-test-cases.md) | reference | — |
| [Tool justifications for the ChatGPT plugin submission](interface/skill-openai-tool-justifications.md) | reference | — |
| [The shippable tools-registry skill (3 personas)](interface/skill.md) | shipped | skill.md, integrate.md, SKILL.md, SKILL.md, … |
| [Web Arena — private comparisons and live provider observations](interface/web-arena.md) | gated | web_arena.py, web_arena_scores.py, web_arena.py, web_arena_quality.py, … |

## Ops (deploy, scale)

| Fragment | Status | Covers |
|---|---|---|
| [Provider capacity — knowing what treg's own vendor accounts have left](ops/capacity.md) | shipped | __init__.py, capacity_notice.py, test_capacity_notice.py, collectors.py, … |
| [Running & deploying the server](ops/deploy.md) | shipped | pyproject.toml, hatch_build.py, build-dashboard.sh, build-web.sh, … |

## Reference

| Fragment | Status | Covers |
|---|---|---|
| [Glossary](reference/glossary.md) | reference | 2026-06-30-jason-tools-registry.md |

## guides

| Fragment | Status | Covers |
|---|---|---|
| [Expanding a catalog category — the add-a-provider playbook](guides/expanding-a-category.md) | guide | oauth_providers.py, authorization.py, oauth_flow.py, oauth_exchange.py, … |


### USAGE.md (CLI reference — first ~250 lines)
# treg — CLI usage

`treg` is the command-line client for **tools-registry**: call shared team tools without holding
their credentials, and turn your local skills into shareable tools. It's a thin client over the
API (`https://treg.to`); the API is the only brain.

Every command reads `~/.treg/config.json` for the endpoint + your token. Get per-command detail
with `treg <command> --help` (e.g. `treg secret --help`, not `treg "secret add"`).

## Install (once)

```bash
cd tools-registry
uv tool install --editable . --python 3.13     # puts `treg` on your PATH, tracking the dev source
# code edits reflect with no reinstall; re-run with --reinstall only after a dependency change
```

## Core idea

**Two sources of callable tools sit behind the same `/call/`.**

- **The catalogue** — ~2,600 curated external endpoints across ~40 data providers (TikTok, Instagram,
  Reddit, SEO and SERP data, enrichment, scraping…). Call one by its **endpoint id**. If nobody on the
  team holds a key for that provider, treg can serve it on **its own key**, billed per call from the
  team's prepaid balance. No provider signup.
- **The vault** — your team's own tools. Any API key, OAuth connection or vendor CLI a member
  registers becomes callable by every teammate and their agents, without the key ever leaving the
  server.

The vocabulary for the vault half:

- A **tool** = an upstream `base_url` + a list of credential **bindings** (each binding injects one
  secret into the request). A request can carry several (e.g. google-ads: OAuth bearer + a
  `developer-token` header).
- A **skill / bundle** = a recipe (SKILL.md) + its secrets + its tool(s).
- The proxy **relays, never models** the upstream, and **injects auth server-side**, so callers
  never hold the key. Your `X-Treg-Token` is stripped before the upstream sees it.

---

## Setup / identity

Auth is **identity-first**: prove who you are once (GitHub or an email code — first proof also
registers you + creates your personal org), then work across all your orgs. Agents/CI can instead
present a per-org token directly.

| Command | Options | What it does |
|---|---|---|
| `treg` | `--json` | no arguments: the registry, your account, the active team and role, its balance, its own tools, and the next commands to run (`help[]`). Every line is best-effort and it always exits 0 |
| `treg config` | `--base-url URL` | show or set the endpoint (prints base URL, email, active org, logged-in) — use `treg org ls` for the full org list |
| `treg login` | _(none)_ | GitHub browser sign-in (register-or-login), stores one identity token |
| `treg login` | `--email EMAIL` | email one-time-code sign-in (register-or-login); prompts for the code. A server that requires a browser check finishes the sign-in in the browser instead |
| `treg login` | `--token TOKEN` | agents/CI: use a per-org token directly |
| `treg logout` | — | clear your stored credentials |
| `treg onboard` | `--mode guided\|quick` · `--name N` · `--yes` · `--reset` | colourful guided first-run — pick **guided build** (you create the team + invite a teammate, step by step) or **quick demo** (we seed a full demo team + tool + activity), ending on a no-key call. Offered `[Y/n]` after your first login; `--reset` removes demo teammates |

```bash
treg config --base-url https://treg.to
treg login                                 # GitHub; or:
treg login --email you@example.com        # emailed 6-digit code (register-or-login)
```

## Teams / orgs

An **org** (team) owns the tools/secrets. After `treg login` the CLI holds a single **identity token**
in `~/.treg/config.json` and sends your **active** org as `X-Treg-Org`; `treg org use <slug>` switches
it. (With `treg login --token`, that per-org token is used directly instead.) Every other command runs
in your active org. Roles: **owner > admin > member** (a member calls + manages
only what they created; admin/owner manage anything in the org; admin+ can invite/remove members).

| Command | Options | What it does |
|---|---|---|
| `treg org create` | `"NAME"` | create a new org; you become its owner (new token, auto-active) |
| `treg org ls` | — | list your orgs (marks the active one) |
| `treg org use` | `SLUG` | switch the active org |
| `treg org rename` | `--name "NAME"`, `--slug SLUG` | (admin+) rename the active org and/or change its slug; existing keys keep working |
| `treg org invite` | `EMAIL`, `--role member\|admin` | (admin+) create a one-time invite **code** to share |
| `treg org members` | — | (admin+) list members + roles |
| `treg org join` | `CODE`, `--email EMAIL` | redeem a code: registers you if new, joins, saves the org token |

```bash
# owner side
treg org create "Team A"                       # active org is now team-a
treg org invite bob@company.com --role member  # prints e.g. inv_7Kd9x2LmQpR4 — send it to Bob

# Bob's side (no email is sent; he gets the code over Slack/DM)
treg config --base-url https://treg.to
treg org join inv_7Kd9x2LmQpR4 --email bob@company.com   # joins + mints HIS own token
treg tool ls            # sees only Team A's tools
treg org use team-a     # switch orgs anytime; one token per org, never mixed
```

## Secrets (credentials — write-only; the API never returns a stored value)

| Command | Options | What it does |
|---|---|---|
| `treg secret add NAME` | `--value V` \| `--file PATH`, `--kind env\|secret_file\|oauth\|cli_auth` | upload a credential (a string value, or a file's contents) |
| `treg secret ls` | — | list (name / kind / owner) |
| `treg secret rm ID` | — | delete (blocked while a tool binds it) |

```bash
treg secret add posthog-key --value "$POSTHOG_API_KEY"
treg secret add gsc --file ./.secrets/token.json --kind oauth
```

## Tools

| Command | Options | What it does |
|---|---|---|
| `treg tool add NAME` | `--base-url URL` (required) | register a tool |
| — single-binding | `--secret ID`, `--injector`, `--auth-in`, `--auth-name`, `--auth-format`, `--secret-field` | the common case |
| — multi-binding (friendly) | `--bind 'secret=ID,injector=,location=,name=,format=,secret_field='` (repeatable) | only `secret=` is required |
| — multi-binding (raw) | `--binding '<json>'` (repeatable) | full binding dict, advanced |
| — health probe | `--health '{"path":"me","expect_status":200}'` | optional validation probe |
| `treg tool ls` | — | list tools + their bindings |
| `treg tool rm ID` | — | delete |

**Defaults** for a single `--secret` and for each `--bind`:
`injector=env`, `location`/`auth-in=header`, `name`/`auth-name=Authorization`,
`format`/`auth-format=Bearer {secret}`, `secret-field=access_token`.

```bash
# single credential
treg tool add posthog --base-url https://us.posthog.com --secret 3
# query-key API instead of a bearer header
treg tool add gsc --base-url https://searchconsole.googleapis.com --secret 3 \
  --injector oauth --secret-field token
# two credentials on one request (google-ads)
treg tool add google-ads --base-url https://googleads.googleapis.com \
  --bind "secret=4,injector=oauth" \
  --bind "secret=5,name=developer-token,format={secret}"
```

## The catalogue (call an API you have no key for)

| Command | Options | What it does |
|---|---|---|
| `treg catalog search` | `"what you want to do"`, `--new [DAYS]`, `--sort newest` | find endpoints by capability, with the same search agents get (name a provider, "exa search", to put its tools first); `--new` keeps tools added in the last DAYS days (30 when bare, max 365), `--sort newest` lists newest first; with either, the words are optional |
| `treg catalog get` | `ENDPOINT_ID` | docs, parameters, **the price**, and how you would be served |
| `treg call ENDPOINT_ID` | `--query K=V`, `--data STR` or `--data @FILE` | call it |
| `treg --json call ENDPOINT_ID` | same | for scripts: one JSON line `{"result": <body>, "_treg": {http_status, call_id, charged_micro}}` on stdout, nothing on stderr |
| `treg call ENDPOINT_ID --await` | `--timeout N` (default 900) | a generation call (video/image): submit, poll the provider, print the final response |
| `treg host FILE` | `--content-type T`, `--json` | host a reference image/audio/video at a public URL a vendor can fetch (30 MB, 7-day TTL, free); prints the URL for `image_urls` / `audio_urls` |
| `treg catalog request` | `"what's missing"` | searched, not there? file it — requests steer what gets added next |
| `treg resources list` | `--provider fishaudio --kind voice` | list Fish-account voices with BYOK, otherwise platform-created voices for the active team |

```bash
treg catalog search "instagram profile"
treg catalog search --new                            # tools added in the last 30 days, newest first
treg catalog search phone --new 60                   # phone tools added in the last 60 days
treg catalog get tikhub.tiktok.user.profile          # shows the price BEFORE you spend
treg call tikhub.tiktok.user.profile --query uniqueId=tiktok
```

**Video and image generation** (`video-gen` / `image-gen` platforms) are async tasks: the call returns
a task id, and `--await` polls until it finishes. Stdout is the final response only; stderr gets the
task id, a resumable `treg call …` command, progress and the result URL. Exit 0 = done, 2 = the
provider failed the task, 3 = timed out (resume with the printed command). Money is reserved at
submission and charged only on success; a failed task refunds the hold. Result URLs are time-limited
(download promptly; treg never stores media). From a coding agent, raise the shell tool's timeout or
run the call in the background - a video takes 1-5 minutes. `treg audit` shows each task's state.

Fish Audio TTS is synchronous and returns audio bytes. Keep stdout clean and redirect it:

```bash
treg call fishaudio.tts.s2-1-pro --method POST --header model=s2.1-pro \
  --data '{"text":"Hello","format":"mp3"}' > speech.mp3
```

Create a voice with repeated `--upload voices=@clip.wav` parts and the fixed private fields shown by
`treg catalog get fishaudio.voices.create`; then use its id as TTS `reference_id`. Platform-created
voices appear in `treg resources list --provider fishaudio --kind voice`. With BYOK the same command
lists the connected Fish account instead. Curl callers use
`GET /orgs/{org_id}/provider-resources?provider=fishaudio&kind=voice`; it returns the same normalized
rows with `X-Treg-Resource-Source: byok|platform`. BYOK users may also call Fish's raw account-wide
list directly. To choose a reusable Fish-supplied voice, call
`fishaudio.voices.discover` with `self=false` and an explicit `licensed=true|false`, then pass a
returned `_id` as the TTS `reference_id`. `licensed=true` selects Fish's rights-secured subset;
`false` includes the broader public/community catalog. On the platform key, treg verifies that
non-team ids remain public before synthesis. `treg catalog get fishaudio.tts.s2-1-pro` lists the
supported generation, prosody, output-format, bitrate, sample-rate, latency, and chunking controls.

**How a catalogued call is served — the credential ladder, in order:**

1. the team registered its own tool for that provider → that tool, that key;
2. the team stored a secret for the provider → injected through a virtual tool;
3. neither → **treg's own key**, metered against the team's prepaid balance.

Rung 3 only applies where treg has both a key and a published price for that endpoint; anything
unpriced is refused rather than served, and you are told to connect your own key. Your own key is
never billed to the balance.

## Review a catalog call

`treg review <call_id> <useful|partly|not_useful|not_sure> [--reason "text"]` rates a catalog
call after you have used the result. Phase 1 invites only direct catalog calls served on treg's
own platform key; sampled calls print an invitation on stderr. Routed and own-key catalog calls
can still be reviewed uninvited. `not_sure` is fine when you cannot tell. The optional reason is
1-200 characters after trimming. Omit private data and raw payloads. Use `feedback` for anything confusing or wrong, then keep going
with the task. The receipt contains `review_id` and `status` (`received` or `already_reviewed`).
If the call record is not written yet, retry shortly with the same call ID.

## Feedback

`treg feedback submit <quality|pricing|friction|other> "message"` submits a problem or suggestion to the
configured registry, under the active team. Add `--call-id ID` (repeatable) or `--endpoint-id ID`
when available. Message `-` reads a prepared, sanitized description from stdin. The command
returns a `feedback_id`. Omit private information and raw requests, responses or logs.
Retrieve a report with `treg feedback get <feedback_id>`.
See `treg feedback --help` and your registry's `/feedback.md` for details.

## Balance & top-up

Only calls on **treg's key** (rung 3 above) cost balance. Everything else — your own keys, your own
tools, vendor CLIs — is free of it.

| Command | Options | What it does |
|---|---|---|
| `treg balance` | `--limit N`, `--json` | credit left, calls in flight, recent spend |
| `treg topup` | | add funds, or set up automatic top-ups |

```bash
treg whoami                  # the account, the active team and your role, the server
treg balance                 # every new team starts with $1.00 of free credit
treg balance --json          # integer micro-USD (1e-6 USD) — the unit the ledger uses
treg topup
```

Out of balance is an HTTP **402** `error: insufficient_balance` carrying `balance_micro`, `estimated_cost_micro` and a `topup_url`,
so an agent can act on it without reading prose. There is also a per-day ceiling on spend against
treg's keys, so a runaway agent has a bounded blast radius.

If treg's **own** account for a provider is out, a metered call is refused with HTTP **503**
`provider_capacity_unavailable` before anything is reserved — nothing is charged, the body names
`resets_at` when known and `alternatives` (other providers for the same capability). Your own key
for the provider is never affected, and treg does not switch providers on your behalf. treg
re-checks the provider about once a minute, so a retry after a minute can succeed. A call that
reaches the provider just as treg's account runs out is relayed as the provider answered, with
`X-Treg-Capacity: exhausted`; `treg call` then prints a notice that the tool is unavailable on
treg's side instead of naming the provider's wallet.

Where the deployment has the overflow relay on, treg may instead serve the **same endpoint** through a
treg-owned aggregator account — same request, same response shape, the relay's real price (0% markup),
`X-Treg-Served-Via: overflow:<name>` on the response. `treg org overflow off` opts your team out (calls
then get the 503 above); `treg org overflow` shows the setting. Own keys are never relayed.

`treg org archive off` takes your team out of treg's archive of answers: no new call of yours is
answered from a stored answer or recorded into one, so metered calls lose the repeat price (own keys
stay free as always). `treg org archive` shows the setting; `treg org archive on` opts back in.
Answers already stored for the team are erased when the team is deleted, or on request; call records

### AGENTS.md (agent instructions — first ~150 lines)
# tools-registry (`treg`) - guide for every coding agent

<!-- Editors: CLAUDE.md imports this file; Codex and Cursor read it directly. -->

treg is the tool catalog for an agent: one base URL, one token, and the agent can call a curated
catalog of external endpoints plus its own team's tools without ever holding an API key. The
load-bearing mechanic is a proxy that makes the caller's **real upstream request**, injects the
credential server-side when one is required, and relays the answer verbatim. A catalog endpoint
explicitly verified as public can instead relay with no injected credential. We never model an
upstream API.

## Paired treg.to checkout

For work on the hosted treg.to service, clone the public `treg` repository and private
`treg-internal` repository as siblings with those exact directory names. When `../treg-internal`
exists, treat both repositories as one operational workspace:

- `treg` owns public product code, portable behavior and self-hosting documentation.
- `treg-internal` owns live production configuration, operational runbooks, incident evidence and
  private admin tools.
- Read both repositories before changing production behavior, but never copy credentials, live
  environment exports, customer data or raw logs between them.
- Everything committed here is public, comments and commit messages included: describe treg.to
  only by mechanism, never by its numbers, dates, hosts, instance counts or schedules. Those go to
  `../treg-internal`.
- Commit and open PRs separately. State the merge order whenever one PR links to or depends on the
  other.

Do not clone `treg-internal` inside this repository and do not make it a Git submodule. Start agents
from the repository that owns the task; the sibling path supplies the other half of treg.to context.

## Non-negotiables

Everything else in this file is guidance; these are the contract, and they win over any other passage.

1. A team's own key always wins over treg's, is never metered, and is never routed or overflowed.
   An operator's exact org/endpoint protective call allowance applies to every credential tier;
   it counts admitted logical calls, not money or provider credits.
   This temporary allowance permits calls when Redis state cannot be confirmed; it is not a durable cap.
2. A hold (the balance `reserve` sets aside for one call) is settled or released exactly once, on
   every path: timeout, cancellation and exceptions included.
3. A request holds zero database connections while upstream or object-storage I/O is in flight.
   Keep `reserve` and `settle` separate; read archive pointers, close the session, then fetch bytes.
4. Plain `/call/` is a faithful relay: the injected credential (on treg's shared key, one of treg's
   accounts for the provider, chosen per call and fixed for anything an account created; on a
   connection to treg's own Meta app it also carries `appsecret_proof`, the HMAC of the injected
   token with the app secret, replacing any caller value), the transport headers listed in
   `src/treg/infra/upstream/relay.py`, and (on treg's shared key only) the per-org and, for pinned
   agents, per-pin re-scoping of the caller's `Idempotency-Key` and treg's own `User-Agent` in place
   of the caller's are the only rewrites of what the caller sent. One addition is allowed: when the
   catalog declares `ceiling_param` (`{in: query, name, unit: usd}` on the provider file or on that
   endpoint's `cost`), the call carries a caller ceiling, and the caller did not already send that
   query name, the call application appends `name=<remaining ceiling in USD>` to the outbound query
   before `relay()`. An explicit caller value is never rewritten. The appended pair is absent from
   the inbound query, so it does not enter `params_hash` or the archive key. A credential
   binding with `location: "json"` explicitly parses and reserializes the top-level JSON object; it
   is not byte-faithful and must never be used with an upstream that signs or hashes the raw body.
   Never add upstream-specific modeling.
   One more rewrite, on 4xx/5xx only: every spelling of an injected credential the provider echoes
   back in an error body is masked (`***`) before the caller, an idempotent replay or the evidence
   row sees it. The error body is read whole (gzip/deflate decoded) up to 8 MiB; on a credentialed
   call one that cannot be scanned is replaced whole, never relayed as a prefix.
   A live-verified free catalog endpoint may declare an anonymous fallback; its empty binding list
   omits credential injection but does not strip or rewrite caller headers.
   Routed endpoints and overflow wrap the child's answer and say so; they never alter it. With
   `X-Treg-Route-Verify`, an email or phone find makes one more linked child call (the check), with its own
   hold and charge, and reports it in `_treg.verification`; the find's answer is not altered. With
   `X-Treg-Route-Confirm`, an email find keeps asking providers after a hit until another returns the
   same address, each attempt billed as usual, and reports it in `_treg.confirmation`; the answer
   returned is the first provider's, unaltered. With `X-Treg-Route-Decisive`, an email check keeps
   asking providers until one answers valid or invalid, each attempt billed as usual, and reports it
   in `_treg.decision`; the answer returned is the deciding provider's, unaltered. Responses needing settlement or ownership evidence are buffered by the application
   up to 8 MiB; exceeding that limit fails without charging, never returns a successful prefix.
   An endpoint declaring `spooled_response` (inline media) instead reads its metered 2xx to an
   unlinked temp file under a per-body cap and per-process budget, settles from only the paths its
   row reads (usage meters, `expect` success leaf), then relays the file byte for byte; it is never
   archived or replayed.
   Authorized free final fetches needing no body evidence stream in full.
   `/table/` runs the same call through the same road and returns it as rows and columns; it never
   changes what `/call/` returns (docs/context/architecture/table.md).
5. Balances change only through money's five entries: grant, topup, reserve, settle, release.
   There is deliberately no refund or adjustment entry; an ops correction is a grant.

**Changing any invariant in this file means editing this file in the same PR.** Routed endpoints
and overflow once shipped with every other doc updated while this file still said "no router";
agents then built against a constitution that was wrong.

## Where the truth lives

- **Design docs are fragments.** `docs/context/` holds one per subsystem, each naming its
  `src/treg/*` sources in frontmatter; `docs/context/README.md` is the generated index and
  `docs/context/foundation/charter.md` the start. Read the fragment before changing an area (the
  `tools-registry-context` skill in `.agents/skills/` loads it).
- **Before pushing:** `bash .agents/skills/tools-registry-context/scripts/drift.sh` maps changed
  sources to fragments. Update them and commit the docs **in the same commit as the code**.
- **Agent-facing files are the product's front door**, not documentation: `src/treg/web/llms.txt`
  and `src/treg/web/skill.md` (installed into every agent by `install.sh`). They, `README.md` and
  this file must agree on how treg works; a behavior change asks whether all four move.
- **Three files move together** or they drift: `src/treg/web/tutorial.js` (the only interactive
  source) and its hand-kept prose mirrors `src/treg/web/tutorial.md` and `docs/TUTORIAL.md`.
- `README.md` is the overview and quickstart, `USAGE.md` the CLI reference, `CONTRIBUTING.md` the
  dev setup, `SECURITY.md` required reading before touching the proxy, runners, auth or secrets.
- If available, `../treg-internal` holds private operational configuration and tools; read its
  `README.md` before changing production settings. Public development does not depend on it.

## Architecture

### Four layers

`routers/` -> `application/` -> `domain/` -> `infra/`. Imports point inward only.

| Layer | Owns | Never |
|---|---|---|
| `routers/` | HTTP and MCP translation in, response shape out | business rules, query orchestration, money |
| `application/` | use-case sequencing, transaction boundaries, compensation, cross-domain composition | empty wrappers around one-domain CRUD |
| `domain/` | rules explainable and testable alone: `identity`, `governance`, `connections`, `tools`, `catalog`, `capacity`, `money`, `asynctasks`, `feedback`, `hub` (a maker's tool made of tools: the manifest, the reference language, the graph), `showcase` (leaderboard applications, tiers, badges, consent), `images` (picture kinds, sizes and limits) | routers, application, concrete SDKs |
| `infra/` | DB engine and sessions, crypto, upstream relay and SSRF, ratestore, the shared key-value store, email, Stripe | decisions |

- Domains do not import each other, with three sanctioned edges: `governance -> identity`,
  `tools -> connections`, `capacity -> catalog` (read-only). `identity` and `money` are leaves.
  import-linter enforces the layering (`[tool.importlinter]` in `pyproject.toml`, run by CI);
  `docs/context/architecture/import-boundaries.md` explains each contract.
- `bootstrap.py` alone knows concrete implementations. `api.py` is the legacy `all`-role
  entrypoint, not where logic goes. `audit.py` is best-effort and drops rows under load, so nothing
  that must persist goes through it; `analytics` is read-only.

### Writes

- **Session discipline.** The application use case opens the session and is the only place that
  commits; domain functions never commit or roll back. A commit mid-flow silently breaks
  compensation, and no import rule can catch it. Money's public `reserve`, `settle` and `release`
  commit by design; a few other domain commits remain. Do not add another; move one out when you
  touch it.
- **Table ownership.** One writer module per table; cross-domain reads are fine. Three recorded
  exceptions: only money writes `org.balance_micro`, the daily-spend counter (`spent_today_*`) and
  the auto-top-up fields; the call runtime may persist an OAuth token refresh into `secret`; audit
  writes `callrecord`, domains only read it (`application/evidence_retention.py` also updates it,
  blanking the two evidence columns past retention).
- **Feedback handling.** This repo owns `FeedbackHandling` and `FeedbackHandlingEvent` models and
  migrations; the private admin service is their only runtime writer. Original reports remain
  owned by the feedback domain. See `docs/context/architecture/feedback.md`.
- **Showcase leaderboard and pictures.** `application/showcase.py` is the only writer of
  `ShowcaseApp`, `ShowcaseAppEvent`, `ShowcaseAppKey`, `ShowcaseWeek`, `ShowcaseCursor` and `ShowcaseVote` (team
  deletion removes them with the team, as it does every team's rows); the private admin acts
  through its staff API (`/admin/showcase/*`), never the tables. `application/images.py` is the
  only writer of `user.avatar_key` and `org.avatar_key`. The public leaderboard never returns a
  team, an exact count or money. See `docs/context/architecture/showcase.md`.
- **The call runtime is self-contained.** `src/treg/application/call/` depends on no management
  code (routes, login, OAuth consent, Stripe top-up), reads only membership, deny rules,
  credentials, catalog prices and balances, and writes only what `tests/test_call_architecture.py`

### CLAUDE.md
@AGENTS.md

<!-- Every cross-agent rule lives in AGENTS.md, so Claude Code, Codex and Cursor read one file and
     cannot drift apart. Add Claude-specific instructions below this comment; there are none today. -->

### CHANGELOG.md (Unreleased + head)
# Changelog

Notable changes to treg. Dates are release dates; anything under **Unreleased** is on `main` but not
yet published to PyPI or Homebrew.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and treg uses
[semantic versioning](https://semver.org/spec/v2.0.0.html).

## Unreleased

### Added

- **`X-Treg-Route-Confirm` on `treg.people.email.find`.** An opt-in header: a hit counts only once
  a second provider returns the same address, so one provider's wrong guess no longer comes back
  alone. Each extra attempt is billed at its own price inside `X-Treg-Route-Max-Cost`. The first
  address is returned either way, with `_treg.confirmation` and `X-Treg-Route-Confirmed` saying
  whether another provider agreed. Without the header nothing changes.

- **`X-Treg-Route-Decisive` on `treg.people.email.verify`.** An opt-in header: an answer counts only
  when it says `valid` or `invalid`. Unknown, catch-all or risky sends the check on to at most two
  more providers, each billed at its own price inside `X-Treg-Route-Max-Cost`, asked in order of
  measured verdict quality where the deployment has it. `_treg.decision` and `X-Treg-Route-Decided`
  say whether one decided. Without the header nothing changes.

- **`jev-memory`, a memory for Claude Code.** A workflow skill (`npx skills add superdesigndev/treg
  --skill jev-memory`, or `/skills/jev-memory/SKILL.md`) that installs the Claude Code mod in
  `examples/claude-code-mods/jev-memory`, or has Claude build the same mod from one prompt. After
  every answered prompt the mod asks Jev, through one `openrouter.ai-judge.decide` call, whether each
  sentence is a lasting preference; sentences at 0.8 or higher are saved to `.claude/jev-memory.md`
  and put back into the first message of later sessions.

- **The tool hub — publish a tool made of other tools.** A team can publish its own tool and let
  other people's agents call it. A hub tool is one folder of four files: `recipe.json` (the
  contract), either a JSON steps recipe or a `run.js` script, `check.json` (sample inputs, run once
  for real at publish), and `README.md`. A fifth file, `data.csv`, travels with the tool and a
  script reads it as `ctx.data`, so a spreadsheet becomes a callable tool with no database.

  Every step goes out through treg under its own hold: a catalog step runs as the caller, a step on
  one of the maker's own tools runs as the maker and is never metered. A caller therefore never
  sees the maker's keys, and `uses` in the manifest names every host a tool may reach. A script
  runs in a separate process with no network of its own; `ctx.call` is its only road out.

  **Three ways to price it**, one `pricing` block per version, in the maker's words: `per_call` (a
  fixed price per successful run), `per_result` (a price times the integer `results` the run
  returns, bounded by a `results_from` input), and `percent` (a percent of the run's provider fees).
  The provider fees are billed to the caller on top. A variable price holds the most the maker can
  earn on that run (derived from the caller's ceiling or the results input, no declared cap needed)
  and settles the real amount, refunding the difference. Callers never see the mode: every surface
  leads with what recent successful runs cost, fees and price together, as one number or a
  low–high range. The price settles to the maker as `earned` credit, spendable at once.

  **Two switches the maker controls**, neither bumping the version: `listed` puts the newest live
  version into catalog search, and `public_log` shows a run log on the tool's share page. A hub
  tool is out of search until its maker lists it. The run log shows outcomes only — time, result,
  duration, steps, units and the price paid — and never who called, the inputs, or the output.

  New commands: `treg hub init | run | publish | ls | earnings | price | list | unlist | log |
  retire`. New MCP verbs: `hub_create`, `hub_update`, `hub_mine`. Every hub tool gets a share page
  at `/hub/<id>`, with an agent twin at `/hub/<id>.md`.

  The whole feature sits behind `TREG_HUB_ENABLED` and is **off by default**. While it is off every
  `/hub/...` route answers `404`, the agent-facing files carry no hub text, and catalog search
  returns no hub row.

### Changed

- The agent plugins (Claude Code, Codex, Cursor, DeepSeek Harness, MiniMax) now always carry the
  hub section. A plugin is a static file installed against any registry, including a self-hosted
  one that may have the hub switched on, so it ships the knowledge and lets the agent find out at
  run time. The section tells an agent to read a `404` as "this registry does not offer the hub"
  rather than retrying.

### LICENSE (Additional Terms)
tools-registry License

Copyright (c) 2026 Superdesign (superdesign.dev)

This software is licensed under the Apache License, Version 2.0 (reproduced in
full below), with the following Additional Terms. The Additional Terms take
precedence over the Apache License to the extent of any conflict.

ADDITIONAL TERMS

1. Hosted service restriction. You may use, modify, and redistribute this
   software freely under the Apache License — including commercial use inside
   your own organization (running your own registry for your own team is
   expressly permitted and encouraged). However, you may NOT use this software,
   in original or modified form, to provide a hosted, managed, or embedded
   service to third parties — for example offering it as a SaaS product,
   a managed registry service, or a component of a product or service that is
   sold, licensed, or otherwise commercially distributed to others — without
   the licensor's explicit prior written authorization. To request such
   authorization, contact jason@superdesign.dev.

2. Contributor terms. By contributing code, documentation, or other material
   to this project, you agree that: (a) your contribution is licensed to the
   project under these same terms; and (b) the licensor may use your
   contribution commercially, including in hosted offerings of this software
   operated by the licensor.

3. Everything else. Except as modified by the Additional Terms above, all
   rights and obligations are governed by the Apache License, Version 2.0
   below.

--------------------------------------------------------------------------

                                 Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

   1. Definitions.

      "License" shall mean the terms and conditions for use, reproduction,
      and distribution as defined by Sections 1 through 9 of this document.

      "Licensor" shall mean the copyright owner or entity authorized by

### examples/ listing
- dir: claude-code-mods
- dir: hub
- dir: proxy-demo

### skills/ listing
- dir: jev-memory
- dir: lead-signals
- dir: make-ugc
- dir: rea-growth
- dir: recruit
- dir: treg
- dir: web-access

### src/treg/ listing
- file: .DS_Store
- file: __init__.py
- file: __main__.py
- file: adsconv.py
- file: agent_pages.py
- file: agents.py
- dir: alembic
- file: analytics.py
- file: api.py
- dir: application
- file: archive.py
- file: archive_bodies.py
- file: audit.py
- file: bootstrap.py
- file: bootstrap_handlers.py
- file: bootstrap_http.py
- file: call_events.py
- file: call_surface.py
- file: caller_metadata.py
- file: capacity_notice.py
- dir: catalog
- file: cli.py
- file: cli_analytics.py
- file: cli_session.py
- file: cli_view.py
- file: client_identity.py
- file: client_ip.py
- file: config.py
- file: convert.py
- file: crypto.py
- dir: domain
- file: egress.py
- file: email.py
- file: feedback_contract.py
- file: fsjail.py
- file: health.py
- file: hints.py
- file: hub_sandbox.py
- dir: infra
- file: jsontext.py
- file: localproxy.py
- file: localrun.py
- file: maintenance.py
- file: mcp.py
- file: mcp_install.py
- file: models.py
- file: oauth.py
- file: oauth_providers.py
- file: policy.py
- file: providers.py
- file: ratestore.py
- file: reconcile.py
- dir: routers
- file: runner.py
- file: sandbox.py
- file: sandbox_identity.py
- file: shell.py
- file: skills.py
- file: timeutil.py
- dir: web
- file: worker.py
- dir: workflow_runs

## Top-level structure
- `.agents/` — agent skills marketplace fragments and maintainer skills (tools-registry-context, vendor-listing, etc.)
- `.claude-plugin/`, `.cursor-plugin/` — plugin marketplace manifests for Claude Code / Cursor
- `.claude/` — Claude Code local skill links
- `AGENTS.md` / `CLAUDE.md` — agent instruction entrypoints (CLAUDE.md points at AGENTS.md)
- `USAGE.md` — full CLI reference
- `design.md` / `design.cn.md` — UI/product design guidelines (not server architecture)
- `docs/` — onboarding, plugin docs, plans, and `docs/context/` design fragments (codemap)
- `examples/` — claude-code-mods (e.g. jev-memory), hub demos, proxy-demo
- `frontend/` — dashboard/frontend build inputs
- `plugin/` / `plugins/` — packaged agent plugins
- `skills/` — public workflow skills (treg, web-access, lead-signals, recruit, make-ugc, jev-memory, rea-growth)
- `src/treg/` — Python package (api, cli, proxy, injectors, oauth, mcp, hub, catalog, models, …)
- `tests/` — pytest suite
- `packages/npm/` — npm packaging
- `deploy/` — Render example deploy config
- `scripts/` — local-dev helpers (dev-local.sh, build-dashboard.sh)
- `pyproject.toml` / `uv.lock` — tools-registry package (CLI base; [server] and [proxy] extras)
- `alembic.ini` — DB migrations for server
