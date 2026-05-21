---
concept: Compiler Options
slug: compiler-options
category: tooling
subcategory: compiler
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Modules"
chapter_number: 2
pdf_page: null
section: "Compiler Options"
extraction_confidence: high
aliases:
  - "compile flags"
  - "debug_info"
  - "export_all"
prerequisites:
  - compiling-erlang-code
extends: []
related:
  - module-attribute
  - macro
contrasts_with: []
answers_questions:
  - "How do I create and compile a module?"
---

# Compiler Options

## Quick Definition

Compiler options (flags) give control over how a module is compiled. They can be passed to the compiler functions or set inside a module with a `-compile` attribute.

## Core Definition

Erlang includes many compilation flags that give more control over how a module is compiled. Common flags are `debug_info` (keeps debug information for debuggers, code-coverage, and static-analysis tools — recommended to always enable), `{outdir,Dir}` (chooses where `.beam` files are written), `export_all` (ignores `-export` and exports all functions; for testing/development only), and `{d,Macro}` or `{d,Macro,Value}` (defines a macro, often used to conditionally include test functions). Flags can be passed to `compile:file/2` or `c/2`, or set inside a module via `-compile([...])` (Hébert, ch. 2, "Compiler Options").

## Prerequisites

- **Compiling Erlang code** — Options modify the compilation process

## Key Properties

1. `debug_info` retains debug data for tooling; recommended to always enable.
2. `{outdir,Dir}` sets the output directory for `.beam` files.
3. `export_all` exports every function, overriding `-export`; testing/development only.
4. `{d,Macro}` / `{d,Macro,Value}` defines a macro at compile time.
5. Flags are passed to `compile:file/2` or `c/2`, or set with the `-compile` attribute.

## Construction / Recognition

To compile with flags from the shell: `c(Module, [debug_info, export_all])`.

To set flags in the module: add `-compile([debug_info, export_all]).` as a module attribute.

## Context & Application

`debug_info` should generally always be on. `export_all` is convenient during development but must not be used in production. The `{d,Macro}` flag enables conditional compilation, commonly to create test functions only when a test macro is defined.

## Examples

**Example** (ch. 2): `c(useless, [debug_info, export_all]).` returns `{ok,useless}`.

**Example** (ch. 2): `c(Module, [{d,'TEST'},{d,'DEBUGMODE'}]).` defines the `TEST` and `DEBUGMODE` macros for conditional compilation.

## Relationships

### Prerequisites

- **Compiling Erlang code** — Options affect compilation

### Related

- **Module attribute** — `-compile` is the in-module way to set flags
- **Macro** — `{d,Macro}` defines macros used in conditional compilation

## Common Errors

- **Error**: Shipping production code compiled with `export_all`
  **Correction**: Use `export_all` only for testing; rely on `-export` in production

## Common Confusions

- **Confusion**: Believing `debug_info` significantly bloats compiled code
  **Clarification**: The space cost is small and almost always worth the tooling benefits

## Source Reference

Chapter 2: "Modules," section "Compiler Options."

## Verification Notes

- Definition: Adapted from the "Compiler Options" section
- Confidence: HIGH — explicit section listing the common flags
- Uncertainties: None
