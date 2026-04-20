---
concept: Nested Destructuring
slug: nested-destructuring
category: destructuring
subcategory: null
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Destructuring"
chapter_number: 40
pdf_page: null
section: "40.12 Nested destructuring"
extraction_confidence: high
aliases:
  - "deep destructuring"
prerequisites:
  - object-destructuring
  - array-destructuring
extends: []
related: []
contrasts_with: []
answers_questions:
  - "How do I use destructuring to extract values from objects and arrays?"
---

# Quick Definition

Nested destructuring places patterns inside other patterns as assignment targets, enabling extraction from deeply nested structures in a single statement.

# Core Definition

Patterns can be used as assignment targets inside other patterns, enabling nesting to arbitrary depths. For example, `[, {first}]` contains a nested object pattern at array index 1. Nested patterns can become difficult to understand, so they are best used in moderation.

# Prerequisites

- **object-destructuring** -- nesting uses object patterns
- **array-destructuring** -- nesting uses array patterns

# Key Properties

1. Patterns can contain other patterns at any depth
2. Array and object patterns can be mixed
3. Should be used in moderation for readability
4. Each nested pattern is an assignment target, not a variable

# Construction / Recognition

```js
const arr = [
  {first: 'Jane', last: 'Bond'},
  {first: 'Lars', last: 'Croft'},
];
const [, {first}] = arr;
// first === 'Lars'
```

# Context & Application

Nested destructuring is useful for extracting specific fields from complex API responses or data structures, but should be kept shallow for readability.

# Examples

```js
const arr = [
  {first: 'Jane', last: 'Bond'},
  {first: 'Lars', last: 'Croft'},
];
const [, {first}] = arr;
assert.equal(first, 'Lars');

// Deeply nested
const obj = {a: {b: {c: 42}}};
const {a: {b: {c}}} = obj;
assert.equal(c, 42);
```

(Chapter 40, Section 40.12, lines 718-740)

# Relationships

## Builds Upon
- **object-destructuring** -- object patterns used as nested targets
- **array-destructuring** -- array patterns used as nested targets

## Enables
- Extracting deeply nested values concisely

## Related
- None

## Contrasts With
- None

# Common Errors

- **Error**: Deeply nesting patterns making code unreadable.
  **Correction**: Extract intermediate values into variables for clarity. Rauschmayer advises "best used in moderation."

# Common Confusions

- **Confusion**: A nested pattern creates intermediate variables.
  **Clarification**: In `{a: {b}}`, only `b` is a variable. `a` is a property key for navigating, not a declared variable.

# Source Reference

Chapter 40: Destructuring, Section 40.12, lines 718-740.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly defined with warning about moderation
- Cross-reference status: verified
