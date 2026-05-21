---
# === CORE IDENTIFICATION ===
concept: Include Files
slug: include-files

# === CLASSIFICATION ===
category: core-idioms
subcategory: module-structure
tier: foundational

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "The Rest of Sequential Erlang"
chapter_number: 8
pdf_page: null
section: "Include Files"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "-include"
  - "-include_lib"
  - "hrl file"
  - header file

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - record
  - macro
  - erlang-preprocessor
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I include files at compile time?"
  - "What is the difference between -include and -include_lib?"
  - "Why do modules share record definitions through include files?"
---

# Quick Definition

Include files are `.hrl` files inserted at compile time with `-include` (or `-include_lib` for library headers); they usually contain record and macro definitions shared by several modules.

# Core Definition

"Files can be included with the syntax `-include(Filename).`" ("The Rest of Sequential Erlang", *Include Files*). By convention include files have the extension `.hrl`, and the `FileName` should contain an absolute or relative path so the preprocessor can locate it. Library header files are included with `-include_lib(Name).`, e.g. `-include_lib("kernel/include/file.hrl").`, in which case the Erlang compiler finds the appropriate file (the leading name, like `kernel`, refers to the application that defines the header). "Include files usually contain record definitions. If many modules need to share common record definitions, then the common record definitions are put into include files that are included by all the modules that need these definitions."

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. `-include(Filename)` inserts a file by absolute or relative path.
2. `-include_lib(Name)` inserts a library header; the compiler resolves the path.
3. Include files conventionally use the `.hrl` extension.
4. The leading component of an `-include_lib` name refers to the application defining the header.
5. Include files usually hold record definitions and macros shared across modules.

# Construction / Recognition

## To Construct/Create:
1. Put shared definitions in a `.hrl` file.
2. Include it: `-include("records.hrl").` or, for a library header, `-include_lib("kernel/include/file.hrl").`

## To Identify/Recognize:
1. An `-include` or `-include_lib` directive marks a compile-time file insertion.

# Context & Application

- **Typical contexts**: sharing record definitions and macros across multiple modules.
- **Common applications**: the `todo` record is stored in `records.hrl` and included by modules that need it.
- **Historical/stylistic notes**: file inclusion is the only way to ensure several modules use the same record definitions — analogous to C `.h` files.

# Examples

**Example 1** (*Include Files*): including a library header:

```erlang
-include_lib("kernel/include/file.hrl").
```

The compiler finds the header; `kernel` refers to the application that defines it.

# Relationships

## Builds Upon
- This is a foundational concept.

## Enables
- This concept does not have downstream cards in scope.

## Related
- **Record** — Include files exist largely to share record definitions.
- **Macro** — Macro definitions are also commonly shared via `.hrl` files.
- **Erlang preprocessor** — The preprocessor performs the file insertion.

## Contrasts With
- No directly contrasting concept in scope.

# Common Errors

- **Error**: Using `-include` for a header that lives inside an application's library path.
  **Correction**: Use `-include_lib` so the compiler resolves the path via the application name.

- **Error**: Giving `-include` a name with no usable path.
  **Correction**: The `FileName` must contain an absolute or relative path so the preprocessor can locate it.

# Common Confusions

- **Confusion**: Thinking `-include_lib` and `-include` are interchangeable.
  **Clarification**: `-include` takes a literal path; `-include_lib` resolves the path through the named application.

# Source Reference

Chapter 8: "The Rest of Sequential Erlang", section "Include Files".

# Verification Notes

- Definition source: Direct quotation and adaptation from *Include Files*.
- Confidence rationale: HIGH — the source explicitly defines both directives and their conventions.
- Uncertainties: None.
- Cross-reference status: Slug `record` extracted in this scope; `macro`, `erlang-preprocessor` extracted in this chapter.
- Re-extraction notes: Fresh extraction; no prior card existed for this slug.
