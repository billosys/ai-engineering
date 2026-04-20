---
concept: Response Writing
slug: response-writing
category: server-side
subcategory: node-modules
tier: intermediate
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Node.js"
chapter_number: 20
pdf_page: null
section: "The HTTP module"
extraction_confidence: high
aliases:
  - response object
  - writeHead
prerequisites:
  - http-createserver
extends: []
related:
  - request-handling
  - stream
contrasts_with: []
answers_questions:
  - "How do I send an HTTP response in Node.js?"
---

# Quick Definition
The response object provides `writeHead(status, headers)` to set status and headers, `write(data)` to send body chunks, and `end()` to complete the response, acting as a writable stream.

# Core Definition
"To send something to the client, you call methods on the `response` object. The first, `writeHead`, will write out the response headers. You give it the status code (200 for 'OK') and an object that contains header values. [...] the actual response body is sent with `response.write`. [...] `response.end` signals the end of the response" (Ch. 20).

# Prerequisites
- **createServer**: Response objects come from the server handler

# Key Properties
1. `writeHead(statusCode, headers)` -- set status and headers
2. `write(chunk)` -- send body data (can call multiple times)
3. `end(data?)` -- finish response (optionally with final data)
4. Is a writable stream -- supports pipe()

# Construction / Recognition
```javascript
response.writeHead(200, {"Content-Type": "text/html"});
response.write(`<h1>Hello!</h1>`);
response.end();
```

Piping a file stream:
```javascript
if (body?.pipe) body.pipe(response);
else response.end(body);
```

# Context & Application
Every HTTP response in Node uses these methods. Streaming responses (piping file content) are efficient for large files.

# Examples
From the file server: "When the value of `body` is a readable stream, it will have a `pipe` method that we can use to forward all content from a readable stream to a writable stream."

# Relationships
## Builds Upon
- http-createserver
## Enables
- HTTP responses, file serving, API responses
## Related
- request-handling, stream, http-status-code
## Contrasts With
- Browser Response object (read-only, from fetch)

# Common Errors
- **Error**: Writing to response after calling end()
  **Correction**: Once end() is called, the response is finished; no more writes allowed

# Common Confusions
- **Confusion**: writeHead must be called before write
  **Clarification**: Headers are sent with the first write if writeHead wasn't called; best to call writeHead explicitly

# Source Reference
Chapter 20: Node.js, Section "The HTTP module", lines 501-515 of 20-nodejs.md.

# Verification Notes
- Definition source: direct from source text
- Confidence rationale: Clearly explained step-by-step
- Cross-reference status: verified
