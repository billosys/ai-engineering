---
# === CORE IDENTIFICATION ===
concept: Revealing Constructor Pattern
slug: revealing-constructor-pattern

# === CLASSIFICATION ===
category: async-programming
subcategory: promises
tier: intermediate

# === PROVENANCE ===
source: "Deep JavaScript"
source_slug: deep-js
authors: "Dr. Axel Rauschmayer"
chapter: "Exploring Promises by implementing them"
chapter_number: 19
section: "19.9 Version 5: Revealing constructor pattern"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "executor pattern"
  - "Promise constructor pattern"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - promise
  - promise-resolution
extends: []
related:
  - promise-exception-handling
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I implement a Promise from scratch?"
---

# Quick Definition

The revealing constructor pattern is the design where Promise resolution/rejection functions are passed as arguments to a constructor callback (the executor), rather than exposed as methods on the Promise object.

# Core Definition

From "Deep JavaScript" (Ch 19.9): "JavaScript Promises are not resolved and rejected via methods, but via functions that are handed to the *executor*, the callback parameter of the constructor." If the executor throws an exception, the Promise is rejected. The ToyPromise implementation uses methods for simplicity, but real Promises use this pattern.

# Prerequisites

- **Promise** — The revealing constructor pattern is how real Promises are created
- **Promise resolution** — The `resolve` and `reject` functions are the resolution interface

# Key Properties

1. The Promise constructor takes an executor function: `new Promise((resolve, reject) => { ... })`
2. `resolve` and `reject` are only accessible inside the executor
3. If the executor throws, the Promise is automatically rejected
4. This pattern prevents external code from resolving/rejecting the Promise

# Construction / Recognition

## To Construct/Create:
1. `new Promise((resolve, reject) => { /* async work */ })`

## To Identify/Recognize:
1. A constructor that passes capabilities (resolve/reject) to its callback

# Context & Application

This pattern encapsulates the resolution capability. Only the code inside the executor can resolve or reject the Promise, preventing accidental or malicious external settlement.

# Examples

**Example 1** (Ch 19):
```js
const promise = new Promise(
  (resolve, reject) => { // executor
    // ...
  });
```

# Relationships

## Builds Upon
- **Promise** — This is the standard construction interface for Promises

## Enables
- **Encapsulated resolution** — External code cannot resolve/reject the Promise

## Related
- **Exception handling in Promises** — Executor exceptions automatically reject

# Common Errors

- **Error**: Trying to call `.resolve()` as a method on a native Promise object
  **Correction**: Native Promises use the revealing constructor pattern; resolve/reject are only available inside the executor

# Common Confusions

- **Confusion**: The ToyPromise `.resolve()` method works the same as native Promises
  **Clarification**: ToyPromise exposes resolve/reject as methods for pedagogical simplicity; native Promises use the constructor callback pattern

# Source Reference

Chapter 19: Exploring Promises by implementing them, Section 19.9, lines 8437+.

# Verification Notes

- Definition source: direct from source text
- Confidence rationale: Explicitly described as the final implementation step
- Cross-reference status: verified (references Domenic Denicola's blog post)
