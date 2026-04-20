---
# === CORE IDENTIFICATION ===
concept: for Loop
slug: for-loop

# === CLASSIFICATION ===
category: language-fundamentals
subcategory: statements
tier: foundational

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Statements"
chapter_number: 5
pdf_page: 123
section: "5.4.3 for"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "C-style for loop"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - while-loop
  - compound-and-empty-statements
extends: []
related:
  - for-of-loop
  - for-in-loop
  - break-continue-statements
contrasts_with:
  - for-of-loop
  - for-in-loop

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I understand before learning about closures? (scope, statements)"
---

# Quick Definition

The `for` loop encodes initialization, test, and increment as three explicit expressions, providing a compact and structured alternative to the `while` loop for counter-based iteration.

# Core Definition

"The for statement provides a looping construct that is often more convenient than the while statement... The for statement encodes each of these three manipulations [initialize, test, increment] as an expression and makes those expressions an explicit part of the loop syntax: `for(initialize ; test ; increment) statement`." (Ch. 5, §5.4.3)

# Prerequisites

- **while-loop** — The `for` loop is equivalent to a structured `while` loop.
- **compound-and-empty-statements** — Loop body is typically a block statement.

# Key Properties

1. Three expressions: `initialize` (runs once), `test` (checked before each iteration), `increment` (runs after each iteration body).
2. Any of the three expressions may be omitted; two semicolons are required.
3. `for(;;)` is an infinite loop (equivalent to `while(true)`).
4. `initialize` can be a variable declaration with `let` (block-scoped to the loop).
5. The comma operator can combine multiple expressions in `initialize` or `increment`.
6. `continue` in a `for` loop evaluates the increment expression before re-testing.

# Construction / Recognition

```js
for (initialize; test; increment)
    statement
```

# Context & Application

The `for` loop is the most common loop when the number of iterations is known or controlled by a counter variable. It is ubiquitous in array traversal and counted iteration.

# Examples

From the source text (§5.4.3, pp. 123-125):

```js
for(let count = 0; count < 10; count++) {
    console.log(count);
}

// Multiple variables with comma operator
let i, j, sum = 0;
for(i = 0, j = 10; i < 10; i++, j--) {
    sum += i * j;
}

// Traversing a linked list
function tail(o) {
    for(; o.next; o = o.next) /* empty */ ;
    return o;
}
```

# Relationships

## Builds Upon
- **while-loop** — `for` is a structured equivalent of `while` with init and increment

## Enables
- Counter-based iteration, array traversal

## Related
- **for-of-loop** — Iterates over values of iterables (different paradigm)
- **for-in-loop** — Iterates over property names
- **break-continue-statements** — Used to control loop flow

## Contrasts With
- **for-of-loop** — `for` uses indices; `for/of` uses iterable values
- **for-in-loop** — `for/in` enumerates property names

# Common Errors

- **Error**: Assuming `continue` in a `for` loop skips the increment.
  **Correction**: In a `for` loop, `continue` evaluates the increment expression before re-testing the condition. This differs from `while`.

# Common Confusions

- **Confusion**: Believing a `for` loop can be perfectly simulated by a `while` loop.
  **Clarification**: Due to `continue` behavior differences, a `while` loop is not an exact equivalent of a `for` loop. A `try/finally` is needed for perfect simulation.

# Source Reference

Chapter 5: Statements, Section 5.4.3, pages 123-125.

# Verification Notes

- Definition source: Direct quote from §5.4.3
- Confidence rationale: High — detailed explanation with equivalences
- Uncertainties: None
- Cross-reference status: Verified
