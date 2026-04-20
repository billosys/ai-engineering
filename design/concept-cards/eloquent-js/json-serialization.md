---
# === CORE IDENTIFICATION ===
concept: JSON Serialization
slug: json-serialization

# === CLASSIFICATION ===
category: data-structures
subcategory: serialization
tier: intermediate

# === PROVENANCE ===
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Data Structures: Objects and Arrays"
chapter_number: 4
pdf_page: null
section: "JSON"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - JSON.stringify
  - JSON.parse

# === TYPED RELATIONSHIPS ===
prerequisites:
  - json
  - object
  - string
extends:
  - json
related: []
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions: []
---

# Quick Definition

JavaScript provides `JSON.stringify` to convert a value into a JSON-encoded string, and `JSON.parse` to convert a JSON string back into the value it represents.

# Core Definition

As described in "Eloquent JavaScript" (Ch 4, lines 1331-1335 of 04-data-structures-objects-and-arrays.md): "JavaScript gives us the functions `JSON.stringify` and `JSON.parse` to convert data to and from this format. The first takes a JavaScript value and returns a JSON-encoded string. The second takes such a string and converts it to the value it encodes."

# Prerequisites

- **json**: Understanding the JSON format.
- **object**: Values being serialized are typically objects or arrays.
- **string**: The serialized form is a string.

# Key Properties

1. `JSON.stringify(value)` converts a JavaScript value to a JSON string.
2. `JSON.parse(string)` converts a JSON string to a JavaScript value.
3. These are inverse operations: `JSON.parse(JSON.stringify(x))` reconstructs `x` (for JSON-compatible values).

# Construction / Recognition

## To Construct/Create:
```javascript
let string = JSON.stringify({squirrel: false, events: ["weekend"]});
let value = JSON.parse(string);
```

## To Identify/Recognize:
- Calls to `JSON.stringify()` or `JSON.parse()`.

# Context & Application

JSON serialization is essential for sending data to web servers, storing data in files or localStorage, and receiving API responses.

# Examples

**Example 1** (Ch 4, lines 1337-1344 of 04-data-structures-objects-and-arrays.md):
```javascript
let string = JSON.stringify({squirrel: false,
                             events: ["weekend"]});
console.log(string);
// → {"squirrel":false,"events":["weekend"]}
console.log(JSON.parse(string).events);
// → ["weekend"]
```

# Relationships

## Builds Upon
- **json** -- Serialization converts to/from JSON format.

## Enables
- Data storage and transmission.

## Related
- None within this source.

## Contrasts With
- None within this source.

# Common Errors

- **Error**: Trying to `JSON.stringify` a value containing functions or circular references.
  **Correction**: Functions are omitted from JSON output; circular references cause errors.

# Common Confusions

- **Confusion**: `JSON.parse` returns the same object.
  **Clarification**: `JSON.parse` creates a **new** object. It is not the original object.

# Source Reference

Chapter 4: Data Structures: Objects and Arrays, Section "JSON", lines 1330-1344 of 04-data-structures-objects-and-arrays.md (book.md line 3312).

# Verification Notes

- Definition source: direct (quoted from lines 1331-1335)
- Confidence rationale: Explicit description with example
- Cross-reference status: verified within chapter
