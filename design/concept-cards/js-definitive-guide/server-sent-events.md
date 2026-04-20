---
concept: Server-Sent Events
slug: server-sent-events
category: browser-apis
subcategory: networking
tier: intermediate
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "JavaScript in Web Browsers"
chapter_number: 15
pdf_page: 546
section: "15.11.2 Server-Sent Events"
extraction_confidence: high
aliases:
  - SSE
  - EventSource
prerequisites:
  - fetch-api
  - addeventlistener
extends: []
related:
  - websocket
contrasts_with:
  - websocket
answers_questions:
  - "How do I use fetch() to make HTTP requests?"
---

# Quick Definition

Server-Sent Events (SSE) use the `EventSource` API to maintain a long-lived HTTP connection through which a server can push text-based events to the client, with automatic reconnection.

# Core Definition

The EventSource API creates a long-lived HTTP connection to a server. The server holds the connection open and writes specially formatted text data whenever it has something to send. The EventSource object translates the server's data into events with `type` and `data` properties. The client registers handlers with `addEventListener()`. If the connection drops, EventSource automatically reconnects (Flanagan, Ch. 15, pp. 546-549).

# Prerequisites

- **fetch-api** — Understanding HTTP requests provides context.
- **addeventlistener** — SSE uses the event listener pattern.

# Key Properties

1. Created with `new EventSource(url)`.
2. Server sends `event:` and `data:` lines separated by blank lines.
3. Default event type is "message" if server omits the event name.
4. Automatic reconnection on connection loss.
5. Unidirectional: server to client only.

# Construction / Recognition

```javascript
let ticker = new EventSource("stockprices.php");
ticker.addEventListener("bid", (event) => {
  displayNewBid(event.data);
});
```

# Context & Application

Ideal for real-time updates like news feeds, stock tickers, chat messages, and notification streams where the server needs to push data to the client.

# Examples

From the source (p. 547): A stock price ticker where the server sends bid events with price data. Also, a chat application using SSE for receiving messages and `fetch()` for posting messages.

# Relationships

## Builds Upon
- **fetch-api** — SSE is HTTP-based
- **addeventlistener** — Event handling pattern

## Enables
- Real-time server-to-client communication

## Related
- **websocket** — Alternative for bidirectional communication

## Contrasts With
- **websocket** — SSE is unidirectional (server-to-client); WebSocket is bidirectional. SSE is text-only; WebSocket supports binary.

# Common Errors

- **Error**: Using SSE when bidirectional communication is needed.
  **Correction**: Use WebSockets for bidirectional communication; SSE is server-to-client only.

# Common Confusions

- **Confusion**: SSE requires WebSocket protocol support.
  **Clarification**: SSE uses standard HTTP with long-polling. No special protocol upgrade is needed.

# Source Reference

Chapter 15: JavaScript in Web Browsers, Section 15.11.2, pages 546-549.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: Clear explanation with protocol details
- Uncertainties: None
- Cross-reference status: Verified
