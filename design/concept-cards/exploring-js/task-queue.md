---
# === CORE IDENTIFICATION ===
concept: Task Queue
slug: task-queue

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
section: "42.1 The event loop"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - message queue
  - callback queue

# === TYPED RELATIONSHIPS ===
prerequisites:
  - event-loop
extends: []
related:
  - run-to-completion
  - set-timeout
contrasts_with:
  - microtask-queue

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What concepts are prerequisite to understanding Promises?"
---

# Quick Definition

The task queue is a data structure that holds pending tasks (pieces of code) waiting to be executed by the event loop.

# Core Definition

In "Exploring JavaScript" Ch. 42, the task queue is the queue from which the event loop dequeues tasks. Task sources -- which may run concurrently with the JavaScript process -- add tasks to the queue. For example, "if a user clicks somewhere and a click listener was registered, then an invocation of that listener is added to the task queue."

# Prerequisites

- **Event loop** -- the task queue is processed by the event loop

# Key Properties

1. Tasks are enqueued by task sources (click handlers, timer callbacks, network responses)
2. Tasks are dequeued and executed one at a time by the event loop
3. New tasks cannot run until the current task completes (run-to-completion)
4. Task sources may run concurrently with the main JavaScript process

# Construction / Recognition

Tasks are added to the queue programmatically via mechanisms like `setTimeout`:
```js
setTimeout(() => {
  console.log('Second task starts');
}, 0);
```

Callback-based async results are also enqueued:
```js
taskQueue.enqueue(() => callback(null, result));
```

(Ch. 41, Section 41.4, lines 153-163)

# Context & Application

The task queue is central to JavaScript's cooperative multitasking model. Understanding it explains why long-running synchronous code blocks the UI and why `setTimeout(fn, 0)` defers execution.

# Examples

From the source:
```js
console.log('First task starts');
setTimeout(() => {
  console.log('Second task starts');
}, 0);
console.log('First task ends');
// Output: First task starts, First task ends, Second task starts
```

(Ch. 42, Section 42.2.3, lines 198-217)

# Relationships

## Builds Upon
- **Event loop** -- the task queue is drained by the event loop

## Enables
- **Callback pattern** -- callbacks are delivered via enqueued tasks
- **Run-to-completion** -- ensured by single-task execution from the queue

## Contrasts With
- **Microtask queue** -- Promise-related tasks use a separate microtask queue with higher priority

# Common Errors

- **Error**: Expecting `setTimeout(fn, 0)` to execute immediately
  **Correction**: It enqueues a task that runs after the current task and any previously queued tasks

# Common Confusions

- **Confusion**: The task queue and microtask queue are the same
  **Clarification**: Microtasks (Promise callbacks) have their own queue and are processed before the next regular task

# Source Reference

Chapter 42: Foundations of asynchronous programming in JavaScript, Section 42.1, lines 38-67.

# Verification Notes

- Definition source: direct from source text
- Confidence rationale: explicitly named and described with pseudocode
- Cross-reference status: verified
