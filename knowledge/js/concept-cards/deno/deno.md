---
# === CORE IDENTIFICATION ===
concept: Deno
slug: deno

# === CLASSIFICATION ===
category: runtime
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "Deno Documentation"
source_slug: deno
authors: "Deno Contributors"
chapter: "runtime/index.md"
chapter_number: null
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Deno runtime"
  - "deno"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - deno-security-model
  - ecmascript-modules
  - deno-typescript-support
  - deno-node-compatibility
  - deno-architecture
contrasts_with:
  - node-js

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is Deno?"
  - "What distinguishes Deno from Node.js?"
---

# Quick Definition
Deno is an open-source JavaScript, TypeScript, and WebAssembly runtime with secure defaults and a great developer experience, built on V8, Rust, and Tokio.

# Core Definition
Deno (pronounced "dee-no") is a modern runtime for JavaScript, TypeScript, and WebAssembly. It is built on the V8 JavaScript engine (the same engine powering Chrome and Node.js), the Rust programming language (for performance and safety), and the Tokio asynchronous runtime (for non-blocking I/O). Deno distinguishes itself through four pillars: first-class TypeScript support with zero configuration, a secure-by-default execution model with granular permissions, a robust built-in toolchain (standard library, linter/formatter, test runner), and full compatibility with Node.js and npm.

# Prerequisites
Foundational concept with no prerequisites.

# Key Properties
1. **TypeScript-ready out of the box** -- Run or import TypeScript without installing anything beyond the Deno CLI; no configuration or additional steps necessary
2. **Secure by default** -- Programs have no access to sensitive APIs (file system, network, environment) unless permissions are explicitly granted
3. **Built-in toolchain** -- Includes a standard library, linter/formatter, test runner, type checker, bundler, and more
4. **Node and npm compatible** -- Fully compatible with Node.js APIs and npm packages
5. **Built on V8, Rust, and Tokio** -- V8 for JavaScript execution, Rust for the runtime implementation, Tokio for the async scheduler
6. **Open source** -- Licensed under an open-source license on GitHub

# Construction / Recognition
- Install on macOS/Linux: `curl -fsSL https://deno.land/install.sh | sh`
- Verify installation: `deno --version`
- Run a script: `deno run script.ts`
- Deno can run JavaScript and TypeScript with no additional tools or configuration

# Context & Application
Deno is used as a general-purpose server-side JavaScript/TypeScript runtime. It is suitable for web servers, CLI tools, scripting, and any application where JavaScript or TypeScript is the language of choice. Its secure-by-default model makes it particularly appropriate for running third-party or untrusted code. Its built-in toolchain reduces the need for external tooling that is common in the Node.js ecosystem (e.g., separate linters, formatters, test runners, TypeScript compilers).

# Examples
From runtime/index.md:
- "Deno is TypeScript-ready out of the box. Zero config or additional steps necessary."
- "Deno is secure by default. Where other runtimes give full access every script they run, Deno allows you to enforce granular permissions."
- "Deno has a robust built-in toolchain. Unlike Node or browser JavaScript, Deno includes a standard library, along with a first-party linter/formatter, test runner, and more."
- "Deno is fully compatible with Node and npm."

# Relationships
## Builds Upon
- V8 JavaScript engine
- Rust programming language
- Tokio asynchronous runtime

## Enables
- deno-security-model
- deno-permissions-system
- ecmascript-modules
- deno-typescript-support
- deno-node-compatibility

## Related
- deno-architecture
- jsr-registry

## Contrasts With
- Node.js (no built-in security sandbox, requires external tooling for TypeScript/linting/formatting)

# Common Errors
1. Assuming Deno requires a `tsconfig.json` or separate TypeScript tooling -- Deno handles TypeScript natively
2. Expecting `node_modules` to be created by default -- Deno uses a global cache unless configured otherwise

# Common Confusions
1. **Deno vs. Node.js** -- Deno is not a fork of Node.js; it is a separate runtime built from scratch with different design principles (security, TypeScript, ESM)
2. **Deno and npm** -- Deno supports npm packages natively via `npm:` specifiers; you do not need to run `npm install` first

# Source Reference
- runtime/index.md: Welcome page describing Deno's key features, installation, and first steps

# Verification Notes
- High confidence: Deno is explicitly defined and described throughout the welcome page
- All feature claims taken directly from source text
