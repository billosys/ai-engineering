---
# === CORE IDENTIFICATION ===
concept: NIFs Attribute
slug: nifs-attribute

# === CLASSIFICATION ===
category: core-idioms
subcategory: module-structure
tier: advanced

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
  - "-nifs"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-module
  - export-attribute
  - on-load-function
extends: []
related:
  - erlang-compilation
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I declare which functions may be loaded as NIFs?"
  - "What is the -nifs attribute?"
  - "Why should I use the -nifs attribute?"
---

# Quick Definition
The `-nifs(Functions)` attribute declares which functions in a module may be replaced by native implementations loaded via `erlang:load_nif/2`, enabling the compiler to make better optimization decisions.

# Core Definition
The Erlang Reference Manual states: "`-nifs(Functions).` -- Specifies which of the functions, defined within the module, may be loaded as NIFs with `erlang:load_nif/2`. `Functions` is a list `[Name1/Arity1, ..., NameN/ArityN]`, where each `NameI` is an atom and `ArityI` an integer." The manual further notes: "While not strictly necessary, it is recommended to use the `-nifs()` attribute in any module that loads NIFs, to allow the compiler to make better decisions regarding optimizations." (Modules, "Pre-Defined Module Attributes" section).

# Prerequisites
- **erlang-module** -- NIFs attribute is a module attribute
- **export-attribute** -- NIF functions are typically exported
- **on-load-function** -- NIF libraries are typically loaded via an on_load function

# Key Properties
1. Syntax: `-nifs([Name1/Arity1, ..., NameN/ArityN]).`
2. Not strictly mandatory, but recommended for modules that load NIFs
3. Helps the compiler make better optimization decisions
4. No need to add `-nifs([])` in modules that do not load NIFs
5. The compiler can infer the absence of NIFs from the lack of `erlang:load_nif/2` calls
6. Introduced with special meaning in Erlang/OTP 25.0

# Construction / Recognition
## To Construct/Create:
1. In a module that loads NIFs, add: `-nifs([my_nif_fun/1, another_nif/2]).`
2. Define Erlang fallback implementations for each listed function
3. Load the NIF library via `-on_load` and `erlang:load_nif/2`

## To Identify/Recognize:
1. The `-nifs([...])` attribute in a module
2. Usually accompanied by an `-on_load` attribute and `erlang:load_nif/2` call

# Context & Application
NIFs (Native Implemented Functions) allow performance-critical code to be written in C or Rust and loaded into the Erlang VM. The `-nifs` attribute tells the compiler which functions are NIF candidates, allowing it to avoid optimizations that would conflict with NIF replacement. Without this attribute, the compiler may apply transformations that make NIF loading fail or behave unexpectedly.

# Examples
**Example 1** (declaring NIF functions):
```erlang
-module(crypto_nifs).
-nifs([hash/2, encrypt/3, decrypt/3]).
-on_load(load_nifs/0).

load_nifs() ->
    erlang:load_nif("crypto_nifs", 0).

%% Erlang fallback (called if NIF not loaded)
hash(_Algorithm, _Data) ->
    erlang:nif_error(not_loaded).
```

# Relationships
## Builds Upon
- **erlang-module** -- NIFs attribute is a module attribute
- **on-load-function** -- NIF libraries are loaded via on_load

## Enables
None directly -- it is an advisory attribute for the compiler.

## Related
- **erlang-compilation** -- The attribute influences compiler optimization decisions

## Contrasts With
None.

# Common Errors
- **Error**: Listing a function in `-nifs` that is not defined in the module
  **Correction**: Every function listed in `-nifs` must have a definition in the module (the Erlang fallback)

- **Error**: Adding `-nifs([])` unnecessarily in modules without NIFs
  **Correction**: This is harmless but unnecessary; the compiler already knows from the absence of `erlang:load_nif/2`

# Common Confusions
- **Confusion**: Thinking `-nifs` automatically loads native code
  **Clarification**: `-nifs` only declares which functions may be replaced by NIFs. The actual loading is done by `erlang:load_nif/2`, typically in an `-on_load` function.

# Source Reference
"Modules" chapter, "Pre-Defined Module Attributes" section.

# Verification Notes
- Definition source: Direct quote from source
- Confidence rationale: High -- explicit definition in source
- Uncertainties: None
- Cross-reference status: All slugs correspond to planned or existing cards
