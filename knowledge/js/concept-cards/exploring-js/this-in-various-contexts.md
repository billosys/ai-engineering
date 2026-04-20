---
concept: this in Various Contexts
slug: this-in-various-contexts
category: objects
subcategory: methods
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Objects"
chapter_number: 30
pdf_page: null
section: "30.6.7 The value of `this` in various contexts"
extraction_confidence: high
aliases: []
prerequisites:
  - this-keyword
extends:
  - this-keyword
related: []
contrasts_with: []
answers_questions:
  - "What is `this` in different JavaScript contexts?"
---

# Quick Definition

The value of `this` depends on the context: `undefined` in ordinary function calls (strict mode), the receiver in method calls, the new instance in `new` calls, `globalThis` in scripts, and `undefined` in modules.

# Core Definition

As described in "Exploring JavaScript" Ch. 30, in callable entities: ordinary function calls have `this === undefined` (strict mode), arrow functions inherit `this` lexically, method calls set `this` to the receiver, and `new` calls set `this` to the new instance. At the top level: `this === globalThis` in `<script>` elements, `this === undefined` in ECMAScript modules, and `this === module.exports` in CommonJS modules. The author recommends pretending `this` doesn't exist in top-level scopes.

# Prerequisites

- The `this` keyword

# Key Properties

1. Function call (ordinary): `this === undefined` (strict mode).
2. Arrow function: `this` from surrounding scope.
3. Method call: `this` is receiver.
4. `new` call: `this` is new instance.
5. Top-level script: `this === globalThis`.
6. Top-level module: `this === undefined`.
7. CommonJS module: `this === module.exports`.

# Construction / Recognition

Reference table:
- `func()` -- `undefined`
- `obj.method()` -- `obj`
- `new C()` -- new instance
- Module top level -- `undefined`
- Script top level -- `globalThis`

# Context & Application

Comprehensive reference for understanding `this` in any JavaScript context.

# Examples

From the source text (Ch. 30, section 30.6.7):

```js
// Function call
function ordinaryFunc() { assert.equal(this, undefined); }

// Method call
const obj = {
  someMethod() { assert.equal(this, obj); }
};
obj.someMethod();
```

# Relationships

## Extends
- **The this Keyword** -- comprehensive context reference

# Source Reference

Chapter 30: Objects, Section 30.6.7, lines 1541-1574.

# Verification Notes

- Definition source: direct
- Confidence rationale: Complete context table provided
- Cross-reference status: verified
