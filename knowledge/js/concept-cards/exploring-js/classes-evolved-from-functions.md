---
concept: Classes Evolved from Functions
slug: classes-evolved-from-functions
category: classes
subcategory: internals
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Classes"
chapter_number: 31
pdf_page: null
section: "31.3.6 Classes evolved from ordinary functions"
extraction_confidence: high
aliases:
  - "constructor functions"
  - "pre-ES6 classes"
prerequisites:
  - class-declaration
  - ordinary-function
extends: []
related:
  - prototype-chain
contrasts_with: []
answers_questions:
  - "How did JavaScript create objects before classes?"
---

# Quick Definition

Before ES6, ordinary functions served as constructor functions, with methods added to `FuncName.prototype` manually. Classes provide better syntax for this same prototype-based pattern.

# Core Definition

As described in "Exploring JavaScript" Ch. 31, before ES6, ordinary functions were used as constructor functions: properties were set via `this.prop` in the function body, and methods were added to `FuncName.prototype`. Classes provide better syntax and additional benefits: subclassing built-in constructors, `super` for overridden properties, method-not-callable protection, and private instance data. A class *is* its constructor function (`typeof` returns `'function'`).

# Prerequisites

- Class declaration
- Ordinary function

# Key Properties

1. Pre-ES6 pattern: `function Ctor() { this.prop = value; }`, `Ctor.prototype.method = function() {}`.
2. Classes are backward-compatible with constructor functions.
3. A class IS the constructor: `typeof MyClass === 'function'`.
4. `MyClass.prototype.constructor === MyClass`.
5. Classes can even extend pre-ES6 constructor functions.

# Construction / Recognition

```js
// Pre-ES6
function StringBuilderConstr(str) {
  this.string = str;
}
StringBuilderConstr.prototype.add = function(s) {
  this.string += s; return this;
};

// ES6+
class StringBuilderClass {
  constructor(str) { this.string = str; }
  add(s) { this.string += s; return this; }
}
```

# Context & Application

Understanding this evolution helps work with legacy code and appreciate why classes work the way they do internally.

# Examples

From the source text (Ch. 31, section 31.3.6):

```js
class SubClass extends SuperConstructor {}
assert.equal(new SubClass() instanceof SuperConstructor, true);
```

# Relationships

## Related
- **Prototype Chain** -- both patterns use prototype chains

# Source Reference

Chapter 31: Classes, Section 31.3.6, lines 1190-1286.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit side-by-side comparison
- Cross-reference status: verified
