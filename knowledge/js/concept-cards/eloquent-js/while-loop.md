---
# === CORE IDENTIFICATION ===
concept: While Loop
slug: while-loop

# === CLASSIFICATION ===
category: control-flow
subcategory: iteration
tier: foundational

# === PROVENANCE ===
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Program Structure"
chapter_number: 2
pdf_page: null
section: "while and do loops"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - while statement

# === TYPED RELATIONSHIPS ===
prerequisites:
  - boolean
  - statement
  - control-flow
  - binding
extends: []
related:
  - do-loop
  - for-loop
  - break-statement
  - continue-statement
contrasts_with:
  - do-loop
  - for-loop

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I know before understanding closures?"
  - "What must I know before learning about prototypes and classes?"
---

# Quick Definition

A `while` loop repeatedly executes a statement (its body) as long as a given expression produces a value that converts to `true`.

# Core Definition

As described in "Eloquent JavaScript" (Ch 2, lines 516-520 of 02-program-structure.md): "A statement starting with the keyword `while` creates a loop. The word `while` is followed by an expression in parentheses and then a statement, much like `if`. The loop keeps entering that statement as long as the expression produces a value that gives `true` when converted to Boolean."

# Prerequisites

- **Boolean** -- The condition is evaluated as Boolean.
- **Statement** -- The loop body is a statement (usually a block).
- **Control Flow** -- Loops are a form of control flow.
- **Binding** -- Loops typically use bindings to track progress.

# Key Properties

1. Checks the condition **before each iteration** (line 519).
2. Executes the body **zero or more times** (if the condition is initially false, the body never executes).
3. Structure: `while (condition) { body }` (lines 517-518).
4. Commonly used with a **counter binding** to track loop progress (lines 523-527).
5. Without a mechanism to eventually make the condition false, creates an **infinite loop** (lines 702-704).

# Construction / Recognition

## To Construct/Create:
1. `while (condition) { body }`.
2. Typically: initialize a counter, test it in the condition, update it in the body.

## To Identify/Recognize:
1. The `while` keyword followed by a parenthesized condition and a body.

# Context & Application

While loops are used when the number of iterations is not known in advance and depends on a condition. They are one of the most fundamental iteration mechanisms in JavaScript.

# Examples

**Example 1** (Ch 2, lines 504-513): Printing even numbers:
```js
let number = 0;
while (number <= 12) {
  console.log(number);
  number = number + 2;
}
// → 0
// → 2
//   … etcetera
```

**Example 2** (Ch 2, lines 537-546): Computing 2^10:
```js
let result = 1;
let counter = 0;
while (counter < 10) {
  result = result * 2;
  counter = counter + 1;
}
console.log(result);
// → 1024
```

# Relationships

## Builds Upon
- **Boolean** -- Condition is Boolean.
- **Binding** -- Counter bindings track loop state.
- **Control Flow** -- Loops alter control flow.

## Enables
- Repeated computation.
- Iteration over data (in later chapters).

## Related
- **For Loop** -- A more compact loop form for the common counter pattern.
- **Break Statement** -- Can exit a while loop early.
- **Continue Statement** -- Can skip to the next iteration.

## Contrasts With
- **Do Loop** -- Checks condition after the body, guaranteeing at least one execution.
- **For Loop** -- Groups initialization, condition, and update together.

# Common Errors

- **Error**: Forgetting to update the counter, creating an infinite loop.
  **Correction**: Ensure the loop body modifies a value that eventually makes the condition false.

# Common Confusions

- **Confusion**: `while` and `do...while` are identical.
  **Clarification**: `while` checks the condition first and may execute zero times. `do...while` always executes at least once.

# Source Reference

Chapter 2: Program Structure, Section "while and do loops", lines 472-557 of 02-program-structure.md (book.md line 1304).

# Verification Notes

- Definition source: direct (quoted from source)
- Confidence rationale: Dedicated section with explicit definition
- Cross-reference status: verified within chapter
