---
concept: "http.createServer()"
slug: http-createserver
category: node-apis
subcategory: HTTP
tier: intermediate
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Server-Side JavaScript with Node"
chapter_number: 16
pdf_page: 632
section: "16.8 HTTP Clients and Servers"
extraction_confidence: high
aliases:
  - HTTP server
  - Node web server
prerequisites:
  - node-programming-model
  - node-eventemitter
  - node-streams
extends: []
related:
  - fetch-api
contrasts_with: []
answers_questions:
  - "How do I create an HTTP server in Node.js?"
---

# Quick Definition

`http.createServer()` creates an HTTP server that listens on a specified port and fires "request" events with `(request, response)` arguments, where `request` is a Readable stream and `response` is a Writable stream.

# Core Definition

To create an HTTP server in Node: (1) create a Server with `new http.Server()` or `http.createServer()`, (2) call `listen(port)` to start listening, (3) register a "request" event handler that receives an IncomingMessage (request) and ServerResponse (response). The request object provides `method`, `url`, and headers; it is also a Readable stream for reading the request body. The response provides `writeHead()`, `setHeader()`, `write()`, and `end()` for sending the response (Flanagan, Ch. 16, pp. 632-636).

# Prerequisites

- **node-programming-model** — Server runs in Node's event loop.
- **node-eventemitter** — Server is an EventEmitter.
- **node-streams** — Request/response are streams.

# Key Properties

1. `server.listen(port)` starts listening for connections.
2. "request" event provides `(request, response)` objects.
3. `request.method`, `request.url` identify the HTTP request.
4. `response.writeHead(statusCode)` sets status and headers.
5. `response.end(body)` sends the response and closes.
6. `request.pipe(response)` can echo request body as response.

# Construction / Recognition

```javascript
const http = require("http");
let server = new http.Server();
server.listen(8000);
server.on("request", (request, response) => {
  response.writeHead(200, {"Content-Type": "text/plain"});
  response.end("Hello World\n");
});
```

# Context & Application

The foundation for Node web servers. Production servers typically use frameworks like Express that build on top of this API.

# Examples

From the source (p. 633-636): A complete static file server that maps URL paths to local files, uses `fs.createReadStream()` piped to the response, and handles 404 errors.

# Relationships

## Builds Upon
- **node-programming-model** — Runs in the event loop
- **node-eventemitter** — Server emits "request" events
- **node-streams** — Request/response are streams

## Enables
- Web application development in Node

## Related
- **fetch-api** — Browser-side HTTP client

## Contrasts With
- (None)

# Common Errors

- **Error**: Forgetting to call `response.end()` after writing the response.
  **Correction**: Always call `end()` to signal that the response is complete.

# Common Confusions

- **Confusion**: `http.createServer()` is sufficient for production servers.
  **Clarification**: It is low-level. Production servers use frameworks like Express for routing, middleware, and other features.

# Source Reference

Chapter 16: Server-Side JavaScript with Node, Section 16.8, pages 632-636.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: Complete server example in source
- Uncertainties: None
- Cross-reference status: Verified
