---
# === CORE IDENTIFICATION ===
concept: The delete Operator
slug: delete-operator

# === CLASSIFICATION ===
category: language-fundamentals
subcategory: operators
tier: intermediate

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Expressions and Operators"
chapter_number: 4
pdf_page: 111
section: "4.13.4 The delete Operator"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - property-access-expressions
extends: []
related:
  - deleting-properties
  - property-attributes
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do property descriptors relate to Object.freeze()?"
---

# Quick Definition

The `delete` operator removes a property from an object. It returns `true` on success or when the operation has no effect, and cannot remove non-configurable properties.

# Core Definition

"delete is a unary operator that attempts to delete the object property or array element specified as its operand... Note that a deleted property or array element is not merely set to the undefined value. When a property is deleted, the property ceases to exist." (Ch. 4, §4.13.4)

# Prerequisites

- **property-access-expressions** — `delete` operates on property access expressions.

# Key Properties

1. Deleting a property makes it cease to exist, not just become `undefined`.
2. Deleting an array element creates a "hole" (sparse array) — length is unchanged.
3. Returns `true` on success, on no-op (nonexistent property), and on non-lvalue operands.
4. Cannot delete non-configurable properties. In strict mode, this throws TypeError; in non-strict, returns `false`.
5. In strict mode, `delete` on an unqualified identifier throws SyntaxError.
6. Only deletes own properties, not inherited ones.

# Construction / Recognition

```js
delete object.property
delete object["property"]
delete array[index]
```

# Context & Application

`delete` is used to remove properties from objects, typically for cleanup or to remove a key from an object used as a map. It is almost always used as a statement rather than for its return value.

# Examples

From the source text (§4.13.4, pp. 111-112):

```js
let o = { x: 1, y: 2};
delete o.x;             // Delete one of its properties
"x" in o                // => false: the property does not exist anymore

let a = [1,2,3];
delete a[2];            // Delete the last element of the array
2 in a                  // => false: array element 2 doesn't exist anymore
a.length                // => 3: note that array length doesn't change

delete Object.prototype // => false: property is non-configurable
var x = 1;
delete globalThis.x     // => false: can't delete var declarations
```

# Relationships

## Builds Upon
- **property-access-expressions** — `delete` operates on property access expressions

## Enables
- **deleting-properties** — Ch. 6 covers `delete` in the context of object property management

## Related
- **property-attributes** — The `configurable` attribute determines whether `delete` works

## Contrasts With
- No direct contrast

# Common Errors

- **Error**: Using `delete` on an array and expecting the length to change.
  **Correction**: `delete` creates a hole; use `Array.splice()` to actually remove elements and shift indices.

# Common Confusions

- **Confusion**: Believing `delete` sets a property to `undefined`.
  **Clarification**: `delete` removes the property entirely. The property ceases to exist, which is different from having a value of `undefined`.

# Source Reference

Chapter 4: Expressions and Operators, Section 4.13.4, pages 111-112.

# Verification Notes

- Definition source: Direct quote from §4.13.4
- Confidence rationale: High — detailed explanation with edge cases
- Uncertainties: None
- Cross-reference status: Verified against §6.4
