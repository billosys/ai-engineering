---
# === CORE IDENTIFICATION ===
concept: module_info
slug: module-info

# === CLASSIFICATION ===
category: core-idioms
subcategory: module-structure
tier: intermediate

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "The Rest of Sequential Erlang"
chapter_number: 8
pdf_page: null
section: "Attributes"

# === CONFIDENCE ===
extraction_confidence: medium

# === VARIANTS (authority control) ===
aliases:
  - "module_info/0"
  - "module_info/1"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - module-attributes
extends: []
related:
  - module-attributes
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I inspect a compiled module's metadata?"
  - "What functions does module_info provide?"
---

# Quick Definition

`module_info/0` and `module_info/1` are functions automatically created for every compiled module that return its metadata — exports, imports, attributes, and compile information.

# Core Definition

"`attrs:module_info()` returns a property list of all the metadata associated with a compiled module. `attrs:module_info(X)`, where `X` is one of `exports`, `imports`, `attributes`, or `compile`, returns the individual attribute associated with the module" ("The Rest of Sequential Erlang", *Attributes*). "The functions `module_info/0` and `module_info/1` are automatically created every time a module is compiled." User-defined attributes from the source file reappear as a subterm of `{attributes, ...}`; the `{compile, ...}` tuple holds compiler-added information. Running `module_info` requires the module's BEAM code to be loaded; the same data can be extracted *without* loading via the `beam_lib` module.

# Prerequisites

- **Module attributes** — `module_info` exists to expose a module's attributes and metadata.

# Key Properties

1. `module_info/0` returns a property list of all module metadata.
2. `module_info/1` accepts `exports`, `imports`, `attributes`, or `compile` and returns just that part.
3. Both functions are auto-generated for every compiled module.
4. User-defined attributes appear under `{attributes, ...}`.
5. Compiler-added data (including the compiler version) appears under `{compile, ...}`.
6. Running `module_info` requires the module to be loaded; `beam_lib:chunks` reads the same data without loading.

# Construction / Recognition

## To Construct/Create:
1. Call `Mod:module_info()` for the full property list.
2. Call `Mod:module_info(exports)` (or `imports`/`attributes`/`compile`) for one part.

## To Identify/Recognize:
1. The auto-generated `module_info/0` and `module_info/1` always appear in a module's own export list.

# Context & Application

- **Typical contexts**: introspecting modules — listing exported functions, reading attributes.
- **Common applications**: Exercise 2 of the chapter uses `Mod:module_info()` over `code:all_loaded()` to find which module exports the most functions.
- **Historical/stylistic notes**: use `beam_lib:chunks` when you want attribute data but do not want to load the module.

# Examples

**Example 1** (*Attributes*): the metadata property list:

```erlang
1> attrs:module_info().
[{exports,[{fac,1},{module_info,0},{module_info,1}]},
 {imports,[]},
 {attributes,[{vsn,[1234]},
              {author,[{joe,armstrong}]},
              {purpose,"example of attributes"}]},
 {compile,[{options,[]},
           {version,"4.8"},
           {time,{2013,5,3,7,36,55}},
           {source,"/Users/joe/jaerlang2/code/attrs.erl"}]}]
```

# Relationships

## Builds Upon
- **Module attributes** — `module_info` reports the attributes declared in a module.

## Enables
- This concept does not have downstream cards in scope.

## Related
- **Module attributes** — The metadata `module_info` returns is largely the module's attributes.

## Contrasts With
- No directly contrasting concept in scope.

# Common Errors

- **Error**: Calling `module_info` on a module whose BEAM code is not loaded.
  **Correction**: Load the module first, or use `beam_lib:chunks` to read attributes without loading.

# Common Confusions

- **Confusion**: Thinking the `{version, ...}` entry is the module's `-vsn`.
  **Clarification**: `{version, "4.8"}` under `{compile, ...}` is the *compiler* version; the module's `-vsn` appears under `{attributes, ...}`.

# Source Reference

Chapter 8: "The Rest of Sequential Erlang", section "Attributes".

# Verification Notes

- Definition source: Direct quotation and adaptation from the *Attributes* section.
- Confidence rationale: MEDIUM — the source describes `module_info` clearly but only as part of the broader Attributes section, with one example.
- Uncertainties: The full set of `module_info/1` keys beyond the four named is not enumerated by the source.
- Cross-reference status: Slug `module-attributes` extracted in this chapter.
- Re-extraction notes: Fresh extraction; no prior card existed for this slug.
