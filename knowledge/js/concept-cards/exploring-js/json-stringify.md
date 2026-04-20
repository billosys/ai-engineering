---
concept: JSON.stringify()
slug: json-stringify
category: standard-library
subcategory: json
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Creating and parsing JSON (JSON)"
chapter_number: 48
pdf_page: null
section: "48.3.1 JSON.stringify()"
extraction_confidence: high
aliases:
  - JSON serialization
  - JSON encoding
prerequisites:
  - json-format
extends: []
related:
  - json-parse
  - json-replacers-revivers
contrasts_with: []
answers_questions:
  - "How do I work with JSON (stringify and parse)?"
---

# Quick Definition

`JSON.stringify(data, replacer?, space?)` converts a JavaScript value to a JSON string, with optional replacer for filtering/transforming and space parameter for indentation.

# Core Definition

"Exploring JavaScript" Ch. 48: "This method converts JavaScript data to a JSON string." Key behaviors: supported primitives are stringified as expected; unsupported numbers become `'null'`; `undefined`, symbols, and functions produce `undefined` (omitted from objects, `null` in arrays); BigInts throw TypeError; objects with `.toJSON()` use that method's result; circular data throws TypeError.

# Prerequisites

- **JSON format** -- stringify produces JSON text

# Key Properties

1. Returns a single-line string by default
2. `space` parameter (number) enables indented multi-line output
3. `undefined`, Symbol, functions become `undefined` (omitted from objects)
4. NaN and Infinity become `'null'`
5. BigInt throws TypeError
6. Objects with `.toJSON()` method use its return value
7. Circular structures throw TypeError
8. `replacer` can be an Array (property whitelist) or function (value visitor)

# Construction / Recognition

```js
JSON.stringify({prop: ['a', 'b']})
// '{"prop":["a","b"]}'

JSON.stringify({prop: ['a', 'b']}, null, 2)
// '{\n  "prop": [\n    "a",\n    "b"\n  ]\n}'
```

(Ch. 48, Section 48.3.1, lines 126-163)

# Context & Application

Primary method for serializing JavaScript data for storage, transmission, or logging. Understanding which values are unsupported is critical.

# Examples

```js
> JSON.stringify(undefined)    // undefined (not a string)
> JSON.stringify(NaN)          // 'null'
> JSON.stringify({a: undefined, b: true})  // '{"b":true}'
> JSON.stringify([undefined, 123])         // '[null,123]'
```

(Ch. 48, Section 48.3.1.3, lines 165-267)

# Relationships

## Builds Upon
- **JSON format** -- output conforms to JSON syntax

## Related
- **JSON.parse()** -- inverse operation
- **JSON replacer** -- customizes serialization

# Common Errors

- **Error**: Expecting `undefined` values to appear in JSON output
  **Correction**: `undefined` is omitted from objects and becomes `null` in arrays

# Common Confusions

- **Confusion**: `JSON.stringify()` can handle any JavaScript value
  **Clarification**: BigInts throw, circular structures throw, and several types produce `undefined`

# Source Reference

Chapter 48: Creating and parsing JSON, Section 48.3.1, lines 126-279.

# Verification Notes

- Definition source: direct from source text
- Confidence rationale: explicit detailed behavior for each type
- Cross-reference status: verified
