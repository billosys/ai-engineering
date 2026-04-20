---
concept: SharedArrayBuffer and Atomics
slug: sharedarraybuffer-atomics
category: node-apis
subcategory: worker threads
tier: advanced
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Server-Side JavaScript with Node"
chapter_number: 16
pdf_page: 649
section: "16.11.5 Sharing Typed Arrays Between Threads"
extraction_confidence: high
aliases:
  - shared memory
  - Atomics object
prerequisites:
  - node-worker-threads
extends: []
related:
  - postmessage
contrasts_with: []
answers_questions:
  - "What distinguishes Web Workers from Node worker threads?"
---

# Quick Definition

SharedArrayBuffer allows typed arrays to be shared (not copied) between threads via `postMessage()`, while the Atomics object provides thread-safe operations (`add()`, `load()`, `store()`, `compareExchange()`) on shared array elements.

# Core Definition

A typed array backed by a SharedArrayBuffer will be shared (not cloned) when passed via `postMessage()`. However, this introduces all the dangers of shared-memory multithreading. Even the `++` operator is not thread-safe. The Atomics object provides atomic operations like `Atomics.add()` that read-modify-write atomically, preventing race conditions. Without Atomics, concurrent increments produce incorrect results (Flanagan, Ch. 16, pp. 649-651).

# Prerequisites

- **node-worker-threads** — SharedArrayBuffer is used between worker threads.

# Key Properties

1. SharedArrayBuffer allows true shared memory between threads.
2. Without Atomics, even simple operations like `++` have race conditions.
3. `Atomics.add(array, index, value)` performs an atomic add.
4. `Atomics.load()` and `Atomics.store()` for thread-safe reads/writes.
5. Strongly discouraged for most use cases due to complexity.

# Construction / Recognition

```javascript
let sharedBuffer = new SharedArrayBuffer(4);
let sharedArray = new Int32Array(sharedBuffer);
// In worker: Atomics.add(sharedArray, 0, 1);
```

# Context & Application

Only for advanced use cases where threads must share data (e.g., pixel buffers for parallel image processing). Most programs should use message passing instead.

# Examples

From the source (p. 649-651): Two threads incrementing a shared counter 10 million times each. Without Atomics, the result is ~12 million (race conditions). With `Atomics.add()`, the correct result of 20 million is achieved.

# Relationships

## Builds Upon
- **node-worker-threads** — Shared memory between workers

## Enables
- True shared-memory parallelism (with care)

## Related
- **postmessage** — Alternative (safer) communication via copying

## Contrasts With
- (None)

# Common Errors

- **Error**: Using `++` on shared typed array elements instead of `Atomics.add()`.
  **Correction**: `++` is not atomic. Use `Atomics.add(array, index, 1)` for thread-safe increments.

# Common Confusions

- **Confusion**: SharedArrayBuffer makes multithreading easy in JavaScript.
  **Clarification**: Shared memory introduces all the classic problems of concurrent programming. Message passing is strongly preferred.

# Source Reference

Chapter 16: Server-Side JavaScript with Node, Section 16.11.5, pages 649-651.

# Verification Notes

- Definition source: Direct from source text with race condition demonstration
- Confidence rationale: Clear example showing both incorrect and correct usage
- Uncertainties: None
- Cross-reference status: Verified
