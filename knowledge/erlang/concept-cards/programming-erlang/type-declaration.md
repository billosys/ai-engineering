---
# === CORE IDENTIFICATION ===
concept: Type Declaration
slug: type-declaration

# === CLASSIFICATION ===
category: data-types
subcategory: typespecs
tier: intermediate

# === PROVENANCE ===
source: "Programming Erlang, Second Edition"
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Types"
chapter_number: 9
pdf_page: null
section: "Specifying Data and Function Types"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "-type"
  - "type alias"
  - "user-defined type"
  - "new type"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-type-notation
extends: []
related:
  - type-specification
  - exported-and-opaque-types
contrasts_with:
  - type-specification
  - exported-and-opaque-types

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a -type declaration in Erlang?"
  - "How do I define a new named data type?"
  - "What are type variables in a type declaration?"
---

# Quick Definition

A type declaration (`-type`) introduces a new named data type, optionally parameterized by type variables. It lets you give meaningful names to data structures and reuse them in specs and other type definitions.

# Core Definition

New types are defined with the syntax `-type NewTypeName(TVar1, TVar2, ... TVarN) :: Type.`, where `TVar1` to `TVarN` are optional type variables and `Type` is a type expression (Armstrong, "Types," "The Grammar of Types"). For example, `-type direction() :: north | south | east | west.` introduces a type `direction()` whose value is one of those four atoms; `-type point() :: {integer(), integer()}.` defines a tuple of two integers. The notation `[X]` denotes a list of type `X`. Type declarations make code "easier to understand and maintain and can be used to detect errors at compile time" (chapter introduction).

# Prerequisites

- **Erlang type notation** — A `-type` body is a type expression; you must understand the type grammar (unions, tuples, lists, ranges) to write one.

# Key Properties

1. Introduced with the `-type` module attribute.
2. Form: `-type Name(TypeVars) :: TypeExpression.`
3. May be parameterized by type variables, e.g. `-type dict(Key, Val) :: [{Key, Val}].`
4. The body can be a union, a tuple, a list, an integer range (`Min..Max`), an atom, or any combination thereof.
5. Named types are referenced by `name()` (with parentheses) in specs and other type definitions.
6. A set of predefined type aliases exists (`boolean()`, `byte()`, `string()`, `iolist()`, `mfa()`, `timeout()`, etc.) defined the same way.

# Construction / Recognition

## To Construct/Create:
1. Choose a descriptive type name.
2. Decide whether type variables are needed (for generic container types).
3. Write `-type Name(...) :: ` followed by the type expression.
4. Reference the new type as `Name()` in `-spec` attributes and other `-type` definitions.

## To Identify/Recognize:
1. Look for a module attribute beginning with `-type` (or `-opaque`).
2. The `::` separates the type name from its definition.

# Context & Application

- **Typical contexts**: Module headers, alongside `-spec` attributes; building a vocabulary of domain types for a module.
- **Common applications**: Naming data shapes for documentation and Dialyzer analysis; defining generic container types via type variables.
- **Historical/stylistic notes**: Armstrong calls writing good type annotations "as much of an art as writing good clear code," balancing precision against verbosity.

# Examples

**Example 1** ("Specifying Data and Function Types"): `-type route() :: [{go, direction(), integer()}].` — a list of 3-tuples each containing the atom `go`, a `direction()`, and an integer.

**Example 2** ("The Grammar of Types"): `-type angle() :: {Degrees::0..360, Minutes::0..60, Seconds::0..60}.` — a 3-tuple of bounded integers, with annotated field names.

**Example 3** ("The Grammar of Types"): `-type dict(Key,Val) :: [{Key,Val}].` — a parameterized dictionary type defined as a list of key/value tuples.

# Relationships

## Builds Upon
- **Erlang type notation** — A declaration's body is written in the type grammar.

## Enables
- **Type specification** — `-spec` attributes reference named types created by `-type`.

## Related
- **Exported and opaque types** — Named types may be exported or made opaque to other modules.

## Contrasts With
- **Type specification** — `-type` defines a data type; `-spec` annotates a function.
- **Exported and opaque types** — `-opaque` hides a type's internal structure; a plain `-type` does not.

# Common Errors

- **Error**: Referencing a named type without parentheses, e.g. `point` instead of `point()`.
  **Correction**: Always write named types with empty (or filled) parentheses: `point()`, `dict(K,V)`.

- **Error**: Over-specifying types into long verbose expressions that hurt readability.
  **Correction**: Balance precision and verbosity; factor complex shapes into separate named types.

# Common Confusions

- **Confusion**: Thinking `-type` checks data at runtime.
  **Clarification**: A `-type` is purely a static annotation; it has no runtime effect.

- **Confusion**: Believing predefined aliases like `string()` are language primitives.
  **Clarification**: They are themselves `-type` aliases (e.g. `-type string() :: [char()].`).

# Source Reference

Chapter 9: "Types," sections "Specifying Data and Function Types," "The Grammar of Types," and "Predefined Types." EPUB source — no page numbers.

# Verification Notes

- Definition source: Direct adaptation of the `-type` grammar and examples from the named sections.
- Confidence rationale: HIGH — the source gives the explicit grammar rule and multiple examples.
- Uncertainties: None.
- Cross-reference status: Verified slugs against planned chapter-9 cards.
- Re-extraction notes: Fresh extraction; prior card for this slug overwritten.
