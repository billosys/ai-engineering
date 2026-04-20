---
concept: Named Export
slug: named-export
category: modules
subcategory: exports
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Modules"
chapter_number: 29
pdf_page: null
section: "29.6.1 Named exports"
extraction_confidence: high
aliases:
  - "named exports"
prerequisites:
  - ecmascript-module
extends: []
related:
  - named-import
  - default-export
  - re-exporting
contrasts_with:
  - default-export
answers_questions:
  - "How do named exports and default exports relate in the module system?"
  - "How do I import and export modules?"
---

# Quick Definition

A named export makes a module-level entity accessible to importers by prefixing its declaration with `export`, allowing a module to have zero or more named exports.

# Core Definition

As described in "Exploring JavaScript" Ch. 29, placing `export` in front of a named entity (function, class, variable) inside a module makes it a named export. All other entities are private to the module. Alternatively, an export clause (`export { a, b }`) can be used after declarations. Export clauses support renaming via `as`.

# Prerequisites

- ECMAScript module

# Key Properties

1. A module can have zero or more named exports.
2. Two styles: inline (`export function f() {}`) or clause (`export { f }`).
3. Export clauses support renaming: `export { sq as square }`.
4. Non-exported entities are private to the module.

# Construction / Recognition

```js
// Inline style
export function square(x) { return x * x; }
export const LIGHT_SPEED = 299792458;

// Clause style
function sq(x) { return x * x; }
export { sq as square };
```

# Context & Application

Named exports are the recommended default for modules. They support multiple exports per module and provide clear, discoverable APIs.

# Examples

From the source text (Ch. 29, section 29.6.1):

```js
// Not exported, private to module
function times(a, b) { return a * b; }

export function square(x) { return times(x, x); }
export const LIGHT_SPEED = 299792458;
```

# Relationships

## Enables
- **Named Import** -- consumers use named imports to access named exports

## Contrasts With
- **Default Export** -- default exports use different syntax and are limited to one per module

# Common Confusions

- **Confusion**: Thinking named importing uses destructuring syntax.
  **Clarification**: Named imports look like destructuring but are different: renaming uses `as` (not `:`), and they can't be nested.

# Source Reference

Chapter 29: Modules, Section 29.6.1, lines 720-851.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit definition with both export styles
- Cross-reference status: verified
