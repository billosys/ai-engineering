---
concept: Do-While Loop
slug: do-while-loop
category: control-flow
subcategory: loops
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Control flow statements"
chapter_number: 25
pdf_page: null
section: "25.6 `do-while` loops"
extraction_confidence: high
aliases:
  - "do-while statement"
prerequisites:
  - while-loop
extends:
  - while-loop
related:
  - while-loop
contrasts_with:
  - while-loop
answers_questions:
  - "How do I create a loop that runs at least once?"
---

# Quick Definition

The `do-while` loop executes its body first and then checks the condition, guaranteeing at least one execution.

# Core Definition

As described in "Exploring JavaScript" Ch. 25, the `do-while` loop works like `while` but checks its condition after each loop iteration, not before. Introduced in ES3. It can be viewed as a `while` loop that runs at least once.

# Prerequisites

- While loop

# Key Properties

1. Introduced in ES3.
2. Condition checked after each iteration (body always runs at least once).
3. Useful for input validation loops.

# Construction / Recognition

```js
do {
  // body
} while (condition);
```

# Context & Application

Used when the loop body must execute at least once, such as prompting for user input until valid input is received.

# Examples

From the source text (Ch. 25, section 25.6):

```js
let input;
do {
  input = prompt('Enter text:');
  console.log(input);
} while (input !== ':q');
```

# Relationships

## Builds Upon
- **While Loop** -- same semantics but condition checked after the body

## Contrasts With
- **While Loop** -- `while` may execute zero times; `do-while` always executes at least once

# Common Errors

- **Error**: Forgetting the semicolon after `while (condition);`.
  **Correction**: The `do-while` statement requires a trailing semicolon.

# Common Confusions

- **Confusion**: Treating `do-while` and `while` as identical.
  **Clarification**: `do-while` always runs the body at least once because the condition is checked after execution.

# Source Reference

Chapter 25: Control flow statements, Section 25.6, lines 584-604.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit definition in source
- Cross-reference status: verified
