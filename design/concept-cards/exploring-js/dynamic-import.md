---
concept: Dynamic Import
slug: dynamic-import
category: modules
subcategory: imports
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Modules"
chapter_number: 29
pdf_page: null
section: "29.14 Loading modules dynamically via `import()`"
extraction_confidence: high
aliases:
  - "import()"
  - "dynamic import()"
prerequisites:
  - ecmascript-module
extends: []
related:
  - named-import
contrasts_with:
  - named-import
answers_questions:
  - "How do I load modules conditionally or lazily?"
---

# Quick Definition

Dynamic `import()` (ES2020) loads a module asynchronously at runtime, returning a Promise that resolves to the module's namespace object, enabling conditional and lazy loading.

# Core Definition

As described in "Exploring JavaScript" Ch. 29, static `import` statements must appear at the top level with a fixed specifier. Dynamic `import()` has no such constraints: it can be used anywhere and with computed specifiers. It returns a Promise resolving to a module namespace object. Use cases include conditional loading, lazy loading, and computed module specifiers.

# Prerequisites

- ECMAScript module

# Key Properties

1. Introduced in ES2020.
2. Returns a Promise resolving to the module namespace object.
3. Can be used anywhere (not just top level).
4. Module specifier can be computed at runtime.
5. Enables code splitting and lazy loading.

# Construction / Recognition

```js
const module = await import('./my-module.mjs');
module.myFunc();
```

# Context & Application

Used for code splitting (loading only what's needed), conditional imports, and computed module paths. Essential for performance optimization in large applications.

# Examples

From the source text (Ch. 29, section 29.1.2):

```js
function importLibrary(moduleSpecifier) {
  return import(moduleSpecifier)
    .then((lib) => {
      assert.equal(lib.one, 1);
      assert.equal(lib.myFunc(), 3);
    });
}
await importLibrary('./lib.mjs');
```

# Relationships

## Contrasts With
- **Named Import** -- static imports are fixed at parse time; dynamic imports are resolved at runtime

# Common Confusions

- **Confusion**: Thinking `import()` is a function.
  **Clarification**: `import()` is an operator (like `typeof`), not a function. It just uses function-call-like syntax.

# Source Reference

Chapter 29: Modules, Section 29.14, lines ~1380-1420.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit definition with use cases
- Cross-reference status: verified
