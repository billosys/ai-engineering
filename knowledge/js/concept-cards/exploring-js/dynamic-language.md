---
# === CORE IDENTIFICATION ===
concept: Dynamic Language
slug: dynamic-language

# === CLASSIFICATION ===
category: language-background
subcategory: design-philosophy
tier: foundational

# === PROVENANCE ===
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "The nature of JavaScript"
chapter_number: 4
pdf_page: null
section: "4.2 The nature of JavaScript"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - dynamically typed language
  - dynamic typing

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - javascript-influences
  - multi-paradigm-language
  - type-coercion
contrasts_with:
  - typescript-static-typing

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What does it mean that JavaScript is a dynamic language?"
---

# Quick Definition

JavaScript is both a dynamic language (objects can be changed at runtime) and dynamically typed (variables don't have fixed types and can hold any value).

# Core Definition

JavaScript is described as dynamic in two senses: "It is a dynamic language: most objects can be changed in various ways at runtime, objects can be created directly, etc." and "It is a dynamically typed language: variables don't have fixed static types and you can assign any value to a given (mutable) variable." (Ch. 4, &sect;4.2).

# Prerequisites

Foundational concept with no prerequisites.

# Key Properties

1. Objects can be modified at runtime (properties added, removed, changed)
2. Variables have no fixed static types
3. Any value can be assigned to any mutable variable
4. Objects can be created directly via literals (no class required)
5. JavaScript engines optimize dynamic features under the hood (e.g., Arrays stored contiguously)

# Construction / Recognition

Dynamic typing is visible when a variable holds different types at different times, or when object properties are added freely at runtime.

# Context & Application

Dynamic typing provides flexibility but can lead to runtime errors. TypeScript adds optional static typing on top of JavaScript. Linters like ESLint help catch type-related issues.

# Examples

From the source text (Ch. 4, &sect;4.2):
- Objects can be changed at runtime: properties added/removed
- Variables accept any value type
- JavaScript Arrays are dictionaries in principle but engines optimize contiguous storage

# Relationships

## Builds Upon
- No prerequisites

## Enables
- **type-coercion** -- dynamic typing leads to implicit conversions
- **typeof-operator** -- needed to check types at runtime

## Related
- **multi-paradigm-language** -- dynamic nature supports multiple paradigms

## Contrasts With
- **static-typing** -- TypeScript adds static types to JavaScript

# Common Errors

- **Error**: Assuming dynamic typing means types don't exist.
  **Correction**: Values always have types; it's the variables that don't have fixed types.

# Common Confusions

- **Confusion**: Conflating "dynamic language" with "dynamically typed."
  **Clarification**: Dynamic language means runtime modifiability; dynamically typed means variables lack fixed types. JavaScript is both.

# Source Reference

Chapter 4: The nature of JavaScript, Section 4.2, lines 46-79.

# Verification Notes

- Definition source: direct from source
- Confidence rationale: Explicitly defined with both senses distinguished
- Cross-reference status: verified
