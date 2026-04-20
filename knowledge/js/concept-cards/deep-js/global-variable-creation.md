---
# === CORE IDENTIFICATION ===
concept: Global Variable Creation
slug: global-variable-creation

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
section: "5.5.2 Creating variables: declarative record vs. object record"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - global declaration rules

# === TYPED RELATIONSHIPS ===
prerequisites:
  - global-environment
  - declarative-environment-record
  - object-environment-record
  - script-scope
extends: []
related:
  - global-object
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does the global scope differ from module scope?"
---

# Quick Definition

Global variable creation in JavaScript follows different rules depending on the declaration keyword: `const`/`let`/`class` create bindings in the declarative environment record, while `var`/function declarations create bindings in the object environment record (global object).

# Core Definition

As described in "Deep JavaScript" (Ch 5, Section 5.5.2): "In order to create a variable that is truly global, we must be in global scope -- which is only the case at the top level of scripts." The rules are: "Top-level `const`, `let`, and `class` create bindings in the declarative environment record. Top-level `var` and function declarations create bindings in the object environment record." This means `const`/`let`/`class` are globally accessible but not on the global object, while `var`/functions become global object properties.

# Prerequisites

- **Global environment** — Global variables live in the global environment.
- **Declarative environment record** — Stores `let`/`const`/`class` bindings.
- **Object environment record** — Stores `var`/function bindings.
- **Script scope** — Must be at the top level of a script.

# Key Properties

1. `const`, `let`, `class` at script top level create **declarative record** bindings.
2. `var`, function declarations at script top level create **object record** bindings.
3. Object record bindings are properties of `globalThis`.
4. Declarative record bindings are **not** properties of `globalThis`.
5. When both records have a binding, the **declarative record wins**.
6. Must be in **global scope** (top level of scripts, not modules).

# Construction / Recognition

## To Construct/Create:
1. Use `var x = value` at script top level for a global object property.
2. Use `const x = value` at script top level for a declarative global.
3. Use `globalThis.x = value` to explicitly create a global object property.

## To Identify/Recognize:
1. Check if a variable is on `globalThis` — if yes, it's in the object record.
2. If globally accessible but not on `globalThis`, it's in the declarative record.

# Context & Application

Understanding global variable creation rules is essential for avoiding accidental collisions with browser built-in properties. The author notes that "The global object is generally considered to be a mistake" and recommends `const`/`let`/`class` to avoid global object pollution. Using `const`/`let` "guarantees that global variable declarations aren't influencing (or influenced by) the built-in global variables of ECMAScript and host platform."

# Examples

**Example 1** (Ch 5): Declaration types and their records:
```html
<script>
  const one = 1;    // declarative record
  var two = 2;      // object record

  console.log(globalThis.one); // undefined
  console.log(globalThis.two); // 2
</script>
```

**Example 2** (Ch 5): The danger of `var` at global scope:
```js
// Changes the location of the current document:
var location = 'https://example.com';

// Shadows window.location, doesn't change it:
let location = 'https://example.com';
```

# Relationships

## Builds Upon
- **Global environment** — The environment where global variables are stored.
- **Declarative environment record** — One of the two storage mechanisms.
- **Object environment record** — The other storage mechanism.

## Enables
- **Safe global declarations** — Understanding the rules allows avoiding global object pollution.

## Related
- **Global object** — The backing store for object record bindings.

## Contrasts With
- None directly.

# Common Errors

- **Error**: Using `var` at global scope for a name that collides with a built-in browser global.
  **Correction**: Use `let` or `const` to avoid modifying the global object's properties.

# Common Confusions

- **Confusion**: All top-level declarations create global object properties.
  **Clarification**: Only `var` and function declarations create global object properties. `const`/`let`/`class` do not.

# Source Reference

Chapter 5: A detailed look at global variables, Sections 5.5.2-5.5.4, lines 214-308.

# Verification Notes

- Definition source: direct (quoted from source)
- Confidence rationale: Explicit rules with examples
- Cross-reference status: verified
