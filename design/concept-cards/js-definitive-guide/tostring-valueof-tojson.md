---
# === CORE IDENTIFICATION ===
concept: toString(), valueOf(), and toJSON() Methods
slug: tostring-valueof-tojson

# === CLASSIFICATION ===
category: objects
subcategory: object-methods
tier: intermediate

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Objects"
chapter_number: 6
pdf_page: 161
section: "6.9 Object Methods"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "object conversion methods"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - objects-as-property-collections
  - prototype-chain
extends: []
related:
  - json-serialization
  - addition-operator
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the prototype chain?"
---

# Quick Definition

`toString()` converts an object to a string, `valueOf()` converts it to a primitive (typically a number), and `toJSON()` customizes JSON serialization. All three are inherited from `Object.prototype` (except `toJSON`) and can be overridden.

# Core Definition

"The toString() method takes no arguments; it returns a string that somehow represents the value of the object on which it is invoked." "The valueOf() method is much like the toString() method, but it is called when JavaScript needs to convert an object to some primitive type other than a string — typically, a number." "Object.prototype does not actually define a toJSON() method, but the JSON.stringify() method looks for a toJSON() method on any object it is asked to serialize." (Ch. 6, §6.9)

# Prerequisites

- **objects-as-property-collections** — These methods are properties of objects.
- **prototype-chain** — These methods are inherited from Object.prototype.

# Key Properties

1. Default `toString()` returns `"[object Object]"` — not useful; override for custom representation.
2. `toString()` is called for string conversion (e.g., with `+` operator).
3. `valueOf()` is called for numeric conversion (e.g., with comparison operators).
4. `toJSON()` is called by `JSON.stringify()` if present; its return value is serialized instead of the object.
5. Date defines useful `toJSON()` returning an ISO date string.

# Construction / Recognition

```js
let point = {
    x: 1, y: 2,
    toString() { return `(${this.x}, ${this.y})`; },
    valueOf() { return Math.hypot(this.x, this.y); },
    toJSON() { return this.toString(); }
};
```

# Context & Application

Overriding these methods allows objects to participate naturally in string concatenation, numeric comparisons, and JSON serialization. They are the hooks for customizing object-to-primitive conversion.

# Examples

From the source text (§6.9, pp. 161-163):

```js
let s = { x: 1, y: 1 }.toString();  // s == "[object Object]"

let point = {
    x: 1, y: 2,
    toString: function() { return `(${this.x}, ${this.y})`; }
};
String(point)  // => "(1, 2)"

let point = {
    x: 3, y: 4,
    valueOf: function() { return Math.hypot(this.x, this.y); }
};
Number(point)  // => 5
point > 4      // => true

let point = {
    x: 1, y: 2,
    toString() { return `(${this.x}, ${this.y})`; },
    toJSON() { return this.toString(); }
};
JSON.stringify([point])  // => '["(1, 2)"]'
```

# Relationships

## Builds Upon
- **prototype-chain** — Methods inherited from Object.prototype

## Enables
- Custom object-to-primitive conversion
- Custom serialization

## Related
- **json-serialization** — `toJSON()` customizes JSON output
- **addition-operator** — Triggers `toString()` or `valueOf()` conversion

## Contrasts With
- No direct contrast

# Common Errors

- **Error**: Forgetting to override `toString()` and getting `"[object Object]"` in string contexts.
  **Correction**: Define a custom `toString()` for meaningful string representations.

# Common Confusions

- **Confusion**: Believing `valueOf()` must return a number.
  **Clarification**: `valueOf()` should return a primitive value (any type), not necessarily a number.

# Source Reference

Chapter 6: Objects, Section 6.9, pages 161-163.

# Verification Notes

- Definition source: Direct quotes from §6.9.1, §6.9.3, §6.9.4
- Confidence rationale: High — each method clearly described with examples
- Uncertainties: None
- Cross-reference status: Verified against §3.9.3
