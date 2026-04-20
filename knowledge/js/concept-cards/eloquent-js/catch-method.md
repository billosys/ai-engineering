---
# === CORE IDENTIFICATION ===
concept: catch Method
slug: catch-method

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
section: "Failure"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - .catch()
  - catch handler

# === TYPED RELATIONSHIPS ===
prerequisites:
  - promise
  - reject
extends:
  - promise
related:
  - then-method
  - error-handling-in-async
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a promise?"
---

# Quick Definition
The `catch` method registers a handler to be called when a promise is rejected, similar to how `then` handles successful resolution. It returns a new promise.

# Core Definition
"To explicitly handle such rejections, promises have a `catch` method that registers a handler to be called when the promise is rejected, similar to how `then` handlers handle normal resolution. It's also very much like `then` in that it returns a new promise, which resolves to the original promise's value when that resolves normally and to the result of the `catch` handler otherwise. If a `catch` handler throws an error, the new promise is also rejected." (Eloquent JavaScript, Ch. 11, lines 380-386)

# Prerequisites
- **Promise**: Understanding promise resolution and rejection
- **Reject**: Understanding how and why promises are rejected

# Key Properties
1. Called only when the promise is rejected
2. Returns a new promise (enabling continued chaining)
3. If the catch handler returns a value, downstream promises resolve normally
4. If the catch handler throws, downstream promises are rejected

# Construction / Recognition
```javascript
new Promise((_, reject) => reject(new Error("Fail")))
  .then(value => console.log("Handler 1:", value))
  .catch(reason => {
    console.log("Caught failure " + reason);
    return "nothing";
  })
  .then(value => console.log("Handler 2:", value));
// -> Caught failure Error: Fail
// -> Handler 2: nothing
```
(lines 429-438)

# Context & Application
Used to handle errors in promise chains, similar to `catch` blocks in try/catch for synchronous code.

# Examples
From the source, the rejection skips the first `then` and is handled by `catch`:
"The first `then` handler function isn't called because at that point of the pipeline the promise holds a rejection. The `catch` handler handles that rejection and returns a value, which is given to the second `then` handler function." (lines 441-444)

# Relationships
## Builds Upon
- Promise rejection mechanism
## Enables
- Error recovery in promise chains
## Related
- `then` method (handles successful resolution)
- Error handling in async code
## Contrasts With
- `then` (which handles success rather than failure)

# Common Errors
- **Error**: Placing `catch` before async steps that may also fail
  **Correction**: Place `catch` at the end of a chain to handle any failure in the entire chain

# Common Confusions
- **Confusion**: `catch` terminates the promise chain
  **Clarification**: `catch` returns a new promise; the chain continues after it, and the returned value becomes a resolution

# Source Reference
Chapter 11: Asynchronous Programming, Section "Failure", lines 380-444 of 11-asynchronous-programming.md.

# Verification Notes
- Definition source: direct quotation
- Confidence rationale: Clearly defined with illustrative example
- Cross-reference status: verified
