---
# === CORE IDENTIFICATION ===
concept: Export Attribute
slug: export-attribute

# === CLASSIFICATION ===
category: api-design
subcategory: module-interface
tier: foundational

# === PROVENANCE ===
source: "Programming Erlang, Second Edition"
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Modules and Functions"
chapter_number: 4
pdf_page: null
section: "Modules Are Where We Store Code"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "-export"
  - export declaration
  - "-import"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - module
  - function
extends: []
related:
  - compiling-modules
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I make a function callable from outside its module?"
  - "What is the export declaration?"
---

# Quick Definition

The `-export` attribute lists which of a module's functions may be called from outside the module. Exported functions are public; functions not exported are private.

# Core Definition

"Following the module declaration is an *export declaration*. The export declaration tells which functions in the module can be called from *outside* the module. They are like *public* declarations in many programming languages. Functions that are not in an export declaration are private and cannot be called from outside the module" (Chapter 1, "Modeling Concurrency"). The argument is a list of `Name/Arity` items: "The notation `Name/N` means a function called `Name` with `N` arguments; `N` is called the *arity* of the function" (Chapter 4, "Modules Are Where We Store Code"). Thus `-export([area/1])` exports the one-argument `area` function. The complementary `-import` declaration brings functions in from another module — "`-import(lists, [map/2, sum/1]).` means the function `map/2` is *imported* from the module `lists`" so it can be called as `map(...)` instead of `lists:map(...)` (Chapter 4, "Simple List Processing").

# Prerequisites

- **Module** — `-export` is a module attribute; it exists only within a module.
- **Function** — It lists functions by name and arity.

# Key Properties

1. `-export` is a module attribute declaring the module's public functions.
2. Its argument is a list of `Name/Arity` items, e.g. `[area/1, test/0]`.
3. `Name/N` denotes a function named `Name` taking `N` arguments (arity `N`).
4. Exported functions are equivalent to public methods; non-exported functions are private.
5. Only exported functions can be called from outside the module.
6. The complementary `-import(Module, [Funcs])` brings in functions so they can be called unqualified.

# Construction / Recognition

## To Export Functions:
1. After the `-module` line, write `-export([Name1/Arity1, Name2/Arity2, ...]).`.
2. Include every function that callers outside the module need.

## To Import Functions:
1. Write `-import(SourceModule, [Name/Arity, ...]).` to call them without the module prefix.

## To Recognize It:
1. A module line of the form `-export([...]).` or `-import(mod, [...]).`.

# Context & Application

- **Typical contexts**: Defining the public interface of every module.
- **Common applications**: `-export([start/1, loop/1]).` for a server; exporting `total/1` as a module's one public entry point.
- **Historical/stylistic notes**: Exported functions = public methods, non-exported = private methods, in the OOP analogy.

# Examples

**Example 1** (Chapter 4, "Modules Are Where We Store Code"): `-export([area/1]).` makes the one-argument `area` function callable from outside the `geometry` module.

**Example 2** (Chapter 4, "Simple List Processing"): In `shop2`, `-import(lists, [map/2, sum/1]).` lets the code write `map(Fun, ...)` instead of `lists:map(Fun, ...)`, while `-export([total/1])` exposes `total/1`.

# Relationships

## Builds Upon
- **Module** — `-export` is part of a module's header.
- **Function** — It references functions by name and arity.

## Enables
- **Compiling modules** — A compiled module exposes exactly its exported functions to callers.

## Related
- **Compiling modules** — Export information is what makes functions callable after compilation.

## Contrasts With
- No directly contrasting concept; `-import` is the complementary attribute, covered here.

# Common Errors

- **Error**: Calling `module:function(...)` for a function not in `-export`.
  **Correction**: Add the function (with the correct arity) to the `-export` list, or it stays private.

- **Error**: Exporting `area` without its arity.
  **Correction**: Export entries are `Name/Arity`, e.g. `area/1`; the arity is required.

# Common Confusions

- **Confusion**: Thinking `/1` in `area/1` means division by one.
  **Clarification**: `/N` denotes arity — the number of arguments — not division.

- **Confusion**: Believing all functions in a module are callable from outside.
  **Clarification**: Only functions listed in `-export` are public; the rest are private.

# Source Reference

"Programming Erlang, Second Edition," Chapter 4: Modules and Functions, sections "Modules Are Where We Store Code" and "Simple List Processing"; Chapter 1: Introducing Concurrency, "Modeling Concurrency." EPUB-origin source; no page numbers.

# Verification Notes

- Definition source: Direct quotations from Chapter 1, "Modeling Concurrency," and Chapter 4, "Modules Are Where We Store Code."
- Confidence rationale: HIGH — the export declaration and `Name/Arity` notation are explicitly defined.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction; no pre-existing card.
