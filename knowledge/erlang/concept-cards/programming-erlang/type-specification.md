---
# === CORE IDENTIFICATION ===
concept: Type Specification
slug: type-specification

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
  - "-spec"
  - "function spec"
  - "spec attribute"
  - "function specification"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-type-notation
extends: []
related:
  - type-declaration
  - dialyzer
  - exported-and-opaque-types
contrasts_with:
  - type-declaration

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a -spec in Erlang?"
  - "How do I declare the types of a function's arguments and return value?"
  - "How does the type system relate to Dialyzer?"
---

# Quick Definition

A type specification (`-spec`) is a module attribute that declares the input argument types and return type of a function. It documents the function's contract and lets Dialyzer check the code for type errors.

# Core Definition

A function specification states what the types of the arguments to a function are and what the type of the return value is. It is written with the `-spec` attribute: "`-spec functionName(T1, T2, ..., Tn) -> Tret when Ti :: Typei, ...`" where `T1`...`Tn` describe the argument types and `Tret` the return type. Additional type variables can be introduced after the optional `when` keyword (Armstrong, "Types," "Specifying the Input and Output Types of a Function"). Writing a `-spec` does not guarantee the function returns — "we have no idea if the function `plan_route` will return anything at all; it might just crash" — but if it does return, the value has the declared type.

# Prerequisites

- **Erlang type notation** — A `-spec` is written in the type grammar; you must read and write type expressions to use it.

# Key Properties

1. Introduced with the `-spec` module attribute.
2. Form: `-spec name(ArgTypes) -> ReturnType.`, optionally followed by a `when` clause binding type variables.
3. Argument positions may be annotated with descriptive variables (e.g. `From::point()`) that link the spec to documentation.
4. A spec is a contract on the return value *if* the function returns; it makes no termination guarantee.
5. Specs work whether or not Dialyzer is run, but they improve the quality of Dialyzer analysis.
6. The official Erlang documentation uses strict rules so spec variable names match the names used in the prose docs.

# Construction / Recognition

## To Construct/Create:
1. Identify the function's arity and argument roles.
2. Write `-spec name(` followed by the type of each argument.
3. Optionally name arguments with `Name::type()` for documentation clarity.
4. Write `-> ` and the return type.
5. If type expressions are long, factor them with a `when` clause: `-> Tret when X :: Type.`

## To Identify/Recognize:
1. Look for a module attribute beginning with `-spec`.
2. The function name and arity precede `->`; the return type follows it.

# Context & Application

- **Typical contexts**: Placed immediately above the function it describes; written for every exported function as a Dialyzer-checkable contract.
- **Common applications**: API documentation, compile-time error detection via Dialyzer, communicating argument roles to readers.
- **Historical/stylistic notes**: Armstrong recommends writing specs for all exported functions *first*, before the code, then uncommenting them as functions are implemented.

# Examples

**Example 1** ("Specifying Data and Function Types"): `-spec plan_route(point(), point()) -> route().` — if `plan_route/2` is called with two `point()` arguments and returns, it returns a `route()`.

**Example 2** ("Specifying Data and Function Types"): `-spec plan_route(From::point(), To::point()) -> ...` — argument names `From` and `To` document the roles the arguments play.

## Worked Example

The `file:open` spec with a `when` qualifier ("Specifying the Input and Output Types of a Function"):

```erlang
-spec file:open(FileName, Modes) -> {ok, Handle} | {error, Why} when
    FileName :: string(),
    Modes    :: [Mode],
    Mode     :: read | write | ...,
    Handle   :: file_handle(),
    Why      :: error_term().
```

The `when` form keeps the descriptive variable names `FileName` and `Modes` so documentation can refer to them by name rather than as "the first argument."

# Relationships

## Builds Upon
- **Erlang type notation** — A spec is an expression in the type grammar.

## Enables
- **Dialyzer** — Specs sharpen the discrepancy analysis Dialyzer performs.

## Related
- **Type declaration** — Specs reference named types created with `-type`.
- **Exported and opaque types** — Specs of cross-module functions use fully qualified type names.

## Contrasts With
- **Type declaration** — `-spec` describes a *function's* signature; `-type` *defines* a named data type.

# Common Errors

- **Error**: Dropping the `when` qualifier and inlining all type expressions, producing an unreadable one-liner.
  **Correction**: Use a `when` clause to name and factor argument types; this also lets documentation refer to arguments by name.

- **Error**: Assuming a `-spec` guarantees the function returns a value.
  **Correction**: A spec only constrains the return value when the function returns; the function may still crash.

# Common Confusions

- **Confusion**: Believing `-spec` and `-type` are interchangeable.
  **Clarification**: `-spec` annotates a function; `-type` defines a reusable named type.

- **Confusion**: Thinking specs are enforced at runtime.
  **Clarification**: Specs are checked statically by Dialyzer (and used for docs); they are not runtime contracts.

# Source Reference

Chapter 9: "Types," sections "Specifying Data and Function Types" and "Specifying the Input and Output Types of a Function." EPUB source — no page numbers.

# Verification Notes

- Definition source: Direct adaptation of the `-spec` form and the `file:open` worked example from the named sections.
- Confidence rationale: HIGH — the source defines the `-spec` form explicitly with grammar and worked examples.
- Uncertainties: None.
- Cross-reference status: Verified slugs against planned chapter-9 cards.
- Re-extraction notes: Fresh extraction; prior card for this slug overwritten.
