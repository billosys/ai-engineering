---
# === CORE IDENTIFICATION ===
concept: Auto-Imported BIFs
slug: auto-imported-bifs

# === CLASSIFICATION ===
category: functions-pattern-matching
subcategory: function-declarations
tier: foundational

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Functions"
chapter_number: null
pdf_page: null
section: "Built-In Functions (BIFs)"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "auto-import"
  - "implicitly imported BIFs"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - built-in-functions
extends:
  - built-in-functions
related:
  - function-calls
  - bif-name-clash-resolution
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are auto-imported BIFs?"
  - "Why can I call some BIFs without the erlang: prefix?"
  - "Which BIFs are auto-imported?"
---

# Quick Definition

Auto-imported BIFs are commonly used built-in functions from the `erlang` module that can be called without the `erlang:` module prefix. They include type conversion BIFs and guard-allowed BIFs.

# Core Definition

The Erlang Reference Manual states: "The most commonly used BIFs belonging to `erlang` are _auto-imported_. They do not need to be prefixed with the module name. Which BIFs are auto-imported is specified in the `erlang` module in ERTS. For example, standard-type conversion BIFs like `atom_to_list` and BIFs allowed in guards can be called without specifying the module name." (Erlang Reference Manual, "Functions", "Built-In Functions (BIFs)").

# Prerequisites

- **built-in-functions** -- Must understand what BIFs are before understanding the auto-import mechanism

# Key Properties

1. Auto-imported BIFs do not need the `erlang:` module prefix
2. The set of auto-imported BIFs is specified in the `erlang` module documentation
3. Includes type conversion BIFs (e.g., `atom_to_list/1`)
4. Includes BIFs allowed in guard expressions (e.g., `is_integer/1`, `length/1`)
5. Auto-import can be suppressed with `-compile({no_auto_import,[F/A]})`
6. Local functions with the same name take precedence over auto-imported BIFs (since R14A)

# Construction / Recognition

## To Identify/Recognize:
1. A function call without a module prefix that is not locally defined or explicitly imported is likely an auto-imported BIF
2. Guard-allowed functions called in guards are auto-imported BIFs

# Context & Application

Auto-importing makes Erlang code more concise by eliminating the need to write `erlang:` before common operations. The mechanism is transparent until a local function name clashes with an auto-imported BIF, at which point the `no_auto_import` directive or explicit module qualification becomes necessary.

# Examples

**Example 1** (Built-In Functions section): Auto-imported BIFs called without module prefix:
```erlang
1> tuple_size({a,b,c}).
3
2> atom_to_list('Erlang').
"Erlang"
```

Both `tuple_size/1` and `atom_to_list/1` are auto-imported from `erlang` and called without the `erlang:` prefix.

# Relationships

## Builds Upon
- **built-in-functions** -- Auto-imported BIFs are a subset of all BIFs

## Enables
- **bif-name-clash-resolution** -- Name clashes with auto-imported BIFs require resolution

## Related
- **function-calls** -- Auto-import affects how implicitly qualified calls are resolved

# Common Errors

- **Error**: Defining a local function with the same name as a pre-R14A auto-imported BIF without adding `-compile({no_auto_import,[F/A]})`
  **Correction**: Use the `no_auto_import` directive to suppress auto-import for that specific BIF

# Common Confusions

- **Confusion**: Assuming auto-imported BIFs are language keywords or special forms
  **Clarification**: Auto-imported BIFs are regular functions that happen to be callable without module qualification; they can be explicitly called as `erlang:function/arity`

# Source Reference

"Functions" chapter, section "Built-In Functions (BIFs)", paragraph on auto-import.

# Verification Notes

- Definition source: Direct quotes from source text
- Confidence rationale: HIGH -- explicit definition in source
- Uncertainties: None
- Cross-reference status: Verified against planned slugs
