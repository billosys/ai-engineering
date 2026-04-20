---
concept: JSON Replacer and Reviver Functions
slug: json-replacer-reviver
category: standard-library
subcategory: serialization
tier: intermediate
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "The JavaScript Standard Library"
chapter_number: 11
pdf_page: 325
section: "11.6.1 JSON Customizations"
extraction_confidence: high
aliases:
  - "replacer function"
  - "reviver function"
  - "toJSON"
prerequisites:
  - json-stringify-parse
extends: []
related: []
contrasts_with: []
answers_questions: []
---

# Quick Definition

Optional callback functions passed to `JSON.stringify()` (replacer) and `JSON.parse()` (reviver) that customize serialization and deserialization by transforming values during the process.

# Core Definition

The replacer (second argument to `stringify()`) filters or transforms values during serialization — it can be a function `(key, value) => ...` or an array of property names. The reviver (second argument to `parse()`) transforms primitive values during deserialization, commonly used to reconstruct Date objects or filter properties. Both are invoked as methods of the containing object.

# Prerequisites

- **json-stringify-parse** — Replacer/reviver extend the basic JSON API

# Key Properties

1. Replacer function: `(key, value) => transformedValue` — return `undefined` to omit
2. Replacer array: only include listed property names in output
3. Reviver function: `(key, value) => transformedValue` — return `undefined` to delete
4. Both functions are called as methods of the containing object (`this` is the container)
5. `toJSON()` method on objects provides custom serialization (e.g., Date uses this)

# Construction / Recognition

```js
// Reviver that reconstructs Dates
let data = JSON.parse(text, function(key, value) {
    if (key[0] === "_") return undefined;  // Remove private props
    if (typeof value === "string" && /^\d{4}-\d{2}-\d{2}T/.test(value)) {
        return new Date(value);
    }
    return value;
});

// Replacer that omits RegExp values
let json = JSON.stringify(o, (k, v) => v instanceof RegExp ? undefined : v);

// Replacer as array (whitelist)
JSON.stringify(address, ["city","state","country"]);
```

# Context & Application

Used when serializing/deserializing data that includes types not natively supported by JSON (like Dates), or when filtering sensitive or unnecessary properties.

# Examples

From the source text (p. 325-326): Reviver that reconstructs Dates from ISO strings and removes properties starting with `_`. Replacer as array: `JSON.stringify(address, ["city","state","country"])` only includes those properties.

# Relationships

## Builds Upon
- **JSON Serialization** — These functions customize the basic stringify/parse behavior

# Common Errors

- **Error**: Defining a custom `toJSON()` and replacer without a matching reviver.
  **Correction**: If you customize serialization, you typically need a custom reviver to reconstruct the original data.

# Common Confusions

- **Confusion**: Expecting the reviver to be called for objects and arrays.
  **Clarification**: The reviver is called only for primitive values within the parsed structure, not for the container objects/arrays themselves.

# Source Reference

Chapter 11: The JavaScript Standard Library, Section 11.6.1, pages 325-326.

# Verification Notes

- Definition source: Synthesized from source text
- Confidence rationale: High
- Uncertainties: None
- Cross-reference status: Verified
