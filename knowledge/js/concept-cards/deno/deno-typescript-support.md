---
# === CORE IDENTIFICATION ===
concept: TypeScript Support
slug: deno-typescript-support

# === CLASSIFICATION ===
category: runtime
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Deno Documentation"
source_slug: deno
authors: "Deno Contributors"
chapter: "runtime/fundamentals/typescript.md"
chapter_number: null
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Deno TypeScript"
  - "first-class TypeScript"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - deno
extends: []
related:
  - deno-node-compatibility
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does Deno support TypeScript?"
  - "What distinguishes Deno from Node.js?"
---

# Quick Definition
TypeScript is a first-class language in Deno: you can run or import TypeScript without any additional tools, configuration, or setup beyond the Deno CLI, with strict mode enabled by default.

# Core Definition
Deno treats TypeScript as a first-class language. The runtime includes a built-in TypeScript compiler that transparently compiles TypeScript to JavaScript with no extra configuration needed. Deno can also type-check TypeScript code without requiring a separate tool like `tsc`. By default, Deno type-checks in strict mode (the TypeScript core team's recommended default). However, type checking is not performed during `deno run` for performance reasons -- the `deno check` subcommand or the `--check` flag on `deno run` must be used to perform type checking.

# Prerequisites
- deno: Understanding of Deno as a runtime

# Key Properties
1. **Zero configuration** -- No `tsconfig.json` needed; TypeScript works out of the box
2. **Built-in compiler** -- Deno compiles TypeScript to JavaScript internally; no separate build step
3. **Strict mode by default** -- Type checking uses TypeScript strict mode as the default
4. **Separate check step** -- `deno run` skips type checking for performance; use `deno check` or `--check` flag
5. **JavaScript type checking** -- JavaScript files can opt into type checking via `// @ts-check` pragma or `compilerOptions.checkJs`
6. **Declaration file support** -- `.d.ts` files are supported via `@ts-self-types`, `@ts-types` directives, and `X-TypeScript-Types` HTTP headers
7. **Library file configuration** -- `compilerOptions.lib` in `deno.json` controls type definitions for different environments (Deno, browser, web worker)

# Construction / Recognition
```sh
# Run TypeScript directly (no type checking)
deno run module.ts

# Type check without executing
deno check module.ts

# Type check then execute
deno run --check module.ts

# Type check including remote modules and npm packages
deno check --all module.ts
```

# Context & Application
Deno's built-in TypeScript support eliminates the need for a separate TypeScript toolchain (tsc, ts-node, tsx, etc.). This simplifies project setup and reduces dependencies. The design decision to skip type checking during `deno run` balances developer experience (fast execution) with correctness (explicit type checking when desired). For CI pipelines, `deno check` is typically run as a separate step.

The `compilerOptions.lib` configuration enables Deno to type-check code for different target environments: browser (using `dom`), Deno (using `deno.ns`), web workers (using `deno.worker`), or combinations thereof (e.g., SSR with `["dom", "deno.ns"]`).

# Examples
From runtime/fundamentals/typescript.md:
- Providing types for untyped JS: `// @ts-types="./add.d.ts"` before an import statement
- Providing types for npm packages: `// @ts-types="npm:@types/lodash"` before importing lodash
- Browser + Deno SSR config in deno.json: `{ "compilerOptions": { "lib": ["dom", "deno.ns"] } }`
- Self-typing a JS file: `// @ts-self-types="./add.d.ts"` at the top of a `.js` file

# Relationships
## Builds Upon
- deno (TypeScript support is a built-in feature of the runtime)

## Enables
- Type-safe development without external tooling
- Declaration file workflows for untyped JavaScript

## Related
- deno-node-compatibility (npm types via `@types/*` packages)

## Contrasts With
- Node.js (requires external tools like ts-node or tsx to run TypeScript; requires tsc for type checking)

# Common Errors
1. Expecting `deno run` to catch type errors -- by default it does not; use `deno check` or `--check`
2. Expecting `.d.ts` sibling discovery like `tsc` -- Deno does NOT automatically find `.d.ts` files next to `.js` files; explicit directives are required

# Common Confusions
1. **Type checking vs. compilation** -- Deno always compiles TypeScript for execution; type CHECKING is the optional step
2. **Strict mode** -- Deno defaults to strict mode, which may surprise developers coming from non-strict TypeScript projects

# Source Reference
- runtime/fundamentals/typescript.md: Complete description of TypeScript support, type checking, declaration files, and library configuration

# Verification Notes
- High confidence: TypeScript support is explicitly described with detailed examples
- Strict mode default is explicitly stated and attributed to the TypeScript core team's recommendation
