---
concept: HTTP Module
slug: http-module
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
  - node:http
prerequisites:
  - nodejs
  - http
extends: []
related:
  - http-createserver
  - request-handling
  - response-writing
  - stream
contrasts_with: []
answers_questions:
  - "How do I create an HTTP server in Node.js?"
  - "What is the Node.js http module?"
---

# Quick Definition
The `node:http` module provides functionality for creating HTTP servers and making HTTP requests in Node.js, with `createServer` as the primary method for building servers.

# Core Definition
"Another central module is called `node:http`. It provides functionality for running an HTTP server" (Ch. 20). The module also has a `request` function for making HTTP requests, though `fetch` (available globally in modern Node) is recommended for most use cases.

# Prerequisites
- **Node.js**: node:http is a built-in module
- **HTTP**: Understanding of the HTTP protocol

# Key Properties
1. `createServer(handler)` -- creates an HTTP server
2. `server.listen(port)` -- starts listening for connections
3. Handler receives `(request, response)` objects
4. Also provides `request()` for client-side HTTP (but prefer `fetch`)

# Construction / Recognition
```javascript
import {createServer} from "node:http";
let server = createServer((request, response) => {
  response.writeHead(200, {"Content-Type": "text/html"});
  response.write(`<h1>Hello!</h1>`);
  response.end();
});
server.listen(8000);
```

# Context & Application
The foundation for building web servers, API servers, and microservices in Node.js. Most Node web frameworks (Express, Koa) build on top of this module.

# Examples
"If you run this script on your own machine, you can point your web browser at http://localhost:8000/hello to make a request to your server."

# Relationships
## Builds Upon
- nodejs, http
## Enables
- Web servers, API servers, file servers
## Related
- http-createserver, request-handling, response-writing, stream
## Contrasts With
- Browser fetch API (client-side only)

# Common Errors
- **Error**: Forgetting to call response.end()
  **Correction**: Always call end() to complete the response; otherwise the connection hangs

# Common Confusions
- **Confusion**: node:http and fetch serve the same purpose
  **Clarification**: node:http creates servers; fetch makes client requests. fetch is also available in Node globally.

# Source Reference
Chapter 20: Node.js, Section "The HTTP module", lines 458-544 of 20-nodejs.md.

# Verification Notes
- Definition source: direct from source text
- Confidence rationale: Core server creation explained
- Cross-reference status: verified (used extensively in Ch. 21)
