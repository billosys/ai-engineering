---
# === CORE IDENTIFICATION ===
concept: null vs undefined
slug: null-vs-undefined

# === CLASSIFICATION ===
category: type-system
subcategory: primitive-types
tier: intermediate

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Types, Values, and Variables"
chapter_number: 3
pdf_page: 57
section: "3.5 null and undefined"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - primitive-vs-object-types
  - boolean-truthy-falsy
extends: []
related:
  - type-coercion
  - strict-vs-loose-equality
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes `null` from `undefined`?"
  - "What distinguishes `==` from `===`?"
---

# Quick Definition

`null` indicates a program-level, intentional absence of value (a language keyword), while `undefined` indicates a system-level, unexpected absence — the value of uninitialized variables, missing properties, and missing function arguments.

# Core Definition

"`null` is a language keyword that evaluates to a special value that is usually used to indicate the absence of a value." "`typeof` operator on null returns the string 'object.'" The `undefined` value "represents a deeper kind of absence. It is the value of variables that have not been initialized and the value you get when you query the value of an object property or array element that does not exist. The undefined value is also the return value of functions that do not explicitly return a value and the value of function parameters for which no argument is passed." `undefined` "is a predefined global constant (not a language keyword like null)." (pp. 57-58)

# Prerequisites

- **primitive-vs-object-types** — Both are primitive values
- **boolean-truthy-falsy** — Both are falsy

# Key Properties

1. `null` is a language keyword; `undefined` is a predefined global constant
2. `typeof null` returns `"object"` (historical quirk)
3. `typeof undefined` returns `"undefined"`
4. Both are falsy
5. `null == undefined` is `true` (loose equality)
6. `null === undefined` is `false` (strict equality — different types)
7. Neither has properties or methods — accessing `.` or `[]` causes TypeError
8. `undefined` is the value of uninitialized variables, missing properties, missing function arguments, and functions without explicit return
9. Author's convention: `undefined` = system-level/unexpected absence; `null` = program-level/expected absence

# Construction / Recognition

```javascript
let x;              // x is undefined (uninitialized)
let obj = {};
obj.missing         // => undefined (nonexistent property)
function f() {}
f()                 // => undefined (no return value)

let y = null;       // Explicitly assigned null
```

# Context & Application

The distinction between null and undefined is one of JavaScript's most commonly tested interview questions and a frequent source of confusion. The `==` operator treats them as equal, but `===` distinguishes them. Using `.` or `[]` on either causes TypeError, making null/undefined checks important for safe property access.

# Examples

From the source text (pp. 57-58):
```javascript
// The equality operator considers them equal
null == undefined       // => true

// The strict equality operator distinguishes them
null === undefined      // => false

// Both are falsy
if (!null) ...          // this executes
if (!undefined) ...     // this executes

// typeof differences
typeof null             // => "object"
typeof undefined        // => "undefined"
```

Author's convention (p. 58): "I consider undefined to represent a system-level, unexpected, or error-like absence of value and null to represent a program-level, normal, or expected absence of value."

# Relationships

## Builds Upon
- **primitive-vs-object-types** — Both are primitive values
- **boolean-truthy-falsy** — Both are falsy

## Enables
- Safe property access patterns
- **strict-vs-loose-equality** — Key example of `==` vs `===` difference

## Related
- **type-coercion** — `null` converts to `0` as a number; `undefined` converts to `NaN`
- **strict-vs-loose-equality** — `null == undefined` is `true` but `null === undefined` is `false`

## Contrasts With
- Each other — this is the core contrast

# Common Errors

- **Error**: Accessing a property on null or undefined: `null.property`.
  **Correction**: Always check for null/undefined before accessing properties, or use optional chaining (`?.`).

# Common Confusions

- **Confusion**: `null` and `undefined` are interchangeable.
  **Clarification**: While `==` considers them equal, they have different semantics: undefined means "not yet assigned" (system-level); null means "intentionally empty" (program-level).

- **Confusion**: `typeof null` returns `"null"`.
  **Clarification**: `typeof null` returns `"object"` — a well-known historical bug that cannot be fixed.

# Source Reference

Chapter 3: Types, Values, and Variables, Section 3.5, pages 57-58.

# Verification Notes

- Definition source: Direct quotes from pp. 57-58
- Confidence rationale: High — clearly and thoroughly explained
- Uncertainties: None
- Cross-reference status: Verified
