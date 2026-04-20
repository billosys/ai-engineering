---
# === CORE IDENTIFICATION ===
concept: Dynamic import()
slug: dynamic-import

# === CLASSIFICATION ===
category: modules
subcategory: es6-modules
tier: intermediate

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Modules"
chapter_number: 10
pdf_page: 281
section: "10.3.6 Dynamic Imports with import()"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "import() operator"
  - "lazy import"
  - "dynamic module loading"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - es6-module-system
  - promise-object
extends: []
related:
  - es6-import-statement
  - async-functions
contrasts_with:
  - es6-import-statement

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does CommonJS (`require`) relate to ES6 modules (`import`)?"
---

# Quick Definition

The ES2020 `import()` operator that dynamically loads an ES6 module at runtime, returning a Promise that resolves to the module's namespace object, enabling code-splitting and lazy loading.

# Core Definition

"You pass a module specifier to import() and it returns a Promise object that represents the asynchronous process of loading and running the specified module. When the dynamic import is complete, the Promise is 'fulfilled' and produces an object like the one you would get with the `import * as` form of the static import statement" (p. 281). Unlike static `import`, `import()` accepts any expression as its module specifier.

# Prerequisites

- **es6-module-system** — Dynamic import extends the ES6 module system
- **promise-object** — import() returns a Promise

# Key Properties

1. Returns a Promise that resolves to the module namespace object
2. Accepts any expression as module specifier (not limited to string literals)
3. Is an operator, not a function (cannot be assigned to a variable)
4. Works in both browsers and Node.js
5. Enables code-splitting when used with bundlers like webpack

# Construction / Recognition

```js
import("./stats.js").then(stats => {
    let average = stats.mean(data);
});

// With async/await:
async function analyzeData(data) {
    let stats = await import("./stats.js");
    return { average: stats.mean(data), stddev: stats.stddev(data) };
}
```

# Context & Application

Essential for web applications that need to load code on demand. Used for code-splitting: initially load minimal code, then load additional modules as needed. Bundlers like webpack use `import()` calls to determine split points.

# Examples

From the source text (p. 281-282): Static import `import * as stats from "./stats.js"` can be replaced with dynamic `import("./stats.js").then(stats => { let average = stats.mean(data); })`. With async/await: `let stats = await import("./stats.js")`.

# Relationships

## Builds Upon
- **ES6 Module System** — Dynamic import is an extension of ES6 modules
- **Promise Object** — The return value is a Promise

## Related
- **Async Functions** — Dynamic import is commonly used with async/await

## Contrasts With
- **ES6 Import Statement** — Static import is declarative and hoisted; dynamic import() is an expression evaluated at runtime

# Common Errors

- **Error**: Treating `import()` as a regular function: `let require = import;`.
  **Correction**: `import()` is an operator, not a function. It cannot be assigned, aliased, or called with `.call()`.

# Common Confusions

- **Confusion**: Expecting dynamic import() to be synchronous like CommonJS require().
  **Clarification**: import() always returns a Promise. Use `await` or `.then()` to access the module.

# Source Reference

Chapter 10: Modules, Section 10.3.6, pages 281-282.

# Verification Notes

- Definition source: Direct quotes from source text
- Confidence rationale: High — well explained with examples
- Uncertainties: None
- Cross-reference status: Verified
