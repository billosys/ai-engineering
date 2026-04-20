---
# === CORE IDENTIFICATION ===
concept: Getter/Setter Naming Prefixes
slug: getter-setter-naming

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
section: "21.2.6 Methods in object literals"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "get/set name prefix"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - function-name-property
  - method-naming
extends:
  - method-naming
related:
  - function-naming-rules
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes a named function expression from an anonymous function?"
---

# Quick Definition

Getter functions have `.name` prefixed with `'get '` and setter functions with `'set '`, distinguishing them from regular methods.

# Core Definition

From "Deep JavaScript" (Ch 21.2.6): "The names of getters are prefixed with `'get'`, the names of setters are prefixed with `'set'`." This applies to both object literal and class definition getters/setters. The spec operation `SetFunctionName()` handles this via its third parameter for name prefixes.

# Prerequisites

- **Function .name property** — Getter/setter naming is a specific naming rule
- **Method naming** — Getters/setters are a special case of method naming

# Key Properties

1. Getter `.name`: `'get ' + propertyName` (e.g., `'get myGetter'`)
2. Setter `.name`: `'set ' + propertyName` (e.g., `'set mySetter'`)
3. Must use `Object.getOwnPropertyDescriptor()` to access the getter/setter function
4. Works in both object literals and class definitions

# Construction / Recognition

## To Construct/Create:
1. `get myGetter() {}` in object literal or class definition

## To Identify/Recognize:
1. A `.name` starting with `'get '` or `'set '`

# Context & Application

The prefix helps distinguish getter/setter functions from regular methods in stack traces and debugging tools.

# Examples

**Example 1** (Ch 21): Object literal:
```js
const obj = {
  get myGetter() {},
  set mySetter(value) {},
};
const getter = Object.getOwnPropertyDescriptor(obj, 'myGetter').get;
assert.equal(getter.name, 'get myGetter');

const setter = Object.getOwnPropertyDescriptor(obj, 'mySetter').set;
assert.equal(setter.name, 'set mySetter');
```

# Relationships

## Builds Upon
- **Method naming** — Getters/setters are a special case with prefixes

## Related
- **Function naming rules** — One of many naming contexts

# Common Errors

- **Error**: Expecting `obj.myGetter.name` to work
  **Correction**: Accessing a getter via property access invokes it; must use `Object.getOwnPropertyDescriptor()` to get the function

# Common Confusions

- **Confusion**: The prefix `'get'` or `'set'` is part of the property name
  **Clarification**: The prefix is added to the `.name` property only; the property key remains unchanged

# Source Reference

Chapter 21: The property .name of functions (bonus), Sections 21.2.6-21.2.7, lines 11437+.

# Verification Notes

- Definition source: direct from source with assertions
- Confidence rationale: Explicitly demonstrated
- Cross-reference status: verified (references SetFunctionName() spec operation)
