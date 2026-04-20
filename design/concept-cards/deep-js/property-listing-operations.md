---
# === CORE IDENTIFICATION ===
concept: Property Listing Operations
slug: property-listing-operations

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
section: "13.1 How enumerability affects property-iterating constructs"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "property-iterating constructs"
  - "introspective operations"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - enumerability
  - property-key
extends: []
related:
  - object-keys
  - reflect-own-keys
  - for-in-loop
  - object-get-own-property-names
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes Object.keys() from Reflect.ownKeys()?"
  - "What is enumerability?"
---

# Quick Definition

Property listing operations are categorized by three dimensions: whether they include non-enumerable properties, whether they include symbol keys, and whether they include inherited properties. Understanding this matrix is key to choosing the right operation.

# Core Definition

As described in "Deep JavaScript" Ch 13, property-listing operations fall into two categories:

**Enumerable-only operations** (short names):
| Operation | String keys | Symbol keys | Inherited |
|-----------|:-----------:|:-----------:|:---------:|
| `Object.keys()` | Yes | No | No |
| `Object.values()` | Yes | No | No |
| `Object.entries()` | Yes | No | No |
| `{...x}` | Yes | Yes | No |
| `Object.assign()` | Yes | Yes | No |
| `JSON.stringify()` | Yes | No | No |
| `for-in` | Yes | No | Yes |

**All-properties operations** (long names):
| Operation | String keys | Symbol keys | Inherited |
|-----------|:-----------:|:-----------:|:---------:|
| `Object.getOwnPropertyNames()` | Yes | No | No |
| `Object.getOwnPropertySymbols()` | No | Yes | No |
| `Reflect.ownKeys()` | Yes | Yes | No |
| `Object.getOwnPropertyDescriptors()` | Yes | Yes | No |

# Prerequisites

- **Enumerability** — the primary dimension that distinguishes operations
- **Property Key** — string vs. symbol key handling varies

# Key Properties

1. Short-named operations ignore non-enumerable properties (the common case)
2. Long-named operations include non-enumerable properties
3. `for-in` is the ONLY operation that includes inherited properties
4. `Object.assign()` and spreading are the only enumerable-only operations that include symbol keys
5. All "all-properties" operations are own-only

# Construction / Recognition

## To Construct/Create:
1. Choose operation based on: need enum-only vs. all? Need symbols? Need inherited?

## To Identify/Recognize:
1. Short name = enum-only; long name = all properties; `Reflect` = meta-level

# Context & Application

This classification is essential for choosing the right tool. The naming convention helps: short names for common operations (enum-only), long names for comprehensive operations.

# Examples

**Example 1** (Ch 13): The naming convention:
- `Object.keys()` — short name, ignores non-enumerable
- `Object.getOwnPropertyNames()` — long name, includes non-enumerable
- `Reflect.ownKeys()` — `Reflect` namespace, includes everything own

# Relationships

## Builds Upon
- **enumerability** — the primary filtering dimension
- **property-key** — string vs. symbol distinction

## Enables
- Choosing the right operation for a given task

## Related
- **object-keys** — most common operation
- **reflect-own-keys** — most comprehensive operation
- **for-in-loop** — only one with inherited properties

## Contrasts With
- None

# Common Errors

- **Error**: Using `Object.keys()` when you need all property keys.
  **Correction**: Use `Reflect.ownKeys()` for all own keys, or `Object.getOwnPropertyNames()` for all own string keys.

# Common Confusions

- **Confusion**: Thinking there is one "list all properties" operation.
  **Clarification**: No single operation lists all properties (own + inherited, string + symbol, enum + non-enum). You must combine operations or traverse the prototype chain manually.

# Source Reference

Chapter 13: Enumerability of properties, Section 13.1, lines 51-269.

# Verification Notes

- Definition source: synthesized from two operation tables in the source
- Confidence rationale: Tables directly from the source text, synthesized into a unified view.
- Cross-reference status: verified
