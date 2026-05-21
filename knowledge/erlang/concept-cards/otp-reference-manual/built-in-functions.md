---
# === CORE IDENTIFICATION ===
concept: Built-In Functions (BIFs)
slug: built-in-functions

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
  - "BIFs"
  - "built-ins"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - function-declaration
  - function-arity
extends: []
related:
  - auto-imported-bifs
  - function-calls
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a BIF in Erlang?"
  - "Where are BIFs implemented?"
  - "Which modules contain BIFs?"
---

# Quick Definition

Built-In Functions (BIFs) are functions implemented in C in the Erlang runtime system, performing operations that are difficult or impossible to implement in pure Erlang. Most BIFs belong to the `erlang` module.

# Core Definition

The Erlang Reference Manual states: "Built-In Functions (BIFs) are implemented in C code in the runtime system. BIFs do things that are difficult or impossible to implement in Erlang. Most of the BIFs belong to module `erlang`, but there are also BIFs belonging to a few other modules, for example `lists` and `ets`." (Erlang Reference Manual, "Functions", "Built-In Functions (BIFs)").

# Prerequisites

- **function-declaration** -- Understanding function declarations provides context for how BIFs are called
- **function-arity** -- BIFs are identified by name/arity like regular functions

# Key Properties

1. BIFs are implemented in C, not Erlang
2. They perform operations difficult or impossible in pure Erlang
3. Most BIFs belong to the `erlang` module
4. Some BIFs belong to other modules (e.g., `lists`, `ets`)
5. Commonly used BIFs from the `erlang` module are auto-imported
6. Auto-imported BIFs can be called without the module prefix
7. Type conversion BIFs (e.g., `atom_to_list`) and guard BIFs are typically auto-imported

# Construction / Recognition

## To Identify/Recognize:
1. Functions that can be called without a module prefix and are not locally defined are likely auto-imported BIFs
2. BIF documentation is in the `erlang` module reference in ERTS
3. Guard-allowed functions (like `is_integer/1`, `length/1`) are BIFs

# Context & Application

BIFs provide the fundamental operations that bridge Erlang code and the runtime system: type checking (`is_atom/1`), type conversion (`atom_to_list/1`), process management (`spawn/3`), and arithmetic. The auto-import mechanism makes commonly used BIFs feel like language primitives. A complete list of BIFs is documented in the `erlang` module in ERTS.

# Examples

**Example 1** (Built-In Functions section): Calling auto-imported BIFs without module prefix:
```erlang
1> tuple_size({a,b,c}).
3
2> atom_to_list('Erlang').
"Erlang"
```

# Relationships

## Builds Upon
- **function-declaration** -- BIFs are called like regular functions
- **function-arity** -- BIFs are identified by name/arity

## Enables
- **auto-imported-bifs** -- The most common BIFs are auto-imported for convenience

## Related
- **function-calls** -- BIFs are called using the same syntax as regular functions
- **bif-name-clash-resolution** -- Local functions can clash with auto-imported BIFs

# Common Errors

- **Error**: Assuming all functions in the `erlang` module are BIFs
  **Correction**: The `erlang` module contains BIFs, but not every function there may be implemented in C; refer to the ERTS documentation for the authoritative BIF list

# Common Confusions

- **Confusion**: Thinking BIFs are special syntax or operators
  **Clarification**: BIFs are regular functions with standard call syntax; they just happen to be implemented in C rather than Erlang

# Source Reference

"Functions" chapter, section "Built-In Functions (BIFs)", with `tuple_size` and `atom_to_list` examples.

# Verification Notes

- Definition source: Direct quotes from source text
- Confidence rationale: HIGH -- explicit definition with examples in source
- Uncertainties: None
- Cross-reference status: Verified against planned slugs
