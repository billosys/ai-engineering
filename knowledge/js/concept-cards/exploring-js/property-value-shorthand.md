---
concept: Property Value Shorthand
slug: property-value-shorthand
category: objects
subcategory: properties
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Objects"
chapter_number: 30
pdf_page: null
section: "30.3.2 Object literals: property value shorthands"
extraction_confidence: high
aliases:
  - "shorthand property"
prerequisites:
  - object-literal
extends: []
related: []
contrasts_with: []
answers_questions:
  - "How do I create an object property from a variable with the same name?"
---

# Quick Definition

Property value shorthand allows omitting the value when a variable name matches the property key: `{x, y}` is equivalent to `{x: x, y: y}`.

# Core Definition

As described in "Exploring JavaScript" Ch. 30, whenever the value of a property is defined via a variable that has the same name as the key, we can omit the key. For example, `{x, y}` is the same as `{x: x, y: y}`.

# Prerequisites

- Object literal

# Key Properties

1. Syntax: `{name}` is equivalent to `{name: name}`.
2. Works with any variable or parameter name.
3. Commonly used in `return` statements and function parameters.

# Construction / Recognition

```js
function createPoint(x, y) {
  return {x, y}; // Same as: {x: x, y: y}
}
```

# Context & Application

Very common in modern JavaScript for creating objects from variables.

# Examples

From the source text (Ch. 30, section 30.3.2):

```js
function createPoint(x, y) {
  return {x, y};
}
assert.deepEqual(createPoint(9, 2), { x: 9, y: 2 });
```

# Relationships

## Builds Upon
- **Object Literal** -- shorthand is an object literal feature

# Source Reference

Chapter 30: Objects, Section 30.3.2, lines 428-444.

# Verification Notes

- Definition source: direct
- Confidence rationale: Simple, explicit definition
- Cross-reference status: verified
