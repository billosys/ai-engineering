---
# === CORE IDENTIFICATION ===
concept: Nested Destructuring
slug: nested-destructuring

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
section: "3.2 The pattern matching algorithm"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - deep destructuring

# === TYPED RELATIONSHIPS ===
prerequisites:
  - destructuring-assignment
  - object-pattern
  - array-pattern
extends:
  - object-pattern
  - array-pattern
related:
  - pattern-matching-algorithm
  - default-values-in-destructuring
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I destructure nested objects and arrays?"
---

# Quick Definition

Nested destructuring is the recursive application of destructuring patterns within other patterns, allowing extraction of values from deeply nested data structures in a single expression.

# Core Definition

As described in "Deep JavaScript" (Ch 3, Section 3.2): The destructuring algorithm is inherently recursive. In rule 2c, `{key: «pattern», «properties»} ← obj` means `«pattern»` can itself be an object or array pattern, not just a variable. Similarly, in rule 3c, array element `«pattern»` can be a nested pattern. This recursion enables arbitrary depth of extraction. Since "A pattern is either: A variable: `x`, An object pattern: `{«properties»}`, An Array pattern: `[«elements»]`", any position that accepts a pattern can contain a nested pattern.

# Prerequisites

- **Destructuring assignment** — Nested destructuring is a recursive application of destructuring.
- **Object pattern** — Nested patterns can appear as property values in object patterns.
- **Array pattern** — Nested patterns can appear as elements in array patterns.

# Key Properties

1. Any pattern position can contain another pattern (object or array).
2. Follows the same recursive algorithm — rules are applied at each nesting level.
3. Mixing object and array patterns is allowed.
4. Default values work at every nesting level.
5. Error handling (TypeError for null/undefined/non-iterable) applies at each level.

# Construction / Recognition

## To Construct/Create:
1. Place an object pattern `{...}` or array pattern `[...]` where a variable would go.
2. The nested pattern matches against the value extracted by the outer pattern.

## To Identify/Recognize:
1. Patterns within patterns: `{a: {b}}` or `[{x}, [y]]` etc.

# Context & Application

Nested destructuring is essential for working with complex data structures like API responses, configuration objects, and nested state. It extracts deeply nested values without intermediate variables.

# Examples

**Example 1** (Ch 3): Recursive nature shown by the rules:
```
// Rule 2c: {key: «pattern», «properties»} ← obj
// Here «pattern» can be another object pattern:
{a: {b: c}} ← {a: {b: 42}}

// Step 1: {b: c} ← obj.a → {b: c} ← {b: 42}
// Step 2: c ← {b: 42}.b → c = 42
```

**Example 2** (Ch 3): Mixed nesting from the move1 example:
```js
// Parameter destructuring with nesting:
[{x=0, y=0} = {}] ← [{z: 3}]

// Step 1: Array element matched → {x=0, y=0} ← {z: 3}
// Step 2: x ← {z:3}.x → undefined → default 0
// Step 3: y ← {z:3}.y → undefined → default 0
```

# Relationships

## Builds Upon
- **Object pattern** — Nested object patterns in property value positions.
- **Array pattern** — Nested patterns in element positions.

## Enables
- **Deep data extraction** — Single expressions can reach into complex structures.

## Related
- **Default values in destructuring** — Defaults work at every nesting level.
- **Pattern matching algorithm** — The recursive nature of the algorithm enables nesting.

## Contrasts With
- None directly.

# Common Errors

- **Error**: Not accounting for `undefined` at intermediate levels.
  **Correction**: If a nested property doesn't exist, the intermediate value is `undefined`, which causes a `TypeError` when the nested pattern tries to destructure it. Use defaults at each level.

# Common Confusions

- **Confusion**: Nested destructuring creates nested objects.
  **Clarification**: Nested destructuring only *extracts* from nested structures; it creates flat variables.

# Source Reference

Chapter 3: The destructuring algorithm, Section 3.2, lines 154-317.

# Verification Notes

- Definition source: synthesized (implicit in the recursive algorithm definition)
- Confidence rationale: High because the recursive nature of patterns is explicitly defined
- Cross-reference status: verified
