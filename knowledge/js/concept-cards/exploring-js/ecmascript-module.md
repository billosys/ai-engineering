---
concept: ECMAScript Module
slug: ecmascript-module
category: modules
subcategory: null
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Modules"
chapter_number: 29
pdf_page: null
section: "29.5 ECMAScript modules"
extraction_confidence: high
aliases:
  - "ES module"
  - "ESM"
  - "JavaScript module"
prerequisites: []
extends: []
related:
  - named-export
  - default-export
  - module-specifier
  - scripts-vs-modules
contrasts_with:
  - commonjs-module
answers_questions:
  - "What is a module in JavaScript (ECMAScript modules)?"
  - "What concepts underpin the module system?"
---

# Quick Definition

An ECMAScript module (ESM) is JavaScript's built-in module format (ES6) that provides file-level scope, explicit imports/exports, static structure, and support for asynchronous loading.

# Core Definition

As described in "Exploring JavaScript" Ch. 29, ECMAScript modules were introduced with ES6 and continue the tradition of JavaScript module systems (CommonJS, AMD). They have one module per file, a local "module scope" (no global variables by default), explicit exports/imports via `export`/`import` keywords, static structure (can't change at runtime), and transparent support for cyclic imports. They share compact syntax with CommonJS and asynchronous loading with AMD.

# Prerequisites

- Foundational concept for the module system

# Key Properties

1. Introduced in ES6.
2. One module per file with its own scope.
3. Static structure: imports/exports can't change at runtime.
4. Supports asynchronous loading (works in browsers and servers).
5. Modules are singletons: imported only once even if referenced multiple times.
6. Imports are read-only live views on exports.
7. Compact syntax: more concise than CommonJS.
8. File extension: `.mjs` or `.js` (depending on configuration).

# Construction / Recognition

```js
// Exporting
export function square(x) { return x * x; }
export const PI = 3.14159;

// Importing
import { square, PI } from './math.mjs';
```

# Context & Application

The standard module format for modern JavaScript on all platforms. Supersedes CommonJS (server) and AMD (browser) module systems.

# Examples

From the source text (Ch. 29, section 29.5):

```js
import {importedFunc1} from './other-module1.mjs';
import {importedFunc2} from './other-module2.mjs';

function internalFunc() { /* ... */ }

export function exportedFunc() {
  importedFunc1();
  importedFunc2();
  internalFunc();
}
```

# Relationships

## Enables
- **Named Export** -- the primary export mechanism
- **Default Export** -- single-value export mechanism
- **Module Specifier** -- identifies where to import from

## Related
- **Scripts vs Modules** -- the two source code unit types

## Contrasts With
- **CommonJS Module** -- synchronous, dynamic structure, server-only predecessor

# Common Errors

- **Error**: Trying to use `require()` in an ESM module.
  **Correction**: Use `import` statements. `require()` is CommonJS syntax.

# Common Confusions

- **Confusion**: Thinking modules run in global scope like scripts.
  **Clarification**: Each module has its own scope; variables are not global by default.

# Source Reference

Chapter 29: Modules, Section 29.5, lines 668-706.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit definition with comparison to predecessors
- Cross-reference status: verified
