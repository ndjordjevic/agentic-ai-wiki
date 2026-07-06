# pushover.net

## Fetch log
- Inbox URL: https://pushover.net/
- Final URL: https://pushover.net/
- Fetched: 2026-07-06
- Pages: 4
- Mode: standard

## Landing page — https://pushover.net/

# Pushover: Simple Notifications Service

Pushover is a push notification platform offering apps for Android, iPhone, iPad, and Desktop devices. The service enables users to receive real-time alerts from integrated websites, services, and applications.

## Key Features

**Client Applications:**
- Android app (available on Google Play)
- iOS app (available on App Store)
- Desktop browser client
- Support for Android Wear and Apple Watch

**Pricing Model:**
The platform offers two options: a one-time in-app purchase after a 30-day free trial for individual users, or "Pushover for Teams"—a monthly per-user subscription for organizations requiring features like user management and automated onboarding.

## Developer Integration

The service provides an API accessible via standard HTTP libraries across multiple programming languages. The page demonstrates integration examples in Command Line, Python 3, Ruby, Go, Perl, and PHP, showing that sending notifications requires basic parameters like token, user identifier, and message content.

## Navigation & Resources

Main menu items include Clients, Integrations, Pricing, Teams, API, Blog, Help, and Login/Signup options. A recent announcement noted "API usage limit changes coming May 1st."

The footer contains links to Privacy policy, Terms of Service, and API Status page, along with social media presence on Bluesky.

## Docs — https://pushover.net/api

# Pushover API Documentation Summary

## Core API Overview

Pushover provides a straightforward REST API for sending push notifications. The service requires no complex authentication like OAuth—standard HTTP requests work fine.

## Essential Requirements

To use the API, you need:

1. **Application Token**: Obtained by registering your app (free). The example format shows "azGDORePK8gMaC0QOYAMyEEuzJnyUi"—30 characters, case-sensitive, alphanumeric only.

2. **User Key**: The recipient's identifier, viewable in the Pushover dashboard. Format matches the token specification.

3. **Message Content**: Required message body with optional title.

## Basic API Call

POST to `https://api.pushover.net/1/messages.json` with these minimum parameters:
- `token` (your app token)
- `user` (recipient key)
- `message` (notification text)

The endpoint accepts responses in JSON (`.json`) or XML (`.xml`) format.

## Notable Features

**Message Formatting**: Supports HTML tags (bold, italics, underline, colored text, links) via `html=1` parameter, or monospace text via `monospace=1`.

**Priority Levels**: Range from -2 (lowest) to 2 (emergency), with emergency requiring `retry` and `expire` parameters for repeated delivery until acknowledged.

**Attachments**: Single image per message, max 5MB, sent via `multipart/form-data` or Base64 encoding.

**Rate Limits**: Free accounts get 10,000 messages monthly; teams receive 25,000. Exceeding limits returns HTTP 429 status.

## API Response

Successful requests return HTTP 200 with `{"status":1}`. Invalid requests return 4xx status with error details in an `errors` array.

## Clients — https://pushover.net/clients

# Pushover Device Clients - Content Summary

Pushover offers three main device client platforms:

**Android Client**
"uses Google's secure push notification service for instant delivery of Pushover messages" and requires Android 6+. It includes a home screen widget and Tasker action plugin support. Available free on Google Play with a 30-day trial.

**iOS Client**
Supports "iPhone and iPad devices running iOS 11 or higher" and utilizes Apple's push notification service. Features include background updates, notification actions for URLs and message acknowledgment, an Apple Watch app, and Watch face complications via the Glances API. Available free in the App Store with a 30-day trial.

**Desktop Client**
Works with "Chrome, Firefox, and Safari" browsers using a bandwidth-efficient real-time push mechanism. On macOS, notifications can reach the desktop directly without a browser running. Available free at their website with a 30-day trial.

All three platforms emphasize secure, instant message delivery without battery drain from polling services.

## Support / FAQ — https://support.pushover.net/

# Pushover Support Knowledge Base Overview

The Pushover Support portal organizes help content into nine main categories:

## Knowledge Base Categories

**Common Problems** (9 articles) covers issues like offline devices, delayed notifications, sound/vibration problems, and duplicate messages.

**General Questions** (8 articles) addresses "What is Pushover and how do I use it?" plus pricing, multi-device viewing, and app integration capabilities.

**API/Integration** (9 articles) includes guidance on obtaining tokens, code examples, message limitations, and getting listed on their public applications page.

**Licensing/Buying** (5 articles) handles in-app purchases, device limits, purchasing for others, and trial period issues.

**iPhone/iPad/Apple Watch** (5 articles) focuses on notification delivery with wearables, shortcuts, and encrypted message displays.

**Android** (4 articles) covers Do Not Disturb overrides, device compatibility, and the Tasker plugin.

**Desktop/Browser** (7 articles) addresses the desktop application, browser permissions, and sound issues across platforms.

**Email Gateway** (2 articles) explains sending notifications via email and timestamp corrections.

**Other** (7 articles) includes account deletion, security reporting, encryption details, and logo usage guidelines.

The site also features a separate **Top Ideas** section showcasing feature requests with community support counts.
