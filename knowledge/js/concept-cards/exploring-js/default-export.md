---
concept: Default Export
slug: default-export
category: modules
subcategory: exports
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Modules"
chapter_number: 29
pdf_page: null
section: "29.7 Default exports and default imports"
extraction_confidence: high
aliases:
  - "export default"
prerequisites:
  - named-export
extends: []
related:
  - default-import
  - named-export
contrasts_with:
  - named-export
answers_questions:
  - "How do named exports and default exports relate in the module system?"
  - "How do I import and export modules?"
---

# Quick Definition

A default export is a single value that a module exports as its primary entity, allowing importers to choose any name for it.

# Core Definition

As described in "Exploring JavaScript" Ch. 29, each module can have at most one default export. The idea is that the module "is" the default-exported value. Internally, a default export is simply a named export whose name is `default`. Two styles exist: labeling a declaration (`export default function myFunc() {}`) or directly exporting a value (`export default 123`). `const`/`let` cannot be default-exported because they may declare multiple values.

# Prerequisites

- Named export (to understand the alternative)

# Key Properties

1. At most one default export per module.
2. Internally, it is a named export with the name `default`.
3. Importers choose their own name for the import.
4. Two styles: labeling a declaration, or directly exporting a value.
5. `const`/`let` cannot be used with `export default`.

# Construction / Recognition

```js
// Style 1: label a declaration
export default function getHello() { return 'hello'; }

// Style 2: export a value directly
export default 123;
```

# Context & Application

Best used when a module contains a single function or class. The author recommends avoiding mixing default and named exports and notes that named-only exports are always safe.

# Examples

From the source text (Ch. 29, section 29.7):

```js
// my-func.mjs
const GREETING = 'Hello!';
export default function () { return GREETING; }

// main.mjs
import myFunc from './my-func.mjs';
assert.equal(myFunc(), 'Hello!');
```

# Relationships

## Contrasts With
- **Named Export** -- named exports are identified by name; default exports are identified by their role as the module's primary value

## Related
- **Default Import** -- the corresponding import syntax

# Common Errors

- **Error**: Trying to `export default const x = 1`.
  **Correction**: `const` can't be default-exported because it might define multiple values. Use `export default 1` or `export default function`.

# Common Confusions

- **Confusion**: Thinking default exports are anonymous.
  **Clarification**: Default exports can have names (`export default function myFunc() {}`). The import name is just not tied to the export name.

# Source Reference

Chapter 29: Modules, Section 29.7, lines 872-1042.

# Verification Notes

- Definition source: direct
- Confidence rationale: Thorough coverage with internal mechanics explained
- Cross-reference status: verified
