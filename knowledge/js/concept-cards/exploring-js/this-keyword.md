---
concept: The this Keyword
slug: this-keyword
category: functions
subcategory: this-binding
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Callable values"
chapter_number: 27
pdf_page: null
section: "27.3.3 The special variable `this` in methods, ordinary functions and arrow functions"
extraction_confidence: high
aliases:
  - "this"
  - "this binding"
  - "receiver"
prerequisites:
  - ordinary-function
  - arrow-function
extends: []
related:
  - method-definition
  - function-call-method
  - function-bind-method
contrasts_with: []
answers_questions:
  - "What distinguishes an arrow function from a traditional function?"
  - "How does `this` work differently in arrow vs traditional functions?"
---

# Quick Definition

`this` is an implicit parameter that refers to the receiver of a method call; it is dynamic in ordinary functions (set by how the function is called) and lexical in arrow functions (inherited from the enclosing scope).

# Core Definition

As described in "Exploring JavaScript" Ch. 27 and Ch. 30, `this` works as follows: in methods, `this` refers to the receiver of the method call. In ordinary functions used as real functions (strict mode), `this` is `undefined`. Arrow functions do not have their own `this` -- they resolve it lexically from the surrounding scope. This distinction is called dynamic `this` vs. lexical `this`.

# Prerequisites

- Ordinary function
- Arrow function

# Key Properties

1. `this` is an implicit parameter, not a variable.
2. Dynamic `this` (ordinary functions): set by the call site (method call sets to receiver, function call sets to `undefined` in strict mode).
3. Lexical `this` (arrow functions): inherited from enclosing scope, like a regular variable.
4. In `new` calls: `this` refers to the newly created instance.
5. Top-level `this`: `undefined` in modules, `globalThis` in scripts.

# Construction / Recognition

```js
const obj = {
  name: 'Jill',
  someMethod() {
    // Dynamic this = obj
    const arrowFunc = () => {
      // Lexical this = also obj
    };
    function ordinaryFunc() {
      // Dynamic this = undefined (function call)
    }
  },
};
```

# Context & Application

Understanding `this` is critical for methods, callbacks inside methods, and event handlers. The primary reason arrow functions were introduced was to provide lexical `this` for callbacks inside methods.

# Examples

From the source text (Ch. 27, section 27.3.3):

```js
const jill = {
  name: 'Jill',
  someMethod() {
    function ordinaryFunc() {
      // this.name throws: this is undefined
    }
    ordinaryFunc();

    const arrowFunc = () => {
      assert.equal(this.name, 'Jill'); // works!
    };
    arrowFunc();
  },
};
jill.someMethod();
```

# Relationships

## Builds Upon
- **Ordinary Function** -- ordinary functions have dynamic `this`
- **Arrow Function** -- arrow functions have lexical `this`

## Enables
- **Method Definition** -- methods use `this` to access the receiver
- **Extracting Methods** -- understanding `this` prevents pitfalls

## Related
- **Function.prototype.call()** -- makes `this` explicit
- **Function.prototype.bind()** -- fixes `this` permanently

# Common Errors

- **Error**: Using an ordinary function as a callback inside a method and expecting `this` to refer to the method's object.
  **Correction**: Use an arrow function for the callback, which inherits `this` lexically.

- **Error**: Extracting a method and calling it as a function, losing `this`.
  **Correction**: Use `.bind()` or an arrow wrapper when extracting methods.

# Common Confusions

- **Confusion**: Thinking `this` always refers to the enclosing object.
  **Clarification**: `this` in ordinary functions is determined by how the function is called, not where it is defined. Only arrow functions inherit `this` from definition context.

# Source Reference

Chapter 27: Callable values, Section 27.3.3, lines 632-735.
Chapter 30: Objects, Section 30.6, lines 1166-1574.

# Verification Notes

- Definition source: direct
- Confidence rationale: Extensive treatment across two chapters
- Cross-reference status: verified across Ch. 27 and Ch. 30
