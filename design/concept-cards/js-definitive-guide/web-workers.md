---
concept: Web Workers
slug: web-workers
category: browser-apis
subcategory: workers
tier: intermediate
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "JavaScript in Web Browsers"
chapter_number: 15
pdf_page: 565
section: "15.13 Web Workers"
extraction_confidence: high
aliases:
  - Worker threads (browser)
  - background threads
prerequisites:
  - dom-tree
  - addeventlistener
extends: []
related:
  - postmessage
contrasts_with:
  - node-worker-threads
answers_questions:
  - "What distinguishes Web Workers from Node worker threads?"
---

# Quick Definition

Web Workers allow JavaScript to run computationally intensive tasks in background threads that cannot access the DOM but communicate with the main thread via `postMessage()` and "message" events, preserving the single-threaded programming model.

# Core Definition

A web worker is a background thread for performing computationally intensive tasks without freezing the user interface. Worker code does not have access to document content, does not share any state with the main thread, and can only communicate through asynchronous message events. Workers are created with `new Worker("worker.js")` and communicate via `postMessage()` and "message" events. Messages are copied using the structured clone algorithm, not shared (Flanagan, Ch. 15, pp. 565-575).

# Prerequisites

- **dom-tree** — Understanding that workers cannot access the DOM.
- **addeventlistener** — Workers use the event model for communication.

# Key Properties

1. Created with `new Worker(url)` where url is a JavaScript file.
2. No access to the DOM or document.
3. Communication via `postMessage()` and "message" events.
4. Messages are copied, not shared (structured clone algorithm).
5. Workers can use `importScripts()` to load additional code.
6. Typed arrays can be transferred (zero-copy) via the transfer list.

# Construction / Recognition

```javascript
let worker = new Worker("worker.js");
worker.postMessage({data: someData});
worker.addEventListener("message", (event) => {
  console.log(event.data);
});
```

# Context & Application

Use workers for CPU-intensive tasks like image processing, data parsing, or complex calculations that would otherwise freeze the UI.

# Examples

From the source (p. 565-575): The Mandelbrot set example uses workers to compute fractal images in parallel, transferring pixel data between the main thread and workers.

# Relationships

## Builds Upon
- Browser event model and the structured clone algorithm

## Enables
- **postmessage** — The communication mechanism between threads

## Related
- **node-worker-threads** — Node's equivalent API

## Contrasts With
- **node-worker-threads** — Web Workers use `importScripts()` and have no `require()`; Node workers use `require()` and `worker_threads` module. Node workers support SharedArrayBuffer more readily.

# Common Errors

- **Error**: Trying to access `document` or DOM APIs from within a worker.
  **Correction**: Workers have no DOM access. Send data to the main thread for DOM updates.

# Common Confusions

- **Confusion**: Web Workers enable shared-memory multithreading.
  **Clarification**: Workers communicate via message passing. SharedArrayBuffer is available but strongly discouraged for most use cases.

# Source Reference

Chapter 15: JavaScript in Web Browsers, Section 15.13, pages 565-575.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: Extensive section with complete examples
- Uncertainties: None
- Cross-reference status: Verified
