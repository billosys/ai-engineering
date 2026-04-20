---
# === CORE IDENTIFICATION ===
concept: Default Parameters
slug: default-parameters

# === CLASSIFICATION ===
category: functions
subcategory: function-inputs
tier: foundational

# === PROVENANCE ===
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Functions"
chapter_number: 3
pdf_page: null
section: "Optional Arguments"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - parameter defaults
  - default argument values

# === TYPED RELATIONSHIPS ===
prerequisites:
  - parameters
  - optional-arguments
extends:
  - optional-arguments
related:
  - rest-parameters
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I define and call a function?"
---

# Quick Definition

Default parameters allow you to specify a fallback value for a function parameter using `=`, which is used when the argument is not provided or is `undefined`.

# Core Definition

As described in "Eloquent JavaScript" (Ch 3, lines 458-462 of 03-functions.md): "If you write an `=` operator after a parameter, followed by an expression, the value of that expression will replace the argument when it is not given. For example, this version of `roundTo` makes its second argument optional. If you don't provide it or pass the value `undefined`, it will default to one."

# Prerequisites

- **parameters**: Default parameters modify how parameters receive values.
- **optional-arguments**: Default parameters build on JavaScript's flexible argument handling.

# Key Properties

1. Written as `parameter = defaultValue` in the parameter list.
2. The default is used when the argument is **not given** or is **`undefined`**.
3. The default value can be any expression (not just a constant).
4. Only parameters with defaults can be safely omitted.

# Construction / Recognition

## To Construct/Create:
```javascript
function roundTo(n, step = 1) {
  let remainder = n % step;
  return n - remainder + (remainder < step / 2 ? 0 : step);
}
```

## To Identify/Recognize:
- `=` after a parameter name in the function definition.

# Context & Application

Default parameters provide a clean way to make function arguments optional without manual `undefined` checks. They make function signatures more self-documenting.

# Examples

**Example 1** (Ch 3, lines 464-474 of 03-functions.md):
```javascript
function roundTo(n, step = 1) {
  let remainder = n % step;
  return n - remainder + (remainder < step / 2 ? 0 : step);
};
console.log(roundTo(4.5));
// → 5
console.log(roundTo(4.5, 2));
// → 4
```

# Relationships

## Builds Upon
- **optional-arguments** -- Default parameters formalize optional argument handling.
- **parameters** -- Default parameters are parameters with fallback values.

## Enables
- More readable and self-documenting function signatures.

## Related
- **rest-parameters** -- Another parameter feature for flexible argument handling.

## Contrasts With
- None within this source.

# Common Errors

- **Error**: Expecting `null` to trigger the default value.
  **Correction**: Only `undefined` (or omission) triggers the default. Passing `null` explicitly uses `null` as the value.

# Common Confusions

- **Confusion**: Default parameters are the same as checking for `undefined` in the body.
  **Clarification**: They are similar in effect, but default parameters are more concise and appear in the function signature, making the API clearer.

# Source Reference

Chapter 3: Functions, Section "Optional Arguments", lines 457-474 of 03-functions.md (book.md line 2297).

# Verification Notes

- Definition source: direct (quoted from lines 458-462)
- Confidence rationale: Explicit explanation with example
- Cross-reference status: verified within chapter
