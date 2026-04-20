---
# === CORE IDENTIFICATION ===
concept: Intercession
slug: intercession

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
aliases:
  - "interceding"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - metaprogramming
extends: []
related:
  - proxy
  - introspection
  - self-modification
contrasts_with:
  - introspection
  - self-modification

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a Proxy in JavaScript?"
---

# Quick Definition

Intercession is a kind of reflective metaprogramming where a program redefines the semantics of language operations, and Proxies are JavaScript's mechanism for achieving this.

# Core Definition

From "Deep JavaScript" (Ch 20.2.1): "**Intercession:** We can redefine the semantics of some language operations." And from (Ch 20.3): "Proxies bring intercession to JavaScript." Before ES6, JavaScript supported introspection and self-modification but not intercession.

The text notes: "The verb form of 'intercession' is 'to intercede'. Interceding is bidirectional in nature. Intercepting is unidirectional in nature."

# Prerequisites

- **Metaprogramming** — Intercession is one of three kinds of reflective metaprogramming

# Key Properties

1. Redefines semantics of language operations (property access, function calls, etc.)
2. ECMAScript 5 did not support intercession; Proxies fill that gap
3. Bidirectional in nature (vs. interception which is unidirectional)

# Construction / Recognition

## To Construct/Create:
1. Use Proxies to intercede in language operations

## To Identify/Recognize:
1. Code that changes what a language operation *means*, not just what it *does*

# Context & Application

Intercession is the most powerful form of metaprogramming. It enables custom property access semantics, virtualized objects, and control over fundamental operations.

# Examples

**Example 1** (Ch 20): Proxy as intercession:
```js
const proxy = new Proxy(target, {
  get(target, propKey, receiver) {
    return 123; // redefines what property access means
  }
});
```

# Relationships

## Builds Upon
- **Metaprogramming** — The most powerful kind

## Enables
- **Proxy** — Proxies are JavaScript's intercession mechanism

## Contrasts With
- **Introspection** — Read-only access vs. redefining semantics
- **Self-modification** — Changing structure vs. redefining operations

# Common Confusions

- **Confusion**: Intercession and interception are the same
  **Clarification**: "Interceding is bidirectional in nature. Intercepting is unidirectional in nature."

# Source Reference

Chapter 20: Metaprogramming with Proxies, Sections 20.2.1, 20.3, lines 9133+.

# Verification Notes

- Definition source: direct from source text
- Confidence rationale: Explicitly defined
- Cross-reference status: verified (references Kiczales et al.)
