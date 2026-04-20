---
# === CORE IDENTIFICATION ===
concept: Type Casting
slug: type-casting

# === CLASSIFICATION ===
category: type-system
subcategory: type-conversion
tier: foundational

# === PROVENANCE ===
source: "Deep JavaScript"
source_slug: deep-js
authors: "Dr. Axel Rauschmayer"
chapter: "Type coercion in JavaScript"
chapter_number: 2
section: "2.6 Glossary: terms related to type conversion"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - casting

# === TYPED RELATIONSHIPS ===
prerequisites:
  - type-coercion
  - explicit-type-conversion
extends: []
related:
  - type-coercion
  - explicit-type-conversion
contrasts_with:
  - type-coercion
  - explicit-type-conversion

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is type coercion in JavaScript?"
---

# Quick Definition

Type casting is a language-dependent term for type conversion; in Java it means explicit checked type conversion, but JavaScript does not formally use the term.

# Core Definition

As defined in "Deep JavaScript" (Ch 2, Section 2.6): "What *type casting* is, depends on the programming language. For example, in Java, it is explicit checked type conversion." The source distinguishes type casting from the JavaScript-specific terms "type coercion" (implicit) and "explicit type conversion" (deliberate use of conversion functions).

# Prerequisites

- **Type coercion** — Understanding the broader conversion taxonomy.
- **Explicit type conversion** — The JavaScript equivalent concept.

# Key Properties

1. Language-dependent meaning.
2. In Java: explicit checked type conversion.
3. JavaScript does not formally use this term in its specification.
4. Often informally used in JavaScript contexts to mean explicit conversion.

# Construction / Recognition

## To Construct/Create:
1. Not applicable in JavaScript specification terms.
2. Informally: `Number(x)`, `String(x)`, etc. are sometimes called "casts."

## To Identify/Recognize:
1. The term "type casting" used in JavaScript discussions usually means explicit type conversion.

# Context & Application

The term appears frequently in discussions about JavaScript but is not part of the ECMAScript specification vocabulary. Understanding the distinction helps when reading cross-language discussions about type systems.

# Examples

**Example 1** (Ch 2): From the glossary — in Java, casting is explicit and checked:
```java
// Java type casting (not JavaScript):
int x = (int) 3.14;  // explicit checked conversion
```

# Relationships

## Builds Upon
- **Type coercion** — Part of the same taxonomy.
- **Explicit type conversion** — The JavaScript-specific equivalent.

## Enables
- **Cross-language understanding** — Helps clarify terminology across languages.

## Related
- **Type coercion** — Implicit conversion (JavaScript's main mechanism).
- **Explicit type conversion** — Deliberate conversion (JavaScript's equivalent to casting).

## Contrasts With
- **Type coercion** — Coercion is implicit; casting is explicit (in Java).
- **Explicit type conversion** — Broader than casting; includes unchecked conversions.

# Common Errors

- **Error**: Assuming "type casting" has a precise meaning in JavaScript.
  **Correction**: JavaScript does not define "type casting." Use "explicit type conversion" or "type coercion" for precision.

# Common Confusions

- **Confusion**: Type casting, type coercion, and type conversion are all the same.
  **Clarification**: Type conversion is the umbrella term. Coercion is implicit conversion. Casting is language-dependent (explicit checked in Java). They are related but distinct concepts.

# Source Reference

Chapter 2: Type coercion in JavaScript, Section 2.6, lines 1055-1057.

# Verification Notes

- Definition source: direct (quoted from glossary)
- Confidence rationale: Explicit definition provided in glossary
- Cross-reference status: verified
