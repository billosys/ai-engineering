---
# === CORE IDENTIFICATION ===
concept: "String() Function"
slug: string-function

# === CLASSIFICATION ===
category: type-system
subcategory: conversion-algorithms
tier: foundational

# === PROVENANCE ===
source: "Deep JavaScript"
source_slug: deep-js
authors: "Dr. Axel Rauschmayer"
chapter: "Type coercion in JavaScript"
chapter_number: 2
section: "2.4.2.1 String()"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "String()"
  - String constructor

# === TYPED RELATIONSHIPS ===
prerequisites:
  - to-string
  - type-coercion
extends:
  - to-string
related:
  - to-primitive
  - symbol-to-primitive
contrasts_with:
  - to-string

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is type coercion in JavaScript?"
---

# Quick Definition

`String()` is JavaScript's built-in function for explicit string conversion, which differs from the spec's `ToString()` by specially handling symbols and supporting both function-call and constructor (`new`) usage.

# Core Definition

As described in "Deep JavaScript" (Ch 2, Section 2.4.2.1): `String()` behaves differently depending on whether it is invoked as a function call or via `new`. When function-called, it converts values to string primitives, with special handling for symbols (returning their descriptive string via `SymbolDescriptiveString()` instead of throwing). When new-called, it creates a `String` wrapper object. For `undefined` with no `new`, it returns the empty string `''`.

# Prerequisites

- **ToString** — String() builds upon the ToString specification algorithm.
- **Type coercion** — Understanding when and why explicit conversion is used.

# Key Properties

1. Function-called: returns a string primitive.
2. New-called: returns a String wrapper object.
3. Special handling for symbols: returns `'Symbol(description)'` instead of throwing.
4. `String(undefined)` returns `''` when function-called (differs from `ToString` which returns `'undefined'`).
5. Uses `new.target` to distinguish call modes.

# Construction / Recognition

## To Construct/Create:
1. `String(value)` for explicit string conversion.
2. `new String(value)` for String wrapper objects (rarely needed).

## To Identify/Recognize:
1. Direct calls to `String()` in code represent explicit string conversion.

# Context & Application

`String()` is the recommended way to explicitly convert values to strings when symbols might be involved. Template literals and `+''` use `ToString()` internally and will throw on symbols. `String()` is safer for general-purpose conversion.

# Examples

**Example 1** (Ch 2): The algorithm in JavaScript form:
```js
function String(value) {
  let s;
  if (value === undefined) {
    s = '';
  } else {
    if (new.target === undefined && TypeOf(value) === 'symbol') {
      return SymbolDescriptiveString(value);
    }
    s = ToString(value);
  }
  if (new.target === undefined) {
    return s;
  }
  return StringCreate(s, new.target.prototype);
}
```

**Example 2** (Ch 2): Symbol handling:
```js
const sym = Symbol('sym');

// String() handles symbols gracefully:
> String(sym)
'Symbol(sym)'

// ToString() (via template literal) throws:
> `${sym}`
TypeError: Cannot convert a Symbol value to a string
```

# Relationships

## Builds Upon
- **ToString** — String() delegates to ToString() for most types.

## Enables
- **Safe string conversion** — Provides a way to convert any value including symbols.

## Related
- **Symbol.prototype.toString()** — Another way to convert symbols to strings.

## Contrasts With
- **ToString** — ToString throws on symbols; String() returns descriptive string.

# Common Errors

- **Error**: Using `'' + symbol` instead of `String(symbol)`.
  **Correction**: String concatenation uses `ToString()` which throws on symbols. Use `String()` for safe conversion.

# Common Confusions

- **Confusion**: `String()` and `new String()` return the same thing.
  **Clarification**: `String()` returns a primitive string; `new String()` returns a String wrapper object. They are different types.

# Source Reference

Chapter 2: Type coercion in JavaScript, Section 2.4.2.1, lines 676-727.

# Verification Notes

- Definition source: direct (algorithm quoted from source)
- Confidence rationale: Full algorithm provided with explanation
- Cross-reference status: verified
