# hunter.io

## Fetch log
- Inbox URL: https://hunter.io/
- Final URL: https://hunter.io/
- Fetched: 2026-06-15
- Pages: 6
- Mode: standard

## Landing page — https://hunter.io/

Hunter is an all-in-one email outreach platform for finding and connecting with professional contacts. The platform serves over 7 million users and is trusted by companies like Canva, Semrush, and Vimeo.

**Core Offering:** Hunter is described as "your all-in-one email outreach platform" for finding and connecting with professional contacts.

**Email Discovery Tools:**
- Domain Search: Find contacts from company websites
- Email Finder: Locate verified email addresses by name
- Email Verifier: Validate addresses to prevent bounce-backs
- B2B Database: Identify leads based on customer profiles

**Outreach Capabilities:**
- Email Sequences for personalized cold email campaigns
- Native CRM integrations, Zapier, and API connections
- Sends through users' own Gmail, Google Workspace, or Outlook accounts

**Data Platform:** Bulk access to email data via API or task-based system for enterprises.

**Browser Extension:** Available for Chrome with 4.7 stars from 12,000+ reviews and 600,000+ users.

**Credibility Indicators:**
- G2 Leader certification (4.4/5 rating)
- Capterra: 4.6/5 rating
- Customer testimonials from executives at Lattice, Acquire.com, and SparkToro

**Compliance:** Hunter emphasizes data sourcing transparency and adherence to data protection regulations.

**Pricing:** Free plan available; no credit card required.

## Docs — https://hunter.io/api-documentation

Hunter API V2 provides developers with access to email discovery, verification, and enrichment services through REST endpoints.

**Core Features — five main capabilities:**
1. **Discover** — Returns companies matching specified criteria (free)
2. **Domain Search** — Finds all email addresses for a given domain
3. **Email Finder** — Locates the most probable email address using domain, first name, and last name
4. **Email Verifier** — Checks deliverability and validates email addresses
5. **Enrichment** — Retrieves comprehensive information about people and companies

**API Structure:** Responses follow a consistent JSON format with `data`, `meta`, and optional `error` sections. The base endpoint is `https://api.hunter.io/v2/`

**Authentication:** Developers must include an API key via:
- Query parameter: `api_key`
- Header: `X-API-KEY`
- Authorization header: `Bearer YOUR_API_KEY`

A test key (`test-api-key`) validates parameters while returning dummy responses.

**Key Endpoints:**
- **Discover**: POST request with natural language or filter parameters
- **Domain Search**: GET with domain/company name, returning up to 100 emails per request
- **Email Finder**: GET requiring domain/company plus name information
- **Email Verifier**: GET for deliverability checks
- **Enrichment**: Separate endpoints for people, companies, or combined lookups

**Rate Limiting:**
- Discover: 5 requests/second, 50/minute
- Domain Search & Email Finder: 15 requests/second, 500/minute
- Email Verifier: 10 requests/second, 300/minute

**Resource Management:** The API supports CRUD operations for leads, custom attributes, lead lists, and email sequences, all available without charge.

## Domain Search — https://hunter.io/domain-search

Hunter offers a web-based email discovery tool accessible at hunter.io/domain-search. The service enables users to "Find email addresses from any company name or website."

**Key Features:**
- Email address discovery with confidence scoring
- Department filtering capabilities
- Source attribution for found addresses
- Bulk domain search functionality
- API access for automated queries
- Browser extension for Chrome

**Pricing & Access:** Users receive a free tier with "up to 50 searches/month" after account creation. The service operates on a search credit system where "one search credit is counted for up to 10 emails found for a single domain."

**Data Verification:** Hunter distinguishes between verified addresses (recently validated) and unverified addresses returned with confidence scores. The platform sources all addresses from "public sources on the web, along with their discovery dates."

## Email Finder — https://hunter.io/email-finder

Hunter's email discovery tool where users input a professional's name and company domain to "find the verified email address of any professional" in seconds.

**Key Features:**
- Email Finder locates professional contact information by combining email formats, web-discovered addresses, and verification status
- Bulk Email Finder for CSV uploads
- Email Finder API for product integration
- Google Sheets add-on
- Reverse Email Lookup (opposite function)

**Technical Details:** The tool searches a database exceeding "one hundred million professional email addresses," with results including verification status, confidence scores, and discovery sources when applicable.

**Compliance:** The service claims GDPR compliance, applying EU data requirements "broadly to cover our entire database."

## Email Verifier — https://hunter.io/email-verifier

Hunter's email verification tool that checks email addresses for validity and deliverability. The service performs comprehensive checks including format validation, domain information verification, SMTP server responses, and accept-all address detection.

**Key Features:**
- Format, domain, and server response validation
- Accept-all (catch-all) verification using proprietary technology
- No signup required for basic verification

**Use Cases:** The tool serves sales teams, marketers, recruiters, founders, PR professionals, and event organizers. Common applications include cleaning prospect lists, preventing bounce-related deliverability issues, protecting sender reputation, and validating form submissions.

**Availability:** Free plan allowing up to 100 email verifications monthly. Additional offerings include bulk verification, API access, Google Sheets integration, and CRM integrations with platforms like HubSpot and Pipedrive.

## Pricing — https://hunter.io/pricing

Hunter offers five subscription tiers for their all-in-one outreach platform:

**Free Plan (€0)**
- 50 monthly credits
- Basic Discover filters
- 1 connected email account
- 500 recipients per sequence
- Unlimited team members

**Starter Plan (€49/month, €34/month yearly)**
- 2,000 monthly credits (24,000 yearly)
- Advanced Discover filters
- 3 connected email accounts
- AI Writing Assistant
- Priority support

**Growth Plan (€149/month, €104/month yearly)**
- 10,000 monthly credits (120,000 yearly)
- Advanced Discover filters
- 10 connected email accounts
- AI Writing Assistant
- Priority support

**Scale Plan (€299/month, €209/month yearly)**
- 25,000 monthly credits (300,000 yearly)
- 20 connected email accounts
- Advanced features across all tools
- Priority support

**Enterprise (Custom pricing)**
- Custom credit allocation
- Dedicated account manager
- Priority support plus personalized assistance

All paid plans include auto-verification, lead enrichment, unlimited users, and CSV export.
