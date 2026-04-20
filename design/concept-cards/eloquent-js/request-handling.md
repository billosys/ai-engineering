---
concept: Request Handling
slug: request-handling
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
  - incoming request
  - request object
prerequisites:
  - http-createserver
extends: []
related:
  - response-writing
  - stream
contrasts_with: []
answers_questions:
  - "How do I read an HTTP request in Node.js?"
---

# Quick Definition
The request object in Node's HTTP server provides the request URL (`url`), HTTP method (`method`), and headers, and acts as a readable stream for the request body.

# Core Definition
"The first contains information about the request, such as its `url` property, which tells us to what URL the request was made" (Ch. 20). The request object is also a readable stream, enabling reading of POST/PUT bodies via "data" and "end" events.

# Prerequisites
- **createServer**: Request objects come from the server handler

# Key Properties
1. `request.url` -- the requested path (e.g., "/hello")
2. `request.method` -- HTTP method ("GET", "POST", etc.)
3. `request.headers` -- object of header key/value pairs (lowercase keys)
4. Readable stream -- read body via "data" and "end" events

# Construction / Recognition
```javascript
createServer((request, response) => {
  console.log(request.method, request.url);
  request.on("data", chunk => { /* process body */ });
  request.on("end", () => { /* body complete */ });
});
```

# Context & Application
Every server handler needs to inspect the request to determine what to do. Method and URL drive routing; headers and body provide additional data.

# Examples
The uppercase echo server:
```javascript
createServer((request, response) => {
  response.writeHead(200, {"Content-Type": "text/plain"});
  request.on("data", chunk =>
    response.write(chunk.toString().toUpperCase()));
  request.on("end", () => response.end());
}).listen(8000);
```

# Relationships
## Builds Upon
- http-createserver
## Enables
- Routing, body parsing, authentication
## Related
- response-writing, stream, server-routing
## Contrasts With
- Browser Request object (from Fetch API)

# Common Errors
- **Error**: Trying to read request body synchronously
  **Correction**: Request body is a stream; use events or stream/consumers helpers

# Common Confusions
- **Confusion**: request.url contains the full URL with protocol and host
  **Clarification**: It contains only the path portion (e.g., "/talks/Unituning")

# Source Reference
Chapter 20: Node.js, Section "The HTTP module", lines 486-544; "Streams", lines 546-616 of 20-nodejs.md.

# Verification Notes
- Definition source: direct from source text
- Confidence rationale: Used in multiple server examples
- Cross-reference status: verified
