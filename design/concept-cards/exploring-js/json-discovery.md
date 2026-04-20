---
concept: JSON Discovery and Standardization
slug: json-discovery
category: standard-library
subcategory: json
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Creating and parsing JSON (JSON)"
chapter_number: 48
pdf_page: null
section: "48.1 The discovery and standardization of JSON"
extraction_confidence: high
aliases:
  - JSON history
  - ECMA-404
prerequisites: []
extends: []
related:
  - json-format
  - json-no-comments
contrasts_with: []
answers_questions:
  - "How do I work with JSON (stringify and parse)?"
---

# Quick Definition

JSON was "discovered" (not invented) by Douglas Crockford around 2001, formalized the existing practice of using JavaScript literal syntax for data interchange, and was standardized as ECMA-404. Its grammar is frozen and will never change.

# Core Definition

"Exploring JavaScript" Ch. 48 quotes Crockford: "I discovered JSON. I do not claim to have invented JSON because it already existed in nature." JSON was standardized as ECMA-404 (1st edition October 2013, 2nd edition December 2017). The standard states: "Because it is so simple, it is not expected that the JSON grammar will ever change. This gives JSON, as a foundational notation, tremendous stability."

# Prerequisites

Foundational concept with no prerequisites.

# Key Properties

1. Discovered by Douglas Crockford circa 2001
2. Practice of using JS literals for data predates Crockford (Netscape, 1996)
3. Standardized as ECMA-404
4. Grammar is frozen -- will never change
5. No improvements will be added (trailing commas, comments, unquoted keys)
6. Supersets of JSON can be created that compile to plain JSON

# Construction / Recognition

Not a code construct. JSON is a data format standard.

# Context & Application

Understanding JSON's design philosophy (simplicity, stability, frozen grammar) helps explain its limitations and widespread adoption.

# Examples

From the source: Crockford noted that "there was someone at Netscape who was using JavaScript array literals for doing data communication as early as 1996."

(Ch. 48, Section 48.1, lines 60-70)

# Relationships

## Related
- **JSON format** -- the format itself
- **JSON does not support comments** -- a consequence of the frozen grammar

# Common Errors

- **Error**: Expecting JSON to add new features
  **Correction**: JSON's grammar is frozen; use supersets like JSONC or JSON5 for extensions

# Common Confusions

- **Confusion**: JSON was designed specifically for JavaScript
  **Clarification**: While based on JavaScript syntax, JSON is a language-independent data format used across all programming languages

# Source Reference

Chapter 48: Creating and parsing JSON, Section 48.1, lines 58-89.

# Verification Notes

- Definition source: direct quotation from Crockford via source text
- Confidence rationale: explicit historical section
- Cross-reference status: verified
