---
concept: Object.assign()
slug: object-assign
category: objects
subcategory: copying
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Objects"
chapter_number: 30
pdf_page: null
section: "30.4.3 Destructive spreading: `Object.assign()`"
extraction_confidence: high
aliases:
  - "Object.assign"
prerequisites:
  - spreading-into-object-literals
extends: []
related:
  - structured-clone
contrasts_with:
  - spreading-into-object-literals
answers_questions:
  - "How do I copy properties from one object to another mutatively?"
---

# Quick Definition

`Object.assign(target, ...sources)` copies all enumerable own properties from source objects to the target, mutating and returning the target.

# Core Definition

As described in "Exploring JavaScript" Ch. 30, `Object.assign(target, source1, source2, ...)` assigns all properties of each source to `target` and returns `target`. It is a destructive (mutating) alternative to spread properties. Like spreading, it performs a shallow copy. Introduced in ES6.

# Prerequisites

- Spreading into object literals

# Key Properties

1. Introduced in ES6.
2. Mutates the target object.
3. Returns the target.
4. Shallow copy (like spreading).
5. Last source wins on key conflicts.

# Construction / Recognition

```js
const result = Object.assign(target, {b: 2}, {c: 3});
// result === target
```

# Context & Application

Use when you need to mutate an existing object. Prefer spread (`{...}`) for non-destructive copying.

# Examples

From the source text (Ch. 30, section 30.4.3):

```js
const target = { a: 1 };
const result = Object.assign(target, {b: 2}, {c: 3, b: true});
assert.deepEqual(result, { a: 1, b: true, c: 3 });
assert.equal(result, target);
```

# Relationships

## Contrasts With
- **Spreading Into Object Literals** -- spreading is non-destructive; `Object.assign()` mutates

## Related
- **structuredClone()** -- deep copy alternative

# Source Reference

Chapter 30: Objects, Section 30.4.3, lines 773-804.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit definition with comparison to spreading
- Cross-reference status: verified
