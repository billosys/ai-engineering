---
concept: Optional Chaining
slug: optional-chaining
category: objects
subcategory: property-access
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Objects"
chapter_number: 30
pdf_page: null
section: "30.7 Optional chaining for property getting and method calls"
extraction_confidence: high
aliases:
  - "?."
  - "optional chaining operator"
prerequisites:
  - object-literal
extends: []
related: []
contrasts_with: []
answers_questions:
  - "How do I safely access deeply nested properties?"
---

# Quick Definition

Optional chaining (`?.`) short-circuits property access or method calls when the left-hand side is `null` or `undefined`, returning `undefined` instead of throwing.

# Core Definition

As described in "Exploring JavaScript" Ch. 30, three optional chaining operators exist: `obj?.prop` (fixed property), `obj?.[expr]` (dynamic property), and `func?.(args)` (function/method call). If the value before `?.` is `null` or `undefined`, the operation returns `undefined` immediately (short-circuiting). Otherwise, it proceeds normally. Introduced in ES2020.

# Prerequisites

- Object literal

# Key Properties

1. Introduced in ES2020.
2. Three forms: `?.prop`, `?.[expr]`, `?.(args)`.
3. Short-circuits: stops evaluation of the whole chain.
4. `null?.prop` returns `undefined` (not `null`).
5. Non-callable values (other than null/undefined) still throw TypeError with `?.()`.

# Construction / Recognition

```js
const name = person?.address?.street?.name;
const result = obj?.method?.(arg);
```

# Context & Application

Useful for accessing properties in data of uncertain shape. The author warns against overuse: it hides problems and makes refactoring harder.

# Examples

From the source text (Ch. 30, section 30.7.1):

```js
const streetNames = persons.map(p => p.address?.street?.name);
assert.deepEqual(streetNames, ['Sesame Street', undefined, undefined]);
```

# Relationships

## Related
- **Nullish Coalescing Operator** -- commonly combined: `obj?.prop ?? 'default'`

# Common Errors

- **Error**: Overusing optional chaining, hiding bugs that should surface early.
  **Correction**: Use optional chaining sparingly; consider extracting and normalizing data instead.

# Source Reference

Chapter 30: Objects, Section 30.7, lines 1576-1852.

# Verification Notes

- Definition source: direct
- Confidence rationale: Thorough coverage with all three forms
- Cross-reference status: verified
