---
concept: Delete Operator
slug: delete-operator
category: objects
subcategory: properties
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Objects"
chapter_number: 30
pdf_page: null
section: "30.9.4 Deleting properties"
extraction_confidence: high
aliases:
  - "delete"
prerequisites:
  - object-literal
extends: []
related:
  - own-property
contrasts_with: []
answers_questions:
  - "How do I remove a property from an object?"
---

# Quick Definition

The `delete` operator removes an own property from an object, returning `true` on success (including when the property doesn't exist).

# Core Definition

As described in "Exploring JavaScript" Ch. 30, `delete obj.prop` removes the property `prop` from `obj`. It only removes own properties. Returns `true` if the property was successfully removed or didn't exist. Returns `false` only for non-configurable properties.

# Prerequisites

- Object literal

# Key Properties

1. Removes own properties.
2. Returns `true` on success (or if property didn't exist).
3. Returns `false` for non-configurable properties.
4. Does not affect prototype chain.

# Construction / Recognition

```js
const obj = {a: 1, b: 2};
delete obj.a;
assert.deepEqual(Object.keys(obj), ['b']);
```

# Context & Application

Used to remove properties from objects, especially in dictionary-style usage. For fixed-layout objects, setting to `undefined` is sometimes preferred.

# Examples

```js
const obj = {a: 1, b: 2};
delete obj.a;
assert.deepEqual(obj, {b: 2});
```

# Relationships

## Related
- **Own Property** -- `delete` only affects own properties

# Source Reference

Chapter 30: Objects, Section 30.9.4.

# Verification Notes

- Definition source: direct
- Confidence rationale: Standard operator definition
- Cross-reference status: verified
