---
concept: toJSON() Method
slug: json-tojson-method
category: standard-library
subcategory: json
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Creating and parsing JSON (JSON)"
chapter_number: 48
pdf_page: null
section: "48.3.1.3 Details on how data is converted to JSON"
extraction_confidence: high
aliases:
  - custom JSON serialization
prerequisites:
  - json-stringify
extends: []
related:
  - json-replacers-revivers
contrasts_with: []
answers_questions:
  - "How do I work with JSON (stringify and parse)?"
---

# Quick Definition

If an object has a `.toJSON()` method, `JSON.stringify()` calls it and stringifies the returned value instead of the object itself. This enables custom classes like `Date` to control their JSON representation.

# Core Definition

"Exploring JavaScript" Ch. 48: "If an object has a method .toJSON(), then the result of that method is stringified." This is how `Date` objects are serialized to strings: "Dates have a method .toJSON() that returns a string."

# Prerequisites

- **JSON.stringify()** -- `.toJSON()` is called by stringify

# Key Properties

1. Called automatically by `JSON.stringify()`
2. Return value is stringified instead of the object
3. Enables custom JSON representations for classes
4. `Date.prototype.toJSON()` returns an ISO string

# Construction / Recognition

```js
class Point {
  constructor(x, y) { this.x = x; this.y = y; }
  toJSON() { return {x: this.x, y: this.y}; }
}
assert.equal(JSON.stringify(new Point(3, 5)), '{"x":3,"y":5}');
```

(Ch. 48, Section 48.3.3, lines 302-317)

# Context & Application

Implement `.toJSON()` on custom classes to control how instances appear in JSON output.

# Examples

```js
> JSON.stringify({toJSON() {return true}})
'true'
> JSON.stringify(new Date(2999, 11, 31))
'"2999-12-30T23:00:00.000Z"'
```

(Ch. 48, Section 48.3.1.3, lines 218-229)

# Relationships

## Builds Upon
- **JSON.stringify()** -- calls `.toJSON()` during serialization

## Related
- **JSON replacers and revivers** -- alternative customization mechanism

# Common Errors

- **Error**: Returning the object itself from `.toJSON()` causing infinite recursion
  **Correction**: Return a plain value (object literal, primitive) from `.toJSON()`

# Common Confusions

- **Confusion**: `.toJSON()` must return a string
  **Clarification**: `.toJSON()` can return any JSON-compatible value; stringify handles the final string conversion

# Source Reference

Chapter 48: Creating and parsing JSON, Section 48.3.1.3, lines 215-229.

# Verification Notes

- Definition source: direct from source text
- Confidence rationale: explicit description with Date example
- Cross-reference status: verified
