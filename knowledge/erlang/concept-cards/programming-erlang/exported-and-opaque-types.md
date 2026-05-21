---
# === CORE IDENTIFICATION ===
concept: Exported and Opaque Types
slug: exported-and-opaque-types

# === CLASSIFICATION ===
category: api-design
subcategory: typespecs
tier: intermediate

# === PROVENANCE ===
source: "Programming Erlang, Second Edition"
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Types"
chapter_number: 9
pdf_page: null
section: "Exported and Local Types"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "-export_type"
  - "-opaque"
  - "opaque type"
  - "abstract data type"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - type-declaration
extends:
  - type-declaration
related:
  - type-specification
  - dialyzer
contrasts_with:
  - type-declaration

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I export a type from one module to another?"
  - "What is an opaque type in Erlang?"
  - "How do opaque types relate to information hiding?"
---

# Quick Definition

An exported type is a `-type` made visible to other modules via `-export_type`, referenced as `module:type()`. An opaque type goes further: it exports the type's *name* but hides its internal structure, so other modules cannot inspect or pattern-match its representation.

# Core Definition

A type defined in one module can be made visible to others with an `-export_type([Name/Arity, ...]).` attribute; the type is then referenced from another module by its fully qualified name, e.g. `a:rich_text()` means "the type `rich_text()` exported from module `a`" (Armstrong, "Types," "Exported and Local Types"). An *opaque* type, declared with `-opaque rich_text() :: [{font(), char()}].` instead of `-type`, exports the name but hides the internal structure: "only the module that creates the data structure knows the details of the type." Code in another module that relies on the internal shape of an opaque type commits an **abstraction violation**, which Dialyzer can detect when type visibility is correctly declared (Armstrong, "Types," "Opaque Types").

# Prerequisites

- **Type declaration** — An exported or opaque type is first a `-type` (or `-opaque`) declaration; you must know how to define named types.

# Key Properties

1. `-export_type([Name/Arity]).` makes a named type referenceable from other modules.
2. A fully qualified type name is written `module:type()`.
3. `-opaque Name() :: ...` declares a type whose name is exported but whose structure is hidden.
4. Other modules may pass opaque values around but must not pattern-match or construct their internal shape.
5. Using the internal structure of an opaque type is an *abstraction violation*.
6. Dialyzer can detect abstraction violations only if the type's visibility is correctly declared in the functions involved.

# Construction / Recognition

## To Construct/Create:
1. Define the type with `-type` (transparent) or `-opaque` (structure-hidden).
2. Add `-export_type([Name/Arity]).` to make it visible.
3. In other modules, refer to it as `module:Name()`.

## To Identify/Recognize:
1. An `-opaque` attribute marks a structure-hidden type.
2. A `module:type()` reference indicates a type imported from another module.

# Context & Application

- **Typical contexts**: Library modules that produce values consumed by client modules; modules that want to keep a data representation private.
- **Common applications**: Defining abstract data types whose representation can change without breaking clients.
- **Historical/stylistic notes**: Modules `a` and `b` cooperating on `rich_text` illustrate transparent export; making `rich_text` opaque illustrates information hiding.

# Examples

**Example 1** ("Exported and Local Types"): Module `a` declares `-type rich_text() :: [{font(), char()}].` and `-export_type([rich_text/0, font/0]).`; module `b` writes `-spec rich_text_length(a:rich_text()) -> integer().`

**Example 2** ("Opaque Types"): `-opaque rich_text() :: [{font(), char()}].` with `-export_type([rich_text/0]).` — module `b` may call `a:make_text(...)` and pass the result to `a:bounding_box(X)` without knowing `X`'s structure.

**Example 3** ("Opaque Types"): A module `c` writing `[F || {F,_} <- X]` over an opaque `rich_text` value "knows" `X` is a list of 2-tuples — an abstraction violation Dialyzer can flag.

# Relationships

## Builds Upon
- **Type declaration** — Exported/opaque types are `-type`/`-opaque` declarations made visible across modules.

## Enables
- **Type specification** — Cross-module specs reference exported types by their qualified name.

## Related
- **Dialyzer** — Detects abstraction violations of opaque types.

## Contrasts With
- **Type declaration** — A plain `-type` is module-local and transparent; an exported or opaque type changes visibility (and, for `-opaque`, hides structure).

# Common Errors

- **Error**: Pattern-matching the internal structure of another module's opaque type.
  **Correction**: Treat opaque values as black boxes; pass them only back to functions of the owning module.

- **Error**: Forgetting `-export_type` so the type cannot be named from other modules.
  **Correction**: Add `-export_type([Name/Arity]).` for any type used in cross-module specs.

# Common Confusions

- **Confusion**: Thinking `-opaque` prevents other modules from *using* the value.
  **Clarification**: Other modules can hold and pass opaque values; they just must not depend on the internal representation.

- **Confusion**: Believing exporting a function automatically exports its argument types.
  **Clarification**: Type export is separate — it requires an explicit `-export_type` attribute.

# Source Reference

Chapter 9: "Types," sections "Exported and Local Types" and "Opaque Types." EPUB source — no page numbers.

# Verification Notes

- Definition source: Direct adaptation of the `-export_type` and `-opaque` discussion and the `rich_text` example.
- Confidence rationale: HIGH — the source defines both mechanisms explicitly with examples.
- Uncertainties: None.
- Cross-reference status: Verified slugs against planned chapter-9 cards.
- Re-extraction notes: Fresh extraction; new card (no prior file).
