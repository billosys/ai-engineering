---
# === CORE IDENTIFICATION ===
concept: for/in Loop
slug: for-in-loop

# === CLASSIFICATION ===
category: language-fundamentals
subcategory: statements
tier: foundational

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Statements"
chapter_number: 5
pdf_page: 128
section: "5.4.5 for/in"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "for-in loop"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - for-loop
  - property-access-expressions
extends: []
related:
  - for-of-loop
  - enumerating-properties
  - in-operator
contrasts_with:
  - for-of-loop

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes Object.keys() from for/in?"
---

# Quick Definition

The `for/in` loop iterates over the enumerable property names (strings) of an object, including inherited enumerable properties, assigning each name to the loop variable.

# Core Definition

"The for/in statement loops through the property names of a specified object... A for/in loop works with any object after the in." It enumerates only *enumerable* properties and only those with string names (not Symbols). "Enumerable inherited properties are also enumerated by the for/in loop." (Ch. 5, §5.4.5)

# Prerequisites

- **for-loop** — `for/in` uses the `for` keyword with `in` semantics.
- **property-access-expressions** — Property names are used to access values.

# Key Properties

1. Enumerates enumerable string-named properties, both own and inherited.
2. Built-in methods (like `toString`) are not enumerable and are skipped.
3. If the body deletes a not-yet-enumerated property, it will not be enumerated.
4. New properties added during iteration may or may not be enumerated.
5. A property already enumerated (or a non-enumerable property with the same name) is not enumerated again.
6. If the object is `null` or `undefined`, the loop is skipped (no error).
7. Use `hasOwnProperty()` inside the loop to filter out inherited properties.

# Construction / Recognition

```js
for (variable in object)
    statement
```

# Context & Application

`for/in` has been part of JavaScript since the beginning. Modern best practice often prefers `for/of` with `Object.keys()` because `for/in` includes inherited properties. However, `for/in` remains useful for quick enumeration when inherited properties are acceptable.

# Examples

From the source text (§5.4.5, pp. 128-130):

```js
for(let p in o) {
    console.log(o[p]);    // Print the value of each property
}

// Filtering inherited properties
for(let p in o) {
    if (!o.hasOwnProperty(p)) continue;  // Skip inherited
}

// Copy property names into an array
let o = { x: 1, y: 2, z: 3 };
let a = [], i = 0;
for(a[i++] in o) /* empty */;
```

# Relationships

## Builds Upon
- **property-access-expressions** — Loop variable is used with bracket notation to access values

## Enables
- Property enumeration patterns (with filtering)

## Related
- **for-of-loop** — Modern alternative for iterating values
- **enumerating-properties** — Ch. 6 covers Object.keys() and related methods
- **in-operator** — Same keyword, different usage (property existence test)

## Contrasts With
- **for-of-loop** — `for/of` iterates values of iterables; `for/in` iterates property names including inherited ones

# Common Errors

- **Error**: Using `for/in` with arrays when `for/of` was intended.
  **Correction**: "A common source of bugs is the accidental use of for/in with arrays when I meant to use for/of." `for/in` on arrays gives string indices and includes inherited properties.

# Common Confusions

- **Confusion**: Believing `for/in` only enumerates own properties.
  **Clarification**: `for/in` includes inherited enumerable properties. Use `Object.keys()` with `for/of` to get only own enumerable properties.

# Source Reference

Chapter 5: Statements, Section 5.4.5, pages 128-130.

# Verification Notes

- Definition source: Direct quote from §5.4.5
- Confidence rationale: High — detailed with caveats about inherited properties
- Uncertainties: None
- Cross-reference status: Verified against §6.6
