---
concept: Spreading Into Object Literals
slug: spreading-into-object-literals
category: objects
subcategory: creation
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Objects"
chapter_number: 30
pdf_page: null
section: "30.4 Spreading into object literals (`...`)"
extraction_confidence: high
aliases:
  - "object spread"
  - "spread properties"
prerequisites:
  - object-literal
extends: []
related:
  - object-assign
contrasts_with: []
answers_questions:
  - "How do I copy or merge object properties?"
---

# Quick Definition

Spread properties (`...obj`) in an object literal copy all enumerable own properties of another object into the new object, enabling shallow copies and non-destructive updates.

# Core Definition

As described in "Exploring JavaScript" Ch. 30, inside an object literal, a spread property `...obj` adds the properties of `obj` to the current object. If keys clash, the last one wins. All values are spreadable (even `undefined` and `null` produce empty results). Spreading copies shallowly -- nested objects are shared, not cloned. Introduced in ES2018.

# Prerequisites

- Object literal

# Key Properties

1. Introduced in ES2018.
2. Shallow copy: nested objects are shared.
3. Last property wins on key conflicts.
4. Spreading `undefined` or `null` produces `{}`.
5. Includes symbol-keyed properties.

# Construction / Recognition

```js
const copy = {...original};
const merged = {...defaults, ...provided};
const updated = {...obj, changedProp: newValue};
```

# Context & Application

Three main use cases: providing default values, non-destructively changing properties, and creating shallow copies.

# Examples

From the source text (Ch. 30, section 30.4.1):

```js
const DEFAULTS = {alpha: 'a', beta: 'b'};
const providedData = {alpha: 1};
const allData = {...DEFAULTS, ...providedData};
assert.deepEqual(allData, {alpha: 1, beta: 'b'});
```

# Relationships

## Related
- **Object.assign()** -- destructive alternative to spreading

# Common Errors

- **Error**: Assuming spread creates a deep copy.
  **Correction**: Spread is shallow. Nested objects are shared. Use `structuredClone()` for deep copies.

# Source Reference

Chapter 30: Objects, Section 30.4, lines 637-804.

# Verification Notes

- Definition source: direct
- Confidence rationale: Thorough coverage with three use cases
- Cross-reference status: verified
