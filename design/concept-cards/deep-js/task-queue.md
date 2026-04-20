---
# === CORE IDENTIFICATION ===
concept: Task Queue
slug: task-queue

# === CLASSIFICATION ===
category: async-programming
subcategory: microtasks
tier: intermediate

# === PROVENANCE ===
source: "Deep JavaScript"
source_slug: deep-js
authors: "Dr. Axel Rauschmayer"
chapter: "Exploring Promises by implementing them"
chapter_number: 19
section: "19.2.1 Method .then()"

# === CONFIDENCE ===
extraction_confidence: medium

# === VARIANTS ===
aliases:
  - "event loop queue"
  - "macrotask queue"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - microtask
  - promise
contrasts_with:
  - microtask

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I implement a Promise from scratch?"
---

# Quick Definition

The task queue is the event loop mechanism that schedules asynchronous operations; Promise reactions are added to this queue to ensure they always execute asynchronously.

# Core Definition

From "Deep JavaScript" (Ch 19.2.1): "Promises must always settle asynchronously. That's why we don't directly execute tasks, we add them to the task queue of the event loop (of browsers, Node.js, etc.)." The ToyPromise implementation simulates this with:
```js
function addToTaskQueue(task) {
  setTimeout(task, 0);
}
```

The text notes this is a simplification: "the real Promise API doesn't use normal tasks (like `setTimeout()`), it uses *microtasks*."

# Prerequisites

None (foundational runtime concept).

# Key Properties

1. Part of the JavaScript event loop in browsers and Node.js
2. Ensures asynchronous execution of scheduled tasks
3. `setTimeout(fn, 0)` adds to the (macro) task queue
4. Promise reactions actually use the microtask queue, not the macrotask queue

# Construction / Recognition

## To Construct/Create:
1. `setTimeout(task, 0)` adds to the macrotask queue
2. Promise reactions are automatically added to the microtask queue by the engine

## To Identify/Recognize:
1. Code that executes after the current synchronous execution completes

# Context & Application

Understanding the task queue is essential for knowing why Promise callbacks never execute synchronously, even when the Promise is already settled. The ToyPromise uses `setTimeout` as a stand-in for the microtask queue.

# Examples

**Example 1** (Ch 19):
```js
function addToTaskQueue(task) {
  setTimeout(task, 0);
}
```

# Relationships

## Enables
- **Asynchronous Promise settlement** — Reactions are always queued, never synchronous

## Contrasts With
- **Microtask** — Real Promises use microtasks, which execute before the next macrotask

# Common Errors

- **Error**: Using `setTimeout` in production Promise implementations
  **Correction**: Real Promises use microtasks (via `queueMicrotask()` or the engine's internal mechanism)

# Common Confusions

- **Confusion**: Promise reactions execute at the same priority as `setTimeout` callbacks
  **Clarification**: Promise microtasks have higher priority than macrotasks like `setTimeout`

# Source Reference

Chapter 19: Exploring Promises by implementing them, Section 19.2.1, lines 8437+.

# Verification Notes

- Definition source: synthesized from implementation and explanation
- Confidence rationale: Medium -- described briefly as implementation detail, not a primary focus
- Cross-reference status: unverified (external concept)
