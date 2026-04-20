---
concept: Non-Destructurable Values
slug: destructuring-non-destructurable-values
category: destructuring
subcategory: null
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Destructuring"
chapter_number: 40
pdf_page: null
section: "40.8 What values can't be destructured?"
extraction_confidence: high
aliases: []
prerequisites:
  - destructuring
  - object-destructuring
  - array-destructuring
extends: []
related: []
contrasts_with: []
answers_questions:
  - "How do I use destructuring to extract values from objects and arrays?"
---

# Quick Definition

Object destructuring fails on `undefined` and `null` (throws TypeError); Array destructuring fails on any non-iterable value (including `undefined`, `null`, numbers, and plain objects).

# Core Definition

Object-destructuring fails if the value is `undefined` or `null` -- the same values that cause property access via dot notation to fail. Array-destructuring demands that the value be iterable, so it fails on `undefined`, `null`, non-iterable primitives (numbers, booleans), and non-iterable objects. An empty pattern can be used as a guard: `const {} = value` throws on null/undefined; `const [] = value` throws on non-iterables.

# Prerequisites

- **destructuring** -- understanding patterns
- **object-destructuring** -- object pattern failure conditions
- **array-destructuring** -- array pattern failure conditions

# Key Properties

1. Object pattern: fails on `undefined` and `null`
2. Array pattern: fails on non-iterables
3. Empty object pattern `{}` = null/undefined guard
4. Empty array pattern `[]` = iterability guard
5. Other primitives (numbers, booleans, strings) can be object-destructured

# Construction / Recognition

```js
// These throw TypeError:
// const {prop} = undefined;
// const {prop} = null;
// const [x] = 123;
// const [x] = {};

// These work:
const {length} = 'abc'; // length === 3
const [a] = 'abc';      // a === 'a'
```

# Context & Application

Understanding failure cases prevents runtime errors when destructuring data that may be null, undefined, or of unexpected types.

# Examples

```js
function throwIfUndefinedOrNull(value) {
  const {} = value; // throws if undefined or null
}

function throwIfNotIterable(value) {
  const [] = value; // throws if not iterable
}

throwIfNotIterable('abc'); // OK: string is iterable
// throwIfNotIterable(true); // TypeError
```

(Chapter 40, Section 40.8, lines 561-627)

# Relationships

## Builds Upon
- **destructuring** -- failure modes

## Enables
- Defensive programming with destructuring

## Related
- None

## Contrasts With
- None

# Common Errors

- **Error**: Destructuring a potentially null API response without checking.
  **Correction**: Guard with `?? {}` or check for null/undefined first.

# Common Confusions

- **Confusion**: All primitives can be array-destructured.
  **Clarification**: Only iterable primitives (strings) can be array-destructured. Numbers and booleans cannot.

# Source Reference

Chapter 40: Destructuring, Section 40.8, lines 561-627.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly defined with examples
- Cross-reference status: verified
