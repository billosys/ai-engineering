---
concept: Promise Object
slug: promise-object
category: async-programming
subcategory: promises
tier: intermediate
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Asynchronous JavaScript"
chapter_number: 13
pdf_page: 363
section: "13.2 Promises"
extraction_confidence: high
aliases:
  - "Promise"
prerequisites:
  - callback-pattern
extends: []
related:
  - promise-then
  - promise-chaining
  - promise-catch
  - promise-constructor
contrasts_with:
  - callback-pattern
answers_questions:
  - "What is a Promise?"
  - "What must I understand before learning about Promises?"
  - "How does `async/await` relate to Promises?"
---

# Quick Definition

An object representing the eventual result of an asynchronous computation, with three possible states — pending, fulfilled (with a value), or rejected (with a reason) — that enables structured asynchronous programming through `.then()` and `.catch()` methods.

# Core Definition

"A Promise is an object that represents the result of an asynchronous computation. That result may or may not be ready yet" (p. 363). Promises have three states: *pending* (not yet settled), *fulfilled* (completed successfully with a value), and *rejected* (failed with an error). Once settled (fulfilled or rejected), a Promise never changes state. Promises also have a *resolved* state meaning they are "locked onto" another Promise's outcome.

# Prerequisites

- **callback-pattern** — Promises are designed to improve on callback-based async programming

# Key Properties

1. Three states: pending, fulfilled, rejected
2. Once settled (fulfilled/rejected), state never changes
3. `.then()` registers callbacks for fulfillment (and optionally rejection)
4. `.catch()` registers callbacks for rejection
5. `.finally()` runs cleanup code regardless of outcome
6. Promises represent single computations, not repeated events

# Construction / Recognition

```js
getJSON(url).then(jsonData => {
    // Called when Promise fulfills
}).catch(error => {
    // Called when Promise rejects
});
```

# Context & Application

The standard mechanism for asynchronous programming in modern JavaScript. Promises are the foundation of the Fetch API, dynamic `import()`, and `async/await`. They cannot represent repeated events (use async iterators for that).

# Examples

From the source text (p. 365-367): `getJSON("/api/user/profile").then(displayUserProfile)`. Promise terminology (p. 367): "fulfilled" = first callback called, "rejected" = second callback called, "pending" = neither yet, "settled" = fulfilled or rejected. "resolved" = locked onto another Promise.

# Relationships

## Builds Upon
- **Callback Pattern** — Promises improve on callbacks by linearizing chains and standardizing error handling

## Enables
- **Promise.then()** — The primary method for handling fulfillment
- **Promise Chaining** — Sequential async operations
- **Promise.catch()** — Error handling
- **Async/Await** — Syntactic sugar over Promises

## Contrasts With
- **Callback Pattern** — Callbacks require nesting; Promises enable linear chains

# Common Errors

- **Error**: Expecting Promises to work for repeated events like click handlers.
  **Correction**: Promises represent single computations. Use event listeners or async iterators for repeated events.

# Common Confusions

- **Confusion**: Conflating "resolved" with "fulfilled."
  **Clarification**: A resolved Promise may not yet be fulfilled — it may be "locked onto" another Promise that hasn't settled yet. Resolved means the Promise's fate is determined, not that it has a value.

# Source Reference

Chapter 13: Asynchronous JavaScript, Section 13.2, pages 363-367.

# Verification Notes

- Definition source: Direct quotes from source text
- Confidence rationale: High — core chapter topic with extensive treatment
- Uncertainties: None
- Cross-reference status: Verified
