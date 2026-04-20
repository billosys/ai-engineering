---
# === CORE IDENTIFICATION ===
concept: Loop
slug: loop

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
  - looping
  - iteration

# === TYPED RELATIONSHIPS ===
prerequisites:
  - control-flow
  - statement
extends: []
related:
  - while-loop
  - do-loop
  - for-loop
  - break-statement
  - continue-statement
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I know before understanding closures?"
  - "What must I know before learning about prototypes and classes?"
---

# Quick Definition

A loop is a form of control flow that allows a piece of code to run multiple times, going back to a previous point in the program and repeating with the current state.

# Core Definition

As described in "Eloquent JavaScript" (Ch 2, lines 493-494 of 02-program-structure.md): "What we need is a way to run a piece of code multiple times. This form of control flow is called a *loop*." And (lines 499-502): "Looping control flow allows us to go back to some point in the program where we were before and repeat it with our current program state."

# Prerequisites

- **Control Flow** -- Loops are a form of control flow.
- **Statement** -- Loop bodies are statements.

# Key Properties

1. Allows running code **multiple times** (line 493).
2. Goes back to a **previous point** and repeats with current state (lines 500-501).
3. Three forms in JavaScript: `while`, `do`, and `for` (Ch 2 summary, line 889).
4. An **infinite loop** occurs when the termination condition is never satisfied (lines 702-704).
5. Can be exited early with `break` or have iterations skipped with `continue`.

# Construction / Recognition

## To Construct/Create:
1. Use `while (condition) { body }`.
2. Use `do { body } while (condition);`.
3. Use `for (init; condition; update) { body }`.

## To Identify/Recognize:
1. Code that repeats execution -- keywords `while`, `do`, or `for`.

# Context & Application

Loops are fundamental to programming. They enable processing collections of data, repeating computations, and any task that involves doing something more than once. The source introduces loops through the practical problem of printing even numbers without writing each `console.log` call manually.

# Examples

**Example 1** (Ch 2, lines 476-487): The problem that motivates loops -- printing even numbers without repetition:
```js
// Without a loop (tedious):
console.log(0);
console.log(2);
console.log(4);
// ... etc.
```

**Example 2** (Ch 2, lines 504-513): The solution with a while loop:
```js
let number = 0;
while (number <= 12) {
  console.log(number);
  number = number + 2;
}
```

# Relationships

## Builds Upon
- **Control Flow** -- Loops alter the flow of execution.
- **Statement** -- Loop bodies are statements.

## Enables
- **While Loop**, **Do Loop**, **For Loop** -- Specific loop forms.
- Repeated computation and data processing.

## Related
- **Break Statement** -- Exits a loop early.
- **Continue Statement** -- Skips to the next iteration.

## Contrasts With
- None directly.

# Common Errors

- **Error**: Creating an infinite loop by failing to update the termination condition.
  **Correction**: "A program stuck in an infinite loop will never finish running, which is usually a bad thing" (lines 703-704). Ensure the loop body modifies state to eventually make the condition false.

# Common Confusions

- **Confusion**: Loops always know how many times they will iterate.
  **Clarification**: While `for` loops often have a known count, `while` and `do` loops may iterate an unpredictable number of times based on runtime conditions.

# Source Reference

Chapter 2: Program Structure, Section "while and do loops", lines 472-580 of 02-program-structure.md (book.md line 1304).

# Verification Notes

- Definition source: direct (quoted from source)
- Confidence rationale: Explicit definition with italicized term
- Cross-reference status: verified within chapter
