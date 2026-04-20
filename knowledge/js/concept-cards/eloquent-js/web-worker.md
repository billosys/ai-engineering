---
# === CORE IDENTIFICATION ===
concept: Web Worker
slug: web-worker

# === CLASSIFICATION ===
category: events
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Handling Events"
chapter_number: 15
pdf_page: null
section: "Events and the event loop"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - Worker

# === TYPED RELATIONSHIPS ===
prerequisites:
  - event-loop
  - event-handler
extends: []
related:
  - asynchronous-programming
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How can I run heavy computation without blocking the page?"
---

# Quick Definition
A web worker is a JavaScript process that runs in a separate thread alongside the main script, communicating via message passing to avoid blocking the UI.

# Core Definition
"For cases where you *really* do want to do some time-consuming thing in the background without freezing the page, browsers provide something called *web workers*. A worker is a JavaScript process that runs alongside the main script, on its own timeline." "To avoid the problems of having multiple threads touching the same data, workers do not share their global scope or any other data with the main script's environment. Instead, you have to communicate with them by sending messages back and forth." (Eloquent JavaScript, Ch. 15, lines 751-754, 771-774)

# Prerequisites
- **Event loop**: Understanding why the main thread can be blocked
- **Event handler**: Workers communicate via message events

# Key Properties
1. Runs in a separate thread from the main script
2. Does not share global scope or data with the main script
3. Communication via `postMessage` and `"message"` events
4. Messages are copied, not shared (only JSON-compatible values)
5. Created with `new Worker("script.js")`

# Construction / Recognition
Worker script (`squareworker.js`):
```javascript
addEventListener("message", event => {
  postMessage(event.data * event.data);
});
```

Main script:
```javascript
let squareWorker = new Worker("code/squareworker.js");
squareWorker.addEventListener("message", event => {
  console.log("The worker responded:", event.data);
});
squareWorker.postMessage(10);
squareWorker.postMessage(24);
```
(lines 764-788)

# Context & Application
Used for CPU-intensive computations that would otherwise freeze the UI, such as image processing, complex calculations, or data parsing.

# Examples
From the source (lines 764-788 shown above).

"Only values that can be represented as JSON can be sent as messages---the other side will receive a *copy* of them, rather than the value itself." (lines 796-797)

# Relationships
## Builds Upon
- Event loop and message-based communication
## Enables
- Background computation without freezing the page
## Related
- Asynchronous programming
## Contrasts With
- Main thread execution (single-threaded, can block UI)

# Common Errors
- **Error**: Trying to access the DOM from a web worker
  **Correction**: Workers cannot access the DOM; only the main thread can

# Common Confusions
- **Confusion**: Workers share memory with the main thread
  **Clarification**: Workers receive copies of messages, not references to shared data

# Source Reference
Chapter 15: Handling Events, Section "Events and the event loop", lines 750-797 of 15-handling-events.md.

# Verification Notes
- Definition source: direct quotation
- Confidence rationale: Clearly defined with complete example
- Cross-reference status: verified
