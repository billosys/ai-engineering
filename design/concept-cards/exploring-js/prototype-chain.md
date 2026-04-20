---
concept: Prototype Chain
slug: prototype-chain
category: objects
subcategory: inheritance
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Objects"
chapter_number: 30
pdf_page: null
section: "30.8 Prototype chains"
extraction_confidence: high
aliases:
  - "prototypal inheritance"
  - "prototype"
  - "__proto__"
prerequisites:
  - object-literal
extends: []
related:
  - own-property
  - class-declaration
  - subclassing
contrasts_with: []
answers_questions:
  - "What is the prototype chain?"
  - "How does subclassing (extends) interact with the prototype chain?"
  - "What must I know before learning about classes and inheritance?"
---

# Quick Definition

The prototype chain is JavaScript's core inheritance mechanism: each object has a prototype (another object or `null`), forming a chain through which property lookups traverse until a match is found or the chain ends.

# Core Definition

As described in "Exploring JavaScript" Ch. 30, prototypes are JavaScript's only inheritance mechanism. Each object has a prototype that is either `null` or an object. The object inherits all properties of its prototype. Given that a prototype can itself have a prototype, we get chains of objects -- prototype chains. Getting a property considers the entire chain (own and inherited). Setting a property only affects the first object (creating an own property that overrides inherited ones). Non-inherited properties are called own properties.

# Prerequisites

- Object literal

# Key Properties

1. Every object has a prototype (another object or `null`).
2. Property reads traverse the entire chain.
3. Property writes only affect the first object (override, not mutate prototype).
4. Own properties are non-inherited; they shadow inherited ones.
5. Set prototype at creation: `{__proto__: proto}` or `Object.create(proto)`.
6. Get prototype: `Object.getPrototypeOf(obj)`.
7. `Object.prototype` ends most prototype chains (its prototype is `null`).

# Construction / Recognition

```js
const proto = { protoProp: 'a' };
const obj = {
  __proto__: proto,
  objProp: 'b',
};
// obj inherits .protoProp from proto
assert.equal(obj.protoProp, 'a');
```

# Context & Application

Prototype chains are the foundation of JavaScript's object-oriented programming. Classes use prototypes internally. Understanding prototype chains is essential before learning classes and inheritance.

# Examples

From the source text (Ch. 30, section 30.8.2):

```js
const proto = { protoProp: 'a' };
const obj = { __proto__: proto };

obj.protoProp = 'x'; // Creates own property, doesn't mutate proto
assert.equal(proto.protoProp, 'a'); // unchanged
assert.equal(obj.protoProp, 'x');   // own property overrides
```

# Relationships

## Enables
- **Class Declaration** -- classes set up prototype chains for instances
- **Subclassing** -- `extends` creates two linked prototype chains

## Related
- **Own Property** -- non-inherited properties
- **Object.hasOwn()** -- checks if a property is own

# Common Errors

- **Error**: Thinking setting a property on an object modifies its prototype.
  **Correction**: Setting creates a new own property that overrides the inherited one; the prototype is unaffected.

# Common Confusions

- **Confusion**: Confusing `.__proto__` (the prototype link) with `.prototype` (the constructor's property for instances).
  **Clarification**: `obj.__proto__` is the prototype of `obj`. `SomeClass.prototype` is the object that becomes the prototype of instances created via `new SomeClass()`.

# Source Reference

Chapter 30: Objects, Section 30.8, lines 1854-2099.

# Verification Notes

- Definition source: direct
- Confidence rationale: Core concept with extensive coverage
- Cross-reference status: verified across Ch. 30 and Ch. 31
