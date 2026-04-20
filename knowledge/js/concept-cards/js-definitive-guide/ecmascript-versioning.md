---
# === CORE IDENTIFICATION ===
concept: ECMAScript Versioning
slug: ecmascript-versioning

# === CLASSIFICATION ===
category: language-fundamentals
subcategory: language-overview
tier: foundational

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Introduction to JavaScript"
chapter_number: 1
pdf_page: 19
section: "JavaScript: Names, Versions, and Modes"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - ECMAScript
  - ES
  - ES6
  - ES2015
  - ES5

# === TYPED RELATIONSHIPS ===
prerequisites:
  - javascript-language-overview
extends: []
related:
  - strict-mode
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I understand before learning about closures?"
---

# Quick Definition

ECMAScript is the official standard name for JavaScript, maintained by ECMA International, with versions identified by edition number (ES5, ES6) or year of release (ES2016-ES2020).

# Core Definition

JavaScript was standardized by ECMA as "ECMAScript" due to trademark issues. The book uses "ECMAScript" and "ES" to refer to the standard and its versions. ES5 is the compatibility baseline. ES6 (released 2015) "added major new features—including class and module syntax—that changed JavaScript from a scripting language into a serious, general-purpose language suitable for large-scale software engineering." Since ES6, specifications follow a yearly release cadence identified by year (ES2016, ES2017, etc.). (p. 19)

# Prerequisites

- **javascript-language-overview** — Must understand what JavaScript is before understanding its standardization history

# Key Properties

1. "JavaScript" is a trademark; "ECMAScript" is the standard name
2. ES5 serves as the compatibility baseline for modern JavaScript
3. ES6 (2015) was the major modernization release (classes, modules)
4. Post-ES6 versions use yearly naming: ES2016, ES2017, ES2018, ES2019, ES2020
5. New language features often implicitly invoke strict mode

# Construction / Recognition

Version features are recognized by syntax: `class` and `import/export` indicate ES6+; arrow functions (`=>`) indicate ES6+; `async`/`await` indicate ES2017+.

# Context & Application

Understanding ECMAScript versions is essential for knowing which features are available in target environments and for reading documentation that references specific ES versions.

# Examples

From the source text (p. 19):
- ES5: the compatibility baseline supported by all browsers through the 2010s
- ES6 (2015): added class syntax, module syntax, let/const, arrow functions
- ES2016-ES2020: yearly incremental additions

# Relationships

## Builds Upon
- **javascript-language-overview** — Versioning is the standardization history of the language

## Enables
- **strict-mode** — ES5 introduced strict mode; ES6 features implicitly enable it

## Related
- **strict-mode** — New language features in ES6+ implicitly invoke strict mode

## Contrasts With
- None within this source

# Common Errors

- **Error**: Using ES6+ features without checking target environment support.
  **Correction**: Check browser/Node.js compatibility for features beyond ES5.

# Common Confusions

- **Confusion**: ES6 and ES2015 are different versions.
  **Clarification**: They are the same version — ES6 is the edition number, ES2015 is the year-based name.

# Source Reference

Chapter 1: Introduction to JavaScript, Section "JavaScript: Names, Versions, and Modes", page 19.

# Verification Notes

- Definition source: Direct quotes from p. 19
- Confidence rationale: High — clearly explained in the source
- Uncertainties: None
- Cross-reference status: Verified
