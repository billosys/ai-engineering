---
# === CORE IDENTIFICATION ===
concept: JSON
slug: json

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
  - JavaScript Object Notation

# === TYPED RELATIONSHIPS ===
prerequisites:
  - object
  - array
  - string
extends: []
related:
  - json-serialization
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions: []
---

# Quick Definition

JSON (JavaScript Object Notation) is a widely used data serialization format that looks similar to JavaScript's object and array notation, used for storing and transmitting data.

# Core Definition

As defined in "Eloquent JavaScript" (Ch 4, lines 1305-1310 of 04-data-structures-objects-and-arrays.md): "What we can do is *serialize* the data. That means it is converted into a flat description. A popular serialization format is called *JSON* (pronounced 'Jason'), which stands for JavaScript Object Notation. It is widely used as a data storage and communication format on the web, even with languages other than JavaScript."

# Prerequisites

- **object**: JSON is based on JavaScript object notation.
- **array**: JSON supports arrays.
- **string**: All JSON property names must be double-quoted strings.

# Key Properties

1. All property names must be surrounded by **double quotes**.
2. Only simple data expressions are allowed (no functions, bindings, or computation).
3. Comments are **not allowed** in JSON.
4. Used as a data storage and communication format across languages.
5. JavaScript provides `JSON.stringify` and `JSON.parse` for conversion.

# Construction / Recognition

## To Construct/Create:
```json
{
  "squirrel": false,
  "events": ["work", "touched tree", "pizza", "running"]
}
```

## To Identify/Recognize:
- Data that looks like JavaScript object/array notation with double-quoted property names.

# Context & Application

JSON is the standard format for web APIs, configuration files, and data interchange. Understanding JSON is essential for any web development work.

# Examples

**Example 1** (Ch 4, lines 1323-1328 of 04-data-structures-objects-and-arrays.md):
```json
{
  "squirrel": false,
  "events": ["work", "touched tree", "pizza", "running"]
}
```

**Example 2** (Ch 4, lines 1337-1344) -- JSON.stringify and JSON.parse:
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
- **object** -- JSON is based on JavaScript object notation.
- **array** -- JSON supports arrays.
- **string** -- JSON requires double-quoted strings.

## Enables
- **json-serialization** -- Converting between JavaScript values and JSON strings.
- Data storage, API communication, configuration files.

## Related
- None within this source.

## Contrasts With
- None within this source.

# Common Errors

- **Error**: Using single quotes for property names in JSON.
  **Correction**: JSON requires double quotes for all property names and string values.

# Common Confusions

- **Confusion**: JSON and JavaScript object literals are identical.
  **Clarification**: JSON is stricter: requires double-quoted keys, no functions, no comments, no trailing commas.

# Source Reference

Chapter 4: Data Structures: Objects and Arrays, Section "JSON", lines 1285-1344 of 04-data-structures-objects-and-arrays.md (book.md line 3312).

# Verification Notes

- Definition source: direct (quoted from lines 1305-1310)
- Confidence rationale: Explicit definition with italicized term "JSON"
- Cross-reference status: verified within chapter
