---
# === CORE IDENTIFICATION ===
concept: TypeScript and Static Typing
slug: typescript-static-typing

# === CLASSIFICATION ===
category: language-background
subcategory: ecosystem
tier: foundational

# === PROVENANCE ===
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "The nature of JavaScript"
chapter_number: 4
pdf_page: null
section: "4.3 Tips for getting started with JavaScript"

# === CONFIDENCE ===
extraction_confidence: medium

# === VARIANTS ===
aliases:
  - TypeScript
  - TS
  - static typing for JavaScript

# === TYPED RELATIONSHIPS ===
prerequisites:
  - dynamic-language
extends: []
related:
  - javascript-ecosystem
contrasts_with:
  - dynamic-language

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What does it mean that JavaScript is a dynamic language?"
---

# Quick Definition

TypeScript is a superset of JavaScript that adds optional static typing, allowing type errors to be caught at compile time rather than runtime.

# Core Definition

"We can add static typing, via TypeScript." (Ch. 3, &sect;3.2.3). "You can statically type JavaScript via TypeScript." (Ch. 4, &sect;4.3). TypeScript addresses JavaScript's dynamic typing by adding optional type annotations that are checked at compile time. It compiles to plain JavaScript.

# Prerequisites

- **dynamic-language** -- TypeScript adds static typing to a dynamic language

# Key Properties

1. Superset of JavaScript (all JS is valid TS)
2. Adds optional static type annotations
3. Type checking at compile time
4. Compiles to plain JavaScript
5. Mentioned throughout the book as a recommended tool

# Construction / Recognition

TypeScript files use `.ts` extension. Type annotations use colon syntax: `function add(a: number, b: number): number`.

# Context & Application

TypeScript is increasingly standard in professional JavaScript development. The book uses TypeScript notation for some API signatures.

# Examples

From the source text (Ch. 10, &sect;10.2.1):
```typescript
console.log(...values: Array<any>): void
console.log(pattern: string, ...values: Array<any>): void
```

# Relationships

## Builds Upon
- **dynamic-language** -- TypeScript adds static types to JavaScript

## Enables
- Compile-time error detection
- Better IDE support and refactoring

## Related
- **javascript-ecosystem** -- TypeScript is part of the ecosystem

## Contrasts With
- **dynamic-language** -- TypeScript adds what dynamic JavaScript lacks

# Common Errors

- **Error**: Thinking TypeScript replaces JavaScript.
  **Correction**: TypeScript compiles to JavaScript; it adds types on top of existing JS.

# Common Confusions

- **Confusion**: Thinking TypeScript and JavaScript are different languages.
  **Clarification**: TypeScript is a superset; all JavaScript is valid TypeScript.

# Source Reference

Chapter 3: Section 3.2.3, line 134. Chapter 4: Section 4.3, line 123.

# Verification Notes

- Definition source: synthesized from multiple mentions
- Confidence rationale: Medium; not deeply covered but repeatedly referenced
- Cross-reference status: verified across multiple chapters
