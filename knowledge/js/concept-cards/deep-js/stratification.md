---
# === CORE IDENTIFICATION ===
concept: Stratification
slug: stratification

# === CLASSIFICATION ===
category: metaprogramming
subcategory: proxies
tier: advanced

# === PROVENANCE ===
source: "Deep JavaScript"
source_slug: deep-js
authors: "Dr. Axel Rauschmayer"
chapter: "Metaprogramming with Proxies"
chapter_number: 20
section: "20.5.1 Stratification: keeping base level and meta level separate"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "level separation"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - proxy
  - metaprogramming
extends: []
related:
  - proxy-handler
  - proxy-target
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a Proxy in JavaScript?"
---

# Quick Definition

Stratification is the Proxy API design principle that keeps the base level (the Proxy object) and the meta level (the handler object) separate, avoiding the problems of mixing programming levels.

# Core Definition

From "Deep JavaScript" (Ch 20.5.1): "Proxies are *stratified*: Base level (the Proxy object) and meta level (the handler object) are separate." This avoids the problem of Firefox's old `__noSuchMethod__` approach where "base level (normal methods) and meta level (`__noSuchMethod__`) are mixed. Base-level code may accidentally invoke or see a meta level method and there is the possibility of accidentally defining a meta level method."

# Prerequisites

- **Proxy** — Stratification is a design principle of the Proxy API
- **Metaprogramming** — Understanding base vs. meta level

# Key Properties

1. The Proxy (base level) and handler (meta level) are separate objects
2. Prevents accidental interaction between normal code and metaprogramming code
3. Avoids problems like `obj.hasOwnProperty` being overridable
4. Handler encapsulation: the handler cannot be accessed via the Proxy

# Construction / Recognition

## To Construct/Create:
1. The Proxy API enforces stratification by design -- handler is always separate

## To Identify/Recognize:
1. The separation between the Proxy object (used by base-level code) and the handler (meta-level configuration)

# Context & Application

Stratification explains why Proxies use a separate handler object rather than special methods on the target. This prevents the mixing of levels that caused problems with earlier approaches like `__noSuchMethod__`.

# Examples

**Example 1** (Ch 20): Problem with non-stratified approach:
```js
// __noSuchMethod__ mixes base and meta levels:
const calc = {
  __noSuchMethod__: function (methodName, args) { ... }
};
// Base-level code can accidentally interact with meta-level method
```

**Example 2** (Ch 20): Problem with base-level `hasOwnProperty`:
```js
const obj = { hasOwnProperty: null };
assert.throws(
  () => obj.hasOwnProperty('width'),
  /^TypeError: obj.hasOwnProperty is not a function/
);
```

# Relationships

## Builds Upon
- **Metaprogramming** — Stratification separates meta and base levels

## Enables
- **Safe metaprogramming** — Prevents accidental level mixing

## Related
- **Proxy handler** — The meta-level component
- **Proxy target** — Part of the base level

# Common Confusions

- **Confusion**: Putting trap-like methods on the target itself would work just as well
  **Clarification**: Mixing levels leads to naming conflicts and accidental invocations; stratification prevents this

# Source Reference

Chapter 20: Metaprogramming with Proxies, Section 20.5.1, lines 9133+.

# Verification Notes

- Definition source: direct from source text
- Confidence rationale: Explicitly defined with historical motivation
- Cross-reference status: verified
