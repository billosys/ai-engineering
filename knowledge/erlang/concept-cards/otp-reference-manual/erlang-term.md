---
# === CORE IDENTIFICATION ===
concept: Erlang Term
slug: erlang-term

# === CLASSIFICATION ===
category: data-types
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Data Types"
chapter_number: null
pdf_page: null
section: "Terms"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - term

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - integer
  - float
  - atom
  - tuple
  - list
  - binary
  - bit-string
  - pid
  - reference
  - port-identifier
  - fun
  - map
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an Erlang term?"
  - "How do atoms, tuples, and lists form the foundation of Erlang's type system?"
---

# Quick Definition
A term is a piece of data of any data type in Erlang. Every value in Erlang -- whether an integer, atom, tuple, list, map, binary, pid, reference, port, or fun -- is a term.

# Core Definition
The Erlang Reference Manual defines a term simply: "A piece of data of any data type is called a _term_." (Data Types, "Terms" section). This is the universal designation for any Erlang value. The manual also notes that "Erlang has no user-defined types, only composite types (data structures) made of Erlang terms," meaning that all complex data structures are ultimately built from terms of the built-in types.

# Prerequisites
This is a foundational concept with no prerequisites within this source.

# Key Properties
1. A term is any piece of data of any Erlang data type
2. Erlang has no user-defined types; all composite structures are made of terms
3. Any function testing for a composite type (e.g., `is_type/1`) might return `true` for a term that coincidentally matches the representation
4. Built-in type test functions do not suffer from the composite-type ambiguity

# Construction / Recognition
## To Construct/Create:
1. Write any literal value (integer, float, atom, string, binary, tuple, list, map)
2. Call any function that returns a value (e.g., `make_ref/0`, `self/0`, `spawn/3`)
3. Compose data structures from other terms

## To Identify/Recognize:
1. Every value in Erlang is a term
2. Use type-test BIFs (`is_integer/1`, `is_atom/1`, `is_tuple/1`, etc.) to identify the specific type of a term

# Context & Application
The concept of "term" is fundamental to Erlang's type system. Since Erlang is dynamically typed, any variable can hold any term. The term concept is pervasive in documentation, type specifications, and function signatures -- `term()` is the top type in Erlang's type system, equivalent to `any()`. Understanding that everything is a term is essential for working with pattern matching, message passing, and ETS/Mnesia storage.

# Examples
**Example 1** (Data Types, "Terms" section): The manual states that Erlang has no user-defined types, meaning that a function like `is_type/1` for a composite type "might return `true` for a term that coincides with the chosen representation."

# Relationships
## Builds Upon
This is the root concept; all data types are kinds of terms.

## Enables
- **integer** -- Integers are a specific kind of term
- **atom** -- Atoms are a specific kind of term
- **tuple** -- Tuples are composite terms
- **list** -- Lists are composite terms
- **map** -- Maps are composite terms
- **binary** -- Binaries are a specific kind of term

## Related
- **pid** -- Process identifiers are terms
- **reference** -- References are terms
- **fun** -- Function objects are terms

## Contrasts With
No direct contrasts; term is the universal value concept.

# Common Errors
- **Error**: Assuming that a successful `is_type/1` check on a composite type guarantees the data was created as that type
  **Correction**: Composite type checks can match coincidental representations. For example, a tuple `{person, "Alice", 30}` would pass `is_tuple/1` regardless of whether it was intended as a "person record."

# Common Confusions
- **Confusion**: Believing Erlang has user-defined types like structs or classes
  **Clarification**: Erlang has no user-defined types. Records and other structured data are conventions built on top of existing term types (tuples, maps, native records).

# Source Reference
Data Types chapter, "Terms" section. Also see the introductory note about no user-defined types.

# Verification Notes
- Definition source: Direct quote from source ("A piece of data of any data type is called a _term_.")
- Confidence rationale: High -- explicit, concise definition in source
- Uncertainties: None
- Cross-reference status: All related slugs correspond to planned cards in this extraction
