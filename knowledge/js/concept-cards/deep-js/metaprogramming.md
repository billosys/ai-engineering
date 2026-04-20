---
# === CORE IDENTIFICATION ===
concept: Metaprogramming
slug: metaprogramming

# === CLASSIFICATION ===
category: metaprogramming
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Deep JavaScript"
source_slug: deep-js
authors: "Dr. Axel Rauschmayer"
chapter: "Metaprogramming with Proxies"
chapter_number: 20
section: "20.2 Programming versus metaprogramming"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "reflective metaprogramming"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - proxy
  - reflect-api
  - introspection
  - self-modification
  - intercession
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a Proxy in JavaScript?"
---

# Quick Definition

Metaprogramming is programming that processes or manipulates program code itself, operating at a meta level above the base (application) level.

# Core Definition

From "Deep JavaScript" (Ch 20.2): "In programming, there are levels: At the *base level* (also called: *application level*), code processes user input. At the *meta level*, code processes base level code." Three kinds of reflective metaprogramming are distinguished (per Kiczales et al.): introspection (read-only access to program structure), self-modification (changing program structure), and intercession (redefining semantics of language operations).

# Prerequisites

None (foundational concept for understanding Proxies).

# Key Properties

1. Operates at the meta level, processing base-level code
2. Three kinds: introspection, self-modification, intercession
3. Base and meta level can be the same language (JavaScript)
4. Proxies bring intercession to JavaScript; `Object.*` methods provide introspection

# Construction / Recognition

## To Construct/Create:
1. Use `Object.keys()` for introspection
2. Use bracket operators and `delete` for self-modification
3. Use Proxies for intercession

## To Identify/Recognize:
1. Code that examines, modifies, or redefines the behavior of other code at runtime

# Context & Application

Understanding metaprogramming is necessary to grasp why Proxies exist. Before Proxies, JavaScript supported introspection and self-modification but not intercession.

# Examples

**Example 1** (Ch 20): Introspection:
```js
for (const key of Object.keys(obj)) {
  console.log(key);
}
```

**Example 2** (Ch 20): Self-modification:
```js
function moveProperty(source, propertyName, target) {
  target[propertyName] = source[propertyName];
  delete source[propertyName];
}
```

# Relationships

## Enables
- **Proxy** — Proxies bring intercession to JavaScript
- **Reflect API** — Provides metaprogramming operations as functions

## Related
- **Introspection** — Read-only access to program structure
- **Self-modification** — Changing program structure
- **Intercession** — Redefining language operation semantics

# Common Errors

- **Error**: Thinking metaprogramming requires a separate language
  **Correction**: JavaScript can be both the meta language and the base language

# Common Confusions

- **Confusion**: All `Object.*` methods are normal programming
  **Clarification**: Many `Object.*` methods (e.g., `Object.keys()`, `Object.defineProperty()`) are actually metaprogramming operations

# Source Reference

Chapter 20: Metaprogramming with Proxies, Section 20.2, lines 9133+.

# Verification Notes

- Definition source: direct from source text
- Confidence rationale: Explicitly defined with academic reference (Kiczales et al.)
- Cross-reference status: verified
