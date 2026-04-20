---
# === CORE IDENTIFICATION ===
concept: Type Checking
slug: type-checking

# === CLASSIFICATION ===
category: error-handling
subcategory: prevention
tier: intermediate

# === PROVENANCE ===
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Bugs and Errors"
chapter_number: 8
pdf_page: null
section: "Types"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - type annotations
  - static typing

# === TYPED RELATIONSHIPS ===
prerequisites:
  - function
  - value
extends: []
related:
  - bug
  - testing
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How can types help prevent bugs?"
  - "What role do types play in JavaScript error prevention?"
---

# Quick Definition
Type checking involves specifying and verifying the types of values in a program, either through comments, tools like TypeScript, or the language itself, to catch type-related errors before runtime.

# Core Definition
Haverbeke notes: "types provide a useful framework for talking about programs. A lot of mistakes come from being confused about the kind of value that goes into or comes out of a function. If you have that information written down, you're less likely to get confused." He mentions TypeScript as the most popular typed JavaScript dialect. (Ch 8, "Types")

# Prerequisites
- **Functions**: Types describe what goes into and comes out of functions
- **Values**: Understanding different value types is fundamental

# Key Properties
1. JavaScript is dynamically typed; types are checked only at runtime
2. Type comments can document expected types: `// (graph: Object, from: string, to: string) => string[]`
3. TypeScript adds static type checking on top of JavaScript
4. Type variables (generics) handle polymorphic functions: `(T[]) => T`

# Construction / Recognition
```javascript
// (graph: Object, from: string, to: string) => string[]
function findRoute(graph, from, to) {
  // ...
}
```

# Context & Application
Type checking helps catch bugs early. While JavaScript doesn't enforce types, using TypeScript or type annotations in comments can prevent many common errors.

# Examples
```javascript
// Type annotation as comment
// (graph: Object, from: string, to: string) => string[]
function findRoute(graph, from, to) {
  // ...
}
```
For generic functions: "You'd need to introduce a *type variable*, *T*, which can stand in for any type, so that you can give `randomPick` a type like `(T[]) => T` (function from an array of *T*s to a *T*)." (Ch 8, "Types", lines 200-207)

# Relationships
## Builds Upon
- function, value
## Enables
- Earlier bug detection, better documentation
## Related
- bug, testing
## Contrasts With
- N/A

# Common Errors
- **Error**: Relying solely on types to prevent all bugs
  **Correction**: Types catch type-related errors but not logic errors; testing is still necessary

# Common Confusions
- **Confusion**: JavaScript has no type system at all
  **Clarification**: JavaScript has types (string, number, etc.) but doesn't check them statically; TypeScript adds static checking

# Source Reference
Chapter 8: Bugs and Errors, Section "Types", lines 167-220.

# Verification Notes
- Definition source: direct
- Confidence rationale: Explicitly discussed with practical examples
- Cross-reference status: verified
