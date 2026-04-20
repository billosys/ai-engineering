---
concept: Function.prototype.bind()
slug: function-bind-method
category: functions
subcategory: function-methods
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Callable values"
chapter_number: 27
pdf_page: null
section: "27.7.3 The function method `.bind()`"
extraction_confidence: high
aliases:
  - ".bind()"
  - "Function.bind"
prerequisites:
  - this-keyword
  - function-call-method
extends: []
related:
  - function-call-method
  - extracting-methods
contrasts_with: []
answers_questions:
  - "How do I permanently fix `this` for a function?"
---

# Quick Definition

`.bind()` returns a new function with a permanently fixed `this` value and optionally pre-filled arguments (partial application).

# Core Definition

As described in "Exploring JavaScript" Ch. 27, `someFunc.bind(thisValue, arg1, arg2)` returns a new function where `this` is always `thisValue` and the first arguments are pre-filled. This is essential when extracting methods from objects, as the extracted function would otherwise lose its `this` binding.

# Prerequisites

- The `this` keyword
- Function.prototype.call()

# Key Properties

1. Returns a new function with fixed `this`.
2. Can pre-fill arguments (partial application).
3. Each call creates a new function object.
4. Essential for extracting methods safely.

# Construction / Recognition

```js
const boundFunc = obj.method.bind(obj);
boundFunc(); // this === obj
```

# Context & Application

Used when passing methods as callbacks (e.g., event handlers) to ensure `this` remains correct.

# Examples

From the source text (Ch. 30, section 30.6.4):

```js
const jane = {
  first: 'Jane',
  says(text) {
    return `${this.first} says "${text}"`;
  },
};
const func = jane.says.bind(jane, 'hello');
assert.equal(func(), 'Jane says "hello"');
```

# Relationships

## Related
- **Function.prototype.call()** -- `.call()` sets `this` for one invocation; `.bind()` creates a permanent binding
- **Extracting Methods** -- `.bind()` solves the method extraction pitfall

# Common Errors

- **Error**: Forgetting that each `.bind()` call creates a new function, making removal of event listeners difficult.
  **Correction**: Store the bound function in a variable if you need to remove it later.

# Source Reference

Chapter 27: Callable values, Section 27.7.3.
Chapter 30: Objects, Section 30.6.4-30.6.5, lines 1282-1402.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit definition with practical usage
- Cross-reference status: verified across Ch. 27 and Ch. 30
