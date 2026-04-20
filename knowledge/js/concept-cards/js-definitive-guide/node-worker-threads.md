---
concept: Node Worker Threads
slug: node-worker-threads
category: node-apis
subcategory: worker threads
tier: advanced
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Server-Side JavaScript with Node"
chapter_number: 16
pdf_page: 642
section: "16.11 Worker Threads"
extraction_confidence: high
aliases:
  - "worker_threads module"
  - Node workers
prerequisites:
  - node-programming-model
  - node-eventemitter
extends: []
related:
  - web-workers
  - postmessage
  - sharedarraybuffer-atomics
contrasts_with:
  - web-workers
answers_questions:
  - "What distinguishes Web Workers from Node worker threads?"
---

# Quick Definition

Node's "worker_threads" module (Node 10+) enables true multithreaded JavaScript execution, where workers communicate with the main thread via `postMessage()` and "message" events, mirroring the Web Workers API.

# Core Definition

Worker threads allow Node to perform true parallel computation. Workers are created with `new Worker(filename)` and communicate via `postMessage()` and "message" events (using structured clone). `threads.isMainThread` distinguishes main from worker code. `threads.parentPort` is the worker's communication channel to the parent. `workerData` passes initial data. MessageChannel/MessagePort enable custom communication channels. Typed arrays can be transferred (not copied) for efficiency. SharedArrayBuffer enables shared memory, but requires Atomics for thread safety (Flanagan, Ch. 16, pp. 642-650).

# Prerequisites

- **node-programming-model** — Must understand Node's single-threaded model to know when workers are needed.
- **node-eventemitter** — Workers use the event pattern.

# Key Properties

1. `new Worker(filename)` creates a worker running the specified file.
2. `threads.isMainThread` is true in main thread, false in workers.
3. `threads.parentPort` provides the worker's communication channel.
4. `workerData` passes initial data to the worker.
5. MessageChannel/MessagePort for custom channels.
6. ArrayBuffers can be transferred (zero-copy) via transfer list.

# Construction / Recognition

```javascript
const threads = require("worker_threads");
if (threads.isMainThread) {
  let worker = new threads.Worker(__filename);
  worker.postMessage(data);
  worker.on("message", result => console.log(result));
} else {
  threads.parentPort.once("message", data => {
    threads.parentPort.postMessage(process(data));
  });
}
```

# Context & Application

Use for CPU-intensive tasks (image processing, scientific computing) or to maintain main-thread responsiveness in servers handling expensive computations.

# Examples

From the source (p. 643-645): A `reticulateSplines()` function that offloads computation to a worker, using the same file for both main and worker code via `isMainThread`.

# Relationships

## Builds Upon
- **node-programming-model** — Extends Node's concurrency beyond single-threaded
- **node-eventemitter** — Workers use message events

## Enables
- True parallel computation in Node

## Related
- **web-workers** — Browser equivalent
- **postmessage** — Same communication pattern
- **sharedarraybuffer-atomics** — Shared memory between threads

## Contrasts With
- **web-workers** — Node workers use `require()` and `worker_threads` module; Web Workers use `importScripts()`. Node workers support `workerData` for initial data.

# Common Errors

- **Error**: Creating workers for lightweight tasks.
  **Correction**: Workers have creation overhead; only use them for significant CPU-bound work.

# Common Confusions

- **Confusion**: Node worker threads share memory by default.
  **Clarification**: Workers communicate via message passing (copying). SharedArrayBuffer is opt-in and requires Atomics for safety.

# Source Reference

Chapter 16: Server-Side JavaScript with Node, Section 16.11, pages 642-650.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: Extensive section with complete examples
- Uncertainties: None
- Cross-reference status: Verified
