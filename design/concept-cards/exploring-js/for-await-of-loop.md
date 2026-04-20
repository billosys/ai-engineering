---
concept: For-Await-Of Loop
slug: for-await-of-loop
category: control-flow
subcategory: loops
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Control flow statements"
chapter_number: 25
pdf_page: null
section: "25.9 `for-await-of` loops"
extraction_confidence: high
aliases:
  - "for await...of"
prerequisites:
  - for-of-loop
extends:
  - for-of-loop
related:
  - for-of-loop
contrasts_with:
  - for-of-loop
answers_questions:
  - "How do I iterate over asynchronous data in JavaScript?"
---

# Quick Definition

The `for-await-of` loop is the asynchronous counterpart of `for-of`, iterating over asynchronous iterables and awaiting each value.

# Core Definition

As described in "Exploring JavaScript" Ch. 25, `for-await-of` is like `for-of` but works with asynchronous iterables instead of synchronous ones. It can only be used inside async functions and async generators. Introduced in ES2018.

# Prerequisites

- For-of loop
- Async functions (conceptual)

# Key Properties

1. Introduced in ES2018.
2. Only usable inside `async` functions and `async` generators.
3. Awaits each yielded value from the asynchronous iterable.

# Construction / Recognition

```js
for await (const item of asyncIterable) {
  // ...
}
```

# Context & Application

Used for iterating over streams, paginated API results, or other asynchronous data sources that implement the async iteration protocol.

# Examples

From the source text (Ch. 25, section 25.9):

```js
for await (const item of asyncIterable) {
  // process each async item
}
```

# Relationships

## Builds Upon
- **For-Of Loop** -- async version of the same pattern

## Contrasts With
- **For-Of Loop** -- `for-of` is synchronous; `for-await-of` works with async iterables

# Common Errors

- **Error**: Using `for-await-of` outside an async context.
  **Correction**: It can only be used inside `async` functions or `async` generators.

# Common Confusions

- **Confusion**: Thinking `for-await-of` can be used with synchronous iterables.
  **Clarification**: While it can technically work with sync iterables, it is designed for async iterables.

# Source Reference

Chapter 25: Control flow statements, Section 25.9, lines 786-800.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit definition; details deferred to async iteration chapter
- Cross-reference status: verified
