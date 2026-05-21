---
# === CORE IDENTIFICATION ===
concept: Exported Type
slug: exported-type

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
section: "Exported and Local Types"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "-export_type"
  - "type export"
  - "local type"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - type-declaration
extends: []
related:
  - type-specification
  - opaque-type
contrasts_with:
  - opaque-type

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I make a type usable from another module?"
  - "What is the difference between a local and an exported type?"
  - "What is the -export_type attribute?"
---

# Quick Definition

An exported type is a `-type` declaration made visible to other modules
via the `-export_type` attribute, so those modules can refer to it as
`module:type()`. Types not exported are local to their module.

# Core Definition

Sometimes a type definition should be local to the module where it is
defined; in other circumstances it should be exported to another module.
A type is exported with the `-export_type([Name/Arity, ...])` attribute
(chapter "Types," section "Exported and Local Types"):

```erlang
-module(a).
-type rich_text() :: [{font(), char()}].
-type font() :: integer().
-export_type([rich_text/0, font/0]).
```

A second module then refers to the type using its fully qualified name:

```erlang
-module(b).
-spec rich_text_length(a:rich_text()) -> integer().
```

`a:rich_text()` means the type `rich_text()` exported from module `a`.

# Prerequisites

- **Type declaration** — only a type created with `-type` (or `-opaque`) can be exported.

# Key Properties

1. Export syntax mirrors function export: `-export_type([Name/Arity, ...])`.
2. The arity is the number of type parameters (`rich_text/0`, `dict/2`).
3. Other modules reference the type with the qualified form `module:type()`.
4. A type not listed in `-export_type` is local to its module.
5. Both `-type` and `-opaque` types can be exported.

# Construction / Recognition

## To Construct an Exported Type:
1. Declare the type with `-type` (or `-opaque`).
2. Add `-export_type([Name/Arity]).` listing it by name and arity.
3. In the consuming module, refer to it as `definingmodule:type()`.

## To Recognize One:
1. Look for the `-export_type` attribute.
2. In other modules, a `mod:type()` qualified name signals a use of an exported type.

# Context & Application

- **Typical contexts**: Modules that produce data structures consumed by other modules.
- **Common applications**: Sharing the type of an API value across module boundaries.
- **Historical/stylistic notes**: The chapter motivates this with two cooperating modules `a` (producer) and `b` (consumer) of `rich_text`.

# Examples

**Example 1** (section "Exported and Local Types"): `-export_type([rich_text/0, font/0]).` exports two zero-parameter types.

**Example 2** (section "Exported and Local Types"): module `b` uses `a:rich_text()` as an argument type in a `-spec`.

# Relationships

## Builds Upon
- **Type declaration** — the thing being exported is a `-type`.

## Enables
- **Type specification** — specs in other modules can reference the exported type.

## Related
- **Type specification** — qualified type names appear inside `-spec`.

## Contrasts With
- **Opaque type** — both can be exported, but an opaque type also hides its internal structure from the consumer.

# Common Errors

- **Error**: Forgetting the arity in `-export_type` (`rich_text` instead of `rich_text/0`).
  **Correction**: Always write `Name/Arity`, where arity is the number of type parameters.

- **Error**: Referencing another module's type without qualifying it.
  **Correction**: Use `module:type()` when the type lives in another module.

# Common Confusions

- **Confusion**: Thinking exporting a type also makes its structure private.
  **Clarification**: A plain exported `-type` exposes its structure; use `-opaque` to hide it.

- **Confusion**: Believing all types are global.
  **Clarification**: A type is local to its module unless exported with `-export_type`.

# Source Reference

Chapter 9: "Types," section "Exported and Local Types." EPUB-origin
source; no page numbers.

# Verification Notes

- Definition source: Direct adaptation of the `-export_type` discussion and the `a`/`b` example.
- Confidence rationale: HIGH — explicit syntax and worked example in the source.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction.
