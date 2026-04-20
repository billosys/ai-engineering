---
concept: structuredClone()
slug: structured-clone
category: objects
subcategory: copying
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Objects"
chapter_number: 30
pdf_page: null
section: "30.5.2 Copying objects deeply via `structuredClone()`"
extraction_confidence: high
aliases:
  - "deep copy"
  - "deep clone"
prerequisites:
  - spreading-into-object-literals
extends: []
related:
  - object-assign
contrasts_with:
  - spreading-into-object-literals
answers_questions:
  - "How do I create a deep copy of an object?"
---

# Quick Definition

`structuredClone()` creates a deep copy of a value, recursively cloning nested objects, unlike the shallow copy produced by spreading or `Object.assign()`.

# Core Definition

As described in "Exploring JavaScript" Ch. 30, `structuredClone(value)` copies objects deeply. It can copy all primitive values (except symbols), most built-in objects (except functions and DOM nodes), and handles cyclical references correctly. Instances of user-defined classes become plain objects. Private fields are not copied. Property attributes are reset to defaults in copies.

# Prerequisites

- Spreading into object literals (to understand shallow vs. deep)

# Key Properties

1. Deep copy: nested objects are independent copies.
2. Cannot copy: symbols, functions, DOM nodes.
3. User-defined class instances become plain objects.
4. Private fields not copied.
5. Cyclical references handled correctly.
6. Property attributes reset to defaults.
7. Not part of ECMAScript spec but well-supported on all platforms.

# Construction / Recognition

```js
const original = {a: 1, b: {c: 2}};
const deep = structuredClone(original);
deep.b.c = 99;
assert.equal(original.b.c, 2); // unaffected
```

# Context & Application

Use when you need a truly independent copy of nested data structures. For simple flat objects, spreading is sufficient.

# Examples

From the source text (Ch. 30, section 30.5.2):

```js
const obj = {id: 'e1fd960b', values: ['a', 'b']};
const deepCopy = structuredClone(obj);
deepCopy.values.push('x');
assert.deepEqual(obj, {id: 'e1fd960b', values: ['a', 'b']}); // unaffected
```

# Relationships

## Contrasts With
- **Spreading Into Object Literals** -- spreading is shallow; `structuredClone()` is deep

# Common Errors

- **Error**: Trying to clone objects with functions or methods.
  **Correction**: `structuredClone()` throws `DOMException` for functions. Remove or replace functions before cloning.

# Source Reference

Chapter 30: Objects, Section 30.5.2-30.5.3, lines 855-1065.

# Verification Notes

- Definition source: direct
- Confidence rationale: Detailed limitations documented
- Cross-reference status: verified
