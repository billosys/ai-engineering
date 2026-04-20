---
# === CORE IDENTIFICATION ===
concept: Object-to-Primitive Conversion
slug: object-to-primitive-conversion

# === CLASSIFICATION ===
category: type-system
subcategory: type-coercion
tier: advanced

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Types, Values, and Variables"
chapter_number: 3
pdf_page: 66
section: "3.9.3 Object to Primitive Conversions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - object coercion
  - prefer-string algorithm
  - prefer-number algorithm

# === TYPED RELATIONSHIPS ===
prerequisites:
  - type-coercion
  - primitive-vs-object-types
  - methods-overview
extends:
  - type-coercion
related:
  - strict-vs-loose-equality
  - boolean-truthy-falsy
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is type coercion in JavaScript?"
---

# Quick Definition

When JavaScript needs to convert an object to a primitive value, it uses one of three algorithms — prefer-string, prefer-number, or no-preference — which call the object's `toString()` and `valueOf()` methods in different orders.

# Core Definition

JavaScript defines "three fundamental algorithms for converting objects to primitive values": *prefer-string* (tries `toString()` first, then `valueOf()`), *prefer-number* (tries `valueOf()` first, then `toString()`), and *no-preference* (uses prefer-string for Date objects, prefer-number for all others). Object-to-boolean is always `true`. The `+` operator and `==`/`!=` use no-preference; relational operators use prefer-number; string concatenation contexts use prefer-string. (pp. 66-70)

# Prerequisites

- **type-coercion** — This is the object-specific part of type coercion
- **primitive-vs-object-types** — Must understand the distinction
- **methods-overview** — Conversion uses toString() and valueOf() methods

# Key Properties

1. **Object-to-boolean**: always `true` (even `new Boolean(false)`)
2. **prefer-string**: `toString()` first, then `valueOf()`
3. **prefer-number**: `valueOf()` first, then `toString()`
4. **no-preference**: Date uses prefer-string; all others use prefer-number
5. `toString()` default: `"[object Object]"` for plain objects
6. Array `toString()`: joins elements with commas
7. Function `toString()`: returns source code string
8. Date `toString()`: human-readable date string
9. `valueOf()` default: returns the object itself (not primitive!)
10. Date `valueOf()`: returns millisecond timestamp
11. The `+` operator uses no-preference algorithm
12. `==` and `!=` use no-preference algorithm
13. `<`, `>`, `<=`, `>=` use prefer-number algorithm

# Construction / Recognition

```javascript
// Why empty arrays convert to 0:
Number([])         // => 0
// [].valueOf() returns [] (not primitive)
// [].toString() returns ""
// Number("") returns 0

Number([99])       // => 99
// [99].toString() returns "99"
// Number("99") returns 99
```

# Context & Application

Understanding object-to-primitive conversion explains many of JavaScript's most surprising behaviors, such as why `[] + []` is `""` and why `[] + {}` is `"[object Object]"`. This is one of the most complex aspects of JavaScript's type system.

# Examples

From the source text (pp. 68-70):
```javascript
({x: 1, y: 2}).toString()    // => "[object Object]"
[1,2,3].toString()            // => "1,2,3"
(function(x) { f(x); }).toString()  // => "function(x) { f(x); }"

let d = new Date(2020,0,1);
d.toString()     // => "Wed Jan 01 2020 00:00:00 GMT-0800 (...)"

let d = new Date(2010, 0, 1);
d.valueOf()      // => 1262332800000

// Why empty arrays convert to 0
Number([])       // => 0: this is unexpected!
Number([99])     // => 99: really?
// Array valueOf() returns the array itself (not primitive),
// so toString() is called: [].toString() is "" → Number("") is 0
```

# Relationships

## Builds Upon
- **type-coercion** — Object-to-primitive is the most complex coercion
- **primitive-vs-object-types** — Converting between the two categories

## Enables
- Understanding complex operator behavior with objects

## Related
- **strict-vs-loose-equality** — `==` triggers no-preference conversion for objects
- **boolean-truthy-falsy** — All objects are truthy regardless of valueOf/toString

## Contrasts With
- None within this source

# Common Errors

- **Error**: Assuming `Number({})` returns `0` like `Number([])`.
  **Correction**: `{}.toString()` returns `"[object Object]"` which converts to `NaN`, not `0`.

# Common Confusions

- **Confusion**: The `+` operator always triggers prefer-number for objects.
  **Clarification**: The `+` operator uses the no-preference algorithm. For non-Date objects this acts like prefer-number, but for Date objects it acts like prefer-string (p. 67).

# Source Reference

Chapter 3: Types, Values, and Variables, Section 3.9.3, pages 66-70.

# Verification Notes

- Definition source: Direct quotes from pp. 66-70
- Confidence rationale: High — thorough, detailed treatment
- Uncertainties: Full customization via Symbol.toPrimitive deferred to §14.4.7
- Cross-reference status: Verified
