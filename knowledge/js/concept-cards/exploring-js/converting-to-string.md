---
# === CORE IDENTIFICATION ===
concept: Converting to String
slug: converting-to-string

# === CLASSIFICATION ===
category: primitive-types
subcategory: strings
tier: intermediate

# === PROVENANCE ===
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Strings"
chapter_number: 22
pdf_page: null
section: "Converting values to strings in JavaScript has pitfalls"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "String()"
  - "string conversion"
  - "stringification"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - string-type
extends: []
related:
  - converting-to-number
  - converting-to-boolean
  - toprimitive
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I convert between JavaScript types (string, number, boolean)?"
---

# Quick Definition

Converting values to strings in JavaScript has pitfalls: `String(v)` is the most reliable built-in method but fails for some edge cases; symbols cannot be concatenated with `+`; and objects with null prototypes throw errors.

# Core Definition

Four common ways to convert to string: `String(v)`, `v.toString()`, `'' + v`, and template literals. Each has limitations: `v.toString()` fails for `undefined` and `null`; `'' + v` throws for symbols; `String()` fails for objects with null prototypes. `JSON.stringify()` works well for objects/arrays but does not support `undefined`, symbols, or bigints (Ch. 22, Section 22.5).

# Prerequisites

- **string-type** -- the target type

# Key Properties

1. `String(v)` is most reliable but fails for `{__proto__: null}` and `Symbol.prototype`
2. `v.toString()` throws for `undefined` and `null`
3. `'' + v` and template literals throw for symbols (to prevent accidental property key conversion)
4. `JSON.stringify()` is good for objects/arrays but does not support bigints (throws), undefined (returns undefined), symbols (returns undefined)
5. Custom `.toString()` method can customize object stringification

# Construction / Recognition

```js
> String(undefined)
'undefined'
> String(null)
'null'
> String(123.45)
'123.45'
> String(true)
'true'

// Symbol pitfall
> '' + Symbol()
TypeError: Cannot convert a Symbol value to a string
> String(Symbol())
'Symbol()'
```

# Context & Application

String conversion is essential for error messages, logging, and display. The author recommends `String()` for most cases but notes that a custom `toString()` combining `JSON.stringify()` and `String()` provides the most robust solution.

# Examples

From the source text:

```js
// Symbols: explicit conversion only
> '' + Symbol()
TypeError: Cannot convert a Symbol value to a string
> String(Symbol())
'Symbol()'

// Null prototype objects
> String({__proto__: null})
TypeError: Cannot convert object to primitive value

// Custom toString
const helloObj = {
  toString() { return 'Hello!'; }
};
assert.equal(String(helloObj), 'Hello!');
```

# Relationships

## Builds Upon
- **string-type** — target type of conversion

## Enables
- Error messages, logging, display

## Related
- **converting-to-number** — another type conversion
- **converting-to-boolean** — another type conversion
- **toprimitive** — used internally during string conversion

## Contrasts With
- None

# Common Errors

- **Error**: Using `'' + value` in error messages that might receive symbols
  **Correction**: Use `String(value)` which handles symbols correctly.

# Common Confusions

- **Confusion**: Thinking `String()` works for all values
  **Clarification**: It fails for objects with null prototypes (no `.toString()` or `.valueOf()` methods).

# Source Reference

Chapter 22: Strings, Section 22.5, lines 409-1320.

# Verification Notes

- Definition source: direct (comprehensive comparison table)
- Confidence rationale: Four methods compared with failure cases
- Cross-reference status: verified
