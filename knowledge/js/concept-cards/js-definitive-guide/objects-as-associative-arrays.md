---
# === CORE IDENTIFICATION ===
concept: Objects as Associative Arrays
slug: objects-as-associative-arrays

# === CLASSIFICATION ===
category: objects
subcategory: property-access
tier: foundational

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Objects"
chapter_number: 6
pdf_page: 151
section: "6.3.1 Objects As Associative Arrays"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "hash map"
  - "dictionary"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - property-access-expressions
  - objects-as-property-collections
extends: []
related:
  - for-in-loop
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes Object.keys() from for/in?"
---

# Quick Definition

JavaScript objects can be used as associative arrays (hash maps/dictionaries) via bracket notation, where string-valued expressions are used as dynamic property names.

# Core Definition

"The second syntax, using square brackets and a string, looks like array access, but to an array indexed by strings rather than by numbers. This kind of array is known as an *associative array* (or hash or map or dictionary). JavaScript objects are associative arrays." Bracket notation allows property names to be computed at runtime, unlike dot notation which requires static identifiers. (Ch. 6, §6.3.1)

# Prerequisites

- **property-access-expressions** — Bracket notation enables dynamic property access.
- **objects-as-property-collections** — Objects store string-to-value mappings.

# Key Properties

1. Bracket notation `object["property"]` accepts any string expression.
2. Property names can be constructed dynamically at runtime.
3. Dot notation requires static identifier names.
4. ES6 `Map` class is often a better choice for associative array use cases.

# Construction / Recognition

```js
let portfolio = {};
portfolio[stockname] = shares;    // Dynamic property name
let value = portfolio[stockname]; // Dynamic property access
```

# Context & Application

Objects are commonly used as dictionaries/maps when keys are strings. This pattern is foundational for configuration objects, lookup tables, and data aggregation. For more complex use cases, `Map` is preferred.

# Examples

From the source text (§6.3.1, pp. 151-152):

```js
// Dynamic property access with runtime names
let addr = "";
for(let i = 0; i < 4; i++) {
    addr += customer[`address${i}`] + "\n";
}

// Using objects as dictionaries
function addstock(portfolio, stockname, shares) {
    portfolio[stockname] = shares;
}

function computeValue(portfolio) {
    let total = 0.0;
    for(let stock in portfolio) {
        let shares = portfolio[stock];
        let price = getQuote(stock);
        total += shares * price;
    }
    return total;
}
```

# Relationships

## Builds Upon
- **property-access-expressions** — Bracket notation is the mechanism
- **objects-as-property-collections** — Objects are the underlying data structure

## Enables
- Dynamic property manipulation patterns

## Related
- **for-in-loop** — Used to iterate all keys in an associative array

## Contrasts With
- No direct contrast; ES6 Map mentioned as a modern alternative

# Common Errors

- **Error**: Using dot notation when the property name is stored in a variable.
  **Correction**: Dot notation only works with literal identifiers. Use bracket notation for dynamic names: `obj[varName]`.

# Common Confusions

- **Confusion**: Believing objects are the only associative data structure in JavaScript.
  **Clarification**: "In ES6 and later, the Map class described in §11.1.2 is often a better choice than using a plain object."

# Source Reference

Chapter 6: Objects, Section 6.3.1, pages 151-152.

# Verification Notes

- Definition source: Direct quote from §6.3.1
- Confidence rationale: High — clear with practical examples
- Uncertainties: None
- Cross-reference status: Verified
