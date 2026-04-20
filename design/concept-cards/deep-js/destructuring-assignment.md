---
# === CORE IDENTIFICATION ===
concept: Destructuring Assignment
slug: destructuring-assignment

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
section: "3.1 Preparing for the pattern matching algorithm"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - destructuring
  - pattern matching assignment

# === TYPED RELATIONSHIPS ===
prerequisites:
  - type-coercion
extends: []
related:
  - object-pattern
  - array-pattern
  - pattern-matching-algorithm
  - default-values-in-destructuring
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is destructuring in JavaScript?"
---

# Quick Definition

Destructuring assignment is a JavaScript syntax that uses patterns to extract data from objects and arrays, assigning matched values to variables.

# Core Definition

As described in "Deep JavaScript" (Ch 3, Section 3.1): "A destructuring assignment looks like this: `«pattern» = «value»`. We want to use `pattern` to extract data from `value`." The chapter presents destructuring as "a recursive pattern matching algorithm" specified via the match operator (`←`): "`«pattern» ← «value»`". Destructuring works for assignments, variable declarations, and parameter definitions.

# Prerequisites

- **Type coercion** — Destructuring builds on JavaScript's type system; patterns can interact with `undefined` and default values.

# Key Properties

1. Uses a **pattern** on the left-hand side to extract data from a **value** on the right-hand side.
2. Operates recursively — patterns can be nested.
3. Works for assignments, variable declarations (`const`, `let`, `var`), and function parameters.
4. Patterns are either: a variable, an object pattern `{...}`, or an array pattern `[...]`.
5. Throws `TypeError` when destructuring `null` or `undefined` with object patterns, or non-iterables with array patterns.

# Construction / Recognition

## To Construct/Create:
1. Write a pattern (object or array) on the left side of `=`.
2. The right side provides the value to destructure.
3. Variables in the pattern are assigned corresponding values.

## To Identify/Recognize:
1. Object or array literal syntax on the left side of an assignment, declaration, or parameter.

# Context & Application

Destructuring is used extensively in modern JavaScript for extracting values from function return values, importing module members, handling API responses, and defining function parameters. Named parameters are simulated by destructuring an object parameter.

# Examples

**Example 1** (Ch 3): Basic matching notation:
```js
«pattern» = «value»

// The algorithm specifies:
«pattern» ← «value»
```

**Example 2** (Ch 3): Named parameters via destructuring:
```js
function move1({x=0, y=0} = {}) {
  return [x, y];
}
assert.deepEqual(move1({x: 3, y: 8}), [3, 8]);
assert.deepEqual(move1({x: 3}), [3, 0]);
assert.deepEqual(move1({}), [0, 0]);
assert.deepEqual(move1(), [0, 0]);
```

# Relationships

## Builds Upon
- **Type coercion** — Default values interact with `undefined` checks.

## Enables
- **Object pattern** — One of the three pattern types.
- **Array pattern** — One of the three pattern types.
- **Nested destructuring** — Patterns can be nested recursively.
- **Default values in destructuring** — Patterns can include default values.

## Related
- **Pattern matching algorithm** — The formal algorithm that specifies how destructuring works.

## Contrasts With
- None directly.

# Common Errors

- **Error**: Destructuring `null` or `undefined` without a default.
  **Correction**: `const {x} = null` throws `TypeError`. Provide a default: `const {x} = value ?? {}`.

# Common Confusions

- **Confusion**: Destructuring creates objects or arrays.
  **Clarification**: Destructuring *extracts* from objects and arrays. The pattern syntax looks like a literal but is used for extraction, not construction.

# Source Reference

Chapter 3: The destructuring algorithm, Section 3.1, lines 1557-1600.

# Verification Notes

- Definition source: direct (quoted from source)
- Confidence rationale: Explicit definition and algorithm provided
- Cross-reference status: verified
