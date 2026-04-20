---
# === CORE IDENTIFICATION ===
concept: Naming Rules for Introspective Operations
slug: naming-rules-for-introspection

# === CLASSIFICATION ===
category: object-model
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Deep JavaScript"
source_slug: deep-js
authors: "Dr. Axel Rauschmayer"
chapter: "Enumerability of properties"
chapter_number: 13
section: "13.1.3 Naming rules for introspective operations"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "introspection naming convention"
  - "property name vs property key"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - property-key
  - enumerability
extends: []
related:
  - property-listing-operations
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes Object.keys() from Reflect.ownKeys()?"
---

# Quick Definition

JavaScript uses a naming convention for property-listing operations: short names (like `Object.keys()`) ignore non-enumerable properties; long names (like `Object.getOwnPropertyNames()`) include them. Additionally, ES6 distinguishes "property keys" (strings or symbols), "property names" (string keys), and "property symbols" (symbol keys).

# Core Definition

As described in "Deep JavaScript" Ch 13, "In JavaScript, common introspective operations have short names, while rarely used operations have long names. Ignoring non-enumerable properties is the norm, which is why operations that do that have short names and operations that don't, long names." The book also notes:
- "Property keys are either strings or symbols."
- "Property names are property keys that are strings."
- "Property symbols are property keys that are symbols."
- "Therefore, a better name for `Object.keys()` would now be `Object.names()`."

`Reflect` methods deviate from this convention because they "provide operations that are more 'meta' and related to Proxies."

# Prerequisites

- **Property Key** — the key/name/symbol terminology
- **Enumerability** — determines which naming tier an operation falls into

# Key Properties

1. Short name = ignores non-enumerable (the common case)
2. Long name = includes non-enumerable
3. "keys" = strings or symbols; "names" = strings only; "symbols" = symbols only
4. `Reflect` methods use short names but are comprehensive (exception to the rule)
5. `Object.keys()` should really be called `Object.names()`

# Construction / Recognition

## To Construct/Create:
1. Not applicable — this is a naming convention

## To Identify/Recognize:
1. Short method name on `Object` => enum-only
2. Long method name on `Object` => includes non-enum
3. `Reflect` method => comprehensive (meta-level)

# Context & Application

This naming convention helps developers choose the right operation without memorizing detailed behavior tables. When you see a short name, assume common behavior (enum-only). When you see a long name, assume comprehensive behavior.

# Examples

**Example 1** (Ch 13):
- `Object.keys()` — short, ignores non-enumerable
- `Object.getOwnPropertyNames()` — long, includes non-enumerable

# Relationships

## Builds Upon
- **property-key** — the key/name/symbol terminology
- **enumerability** — the dimension the naming convention maps to

## Enables
- Quick identification of operation behavior from method name

## Related
- **property-listing-operations** — the operations this convention applies to

## Contrasts With
- None

# Common Errors

- **Error**: Expecting `Reflect.ownKeys()` to follow the short-name convention (enum-only).
  **Correction**: `Reflect` methods are an exception — they are comprehensive despite having short names.

# Common Confusions

- **Confusion**: Thinking "keys" means "string keys."
  **Clarification**: In ES6+ terminology, "keys" means both strings and symbols. "Names" means string keys only. `Object.keys()` is misnamed by this convention.

# Source Reference

Chapter 13: Enumerability of properties, Section 13.1.3, lines 271-299.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly explained with terminology definitions.
- Cross-reference status: verified
