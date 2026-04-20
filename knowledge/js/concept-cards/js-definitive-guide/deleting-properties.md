---
# === CORE IDENTIFICATION ===
concept: Deleting Properties
slug: deleting-properties

# === CLASSIFICATION ===
category: objects
subcategory: property-operations
tier: intermediate

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Objects"
chapter_number: 6
pdf_page: 155
section: "6.4 Deleting Properties"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - delete-operator
  - own-vs-inherited-properties
  - property-attributes
extends:
  - delete-operator
related: []
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do property descriptors relate to Object.freeze()?"
---

# Quick Definition

The `delete` operator removes own properties from objects. It only deletes own properties (not inherited), cannot delete non-configurable properties, and returns `true` on success or no-op.

# Core Definition

"The delete operator removes a property from an object. Its single operand should be a property access expression... The delete operator only deletes own properties, not inherited ones." It returns `true` if the delete succeeded, had no effect, or was applied to a non-property expression. It cannot remove non-configurable properties. (Ch. 6, §6.4)

# Prerequisites

- **delete-operator** — The `delete` operator mechanics from Ch. 4.
- **own-vs-inherited-properties** — `delete` only operates on own properties.
- **property-attributes** — The `configurable` attribute determines deletability.

# Key Properties

1. Only deletes own properties — to delete an inherited property, must delete from the prototype.
2. Deleting from the prototype affects all inheriting objects.
3. `delete` returns `true` on success, on no-op (nonexistent property), and on non-lvalue.
4. Non-configurable properties cannot be deleted; in strict mode, TypeError is thrown.
5. Global variables and functions declared with `var`/`function` are non-configurable.
6. In strict mode, `delete` on an unqualified identifier is a SyntaxError.

# Construction / Recognition

```js
delete book.author;
delete book["main title"];
```

# Context & Application

Property deletion is used for cleanup, removing keys from dictionary objects, and managing dynamic property sets. It is important to understand what `delete` cannot remove (non-configurable properties, var declarations).

# Examples

From the source text (§6.4, pp. 155-156):

```js
let o = {x: 1};
delete o.x           // => true: deletes property x
delete o.x           // => true: does nothing (x doesn't exist) but true anyway
delete o.toString    // => true: does nothing (toString isn't own property)

// Non-configurable properties
delete Object.prototype  // => false: non-configurable
var x = 1;
delete globalThis.x     // => false: can't delete var declarations

// In strict mode:
// delete Object.prototype  // TypeError
// delete x                  // SyntaxError
```

# Relationships

## Builds Upon
- **delete-operator** — Ch. 4 operator mechanics
- **own-vs-inherited-properties** — Only own properties can be deleted
- **property-attributes** — `configurable` controls deletability

## Enables
- Dynamic property management on objects

## Related
- No additional related concepts

## Contrasts With
- No direct contrast

# Common Errors

- **Error**: Attempting to delete an inherited property by deleting from the child object.
  **Correction**: "To delete an inherited property, you must delete it from the prototype object in which it is defined."

# Common Confusions

- **Confusion**: Expecting `delete` to return `false` when deleting a nonexistent property.
  **Clarification**: `delete` returns `true` for nonexistent properties (it "succeeds" because the property already doesn't exist).

# Source Reference

Chapter 6: Objects, Section 6.4, pages 155-156.

# Verification Notes

- Definition source: Direct quote from §6.4
- Confidence rationale: High — comprehensive with edge cases
- Uncertainties: None
- Cross-reference status: Verified against §4.13.4
