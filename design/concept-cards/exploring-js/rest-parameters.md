---
concept: Rest Parameters
slug: rest-parameters
category: functions
subcategory: parameters
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Callable values"
chapter_number: 27
pdf_page: null
section: "27.6.5 Rest parameters"
extraction_confidence: high
aliases:
  - "rest parameter"
  - "variadic parameters"
  - "...args"
prerequisites:
  - ordinary-function
extends: []
related:
  - spread-into-function-calls
  - parameter-default-values
contrasts_with:
  - spread-into-function-calls
answers_questions:
  - "How do I accept a variable number of arguments?"
---

# Quick Definition

A rest parameter (ES6), declared with `...name`, collects all remaining arguments into an Array.

# Core Definition

As described in "Exploring JavaScript" Ch. 27, a rest parameter is declared by prefixing an identifier with `...`. During a call, it receives an Array with all remaining arguments. If there are no extra arguments, it is an empty Array. Only one rest parameter is allowed, and it must be last. Introduced in ES6.

# Prerequisites

- Ordinary function (or arrow function)

# Key Properties

1. Introduced in ES6.
2. Must be the last parameter.
3. Only one rest parameter per function.
4. Collects remaining arguments into a real Array (not Arguments object).
5. Empty Array if no remaining arguments.

# Construction / Recognition

```js
function f(x, ...y) {
  return [x, y];
}
f('a', 'b', 'c'); // ['a', ['b', 'c']]
```

# Context & Application

Used for variadic functions that accept any number of arguments. Replaces the legacy `arguments` object with a proper Array.

# Examples

From the source text (Ch. 27, section 27.6.5):

```js
function f(x, ...y) {
  return [x, y];
}
assert.deepEqual(f('a', 'b', 'c'), ['a', ['b', 'c']]);
assert.deepEqual(f(), [undefined, []]);
```

# Relationships

## Related
- **Parameter Default Values** -- another ES6 parameter feature

## Contrasts With
- **Spread Into Function Calls** -- spread expands; rest collects. Same `...` syntax, opposite directions.

# Common Errors

- **Error**: Placing the rest parameter before other parameters.
  **Correction**: Rest parameters must always be last: `function f(...rest, last) {}` is a SyntaxError.

# Common Confusions

- **Confusion**: Confusing rest parameters with spread arguments.
  **Clarification**: Rest (definition side) collects arguments into an Array; spread (call side) expands an iterable into arguments.

# Source Reference

Chapter 27: Callable values, Section 27.6.5, lines 1226-1298.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit definition with restrictions
- Cross-reference status: verified
