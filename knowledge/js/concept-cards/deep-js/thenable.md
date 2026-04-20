---
# === CORE IDENTIFICATION ===
concept: Thenable
slug: thenable

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
section: "19.7.2 Flattening makes Promise states more complicated"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "thenable object"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - promise
extends: []
related:
  - promise-flattening
  - lock-in-state
  - promise-resolution
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a thenable?"
---

# Quick Definition

A thenable is any object with a `.then()` method, used by Promise flattening to enable interoperability between different Promise implementations.

# Core Definition

From "Deep JavaScript" (Ch 19.7.2): "Q doesn't have to be a Promise, only a so-called *thenable*. A thenable is an object with a method `.then()`. The reason for this added flexibility is to enable different Promise implementations to work together (which mattered when Promises were first added to the language)."

The ToyPromise implementation detects thenables with:
```js
function isThenable(value) {
  return typeof value === 'object' && value !== null
    && typeof value.then === 'function';
}
```

# Prerequisites

- **Promise** — Thenables are a generalization of the Promise interface

# Key Properties

1. Any object with a `.then()` method qualifies as a thenable
2. Must be a non-null object (not a primitive)
3. All native Promises are thenables, but not all thenables are Promises
4. Used by Promise flattening during resolution

# Construction / Recognition

## To Construct/Create:
1. Create any object with a `.then()` method: `{ then(onFulfilled, onRejected) { ... } }`

## To Identify/Recognize:
1. Check: `typeof value === 'object' && value !== null && typeof value.then === 'function'`

# Context & Application

Thenables were critical when Promises were first standardized in ES6, because multiple Promise libraries existed (Q, Bluebird, RSVP, etc.). By accepting thenables rather than requiring native Promises, the spec enabled interoperability between these libraries.

# Examples

**Example 1** (Ch 19): Thenable detection function:
```js
function isThenable(value) {
  return typeof value === 'object' && value !== null
    && typeof value.then === 'function';
}
```

# Relationships

## Builds Upon
- **Promise** — Thenables generalize the Promise concept

## Enables
- **Promise flattening** — Resolution detects thenables to decide whether to flatten
- **Cross-library interoperability** — Different Promise implementations can work together

## Related
- **Lock-in state** — Resolving with a thenable causes lock-in

# Common Errors

- **Error**: Assuming only native Promise objects trigger flattening
  **Correction**: Any object with a `.then()` method is treated as a thenable during resolution

# Common Confusions

- **Confusion**: A thenable and a Promise are the same thing
  **Clarification**: A thenable is any object with a `.then()` method. A Promise is a specific standardized object with `.then()`, `.catch()`, `.finally()`, and specific internal state management. All Promises are thenables, but not vice versa.

# Source Reference

Chapter 19: Exploring Promises by implementing them, Section 19.7.2-19.7.3, lines 8437+.

# Verification Notes

- Definition source: direct quote from source
- Confidence rationale: Explicitly defined with detection function
- Cross-reference status: verified
