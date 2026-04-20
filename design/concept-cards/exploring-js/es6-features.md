---
# === CORE IDENTIFICATION ===
concept: ES6 Feature Overview
slug: es6-features

# === CLASSIFICATION ===
category: language-background
subcategory: evolution
tier: foundational

# === PROVENANCE ===
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "New JavaScript features"
chapter_number: 6
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: medium

# === VARIANTS ===
aliases:
  - ECMAScript 2015 features
  - ES2015 features

# === TYPED RELATIONSHIPS ===
prerequisites:
  - ecmascript-versions
extends: []
related:
  - ecmascript-standard
  - annual-release-features
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What were the major features introduced in ES6?"
---

# Quick Definition

ES6 (ECMAScript 2015) was the largest single update to JavaScript, introducing `let`/`const`, classes, modules, arrow functions, destructuring, template literals, generators, Promises, and much more.

# Core Definition

ES6 was published in June 2015 and was "a large update that fulfilled many of the promises of ECMAScript 4" (Ch. 5, &sect;5.3). The chapter on new features notes that "ES2016 was the first truly incremental release of ECMAScript -- which is why ES6 has too many features to list" (Ch. 6, introduction). Key ES6 features include: `let`/`const`, classes, modules, arrow functions, destructuring, template literals, generators, Promises, default parameters, rest/spread operators, iterators, `Symbol`, `Map`/`Set`, and `Proxy`.

# Prerequisites

- **ecmascript-versions** -- ES6's place in the version timeline

# Key Properties

1. Published June 2015; the largest single update
2. Introduced block-scoped variables (`let`, `const`)
3. Added classes as syntactic sugar for prototypal inheritance
4. Built-in module system (ESM)
5. Arrow functions from CoffeeScript influence
6. Destructuring from Lisp influence
7. Template literals from E language influence
8. Too many features to list -- covered in dedicated chapters

# Construction / Recognition

ES6 features are ubiquitous in modern JavaScript. Code using `let`, `const`, `=>`, `class`, `import`/`export`, and template literals is ES6+.

# Context & Application

ES6 is the dividing line between "old" and "modern" JavaScript. Most modern JavaScript education starts from ES6 features.

# Examples

From the source text (Ch. 5, &sect;5.3; Ch. 6):
- `let` and `const` replaced `var`
- Classes replaced `function`/`.prototype` patterns
- Built-in modules replaced CommonJS/AMD
- Arrow functions: `(a, b) => a + b`

# Relationships

## Builds Upon
- **ecmascript-versions** -- ES6 in the version timeline

## Enables
- **let-declaration** -- introduced in ES6
- **const-declaration** -- introduced in ES6
- **strict-mode** -- implicitly on in modules and classes (ES6)

## Related
- **annual-release-features** -- the post-ES6 incremental model

## Contrasts With
- No direct contrast

# Common Errors

- **Error**: Assuming all ES6 features are equally well-supported everywhere.
  **Correction**: Check compatibility tables; some features required years for full browser support.

# Common Confusions

- **Confusion**: Thinking ES6 and ES2015 are different things.
  **Clarification**: ES6 is the colloquial name for the version officially named ECMAScript 2015.

# Source Reference

Chapter 5: Section 5.3, lines 110-112. Chapter 6: introduction, lines 39-49.

# Verification Notes

- Definition source: synthesized from Ch. 5 and Ch. 6 introductory text
- Confidence rationale: Medium because the detailed feature list is referenced rather than enumerated in these chapters
- Cross-reference status: verified
