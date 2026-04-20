---
# === CORE IDENTIFICATION ===
concept: ES6 Module System
slug: es6-module-system

# === CLASSIFICATION ===
category: modules
subcategory: es6-modules
tier: foundational

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Modules"
chapter_number: 10
pdf_page: 273
section: "10.3 Modules in ES6"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "ES modules"
  - "ESM"
  - "JavaScript modules"
  - "ECMAScript modules"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - module-pattern-iife
extends: []
related:
  - es6-named-exports
  - es6-default-export
  - es6-import-statement
  - dynamic-import
  - commonjs-require
contrasts_with:
  - commonjs-require

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does CommonJS (`require`) relate to ES6 modules (`import`)?"
  - "How do I implement the module pattern in JavaScript?"
  - "What distinguishes named exports from default exports in ES6 modules?"
---

# Quick Definition

The official JavaScript module system introduced in ES6, using `import` and `export` keywords to provide static, declarative modularity as a core language feature.

# Core Definition

ES6 modules give JavaScript "real modularity as a core language feature" (p. 273). Each file is its own module with a private context. Values must be explicitly exported with `export` and explicitly imported with `import`. Unlike CommonJS, ES6 modules are statically analyzable: "the symbols exported can be determined before the module is actually run" (p. 275). Module code is automatically in strict mode.

# Prerequisites

- **module-pattern-iife** — Understanding why modules are needed and how closures provide privacy

# Key Properties

1. Each file has its own private context — top-level declarations are not shared globally
2. Code is automatically in strict mode; `this` is undefined at the top level
3. `import` and `export` are static — they cannot appear inside conditionals, loops, or functions
4. Imports are hoisted to the top of the module
5. Module specifiers must be absolute paths, `./` relative paths, or `../` relative paths (no "bare" specifiers in standard)

# Construction / Recognition

Identified by the presence of `import` or `export` keywords at the top level of a file, or by `<script type="module">` in HTML.

# Context & Application

The standard module system for modern JavaScript in both browsers and Node.js. Used with bundlers like webpack for production. Supported natively in all modern browsers. Node 13+ supports ES6 modules, though most Node code still uses CommonJS.

# Examples

From the source text (p. 273-275): Modules differ from scripts: strict mode is automatic, `this` is undefined at top level, and top-level declarations are private. In browsers: `<script type="module">import "./main.js";</script>` (p. 280).

# Relationships

## Builds Upon
- **Module Pattern** — ES6 modules formalize the encapsulation that IIFEs provided informally

## Enables
- **ES6 Named Exports** — The `export` keyword for named values
- **ES6 Default Export** — The `export default` syntax
- **ES6 Import Statement** — The `import` keyword for consuming modules
- **Dynamic Import** — The `import()` operator for lazy loading

## Contrasts With
- **CommonJS Require** — CommonJS is dynamic (runtime), ES6 is static (analyzable before execution); CommonJS uses `require()`/`module.exports`, ES6 uses `import`/`export`

# Common Errors

- **Error**: Using bare module specifiers like `import { x } from "utils"` in browser code without a bundler.
  **Correction**: Use relative paths like `"./utils.js"` — bare specifiers are not allowed in the ES6 specification (though bundlers support them).

# Common Confusions

- **Confusion**: Thinking ES6 modules and CommonJS modules are interchangeable.
  **Clarification**: They have different syntax, different loading semantics (static vs. dynamic), and different handling of `this` and strict mode. Node supports both but they are distinct systems.

# Source Reference

Chapter 10: Modules, Section 10.3, pages 273-283.

# Verification Notes

- Definition source: Direct quotes and synthesis from source text
- Confidence rationale: High — core section topic with extensive coverage
- Uncertainties: None
- Cross-reference status: Verified
