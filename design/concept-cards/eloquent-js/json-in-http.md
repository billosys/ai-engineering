---
concept: JSON in HTTP
slug: json-in-http
category: http-forms
subcategory: data-format
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
  - JSON response
  - JSON API
prerequisites:
  - fetch-api
  - response-object
extends: []
related:
  - content-type
  - rest-api
contrasts_with: []
answers_questions:
  - "How do I work with JSON in HTTP requests and responses?"
  - "How do I parse a JSON response from fetch?"
---

# Quick Definition
JSON (JavaScript Object Notation) is the standard data interchange format for HTTP APIs, read from responses via `response.json()` and sent in request bodies with the appropriate Content-Type header.

# Core Definition
The Response object's `json` method "returns a promise that resolves to the value you get when parsing the body as JSON or rejects if it's not valid JSON" (Ch. 18). When sending JSON, include `Content-Type: application/json` and use `JSON.stringify` for the body.

# Prerequisites
- **Fetch API**: For making requests
- **Response object**: For reading JSON responses

# Key Properties
1. `response.json()` parses response body as JSON (returns promise)
2. Send JSON body with `body: JSON.stringify(data)`
3. Set `Content-Type: application/json` header when sending JSON
4. JSON is the dominant data format for web APIs

# Construction / Recognition
Reading JSON:
```javascript
fetch("api/data").then(resp => resp.json()).then(data => {
  console.log(data);
});
```

Sending JSON:
```javascript
fetch(url, {
  method: "PUT",
  headers: {"Content-Type": "application/json"},
  body: JSON.stringify({presenter: "Maureen", summary: "..."})
});
```

# Context & Application
Used for virtually all modern web API communication. REST APIs typically exchange JSON documents for creating, reading, updating, and deleting resources.

# Examples
From Ch. 18: "Another approach is to build your communication around the concept of resources and HTTP methods. Instead of a remote procedure called `addUser`, you use a `PUT` request to `/users/larry`. [...] you define a JSON document format that represents a user."

# Relationships
## Builds Upon
- fetch-api, response-object
## Enables
- REST APIs, client-server communication, data exchange
## Related
- content-type, rest-api, http-method
## Contrasts With
- Form-encoded data (application/x-www-form-urlencoded)

# Common Errors
- **Error**: Forgetting Content-Type header when sending JSON
  **Correction**: Always include `"Content-Type": "application/json"` in request headers

# Common Confusions
- **Confusion**: response.json() returns the parsed object directly
  **Clarification**: It returns a promise that resolves to the parsed object

# Source Reference
Chapter 18: HTTP and Forms, Section "Fetch", lines 321-324; Section "Appreciating HTTP", lines 391-428 of 18-http-and-forms.md.

# Verification Notes
- Definition source: synthesized from multiple sections
- Confidence rationale: Core concept used throughout Ch. 18-21
- Cross-reference status: verified (Ch. 20, 21 use JSON extensively)
