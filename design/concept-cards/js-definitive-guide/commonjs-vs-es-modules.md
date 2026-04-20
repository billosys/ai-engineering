---
concept: CommonJS vs ES Modules Differences
slug: commonjs-vs-es-modules
category: modules
subcategory: comparison
tier: intermediate
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Modules"
chapter_number: 10
pdf_page: 273
section: "10.3 Modules in ES6"
extraction_confidence: high
aliases: []
prerequisites:
  - commonjs-require
  - es6-module-system
extends: []
related: []
contrasts_with: []
answers_questions:
  - "How does CommonJS (`require`) relate to ES6 modules (`import`)?"
---

# Quick Definition

The key differences between Node's CommonJS modules (`require`/`exports`) and ES6 modules (`import`/`export`): static vs. dynamic, strict mode by default, different `this` behavior, and different loading semantics.

# Core Definition

ES6 modules differ from CommonJS in several important ways: ES6 imports/exports are static (analyzable before execution) while require() is dynamic (runtime). ES6 modules are automatically in strict mode with `this` undefined at the top level. ES6 module specifiers must be literal strings (not expressions). "ES6 modularity is conceptually the same as Node modularity: each file is its own module... ES6 modules differ from Node modules in the syntax used for exporting and importing" (p. 273).

# Prerequisites

- **commonjs-require** — Understanding CommonJS modules
- **es6-module-system** — Understanding ES6 modules

# Key Properties

1. **Syntax**: CJS uses `require()`/`module.exports`; ESM uses `import`/`export`
2. **Loading**: CJS is synchronous/dynamic; ESM is asynchronous/static
3. **Analysis**: ESM exports determinable before execution; CJS requires runtime execution
4. **Strict mode**: ESM is always strict; CJS is not strict by default
5. **`this`**: ESM has `this` undefined at top level; CJS has `this` as the module object
6. **Specifiers**: ESM requires literal strings; CJS allows expressions in require()

# Construction / Recognition

CommonJS:
```js
const fs = require("fs");
module.exports = { mean, stddev };
```

ES6:
```js
import fs from "fs";
export { mean, stddev };
```

# Context & Application

Understanding these differences is critical when working in Node.js environments that support both systems, when migrating code from CJS to ESM, or when configuring bundlers.

# Examples

From the source text (p. 273): Node "finds itself in the awkward position of having to support two not entirely compatible module systems." ES6 module code "is automatically in strict mode" and "this is undefined even in top-level code" (p. 273).

# Relationships

## Builds Upon
- **CommonJS Require** — One of the two systems being compared
- **ES6 Module System** — The other system being compared

# Common Errors

- **Error**: Using `require()` inside an ES6 module or `import` in a CommonJS file without configuration.
  **Correction**: In Node, use `.mjs` extension for ES6 modules or set `"type": "module"` in package.json. Don't mix module systems in a single file.

# Common Confusions

- **Confusion**: Thinking ESM and CJS can freely interoperate in Node.
  **Clarification**: While Node supports both, there are restrictions on mixing. ESM can import CJS (default export), but CJS cannot use `require()` on ESM modules (it must use dynamic `import()`).

# Source Reference

Chapter 10: Modules, Section 10.3, pages 273-274.

# Verification Notes

- Definition source: Synthesized from source text
- Confidence rationale: High
- Uncertainties: None
- Cross-reference status: Verified
