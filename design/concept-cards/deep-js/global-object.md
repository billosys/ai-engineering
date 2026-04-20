---
# === CORE IDENTIFICATION ===
concept: Global Object
slug: global-object

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
  - window object
  - global

# === TYPED RELATIONSHIPS ===
prerequisites:
  - environment
  - lexical-environment
extends: []
related:
  - global-this
  - object-environment-record
  - global-environment
  - window-proxy
contrasts_with:
  - declarative-environment-record

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does the global scope differ from module scope?"
---

# Quick Definition

The global object is a JavaScript object whose properties become global variables, accessible via `globalThis` on all platforms.

# Core Definition

As described in "Deep JavaScript" (Ch 5, Section 5.3): "The global object is an object whose properties become global variables." It can be accessed via `globalThis` (all platforms), `window` (browsers, excluding Web Workers), `self` (all browser contexts), or `global` (Node.js). The global object serves as the backing store for the object environment record in the global environment.

# Prerequisites

- **Environment** — The global object is part of the global environment.
- **Lexical environment** — The global object backs one of the two records in the global environment.

# Key Properties

1. Properties of the global object are global variables.
2. Accessed via `globalThis` (standardized, all platforms).
3. Platform-specific aliases: `window` (browser), `self` (browser + workers), `global` (Node.js).
4. Contains built-in ECMAScript globals (e.g., `Array`, `Object`, `Math`).
5. Contains host platform globals (e.g., `document`, `console`).
6. Backs the **object environment record** of the global environment.
7. `var` and function declarations at script top level create properties on it.

# Construction / Recognition

## To Construct/Create:
1. The global object is created automatically by the JavaScript runtime.
2. Properties can be added via `globalThis.propName = value` or via `var` declarations at script scope.

## To Identify/Recognize:
1. Access via `globalThis` in any JavaScript environment.

# Context & Application

The global object is generally considered a design mistake, which is why modern declarations (`const`, `let`, `class`) do not create properties on it. In modern code, most work happens in modules which have their own scope. The global object primarily matters for built-in globals and legacy code.

# Examples

**Example 1** (Ch 5): `var` creates global object properties; `const` does not:
```html
<script>
  const one = 1;
  var two = 2;
</script>
<script>
  console.log(one); // 1
  console.log(two); // 2

  // Not all declarations create properties of the global object:
  console.log(globalThis.one); // undefined
  console.log(globalThis.two); // 2
</script>
```

# Relationships

## Builds Upon
- **Lexical environment** — The global object backs one of the environment records.

## Enables
- **Object environment record** — The global object provides the storage for this record.
- **Legacy global variables** — `var` and function declarations at top level become global object properties.

## Related
- **globalThis** — The standard way to access the global object.
- **WindowProxy** — In browsers, `globalThis` points to WindowProxy, not directly to the Window object.

## Contrasts With
- **Declarative environment record** — Modern declarations (`let`, `const`, `class`) use the declarative record, not the global object.

# Common Errors

- **Error**: Expecting `const` declarations to appear on `globalThis`.
  **Correction**: Only `var` and function declarations create properties on the global object. `const`, `let`, and `class` use the declarative environment record.

# Common Confusions

- **Confusion**: All global variables are properties of the global object.
  **Clarification**: Only variables declared with `var` or function declarations at script top level are global object properties. `let`/`const`/`class` declarations are in the declarative record and not on the global object.

# Source Reference

Chapter 5: A detailed look at global variables, Section 5.3, lines 81-101.

# Verification Notes

- Definition source: direct (quoted from source)
- Confidence rationale: Explicit definition provided
- Cross-reference status: verified
