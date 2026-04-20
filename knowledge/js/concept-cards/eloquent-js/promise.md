---
# === CORE IDENTIFICATION ===
concept: Promise
slug: promise

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
section: "Promises"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - Promise object

# === TYPED RELATIONSHIPS ===
prerequisites:
  - function
  - callback
extends: []
related:
  - then-method
  - catch-method
  - promise-chaining
  - resolve
  - reject
  - async-function
contrasts_with:
  - callback

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a promise?"
  - "How do promises relate to callbacks?"
  - "What must I know before using promises and async/await?"
---

# Quick Definition
A promise is an object representing a value that may not be available yet, providing a `then` method to register functions that should be called when the value becomes available.

# Core Definition
"A *promise* is a receipt representing a value that may not be available yet. It provides a `then` method that allows you to register a function that should be called when the action for which it is waiting finishes. When the promise is *resolved*, meaning its value becomes available, such functions (there can be multiple) are called with the result value. It is possible to call `then` on a promise that has already resolved---your function will still be called." (Eloquent JavaScript, Ch. 11, lines 213-219)

# Prerequisites
- **Functions**: Promises use functions as handlers for resolution and rejection
- **Callbacks**: Understanding callbacks helps understand what problem promises solve

# Key Properties
1. A promise can be either *resolved* (success) or *rejected* (failure)
2. Once resolved or rejected, a promise cannot change state again
3. The `then` method returns another promise, enabling chaining
4. Promises handle errors through rejection propagation
5. Even already-resolved promises call `then` handlers asynchronously

# Construction / Recognition
```javascript
let fifteen = Promise.resolve(15);
fifteen.then(value => console.log(`Got ${value}`));
// -> Got 15
```

# Context & Application
Promises are the standard mechanism for asynchronous programming in modern JavaScript, used by fetch APIs, file operations, and as the foundation for async/await.

# Examples
From the source, creating a promise-based wrapper:
```javascript
function textFile(filename) {
  return new Promise(resolve => {
    readTextFile(filename, text => resolve(text));
  });
}

textFile("plans.txt").then(console.log);
```
(lines 246-253)

"It is useful to think of a promise as a device that lets code ignore the question of when a value is going to arrive. A normal value has to actually exist before we can reference it. A promised value is a value that *might* already be there or might appear at some point in the future." (lines 317-323)

# Relationships
## Builds Upon
- Callbacks (promises wrap the callback pattern in a cleaner interface)
## Enables
- Promise chaining, async/await, Promise.all
## Related
- `then` method, `catch` method, `resolve`, `reject`
## Contrasts With
- Raw callbacks (promises provide better error handling and composition)

# Common Errors
- **Error**: Forgetting that promises always resolve or reject asynchronously, even if already settled
  **Correction**: "Even if a promise is already resolved, waiting for it will cause your callback to run after the current script finishes, rather than right away." (lines 1011-1013)

# Common Confusions
- **Confusion**: A promise *is* the result value
  **Clarification**: A promise is a container for a future value; you access the value through `then` or `await`, not directly

# Source Reference
Chapter 11: Asynchronous Programming, Section "Promises", lines 201-323 of 11-asynchronous-programming.md.

# Verification Notes
- Definition source: direct quotation
- Confidence rationale: Central concept with extensive explanation and examples
- Cross-reference status: verified against chapter summary
