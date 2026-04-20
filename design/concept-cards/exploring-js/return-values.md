---
concept: Return Values
slug: return-values
category: functions
subcategory: null
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Callable values"
chapter_number: 27
pdf_page: null
section: "27.5 Returning values from functions and methods"
extraction_confidence: high
aliases:
  - "return statement"
  - "implicit return"
prerequisites:
  - ordinary-function
extends: []
related:
  - arrow-function
contrasts_with: []
answers_questions:
  - "What happens if a function doesn't return a value?"
---

# Quick Definition

The `return` statement exits a function and provides a value to the caller; if omitted or used without a value, the function returns `undefined`.

# Core Definition

As described in "Exploring JavaScript" Ch. 27, the `return` statement explicitly returns a value from a function. If execution reaches the end of a function without an explicit `return`, JavaScript returns `undefined`. Arrow functions with expression bodies implicitly return the expression's value.

# Prerequisites

- Ordinary function

# Key Properties

1. `return value` exits and provides a value.
2. No explicit return means `undefined` is returned.
3. Arrow functions with expression bodies: `() => expr` returns `expr`.
4. Applies to both functions and methods.

# Construction / Recognition

```js
function explicit() { return 123; }
function implicit() { /* no return */ }
assert.equal(implicit(), undefined);

const arrow = () => 123; // implicit return
```

# Context & Application

Understanding implicit `undefined` return helps debug unexpected values and write clearer code.

# Examples

From the source text (Ch. 27, section 27.5):

```js
function noReturn() { /* No explicit return */ }
assert.equal(noReturn(), undefined);
```

# Relationships

## Related
- **Arrow Function** -- expression body provides implicit return

# Source Reference

Chapter 27: Callable values, Section 27.5, lines 1091-1131.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit behavior documented
- Cross-reference status: verified
