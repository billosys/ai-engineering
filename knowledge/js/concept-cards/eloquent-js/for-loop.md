---
# === CORE IDENTIFICATION ===
concept: For Loop
slug: for-loop

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
section: "for loops"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - for statement

# === TYPED RELATIONSHIPS ===
prerequisites:
  - while-loop
  - binding
extends: []
related:
  - break-statement
  - continue-statement
contrasts_with:
  - while-loop
  - do-loop

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I know before understanding closures?"
  - "What must I know before learning about prototypes and classes?"
---

# Quick Definition

A `for` loop provides a shorter, more comprehensive form for the common loop pattern of initializing a counter, testing a condition, and updating the counter, grouping all three parts in the `for` header.

# Core Definition

As described in "Eloquent JavaScript" (Ch 2, lines 627-629 of 02-program-structure.md): "Because this pattern is so common, JavaScript and similar languages provide a slightly shorter and more comprehensive form, the `for` loop." And (lines 648-653): "The parentheses after a `for` keyword must contain two semicolons. The part before the first semicolon *initializes* the loop, usually by defining a binding. The second part is the expression that *checks* whether the loop must continue. The final part *updates* the state of the loop after every iteration."

# Prerequisites

- **While Loop** -- The for loop is a more compact version of the common while loop pattern.
- **Binding** -- The initializer typically defines a counter binding.

# Key Properties

1. Three-part header: **initialize; check; update** separated by semicolons (lines 649-652).
2. The initializer runs **once** before the loop starts.
3. The check runs **before each iteration** -- if false, the loop stops.
4. The update runs **after each iteration**.
5. "In most cases, this is shorter and clearer than a `while` construct" (line 653).
6. Any of the three parts can be **omitted** (e.g., for infinite loops with break) (lines 694-697).

# Construction / Recognition

## To Construct/Create:
1. `for (let i = 0; i < n; i++) { body }`.
2. `for (init; condition; update) { body }`.

## To Identify/Recognize:
1. The `for` keyword followed by parentheses containing two semicolons.

# Context & Application

For loops are the most common loop form when the number of iterations follows a counter pattern. They are used extensively for iterating over ranges, arrays (in later chapters), and any counted repetition.

# Examples

**Example 1** (Ch 2, lines 631-638): Printing even numbers:
```js
for (let number = 0; number <= 12; number = number + 2) {
  console.log(number);
}
// → 0
// → 2
//   … etcetera
```

**Example 2** (Ch 2, lines 659-666): Computing 2^10:
```js
let result = 1;
for (let counter = 0; counter < 10; counter = counter + 1) {
  result = result * 2;
}
console.log(result);
// → 1024
```

# Relationships

## Builds Upon
- **While Loop** -- For is a more compact form of the common while pattern.
- **Binding** -- Initializer typically defines a binding.

## Enables
- Counted iteration.
- Array traversal (later chapters).

## Related
- **Break Statement** -- Can exit a for loop early.
- **Continue Statement** -- Can skip to the next iteration.

## Contrasts With
- **While Loop** -- While separates init/check/update; for groups them.
- **Do Loop** -- Do always executes at least once; for checks first.

# Common Errors

- **Error**: Writing a for loop without an update, causing an infinite loop.
  **Correction**: The update part (third section in parentheses) must eventually make the condition false, or use `break`.

# Common Confusions

- **Confusion**: For loops and while loops have different capabilities.
  **Clarification**: Any for loop can be rewritten as a while loop and vice versa. For loops are a convenience for the common counter pattern.

# Source Reference

Chapter 2: Program Structure, Section "for loops", lines 616-666 of 02-program-structure.md (book.md line 1304).

# Verification Notes

- Definition source: direct (quoted from source)
- Confidence rationale: Dedicated section with explicit structure explanation
- Cross-reference status: verified within chapter
