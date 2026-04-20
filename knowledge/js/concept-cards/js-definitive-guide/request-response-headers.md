---
concept: Request, Response, and Headers Objects
slug: request-response-headers
category: browser-apis
subcategory: networking
tier: intermediate
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "JavaScript in Web Browsers"
chapter_number: 15
pdf_page: 537
section: "15.11.1 fetch()"
extraction_confidence: high
aliases:
  - Response object
  - Request object
  - Headers object
prerequisites:
  - fetch-api
extends:
  - fetch-api
related: []
contrasts_with: []
answers_questions:
  - "How do I use fetch() to make HTTP requests?"
---

# Quick Definition

The fetch API uses three key objects: `Request` (encapsulating URL and options), `Response` (status, headers, and body), and `Headers` (a case-insensitive map of HTTP headers with `has()`, `get()`, and iterable interface).

# Core Definition

The Response object has properties including `status` (HTTP code), `statusText`, `ok` (true for 2xx), and `headers` (a Headers object). The Headers object provides `has()` and `get()` for header access and is iterable. A Request object can be created with `new Request(url, options)` and passed to `fetch()`. The options object supports `method`, `headers`, `body`, `cache`, `redirect`, `referrer`, and `signal` (for abort control) (Flanagan, Ch. 15, pp. 537-545).

# Prerequisites

- **fetch-api** — These objects are the building blocks of the fetch API.

# Key Properties

1. `Response.status`: HTTP status code (200, 404, etc.).
2. `Response.ok`: true if status is 200-299.
3. `Response.headers`: a Headers object.
4. `Headers.get(name)`: case-insensitive header lookup.
5. `Request(url, options)`: constructs a reusable request object.
6. Options include `method`, `headers`, `body`, `signal`, `cache`, `redirect`.

# Construction / Recognition

```javascript
let authHeaders = new Headers();
authHeaders.set("Authorization", `Basic ${btoa(`${username}:${password}`)}`);
fetch("/api/users/", { headers: authHeaders })
  .then(response => response.json());
```

# Context & Application

Used when you need fine-grained control over HTTP requests: setting custom headers, specifying request methods (POST, PUT, DELETE), or uploading request bodies.

# Examples

From the source (p. 538):
```javascript
fetch(url, {
  method: "POST",
  headers: new Headers({"Content-Type": "application/json"}),
  body: JSON.stringify(requestBody)
})
```

# Relationships

## Builds Upon
- **fetch-api** — These are the core objects of the fetch API

## Enables
- Cross-origin requests via CORS headers
- File uploads via FormData body

## Related
- (None)

## Contrasts With
- (None)

# Common Errors

- **Error**: Setting "Content-Type" for string bodies but forgetting units or format.
  **Correction**: When sending JSON, always set `Content-Type: application/json` explicitly.

# Common Confusions

- **Confusion**: You must always create Request objects.
  **Clarification**: Passing a URL string and options object directly to `fetch()` works fine. Request objects are optional.

# Source Reference

Chapter 15: JavaScript in Web Browsers, Section 15.11.1, pages 537-545.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: Detailed coverage of all options
- Uncertainties: None
- Cross-reference status: Verified
