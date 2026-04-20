---
# === CORE IDENTIFICATION ===
concept: Promise Chaining
slug: promise-chaining

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
  - then chaining
  - promise pipeline

# === TYPED RELATIONSHIPS ===
prerequisites:
  - promise
  - then-method
extends:
  - then-method
related:
  - catch-method
  - async-function
contrasts_with:
  - callback-hell

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do promises relate to callbacks?"
---

# Quick Definition
Promise chaining is the pattern of linking multiple `then` calls together to create a pipeline of sequential asynchronous operations, where each step's output feeds into the next.

# Core Definition
"You can 'chain' multiple calls to `then` together to set up a sequence of asynchronous actions." "The chains of promise values created by calls to `then` and `catch` thus form a pipeline through which asynchronous values or failures move." (Eloquent JavaScript, Ch. 11, lines 266-267, 417-419)

# Prerequisites
- **Promise**: Understanding the promise concept
- **then method**: Knowledge that `then` returns a new promise

# Key Properties
1. Each `then` returns a new promise, enabling flat sequential composition
2. Synchronous return values are automatically wrapped in resolved promises
3. If a handler returns a promise, the chain waits for it to settle
4. Failures propagate through the chain until caught

# Construction / Recognition
```javascript
function randomFile(listFile) {
  return textFile(listFile)
    .then(content => content.trim().split("\n"))
    .then(ls => ls[Math.floor(Math.random() * ls.length)])
    .then(filename => textFile(filename));
}
```
(lines 275-281)

# Context & Application
Promise chaining replaces deeply nested callbacks with a flat, readable sequence of transformations and async steps.

# Examples
From the source: "The initial promise fetches the list of files as a string. The first `then` call transforms that string into an array of lines, producing a new promise. The second `then` call picks a random line from that, producing a third promise that yields a single filename. The final `then` call reads this file." (lines 285-291)

The text also notes: "The kind of `then` wrappers that only do some synchronous data transformation are often useful, such as when you want to return a promise that produces a processed version of some asynchronous result." (lines 303-306)
```javascript
function jsonFile(filename) {
  return textFile(filename).then(JSON.parse);
}
```
(lines 309-311)

# Relationships
## Builds Upon
- `then` method's ability to return new promises
## Enables
- Flat, readable asynchronous pipelines
## Related
- `catch` method for error handling in chains
## Contrasts With
- Callback hell (nested callbacks that chains replace)

# Common Errors
- **Error**: Breaking the chain by not returning the promise from a `then` handler
  **Correction**: Always return values (including promises) from `then` handlers to maintain the chain

# Common Confusions
- **Confusion**: Each `then` modifies the original promise
  **Clarification**: Each `then` creates a new promise; the original remains unchanged

# Source Reference
Chapter 11: Asynchronous Programming, Section "Promises", lines 262-323 of 11-asynchronous-programming.md.

# Verification Notes
- Definition source: direct quotation
- Confidence rationale: Multiple examples and thorough explanation
- Cross-reference status: verified
