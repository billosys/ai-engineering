---
# === CORE IDENTIFICATION ===
concept: Function Arity
slug: function-arity

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
section: "Function Declaration Syntax"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "arity"
  - "argument count"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - function-declaration
extends: []
related:
  - function-clause
  - built-in-functions
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is arity in Erlang?"
  - "How are Erlang functions uniquely identified?"
  - "What does mod:f/N notation mean?"
---

# Quick Definition

The arity of a function is the number of its arguments. A function is uniquely identified by the combination of module name, function name, and arity, commonly denoted as `mod:f/N`.

# Core Definition

The Erlang Reference Manual states: "The number of arguments `N` is the _arity_ of the function. A function is uniquely defined by the module name, function name, and arity. That is, two functions with the same name and in the same module, but with different arities are two different functions." The conventional notation is described: "A function named `f` in module `mod` and with arity `N` is often denoted as `mod:f/N`." (Erlang Reference Manual, "Functions", "Function Declaration Syntax").

# Prerequisites

- **function-declaration** -- Understanding function declarations is needed to understand arity as part of identity

# Key Properties

1. Arity is the number of arguments a function takes
2. The triple (module, name, arity) uniquely identifies a function
3. Same name, different arity = different functions
4. The notation `mod:f/N` denotes function `f` in module `mod` with arity `N`
5. Arity is a non-negative integer

# Construction / Recognition

## To Construct/Create:
1. Count the number of arguments in the function declaration
2. Use the notation `Module:Function/Arity` to refer to the function

## To Identify/Recognize:
1. The `/N` suffix in function references indicates arity
2. `-export([f/1, f/2]).` exports two different functions both named `f`

# Context & Application

Arity is central to Erlang's function identity model. It enables function overloading by argument count (unlike many languages where overloading is by type). The `mod:f/N` notation is used universally in documentation, error messages, export declarations, and the `fun Module:Function/Arity` syntax. Understanding that `f/1` and `f/2` are distinct functions is essential for reading Erlang code and documentation.

# Examples

**Example 1** (Function Declaration Syntax section): "A function named `f` in module `mod` and with arity `N` is often denoted as `mod:f/N`."

**Example 2** (Function Declaration Syntax section): The factorial function is `mod:fact/1` -- it is named `fact`, lives in module `mod`, and takes one argument.

# Relationships

## Builds Upon
- **function-declaration** -- Arity is determined by the number of arguments in the declaration

## Enables
- **function-calls** -- Function calls must match the arity of the declaration
- **built-in-functions** -- BIFs are identified by name/arity (e.g., `erlang:length/1`)

## Related
- **function-clause** -- All clauses of a function must have the same arity

# Common Errors

- **Error**: Calling a function with the wrong number of arguments
  **Correction**: Ensure the call matches the declared arity; `f(X)` calls `f/1`, not `f/2`

# Common Confusions

- **Confusion**: Thinking `f/1` and `f/2` are overloaded versions of the same function
  **Clarification**: They are completely separate functions that happen to share a name; they have independent clause sets and can have unrelated behavior

# Source Reference

"Functions" chapter, section "Function Declaration Syntax", paragraphs on arity and naming notation.

# Verification Notes

- Definition source: Direct quotes from source text
- Confidence rationale: HIGH -- explicit definition with notation convention
- Uncertainties: None
- Cross-reference status: Verified against planned slugs
