---
concept: Truthy and Falsy Values
slug: truthy-and-falsy-values
category: control-flow
subcategory: conditionals
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Control flow statements"
chapter_number: 25
pdf_page: null
section: "25.2 Conditions of control flow statements"
extraction_confidence: high
aliases:
  - "truthiness"
  - "falsiness"
  - "truthy"
  - "falsy"
prerequisites: []
extends: []
related:
  - if-statement
  - while-loop
contrasts_with: []
answers_questions:
  - "Which values are treated as false in JavaScript conditions?"
---

# Quick Definition

A falsy value evaluates to `false` when coerced to boolean; all other values are truthy. Control flow conditions (`if`, `while`, `do-while`) accept any truthy value, not just `true`.

# Core Definition

As described in "Exploring JavaScript" Ch. 25, control flow conditions only need to be truthy (equivalent to `true` when coerced to boolean). The complete list of falsy values is: `undefined`, `null`, `false`, `0`, `NaN`, `0n`, and `''`. All other values are truthy.

# Prerequisites

- Foundational concept with no prerequisites

# Key Properties

1. `if (value) {}` is equivalent to `if (Boolean(value) === true) {}`.
2. Exactly seven falsy values exist: `undefined`, `null`, `false`, `0`, `NaN`, `0n`, `''`.
3. All objects (including empty arrays and empty objects) are truthy.
4. Truthiness applies to `if`, `while`, `do-while`, ternary operator, and logical operators.

# Construction / Recognition

```js
if (value) { /* truthy branch */ }
if (!value) { /* falsy branch */ }
```

# Context & Application

Understanding truthiness is essential for idiomatic JavaScript conditionals, short-circuit evaluation, and default value patterns.

# Examples

From the source text (Ch. 25, section 25.2):

```js
// These two are equivalent:
if (value) {}
if (Boolean(value) === true) {}
```

# Relationships

## Enables
- **If Statement** -- conditions rely on truthiness
- **While Loop** -- loop condition uses truthiness

# Common Errors

- **Error**: Assuming `0` or `''` will be truthy because they are "real values."
  **Correction**: `0`, `''`, and `NaN` are all falsy despite being non-nullish.

# Common Confusions

- **Confusion**: Mixing up nullish (`null`/`undefined`) with falsy.
  **Clarification**: All nullish values are falsy, but not all falsy values are nullish (e.g., `0`, `''`, `false`, `NaN`, `0n`).

# Source Reference

Chapter 25: Control flow statements, Section 25.2, lines 190-212.

# Verification Notes

- Definition source: direct
- Confidence rationale: Exhaustive list of falsy values provided in source
- Cross-reference status: verified with section 17.2
