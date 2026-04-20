---
concept: Dispatched vs Direct Method Calls
slug: dispatched-vs-direct-method-calls
category: classes
subcategory: internals
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Classes"
chapter_number: 31
pdf_page: null
section: "31.3.5 Dispatched vs. direct method calls"
extraction_confidence: high
aliases:
  - "dynamic dispatch"
  - "direct method call"
prerequisites:
  - prototype-chain
  - class-declaration
extends: []
related:
  - function-call-method
contrasts_with: []
answers_questions:
  - "How do method calls work with prototype chains?"
---

# Quick Definition

Dispatched method calls traverse the prototype chain to find and invoke a method, while direct method calls bypass dispatch by calling a method explicitly via its prototype with `.call()`.

# Core Definition

As described in "Exploring JavaScript" Ch. 31, normal method calls are dispatched: JavaScript traverses the prototype chain to find the method, then invokes it with `this` set to the receiver. Direct method calls skip the lookup: `SomeClass.prototype.method.call(obj)` calls the method directly. Direct calls are useful for borrowing methods from `Object.prototype` for objects that don't inherit from it.

# Prerequisites

- Prototype chain
- Class declaration

# Key Properties

1. Dispatched: `obj.method()` -- finds method via prototype chain, sets `this` to `obj`.
2. Direct: `Proto.method.call(obj)` -- calls method directly, sets `this` explicitly.
3. Direct calls are useful for borrowing methods from objects not in the prototype chain.
4. `this` always points to the instance, regardless of where the method is in the chain.

# Construction / Recognition

```js
// Dispatched
jane.describe();

// Direct (equivalent)
Person.prototype.describe.call(jane);
```

# Context & Application

Direct method calls are used when borrowing `Object.prototype` methods for objects with `null` prototypes.

# Examples

From the source text (Ch. 31, section 31.3.5.2):

```js
const obj = Object.create(null);
// obj has no toString()
assert.equal(
  Object.prototype.toString.call(obj),
  '[object Object]'
);
```

# Relationships

## Related
- **Function.prototype.call()** -- used for direct method calls

# Source Reference

Chapter 31: Classes, Section 31.3.5, lines 1060-1188.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit two-step breakdown of dispatch
- Cross-reference status: verified
