---
# === CORE IDENTIFICATION ===
concept: Import Attributes
slug: deno-import-attributes

# === CLASSIFICATION ===
category: modules
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Deno Documentation"
source_slug: deno
authors: "Deno Contributors"
chapter: "runtime/fundamentals/modules.md"
chapter_number: null
pdf_page: null
section: "Import attributes"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "import assertions"
  - "with { type }"
  - "import with syntax"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - ecmascript-modules
extends:
  - ecmascript-modules
related:
  - deno
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I import JSON files in Deno?"
  - "How do I import non-JavaScript resources in Deno?"
---

# Quick Definition
Import attributes use the `with { type: "json" }` syntax to import non-JavaScript resources like JSON, text, and binary files as typed modules in Deno.

# Core Definition
Import attributes are a syntax extension to ECMAScript module imports that specify the type of a non-JavaScript resource being imported. Deno supports the `with { type: "json" }` syntax for importing JSON files as JavaScript objects. Starting with Deno 2.4, experimental support for `text` and `bytes` types was added (requiring `--unstable-raw-imports` or the `unstable.raw-import` option in `deno.json`).

The syntax follows the TC39 Import Attributes proposal and provides a safe, explicit way to import non-code resources without ambiguity about their interpretation.

# Prerequisites
- ecmascript-modules: Understanding of ESM import syntax

# Key Properties
1. **JSON imports** -- `import data from "./data.json" with { type: "json" }` imports JSON as a JavaScript object
2. **Text imports (experimental)** -- `import text from "./log.txt" with { type: "text" }` imports file contents as a string
3. **Bytes imports (experimental)** -- `import bytes from "./image.png" with { type: "bytes" }` imports file contents as a `Uint8Array`
4. **Explicit typing** -- The `with` clause makes the import type unambiguous
5. **Unstable flag required** -- Text and bytes imports require `--unstable-raw-imports` CLI flag or `unstable.raw-import` in `deno.json`

# Construction / Recognition
```ts
// JSON import
import data from "./data.json" with { type: "json" };
console.log(data.property);

// Text import (experimental, requires --unstable-raw-imports)
import text from "./log.txt" with { type: "text" };
console.log(typeof text === "string"); // true

// Bytes import (experimental, requires --unstable-raw-imports)
import bytes from "./image.png" with { type: "bytes" };
console.log(bytes instanceof Uint8Array); // true
```

# Context & Application
Import attributes provide a standardized way to import non-JavaScript resources in Deno. JSON imports are the most common use case, replacing the need for `JSON.parse(Deno.readTextFileSync(...))` with a cleaner, declarative syntax. Text and bytes imports extend this pattern to arbitrary file types, enabling use cases like embedding configuration files, templates, or binary assets directly into modules.

The feature is based on the TC39 Import Attributes proposal and aligns Deno with emerging JavaScript standards for resource imports.

# Examples
From runtime/fundamentals/modules.md, section "Import attributes":
- JSON: `import data from "./data.json" with { type: "json" };`
- Text: `import text from "./log.txt" with { type: "text" };` -- returns a string
- Bytes: `import bytes from "./image.png" with { type: "bytes" };` -- returns a `Uint8Array`

# Relationships
## Builds Upon
- ecmascript-modules (import attributes extend the ESM import syntax)

## Related
- deno (import attributes are a Deno runtime feature)

## Contrasts With
- Dynamic file reading (`Deno.readTextFile`, `Deno.readFile`) -- import attributes are declarative and static

# Common Errors
1. Omitting the `with { type: "json" }` clause when importing JSON -- Deno requires the explicit type annotation
2. Using text/bytes imports without the `--unstable-raw-imports` flag -- these are experimental features

# Common Confusions
1. **Import attributes vs. import assertions** -- Import attributes (`with`) replaced the earlier import assertions (`assert`) syntax; Deno uses the `with` keyword
2. **Static vs. dynamic** -- Import attributes work with both static `import` declarations and dynamic `import()` calls

# Source Reference
- runtime/fundamentals/modules.md, section "Import attributes": Syntax, supported types, and experimental features

# Verification Notes
- High confidence: Import attributes are explicitly documented with examples for all three supported types
- Experimental status of text/bytes imports is explicitly noted with required flags
