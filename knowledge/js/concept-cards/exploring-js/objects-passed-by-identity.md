---
# === CORE IDENTIFICATION ===
concept: Objects Passed by Identity
slug: objects-passed-by-identity

# === CLASSIFICATION ===
category: types-values
subcategory: objects
tier: foundational

# === PROVENANCE ===
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Values"
chapter_number: 14
pdf_page: null
section: "14.6.2 Objects are passed by identity"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - pass by identity
  - pass by sharing
  - pass by reference (informal)

# === TYPED RELATIONSHIPS ===
prerequisites:
  - objects-overview
extends:
  - objects-overview
related:
  - garbage-collection
contrasts_with:
  - primitives-passed-by-value

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes primitive values from objects?"
---

# Quick Definition

Objects are passed by identity: when assigned to variables or passed to functions, only the object's identity (a transparent reference/pointer) is copied, not the object itself. Multiple variables can share the same object.

# Core Definition

"Objects are *passed by identity*: Variables (including parameters) store the *identities* of objects. The identity of an object is a *transparent reference* (think pointer) to the object's actual data on the *heap*. When assigning an object to a variable or passing it as an argument to a function, its identity is copied." (Ch. 14, &sect;14.6.2). Each object literal creates a fresh object on the heap and returns its identity.

# Prerequisites

- **objects-overview** -- this describes how objects are handled

# Key Properties

1. Variables store object identities (transparent references/pointers)
2. Assignment copies the identity, not the object
3. Multiple variables can share the same object
4. Changing the object through one variable affects all variables sharing it
5. JavaScript uses garbage collection to manage object memory
6. Term "passing by identity" coined by Allen Wirfs-Brock (2019)

# Construction / Recognition

```js
const a = {};     // fresh empty object
const b = a;      // copy identity, not object
assert.equal(a === b, true);  // same object

a.name = 'Tessa';
assert.equal(b.name, 'Tessa'); // change visible through both
```

# Context & Application

Understanding pass-by-identity is crucial for avoiding bugs where shared objects are unintentionally modified.

# Examples

From the source text (Ch. 14, &sect;14.6.2):
```js
const a = {};
const b = a;
assert.equal(a === b, true);

a.name = 'Tessa';
assert.equal(b.name, 'Tessa');
```

Garbage collection:
```js
let obj = { prop: 'value' };
obj = {};
// Old { prop: 'value' } is now garbage
```

# Relationships

## Builds Upon
- **objects-overview** -- identity passing is a key object behavior

## Enables
- Shared mutable state patterns
- **garbage-collection** -- objects are garbage-collected when no identity references remain

## Related
- No additional

## Contrasts With
- **primitives-passed-by-value** -- primitives copy content, not identity

# Common Errors

- **Error**: Assuming `const b = a` creates a copy of the object.
  **Correction**: It copies the identity; both `a` and `b` point to the same object.

# Common Confusions

- **Confusion**: Calling this "pass by reference."
  **Clarification**: JavaScript uses "pass by identity" (or "pass by sharing"), not pass by reference. In true pass-by-reference (like C++ `&`), assigning to a parameter changes the caller's variable. In JavaScript, assigning to a parameter only has local effect.

# Source Reference

Chapter 14: Values, Section 14.6.2, lines 269-312.

# Verification Notes

- Definition source: direct from source
- Confidence rationale: Detailed with explicit distinction from pass-by-reference
- Cross-reference status: verified against &sect;14.6.4
