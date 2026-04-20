---
concept: Content-Type Header
slug: content-type
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
  - MIME type
  - media type
prerequisites:
  - request-headers
extends: []
related:
  - json-in-http
  - http-method
contrasts_with: []
answers_questions:
  - "What is the Content-Type header?"
  - "How does the browser know how to display a response?"
---

# Quick Definition
The `Content-Type` header specifies the media type (MIME type) of an HTTP message body, telling the recipient how to interpret the content (e.g., `text/html`, `application/json`, `text/plain`).

# Core Definition
"Without a `Content-Type` header in the response, the browser won't know how to display the document" (Ch. 18, "The protocol"). Common types include `text/html` for web pages, `application/json` for API data, and `application/x-www-form-urlencoded` for form submissions.

# Prerequisites
- **HTTP headers**: Content-Type is an HTTP header

# Key Properties
1. Required for responses with a body
2. `text/html` -- HTML documents
3. `application/json` -- JSON data
4. `text/plain` -- plain text
5. `application/x-www-form-urlencoded` -- form data

# Construction / Recognition
```http
Content-Type: text/html
```

```javascript
fetch(url, {
  method: "POST",
  headers: {"Content-Type": "application/json"},
  body: JSON.stringify(data)
});
```

# Context & Application
Every HTTP response with a body should include Content-Type. When sending JSON to a server, always set the Content-Type header to `application/json`.

# Examples
From Chapter 20, the file server uses the `mime-types` package to set Content-Type:
```javascript
return {body: createReadStream(path), type: lookup(path)};
```

# Relationships
## Builds Upon
- request-headers
## Enables
- Proper content interpretation, JSON APIs, file serving
## Related
- json-in-http, http-method
## Contrasts With
- File extension (a hint, not a protocol-level declaration)

# Common Errors
- **Error**: Sending JSON without setting Content-Type
  **Correction**: Always include `"Content-Type": "application/json"` when sending JSON

# Common Confusions
- **Confusion**: Content-Type and file extension always match
  **Clarification**: Content-Type is the authoritative indicator; file extensions are just conventions

# Source Reference
Chapter 18: HTTP and Forms, Section "The protocol", lines 148-157 of 18-http-and-forms.md.

# Verification Notes
- Definition source: direct from source text
- Confidence rationale: Mentioned in multiple contexts
- Cross-reference status: verified (Ch. 18, 20, 21)
