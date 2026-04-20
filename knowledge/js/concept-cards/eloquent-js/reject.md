---
# === CORE IDENTIFICATION ===
concept: Reject (Promise)
slug: reject

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
  - Promise.reject
  - rejected promise
  - rejection

# === TYPED RELATIONSHIPS ===
prerequisites:
  - promise
extends: []
related:
  - resolve
  - catch-method
  - error-handling-in-async
contrasts_with:
  - resolve

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a promise?"
---

# Quick Definition
Rejecting a promise means settling it as failed with a reason value, typically an error, which is propagated to `catch` handlers.

# Core Definition
"Promises... can be either resolved (the action finished successfully) or rejected (it failed)." "Much like resolving a promise provides a value, rejecting one also provides a value, usually called the *reason* of the rejection. When an exception in a handler function causes the rejection, the exception value is used as the reason." "There's a `Promise.reject` function that creates a new, immediately rejected promise." (Eloquent JavaScript, Ch. 11, lines 360-377)

# Prerequisites
- **Promise**: Understanding promise states and settlement

# Key Properties
1. A rejected promise carries a reason value (typically an error)
2. Rejections propagate through promise chains until caught
3. `Promise.reject(reason)` creates an immediately rejected promise
4. Throwing an exception inside a `then` handler automatically rejects the next promise
5. Unhandled rejections are reported as errors by the environment

# Construction / Recognition
```javascript
function textFile(filename) {
  return new Promise((resolve, reject) => {
    readTextFile(filename, (text, error) => {
      if (error) reject(error);
      else resolve(text);
    });
  });
}
```
(lines 406-413)

# Context & Application
Rejection is the promise equivalent of throwing an exception. It signals that an asynchronous operation has failed and allows error handling through `catch` or rejection handlers.

# Examples
From the source:
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

# Relationships
## Builds Upon
- The Promise concept
## Enables
- Error propagation through promise chains
## Related
- `catch` method (handles rejections)
- Error handling in async code
## Contrasts With
- `resolve` (settling a promise as successful)

# Common Errors
- **Error**: Not handling rejections, leading to unhandled promise rejection warnings
  **Correction**: "JavaScript environments can detect when a promise rejection isn't handled and will report this as an error." (lines 447-449)

# Common Confusions
- **Confusion**: Rejections stop at the first `catch`
  **Clarification**: A `catch` handler can return a value, converting the rejection back to a resolution for downstream handlers

# Source Reference
Chapter 11: Asynchronous Programming, Section "Failure", lines 325-449 of 11-asynchronous-programming.md.

# Verification Notes
- Definition source: direct quotation
- Confidence rationale: Extensively explained with examples
- Cross-reference status: verified
