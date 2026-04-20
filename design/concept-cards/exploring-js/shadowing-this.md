---
concept: Shadowing this
slug: shadowing-this
category: objects
subcategory: methods
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Objects"
chapter_number: 30
pdf_page: null
section: "30.6.6 `this` pitfall: accidentally shadowing `this`"
extraction_confidence: high
aliases:
  - "this shadowing"
prerequisites:
  - this-keyword
  - arrow-function
extends: []
related:
  - extracting-methods
contrasts_with: []
answers_questions:
  - "Why can't I access `this` inside a nested ordinary function?"
---

# Quick Definition

An ordinary function nested inside a method shadows the method's `this` with its own `undefined` value, preventing access to the outer object -- a pitfall solved by using arrow functions.

# Core Definition

As described in "Exploring JavaScript" Ch. 30, when an ordinary function is used as a callback inside a method, it has its own `this` (set to `undefined` in strict mode), which shadows the method's `this`. The simplest fix is to use an arrow function, which doesn't have its own `this`. Other fixes include storing `this` in a variable (`const that = this`), using `.bind(this)`, or passing `this` as an extra argument to methods like `.map()`.

# Prerequisites

- The `this` keyword
- Arrow function

# Key Properties

1. Only affects ordinary functions, not arrow functions.
2. Arrow functions don't have `this`, so they can't shadow it.
3. Multiple workarounds: arrow functions, `const that = this`, `.bind(this)`.

# Construction / Recognition

```js
const prefixer = {
  prefix: '==> ',
  prefixArray(arr) {
    return arr.map(function (x) {
      return this.prefix + x;  // ERROR: this is undefined
    });
  },
};

// Fix: use arrow function
prefixArray(arr) {
  return arr.map((x) => this.prefix + x);  // works
}
```

# Context & Application

A common pitfall when using `.map()`, `.filter()`, `.forEach()` or other array methods with ordinary function callbacks inside methods.

# Examples

From the source text (Ch. 30, section 30.6.6):

```js
const prefixer = {
  prefix: '==> ',
  prefixStringArray(stringArray) {
    return stringArray.map(
      (x) => { return this.prefix + x; }
    );
  },
};
assert.deepEqual(
  prefixer.prefixStringArray(['a', 'b']),
  ['==> a', '==> b']
);
```

# Relationships

## Builds Upon
- **The this Keyword** -- understanding dynamic vs lexical this
- **Arrow Function** -- the primary solution

# Source Reference

Chapter 30: Objects, Section 30.6.6, lines 1421-1540.

# Verification Notes

- Definition source: direct
- Confidence rationale: Multiple solutions with detailed examples
- Cross-reference status: verified
