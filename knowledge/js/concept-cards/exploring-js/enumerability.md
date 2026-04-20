---
concept: Enumerability
slug: enumerability
category: objects
subcategory: property-attributes
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Objects"
chapter_number: 30
pdf_page: null
section: "30.9.5 Enumerability"
extraction_confidence: high
aliases:
  - "enumerable property"
prerequisites:
  - own-property
extends: []
related:
  - object-keys-values-entries
  - for-in-loop
contrasts_with: []
answers_questions:
  - "Why do some properties not appear in Object.keys()?"
---

# Quick Definition

Enumerability is a property attribute that controls whether a property appears in certain listing operations like `Object.keys()`, `for-in`, and spreading.

# Core Definition

As described in "Exploring JavaScript" Ch. 30, each property has an `enumerable` attribute. When `true`, the property is visible to `Object.keys()`, `Object.entries()`, spreading, and `for-in`. Most properties created via normal assignment or object literals are enumerable. Built-in properties like `.length` on arrays are non-enumerable. Property attributes are covered in more detail in section 30.10.

# Prerequisites

- Own property

# Key Properties

1. Boolean property attribute (`enumerable`).
2. Affects `Object.keys()`, `Object.entries()`, spreading, `for-in`.
3. Properties created normally are enumerable.
4. Built-in properties (e.g., `.length`) are typically non-enumerable.
5. Part of the property descriptor system (ES5).

# Construction / Recognition

```js
const obj = {a: 1};
// 'a' is enumerable
Object.keys(obj); // ['a']

// .length of strings is non-enumerable
assert.deepEqual({...'abc'}, {'0':'a','1':'b','2':'c'});
// .length is not spread
```

# Context & Application

Enumerability explains why some properties are "hidden" from enumeration. Mostly a concern when working with property descriptors or understanding built-in object behavior.

# Examples

From the source text (Ch. 30, section 30.4):

```js
// Spreading only copies enumerable properties
// .length of strings is not enumerable, so it's not spread
assert.deepEqual({...'abc'}, {'0':'a','1':'b','2':'c'});
```

# Relationships

## Related
- **Object.keys/values/entries** -- only list enumerable properties
- **For-In Loop** -- iterates enumerable properties (own and inherited)

# Source Reference

Chapter 30: Objects, Section 30.9.5.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit attribute description
- Cross-reference status: verified
