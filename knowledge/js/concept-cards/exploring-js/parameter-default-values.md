---
concept: Parameter Default Values
slug: parameter-default-values
category: functions
subcategory: parameters
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Callable values"
chapter_number: 27
pdf_page: null
section: "27.6.4 Parameter default values"
extraction_confidence: high
aliases:
  - "default parameters"
prerequisites:
  - ordinary-function
extends: []
related:
  - rest-parameters
contrasts_with: []
answers_questions:
  - "How do I provide default values for function parameters?"
---

# Quick Definition

Parameter default values (ES6) specify the value to use when a parameter is not provided or is explicitly `undefined`.

# Core Definition

As described in "Exploring JavaScript" Ch. 27, parameter default values use the syntax `function f(x, y=0)`. The default is used when the argument is missing or is `undefined`. Other falsy values like `null`, `0`, or `''` do not trigger the default. Introduced in ES6.

# Prerequisites

- Ordinary function (or arrow function)

# Key Properties

1. Introduced in ES6.
2. Triggered by missing arguments or explicit `undefined`.
3. Not triggered by `null`, `0`, `''`, or other falsy values.
4. Default expressions are evaluated lazily (only when needed).
5. Can reference earlier parameters.

# Construction / Recognition

```js
function f(x, y = 0) {
  return [x, y];
}
```

# Context & Application

Used to make parameters optional with sensible fallback values, reducing the need for explicit `undefined` checks inside functions.

# Examples

From the source text (Ch. 27, section 27.6.4):

```js
function f(x, y=0) {
  return [x, y];
}
assert.deepEqual(f(1), [1, 0]);
assert.deepEqual(f(), [undefined, 0]);
assert.deepEqual(f(undefined, undefined), [undefined, 0]);
```

# Relationships

## Related
- **Rest Parameters** -- another ES6 parameter feature

# Common Errors

- **Error**: Expecting `null` to trigger the default value.
  **Correction**: Only `undefined` (or a missing argument) triggers defaults. `null` is passed through as-is.

# Common Confusions

- **Confusion**: Thinking defaults work like the `||` pattern.
  **Clarification**: `||` treats all falsy values as "missing"; defaults only treat `undefined` as missing.

# Source Reference

Chapter 27: Callable values, Section 27.6.4, lines 1199-1224.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit examples showing undefined behavior
- Cross-reference status: verified
