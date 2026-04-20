---
concept: Computed Property Keys
slug: computed-property-keys
category: objects
subcategory: properties
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Objects"
chapter_number: 30
pdf_page: null
section: "30.9.2 Computed keys in object literals"
extraction_confidence: high
aliases:
  - "dynamic property keys"
  - "[expr] key"
prerequisites:
  - object-literal
extends: []
related:
  - property-value-shorthand
contrasts_with: []
answers_questions:
  - "How do I use dynamic expressions as property keys?"
---

# Quick Definition

Computed property keys use bracket notation (`[expr]`) in object literals and class bodies to dynamically determine property keys from expressions.

# Core Definition

As described in "Exploring JavaScript" Ch. 30, computed keys in object literals use the syntax `[expression]: value`. The expression is evaluated at runtime to produce the property key. This works for properties, methods, getters, and setters. Symbols are commonly used as computed keys.

# Prerequisites

- Object literal

# Key Properties

1. Syntax: `{ [expression]: value }`.
2. Expression evaluated at runtime.
3. Works for properties, methods, getters, setters.
4. Commonly used with Symbols.
5. Also supported in class bodies.

# Construction / Recognition

```js
const key = 'hello';
const obj = { [key]: 'world' };
// { hello: 'world' }
```

# Context & Application

Used when property keys need to be determined dynamically, or when using Symbols as property keys.

# Examples

```js
const symbolKey = Symbol('myKey');
const obj = {
  [symbolKey]: 'symbol value',
  ['computed' + 'Key']: 42,
};
```

# Relationships

## Builds Upon
- **Object Literal** -- computed keys are an object literal feature

# Source Reference

Chapter 30: Objects, Section 30.9.2.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit syntax shown
- Cross-reference status: verified
