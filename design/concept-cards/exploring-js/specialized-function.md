---
concept: Specialized Function
slug: specialized-function
category: functions
subcategory: function-types
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Callable values"
chapter_number: 27
pdf_page: null
section: "27.3 Specialized functions"
extraction_confidence: high
aliases:
  - "single-purpose function"
prerequisites:
  - ordinary-function
extends: []
related:
  - arrow-function
  - class-declaration
contrasts_with:
  - ordinary-function
answers_questions:
  - "What is a specialized function in JavaScript?"
---

# Quick Definition

Specialized functions (ES6) are single-purpose versions of ordinary functions: arrow functions (real functions only), methods (methods only), and classes (constructors only).

# Core Definition

As described in "Exploring JavaScript" Ch. 27, JavaScript has two categories of functions: ordinary functions (multi-role) and specialized functions (single-role). Specialized functions were added in ES6. Arrow functions can only be real functions. Methods can only be methods. Classes can only be constructors. Despite specialization, all are still categorized as functions (`instanceof Function` is `true`).

# Prerequisites

- Ordinary function

# Key Properties

1. Introduced in ES6.
2. Three kinds: arrow function, method, class.
3. Each is restricted to exactly one role.
4. All are still `instanceof Function`.
5. Recommended over ordinary functions for their specialized roles.

# Construction / Recognition

```js
// Arrow function (real function only)
const arrow = () => 123;

// Method (method only)
const obj = { myMethod() { return 'abc'; } };

// Class (constructor only)
class MyClass {}
```

# Context & Application

The recommendation is to prefer specialized functions over ordinary functions. Use arrow functions for real functions, method definitions for methods, and class declarations for constructors.

# Examples

From the source text (Ch. 27, section 27.3):

Capability table:
- Ordinary function: function call (this=undefined), method call, constructor call
- Arrow function: function call only (lexical this)
- Method: method call only (this=undefined if function-called)
- Class: constructor call only

# Relationships

## Builds Upon
- **Ordinary Function** -- specialized functions replace ordinary functions in specific roles

## Related
- **Arrow Function** -- specialized for real function role
- **Class Declaration** -- specialized for constructor role

## Contrasts With
- **Ordinary Function** -- ordinary functions can play all roles; specialized functions play one

# Common Errors

- **Error**: Trying to use a class as a regular function call.
  **Correction**: Classes can only be invoked with `new`.

# Common Confusions

- **Confusion**: Thinking specialized functions are a completely different type from ordinary functions.
  **Clarification**: All functions (ordinary and specialized) are instances of `Function`.

# Source Reference

Chapter 27: Callable values, Section 27.3, lines 340-514.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit taxonomy table in source
- Cross-reference status: verified
