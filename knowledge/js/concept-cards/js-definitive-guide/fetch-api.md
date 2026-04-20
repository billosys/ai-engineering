---
concept: "fetch() API"
slug: fetch-api
category: browser-apis
subcategory: networking
tier: intermediate
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "JavaScript in Web Browsers"
chapter_number: 15
pdf_page: 535
section: "15.11.1 fetch()"
extraction_confidence: high
aliases:
  - Fetch API
  - window.fetch
prerequisites:
  - dom-tree
extends: []
related:
  - request-response-headers
  - server-sent-events
  - websocket
contrasts_with: []
answers_questions:
  - "How do I use fetch() to make HTTP requests?"
---

# Quick Definition

`fetch()` is a Promise-based API for making HTTP/HTTPS requests that returns a Response object with methods like `json()`, `text()`, and `blob()` for parsing the response body.

# Core Definition

Using `fetch()` is a three-step process: (1) call `fetch()` with a URL, (2) get the Response object when the HTTP response headers arrive, and (3) call a method on the Response to get the body. The API is entirely Promise-based. The Promise returned by `fetch()` resolves to a Response object even for HTTP error status codes (404, 500); it only rejects if the browser cannot contact the server at all. The `response.ok` property is true for status codes 200-299 (Flanagan, Ch. 15, pp. 535-545).

# Prerequisites

- **dom-tree** — fetch() is used in browser-side JavaScript (also available in Node 18+).

# Key Properties

1. Returns a Promise that resolves to a Response object.
2. Response body methods: `json()`, `text()`, `blob()`, `arrayBuffer()`, `formData()`.
3. Only rejects on network failure, not on HTTP error codes.
4. `response.ok` is true for 2xx status codes.
5. Second argument accepts options: `method`, `headers`, `body`, `signal` (for aborting).

# Construction / Recognition

```javascript
fetch("/api/users/current")
  .then(response => response.json())
  .then(currentUser => { displayUserInfo(currentUser); });

// With async/await:
let response = await fetch("/api/service/status");
let body = await response.text();
```

# Context & Application

The standard way to make HTTP requests from the browser. Replaces the older XMLHttpRequest API.

# Examples

From the source (p. 536):
```javascript
async function isServiceReady() {
  let response = await fetch("/api/service/status");
  let body = await response.text();
  return body === "ready";
}
```

# Relationships

## Builds Upon
- Promises (Ch. 13) — fetch() is Promise-based

## Enables
- **request-response-headers** — Detailed request/response manipulation

## Related
- **server-sent-events** — Alternative for server-push
- **websocket** — Alternative for bidirectional communication

## Contrasts With
- (XMLHttpRequest — older, replaced by fetch)

# Common Errors

- **Error**: Assuming `fetch()` rejects on 404 or 500 status codes.
  **Correction**: `fetch()` only rejects on network failure. Always check `response.ok` or `response.status`.

# Common Confusions

- **Confusion**: The response body is available immediately after `fetch()` resolves.
  **Clarification**: The Promise resolves when headers arrive. The body requires a second async step (`.json()`, `.text()`, etc.).

# Source Reference

Chapter 15: JavaScript in Web Browsers, Section 15.11.1, pages 535-545.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: Extensively covered with multiple examples
- Uncertainties: None
- Cross-reference status: Verified
