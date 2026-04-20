---
concept: EventEmitter
slug: node-eventemitter
category: node-apis
subcategory: fundamentals
tier: foundational
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Server-Side JavaScript with Node"
chapter_number: 16
pdf_page: 606
section: "16.4 Events and EventEmitter"
extraction_confidence: high
aliases:
  - Node events
  - EventEmitter class
prerequisites:
  - node-programming-model
extends: []
related:
  - node-streams
  - addeventlistener
contrasts_with:
  - addeventlistener
answers_questions:
  - "What is a Node.js stream?"
---

# Quick Definition

EventEmitter is Node's base class for event-based APIs, providing `on()` to register handlers, `emit()` to trigger events, `once()` for one-time handlers, and `off()` to remove handlers, with a special "error" event that throws if unhandled.

# Core Definition

Objects that emit events are instances of EventEmitter or its subclasses. The `on()` method registers a handler for a named event type. Handlers are invoked synchronously in registration order when `emit()` is called. `once()` registers a handler that auto-removes after first invocation. `off()` (or `removeListener()`) removes handlers. The "error" event is special: if emitted with no registered handlers, it throws an exception (Flanagan, Ch. 16, pp. 606-607).

# Prerequisites

- **node-programming-model** — EventEmitter is central to Node's event-based concurrency.

# Key Properties

1. `on(eventType, handler)` registers a handler (alias: `addListener()`).
2. `once(eventType, handler)` registers a one-time handler.
3. `off(eventType, handler)` removes a handler (alias: `removeListener()`).
4. `emit(eventType, ...args)` invokes handlers synchronously.
5. Unhandled "error" events throw exceptions.

# Construction / Recognition

```javascript
const EventEmitter = require("events");
const net = require("net");
let server = new net.Server();
server instanceof EventEmitter // => true
server.on("connection", socket => { socket.end("Hello World", "utf8"); });
```

# Context & Application

Used by streams, servers, child processes, and many other Node APIs. Essential for understanding any event-based Node API.

# Examples

From the source (p. 606): A net.Server emits "listening", "connection", and "close" events. The "connection" handler receives a socket object.

# Relationships

## Builds Upon
- **node-programming-model** — The event pattern that drives Node

## Enables
- **node-streams** — Streams are EventEmitters
- **http-createserver** — HTTP servers are EventEmitters

## Related
- **addeventlistener** — Browser equivalent (different API, same concept)

## Contrasts With
- **addeventlistener** — Browser uses `addEventListener()`; Node uses `on()`. Node handlers are synchronous; browser handlers are asynchronous.

# Common Errors

- **Error**: Not registering a handler for "error" events on an EventEmitter.
  **Correction**: Always handle "error" events; unhandled ones throw exceptions and can crash the process.

# Common Confusions

- **Confusion**: `emit()` invokes handlers asynchronously.
  **Clarification**: `emit()` is synchronous -- it invokes all handlers before returning.

# Source Reference

Chapter 16: Server-Side JavaScript with Node, Section 16.4, pages 606-607.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: Key Node concept with clear API documentation
- Uncertainties: None
- Cross-reference status: Verified
