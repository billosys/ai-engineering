---
# === CORE IDENTIFICATION ===
concept: Moduledoc Attribute
slug: moduledoc-attribute

# === CLASSIFICATION ===
category: documentation
subcategory: module-documentation
tier: foundational

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Documentation"
chapter_number: null
pdf_page: null
section: "Documenting a module"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "-moduledoc"
  - "module documentation attribute"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - doc-attribute
  - documentation-metadata
  - external-documentation-files
  - documentation-visibility
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I document an Erlang module?"
  - "What is the -moduledoc attribute?"
  - "Where must -moduledoc be placed in a module?"
---

# Quick Definition
The `-moduledoc` attribute documents the overall purpose of an Erlang module. It must be placed before the first `-doc` attribute or function declaration, and accepts a string (typically in Markdown format), a file reference, or `false` to hide the module.

# Core Definition
The Erlang Reference Manual states: "Documentation in Erlang is done through the `-moduledoc` and `-doc` attributes." The "-moduledoc` attribute has to be located before the first `-doc` attribute or function declaration. It documents the overall purpose of the module." (Documentation). The attribute accepts a string, a triple-quoted string (for multi-line content), `{file, "path/to/doc.md"}` for external documentation, or `false` to hide the module from documentation. The default format is Markdown, but can be changed via the `format` metadata key.

# Prerequisites
This is a foundational documentation concept with no prerequisites.

# Key Properties
1. Syntax: `-moduledoc "text".` or `-moduledoc """multi-line text""".`
2. Must appear before the first `-doc` attribute or function declaration
3. Documents the overall purpose of the module
4. Default format is Markdown (`text/markdown`)
5. Can reference external files: `-moduledoc {file, "path"}.`
6. Can hide the module: `-moduledoc false.`
7. Available since Erlang/OTP 27
8. Supports metadata via `-moduledoc #{key => value}.`

# Construction / Recognition
## To Construct:
1. Place `-moduledoc` at the top of the module, after `-module` and before any `-doc` or function
2. Provide a string describing the module's purpose
3. Start with a short paragraph, then go into greater detail
4. Optionally add metadata with a separate `-moduledoc #{...}.` attribute

## To Identify:
1. Lines beginning with `-moduledoc` in module source
2. Located near the top of the module, after the `-module` declaration

# Context & Application
The `-moduledoc` attribute is the primary mechanism for documenting Erlang modules. The documentation is compiled into EEP-48 documentation chunks in the beam file and can be retrieved using `code:get_doc/1` or viewed with the shell `h/1` command. It should start with a short paragraph describing the module, then elaborate with examples and detailed explanations.

# Examples
**Example 1** (Documentation):
```erlang
-module(arith).
-moduledoc """
A module for basic arithmetic.
""".

-export([add/2]).

-doc "Adds two numbers.".
add(One, Two) -> One + Two.
```

**Example 2** (Documenting a module -- detailed):
```erlang
-module(arith).
-moduledoc """
   A module for basic arithmetic.

   This module can be used to add and subtract values. For example:

   ```erlang
   1> arith:subtract(arith:add(2, 3), 1).
   4
   ```
   """.
```

**Example 3** (External file and metadata):
```erlang
-moduledoc {file, "../doc/arith.asciidoc"}.
-moduledoc #{since => "0.1", format => "text/asciidoc"}.
-moduledoc #{deprecated => "Use the Erlang arithmetic operators instead."}.
```

# Relationships
## Builds Upon
None -- this is a foundational documentation concept.

## Enables
- **documentation-metadata** -- Moduledoc supports metadata maps
- **external-documentation-files** -- Moduledoc can reference external files
- **documentation-visibility** -- Moduledoc can hide modules

## Related
- **doc-attribute** -- The function/type/callback counterpart

## Contrasts With
None.

# Common Errors
- **Error**: Placing `-moduledoc` after a function declaration or `-doc` attribute
  **Correction**: `-moduledoc` must appear before the first `-doc` attribute or function declaration.

# Common Confusions
- **Confusion**: Thinking `-moduledoc` and `-doc` serve the same purpose
  **Clarification**: `-moduledoc` documents the module as a whole. `-doc` documents individual functions, types, or callbacks.

# Source Reference
"Documentation" chapter, introductory section and "Documenting a module" section.

# Verification Notes
- Definition source: Direct from source text
- Confidence rationale: High -- explicit definition and examples
- Uncertainties: None
- Cross-reference status: All slugs verified
