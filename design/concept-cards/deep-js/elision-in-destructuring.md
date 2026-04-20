---
# === CORE IDENTIFICATION ===
concept: Elision (Holes) in Array Destructuring
slug: elision-in-destructuring

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
  - holes in destructuring
  - array destructuring holes

# === TYPED RELATIONSHIPS ===
prerequisites:
  - array-pattern
extends:
  - array-pattern
related:
  - pattern-matching-algorithm
  - rest-element
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I destructure nested objects and arrays?"
---

# Quick Definition

Elision (holes) in array destructuring uses commas without patterns to skip iterator values, advancing the iterator without assigning.

# Core Definition

As described in "Deep JavaScript" (Ch 3, Section 3.2.4, rule 3e): The elision rule handles holes in array patterns: `, «elements» ← iterator` results in `getNext(iterator); // skip` followed by `«elements» ← iterator`. The iterator is advanced but the value is discarded. This enables selective extraction from iterables.

# Prerequisites

- **Array pattern** — Elision is a feature of array destructuring patterns.

# Key Properties

1. Syntax: empty positions (commas without patterns) in array patterns.
2. Advances the iterator by one position, discarding the value.
3. Can be used multiple times to skip multiple values.
4. Follows rule 3e of the pattern matching algorithm.

# Construction / Recognition

## To Construct/Create:
1. Place commas without variable names in an array pattern: `const [, second] = arr`.

## To Identify/Recognize:
1. Adjacent commas or leading commas in an array destructuring pattern.

# Context & Application

Elision is useful when you need a specific element by position but do not need preceding elements. For example, extracting only the third element of an array: `const [,,third] = arr`.

# Examples

**Example 1** (Ch 3): Rule 3e:
```
- (3e) , «elements» ← iterator  (hole, elision)
  getNext(iterator); // skip
  «elements» ← iterator
```

**Example 2**: Practical usage:
```js
const [, second, , fourth] = [1, 2, 3, 4];
// second === 2
// fourth === 4
```

# Relationships

## Builds Upon
- **Array pattern** — Elision is a special element type within array patterns.

## Enables
- **Selective extraction** — Extract specific positional elements without binding others.

## Related
- **Rest element** — Another way to handle remaining elements (collects vs. skips).

## Contrasts With
- None directly.

# Common Errors

- **Error**: Using elision in object patterns.
  **Correction**: Elision only works in array patterns. Object patterns use property keys, not positions.

# Common Confusions

- **Confusion**: Elision and the `undefined` value assignment are the same.
  **Clarification**: Elision discards the value entirely; it does not assign `undefined` to any variable. The iterator is advanced but nothing is stored.

# Source Reference

Chapter 3: The destructuring algorithm, Section 3.2.4, rule 3e, lines 284-289.

# Verification Notes

- Definition source: direct (rule quoted from source)
- Confidence rationale: Specific rule provided
- Cross-reference status: verified
