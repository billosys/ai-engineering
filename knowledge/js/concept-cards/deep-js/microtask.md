---
# === CORE IDENTIFICATION ===
concept: Microtask
slug: microtask

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
  - "microtask queue"
  - "Promise job"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - task-queue
extends: []
related:
  - promise
contrasts_with:
  - task-queue

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I implement a Promise from scratch?"
---

# Quick Definition

A microtask is a lightweight asynchronous task, tightly coupled with the current macrotask, that the real Promise API uses instead of normal tasks to execute Promise reactions.

# Core Definition

From "Deep JavaScript" (Ch 19.2.1): "Note that the real Promise API doesn't use normal tasks (like `setTimeout()`), it uses *microtasks*, which are tightly coupled with the current normal task and always execute directly after it." The ToyPromise uses `setTimeout` as a simplified stand-in.

# Prerequisites

- **Task queue** — Microtasks are a higher-priority variant of the task queue

# Key Properties

1. Execute immediately after the current macrotask, before the next macrotask
2. Have higher priority than macrotasks (e.g., `setTimeout`, I/O callbacks)
3. Used by the real Promise API for scheduling reactions
4. Can be scheduled via `queueMicrotask()` in modern environments

# Construction / Recognition

## To Construct/Create:
1. Promise reactions are automatically scheduled as microtasks
2. `queueMicrotask(fn)` explicitly schedules a microtask

## To Identify/Recognize:
1. Code that executes after synchronous code but before `setTimeout` callbacks

# Context & Application

Microtasks ensure Promise reactions execute as soon as possible after the current task completes, providing better performance and more predictable ordering than macrotasks.

# Examples

**Example 1** (Ch 19): The ToyPromise simplification:
```js
function addToTaskQueue(task) {
  setTimeout(task, 0); // Uses macrotask; real Promises use microtasks
}
```

# Relationships

## Builds Upon
- **Task queue** — Microtasks are a special category within the event loop

## Related
- **Promise** — Promise reactions are scheduled as microtasks

## Contrasts With
- **Task queue (macrotask)** — Microtasks execute before the next macrotask

# Common Errors

- **Error**: Assuming `setTimeout(fn, 0)` behaves identically to microtasks
  **Correction**: Microtasks execute before any pending macrotasks, making them faster

# Common Confusions

- **Confusion**: Microtasks and macrotasks are the same scheduling mechanism
  **Clarification**: Microtasks have higher priority and execute between macrotasks

# Source Reference

Chapter 19: Exploring Promises by implementing them, Section 19.2.1, lines 8437+.

# Verification Notes

- Definition source: direct from source text
- Confidence rationale: Medium -- briefly mentioned, not the chapter's focus
- Cross-reference status: unverified (links to external article by Jake Archibald)
