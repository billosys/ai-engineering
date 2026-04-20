---
concept: JSON Replacers and Revivers
slug: json-replacers-revivers
category: standard-library
subcategory: json
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Creating and parsing JSON (JSON)"
chapter_number: 48
pdf_page: null
section: "48.4 Customizing stringification and parsing"
extraction_confidence: high
aliases:
  - JSON value visitors
  - JSON replacer
  - JSON reviver
prerequisites:
  - json-stringify
  - json-parse
extends: []
related: []
contrasts_with: []
answers_questions:
  - "How do I work with JSON (stringify and parse)?"
---

# Quick Definition

Replacers and revivers are value visitor functions that customize JSON serialization and deserialization: a replacer transforms JavaScript values before stringification, while a reviver transforms parsed values before they are returned, enabling support for custom types like RegExp or Date.

# Core Definition

"Exploring JavaScript" Ch. 48: "JSON.stringify() lets the value visitor in its parameter replacer transform JavaScript data before it is stringified. JSON.parse() lets the value visitor in its parameter reviver transform parsed JavaScript data before it is returned." Visitor signature: `(key: string, value: any) => any`. Returning `value` means no change; returning a different value replaces it; returning `undefined` omits it. Replacer visits top-down; reviver visits bottom-up.

# Prerequisites

- **JSON.stringify()** -- replacer is a parameter of stringify
- **JSON.parse()** -- reviver is a parameter of parse

# Key Properties

1. Replacer: `stringify(data, replacer)` -- visits top-down (root first)
2. Reviver: `parse(text, reviver)` -- visits bottom-up (leaves first)
3. Visitor signature: `function(key, value)` with `this` as parent
4. Return `value` for no change, different value to replace, `undefined` to omit
5. Replacer can also be an Array of property names (whitelist)

# Construction / Recognition

Replacer (stringifying RegExp):
```js
function replacer(key, value) {
  if (value instanceof RegExp) {
    return { __type__: 'RegExp', source: value.source, flags: value.flags };
  }
  return value;
}
JSON.stringify({regex: /abc/ui}, replacer, 2);
```

Reviver (parsing RegExp):
```js
function reviver(key, value) {
  if (value && value.__type__ === 'RegExp') {
    return new RegExp(value.source, value.flags);
  }
  return value;
}
JSON.parse(str, reviver);
```

(Ch. 48, Section 48.4.4-48.4.5, lines 486-539)

# Context & Application

Used to handle types that JSON does not natively support: Dates, RegExp, custom classes, Maps, Sets, etc.

# Examples

See construction examples above. (Ch. 48, Section 48.4.4-48.4.5, lines 468-539)

# Relationships

## Builds Upon
- **JSON.stringify()** -- replacer customizes serialization
- **JSON.parse()** -- reviver customizes deserialization

# Common Errors

- **Error**: Forgetting to return `value` in the default case
  **Correction**: Always return `value` when no transformation is needed; otherwise values are lost

# Common Confusions

- **Confusion**: Replacer and reviver visit in the same order
  **Clarification**: Replacer is top-down (root first); reviver is bottom-up (leaves first)

# Source Reference

Chapter 48: Creating and parsing JSON, Section 48.4, lines 351-539.

# Verification Notes

- Definition source: direct from source text
- Confidence rationale: explicit section with visit order and examples
- Cross-reference status: verified
