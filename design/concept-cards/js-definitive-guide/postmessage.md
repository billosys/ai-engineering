---
concept: postMessage
slug: postmessage
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
  - message passing
  - structured clone
prerequisites:
  - web-workers
extends: []
related:
  - node-worker-threads
contrasts_with: []
answers_questions:
  - "What distinguishes Web Workers from Node worker threads?"
---

# Quick Definition

`postMessage()` sends a structured-cloned copy of a JavaScript value between threads (workers, iframes, or windows), with an optional transfer list for zero-copy transfer of typed arrays and MessagePorts.

# Core Definition

The `postMessage()` method copies its argument using the structured clone algorithm (which handles Map, Set, Date, RegExp, typed arrays, and circular references but not functions or DOM elements) and delivers it as a "message" event to the receiving thread. The optional second argument is a transfer list: an array of ArrayBuffers or MessagePorts that are transferred (moved, not copied) to the receiving thread, becoming unusable in the sending thread (Flanagan, Ch. 15, pp. 565-575).

# Prerequisites

- **web-workers** — postMessage is the communication mechanism for workers.

# Key Properties

1. Messages are copied via the structured clone algorithm, not shared.
2. Transfer list enables zero-copy transfer of ArrayBuffers and MessagePorts.
3. Transferred objects become unusable in the sending thread.
4. Also used for cross-origin iframe communication.
5. The structured clone algorithm cannot copy functions, DOM elements, or class prototypes.

# Construction / Recognition

```javascript
worker.postMessage({data: pixels}, [pixels.buffer]);
// pixels.buffer is transferred, not copied
```

# Context & Application

The fundamental communication mechanism for all multithreaded JavaScript, both in browsers (Web Workers) and Node.js (worker_threads).

# Examples

From the source (p. 565): Workers receive messages via `self.onmessage` or `addEventListener("message", ...)` and send responses back with `self.postMessage()`.

# Relationships

## Builds Upon
- **web-workers** — postMessage is how workers communicate

## Enables
- Efficient data exchange between threads

## Related
- **node-worker-threads** — Uses the same postMessage/message event pattern

## Contrasts With
- (None)

# Common Errors

- **Error**: Using a transferred ArrayBuffer after calling postMessage with it in the transfer list.
  **Correction**: Transferred buffers become zero-length and unusable in the sending thread.

# Common Confusions

- **Confusion**: postMessage shares data between threads.
  **Clarification**: postMessage copies data (or transfers ownership). Data is never shared unless using SharedArrayBuffer.

# Source Reference

Chapter 15: JavaScript in Web Browsers, Section 15.13, pages 565-575.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: Key mechanism clearly explained
- Uncertainties: None
- Cross-reference status: Verified
