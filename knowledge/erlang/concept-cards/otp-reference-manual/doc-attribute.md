---
# === CORE IDENTIFICATION ===
concept: Doc Attribute
slug: doc-attribute

# === CLASSIFICATION ===
category: documentation
subcategory: entity-documentation
tier: foundational

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Documentation"
chapter_number: null
pdf_page: null
section: "Documenting functions, user-defined types, and callbacks"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "-doc"
  - "doc attribute"
  - "function documentation"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - moduledoc-attribute
  - documentation-metadata
  - doc-signatures
  - external-documentation-files
  - documentation-visibility
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I document a function in Erlang?"
  - "How do I document a type or callback?"
  - "What is the -doc attribute?"
  - "What entities can be documented with -doc?"
---

# Quick Definition
The `-doc` attribute documents individual functions, user-defined types (`-type`, `-opaque`), and callbacks (`-callback`). It must immediately precede the entity it documents and accepts a string, a file reference, or `false` to hide the entity.

# Core Definition
The Erlang Reference Manual states: "The `-doc` attribute always precedes the function or attribute it documents. The attributes that can be documented are user-defined types (`-type` and `-opaque`) and behaviour module attributes (`-callback`)." (Documentation). `-doc` attributes have been available since Erlang/OTP 27. The attribute accepts a string (typically Markdown), `{file, "path"}` for external files, or `false` to hide the entity. Documentation can include examples that are testable using `ct_doctest`.

# Prerequisites
This is a foundational documentation concept with no prerequisites.

# Key Properties
1. Syntax: `-doc "text".` or `-doc """multi-line text""".`
2. Must immediately precede the entity it documents
3. Can document: exported functions, `-type`, `-opaque`, and `-callback`
4. Available since Erlang/OTP 27
5. Default format is Markdown
6. Can reference external files: `-doc {file, "path"}.`
7. Can hide entities: `-doc false.`
8. Supports metadata via `-doc #{key => value}.`
9. Examples in documentation can be tested with `ct_doctest`
10. Documentation for non-exported entities is ignored and generates a warning

# Construction / Recognition
## To Construct:
1. Place `-doc` immediately before the function, type, or callback
2. Provide a string starting with a short description paragraph
3. Optionally add detailed explanation and examples
4. Optionally add metadata with a separate `-doc #{...}.` attribute

## To Identify:
1. Lines beginning with `-doc` immediately before a function, type, or callback definition
2. Can appear as `-doc "..."`, `-doc """..."""`, `-doc #{...}`, or `-doc false`

# Context & Application
The `-doc` attribute is the standard way to document functions, types, and callbacks in Erlang modules. Each entry should start with a short paragraph describing the entity's purpose, then provide detail if needed. The documentation is compiled into EEP-48 chunks and is viewable via `h/1` in the shell. Images and diagrams are not recommended for `-doc` content because it is used by IDEs and shell help.

# Examples
**Example 1** (Documenting functions, user-defined types, and callbacks):
```erlang
-doc """
A number that can be used by the arith module.

We use a special number here so that we know
that this number comes from this module.
""".
-opaque number() :: {arith, erlang:number()}.

-doc """
Adds two numbers.

### Example:

```
1> arith:add(arith:number(1), arith:number(2)). {arith, 3}
```
""".
-spec add(number(), number()) -> number().
add({arith, One}, {arith, Two}) -> {arith, One + Two}.
```

**Example 2** (Documentation -- simple):
```erlang
-doc "Adds two numbers.".
add(One, Two) -> One + Two.
```

# Relationships
## Builds Upon
None -- this is a foundational documentation concept.

## Enables
- **documentation-metadata** -- Doc supports metadata maps
- **doc-signatures** -- Doc entries have associated signatures
- **external-documentation-files** -- Doc can reference external files
- **documentation-visibility** -- Doc can hide entities

## Related
- **moduledoc-attribute** -- The module-level counterpart

## Contrasts With
None.

# Common Errors
- **Error**: Adding `-doc` to a non-exported function or type
  **Correction**: Documentation on automatically hidden entities (non-exported) is ignored and generates a warning. Use comments for non-exported entities.

- **Error**: Placing `-doc` after the entity it documents
  **Correction**: `-doc` must immediately precede the function, type, or callback it documents.

# Common Confusions
- **Confusion**: Thinking `-doc` can document any module element
  **Clarification**: `-doc` can only document exported functions, user-defined types (`-type`, `-opaque`), and callbacks (`-callback`). Other module attributes cannot be documented with `-doc`.

# Source Reference
"Documentation" chapter, "Documenting functions, user-defined types, and callbacks" section.

# Verification Notes
- Definition source: Direct from source text
- Confidence rationale: High -- explicit definition and examples
- Uncertainties: None
- Cross-reference status: All slugs verified
