---
# === CORE IDENTIFICATION ===
concept: Undefined Value
slug: undefined-value

# === CLASSIFICATION ===
category: primitive-types
subcategory: non-values
tier: foundational

# === PROVENANCE ===
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "The non-values undefined and null"
chapter_number: 16
pdf_page: null
section: "undefined vs. null"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - null-value
  - falsy-and-truthy-values
contrasts_with:
  - null-value

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is `undefined` and how does it differ from `null`?"
  - "What distinguishes `null` from `undefined`?"
  - "What distinguishes primitive values from objects?"
---

# Quick Definition

`undefined` is a primitive value that means "not initialized" or "not existing" -- it is the non-value used by the language itself when something is uninitialized or missing.

# Core Definition

`undefined` means "not initialized" (e.g., a variable) or "not existing" (e.g., a property of an object). It is the non-value used by the language (when something is uninitialized, etc.), as opposed to `null` which represents an intentional absence of value chosen by the programmer (Ch. 16, Section 16.1).

# Prerequisites

Foundational concept with no prerequisites.

# Key Properties

1. `typeof undefined` is `'undefined'`
2. `undefined` is falsy
3. Accessing properties on `undefined` throws a `TypeError`
4. `undefined` and `null` are the only values that throw when you read a property from them
5. JSON does not support `undefined` -- properties with `undefined` values are omitted by `JSON.stringify()`

# Construction / Recognition

`undefined` appears in these contexts:
- Uninitialized `let` variable: `let myVar; // undefined`
- Missing function parameter: `func()` when `func(x)` expected
- Missing object property: `obj.unknownProp`
- Function with no `return` statement

# Context & Application

`undefined` appears naturally throughout JavaScript as the language's default "no value" signal. Understanding when `undefined` appears is essential for writing defensive code and avoiding `TypeError` from property access on `undefined`.

# Examples

From the source text:

```js
// Uninitialized variable
let myVar;
assert.equal(myVar, undefined);

// Missing parameter
function func(x) { return x; }
assert.equal(func(), undefined);

// Missing property
const obj = {};
assert.equal(obj.unknownProp, undefined);

// No return statement
function func() {}
assert.equal(func(), undefined);
```

# Relationships

## Builds Upon
- No prerequisites

## Enables
- **nullish-coalescing-operator** — triggers the default value
- **falsy-and-truthy-values** — `undefined` is falsy

## Related
- **null-value** — the other non-value in JavaScript

## Contrasts With
- **null-value** — `null` means "intentional absence of an object value"; `undefined` means "not initialized/not existing"

# Common Errors

- **Error**: Accessing a property on `undefined` (e.g., `undefined.prop`)
  **Correction**: Check for `undefined` before accessing properties, or use optional chaining (`?.`).

# Common Confusions

- **Confusion**: Thinking `undefined` and `null` are interchangeable
  **Clarification**: `undefined` is used by the language for uninitialized/missing values; `null` is used by programmers to explicitly indicate "no value."

# Source Reference

Chapter 16: The non-values undefined and null, Sections 16.1-16.2.1, lines 56-120.

# Verification Notes

- Definition source: direct (quoted from spec via the author)
- Confidence rationale: Explicit definition with comprehensive occurrence list
- Cross-reference status: verified
