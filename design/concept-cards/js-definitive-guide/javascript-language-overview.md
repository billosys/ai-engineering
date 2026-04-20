---
# === CORE IDENTIFICATION ===
concept: JavaScript Language Overview
slug: javascript-language-overview

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
pdf_page: 18
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - JS
  - ECMAScript

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - ecmascript-versioning
  - host-environments
  - strict-mode
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I understand before learning about closures?"
---

# Quick Definition

JavaScript is a high-level, dynamic, interpreted programming language that supports object-oriented and functional programming styles, with untyped variables and syntax loosely based on Java.

# Core Definition

As described in Chapter 1, "JavaScript is a high-level, dynamic, interpreted programming language that is well-suited to object-oriented and functional programming styles. JavaScript's variables are untyped. Its syntax is loosely based on Java, but the languages are otherwise unrelated. JavaScript derives its first-class functions from Scheme and its prototype-based inheritance from the little-known language Self." (p. 18)

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. High-level, dynamic, and interpreted
2. Supports both object-oriented and functional programming styles
3. Variables are untyped (any variable can hold any type of value)
4. First-class functions derived from Scheme
5. Prototype-based inheritance derived from Self
6. Most-deployed programming language in history

# Construction / Recognition

JavaScript programs can be run in web browsers (via developer console or `<script>` tags) or via Node.js from the command line. The language itself defines a minimal API; input/output is provided by the host environment.

# Context & Application

JavaScript is the programming language of the web, running in all modern browsers. Since 2010, Node.js has enabled JavaScript programming outside of browsers, making it the most-used programming language among software developers.

# Examples

From the source text (p. 21):
```
$ node
> let x = 2, y = 3;
undefined
> x + y
5
> (x === 2) && (y === 3)
true
```

# Relationships

## Builds Upon
- None — this is the root concept for the language

## Enables
- **ecmascript-versioning** — Understanding the language leads to understanding its standardization history
- **host-environments** — The language runs within host environments
- **strict-mode** — A mode that corrects early language mistakes

## Related
- **ecmascript-versioning** — JavaScript is standardized as ECMAScript

## Contrasts With
- None within this source

# Common Errors

- **Error**: Assuming JavaScript and Java are related languages.
  **Correction**: Despite the name and superficial syntactic resemblance, JavaScript is completely different from Java (p. 18).

# Common Confusions

- **Confusion**: JavaScript is just a scripting language for simple web page effects.
  **Clarification**: JavaScript has "long since outgrown its scripting-language roots to become a robust and efficient general-purpose language suitable for serious software engineering and projects with huge codebases" (p. 18).

# Source Reference

Chapter 1: Introduction to JavaScript, pages 18-20.

# Verification Notes

- Definition source: Direct quote from p. 18
- Confidence rationale: High — the source provides a clear, authoritative definition
- Uncertainties: None
- Cross-reference status: Verified against source text
