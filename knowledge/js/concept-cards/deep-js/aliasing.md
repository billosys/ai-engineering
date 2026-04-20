---
# === CORE IDENTIFICATION ===
concept: Aliasing
slug: aliasing

# === CLASSIFICATION ===
category: data-management
subcategory: shared-state
tier: intermediate

# === PROVENANCE ===
source: "Deep JavaScript"
source_slug: deep-js
authors: "Dr. Axel Rauschmayer"
chapter: "The problems of shared mutable state and how to avoid them"
chapter_number: 9
section: "What is shared mutable state and why is it problematic?"

# === CONFIDENCE ===
extraction_confidence: medium

# === VARIANTS ===
aliases:
  - "shared references"
  - "reference aliasing"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - shared-mutable-state
  - defensive-copying
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is shared mutable state?"
---

# Quick Definition

Aliasing occurs when multiple variables, parameters, or properties reference the same object, creating the "shared" part of shared mutable state.

# Core Definition

As synthesized from "Deep JavaScript" Ch 9, aliasing is the fundamental mechanism by which data becomes shared. When a function receives an object as a parameter, the parameter is an alias for the caller's variable -- both reference the same object. Any mutation through one alias is visible through all others. In the Ch 9 motivating example, `logElements(arr)` creates an alias: the parameter `arr` inside `logElements` references the same array as `arr` in `main()`.

# Prerequisites

- **Object references** -- objects in JavaScript are accessed via references, not values

# Key Properties

1. Created whenever an object reference is passed to a function, assigned to another variable, or stored in a data structure.
2. All aliases point to the same underlying object.
3. Mutations through any alias affect all aliases.
4. Aliasing is ubiquitous in JavaScript -- it happens with every function call involving objects.
5. Only problematic when combined with mutation.

# Construction / Recognition

## To Construct/Create:
1. Pass an object as a function argument.
2. Assign an object reference to another variable.
3. Store an object reference in a collection.

## To Identify/Recognize:
1. Two variables satisfy `a === b` (same identity).
2. A function parameter references the caller's object.

# Context & Application

Aliasing is an inherent feature of pass-by-sharing semantics in JavaScript. It is not a problem by itself -- the problem emerges when aliased data is mutated. Understanding aliasing is the first step to understanding shared mutable state.

# Examples

**Example 1** (Ch 9): Function parameter aliasing:
```js
function logElements(arr) {
  // `arr` here is an alias for the array in main()
  while (arr.length > 0) {
    console.log(arr.shift()); // Mutates the shared array!
  }
}

function main() {
  const arr = ['banana', 'orange', 'apple'];
  logElements(arr); // Passes a reference, creating an alias
  // arr is now empty!
}
```

**Example 2** (Ch 9): Aliasing in `StringBuilder`:
```js
const sb = new StringBuilder();
sb.add('Hello');
const parts = sb.getParts(); // alias for internal _data
parts.length = 0; // Mutates internal state through alias!
```

# Relationships

## Builds Upon
- **Object references** -- aliasing is a consequence of reference-based object access

## Enables
- **Shared mutable state** -- aliasing creates the "shared" condition

## Related
- **Defensive copying** -- breaks aliasing by creating independent copies

## Contrasts With
(none at this specificity)

# Common Errors

- **Error**: Not realizing that passing an object to a function creates an alias.
  **Correction**: In JavaScript, objects are always passed by reference (sharing). The function can mutate the caller's data.

# Common Confusions

- **Confusion**: `const` prevents aliasing issues.
  **Clarification**: `const` only prevents reassignment of the variable itself. The referenced object can still be mutated through any alias.

# Source Reference

Chapter 9: "The problems of shared mutable state and how to avoid them", Section 9.1, lines 3878-3970.

# Verification Notes

- Definition source: synthesized from the motivating example and shared state definition
- Confidence rationale: The concept of aliasing is demonstrated but not explicitly named in the source. It is the implicit mechanism behind the shared state examples.
- Cross-reference status: verified against Ch 9 sections 9.1 and 9.2
