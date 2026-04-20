---
# === CORE IDENTIFICATION ===
concept: globalThis
slug: global-this

# === CLASSIFICATION ===
category: language-mechanics
subcategory: scoping
tier: intermediate

# === PROVENANCE ===
source: "Deep JavaScript"
source_slug: deep-js
authors: "Dr. Axel Rauschmayer"
chapter: "A detailed look at global variables"
chapter_number: 5
section: "5.3 The global object"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "window"
  - "self"
  - "global"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - global-object
extends: []
related:
  - window-proxy
  - global-environment
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does the global scope differ from module scope?"
---

# Quick Definition

`globalThis` is the standardized global variable that provides access to the global object on all JavaScript platforms, with its name reflecting that it has the same value as `this` in global scope.

# Core Definition

As described in "Deep JavaScript" (Ch 5, Section 5.3): `globalThis` is "[a]vailable on all platforms" for accessing the global object. "The name is based on the fact that it has the same value as `this` in global scope." Other platform-specific alternatives include `window` (browsers, not Web Workers/Node.js), `self` (browsers including Web Workers, not Node.js), and `global` (Node.js only).

# Prerequisites

- **Global object** — `globalThis` provides access to the global object.

# Key Properties

1. Available on **all platforms** (browsers, Node.js, Web Workers, etc.).
2. Name reflects `this` in global scope.
3. In browsers, points to `WindowProxy`, not directly to `Window`.
4. Standardized replacement for platform-specific `window`/`self`/`global`.

# Construction / Recognition

## To Construct/Create:
1. Simply reference `globalThis` in any JavaScript environment.

## To Identify/Recognize:
1. The identifier `globalThis` anywhere in code.

# Context & Application

`globalThis` solves the problem of accessing the global object in cross-platform code. Before its introduction, code had to detect the platform and use `window`, `self`, or `global` accordingly. It is particularly useful in libraries that must work across browsers, Node.js, and Web Workers.

# Examples

**Example 1** (Ch 5): Accessing global variables:
```js
console.log(globalThis.two); // 2  (if var two = 2 was declared)
console.log(globalThis.one); // undefined (if const one = 1 was declared)
```

# Relationships

## Builds Upon
- **Global object** — `globalThis` provides access to it.

## Enables
- **Cross-platform global access** — Works everywhere without platform detection.

## Related
- **WindowProxy** — In browsers, `globalThis` actually points to WindowProxy.

## Contrasts With
- None directly.

# Common Errors

- **Error**: Assuming `globalThis` changes in browsers when an iframe's URL changes.
  **Correction**: `globalThis` always points to the same `WindowProxy`, even when the underlying `Window` object changes.

# Common Confusions

- **Confusion**: `globalThis` is the global object itself.
  **Clarification**: In browsers, `globalThis` is actually `WindowProxy`, which forwards to the current `Window`. In other environments, it directly references the global object.

# Source Reference

Chapter 5: A detailed look at global variables, Section 5.3, lines 86-101.

# Verification Notes

- Definition source: direct (quoted from source)
- Confidence rationale: Explicit definition provided
- Cross-reference status: verified
