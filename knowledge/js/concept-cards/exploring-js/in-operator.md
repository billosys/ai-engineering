---
concept: in Operator
slug: in-operator
category: objects
subcategory: property-access
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Objects"
chapter_number: 30
pdf_page: null
section: "30.9.3 The `in` operator"
extraction_confidence: high
aliases:
  - "in"
prerequisites:
  - object-literal
  - prototype-chain
extends: []
related:
  - own-property
contrasts_with: []
answers_questions:
  - "How do I check if an object has a specific property?"
---

# Quick Definition

The `in` operator checks whether an object has a property with a given key, considering both own and inherited properties.

# Core Definition

As described in "Exploring JavaScript" Ch. 30, `key in obj` returns `true` if `obj` has a property with key `key` (own or inherited). Since ES2022, `in` can also check for private slots: `#field in obj` (only inside the declaring class). Use `Object.hasOwn(obj, key)` to check only own properties.

# Prerequisites

- Object literal
- Prototype chain

# Key Properties

1. Checks both own and inherited properties.
2. Returns boolean.
3. Since ES2022: `#field in obj` checks private slots.
4. For own-only checks, use `Object.hasOwn()`.

# Construction / Recognition

```js
'toString' in {}         // true (inherited)
'nonExistent' in {}      // false
```

# Context & Application

Used for property existence checks, feature detection, and (since ES2022) private slot checking.

# Examples

```js
const proto = { protoProp: 'a' };
const obj = { __proto__: proto, objProp: 'b' };
assert.equal('protoProp' in obj, true);  // inherited
assert.equal('objProp' in obj, true);    // own
assert.equal(Object.hasOwn(obj, 'protoProp'), false); // not own
```

# Relationships

## Related
- **Own Property** -- `in` checks all properties; `Object.hasOwn()` checks only own

# Source Reference

Chapter 30: Objects, Section 30.9.3.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit usage shown
- Cross-reference status: verified
