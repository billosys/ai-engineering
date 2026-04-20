---
concept: Own Property
slug: own-property
category: objects
subcategory: properties
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Objects"
chapter_number: 30
pdf_page: null
section: "30.8.1 JavaScript's operations: all properties vs. own properties"
extraction_confidence: high
aliases:
  - "own properties"
prerequisites:
  - prototype-chain
extends: []
related:
  - object-has-own
contrasts_with: []
answers_questions:
  - "What is the difference between own and inherited properties?"
---

# Quick Definition

An own property is a non-inherited property that belongs directly to an object, as opposed to properties inherited from the prototype chain.

# Core Definition

As described in "Exploring JavaScript" Ch. 30, non-inherited properties are called own properties. Some operations consider all properties (getting), while others only consider own properties (`Object.keys()`, setting). When setting a property via an object, only that object is affected -- even if the property exists on a prototype, a new own property is created that overrides the inherited one.

# Prerequisites

- Prototype chain

# Key Properties

1. Own properties belong directly to the object.
2. Getting reads both own and inherited properties.
3. Setting always creates/modifies an own property.
4. `Object.keys()`, `Object.entries()` only list own enumerable properties.
5. `Object.hasOwn(obj, key)` (ES2022) checks if a property is own.

# Construction / Recognition

```js
const proto = { inherited: 'a' };
const obj = { __proto__: proto, own: 'b' };
assert.deepEqual(Object.keys(obj), ['own']); // only own
assert.equal('inherited' in obj, true);        // includes inherited
```

# Context & Application

Understanding own vs inherited properties is crucial for property enumeration, prototype chain behavior, and avoiding unintended prototype mutations.

# Examples

From the source text (Ch. 30, section 30.8.4):

```js
assert.equal(Object.hasOwn(obj, 'objProp'), true);
assert.equal(Object.hasOwn(obj, 'protoProp'), false);
assert.equal(Object.hasOwn(proto, 'protoProp'), true);
```

# Relationships

## Builds Upon
- **Prototype Chain** -- own properties are the non-inherited portion

# Source Reference

Chapter 30: Objects, Section 30.8.1 and 30.8.4, lines 1903-2099.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit definition in source
- Cross-reference status: verified
