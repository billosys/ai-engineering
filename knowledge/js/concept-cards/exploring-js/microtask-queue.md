---
concept: Microtask Queue
slug: microtask-queue
category: async-programming
subcategory: null
tier: advanced
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Async functions"
chapter_number: 44
pdf_page: null
section: "44.2.1 Awaiting fulfilled Promises"
extraction_confidence: medium
aliases:
  - microtasks
  - Promise job queue
prerequisites:
  - event-loop
  - task-queue
  - promise
extends: []
related:
  - set-timeout
contrasts_with:
  - task-queue
answers_questions:
  - "What concepts are prerequisite to understanding Promises?"
---

# Quick Definition

The microtask queue is a separate, higher-priority queue used for Promise-related callbacks. Microtasks are always processed before the next regular task, ensuring Promise reactions execute promptly.

# Core Definition

"Exploring JavaScript" Ch. 44 mentions that "Promise-related tasks are so-called microtasks which are different from normal tasks and always handled before them (via a microtask queue)." The function `queueMicrotask()` schedules microtasks directly.

# Prerequisites

- **Event loop** -- microtasks are processed within the event loop
- **Task queue** -- microtask queue has higher priority than the task queue
- **Promise** -- Promise callbacks use the microtask queue

# Key Properties

1. Separate from the regular task queue
2. Higher priority: all microtasks processed before the next regular task
3. Promise `.then()`, `.catch()`, `.finally()` callbacks are microtasks
4. `queueMicrotask()` schedules microtasks directly
5. `await` results are delivered via microtasks

# Construction / Recognition

```js
async function awaitPromise() {
  queueMicrotask(() => console.log('OTHER TASK'));
  console.log('before');
  await Promise.resolve('fulfilled');
  console.log('after');
}
// Output: before, OTHER TASK, after
```

(Ch. 44, Section 44.2.1, lines 288-304)

# Context & Application

Understanding microtasks explains timing of Promise callbacks and why `queueMicrotask()` must be used instead of `setTimeout()` for testing Promise ordering.

# Examples

See construction example above. (Ch. 44, Section 44.2.1, lines 288-311)

# Relationships

## Builds Upon
- **Event loop** -- microtasks are processed within the loop
- **Task queue** -- microtask queue is separate and higher priority

## Contrasts With
- **Task queue** -- regular tasks; microtasks always execute first

# Common Errors

- **Error**: Using `setTimeout(fn, 0)` to run code after a Promise resolves
  **Correction**: Use `queueMicrotask()` or `.then()` for code that should run at microtask priority

# Common Confusions

- **Confusion**: Microtasks and tasks are the same
  **Clarification**: Microtasks have higher priority and are processed before the next task

# Source Reference

Chapter 44: Async functions, Section 44.2.1, lines 306-311.

# Verification Notes

- Definition source: synthesized from brief mention in source
- Confidence rationale: medium -- briefly mentioned, not a full section
- Cross-reference status: verified via MDN reference in source
