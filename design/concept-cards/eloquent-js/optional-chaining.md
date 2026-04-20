---
# === CORE IDENTIFICATION ===
concept: Optional Chaining
slug: optional-chaining

# === CLASSIFICATION ===
category: data-structures
subcategory: syntax
tier: intermediate

# === PROVENANCE ===
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Data Structures: Objects and Arrays"
chapter_number: 4
pdf_page: null
section: "Optional property access"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - optional property access
  - safe navigation operator

# === TYPED RELATIONSHIPS ===
prerequisites:
  - property-access
  - object
extends:
  - property-access
related:
  - property
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions: []
---

# Quick Definition

Optional chaining (`?.`) allows safe property access on values that might be `null` or `undefined`, returning `undefined` instead of throwing an error.

# Core Definition

As described in "Eloquent JavaScript" (Ch 4, lines 1252-1254 of 04-data-structures-objects-and-arrays.md): "When you aren't sure whether a given value produces an object, but still want to read a property from it when it does, you can use a variant of the dot notation: `object?.property`." And (lines 1267-1271): "The expression `a?.b` means the same as `a.b` when `a` isn't null or undefined. When it is, it evaluates to `undefined`."

# Prerequisites

- **property-access**: Optional chaining extends property access syntax.
- **object**: Used when values might not be objects.

# Key Properties

1. `a?.b` returns `a.b` if `a` is not null/undefined; otherwise `undefined`.
2. Works with dot notation: `object?.property`.
3. Works with bracket notation: `object?.[index]`.
4. Works with function calls: `func?.()`.

# Construction / Recognition

## To Construct/Create:
```javascript
function city(object) {
  return object.address?.city;
}
```

## To Identify/Recognize:
- `?.` between an expression and a property name, bracket, or parentheses.

# Context & Application

Optional chaining is essential for safely navigating nested object structures where intermediate values might be null or undefined, such as when processing API responses.

# Examples

**Example 1** (Ch 4, lines 1256-1264 of 04-data-structures-objects-and-arrays.md):
```javascript
function city(object) {
  return object.address?.city;
}
console.log(city({address: {city: "Toronto"}}));
// → Toronto
console.log(city({name: "Vera"}));
// → undefined
```

**Example 2** (Ch 4, lines 1278-1283):
```javascript
console.log("string".notAMethod?.());
// → undefined
console.log({}.arrayProp?.[0]);
// → undefined
```

# Relationships

## Builds Upon
- **property-access** -- Optional chaining is a variant of property access.

## Enables
- Safe navigation of nested data structures.

## Related
- **property** -- Accessed safely via optional chaining.

## Contrasts With
- None within this source.

# Common Errors

- **Error**: Using `?.` when you know the value exists (unnecessary overhead and confusion).
  **Correction**: Use regular `.` when the value is guaranteed to exist. Reserve `?.` for genuinely uncertain cases.

# Common Confusions

- **Confusion**: `?.` prevents all errors in a chain.
  **Clarification**: `?.` only handles null/undefined on its left side. If the left side is a non-null non-object value, you may still get an error.

# Source Reference

Chapter 4: Data Structures: Objects and Arrays, Section "Optional property access", lines 1249-1283 of 04-data-structures-objects-and-arrays.md (book.md line 3312).

# Verification Notes

- Definition source: direct (quoted from lines 1252-1254 and 1267-1271)
- Confidence rationale: Explicit dedicated section
- Cross-reference status: verified within chapter
