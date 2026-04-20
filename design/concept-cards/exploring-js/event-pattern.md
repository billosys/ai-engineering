---
# === CORE IDENTIFICATION ===
concept: Event Pattern for Async Results
slug: event-pattern

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
section: "42.3.1 Delivering asynchronous results via events"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - event-based async pattern
  - event listeners

# === TYPED RELATIONSHIPS ===
prerequisites:
  - event-loop
  - task-queue
extends: []
related:
  - callback-pattern
contrasts_with:
  - promise
  - callback-pattern

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do callbacks, Promises, and async/await relate as async patterns?"
---

# Quick Definition

The event pattern delivers asynchronous results zero or more times via event objects sent to registered event listeners by an event source.

# Core Definition

"Exploring JavaScript" Ch. 42 describes events as a pattern with three roles: "The event (an object) carries the data to be delivered. The event listener is a function that receives events via a parameter. The event source sends events and lets us register event listeners." Events are used to deliver values asynchronously and "do so zero or more times."

# Prerequisites

- **Event loop** -- events are delivered via the event loop
- **Task queue** -- event handlers are enqueued as tasks

# Key Properties

1. Three roles: event object, event listener, event source
2. Delivers results zero or more times (unlike callbacks/Promises which are one-shot)
3. Multiple variations exist: DOM events, IndexedDB events, XMLHttpRequest events
4. Event listeners are registered before or after the operation starts

# Construction / Recognition

DOM events example:
```js
const element = document.getElementById('my-link');
element.addEventListener('click', clickListener);

function clickListener(event) {
  event.preventDefault();
  console.log(event.shiftKey);
}
```

(Ch. 42, Section 42.3.1.3, lines 380-386)

# Context & Application

Events are used extensively in browsers (DOM events, XMLHttpRequest) and some Node.js APIs. They are best for ongoing notifications (multiple values over time) rather than one-shot results.

# Examples

IndexedDB example:
```js
const openRequest = indexedDB.open('MyDatabase', 1);
openRequest.onsuccess = (event) => {
  const db = event.target.result;
};
openRequest.onerror = (error) => {
  console.error(error);
};
```

(Ch. 42, Section 42.3.1.1, lines 300-311)

# Relationships

## Builds Upon
- **Event loop** -- event handlers execute as tasks
- **Task queue** -- event handlers are enqueued

## Related
- **Callback pattern** -- callbacks are another async result delivery mechanism

## Contrasts With
- **Promise** -- Promises deliver exactly one result; events deliver zero or more
- **Callback pattern** -- callbacks are for one-off results; events for repeated delivery

# Common Errors

- **Error**: Registering event listeners after the event has already fired without caching
  **Correction**: For one-shot events, use Promises which cache their result; for ongoing events, register early

# Common Confusions

- **Confusion**: Events and Promises are interchangeable
  **Clarification**: Events are for repeated notifications; Promises are for single async results

# Source Reference

Chapter 42: Foundations of asynchronous programming in JavaScript, Section 42.3.1, lines 277-393.

# Verification Notes

- Definition source: direct from source text
- Confidence rationale: explicit definition with three named roles
- Cross-reference status: verified
