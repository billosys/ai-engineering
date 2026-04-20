---
concept: JSON Serialization and Parsing
slug: json-stringify-parse
category: standard-library
subcategory: serialization
tier: foundational
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "The JavaScript Standard Library"
chapter_number: 11
pdf_page: 323
section: "11.6 JSON Serialization and Parsing"
extraction_confidence: high
aliases:
  - "JSON.stringify"
  - "JSON.parse"
  - "JSON serialization"
prerequisites: []
extends: []
related:
  - json-replacer-reviver
contrasts_with: []
answers_questions: []
---

# Quick Definition

The `JSON.stringify()` and `JSON.parse()` methods for converting JavaScript data structures to JSON strings and back, supporting primitives, arrays, objects, and customization through replacer/reviver functions.

# Core Definition

"The easiest way to serialize data in JavaScript uses a serialization format known as JSON" (p. 323). `JSON.stringify()` converts objects/arrays to JSON strings. `JSON.parse()` reconstructs data from JSON strings. JSON supports numbers, strings, booleans, `null`, arrays, and objects, but not `Map`, `Set`, `RegExp`, `Date`, or typed arrays.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. `JSON.stringify()` converts to string; `JSON.parse()` converts back
2. Supports: numbers, strings, booleans, null, arrays, plain objects
3. Does not support: Map, Set, RegExp, Date, typed arrays, functions, undefined
4. Third argument to `stringify()` controls indentation (number or string)
5. Objects with `toJSON()` method get custom serialization (e.g., Date)
6. Can be used for deep copying: `JSON.parse(JSON.stringify(o))`

# Construction / Recognition

```js
let o = {s: "", n: 0, a: [true, false, null]};
let s = JSON.stringify(o);     // '{"s":"","n":0,"a":[true,false,null]}'
let copy = JSON.parse(s);
JSON.stringify(o, null, 2);    // Pretty-printed with 2-space indent
```

# Context & Application

The universal data interchange format for web APIs, configuration files, and inter-process communication. Understanding JSON limitations is essential for correct serialization.

# Examples

From the source text (p. 323-324): Deep copy via JSON: `function deepcopy(o) { return JSON.parse(JSON.stringify(o)); }`. Pretty-printing: `JSON.stringify(o, null, 2)` produces formatted output with 2-space indentation.

# Relationships

## Enables
- **JSON replacer/reviver** — Customization hooks for serialization/deserialization

# Common Errors

- **Error**: Expecting Date objects to survive a JSON round-trip as Dates.
  **Correction**: Dates are serialized as ISO strings by their `toJSON()` method. Use a reviver function with `JSON.parse()` to reconstruct them.

# Common Confusions

- **Confusion**: Thinking JSON.stringify can serialize any JavaScript value.
  **Clarification**: Functions, undefined, Symbols, Map, Set, RegExp, and circular references cannot be serialized. Non-serializable values are omitted or cause errors.

# Source Reference

Chapter 11: The JavaScript Standard Library, Section 11.6, pages 323-326.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: High
- Uncertainties: None
- Cross-reference status: Verified
