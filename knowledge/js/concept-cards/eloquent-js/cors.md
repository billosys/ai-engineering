---
concept: CORS
slug: cors
category: http-forms
subcategory: security
tier: intermediate
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "HTTP and Forms"
chapter_number: 18
pdf_page: null
section: "HTTP sandboxing"
extraction_confidence: high
aliases:
  - Cross-Origin Resource Sharing
  - same-origin policy
prerequisites:
  - fetch-api
  - http
extends: []
related:
  - request-headers
contrasts_with: []
answers_questions:
  - "Why can't my JavaScript fetch data from another domain?"
  - "What is CORS?"
---

# Quick Definition
CORS (Cross-Origin Resource Sharing) is a security mechanism where browsers block scripts from making HTTP requests to domains different from the page's origin, unless the server explicitly permits it via the `Access-Control-Allow-Origin` header.

# Core Definition
"Browsers protect us by disallowing scripts to make HTTP requests to other domains" (Ch. 18, "HTTP sandboxing"). Servers can opt in to cross-origin requests: "servers can include a header like this in their response to explicitly indicate to the browser that it is okay for the request to come from another domain: `Access-Control-Allow-Origin: *`."

# Prerequisites
- **Fetch API**: CORS restrictions apply to fetch and XMLHttpRequest
- **HTTP**: Understanding of request/response headers

# Key Properties
1. Browser enforces same-origin policy by default
2. Server must send `Access-Control-Allow-Origin` header to allow cross-origin requests
3. `*` allows all origins; specific origin restricts to one domain
4. Applies to JavaScript-initiated requests, not HTML elements like `<img>` or `<script>`

# Construction / Recognition
Server response header:
```http
Access-Control-Allow-Origin: *
```

# Context & Application
CORS affects any web application that communicates with APIs on different domains. Understanding it is essential for API design and debugging "blocked by CORS policy" errors.

# Examples
"If I visit themafia.org, I do not want its scripts to be able to make a request to mybank.com, using identifying information from my browser."

# Relationships
## Builds Upon
- fetch-api, http, request-headers
## Enables
- Cross-domain API access, third-party integrations
## Related
- request-headers
## Contrasts With
- Server-to-server requests (no CORS restrictions)

# Common Errors
- **Error**: Adding CORS headers on the client side
  **Correction**: CORS headers must be set by the server, not the client

# Common Confusions
- **Confusion**: CORS blocks all cross-origin requests
  **Clarification**: It blocks JavaScript-initiated requests; images, scripts, and form submissions are not blocked

# Source Reference
Chapter 18: HTTP and Forms, Section "HTTP sandboxing", lines 364-389 of 18-http-and-forms.md.

# Verification Notes
- Definition source: direct from source text
- Confidence rationale: Clearly explained with motivation
- Cross-reference status: verified
