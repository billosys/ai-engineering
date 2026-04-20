---
concept: Function.prototype.apply()
slug: function-apply-method
category: functions
subcategory: function-methods
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Callable values"
chapter_number: 27
pdf_page: null
section: "27.7.2 The function method `.apply()`"
extraction_confidence: high
aliases:
  - ".apply()"
  - "Function.apply"
prerequisites:
  - function-call-method
extends: []
related:
  - function-call-method
  - spread-into-function-calls
contrasts_with:
  - function-call-method
answers_questions:
  - "How do I call a function with `this` and an array of arguments?"
---

# Quick Definition

`.apply()` invokes a function with an explicitly specified `this` value and arguments provided as an array (or array-like object).

# Core Definition

As described in "Exploring JavaScript" Ch. 27, `.apply()` is like `.call()` but takes arguments as an array: `func.apply(thisValue, [arg1, arg2])`. In modern JavaScript, spreading (`func.call(thisValue, ...args)`) is often preferred.

# Prerequisites

- Function.prototype.call()

# Key Properties

1. Arguments provided as an array (second parameter).
2. First parameter is the `this` value.
3. Largely superseded by spread syntax in modern code.

# Construction / Recognition

```js
func.apply(thisValue, [arg1, arg2, arg3]);
// Modern equivalent:
func.call(thisValue, ...args);
```

# Context & Application

Historically used to pass arrays as arguments. In modern JavaScript, spread syntax is preferred.

# Examples

```js
Math.max.apply(null, [1, 5, 3]); // 5
// Modern equivalent:
Math.max(...[1, 5, 3]);          // 5
```

# Relationships

## Contrasts With
- **Function.prototype.call()** -- `.call()` takes individual args; `.apply()` takes an array

## Related
- **Spread Into Function Calls** -- modern replacement for `.apply()` use cases

# Source Reference

Chapter 27: Callable values, Section 27.7.2.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit definition with modern alternative
- Cross-reference status: verified
