---
# === CORE IDENTIFICATION ===
concept: Preprocessor Directives in Modules
slug: preprocessor-directives

# === CLASSIFICATION ===
category: core-idioms
subcategory: module-structure
tier: foundational

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Modules"
chapter_number: null
pdf_page: null
section: "Preprocessor"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "preprocessor"
  - "Erlang preprocessor"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-module
extends: []
related:
  - file-inclusion
  - macro-definition
  - conditional-compilation
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What preprocessor features does Erlang support?"
  - "How does the Erlang preprocessor work?"
  - "What syntax does the Erlang preprocessor use?"
---

# Quick Definition
The Erlang preprocessor uses the same syntax as module attributes to support file inclusion, macros, and conditional compilation. Preprocessor directives are processed during compilation before the code is parsed.

# Core Definition
The Erlang Reference Manual states: "The same syntax as for module attributes is used by the preprocessor, which supports file inclusion, macros, and conditional compilation." The basic forms are: `-include("SomeFile.hrl").` and `-define(Macro, Replacement).` (Modules, "Preprocessor" section).

# Prerequisites
- **erlang-module** -- Preprocessor directives appear within modules using module attribute syntax

# Key Properties
1. Uses the same `-Tag(Value).` syntax as module attributes
2. Supports three categories of directives: file inclusion, macros, and conditional compilation
3. Processed at compile time, before the code is fully parsed
4. Include files conventionally use the `.hrl` extension
5. Macro definitions and uses are expanded during compilation
6. Conditional compilation allows different code paths based on defined macros

# Construction / Recognition
## To Construct/Create:
1. File inclusion: `-include("file.hrl").` or `-include_lib("app/include/file.hrl").`
2. Macro definition: `-define(MACRO, value).`
3. Conditional: `-ifdef(MACRO). ... -endif.`

## To Identify/Recognize:
1. Directives using `-include`, `-include_lib`, `-define`, `-undef`, `-ifdef`, `-ifndef`, `-if`, `-elif`, `-else`, `-endif`
2. Macro usage with `?MACRO` syntax

# Context & Application
The preprocessor is essential for sharing definitions across modules (via include files), creating reusable code patterns (via macros), and adapting code to different platforms or configurations (via conditional compilation). Record definitions, which must be identical across modules that use them, are typically placed in `.hrl` include files.

# Examples
**Example 1** (Preprocessor section):
```erlang
-include("SomeFile.hrl").
-define(Macro, Replacement).
```

# Relationships
## Builds Upon
- **erlang-module** -- Preprocessor directives use module attribute syntax

## Enables
- **file-inclusion** -- `-include` and `-include_lib` directives
- **macro-definition** -- `-define` directive
- **conditional-compilation** -- `-ifdef`, `-ifndef`, `-if`, `-elif`, `-else`, `-endif`

## Related
- **predefined-macros** -- Built-in macros like `?MODULE`, `?FILE`, `?LINE`

## Contrasts With
None.

# Common Errors
- **Error**: Confusing preprocessor directives with runtime constructs
  **Correction**: Preprocessor directives are purely compile-time; they do not exist at runtime

# Common Confusions
- **Confusion**: Thinking Erlang's preprocessor is as powerful as C's preprocessor
  **Clarification**: Erlang's preprocessor is simpler and more constrained. Macros must expand to valid Erlang syntax, and there is no macro concatenation operator like C's `##`.

# Source Reference
"Modules" chapter, "Preprocessor" section.

# Verification Notes
- Definition source: Direct quote from source
- Confidence rationale: High -- explicit description in source
- Uncertainties: None
- Cross-reference status: All slugs correspond to planned or existing cards
