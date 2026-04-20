---
# === CORE IDENTIFICATION ===
concept: Event Loop
slug: event-loop

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
  - JS event loop
  - task loop

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - task-queue
  - run-to-completion
  - asynchronous-programming-overview
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What concepts are prerequisite to understanding Promises?"
  - "What distinguishes synchronous from asynchronous code execution?"
---

# Quick Definition

The event loop is a continuously running loop inside the JavaScript process that dequeues and executes tasks one at a time from the task queue.

# Core Definition

As described in "Exploring JavaScript" Ch. 42, "The event loop runs continuously inside the JavaScript process. During each loop iteration, it takes one task out of the queue (if the queue is empty, it waits until it isn't) and executes it. After the task is finished, control goes back to the event loop, which then retrieves the next task from the queue and executes it."

# Prerequisites

Foundational concept with no prerequisites.

# Key Properties

1. JavaScript normally runs in a single process (both in browsers and Node.js)
2. Tasks are pieces of code (functions with zero parameters) managed via a queue
3. Task sources add tasks to the queue and may run concurrently with the JavaScript process
4. The event loop processes one task at a time, sequentially

# Construction / Recognition

The event loop can be approximated as:
```js
while (true) {
  const task = taskQueue.dequeue();
  task(); // run task
}
```

(Ch. 42, Section 42.1, lines 61-67)

# Context & Application

The event loop is the foundation of all asynchronous behavior in JavaScript. Events such as mouse clicks, timer callbacks, and network responses add tasks to the queue. Understanding the event loop is essential for understanding why async patterns exist.

# Examples

From the source text, the event loop model shows task sources (user clicks, timer callbacks, network responses) adding tasks to the task queue, which the event loop drains one task at a time.

(Ch. 42, Section 42.1, lines 42-78)

# Relationships

## Builds Upon
- No prerequisites

## Enables
- **Task queue** -- the queue the event loop processes
- **Run-to-completion** -- guaranteed by the event loop's one-task-at-a-time model
- **Callback pattern** -- callbacks are scheduled as tasks in the queue

## Related
- **setTimeout** -- schedules tasks for later execution via the event loop

# Common Errors

- **Error**: Assuming multiple tasks run in parallel within the JavaScript process
  **Correction**: Only one task runs at a time; concurrency comes from task sources outside the JS process

# Common Confusions

- **Confusion**: The event loop is a browser-specific concept
  **Clarification**: Both browsers and Node.js use an event loop model for JavaScript execution

# Source Reference

Chapter 42: Foundations of asynchronous programming in JavaScript, Section 42.1, lines 38-78.

# Verification Notes

- Definition source: direct from source text
- Confidence rationale: explicit definition with pseudocode
- Cross-reference status: verified against Ch. 41 reference
