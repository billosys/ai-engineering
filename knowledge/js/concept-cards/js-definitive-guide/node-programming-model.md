---
concept: Node Programming Model
slug: node-programming-model
category: node-apis
subcategory: fundamentals
tier: foundational
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Server-Side JavaScript with Node"
chapter_number: 16
pdf_page: 594
section: "16.1 Node Programming Basics"
extraction_confidence: high
aliases:
  - Node.js basics
  - Node event loop
prerequisites: []
extends: []
related:
  - error-first-callbacks
  - node-eventemitter
contrasts_with: []
answers_questions:
  - "How do I create an HTTP server in Node.js?"
---

# Quick Definition

Node is a single-threaded, event-loop-based JavaScript runtime that achieves high concurrency through asynchronous, nonblocking I/O APIs, where callbacks and event handlers are invoked when operations complete rather than blocking the thread.

# Core Definition

Node achieves high levels of concurrency while maintaining a single-threaded programming model by making its API asynchronous and nonblocking by default. At its core, Node runs an "event loop": it executes your initial code, registers callbacks with the OS, then blocks until an event occurs, at which point it invokes the appropriate callback. Programs do not exit until all callbacks have been called and there are no more pending events (Flanagan, Ch. 16, pp. 594, 600-602).

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Single-threaded: no locks, deadlocks, or race conditions.
2. Asynchronous by default: even filesystem operations are nonblocking.
3. Programs keep running as long as there are pending events or callbacks.
4. `process.exit()` forces termination; `process.on("SIGINT", ...)` handles signals.
5. Unhandled exceptions crash the process unless caught with `process.setUncaughtExceptionCaptureCallback()`.

# Construction / Recognition

A Node program runs its initial code, registers event handlers, then enters the event loop. It exits when no more events are pending.

# Context & Application

The foundation for all Node programming. Understanding the event loop is essential for writing efficient, non-blocking servers and scripts.

# Examples

From the source (p. 594): "A Node-based server program that listens for incoming network connections will theoretically run forever because it will always be waiting for more events."

# Relationships

## Builds Upon
- (None - foundational)

## Enables
- **error-first-callbacks** — Node's callback pattern
- **node-eventemitter** — Event-based APIs
- **node-streams** — Streaming I/O

## Related
- **web-workers** — Browser's equivalent concurrency model

## Contrasts With
- (None)

# Common Errors

- **Error**: Writing blocking/synchronous code in the event loop of a server.
  **Correction**: Use asynchronous APIs to avoid blocking the event loop and preventing other requests from being handled.

# Common Confusions

- **Confusion**: Single-threaded means Node cannot handle concurrent requests.
  **Clarification**: Node handles concurrency through the event loop and nonblocking I/O, not threads.

# Source Reference

Chapter 16: Server-Side JavaScript with Node, Sections 16.1-16.2, pages 594-602.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: Core concept thoroughly explained
- Uncertainties: None
- Cross-reference status: Verified
