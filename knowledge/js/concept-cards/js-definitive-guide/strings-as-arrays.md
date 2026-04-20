---
# === CORE IDENTIFICATION ===
concept: Strings as Arrays
slug: strings-as-arrays

# === CLASSIFICATION ===
category: arrays
subcategory: array-like objects
tier: intermediate

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Arrays"
chapter_number: 7
pdf_page: 196
section: "7.10 Strings as Arrays"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - array-fundamentals
  - array-like-objects
extends: []
related: []
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Can I use array bracket notation on strings?"
---

# Quick Definition

JavaScript strings behave like read-only arrays of UTF-16 characters: individual characters can be accessed via bracket notation, and generic array methods can be applied to them.

# Core Definition

"JavaScript strings behave like read-only arrays of UTF-16 Unicode characters. Instead of accessing individual characters with the charAt() method, you can use square brackets." Generic array methods can be applied to strings via Function.call. However, strings are immutable, so they cannot be modified in place. (Flanagan, p. 196)

# Prerequisites

- **array-fundamentals** — Understanding of array access patterns
- **array-like-objects** — Strings are a form of array-like value

# Key Properties

1. Bracket notation works: `s[1]` instead of `s.charAt(1)`
2. Strings are read-only (immutable)
3. `typeof` still returns "string"; `Array.isArray()` returns false
4. Generic array methods can be applied via call()

# Construction / Recognition

```javascript
let s = "test";
s[1]  // => "e"
```

# Context & Application

Bracket notation on strings is more concise than charAt(). Array methods on strings can be useful but strings should generally be handled as strings.

# Examples

```javascript
let s = "test";
s.charAt(0)  // => "t"
s[1]         // => "e"

Array.prototype.join.call("JavaScript", " ")  // => "J a v a S c r i p t"
```
(Flanagan, p. 196)

# Relationships

## Builds Upon
- **array-fundamentals** — Uses array-like access patterns
- **array-like-objects** — Strings are array-like but best handled as strings

## Enables
- Concise character access

## Related
- None specific within scope

## Contrasts With
- None specific

# Common Errors

- **Error**: Trying to modify string characters via bracket notation.
  **Correction**: Strings are immutable. Create a new string instead.

# Common Confusions

- **Confusion**: Strings are arrays.
  **Clarification**: Strings are array-like but are not arrays. Array.isArray("test") returns false.

# Source Reference

Chapter 7: Arrays, Section 7.10, page 196.

# Verification Notes

- Definition source: Direct quote from source text
- Confidence rationale: Clearly stated
- Uncertainties: None
- Cross-reference status: Verified
