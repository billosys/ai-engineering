---
# === CORE IDENTIFICATION ===
concept: ECMAScript Standard
slug: ecmascript-standard

# === CLASSIFICATION ===
category: language-background
subcategory: history
tier: foundational

# === PROVENANCE ===
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "History and evolution of JavaScript"
chapter_number: 5
pdf_page: null
section: "5.2 Standardization: JavaScript vs. ECMAScript"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - ECMAScript
  - ECMA-262
  - "ES"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - javascript-creation
extends: []
related:
  - tc39-committee
  - ecmascript-versions
  - tc39-process
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the relationship between JavaScript and ECMAScript?"
---

# Quick Definition

ECMAScript is the official language standard for JavaScript, maintained by Ecma International as ECMA-262. The terms JavaScript and ECMAScript are often used interchangeably.

# Core Definition

There are two standards for JavaScript: ECMA-262 (primary, hosted by Ecma International) and ISO/IEC 16262 (secondary). The language is called *ECMAScript* in the standard because Sun (now Oracle) trademarked "JavaScript." "Often, JavaScript and ECMAScript mean the same thing." When distinguished: "The term *JavaScript* refers to the language and its implementations. The term *ECMAScript* refers to the language standard and language versions." (Ch. 5, &sect;5.2).

# Prerequisites

- **javascript-creation** -- JavaScript had to exist before standardization

# Key Properties

1. Primary standard: ECMA-262, hosted by Ecma International
2. Secondary standard: ISO/IEC 16262
3. "ECMAScript" name chosen because Sun trademarked "JavaScript"
4. "ECMA" originally stood for European Computer Manufacturers Association, later became "Ecma" (proper name)
5. Versions originally numbered (ES1-ES6), then by year (ES2016+)

# Construction / Recognition

ECMAScript version references appear as ES6, ES2015, ES2020, etc. "ESX" and "ECMAScript X" are equivalent notations.

# Context & Application

Understanding the standard is essential for knowing which features are officially part of the language versus platform-specific extensions.

# Examples

From the source text (Ch. 5, &sect;5.2):
- "ECMAScript 6" = "ES6" = "ECMAScript 2015" (the 6th edition, published 2015)
- JavaScript = language and implementations
- ECMAScript = language standard and versions

# Relationships

## Builds Upon
- **javascript-creation** -- standardization followed creation

## Enables
- **ecmascript-versions** -- the timeline of specific versions
- **tc39-process** -- the process for evolving the standard

## Related
- **tc39-committee** -- the committee that manages the standard

## Contrasts With
- No direct contrast

# Common Errors

- **Error**: Treating ECMAScript and JavaScript as completely different things.
  **Correction**: They usually mean the same thing; the distinction matters mainly in formal/standards contexts.

# Common Confusions

- **Confusion**: Thinking "ECMAScript 6" and "ES2015" are different versions.
  **Clarification**: They are the same version; ES6 was the first to use a year-based name (2015).

# Source Reference

Chapter 5: History and evolution of JavaScript, Section 5.2, lines 60-90.

# Verification Notes

- Definition source: direct from source
- Confidence rationale: Explicitly defined with detailed explanation
- Cross-reference status: verified
