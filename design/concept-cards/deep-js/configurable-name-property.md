---
# === CORE IDENTIFICATION ===
concept: Configurable Name Property
slug: configurable-name-property

# === CLASSIFICATION ===
category: functions
subcategory: naming
tier: intermediate

# === PROVENANCE ===
source: "Deep JavaScript"
source_slug: deep-js
authors: "Dr. Axel Rauschmayer"
chapter: "The property .name of functions (bonus)"
chapter_number: 21
section: "21.4 Changing the names of functions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - function-name-property
extends: []
related:
  - function-naming-rules
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes a named function expression from an anonymous function?"
---

# Quick Definition

The `.name` property of functions is non-writable but configurable, meaning it cannot be changed via assignment but can be changed via `Object.defineProperty()`.

# Core Definition

From "Deep JavaScript" (Ch 21.4): The property attributes of `.name` are: `{ value: 'func', writable: false, enumerable: false, configurable: true }`. "The property not being writable means that we can't change its value via assignment." But: "The property is, however, configurable, which means that we can change it by re-defining it."

# Prerequisites

- **Function .name property** — Understanding the property being described

# Key Properties

1. `writable: false` -- cannot change via `func.name = 'newName'` (throws in strict mode)
2. `configurable: true` -- can change via `Object.defineProperty(func, 'name', { value: 'newName' })`
3. `enumerable: false` -- does not appear in `Object.keys()` or `for...in`

# Construction / Recognition

## To Construct/Create:
1. Use `Object.defineProperty(func, 'name', { value: 'newName' })` to change the name

## To Identify/Recognize:
1. `Object.getOwnPropertyDescriptor(func, 'name')` reveals the attributes

# Context & Application

The configurability allows frameworks and tools to rename functions for better debugging or to match expected conventions, while the non-writability prevents accidental changes.

# Examples

**Example 1** (Ch 21): Cannot assign:
```js
const func = function () {};
assert.throws(
  () => func.name = 'differentName',
  /^TypeError: Cannot assign to read only property 'name'/
);
```

**Example 2** (Ch 21): Can redefine:
```js
Object.defineProperty(func, 'name', { value: 'differentName' });
assert.equal(func.name, 'differentName');
```

# Relationships

## Builds Upon
- **Function .name property** — Describes the property's attributes

# Common Errors

- **Error**: Trying `func.name = 'newName'` to rename a function
  **Correction**: Use `Object.defineProperty()` because `.name` is non-writable

# Common Confusions

- **Confusion**: Non-writable means the name can never be changed
  **Clarification**: `configurable: true` allows redefinition via `Object.defineProperty()`

# Source Reference

Chapter 21: The property .name of functions (bonus), Section 21.4, lines 11437+.

# Verification Notes

- Definition source: direct from source with property descriptor and examples
- Confidence rationale: Complete attribute listing shown
- Cross-reference status: verified
