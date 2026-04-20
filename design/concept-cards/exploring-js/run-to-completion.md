---
# === CORE IDENTIFICATION ===
concept: Run-to-Completion Semantics
slug: run-to-completion

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
section: "42.2.4 Run-to-completion semantics"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - run to completion

# === TYPED RELATIONSHIPS ===
prerequisites:
  - event-loop
  - task-queue
extends: []
related:
  - asynchronous-programming-overview
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What concepts are prerequisite to understanding Promises?"
  - "What distinguishes synchronous from asynchronous code execution?"
---

# Quick Definition

Run-to-completion semantics means that each JavaScript task is always finished before the next task is executed, guaranteeing no concurrent modification of shared data within a task.

# Core Definition

"Exploring JavaScript" Ch. 42 states: "Each task is always finished ('run to completion') before the next task is executed." This is a fundamental guarantee of the JavaScript execution model. As a consequence, "tasks don't have to worry about their data being changed while they are working on it (concurrent modification)."

# Prerequisites

- **Event loop** -- provides the mechanism for sequential task execution
- **Task queue** -- holds tasks that run to completion

# Key Properties

1. No task can be interrupted by another task
2. Eliminates concurrent modification concerns within a single task
3. Simplifies reasoning about JavaScript code
4. Only run-to-completion semantics prevents race conditions in patterns like IndexedDB's asynchronous configuration

# Construction / Recognition

```js
console.log('First task starts');
setTimeout(() => {
  console.log('Second task starts');
}, 0);
console.log('First task ends');
// Output: First task starts, First task ends, Second task starts
```

The first task runs completely before the second task begins.

(Ch. 42, Section 42.2.4, lines 248-258)

# Context & Application

Run-to-completion is why JavaScript does not need locks or mutexes for shared state. It is also why long-running code blocks the UI -- no other task can run until it finishes.

# Examples

From the source, the IndexedDB example relies on run-to-completion: "Only run-to-completion semantics saves us from race conditions here and ensures that the operation runs after the current code fragment is finished."

(Ch. 42, Section 42.3.1.1, lines 324-328)

# Relationships

## Builds Upon
- **Event loop** -- enforces one-task-at-a-time execution
- **Task queue** -- tasks in the queue wait for the current one to complete

## Enables
- **Callback pattern** -- safe to configure callbacks before async operations complete
- **Promise** -- Promise settlement notifications are delivered as tasks

## Related
- **Asynchronous programming overview** -- run-to-completion shapes all async patterns

# Common Errors

- **Error**: Using busy-wait loops assuming they will "yield" to other tasks
  **Correction**: A while loop blocks the entire process; use `setTimeout` or async patterns to yield

# Common Confusions

- **Confusion**: JavaScript tasks can be preempted like threads in other languages
  **Clarification**: JavaScript tasks always run to completion; there is no preemptive multitasking

# Source Reference

Chapter 42: Foundations of asynchronous programming in JavaScript, Section 42.2.4, lines 233-258.

# Verification Notes

- Definition source: direct quotation from source
- Confidence rationale: explicitly defined with blockquote emphasis
- Cross-reference status: verified
