---
concept: SharedArrayBuffer
slug: shared-array-buffer
category: collections
subcategory: null
tier: advanced
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Typed Arrays: handling binary data (advanced)"
chapter_number: 35
pdf_page: null
section: "35.1.3 SharedArrayBuffer"
extraction_confidence: high
aliases:
  - "SharedArrayBuffer"
  - "Atomics"
prerequisites:
  - array-buffer
extends:
  - array-buffer
related: []
contrasts_with:
  - array-buffer
answers_questions:
  - "How do `Map` and `Set` differ from plain objects and arrays as collections?"
---

# Quick Definition

SharedArrayBuffer (ES2017) is an ArrayBuffer variant whose memory can be accessed concurrently by multiple agents (main thread and Web Workers), paired with the Atomics API for thread-safe operations.

# Core Definition

SharedArrayBuffer is an ArrayBuffer whose memory can be accessed by multiple agents (main thread or web workers) concurrently. Unlike regular ArrayBuffers which can be transferred, SharedArrayBuffers are cloned (sharing the data storage). They can be resized but only grown, not shrunk. The Atomics global object provides functions for atomic operations on shared memory.

# Prerequisites

- **array-buffer** -- SharedArrayBuffer extends the concept

# Key Properties

1. Introduced in ES2017
2. Shared memory between agents (threads)
3. Cloned (not transferred) between agents
4. Can only grow, not shrink (when resizable)
5. Requires Atomics API for safe concurrent access
6. Subject to cross-origin isolation requirements in browsers

# Construction / Recognition

```js
const sab = new SharedArrayBuffer(4);
const view = new Int32Array(sab);
// Can be shared with a Web Worker
```

# Context & Application

Used for high-performance concurrent programming, shared state between Web Workers, and WebAssembly shared memory.

# Examples

```js
const sab = new SharedArrayBuffer(4);
const view = new Int32Array(sab);
Atomics.store(view, 0, 42);
Atomics.load(view, 0); // 42
```

(Chapter 35, Section 35.1.3, lines 200-227)

# Relationships

## Builds Upon
- **array-buffer** -- variant with shared memory

## Enables
- Concurrent programming between agents

## Related
- None

## Contrasts With
- **array-buffer** -- regular ArrayBuffer is not shared and can be transferred

# Common Errors

- **Error**: Accessing SharedArrayBuffer data without Atomics.
  **Correction**: Use Atomics for thread-safe reads/writes to avoid data races.

# Common Confusions

- **Confusion**: SharedArrayBuffer works like regular ArrayBuffer.
  **Clarification**: SharedArrayBuffer requires Atomics for safe access, cannot be transferred (only cloned), and has cross-origin isolation requirements in browsers.

# Source Reference

Chapter 35: Typed Arrays, Section 35.1.3, lines 200-227.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly defined with ES2017 marker
- Cross-reference status: verified
