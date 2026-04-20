---
# === CORE IDENTIFICATION ===
concept: Event Loop
slug: event-loop

# === CLASSIFICATION ===
category: asynchronous-programming
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Asynchronous Programming"
chapter_number: 11
pdf_page: null
section: "The event loop"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - JavaScript event loop
  - run loop

# === TYPED RELATIONSHIPS ===
prerequisites:
  - asynchronous-programming
  - callback
extends: []
related:
  - promise
  - event-handler
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes synchronous from asynchronous code?"
---

# Quick Definition
The event loop is the mechanism by which JavaScript environments execute code one piece at a time, processing queued events and callbacks between executions.

# Core Definition
"No matter how closely together events---such as timeouts or incoming requests---happen, a JavaScript environment will run only one program at a time. You can think of this as it running a big loop *around* your program, called the *event loop*. When there's nothing to be done, that loop is paused. But as events come in, they are added to a queue, and their code is executed one after the other. Because no two things run at the same time, slow-running code can delay the handling of other events." (Eloquent JavaScript, Ch. 11, lines 986-992)

# Prerequisites
- **Asynchronous programming**: Understanding why code needs to be scheduled
- **Callbacks**: Understanding that callbacks are queued for later execution

# Key Properties
1. Only one piece of code runs at a time (single-threaded execution)
2. Events are added to a queue and processed one at a time
3. Callbacks and promise handlers run on their own empty call stack
4. Slow-running code blocks all other event processing
5. Promises always resolve asynchronously, even if already settled

# Construction / Recognition
The event loop's behavior is demonstrated when a synchronous busy-wait delays a timeout:
```javascript
let start = Date.now();
setTimeout(() => {
  console.log("Timeout ran at", Date.now() - start);
}, 20);
while (Date.now() < start + 50) {}
console.log("Wasted time until", Date.now() - start);
// -> Wasted time until 50
// -> Timeout ran at 55
```
(lines 999-1008)

# Context & Application
The event loop is the runtime model that makes JavaScript's asynchronous programming possible. Understanding it is essential for debugging timing issues and ensuring responsive applications.

# Examples
From the source, demonstrating that promise resolution is always async:
```javascript
Promise.resolve("Done").then(console.log);
console.log("Me first!");
// -> Me first!
// -> Done
```
(lines 1017-1021)

"Asynchronous behavior happens on its own empty function call stack. This is one of the reasons that, without promises, managing exceptions across asynchronous code is so hard." (lines 967-969)

# Relationships
## Builds Upon
- Single-threaded JavaScript execution model
## Enables
- Non-blocking I/O despite single-threaded execution
- Predictable ordering of event processing
## Related
- Event handlers (processed via the event loop)
- Promise resolution (scheduled via microtask queue)
## Contrasts With
- Multi-threaded execution models

# Common Errors
- **Error**: Writing long-running synchronous code that blocks the event loop
  **Correction**: Break heavy computation into smaller chunks or use web workers

# Common Confusions
- **Confusion**: `setTimeout(fn, 0)` runs the callback immediately
  **Clarification**: It schedules the callback to run after the current script finishes and any pending events are processed

# Source Reference
Chapter 11: Asynchronous Programming, Section "The event loop", lines 950-1025 of 11-asynchronous-programming.md.

# Verification Notes
- Definition source: direct quotation
- Confidence rationale: Central concept with clear definition and examples
- Cross-reference status: verified against Ch. 15 discussion
