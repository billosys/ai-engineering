---
# === CORE IDENTIFICATION ===
concept: Object.prototype.toString
slug: object-prototype-tostring

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
section: "2.4.2.3 Object.prototype.toString"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - default toString

# === TYPED RELATIONSHIPS ===
prerequisites:
  - to-string
  - ordinary-to-primitive
extends: []
related:
  - to-primitive
  - symbol-to-primitive
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does ToPrimitive relate to ToString and ToNumber?"
---

# Quick Definition

`Object.prototype.toString` is the default `.toString()` method that produces `'[object Tag]'` strings, using `Symbol.toStringTag` to customize the tag, and is the fallback when objects need string conversion.

# Core Definition

As described in "Deep JavaScript" (Ch 2, Section 2.4.2.3): The default `Object.prototype.toString` determines a built-in tag based on the object's internal slots (e.g., `'Array'`, `'Function'`, `'RegExp'`, `'Date'`, etc.), then checks for a `Symbol.toStringTag` property to override it. The result format is always `'[object Tag]'`. This is used when converting plain objects to strings and is the default for all objects that don't override `.toString()`.

# Prerequisites

- **ToString** — Object.prototype.toString is called during string conversion of objects.
- **OrdinaryToPrimitive** — This method may be called as part of the ordinary-to-primitive path.

# Key Properties

1. Returns format: `'[object Tag]'`.
2. Determines built-in tag based on internal slots (Array, Function, Error, etc.).
3. Default tag is `'Object'`.
4. `Symbol.toStringTag` overrides the tag.
5. Most built-in types override `.toString()` with more useful implementations.
6. `Object.prototype.toString.call(value)` is a reliable type-checking technique.

# Construction / Recognition

## To Construct/Create:
1. Call `.toString()` on an object that doesn't override it.
2. Or call `Object.prototype.toString.call(value)` explicitly.

## To Identify/Recognize:
1. Output matching `'[object Something]'` format.

# Context & Application

`Object.prototype.toString` is useful for type detection because it reveals internal type information even when `.toString()` is overridden. The pattern `Object.prototype.toString.call(value)` is used in libraries for reliable type checking.

# Examples

**Example 1** (Ch 2): Default toString on objects:
```js
> String({})
'[object Object]'
```

**Example 2** (Ch 2): Customizing with Symbol.toStringTag:
```js
class MyClass {}
MyClass.prototype[Symbol.toStringTag] = 'Custom!';
assert.equal(
  String(new MyClass()), '[object Custom!]');
```

**Example 3** (Ch 2): Comparing overridden vs. original:
```js
> ['a', 'b'].toString()
'a,b'
> Object.prototype.toString.call(['a', 'b'])
'[object Array]'
```

# Relationships

## Builds Upon
- **ToString** — Called as part of string conversion chain.
- **OrdinaryToPrimitive** — May invoke toString() during primitive conversion.

## Enables
- **Type detection** — `Object.prototype.toString.call()` as reliable type checking.
- **Custom string tags** — `Symbol.toStringTag` customization.

## Related
- **Symbol.toPrimitive** — Alternative override mechanism for primitive conversion.

## Contrasts With
- None directly.

# Common Errors

- **Error**: Relying on `.toString()` for type detection on values that override it.
  **Correction**: Use `Object.prototype.toString.call(value)` for reliable type detection.

# Common Confusions

- **Confusion**: `String(obj)` always calls `Object.prototype.toString`.
  **Clarification**: `String(obj)` calls `ToPrimitive`, which may call `toString()` or `valueOf()` depending on the hint. If the object overrides `.toString()`, that override is called, not `Object.prototype.toString`.

# Source Reference

Chapter 2: Type coercion in JavaScript, Section 2.4.2.3, lines 753-839.

# Verification Notes

- Definition source: direct (algorithm quoted from source)
- Confidence rationale: Full algorithm provided with examples
- Cross-reference status: verified
