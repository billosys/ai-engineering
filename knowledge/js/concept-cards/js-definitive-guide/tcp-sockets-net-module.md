---
concept: TCP Sockets (net Module)
slug: tcp-sockets-net-module
category: node-apis
subcategory: networking
tier: intermediate
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Server-Side JavaScript with Node"
chapter_number: 16
pdf_page: 636
section: "16.9 Non-HTTP Network Servers and Clients"
extraction_confidence: high
aliases:
  - net module
  - TCP server
  - TCP client
prerequisites:
  - node-programming-model
  - node-streams
extends: []
related:
  - http-createserver
contrasts_with: []
answers_questions:
  - "How do I create an HTTP server in Node.js?"
---

# Quick Definition

Node's "net" module provides TCP networking with `net.createServer()` for servers that emit "connection" events with Duplex Socket objects, and `net.createConnection()` for clients that connect to a server on a specified port.

# Core Definition

The "net" module defines Server and Socket classes. Call `net.createServer()` and then `listen(port)` to create a TCP server. The server emits "connection" events with a Socket (Duplex stream) for each client. Clients connect with `net.createConnection(port, hostname)`. Socket objects are Duplex streams: write to send data, read to receive data. Call `end()` to disconnect (Flanagan, Ch. 16, pp. 636-637).

# Prerequisites

- **node-programming-model** — Networking uses Node's event-based model.
- **node-streams** — Sockets are Duplex streams.

# Key Properties

1. `net.createServer()` creates a TCP server.
2. `server.listen(port)` starts listening.
3. "connection" event provides a Socket (Duplex stream) per client.
4. `net.createConnection(port, host)` creates a client socket.
5. Sockets support `pipe()` for easy data transfer.

# Construction / Recognition

```javascript
const net = require("net");
let server = net.createServer();
server.listen(6789);
server.on("connection", socket => {
  socket.end("Hello World\n");
});
```

# Context & Application

Used for non-HTTP protocols, custom server implementations, and inter-process communication.

# Examples

From the source (p. 636-637): A knock-knock joke server that reads user responses via readline on the socket and sends punchlines back.

# Relationships

## Builds Upon
- **node-programming-model** — Event-based networking
- **node-streams** — Sockets are Duplex streams

## Enables
- Custom protocol implementations

## Related
- **http-createserver** — HTTP is built on top of TCP

## Contrasts With
- (None)

# Common Errors

- **Error**: Forgetting to close sockets when done.
  **Correction**: Always call `socket.end()` to properly close the connection.

# Common Confusions

- **Confusion**: The "net" module is only for TCP.
  **Clarification**: The "net" module also supports Unix domain sockets. For UDP, use the "dgram" module.

# Source Reference

Chapter 16: Server-Side JavaScript with Node, Section 16.9, pages 636-637.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: Complete server and client example
- Uncertainties: None
- Cross-reference status: Verified
