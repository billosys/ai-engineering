---
# === CORE IDENTIFICATION ===
concept: Module Pattern (IIFE + Closure)
slug: module-pattern-iife

# === CLASSIFICATION ===
category: modules
subcategory: closure-based-modules
tier: foundational

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Modules"
chapter_number: 10
pdf_page: 267
section: "10.1 Modules with Classes, Objects, and Closures"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "IIFE module pattern"
  - "closure-based module"
  - "revealing module pattern"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - commonjs-require
  - es6-module-system
contrasts_with:
  - es6-module-system
  - commonjs-require

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I implement the module pattern in JavaScript?"
  - "How does CommonJS (`require`) relate to ES6 modules (`import`)?"
---

# Quick Definition

A technique using immediately invoked function expressions (IIFEs) and closures to encapsulate private implementation details and expose a public API, predating built-in module systems.

# Core Definition

The module pattern uses an immediately invoked function expression to create a private scope where implementation details are hidden, returning an object (or value) that serves as the module's public API. As Flanagan explains, "local variables and nested functions declared within a function are private to that function. This means that we can use immediately invoked function expressions to achieve a kind of modularity" (p. 268).

# Prerequisites

This is a foundational concept with no prerequisites within this source beyond basic understanding of functions and closures.

# Key Properties

1. Uses an IIFE to create a private scope for implementation details
2. Returns a public API as an object with methods/properties
3. Private variables and functions are inaccessible from outside the closure
4. Was the primary modularity mechanism before ES6 modules and Node require()

# Construction / Recognition

Wrap module code in `(function() { ... }())` and return an object containing the public API:

```js
const stats = (function() {
    const sum = (x, y) => x + y;
    const square = x => x * x;
    function mean(data) {
        return data.reduce(sum)/data.length;
    }
    function stddev(data) {
        let m = mean(data);
        return Math.sqrt(
            data.map(x => x - m).map(square).reduce(sum)/(data.length-1)
        );
    }
    return { mean, stddev };
}());
```

# Context & Application

Used before ES6 modules and Node's require() were available. Still seen in legacy codebases and as a conceptual foundation for understanding how bundling tools like webpack work. Code-bundling tools automate this pattern by wrapping each file in an IIFE.

# Examples

From the source text (p. 268-269): A stats module using IIFE that exports `mean()` and `stddev()` while keeping `sum` and `square` private. Usage: `stats.mean([1, 3, 5, 7, 9])` returns `5`.

The text also shows how bundling tools automate this: each module file's contents are wrapped in an IIFE, with exports collected into a `modules` object accessed by a `require()` function (p. 269).

# Relationships

## Builds Upon
- **Functions and Closures** — The pattern relies entirely on function scope and closure to create privacy

## Enables
- **CommonJS Require** — The automated version of this pattern became the basis for Node's module system
- **ES6 Module System** — Understanding this pattern provides context for why ES6 modules were needed

## Related
- **CommonJS Require** — Node's require() system automates and standardizes this pattern
- **ES6 Module System** — The modern replacement that provides native language-level modularity

## Contrasts With
- **ES6 Module System** — ES6 modules use declarative import/export keywords rather than IIFE closures
- **CommonJS Require** — CommonJS provides a standardized API rather than ad-hoc IIFE patterns

# Common Errors

- **Error**: Forgetting to use `var`, `let`, or `const` inside the IIFE, accidentally leaking variables to global scope.
  **Correction**: Always declare variables with `const`, `let`, or `var` inside the module function.

# Common Confusions

- **Confusion**: Believing the curly braces in `return { mean, stddev }` define an object literal the same way as ES6 module `export { mean, stddev }`.
  **Clarification**: In the module pattern, the return value is a true object literal. In ES6 export syntax, the curly braces are special export syntax, not an object literal.

# Source Reference

Chapter 10: Modules, Section 10.1, pages 267-270.

# Verification Notes

- Definition source: Direct synthesis from source text
- Confidence rationale: High — extensively described with multiple examples
- Uncertainties: None
- Cross-reference status: Verified against sections 10.2 and 10.3
