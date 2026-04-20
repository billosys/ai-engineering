---
concept: Object.keys/values/entries
slug: object-keys-values-entries
category: objects
subcategory: property-enumeration
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Objects"
chapter_number: 30
pdf_page: null
section: "30.9.6-30.9.8 Listing property keys, values, entries"
extraction_confidence: high
aliases:
  - "Object.keys()"
  - "Object.values()"
  - "Object.entries()"
prerequisites:
  - own-property
extends: []
related:
  - object-from-entries
contrasts_with: []
answers_questions:
  - "How do I list the properties of an object?"
---

# Quick Definition

`Object.keys()`, `Object.values()`, and `Object.entries()` return arrays of an object's own enumerable string-keyed property keys, values, or key-value pairs, respectively.

# Core Definition

As described in "Exploring JavaScript" Ch. 30, these three methods return own enumerable string-keyed properties. `Object.keys()` returns keys as strings, `Object.values()` (ES2017) returns values, and `Object.entries()` (ES2017) returns `[key, value]` pairs. They ignore symbol-keyed and non-enumerable properties. Properties are listed deterministically.

# Prerequisites

- Own property

# Key Properties

1. Only own, enumerable, string-keyed properties.
2. `Object.keys()` -- returns string array of keys.
3. `Object.values()` (ES2017) -- returns array of values.
4. `Object.entries()` (ES2017) -- returns array of `[key, value]` pairs.
5. Symbol-keyed properties are ignored.
6. Property order is deterministic.

# Construction / Recognition

```js
const obj = {a: 1, b: 2, c: 3};
Object.keys(obj);    // ['a', 'b', 'c']
Object.values(obj);  // [1, 2, 3]
Object.entries(obj);  // [['a', 1], ['b', 2], ['c', 3]]
```

# Context & Application

Used for iterating over object properties, converting objects to other data structures, and extracting property information.

# Examples

From the source text (Ch. 30, section 30.9.6-30.9.8) -- conceptual usage:

```js
const obj = {a: 1, b: 2};
for (const [key, value] of Object.entries(obj)) {
  console.log(`${key}: ${value}`);
}
```

# Relationships

## Builds Upon
- **Own Property** -- only lists own properties

## Related
- **Object.fromEntries()** -- reverse operation, creates object from entries

# Source Reference

Chapter 30: Objects, Section 30.9.6-30.9.8.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit definitions in source
- Cross-reference status: verified
