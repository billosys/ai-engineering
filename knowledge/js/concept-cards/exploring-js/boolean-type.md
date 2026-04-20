---
# === CORE IDENTIFICATION ===
concept: Boolean Type
slug: boolean-type

# === CLASSIFICATION ===
category: primitive-types
subcategory: booleans
tier: foundational

# === PROVENANCE ===
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Booleans"
chapter_number: 17
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "boolean"
  - "bool"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - converting-to-boolean
  - falsy-and-truthy-values
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I convert between JavaScript types (string, number, boolean)?"
  - "What distinguishes primitive values from objects?"
---

# Quick Definition

The boolean type is a primitive type comprising exactly two values: `false` and `true`, used for logical operations and conditional control flow.

# Core Definition

"The primitive type *boolean* comprises two values -- `false` and `true`." The `typeof` operator returns `'boolean'` for both values (Ch. 17, introduction).

# Prerequisites

Foundational concept with no prerequisites.

# Key Properties

1. Two values: `false` and `true`
2. `typeof false` and `typeof true` return `'boolean'`
3. Primitive type (not an object)

# Construction / Recognition

```js
> typeof false
'boolean'
> typeof true
'boolean'
```

# Context & Application

Booleans are used as conditions in `if` statements, `while` loops, `do-while` loops, and ternary expressions. JavaScript often implicitly converts other types to booleans in these contexts.

# Examples

From the source text:

```js
> typeof false
'boolean'
> typeof true
'boolean'
```

# Relationships

## Builds Upon
- No prerequisites

## Enables
- **converting-to-boolean** — converting other types to boolean
- **falsy-and-truthy-values** — classification of values by their boolean conversion

## Related
- **conditional-operator** — uses boolean conditions

## Contrasts With
- None

# Common Errors

- **Error**: Using `new Boolean()` to create booleans
  **Correction**: Never use `new Boolean()` -- it creates a Boolean object (which is truthy even for `new Boolean(false)`). Use literal `true`/`false` or `Boolean()` as a function.

# Common Confusions

- **Confusion**: Thinking `Boolean` objects and boolean primitives are the same
  **Clarification**: `new Boolean(false)` creates a truthy object, not a falsy primitive.

# Source Reference

Chapter 17: Booleans, introduction, lines 41-49.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit definition
- Cross-reference status: verified
