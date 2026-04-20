---
concept: Object Destructuring
slug: object-destructuring
category: destructuring
subcategory: null
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Destructuring"
chapter_number: 40
pdf_page: null
section: "40.4 Object-destructuring"
extraction_confidence: high
aliases:
  - "object pattern"
  - "property destructuring"
prerequisites:
  - destructuring
extends: []
related:
  - array-destructuring
  - rest-properties
  - destructuring-default-values
contrasts_with:
  - array-destructuring
answers_questions:
  - "What is destructuring?"
  - "How do I use destructuring to extract values from objects and arrays?"
---

# Quick Definition

Object destructuring uses patterns that look like object literals (`{key: variable}`) to batch-extract property values, with a shorthand form (`{key}`) when the variable name matches the property name.

# Core Definition

Object-destructuring lets us batch-extract values of properties via patterns that look like object literals. The pattern `{street: s, city: c}` extracts properties `street` and `city` into variables `s` and `c`. Property value shorthands allow `{street, city}` when variable names match property names. Object destructuring can also work with primitives (accessing their properties) and with arrays (accessing by numeric index).

# Prerequisites

- **destructuring** -- the general concept

# Key Properties

1. Introduced in ES2015 (ES6)
2. Pattern: `{propKey: variable}` or shorthand `{propKey}`
3. Can destructure primitives: `const {length: len} = 'abc'`
4. Can destructure arrays by index: `const {0: x, 2: y} = ['a','b','c']`
5. Supports rest properties: `const {a, ...rest} = obj`
6. Fails on `undefined` and `null`

# Construction / Recognition

```js
const address = {street: 'Evergreen', city: 'Springfield'};
const {street: s, city: c} = address;
// shorthand
const {street, city} = address;
```

# Context & Application

Object destructuring is ubiquitous in modern JavaScript: importing named exports, extracting function options, handling API responses, and processing multiple return values.

# Examples

```js
const address = {
  street: 'Evergreen Terrace',
  number: '742',
  city: 'Springfield',
};
const {street, city} = address;
assert.equal(street, 'Evergreen Terrace');
assert.equal(city, 'Springfield');

// Destructure primitive
const {length: len} = 'abc';
assert.equal(len, 3);
```

(Chapter 40, Section 40.4, lines 212-304)

# Relationships

## Builds Upon
- **destructuring** -- specific pattern type

## Enables
- **rest-properties** -- collecting remaining properties
- **destructuring-default-values** -- defaults for missing properties

## Related
- **array-destructuring** -- the other pattern type

## Contrasts With
- **array-destructuring** -- object patterns match by key; array patterns match by position

# Common Errors

- **Error**: Starting a statement with object destructuring assignment: `{x} = {x: 1}`.
  **Correction**: Wrap in parentheses: `({x} = {x: 1})`. JavaScript parses leading `{` as a block.

# Common Confusions

- **Confusion**: The colon in `{key: var}` sets a value.
  **Clarification**: The colon maps a source property key to a target variable. `{street: s}` reads `street` into variable `s`.

# Source Reference

Chapter 40: Destructuring, Section 40.4, lines 212-304.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly defined with examples
- Cross-reference status: verified
