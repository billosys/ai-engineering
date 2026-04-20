---
concept: Scripts vs Modules
slug: scripts-vs-modules
category: modules
subcategory: null
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Modules"
chapter_number: 29
pdf_page: null
section: "29.2 JavaScript's source code units: scripts and modules"
extraction_confidence: high
aliases:
  - "source code units"
prerequisites: []
extends: []
related:
  - ecmascript-module
  - commonjs-module
contrasts_with: []
answers_questions:
  - "What concepts underpin the module system?"
---

# Quick Definition

JavaScript has two kinds of source code units: scripts (run in global scope, legacy) and modules (have their own scope, use import/export, modern).

# Core Definition

As described in "Exploring JavaScript" Ch. 29, JavaScript source code can be delivered as scripts (legacy, run in global scope in browsers), CommonJS modules (server-side, synchronous), AMD modules (browser-side, async, legacy), or ECMAScript modules (modern, both browser and server, async). Scripts are precursors of modules; modules provide their own scope, explicit imports/exports, and no global variables.

# Prerequisites

- Foundational concept with no prerequisites

# Key Properties

1. Scripts: run in global scope, no imports/exports, loaded synchronously in browsers.
2. Modules: own scope, explicit exports/imports, loaded asynchronously.
3. Scripts use `<script>` tags; modules use `<script type="module">`.
4. In modules, `this` is `undefined` at the top level.
5. Modules are in strict mode by default.

# Construction / Recognition

```html
<!-- Script -->
<script src="app.js"></script>

<!-- Module -->
<script type="module" src="app.mjs"></script>
```

# Context & Application

Understanding the script-module distinction is fundamental to working with modern JavaScript. Legacy codebases may mix both; modern projects should use modules exclusively.

# Examples

From the source text (Ch. 29, section 29.3) -- IIFE revealing module pattern (pre-module era):

```js
var myModule = (function () {
  var importedFunc1 = otherModule1.importedFunc1;
  function exportedFunc() { importedFunc1(); }
  return { exportedFunc: exportedFunc };
})();
```

# Relationships

## Related
- **ECMAScript Module** -- the modern module format
- **CommonJS Module** -- server-side predecessor

# Common Confusions

- **Confusion**: Thinking scripts and modules behave the same way.
  **Clarification**: Modules have their own scope, strict mode by default, and `this === undefined` at top level.

# Source Reference

Chapter 29: Modules, Section 29.2-29.3, lines 291-547.

# Verification Notes

- Definition source: synthesized
- Confidence rationale: Synthesized from comparison across sections
- Cross-reference status: verified
