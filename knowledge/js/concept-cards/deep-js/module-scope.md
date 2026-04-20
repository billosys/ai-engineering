---
# === CORE IDENTIFICATION ===
concept: Module Scope
slug: module-scope

# === CLASSIFICATION ===
category: language-mechanics
subcategory: scoping
tier: intermediate

# === PROVENANCE ===
source: "Deep JavaScript"
source_slug: deep-js
authors: "Dr. Axel Rauschmayer"
chapter: "A detailed look at global variables"
chapter_number: 5
section: "5.5.1 Script scope and module scopes"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - ESM scope
  - ECMAScript module scope

# === TYPED RELATIONSHIPS ===
prerequisites:
  - script-scope
  - global-environment
extends:
  - lexical-scope
related:
  - declarative-environment-record
contrasts_with:
  - script-scope

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does the global scope differ from module scope?"
---

# Quick Definition

Module scope is the individual scope of each ECMAScript module, which is a subscope of the global (script) scope, meaning module-level declarations are local to the module and not globally visible.

# Core Definition

As described in "Deep JavaScript" (Ch 5, Section 5.5.1): "In contrast, each module has its own scope that is a subscope of the script scope." The chapter illustrates this with a block analogy showing module scopes nested inside the global scope. Because module code is never in global scope, "the rules governing global variables rarely matter for module-based code." Each module's environment has the global environment as its outer environment.

# Prerequisites

- **Script scope** — Module scope is a subscope of script scope.
- **Global environment** — Module environments chain to the global environment via `outer`.

# Key Properties

1. Each module has its **own** scope (separate from other modules).
2. Module scope is a **subscope** of global (script) scope.
3. Module-level declarations are **not** global variables.
4. Module environments' `outer` reference points to the global environment.
5. Variables must be explicitly exported/imported to be shared between modules.
6. Never in global scope — global variable rules rarely matter.

# Construction / Recognition

## To Construct/Create:
1. Use `<script type="module">` in HTML.
2. Use `.mjs` files or `"type": "module"` in Node.js.
3. Write code at the top level of a module file.

## To Identify/Recognize:
1. Code at the top level of an ES module is in module scope, not global scope.

# Context & Application

Module scope is the default for modern JavaScript development. Because most modern code lives in modules, the complexities of global scope (dual environment records, global object pollution) are largely avoided. Module scope variables are private by default and shared only through the export/import system.

# Examples

**Example 1** (Ch 5): Nested scope visualization:
```js
{ // Global scope (scope of *all* scripts)
  // (Global variables)
  { // Scope of module 1
    ···
  }
  { // Scope of module 2
    ···
  }
}
```

**Example 2** (Ch 5): From the summary diagram: "Each ECMAScript module has its own environment whose outer environment is the global environment."

# Relationships

## Builds Upon
- **Script scope** — Module scope is a subscope of script scope.
- **Global environment** — Module environments have global environment as outer.

## Enables
- **Encapsulation** — Module-level variables are private by default.
- **Explicit sharing** — Only exported values are accessible from other modules.

## Related
- **Declarative environment record** — Module environments use declarative records.

## Contrasts With
- **Script scope** — Script scope is global and shared; module scope is local to each module.

# Common Errors

- **Error**: Expecting module-level `const` to be accessible in other modules without export.
  **Correction**: Module-level declarations are local. Use `export` to share them.

- **Error**: Using `var` in a module expecting it to create a global variable.
  **Correction**: In modules, `var` is scoped to the module, not the global scope. It does not create a global object property.

# Common Confusions

- **Confusion**: Module scope and global scope are the same because modules can access global variables.
  **Clarification**: Module scope can *access* global variables (via the outer chain), but module-level declarations are not global. The scopes are different.

# Source Reference

Chapter 5: A detailed look at global variables, Section 5.5.1, lines 187-212, and Section 5.6, lines 311-323.

# Verification Notes

- Definition source: direct (quoted from source)
- Confidence rationale: Explicit definition with visualization
- Cross-reference status: verified
