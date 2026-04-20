---
concept: HTTP Status Code
slug: http-status-code
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
  - status code
  - response code
prerequisites:
  - http
extends: []
related:
  - response-object
  - http-method
contrasts_with: []
answers_questions:
  - "What are HTTP status codes?"
  - "What does a 404 or 200 status mean?"
---

# Quick Definition
HTTP status codes are three-digit numbers in the server's response indicating the outcome: 2xx for success, 4xx for client errors, and 5xx for server errors.

# Core Definition
"Status codes starting with a 2 indicate that the request succeeded. Codes starting with 4 mean there was something wrong with the request. The most famous HTTP status code is probably 404, which means that the resource could not be found. Codes that start with 5 mean an error happened on the server and the request is not to blame" (Ch. 18, "The protocol").

# Prerequisites
- **HTTP**: Status codes are part of HTTP responses

# Key Properties
1. 200 -- OK (success)
2. 204 -- No Content (success, no body)
3. 304 -- Not Modified (conditional request, use cache)
4. 404 -- Not Found
5. 405 -- Method Not Allowed
6. 500 -- Internal Server Error

# Construction / Recognition
```http
HTTP/1.1 200 OK
```
```http
HTTP/1.1 404 Not Found
```

# Context & Application
Every HTTP response includes a status code. Proper handling of status codes is essential for robust web applications.

# Examples
The 405 code in practice:
```javascript
fetch("example/data.txt", {method: "DELETE"}).then(resp => {
  console.log(resp.status); // → 405
});
```
"The 405 status code means 'method not allowed', an HTTP server's way of saying 'I'm afraid I can't do that.'"

# Relationships
## Builds Upon
- http
## Enables
- Error handling, conditional requests, caching
## Related
- response-object, fetch-api, etag
## Contrasts With
- Application-level error codes (custom error objects in response body)

# Common Errors
- **Error**: Not checking status codes after fetch
  **Correction**: Always check response.status or response.ok since fetch doesn't reject on 4xx/5xx

# Common Confusions
- **Confusion**: A 200 response always means everything is fine
  **Clarification**: The request succeeded, but the data may still indicate a logical error

# Source Reference
Chapter 18: HTTP and Forms, Section "The protocol", lines 119-164 of 18-http-and-forms.md.

# Verification Notes
- Definition source: direct from source text
- Confidence rationale: Multiple codes explained
- Cross-reference status: verified (also used in Ch. 20, 21)
