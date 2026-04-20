---
concept: Function.prototype.call()
slug: function-call-method
category: functions
subcategory: function-methods
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Callable values"
chapter_number: 27
pdf_page: null
section: "27.7.1 The function method `.call()`"
extraction_confidence: high
aliases:
  - ".call()"
  - "Function.call"
prerequisites:
  - this-keyword
extends: []
related:
  - function-apply-method
  - function-bind-method
contrasts_with:
  - function-apply-method
answers_questions:
  - "How do I explicitly set `this` when calling a function?"
---

# Quick Definition

`.call()` invokes a function with an explicitly specified `this` value and individual arguments.

# Core Definition

As described in "Exploring JavaScript" Ch. 27, `someFunc.call(thisValue, arg1, arg2, arg3)` is equivalent to `someFunc(arg1, arg2, arg3)` but allows specifying `this`. It makes the normally implicit `this` parameter explicit.

# Prerequisites

- The `this` keyword

# Key Properties

1. First argument is the `this` value.
2. Remaining arguments are passed individually.
3. Makes implicit `this` explicit.
4. A method call `obj.method(a, b)` is equivalent to `obj.method.call(obj, a, b)`.

# Construction / Recognition

```js
func.call(thisValue, arg1, arg2);
```

# Context & Application

Used for borrowing methods from other objects, invoking functions with a specific `this`, and understanding method dispatch.

# Examples

From the source text (Ch. 27, section 27.7.1):

```js
obj.someMethod('a', 'b')
// equivalent to:
obj.someMethod.call(obj, 'a', 'b');
```

# Relationships

## Related
- **Function.prototype.apply()** -- like `.call()` but takes an array of arguments
- **Function.prototype.bind()** -- returns a new function with fixed `this`

## Contrasts With
- **Function.prototype.apply()** -- `.call()` takes individual args; `.apply()` takes an array

# Source Reference

Chapter 27: Callable values, Section 27.7.1, lines 1478-1499.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit equivalence shown
- Cross-reference status: verified
