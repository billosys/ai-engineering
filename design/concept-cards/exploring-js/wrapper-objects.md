---
# === CORE IDENTIFICATION ===
concept: Wrapper Objects
slug: wrapper-objects

# === CLASSIFICATION ===
category: types-values
subcategory: type-system
tier: foundational

# === PROVENANCE ===
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Values"
chapter_number: 14
pdf_page: null
section: "14.8.1.1 Wrapper classes for primitive values (advanced)"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - wrapper classes
  - boxing

# === TYPED RELATIONSHIPS ===
prerequisites:
  - primitive-values
  - constructor-functions
extends: []
related:
  - typeof-operator
  - instanceof-operator
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are primitive values vs. objects in JavaScript?"
---

# Quick Definition

Wrapper objects are created by `new`-invoking primitive constructors (like `new Boolean(true)`), producing objects that wrap primitive values. They differ from primitives in type and identity behavior and should be avoided.

# Core Definition

"If we new-invoke a constructor function associated with a primitive type, it returns a so-called *wrapper object*. This is the standard way of converting a primitive value to an object -- by 'wrapping' it." (Ch. 14, &sect;14.8.1.1). The primitive is not an instance of the wrapper class (`true instanceof Boolean` is `false`). The wrapper is not a primitive (`typeof wrapper` is `'object'`). Wrappers can be unwrapped via `.valueOf()`.

# Prerequisites

- **primitive-values** -- wrapper objects wrap primitives
- **constructor-functions** -- wrapper classes are constructor functions

# Key Properties

1. Created via `new Boolean()`, `new Number()`, `new String()`, or `Object()`
2. `typeof wrapper` returns `'object'`, not the primitive type
3. `wrapper instanceof Boolean` returns `true` (unlike the primitive)
4. Unwrap via `.valueOf()`
5. Should be avoided in normal code
6. `Object(prim)` also wraps primitives

# Construction / Recognition

```js
const prim = true;
assert.equal(typeof prim, 'boolean');
assert.equal(prim instanceof Boolean, false);

const wrapper = Object(prim);
assert.equal(typeof wrapper, 'object');
assert.equal(wrapper instanceof Boolean, true);
assert.equal(wrapper.valueOf(), prim); // unwrap
```

# Context & Application

Wrapper objects "virtually never show up in normal code" and should be avoided. Understanding them helps explain `typeof` and `instanceof` behavior.

# Examples

From the source text (Ch. 14, &sect;14.8.1.1):
```js
const prim = true;
assert.equal(typeof prim, 'boolean');
assert.equal(prim instanceof Boolean, false);

const wrapper = Object(prim);
assert.equal(typeof wrapper, 'object');
assert.equal(wrapper instanceof Boolean, true);
assert.equal(wrapper.valueOf(), prim);
```

# Relationships

## Builds Upon
- **primitive-values** -- wrappers wrap primitives
- **constructor-functions** -- created via new-invocation

## Enables
- Understanding typeof/instanceof quirks

## Related
- **typeof-operator** -- wrapper objects return 'object'
- **instanceof-operator** -- wrappers are instances; primitives are not

## Contrasts With
- No direct contrast

# Common Errors

- **Error**: Creating wrapper objects accidentally with `new String('abc')`.
  **Correction**: Use `String('abc')` (without `new`) for type conversion. Never use `new` with primitive constructors.

# Common Confusions

- **Confusion**: Thinking `new Number(123) === 123` is true.
  **Clarification**: The wrapper is an object; the literal is a primitive. They have different types and `===` returns false.

# Source Reference

Chapter 14: Values, Section 14.8.1.1, lines 703-735.

# Verification Notes

- Definition source: direct from source
- Confidence rationale: Complete wrapper lifecycle shown (wrap, type check, unwrap)
- Cross-reference status: verified
