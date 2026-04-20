---
concept: Response Object
slug: response-object
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
  - HTTP response
  - fetch response
prerequisites:
  - fetch-api
  - promise
extends: []
related:
  - http-status-code
  - json-in-http
contrasts_with: []
answers_questions:
  - "How do I read a fetch response?"
  - "What information does an HTTP response contain?"
---

# Quick Definition
The Response object, returned by `fetch`, provides access to the HTTP response's status code, headers, and body, with async methods like `.text()` and `.json()` to read the body content.

# Core Definition
"Calling `fetch` returns a promise that resolves to a `Response` object holding information about the server's response, such as its status code and its headers" (Ch. 18). The body is read asynchronously: "To get at the actual content of a response, you can use its `text` method. Because [...] reading the response body might take a while longer, this again returns a promise."

# Prerequisites
- **Fetch API**: Response is returned by fetch
- **Promises**: Body methods return promises

# Key Properties
1. `status` -- numeric HTTP status code (200, 404, etc.)
2. `headers` -- case-insensitive Map-like object
3. `.text()` -- returns promise resolving to body as string
4. `.json()` -- returns promise resolving to parsed JSON
5. Promise from fetch resolves even on error status codes

# Construction / Recognition
```javascript
fetch("example/data.txt")
  .then(resp => resp.text())
  .then(text => console.log(text));

// JSON response
fetch("api/data")
  .then(resp => resp.json())
  .then(data => console.log(data));
```

# Context & Application
Every fetch call returns a Response. Understanding its two-phase reading (headers first, then body) is essential for proper async programming.

# Examples
Checking status and reading JSON:
```javascript
let response = await fetch("api/data");
if (response.ok) {
  let data = await response.json();
}
```

# Relationships
## Builds Upon
- fetch-api, promise
## Enables
- Reading API data, error handling, content processing
## Related
- http-status-code, json-in-http, request-headers
## Contrasts With
- Node.js response streams (different API)

# Common Errors
- **Error**: Calling .json() on a non-JSON response
  **Correction**: Check Content-Type header or use try/catch; .json() rejects on invalid JSON

# Common Confusions
- **Confusion**: response.text() and response.json() can both be called on the same response
  **Clarification**: The body can only be consumed once; calling text() then json() will fail

# Source Reference
Chapter 18: HTTP and Forms, Section "Fetch", lines 269-324 of 18-http-and-forms.md.

# Verification Notes
- Definition source: direct from source text
- Confidence rationale: Thoroughly explained
- Cross-reference status: verified
