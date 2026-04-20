---
concept: JSON Format
slug: json-format
category: standard-library
subcategory: json
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Creating and parsing JSON (JSON)"
chapter_number: 48
pdf_page: null
section: "48.2 JSON syntax"
extraction_confidence: high
aliases:
  - JavaScript Object Notation
  - JSON syntax
prerequisites: []
extends: []
related:
  - json-stringify
  - json-parse
contrasts_with: []
answers_questions:
  - "How do I work with JSON (stringify and parse)?"
---

# Quick Definition

JSON (JavaScript Object Notation) is a text-based data format whose syntax is a subset of JavaScript expressions, supporting objects (with double-quoted string keys), arrays, strings, numbers, booleans, and `null` -- but not `undefined`, functions, `NaN`, `Infinity`, or comments.

# Core Definition

"Exploring JavaScript" Ch. 48: "JSON ('JavaScript Object Notation') is a storage format that uses text to encode data. Its syntax is a subset of JavaScript expressions." JSON supports: object literals (double-quoted keys, no trailing commas), array literals (no holes/trailing commas), `null`, booleans, numbers (excluding NaN/Infinity), and double-quoted strings. "JSON's grammar is frozen" and "will never get improvements such as optional trailing commas, comments, or unquoted keys."

# Prerequisites

Foundational concept with no prerequisites.

# Key Properties

1. Discovered (not invented) by Douglas Crockford, standardized as ECMA-404
2. Syntax is a subset of JavaScript expressions
3. Object keys must be double-quoted strings
4. No trailing commas allowed
5. No `undefined`, `NaN`, `Infinity`, functions, or comments
6. Cannot directly represent cyclic structures
7. Grammar is frozen -- will never change

# Construction / Recognition

```json
{
  "first": "Jane",
  "last": "Porter",
  "married": true,
  "born": 1890,
  "friends": [ "Tarzan", "Cheeta" ]
}
```

(Ch. 48, Section 48.2, lines 44-53)

# Context & Application

JSON is the dominant data interchange format for web APIs, configuration files, and data storage. Accessed in JavaScript via the global `JSON` namespace object.

# Examples

See construction example above. (Ch. 48, introduction, lines 44-53)

# Relationships

## Enables
- **JSON.stringify()** -- converts JavaScript values to JSON
- **JSON.parse()** -- converts JSON text to JavaScript values

# Common Errors

- **Error**: Including trailing commas in JSON
  **Correction**: Remove trailing commas; JSON does not allow them

# Common Confusions

- **Confusion**: JSON supports JavaScript comments
  **Clarification**: JSON does not support comments; they were intentionally excluded to prevent misuse as parsing directives

# Source Reference

Chapter 48: Creating and parsing JSON, Section 48.2, lines 91-113.

# Verification Notes

- Definition source: direct from source text
- Confidence rationale: explicit syntax specification
- Cross-reference status: verified
