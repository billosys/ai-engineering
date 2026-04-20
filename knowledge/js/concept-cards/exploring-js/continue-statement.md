---
concept: Continue Statement
slug: continue-statement
category: control-flow
subcategory: loop-control
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Control flow statements"
chapter_number: 25
pdf_page: null
section: "25.1.3 `continue`"
extraction_confidence: high
aliases:
  - "continue"
prerequisites:
  - while-loop
  - for-loop
extends: []
related:
  - break-statement
contrasts_with:
  - break-statement
answers_questions:
  - "How do I skip to the next iteration of a loop?"
---

# Quick Definition

The `continue` statement skips the rest of the current loop iteration and proceeds to the next one.

# Core Definition

As described in "Exploring JavaScript" Ch. 25, `continue` only works inside `while`, `do-while`, `for`, `for-of`, `for-await-of`, and `for-in`. It immediately leaves the current loop iteration and continues with the next one.

# Prerequisites

- Loop statements

# Key Properties

1. Only valid inside loop bodies (not `switch`).
2. Skips remaining statements in the current iteration.
3. The loop condition is re-evaluated before the next iteration.

# Construction / Recognition

```js
for (const line of lines) {
  if (line.startsWith('#')) continue;
  console.log(line);
}
```

# Context & Application

Useful for filtering out certain iterations without nesting code in an `else` block. Makes code flatter and more readable when skipping items.

# Examples

From the source text (Ch. 25, section 25.1.3):

```js
const lines = [
  'Normal line',
  '# Comment',
  'Another normal line',
];
for (const line of lines) {
  if (line.startsWith('#')) continue;
  console.log(line);
}
// Output: Normal line
//         Another normal line
```

# Relationships

## Contrasts With
- **Break Statement** -- `break` exits the loop entirely; `continue` only skips one iteration

# Common Errors

- **Error**: Trying to use `continue` inside a `switch` statement (without an enclosing loop).
  **Correction**: `continue` only works inside loops.

# Common Confusions

- **Confusion**: Thinking `continue` exits the loop.
  **Clarification**: `continue` only skips to the next iteration; `break` exits the loop.

# Source Reference

Chapter 25: Control flow statements, Section 25.1.3, lines 163-189.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit definition with example
- Cross-reference status: verified
