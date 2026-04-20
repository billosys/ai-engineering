---
# === CORE IDENTIFICATION ===
concept: Mutability
slug: mutability

# === CLASSIFICATION ===
category: data-structures
subcategory: core-concepts
tier: intermediate

# === PROVENANCE ===
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Data Structures: Objects and Arrays"
chapter_number: 4
pdf_page: null
section: "Mutability"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - mutable
  - immutable
  - object identity

# === TYPED RELATIONSHIPS ===
prerequisites:
  - object
  - value
  - binding
extends: []
related:
  - array
  - property
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I know before learning about prototypes and classes?"
---

# Quick Definition

Objects are mutable -- their properties can be changed after creation -- while primitive values (numbers, strings, Booleans) are immutable and cannot be altered.

# Core Definition

As described in "Eloquent JavaScript" (Ch 4, lines 412-424 of 04-data-structures-objects-and-arrays.md): "We saw that object values can be modified. The types of values discussed in earlier chapters, such as numbers, strings, and Booleans, are all *immutable* -- it is impossible to change values of those types." And: "Objects work differently. You *can* change their properties, causing a single object value to have different content at different times."

Further, on object identity (lines 476-481): "When you compare objects with JavaScript's `==` operator, it compares by identity: it will produce `true` only if both objects are precisely the same value. Comparing different objects will return `false`, even if they have identical properties."

# Prerequisites

- **object**: Mutability primarily concerns objects.
- **value**: Understanding the difference between values and bindings.
- **binding**: Bindings point to values; mutability is about the values, not the bindings.

# Key Properties

1. **Primitives are immutable**: numbers, strings, and Booleans cannot be changed.
2. **Objects are mutable**: their properties can be changed at any time.
3. Two bindings can reference the **same object** (shared identity).
4. `==` compares objects by **identity**, not by content.
5. A `const` binding to an object prevents rebinding but NOT property changes.

# Construction / Recognition

## To Construct/Create:
Mutability is inherent to objects. To demonstrate:
```javascript
let object1 = {value: 10};
let object2 = object1;      // same object
object1.value = 15;
console.log(object2.value);  // → 15
```

## To Identify/Recognize:
- Changing a property on one reference affects all references to the same object.

# Context & Application

Understanding mutability is critical for avoiding bugs. Shared mutable state is a common source of errors. The distinction between binding immutability (`const`) and value immutability is fundamental.

# Examples

**Example 1** (Ch 4, lines 434-449 of 04-data-structures-objects-and-arrays.md):
```javascript
let object1 = {value: 10};
let object2 = object1;
let object3 = {value: 10};

console.log(object1 == object2);
// → true
console.log(object1 == object3);
// → false

object1.value = 15;
console.log(object2.value);
// → 15
console.log(object3.value);
// → 10
```

**Example 2** (Ch 4, lines 467-473) -- const and mutability:
```javascript
const score = {visitors: 0, home: 0};
// This is okay
score.visitors = 1;
// This isn't allowed
score = {visitors: 1, home: 1};
```

# Relationships

## Builds Upon
- **object** -- Objects are the mutable type.
- **value** -- Primitives are immutable.
- **binding** -- `const` constrains the binding, not the value.

## Enables
- Understanding shared state and reference semantics.

## Related
- **array** -- Arrays are objects and thus mutable.
- **property** -- Properties of objects can be changed.

## Contrasts With
- None within this source (implicitly contrasts immutable primitives with mutable objects).

# Common Errors

- **Error**: Expecting `const` to prevent changes to object properties.
  **Correction**: `const` prevents reassignment of the binding, but the object's contents can still be modified.

# Common Confusions

- **Confusion**: Two objects with identical properties are equal.
  **Clarification**: JavaScript's `==` compares objects by identity, not by content. Two different objects with the same properties are not equal.

# Source Reference

Chapter 4: Data Structures: Objects and Arrays, Section "Mutability", lines 405-484 of 04-data-structures-objects-and-arrays.md (book.md line 3312).

# Verification Notes

- Definition source: direct (quoted from lines 412-424)
- Confidence rationale: Explicit dedicated section with italicized terms
- Cross-reference status: verified within chapter
