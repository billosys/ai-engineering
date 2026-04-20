---
concept: CommonJS Module
slug: commonjs-module
category: modules
subcategory: null
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Modules"
chapter_number: 29
pdf_page: null
section: "29.4.1 Server side: CommonJS modules"
extraction_confidence: high
aliases:
  - "CJS"
  - "require/module.exports"
prerequisites:
  - scripts-vs-modules
extends: []
related:
  - ecmascript-module
contrasts_with:
  - ecmascript-module
answers_questions:
  - "What concepts underpin the module system?"
---

# Quick Definition

CommonJS is the module format used by Node.js before ESM, using `require()` for imports and `module.exports` for exports, with synchronous loading.

# Core Definition

As described in "Exploring JavaScript" Ch. 29, CommonJS modules were the foundation of the original Node.js module system. They use `require('./module')` for imports and `module.exports = { ... }` for exports. CommonJS is designed for servers, loads synchronously, and has compact syntax. ESM shares its compact syntax and support for cyclic dependencies.

# Prerequisites

- Scripts vs modules

# Key Properties

1. Designed for server-side JavaScript.
2. Synchronous loading.
3. `require()` for imports, `module.exports` for exports.
4. Dynamic structure (can conditionally require).
5. Decreasing usage; ESM is the modern replacement.
6. File extensions: `.js` or `.cjs`.

# Construction / Recognition

```js
const importedFunc = require('./other-module.js').importedFunc;
module.exports = { exportedFunc };
```

# Context & Application

Still widely used in existing Node.js codebases. Understanding CommonJS is necessary for working with legacy code and understanding why ESM was designed.

# Examples

From the source text (Ch. 29, section 29.4.1):

```js
var importedFunc1 = require('./other-module1.js').importedFunc1;
function exportedFunc() { importedFunc1(); }
module.exports = { exportedFunc: exportedFunc };
```

# Relationships

## Contrasts With
- **ECMAScript Module** -- ESM has static structure, async loading, and is the modern standard

# Source Reference

Chapter 29: Modules, Section 29.4.1, lines 557-599.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit description with characteristics
- Cross-reference status: verified
