---
concept: Fetch Options
slug: fetch-options
category: http-forms
subcategory: network
tier: intermediate
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "HTTP and Forms"
chapter_number: 18
pdf_page: null
section: "Fetch"
extraction_confidence: high
aliases:
  - fetch configuration
  - request options
prerequisites:
  - fetch-api
extends: []
related:
  - http-method
  - request-headers
  - json-in-http
contrasts_with: []
answers_questions:
  - "How do I configure fetch requests with custom methods, headers, and body?"
---

# Quick Definition
The optional second argument to `fetch` is an options object that configures the request method, headers, body, and other settings like credentials and mode.

# Core Definition
"By default, `fetch` uses the `GET` method to make its request and does not include a request body. You can configure it differently by passing an object with extra options as a second argument" (Ch. 18, "Fetch"). Options include `method`, `headers`, and `body`.

# Prerequisites
- **Fetch API**: Options are passed to fetch

# Key Properties
1. `method` -- HTTP method string ("GET", "POST", "PUT", "DELETE")
2. `headers` -- object with header name/value pairs
3. `body` -- request body (string, FormData, etc.)
4. Default method is GET with no body

# Construction / Recognition
```javascript
fetch("example/data.txt", {method: "DELETE"});

fetch("example/data.txt", {headers: {Range: "bytes=8-19"}})
  .then(resp => resp.text());

fetch(url, {
  method: "PUT",
  headers: {"Content-Type": "application/json"},
  body: JSON.stringify(data)
});
```

# Context & Application
Any non-GET fetch request requires options. All API interactions that send data or use non-default methods need this configuration.

# Examples
"To add a request body for a `PUT` or `POST` request, you can include a `body` option. To set headers, there's the `headers` option."

# Relationships
## Builds Upon
- fetch-api
## Enables
- Sending data, custom headers, non-GET requests
## Related
- http-method, request-headers, json-in-http
## Contrasts With
- Default GET request (no options needed)

# Common Errors
- **Error**: Sending a body with a GET request
  **Correction**: GET and DELETE typically don't have bodies; use POST or PUT

# Common Confusions
- **Confusion**: Headers option replaces all headers
  **Clarification**: It adds to browser-provided headers; the browser still sends Host, etc.

# Source Reference
Chapter 18: HTTP and Forms, Section "Fetch", lines 327-362 of 18-http-and-forms.md.

# Verification Notes
- Definition source: direct from source text
- Confidence rationale: All options explained
- Cross-reference status: verified
