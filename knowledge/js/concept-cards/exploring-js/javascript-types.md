---
# === CORE IDENTIFICATION ===
concept: JavaScript Types
slug: javascript-types

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
section: "14.1 What's a type?"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - JavaScript type system

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - specification-types
  - primitive-values
  - objects-overview
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are primitive values vs. objects in JavaScript?"
---

# Quick Definition

In JavaScript, types are sets of values. The language has eight specification types, broadly divided into two categories: primitive values and objects.

# Core Definition

"For this chapter, I consider types to be sets of values -- for example, the type `boolean` is the set { `false`, `true` }." (Ch. 14, &sect;14.1). JavaScript distinguishes two fundamental categories: primitive values and objects, forming a type hierarchy where all values are either primitives or objects.

# Prerequisites

Foundational concept with no prerequisites.

# Key Properties

1. Types are sets of values
2. Two fundamental categories: primitives and objects
3. Eight specification types total
4. Type hierarchy: all values are either primitives or objects
5. Classes subdivide the `object` type into subtypes

# Construction / Recognition

Types are checked via `typeof` (for primitives and functions) and `instanceof` (for objects/classes).

# Context & Application

The type system is the foundation for understanding JavaScript values, operators, and type coercion.

# Examples

From the source text (Ch. 14, &sect;14.1):
- `boolean` type = set { `false`, `true` }

# Relationships

## Builds Upon
- No prerequisites

## Enables
- **specification-types** -- the eight formal types
- **primitive-values** -- one of the two categories
- **objects-overview** -- the other category

## Related
- No additional

## Contrasts With
- No direct contrast

# Common Errors

- **Error**: Thinking JavaScript has no types because it's dynamically typed.
  **Correction**: JavaScript has types; variables don't have fixed types, but values always do.

# Common Confusions

- **Confusion**: Conflating "type" with "class."
  **Clarification**: Types are specification-level categories; classes create subtypes of `object`.

# Source Reference

Chapter 14: Values, Section 14.1, lines 71-77.

# Verification Notes

- Definition source: direct from source
- Confidence rationale: Explicit type-as-set definition
- Cross-reference status: verified
