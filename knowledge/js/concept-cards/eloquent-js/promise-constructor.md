---
# === CORE IDENTIFICATION ===
concept: Promise Constructor
slug: promise-constructor

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
  - new Promise()

# === TYPED RELATIONSHIPS ===
prerequisites:
  - promise
  - function
extends:
  - promise
related:
  - resolve
  - reject
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a promise?"
---

# Quick Definition
The `Promise` constructor creates a new promise by taking a function argument that receives `resolve` and `reject` functions, which are called to settle the promise.

# Core Definition
"To create a promise that does not immediately resolve, you can use `Promise` as a constructor. It has a somewhat odd interface: the constructor expects a function as its argument, which it immediately calls, passing it a function that it can use to resolve the promise." The constructor also passes a second argument for rejection. (Eloquent JavaScript, Ch. 11, lines 235-239, 395-397)

# Prerequisites
- **Promise**: Understanding what a promise represents
- **Functions**: The constructor takes a function (the executor) as its argument

# Key Properties
1. The executor function is called *immediately* by the constructor
2. The executor receives two arguments: `resolve` and `reject`
3. Calling `resolve(value)` settles the promise as fulfilled
4. Calling `reject(reason)` settles the promise as rejected
5. A promise can be resolved or rejected only once

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
Used to wrap callback-based APIs in promise-based interfaces, or when you need manual control over when a promise resolves or rejects.

# Examples
From the source, a simple resolve-only example:
```javascript
function textFile(filename) {
  return new Promise(resolve => {
    readTextFile(filename, text => resolve(text));
  });
}
```
(lines 246-250)

A timeout wrapper using the constructor:
```javascript
function withTimeout(promise, time) {
  return new Promise((resolve, reject) => {
    promise.then(resolve, reject);
    setTimeout(() => reject("Timed out"), time);
  });
}
```
(lines 534-539)

# Relationships
## Builds Upon
- The Promise concept
## Enables
- Wrapping callback APIs in promises
- Creating custom async operations
## Related
- `resolve` and `reject` functions
## Contrasts With
- `Promise.resolve()` which creates an already-resolved promise

# Common Errors
- **Error**: Forgetting to call `reject` on error paths
  **Correction**: Always handle both success and failure paths in the executor

# Common Confusions
- **Confusion**: The executor function runs asynchronously
  **Clarification**: The executor runs immediately and synchronously; it is the *resolution* that may happen later

# Source Reference
Chapter 11: Asynchronous Programming, Section "Promises" and "Failure", lines 235-413 of 11-asynchronous-programming.md.

# Verification Notes
- Definition source: direct quotation
- Confidence rationale: Multiple clear examples with explanation
- Cross-reference status: verified
