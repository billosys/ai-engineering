---
# === CORE IDENTIFICATION ===
concept: Named Parameters via Destructuring
slug: named-parameters-via-destructuring

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
section: "3.4 Applying the algorithm"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - options object pattern
  - destructured parameters

# === TYPED RELATIONSHIPS ===
prerequisites:
  - destructuring-assignment
  - object-pattern
  - default-values-in-destructuring
extends:
  - object-pattern
related:
  - pattern-matching-algorithm
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is destructuring in JavaScript?"
  - "How do I destructure nested objects and arrays?"
---

# Quick Definition

Named parameters in JavaScript are simulated by destructuring an object parameter, allowing callers to pass an object literal with named properties instead of relying on positional arguments.

# Core Definition

As described in "Deep JavaScript" (Ch 3, Section 3.4): "In JavaScript, named parameters are simulated via objects: The caller uses an object literal and the callee uses destructuring." The chapter demonstrates two approaches — `move1({x=0, y=0} = {})` with per-property defaults and `move2({x, y} = {x: 0, y: 0})` with a whole-object default — and shows why per-property defaults are more robust using the pattern matching algorithm.

# Prerequisites

- **Destructuring assignment** — Named parameters use destructuring.
- **Object pattern** — The parameter is an object pattern.
- **Default values in destructuring** — Per-property defaults make named parameters robust.

# Key Properties

1. Caller uses an object literal: `func({x: 3, y: 8})`.
2. Callee destructures the parameter: `function func({x, y})`.
3. Per-property defaults (`{x=0, y=0}`) handle missing properties.
4. A whole-pattern default (`= {}`) handles the case of no argument at all.
5. Formal parameters are matched against actual parameters like destructuring.

# Construction / Recognition

## To Construct/Create:
1. Define a function with an object pattern as a parameter.
2. Add per-property defaults for optional named parameters.
3. Add `= {}` as the parameter default to allow calling with no arguments.

## To Identify/Recognize:
1. Function parameters using object destructuring syntax.

# Context & Application

Named parameters are a common JavaScript pattern for functions with many optional parameters. The destructuring approach is cleaner than positional parameters and more maintainable as APIs evolve. The per-property default pattern (`move1`) is preferred over the whole-object default pattern (`move2`).

# Examples

**Example 1** (Ch 3): The correct pattern:
```js
function move1({x=0, y=0} = {}) {
  return [x, y];
}
assert.deepEqual(move1({x: 3, y: 8}), [3, 8]);
assert.deepEqual(move1({x: 3}), [3, 0]);
assert.deepEqual(move1({}), [0, 0]);
assert.deepEqual(move1(), [0, 0]);
```

**Example 2** (Ch 3): The problematic pattern:
```js
function move2({x, y} = { x: 0, y: 0 }) {
  return [x, y];
}
// Fails for partial arguments:
// move2({z: 3}) → x and y are both undefined
```

**Example 3** (Ch 3): Parameter matching expressed as destructuring:
```js
function func(a=0, b=0) { ··· }
func(1, 2);
// equivalent to: [a=0, b=0] ← [1, 2]
```

# Relationships

## Builds Upon
- **Object pattern** — Parameters are destructured using object patterns.
- **Default values in destructuring** — Per-property defaults handle optional parameters.

## Enables
- **Flexible APIs** — Functions can accept any subset of named parameters.

## Related
- **Pattern matching algorithm** — Explains the detailed behavior.

## Contrasts With
- None directly.

# Common Errors

- **Error**: Using `{x, y} = {x: 0, y: 0}` instead of `{x=0, y=0} = {}`.
  **Correction**: The whole-object default is only used when the argument is `undefined`. With a partial argument like `{z: 3}`, individual properties are `undefined` and no defaults apply. Use per-property defaults.

# Common Confusions

- **Confusion**: The `= {}` default and per-property defaults serve the same purpose.
  **Clarification**: The `= {}` default handles the case of no argument at all. Per-property defaults (`x=0, y=0`) handle missing individual properties. Both are needed for a robust API.

# Source Reference

Chapter 3: The destructuring algorithm, Section 3.4, lines 355-551.

# Verification Notes

- Definition source: direct (quoted and demonstrated in source)
- Confidence rationale: Central example of the chapter with detailed walkthrough
- Cross-reference status: verified
