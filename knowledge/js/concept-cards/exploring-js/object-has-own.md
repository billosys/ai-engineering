---
concept: Object.hasOwn()
slug: object-has-own
category: objects
subcategory: property-access
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Objects"
chapter_number: 30
pdf_page: null
section: "30.8.4 `Object.hasOwn()`"
extraction_confidence: high
aliases:
  - "Object.hasOwn"
  - "hasOwn"
prerequisites:
  - own-property
  - in-operator
extends: []
related:
  - in-operator
contrasts_with:
  - in-operator
answers_questions:
  - "How do I check if a property is own (not inherited)?"
---

# Quick Definition

`Object.hasOwn(obj, key)` (ES2022) checks whether `obj` has an own (non-inherited) property with the given key, replacing the older `obj.hasOwnProperty(key)`.

# Core Definition

As described in "Exploring JavaScript" Ch. 30, `Object.hasOwn()` was introduced in ES2022 to check if a property is own. Unlike the older `hasOwnProperty()`, it works with objects that don't inherit from `Object.prototype` (e.g., `Object.create(null)`).

# Prerequisites

- Own property
- `in` operator (to understand the alternative)

# Key Properties

1. Introduced in ES2022.
2. Returns boolean.
3. Only checks own properties (not inherited).
4. Works with all objects (including those with `null` prototype).
5. Replaces `Object.prototype.hasOwnProperty()`.

# Construction / Recognition

```js
Object.hasOwn(obj, 'propName'); // true if own
```

# Context & Application

Use when you need to distinguish own from inherited properties, especially with dictionary-style objects.

# Examples

From the source text (Ch. 30, section 30.8.4):

```js
const proto = { protoProp: 'protoProp' };
const obj = { __proto__: proto, objProp: 'objProp' };
assert.equal('protoProp' in obj, true);
assert.equal(Object.hasOwn(obj, 'protoProp'), false);
assert.equal(Object.hasOwn(proto, 'protoProp'), true);
```

# Relationships

## Contrasts With
- **in Operator** -- `in` checks all properties; `Object.hasOwn()` checks only own

# Source Reference

Chapter 30: Objects, Section 30.8.4, lines 2071-2099.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit definition with comparison
- Cross-reference status: verified
