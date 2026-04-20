---
# === CORE IDENTIFICATION ===
concept: Resolve (Promise)
slug: resolve

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
  - Promise.resolve
  - resolved promise
  - fulfillment

# === TYPED RELATIONSHIPS ===
prerequisites:
  - promise
extends: []
related:
  - reject
  - then-method
  - promise-constructor
contrasts_with:
  - reject

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a promise?"
---

# Quick Definition
Resolving a promise means settling it successfully with a value, making that value available to any registered `then` handlers.

# Core Definition
"When the promise is *resolved*, meaning its value becomes available, such functions (there can be multiple) are called with the result value." The static method `Promise.resolve` "ensures that the value you give it is wrapped in a promise. If it's already a promise, it is simply returned. Otherwise, you get a new promise that immediately resolves with your value as its result." (Eloquent JavaScript, Ch. 11, lines 216-226)

# Prerequisites
- **Promise**: Understanding the promise concept and its states

# Key Properties
1. A resolved promise has a value that can be consumed via `then`
2. `Promise.resolve(value)` creates an immediately resolved promise
3. If `Promise.resolve` receives a promise, it returns that same promise
4. Resolution can only happen once per promise

# Construction / Recognition
```javascript
let fifteen = Promise.resolve(15);
fifteen.then(value => console.log(`Got ${value}`));
// -> Got 15
```
(lines 229-231)

# Context & Application
Used to create already-resolved promises for testing, wrapping synchronous values in the promise interface, or settling promises from async operations.

# Examples
From the source, wrapping a value:
```javascript
let fifteen = Promise.resolve(15);
fifteen.then(value => console.log(`Got ${value}`));
// -> Got 15
```

Resolving within a constructor:
```javascript
function textFile(filename) {
  return new Promise(resolve => {
    readTextFile(filename, text => resolve(text));
  });
}
```
(lines 246-250)

# Relationships
## Builds Upon
- The Promise concept
## Enables
- Accessing the settled value through `then`
## Related
- `then` method (consumes resolved values)
## Contrasts With
- `reject` (settling a promise as failed)

# Common Errors
- **Error**: Expecting `resolve` to call `then` handlers synchronously
  **Correction**: "Even if a promise is already resolved, waiting for it will cause your callback to run after the current script finishes, rather than right away." (lines 1011-1013)

# Common Confusions
- **Confusion**: Resolving a promise with another promise immediately provides the inner value
  **Clarification**: If you resolve a promise with another promise, the outer promise adopts the state of the inner promise

# Source Reference
Chapter 11: Asynchronous Programming, Section "Promises", lines 213-232 of 11-asynchronous-programming.md.

# Verification Notes
- Definition source: direct quotation
- Confidence rationale: Clearly defined with examples
- Cross-reference status: verified
