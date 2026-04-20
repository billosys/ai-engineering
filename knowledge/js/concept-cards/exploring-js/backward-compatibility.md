---
# === CORE IDENTIFICATION ===
concept: Backward Compatibility
slug: backward-compatibility

# === CLASSIFICATION ===
category: language-background
subcategory: design-philosophy
tier: foundational

# === PROVENANCE ===
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "History and evolution of JavaScript"
chapter_number: 5
pdf_page: null
section: "5.6 How to not break the web while changing JavaScript"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "don't break the web"
  - web compatibility

# === TYPED RELATIONSHIPS ===
prerequisites:
  - ecmascript-standard
extends: []
related:
  - javascript-quirks
  - strict-mode
  - let-declaration
  - const-declaration
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Why can't JavaScript remove quirks and outdated features?"
---

# Quick Definition

JavaScript maintains strict backward compatibility: new versions never remove old features. Instead, better alternatives are introduced alongside existing quirks.

# Core Definition

JavaScript evolves without breaking existing code through three strategies (Ch. 5, &sect;5.6): "New versions are always completely backward compatible"; "Old features aren't removed or fixed. Instead, better versions of them are introduced" (e.g., `let`/`const` instead of `var`); and changes are made "inside new syntactic constructs" that opt in implicitly (e.g., `yield` only a keyword in generators, modules and classes are implicitly strict mode).

# Prerequisites

- **ecmascript-standard** -- the standard that maintains backward compatibility

# Key Properties

1. New versions are always completely backward compatible
2. Old features are never removed; better alternatives are introduced
3. Changes happen inside new syntactic constructs (implicit opt-in)
4. Examples: `let`/`const` replace `var`; modules/classes are implicitly strict
5. Breaking changes would bloat engines, confuse programmers, and complicate refactoring

# Construction / Recognition

Backward compatibility is why `var`, `==`, and other legacy features still work. It explains why JavaScript has multiple ways to do the same thing.

# Context & Application

This principle is why learning JavaScript means understanding both modern and legacy patterns. It also explains why tools like linters recommend newer constructs.

# Examples

From the source text (Ch. 5, &sect;5.6):
- `let` and `const` are "improved versions of `var`"
- `yield` is only a keyword inside generators (ES6)
- All code inside modules and classes is implicitly in strict mode

# Relationships

## Builds Upon
- **ecmascript-standard** -- backward compatibility is a property of the standard

## Enables
- **strict-mode** -- a compatibility-safe way to improve behavior
- **let-declaration** -- an improved alternative to var

## Related
- **javascript-quirks** -- quirks persist due to backward compatibility

## Contrasts With
- No direct contrast

# Common Errors

- **Error**: Expecting old features to be removed in new versions.
  **Correction**: JavaScript never removes features; it only adds better alternatives.

# Common Confusions

- **Confusion**: Thinking backward compatibility means all old patterns are good.
  **Clarification**: Old features work but modern alternatives (let/const, ===, etc.) are preferred.

# Source Reference

Chapter 5: History and evolution of JavaScript, Section 5.6, lines 462-504.

# Verification Notes

- Definition source: direct from source
- Confidence rationale: Explicit strategy description with concrete examples
- Cross-reference status: verified against Ch. 7, &sect;7.5
