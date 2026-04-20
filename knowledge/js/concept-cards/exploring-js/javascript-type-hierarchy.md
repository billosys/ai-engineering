---
# === CORE IDENTIFICATION ===
concept: JavaScript Type Hierarchy
slug: javascript-type-hierarchy

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
section: "14.2 JavaScript's type hierarchy"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - type tree

# === TYPED RELATIONSHIPS ===
prerequisites:
  - javascript-types
extends:
  - javascript-types
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

JavaScript's type hierarchy divides all values into two categories: primitive values (seven types) and objects. Objects are further subdivided by classes, with virtually all objects being instances of `Object`.

# Core Definition

JavaScript's type hierarchy (Ch. 14, &sect;14.2) shows: "JavaScript distinguishes two kinds of values: primitive values and objects." The hierarchy includes seven primitive types and the object type. Objects are further categorized by classes: "Some objects are not instances of the class `Object`. However, such objects are rare. Virtually all objects we'll encounter are indeed instances of `Object`."

# Prerequisites

- **javascript-types** -- the foundation of the hierarchy

# Key Properties

1. Top-level split: primitives vs. objects
2. Seven primitive types beneath the primitive branch
3. Object type subdivided by classes (Array, Function, RegExp, etc.)
4. Virtually all objects are instances of Object
5. Rare exceptions: some objects are not Object instances

# Construction / Recognition

The hierarchy is depicted in Figure 14.1 of the source text, showing a tree with "any" at the root, branching into primitive types and the object type.

# Context & Application

Understanding the type hierarchy helps with type checking (`typeof` for primitives, `instanceof` for objects) and understanding inheritance.

# Examples

From the source text (Ch. 14, &sect;14.2):
- Primitives: undefined, null, boolean, number, bigint, string, symbol
- Objects: plain objects, Arrays, Functions, RegExps, Dates, etc.
- "Some objects are not instances of the class `Object`" (rare)

# Relationships

## Builds Upon
- **javascript-types** -- the foundation

## Enables
- Correct type checking strategies

## Related
- **specification-types** -- the formal eight types
- **primitive-values** -- one branch of the hierarchy
- **objects-overview** -- the other branch

## Contrasts With
- No direct contrast

# Common Errors

- **Error**: Assuming all objects are instances of Object.
  **Correction**: Virtually all are, but objects created with `Object.create(null)` are not.

# Common Confusions

- **Confusion**: Thinking JavaScript has many types.
  **Clarification**: The specification defines only eight types. Classes create subtypes of `object`, but they're not separate spec types.

# Source Reference

Chapter 14: Values, Section 14.2, lines 78-101.

# Verification Notes

- Definition source: direct from source
- Confidence rationale: Diagram-referenced, explicit hierarchy description
- Cross-reference status: verified
