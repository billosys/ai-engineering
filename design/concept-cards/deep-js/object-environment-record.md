---
# === CORE IDENTIFICATION ===
concept: Object Environment Record
slug: object-environment-record

# === CLASSIFICATION ===
category: language-mechanics
subcategory: environments
tier: intermediate

# === PROVENANCE ===
source: "Deep JavaScript"
source_slug: deep-js
authors: "Dr. Axel Rauschmayer"
chapter: "A detailed look at global variables"
chapter_number: 5
section: "5.5.2 Creating variables: declarative record vs. object record"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - object record

# === TYPED RELATIONSHIPS ===
prerequisites:
  - environment-record
  - global-object
  - global-environment
extends:
  - environment-record
related:
  - declarative-environment-record
  - script-scope
contrasts_with:
  - declarative-environment-record

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does the global scope differ from module scope?"
---

# Quick Definition

An object environment record stores variable bindings as properties of a JavaScript object (in the global case, the global object), used for `var` and function declarations at the global scope level.

# Core Definition

As described in "Deep JavaScript" (Ch 5, Section 5.5): "An *object environment record* has the same interface as a normal environment record, but keeps its bindings in a JavaScript object. In this case, the object is the global object." In the global environment, "Top-level `var` and function declarations create bindings in the object environment record." This means these declarations become properties of the global object.

# Prerequisites

- **Environment record** — An object record is a type of environment record.
- **Global object** — The backing JavaScript object for the record.
- **Global environment** — Contains an object environment record.

# Key Properties

1. Stores bindings as **properties of a JavaScript object**.
2. In the global environment, the backing object is the **global object**.
3. Stores `var` and function declaration bindings at the global level.
4. Bindings **are** properties of the global object (accessible via `globalThis`).
5. Contains built-in ECMAScript globals and host platform globals.
6. Same interface as a declarative record, different storage mechanism.

# Construction / Recognition

## To Construct/Create:
1. Declare variables with `var` or function declarations at the top level of a script.
2. Assign properties to `globalThis`.

## To Identify/Recognize:
1. Variables that are accessible as `globalThis.variableName`.

# Context & Application

The object environment record explains the legacy behavior where `var` declarations and function declarations at the top level become properties of the global object. This is considered a design mistake, which is why `let`/`const`/`class` use the declarative record instead. The object record also holds all built-in globals like `Array`, `Object`, `Math`, `console`, etc.

# Examples

**Example 1** (Ch 5): `var` creates object record bindings:
```html
<script>
  var two = 2;
</script>
<script>
  console.log(globalThis.two); // 2 (on global object)
</script>
```

**Example 2** (Ch 5): `var` can collide with host globals:
```js
// Changes the location of the current document:
var location = 'https://example.com';

// Shadows window.location, doesn't change it:
let location = 'https://example.com';
```
`var location` modifies the global object's `location` property (dangerous). `let location` creates a declarative record binding that shadows it (safe).

# Relationships

## Builds Upon
- **Environment record** — Object record is a subtype.
- **Global object** — The backing store for bindings.

## Enables
- **Legacy global access** — `var` declarations accessible via `globalThis`.
- **Built-in global access** — ECMAScript built-ins stored as global object properties.

## Related
- **Script scope** — Object record is part of the global scope.

## Contrasts With
- **Declarative environment record** — Internal storage; `let`/`const`/`class` bindings not on global object.

# Common Errors

- **Error**: Using `var` at the global level for a variable name that collides with a browser built-in.
  **Correction**: `var location = ...` modifies `window.location`. Use `let` or `const` to avoid polluting the global object.

# Common Confusions

- **Confusion**: The object environment record and the global object are different things.
  **Clarification**: The object environment record *uses* the global object for storage. They are not the same — the record provides the environment record interface; the global object provides the storage.

# Source Reference

Chapter 5: A detailed look at global variables, Section 5.5.2, lines 214-240.

# Verification Notes

- Definition source: direct (quoted from source)
- Confidence rationale: Explicit definition with examples
- Cross-reference status: verified
