---
# === CORE IDENTIFICATION ===
concept: Rest Element in Destructuring
slug: rest-element

# === CLASSIFICATION ===
category: language-mechanics
subcategory: destructuring
tier: intermediate

# === PROVENANCE ===
source: "Deep JavaScript"
source_slug: deep-js
authors: "Dr. Axel Rauschmayer"
chapter: "The destructuring algorithm"
chapter_number: 3
section: "3.2.4 Rules for Array patterns"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - rest pattern
  - spread in destructuring
  - "...rest"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - array-pattern
  - destructuring-assignment
extends:
  - array-pattern
related:
  - pattern-matching-algorithm
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I destructure nested objects and arrays?"
---

# Quick Definition

A rest element (`...«pattern»`) in array destructuring collects all remaining iterator values into an array, and must always be the last element in the pattern.

# Core Definition

As described in "Deep JavaScript" (Ch 3, Section 3.2.4, rule 3f): The rest element `...«pattern» ← iterator` collects all remaining values from the iterator into a new array, then matches the pattern against that array. The algorithm creates a temporary array, iterates over remaining elements pushing each into the array, then matches the pattern against the result.

# Prerequisites

- **Array pattern** — Rest elements exist within array destructuring patterns.
- **Destructuring assignment** — Rest elements are part of the destructuring system.

# Key Properties

1. Syntax: `...«pattern»` within an array pattern.
2. Always the **last** element in the pattern.
3. Collects all remaining iterator values into a new array.
4. The `«pattern»` can be a variable or a nested pattern.
5. If the iterator is exhausted, produces an empty array.

# Construction / Recognition

## To Construct/Create:
1. Place `...variableName` as the last element in an array destructuring pattern.

## To Identify/Recognize:
1. Three dots `...` followed by a variable or pattern inside array destructuring brackets.

# Context & Application

Rest elements are used for splitting arrays into head and tail, collecting variable-length arguments, and extracting "everything else" from an iterable.

# Examples

**Example 1** (Ch 3): Rule 3f algorithm:
```js
// (3f) ...«pattern» ← iterator  (always last part!)
const tmp = [];
for (const elem of iterator) {
  tmp.push(elem);
}
«pattern» ← tmp
```

**Example 2**: Practical usage:
```js
const [first, ...rest] = [1, 2, 3, 4];
// first === 1
// rest === [2, 3, 4]
```

# Relationships

## Builds Upon
- **Array pattern** — Rest elements are a specialized element type within array patterns.

## Enables
- **Head/tail decomposition** — Common functional programming pattern: `const [head, ...tail] = arr`.

## Related
- **Pattern matching algorithm** — Rule 3f specifies rest element behavior.

## Contrasts With
- None in immediate taxonomy.

# Common Errors

- **Error**: Placing a rest element before other elements.
  **Correction**: Rest elements must be the last element. `const [...rest, last] = arr` is a syntax error.

# Common Confusions

- **Confusion**: Rest element in destructuring and spread syntax in array literals are the same.
  **Clarification**: They use the same `...` syntax but are different operations. Rest collects values during destructuring; spread expands values during construction.

# Source Reference

Chapter 3: The destructuring algorithm, Section 3.2.4, rule 3f, lines 291-299.

# Verification Notes

- Definition source: direct (rule quoted from source)
- Confidence rationale: Specific rule provided with algorithm
- Cross-reference status: verified
