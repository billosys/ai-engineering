---
concept: Node Module System
slug: node-module-system
category: node-apis
subcategory: fundamentals
tier: foundational
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Server-Side JavaScript with Node"
chapter_number: 16
pdf_page: 598
section: "16.1.4 Node Modules"
extraction_confidence: high
aliases:
  - CommonJS modules
  - "require()"
  - "module.exports"
prerequisites:
  - node-programming-model
extends: []
related:
  - npm-package-management
contrasts_with: []
answers_questions:
  - "How do I create an HTTP server in Node.js?"
---

# Quick Definition

Node supports two module systems: the original CommonJS system (using `require()` and `module.exports`) and ES6 modules (using `import`/`export`), with file extensions `.cjs`/`.mjs` or `package.json` "type" field controlling which system is used.

# Core Definition

Node's original module system uses `require()` to import and `exports`/`module.exports` to export (CommonJS modules). Node 13+ also supports ES6 modules with `import`/`export`. Files ending in `.mjs` are always ES6 modules; `.cjs` are always CommonJS. For `.js` files, the nearest `package.json` "type" field determines the system: `"module"` for ES6, `"commonjs"` (default) for CommonJS. ES6 modules can import CommonJS modules, but CommonJS cannot `require()` ES6 modules (Flanagan, Ch. 16, pp. 598-599).

# Prerequisites

- **node-programming-model** — Module system is fundamental to Node.

# Key Properties

1. CommonJS: `require()` to import, `module.exports` to export.
2. ES6: `import`/`export` keywords.
3. `.mjs` = ES6 module; `.cjs` = CommonJS module.
4. `package.json` "type" field: "module" or "commonjs".
5. ES6 can import CommonJS, but not vice versa.
6. Default is CommonJS when no "type" field exists.

# Construction / Recognition

```javascript
// CommonJS
const fs = require("fs");
module.exports = myFunction;

// ES6 module
import fs from "fs";
export default myFunction;
```

# Context & Application

Understanding both module systems is essential for working with Node's vast ecosystem, which includes packages in both formats.

# Examples

From the source (p. 598-599): A file ending in `.mjs` automatically uses ES6 modules with `import`/`export`, while `.cjs` uses `require()`/`module.exports`.

# Relationships

## Builds Upon
- **node-programming-model** — Modules organize Node programs

## Enables
- Code organization and reuse

## Related
- **npm-package-management** — npm manages module packages

## Contrasts With
- (None)

# Common Errors

- **Error**: Using `require()` in an ES6 module file.
  **Correction**: ES6 modules use `import`, not `require()`. Node does not define `require()` in ES6 module context.

# Common Confusions

- **Confusion**: CommonJS and ES6 modules are interchangeable.
  **Clarification**: They have different semantics. CommonJS is synchronous; ES6 modules are asynchronous. ES6 modules can import CommonJS, but not the reverse.

# Source Reference

Chapter 16: Server-Side JavaScript with Node, Section 16.1.4, pages 598-599.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: Both systems clearly contrasted
- Uncertainties: None
- Cross-reference status: Verified
