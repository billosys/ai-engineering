---
# === CORE IDENTIFICATION ===
concept: History of Undefined and Null
slug: history-of-undefined-and-null

# === CLASSIFICATION ===
category: primitive-types
subcategory: non-values
tier: foundational

# === PROVENANCE ===
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "The non-values undefined and null"
chapter_number: 16
pdf_page: null
section: "The history of undefined and null"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - undefined-value
  - null-value
extends: []
related: []
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is `undefined` and how does it differ from `null`?"
  - "What distinguishes `null` from `undefined`?"
---

# Quick Definition

JavaScript has two non-values because it borrowed `null` from Java (for "not an object") but needed `undefined` as a separate value meaning "neither an object nor a primitive value" for uninitialized storage locations.

# Core Definition

In Java, initialization values depend on static type: object types initialize to `null`, primitive types to type-specific values (e.g., `int` to `0`). JavaScript borrowed `null` from Java to mean "not an object." But since JavaScript storage locations can hold both objects and primitives, it needed an initialization value meaning "neither an object nor a primitive value" -- hence `undefined` was introduced (Ch. 16, Section 16.6).

# Prerequisites

- **undefined-value** -- one of the two non-values
- **null-value** -- the other non-value

# Key Properties

1. `null` borrowed from Java meaning "not an object"
2. `undefined` created for JavaScript's dynamic typing needs
3. JavaScript storage locations can hold any type (unlike Java's static typing)
4. `undefined` means "neither an object nor a primitive value"

# Construction / Recognition

Historical context explains the design decision; no syntax required.

# Context & Application

Understanding the history explains why JavaScript has two seemingly redundant non-values and helps developers choose between them appropriately.

# Examples

From the source text:

```js
// null: "not an object" (from Java)
> Object.getPrototypeOf(Object.prototype)
null

// undefined: "not initialized" (JavaScript addition)
let myVar;
assert.equal(myVar, undefined);
```

# Relationships

## Builds Upon
- **undefined-value** — explains why it exists
- **null-value** — explains its Java origins

## Enables
- Informed choice between `undefined` and `null`

## Related
- None

## Contrasts With
- None

# Common Errors

- **Error**: None specific to history

# Common Confusions

- **Confusion**: Thinking having two non-values is a design flaw
  **Clarification**: While it adds complexity, each serves a distinct purpose rooted in JavaScript's design history.

# Source Reference

Chapter 16: The non-values undefined and null, Section 16.6, lines 479-495.

# Verification Notes

- Definition source: direct
- Confidence rationale: Historical explanation provided by the author
- Cross-reference status: verified
