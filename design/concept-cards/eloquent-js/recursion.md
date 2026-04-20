---
# === CORE IDENTIFICATION ===
concept: Recursion
slug: recursion

# === CLASSIFICATION ===
category: functions
subcategory: advanced-functions
tier: intermediate

# === PROVENANCE ===
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Functions"
chapter_number: 3
pdf_page: null
section: "Recursion"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - recursive function

# === TYPED RELATIONSHIPS ===
prerequisites:
  - function-definition
  - return-value
  - call-stack
  - conditional-execution
extends: []
related:
  - stack-overflow
  - closure
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a function?"
---

# Quick Definition

Recursion is when a function calls itself, allowing certain problems to be expressed more naturally than with loops, especially problems involving branching structures.

# Core Definition

As described in "Eloquent JavaScript" (Ch 3, lines 571-574 of 03-functions.md): "It is perfectly okay for a function to call itself, as long as it doesn't do it so often that it overflows the stack. A function that calls itself is called *recursive*. Recursion allows some functions to be written in a different style."

Further (lines 635-639): "Recursion is not always just an inefficient alternative to looping. Some problems really are easier to solve with recursion than with loops. Most often these are problems that require exploring or processing several 'branches', each of which might branch out again into even more branches."

# Prerequisites

- **function-definition**: Recursive functions are functions.
- **return-value**: Recursive calls use return values from sub-calls.
- **call-stack**: Each recursive call adds a frame to the call stack.
- **conditional-execution**: Base cases use conditionals to stop recursion.

# Key Properties

1. A recursive function calls itself.
2. Must have a **base case** that stops the recursion.
3. Typically about 3x slower than equivalent loops in JavaScript.
4. Particularly suited for problems with branching structures.
5. Trades efficiency for clarity in many cases.

# Construction / Recognition

## To Construct/Create:
1. Define a base case (when to stop).
2. Define the recursive case (call self with a simpler input).

## To Identify/Recognize:
- A function that contains a call to itself.

# Context & Application

Recursion is essential for tree traversal, graph exploration, divide-and-conquer algorithms, and any problem with a naturally recursive structure. The author advises starting with correct, readable code and optimizing later if needed.

# Examples

**Example 1** (Ch 3, lines 578-589 of 03-functions.md) -- power function:
```javascript
function power(base, exponent) {
  if (exponent == 0) {
    return 1;
  } else {
    return base * power(base, exponent - 1);
  }
}
console.log(power(2, 3));
// → 8
```

**Example 2** (Ch 3, lines 653-670 of 03-functions.md) -- findSolution:
```javascript
function findSolution(target) {
  function find(current, history) {
    if (current == target) {
      return history;
    } else if (current > target) {
      return null;
    } else {
      return find(current + 5, `(${history} + 5)`) ??
             find(current * 3, `(${history} * 3)`);
    }
  }
  return find(1, "1");
}
console.log(findSolution(24));
// → (((1 * 3) + 5) * 3)
```

# Relationships

## Builds Upon
- **function-definition** -- Recursive functions are functions.
- **call-stack** -- Each recursive call uses stack space.

## Enables
- Solutions to branching/tree-structured problems.

## Related
- **stack-overflow** -- Unbounded recursion causes stack overflow.
- **closure** -- The `findSolution` example uses nested functions with closures.

## Contrasts With
- None within this source (implicitly contrasts with iterative loops).

# Common Errors

- **Error**: Forgetting the base case, leading to infinite recursion.
  **Correction**: Always include a condition that returns without a recursive call.

# Common Confusions

- **Confusion**: Recursion is always better or always worse than loops.
  **Clarification**: "The dilemma of speed versus elegance is an interesting one." Recursion is slower but sometimes much clearer, especially for branching problems.

# Source Reference

Chapter 3: Functions, Section "Recursion", lines 568-737 of 03-functions.md (book.md line 2297).

# Verification Notes

- Definition source: direct (quoted from lines 571-574)
- Confidence rationale: Explicit definition with italicized term "recursive"
- Cross-reference status: verified within chapter
