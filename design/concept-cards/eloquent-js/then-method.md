---
# === CORE IDENTIFICATION ===
concept: then Method
slug: then-method

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
  - .then()
  - then handler

# === TYPED RELATIONSHIPS ===
prerequisites:
  - promise
extends:
  - promise
related:
  - catch-method
  - promise-chaining
  - resolve
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a promise?"
  - "How do promises relate to callbacks?"
---

# Quick Definition
The `then` method registers a function to be called when a promise resolves successfully, and itself returns a new promise that resolves to the return value of the handler.

# Core Definition
"A useful thing about the `then` method is that it itself returns another promise. This one resolves to the value returned by the callback function or, if that returned value is a promise, to the value that promise resolves to." Additionally, "`then` also accepts a rejection handler as a second argument, so you can install both types of handlers in a single method call: `.then(acceptHandler, rejectHandler)`." (Eloquent JavaScript, Ch. 11, lines 262-267, 389-392)

# Prerequisites
- **Promise**: Must understand what a promise is and its states

# Key Properties
1. Returns a new promise (enabling chaining)
2. The handler's return value becomes the resolved value of the returned promise
3. If the handler returns a promise, the returned promise adopts its state
4. If the handler throws, the returned promise is rejected
5. Accepts an optional second argument for rejection handling

# Construction / Recognition
```javascript
let fifteen = Promise.resolve(15);
fifteen.then(value => console.log(`Got ${value}`));
// -> Got 15
```

# Context & Application
`then` is the primary way to consume promise values and build sequential chains of asynchronous operations.

# Examples
From the source, a chain of transformations:
```javascript
function randomFile(listFile) {
  return textFile(listFile)
    .then(content => content.trim().split("\n"))
    .then(ls => ls[Math.floor(Math.random() * ls.length)])
    .then(filename => textFile(filename));
}
```
(lines 275-281)

A data processing pipeline:
```javascript
function jsonFile(filename) {
  return textFile(filename).then(JSON.parse);
}
```
(lines 309-311)

# Relationships
## Builds Upon
- Promise objects
## Enables
- Promise chaining for sequential async operations
## Related
- `catch` method (for handling rejections)
## Contrasts With
- Direct callback passing (then provides composability)

# Common Errors
- **Error**: Forgetting that `then` always returns a new promise, not the original
  **Correction**: Chain from the result of `then`, not from the original promise

# Common Confusions
- **Confusion**: `then` handlers run synchronously
  **Clarification**: `then` handlers always run asynchronously, even on already-resolved promises

# Source Reference
Chapter 11: Asynchronous Programming, Section "Promises", lines 262-323 of 11-asynchronous-programming.md.

# Verification Notes
- Definition source: direct quotation
- Confidence rationale: Thoroughly explained with multiple examples
- Cross-reference status: verified
