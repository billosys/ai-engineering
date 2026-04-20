---
concept: createServer
slug: http-createserver
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
  - http.createServer
prerequisites:
  - http-module
extends:
  - http-module
related:
  - request-handling
  - response-writing
contrasts_with: []
answers_questions:
  - "How do I create an HTTP server in Node.js?"
---

# Quick Definition
`createServer` takes a request handler function and returns a server object; calling `listen(port)` on it starts accepting connections, invoking the handler for each incoming request.

# Core Definition
"The function passed as the argument to `createServer` is called every time a client connects to the server. The `request` and `response` bindings are objects representing the incoming and outgoing data" (Ch. 20).

# Prerequisites
- **HTTP module**: createServer is from node:http

# Key Properties
1. Handler function: `(request, response) => void`
2. `request.url` -- the requested path
3. `request.method` -- the HTTP method
4. `server.listen(port)` -- start accepting connections
5. Server stays running until process is terminated (Ctrl-C)

# Construction / Recognition
```javascript
import {createServer} from "node:http";
createServer((request, response) => {
  response.writeHead(200, {"Content-Type": "text/html"});
  response.write(`<h1>Hello!</h1>
    <p>You asked for <code>${request.url}</code></p>`);
  response.end();
}).listen(8000);
```

# Context & Application
The entry point for every Node HTTP server. Web frameworks wrap this function with routing, middleware, and convenience features.

# Examples
From the file server, routing by method:
```javascript
createServer((request, response) => {
  let handler = methods[request.method] || notAllowed;
  handler(request).then(({body, status = 200, type = "text/plain"}) => {
    response.writeHead(status, {"Content-Type": type});
    if (body?.pipe) body.pipe(response);
    else response.end(body);
  });
}).listen(8000);
```

# Relationships
## Builds Upon
- http-module
## Enables
- HTTP servers, API endpoints, file servers
## Related
- request-handling, response-writing, stream
## Contrasts With
- Express app.listen() (higher-level abstraction)

# Common Errors
- **Error**: Forgetting to call listen()
  **Correction**: Without listen(), the server is created but never starts accepting connections

# Common Confusions
- **Confusion**: The handler runs once
  **Clarification**: The handler runs for EVERY incoming request

# Source Reference
Chapter 20: Node.js, Section "The HTTP module", lines 464-527 of 20-nodejs.md.

# Verification Notes
- Definition source: direct from source text
- Confidence rationale: Complete example with explanation
- Cross-reference status: verified
