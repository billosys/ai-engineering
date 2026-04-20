---
# === CORE IDENTIFICATION ===
concept: Global Object
slug: global-object

# === CLASSIFICATION ===
category: variables-scope
subcategory: scoping
tier: foundational

# === PROVENANCE ===
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Variables and assignment"
chapter_number: 13
pdf_page: null
section: "13.7.1 globalThis"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - globalThis
  - window
  - self
  - global

# === TYPED RELATIONSHIPS ===
prerequisites:
  - global-scope
extends: []
related:
  - var-declaration
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I declare and use variables with proper scoping?"
---

# Quick Definition

The global object is a JavaScript object that stores global object variables (created by `var` and `function` declarations in script scope), accessed cross-platform via `globalThis` (^ES2020^).

# Core Definition

"The global variable `globalThis` is the standard way of accessing the global object." (Ch. 13, &sect;13.7.1). ^ES2020^: `globalThis` provides cross-platform access (browsers, Node.js, Web Workers). It replaces platform-specific alternatives: `window` (browsers only), `self` (browsers + Web Workers), `global` (Node.js only). "The global object is now considered a mistake that JavaScript can't get rid of, due to backward compatibility."

# Prerequisites

- **global-scope** -- the global object is part of the global scope mechanism

# Key Properties

1. ^ES2020^: `globalThis` standardized
2. Stores `var` and `function` declaration variables from global script scope
3. Does NOT store `const`/`let`/`class` declarations
4. Cross-platform: `globalThis` works everywhere
5. Platform-specific: `window` (browser), `self` (browser + Worker), `global` (Node.js)
6. Considered a design mistake; use is discouraged in favor of modules

# Construction / Recognition

```js
// Access global object
globalThis

// Prefer variable access over property access
encodeURIComponent(str);      // yes
window.encodeURIComponent(str); // no (unnecessary prefix)
```

# Context & Application

Use `globalThis` primarily for polyfills and feature detection. For normal code, prefer modules and local scope.

# Examples

From the source text (Ch. 13, &sect;13.7.1):
```js
// Prefer:
encodeURIComponent(str);
// Not:
window.encodeURIComponent(str);
```

Platform availability:
- `globalThis`: browser, Web Workers, Node.js
- `window`: browser only
- `self`: browser + Web Workers
- `global`: Node.js only

# Relationships

## Builds Upon
- **global-scope** -- the global object is part of global scope

## Enables
- Polyfills and feature detection

## Related
- **var-declaration** -- var creates global object properties in global scope

## Contrasts With
- No direct contrast

# Common Errors

- **Error**: Using `window.` prefix for global functions like `encodeURIComponent`.
  **Correction**: Access global functions directly; the prefix is unnecessary.

# Common Confusions

- **Confusion**: Thinking all global variables are on the global object.
  **Clarification**: Only `var` and `function` declarations create global object properties. `const`/`let` do not.

# Source Reference

Chapter 13: Variables and assignment, Section 13.7.1, lines 406-576.

# Verification Notes

- Definition source: direct from source
- Confidence rationale: Detailed with platform compatibility table
- Cross-reference status: verified
