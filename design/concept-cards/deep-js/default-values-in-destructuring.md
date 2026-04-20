---
# === CORE IDENTIFICATION ===
concept: Default Values in Destructuring
slug: default-values-in-destructuring

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
section: "3.4.4 Conclusion: Default values are a feature of pattern parts"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - destructuring defaults

# === TYPED RELATIONSHIPS ===
prerequisites:
  - destructuring-assignment
  - object-pattern
  - array-pattern
extends: []
related:
  - pattern-matching-algorithm
  - nested-destructuring
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is destructuring in JavaScript?"
  - "How do I destructure nested objects and arrays?"
---

# Quick Definition

Default values in destructuring provide fallback values that are used when a destructured property or element is `undefined` or missing.

# Core Definition

As described in "Deep JavaScript" (Ch 3, Section 3.4.4): "Default values are a feature of pattern parts (object properties or Array elements). If a part has no match or is matched against `undefined` then the default value is used. That is, the pattern is matched against the default value, instead." The check is specifically against `undefined` — not `null` or other falsy values. In object patterns (rule 2d), `obj.key !== undefined` determines whether the actual value or the default is used. In array patterns (rule 3d), the same check applies to iterator values.

# Prerequisites

- **Destructuring assignment** — Defaults are used within destructuring.
- **Object pattern** — Rule 2d defines default behavior for objects.
- **Array pattern** — Rule 3d defines default behavior for arrays.

# Key Properties

1. Triggered when the matched value is `undefined` (or missing).
2. Not triggered by `null`, `0`, `''`, or other falsy values.
3. The **pattern** is matched against the default value (enabling nested defaults).
4. Defaults are a property of individual pattern parts, not the whole pattern.
5. Default values can be any expression (evaluated lazily, only when needed).

# Construction / Recognition

## To Construct/Create:
1. Add `= defaultValue` after a variable or pattern in a destructuring expression.
2. For object patterns: `{key: pattern = default}`.
3. For array patterns: `[pattern = default]`.

## To Identify/Recognize:
1. The `=` sign within a destructuring pattern (not to be confused with assignment).

# Context & Application

Default values are critical for function parameters with optional properties. The chapter uses the distinction between `move1({x=0, y=0} = {})` and `move2({x, y} = {x: 0, y: 0})` to illustrate that defaults on individual pattern parts are more robust than a single default for the whole parameter.

# Examples

**Example 1** (Ch 3): Rule 2d (object pattern default):
```js
// Rule: {key: «pattern» = default_value, «properties»} ← obj
const tmp = obj.key;
if (tmp !== undefined) {
  «pattern» ← tmp
} else {
  «pattern» ← default_value
}
```

**Example 2** (Ch 3): move1 vs. move2 — why per-property defaults are better:
```js
function move1({x=0, y=0} = {}) { return [x, y]; }
function move2({x, y} = { x: 0, y: 0 }) { return [x, y]; }

// move1 works correctly in all cases:
assert.deepEqual(move1({z: 3}), [0, 0]);

// move2 fails: defaults are ignored because argument is not undefined
// {x, y} ← {z: 3} → x and y are both undefined
```

**Example 3** (Ch 3): Per-property defaults win over whole-pattern defaults:
```js
// move1({z: 3}) → [{x=0, y=0} = {}] ← [{z: 3}]
// {x=0, y=0} ← {z: 3}  (actual arg used, not default {})
// x ← undefined → default 0, y ← undefined → default 0
// Result: [0, 0] ✓
```

# Relationships

## Builds Upon
- **Object pattern** — Rule 2d adds defaults to object patterns.
- **Array pattern** — Rule 3d adds defaults to array patterns.

## Enables
- **Robust function parameters** — Per-property defaults handle partial arguments.
- **Named parameters** — Combined with object destructuring for flexible function signatures.

## Related
- **Pattern matching algorithm** — Defaults are encoded in specific rules.

## Contrasts With
- None directly.

# Common Errors

- **Error**: Putting the default on the whole parameter instead of individual properties.
  **Correction**: `function move({x, y} = {x: 0, y: 0})` only uses the default when **no** argument is passed. Use `function move({x=0, y=0} = {})` for per-property defaults.

- **Error**: Expecting defaults to trigger for `null`.
  **Correction**: Defaults only trigger for `undefined`, not `null`. `const {x = 5} = {x: null}` assigns `null` to `x`.

# Common Confusions

- **Confusion**: A default value for a destructuring parameter replaces all missing properties.
  **Clarification**: The default for the whole parameter (e.g., `= {}`) is used only when the entire argument is `undefined`. Defaults on individual pattern parts (e.g., `x=0`) handle missing properties.

# Source Reference

Chapter 3: The destructuring algorithm, Sections 3.2.3-3.2.4 and 3.4, lines 202-551.

# Verification Notes

- Definition source: direct (quoted conclusion from Section 3.4.4)
- Confidence rationale: Central theme of the chapter with detailed examples
- Cross-reference status: verified
