---
# === CORE IDENTIFICATION ===
concept: JSON Serialization
slug: json-serialization

# === CLASSIFICATION ===
category: objects
subcategory: serialization
tier: intermediate

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Objects"
chapter_number: 6
pdf_page: 160
section: "6.8 Serializing Objects"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "JSON.stringify()"
  - "JSON.parse()"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - objects-as-property-collections
  - own-vs-inherited-properties
extends: []
related:
  - to-json-method
  - object-assign
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes shallow copy from deep copy of objects?"
---

# Quick Definition

`JSON.stringify()` converts an object's state to a JSON string; `JSON.parse()` restores it. Only enumerable own properties with serializable values are included. Functions, RegExp, Error, and `undefined` are omitted.

# Core Definition

"Object *serialization* is the process of converting an object's state to a string from which it can later be restored. The functions JSON.stringify() and JSON.parse() serialize and restore JavaScript objects." "JSON.stringify() serializes only the enumerable own properties of an object. If a property value cannot be serialized, that property is simply omitted." (Ch. 6, §6.8)

# Prerequisites

- **objects-as-property-collections** — Serialization operates on an object's properties.
- **own-vs-inherited-properties** — Only own enumerable properties are serialized.

# Key Properties

1. Supported types: objects, arrays, strings, finite numbers, `true`, `false`, `null`.
2. `NaN`, `Infinity`, `-Infinity` serialize to `null`.
3. Date objects serialize to ISO strings but `JSON.parse()` does not restore them as Dates.
4. Functions, RegExp, Error, and `undefined` cannot be serialized.
5. Non-serializable property values are silently omitted.
6. Both functions accept optional second arguments for customization.
7. JSON syntax is a subset of JavaScript syntax.

# Construction / Recognition

```js
let s = JSON.stringify(object);
let o = JSON.parse(s);
```

# Context & Application

JSON serialization is the primary mechanism for data interchange in web applications, API communication, and persistent storage. Understanding its limitations (no functions, no circular references, no Date restoration) is essential.

# Examples

From the source text (§6.8, pp. 160-161):

```js
let o = {x: 1, y: {z: [false, null, ""]}};
let s = JSON.stringify(o);    // s == '{"x":1,"y":{"z":[false,null,""]}}'
let p = JSON.parse(s);        // p == {x: 1, y: {z: [false, null, ""]}}
```

# Relationships

## Builds Upon
- **objects-as-property-collections** — Serialization operates on properties
- **own-vs-inherited-properties** — Only own enumerable properties are serialized

## Enables
- Data interchange and persistence

## Related
- **to-json-method** — Custom serialization via `toJSON()`
- **object-assign** — Alternative for copying (but not serialization)

## Contrasts With
- No direct contrast

# Common Errors

- **Error**: Expecting `JSON.parse(JSON.stringify(date))` to restore a Date object.
  **Correction**: Dates are serialized as strings and are not automatically restored as Date objects.

- **Error**: Expecting functions or `undefined` to appear in serialized output.
  **Correction**: These values are silently omitted from the output.

# Common Confusions

- **Confusion**: Using `JSON.stringify()`/`JSON.parse()` as a deep copy mechanism.
  **Clarification**: While `JSON.parse(JSON.stringify(obj))` creates a deep copy, it loses functions, Dates, `undefined` values, and any non-JSON-serializable data.

# Source Reference

Chapter 6: Objects, Section 6.8, pages 160-161.

# Verification Notes

- Definition source: Direct quote from §6.8
- Confidence rationale: High — clear description with limitations
- Uncertainties: None
- Cross-reference status: Verified
