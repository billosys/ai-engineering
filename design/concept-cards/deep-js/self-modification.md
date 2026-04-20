---
# === CORE IDENTIFICATION ===
concept: Self-Modification
slug: self-modification

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
  - introspection
  - intercession
contrasts_with:
  - introspection
  - intercession

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a Proxy in JavaScript?"
---

# Quick Definition

Self-modification is a kind of reflective metaprogramming where a program changes its own structure at runtime.

# Core Definition

From "Deep JavaScript" (Ch 20.2.1): "**Self-modification:** We can change that structure." Example: the `moveProperty` function modifies object structure using bracket operators and the `delete` operator.

# Prerequisites

- **Metaprogramming** — Self-modification is one of three kinds of reflective metaprogramming

# Key Properties

1. Changes program structure at runtime (adding/removing properties, etc.)
2. Available in JavaScript via bracket operators, assignment, `delete`, `Object.defineProperty()`
3. More invasive than introspection but less powerful than intercession

# Construction / Recognition

## To Construct/Create:
1. Use `delete`, property assignment, `Object.defineProperty()`, etc.

## To Identify/Recognize:
1. Code that modifies its own object structure at runtime

# Context & Application

Self-modification was available in JavaScript before Proxies. It is the middle ground between read-only introspection and semantic-changing intercession.

# Examples

**Example 1** (Ch 20):
```js
function moveProperty(source, propertyName, target) {
  target[propertyName] = source[propertyName];
  delete source[propertyName];
}
```

# Relationships

## Builds Upon
- **Metaprogramming** — A specific kind

## Contrasts With
- **Introspection** — Read-only vs. modifying
- **Intercession** — Modifying structure vs. redefining semantics

# Common Confusions

- **Confusion**: Self-modification is the same as intercession
  **Clarification**: Self-modification changes structure; intercession redefines the meaning of operations

# Source Reference

Chapter 20: Metaprogramming with Proxies, Section 20.2.1, lines 9133+.

# Verification Notes

- Definition source: direct from source text
- Confidence rationale: Explicitly defined with example
- Cross-reference status: verified
