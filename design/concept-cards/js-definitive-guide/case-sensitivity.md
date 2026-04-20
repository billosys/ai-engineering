---
# === CORE IDENTIFICATION ===
concept: Case Sensitivity
slug: case-sensitivity

# === CLASSIFICATION ===
category: language-fundamentals
subcategory: lexical-structure
tier: foundational

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Lexical Structure"
chapter_number: 2
pdf_page: 32
section: "2.1 The Text of a JavaScript Program"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - javascript-language-overview
extends: []
related:
  - identifiers
  - reserved-words
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I understand before learning about closures?"
---

# Quick Definition

JavaScript is a case-sensitive language: keywords, variable names, function names, and all other identifiers must always use a consistent capitalization of letters.

# Core Definition

"JavaScript is a case-sensitive language. This means that language keywords, variables, function names, and other identifiers must always be typed with a consistent capitalization of letters. The while keyword, for example, must be typed 'while,' not 'While' or 'WHILE.' Similarly, online, Online, OnLine, and ONLINE are four distinct variable names." (p. 32)

# Prerequisites

- **javascript-language-overview** — Must understand the language basics

# Key Properties

1. Keywords must be lowercase: `while`, not `While` or `WHILE`
2. Variables with different capitalization are distinct: `online`, `Online`, `OnLine`, `ONLINE`
3. Applies to all identifiers: variables, functions, classes, properties
4. JavaScript ignores spaces between tokens and mostly ignores line breaks

# Construction / Recognition

Case sensitivity affects every identifier in JavaScript code. Mismatched case results in undefined variables or reference errors.

# Context & Application

Case sensitivity is one of the first things to understand when writing JavaScript. It affects variable naming conventions (camelCase is standard) and can be a source of hard-to-find bugs.

# Examples

From the source text (p. 32):
- `while` must be typed "while," not "While" or "WHILE"
- `online`, `Online`, `OnLine`, and `ONLINE` are four distinct variable names

# Relationships

## Builds Upon
- **javascript-language-overview** — Case sensitivity is a basic language property

## Enables
- **identifiers** — Identifier naming must respect case sensitivity
- **reserved-words** — Reserved words are case-sensitive

## Related
- **identifiers** — Identifier names are case-sensitive
- **reserved-words** — Reserved words are always lowercase

## Contrasts With
- None within this source

# Common Errors

- **Error**: Writing `While` or `WHILE` instead of `while`.
  **Correction**: All JavaScript keywords are lowercase.

# Common Confusions

- **Confusion**: HTML attribute names are case-sensitive like JavaScript.
  **Clarification**: HTML is case-insensitive; JavaScript is case-sensitive. This distinction matters in client-side programming.

# Source Reference

Chapter 2: Lexical Structure, Section 2.1, page 32.

# Verification Notes

- Definition source: Direct quote from p. 32
- Confidence rationale: High — clearly stated
- Uncertainties: None
- Cross-reference status: Verified
