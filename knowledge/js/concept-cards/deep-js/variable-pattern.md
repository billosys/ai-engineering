---
# === CORE IDENTIFICATION ===
concept: Variable Pattern
slug: variable-pattern

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
section: "3.2.2 Rules for variable"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - simple assignment pattern

# === TYPED RELATIONSHIPS ===
prerequisites:
  - destructuring-assignment
extends: []
related:
  - object-pattern
  - array-pattern
  - pattern-matching-algorithm
contrasts_with:
  - object-pattern
  - array-pattern

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is destructuring in JavaScript?"
---

# Quick Definition

A variable pattern is the simplest destructuring pattern — a plain variable name that is directly assigned the matched value, including `undefined` and `null`.

# Core Definition

As described in "Deep JavaScript" (Ch 3, Section 3.2.2, rule 1): The variable pattern rule states: `x ← value` (including `undefined` and `null`) results in `x = value`. This is the base case of the recursive destructuring algorithm — the point at which pattern matching results in actual variable assignment. A pattern is either a variable, an object pattern, or an array pattern; the variable pattern is the terminal case.

# Prerequisites

- **Destructuring assignment** — Variable patterns are the base case of destructuring.

# Key Properties

1. The simplest pattern type — just a variable name.
2. Assigns the value directly, including `undefined` and `null`.
3. Does not throw errors — any value is accepted.
4. Serves as the terminal/base case for the recursive algorithm.

# Construction / Recognition

## To Construct/Create:
1. Use a simple variable name in a destructuring position.

## To Identify/Recognize:
1. A plain identifier (not `{}` or `[]`) in a pattern position.

# Context & Application

Variable patterns appear as the innermost parts of every destructuring expression. When an object pattern has `{key: x}`, the `x` is a variable pattern. Every destructuring ultimately resolves to one or more variable pattern assignments.

# Examples

**Example 1** (Ch 3): Rule 1:
```
- (1) x ← value (including undefined and null)
  x = value
```

**Example 2** (Ch 3): Variable patterns as inner parts of object destructuring:
```js
// {first: f, last: l} ← obj
// Resolves to:
// f ← obj.first  →  f = obj.first  (variable pattern)
// l ← obj.last   →  l = obj.last   (variable pattern)
```

# Relationships

## Builds Upon
- **Destructuring assignment** — Variable pattern is the base case.

## Enables
- **All destructuring** — Every destructuring ultimately resolves to variable pattern assignments.

## Related
- **Object pattern** — Contains variable patterns as property values.
- **Array pattern** — Contains variable patterns as elements.

## Contrasts With
- **Object pattern** — Object patterns recurse into object properties; variable patterns terminate.
- **Array pattern** — Array patterns recurse over iterable elements; variable patterns terminate.

# Common Errors

- **Error**: Expecting a variable pattern to throw on `undefined`.
  **Correction**: Variable patterns accept any value including `undefined` and `null`. Only object and array patterns throw on certain values.

# Common Confusions

- **Confusion**: Variable patterns are different from normal variable assignment.
  **Clarification**: `x ← value` is exactly equivalent to `x = value`. The pattern matching algorithm simply produces a normal assignment at the variable level.

# Source Reference

Chapter 3: The destructuring algorithm, Section 3.2.2, rule 1, lines 170-178.

# Verification Notes

- Definition source: direct (rule quoted from source)
- Confidence rationale: Explicit rule provided
- Cross-reference status: verified
