---
# === CORE IDENTIFICATION ===
concept: Arity
slug: arity

# === CLASSIFICATION ===
category: functions-pattern-matching
subcategory: function-definition
tier: foundational

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "The Rest of Sequential Erlang"
chapter_number: 8
pdf_page: null
section: "Arity"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - function arity
  - "Name/N"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - module-attributes
  - function-reference
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the arity of a function?"
  - "Are two functions with the same name but different arity the same function?"
  - "Why are auxiliary functions named with the same name and different arity?"
---

# Quick Definition

The arity of a function is the number of arguments it accepts. In Erlang, two functions with the same name but different arity are entirely different functions.

# Core Definition

"The *arity* of a function is the number of arguments that the function has. In Erlang, two functions with the same name and different arity in the same module represent *entirely* different functions. They have *nothing* to do with each other apart from a coincidental use of the same name" ("The Rest of Sequential Erlang", *Arity*). A function is identified by the pair `Name/Arity` — for example `sum/1` and `sum/2` are two distinct functions. By convention, Erlang programmers use same-name/different-arity functions as auxiliary functions, and often hide the auxiliary by not exporting it.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Arity is the count of arguments a function takes.
2. A function is uniquely identified by `Name/Arity`.
3. Same name + different arity = entirely different functions.
4. Auxiliary functions are conventionally given the main function's name with a higher arity.
5. An auxiliary function is often "hidden" by not exporting it.

# Construction / Recognition

## To Construct/Create:
1. Define functions of different arity under one name: `sum/1` and `sum/2`.

## To Identify/Recognize:
1. Refer to a function as `Name/Arity` (e.g. in `-export` lists and function references).

# Context & Application

- **Typical contexts**: every function definition and export declaration.
- **Common applications**: `sum(L) -> sum(L, 0).` delegates to the auxiliary `sum/2` accumulator function.
- **Historical/stylistic notes**: choosing `sum/2` over an invented name like `hedgehog/2` gives the reader a clue about the helper's purpose without inventing a new name.

# Examples

**Example 1** (*Arity*): two distinct functions sharing a name:

```erlang
sum(L) -> sum(L, 0).

sum([], N)    -> N;
sum([H|T], N) -> sum(T, H+N).
```

`sum/1` and `sum/2` are different functions; a module defining `sum(L)` would export only `sum/1`, hiding `sum/2`.

# Relationships

## Builds Upon
- This is a foundational concept.

## Enables
- This concept does not have downstream cards in scope.

## Related
- **Module attributes** — `-export` and `-import` lists name functions as `Name/Arity`.
- **Function reference** — `fun Name/Arity` uses arity to identify the function.

## Contrasts With
- No directly contrasting concept in scope.

# Common Errors

- **Error**: Calling `abc:a(5)` when only `a/2` is exported.
  **Correction**: `a/1` and `a/2` are different functions; export the specific arity you need to call.

# Common Confusions

- **Confusion**: Thinking same-name functions of different arity are overloads of one function.
  **Clarification**: They are entirely separate functions that merely share a name; arity is part of the function's identity.

# Source Reference

Chapter 8: "The Rest of Sequential Erlang", section "Arity".

# Verification Notes

- Definition source: Direct quotation from *Arity*.
- Confidence rationale: HIGH — the source explicitly defines arity and the same-name/different-arity rule with an example.
- Uncertainties: None.
- Cross-reference status: Slugs `module-attributes`, `function-reference` extracted in this chapter.
- Re-extraction notes: Fresh extraction; no prior card existed for this slug.
