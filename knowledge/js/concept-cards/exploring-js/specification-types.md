---
# === CORE IDENTIFICATION ===
concept: ECMAScript Specification Types
slug: specification-types

# === CLASSIFICATION ===
category: types-values
subcategory: type-system
tier: foundational

# === PROVENANCE ===
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Values"
chapter_number: 14
pdf_page: null
section: "14.3 The types of the language specification"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - eight types
  - language types

# === TYPED RELATIONSHIPS ===
prerequisites:
  - javascript-types
extends:
  - javascript-types
related:
  - typeof-operator
  - primitive-values
  - objects-overview
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are primitive values vs. objects in JavaScript?"
  - "What is the `typeof` operator and what does it return for each type?"
---

# Quick Definition

The ECMAScript specification defines exactly eight types: `undefined`, `null`, `boolean`, `number`, `bigint`, `string`, `symbol`, and `object`. The first seven are primitive types; the last is the object type.

# Core Definition

"The ECMAScript specification only knows a total of eight types." (Ch. 14, &sect;14.3):
- `undefined` with the only element `undefined`
- `null` with the only element `null`
- `boolean` with elements `false` and `true`
- `number`, the type of all numbers (e.g., `-123`, `3.141`)
- `bigint`, the type of all big integers (e.g., `-123n`)
- `string`, the type of all strings (e.g., `'abc'`)
- `symbol`, the type of all symbols (e.g., `Symbol('My Symbol')`)
- `object`, the type of all objects

# Prerequisites

- **javascript-types** -- specification types formalize the type system

# Key Properties

1. Exactly eight types in the specification
2. Seven primitive types + one object type
3. `undefined` and `null` are singleton types (one element each)
4. `boolean` has exactly two elements
5. `object` (lowercase) is different from `Object` (the class)
6. Names use TypeScript conventions, not spec names

# Construction / Recognition

Each type is identifiable via `typeof` (with known quirks).

# Context & Application

These eight types are the foundation of JavaScript's type system. All values belong to exactly one of these types.

# Examples

From the source text (Ch. 14, &sect;14.3):
- `undefined`: only element is `undefined`
- `null`: only element is `null`
- `boolean`: `false` and `true`
- `number`: `-123`, `3.141`
- `bigint`: `-123n`
- `string`: `'abc'`
- `symbol`: `Symbol('My Symbol')`
- `object`: all objects

# Relationships

## Builds Upon
- **javascript-types** -- formalizes the type system

## Enables
- **typeof-operator** -- returns the type of a value
- **primitive-values** -- the seven primitive types
- **objects-overview** -- the object type

## Related
- No additional

## Contrasts With
- No direct contrast

# Common Errors

- **Error**: Thinking there are more than eight types.
  **Correction**: The spec defines exactly eight. Classes create subtypes of `object`, not new spec types.

# Common Confusions

- **Confusion**: Confusing `object` (spec type, lowercase) with `Object` (class, uppercase).
  **Clarification**: `object` is the spec type for all objects; `Object` is the base class for most (but not all) objects.

# Source Reference

Chapter 14: Values, Section 14.3, lines 103-118.

# Verification Notes

- Definition source: direct from source
- Confidence rationale: Complete enumeration of all eight types
- Cross-reference status: verified
