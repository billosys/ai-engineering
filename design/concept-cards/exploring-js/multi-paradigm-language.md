---
# === CORE IDENTIFICATION ===
concept: Multi-Paradigm Language
slug: multi-paradigm-language

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
  - OOP and FP support
  - multi-paradigm programming

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - javascript-influences
  - dynamic-language
  - closures
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What programming paradigms does JavaScript support?"
---

# Quick Definition

JavaScript supports both object-oriented programming (mutable state, objects, inheritance, classes) and functional programming (first-class functions, closures, partial application).

# Core Definition

JavaScript has both "functional programming features: first-class functions, closures, partial application via `bind()`, etc." and "object-oriented features: mutable state, objects, inheritance, classes, etc." (Ch. 4, &sect;4.2). This multi-paradigm nature stems from its diverse language influences.

# Prerequisites

Foundational concept with no prerequisites.

# Key Properties

1. Functional programming: first-class functions, closures, partial application via `bind()`
2. Object-oriented programming: mutable state, objects, inheritance, classes
3. The flexibility allows developers to choose the most appropriate paradigm per problem
4. C-family syntax provides familiar structure

# Construction / Recognition

Functional style: arrow functions, `.map()`, `.filter()`, closures. Object-oriented style: classes, `this`, inheritance via `extends`.

# Context & Application

Most modern JavaScript code blends both paradigms. React uses functional components with hooks; class-based patterns remain common in many frameworks.

# Examples

From the source text (Ch. 4, &sect;4.2):
- Functional: first-class functions, closures, `bind()` for partial application
- Object-oriented: mutable state, objects, inheritance, classes

# Relationships

## Builds Upon
- No prerequisites

## Enables
- **closures** -- functional programming feature
- **classes** -- object-oriented feature

## Related
- **javascript-influences** -- Scheme (FP) and Self (OOP) influenced these paradigms

## Contrasts With
- No direct contrast

# Common Errors

- **Error**: Trying to use JavaScript as purely one paradigm.
  **Correction**: JavaScript is designed to blend paradigms; effective code often uses both.

# Common Confusions

- **Confusion**: Thinking classes and functional programming are incompatible in JavaScript.
  **Clarification**: JavaScript freely mixes both; classes can contain methods using closures and higher-order functions.

# Source Reference

Chapter 4: The nature of JavaScript, Section 4.2, lines 46-79.

# Verification Notes

- Definition source: direct from source
- Confidence rationale: Explicitly stated features for both paradigms
- Cross-reference status: verified
