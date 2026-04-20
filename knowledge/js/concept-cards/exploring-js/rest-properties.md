---
concept: Rest Properties in Destructuring
slug: rest-properties
category: destructuring
subcategory: null
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Destructuring"
chapter_number: 40
pdf_page: null
section: "40.4.2 Rest properties"
extraction_confidence: high
aliases:
  - "rest property"
  - "...rest in object destructuring"
prerequisites:
  - object-destructuring
extends: []
related:
  - rest-elements
  - spread-syntax
contrasts_with:
  - spread-syntax
answers_questions:
  - "How do rest parameters and spread syntax relate to each other?"
---

# Quick Definition

A rest property (`...variable`) in an object destructuring pattern collects all remaining own data properties not mentioned in the pattern into a new object.

# Core Definition

In object patterns, rest properties (which must come last) collect all data properties whose keys are not mentioned in the pattern into a new plain object. The syntax `{a: propValue, ...remaining} = obj` extracts property `a` and puts all other properties into `remaining`. This can be viewed as non-destructively removing a property from an object.

# Prerequisites

- **object-destructuring** -- rest properties are used in object patterns

# Key Properties

1. Introduced in ES2018 (rest/spread properties)
2. Must be last in the pattern
3. Collects remaining own properties into a new object
4. Effectively non-destructive property removal

# Construction / Recognition

```js
const obj = {a: 1, b: 2, c: 3};
const {a: propValue, ...remaining} = obj;
// propValue === 1, remaining === {b: 2, c: 3}
```

# Context & Application

Rest properties are commonly used to extract known properties and pass the remainder to other functions (e.g., React component props).

# Examples

```js
const obj = {a: 1, b: 2, c: 3};
const {a, ...remaining} = obj;
assert.equal(a, 1);
assert.deepEqual(remaining, {b: 2, c: 3});
```

(Chapter 40, Section 40.4.2, lines 282-304)

# Relationships

## Builds Upon
- **object-destructuring** -- used within object patterns

## Enables
- Property extraction and forwarding patterns

## Related
- **rest-elements** -- array equivalent
- **spread-syntax** -- object spread is the construction counterpart

## Contrasts With
- **spread-syntax** -- spread properties expand; rest properties collect

# Common Errors

- **Error**: Using rest properties to capture inherited properties.
  **Correction**: Rest properties only collect own (non-inherited) data properties.

# Common Confusions

- **Confusion**: Rest properties include the extracted properties.
  **Clarification**: The rest object contains only the properties NOT mentioned in the pattern.

# Source Reference

Chapter 40: Destructuring, Section 40.4.2, lines 282-304.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly defined
- Cross-reference status: verified
