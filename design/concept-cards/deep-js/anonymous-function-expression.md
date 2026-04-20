---
# === CORE IDENTIFICATION ===
concept: Anonymous Function Expression
slug: anonymous-function-expression

# === CLASSIFICATION ===
category: functions
subcategory: naming
tier: intermediate

# === PROVENANCE ===
source: "Deep JavaScript"
source_slug: deep-js
authors: "Dr. Axel Rauschmayer"
chapter: "The property .name of functions (bonus)"
chapter_number: 21
section: "21.2.2 Variable declarations and anonymous functions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "anonymous function"
  - "unnamed function expression"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - function-name-property
extends: []
related:
  - function-naming-rules
  - arrow-function-naming
contrasts_with:
  - named-function-expression

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes a named function expression from an anonymous function?"
---

# Quick Definition

An anonymous function expression is a function expression without an explicit name that gets its `.name` property inferred from context such as variable declarations, assignments, or property definitions.

# Core Definition

From "Deep JavaScript" (Ch 21.2.2): "A function created by an anonymous function expression picks up a name if it is the initialization value of a variable declaration." The name inference works for `let`, `const`, `var` declarations, assignments, default values, and property definitions. However, truly anonymous functions (e.g., returned from factories) have an empty string `''` as their name.

# Prerequisites

- **Function .name property** — Anonymous functions get their name through inference

# Key Properties

1. No explicit name in the function syntax: `function () {}` or `() => {}`
2. Name is inferred from context (variable, property, parameter, etc.)
3. If no context provides a name, `.name` is `''` (empty string)
4. Arrow functions follow the same inference rules

# Construction / Recognition

## To Construct/Create:
1. `const func = function () {};` -- name inferred as `'func'`
2. `const func = () => {};` -- name inferred as `'func'`

## To Identify/Recognize:
1. A function expression without a name between `function` and `(`

# Context & Application

Despite being "anonymous," most function expressions in practice get meaningful names through inference. Truly nameless functions only occur in specific patterns like factory returns or immediately invoked expressions.

# Examples

**Example 1** (Ch 21): Variable declaration inference:
```js
let letFunc = function () {};
assert.equal(letFunc.name, 'letFunc');

const constFunc = function () {};
assert.equal(constFunc.name, 'constFunc');
```

**Example 2** (Ch 21): Assignment inference:
```js
let assignedFunc;
assignedFunc = function () {};
assert.equal(assignedFunc.name, 'assignedFunc');
```

**Example 3** (Ch 21): No context -- truly anonymous:
```js
function functionFactory() {
  return function () {};
}
const func = functionFactory();
assert.equal(func.name, ''); // truly anonymous
```

# Relationships

## Builds Upon
- **Function .name property** — Name inference populates `.name`

## Related
- **Function naming rules** — The rules governing name inference
- **Arrow function naming** — Arrow functions are always anonymous expressions

## Contrasts With
- **Named function expression** — Has an explicit name that takes precedence

# Common Errors

- **Error**: Assuming all anonymous functions have empty names
  **Correction**: JavaScript infers names from context; only truly contextless functions have empty names

# Common Confusions

- **Confusion**: An arrow function assigned to `const` has no name
  **Clarification**: Arrow functions get names from variable declarations just like anonymous function expressions

# Source Reference

Chapter 21: The property .name of functions (bonus), Section 21.2.2, lines 11437+.

# Verification Notes

- Definition source: direct from source with examples
- Confidence rationale: Multiple examples with assertions
- Cross-reference status: verified
