---
# === CORE IDENTIFICATION ===
concept: Converting Symbols
slug: converting-symbols

# === CLASSIFICATION ===
category: primitive-types
subcategory: symbols
tier: advanced

# === PROVENANCE ===
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Symbols"
chapter_number: 24
pdf_page: null
section: "Converting symbols"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - symbol-type
extends: []
related:
  - converting-to-string
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I convert between JavaScript types (string, number, boolean)?"
---

# Quick Definition

Symbols have strict conversion rules: they convert to boolean freely, but converting to number always throws `TypeError`, and coercing to string (via `+` or template literals) throws `TypeError` to prevent accidental property key type changes.

# Core Definition

Converting symbols: to boolean works (`Boolean(sym)` is `true`, `!sym` works); to number always throws `TypeError` (both `Number(sym)` and `sym*2`); to string works explicitly (`String(sym)` and `sym.toString()` are OK) but coercion throws (`''+sym` and `` `${sym}` `` throw `TypeError`). The intent of string coercion throwing is "to warn about accidentally turning a symbol into a string (which is a different kind of property key)" (Ch. 24, Section 24.5).

# Prerequisites

- **symbol-type** -- symbols being converted

# Key Properties

1. To boolean: always works (`Boolean(sym)` -> `true`)
2. To number: always throws `TypeError`
3. To string explicitly: works (`String(sym)`, `sym.toString()`)
4. To string via coercion: throws `TypeError` (`'' + sym`, `` `${sym}` ``)
5. Design intent: prevent accidental symbol-to-string conversion

# Construction / Recognition

```js
// Boolean: OK
Boolean(Symbol()) // true
!Symbol()         // false

// Number: TypeError
Number(Symbol())  // TypeError
Symbol() * 2      // TypeError

// String: explicit OK, coercion throws
String(Symbol('x'))  // 'Symbol(x)'
'' + Symbol()        // TypeError
`${Symbol()}`        // TypeError
```

# Context & Application

This is a practical concern when building error messages or logging that may include symbol values. Always use `String(sym)` for explicit conversion.

# Examples

From the source text:

```js
> const mySymbol = Symbol('mySymbol');
> 'Symbol I used: ' + mySymbol
TypeError: Cannot convert a Symbol value to a string
> 'Symbol I used: ' + String(mySymbol)
'Symbol I used: Symbol(mySymbol)'
```

# Relationships

## Builds Upon
- **symbol-type** — symbols being converted

## Enables
- Understanding error messages involving symbols

## Related
- **converting-to-string** — symbols are a special case in string conversion

## Contrasts With
- None

# Common Errors

- **Error**: Using `'prefix' + sym` to build a string with a symbol
  **Correction**: Use `'prefix' + String(sym)` for explicit conversion.

# Common Confusions

- **Confusion**: Thinking `TypeError` on string coercion is a bug
  **Clarification**: It is intentional to prevent accidentally creating a string property key from a symbol property key.

# Source Reference

Chapter 24: Symbols, Section 24.5, lines 362-494.

# Verification Notes

- Definition source: direct (conversion table provided)
- Confidence rationale: Complete conversion table with rationale
- Cross-reference status: verified
