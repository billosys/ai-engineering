---
# === CORE IDENTIFICATION ===
concept: setTimeout()
slug: set-timeout

# === CLASSIFICATION ===
category: async-programming
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Foundations of asynchronous programming in JavaScript"
chapter_number: 42
pdf_page: null
section: "42.2.3 Scheduling new tasks via setTimeout()"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - setTimeout
  - timer scheduling

# === TYPED RELATIONSHIPS ===
prerequisites:
  - event-loop
  - task-queue
extends: []
related:
  - blocking-the-javascript-process
  - callback-pattern
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What concepts are prerequisite to understanding Promises?"
---

# Quick Definition

`setTimeout(callback, ms)` is a global function that schedules a callback to be added to the task queue after a delay of `ms` milliseconds, enabling deferred execution and task breaks.

# Core Definition

In "Exploring JavaScript" Ch. 42, `setTimeout()` is described as a way to "schedule a task for later execution." It is available on both browsers and Node.js. Its signature is `function setTimeout(callback: () => void, ms: number): any`. The returned handle can be passed to `clearTimeout()` to cancel the scheduled callback.

# Prerequisites

- **Event loop** -- `setTimeout` enqueues tasks for the event loop
- **Task queue** -- the callback is added to the task queue after the delay

# Key Properties

1. The callback does not execute during the current task, even with delay 0
2. A delay of 0 means "as soon as possible after current task and already-queued tasks"
3. Returns a handle that can be cancelled via `clearTimeout(handle)`
4. Available in both browsers and Node.js

# Construction / Recognition

```js
console.log('First task starts');
setTimeout(() => {
  console.log('Second task starts');
}, 0);
console.log('First task ends');
// Output: First task starts, First task ends, Second task starts
```

(Ch. 42, Section 42.2.3, lines 196-217)

# Context & Application

`setTimeout` is used to break long-running operations into smaller tasks, defer execution, implement timeouts for Promises, and schedule future work.

# Examples

From the source, `setTimeout` with delay 0 demonstrates task scheduling:
```js
setTimeout(() => { console.log('Second task starts'); }, 0);
```
This adds a new task that runs after the current task completes.

(Ch. 42, Section 42.2.3, lines 198-217)

# Relationships

## Builds Upon
- **Event loop** -- setTimeout schedules tasks for the event loop
- **Task queue** -- callbacks are enqueued in the task queue

## Enables
- **Promise timeout pattern** -- `setTimeout` used with `Promise.race()` for timeouts

## Related
- **Blocking the JavaScript process** -- setTimeout is a tool to avoid blocking

# Common Errors

- **Error**: Expecting `setTimeout(fn, 100)` to execute exactly after 100ms
  **Correction**: The delay is a minimum; execution depends on when the event loop reaches the task

# Common Confusions

- **Confusion**: `setTimeout(fn, 0)` executes the callback immediately
  **Clarification**: It defers to the next event loop iteration, after the current task and any previously queued tasks

# Source Reference

Chapter 42: Foundations of asynchronous programming in JavaScript, Section 42.2.3, lines 173-231.

# Verification Notes

- Definition source: direct from source text
- Confidence rationale: explicit definition with type signature
- Cross-reference status: verified
