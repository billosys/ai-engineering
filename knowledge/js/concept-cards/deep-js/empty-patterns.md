---
# === CORE IDENTIFICATION ===
concept: Empty Destructuring Patterns
slug: empty-patterns

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
section: "3.3 Empty object patterns and Array patterns"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - empty object pattern
  - empty array pattern

# === TYPED RELATIONSHIPS ===
prerequisites:
  - object-pattern
  - array-pattern
extends:
  - object-pattern
  - array-pattern
related:
  - pattern-matching-algorithm
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is destructuring in JavaScript?"
---

# Quick Definition

Empty destructuring patterns (`{}` and `[]`) extract no values but enforce constraints: `{}` requires the value is not `null` or `undefined`, and `[]` requires the value is iterable.

# Core Definition

As described in "Deep JavaScript" (Ch 3, Section 3.3): "Empty destructuring patterns force values to have certain characteristics, but have no other effects." An empty object pattern `{}` is legal for any value that is not `undefined` or `null` (otherwise `TypeError`). An empty array pattern `[]` is legal for any iterable value (otherwise `TypeError`). These follow directly from the algorithm's termination rules (2e and 3g) combined with the error rules (2a/2b and 3a).

# Prerequisites

- **Object pattern** — Empty object pattern `{}` is a special case.
- **Array pattern** — Empty array pattern `[]` is a special case.

# Key Properties

1. `{}` on any non-null, non-undefined value: no effect.
2. `{}` on `null` or `undefined`: throws `TypeError`.
3. `[]` on any iterable: no effect.
4. `[]` on non-iterable: throws `TypeError`.
5. Useful as type/protocol assertions.

# Construction / Recognition

## To Construct/Create:
1. `const {} = value;` — asserts value is not null/undefined.
2. `const [] = value;` — asserts value is iterable.

## To Identify/Recognize:
1. Empty braces or brackets on the left side of destructuring with no variable bindings.

# Context & Application

Empty patterns can be used as runtime assertions. While uncommon in practice, they demonstrate the algorithm's error-handling rules and help understand why certain destructuring expressions throw errors.

# Examples

**Example 1** (Ch 3): Empty object pattern:
```js
const {} = 123; // OK, neither undefined nor null
assert.throws(
  () => { const {} = null; },
  /^TypeError: Cannot destructure 'null' as it is null.$/);
```

**Example 2** (Ch 3): Empty array pattern:
```js
const [] = 'abc'; // OK, iterable
assert.throws(
  () => { const [] = 123; },  // not iterable
  /^TypeError: 123 is not iterable$/);
```

# Relationships

## Builds Upon
- **Object pattern** — Empty object pattern follows rules 2a, 2b, 2e.
- **Array pattern** — Empty array pattern follows rules 3a, 3b, 3g.

## Enables
- **Runtime assertions** — Can be used to assert value constraints.

## Related
- **Pattern matching algorithm** — Error and termination rules explain empty pattern behavior.

## Contrasts With
- None directly.

# Common Errors

- **Error**: Thinking `const {} = 0` throws an error.
  **Correction**: Any value that is not `null` or `undefined` can be destructured with `{}`. Numbers, strings, and booleans are all fine.

# Common Confusions

- **Confusion**: Empty patterns are useless syntax errors.
  **Clarification**: They are valid and enforce type constraints, though rarely used in practice.

# Source Reference

Chapter 3: The destructuring algorithm, Section 3.3, lines 320-353.

# Verification Notes

- Definition source: direct (quoted from source)
- Confidence rationale: Explicit discussion with examples
- Cross-reference status: verified
