---
concept: Fetch API
slug: fetch-api
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
  - fetch function
  - fetch()
prerequisites:
  - promise
  - http
extends: []
related:
  - response-object
  - http-method
  - fetch-options
contrasts_with: []
answers_questions:
  - "How do I make an HTTP request with fetch?"
  - "How do I make HTTP requests from JavaScript?"
---

# Quick Definition
The `fetch` function is the browser's interface for making HTTP requests, returning a promise that resolves to a `Response` object containing the server's response status, headers, and body.

# Core Definition
"The interface through which browser JavaScript can make HTTP requests is called `fetch`" (Ch. 18, "Fetch"). Calling `fetch` returns a promise that "resolves to a `Response` object holding information about the server's response, such as its status code and its headers." The promise resolves successfully even for error status codes; it only rejects on network failures.

# Prerequisites
- **Promises**: fetch returns a promise
- **HTTP**: Understanding of request/response model

# Key Properties
1. First argument is the URL (absolute or relative)
2. Optional second argument is an options object (method, headers, body)
3. Returns a promise resolving to a Response object
4. Promise resolves even for 404/500 status codes
5. Body must be read separately via `.text()` or `.json()` (also returns promises)

# Construction / Recognition
```javascript
fetch("example/data.txt").then(response => {
  console.log(response.status);    // → 200
  console.log(response.headers.get("Content-Type"));
  // → text/plain
});
```

# Context & Application
The primary way to make HTTP requests from browser JavaScript. Used for loading data, submitting forms programmatically, communicating with APIs, and building single-page applications.

# Examples
Reading response body:
```javascript
fetch("example/data.txt")
  .then(resp => resp.text())
  .then(text => console.log(text));
```

Sending a DELETE request:
```javascript
fetch("example/data.txt", {method: "DELETE"}).then(resp => {
  console.log(resp.status); // → 405
});
```

# Relationships
## Builds Upon
- promise, http, url
## Enables
- AJAX, API communication, single-page applications
## Related
- response-object, http-method, fetch-options, json-in-http, cors
## Contrasts With
- XMLHttpRequest (older, callback-based)

# Common Errors
- **Error**: Assuming fetch rejects on 404 or 500 errors
  **Correction**: fetch only rejects on network errors; check response.status or response.ok

# Common Confusions
- **Confusion**: fetch() immediately gives you the response body
  **Clarification**: The initial promise gives you headers/status; body requires a second async call (.text() or .json())

# Source Reference
Chapter 18: HTTP and Forms, Section "Fetch", lines 265-362 of 18-http-and-forms.md.

# Verification Notes
- Definition source: direct from source text
- Confidence rationale: Thoroughly explained with multiple examples
- Cross-reference status: verified
