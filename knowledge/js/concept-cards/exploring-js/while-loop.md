---
concept: While Loop
slug: while-loop
category: control-flow
subcategory: loops
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Control flow statements"
chapter_number: 25
pdf_page: null
section: "25.5 `while` loops"
extraction_confidence: high
aliases:
  - "while statement"
prerequisites:
  - truthy-and-falsy-values
extends: []
related:
  - do-while-loop
  - for-loop
contrasts_with:
  - do-while-loop
  - for-of-loop
answers_questions:
  - "How do I repeat code while a condition is true?"
---

# Quick Definition

The `while` loop evaluates its condition before each iteration and executes its body as long as the condition is truthy.

# Core Definition

As described in "Exploring JavaScript" Ch. 25, a `while` loop has the syntax `while (condition) { statements }`. Before each iteration, the condition is evaluated: if falsy, the loop ends; if truthy, the body executes one more time. Introduced in ES1.

# Prerequisites

- Truthy and falsy values

# Key Properties

1. Introduced in ES1.
2. Condition is checked before each iteration (zero or more executions).
3. If condition is always `true`, creates an infinite loop (use `break` to exit).

# Construction / Recognition

```js
while (condition) {
  // body
}
```

# Context & Application

Used when the number of iterations is unknown and depends on a runtime condition. Prefer `for-of` for iterating over collections.

# Examples

From the source text (Ch. 25, section 25.5.1):

```js
const arr = ['a', 'b', 'c'];
while (arr.length > 0) {
  const elem = arr.shift();
  console.log(elem);
}
```

# Relationships

## Contrasts With
- **Do-While Loop** -- `do-while` checks condition after each iteration (runs at least once)
- **For-Of Loop** -- `for-of` iterates over iterables with cleaner syntax

# Common Errors

- **Error**: Creating an infinite loop by not updating the condition variable inside the body.
  **Correction**: Ensure the loop body modifies state that eventually makes the condition falsy.

# Common Confusions

- **Confusion**: Thinking `while` always executes at least once.
  **Clarification**: `while` checks the condition first; use `do-while` for at-least-once execution.

# Source Reference

Chapter 25: Control flow statements, Section 25.5, lines 535-582.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit syntax and semantics in source
- Cross-reference status: verified
