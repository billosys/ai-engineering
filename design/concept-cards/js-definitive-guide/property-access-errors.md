---
# === CORE IDENTIFICATION ===
concept: Property Access Errors
slug: property-access-errors

# === CLASSIFICATION ===
category: objects
subcategory: property-access
tier: foundational

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Objects"
chapter_number: 6
pdf_page: 154
section: "6.3.3 Property Access Errors"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - property-access-expressions
  - prototype-chain
extends: []
related:
  - optional-chaining
  - property-attributes
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do property descriptors relate to Object.freeze()?"
---

# Quick Definition

Querying a nonexistent property returns `undefined` (not an error), but accessing a property on `null` or `undefined` throws a TypeError. Setting properties can fail silently in non-strict mode or throw TypeError in strict mode.

# Core Definition

"It is not an error to query a property that does not exist" — the result is `undefined`. "It is an error, however, to attempt to query a property of an object that does not exist. The null and undefined values have no properties, and it is an error to query properties of these values." Property assignment can fail when: the property is read-only, an inherited read-only property exists, or the object is not extensible. (Ch. 6, §6.3.3)

# Prerequisites

- **property-access-expressions** — Understanding property access mechanics.
- **prototype-chain** — Read-only inherited properties block assignment.

# Key Properties

1. Querying a missing property returns `undefined`.
2. Querying a property on `null` or `undefined` throws TypeError.
3. Use `?.` (optional chaining) or `&&` guards to avoid TypeError on nested access.
4. Setting a read-only own property fails (TypeError in strict mode).
5. Setting an inherited read-only property fails (cannot hide with own property).
6. Adding properties to a non-extensible object fails.
7. In non-strict mode, these failures are silent.

# Construction / Recognition

```js
book.subtitle          // => undefined (property doesn't exist)
book.subtitle.length   // TypeError! (can't access property of undefined)
book?.subtitle?.length // => undefined (safe with optional chaining)
```

# Context & Application

Understanding when property access fails and how to guard against it is essential for writing robust code, especially when working with deeply nested objects or data from external sources.

# Examples

From the source text (§6.3.3, pp. 154-155):

```js
book.subtitle               // => undefined
let len = book.subtitle.length;  // !TypeError

// Guard patterns:
let surname = undefined;
if (book) {
    if (book.author) {
        surname = book.author.surname;
    }
}
// Idiomatic alternative:
surname = book && book.author && book.author.surname;
// ES2020 optional chaining:
let surname = book?.author?.surname;
```

# Relationships

## Builds Upon
- **property-access-expressions** — Error conditions for property access
- **prototype-chain** — Read-only inherited properties affect assignment

## Enables
- Understanding defensive coding patterns

## Related
- **optional-chaining** — `?.` guards against TypeError
- **property-attributes** — Read-only and non-extensible affect assignment

## Contrasts With
- No direct contrast

# Common Errors

- **Error**: Chaining property access without null checks.
  **Correction**: Use optional chaining (`?.`) or explicit checks for intermediate values.

# Common Confusions

- **Confusion**: Expecting a missing property to throw an error.
  **Clarification**: Querying a nonexistent property simply returns `undefined`. Only accessing a property *on* `null`/`undefined` throws.

# Source Reference

Chapter 6: Objects, Section 6.3.3, pages 154-155.

# Verification Notes

- Definition source: Direct quote from §6.3.3
- Confidence rationale: High — detailed error conditions and guard patterns
- Uncertainties: None
- Cross-reference status: Verified against §4.4.1
