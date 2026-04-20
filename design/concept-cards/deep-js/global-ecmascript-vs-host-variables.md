---
# === CORE IDENTIFICATION ===
concept: Global ECMAScript vs. Host Variables
slug: global-ecmascript-vs-host-variables

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
section: "5.5.4 Global ECMAScript variables and global host variables"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - built-in globals

# === TYPED RELATIONSHIPS ===
prerequisites:
  - global-object
  - object-environment-record
extends: []
related:
  - global-environment
  - declarative-environment-record
  - global-variable-creation
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does the global scope differ from module scope?"
---

# Quick Definition

The global object contains two categories of built-in properties: ECMAScript standard built-in globals (like `Array`, `Object`, `Math`) and host platform globals (like `document`, `console`, `location`), both stored in the object environment record.

# Core Definition

As described in "Deep JavaScript" (Ch 5, Section 5.5.4): "In addition to variables created via `var` and function declarations, the global object contains the following properties: All built-in global variables of ECMAScript. All built-in global variables of the host platform (browser, Node.js, etc.)." Using `const` or `let` "guarantees that global variable declarations aren't influencing (or influenced by) the built-in global variables of ECMAScript and host platform."

# Prerequisites

- **Global object** — Both types of built-in globals are properties of the global object.
- **Object environment record** — Built-in globals are stored here.

# Key Properties

1. **ECMAScript built-ins**: `Array`, `Object`, `Math`, `JSON`, `Number`, `String`, etc.
2. **Host platform built-ins**: `document`, `console`, `location`, `setTimeout`, etc. (browser-specific).
3. Both are properties of the global object.
4. `var` declarations at global scope can accidentally collide with these.
5. `let`/`const` declarations are safe from such collisions.

# Construction / Recognition

## To Construct/Create:
1. Provided automatically by the runtime. Not created by user code.

## To Identify/Recognize:
1. Properties on `globalThis` that are not user-declared.

# Context & Application

This distinction matters when writing global-scope code. Using `var` to declare a variable with the same name as a host built-in (like `location`) will modify the global object property, potentially causing errors. Using `let`/`const` creates a declarative-record binding that shadows the global object property without modifying it.

# Examples

**Example 1** (Ch 5): The danger of `var` with host globals:
```js
// Changes the location of the current document (dangerous!):
var location = 'https://example.com';

// Shadows window.location, doesn't change it (safe):
let location = 'https://example.com';
```

# Relationships

## Builds Upon
- **Global object** — Both categories are global object properties.
- **Object environment record** — The storage mechanism for built-in globals.

## Enables
- **Understanding variable collisions** — Explains why `var` at global scope can cause bugs.

## Related
- **Global variable creation** — User declarations interact with built-in globals.
- **Declarative environment record** — `let`/`const` avoids collision via separate storage.

## Contrasts With
- None directly.

# Common Errors

- **Error**: Using `var` for common names like `location`, `name`, `status` at global scope.
  **Correction**: These are browser built-in globals. Use `let`/`const` to avoid modifying them.

# Common Confusions

- **Confusion**: ECMAScript built-ins and host built-ins are the same thing.
  **Clarification**: ECMAScript built-ins are standardized across all platforms (e.g., `Array`). Host built-ins are platform-specific (e.g., `document` in browsers, `process` in Node.js).

# Source Reference

Chapter 5: A detailed look at global variables, Section 5.5.4, lines 259-308.

# Verification Notes

- Definition source: direct (quoted from source)
- Confidence rationale: Explicit definition with examples
- Cross-reference status: verified
