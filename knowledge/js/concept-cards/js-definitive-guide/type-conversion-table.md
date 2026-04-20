---
# === CORE IDENTIFICATION ===
concept: Type Conversion Table
slug: type-conversion-table

# === CLASSIFICATION ===
category: type-system
subcategory: type-coercion
tier: advanced

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Types, Values, and Variables"
chapter_number: 3
pdf_page: 62
section: "3.9 Type Conversions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - Table 3-2
  - conversion rules

# === TYPED RELATIONSHIPS ===
prerequisites:
  - type-coercion
extends:
  - type-coercion
related:
  - boolean-truthy-falsy
  - explicit-type-conversion
  - object-to-primitive-conversion
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is type coercion in JavaScript?"
---

# Quick Definition

Table 3-2 in the source provides the definitive reference for how every JavaScript value converts to String, Number, and Boolean, including surprising cases like `null` converting to `0` and `-0` converting to `"0"`.

# Core Definition

Table 3-2 "summarizes how values convert from one type to another in JavaScript." The conversions cover every primitive value and common object types converting to String, Number, and Boolean. Key surprising conversions are highlighted in the source. (p. 62)

# Prerequisites

- **type-coercion** — Must understand the concept of type conversion

# Key Properties

**Surprising conversions (bold in source):**

| Value | to String | to Number | to Boolean |
|---|---|---|---|
| undefined | "undefined" | **NaN** | false |
| null | "null" | **0** | false |
| true | "true" | 1 | - |
| false | "false" | **0** | - |
| "" (empty string) | - | **0** | **false** |
| "1.2" (numeric string) | - | 1.2 | true |
| "one" (non-numeric) | - | NaN | true |
| 0 | "0" | - | **false** |
| -0 | **"0"** | - | **false** |
| NaN | "NaN" | - | **false** |
| Infinity | "Infinity" | - | true |
| {} (any object) | see §3.9.3 | see §3.9.3 | **true** |
| [] (empty array) | **""** | **0** | **true** |
| [9] (one numeric element) | "9" | **9** | true |
| ['a'] (other array) | use join() | NaN | true |
| function(){} | see §3.9.3 | NaN | true |

# Construction / Recognition

Use this table as a reference when predicting JavaScript operator behavior or debugging unexpected coercion results.

# Context & Application

This table is the definitive reference for predicting JavaScript's type conversion behavior. It explains why expressions like `[] + []` produce `""` and why `null + 1` produces `1`.

# Examples

Applying the table:
```javascript
Number(null)           // => 0 (not NaN!)
Number(undefined)      // => NaN
Number("")             // => 0
Number("one")          // => NaN
String(-0)             // => "0" (not "-0")
Boolean([])            // => true (all objects are truthy)
Number([])             // => 0 ([] → "" → 0)
Number([9])            // => 9 ([9] → "9" → 9)
```

# Relationships

## Builds Upon
- **type-coercion** — This table is the detailed specification of coercion rules

## Enables
- Predicting behavior of any operator with mixed types

## Related
- **boolean-truthy-falsy** — The Boolean column matches truthy/falsy rules
- **explicit-type-conversion** — Same rules used by Boolean(), Number(), String()
- **object-to-primitive-conversion** — How objects in the table get their values

## Contrasts With
- None within this source

# Common Errors

- **Error**: Assuming `Number(null)` returns `NaN` like `Number(undefined)`.
  **Correction**: `null` converts to `0`; `undefined` converts to `NaN`. They are not symmetric.

# Common Confusions

- **Confusion**: Empty arrays are falsy because they convert to `0`.
  **Clarification**: All objects (including `[]`) are truthy. The Number conversion `[] → 0` goes through `toString()` producing `""`, then `Number("")` producing `0`. But Boolean conversion is direct: all objects → `true`.

# Source Reference

Chapter 3: Types, Values, and Variables, Section 3.9, Table 3-2, pages 62-63.

# Verification Notes

- Definition source: Reproduced from Table 3-2, pp. 62-63
- Confidence rationale: High — table directly transcribed from source
- Uncertainties: None
- Cross-reference status: Verified
