---
concept: Destructuring Default Values
slug: destructuring-default-values
category: destructuring
subcategory: null
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Destructuring"
chapter_number: 40
pdf_page: null
section: "40.10 Default values"
extraction_confidence: high
aliases:
  - "default values in destructuring"
prerequisites:
  - destructuring
extends: []
related:
  - object-destructuring
  - array-destructuring
contrasts_with: []
answers_questions:
  - "How do I use destructuring to extract values from objects and arrays?"
---

# Quick Definition

Default values in destructuring patterns (specified with `=`) provide fallback values when a matched position or property is `undefined` or missing.

# Core Definition

Normally, if a pattern has no match, the corresponding variable is set to `undefined`. A default value (via `=`) specifies a different value to use. Default values are triggered when the match result would be `undefined` -- either because the property/element doesn't exist, or because it exists but has value `undefined`.

# Prerequisites

- **destructuring** -- defaults extend destructuring

# Key Properties

1. Specified with `=` after the variable
2. Triggered when match result is `undefined`
3. Works in both object and array patterns
4. Compatible with property value shorthands: `{first='', last=''}`

# Construction / Recognition

```js
// Array destructuring defaults
const [x=1, y=2] = [];
// x === 1, y === 2

// Object destructuring defaults
const {first: f='', last: l=''} = {};
// f === '', l === ''

// Shorthand
const {first='', last=''} = {};
```

# Context & Application

Default values are essential for function options patterns and for handling partial data where some fields may be missing.

# Examples

```js
const [x=1, y=2] = [];
assert.equal(x, 1);
assert.equal(y, 2);

const {first='', last=''} = {};
assert.equal(first, '');
assert.equal(last, '');

const {prop: p = 123} = {};
assert.equal(p, 123);
```

(Chapter 40, Section 40.10, lines 633-697)

# Relationships

## Builds Upon
- **destructuring** -- enhances destructuring

## Enables
- Robust handling of partial data

## Related
- **object-destructuring** -- defaults in object patterns
- **array-destructuring** -- defaults in array patterns

## Contrasts With
- None

# Common Errors

- **Error**: Expecting defaults to trigger for `null`.
  **Correction**: Defaults only trigger for `undefined`, not `null`. Use nullish coalescing (`??`) for null handling.

# Common Confusions

- **Confusion**: Defaults trigger when a property is `null`.
  **Clarification**: Only `undefined` (or missing) triggers defaults. `null` is assigned as-is.

# Source Reference

Chapter 40: Destructuring, Section 40.10, lines 633-697.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly defined with examples
- Cross-reference status: verified
