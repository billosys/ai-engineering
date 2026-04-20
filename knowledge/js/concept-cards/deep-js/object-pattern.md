---
# === CORE IDENTIFICATION ===
concept: Object Pattern
slug: object-pattern

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
section: "3.2.3 Rules for object patterns"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - object destructuring pattern

# === TYPED RELATIONSHIPS ===
prerequisites:
  - destructuring-assignment
  - pattern-matching-algorithm
extends:
  - destructuring-assignment
related:
  - array-pattern
  - default-values-in-destructuring
  - nested-destructuring
contrasts_with:
  - array-pattern

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is destructuring in JavaScript?"
  - "How do I destructure nested objects and arrays?"
---

# Quick Definition

An object pattern is a destructuring pattern that uses `{«properties»}` syntax to match against objects, extracting values by property key.

# Core Definition

As described in "Deep JavaScript" (Ch 3, Section 3.2.3): Object patterns are governed by rules 2a-2e. Rules 2a and 2b throw `TypeError` when matching against `undefined` or `null`. Rule 2c matches a property key and recurses: `«pattern» ← obj.key` then `{«properties»} ← obj`. Rule 2d handles default values: if `obj.key` is `undefined`, the default value is used. Rule 2e terminates when no properties remain.

# Prerequisites

- **Destructuring assignment** — Object patterns are one form of destructuring.
- **Pattern matching algorithm** — The rules that govern object pattern behavior.

# Key Properties

1. Matches against objects by property key.
2. Throws `TypeError` for `undefined` or `null` values (rules 2a, 2b).
3. Iterates over pattern properties recursively (rules 2c, 2d, 2e).
4. Supports default values via `=` syntax (rule 2d).
5. Property values can be nested patterns (enabling deep destructuring).
6. Supports property value shorthands: `{x}` is equivalent to `{x: x}`.

# Construction / Recognition

## To Construct/Create:
1. Use `{}` with property keys on the left side of an assignment.
2. Property values can be variables, nested patterns, or include defaults.

## To Identify/Recognize:
1. Curly braces on the left side of `=`, in a declaration, or in a parameter list.

# Context & Application

Object patterns are the most common form of destructuring in JavaScript. They are used for extracting properties from objects, handling function options objects, and importing named exports from modules.

# Examples

**Example 1** (Ch 3): Rules for object patterns:
```
- (2a) {«properties»} ← undefined    → throw new TypeError();
- (2b) {«properties»} ← null         → throw new TypeError();
- (2c) {key: «pattern», «properties»} ← obj
    «pattern» ← obj.key
    {«properties»} ← obj
- (2d) {key: «pattern» = default_value, «properties»} ← obj
    const tmp = obj.key;
    if (tmp !== undefined) { «pattern» ← tmp }
    else { «pattern» ← default_value }
    {«properties»} ← obj
- (2e) {} ← obj                      → // We are finished
```

**Example 2** (Ch 3): Empty object pattern as guard:
```js
const {} = 123; // OK, neither undefined nor null
assert.throws(
  () => { const {} = null; },
  /^TypeError/);
```

# Relationships

## Builds Upon
- **Destructuring assignment** — Object patterns are a type of destructuring.
- **Pattern matching algorithm** — Rules 2a-2e govern object patterns.

## Enables
- **Nested destructuring** — Object pattern property values can be nested patterns.
- **Default values in destructuring** — Rule 2d adds default value support.

## Related
- **Property value shorthands** — `{x}` means `{x: x}` in patterns.

## Contrasts With
- **Array pattern** — Array patterns use `[]` and iterate via iterators; object patterns use `{}` and access by key.

# Common Errors

- **Error**: Destructuring `null` without checking.
  **Correction**: Object patterns always throw `TypeError` on `null` or `undefined`. Provide a default: `const {x} = value ?? {}`.

# Common Confusions

- **Confusion**: Object patterns match by position (like arrays).
  **Clarification**: Object patterns match by property key name, not by position. Order does not matter.

# Source Reference

Chapter 3: The destructuring algorithm, Section 3.2.3, lines 180-224.

# Verification Notes

- Definition source: direct (rules quoted from source)
- Confidence rationale: Complete rule set provided
- Cross-reference status: verified
