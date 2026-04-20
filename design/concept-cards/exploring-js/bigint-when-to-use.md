---
# === CORE IDENTIFICATION ===
concept: When to Use BigInts vs Numbers
slug: bigint-when-to-use

# === CLASSIFICATION ===
category: primitive-types
subcategory: bigints
tier: advanced

# === PROVENANCE ===
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Bigints -- arbitrary-precision integers (advanced)"
chapter_number: 20
pdf_page: null
section: "How do I decide when to use numbers and when to use bigints?"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - number-type
  - bigint-type
  - safe-integers
extends: []
related: []
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions: []
---

# Quick Definition

Use numbers for integers up to 53 bits and for array indices (they are ubiquitous and efficient). Use bigints when you need integers beyond 53 bits, such as for large IDs or financial calculations.

# Core Definition

Rauschmayer's recommendations: "Use numbers for up to 53 bits and for Array indices. Rationale: They already appear everywhere and are handled efficiently by most engines (especially if they fit into 31 bits)." "Use bigints for large numeric values: If your fraction-less values don't fit into 53 bits, you have no choice but to move to bigints." All existing web APIs return and accept only numbers (Ch. 20, Section 20.9.1).

# Prerequisites

- **number-type** -- one of the two numeric types
- **bigint-type** -- the other numeric type
- **safe-integers** -- the precision limit that motivates bigints

# Key Properties

1. Numbers for: up to 53-bit integers, array indices, web API interop
2. Bigints for: values exceeding 53 bits, financial amounts in cents, 64-bit IDs
3. Web APIs currently only work with numbers
4. Numbers more efficient in most engines (especially 31-bit range)

# Construction / Recognition

Decision rule: If your integer values fit in 53 bits and you work with standard APIs, use numbers. Otherwise, use bigints.

# Context & Application

This is a practical decision that affects API design, data storage, and performance.

# Examples

From the source text:

Use numbers for:
- `Array.prototype.forEach()` indices
- `Array.prototype.entries()` indices
- Standard web API parameters

Use bigints for:
- Twitter/X 64-bit post IDs (previously stored as strings)
- Financial amounts multiplied to remove decimals (e.g., USD cents)

# Relationships

## Builds Upon
- **number-type** — default numeric type
- **bigint-type** — alternative for large integers
- **safe-integers** — the boundary between number and bigint territory

## Enables
- Informed numeric type selection

## Related
- None

## Contrasts With
- None

# Common Errors

- **Error**: Using bigints for everything "to be safe"
  **Correction**: Bigints are less efficient and not supported by most web APIs. Use numbers when 53-bit precision suffices.

# Common Confusions

- **Confusion**: Thinking bigints are always better than numbers
  **Clarification**: Numbers are more efficient and universally supported. Only switch to bigints when you actually need >53 bit precision.

# Source Reference

Chapter 20: Bigints, Section 20.9.1, lines 938-954.

# Verification Notes

- Definition source: direct (author's explicit recommendations)
- Confidence rationale: Clear guidelines from the author
- Cross-reference status: verified
