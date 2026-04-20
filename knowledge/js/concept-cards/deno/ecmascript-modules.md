---
# === CORE IDENTIFICATION ===
concept: ECMAScript Modules
slug: ecmascript-modules

# === CLASSIFICATION ===
category: modules
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "Deno Documentation"
source_slug: deno
authors: "Deno Contributors"
chapter: "runtime/fundamentals/modules.md"
chapter_number: null
pdf_page: null
section: "Importing modules"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - ESM
  - ES modules
  - "ECMAScript module system"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - deno
extends: []
related:
  - deno-import-maps
  - jsr-registry
  - deno-npm-specifiers
  - deno-import-attributes
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is Deno's module system?"
  - "How does Deno's module system relate to ECMAScript modules?"
---

# Quick Definition
Deno uses ECMAScript modules (ESM) as its default module system, requiring full file extensions on local imports, supporting URL imports, and aligning with the official JavaScript standard for modules.

# Core Definition
Deno adopts ECMAScript modules as its default and primary module system, aligning with the official JavaScript standard. This means all local imports use the `import`/`export` syntax and must include the full file extension (e.g., `./calc.ts`, not `./calc`). Deno supports importing modules from local files, URLs (`https://`), and package registries (`jsr:`, `npm:`). By adopting ESM, Deno ensures compatibility with the evolving JavaScript ecosystem, enables better tree-shaking, and avoids the complexities of legacy module formats like CommonJS.

# Prerequisites
- deno: Understanding of Deno as a runtime

# Key Properties
1. **File extensions required** -- Local import specifiers must always include the full file extension; omitting it is an error
2. **URL imports** -- Modules can be imported directly from HTTP/HTTPS URLs
3. **Registry specifiers** -- Third-party modules use `jsr:`, `npm:`, or `https://` prefixes
4. **WebAssembly imports** -- `.wasm` files can be imported directly
5. **Data URL imports** -- Modules can be created from `data:` URLs for testing and prototyping
6. **No CommonJS by default** -- ESM is the default; CommonJS is supported through `.cjs` extension or `package.json` configuration
7. **Standard-compliant** -- Based on the ECMAScript module specification and Import Maps Standard

# Construction / Recognition
```ts
// Local import (extension required)
import { add } from "./calc.ts";

// WRONG: missing extension
import { add } from "./calc";

// URL import
import { Application } from "https://deno.land/x/oak/mod.ts";

// Registry imports
import { camelCase } from "jsr:@luca/cases@1.0.0";
import { say } from "npm:cowsay@1.6.0";
```

# Context & Application
ESM is the foundational module system in Deno. All other module features (import maps, JSR, npm specifiers, import attributes) build on top of ESM. The requirement for file extensions in local imports is a deliberate design choice that aligns with how browsers resolve modules and avoids the ambiguity of Node.js's extensionless resolution algorithm.

HTTPS imports are supported for convenience but are recommended only for small projects or single-file scripts. For larger applications, the documentation recommends using a package registry (JSR or npm) and import maps for centralized version management.

# Examples
From runtime/fundamentals/modules.md:
- Local module: `import { add } from "./calc.ts";` with `deno run main.ts`
- Third-party: `import { camelCase } from "jsr:@luca/cases@1.0.0";`
- URL: `import { Application } from "https://deno.land/x/oak/mod.ts";`
- WebAssembly: `import { add } from "./add.wasm";`

# Relationships
## Builds Upon
- deno (ESM is a core design decision of the runtime)

## Enables
- deno-import-maps (import maps remap ESM specifiers)
- jsr-registry (JSR packages are imported via ESM)
- deno-npm-specifiers (npm packages are imported via ESM)
- deno-import-attributes (import attributes modify ESM imports)

## Related
- deno-node-compatibility (CommonJS is supported for Node compat but ESM is preferred)

## Contrasts With
- CommonJS (Node.js's legacy module system; supported in Deno but not the default)

# Common Errors
1. Omitting file extensions on local imports -- Deno requires `.ts`, `.js`, etc. on all local specifiers
2. Using HTTPS imports without pinning versions in large projects -- can lead to version conflicts across files

# Common Confusions
1. **ESM vs. CommonJS in Deno** -- ESM is the default; CommonJS requires explicit opt-in via `.cjs` extension or `package.json` type field
2. **Extension requirement** -- Unlike Node.js, Deno does not resolve extensionless imports; this is by design to match browser behavior

# Source Reference
- runtime/fundamentals/modules.md: Overview of ECMAScript modules, import syntax, URL imports, and third-party module usage

# Verification Notes
- High confidence: ESM as the default module system is explicitly stated and demonstrated throughout
- File extension requirement is explicitly highlighted as an error when omitted
