---
# === CORE IDENTIFICATION ===
concept: Compile Attribute
slug: compile-attribute

# === CLASSIFICATION ===
category: core-idioms
subcategory: module-structure
tier: intermediate

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Modules"
chapter_number: null
pdf_page: null
section: "Pre-Defined Module Attributes"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "-compile"
  - "compile option attribute"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-module
extends: []
related:
  - module-declaration
  - export-attribute
  - erlang-compilation
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I set compiler options from within an Erlang source file?"
  - "What is the -compile attribute?"
  - "How do I enable or disable compiler warnings in a module?"
---

# Quick Definition
The `-compile(Options)` attribute specifies compiler options directly within the module source. `Options` is a single option or a list of options that are added to the option list when compiling the module.

# Core Definition
The Erlang Reference Manual states: "`-compile(Options).` -- Compiler options. `Options` is a single option or a list of options. This attribute is added to the option list when compiling the module. See module `compile` in Compiler." (Modules, "Pre-Defined Module Attributes" section).

# Prerequisites
- **erlang-module** -- The compile attribute is a module attribute

# Key Properties
1. Syntax: `-compile(Options).` where `Options` is a single option or a list
2. Options specified here are added to (not replacing) the compiler's option list
3. Common options include `export_all`, `nowarn_unused_vars`, `inline`, `{inline, [F/A, ...]}`
4. Must be placed before any function declarations
5. Multiple `-compile` attributes can appear in the same module

# Construction / Recognition
## To Construct/Create:
1. Single option: `-compile(export_all).`
2. List of options: `-compile([export_all, nowarn_unused_function]).`
3. Parameterized option: `-compile({inline, [{my_fun, 1}]}).`

## To Identify/Recognize:
1. The `-compile(...)` attribute containing option atoms or a list of option atoms/tuples

# Context & Application
The compile attribute is useful for setting module-specific compiler behavior without requiring command-line flags. Common uses include: enabling `export_all` during development, suppressing specific warnings, requesting inlining of specific functions, and controlling native compilation. In production code, `export_all` is discouraged as it exposes all functions as public API.

# Examples
**Example 1** (development convenience):
```erlang
-module(my_module).
-compile(export_all).  % export all functions (development only)
```

**Example 2** (multiple options):
```erlang
-module(my_module).
-compile([nowarn_unused_function, {inline, [{helper/1}]}]).
```

# Relationships
## Builds Upon
- **erlang-module** -- Compile is a module attribute

## Enables
- **erlang-compilation** -- Influences how the compiler processes the module

## Related
- **export-attribute** -- `export_all` compile option is an alternative to listing exports
- **module-declaration** -- Another pre-defined module attribute

## Contrasts With
None.

# Common Errors
- **Error**: Using `-compile(export_all)` in production code
  **Correction**: Explicitly list exported functions with `-export` to maintain a clear public API

- **Error**: Placing `-compile` after function declarations
  **Correction**: Pre-defined module attributes must be placed before any function declarations

# Common Confusions
- **Confusion**: Thinking `-compile` options override command-line options
  **Clarification**: The attribute options are added to the option list, not replacing it. Both sources of options are in effect.

# Source Reference
"Modules" chapter, "Pre-Defined Module Attributes" section.

# Verification Notes
- Definition source: Direct quote from source
- Confidence rationale: High -- explicit definition in source
- Uncertainties: Specific option details are in the `compile` module documentation, not in this section
- Cross-reference status: All slugs correspond to planned or existing cards
