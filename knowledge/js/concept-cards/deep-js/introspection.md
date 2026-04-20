---
# === CORE IDENTIFICATION ===
concept: Introspection
slug: introspection

# === CLASSIFICATION ===
category: metaprogramming
subcategory: reflection
tier: advanced

# === PROVENANCE ===
source: "Deep JavaScript"
source_slug: deep-js
authors: "Dr. Axel Rauschmayer"
chapter: "Metaprogramming with Proxies"
chapter_number: 20
section: "20.2.1 Kinds of metaprogramming"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - metaprogramming
extends: []
related:
  - self-modification
  - intercession
contrasts_with:
  - self-modification
  - intercession

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a Proxy in JavaScript?"
---

# Quick Definition

Introspection is a kind of reflective metaprogramming where a program has read-only access to its own structure.

# Core Definition

From "Deep JavaScript" (Ch 20.2.1): "**Introspection:** We have read-only access to the structure of a program." Example: `Object.keys()` performs introspection by examining an object's properties at runtime.

# Prerequisites

- **Metaprogramming** — Introspection is one of three kinds of reflective metaprogramming

# Key Properties

1. Read-only -- does not modify program structure
2. Available in JavaScript via `Object.keys()`, `typeof`, `instanceof`, etc.
3. The least invasive form of metaprogramming

# Construction / Recognition

## To Construct/Create:
1. Use `Object.keys()`, `Object.getOwnPropertyDescriptor()`, `typeof`, etc.

## To Identify/Recognize:
1. Code that examines program structure without modifying it

# Context & Application

Introspection was available in JavaScript long before Proxies. It is the safest form of metaprogramming.

# Examples

**Example 1** (Ch 20):
```js
const obj = { hello() { console.log('Hello!'); } };
for (const key of Object.keys(obj)) {
  console.log(key); // introspection
}
```

# Relationships

## Builds Upon
- **Metaprogramming** — A specific kind

## Contrasts With
- **Self-modification** — Introspection is read-only; self-modification changes structure
- **Intercession** — Introspection reads; intercession redefines semantics

# Common Confusions

- **Confusion**: `Object.keys()` is normal programming, not metaprogramming
  **Clarification**: Examining an object's structure at runtime is metaprogramming, even though it looks like normal code in JavaScript

# Source Reference

Chapter 20: Metaprogramming with Proxies, Section 20.2.1, lines 9133+.

# Verification Notes

- Definition source: direct from source text
- Confidence rationale: Explicitly defined with example
- Cross-reference status: verified (references Kiczales et al.)
