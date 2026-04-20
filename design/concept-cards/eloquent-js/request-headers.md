---
concept: Request and Response Headers
slug: request-headers
category: http-forms
subcategory: protocol
tier: intermediate
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "HTTP and Forms"
chapter_number: 18
pdf_page: null
section: "The protocol"
extraction_confidence: high
aliases:
  - HTTP headers
  - response headers
prerequisites:
  - http
extends: []
related:
  - http-method
  - content-type
  - fetch-options
contrasts_with: []
answers_questions:
  - "What are HTTP headers?"
  - "How do I set custom headers with fetch?"
---

# Quick Definition
HTTP headers are `name: value` pairs included in requests and responses that provide metadata such as content type, content length, authentication tokens, and caching directives.

# Core Definition
"The first line of a request or response may be followed by any number of headers. These are lines in the form `name: value` that specify extra information about the request or response" (Ch. 18, "The protocol"). Headers like `Content-Type` tell the browser how to interpret the response. Headers in the Response object are accessed via a case-insensitive Map-like object.

# Prerequisites
- **HTTP**: Headers are part of the HTTP protocol

# Key Properties
1. Format: `Name: value` pairs
2. Case-insensitive names
3. Some are required (Content-Type in responses)
4. Browser adds some automatically (Host, etc.)
5. Custom headers can be set via fetch's `headers` option

# Construction / Recognition
```http
Content-Length: 87320
Content-Type: text/html
Last-Modified: Fri, 13 Oct 2023 10:05:41 GMT
```

Setting headers with fetch:
```javascript
fetch("example/data.txt", {headers: {Range: "bytes=8-19"}})
  .then(resp => resp.text())
  .then(console.log);
```

# Context & Application
Essential for API communication, authentication, content negotiation, caching, and CORS. Every HTTP interaction involves headers.

# Examples
Reading response headers:
```javascript
fetch("example/data.txt").then(response => {
  console.log(response.headers.get("Content-Type"));
  // → text/plain
});
```

# Relationships
## Builds Upon
- http
## Enables
- Content type negotiation, authentication, caching, cors
## Related
- content-type, fetch-options, etag
## Contrasts With
- Request body (headers are metadata; body is content)

# Common Errors
- **Error**: Treating header names as case-sensitive
  **Correction**: HTTP header names are case-insensitive

# Common Confusions
- **Confusion**: All headers can be set by client JavaScript
  **Clarification**: Browsers restrict certain headers for security; some can only be set by the browser

# Source Reference
Chapter 18: HTTP and Forms, Section "The protocol", lines 136-164, and Section "Fetch", lines 344-362 of 18-http-and-forms.md.

# Verification Notes
- Definition source: direct from source text
- Confidence rationale: Multiple examples provided
- Cross-reference status: verified
