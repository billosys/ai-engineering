---
concept: WebSocket
slug: websocket
category: browser-apis
subcategory: networking
tier: intermediate
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "JavaScript in Web Browsers"
chapter_number: 15
pdf_page: 550
section: "15.11.3 WebSockets"
extraction_confidence: high
aliases:
  - WebSocket API
  - wss protocol
prerequisites:
  - fetch-api
  - addeventlistener
extends: []
related:
  - server-sent-events
contrasts_with:
  - server-sent-events
answers_questions:
  - "How do I use fetch() to make HTTP requests?"
---

# Quick Definition

The WebSocket API provides a bidirectional, message-based communication channel between browser and server over a persistent connection using the `wss://` protocol, supporting both text and binary messages.

# Core Definition

WebSockets allow JavaScript code to exchange text and binary messages with a server. Created with `new WebSocket("wss://...")`, the connection starts with an HTTP upgrade handshake. The `send()` method transmits messages (strings, Blobs, ArrayBuffers, typed arrays). Incoming messages trigger "message" events with a `data` property. Connection lifecycle events include "open", "close", and "error". The `readyState` property tracks connection state (CONNECTING, OPEN, CLOSING, CLOSED) (Flanagan, Ch. 15, pp. 550-553).

# Prerequisites

- **fetch-api** — Understanding HTTP networking provides context.
- **addeventlistener** — WebSocket uses the event pattern.

# Key Properties

1. URLs use `wss://` (secure) instead of `https://`.
2. Bidirectional: both client and server can send messages.
3. Supports text (strings) and binary (Blob/ArrayBuffer) messages.
4. `readyState` tracks connection state through four constants.
5. Optional protocol negotiation via the second constructor argument.

# Construction / Recognition

```javascript
let socket = new WebSocket("wss://example.com/stockticker");
socket.addEventListener("message", (event) => { console.log(event.data); });
socket.send("Hello server");
```

# Context & Application

Used for real-time applications requiring bidirectional communication: chat, collaborative editing, multiplayer games, live dashboards.

# Examples

From the source (p. 550-552): Creating a WebSocket connection, listening for "open", "message", "close", and "error" events, and sending messages with `socket.send()`.

# Relationships

## Builds Upon
- HTTP (initial handshake) and the browser event model

## Enables
- Real-time bidirectional communication

## Related
- **server-sent-events** — Alternative for server-to-client only

## Contrasts With
- **server-sent-events** — SSE is unidirectional and text-only; WebSocket is bidirectional and supports binary

# Common Errors

- **Error**: Using `http://` or `https://` URLs for WebSocket connections.
  **Correction**: Use `ws://` or `wss://` (secure) URLs.

# Common Confusions

- **Confusion**: WebSockets use the HTTP protocol.
  **Clarification**: WebSocket is a separate protocol. The connection starts as HTTP but is upgraded via the `Upgrade: websocket` header.

# Source Reference

Chapter 15: JavaScript in Web Browsers, Section 15.11.3, pages 550-553.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: Clear API documentation with lifecycle
- Uncertainties: None
- Cross-reference status: Verified
