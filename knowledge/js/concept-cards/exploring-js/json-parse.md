---
concept: JSON.parse()
slug: json-parse
category: standard-library
subcategory: json
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Creating and parsing JSON (JSON)"
chapter_number: 48
pdf_page: null
section: "48.3.2 JSON.parse()"
extraction_confidence: high
aliases:
  - JSON deserialization
  - JSON decoding
prerequisites:
  - json-format
extends: []
related:
  - json-stringify
  - json-replacers-revivers
contrasts_with: []
answers_questions:
  - "How do I work with JSON (stringify and parse)?"
---

# Quick Definition

`JSON.parse(text, reviver?)` converts a JSON string into a JavaScript value, with an optional reviver function that can transform parsed values during deserialization.

# Core Definition

"Exploring JavaScript" Ch. 48: "This method converts a JSON text to a JavaScript value." The optional `reviver` parameter is a "value visitor that can transform the parsed JSON data before it is returned." The reviver visits values bottom-up (leaves first, root last).

# Prerequisites

- **JSON format** -- parse accepts JSON text

# Key Properties

1. Accepts valid JSON text, returns JavaScript value
2. Throws SyntaxError for invalid JSON
3. Optional `reviver` transforms values during parsing
4. Reviver visits bottom-up (leaves first, root last)
5. Reviver returning `undefined` omits the value

# Construction / Recognition

```js
> JSON.parse('{"prop":["a","b"]}')
{ prop: [ 'a', 'b' ] }
```

(Ch. 48, Section 48.3.2, lines 281-294)

# Context & Application

Primary method for deserializing JSON data received from APIs, files, or storage.

# Examples

Roundtrip with a class:
```js
class Point {
  static fromJson(jsonObj) { return new Point(jsonObj.x, jsonObj.y); }
  constructor(x, y) { this.x = x; this.y = y; }
  toJSON() { return {x: this.x, y: this.y}; }
}
Point.fromJson(JSON.parse('{"x":3,"y":5}'));
```

(Ch. 48, Section 48.3.3, lines 296-338)

# Relationships

## Builds Upon
- **JSON format** -- input must be valid JSON

## Related
- **JSON.stringify()** -- inverse operation
- **JSON reviver** -- customizes deserialization

# Common Errors

- **Error**: Parsing JSON with single-quoted strings
  **Correction**: JSON requires double-quoted strings; ensure input is valid JSON

# Common Confusions

- **Confusion**: `JSON.parse()` produces the same types as the original data
  **Clarification**: Dates become strings, class instances become plain objects; use revivers or factory methods for reconstruction

# Source Reference

Chapter 48: Creating and parsing JSON, Section 48.3.2, lines 281-338.

# Verification Notes

- Definition source: direct from source text
- Confidence rationale: explicit definition with example
- Cross-reference status: verified
